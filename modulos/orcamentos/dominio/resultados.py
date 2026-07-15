"""Resultados explícitos para operações do núcleo de domínio em memória."""

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class ResultadoOperacao(Generic[T]):
    sucesso: bool
    valor: T | None = None
    erro: str | None = None

    @classmethod
    def ok(cls, valor=None):
        return cls(sucesso=True, valor=valor)

    @classmethod
    def falha(cls, erro: str):
        if not erro:
            raise ValueError("Uma falha deve possuir mensagem.")
        return cls(sucesso=False, erro=erro)
