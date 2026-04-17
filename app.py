import streamlit as st
import pandas as pd
from datetime import datetime

from services.github import salvar_github, carregar_github

st.set_page_config(layout="wide")
st.title("FOS ENGENHARIA LTDA")

# =========================
# ARQUIVOS
# =========================
ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"
ARQ_HOR = "data/horarios.csv"
ARQ_DIAS = "data/dias.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# ESTADO
# =========================
if "tela" not in st.session_state:
    st.session_state.tela = "menu"

# =========================
# MENU PRINCIPAL
# =========================
if st.session_state.tela == "menu":

    col1, col2, col3 = st.columns(3)

    if col1.button("📊 ORÇAMENTO", use_container_width=True):
        st.session_state.tela = "orcamento"

    if col2.button("🚜 EQUIPAMENTOS", use_container_width=True):
        st.session_state.tela = "equip"

    if col3.button("📁 DADOS", use_container_width=True):
        st.session_state.tela = "dados"

# =========================
# DADOS MENU
# =========================
elif st.session_state.tela == "dados":

    st.header("Dados do Sistema")

    col1, col2 = st.columns(2)

    if col1.button("Materiais"):
        st.session_state.tela = "dados_mat"

    if col1.button("Desaguamento"):
        st.session_state.tela = "dados_desag"

    if col2.button("Horários"):
        st.session_state.tela = "dados_hor"

    if col2.button("Dias de Trabalho"):
        st.session_state.tela = "dados_dias"

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# CRUD GENÉRICO SIMPLES
# =========================
def tela_crud(arquivo, colunas, titulo):

    st.header(titulo)

    df = carregar_github(arquivo, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=colunas)

    st.dataframe(df)

    st.divider()

    valores = []
    for c in colunas:
        valores.append(st.text_input(c))

    if st.button("Adicionar"):
        novo = pd.DataFrame([valores], columns=colunas)
        df = pd.concat([df, novo], ignore_index=True)
        salvar_github(df, arquivo, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "dados"

# =========================
# TELAS DADOS
# =========================
elif st.session_state.tela == "dados_mat":
    tela_crud(ARQ_MAT, ["Material","Solidos_InSitu","Solidos_Desaguado"], "Materiais")

elif st.session_state.tela == "dados_desag":
    tela_crud(ARQ_DESAG, ["Tipo"], "Tipos de Desaguamento")

elif st.session_state.tela == "dados_hor":
    tela_crud(ARQ_HOR, ["Inicio","Fim"], "Horários de Trabalho")

elif st.session_state.tela == "dados_dias":
    tela_crud(ARQ_DIAS, ["Descricao"], "Dias de Trabalho")

# =========================
# EQUIPAMENTOS
# =========================
elif st.session_state.tela == "equip":

    df = carregar_github(ARQ_EQUIP, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Equipamento","Vazao","Consumo","Valor"])

    st.dataframe(df)

    nome = st.text_input("Nome")
    vazao = st.number_input("Vazão", value=1000.0)
    consumo = st.number_input("Consumo", value=60.0)
    valor = st.number_input("Valor", value=1000000.0)

    if st.button("Adicionar"):
        novo = pd.DataFrame([[nome, vazao, consumo, valor]], columns=df.columns)
        df = pd.concat([df, novo], ignore_index=True)
        salvar_github(df, ARQ_EQUIP, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# ORÇAMENTO - TELA 1 COMPLETA
# =========================
elif st.session_state.tela == "orcamento":

    st.header("Orçamento - Etapa 1")

    df_equip = carregar_github(ARQ_EQUIP, TOKEN, REPO)
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)
    df_desag = carregar_github(ARQ_DESAG, TOKEN, REPO)
    df_hor = carregar_github(ARQ_HOR, TOKEN, REPO)
    df_dias = carregar_github(ARQ_DIAS, TOKEN, REPO)

    # DRAGA
    draga = st.selectbox("Informe a draga", df_equip["Equipamento"])
    dados = df_equip[df_equip["Equipamento"] == draga].iloc[0]
    vazao_padrao = float(dados["Vazao"])

    if "vazao_input" not in st.session_state:
        st.session_state.vazao_input = vazao_padrao

    if st.session_state.get("ultima_draga") != draga:
        st.session_state.vazao_input = vazao_padrao
        st.session_state.ultima_draga = draga

    vazao = st.number_input("Vazão (m³/h)", value=st.session_state.vazao_input)

    if vazao != vazao_padrao:
        st.warning("* valor alterado manualmente")

    # VOLUME
    volume = st.number_input("Volume a ser dragado (m³)")

    # MATERIAL
    material = st.selectbox("Tipo de material", df_mat["Material"])

    # DISTÂNCIA
    st.subheader("Distância de recalque")
    col1, col2 = st.columns(2)
    flutuante = col1.number_input("Linha flutuante (m)")
    terrestre = col2.number_input("Linha terrestre (m)")

    # PROFUNDIDADE
    profundidade = st.number_input("Profundidade (m)")

    # ESPESSURA
    espessura = st.number_input("Espessura média de corte (m)")

    # DESAGUAMENTO
    desag = st.selectbox("Tipo de desaguamento", df_desag["Tipo"])

    # HORARIO
    horario = st.selectbox("Horário de trabalho", df_hor.apply(lambda x: f"{x['Inicio']} - {x['Fim']}", axis=1))

    # DIAS
    dias = st.selectbox("Dias de trabalho", df_dias["Descricao"])

    if st.button("Continuar"):
        st.success("Dados capturados")

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
