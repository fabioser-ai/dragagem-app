"""Caso de uso da aba 8. Desmob. Draga."""

from modulos.orcamentos.dominio.desmobilizacao_draga import DesmobilizacaoDraga
from modulos.orcamentos.dominio.modelos import VersaoOrcamento


def salvar_desmobilizacao_draga(
    versao: VersaoOrcamento, desmobilizacao: DesmobilizacaoDraga
):
    return versao.registrar_desmobilizacao_draga(desmobilizacao)
