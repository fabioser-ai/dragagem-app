"""Caso de uso da aba 4. Forn. Bag."""

from modulos.orcamentos.dominio.fornecimento_bag import FornecimentoBag
from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def salvar_fornecimento_bag(
    versao: VersaoOrcamento, fornecimento: FornecimentoBag
) -> ResultadoOperacao[FornecimentoBag]:
    return versao.registrar_fornecimento_bag(fornecimento)
