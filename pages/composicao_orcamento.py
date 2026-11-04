"""Entrada isolada da Composição de Orçamento (desenvolvimento incremental)."""

import streamlit as st

from services.ui import renderizar_cabecalho_modulo


def _voltar_menu():
    st.session_state.tela = "menu"
    st.rerun()


def render():
    renderizar_cabecalho_modulo(
        "Composição de Orçamento",
        "← TELA INICIAL",
        _voltar_menu,
        key="composicao_orcamento_voltar_menu",
    )
    st.info("Módulo em construção. As etapas serão definidas progressivamente.")
