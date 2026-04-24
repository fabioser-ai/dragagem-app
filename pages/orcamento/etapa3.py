import streamlit as st
import pandas as pd
from services.github import carregar_github

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
        st.warning("Base de insumos vazia")
        return

    # Garante estrutura correta
    if "Preco_Unitario" not in df_insumos.columns:
        df_insumos["Preco_Unitario"] = 0.0

    # =========================
    # INICIALIZA SESSION STATE
    # =========================
    if "insumos_editados" not in st.session_state:
        df_insumos["Qtd"] = 0.0
        st.session_state.insumos_editados = df_insumos.copy()

    # =========================
    # TABELA EDITÁVEL
    # =========================
    st.subheader("Entrada de Insumos")

    df_editado = st.data_editor(
        st.session_state.insumos_editados,
        use_container_width=True,
        num_rows="fixed",
        key="editor_insumos",
        column_config={
            "Insumo": st.column_config.TextColumn("Insumo", disabled=True),
            "Qtd": st.column_config.NumberColumn("Quantidade", min_value=0.0, step=1.0),
            "Preco_Unitario": st.column_config.NumberColumn("Preço Unitário (R$)", min_value=0.0),
        }
    )

    # Atualiza session sem perder dados
    st.session_state.insumos_editados = df_editado

    # =========================
    # BOTÃO DE CÁLCULO
    # =========================
    if st.button("Calcular custos"):

        df_calc = df_editado.copy()

        # =========================
        # CÁLCULO INSUMOS
        # =========================
        df_calc["Total"] = df_calc["Qtd"] * df_calc["Preco_Unitario"]

        total_insumos = df_calc["Total"].sum()

        # =========================
        # CUSTO EQUIPE
        # =========================
        st.subheader("Custo da Equipe")

        custo_hora = st.session_state.orcamento.get("custo_mensal_equipe", 0)

        horas_dia = st.number_input("Horas por dia", value=8.0)
        dias = st.number_input("Número de dias", value=1)

        custo_equipe_total = custo_hora * horas_dia * dias

        st.info(
            f"Custo equipe: R$ {custo_hora:,.2f}/h × "
            f"{horas_dia}h × {dias} dias = "
            f"R$ {custo_equipe_total:,.2f}"
        )

        # =========================
        # RESULTADO FINAL
        # =========================
        st.subheader("Resultado")

        df_resultado = df_calc[df_calc["Qtd"] > 0]

        st.dataframe(
            df_resultado[["Insumo", "Qtd", "Preco_Unitario", "Total"]],
            use_container_width=True
        )

        total_geral = total_insumos + custo_equipe_total

        st.success(f"Custo total insumos: R$ {total_insumos:,.2f}")
        st.success(f"Custo equipe: R$ {custo_equipe_total:,.2f}")
        st.success(f"CUSTO TOTAL: R$ {total_geral:,.2f}")

        # =========================
        # SALVAR
        # =========================
        st.session_state.orcamento.update({
            "insumos": df_resultado.to_dict(orient="records"),
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
        st.success("Orçamento pronto (próxima etapa futura)")
