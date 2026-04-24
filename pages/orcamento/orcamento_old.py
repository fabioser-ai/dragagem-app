import streamlit as st

from pages.orcamento.etapa0 import etapa0
from pages.orcamento.etapa1 import etapa1
from pages.orcamento.etapa2 import etapa2
from pages.orcamento.etapa3 import etapa3

def render():

    if "tela_orcamento" not in st.session_state:
        st.session_state.tela_orcamento = "etapa0"

    # ROTEAMENTO INTERNO
    if st.session_state.tela_orcamento == "etapa0":
        etapa0()

    elif st.session_state.tela_orcamento == "etapa1":
        etapa1()

    elif st.session_state.tela_orcamento == "etapa2":
        etapa2()

    elif st.session_state.tela_orcamento == "etapa3":
        etapa3()
