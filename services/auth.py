import json
import time
import streamlit as st
from services.log import registrar_log


SESSION_TIMEOUT_SECONDS = 60 * 60  # 1 hora


def carregar_usuarios():
    try:
        return json.loads(st.secrets["APP_USERS"])
    except Exception:
        return {}


def inicializar_auth():
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False
    if "usuario" not in st.session_state:
        st.session_state.usuario = None
    if "perfil" not in st.session_state:
        st.session_state.perfil = None
    if "ultimo_acesso" not in st.session_state:
        st.session_state.ultimo_acesso = time.time()


def logout():
    usuario = st.session_state.get("usuario")
    perfil = st.session_state.get("perfil")

    if usuario and perfil:
        registrar_log(usuario, perfil, "logout")

    st.session_state.autenticado = False
    st.session_state.usuario = None
    st.session_state.perfil = None
    st.session_state.tela = "menu"
    st.rerun()


def sessao_expirada():
    agora = time.time()
    ultimo = st.session_state.get("ultimo_acesso", agora)

    if agora - ultimo > SESSION_TIMEOUT_SECONDS:
        return True

    st.session_state.ultimo_acesso = agora
    return False


def verificar_login():
    inicializar_auth()

    if st.session_state.autenticado:
        if sessao_expirada():
            usuario = st.session_state.get("usuario")
            perfil = st.session_state.get("perfil")

            if usuario and perfil:
                registrar_log(usuario, perfil, "sessao_expirada")

            st.warning("Sessão expirada. Faça login novamente.")
            logout()

        return True

    st.markdown("## 🔒 Acesso restrito")
    st.caption("Sistema interno FOS Engenharia LTDA")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        usuarios = carregar_usuarios()

        if usuario in usuarios and senha == usuarios[usuario]["password"]:
            perfil = usuarios[usuario].get("role", "user")

            st.session_state.autenticado = True
            st.session_state.usuario = usuario
            st.session_state.perfil = perfil
            st.session_state.ultimo_acesso = time.time()

            registrar_log(usuario, perfil, "login")

            st.rerun()
        else:
            st.error("Usuário ou senha incorretos. Atenção a maiúsculas e minúsculas.")

    return False


def exigir_admin():
    if st.session_state.get("perfil") != "admin":
        st.error("Acesso restrito ao administrador.")
        st.stop()
