"""Equivalência funcional mínima da aba 10. Plan. Preços."""

from dataclasses import dataclass
import math


WORKSHEET_ORIGEM_PLANILHA_PRECOS = "10. Plan. Preços"
INDICE_WORKSHEET_PLANILHA_PRECOS = 15


def _numero(valor, campo):
    if valor is not None and (
        isinstance(valor, bool)
        or not isinstance(valor, (int, float))
        or not math.isfinite(valor)
        or valor < 0
    ):
        raise ValueError(f"{campo} deve ser numérico não negativo ou vazio.")
    return float(valor) if valor is not None else None


@dataclass(frozen=True, slots=True)
class EntradaLinhaPlanilhaPrecos:
    id: str
    quantidade_manual: float | None
    bdi: float | None

    def __post_init__(self):
        if not isinstance(self.id, str) or not self.id.strip():
            raise ValueError("Identificador da linha deve ser informado.")
        object.__setattr__(self, "id", self.id.strip())
        object.__setattr__(
            self,
            "quantidade_manual",
            _numero(self.quantidade_manual, "quantidade"),
        )
        object.__setattr__(self, "bdi", _numero(self.bdi, "BDI"))


def _entradas_iniciais():
    return (
        EntradaLinhaPlanilhaPrecos("mobilizacao-draga", 1, 60),
        EntradaLinhaPlanilhaPrecos("mobilizacao-polimero", 1, 60),
        EntradaLinhaPlanilhaPrecos("preparo-celula", None, 60),
        EntradaLinhaPlanilhaPrecos("fornecimento-bags", None, 45),
        EntradaLinhaPlanilhaPrecos("dragagem-operacao", None, 60),
        EntradaLinhaPlanilhaPrecos("medicao", 1, 60),
        EntradaLinhaPlanilhaPrecos("desmobilizacao-draga", 1, 60),
        EntradaLinhaPlanilhaPrecos("desmobilizacao-polimero", 1, 60),
    )


@dataclass(frozen=True, slots=True)
class PlanilhaPrecos:
    linhas: tuple[EntradaLinhaPlanilhaPrecos, ...] = _entradas_iniciais()

    def __post_init__(self):
        if not isinstance(self.linhas, tuple) or not all(
            isinstance(item, EntradaLinhaPlanilhaPrecos) for item in self.linhas
        ):
            raise ValueError("Entradas da Planilha de Preços inválidas.")
        ids = [item.id for item in self.linhas]
        if len(ids) != len(set(ids)):
            raise ValueError("Identificadores da Planilha de Preços devem ser únicos.")
        if tuple(ids) != tuple(item[0] for item in LINHAS_PLANILHA_PRECOS):
            raise ValueError("Estrutura da Planilha de Preços inválida.")


@dataclass(frozen=True, slots=True)
class ReferenciasPlanilhaPrecos:
    mobilizacao_draga_f27: float | None
    mobilizacao_polimero_f27: float | None
    preparacao_celula_f29: float | None
    preparacao_celula_n7: float | None
    fornecimento_bag_f29: float | None
    fornecimento_bag_d15_d23: float | None
    dragagem_d248: float | None
    fornecimento_bag_b33: float | None
    medicao_f20: float | None
    desmobilizacao_draga_f21: float | None
    desmobilizacao_polimero_f26: float | None

    def __post_init__(self):
        for campo in self.__dataclass_fields__:
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))


@dataclass(frozen=True, slots=True)
class ResultadoLinhaPlanilhaPrecos:
    id: str
    numero: int
    descricao: str
    unidade: str
    custo_total: float | None
    quantidade: float | None
    bdi: float | None
    custo_unitario: float | None
    preco_unitario: float | None
    preco_total: float


@dataclass(frozen=True, slots=True)
class ResultadosPlanilhaPrecos:
    linhas: tuple[ResultadoLinhaPlanilhaPrecos, ...]
    custo_total: float
    preco_venda: float
    valor_auxiliar_j18: float | None


LINHAS_PLANILHA_PRECOS = (
    (
        "mobilizacao-draga",
        1,
        "Mobilizaçao e Montagem da Draga",
        "un ",
        "mobilizacao_draga_f27",
        None,
    ),
    (
        "mobilizacao-polimero",
        2,
        "Mobilizaçao e Montagem Equipto Polímero e Barrilete",
        "un ",
        "mobilizacao_polimero_f27",
        None,
    ),
    (
        "preparo-celula",
        3,
        "Preparo de Célula",
        "m²",
        "preparacao_celula_f29",
        "preparacao_celula_n7",
    ),
    (
        "fornecimento-bags",
        4,
        "Fornecimento de Bags",
        "un ",
        "fornecimento_bag_f29",
        "fornecimento_bag_d15_d23",
    ),
    (
        "dragagem-operacao",
        6,
        "Dragagem e Operaçao do Sistema de Polimero (incluindo fornecimento do polimero)",
        "m3",
        "dragagem_d248",
        "fornecimento_bag_b33",
    ),
    (
        "medicao",
        7,
        "Medição",
        "un ",
        "medicao_f20",
        None,
    ),
    (
        "desmobilizacao-draga",
        9,
        "Desmobilização Draga",
        "un ",
        "desmobilizacao_draga_f21",
        None,
    ),
    (
        "desmobilizacao-polimero",
        10,
        "Desmobilização do Equipamento Polímero",
        "un ",
        "desmobilizacao_polimero_f26",
        None,
    ),
)


FORMULAS_PLANILHA_PRECOS = (
    ("C4", "='1. Mob. Draga'!F27"),
    ("G4", "=C4/E4"),
    ("I4", "=((H4/100)+1)*G4"),
    ("J4", "=E4*I4"),
    ("C5", "='2. Mob. Eq. Polimero'!F27"),
    ("G5", "=C5/E5"),
    ("I5", "=((H5/100)+1)*G5"),
    ("J5", "=E5*I5"),
    ("C6", "='3. Prep. Célula'!F29"),
    ("E6", "='3. Prep. Célula'!N7"),
    ("G6", "=C6/E6"),
    ("I6", "=((H6/100)+1)*G6"),
    ("J6", "=E6*I6"),
    ("C7", "='4. Forn. Bag'!F29"),
    ("E7", "=SUM('4. Forn. Bag'!D15:D23)"),
    ("G7", "=C7/E7"),
    ("I7", "=((H7/100)+1)*G7"),
    ("J7", "=E7*I7"),
    ("C8", "='6. Dragagem'!D248"),
    ("E8", "='4. Forn. Bag'!B33"),
    ("G8", "=C8/E8"),
    ("I8", "=((H8/100)+1)*G8"),
    ("J8", "=E8*I8"),
    ("C9", "='7. Medição'!F20"),
    ("G9", "=C9/E9"),
    ("I9", "=((H9/100)+1)*G9"),
    ("J9", "=E9*I9"),
    ("C10", "='8. Desmob. Draga'!F21"),
    ("G10", "=C10/E10"),
    ("I10", "=((H10/100)+1)*G10"),
    ("J10", "=E10*I10"),
    ("C11", "='9. Desmob. Eq. Polimero '!F26"),
    ("G11", "=C11/E11"),
    ("I11", "=((H11/100)+1)*G11"),
    ("J11", "=E11*I11"),
    ("C12", "=SUM(C5:C11)"),
    ("J12", "=SUM(J4:J11)"),
    ("J18", "=(SUM(J6:J9))/E8"),
)


def calcular_planilha_precos(
    planilha: PlanilhaPrecos,
    referencias: ReferenciasPlanilhaPrecos,
) -> ResultadosPlanilhaPrecos:
    """Reproduz as 38 fórmulas reais, incluindo as nove compartilhadas."""

    entradas = {item.id: item for item in planilha.linhas}
    resultados = []
    for id_, numero, descricao, unidade, custo_ref, quantidade_ref in LINHAS_PLANILHA_PRECOS:
        entrada = entradas[id_]
        custo_total = getattr(referencias, custo_ref)
        quantidade = (
            getattr(referencias, quantidade_ref)
            if quantidade_ref is not None
            else entrada.quantidade_manual
        )
        custo_unitario = (
            None
            if quantidade in (None, 0)
            else (0.0 if custo_total is None else custo_total) / quantidade
        )
        preco_unitario = (
            None
            if custo_unitario is None
            else (1 + (0.0 if entrada.bdi is None else entrada.bdi) / 100)
            * custo_unitario
        )
        preco_total = (
            0.0
            if quantidade is None or preco_unitario is None
            else quantidade * preco_unitario
        )
        resultados.append(
            ResultadoLinhaPlanilhaPrecos(
                id_,
                numero,
                descricao,
                unidade,
                custo_total,
                quantidade,
                entrada.bdi,
                custo_unitario,
                preco_unitario,
                preco_total,
            )
        )

    # C12 exclui deliberadamente C4, exatamente como =SUM(C5:C11).
    custo_total = sum(
        0.0 if item.custo_total is None else item.custo_total
        for item in resultados[1:]
    )
    preco_venda = sum(item.preco_total for item in resultados)
    quantidade_dragagem = resultados[4].quantidade
    auxiliar = None
    if quantidade_dragagem not in (None, 0):
        auxiliar = sum(item.preco_total for item in resultados[2:6]) / quantidade_dragagem
    return ResultadosPlanilhaPrecos(
        tuple(resultados), custo_total, preco_venda, auxiliar
    )
