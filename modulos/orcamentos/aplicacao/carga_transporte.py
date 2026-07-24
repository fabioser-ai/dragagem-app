"""Casos de uso da equivalência funcional de Carga e Transporte."""

from modulos.orcamentos.dominio.carga_transporte import CargaTransporte
from modulos.orcamentos.dominio.modelos import VersaoOrcamento


def salvar_carga_transporte(
    versao: VersaoOrcamento, carga_transporte: CargaTransporte
):
    return versao.registrar_carga_transporte(carga_transporte)
