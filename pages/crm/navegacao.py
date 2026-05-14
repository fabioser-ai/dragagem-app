import streamlit as st


def menu_crm():
    st.sidebar.markdown("## CRM")

    opcoes = {
        "Clientes": "clientes",
        "Contatos": "contatos",
        "Interações": "interacoes",
        "Consulta geral": "consulta",
    }

    escolha = st.sidebar.radio(
        "Navegação CRM",
        list(opcoes.keys()),
        label_visibility="collapsed",
    )

    return opcoes[escolha]
