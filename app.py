import streamlit as st
import pandas as pd
from datetime import datetime

from services.github import salvar_github, carregar_github
from services.codigos import gerar_codigo_obra
from services.calculos import *

st.set_page_config(layout="wide")

# =========================
# ESTILO
# =========================
st.markdown("""
<style>
button[kind="secondary"] {
    height: 80px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.title("FOS ENGENHARIA LTDA")

# =========================
# CONFIG
# =========================
ARQUIVO_EQUIP = "data/equipamentos.csv"
ARQUIVO_ORC = "data/orcamentos.csv"
ARQUIVO_FERIAS = "data/ferias.csv"
ARQUIVO_SALARIOS = "data/salarios.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# ESTADO
# =========================
if "tela" not in st.session_state:
    st.session_state.tela = "menu"

# =========================
# MENU DASHBOARD
# =========================
if st.session_state.tela == "menu":

    st.subheader("Selecione uma opção")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📊 ORÇAMENTO", use_container_width=True):
            st.session_state.tela = "orcamento"

        if st.button("📅 FÉRIAS", use_container_width=True):
            st.session_state.tela = "ferias"

    with col2:
        if st.button("🚜 EQUIPAMENTOS", use_container_width=True):
            st.session_state.tela = "equip"

        if st.button("💰 SALÁRIOS", use_container_width=True):
            st.session_state.tela = "salarios"

    with col3:
        if st.button("📈 OBRAS", use_container_width=True):
            st.session_state.tela = "obras"

# =========================
# ORÇAMENTO
# =========================
elif st.session_state.tela == "orcamento":

    st.header("Orçamento - Etapa 1")

    df = carregar_github(ARQUIVO_EQUIP, TOKEN, REPO)

    if df.empty:
        st.warning("Cadastre equipamentos primeiro!")
    else:

        draga = st.selectbox("Informe a draga", df["Equipamento"])
        dados = df[df["Equipamento"] == draga].iloc[0]

        vazao_padrao = float(dados["Vazao"])

        if "vazao_input" not in st.session_state:
            st.session_state.vazao_input = vazao_padrao

        if st.session_state.get("ultima_draga") != draga:
            st.session_state.vazao_input = vazao_padrao
            st.session_state.ultima_draga = draga

        vazao = st.number_input("Vazão (m³/h)", value=st.session_state.vazao_input, key="vazao_input")

        if vazao != vazao_padrao:
            st.warning("* valor alterado manualmente")

        if st.button("Continuar"):
            st.session_state.draga = draga
            st.session_state.vazao_final = vazao
            st.success("Dados salvos")

        if st.button("⬅ Voltar"):
            st.session_state.tela = "menu"

# =========================
# EQUIPAMENTOS - TELA 1
# =========================
elif st.session_state.tela == "equip":

    st.header("Equipamentos")

    df = carregar_github(ARQUIVO_EQUIP, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Equipamento", "Vazao", "Consumo", "Valor"])

    st.dataframe(df)

    st.divider()

    # BOTÃO PARA IR PARA EDIÇÃO
    if st.button("✏️ Atualizar equipamento"):
        st.session_state.tela = "equip_edit"

    st.divider()

    # NOVO EQUIPAMENTO
    st.subheader("Novo equipamento")

    nome = st.text_input("Nome")
    vazao = st.number_input("Vazão", value=1000.0)
    consumo = st.number_input("Consumo", value=60.0)
    valor = st.number_input("Valor", value=1000000.0)

    if st.button("Adicionar"):
        novo = pd.DataFrame([[nome, vazao, consumo, valor]], columns=df.columns)
        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_EQUIP, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# EQUIPAMENTOS - TELA 2 (EDIÇÃO)
# =========================
elif st.session_state.tela == "equip_edit":

    st.header("Atualizar Equipamento")

    df = carregar_github(ARQUIVO_EQUIP, TOKEN, REPO)

    if df.empty:
        st.warning("Sem equipamentos cadastrados")
    else:

        sel = st.selectbox("Selecione o equipamento", df["Equipamento"])
        linha = df[df["Equipamento"] == sel].iloc[0]

        nome = st.text_input("Nome", value=linha["Equipamento"])
        vazao = st.number_input("Vazão", value=float(linha["Vazao"]))
        consumo = st.number_input("Consumo", value=float(linha["Consumo"]))
        valor = st.number_input("Valor", value=float(linha["Valor"]))

        col1, col2 = st.columns(2)

        if col1.button("Salvar alteração"):
            idx = df["Equipamento"] == sel

            df.loc[idx, "Equipamento"] = nome
            df.loc[idx, "Vazao"] = vazao
            df.loc[idx, "Consumo"] = consumo
            df.loc[idx, "Valor"] = valor

            salvar_github(df, ARQUIVO_EQUIP, TOKEN, REPO)
            st.success("Atualizado!")
            st.rerun()

        if col2.button("Excluir equipamento"):
            df = df[df["Equipamento"] != sel]

            salvar_github(df, ARQUIVO_EQUIP, TOKEN, REPO)
            st.warning("Removido!")
            st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "equip"

# =========================
# FÉRIAS
# =========================
elif st.session_state.tela == "ferias":

    st.header("Férias e Folgas")

    df = carregar_github(ARQUIVO_FERIAS, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Funcionario","Data_Inicio","Data_Fim","Tipo"])

    st.dataframe(df)

    nome = st.text_input("Funcionário")
    data_inicio = st.date_input("Data início")
    data_fim = st.date_input("Data fim")
    tipo = st.selectbox("Tipo", ["Férias", "Folga"])

    if st.button("Salvar"):
        novo = pd.DataFrame([[nome, data_inicio, data_fim, tipo]], columns=df.columns)
        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_FERIAS, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# SALÁRIOS
# =========================
elif st.session_state.tela == "salarios":

    st.header("Salários")

    df = carregar_github(ARQUIVO_SALARIOS, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Cargo", "Valor_Hora"])

    st.dataframe(df)

    cargo = st.text_input("Cargo")
    valor = st.number_input("Valor/hora", value=20.0)

    if st.button("Salvar"):
        novo = pd.DataFrame([[cargo, valor]], columns=df.columns)
        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_SALARIOS, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# OBRAS
# =========================
elif st.session_state.tela == "obras":

    st.header("Histórico de Obras")

    df = carregar_github(ARQUIVO_ORC, TOKEN, REPO)

    if not df.empty:
        st.dataframe(df)

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
