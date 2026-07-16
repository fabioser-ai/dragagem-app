"""Caso de uso da aba 1. Mob. Draga."""

from modulos.orcamentos.dominio.mobilizacao_draga import MobilizacaoDraga
from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def salvar_mobilizacao_draga(
    versao: VersaoOrcamento, mobilizacao: MobilizacaoDraga
) -> ResultadoOperacao[MobilizacaoDraga]:
    return versao.registrar_mobilizacao_draga(mobilizacao)
