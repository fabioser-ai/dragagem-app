import streamlit as st

from pages import menu, dados, ferias, orcamento

st.set_page_config(layout="wide")

if "tela" not in st.session_state:
    st.session_state.tela = "menu"

# ROTEADOR
if st.session_state.tela == "menu":
    menu.render()

elif st.session_state.tela == "dados":
    dados.render()

elif st.session_state.tela == "ferias":
    ferias.render()

elif st.session_state.tela == "orcamento":
    orcamento.etapa1()

elif st.session_state.tela == "orcamento2":
    orcamento.etapa2()
