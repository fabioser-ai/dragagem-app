import json
import time

import streamlit as st

from services.loading_fos import _LOGO_FOS
from services.log import registrar_log


SESSION_TIMEOUT_SECONDS = 60 * 60
CHAVE_LOG_PENDENTE = "_log_acesso_pendente"
CHAVE_RECUPERACAO_ADMIN = "_custodia_admin_recuperada"


class _AutenticacaoOperacionalIndisponivel:
    dados = None
    indisponivel = True


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
        from services.credenciais_operacionais import autenticar_usuario_operacional_resultado

        return autenticar_usuario_operacional_resultado(
            login=usuario, senha=senha, usuarios_protegidos=usuarios_protegidos
        )
    except Exception:
        return _AutenticacaoOperacionalIndisponivel()


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


def _renderizar_cabecalho_login_fos():
    """Cabeçalho visual do login; não interfere na lógica de autenticação."""
    st.markdown(
        f"""
        <style>
        .fos-login-brand {{
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            text-align:center;
            margin: 1.4rem 0 1.8rem;
        }}
        .fos-login-logo-wrap {{
            position:relative;
            width:150px;
            height:150px;
            display:flex;
            align-items:center;
            justify-content:center;
            animation: fosLoginEnter .8s cubic-bezier(.2,.8,.2,1) both;
        }}
        .fos-login-logo-wrap::before {{
            content:"";
            position:absolute;
            inset:12px;
            border-radius:50%;
            background:radial-gradient(circle, rgba(169,80,53,.12) 0%, rgba(169,80,53,0) 68%);
            animation: fosLoginHalo 3.2s ease-in-out infinite;
        }}
        .fos-login-logo {{
            position:relative;
            z-index:1;
            width:118px;
            max-width:32vw;
            filter: drop-shadow(0 10px 18px rgba(60,38,30,.14));
            animation: fosLoginFloat 4.8s ease-in-out infinite;
        }}
        .fos-login-title {{
            margin:.35rem 0 .2rem;
            color:#263445;
            font-size:1.7rem;
            line-height:1.15;
            font-weight:760;
            letter-spacing:-.02em;
            animation: fosLoginText .65s .18s ease-out both;
        }}
        .fos-login-subtitle {{
            margin:0;
            color:#7b8794;
            font-size:.94rem;
            animation: fosLoginText .65s .28s ease-out both;
        }}
        @keyframes fosLoginEnter {{
            0% {{ opacity:0; transform:translateY(14px) scale(.94); }}
            100% {{ opacity:1; transform:translateY(0) scale(1); }}
        }}
        @keyframes fosLoginFloat {{
            0%,100% {{ transform:translateY(0); }}
            50% {{ transform:translateY(-4px); }}
        }}
        @keyframes fosLoginHalo {{
            0%,100% {{ opacity:.35; transform:scale(.92); }}
            50% {{ opacity:.72; transform:scale(1.06); }}
        }}
        @keyframes fosLoginText {{
            0% {{ opacity:0; transform:translateY(8px); }}
            100% {{ opacity:1; transform:translateY(0); }}
        }}
        @media (prefers-reduced-motion: reduce) {{
            .fos-login-logo-wrap,
            .fos-login-logo,
            .fos-login-logo-wrap::before,
            .fos-login-title,
            .fos-login-subtitle {{ animation:none !important; }}
        }}
        </style>
        <div class="fos-login-brand">
            <div class="fos-login-logo-wrap">
                <img class="fos-login-logo" src="{_LOGO_FOS}" alt="FOS Engenharia">
            </div>
            <div class="fos-login-title">Acesso ao APP FOS</div>
            <div class="fos-login-subtitle">Sistema interno FOS Engenharia LTDA</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


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
        _renderizar_cabecalho_login_fos()
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
    autenticacao_operacional_indisponivel = usuarios_confirmados is None
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
        resultado_operacional = _autenticar_operacional(usuario, senha, usuarios)
        if hasattr(resultado_operacional, "dados"):
            dados_usuario = resultado_operacional.dados
            autenticacao_operacional_indisponivel = bool(
                getattr(resultado_operacional, "indisponivel", False)
            )
        else:
            # Compatibilidade defensiva com integrações legadas/mocks.
            dados_usuario = resultado_operacional

    if dados_usuario is None:
        if autenticacao_operacional_indisponivel:
            st.error(
                "Não foi possível validar seu acesso neste momento. "
                "Tente novamente em alguns minutos."
            )
        else:
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