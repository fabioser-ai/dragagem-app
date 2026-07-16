"""Fotografia mínima e relações confirmadas na aba Barrilete do Excel oficial."""

from dataclasses import dataclass


def _numero_nao_negativo(valor, campo, *, vazio=True):
    if valor is None and vazio:
        return None
    if isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor < 0:
        sufixo = " ou vazio" if vazio else ""
        raise ValueError(f"{campo} deve ser numérico não negativo{sufixo}.")
    return float(valor)


def _texto(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} deve ser texto não vazio.")
    return valor.strip()


@dataclass(frozen=True, slots=True)
class ItemBarrilete:
    """Linha genérica do bloco de materiais/serviços da composição."""

    id: str
    descricao: str
    unidade: str
    quantidade: float | None
    preco_base: float | None
    multiplicador_preco: float | None
    preco_unitario_manual: float | None
    preco_total_informado: float | None

    def __post_init__(self):
        for campo in ("id", "descricao", "unidade"):
            object.__setattr__(self, campo, _texto(getattr(self, campo), campo))
        for campo in (
            "quantidade",
            "preco_base",
            "multiplicador_preco",
            "preco_unitario_manual",
            "preco_total_informado",
        ):
            object.__setattr__(
                self, campo, _numero_nao_negativo(getattr(self, campo), campo)
            )
        formula = self.preco_base is not None or self.multiplicador_preco is not None
        if formula and (
            self.preco_base is None
            or self.multiplicador_preco is None
            or self.preco_unitario_manual is not None
        ):
            raise ValueError("Preço unitário deve ser manual ou base multiplicada, nunca ambos.")

    @property
    def preco_unitario(self):
        if self.preco_base is None:
            return self.preco_unitario_manual
        return self.preco_base * self.multiplicador_preco


def _itens_iniciais():
    def formula(id_, descricao, unidade, quantidade, base, total):
        return ItemBarrilete(id_, descricao, unidade, quantidade, base, 1.4, None, total)

    def manual(id_, descricao, unidade, quantidade, unitario, total):
        return ItemBarrilete(id_, descricao, unidade, quantidade, None, None, unitario, total)

    return (
        formula("tubo-ferro-8", 'Tubo de ferro c/6m diametro de 8"', "pç", 6, 400, 3360),
        formula("toco-050", "Toco 0,50m", "pç", 8, 165, 1848),
        formula("joelho-90", "Joelho 90°", "pç", 8, 165, 1848),
        formula("tee-6x4", 'Tee 6" x 4" flangeado', "pç", 6, 220, 1848),
        formula("ponteira-4", 'Ponteira flange x escama diam. 4"', "pç", 6, 55, 462),
        formula("cap-6", 'Cap. 6"', "pç", 1, 35, 49),
        formula("valvula-gaveta-4", 'Válvula Gaveta 4"', "pç", 1, 2000, 2800),
        formula("valvula-gaveta-3", 'Válvula Gaveta 3"', "pç", 4, 1100, 6160),
        manual("mangueira-conduto", "Mangueira Conduto d’água", "m", 200, 30, 6000),
        formula("bracadeiras", "Braçadeiras", "pç", 24, 14, 470.4),
        formula("curva-pvc-4", 'Curva longa de PVC 4"', "pç", 4, 35, 196),
        formula("valvula-esfera-2", 'Válvula esfera 2"', "pç", 2, 60, 168),
        manual("bomba-lameira", "Bomba lameira", "pç", 1, 3000, 3000),
    )


@dataclass(frozen=True, slots=True)
class Barrilete:
    quantidade_operadores: float | None = 2.0
    custo_hora_operador: float | None = 23.0
    encargos_operador: float | None = 110.0
    quantidade_ajudantes: float | None = 2.0
    custo_hora_ajudante: float | None = 10.0
    encargos_ajudante: float | None = 110.0
    custo_refeicao: float | None = 30.0
    custo_transporte: float | None = 10.0
    itens: tuple[ItemBarrilete, ...] = _itens_iniciais()
    bdi: float | None = None

    def __post_init__(self):
        for campo in (
            "quantidade_operadores",
            "custo_hora_operador",
            "encargos_operador",
            "quantidade_ajudantes",
            "custo_hora_ajudante",
            "encargos_ajudante",
            "custo_refeicao",
            "custo_transporte",
            "bdi",
        ):
            object.__setattr__(
                self, campo, _numero_nao_negativo(getattr(self, campo), campo)
            )
        if not isinstance(self.itens, tuple) or not all(
            isinstance(item, ItemBarrilete) for item in self.itens
        ):
            raise ValueError("Itens do Barrilete inválidos.")
        ids = [item.id for item in self.itens]
        if len(ids) != len(set(ids)):
            raise ValueError("Identificadores dos itens do Barrilete devem ser únicos.")


@dataclass(frozen=True, slots=True)
class ResultadosBarrilete:
    total_operadores: float
    total_ajudantes: float
    quantidade_apoio: float
    total_refeicoes: float
    total_transporte: float
    custo_por_dia: float
    preco_mao_obra_montagem: float
    total_composicao: float
    depreciacao: float
    valor_bdi: float
    preco_final: float


def calcular_barrilete(
    barrilete: Barrilete, horas_por_dia: float | None
) -> ResultadosBarrilete:
    """Reproduz somente as fórmulas existentes nas células F5:F9 e E/F27:F31."""

    def zero(valor):
        return 0.0 if valor is None else valor

    horas = zero(horas_por_dia)
    qtd_operadores = zero(barrilete.quantidade_operadores)
    qtd_ajudantes = zero(barrilete.quantidade_ajudantes)
    total_operadores = (
        qtd_operadores * zero(barrilete.custo_hora_operador) * horas
    ) * (1 + zero(barrilete.encargos_operador) / 100)
    total_ajudantes = (
        qtd_ajudantes * zero(barrilete.custo_hora_ajudante) * horas
    ) * (1 + zero(barrilete.encargos_ajudante) / 100)
    quantidade_apoio = qtd_operadores + qtd_ajudantes
    total_refeicoes = quantidade_apoio * zero(barrilete.custo_refeicao)
    total_transporte = quantidade_apoio * zero(barrilete.custo_transporte)
    custo_por_dia = total_operadores + total_ajudantes + total_refeicoes + total_transporte

    # No Excel, F14:F26 são valores informados, não fórmulas. E27 referencia F9 e
    # F27 preserva o total informado da linha. Essa distinção é intencional.
    totais_informados = sum(zero(item.preco_total_informado) for item in barrilete.itens)
    preco_mao_obra_montagem = custo_por_dia
    total_composicao = totais_informados + preco_mao_obra_montagem
    depreciacao = total_composicao * 0.2
    valor_bdi = depreciacao * (zero(barrilete.bdi) / 100)
    return ResultadosBarrilete(
        total_operadores,
        total_ajudantes,
        quantidade_apoio,
        total_refeicoes,
        total_transporte,
        custo_por_dia,
        preco_mao_obra_montagem,
        total_composicao,
        depreciacao,
        valor_bdi,
        depreciacao + valor_bdi,
    )
