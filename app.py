import streamlit as st
import pandas as pd
from datetime import datetime

from services.github import salvar_github, carregar_github
from services.codigos import gerar_codigo_obra
from services.calculos import *

st.set_page_config(layout="wide")

# =========================
# ESTILO (CSS)
# =========================
st.markdown("""
<style>
.card {
    padding: 30px;
    border-radius: 15px;
    background-color: #1f2937;
    color: white;
    text-align: center;
    font-size: 20px;
    transition: 0.3s;
}
.card:hover {
    background-color: #374151;
    transform: scale(1.03);
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

    st.header("Orçamento")

    df = carregar_github(ARQUIVO_EQUIP, TOKEN, REPO)

    if df.empty:
        st.warning("Cadastre equipamentos primeiro!")
    else:

        equipamento = st.selectbox("Equipamento", df["Equipamento"])
        eq = df[df["Equipamento"] == equipamento].iloc[0]

        df_orc = carregar_github(ARQUIVO_ORC, TOKEN, REPO)
        codigo = gerar_codigo_obra(df_orc)

        st.info(f"Código: {codigo}")

        descricao = st.text_input("Descrição")

        volume = st.number_input("Volume", value=10000.0)
        distancia = st.number_input("Distância", value=2000.0)
        preco = st.number_input("Preço", value=16.18)
        horas = st.number_input("Horas/dia", value=20)

        if st.button("Calcular"):

            prod = calcular_producao(eq["Vazao"], distancia)
            tempo = calcular_tempo(volume, prod)
            dias = calcular_dias(tempo, horas)

            custo = calcular_diesel(eq["Consumo"], tempo, 6)
            receita = calcular_receita(volume, preco)
            lucro = calcular_lucro(receita, custo)

            st.write(f"Lucro: R$ {lucro:,.0f}")

            if st.button("Salvar"):
                df_orc = carregar_github(ARQUIVO_ORC, TOKEN, REPO)

                if df_orc.empty:
                    df_orc = pd.DataFrame(columns=[
                        "Codigo","Data","Descricao","Equipamento",
                        "Volume","Distancia","Produtividade","Tempo_h",
                        "Dias","Custo_Diesel","Receita","Lucro"
                    ])

                novo = pd.DataFrame([[
                    codigo, datetime.now(), descricao, equipamento,
                    volume, distancia, prod, tempo,
                    dias, custo, receita, lucro
                ]], columns=df_orc.columns)

                df_orc = pd.concat([df_orc, novo], ignore_index=True)

                salvar_github(df_orc, ARQUIVO_ORC, TOKEN, REPO)

                st.success("Salvo!")

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# EQUIPAMENTOS
# =========================
elif st.session_state.tela == "equip":

    st.header("Equipamentos")

    df = carregar_github(ARQUIVO_EQUIP, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Equipamento", "Vazao", "Consumo", "Valor"])

    st.dataframe(df)

    nome = st.text_input("Nome")
    vazao = st.number_input("Vazão", value=1000.0)
    consumo = st.number_input("Consumo", value=60.0)
    valor = st.number_input("Valor", value=1000000.0)

    if st.button("Adicionar"):
        novo = pd.DataFrame([[nome, vazao, consumo, valor]], columns=df.columns)
        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_EQUIP, TOKEN, REPO)
        st.success("Salvo!")

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# FÉRIAS
# =========================
elif st.session_state.tela == "ferias":

    st.header("Férias")

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

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# OBRAS
# =========================
elif st.session_state.tela == "obras":

    st.header("Histórico")

    df = carregar_github(ARQUIVO_ORC, TOKEN, REPO)

    if not df.empty:
        st.dataframe(df)

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
