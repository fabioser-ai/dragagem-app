import streamlit as st
import pandas as pd
from services.github import carregar_github

ARQ_SAL = "data/salarios.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# FORMATADOR BR
# =========================
def formatar_real(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# =========================
# ETAPA 2
# =========================
def etapa2():

    st.header("Dimensionamento de Equipe")

    if "orcamento" not in st.session_state:
        st.warning("Volte para a etapa anterior.")
        return

    # =========================
    # CARREGAR SALÁRIOS
    # =========================
    df_sal = carregar_github(ARQ_SAL, TOKEN, REPO)

    if df_sal.empty:
        st.warning("Base de salários vazia")
        return

    df_sal["Valor_Hora"] = pd.to_numeric(df_sal["Valor_Hora"], errors="coerce").fillna(0)

    # =========================
    # LEIS SOCIAIS
    # =========================
    leis = st.number_input("Leis Sociais (%)", value=110.0)
    st.info(f"Encargos aplicados: {leis:.1f}%")

    # =========================
    # SESSION STATE
    # =========================
    if "df_equipe" not in st.session_state:
        df_inicial = df_sal.copy()
        df_inicial["Qtd"] = 0
        df_inicial["Adicional 25%"] = False
        st.session_state.df_equipe = df_inicial

    # =========================
    # FORM (ANTI-RERUN)
    # =========================
    st.subheader("Entrada de Dados")

    with st.form("form_equipe"):

        df_editado = st.data_editor(
            st.session_state.df_equipe,
            use_container_width=True,
            hide_index=True,
            num_rows="fixed",
            column_config={
                "Qtd": st.column_config.NumberColumn("Qtd", min_value=0, step=1),
                "Posicao": st.column_config.TextColumn("Posição", disabled=True),
                "Valor_Hora": st.column_config.NumberColumn("Valor Hora (R$)", disabled=True),
                "Adicional 25%": st.column_config.CheckboxColumn("Adic. 25%"),
            }
        )

        calcular = st.form_submit_button("Calcular custos")

    # =========================
    # CÁLCULO
    # =========================
    if calcular:

        st.session_state.df_equipe = df_editado.copy()

        df_calc = df_editado.copy()

        # cálculos
        df_calc["Encargos"] = df_calc["Valor_Hora"] * (leis / 100)
        df_calc["Base + Encargos"] = df_calc["Valor_Hora"] + df_calc["Encargos"]
        df_calc["Valor 25%"] = df_calc["Base + Encargos"] * 0.25

        df_calc["Valor Final"] = df_calc.apply(
            lambda row: row["Base + Encargos"] + row["Valor 25%"]
            if row["Adicional 25%"]
            else row["Base + Encargos"],
            axis=1
        )

        df_calc["Total"] = df_calc["Qtd"] * df_calc["Valor Final"]

        total_hora = df_calc["Total"].sum()

        # =========================
        # FILTRO (Qtd > 0)
        # =========================
        df_display = df_calc[df_calc["Qtd"] > 0].copy()

        if df_display.empty:
            st.info("Nenhum funcionário selecionado.")
            return

        # alerta
        if df_display["Adicional 25%"].any():
            st.warning("⚠️ Adicional de 25% aplicado")

        # formatação BR
        for col in ["Valor_Hora", "Encargos", "Valor 25%", "Total"]:
            df_display[col] = df_display[col].apply(formatar_real)

        # =========================
        # RESULTADO
        # =========================
        st.subheader("Resultado Calculado")

        st.dataframe(
            df_display[
                [
                    "Qtd",
                    "Posicao",
                    "Valor_Hora",
                    "Encargos",
                    "Valor 25%",
                    "Total",
                ]
            ],
            use_container_width=True,
            hide_index=True
        )

        st.success(f"Custo por hora da equipe: R$ {formatar_real(total_hora)}")

        # =========================
        # SALVAR
        # =========================
        st.session_state.orcamento.update({
            "equipe": df_calc.to_dict(orient="records"),
            "custo_hora_equipe": total_hora,
            "leis_sociais": leis
        })

    # =========================
    # NAVEGAÇÃO
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento1"
        st.rerun()

    if col2.button("Continuar"):
        st.session_state.tela = "orcamento3"
        st.rerun()
