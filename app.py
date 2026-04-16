import streamlit as st
import pandas as pd
import os
from datetime import datetime

from services.github import salvar_github
from services.codigos import gerar_codigo_obra
from services.calculos import *

st.title("FOS ENGENHARIA LTDA")

# =========================
# ESTADO
# =========================
if "etapa" not in st.session_state:
    st.session_state.etapa = 0

if "equipamento_sel" not in st.session_state:
    st.session_state.equipamento_sel = None

if "codigo_obra" not in st.session_state:
    st.session_state.codigo_obra = None

if "descricao_obra" not in st.session_state:
    st.session_state.descricao_obra = ""

# =========================
# ARQUIVOS
# =========================
ARQUIVO_FERIAS = "data/ferias.csv"
ARQUIVO_EQUIP = "data/equipamentos.csv"
ARQUIVO_ORC = "data/orcamentos.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# CRIAÇÃO DE ARQUIVOS
# =========================
if not os.path.exists(ARQUIVO_ORC):
    pd.DataFrame(columns=[
        "Codigo","Data","Descricao","Equipamento",
        "Volume","Distancia","Produtividade","Tempo_h",
        "Dias","Custo_Diesel","Receita","Lucro"
    ]).to_csv(ARQUIVO_ORC, index=False)

# =========================
# MENU
# =========================
if st.session_state.etapa == 0:

    st.header("Menu Principal")

    col1, col2, col3, col4, col5 = st.columns(5)

    if col1.button("📊 Orçamento"):
        st.session_state.etapa = 1

    if col2.button("⚙️ Base"):
        st.session_state.etapa = 100

    if col3.button("📅 Férias"):
        st.session_state.etapa = 200

    if col4.button("🚜 Equipamentos"):
        st.session_state.etapa = 300

    if col5.button("📈 Obras"):
        st.session_state.etapa = 400

# =========================
# DASHBOARD DE OBRAS
# =========================
elif st.session_state.etapa == 400:

    st.header("📈 Histórico de Obras")

    df = pd.read_csv(ARQUIVO_ORC)

    if df.empty:
        st.warning("Nenhuma obra registrada ainda")
    else:

        # Filtro
        equipamentos = ["Todos"] + list(df["Equipamento"].unique())
        filtro = st.selectbox("Filtrar por equipamento", equipamentos)

        if filtro != "Todos":
            df = df[df["Equipamento"] == filtro]

        st.dataframe(df)

        st.divider()

        # KPIs
        total_receita = df["Receita"].sum()
        total_lucro = df["Lucro"].sum()
        margem = (total_lucro / total_receita * 100) if total_receita > 0 else 0

        col1, col2, col3 = st.columns(3)

        col1.metric("Receita Total", f"R$ {total_receita:,.0f}")
        col2.metric("Lucro Total", f"R$ {total_lucro:,.0f}")
        col3.metric("Margem Média", f"{margem:.1f}%")

        st.divider()

        # Ranking
        st.subheader("🏆 Ranking de Equipamentos")

        ranking = df.groupby("Equipamento")["Lucro"].sum().sort_values(ascending=False)

        st.dataframe(ranking)

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# RESTO DO APP (SEM ALTERAÇÃO)
# =========================
elif st.session_state.etapa == 1:

    st.header("Selecionar Equipamento")

    df = pd.read_csv(ARQUIVO_EQUIP)

    equipamento = st.selectbox("Equipamento", df["Equipamento"])
    eq = df[df["Equipamento"] == equipamento].iloc[0]

    st.write(f"Vazão: {eq['Vazao']}")
    st.write(f"Consumo: {eq['Consumo']}")

    if st.button("Continuar"):
        st.session_state.equipamento_sel = equipamento
        st.session_state.etapa = 2

    if st.button("Voltar"):
        st.session_state.etapa = 0

elif st.session_state.etapa == 2:

    st.header("Parâmetros")

    df = pd.read_csv(ARQUIVO_EQUIP)
    equipamento = st.session_state.equipamento_sel
    eq = df[df["Equipamento"] == equipamento].iloc[0]

    df_orc = pd.read_csv(ARQUIVO_ORC)
    codigo = gerar_codigo_obra(df_orc)

    st.info(f"Código: {codigo}")

    descricao = st.text_input("Descrição da obra")

    volume = st.number_input("Volume", value=10000.0)
    distancia = st.number_input("Distância", value=2000.0)
    preco = st.number_input("Preço", value=16.18)
    horas = st.number_input("Horas/dia", value=20)

    if st.button("Calcular"):
        st.session_state.calc = {
            "codigo": codigo,
            "descricao": descricao,
            "volume": volume,
            "distancia": distancia,
            "preco": preco,
            "vazao": eq["Vazao"],
            "consumo": eq["Consumo"],
            "horas": horas,
            "equipamento": equipamento
        }
        st.session_state.etapa = 3

elif st.session_state.etapa == 3:

    d = st.session_state.calc

    prod = calcular_producao(d["vazao"], d["distancia"])
    tempo = calcular_tempo(d["volume"], prod)
    dias = calcular_dias(tempo, d["horas"])

    diesel = 6
    custo = calcular_diesel(d["consumo"], tempo, diesel)

    receita = calcular_receita(d["volume"], d["preco"])
    lucro = calcular_lucro(receita, custo)

    st.write(f"Código: {d['codigo']}")
    st.write(f"Descrição: {d['descricao']}")
    st.write(f"Lucro: R$ {lucro:,.0f}")

    if st.button("Salvar"):

        df = pd.read_csv(ARQUIVO_ORC)

        novo = pd.DataFrame([[
            d["codigo"], pd.Timestamp.now(), d["descricao"],
            d["equipamento"], d["volume"], d["distancia"],
            prod, tempo, dias, custo, receita, lucro
        ]], columns=df.columns)

        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_ORC, TOKEN, REPO)

        st.success("Salvo!")

    if st.button("Novo"):
        st.session_state.etapa = 0
