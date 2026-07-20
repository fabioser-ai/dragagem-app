"""Caso de uso da aba 5. Operação Sistema."""

from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.operacao_sistema import OperacaoSistema
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def salvar_operacao_sistema(
    versao: VersaoOrcamento, operacao: OperacaoSistema
) -> ResultadoOperacao[OperacaoSistema]:
    return versao.registrar_operacao_sistema(operacao)
