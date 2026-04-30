import streamlit as st
import pandas as pd
from services.github import carregar_github

ARQ_OBRAS = "data/orcamentos.csv"
TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]


def dashboard_orcamento():

    st.title("📊 Gestão de Orçamentos")

    if st.button("⬅ Voltar ao menu"):
        st.session_state.tela = "menu"
        st.rerun()

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Novo orçamento", use_container_width=True):
            if "orcamento" in st.session_state:
                del st.session_state["orcamento"]

            st.session_state.tela = "orcamento_etapa0"
            st.rerun()

    with col2:
        if st.button("📂 Continuar orçamento", use_container_width=True):
            st.session_state.tela = "orcamento_lista"
            st.rerun()

    st.divider()

    # =========================
    # LISTA DIRETA
    # =========================
    try:
        df = carregar_github(ARQ_OBRAS, TOKEN, REPO)
    except:
        df = pd.DataFrame()

    if df.empty:
        st.info("Nenhum orçamento cadastrado.")
        return

    st.subheader("📋 Lista de Orçamentos")

    filtro = st.selectbox(
        "Filtrar por status",
        ["Todos", "Rascunho", "Finalizado", "Cancelado"]
    )

    if filtro != "Todos":
        df = df[df["Status"] == filtro]

    if df.empty:
        st.warning("Nenhum orçamento encontrado.")
        return

    st.dataframe(df, use_container_width=True)

    escolha = st.selectbox(
        "Selecionar orçamento para abrir",
        df["Codigo"]
    )

    if st.button("Abrir orçamento"):

        linha = df[df["Codigo"] == escolha].iloc[0]

        st.session_state.orcamento = linha.to_dict()

        etapa = linha.get("Etapa_Atual", "Etapa 0")

        if etapa == "Etapa 0":
            st.session_state.tela = "orcamento_etapa0"
        elif etapa == "Etapa 1":
            st.session_state.tela = "orcamento1"
        elif etapa == "Etapa 2":
            st.session_state.tela = "orcamento2"
        elif etapa == "Etapa 3":
            st.session_state.tela = "orcamento3"
        else:
            st.session_state.tela = "orcamento_etapa0"

        st.rerun()
