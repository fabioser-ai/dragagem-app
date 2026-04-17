import streamlit as st
import pandas as pd
from services.github import carregar_github, salvar_github

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

ARQ_FERIAS = "data/ferias.csv"

def render():

    st.title("Férias e Folgas")

    df = carregar_github(ARQ_FERIAS, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Funcionario","Data_Inicio","Data_Fim","Tipo"])

    st.dataframe(df)

    # =========================
    # EDITAR
    # =========================
    if not df.empty:

        idx = st.selectbox("Selecionar", df.index)
        linha = df.loc[idx]

        nome = st.text_input("Funcionário", value=linha["Funcionario"])
        data_inicio = st.date_input("Data início", value=pd.to_datetime(linha["Data_Inicio"]))
        data_fim = st.date_input("Data fim", value=pd.to_datetime(linha["Data_Fim"]))
        tipo = st.selectbox("Tipo", ["Férias","Folga"])

        col1, col2 = st.columns(2)

        if col1.button("Salvar"):
            df.loc[idx] = [nome, data_inicio, data_fim, tipo]
            salvar_github(df, ARQ_FERIAS, TOKEN, REPO)
            st.success("Atualizado!")
            st.rerun()

        if col2.button("Excluir"):
            df = df.drop(idx).reset_index(drop=True)
            salvar_github(df, ARQ_FERIAS, TOKEN, REPO)
            st.warning("Removido!")
            st.rerun()

    st.divider()

    # =========================
    # NOVO
    # =========================
    nome = st.text_input("Novo funcionário")
    data_inicio = st.date_input("Nova data início")
    data_fim = st.date_input("Nova data fim")
    tipo = st.selectbox("Novo tipo", ["Férias","Folga"])

    if st.button("Adicionar"):
        df.loc[len(df)] = [nome, data_inicio, data_fim, tipo]
        salvar_github(df, ARQ_FERIAS, TOKEN, REPO)
        st.success("Adicionado!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
