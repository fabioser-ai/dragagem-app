import streamlit as st
import pandas as pd
from services.github import carregar_github

ARQ_INSUMOS = "data/insumos.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

def etapa3():

    st.header("Custo do Barrilete")

    # =========================
    # CARREGAR BASE
    # =========================
    try:
        df_insumos = carregar_github(ARQ_INSUMOS, TOKEN, REPO)
    except:
        df_insumos = pd.DataFrame(columns=["Item", "Preco_Unitario"])

    if df_insumos.empty:
        st.warning("Base de insumos vazia")
        return

    # =========================
    # SESSION STATE (CRÍTICO)
    # =========================
    if "insumos_edit" not in st.session_state:
        df = df_insumos.copy()
        df["Qtd"] = 0
        st.session_state.insumos_edit = df

    if "resultado_etapa3" not in st.session_state:
        st.session_state.resultado_etapa3 = None

    # =========================
    # INPUT
    # =========================
    st.subheader("Entrada de Insumos")

    df_editado = st.data_editor(
        st.session_state.insumos_edit,
        use_container_width=True,
        key="editor_insumos",
        column_config={
            "Qtd": st.column_config.NumberColumn("Qtd", step=1, min_value=0),
            "Preco_Unitario": st.column_config.NumberColumn("Preço Unitário (R$)")
        }
    )

    # Atualiza estado SEM recalcular
    st.session_state.insumos_edit = df_editado

    # =========================
    # BOTÃO CALCULAR
    # =========================
    if st.button("Calcular Custos"):

        df_calc = df_editado.copy()

        df_calc["Total"] = df_calc["Qtd"] * df_calc["Preco_Unitario"]

        total_geral = df_calc["Total"].sum()

        # FILTRAR SOMENTE QTD > 0
        df_calc = df_calc[df_calc["Qtd"] > 0]

        # SALVAR RESULTADO (ESSENCIAL)
        st.session_state.resultado_etapa3 = {
            "df": df_calc,
            "total": total_geral
        }

    # =========================
    # RESULTADO (PERSISTENTE)
    # =========================
    if st.session_state.resultado_etapa3:

        st.subheader("Resultado Calculado")

        st.dataframe(
            st.session_state.resultado_etapa3["df"],
            use_container_width=True
        )

        st.success(
            f"Custo total do barrilete: R$ {st.session_state.resultado_etapa3['total']:,.2f}"
        )

    # =========================
    # CUSTO DA EQUIPE (INTEGRAÇÃO ETAPA 2)
    # =========================
    if "custo_hora_equipe" in st.session_state.orcamento:

        st.subheader("Custo da Equipe")

        dias = st.number_input("Número de dias", min_value=0)

        custo_dia = st.session_state.orcamento["custo_hora_equipe"] * 8
        custo_total = custo_dia * dias

        st.write(f"Custo por dia: R$ {custo_dia:,.2f}")
        st.success(f"Custo total equipe: R$ {custo_total:,.2f}")
