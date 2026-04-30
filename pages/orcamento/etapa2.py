import json
import streamlit as st
import pandas as pd
from datetime import datetime
from services.github import carregar_github, salvar_github

ARQ_SAL = "data/salarios.csv"
ARQ_OBRAS = "data/orcamentos.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]


# =========================
# FORMATADOR BR
# =========================
def formatar_real(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# =========================
# SALVAR RASCUNHO (CORRIGIDO)
# =========================
def salvar_rascunho_orcamento(dados):

    try:
        df = carregar_github(ARQ_OBRAS, TOKEN, REPO)
    except:
        df = pd.DataFrame()

    if df.empty:
        df = pd.DataFrame()

    # 🔥 CORREÇÃO CRÍTICA (resolve pyarrow bug)
    df = df.astype("object")

    codigo = dados.get("Codigo")

    if not codigo:
        st.error("Código não encontrado.")
        st.stop()

    dados_limpos = {}

    for k, v in dados.items():

        if isinstance(v, (list, dict)):
            v = json.dumps(v, ensure_ascii=False, default=str)

        elif isinstance(v, (pd.Timestamp, datetime)):
            v = v.strftime("%Y-%m-%d %H:%M:%S")

        elif pd.isna(v):
            v = ""

        dados_limpos[k] = v

    if "Codigo" in df.columns and str(codigo) in df["Codigo"].astype(str).values:

        idx = df[df["Codigo"].astype(str) == str(codigo)].index[0]

        for k, v in dados_limpos.items():

            if k not in df.columns:
                df[k] = ""

            df[k] = df[k].astype("object")

            df.at[idx, k] = v

    else:
        df = pd.concat([df, pd.DataFrame([dados_limpos])], ignore_index=True)

    salvar_github(df, ARQ_OBRAS, TOKEN, REPO)


# =========================
# PREPARAR DF
# =========================
def preparar_df(df):

    df = df.copy()

    if "Qtd" not in df.columns:
        df["Qtd"] = 0

    if "Adicional 25%" not in df.columns:
        df["Adicional 25%"] = False

    df["Qtd"] = pd.to_numeric(df["Qtd"], errors="coerce").fillna(0).astype(int)
    df["Valor_Hora"] = pd.to_numeric(df["Valor_Hora"], errors="coerce").fillna(0)
    df["Adicional 25%"] = df["Adicional 25%"].fillna(False)

    return df


# =========================
# RECONSTRUIR EQUIPE
# =========================
def carregar_equipe(dados, df_sal):

    if dados.get("Equipe_JSON"):

        try:
            df = pd.DataFrame(json.loads(dados["Equipe_JSON"]))

            if not df.empty:
                return preparar_df(df)

        except:
            pass

    df = df_sal.copy()
    df["Qtd"] = 0
    df["Adicional 25%"] = False

    return preparar_df(df)


# =========================
# CALCULAR
# =========================
def calcular(df, leis):

    df = preparar_df(df)

    df["Encargos"] = df["Valor_Hora"] * (leis / 100)
    df["Base + Encargos"] = df["Valor_Hora"] + df["Encargos"]
    df["Valor 25%"] = df["Base + Encargos"] * 0.25

    df["Valor Final"] = df.apply(
        lambda r: r["Base + Encargos"] + r["Valor 25%"]
        if r["Adicional 25%"]
        else r["Base + Encargos"],
        axis=1,
    )

    df["Total"] = df["Qtd"] * df["Valor Final"]

    return df, df["Total"].sum()


# =========================
# ETAPA 2
# =========================
def etapa2():

    st.header("Dimensionamento de Equipe")

    if "orcamento" not in st.session_state:
        st.warning("Volte para a etapa anterior.")
        return

    dados = st.session_state.orcamento

    # =========================
    # BASE
    # =========================
    df_sal = carregar_github(ARQ_SAL, TOKEN, REPO)

    if df_sal.empty:
        st.warning("Base de salários vazia.")
        return

    df_sal = preparar_df(df_sal)

    # =========================
    # LEIS
    # =========================
    leis = st.number_input(
        "Leis Sociais (%)",
        value=float(dados.get("Leis_Sociais", 110)),
        key="leis_etapa2"
    )

    st.info(f"Encargos: {leis:.1f}%")

    # =========================
    # SESSION STATE
    # =========================
    codigo = dados.get("Codigo")
    chave = f"equipe_{codigo}"

    if chave not in st.session_state:
        st.session_state[chave] = carregar_equipe(dados, df_sal)

    # =========================
    # EDITOR
    # =========================
    with st.form("form"):

        df_editado = st.data_editor(
            st.session_state[chave],
            key=f"editor_{codigo}",
            use_container_width=True,
            hide_index=True,
        )

        calcular_btn = st.form_submit_button("Calcular")

    # =========================
    # CÁLCULO
    # =========================
    if calcular_btn:

        st.session_state[chave] = preparar_df(df_editado)

        df_calc, total = calcular(st.session_state[chave], leis)

        df_vis = df_calc[df_calc["Qtd"] > 0]

        if not df_vis.empty:

            st.subheader("Resultado")

            for col in ["Valor_Hora", "Encargos", "Valor 25%", "Valor Final", "Total"]:
                df_vis[col] = df_vis[col].apply(formatar_real)

            st.dataframe(df_vis, use_container_width=True)

            st.success(f"Custo/hora: R$ {formatar_real(total)}")

        # =========================
        # SALVAR
        # =========================
        st.session_state.orcamento.update({
            "Equipe_JSON": json.dumps(df_calc.to_dict("records"), ensure_ascii=False),
            "Custo_Hora_Equipe": total,
            "Leis_Sociais": leis,
            "Etapa_Atual": "Etapa 2",
            "Ultima_Atualizacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

        salvar_rascunho_orcamento(st.session_state.orcamento)

        st.success("Salvo com sucesso.")

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
