import streamlit as st
import pandas as pd
from services.github import carregar_github, salvar_github

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"
ARQ_HOR = "data/horarios.csv"
ARQ_DIAS = "data/dias.csv"

# =========================
# FUNÇÃO GENÉRICA
# =========================
def crud(arquivo, colunas, titulo, chave):
    st.subheader(titulo)

    df = carregar_github(arquivo, TOKEN, REPO)
    if df.empty:
        df = pd.DataFrame(columns=colunas)

    st.dataframe(df)

    # ===== EDITAR =====
    if not df.empty:
        idx = st.selectbox("Selecionar para editar", df.index, key=f"sel_{chave}")
        linha = df.loc[idx]

        novos = []
        for c in colunas:
            novos.append(
                st.text_input(c, value=str(linha[c]), key=f"{chave}_{c}")
            )

        col1, col2 = st.columns(2)

        if col1.button("Salvar", key=f"save_{chave}"):
            df.loc[idx] = novos
            salvar_github(df, arquivo, TOKEN, REPO)
            st.success("Atualizado!")
            st.rerun()

        if col2.button("Excluir", key=f"del_{chave}"):
            df = df.drop(idx).reset_index(drop=True)
            salvar_github(df, arquivo, TOKEN, REPO)
            st.warning("Removido!")
            st.rerun()

    st.divider()

    # ===== NOVO =====
    st.write("Adicionar novo")
    valores = [st.text_input(c, key=f"new_{chave}_{c}") for c in colunas]

    if st.button("Adicionar", key=f"add_{chave}"):
        df.loc[len(df)] = valores
        salvar_github(df, arquivo, TOKEN, REPO)
        st.success("Adicionado!")
        st.rerun()

# =========================
# TELA PRINCIPAL
# =========================
def render():

    st.title("Dados")

    col1, col2, col3 = st.columns(3)

    if col1.button("Equipamentos"):
        st.session_state.subdados = "equip"

    if col1.button("Materiais"):
        st.session_state.subdados = "mat"

    if col2.button("Desaguamento"):
        st.session_state.subdados = "desag"

    if col2.button("Horários"):
        st.session_state.subdados = "hor"

    if col3.button("Dias"):
        st.session_state.subdados = "dias"

    if "subdados" not in st.session_state:
        st.session_state.subdados = None

    st.divider()

    if st.session_state.subdados == "equip":
        crud(ARQ_EQUIP, ["Equipamento","Vazao","Consumo","Valor"], "Equipamentos", "equip")

    elif st.session_state.subdados == "mat":
        crud(ARQ_MAT, ["Material","Solidos_InSitu","Solidos_Desaguado"], "Materiais", "mat")

    elif st.session_state.subdados == "desag":
        crud(ARQ_DESAG, ["Tipo"], "Desaguamento", "desag")

    elif st.session_state.subdados == "hor":
        crud(ARQ_HOR, ["Inicio","Fim"], "Horários", "hor")

    elif st.session_state.subdados == "dias":
        crud(ARQ_DIAS, ["Descricao"], "Dias", "dias")

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
