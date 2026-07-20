"""Caso de uso da aba Canteiro."""

from modulos.orcamentos.dominio.canteiro import Canteiro
from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def salvar_canteiro(
    versao: VersaoOrcamento, canteiro: Canteiro
) -> ResultadoOperacao[Canteiro]:
    return versao.registrar_canteiro(canteiro)
