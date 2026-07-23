"""Equivalência funcional mínima da aba 8. Desmob. Draga."""

from dataclasses import dataclass
import math


def _texto(valor, campo, *, vazio=False):
    if not isinstance(valor, str) or (not vazio and not valor.strip()):
        raise ValueError(f"{campo} deve ser texto{' ou vazio' if vazio else ' não vazio'}.")
    return valor.strip()


def _numero(valor, campo):
    if valor is not None and (
        isinstance(valor, bool) or not isinstance(valor, (int, float))
        or not math.isfinite(valor) or valor < 0
    ):
        raise ValueError(f"{campo} deve ser numérico não negativo ou vazio.")
    return float(valor) if valor is not None else None


@dataclass(frozen=True, slots=True)
class LinhaMaoObraDesmobilizacao:
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
class ItemDesmobilizacaoDraga:
    id: str
    numero: int | None
    descricao: str
    unidade: str
    quantidade: float | None
    preco_unitario_manual: float | None
    preco_unitario_custo_diario: bool
    observacao: str = ""

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição"))
        object.__setattr__(self, "unidade", _texto(self.unidade, "unidade"))
        object.__setattr__(self, "observacao", _texto(self.observacao, "observação", vazio=True))
        if self.numero is not None and (
            isinstance(self.numero, bool) or not isinstance(self.numero, int) or self.numero < 0
        ):
            raise ValueError("Número do item deve ser inteiro não negativo ou vazio.")
        object.__setattr__(self, "quantidade", _numero(self.quantidade, "quantidade"))
        object.__setattr__(
            self, "preco_unitario_manual",
            _numero(self.preco_unitario_manual, "preço unitário"),
        )
        if not isinstance(self.preco_unitario_custo_diario, bool):
            raise ValueError("Origem do preço unitário inválida.")
        if self.preco_unitario_custo_diario and self.preco_unitario_manual is not None:
            raise ValueError("Preço unitário deve ser manual ou vir do custo diário.")


def _equipe_inicial():
    return (
        LinhaMaoObraDesmobilizacao(
            "operador-tecnico", "Operador de Draga + técnico operação polím.",
            2, 28.35, 110,
        ),
        LinhaMaoObraDesmobilizacao(
            "ajudante-geral", "Ajudante Geral", 5, 11.13, 110,
        ),
    )


def _itens_iniciais():
    return (
        ItemDesmobilizacaoDraga(
            "cobertura-equipamento", 1, "Verba para Cobertura do equipamento",
            "vb", None, None, False,
        ),
        ItemDesmobilizacaoDraga(
            "frete-equipamento", 2, "Frete para mobilização do equipamento",
            "vb", 2, 1300, False, "Fabiano 23/03/2026",
        ),
        ItemDesmobilizacaoDraga(
            "mao-obra-desmontagem", 3, "Mão de obra de apoio na desmontagem",
            "dia", 3, None, True,
        ),
        ItemDesmobilizacaoDraga(
            "guindaste-desmontagem", 5,
            "Guindaste p/ carregamento e desmontagem DRAGA",
            "dia", 1, 3500, False,
        ),
        ItemDesmobilizacaoDraga(
            "frete-repetido", None, "Frete para mobilização do equipamento",
            "dia", 2, 2000, False,
        ),
    )


@dataclass(frozen=True, slots=True)
class DesmobilizacaoDraga:
    equipe: tuple[LinhaMaoObraDesmobilizacao, ...] = _equipe_inicial()
    custo_refeicao: float | None = 30.0
    custo_transporte: float | None = 10.0
    itens: tuple[ItemDesmobilizacaoDraga, ...] = _itens_iniciais()
    bdi: float | None = 0.0

    def __post_init__(self):
        object.__setattr__(self, "custo_refeicao", _numero(self.custo_refeicao, "refeição"))
        object.__setattr__(
            self, "custo_transporte", _numero(self.custo_transporte, "transporte")
        )
        object.__setattr__(self, "bdi", _numero(self.bdi, "BDI"))
        if not isinstance(self.equipe, tuple) or not all(
            isinstance(x, LinhaMaoObraDesmobilizacao) for x in self.equipe
        ):
            raise ValueError("Equipe da desmobilização inválida.")
        if not isinstance(self.itens, tuple) or not all(
            isinstance(x, ItemDesmobilizacaoDraga) for x in self.itens
        ):
            raise ValueError("Itens da desmobilização inválidos.")
        ids = [x.id for x in self.equipe] + [x.id for x in self.itens]
        if len(ids) != len(set(ids)):
            raise ValueError("Identificadores da desmobilização devem ser únicos.")


@dataclass(frozen=True, slots=True)
class ResultadoMaoObraDesmobilizacao:
    id: str
    horas_dia: float | None
    total: float


@dataclass(frozen=True, slots=True)
class ResultadoItemDesmobilizacao:
    id: str
    preco_unitario: float | None
    preco_total: float


@dataclass(frozen=True, slots=True)
class ResultadosDesmobilizacaoDraga:
    mao_obra: tuple[ResultadoMaoObraDesmobilizacao, ...]
    quantidade_pessoas: float
    total_refeicoes: float
    total_transportes: float
    custo_por_dia: float
    itens: tuple[ResultadoItemDesmobilizacao, ...]
    total_composicao: float
    valor_bdi: float
    preco_final: float


FORMULAS_DESMOBILIZACAO_DRAGA = (
    ("D5", "='Dados Obra '!B26"),
    ("F5", "=(A5*C5*D5)+(A5*C5*D5)*(E5/100)"),
    ("D6", "='Dados Obra '!B26"),
    ("F6", "=(A6*C6*D6)+(A6*C6*D6)*(E6/100)"),
    ("A7", "=A5+A6"),
    ("F7", "=A7*C7"),
    ("A8", "=A5+A6"),
    ("F8", "=A8*C8"),
    ("F9", "=SUM(F5:F8)"),
    ("F14", "=D14*E14"),
    ("F15", "=D15*E15"),
    ("E16", "=F9"),
    ("F16", "=D16*E16"),
    ("F17", "=D17*E17"),
    ("F18", "=D18*E18"),
    ("F19", "=SUM(F14:F18)"),
    ("F20", "=F19*(E20/100)"),
    ("F21", "=SUM(F19:F20)"),
)


def calcular_desmobilizacao_draga(
    desmobilizacao: DesmobilizacaoDraga,
    horas_dados_obra: float | None,
) -> ResultadosDesmobilizacaoDraga:
    """Reproduz somente as 18 fórmulas reais de 8. Desmob. Draga."""
    horas = _numero(horas_dados_obra, "horas de Dados Obra")
    zero = lambda valor: 0.0 if valor is None else valor

    mao_obra = tuple(
        ResultadoMaoObraDesmobilizacao(
            linha.id,
            horas,
            zero(linha.quantidade) * zero(linha.custo_hora) * zero(horas)
            * (1 + zero(linha.encargos_sociais) / 100),
        )
        for linha in desmobilizacao.equipe
    )
    pessoas = sum(zero(x.quantidade) for x in desmobilizacao.equipe)
    refeicoes = pessoas * zero(desmobilizacao.custo_refeicao)
    transportes = pessoas * zero(desmobilizacao.custo_transporte)
    custo_por_dia = sum(x.total for x in mao_obra) + refeicoes + transportes

    itens = []
    for item in desmobilizacao.itens:
        unitario = custo_por_dia if item.preco_unitario_custo_diario else item.preco_unitario_manual
        itens.append(ResultadoItemDesmobilizacao(
            item.id, unitario, zero(item.quantidade) * zero(unitario)
        ))
    total = sum(x.preco_total for x in itens)
    valor_bdi = total * zero(desmobilizacao.bdi) / 100
    return ResultadosDesmobilizacaoDraga(
        mao_obra, pessoas, refeicoes, transportes, custo_por_dia,
        tuple(itens), total, valor_bdi, total + valor_bdi,
    )
