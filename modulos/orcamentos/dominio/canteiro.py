"""Fotografia funcional mínima da aba Canteiro."""

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
class LinhaMaoObraCanteiro:
    id: str
    descricao: str
    quantidade: float | None
    custo_hora: float | None
    horas_dia: float | None
    encargos_sociais: float | None

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição", vazio=True))
        for campo in ("quantidade", "custo_hora", "horas_dia", "encargos_sociais"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))


@dataclass(frozen=True, slots=True)
class ItemCanteiro:
    id: str
    numero: int
    descricao: str
    unidade: str
    quantidade_manual: float | None
    quantidade_prazo: bool
    quantidade_quatro_prazos: bool
    quantidade_pessoas: bool
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
        flags = (
            self.quantidade_prazo, self.quantidade_quatro_prazos,
            self.quantidade_pessoas, self.preco_unitario_custo_diario,
            self.preco_total_calculado,
        )
        if not all(isinstance(valor, bool) for valor in flags):
            raise ValueError("Origens do item inválidas.")
        if sum((self.quantidade_manual is not None, *flags[:3])) > 1:
            raise ValueError("Quantidade deve possuir uma única origem.")
        if self.preco_unitario_manual is not None and self.preco_unitario_custo_diario:
            raise ValueError("Preço unitário deve possuir uma única origem.")
        if self.preco_total_calculado and self.preco_total_manual is not None:
            raise ValueError("Preço total deve ser manual ou calculado, nunca ambos.")


def _equipe_inicial():
    return (
        LinhaMaoObraCanteiro("linha-vazia", "", None, 30, 9, 110),
        LinhaMaoObraCanteiro("operador-draga", "Operador de Draga", 2, 28.35, 9, 110),
        LinhaMaoObraCanteiro("ajudante-geral", "Ajudante Geral", 2, 11.13, 9, 110),
    )


def _itens_iniciais():
    def item(numero, id_, descricao, unidade, quantidade, unitario, total, observacao="", **flags):
        return ItemCanteiro(
            id_, numero, descricao, unidade, quantidade,
            flags.get("prazo", False), flags.get("quatro_prazos", False),
            flags.get("pessoas", False), unitario,
            flags.get("custo_diario", False), flags.get("calculado", False),
            total, observacao,
        )
    return (
        item(1, "container-almoxarifado", "Container almoxarifado", "mês", None, 1000, None, "Consorcio", prazo=True, calculado=True),
        item(2, "container-sanitario", "Container Sanitário/Vestiário", "mês", None, None, 0),
        item(3, "container-escritorio", "Container Escritório", "mês", None, None, 0),
        item(4, "frete-containers", "Frete para Containers", "vb", None, 500, 0),
        item(5, "ppra-pcmso-ltcat", "PPRA + PCMSO + LTCAT", "vb", 1, 1500, 1500),
        item(6, "arts", "ART Principal + ARTS co-resp.", "vb", 1, 800, 800),
        item(7, "placa-obra", "Placa de obra", "vb", None, None, 0),
        item(8, "vigilancia", "Vigilância", "mês", None, None, 0, "Consorcio"),
        item(9, "agua-potavel", "água potável", "gl", None, 20, 240, "Consorcio", quatro_prazos=True),
        item(10, "material-escritorio", "material de escritório", "mês", None, 300, 900, "Consorcio", prazo=True),
        item(11, "banheiro-quimico", "Banheiro Quimico", "mes", None, 2000, 6000, "Consorcio", prazo=True),
        item(12, "exames-medicos", "custo Exames médicos", "un", None, 440, 1760, pessoas=True),
        item(13, "mao-obra-integracao", "Mão de obra (integração)", "dia", 3, None, 4957.032, custo_diario=True),
    )


@dataclass(frozen=True, slots=True)
class Canteiro:
    equipe: tuple[LinhaMaoObraCanteiro, ...] = _equipe_inicial()
    custo_refeicao: float | None = 30.0
    custo_transporte: float | None = 10.0
    itens: tuple[ItemCanteiro, ...] = _itens_iniciais()
    bdi: float | None = 1.0

    def __post_init__(self):
        for campo in ("custo_refeicao", "custo_transporte", "bdi"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if not isinstance(self.equipe, tuple) or not all(isinstance(x, LinhaMaoObraCanteiro) for x in self.equipe):
            raise ValueError("Equipe do Canteiro inválida.")
        if not isinstance(self.itens, tuple) or not all(isinstance(x, ItemCanteiro) for x in self.itens):
            raise ValueError("Itens do Canteiro inválidos.")
        ids = [x.id for x in self.equipe] + [x.id for x in self.itens]
        if len(ids) != len(set(ids)):
            raise ValueError("Identificadores do Canteiro devem ser únicos.")


@dataclass(frozen=True, slots=True)
class ResultadoLinhaCanteiro:
    id: str
    total: float


@dataclass(frozen=True, slots=True)
class ResultadoItemCanteiro:
    id: str
    quantidade: float | None
    preco_unitario: float | None
    preco_total: float | None


@dataclass(frozen=True, slots=True)
class ResultadosCanteiro:
    mao_obra: tuple[ResultadoLinhaCanteiro, ...]
    quantidade_pessoas: float
    total_refeicoes: float
    total_transportes: float
    custo_por_dia: float
    prazo_arredondado: int | None
    itens: tuple[ResultadoItemCanteiro, ...]
    total_composicao: float
    prazo_operacao: float | None
    preco_unitario: float | None
    valor_bdi: float
    preco_final: float


def calcular_canteiro(canteiro: Canteiro, prazo_producao: float | None) -> ResultadosCanteiro:
    """Reproduz somente as 20 fórmulas efetivamente presentes na aba oficial."""
    zero = lambda valor: 0.0 if valor is None else valor
    mao_obra = tuple(
        ResultadoLinhaCanteiro(
            linha.id,
            zero(linha.quantidade) * zero(linha.custo_hora) * zero(linha.horas_dia)
            * (1 + zero(linha.encargos_sociais) / 100),
        )
        for linha in canteiro.equipe
    )
    pessoas = sum(zero(linha.quantidade) for linha in canteiro.equipe)
    refeicoes = pessoas * zero(canteiro.custo_refeicao)
    transportes = pessoas * zero(canteiro.custo_transporte)
    custo_dia = sum(x.total for x in mao_obra) + refeicoes + transportes
    prazo = math.ceil(prazo_producao) if prazo_producao is not None else None
    resultados = []
    for item in canteiro.itens:
        quantidade = item.quantidade_manual
        if item.quantidade_prazo:
            quantidade = prazo
        elif item.quantidade_quatro_prazos:
            quantidade = None if prazo is None else 4 * prazo
        elif item.quantidade_pessoas:
            quantidade = pessoas
        unitario = custo_dia if item.preco_unitario_custo_diario else item.preco_unitario_manual
        total = item.preco_total_manual
        if item.preco_total_calculado:
            total = zero(quantidade) * zero(unitario)
        resultados.append(ResultadoItemCanteiro(item.id, quantidade, unitario, total))
    total_composicao = sum(zero(x.preco_total) for x in resultados)
    prazo_operacao = None if prazo is None else prazo - 1
    preco_unitario = None
    if prazo_operacao not in (None, 0):
        preco_unitario = total_composicao / prazo_operacao
    valor_bdi = zero(preco_unitario) * zero(canteiro.bdi) / 100
    return ResultadosCanteiro(
        mao_obra, pessoas, refeicoes, transportes, custo_dia, prazo,
        tuple(resultados), total_composicao, prazo_operacao, preco_unitario,
        valor_bdi, zero(preco_unitario) + valor_bdi,
    )
