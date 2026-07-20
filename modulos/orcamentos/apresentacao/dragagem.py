"""Representação funcional mínima da aba 6. Dragagem."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.dragagem import salvar_dragagem
from modulos.orcamentos.dominio.canteiro import calcular_canteiro
from modulos.orcamentos.dominio.dragagem import (
    Dragagem, EntradaDragagem, FORMULAS_DRAGAGEM, OBSERVACOES_DRAGAGEM,
    calcular_dragagem,
)
from modulos.orcamentos.dominio.fornecimento_bag import calcular_fornecimento_bag
from modulos.orcamentos.dominio.operacao_sistema import calcular_operacao_sistema
from modulos.orcamentos.dominio.producao import calcular_producao
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _numero(rotulo, valor, chave):
    return st.number_input(rotulo, value=valor, min_value=0.0, key=chave)


def _formatar(valor, unidade=""):
    if valor is None:
        return "Pendente"
    texto = f"{valor:,.4f}".rstrip("0").rstrip(".").replace(",", "_").replace(".", ",").replace("_", ".")
    return f"{texto} {unidade}".strip()


def _referencias_externas(versao):
    dados = versao.dados_obra
    prazo = None
    if dados is not None:
        prazo = calcular_producao(
            versao.producao, dados.horario_trabalho, dados.dias_trabalho,
            dados.volume_dragagem,
        ).prazo_meses
    canteiro_f32 = calcular_canteiro(versao.canteiro, prazo).preco_final
    horas = dados.horario_trabalho if dados is not None else None
    tonelada = calcular_fornecimento_bag(
        versao.fornecimento_bag, horas
    ).memorial_fisico.tonelada_seca
    operacao_f24 = calcular_operacao_sistema(
        versao.operacao_sistema, horas, tonelada, prazo
    ).custo_mensal
    return canteiro_f32, operacao_f24, prazo


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_dragagem_salva", False):
        st.success("Dragagem salva.")
    atual = versao.dragagem
    canteiro_f32, operacao_f24, prazo = _referencias_externas(versao)
    resultados = calcular_dragagem(atual, canteiro_f32, operacao_f24, prazo)

    with st.form("dragagem_formulario"):
        st.subheader('Custo de Dragagem — Draga 6"')
        st.markdown('**Aba Excel: 6. Dragagem · intervalo A1:Q253**')
        st.markdown(
            "Referências explícitas: Canteiro!F32, '5. Operação Sistema'!F24 "
            "e Produção!D24. Os demais valores permanecem locais."
        )
        for observacao in OBSERVACOES_DRAGAGEM:
            st.markdown(f"- {observacao}")
        entradas_editadas = []
        bloco_atual = None
        for entrada in atual.entradas:
            if entrada.bloco != bloco_atual:
                bloco_atual = entrada.bloco
                st.markdown(f"### {bloco_atual}")
            valor = _numero(
                f"{entrada.celula} · {entrada.descricao} ({entrada.unidade or 'sem unidade'})",
                entrada.valor,
                f"dragagem_{entrada.celula}",
            )
            entradas_editadas.append(EntradaDragagem(
                entrada.celula, entrada.bloco, entrada.descricao, valor, entrada.unidade,
            ))

        st.markdown("### Memoriais e resultados calculados")
        for celula, formula in FORMULAS_DRAGAGEM:
            st.metric(f"{celula} · {formula}", _formatar(resultados.valor(celula)))

        st.markdown("### Resumo da composição")
        resumo = st.columns(4)
        with resumo[0]: st.metric("Despesas diretas — G181", _formatar(resultados.valor("G181"), "R$"))
        with resumo[1]: st.metric("Custo mensal — D246", _formatar(resultados.valor("D246"), "R$"))
        with resumo[2]: st.metric("Custo total — D248", _formatar(resultados.valor("D248"), "R$"))
        with resumo[3]: st.metric("Preço/hora — J253", _formatar(resultados.valor("J253"), "R$/h"))
        submetido = st.form_submit_button("Salvar Dragagem")

    if not submetido:
        return
    try:
        dragagem = Dragagem(tuple(entradas_editadas))
    except ValueError as erro:
        st.error(str(erro))
        return
    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_dragagem(copia_versao, dragagem)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_dragagem_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
