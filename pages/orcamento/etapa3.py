import streamlit as st
import pandas as pd
from datetime import datetime
from services.github import carregar_github, salvar_github

ARQ_INSUMOS = "data/insumos.csv"
ARQ_HIST = "data/insumos_historico.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# FORMATADOR BR
# =========================
def formatar_real(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# =========================
# ETAPA 3
# =========================
def etapa3():

    st.header("Custo do Barrilete (Insumos)")

    df_insumos = carregar_github(ARQ_INSUMOS, TOKEN, REPO)

    if df_insumos.empty:
        st.error("Base de insumos vazia")
        return

    df_insumos["Preco_Atual"] = pd.to_numeric(
        df_insumos["Preco_Atual"], errors="coerce"
    ).fillna(0)

    # =========================
    # SESSION STATE
    # =========================
    if "df_barrilete" not in st.session_state:
        df_init = df_insumos.copy()
        df_init["Qtd"] = 0
        df_init["Preço Unitário"] = df_init["Preco_Atual"]

        st.session_state.df_barrilete = df_init[["Item", "Qtd", "Preço Unitário"]]

    # =========================
    # FORM (SEM PERDER DADOS)
    # =========================
    with st.form("form_barrilete"):

        df_editado = st.data_editor(
            st.session_state.df_barrilete,
            use_container_width=True,
            hide_index=True
        )

        dias = st.number_input("Número de dias", min_value=1, value=1)

        calcular = st.form_submit_button("Calcular custos")

    # =========================
    # PROCESSAMENTO
    # =========================
    if calcular:

        df_antigo = df_insumos.set_index("Item")["Preco_Atual"]

        df_novo = df_editado.copy()

        # =========================
        # HISTÓRICO (BACKGROUND)
        # =========================
        try:
            df_hist = carregar_github(ARQ_HIST, TOKEN, REPO)
        except:
            df_hist = pd.DataFrame(columns=["Item","Preco","Data"])

        novos_registros = []

        for _, row in df_novo.iterrows():

            item = row["Item"]
            preco_novo = float(row["Preço Unitário"])
            preco_antigo = float(df_antigo.get(item, 0))

            if preco_novo != preco_antigo:

                novos_registros.append({
                    "Item": item,
                    "Preco": preco_novo,
                    "Data": datetime.now().strftime("%d/%m/%Y %H:%M")
                })

                df_insumos.loc[
                    df_insumos["Item"] == item, "Preco_Atual"
                ] = preco_novo

        if novos_registros:
            df_hist = pd.concat(
                [df_hist, pd.DataFrame(novos_registros)],
                ignore_index=True
            )
            salvar_github(df_hist, ARQ_HIST, TOKEN, REPO)

        salvar_github(df_insumos, ARQ_INSUMOS, TOKEN, REPO)

        # =========================
        # CÁLCULO
        # =========================
        df_novo["Total"] = df_novo["Qtd"] * df_novo["Preço Unitário"]

        df_display = df_novo[df_novo["Qtd"] > 0].copy()

        total_materiais = df_novo["Total"].sum()

        # =========================
        # TABELA FINAL
        # =========================
        if not df_display.empty:

            df_display["Preço Unitário"] = df_display["Preço Unitário"].apply(formatar_real)
            df_display["Total"] = df_display["Total"].apply(formatar_real)

            st.subheader("Insumos utilizados")

            st.dataframe(
                df_display[["Item","Qtd","Preço Unitário","Total"]],
                use_container_width=True,
                hide_index=True
            )

        # =========================
        # MÃO DE OBRA
        # =========================
        custo_hora = st.session_state.orcamento.get("custo_hora_equipe", 0)
        custo_total_equipe = custo_hora * 8 * dias

        # =========================
        # TOTAL
        # =========================
        total_geral = total_materiais + custo_total_equipe

        st.subheader("Resumo")

        st.write(f"Insumos: R$ {formatar_real(total_materiais)}")
        st.write(f"Mão de obra: R$ {formatar_real(custo_total_equipe)}")

        st.success(f"TOTAL GERAL: R$ {formatar_real(total_geral)}")
