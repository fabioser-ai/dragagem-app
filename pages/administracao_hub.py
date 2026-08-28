import streamlit as st

from services.autorizacao import pode_gerenciar_administracao
from services.ui import renderizar_cabecalho_modulo
from pages import administracao as legado


def _voltar_menu():
    st.session_state[legado.AREA_ADMINISTRACAO] = None
    st.session_state.tela = "menu"
    st.rerun()


def _voltar_administracao():
    st.session_state[legado.AREA_ADMINISTRACAO] = None
    st.rerun()


def render():
    if not pode_gerenciar_administracao():
        st.error("Acesso restrito à custódia administrativa.")
        st.stop()

    area = st.session_state.get(legado.AREA_ADMINISTRACAO)
    areas_validas = {nome for nome, _ in legado.AREAS_ADMINISTRACAO}

    if area not in areas_validas:
        renderizar_cabecalho_modulo(
            "Administração",
            "← TELA INICIAL",
            _voltar_menu,
            key="administracao_header_menu",
        )
        st.caption("Gerencie pessoas, acessos, funções e histórico em um só lugar.")
        legado._render_inicio_administracao()
        return

    objetivos = dict(legado.AREAS_ADMINISTRACAO)
    renderizar_cabecalho_modulo(
        area,
        "← ADMINISTRAÇÃO",
        _voltar_administracao,
        key=f"administracao_header_{area.casefold()}",
    )
    st.caption(objetivos[area])

    if area == "Pessoas":
        legado._render_usuarios()
    elif area == "Acessos":
        legado._render_area_acessos()
    elif area == "Roles":
        legado._render_area_roles()
    elif area == "Diagnóstico":
        legado._render_area_diagnostico()
    else:
        legado._render_area_auditoria()
