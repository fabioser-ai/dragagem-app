"""Fotografia funcional mínima da aba 2. Mob. Eq. Polimero."""

from dataclasses import dataclass
import math


def _numero(valor, campo):
    if valor is not None and (
        isinstance(valor, bool)
        or not isinstance(valor, (int, float))
        or not math.isfinite(valor)
        or valor < 0
    ):
        raise ValueError(f"{campo} deve ser numérico não negativo ou vazio.")
    return float(valor) if valor is not None else None


def _texto(valor, campo, *, vazio=False):
    if not isinstance(valor, str) or (not vazio and not valor.strip()):
        raise ValueError(f"{campo} deve ser texto{' ou vazio' if vazio else ' não vazio'}.")
    return valor.strip()


@dataclass(frozen=True, slots=True)
class LinhaMaoObraPolimero:
    id: str
    descricao: str
    quantidade: float | None
    custo_hora: float | None
    encargos_sociais: float | None

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição"))
        for campo in ("quantidade", "custo_hora", "encargos_sociais"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))


@dataclass(frozen=True, slots=True)
class ItemMobilizacaoEquipamentoPolimero:
    id: str
    numero: int
    descricao: str
    unidade: str
    quantidade: float | None
    preco_unitario_manual: float | None
    preco_unitario_barrilete: bool
    preco_unitario_custo_diario: bool
    preco_total_calculado: bool
    preco_total_manual: float | None
    observacao: str = ""

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição"))
        object.__setattr__(self, "unidade", _texto(self.unidade, "unidade"))
        object.__setattr__(self, "observacao", _texto(self.observacao, "observação", vazio=True))
        if isinstance(self.numero, bool) or not isinstance(self.numero, int) or self.numero < 1:
            raise ValueError("número do item deve ser inteiro positivo.")
        for campo in ("quantidade", "preco_unitario_manual", "preco_total_manual"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        origens = (
            self.preco_unitario_manual is not None,
            self.preco_unitario_barrilete,
            self.preco_unitario_custo_diario,
        )
        if not all(isinstance(valor, bool) for valor in (
            self.preco_unitario_barrilete,
            self.preco_unitario_custo_diario,
            self.preco_total_calculado,
        )):
            raise ValueError("Origens de preço inválidas.")
        if sum(origens) > 1:
            raise ValueError("Preço unitário deve possuir uma única origem.")
        if self.preco_total_calculado and self.preco_total_manual is not None:
            raise ValueError("Preço total deve ser manual ou calculado, nunca ambos.")


def _equipe_inicial():
    return (
        LinhaMaoObraPolimero("operador-polimero", "Operador de Polimero", 2, 28.35, 110),
        LinhaMaoObraPolimero("ajudante-geral", "Ajudante Geral", 2, 11.13, 110),
    )


def _itens_iniciais():
    def manual(numero, id_, descricao, unidade, quantidade, unitario, total, observacao=""):
        return ItemMobilizacaoEquipamentoPolimero(
            id_, numero, descricao, unidade, quantidade, unitario,
            False, False, False, total, observacao,
        )

    return (
        ItemMobilizacaoEquipamentoPolimero(
            "cobertura-equipamento", 1, "Verba para Cobertura do equipamento", "vb",
            1, 15000, False, False, True, None, "",
        ),
        manual(2, "munck-cobertura", "Munck para montagem cobertura", "vb", 1, 2000, 2000, "Muncar"),
        manual(2, "brita-piso", "Brita 1 para lastro no piso", "m³", 3, 80, 240),
        manual(3, "concreto-piso", "Concreto para piso", "m³", 5, 400, 2000),
        manual(4, "frete-equipamento", "Frete para mobilização do equipamento", "vb", 1, 1500, 1500, "Fabiano"),
        manual(5, "instalacoes-hidraulicas", "Instalações hidráulicas", "vb", 1, 1500, 1500),
        manual(6, "instalacoes-eletricas", "Instalações elétricas", "vb", 1, 1500, 1500),
        manual(7, "maquina-wap", "Máquina Wap", "vb", 0.5, 4000, 2000),
        ItemMobilizacaoEquipamentoPolimero(
            "barrilete", 8, "Barrilete", "vb", 1, None,
            True, False, False, 5923.36, "",
        ),
        ItemMobilizacaoEquipamentoPolimero(
            "mao-obra-apoio", 9, "Mão de obra de apoio na montagem", "dia", 5, None,
            False, True, False, 8261.72, "",
        ),
    )


@dataclass(frozen=True, slots=True)
class MobilizacaoEquipamentoPolimero:
    equipe: tuple[LinhaMaoObraPolimero, ...] = _equipe_inicial()
    custo_refeicao: float | None = 30.0
    custo_transporte: float | None = 10.0
    itens: tuple[ItemMobilizacaoEquipamentoPolimero, ...] = _itens_iniciais()
    bdi: float | None = 0.0

    def __post_init__(self):
        for campo in ("custo_refeicao", "custo_transporte", "bdi"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if not isinstance(self.equipe, tuple) or not all(
            isinstance(item, LinhaMaoObraPolimero) for item in self.equipe
        ):
            raise ValueError("Equipe da mobilização do equipamento de polímero inválida.")
        if not isinstance(self.itens, tuple) or not all(
            isinstance(item, ItemMobilizacaoEquipamentoPolimero) for item in self.itens
        ):
            raise ValueError("Itens da mobilização do equipamento de polímero inválidos.")
        ids = [item.id for item in self.equipe] + [item.id for item in self.itens]
        if len(ids) != len(set(ids)):
            raise ValueError("Identificadores da mobilização devem ser únicos.")


@dataclass(frozen=True, slots=True)
class ResultadoLinhaMaoObraPolimero:
    id: str
    horas_dia: float | None
    total: float


@dataclass(frozen=True, slots=True)
class ResultadoItemPolimero:
    id: str
    preco_unitario: float | None
    preco_total: float | None


@dataclass(frozen=True, slots=True)
class ResultadosMobilizacaoEquipamentoPolimero:
    mao_obra: tuple[ResultadoLinhaMaoObraPolimero, ...]
    quantidade_apoio: float
    total_refeicoes: float
    total_transportes: float
    custo_por_dia: float
    itens: tuple[ResultadoItemPolimero, ...]
    total_composicao: float
    valor_bdi: float
    preco_final: float


def calcular_mobilizacao_equipamento_polimero(
    mobilizacao: MobilizacaoEquipamentoPolimero,
    horas_por_dia: float | None,
    preco_barrilete: float | None,
) -> ResultadosMobilizacaoEquipamentoPolimero:
    """Reproduz somente as 15 fórmulas efetivamente presentes na aba oficial."""

    def zero(valor):
        return 0.0 if valor is None else valor

    horas = zero(horas_por_dia)
    mao_obra = []
    for linha in mobilizacao.equipe:
        total = zero(linha.quantidade) * zero(linha.custo_hora) * horas
        total *= 1 + zero(linha.encargos_sociais) / 100
        mao_obra.append(ResultadoLinhaMaoObraPolimero(linha.id, horas_por_dia, total))

    quantidade_apoio = sum(zero(linha.quantidade) for linha in mobilizacao.equipe)
    total_refeicoes = quantidade_apoio * zero(mobilizacao.custo_refeicao)
    total_transportes = quantidade_apoio * zero(mobilizacao.custo_transporte)
    custo_por_dia = sum(item.total for item in mao_obra) + total_refeicoes + total_transportes

    itens = []
    for item in mobilizacao.itens:
        unitario = item.preco_unitario_manual
        if item.preco_unitario_barrilete:
            unitario = preco_barrilete
        elif item.preco_unitario_custo_diario:
            unitario = custo_por_dia
        total = item.preco_total_manual
        if item.preco_total_calculado:
            total = zero(item.quantidade) * zero(unitario)
        itens.append(ResultadoItemPolimero(item.id, unitario, total))

    total_composicao = sum(zero(item.preco_total) for item in itens)
    valor_bdi = total_composicao * zero(mobilizacao.bdi) / 100
    return ResultadosMobilizacaoEquipamentoPolimero(
        tuple(mao_obra), quantidade_apoio, total_refeicoes, total_transportes,
        custo_por_dia, tuple(itens), total_composicao, valor_bdi,
        total_composicao + valor_bdi,
    )
