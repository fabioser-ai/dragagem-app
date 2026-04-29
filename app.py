import streamlit as st

# Módulos principais
from pages import menu, dados, ferias

# Módulo orçamento (novo - modular)
from pages.orcamento.etapa0 import etapa0
from pages.orcamento.etapa1 import etapa1
from pages.orcamento.etapa2 import etapa2
from pages.orcamento.etapa3 import etapa3

# =========================
# CONFIGURAÇÃO
# =========================
st.set_page_config(layout="wide")
from services.auth import verificar_login

if not verificar_login():
    st.stop()
# =========================
# ESTADO INICIAL
# =========================
if "tela" not in st.session_state:
    st.session_state.tela = "menu"

# =========================
# ROTEADOR
# =========================
if st.session_state.tela == "menu":
    menu.render()

elif st.session_state.tela == "dados":
    from services.auth import exigir_admin
    exigir_admin()
    dados.render()


elif st.session_state.tela == "ferias":
    ferias.render()

# =========================
# MÓDULO OBRAS
# =========================
elif st.session_state.tela == "obras":
    import pandas as pd
    from services.github import carregar_github

    st.title("📊 Obras")

    ARQ_OBRAS = "data/orcamentos.csv"

    try:
        df = carregar_github(
            ARQ_OBRAS,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"]
        )
    except:
        df = pd.DataFrame()

    if df.empty:
        st.warning("Nenhuma obra cadastrada ainda.")
    else:
        st.subheader("Lista de Obras")
        st.dataframe(df, use_container_width=True)

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
        st.rerun()

# =========================
# ORÇAMENTO (MODULAR)
# =========================
elif st.session_state.tela == "orcamento":
    etapa0()

elif st.session_state.tela == "orcamento1":
    etapa1()

elif st.session_state.tela == "orcamento2":
    etapa2()

elif st.session_state.tela == "orcamento3":
    etapa3()
