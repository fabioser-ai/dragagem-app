"""Caso de uso da aba 2. Mob. Eq. Polimero."""

from modulos.orcamentos.dominio.mobilizacao_equipamento_polimero import (
    MobilizacaoEquipamentoPolimero,
)
from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def salvar_mobilizacao_equipamento_polimero(
    versao: VersaoOrcamento, mobilizacao: MobilizacaoEquipamentoPolimero
) -> ResultadoOperacao[MobilizacaoEquipamentoPolimero]:
    return versao.registrar_mobilizacao_equipamento_polimero(mobilizacao)
