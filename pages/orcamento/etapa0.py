import streamlit as st
import pandas as pd
from datetime import datetime
from services.github import carregar_github, salvar_github

ARQ_CLIENTES = "data/clientes.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"

def etapa0():

    st.header("Informações da Obra")

    df_clientes = carregar_github(ARQ_CLIENTES, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"])
    if df_clientes.empty:
        df_clientes = pd.DataFrame(columns=["Cliente"])

    cliente = st.selectbox("Cliente", df_clientes["Cliente"])
    novo_cliente = st.text_input("Ou adicionar novo cliente")

    nome_obra = st.text_input("Nome da obra")
    local = st.text_input("Local de execução")
    data = st.date_input("Data", value=datetime.now())

    volume = st.number_input("Volume a ser dragado")

    if st.button("Continuar"):

        if novo_cliente:
            cliente_final = novo_cliente
            df_clientes.loc[len(df_clientes)] = [novo_cliente]
            salvar_github(df_clientes, ARQ_CLIENTES, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"])
        else:
            cliente_final = cliente

        st.session_state.orcamento = {
            "cliente": cliente_final,
            "nome_obra": nome_obra,
            "local": local,
            "data": data.strftime("%d/%m/%Y"),
            "volume": volume
        }

        st.session_state.tela_orcamento = "etapa1"
        st.rerun()
