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
    # CARREGAR BASE
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
    # BASE
    # =========================
    df = df_sal.copy()

    if "equipe" in st.session_state.orcamento:
        df_antigo = pd.DataFrame(st.session_state.orcamento["equipe"])
        for i in range(min(len(df), len(df_antigo))):
            df.loc[i, "Qtd"] = df_antigo.loc[i, "Qtd"]
            df.loc[i, "Adicional 25%"] = df_antigo.loc[i, "Adicional 25%"]
    else:
        df["Qtd"] = 0
        df["Adicional 25%"] = False

    # =========================
    # INPUT
    # =========================
    st.subheader("Entrada de Dados")

    df_editado = st.data_editor(
        df[
            [
                "Qtd",
                "Posicao",
                "Valor_Hora",
                "Adicional 25%"
            ]
        ],
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
        column_config={
            "Qtd": st.column_config.NumberColumn("Qtd", min_value=0, step=1),
            "Posicao": st.column_config.TextColumn("Posição", disabled=True),
            "Valor_Hora": st.column_config.NumberColumn("Valor Hora (R$)", disabled=True),
            "Adicional 25%": st.column_config.CheckboxColumn("Adic. 25%"),
        },
        key="editor_equipe"
    )

    # =========================
    # CÁLCULOS
    # =========================
    df_calc = df_editado.copy()

    # ENCARGOS (SEPARADO)
    df_calc["Encargos"] = df_calc["Valor_Hora"] * (leis / 100)

    # BASE + ENCARGOS
    df_calc["Base + Encargos"] = df_calc["Valor_Hora"] + df_calc["Encargos"]

    # VALOR DO 25% (SEPARADO)
    df_calc["Valor 25%"] = df_calc["Base + Encargos"] * 0.25

    # VALOR FINAL
    df_calc["Valor Final"] = df_calc.apply(
        lambda row: row["Base + Encargos"] + row["Valor 25%"]
        if row["Adicional 25%"]
        else row["Base + Encargos"],
        axis=1
    )

    # TOTAL
    df_calc["Total"] = df_calc["Qtd"] * df_calc["Valor Final"]

    total_hora = df_calc["Total"].sum()

    # =========================
    # ALERTA
    # =========================
    if df_calc["Adicional 25%"].any():
        st.warning("⚠️ Adicional de 25% aplicado")

    # =========================
    # FORMATAR VISUAL
    # =========================
    df_display = df_calc.copy()

    for col in ["Valor_Hora", "Encargos", "Valor 25%", "Valor Final", "Total"]:
        df_display[col] = df_display[col].apply(formatar_real)

    # =========================
    # RESULTADO FINAL
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
                "Valor Final",
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
