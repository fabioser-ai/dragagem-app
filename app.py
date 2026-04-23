import streamlit as st

from pages import menu, dados, ferias, orcamento

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
# ROTEADOR
# =========================
if st.session_state.tela == "menu":
    menu.render()

elif st.session_state.tela == "dados":
    dados.render()

elif st.session_state.tela == "ferias":
    ferias.render()

# =========================
# MÓDULO OBRAS (NOVO)
# =========================
elif st.session_state.tela == "obras":
    st.title("📊 Obras")
    st.info("Módulo em construção")

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
        st.rerun()

# =========================
# ORÇAMENTO
# =========================
elif st.session_state.tela == "orcamento":
    orcamento.etapa0()

elif st.session_state.tela == "orcamento1":
    orcamento.etapa1()

elif st.session_state.tela == "orcamento2":
    orcamento.etapa2()
