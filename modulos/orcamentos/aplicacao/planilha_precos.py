"""Casos de uso da equivalência funcional da Planilha de Preços."""

from modulos.orcamentos.dominio.barrilete import calcular_barrilete
from modulos.orcamentos.dominio.canteiro import calcular_canteiro
from modulos.orcamentos.dominio.desmobilizacao_draga import (
    calcular_desmobilizacao_draga,
)
from modulos.orcamentos.dominio.desmobilizacao_equipamento_polimero import (
    calcular_desmobilizacao_equipamento_polimero,
)
from modulos.orcamentos.dominio.dragagem import calcular_dragagem
from modulos.orcamentos.dominio.fornecimento_bag import calcular_fornecimento_bag
from modulos.orcamentos.dominio.medicao_orcamento import (
    calcular_medicao_orcamento,
)
from modulos.orcamentos.dominio.mobilizacao_draga import (
    calcular_mobilizacao_draga,
)
from modulos.orcamentos.dominio.mobilizacao_equipamento_polimero import (
    calcular_mobilizacao_equipamento_polimero,
)
from modulos.orcamentos.dominio.modelos import VersaoOrcamento
from modulos.orcamentos.dominio.operacao_sistema import (
    calcular_operacao_sistema,
)
from modulos.orcamentos.dominio.planilha_precos import (
    PlanilhaPrecos,
    ReferenciasPlanilhaPrecos,
)
from modulos.orcamentos.dominio.preparacao_celula import (
    calcular_preparacao_celula,
)
from modulos.orcamentos.dominio.producao import calcular_producao


def compor_referencias_planilha_precos(
    versao: VersaoOrcamento,
) -> ReferenciasPlanilhaPrecos:
    """Compõe localmente as referências explícitas da worksheet de preços."""

    dados = versao.dados_obra
    horas = dados.horario_trabalho if dados is not None else None
    prazo = None
    if dados is not None:
        prazo = calcular_producao(
            versao.producao,
            dados.horario_trabalho,
            dados.dias_trabalho,
            dados.volume_dragagem,
        ).prazo_meses

    barrilete = calcular_barrilete(versao.barrilete, horas)
    mobilizacao_draga = calcular_mobilizacao_draga(versao.mobilizacao_draga)
    mobilizacao_polimero = calcular_mobilizacao_equipamento_polimero(
        versao.mobilizacao_equipamento_polimero,
        horas,
        barrilete.preco_final,
    )
    preparacao = calcular_preparacao_celula(versao.preparacao_celula, horas)
    fornecimento = calcular_fornecimento_bag(versao.fornecimento_bag, horas)
    canteiro = calcular_canteiro(versao.canteiro, prazo)
    operacao = calcular_operacao_sistema(
        versao.operacao_sistema,
        horas,
        fornecimento.memorial_fisico.tonelada_seca,
        prazo,
    )
    dragagem = calcular_dragagem(
        versao.dragagem,
        canteiro.preco_final,
        operacao.custo_mensal,
        prazo,
    )
    medicao = calcular_medicao_orcamento(versao.medicao_orcamento)
    desmobilizacao_draga = calcular_desmobilizacao_draga(
        versao.desmobilizacao_draga, horas
    )
    desmobilizacao_polimero = (
        calcular_desmobilizacao_equipamento_polimero(
            versao.desmobilizacao_equipamento_polimero,
            horas,
            barrilete.preco_final,
        )
    )
    return ReferenciasPlanilhaPrecos(
        mobilizacao_draga.preco_final_repetido,
        mobilizacao_polimero.preco_final,
        preparacao.preco_final,
        preparacao.composicao_real.area_total,
        fornecimento.preco_final,
        fornecimento.total_quantidade_area,
        dragagem.valor("D248"),
        versao.fornecimento_bag.memorial_fisico.volume,
        medicao.preco_final,
        desmobilizacao_draga.preco_final,
        desmobilizacao_polimero.preco_final,
    )


def salvar_planilha_precos(
    versao: VersaoOrcamento, planilha_precos: PlanilhaPrecos
):
    return versao.registrar_planilha_precos(planilha_precos)
