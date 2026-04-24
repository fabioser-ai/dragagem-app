import streamlit as st
import pandas as pd
from services.github import carregar_github

ARQ_SAL = "data/salarios.csv"

def etapa2():

    st.header("Dimensionamento de Equipe")

    df = carregar_github(ARQ_SAL, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"])

    if df.empty:
        st.warning("Sem dados de salário")
        return

    leis = st.number_input("Leis sociais (%)", value=110.0)
    fator_leis = 1 + leis / 100

    df = df.copy()
    df["Qtd"] = 0
    df["Adicional 25%"] = False

    df["Valor_Base"] = df["Valor_Hora"]
    df["Valor_Leis"] = df["Valor_Base"] * fator_leis

    df_edit = st.data_editor(
        df,
        use_container_width=True,
        column_config={
            "Qtd": st.column_config.NumberColumn("Qtd", min_value=0),
            "Adicional 25%": st.column_config.CheckboxColumn("25%"),
        }
    )

    df_edit["Valor_Final"] = df_edit["Valor_Leis"] * df_edit["Adicional 25%"].apply(lambda x: 1.25 if x else 1.0)
    df_edit["Total"] = df_edit["Qtd"] * df_edit["Valor_Final"]

    total = df_edit["Total"].sum()

    st.success(f"Total equipe: R$ {total:,.2f}")

    st.session_state.orcamento["equipe"] = df_edit.to_dict("records")

    col1, col2 = st.columns(2)

    if col1.button("Voltar"):
        st.session_state.tela_orcamento = "etapa1"
        st.rerun()

    if col2.button("Continuar"):
        st.session_state.tela_orcamento = "etapa3"
        st.rerun()
