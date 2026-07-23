"""Equivalência funcional mínima da aba 9. Desmob. Eq. Polimero."""

from dataclasses import dataclass
import math


def _texto(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} deve ser texto não vazio.")
    return valor.strip()


def _numero(valor, campo):
    if valor is not None and (
        isinstance(valor, bool) or not isinstance(valor, (int, float))
        or not math.isfinite(valor) or valor < 0
    ):
        raise ValueError(f"{campo} deve ser numérico não negativo ou vazio.")
    return float(valor) if valor is not None else None


@dataclass(frozen=True, slots=True)
class LinhaMaoObraDesmobilizacaoPolimero:
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
class ItemDesmobilizacaoEquipamentoPolimero:
    id: str
    numero: int
    descricao: str
    unidade: str
    quantidade: float | None
    preco_unitario_manual: float | None
    preco_unitario_barrilete: bool
    preco_unitario_custo_diario: bool

    def __post_init__(self):
        for campo in ("id", "descricao", "unidade"):
            object.__setattr__(self, campo, _texto(getattr(self, campo), campo))
        if (
            isinstance(self.numero, bool) or not isinstance(self.numero, int)
            or self.numero < 0
        ):
            raise ValueError("Número do item deve ser inteiro não negativo.")
        object.__setattr__(self, "quantidade", _numero(self.quantidade, "quantidade"))
        object.__setattr__(
            self, "preco_unitario_manual",
            _numero(self.preco_unitario_manual, "preço unitário"),
        )
        if not isinstance(self.preco_unitario_barrilete, bool) or not isinstance(
            self.preco_unitario_custo_diario, bool
        ):
            raise ValueError("Origem do preço unitário inválida.")
        origens = sum((
            self.preco_unitario_manual is not None,
            self.preco_unitario_barrilete,
            self.preco_unitario_custo_diario,
        ))
        if origens > 1:
            raise ValueError("Preço unitário deve possuir no máximo uma origem.")


def _equipe_inicial():
    return (
        LinhaMaoObraDesmobilizacaoPolimero(
            "operador-tecnico",
            "Operador de Draga + técnico operação polím.",
            2, 15.15, 110,
        ),
        LinhaMaoObraDesmobilizacaoPolimero(
            "ajudante-geral", "Ajudante Geral", 5, 11.13, 110,
        ),
    )


def _itens_iniciais():
    def manual(id_, numero, descricao, unidade, quantidade, preco):
        return ItemDesmobilizacaoEquipamentoPolimero(
            id_, numero, descricao, unidade, quantidade, preco, False, False
        )

    return (
        manual(
            "cobertura-equipamento", 1, "Verba para Cobertura do equipamento",
            "vb", None, None,
        ),
        manual("brita-piso", 2, "Brita 1 para lastro no piso", "m³", None, None),
        manual("concreto-piso", 3, "Concreto para piso ", "m³", None, None),
        manual(
            "frete-equipamento", 4, "Frete para mobilização do equipamento",
            "vb", 2, 1500,
        ),
        manual("instalacoes-hidraulicas", 5, "Instalações hidráulicas", "vb", None, 1000),
        manual("instalacoes-eletricas", 6, "Instalações elétricas", "vb", None, 1000),
        manual("maquina-wap", 7, "Máquina Wap", "vb", None, 4500),
        ItemDesmobilizacaoEquipamentoPolimero(
            "barrilete", 8, "Barrilete", "vb", None, None, True, False
        ),
        ItemDesmobilizacaoEquipamentoPolimero(
            "mao-obra-apoio", 9, "Mão de obra de apoio na montagem",
            "dia", 2, None, False, True,
        ),
    )


@dataclass(frozen=True, slots=True)
class DesmobilizacaoEquipamentoPolimero:
    equipe: tuple[LinhaMaoObraDesmobilizacaoPolimero, ...] = _equipe_inicial()
    custo_refeicao: float | None = 30.0
    custo_transporte: float | None = 10.0
    itens: tuple[ItemDesmobilizacaoEquipamentoPolimero, ...] = _itens_iniciais()
    bdi: float | None = 0.0

    def __post_init__(self):
        object.__setattr__(self, "custo_refeicao", _numero(self.custo_refeicao, "refeição"))
        object.__setattr__(
            self, "custo_transporte", _numero(self.custo_transporte, "transporte")
        )
        object.__setattr__(self, "bdi", _numero(self.bdi, "BDI"))
        if not isinstance(self.equipe, tuple) or not all(
            isinstance(x, LinhaMaoObraDesmobilizacaoPolimero) for x in self.equipe
        ):
            raise ValueError("Equipe da desmobilização do equipamento de polímero inválida.")
        if not isinstance(self.itens, tuple) or not all(
            isinstance(x, ItemDesmobilizacaoEquipamentoPolimero) for x in self.itens
        ):
            raise ValueError("Itens da desmobilização do equipamento de polímero inválidos.")
        ids = [x.id for x in self.equipe] + [x.id for x in self.itens]
        if len(ids) != len(set(ids)):
            raise ValueError("Identificadores da desmobilização devem ser únicos.")


@dataclass(frozen=True, slots=True)
class ResultadoMaoObraDesmobilizacaoPolimero:
    id: str
    horas_dia: float | None
    total: float


@dataclass(frozen=True, slots=True)
class ResultadoItemDesmobilizacaoPolimero:
    id: str
    preco_unitario: float | None
    preco_total: float


@dataclass(frozen=True, slots=True)
class ResultadosDesmobilizacaoEquipamentoPolimero:
    mao_obra: tuple[ResultadoMaoObraDesmobilizacaoPolimero, ...]
    quantidade_pessoas: float
    total_refeicoes: float
    total_transportes: float
    custo_por_dia: float
    itens: tuple[ResultadoItemDesmobilizacaoPolimero, ...]
    total_composicao: float
    valor_bdi: float
    preco_final: float


FORMULAS_DESMOBILIZACAO_EQUIPAMENTO_POLIMERO = (
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
    ("F16", "=D16*E16"),
    ("F17", "=D17*E17"),
    ("F18", "=D18*E18"),
    ("F19", "=D19*E19"),
    ("F20", "=D20*E20"),
    ("E21", "=Barrilete!F31"),
    ("F21", "=D21*E21"),
    ("E22", "=F9"),
    ("F22", "=D22*E22"),
    ("F24", "=SUM(F14:F22)"),
    ("F25", "=F24*(E25/100)"),
    ("F26", "=SUM(F24:F25)"),
)


def calcular_desmobilizacao_equipamento_polimero(
    desmobilizacao: DesmobilizacaoEquipamentoPolimero,
    horas_dados_obra: float | None,
    preco_barrilete: float | None,
) -> ResultadosDesmobilizacaoEquipamentoPolimero:
    """Reproduz as 23 fórmulas reais da aba 9. Desmob. Eq. Polimero."""
    horas = _numero(horas_dados_obra, "horas de Dados Obra")
    barrilete = _numero(preco_barrilete, "preço do Barrilete")
    zero = lambda valor: 0.0 if valor is None else valor

    mao_obra = tuple(
        ResultadoMaoObraDesmobilizacaoPolimero(
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
        unitario = item.preco_unitario_manual
        if item.preco_unitario_barrilete:
            unitario = barrilete
        elif item.preco_unitario_custo_diario:
            unitario = custo_por_dia
        itens.append(ResultadoItemDesmobilizacaoPolimero(
            item.id, unitario, zero(item.quantidade) * zero(unitario)
        ))
    total = sum(x.preco_total for x in itens)
    valor_bdi = total * zero(desmobilizacao.bdi) / 100
    return ResultadosDesmobilizacaoEquipamentoPolimero(
        mao_obra, pessoas, refeicoes, transportes, custo_por_dia,
        tuple(itens), total, valor_bdi, total + valor_bdi,
    )
