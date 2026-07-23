"""Casos de uso da equivalência funcional da aba 7. Medição."""

from modulos.orcamentos.dominio.medicao_orcamento import MedicaoOrcamento
from modulos.orcamentos.dominio.modelos import VersaoOrcamento


def salvar_medicao_orcamento(
    versao: VersaoOrcamento, medicao: MedicaoOrcamento
):
    return versao.registrar_medicao_orcamento(medicao)
