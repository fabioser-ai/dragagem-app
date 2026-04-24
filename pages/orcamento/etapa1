import streamlit as st
import pandas as pd
from services.github import carregar_github

ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"

def etapa1():

    st.header("Cálculo de Produção da Draga")

    dados = st.session_state.orcamento

    df_equip = carregar_github(ARQ_EQUIP, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"])
    df_mat = carregar_github(ARQ_MAT, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"])

    draga = st.selectbox("Draga", df_equip["Equipamento"])
    vazao = st.number_input("Vazão", value=float(df_equip[df_equip["Equipamento"]==draga]["Vazao"].iloc[0]))

    conc = st.number_input("Concentração", value=0.35)
    ef = st.number_input("Eficiência", value=0.85)

    prod_h = vazao * ef * conc

    st.success(f"Produção hora: {prod_h:.2f}")

    st.session_state.orcamento.update({
        "draga": draga,
        "vazao": vazao,
        "concentracao": conc,
        "eficiencia": ef,
        "producao_hora": prod_h
    })

    col1, col2 = st.columns(2)

    if col1.button("Voltar"):
        st.session_state.tela_orcamento = "etapa0"
        st.rerun()

    if col2.button("Continuar"):
        st.session_state.tela_orcamento = "etapa2"
        st.rerun()
