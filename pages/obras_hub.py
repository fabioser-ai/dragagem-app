import pandas as pd
import streamlit as st

from services.orcamentos_legado_operacional import carregar_github
from services.ui import renderizar_cabecalho_modulo


def _voltar_menu():
    st.session_state.tela = "menu"
    st.rerun()


def render():
    renderizar_cabecalho_modulo(
        "Obras",
        "← TELA INICIAL",
        _voltar_menu,
        key="obras_header_menu",
    )

    try:
        df = carregar_github(
            "data/orcamentos.csv",
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )
    except Exception:
        df = pd.DataFrame()

    if df.empty:
        st.warning("Nenhuma obra cadastrada ainda.")
    else:
        st.subheader("Lista de Obras")
        st.dataframe(df, use_container_width=True)
