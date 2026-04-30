import streamlit as st
import pandas as pd
from services.github import carregar_github

ARQ_OBRAS = "data/orcamentos.csv"
TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]


def carregar_orcamentos():
    try:
        return carregar_github(ARQ_OBRAS, TOKEN, REPO)
    except Exception:
        return pd.DataFrame()


def abrir_orcamento(linha):
    st.session_state.orcamento = linha.to_dict()

    etapa = str(linha.get("Etapa_Atual", "Etapa 0"))

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


def dashboard_orcamento():
    st.title("Gestão de Orçamentos")

    if "modo_orcamento" not in st.session_state:
        st.session_state.modo_orcamento = "inicio"

    if st.button("⬅ Voltar ao menu", key="orc_voltar_menu"):
        st.session_state.tela = "menu"
        st.session_state.modo_orcamento = "inicio"
        st.rerun()

    st.divider()

    if st.session_state.modo_orcamento == "inicio":
        col1, col2 = st.columns(2)

        with col1:
            if st.button("➕ Novo orçamento", use_container_width=True):
                if "orcamento" in st.session_state:
                    del st.session_state["orcamento"]

                st.session_state.modo_orcamento = "inicio"
                st.session_state.tela = "orcamento_etapa0"
                st.rerun()

        with col2:
            if st.button("📂 Continuar orçamento", use_container_width=True):
                st.session_state.modo_orcamento = "continuar"
                st.rerun()

        st.divider()

        df = carregar_orcamentos()

        if df.empty:
            st.info("Nenhum orçamento cadastrado ainda.")
            return

        st.subheader("Lista geral de orçamentos")
        st.dataframe(df, use_container_width=True)
        return

    if st.session_state.modo_orcamento == "continuar":
        st.subheader("Continuar orçamento existente")

        if st.button("⬅ Voltar", key="orc_voltar_inicio"):
            st.session_state.modo_orcamento = "inicio"
            st.rerun()

        df = carregar_orcamentos()

        if df.empty:
            st.warning("Nenhum orçamento encontrado.")
            return

        if "Status" not in df.columns:
            st.error("O arquivo data/orcamentos.csv não possui a coluna Status.")
            return

        df_abertos = df[df["Status"].astype(str) != "Finalizado"].copy()

        if df_abertos.empty:
            st.info("Não há orçamentos em andamento.")
            return

        df_abertos["Descricao"] = (
            df_abertos["Codigo"].astype(str)
            + " | "
            + df_abertos.get("Cliente", "").astype(str)
            + " | "
            + df_abertos.get("Nome_Obra", "").astype(str)
            + " | "
            + df_abertos.get("Status", "").astype(str)
            + " | "
            + df_abertos.get("Etapa_Atual", "").astype(str)
        )

        escolha = st.selectbox(
            "Selecione o orçamento",
            df_abertos["Descricao"],
            key="orc_select_continuar",
        )

        codigo = escolha.split(" | ")[0]
        linha = df_abertos[df_abertos["Codigo"].astype(str) == codigo].iloc[0]

        st.dataframe(pd.DataFrame([linha]), use_container_width=True)

        if st.button("Abrir orçamento selecionado", use_container_width=True):
            abrir_orcamento(linha)
