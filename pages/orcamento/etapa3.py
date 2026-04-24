import streamlit as st
import pandas as pd
from datetime import datetime
from services.github import carregar_github, salvar_github

ARQ_INSUMOS = "data/insumos.csv"
ARQ_HIST_PRECO = "data/insumos_historico.csv"
ARQ_HIST_USO = "data/insumos_uso_historico.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
def formatar_real(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

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
    # HISTÓRICO DE USO (QTD)
    # =========================
    try:
        df_uso = carregar_github(ARQ_HIST_USO, TOKEN, REPO)
    except:
        df_uso = pd.DataFrame(columns=["Item","Qtd","Data","Obra"])

    # pega última qtd por item
    ult_qtd = {}

    if not df_uso.empty:
        df_uso = df_uso.sort_values("Data")
        ultimos = df_uso.groupby("Item").last()
        ult_qtd = ultimos["Qtd"].to_dict()

    # =========================
    # SESSION STATE
    # =========================
    if "df_barrilete" not in st.session_state:

        df_init = df_insumos.copy()

        df_init["Qtd"] = df_init["Item"].map(ult_qtd).fillna(0)
        df_init["Preço Unitário"] = df_init["Preco_Atual"]

        st.session_state.df_barrilete = df_init[["Item", "Qtd", "Preço Unitário"]]

    # =========================
    # FORM
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
        # HISTÓRICO DE PREÇO
        # =========================
        try:
            df_hist_preco = carregar_github(ARQ_HIST_PRECO, TOKEN, REPO)
        except:
            df_hist_preco = pd.DataFrame(columns=["Item","Preco","Data"])

        novos_precos = []

        for _, row in df_novo.iterrows():

            item = row["Item"]
            preco_novo = float(row["Preço Unitário"])
            preco_antigo = float(df_antigo.get(item, 0))

            if preco_novo != preco_antigo:

                novos_precos.append({
                    "Item": item,
                    "Preco": preco_novo,
                    "Data": datetime.now().strftime("%d/%m/%Y %H:%M")
                })

                df_insumos.loc[df_insumos["Item"] == item, "Preco_Atual"] = preco_novo

        if novos_precos:
            df_hist_preco = pd.concat(
                [df_hist_preco, pd.DataFrame(novos_precos)],
                ignore_index=True
            )
            salvar_github(df_hist_preco, ARQ_HIST_PRECO, TOKEN, REPO)

        salvar_github(df_insumos, ARQ_INSUMOS, TOKEN, REPO)

        # =========================
        # HISTÓRICO DE USO (QTD)
        # =========================
        novos_usos = []

        obra = st.session_state.orcamento.get("codigo", "SEM_OBRA")

        for _, row in df_novo.iterrows():

            if row["Qtd"] > 0:
                novos_usos.append({
                    "Item": row["Item"],
                    "Qtd": row["Qtd"],
                    "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "Obra": obra
                })

        if novos_usos:
            df_uso = pd.concat(
                [df_uso, pd.DataFrame(novos_usos)],
                ignore_index=True
            )
            salvar_github(df_uso, ARQ_HIST_USO, TOKEN, REPO)

        # =========================
        # CÁLCULO
        # =========================
        df_novo["Total"] = df_novo["Qtd"] * df_novo["Preço Unitário"]

        df_display = df_novo[df_novo["Qtd"] > 0].copy()
        total_materiais = df_novo["Total"].sum()

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

        total_geral = total_materiais + custo_total_equipe

        st.subheader("Resumo")

        st.write(f"Insumos: R$ {formatar_real(total_materiais)}")
        st.write(f"Mão de obra: R$ {formatar_real(custo_total_equipe)}")

        st.success(f"TOTAL GERAL: R$ {formatar_real(total_geral)}")
