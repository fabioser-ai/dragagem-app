"""Equivalência funcional mínima da worksheet Planilha1."""

from dataclasses import dataclass
import math

from modulos.orcamentos.dominio.planilha_precos import ResultadosPlanilhaPrecos


WORKSHEET_ORIGEM_PLANILHA1 = "Planilha1"
INDICE_WORKSHEET_PLANILHA1 = 16
DIMENSAO_WORKSHEET_PLANILHA1 = "A2:F7"


def _quantidade(valor):
    if (
        isinstance(valor, bool)
        or not isinstance(valor, (int, float))
        or not math.isfinite(valor)
        or valor < 0
    ):
        raise ValueError("Quantidade deve ser numérica não negativa.")
    return float(valor)


@dataclass(frozen=True, slots=True)
class EntradaLinhaPlanilha1:
    id: str
    quantidade: float

    def __post_init__(self):
        if not isinstance(self.id, str) or not self.id.strip():
            raise ValueError("Identificador da linha deve ser informado.")
        object.__setattr__(self, "id", self.id.strip())
        object.__setattr__(self, "quantidade", _quantidade(self.quantidade))


def _entradas_iniciais():
    return (
        EntradaLinhaPlanilha1("mobilizacao", 1),
        EntradaLinhaPlanilha1("preparo-celula", 2496),
        EntradaLinhaPlanilha1("dragagem-desaguamento", 5000),
        EntradaLinhaPlanilha1("desmobilizacao", 1),
    )


@dataclass(frozen=True, slots=True)
class Planilha1:
    linhas: tuple[EntradaLinhaPlanilha1, ...] = _entradas_iniciais()

    def __post_init__(self):
        if not isinstance(self.linhas, tuple) or not all(
            isinstance(item, EntradaLinhaPlanilha1) for item in self.linhas
        ):
            raise ValueError("Entradas da Planilha1 inválidas.")
        if tuple(item.id for item in self.linhas) != tuple(
            item[0] for item in LINHAS_PLANILHA1
        ):
            raise ValueError("Estrutura da Planilha1 inválida.")


@dataclass(frozen=True, slots=True)
class ResultadoLinhaPlanilha1:
    id: str
    numero: int
    descricao: str
    unidade: str
    quantidade: float
    preco_unitario: float | None
    preco_total: float


@dataclass(frozen=True, slots=True)
class ResultadosPlanilha1:
    linhas: tuple[ResultadoLinhaPlanilha1, ...]
    total_geral: float


LINHAS_PLANILHA1 = (
    ("mobilizacao", 1, "Mobilização e Montagem dos Equipamentos", "vb"),
    (
        "preparo-celula",
        2,
        "Preparo de Célula de Desaguamento dos Bags, incluindo "
        "impermeabilização com manta PEAD, bidim e Camada drenante",
        "m2",
    ),
    (
        "dragagem-desaguamento",
        3,
        "Dragagem e desaguamento de sedimentos através do processo de "
        "acondicionamento em Geobags de alta resistência, incluindo "
        "fornecimento e operação dos Geobags",
        "m3",
    ),
    ("desmobilizacao", 4, "Desmobilização dos Equipamentos ", "vb"),
)


FORMULAS_PLANILHA1 = (
    ("E3", "=SUM('10. Plan. Preços'!J4:J5)"),
    ("F3", "=D3*E3"),
    ("E4", "=F4/D4"),
    ("F4", "=SUM('10. Plan. Preços'!J6)"),
    ("E5", "=F5/D5"),
    ("F5", "=SUM('10. Plan. Preços'!J7:J9)"),
    ("E6", "=F6"),
    ("F6", "=SUM('10. Plan. Preços'!J10:J11)"),
    ("F7", "=SUM(F3:F6)"),
)


def calcular_planilha1(
    planilha: Planilha1,
    planilha_precos: ResultadosPlanilhaPrecos,
) -> ResultadosPlanilha1:
    """Reproduz as nove fórmulas reais da worksheet."""

    entradas = {item.id: item for item in planilha.linhas}
    referencias = (
        planilha_precos.linhas[0].preco_total
        + planilha_precos.linhas[1].preco_total,
        planilha_precos.linhas[2].preco_total,
        sum(item.preco_total for item in planilha_precos.linhas[3:6]),
        planilha_precos.linhas[6].preco_total
        + planilha_precos.linhas[7].preco_total,
    )
    resultados = []
    for indice, (id_, numero, descricao, unidade) in enumerate(LINHAS_PLANILHA1):
        quantidade = entradas[id_].quantidade
        referencia = referencias[indice]
        if indice == 0:
            preco_unitario = referencia
            preco_total = quantidade * preco_unitario
        elif indice == 3:
            preco_total = referencia
            preco_unitario = preco_total
        else:
            preco_total = referencia
            preco_unitario = None if quantidade == 0 else preco_total / quantidade
        resultados.append(
            ResultadoLinhaPlanilha1(
                id_,
                numero,
                descricao,
                unidade,
                quantidade,
                preco_unitario,
                preco_total,
            )
        )
    return ResultadosPlanilha1(
        tuple(resultados),
        sum(item.preco_total for item in resultados),
    )
