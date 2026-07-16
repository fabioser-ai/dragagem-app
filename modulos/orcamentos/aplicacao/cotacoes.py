"""Caso de uso da aba Cotações."""

from modulos.orcamentos.dominio.cotacoes import Cotacoes
from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def salvar_cotacoes(
    versao: VersaoOrcamento, cotacoes: Cotacoes
) -> ResultadoOperacao[Cotacoes]:
    return versao.registrar_cotacoes(cotacoes)
