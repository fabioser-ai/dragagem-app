import streamlit as st

from services.auth import logout
from services.autorizacao import possui_perfil, possui_privilegio_administrativo
from services.ui import renderizar_cabecalho_modulo
from pages import prestacao_contas as legado


def _voltar_menu():
    st.session_state.tela = "menu"
    st.rerun()


def _sair():
    logout()


def render():
    if possui_perfil("funcionario"):
        renderizar_cabecalho_modulo(
            "Prestação de Contas",
            "SAIR",
            _sair,
            key="prestacao_header_sair",
        )
        aba_nova, aba_minhas = st.tabs(["Nova Despesa", "Minhas Despesas"])
        with aba_nova:
            legado.render_nova_despesa()
        with aba_minhas:
            legado.render_minhas_despesas()
        return

    renderizar_cabecalho_modulo(
        "Prestação de Contas",
        "← TELA INICIAL",
        _voltar_menu,
        key="prestacao_header_menu",
    )

    if possui_privilegio_administrativo():
        aba_todas, aba_nova, aba_minhas, aba_tipos = st.tabs(
            ["Todas as Despesas", "Nova Despesa", "Minhas Despesas", "Tipos de Despesa"]
        )
        with aba_todas:
            legado.render_todas_despesas()
        with aba_nova:
            legado.render_nova_despesa()
        with aba_minhas:
            legado.render_minhas_despesas()
        with aba_tipos:
            legado.render_tipos_despesa()
    else:
        aba_nova, aba_minhas = st.tabs(["Nova Despesa", "Minhas Despesas"])
        with aba_nova:
            legado.render_nova_despesa()
        with aba_minhas:
            legado.render_minhas_despesas()
