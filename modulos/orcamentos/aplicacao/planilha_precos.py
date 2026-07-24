"""Casos de uso da equivalência funcional da Planilha de Preços."""

from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.planilha_precos import PlanilhaPrecos


def salvar_planilha_precos(
    versao: VersaoOrcamento, planilha_precos: PlanilhaPrecos
):
    return versao.registrar_planilha_precos(planilha_precos)
