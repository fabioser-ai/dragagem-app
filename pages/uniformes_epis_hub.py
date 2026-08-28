import streamlit as st

from services.autorizacao import pode, pode_acessar
from services.ui import renderizar_cabecalho_modulo
from pages import uniformes_epis as legado


def _voltar_menu():
    st.session_state.tela = "menu"
    st.rerun()


def render():
    if not pode_acessar("uniformes_epis"):
        st.error("Você não possui permissão para acessar Uniformes e EPIs.")
        return

    renderizar_cabecalho_modulo(
        "Uniformes e EPIs",
        "← TELA INICIAL",
        _voltar_menu,
        key="uniformes_header_menu",
    )
    st.caption("Controle de catálogo, compras, valores e localização física por obra.")

    token, repo = legado._configuracao()
    bases = legado.carregar_bases(token, repo)
    falhas = [
        resultado
        for resultado in bases.values()
        if not resultado.leitura_confirmada
    ]
    if falhas:
        st.error(
            "A leitura dos dados não foi confirmada. O módulo foi bloqueado "
            "para evitar perda de informações: " + legado._detalhes(falhas[0])
        )
        return

    itens = bases["itens"].dados
    compras = bases["compras"].dados
    movimentacoes = bases["movimentacoes"].dados
    entregas = bases["entregas"].dados
    estoque = legado.calcular_estoque(itens, compras, movimentacoes, entregas)
    posses = legado.calcular_posse_funcionarios(itens, entregas)
    pode_editar = pode(modulo="uniformes_epis", recurso="cadastros", acao="editar")

    (
        resumo,
        cadastro,
        aba_compras,
        aba_movimentos,
        aba_entregas,
        aba_historicos,
    ) = st.tabs(
        [
            "Visão geral",
            "Itens",
            "Compras",
            "Movimentações",
            "Entregas",
            "Históricos",
        ]
    )
    with resumo:
        legado._render_resumo(itens, compras, movimentacoes, estoque)
    with cadastro:
        legado._render_itens(itens, bases["itens"], pode_editar)
    with aba_compras:
        legado._render_compras(itens, compras, bases["compras"], pode_editar)
    with aba_movimentos:
        legado._render_movimentacoes(
            itens,
            movimentacoes,
            estoque,
            bases["movimentacoes"],
            pode_editar,
        )
    with aba_entregas:
        legado._render_ciclo_funcionario(
            itens,
            entregas,
            estoque,
            posses,
            bases["entregas"],
            pode_editar,
        )
    with aba_historicos:
        legado._render_historicos(
            itens, compras, movimentacoes, entregas, posses
        )
