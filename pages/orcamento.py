import streamlit as st
import pandas as pd
from services.github import carregar_github

ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# ETAPA 1
# =========================
def etapa1():

    st.header("Orçamento - Etapa 1")

    df_equip = carregar_github(ARQ_EQUIP, TOKEN, REPO)
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)
    df_desag = carregar_github(ARQ_DESAG, TOKEN, REPO)

    draga = st.selectbox("Draga", df_equip["Equipamento"])
    dados = df_equip[df_equip["Equipamento"] == draga].iloc[0]

    vazao = st.number_input("Vazão", value=float(dados["Vazao"]))
    volume = st.number_input("Volume")

    material = st.selectbox("Material", df_mat["Material"])
    desag = st.selectbox("Desaguamento", df_desag["Tipo"])

    col1, col2 = st.columns(2)
    flutuante = col1.number_input("Linha flutuante")
    terrestre = col2.number_input("Linha terrestre")

    if st.button("Continuar"):
        st.session_state.orcamento = {
            "vazao": vazao,
            "volume": volume,
            "material": material,
            "desag": desag,
            "flutuante": flutuante,
            "terrestre": terrestre
        }
        st.session_state.tela = "orcamento2"
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
        st.rerun()

# =========================
# ETAPA 2
# =========================
def etapa2():

    st.header("Orçamento - Produção")

    dados = st.session_state.orcamento
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)

    # Distância
    col1, col2 = st.columns(2)

    flutuante = col1.number_input("Linha flutuante", value=dados["flutuante"])
    terrestre = col2.number_input("Linha terrestre", value=dados["terrestre"])

    distancia_total = flutuante + terrestre
    st.info(f"Distância total: {distancia_total:.0f} m")

    # Cálculo
    linha = df_mat[df_mat["Material"] == dados["material"]].iloc[0]
    concentracao = float(linha["Solidos_InSitu"]) / 100

    eficiencia_map = {
        "Geobag": 0.85,
        "Centrífuga": 0.90,
        "Bombeamento direto": 0.95,
        "Bacia ecológica": 0.80
    }

    eficiencia = eficiencia_map.get(dados["desag"], 0.85)

    vazao_real = dados["vazao"] * eficiencia * concentracao

    # Explicação
    st.subheader("Cálculo")

    st.write(f"Vazão: {dados['vazao']}")
    st.write(f"Eficiência: {eficiencia}")
    st.write(f"Concentração: {concentracao}")

    st.code(f"{dados['vazao']} × {eficiencia} × {concentracao}")

    st.success(f"Vazão real: {vazao_real:.2f} m³/h")

    # salvar
    st.session_state.orcamento["vazao_real"] = vazao_real

    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento"
        st.rerun()

    if col2.button("Continuar"):
        st.success("Próxima etapa em breve")
