"""Caso de uso da aba 3. Prep. Célula."""

from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.preparacao_celula import PreparacaoCelula
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def salvar_preparacao_celula(
    versao: VersaoOrcamento, preparacao: PreparacaoCelula
) -> ResultadoOperacao[PreparacaoCelula]:
    return versao.registrar_preparacao_celula(preparacao)
