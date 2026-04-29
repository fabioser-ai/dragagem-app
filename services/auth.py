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


def limpar_sessao():
    chaves_para_limpar = [
        "autenticado",
        "usuario",
        "perfil",
        "tela",
        "ultimo_acesso",
    ]

    for chave in chaves_para_limpar:
        if chave in st.session_state:
            del st.session_state[chave]


def logout():
    usuario = st.session_state.get("usuario")
    perfil = st.session_state.get("perfil")

    try:
        if usuario and perfil:
            registrar_log(usuario, perfil, "logout")
    except Exception:
        pass

    limpar_sessao()
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

            try:
                if usuario and perfil:
                    registrar_log(usuario, perfil, "sessao_expirada")
            except Exception:
                pass

            st.warning("Sessão expirada. Faça login novamente.")
            limpar_sessao()
            st.rerun()

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

            try:
                registrar_log(usuario, perfil, "login")
            except Exception:
                pass

            st.rerun()
        else:
            st.error("Usuário ou senha incorretos. Atenção a maiúsculas e minúsculas.")

    return False


def exigir_admin():
    if st.session_state.get("perfil") != "admin":
        st.error("Acesso restrito ao administrador.")
        st.stop()
