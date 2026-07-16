"""Fotografia fiel da aba ``Cotaçoes`` do Excel oficial."""

from dataclasses import dataclass, field


def _texto(valor, campo):
    if not isinstance(valor, str):
        raise ValueError(f"{campo} deve ser texto.")
    return valor


def _preco(valor, campo):
    if valor is not None and (
        isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor < 0
    ):
        raise ValueError(f"{campo} deve ser monetário não negativo ou vazio.")
    return float(valor) if valor is not None else None


@dataclass(frozen=True, slots=True)
class CotacaoGuindaste:
    nome: str = ""
    contato: str = ""
    telefone: str = ""
    detalhe: str = ""
    preco_hora: float | None = None
    preco_diaria: float | None = None

    def __post_init__(self):
        for campo in ("nome", "contato", "telefone", "detalhe"):
            object.__setattr__(self, campo, _texto(getattr(self, campo), campo))
        for campo in ("preco_hora", "preco_diaria"):
            object.__setattr__(self, campo, _preco(getattr(self, campo), campo))


@dataclass(frozen=True, slots=True)
class CotacaoContainer:
    nome: str = ""
    contato: str = ""
    telefone: str = ""
    detalhe: str = ""
    preco_mes: float | None = None
    frete_hora: float | None = None

    def __post_init__(self):
        for campo in ("nome", "contato", "telefone", "detalhe"):
            object.__setattr__(self, campo, _texto(getattr(self, campo), campo))
        for campo in ("preco_mes", "frete_hora"):
            object.__setattr__(self, campo, _preco(getattr(self, campo), campo))


@dataclass(frozen=True, slots=True)
class CotacaoMensal:
    nome: str = ""
    contato: str = ""
    telefone: str = ""
    detalhe: str = ""
    preco_mes: float | None = None

    def __post_init__(self):
        for campo in ("nome", "contato", "telefone", "detalhe"):
            object.__setattr__(self, campo, _texto(getattr(self, campo), campo))
        object.__setattr__(self, "preco_mes", _preco(self.preco_mes, "preco_mes"))


def _linhas(tipo, quantidade):
    return tuple(tipo() for _ in range(quantidade))


@dataclass(frozen=True, slots=True)
class Cotacoes:
    guindaste: tuple[CotacaoGuindaste, ...] = field(
        default_factory=lambda: _linhas(CotacaoGuindaste, 4)
    )
    container: tuple[CotacaoContainer, ...] = field(
        default_factory=lambda: _linhas(CotacaoContainer, 3)
    )
    banheiro_quimico: tuple[CotacaoMensal, ...] = field(
        default_factory=lambda: _linhas(CotacaoMensal, 3)
    )
    destinacao: tuple[CotacaoMensal, ...] = field(
        default_factory=lambda: _linhas(CotacaoMensal, 3)
    )

    def __post_init__(self):
        especificacao = (
            ("guindaste", CotacaoGuindaste, 4),
            ("container", CotacaoContainer, 3),
            ("banheiro_quimico", CotacaoMensal, 3),
            ("destinacao", CotacaoMensal, 3),
        )
        for campo, tipo, quantidade in especificacao:
            linhas = getattr(self, campo)
            if not isinstance(linhas, tuple) or len(linhas) != quantidade or not all(
                isinstance(item, tipo) for item in linhas
            ):
                raise ValueError(f"Seção {campo} deve possuir {quantidade} linhas.")
