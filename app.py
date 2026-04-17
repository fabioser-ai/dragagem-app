import streamlit as st

from pages import menu, dados, ferias, orcamento

# =========================
# CONFIGURAÇÃO INICIAL
# =========================
st.set_page_config(layout="wide")

# =========================
# CONTROLE DE NAVEGAÇÃO
# =========================
if "tela" not in st.session_state:
    st.session_state.tela = "menu"

# =========================
# ROTEADOR DE TELAS
# =========================
if st.session_state.tela == "menu":
    menu.render()

elif st.session_state.tela == "dados":
    dados.render()

elif st.session_state.tela == "ferias":
    ferias.render()

# =========================
# ORÇAMENTO (FLUXO COMPLETO)
# =========================
elif st.session_state.tela == "orcamento":
    orcamento.etapa0()

elif st.session_state.tela == "orcamento1":
    orcamento.etapa1()

elif st.session_state.tela == "orcamento2":
    orcamento.etapa2()
