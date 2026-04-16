import streamlit as st
import pandas as pd
from datetime import datetime

from services.github import salvar_github, carregar_github
from services.codigos import gerar_codigo_obra
from services.calculos import *

st.title("FOS ENGENHARIA LTDA")

# =========================
# CONFIG
# =========================
ARQUIVO_EQUIP = "data/equipamentos.csv"
ARQUIVO_ORC = "data/orcamentos.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# ESTADO
# =========================
if "etapa" not in st.session_state:
    st.session_state.etapa = 0

if "equipamento_sel" not in st.session_state:
    st.session_state.equipamento_sel = None

# =========================
# MENU
# =========================
if st.session_state.etapa == 0:

    st.header("Menu Principal")

    col1, col2, col3 = st.columns(3)

    if col1.button("📊 Orçamento"):
        st.session_state.etapa = 1

    if col2.button("🚜 Equipamentos"):
        st.session_state.etapa = 300

    if col3.button("📈 Obras"):
        st.session_state.etapa = 400

# =========================
# EQUIPAMENTOS
# =========================
elif st.session_state.etapa == 300:

    st.header("🚜 Equipamentos")

    df = carregar_github(ARQUIVO_EQUIP, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Equipamento", "Vazao", "Consumo", "Valor"])

    st.dataframe(df)

    if st.button("🔄 Atualizar dados"):
        st.rerun()

    st.divider()

    # EDITAR
    if not df.empty:

        sel = st.selectbox("Selecionar", df["Equipamento"])
        linha = df[df["Equipamento"] == sel].iloc[0]

        nome = st.text_input("Nome", value=linha["Equipamento"])
        vazao = st.number_input("Vazão", value=float(linha["Vazao"]))
        consumo = st.number_input("Consumo", value=float(linha["Consumo"]))
        valor = st.number_input("Valor", value=float(linha["Valor"]))

        col1, col2 = st.columns(2)

        if col1.button("Salvar"):
            idx = df["Equipamento"] == sel

            df.loc[idx, "Equipamento"] = nome
            df.loc[idx, "Vazao"] = vazao
            df.loc[idx, "Consumo"] = consumo
            df.loc[idx, "Valor"] = valor

            salvar_github(df, ARQUIVO_EQUIP, TOKEN, REPO)

            st.success("Atualizado no GitHub!")
            st.rerun()

        if col2.button("Excluir"):
            df = df[df["Equipamento"] != sel]

            salvar_github(df, ARQUIVO_EQUIP, TOKEN, REPO)

            st.warning("Removido!")
            st.rerun()

    st.divider()

    # NOVO
    st.subheader("Novo equipamento")

    nome_n = st.text_input("Nome novo")
    vazao_n = st.number_input("Vazão nova", value=1000.0)
    consumo_n = st.number_input("Consumo novo", value=60.0)
    valor_n = st.number_input("Valor novo", value=1000000.0)

    if st.button("Adicionar"):
        novo = pd.DataFrame([[nome_n, vazao_n, consumo_n, valor_n]],
                            columns=df.columns)

        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_EQUIP, TOKEN, REPO)

        st.success("Adicionado no GitHub!")
        st.rerun()

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# DASHBOARD
# =========================
elif st.session_state.etapa == 400:

    st.header("📈 Histórico de Obras")

    df = carregar_github(ARQUIVO_ORC, TOKEN, REPO)

    if df.empty:
        st.warning("Sem dados ainda")
    else:

        st.dataframe(df)

        receita = df["Receita"].sum()
        lucro = df["Lucro"].sum()
        margem = (lucro / receita * 100) if receita > 0 else 0

        col1, col2, col3 = st.columns(3)

        col1.metric("Receita", f"R$ {receita:,.0f}")
        col2.metric("Lucro", f"R$ {lucro:,.0f}")
        col3.metric("Margem", f"{margem:.1f}%")

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# ORÇAMENTO
# =========================
elif st.session_state.etapa == 1:

    df = carregar_github(ARQUIVO_EQUIP, TOKEN, REPO)

    if df.empty:
        st.warning("Cadastre equipamentos primeiro!")
    else:

        equipamento = st.selectbox("Equipamento", df["Equipamento"])
        eq = df[df["Equipamento"] == equipamento].iloc[0]

        if st.button("Continuar"):
            st.session_state.equipamento_sel = equipamento
            st.session_state.etapa = 2

elif st.session_state.etapa == 2:

    df = carregar_github(ARQUIVO_EQUIP, TOKEN, REPO)
    eq = df[df["Equipamento"] == st.session_state.equipamento_sel].iloc[0]

    df_orc = carregar_github(ARQUIVO_ORC, TOKEN, REPO)
    codigo = gerar_codigo_obra(df_orc)

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
            "equipamento": st.session_state.equipamento_sel
        }
        st.session_state.etapa = 3

elif st.session_state.etapa == 3:

    d = st.session_state.calc

    prod = calcular_producao(d["vazao"], d["distancia"])
    tempo = calcular_tempo(d["volume"], prod)
    dias = calcular_dias(tempo, d["horas"])

    custo = calcular_diesel(d["consumo"], tempo, 6)
    receita = calcular_receita(d["volume"], d["preco"])
    lucro = calcular_lucro(receita, custo)

    st.write(f"Código: {d['codigo']}")
    st.write(f"Descrição: {d['descricao']}")
    st.write(f"Lucro: R$ {lucro:,.0f}")

    if st.button("Salvar"):

        df = carregar_github(ARQUIVO_ORC, TOKEN, REPO)

        if df.empty:
            df = pd.DataFrame(columns=[
                "Codigo","Data","Descricao","Equipamento",
                "Volume","Distancia","Produtividade","Tempo_h",
                "Dias","Custo_Diesel","Receita","Lucro"
            ])

        novo = pd.DataFrame([[
            d["codigo"], datetime.now(), d["descricao"],
            d["equipamento"], d["volume"], d["distancia"],
            prod, tempo, dias, custo, receita, lucro
        ]], columns=df.columns)

        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_ORC, TOKEN, REPO)

        st.success("Salvo no GitHub!")
