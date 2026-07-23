"""Caso de uso da aba 9. Desmob. Eq. Polimero."""

from modulos.orcamentos.dominio.desmobilizacao_equipamento_polimero import (
    DesmobilizacaoEquipamentoPolimero,
)
from modulos.orcamentos.dominio.modelos import VersaoOrcamento


def salvar_desmobilizacao_equipamento_polimero(
    versao: VersaoOrcamento,
    desmobilizacao: DesmobilizacaoEquipamentoPolimero,
):
    return versao.registrar_desmobilizacao_equipamento_polimero(desmobilizacao)
