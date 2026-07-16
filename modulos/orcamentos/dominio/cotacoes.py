"""Itens mutáveis de cotação pertencentes a uma versão do orçamento."""

from dataclasses import dataclass
from uuid import uuid4


def _texto(valor, campo, *, obrigatorio=False):
    if not isinstance(valor, str) or (obrigatorio and not valor.strip()):
        raise ValueError(f"{campo} deve ser texto{' não vazio' if obrigatorio else ''}.")
    return valor.strip() if obrigatorio else valor


def _valor_monetario(valor, campo):
    if valor is not None and (
        isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor < 0
    ):
        raise ValueError(f"{campo} deve ser monetário não negativo ou vazio.")
    return float(valor) if valor is not None else None


@dataclass(frozen=True, slots=True)
class PropostaFornecedor:
    nome: str = ""
    contato: str = ""
    telefone: str = ""
    detalhe: str = ""
    primeiro_valor: float | None = None
    segundo_valor: float | None = None

    def __post_init__(self):
        for campo in ("nome", "contato", "telefone", "detalhe"):
            object.__setattr__(self, campo, _texto(getattr(self, campo), campo))
        for campo in ("primeiro_valor", "segundo_valor"):
            object.__setattr__(
                self, campo, _valor_monetario(getattr(self, campo), campo)
            )

    @property
    def preenchida(self):
        return any(
            valor not in (None, "")
            for valor in (
                self.nome,
                self.contato,
                self.telefone,
                self.detalhe,
                self.primeiro_valor,
                self.segundo_valor,
            )
        )


@dataclass(frozen=True, slots=True)
class ItemCotacao:
    id: str
    nome: str
    rotulo_primeiro_valor: str
    rotulo_segundo_valor: str | None
    propostas: tuple[PropostaFornecedor, ...]

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id", obrigatorio=True))
        object.__setattr__(self, "nome", _texto(self.nome, "nome", obrigatorio=True))
        object.__setattr__(
            self,
            "rotulo_primeiro_valor",
            _texto(
                self.rotulo_primeiro_valor,
                "rótulo do primeiro valor",
                obrigatorio=True,
            ),
        )
        segundo = self.rotulo_segundo_valor
        if segundo is not None:
            segundo = _texto(segundo, "rótulo do segundo valor").strip() or None
        object.__setattr__(self, "rotulo_segundo_valor", segundo)
        if not isinstance(self.propostas, tuple) or not all(
            isinstance(proposta, PropostaFornecedor) for proposta in self.propostas
        ):
            raise ValueError("propostas devem formar uma lista válida.")

    @property
    def preenchido(self):
        return any(proposta.preenchida for proposta in self.propostas)

    @classmethod
    def novo(cls, nome, rotulo_primeiro, rotulo_segundo=None):
        return cls(
            uuid4().hex,
            nome,
            rotulo_primeiro,
            rotulo_segundo,
            tuple(PropostaFornecedor() for _ in range(3)),
        )


@dataclass(frozen=True, slots=True)
class Cotacoes:
    itens: tuple[ItemCotacao, ...]

    def __post_init__(self):
        if not isinstance(self.itens, tuple) or not all(
            isinstance(item, ItemCotacao) for item in self.itens
        ):
            raise ValueError("itens de cotação inválidos.")
        ids = [item.id for item in self.itens]
        if len(ids) != len(set(ids)):
            raise ValueError("identificadores de itens devem ser únicos.")

    @classmethod
    def iniciais(cls):
        def item(identificador, nome, primeiro, segundo, quantidade):
            return ItemCotacao(
                identificador,
                nome,
                primeiro,
                segundo,
                tuple(PropostaFornecedor() for _ in range(quantidade)),
            )

        return cls(
            (
                item("inicial-guindaste", "Guindaste", "Preço por hora", "Preço por diária", 4),
                item("inicial-container", "Container", "Preço por mês", "Frete por hora", 3),
                item(
                    "inicial-banheiro-quimico",
                    "Banheiro Químico",
                    "Preço por mês",
                    None,
                    3,
                ),
                item("inicial-destinacao", "Destinação", "Preço por mês", None, 3),
            )
        )
