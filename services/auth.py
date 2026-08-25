import json
import time

import streamlit as st

from services.log import registrar_log


SESSION_TIMEOUT_SECONDS = 60 * 60
CHAVE_LOG_PENDENTE = "_log_acesso_pendente"
CHAVE_RECUPERACAO_ADMIN = "_custodia_admin_recuperada"


def carregar_usuarios():
    try:
        return json.loads(st.secrets["APP_USERS"])
    except Exception:
        return {}


def _carregar_usuarios_confirmado():
    try:
        bruto = st.secrets["APP_USERS"]
        usuarios = json.loads(bruto) if isinstance(bruto, str) else bruto
        return usuarios if isinstance(usuarios, dict) else None
    except Exception:
        return None


def _autenticar_operacional(usuario, senha, usuarios_protegidos):
    """Autentica a base operacional; qualquer ambiguidade resulta em negação."""
    try:
        from services.credenciais_operacionais import autenticar_usuario_operacional

        return autenticar_usuario_operacional(
            login=usuario, senha=senha, usuarios_protegidos=usuarios_protegidos
        )
    except Exception:
        return None


def _abrir_sessao(*, usuario, perfil, matricula, nome):
    st.session_state["autenticado"] = True
    st.session_state["usuario"] = usuario
    st.session_state["perfil"] = perfil
    st.session_state["matricula"] = matricula
    st.session_state["nome"] = nome
    st.session_state["ultimo_acesso"] = time.time()
    st.session_state["tela"] = "menu"
    _agendar_log(usuario, perfil, "login")


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
        CHAVE_RECUPERACAO_ADMIN,
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

    usuarios_confirmados = _carregar_usuarios_confirmado()
    usuarios = usuarios_confirmados or {}
    protegidos_normalizados = {
        str(login).strip().casefold() for login in usuarios
    }
    dados_usuario = None
    if usuario in usuarios and senha == usuarios[usuario].get("password"):
        dados_usuario = {
            "usuario": usuario,
            "perfil": usuarios[usuario].get("role", "user"),
            "matricula": usuarios[usuario].get("matricula", ""),
            "nome": usuarios[usuario].get("nome", usuario),
        }
    elif (
        usuarios_confirmados is not None
        and str(usuario).strip().casefold() not in protegidos_normalizados
    ):
        dados_usuario = _autenticar_operacional(usuario, senha, usuarios)

    if dados_usuario is None:
        st.error("Usuário ou senha incorretos. Atenção a maiúsculas e minúsculas.")
        return False

    _abrir_sessao(**dados_usuario)

    # Continua no mesmo ciclo: não há rerun entre a confirmação e o menu.
    area_login.empty()
    return True


def exigir_admin():
    from services.autorizacao import possui_privilegio_administrativo

    if not possui_privilegio_administrativo():
        st.error("Acesso restrito ao administrador.")
        st.stop()
