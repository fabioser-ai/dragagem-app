import streamlit as st

# Módulos principais
from pages import menu, dados, ferias

# =========================
# CONFIGURAÇÃO
# =========================
st.set_page_config(layout="wide")

# =========================
# ESTADO INICIAL
# =========================
if "tela" not in st.session_state:
    st.session_state.tela = "menu"

# =========================
# ROTEADOR PRINCIPAL
# =========================
if st.session_state.tela == "menu":
    menu.render()

elif st.session_state.tela == "dados":
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
# ORÇAMENTO (NOVO MODELO MODULAR)
# =========================
elif st.session_state.tela in ["orcamento", "orcamento1", "orcamento2", "orcamento3"]:

    try:
        # NOVO MODELO (modular)
        from pages.orcamento import etapa0, etapa1, etapa2, etapa3

        if st.session_state.tela == "orcamento":
            etapa0()

        elif st.session_state.tela == "orcamento1":
            etapa1()

        elif st.session_state.tela == "orcamento2":
            etapa2()

        elif st.session_state.tela == "orcamento3":
            etapa3()

    except Exception as e:
        # FALLBACK PARA MODELO ANTIGO (segurança total)
        from pages import orcamento

        st.warning("⚠️ Usando versão antiga do orçamento (fallback automático)")

        if st.session_state.tela == "orcamento":
            orcamento.etapa0()

        elif st.session_state.tela == "orcamento1":
            orcamento.etapa1()

        elif st.session_state.tela == "orcamento2":
            orcamento.etapa2()

        st.error(f"Erro na versão nova: {e}")
