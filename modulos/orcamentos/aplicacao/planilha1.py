"""Casos de uso da equivalência funcional da Planilha1."""

from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.planilha1 import Planilha1


def salvar_planilha1(versao: VersaoOrcamento, planilha1: Planilha1):
    return versao.registrar_planilha1(planilha1)
