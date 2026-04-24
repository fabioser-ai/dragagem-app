import streamlit as st
import pandas as pd
from services.github import carregar_github

ARQ_SAL = "data/salarios.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

def formatar_real(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def etapa2():

    st.header("Dimensionamento de Equipe")

    if "orcamento" not in st.session_state:
        st.warning("Volte para a etapa anterior.")
        return

    df_sal = carregar_github(ARQ_SAL, TOKEN, REPO)

    if df_sal.empty:
        st.warning("Base de salários vazia")
        return

    df_sal["Valor_Hora"] = pd.to_numeric(df_sal["Valor_Hora"], errors="coerce").fillna(0)

    # =========================
    # LEIS SOCIAIS
    # =========================
    leis = st.number_input("Leis Sociais (%)", value=110.0)
    fator_leis = 1 + leis / 100

    st.info(f"Fator aplicado: {fator_leis:.2f}")

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

    # ✔ CORREÇÃO PRINCIPAL AQUI
    df["Valor c/ Leis"] = df["Valor_Hora"] * fator_leis

    # =========================
    # INPUT
    # =========================
    st.subheader("Entrada de Dados")

    df_editado = st.data_editor(
        df[["Qtd", "Posicao", "Valor_Hora", "Adicional 25%", "Valor c/ Leis"]],
        use_container_width=True,
        num_rows="fixed",
        hide_index=True,
        column_config={
            "Qtd": st.column_config.NumberColumn("Qtd", min_value=0, step=1),
            "Posicao": st.column_config.TextColumn("Posição", disabled=True),
            "Valor_Hora": st.column_config.NumberColumn("Valor Hora (R$)", disabled=True),
            "Adicional 25%": st.column_config.CheckboxColumn("Adic. 25%"),
            "Valor c/ Leis": st.column_config.NumberColumn("C/ Leis (R$)", disabled=True),
        },
        key="editor_equipe"
    )

    # =========================
    # CÁLCULO
    # =========================
    df_calc = df_editado.copy()

    df_calc["Fator_Adicional"] = df_calc["Adicional 25%"].apply(
        lambda x: 1.25 if x else 1.0
    )

    df_calc["Valor c/ 25%"] = df_calc["Valor c/ Leis"] * df_calc["Fator_Adicional"]

    df_calc["Total"] = df_calc["Qtd"] * df_calc["Valor c/ 25%"]

    total_hora = df_calc["Total"].sum()

    # =========================
    # ALERTA
    # =========================
    if df_calc["Adicional 25%"].any():
        st.warning("⚠️ Adicional de 25% aplicado em parte da equipe")

    # =========================
    # FORMATAÇÃO BR
    # =========================
    df_display = df_calc.copy()

    for col in ["Valor_Hora", "Valor c/ Leis", "Valor c/ 25%", "Total"]:
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
                "Adicional 25%",
                "Valor c/ Leis",
                "Valor c/ 25%",
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
