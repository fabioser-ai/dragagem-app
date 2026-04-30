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
# SALVAR RASCUNHO
# =========================
def salvar_rascunho_orcamento(dados):
    try:
        df = carregar_github(ARQ_OBRAS, TOKEN, REPO)
    except Exception:
        df = pd.DataFrame()

    if df.empty:
        df = pd.DataFrame()

    codigo = dados.get("Codigo")

    if not codigo:
        st.error("Código do orçamento não encontrado. Volte para a Etapa 0.")
        st.stop()

    if "Codigo" in df.columns and codigo in df["Codigo"].astype(str).values:
        idx = df[df["Codigo"].astype(str) == str(codigo)].index[0]

        for k, v in dados.items():

    # 🔥 correção crítica
    if isinstance(v, (list, dict)):
        v = json.dumps(v, ensure_ascii=False)

    df.loc[idx, k] = v
    
    else:
        df = pd.concat([df, pd.DataFrame([dados])], ignore_index=True)

    salvar_github(df, ARQ_OBRAS, TOKEN, REPO)


# =========================
# RECONSTRUIR EQUIPE SALVA
# =========================
def carregar_equipe_salva(dados, df_sal):
    equipe_json = dados.get("Equipe_JSON", "")

    if equipe_json:
        try:
            equipe = json.loads(equipe_json)
            df = pd.DataFrame(equipe)

            if not df.empty:
                return df
        except Exception:
            pass

    df_inicial = df_sal.copy()
    df_inicial["Qtd"] = 0
    df_inicial["Adicional 25%"] = False

    return df_inicial


# =========================
# CALCULAR EQUIPE
# =========================
def calcular_equipe(df_editado, leis):
    df_calc = df_editado.copy()

    df_calc["Qtd"] = pd.to_numeric(df_calc["Qtd"], errors="coerce").fillna(0)
    df_calc["Valor_Hora"] = pd.to_numeric(df_calc["Valor_Hora"], errors="coerce").fillna(0)

    df_calc["Encargos"] = df_calc["Valor_Hora"] * (leis / 100)
    df_calc["Base + Encargos"] = df_calc["Valor_Hora"] + df_calc["Encargos"]
    df_calc["Valor 25%"] = df_calc["Base + Encargos"] * 0.25

    df_calc["Valor Final"] = df_calc.apply(
        lambda row: row["Base + Encargos"] + row["Valor 25%"]
        if row["Adicional 25%"]
        else row["Base + Encargos"],
        axis=1,
    )

    df_calc["Total"] = df_calc["Qtd"] * df_calc["Valor Final"]

    total_hora = df_calc["Total"].sum()

    return df_calc, total_hora


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
    # CARREGAR SALÁRIOS
    # =========================
    df_sal = carregar_github(ARQ_SAL, TOKEN, REPO)

    if df_sal.empty:
        st.warning("Base de salários vazia.")
        return

    df_sal["Valor_Hora"] = pd.to_numeric(df_sal["Valor_Hora"], errors="coerce").fillna(0)

    # =========================
    # LEIS SOCIAIS
    # =========================
    leis_salvas = float(dados.get("Leis_Sociais", dados.get("leis_sociais", 110.0)) or 110.0)

    leis = st.number_input(
        "Leis Sociais (%)",
        value=leis_salvas,
        key="leis_sociais_etapa2",
    )

    st.info(f"Encargos aplicados: {leis:.1f}%")

    # =========================
    # SESSION STATE
    # =========================
    codigo = dados.get("Codigo", "sem_codigo")
    chave_equipe = f"df_equipe_{codigo}"

    if chave_equipe not in st.session_state:
        st.session_state[chave_equipe] = carregar_equipe_salva(dados, df_sal)

    # =========================
    # FORM
    # =========================
    st.subheader("Entrada de Dados")

    with st.form("form_equipe"):

        df_editado = st.data_editor(
            st.session_state[chave_equipe],
            use_container_width=True,
            hide_index=True,
            num_rows="fixed",
            column_config={
                "Qtd": st.column_config.NumberColumn("Qtd", min_value=0, step=1),
                "Posicao": st.column_config.TextColumn("Posição", disabled=True),
                "Valor_Hora": st.column_config.NumberColumn("Valor Hora (R$)", disabled=True),
                "Adicional 25%": st.column_config.CheckboxColumn("Adic. 25%"),
            },
        )

        calcular = st.form_submit_button("Calcular e salvar equipe")

    # =========================
    # CÁLCULO
    # =========================
    if calcular:

        st.session_state[chave_equipe] = df_editado.copy()

        df_calc, total_hora = calcular_equipe(df_editado, leis)

        df_display = df_calc[df_calc["Qtd"] > 0].copy()

        if df_display.empty:
            st.info("Nenhum funcionário selecionado.")
        else:
            if df_display["Adicional 25%"].any():
                st.warning("⚠️ Adicional de 25% aplicado.")

            for col in ["Valor_Hora", "Encargos", "Valor 25%", "Valor Final", "Total"]:
                df_display[col] = df_display[col].apply(formatar_real)

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
                hide_index=True,
            )

            st.success(f"Custo por hora da equipe: R$ {formatar_real(total_hora)}")

        equipe_json = json.dumps(df_calc.to_dict(orient="records"), ensure_ascii=False, default=str)

        dados_atualizados = {
            "Equipe_JSON": equipe_json,
            "Custo_Hora_Equipe": total_hora,
            "Leis_Sociais": leis,
            "Status": "Rascunho",
            "Etapa_Atual": "Etapa 2",
            "Ultima_Atualizacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            # Compatibilidade com etapas antigas
            "equipe": df_calc.to_dict(orient="records"),
            "custo_hora_equipe": total_hora,
            "custo_mensal_equipe": total_hora,
            "leis_sociais": leis,
        }

        st.session_state.orcamento.update(dados_atualizados)

        salvar_rascunho_orcamento(st.session_state.orcamento)

        st.success("Equipe salva no orçamento.")

    # =========================
    # RESUMO SALVO
    # =========================
    custo_salvo = dados.get("Custo_Hora_Equipe", dados.get("custo_hora_equipe", None))

    if custo_salvo is not None:
        try:
            st.info(f"Custo por hora salvo: R$ {formatar_real(float(custo_salvo))}")
        except Exception:
            pass

    # =========================
    # NAVEGAÇÃO
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar", key="voltar_etapa2"):
        st.session_state.tela = "orcamento1"
        st.rerun()

    if col2.button("Salvar e continuar", key="continuar_etapa2"):
        if "Custo_Hora_Equipe" not in st.session_state.orcamento and "custo_hora_equipe" not in st.session_state.orcamento:
            st.warning("Calcule e salve a equipe antes de continuar.")
        else:
            st.session_state.orcamento["Etapa_Atual"] = "Etapa 2"
            st.session_state.orcamento["Ultima_Atualizacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            salvar_rascunho_orcamento(st.session_state.orcamento)

            st.session_state.tela = "orcamento3"
            st.rerun()
