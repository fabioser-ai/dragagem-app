import json
import time

import streamlit as st

from services.log import registrar_log


SESSION_TIMEOUT_SECONDS = 60 * 60
CHAVE_LOG_PENDENTE = "_log_acesso_pendente"


def carregar_usuarios():
    try:
        return json.loads(st.secrets["APP_USERS"])
    except Exception:
        return {}


def inicializar_auth():
    padroes = {
        "autenticado": False,
        "usuario": None,
        "perfil": None,
        "matricula": None,
        "nome": None,
        "ultimo_acesso": time.time(),
    }
    for chave, valor in padroes.items():
        if chave not in st.session_state:
            st.session_state[chave] = valor


def limpar_sessao():
    for chave in (
        "autenticado",
        "usuario",
        "perfil",
        "matricula",
        "nome",
        "tela",
        "ultimo_acesso",
        CHAVE_LOG_PENDENTE,
    ):
        st.session_state.pop(chave, None)


def _agendar_log(usuario, perfil, acao):
    st.session_state[CHAVE_LOG_PENDENTE] = (usuario, perfil, acao)


def processar_log_pendente():
    pendente = st.session_state.pop(CHAVE_LOG_PENDENTE, None)
    if not pendente:
        return None

    try:
        return registrar_log(*pendente)
    except Exception:
        return None


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

            limpar_sessao()
            st.warning("Sessão expirada. Faça login novamente.")
            return False
        return True

    area_login = st.empty()
    with area_login.container():
        st.markdown("## 🔒 Acesso restrito")
        st.caption("Sistema interno FOS Engenharia LTDA")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        entrar = st.button("Entrar")

    if not entrar:
        return False

    usuarios = carregar_usuarios()
    if usuario not in usuarios or senha != usuarios[usuario]["password"]:
        st.error("Usuário ou senha incorretos. Atenção a maiúsculas e minúsculas.")
        return False

    dados_usuario = usuarios[usuario]
    perfil = dados_usuario.get("role", "user")
    st.session_state.autenticado = True
    st.session_state.usuario = usuario
    st.session_state.perfil = perfil
    st.session_state.matricula = dados_usuario.get("matricula", "")
    st.session_state.nome = dados_usuario.get("nome", usuario)
    st.session_state.ultimo_acesso = time.time()
    st.session_state.tela = "menu"
    _agendar_log(usuario, perfil, "login")

    # Continua no mesmo ciclo: não há rerun entre a confirmação e o menu.
    area_login.empty()
    return True


def exigir_admin():
    if st.session_state.get("perfil") != "admin":
        st.error("Acesso restrito ao administrador.")
        st.stop()
