"""Fotografia funcional mínima da aba 3. Prep. Célula."""

from dataclasses import dataclass
import math


def _numero(valor, campo):
    if valor is not None and (
        isinstance(valor, bool) or not isinstance(valor, (int, float))
        or not math.isfinite(valor) or valor < 0
    ):
        raise ValueError(f"{campo} deve ser numérico não negativo ou vazio.")
    return float(valor) if valor is not None else None


def _texto(valor, campo, *, vazio=False):
    if not isinstance(valor, str) or (not vazio and not valor.strip()):
        raise ValueError(f"{campo} deve ser texto{' ou vazio' if vazio else ' não vazio'}.")
    return valor.strip()


@dataclass(frozen=True, slots=True)
class LinhaMaoObraPreparacaoCelula:
    id: str
    descricao: str
    quantidade: float | None
    custo_hora: float | None
    horas_dados_obra: bool
    horas_referencia_id: str | None
    encargos_sociais: float | None

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição"))
        for campo in ("quantidade", "custo_hora", "encargos_sociais"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if not isinstance(self.horas_dados_obra, bool):
            raise ValueError("Origem das horas inválida.")
        if self.horas_referencia_id is not None:
            object.__setattr__(self, "horas_referencia_id", _texto(self.horas_referencia_id, "referência de horas"))
        if self.horas_dados_obra == (self.horas_referencia_id is not None):
            raise ValueError("Horas devem possuir uma única origem.")


@dataclass(frozen=True, slots=True)
class ComposicaoRealPreparacaoCelula:
    fator_pead: float | None = 1.196
    fator_bidim: float | None = 1.48
    fator_brita: float | None = 0.15
    fator_retro: float | None = 0.023
    fator_mao_obra: float | None = 0.023
    parcela_pead_1: float | None = 260.0
    parcela_pead_2: float | None = 524.0
    parcela_pead_3: float | None = 491.0
    parcela_pead_4: float | None = 512.0
    area_celula_pead: float | None = 2500.0
    parcela_brita: float | None = 722.0

    def __post_init__(self):
        for campo in self.__dataclass_fields__:
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))


@dataclass(frozen=True, slots=True)
class ItemPreparacaoCelula:
    id: str
    numero: int
    descricao: str
    unidade: str
    quantidade_manual: float | None
    quantidade_pead: bool
    quantidade_referencia_pead: bool
    quantidade_bidim: bool
    quantidade_brita: bool
    preco_unitario_manual: float | None
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
        for campo in ("quantidade_manual", "preco_unitario_manual", "preco_total_manual"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        quantidades = (
            self.quantidade_pead, self.quantidade_referencia_pead,
            self.quantidade_bidim, self.quantidade_brita,
        )
        flags = (*quantidades, self.preco_unitario_custo_diario, self.preco_total_calculado)
        if not all(isinstance(valor, bool) for valor in flags):
            raise ValueError("Origens do item inválidas.")
        if sum((self.quantidade_manual is not None, *quantidades)) > 1:
            raise ValueError("Quantidade deve possuir uma única origem.")
        if self.preco_unitario_manual is not None and self.preco_unitario_custo_diario:
            raise ValueError("Preço unitário deve possuir uma única origem.")
        if self.preco_total_calculado and self.preco_total_manual is not None:
            raise ValueError("Preço total deve ser manual ou calculado, nunca ambos.")


def _equipe_inicial():
    return (
        LinhaMaoObraPreparacaoCelula("operador-lider", "Operador Líder", 0, 14.5, True, None, 110),
        LinhaMaoObraPreparacaoCelula("operador-draga", "Operador de Draga", 2, 28.35, False, "operador-lider", 110),
        LinhaMaoObraPreparacaoCelula("ajudante-geral", "Ajudante Geral", 2, 11.13, True, None, 110),
    )


def _itens_iniciais():
    def item(numero, id_, descricao, unidade, quantidade, unitario, total, observacao="", **flags):
        return ItemPreparacaoCelula(
            id_, numero, descricao, unidade, quantidade,
            flags.get("pead", False), flags.get("ref_pead", False),
            flags.get("bidim", False), flags.get("brita", False), unitario,
            flags.get("custo_diario", False), flags.get("calculado", False),
            total, observacao,
        )
    return (
        item(1, "preparo-terreno", "Preparo Terreno - Patrola / tratos de esteira", "dia", None, 2500, None, calculado=True),
        item(2, "mobilizacao-patrola", "Mobilização dao Patrola", "dia", None, 2500, 0),
        item(3, "aluguel-retro", "Preparo Terreno - Aluguel de Retro", "dia", 2, 1500, 3000),
        item(4, "mobilizacao-retro", "Mobilização/desmobilização de Retro", "dia", 2, 1000, 2000),
        item(5, "regularizacao-manual", "Regularização manual - Mão de obra", "dia", 5, None, 8261.72, custo_diario=True),
        item(6, "pead", "PEAD", "m²", None, 22, 65780, "19,08 Preço Curitina", pead=True),
        item(7, "mao-obra-pead", "Mão de obra instal. PEAD", "m²", None, 4, None, "B&B", ref_pead=True, calculado=True),
        item(8, "taxa-mobilizacao-pead", "taxa Mobilizaçao PEAD Mao de obras", "vb", 1, 5000, None, "B&B", calculado=True),
        item(9, "bidim", "Bidim RT 14 (4,90 x 100m)", "m²", None, 6, 22279.92, "3,50 Preço Curitiba", bidim=True),
        item(10, "brita", "Brita 2", "m³", None, 100, 43280.25, "SABESP", brita=True),
        item(11, "retro-brita", "Retro escavadeira para espalhamento Brita", "dia", 5, 1500, 7500),
        item(12, "mao-obra-bidim-brita", "Mão de obra de instal. Bidim e Brita", "dia", 5, None, 8261.72, custo_diario=True),
    )


@dataclass(frozen=True, slots=True)
class PreparacaoCelula:
    equipe: tuple[LinhaMaoObraPreparacaoCelula, ...] = _equipe_inicial()
    custo_refeicao: float | None = 30.0
    custo_transporte: float | None = 10.0
    composicao_real: ComposicaoRealPreparacaoCelula = ComposicaoRealPreparacaoCelula()
    itens: tuple[ItemPreparacaoCelula, ...] = _itens_iniciais()
    quantidade_repeticoes: float | None = 1.0

    def __post_init__(self):
        for campo in ("custo_refeicao", "custo_transporte", "quantidade_repeticoes"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if not isinstance(self.equipe, tuple) or not all(isinstance(x, LinhaMaoObraPreparacaoCelula) for x in self.equipe):
            raise ValueError("Equipe da preparação da célula inválida.")
        if not isinstance(self.composicao_real, ComposicaoRealPreparacaoCelula):
            raise ValueError("Composição real da preparação da célula inválida.")
        if not isinstance(self.itens, tuple) or not all(isinstance(x, ItemPreparacaoCelula) for x in self.itens):
            raise ValueError("Itens da preparação da célula inválidos.")
        ids = [x.id for x in self.equipe] + [x.id for x in self.itens]
        if len(ids) != len(set(ids)):
            raise ValueError("Identificadores da preparação da célula devem ser únicos.")


@dataclass(frozen=True, slots=True)
class ResultadoLinhaPreparacaoCelula:
    id: str
    horas_dia: float | None
    total: float


@dataclass(frozen=True, slots=True)
class ResultadoComposicaoRealPreparacaoCelula:
    soma_pead: float
    area_total: float
    quantidade_pead: float
    quantidade_bidim: float
    quantidade_brita_base: float
    horas_retro: float
    horas_mao_obra: float
    dias_mao_obra: float


@dataclass(frozen=True, slots=True)
class ResultadoItemPreparacaoCelula:
    id: str
    quantidade: float | None
    preco_unitario: float | None
    preco_total: float | None


@dataclass(frozen=True, slots=True)
class ResultadosPreparacaoCelula:
    mao_obra: tuple[ResultadoLinhaPreparacaoCelula, ...]
    quantidade_pessoas: float
    total_refeicoes: float
    total_transportes: float
    custo_por_dia: float
    composicao_real: ResultadoComposicaoRealPreparacaoCelula
    itens: tuple[ResultadoItemPreparacaoCelula, ...]
    total: float
    total_repeticoes: float
    preco_final: float


def calcular_preparacao_celula(
    preparacao: PreparacaoCelula, horas_dados_obra: float | None
) -> ResultadosPreparacaoCelula:
    """Reproduz somente as 36 fórmulas efetivamente presentes na aba oficial."""
    zero = lambda valor: 0.0 if valor is None else valor
    horas_por_id = {}
    mao_obra = []
    for linha in preparacao.equipe:
        horas = horas_dados_obra if linha.horas_dados_obra else horas_por_id.get(linha.horas_referencia_id)
        horas_por_id[linha.id] = horas
        total = zero(linha.quantidade) * zero(linha.custo_hora) * zero(horas)
        total *= 1 + zero(linha.encargos_sociais) / 100
        mao_obra.append(ResultadoLinhaPreparacaoCelula(linha.id, horas, total))
    pessoas = sum(zero(x.quantidade) for x in preparacao.equipe)
    refeicoes = pessoas * zero(preparacao.custo_refeicao)
    transportes = pessoas * zero(preparacao.custo_transporte)
    custo_dia = sum(x.total for x in mao_obra) + refeicoes + transportes

    c = preparacao.composicao_real
    soma_pead = sum(zero(x) for x in (c.parcela_pead_1, c.parcela_pead_2, c.parcela_pead_3, c.parcela_pead_4))
    area_total = soma_pead + zero(c.parcela_brita)
    quantidade_pead = zero(c.fator_pead) * zero(c.area_celula_pead)
    quantidade_bidim = zero(c.fator_bidim) * area_total
    quantidade_brita_base = zero(c.fator_brita) * area_total
    horas_retro = zero(c.fator_retro) * area_total
    horas_mao_obra = zero(c.fator_mao_obra) * area_total
    dias_mao_obra = horas_mao_obra / 10
    composicao = ResultadoComposicaoRealPreparacaoCelula(
        soma_pead, area_total, quantidade_pead, quantidade_bidim,
        quantidade_brita_base, horas_retro, horas_mao_obra, dias_mao_obra,
    )

    itens = []
    for item in preparacao.itens:
        quantidade = item.quantidade_manual
        if item.quantidade_pead:
            quantidade = quantidade_pead
        elif item.quantidade_referencia_pead:
            quantidade = quantidade_pead
        elif item.quantidade_bidim:
            quantidade = quantidade_bidim
        elif item.quantidade_brita:
            quantidade = quantidade_brita_base * 1.15
        unitario = custo_dia if item.preco_unitario_custo_diario else item.preco_unitario_manual
        total_item = item.preco_total_manual
        if item.preco_total_calculado:
            total_item = zero(quantidade) * zero(unitario)
        itens.append(ResultadoItemPreparacaoCelula(item.id, quantidade, unitario, total_item))
    total = sum(zero(x.preco_total) for x in itens)
    total_repeticoes = total * zero(preparacao.quantidade_repeticoes)
    return ResultadosPreparacaoCelula(
        tuple(mao_obra), pessoas, refeicoes, transportes, custo_dia,
        composicao, tuple(itens), total, total_repeticoes, total_repeticoes,
    )
