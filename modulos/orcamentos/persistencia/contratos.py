"""Contratos públicos e explícitos da persistência de Orçamentos."""

from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar

T = TypeVar("T")


class StatusPersistencia(str, Enum):
    SUCESSO = "sucesso"
    CONFLITO = "conflito"
    BRANCH_AVANCADA = "branch_avancada"
    DADO_INEXISTENTE = "dado_inexistente"
    DADO_CORROMPIDO = "dado_corrompido"
    ERRO_REMOTO = "erro_remoto"
    OPERACAO_PARCIAL_RECUSADA = "operacao_parcial_recusada"
    REQUISICAO_INVALIDA = "requisicao_invalida"


@dataclass(frozen=True, slots=True)
class ResultadoPersistencia(Generic[T]):
    status: StatusPersistencia
    valor: T | None = None
    snapshot_esperado: str | None = None
    snapshot_observado: str | None = None
    commit_sha: str | None = None
    arquivos: tuple[str, ...] = ()
    erro: str | None = None

    @property
    def sucesso(self) -> bool:
        return self.status is StatusPersistencia.SUCESSO
