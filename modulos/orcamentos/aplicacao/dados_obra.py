"""Caso de uso da aba Dados Obra."""

from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def salvar_dados_obra(
    versao: VersaoOrcamento, dados: DadosObra
) -> ResultadoOperacao[DadosObra]:
    """Registra a fotografia integral da aba na versão em elaboração."""
    return versao.registrar_dados_obra(dados)
