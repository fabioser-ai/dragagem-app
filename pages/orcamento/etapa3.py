import streamlit as st
import pandas as pd
from services.github import carregar_github, salvar_github

# =========================
# ARQUIVO
# =========================
ARQ_INSUMOS = "data/insumos.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]


def etapa3():

    st.header("Custo do Barrilete")

    # =========================
    # CARREGAR INSUMOS
    # =========================
    try:
        df_insumos = carregar_github(ARQ_INSUMOS, TOKEN, REPO)
    except:
        df_insumos = pd.DataFrame(columns=["Insumo", "Preco_Unitario"])

    if df_insumos.empty:
        df_insumos = pd.DataFrame(columns=["Insumo", "Preco_Unitario"])

    # garantir colunas
    if "Preco_Unitario" not in df_insumos.columns:
        df_insumos["Preco_Unitario"] = 0.0

    # =========================
    # CRUD INSUMOS (BASE)
    # =========================
    st.subheader("Cadastro de Insumos")

    df_base = df_insumos.copy().fillna({
        "Insumo": "",
        "Preco_Unitario": 0.0
    })

    df_crud = st.data_editor(
        df_base,
        use_container_width=True,
        num_rows="dynamic",
        key="crud_insumos",
        column_config={
            "Insumo": st.column_config.TextColumn("Insumo"),
            "Preco_Unitario": st.column_config.NumberColumn("Preço Unitário (R$)", min_value=0.0),
        }
    )

    col1, col2 = st.columns(2)

    if col1.button("💾 Salvar Insumos"):

        df_salvar = df_crud.copy()

        df_salvar = df_salvar[df_salvar["Insumo"] != ""]
        df_salvar["Preco_Unitario"] = pd.to_numeric(
            df_salvar["Preco_Unitario"], errors="coerce"
        ).fillna(0)

        salvar_github(df_salvar, ARQ_INSUMOS, TOKEN, REPO)

        st.success("Insumos salvos com sucesso")
        st.rerun()

    if col2.button("🔄 Atualizar lista"):
        st.rerun()

    st.divider()

    # =========================
    # VALIDAR EQUIPE
    # =========================
    custo_hora = st.session_state.orcamento.get("custo_hora_equipe")

    if not custo_hora:
        st.error("Custo da equipe não definido. Volte na Etapa 2.")
        return

    # =========================
    # USO DOS INSUMOS
    # =========================
    st.subheader("Composição do Barrilete")

    # session_state anti-reset
    if "insumos_editados" not in st.session_state:
        df_temp = df_insumos.copy()
        df_temp["Qtd"] = 0.0
        st.session_state.insumos_editados = df_temp

    df_editado = st.data_editor(
        st.session_state.insumos_editados,
        use_container_width=True,
        num_rows="fixed",
        key="editor_insumos",
        column_config={
            "Insumo": st.column_config.TextColumn("Insumo", disabled=True),
            "Qtd": st.column_config.NumberColumn("Quantidade", min_value=0.0),
            "Preco_Unitario": st.column_config.NumberColumn("Preço Unitário (R$)", min_value=0.0),
        }
    )

    # salvar edição (anti reset)
    st.session_state.insumos_editados = df_editado

    # =========================
    # EQUIPE
    # =========================
    st.subheader("Equipe")

    col1, col2 = st.columns(2)

    horas_dia = col1.number_input("Horas por dia", value=8.0)
    dias = col2.number_input("Número de dias", value=1)

    custo_equipe_total = custo_hora * horas_dia * dias

    st.info(
        f"Custo equipe: R$ {custo_hora:,.2f}/h × "
        f"{horas_dia}h × {dias} dias = "
        f"R$ {custo_equipe_total:,.2f}"
    )

    # =========================
    # CÁLCULO
    # =========================
    df_calc = df_editado.copy()

    df_calc["Qtd"] = pd.to_numeric(df_calc["Qtd"], errors="coerce").fillna(0)
    df_calc["Preco_Unitario"] = pd.to_numeric(df_calc["Preco_Unitario"], errors="coerce").fillna(0)

    df_calc["Total"] = df_calc["Qtd"] * df_calc["Preco_Unitario"]

    total_insumos = df_calc["Total"].sum()

    # linha equipe
    df_equipe = pd.DataFrame([{
        "Insumo": "Equipe",
        "Qtd": horas_dia * dias,
        "Preco_Unitario": custo_hora,
        "Total": custo_equipe_total
    }])

    df_final = pd.concat([df_calc, df_equipe], ignore_index=True)

    # remover linhas zeradas
    df_final = df_final[df_final["Total"] > 0]

    total_geral = total_insumos + custo_equipe_total

    # =========================
    # RESULTADO
    # =========================
    st.subheader("Resultado Final")

    st.dataframe(
        df_final[["Insumo", "Qtd", "Preco_Unitario", "Total"]],
        use_container_width=True
    )

    st.success(f"Insumos: R$ {total_insumos:,.2f}")
    st.success(f"Equipe: R$ {custo_equipe_total:,.2f}")
    st.success(f"TOTAL: R$ {total_geral:,.2f}")

    # =========================
    # SALVAR
    # =========================
    st.session_state.orcamento.update({
        "insumos": df_calc.to_dict(orient="records"),
        "custo_insumos": total_insumos,
        "custo_equipe_total": custo_equipe_total,
        "custo_total_barrilete": total_geral,
        "dias_barrilete": dias,
        "horas_dia_barrilete": horas_dia
    })

    # =========================
    # NAVEGAÇÃO
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento2"
        st.rerun()

    if col2.button("Finalizar"):
        st.success("Orçamento finalizado")
