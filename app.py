import streamlit as st
import pandas as pd
from datetime import datetime

from services.github import salvar_github, carregar_github
from services.codigos import gerar_codigo_obra
from services.calculos import *

st.set_page_config(layout="wide")

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
# SIDEBAR MENU
# =========================
st.sidebar.title("Menu")

opcao = st.sidebar.radio(
    "Navegação",
    [
        "📊 Orçamento",
        "🚜 Equipamentos",
        "📅 Férias/Folgas",
        "💰 Salários",
        "📈 Obras"
    ]
)

# =========================
# ORÇAMENTO
# =========================
if opcao == "📊 Orçamento":

    st.header("Orçamento de Dragagem")

    df = carregar_github(ARQUIVO_EQUIP, TOKEN, REPO)

    if df.empty:
        st.warning("Cadastre equipamentos primeiro!")
    else:

        equipamento = st.selectbox("Equipamento", df["Equipamento"])

        eq = df[df["Equipamento"] == equipamento].iloc[0]

        df_orc = carregar_github(ARQUIVO_ORC, TOKEN, REPO)
        codigo = gerar_codigo_obra(df_orc)

        st.info(f"Código da obra: {codigo}")

        descricao = st.text_input("Descrição da obra")

        col1, col2 = st.columns(2)

        with col1:
            volume = st.number_input("Volume (m³)", value=10000.0)
            distancia = st.number_input("Distância (m)", value=2000.0)

        with col2:
            preco = st.number_input("Preço (R$/m³)", value=16.18)
            horas = st.number_input("Horas/dia", value=20)

        if st.button("Calcular"):

            prod = calcular_producao(eq["Vazao"], distancia)
            tempo = calcular_tempo(volume, prod)
            dias = calcular_dias(tempo, horas)

            custo = calcular_diesel(eq["Consumo"], tempo, 6)
            receita = calcular_receita(volume, preco)
            lucro = calcular_lucro(receita, custo)

            st.subheader("Resultado")

            st.write(f"Produção: {prod:,.0f} m³/h")
            st.write(f"Tempo: {tempo:,.1f} h")
            st.write(f"Dias: {dias:,.1f}")

            st.write(f"Receita: R$ {receita:,.0f}")
            st.write(f"Custo Diesel: R$ {custo:,.0f}")
            st.write(f"Lucro: R$ {lucro:,.0f}")

            if st.button("Salvar orçamento"):

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

                st.success("Orçamento salvo!")

# =========================
# EQUIPAMENTOS
# =========================
elif opcao == "🚜 Equipamentos":

    st.header("Equipamentos")

    df = carregar_github(ARQUIVO_EQUIP, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Equipamento", "Vazao", "Consumo", "Valor"])

    st.dataframe(df)

    st.divider()

    if not df.empty:

        sel = st.selectbox("Selecionar", df["Equipamento"])
        linha = df[df["Equipamento"] == sel].iloc[0]

        nome = st.text_input("Nome", value=linha["Equipamento"])
        vazao = st.number_input("Vazão", value=float(linha["Vazao"]))
        consumo = st.number_input("Consumo", value=float(linha["Consumo"]))
        valor = st.number_input("Valor", value=float(linha["Valor"]))

        if st.button("Salvar alteração"):
            idx = df["Equipamento"] == sel

            df.loc[idx, "Equipamento"] = nome
            df.loc[idx, "Vazao"] = vazao
            df.loc[idx, "Consumo"] = consumo
            df.loc[idx, "Valor"] = valor

            salvar_github(df, ARQUIVO_EQUIP, TOKEN, REPO)
            st.success("Atualizado!")
            st.rerun()

        if st.button("Excluir equipamento"):
            df = df[df["Equipamento"] != sel]

            salvar_github(df, ARQUIVO_EQUIP, TOKEN, REPO)
            st.warning("Removido!")
            st.rerun()

    st.divider()

    st.subheader("Novo equipamento")

    nome_n = st.text_input("Nome novo")
    vazao_n = st.number_input("Vazão", value=1000.0)
    consumo_n = st.number_input("Consumo", value=60.0)
    valor_n = st.number_input("Valor", value=1000000.0)

    if st.button("Adicionar"):
        novo = pd.DataFrame([[nome_n, vazao_n, consumo_n, valor_n]],
                            columns=df.columns)

        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_EQUIP, TOKEN, REPO)
        st.success("Adicionado!")
        st.rerun()

# =========================
# FÉRIAS
# =========================
elif opcao == "📅 Férias/Folgas":

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
        novo = pd.DataFrame([[nome, data_inicio, data_fim, tipo]],
                            columns=df.columns)

        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_FERIAS, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

# =========================
# SALÁRIOS
# =========================
elif opcao == "💰 Salários":

    st.header("Salários")

    df = carregar_github(ARQUIVO_SALARIOS, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Cargo", "Valor_Hora"])

    st.dataframe(df)

    cargo = st.text_input("Cargo")
    valor = st.number_input("Valor por hora", value=20.0)

    if st.button("Adicionar"):
        novo = pd.DataFrame([[cargo, valor]], columns=df.columns)

        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_SALARIOS, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

# =========================
# DASHBOARD
# =========================
elif opcao == "📈 Obras":

    st.header("Histórico de Obras")

    df = carregar_github(ARQUIVO_ORC, TOKEN, REPO)

    if df.empty:
        st.warning("Sem dados ainda")
    else:

        st.dataframe(df)

        receita = df["Receita"].sum()
        lucro = df["Lucro"].sum()
        margem = (lucro / receita * 100) if receita > 0 else 0

        st.metric("Receita", f"R$ {receita:,.0f}")
        st.metric("Lucro", f"R$ {lucro:,.0f}")
        st.metric("Margem", f"{margem:.1f}%")
