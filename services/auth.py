import streamlit as st


def verificar_login():
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    if st.session_state.autenticado:
        return True

    st.markdown("## 🔒 Acesso restrito")

    senha = st.text_input("Digite a senha", type="password")

    if st.button("Entrar"):
        if senha == st.secrets["APP_PASSWORD"]:
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Senha incorreta")

    return False
