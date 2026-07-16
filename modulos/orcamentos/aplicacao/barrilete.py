"""Caso de uso da aba Barrilete."""

from modulos.orcamentos.dominio.barrilete import Barrilete
from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def salvar_barrilete(
    versao: VersaoOrcamento, barrilete: Barrilete
) -> ResultadoOperacao[Barrilete]:
    return versao.registrar_barrilete(barrilete)
