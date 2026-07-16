"""Casos de uso locais para identificação e premissas."""

from dataclasses import dataclass

from modulos.orcamentos.dominio.identidades import CenarioId
from modulos.orcamentos.dominio.modelos import Orcamento, VersaoOrcamento
from modulos.orcamentos.dominio.premissas import OrigemPremissa, Premissa, ValorPremissa
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


@dataclass(frozen=True, slots=True)
class RascunhoPremissa:
    conceito: str
    unidade: str
    autor: str
    valor_sugerido: str | None = None
    valor_adotado: str | None = None
    origem_adotada: OrigemPremissa = OrigemPremissa.ENGENHARIA
    vigencia: str | None = None
    justificativa: str | None = None


def atualizar_identificacao(
    orcamento: Orcamento,
    versao: VersaoOrcamento,
    *,
    objeto: str,
    finalidade: str,
    responsavel: str,
) -> ResultadoOperacao[Orcamento]:
    if versao.orcamento_id != orcamento.id:
        return ResultadoOperacao.falha("A versão pertence a outro orçamento.")
    if not versao.editavel:
        return ResultadoOperacao.falha("A identificação só pode mudar durante a elaboração.")
    try:
        valores = [objeto, finalidade, responsavel]
        if any(not isinstance(valor, str) or not valor.strip() for valor in valores):
            raise ValueError
        orcamento.objeto, orcamento.finalidade, orcamento.responsavel = (
            valor.strip() for valor in valores
        )
    except (TypeError, ValueError):
        return ResultadoOperacao.falha("Objeto, finalidade e responsável são obrigatórios.")
    return ResultadoOperacao.ok(orcamento)


def aplicar_rascunho(
    versao: VersaoOrcamento,
    cenario_id: CenarioId,
    rascunho: RascunhoPremissa,
) -> ResultadoOperacao[Premissa]:
    try:
        conceito = rascunho.conceito.strip()
        unidade = rascunho.unidade.strip()
        autor = rascunho.autor.strip()
        if not conceito or not unidade or not autor:
            raise ValueError
        historico = versao.historico_premissa(cenario_id, conceito)
        anterior = historico[-1] if historico else None
        sugerido = anterior.sugerido if anterior else None
        adotado = anterior.adotado if anterior else None
        if rascunho.valor_sugerido and rascunho.valor_sugerido.strip():
            sugerido = ValorPremissa(
                rascunho.valor_sugerido,
                unidade,
                OrigemPremissa.SUGESTAO,
                autor,
                rascunho.vigencia,
            )
        if rascunho.valor_adotado and rascunho.valor_adotado.strip():
            if rascunho.origem_adotada is OrigemPremissa.MANUAL and not (
                rascunho.justificativa and rascunho.justificativa.strip()
            ):
                return ResultadoOperacao.falha(
                    "Valor manual exige justificativa explícita."
                )
            adotado = ValorPremissa(
                rascunho.valor_adotado,
                unidade,
                rascunho.origem_adotada,
                autor,
                rascunho.vigencia,
                rascunho.justificativa,
            )
        premissa = Premissa(conceito, len(historico) + 1, sugerido, adotado)
    except (AttributeError, TypeError, ValueError):
        return ResultadoOperacao.falha("Rascunho de premissa inválido.")
    return versao.registrar_premissa(cenario_id, premissa)
