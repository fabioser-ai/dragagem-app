"""Equivalência funcional mínima da aba 8. Carga e Transporte."""

from dataclasses import dataclass
import math


WORKSHEET_ORIGEM_CARGA_TRANSPORTE = "8. Carga e Transporte"
INDICE_WORKSHEET_CARGA_TRANSPORTE = 12


def _numero(valor, campo):
    if valor is not None and (
        isinstance(valor, bool)
        or not isinstance(valor, (int, float))
        or not math.isfinite(valor)
        or valor < 0
    ):
        raise ValueError(f"{campo} deve ser numérico não negativo ou vazio.")
    return float(valor) if valor is not None else None


def _texto(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} deve ser texto não vazio.")
    return valor.strip()


@dataclass(frozen=True, slots=True)
class LinhaMaoObraCargaTransporte:
    id: str
    descricao: str
    quantidade: float | None
    custo_hora: float | None
    horas_dia_manual: float | None
    horas_referencia_id: str | None
    encargos_sociais: float | None

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição"))
        for campo in (
            "quantidade",
            "custo_hora",
            "horas_dia_manual",
            "encargos_sociais",
        ):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if self.horas_referencia_id is not None:
            object.__setattr__(
                self,
                "horas_referencia_id",
                _texto(self.horas_referencia_id, "referência de horas"),
            )
        if (self.horas_dia_manual is None) == (self.horas_referencia_id is None):
            raise ValueError("Horas/dia devem ser manuais ou referenciadas.")


@dataclass(frozen=True, slots=True)
class ItemCargaTransporte:
    id: str
    numero: int
    descricao: str
    unidade: str
    quantidade: float | None
    preco_unitario_manual: float | None
    preco_unitario_custo_diario: bool

    def __post_init__(self):
        for campo in ("id", "descricao", "unidade"):
            object.__setattr__(self, campo, _texto(getattr(self, campo), campo))
        if (
            isinstance(self.numero, bool)
            or not isinstance(self.numero, int)
            or self.numero < 1
        ):
            raise ValueError("Número do item deve ser inteiro positivo.")
        object.__setattr__(self, "quantidade", _numero(self.quantidade, "quantidade"))
        object.__setattr__(
            self,
            "preco_unitario_manual",
            _numero(self.preco_unitario_manual, "preço unitário"),
        )
        if not isinstance(self.preco_unitario_custo_diario, bool):
            raise ValueError("Origem do preço unitário inválida.")
        if (
            self.preco_unitario_manual is not None
            and self.preco_unitario_custo_diario
        ):
            raise ValueError("Preço unitário deve possuir uma única origem.")


def _equipe_inicial():
    return (
        LinhaMaoObraCargaTransporte(
            "operador-lider", "Operador Líder", None, 14.5, 9, None, 110
        ),
        LinhaMaoObraCargaTransporte(
            "operador-draga",
            "Operador de Draga",
            2,
            15.1,
            None,
            "operador-lider",
            110,
        ),
        LinhaMaoObraCargaTransporte(
            "ajudante-geral", "Ajudante Geral", 5, 8, 9, None, 110
        ),
    )


def _itens_iniciais():
    return (
        ItemCargaTransporte(
            "carga-transporte-6km",
            1,
            "Carga e Transporte (6KM)",
            "m3",
            None,
            32,
            False,
        ),
        ItemCargaTransporte(
            "batimetria-fos", 3, "Batimetria FOS", "dias", None, None, False
        ),
        ItemCargaTransporte(
            "acompanhamento-fos",
            4,
            "Acompanhamento  FOS",
            "dia",
            None,
            None,
            True,
        ),
    )


@dataclass(frozen=True, slots=True)
class CargaTransporte:
    equipe: tuple[LinhaMaoObraCargaTransporte, ...] = _equipe_inicial()
    custo_refeicao: float | None = 30.0
    custo_transporte: float | None = 10.0
    itens: tuple[ItemCargaTransporte, ...] = _itens_iniciais()
    bdi_principal: float | None = None
    bdi_secundario: float | None = 0.0

    def __post_init__(self):
        for campo in (
            "custo_refeicao",
            "custo_transporte",
            "bdi_principal",
            "bdi_secundario",
        ):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if not isinstance(self.equipe, tuple) or not all(
            isinstance(item, LinhaMaoObraCargaTransporte) for item in self.equipe
        ):
            raise ValueError("Equipe de Carga e Transporte inválida.")
        if not isinstance(self.itens, tuple) or not all(
            isinstance(item, ItemCargaTransporte) for item in self.itens
        ):
            raise ValueError("Itens de Carga e Transporte inválidos.")
        ids_equipe = {item.id for item in self.equipe}
        ids = [item.id for item in self.equipe] + [item.id for item in self.itens]
        if len(ids) != len(set(ids)):
            raise ValueError("Identificadores de Carga e Transporte devem ser únicos.")
        if any(
            item.horas_referencia_id is not None
            and item.horas_referencia_id not in ids_equipe
            for item in self.equipe
        ):
            raise ValueError("Referência de horas de Carga e Transporte inválida.")


@dataclass(frozen=True, slots=True)
class ResultadoLinhaMaoObraCargaTransporte:
    id: str
    horas_dia: float | None
    total: float


@dataclass(frozen=True, slots=True)
class ResultadoItemCargaTransporte:
    id: str
    preco_unitario: float | None
    preco_total: float


@dataclass(frozen=True, slots=True)
class ResultadosCargaTransporte:
    mao_obra: tuple[ResultadoLinhaMaoObraCargaTransporte, ...]
    quantidade_pessoas: float
    total_refeicoes: float
    total_transportes: float
    custo_por_dia: float
    itens: tuple[ResultadoItemCargaTransporte, ...]
    total: float
    valor_bdi_principal: float
    preco_final: float
    valor_bdi_secundario: float
    preco_final_secundario: float


FORMULAS_CARGA_TRANSPORTE = (
    ("F5", "=(A5*C5*D5)+(A5*C5*D5)*(E5/100)"),
    ("D6", "=D5"),
    ("F6", "=(A6*C6*D6)+(A6*C6*D6)*(E6/100)"),
    ("F7", "=(A7*C7*D7)+(A7*C7*D7)*(E7/100)"),
    ("A8", "=A5+A7+A6"),
    ("F8", "=A8*C8"),
    ("A9", "=A8"),
    ("F9", "=A9*C9"),
    ("F10", "=SUM(F5:F9)"),
    ("F15", "=D15*E15"),
    ("F16", "=D16*E16"),
    ("E17", "=F10"),
    ("F17", "=D17*E17"),
    ("F18", "=SUM(F15:F17)"),
    ("F19", "=F18*(E19/100)"),
    ("F20", "=SUM(F18:F19)"),
    ("F22", "=F21*(E22/100)"),
    ("F23", "=SUM(F21:F22)"),
)


def calcular_carga_transporte(
    carga_transporte: CargaTransporte,
) -> ResultadosCargaTransporte:
    """Reproduz somente as 18 fórmulas efetivamente presentes na aba."""
    zero = lambda valor: 0.0 if valor is None else valor
    horas_por_id = {}
    mao_obra = []
    for linha in carga_transporte.equipe:
        horas = linha.horas_dia_manual
        if linha.horas_referencia_id is not None:
            horas = horas_por_id.get(linha.horas_referencia_id)
        horas_por_id[linha.id] = horas
        total = (
            zero(linha.quantidade)
            * zero(linha.custo_hora)
            * zero(horas)
            * (1 + zero(linha.encargos_sociais) / 100)
        )
        mao_obra.append(
            ResultadoLinhaMaoObraCargaTransporte(linha.id, horas, total)
        )

    pessoas = sum(zero(item.quantidade) for item in carga_transporte.equipe)
    refeicoes = pessoas * zero(carga_transporte.custo_refeicao)
    transportes = pessoas * zero(carga_transporte.custo_transporte)
    custo_por_dia = sum(item.total for item in mao_obra) + refeicoes + transportes

    itens = []
    for item in carga_transporte.itens:
        unitario = (
            custo_por_dia
            if item.preco_unitario_custo_diario
            else item.preco_unitario_manual
        )
        itens.append(
            ResultadoItemCargaTransporte(
                item.id, unitario, zero(item.quantidade) * zero(unitario)
            )
        )
    total = sum(item.preco_total for item in itens)
    bdi_principal = total * zero(carga_transporte.bdi_principal) / 100
    # F21 não existe no XML; F22/F23 avaliam a referência vazia como zero.
    bdi_secundario = 0.0 * zero(carga_transporte.bdi_secundario) / 100
    return ResultadosCargaTransporte(
        tuple(mao_obra),
        pessoas,
        refeicoes,
        transportes,
        custo_por_dia,
        tuple(itens),
        total,
        bdi_principal,
        total + bdi_principal,
        bdi_secundario,
        bdi_secundario,
    )
