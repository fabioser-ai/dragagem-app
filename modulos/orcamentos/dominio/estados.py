"""Estados semânticos mínimos do núcleo de Orçamentos."""

from enum import Enum


class EstadoVersao(str, Enum):
    ELABORACAO = "elaboracao"
    CONGELADA = "congelada"
    APROVADA = "aprovada"


class EstadoCenario(str, Enum):
    ATIVO = "ativo"
    DESCARTADO = "descartado"
