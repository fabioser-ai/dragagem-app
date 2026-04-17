import streamlit as st

def render():
    st.title("FOS ENGENHARIA LTDA")

    col1, col2, col3 = st.columns(3)

    if col1.button("📊 ORÇAMENTO", use_container_width=True):
        st.session_state.tela = "orcamento"

    if col1.button("📅 FÉRIAS", use_container_width=True):
        st.session_state.tela = "ferias"

    if col2.button("📈 OBRAS", use_container_width=True):
        st.session_state.tela = "obras"

    if col3.button("📁 DADOS", use_container_width=True):
        st.session_state.tela = "dados"
