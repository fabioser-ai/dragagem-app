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
        df_insumos = pd.DataFrame()

    if df_insumos.empty:
        st.warning("Base de insumos vazia")
        return

    # =========================
    # NORMALIZAR COLUNAS
    # =========================
    df_insumos.columns = df_insumos.columns.str.strip()

    # possíveis nomes de preço
    col_preco = None
    for c in df_insumos.columns:
        if c.lower() in ["preco_unitario", "preco", "valor", "preço", "preço_unitario"]:
            col_preco = c
            break

    if not col_preco:
        st.error("Coluna de preço não encontrada no CSV")
        st.write("Colunas encontradas:", list(df_insumos.columns))
        return

    # padroniza nome
    df_insumos = df_insumos.rename(columns={col_preco: "Preco_Unitario"})

    if "Item" not in df_insumos.columns:
        st.error("Coluna 'Item' não encontrada no CSV")
        return

    # =========================
    # SESSION STATE
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

    st.session_state.insumos_edit = df_editado

    # =========================
    # CALCULAR
    # =========================
    if st.button("Calcular Custos"):

        df_calc = df_editado.copy()

        # segurança extra
        df_calc["Preco_Unitario"] = pd.to_numeric(
            df_calc["Preco_Unitario"], errors="coerce"
        ).fillna(0)

        df_calc["Qtd"] = pd.to_numeric(
            df_calc["Qtd"], errors="coerce"
        ).fillna(0)

        df_calc["Total"] = df_calc["Qtd"] * df_calc["Preco_Unitario"]

        df_calc = df_calc[df_calc["Qtd"] > 0]

        total_geral = df_calc["Total"].sum()

        st.session_state.resultado_etapa3 = {
            "df": df_calc,
            "total": total_geral
        }

    # =========================
    # RESULTADO
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
    # EQUIPE
    # =========================
    if "custo_hora_equipe" in st.session_state.orcamento:

        st.subheader("Custo da Equipe")

        dias = st.number_input("Número de dias", min_value=0)

        custo_dia = st.session_state.orcamento["custo_hora_equipe"] * 8
        custo_total = custo_dia * dias

        st.write(f"Custo por dia: R$ {custo_dia:,.2f}")
        st.success(f"Custo total equipe: R$ {custo_total:,.2f}")
