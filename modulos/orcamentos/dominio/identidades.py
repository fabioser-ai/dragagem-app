"""Identidades lógicas do domínio de Orçamentos."""

from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class Identidade:
    valor: str

    def __post_init__(self):
        if not isinstance(self.valor, str) or not self.valor.strip():
            raise ValueError("A identidade deve ser uma string não vazia.")
        object.__setattr__(self, "valor", self.valor.strip())

    @classmethod
    def nova(cls):
        return cls(uuid4().hex)

    def __str__(self):
        return self.valor


class OrcamentoId(Identidade):
    pass


class VersaoId(Identidade):
    pass


class CenarioId(Identidade):
    pass
