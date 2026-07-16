"""Criação estrutural mínima de um orçamento utilizável."""

from modulos.orcamentos.dominio.identidades import CenarioId, OrcamentoId, VersaoId
from modulos.orcamentos.dominio.modelos import Cenario, Orcamento, VersaoOrcamento
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def criar_orcamento_vazio(
    autor: str,
) -> ResultadoOperacao[tuple[Orcamento, VersaoOrcamento]]:
    """Cria Orçamento, Versão 1 e Cenário Principal, sem dados de planilha."""
    try:
        responsavel = autor.strip()
        if not responsavel:
            raise ValueError
        orcamento = Orcamento(
            OrcamentoId.nova(), "Novo orçamento", "Proposta", responsavel
        )
        versao = VersaoOrcamento(VersaoId.nova(), orcamento.id, 1, responsavel)
        cenario = Cenario(CenarioId.nova(), versao.id, "Cenário Principal")
    except (AttributeError, TypeError, ValueError):
        return ResultadoOperacao.falha("Autor inválido para criação do orçamento.")

    resultado_cenario = versao.adicionar_cenario(cenario)
    if not resultado_cenario.sucesso:
        return ResultadoOperacao.falha(resultado_cenario.erro)
    resultado_versao = orcamento.adicionar_versao(versao)
    if not resultado_versao.sucesso:
        return ResultadoOperacao.falha(resultado_versao.erro)
    return ResultadoOperacao.ok((orcamento, versao))
