"""Caso de uso da aba Produção."""

from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.producao import Producao
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def salvar_producao(
    versao: VersaoOrcamento, producao: Producao
) -> ResultadoOperacao[Producao]:
    return versao.registrar_producao(producao)
