import streamlit as st
import pandas as pd

from services.github import salvar_github, carregar_github

st.set_page_config(layout="wide")
st.title("FOS ENGENHARIA LTDA")

# =========================
# ARQUIVOS
# =========================
ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"
ARQ_FERIAS = "data/ferias.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# ESTADO
# =========================
if "tela" not in st.session_state:
    st.session_state.tela = "menu"

# =========================
# MENU
# =========================
if st.session_state.tela == "menu":

    if st.button("📊 ORÇAMENTO"):
        st.session_state.tela = "orcamento"

# =========================
# ORÇAMENTO ETAPA 1
# =========================
elif st.session_state.tela == "orcamento":

    st.header("Orçamento - Etapa 1")

    df_equip = carregar_github(ARQ_EQUIP, TOKEN, REPO)
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)
    df_desag = carregar_github(ARQ_DESAG, TOKEN, REPO)

    draga = st.selectbox("Draga", df_equip["Equipamento"])
    dados = df_equip[df_equip["Equipamento"] == draga].iloc[0]

    vazao = st.number_input("Vazão (m³/h)", value=float(dados["Vazao"]))
    volume = st.number_input("Volume (m³)")

    material = st.selectbox("Material", df_mat["Material"])
    desag = st.selectbox("Desaguamento", df_desag["Tipo"])

    col1, col2 = st.columns(2)
    flutuante = col1.number_input("Linha flutuante (m)")
    terrestre = col2.number_input("Linha terrestre (m)")

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

# =========================
# ORÇAMENTO ETAPA 2
# =========================
elif st.session_state.tela == "orcamento2":

    st.header("Orçamento - Produção")

    dados = st.session_state.orcamento
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)

    # =========================
    # AJUSTE DE DISTÂNCIA
    # =========================
    st.subheader("Distância de Recalque")

    col1, col2 = st.columns(2)

    flutuante = col1.number_input(
        "Linha flutuante (m)",
        value=float(dados["flutuante"])
    )

    terrestre = col2.number_input(
        "Linha terrestre (m)",
        value=float(dados["terrestre"])
    )

    distancia_total = flutuante + terrestre

    st.info(f"Distância total: {distancia_total:.0f} m")

    st.divider()

    # =========================
    # CÁLCULO
    # =========================
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

    # =========================
    # EXPLICAÇÃO
    # =========================
    st.subheader("Cálculo da Vazão Real")

    st.write(f"Vazão: {dados['vazao']:.2f}")
    st.write(f"Eficiência: {eficiencia:.2f}")
    st.write(f"Concentração: {concentracao:.2f}")

    st.code(f"{dados['vazao']:.2f} × {eficiencia:.2f} × {concentracao:.2f}")

    st.success(f"Vazão real: {vazao_real:.2f} m³/h")

    # salvar atualização
    st.session_state.orcamento["flutuante"] = flutuante
    st.session_state.orcamento["terrestre"] = terrestre
    st.session_state.orcamento["vazao_real"] = vazao_real

    # =========================
    # NAVEGAÇÃO
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento"
        st.rerun()

    if col2.button("Continuar"):
        st.success("Pronto para próxima etapa")
