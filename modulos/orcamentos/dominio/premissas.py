"""Valores de domínio para premissas adotadas em um cenário."""

from dataclasses import dataclass
from enum import Enum


class OrigemPremissa(str, Enum):
    SUGESTAO = "sugestao"
    CLIENTE = "cliente"
    ENGENHARIA = "engenharia"
    MANUAL = "manual"


@dataclass(frozen=True, slots=True)
class ValorPremissa:
    valor: str
    unidade: str
    origem: OrigemPremissa
    autor: str
    vigencia: str | None = None
    justificativa: str | None = None

    def __post_init__(self):
        for campo in ("valor", "unidade", "autor"):
            conteudo = getattr(self, campo)
            if not isinstance(conteudo, str) or not conteudo.strip():
                raise ValueError(f"{campo} deve ser informado.")
            object.__setattr__(self, campo, conteudo.strip())
        for campo in ("vigencia", "justificativa"):
            conteudo = getattr(self, campo)
            if conteudo is not None:
                if not isinstance(conteudo, str) or not conteudo.strip():
                    raise ValueError(f"{campo} deve ser texto não vazio quando informado.")
                object.__setattr__(self, campo, conteudo.strip())


@dataclass(frozen=True, slots=True)
class Premissa:
    conceito: str
    sequencia: int
    sugerido: ValorPremissa | None = None
    adotado: ValorPremissa | None = None

    def __post_init__(self):
        if not isinstance(self.conceito, str) or not self.conceito.strip():
            raise ValueError("conceito deve ser informado.")
        object.__setattr__(self, "conceito", self.conceito.strip())
        if not isinstance(self.sequencia, int) or self.sequencia < 1:
            raise ValueError("sequencia deve ser inteira positiva.")
        if self.sugerido is None and self.adotado is None:
            raise ValueError("A premissa precisa possuir valor sugerido ou adotado.")
        if self.sugerido and self.adotado and self.sugerido.unidade != self.adotado.unidade:
            raise ValueError("Valor sugerido e adotado devem usar a mesma unidade.")

    @property
    def pendente(self) -> bool:
        return self.adotado is None
