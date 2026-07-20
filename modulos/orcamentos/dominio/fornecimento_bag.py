"""Fotografia funcional mínima da aba 4. Forn. Bag."""

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
class LinhaMaoObraFornecimentoBag:
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
class MemorialFisicoBag:
    volume: float | None = 5000.0
    percentual_solidos_situ: float | None = 0.1
    percentual_solidos_desagua: float | None = 0.2

    def __post_init__(self):
        for campo in self.__dataclass_fields__:
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))


@dataclass(frozen=True, slots=True)
class OpcaoDimensionamentoBag:
    id: str
    descricao: str
    capacidade: float | None
    quantidade_area: float | None
    volume_total_calculado: bool
    volume_total_manual: float | None
    reinicio_celula: float | None
    volume_final_calculado: bool
    volume_final_manual: float | None
    preco_por_m3: float | None
    unidade_preco: str = "/m3"

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição"))
        object.__setattr__(self, "unidade_preco", _texto(self.unidade_preco, "unidade de preço", vazio=True))
        for campo in (
            "capacidade", "quantidade_area", "volume_total_manual", "reinicio_celula",
            "volume_final_manual", "preco_por_m3",
        ):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if not isinstance(self.volume_total_calculado, bool) or not isinstance(self.volume_final_calculado, bool):
            raise ValueError("Origens dos volumes inválidas.")
        if self.volume_total_calculado and self.volume_total_manual is not None:
            raise ValueError("Volume total deve ser manual ou calculado.")
        if self.volume_final_calculado and self.volume_final_manual is not None:
            raise ValueError("Volume final deve ser manual ou calculado.")


@dataclass(frozen=True, slots=True)
class ItemFornecimentoBag:
    id: str
    numero: int | None
    descricao: str
    unidade: str
    quantidade_manual: float | None
    quantidade_opcao_id: str | None
    quantidade_multiplica_reinicio: bool
    quantidade_arredondada: bool
    preco_unitario_manual: float | None
    preco_unitario_opcao_id: str | None
    preco_unitario_bag_6x30: bool
    preco_unitario_custo_diario: bool
    preco_total_calculado: bool
    preco_total_manual: float | None

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição"))
        object.__setattr__(self, "unidade", _texto(self.unidade, "unidade", vazio=True))
        if self.numero is not None and (
            isinstance(self.numero, bool) or not isinstance(self.numero, int) or self.numero < 1
        ):
            raise ValueError("número do item deve ser inteiro positivo ou vazio.")
        for campo in ("quantidade_manual", "preco_unitario_manual", "preco_total_manual"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if self.quantidade_opcao_id is not None:
            object.__setattr__(self, "quantidade_opcao_id", _texto(self.quantidade_opcao_id, "opção da quantidade"))
        if self.preco_unitario_opcao_id is not None:
            object.__setattr__(self, "preco_unitario_opcao_id", _texto(self.preco_unitario_opcao_id, "opção do preço"))
        flags = (
            self.quantidade_multiplica_reinicio, self.quantidade_arredondada,
            self.preco_unitario_bag_6x30, self.preco_unitario_custo_diario,
            self.preco_total_calculado,
        )
        if not all(isinstance(x, bool) for x in flags):
            raise ValueError("Origens do item inválidas.")
        if self.quantidade_manual is not None and self.quantidade_opcao_id is not None:
            raise ValueError("Quantidade deve possuir uma única origem.")
        origens_preco = (
            self.preco_unitario_manual is not None,
            self.preco_unitario_opcao_id is not None,
            self.preco_unitario_bag_6x30,
            self.preco_unitario_custo_diario,
        )
        if sum(origens_preco) > 1:
            raise ValueError("Preço unitário deve possuir uma única origem.")
        if self.preco_total_calculado and self.preco_total_manual is not None:
            raise ValueError("Preço total deve ser manual ou calculado.")


def _equipe_inicial():
    return (
        LinhaMaoObraFornecimentoBag("operador-lider", "Operador Líder", 0, 17, True, None, 110),
        LinhaMaoObraFornecimentoBag("operador-draga", "Operador de Draga", 2, 28.35, False, "operador-lider", 110),
        LinhaMaoObraFornecimentoBag("ajudante-geral", "Ajudante Geral", 5, 11.13, True, None, 110),
    )


def _opcoes_iniciais():
    def opcao(id_, descricao, capacidade, quantidade, calc_total, total, reinicio, calc_final, final, preco, unidade="/m3"):
        return OpcaoDimensionamentoBag(
            id_, descricao, capacidade, quantidade, calc_total, total, reinicio,
            calc_final, final, preco, unidade,
        )
    return (
        opcao("bag-6x50", "BAG 6 x 50", 550, 0, True, None, None, True, None, None, ""),
        opcao("bag-8x30", "Bag 8 x 30", 460, 5, False, 2300, 1, False, 2300, 75),
        opcao("bag-8x25", "Bag 8 x 25", 375, None, False, 0, None, False, 0, 52),
        opcao("bag-18x13", "Bag 18 x 13", None, None, False, 0, None, False, 0, None, ""),
        opcao("bag-6x30", "Bag 6 x 30", 340, None, False, 0, None, False, 0, None, ""),
        opcao("bag-8x10", "Bag 8 x 10", 150, None, True, None, None, True, None, 57),
        opcao("bag-8x13", "Bag 8 x 13", 190, None, True, None, None, True, None, 57),
        opcao("bag-8x14", "Bag 8 x 14", 200, None, False, 0, None, False, 0, 57),
        opcao("bag-8x15", "Bag 8 x 15", 225, 10, False, 2250, 1, False, 2250, 75),
        opcao("bag-8x20", "Bag 8 x 20", 300, None, False, 0, None, False, 0, 57),
        opcao("bag-6x15", "Bag 6 x 15", 160, None, False, 0, None, False, 0, 57),
    )


def _itens_iniciais():
    def item(numero, id_, descricao, unidade, quantidade, q_opcao, multiplica, arredonda, unitario, p_opcao, p_6x30, custo_dia, calculado, total):
        return ItemFornecimentoBag(
            id_, numero, descricao, unidade, quantidade, q_opcao, multiplica,
            arredonda, unitario, p_opcao, p_6x30, custo_dia, calculado, total,
        )
    return (
        item(1, "bag-comercial-8x10", "Bag 8 x 10m", "pç", None, "bag-8x10", False, False, None, "bag-8x10", False, False, True, None),
        item(None, "bag-comercial-8x13", "Bag 8 x 13m", "", 0, None, False, False, None, "bag-8x13", False, False, False, 0),
        item(None, "bag-comercial-8x14", "Bag 8 x 14m", "", 0, None, False, False, 11400, None, False, False, False, 0),
        item(None, "bag-comercial-8x15", "Bag 8 x 15m", "", 10, None, False, False, 16875, None, False, False, False, 168750),
        item(None, "bag-comercial-8x20", "Bag 8 x 20m", "", 0, None, False, False, 17100, None, False, False, False, 0),
        item(None, "bag-comercial-6x15", "Bag 6 x 15m", "", 0, None, False, False, 9120, None, False, False, False, 0),
        item(2, "bag-comercial-8x30", "Bag 8,00 x 30m", "pç", None, "bag-8x30", True, True, None, "bag-8x30", False, False, False, 172500),
        item(3, "bag-comercial-8x25", "Bag 8,00 x 25,00m", "pc", None, "bag-8x25", True, False, None, "bag-8x25", False, False, False, 0),
        item(4, "bag-comercial-6x30", "Bag 6,00 x 30,00m", "pç", None, None, False, False, None, None, True, False, False, 0),
        item(5, "frete", "Frete para os Bags", "un", 1, None, False, False, 5000, None, False, False, False, 5000),
        item(6, "munck", "Munck para descarregamento", "dia", 1, None, False, False, 2000, None, False, False, False, 2000),
        item(7, "mao-obra-instalacao", "Mão de obra para instalação", "dia", 3, None, False, False, None, None, False, True, False, 7210.245),
    )


@dataclass(frozen=True, slots=True)
class FornecimentoBag:
    equipe: tuple[LinhaMaoObraFornecimentoBag, ...] = _equipe_inicial()
    custo_refeicao: float | None = 30.0
    custo_transporte: float | None = 10.0
    memorial_fisico: MemorialFisicoBag = MemorialFisicoBag()
    opcoes: tuple[OpcaoDimensionamentoBag, ...] = _opcoes_iniciais()
    fator_preco_bag_6x30: float | None = None
    itens: tuple[ItemFornecimentoBag, ...] = _itens_iniciais()
    bdi: float | None = 0.0

    def __post_init__(self):
        for campo in ("custo_refeicao", "custo_transporte", "fator_preco_bag_6x30", "bdi"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if not isinstance(self.equipe, tuple) or not all(isinstance(x, LinhaMaoObraFornecimentoBag) for x in self.equipe):
            raise ValueError("Equipe do fornecimento de bags inválida.")
        if not isinstance(self.memorial_fisico, MemorialFisicoBag):
            raise ValueError("Memorial físico dos bags inválido.")
        if not isinstance(self.opcoes, tuple) or not all(isinstance(x, OpcaoDimensionamentoBag) for x in self.opcoes):
            raise ValueError("Opções de dimensionamento dos bags inválidas.")
        if not isinstance(self.itens, tuple) or not all(isinstance(x, ItemFornecimentoBag) for x in self.itens):
            raise ValueError("Itens do fornecimento de bags inválidos.")
        ids = [x.id for x in self.equipe] + [x.id for x in self.opcoes] + [x.id for x in self.itens]
        if len(ids) != len(set(ids)):
            raise ValueError("Identificadores do fornecimento de bags devem ser únicos.")


@dataclass(frozen=True, slots=True)
class ResultadoLinhaFornecimentoBag:
    id: str
    horas_dia: float | None
    total: float


@dataclass(frozen=True, slots=True)
class ResultadoMemorialFisicoBag:
    tonelada_seca: float
    volume_material_bags: float | None


@dataclass(frozen=True, slots=True)
class ResultadoOpcaoDimensionamentoBag:
    id: str
    volume_total: float
    volume_final: float


@dataclass(frozen=True, slots=True)
class ResultadoItemFornecimentoBag:
    id: str
    quantidade: float | None
    preco_unitario: float | None
    preco_total: float | None


@dataclass(frozen=True, slots=True)
class ResultadosFornecimentoBag:
    mao_obra: tuple[ResultadoLinhaFornecimentoBag, ...]
    quantidade_pessoas: float
    total_refeicoes: float
    total_transportes: float
    custo_por_dia: float
    memorial_fisico: ResultadoMemorialFisicoBag
    opcoes: tuple[ResultadoOpcaoDimensionamentoBag, ...]
    total_quantidade_area: float
    total_volume: float
    total_volume_final: float
    itens: tuple[ResultadoItemFornecimentoBag, ...]
    total: float
    valor_bdi: float
    preco_final: float


def calcular_fornecimento_bag(
    fornecimento: FornecimentoBag, horas_dados_obra: float | None
) -> ResultadosFornecimentoBag:
    """Reproduz somente as 35 fórmulas efetivamente presentes na aba oficial."""
    zero = lambda valor: 0.0 if valor is None else valor
    horas_por_id = {}
    mao_obra = []
    for linha in fornecimento.equipe:
        horas = horas_dados_obra if linha.horas_dados_obra else horas_por_id.get(linha.horas_referencia_id)
        horas_por_id[linha.id] = horas
        total = zero(linha.quantidade) * zero(linha.custo_hora) * zero(horas)
        total *= 1 + zero(linha.encargos_sociais) / 100
        mao_obra.append(ResultadoLinhaFornecimentoBag(linha.id, horas, total))
    pessoas = sum(zero(x.quantidade) for x in fornecimento.equipe)
    refeicoes = pessoas * zero(fornecimento.custo_refeicao)
    transportes = pessoas * zero(fornecimento.custo_transporte)
    custo_dia = sum(x.total for x in mao_obra) + refeicoes + transportes

    m = fornecimento.memorial_fisico
    tonelada_seca = zero(m.volume) * zero(m.percentual_solidos_situ)
    volume_material = None
    if m.percentual_solidos_desagua not in (None, 0):
        volume_material = tonelada_seca / m.percentual_solidos_desagua
    memorial = ResultadoMemorialFisicoBag(tonelada_seca, volume_material)

    opcoes = []
    opcoes_entrada = {x.id: x for x in fornecimento.opcoes}
    for opcao in fornecimento.opcoes:
        volume_total = opcao.volume_total_manual
        if opcao.volume_total_calculado:
            volume_total = zero(opcao.capacidade) * zero(opcao.quantidade_area)
        volume_final = opcao.volume_final_manual
        if opcao.volume_final_calculado:
            volume_final = zero(opcao.reinicio_celula) * zero(volume_total)
        opcoes.append(ResultadoOpcaoDimensionamentoBag(opcao.id, zero(volume_total), zero(volume_final)))
    opcoes_resultado = {x.id: x for x in opcoes}

    itens = []
    for item in fornecimento.itens:
        quantidade = item.quantidade_manual
        if item.quantidade_opcao_id is not None:
            opcao = opcoes_entrada[item.quantidade_opcao_id]
            quantidade = zero(opcao.quantidade_area)
            if item.quantidade_multiplica_reinicio:
                quantidade *= zero(opcao.reinicio_celula)
            if item.quantidade_arredondada:
                quantidade = math.ceil(quantidade)
        unitario = item.preco_unitario_manual
        if item.preco_unitario_opcao_id is not None:
            opcao = opcoes_entrada[item.preco_unitario_opcao_id]
            unitario = zero(opcao.preco_por_m3) * zero(opcao.capacidade)
        elif item.preco_unitario_bag_6x30:
            unitario = zero(opcoes_entrada["bag-6x30"].capacidade) * zero(fornecimento.fator_preco_bag_6x30) * 1.1
        elif item.preco_unitario_custo_diario:
            unitario = custo_dia
        total_item = item.preco_total_manual
        if item.preco_total_calculado:
            total_item = zero(quantidade) * zero(unitario)
        itens.append(ResultadoItemFornecimentoBag(item.id, quantidade, unitario, total_item))

    total = sum(zero(x.preco_total) for x in itens)
    valor_bdi = total * zero(fornecimento.bdi) / 100
    return ResultadosFornecimentoBag(
        tuple(mao_obra), pessoas, refeicoes, transportes, custo_dia, memorial,
        tuple(opcoes), sum(zero(x.quantidade_area) for x in fornecimento.opcoes),
        sum(x.volume_total for x in opcoes), sum(x.volume_final for x in opcoes),
        tuple(itens), total, valor_bdi, total + valor_bdi,
    )
