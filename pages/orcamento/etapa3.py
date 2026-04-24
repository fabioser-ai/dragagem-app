import streamlit as st
import pandas as pd
from services.github import carregar_github

ARQ_INSUMOS = "data/insumos.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]


def etapa3():

    st.header("Custos do Barrilete")

    # =========================
    # CARREGAR INSUMOS
    # =========================
    try:
        df_insumos = carregar_github(ARQ_INSUMOS, TOKEN, REPO)
    except:
        st.error("Erro ao carregar insumos.csv")
        return

    if df_insumos.empty:
        st.warning("Base de insumos vazia")
        return

    # =========================
    # GARANTIR COLUNAS
    # =========================
    if "Insumo" not in df_insumos.columns:
        st.error("Coluna 'Insumo' não encontrada")
        return

    if "Preco_Unitario" not in df_insumos.columns:
        df_insumos["Preco_Unitario"] = 0.0

    # =========================
    # SESSION STATE (ANTI RESET)
    # =========================
    if "etapa3_df" not in st.session_state:
        df = df_insumos.copy()
        df["Qtd"] = 0
        st.session_state.etapa3_df = df

    # =========================
    # TABELA EDITÁVEL
    # =========================
    st.subheader("Entrada de Insumos")

    df_editado = st.data_editor(
        st.session_state.etapa3_df,
        use_container_width=True,
        num_rows="fixed",
        key="editor_etapa3",
        column_config={
            "Insumo": st.column_config.TextColumn("Insumo", disabled=True),
            "Preco_Unitario": st.column_config.NumberColumn("Preço Unitário (R$)", format="%.2f"),
            "Qtd": st.column_config.NumberColumn("Quantidade", step=1, min_value=0),
        }
    )

    # salva estado SEM recalcular
    st.session_state.etapa3_df = df_editado.copy()

    # =========================
    # CUSTO DE EQUIPE
    # =========================
    st.divider()
    st.subheader("Custo de Equipe")

    custo_hora = st.session_state.orcamento.get("custo_mensal_equipe", 0)

    dias = st.number_input("Número de dias", value=1, min_value=0)

    custo_equipe_total = custo_hora * dias

    st.info(f"Custo equipe: R$ {custo_hora:,.2f} x {dias} dias = R$ {custo_equipe_total:,.2f}")

    # =========================
    # BOTÃO DE CÁLCULO
    # =========================
    if st.button("Calcular Custos"):

        df_calc = st.session_state.etapa3_df.copy()

        # cálculo seguro
        df_calc["Total"] = df_calc["Qtd"] * df_calc["Preco_Unitario"]

        # remover zeros
        df_calc = df_calc[df_calc["Qtd"] > 0]

        total_materiais = df_calc["Total"].sum()
        total_geral = total_materiais + custo_equipe_total

        # salva resultado (evita duplicação)
        st.session_state.resultado_etapa3 = {
            "df": df_calc,
            "materiais": total_materiais,
            "equipe": custo_equipe_total,
            "total": total_geral
        }

    # =========================
    # EXIBIR RESULTADO
    # =========================
    if "resultado_etapa3" in st.session_state:

        res = st.session_state.resultado_etapa3

        st.subheader("Resultado Calculado")

        st.dataframe(
            res["df"][["Insumo", "Qtd", "Preco_Unitario", "Total"]],
            use_container_width=True
        )

        st.success(f"Materiais: R$ {res['materiais']:,.2f}")
        st.success(f"Equipe: R$ {res['equipe']:,.2f}")
        st.success(f"TOTAL GERAL: R$ {res['total']:,.2f}")

    # =========================
    # NAVEGAÇÃO
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento2"
        st.rerun()

    if col2.button("Finalizar"):
        st.success("Orçamento finalizado (próximo passo: salvar)")
