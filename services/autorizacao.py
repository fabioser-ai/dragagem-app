"""Autoridade central de identidade e autorização do APP FOS.

Os módulos informam o contexto da decisão; somente esta camada seleciona a
autoridade configurada e interpreta a sessão.
"""

import re

import streamlit as st

from services.permissoes import (
    eh_administrador_sistema,
    eh_superadmin,
    obras_permitidas,
    perfil_global,
    pode_acessar_modulo,
    pode_executar,
)
from services import rbac_authority


ROTAS_POR_MODULO = {
    "dados": "dados",
    "ferias": "ferias",
    "prestacao_contas": "prestacao_contas",
    "carregando_medicoes": "medicoes",
    "medicoes": "medicoes",
    "crm": "crm",
    "uniformes_epis": "uniformes_epis",
    "novo_orcamento": "orcamento",
    "obras": "obras",
    "orcamento": "orcamento",
    "orcamento_lista": "orcamento",
    "orcamento_etapa0": "orcamento",
    "orcamento1": "orcamento",
    "orcamento2": "orcamento",
    "orcamento3": "orcamento",
}

ROTAS_FUNCIONARIO = {
    "menu",
    "prestacao_contas",
    "carregando_medicoes",
    "medicoes",
}

SECRET_PROPRIETARIO = "SYSTEM_OWNER_ID"
CHAVE_RECUPERACAO_ADMIN = "_custodia_admin_recuperada"
CHAVE_ULTIMA_DECISAO = "_ultima_decisao_autorizacao"
SECRET_MODO_AUTORIZACAO = "AUTHORIZATION_MODE"
MODO_RBAC = "RBAC"
MODO_LEGACY = "LEGACY"
# TEMPORARY_OWNER_BYPASS: REMOVER APÓS HOMOLOGAÇÃO DO RBAC.
TEMPORARY_OWNER_BYPASS = True
_PADRAO_IDENTIDADE = re.compile(r"^[A-Za-z0-9_.@+-]{1,128}$")


def _identidade_proprietario_configurada():
    """Lê somente o secret canônico e nunca aplica fallback para APP_USERS."""
    try:
        valor = st.secrets[SECRET_PROPRIETARIO]
    except Exception:
        return None, "secret_ausente"

    if not isinstance(valor, str):
        return None, "secret_invalido"

    normalizado = valor.strip().casefold()
    if valor != valor.strip() or not _PADRAO_IDENTIDADE.fullmatch(valor):
        return None, "secret_invalido"

    return normalizado, "valida"


def identificador_proprietario():
    """Retorna a identidade canônica para consumidores internos autorizados."""
    identidade, estado = _identidade_proprietario_configurada()
    return identidade if estado == "valida" else None


def identidade_proprietario_valida():
    """Confirma apenas a validade do secret, independentemente de APP_USERS."""
    _, estado = _identidade_proprietario_configurada()
    return estado == "valida"


def usuario_proprietario():
    """Decide se a sessão autenticada pertence ao único proprietário canônico."""
    identidade = identificador_proprietario()
    if not autenticado() or identidade is None:
        return False
    usuario = str(st.session_state.get("usuario") or "").strip().casefold()
    return bool(usuario) and usuario == identidade


def pode_recuperar_administracao():
    """A recuperação exige sessão autenticada e identidade canônica revalidada."""
    return usuario_proprietario()


def recuperacao_administrativa_ativa():
    """Valida novamente a custódia; a marca isolada de sessão não concede acesso."""
    return usuario_proprietario() and bool(
        st.session_state.get(CHAVE_RECUPERACAO_ADMIN, False)
    )


def diagnostico_identidade_proprietario():
    """Produz diagnóstico seguro, sem expor o valor do secret ou da identidade."""
    _, estado = _identidade_proprietario_configurada()
    if estado != "valida":
        return {
            "codigo": estado,
            "identidade_valida": False,
            "sessao_proprietario": False,
            "recuperacao_ativa": False,
        }
    if not autenticado():
        codigo = "sessao_nao_autenticada"
    elif not usuario_proprietario():
        codigo = "sessao_nao_proprietaria"
    elif usuario_superadmin():
        codigo = "proprietario_superadmin"
    elif recuperacao_administrativa_ativa():
        codigo = "proprietario_recuperado"
    else:
        codigo = "proprietario_sem_superadmin"
    return {
        "codigo": codigo,
        "identidade_valida": True,
        "sessao_proprietario": usuario_proprietario(),
        "recuperacao_ativa": recuperacao_administrativa_ativa(),
    }


def _registrar_recuperacao(resultado):
    try:
        from services.log import registrar_log

        registrar_log(
            str(st.session_state.get("usuario") or ""),
            str(st.session_state.get("perfil") or ""),
            f"recuperacao_administracao_{resultado}",
        )
        return True
    except Exception:
        return False


def recuperar_administracao():
    """Restaura na sessão apenas a autoridade administrativa do proprietário."""
    if not pode_recuperar_administracao():
        st.session_state.pop(CHAVE_RECUPERACAO_ADMIN, None)
        log_registrado = _registrar_recuperacao("negada")
        return {"sucesso": False, "codigo": "recuperacao_negada", "log_registrado": log_registrado}

    # Revalidação deliberadamente imediata antes da elevação de sessão.
    if not usuario_proprietario():
        st.session_state.pop(CHAVE_RECUPERACAO_ADMIN, None)
        log_registrado = _registrar_recuperacao("negada")
        return {"sucesso": False, "codigo": "recuperacao_negada", "log_registrado": log_registrado}

    st.session_state[CHAVE_RECUPERACAO_ADMIN] = True
    log_registrado = _registrar_recuperacao("concedida")
    return {"sucesso": True, "codigo": "recuperacao_concedida", "log_registrado": log_registrado}


def autenticado():
    """Retorna se há uma identidade autenticada válida na sessão corrente."""
    return bool(st.session_state.get("autenticado", False))


def iniciar_execucao_autorizacao():
    """Abre um novo ciclo de decisões com fontes RBAC frescas."""
    rbac_authority.iniciar_execucao()


def usuario_superadmin():
    """Reconhece o superadmin somente dentro de uma sessão autenticada."""
    return autenticado() and eh_superadmin()


def modo_autorizacao():
    """Aceita somente modos exclusivos; ausência configura o corte para RBAC."""
    try:
        valor = st.secrets.get(SECRET_MODO_AUTORIZACAO, MODO_RBAC)
    except Exception:
        valor = MODO_RBAC
    normalizado = str(valor or "").strip().upper()
    return normalizado if normalizado in {MODO_RBAC, MODO_LEGACY} else None


def temporary_owner_bypass():
    """Cabo de segurança exclusivo da identidade canônica protegida."""
    return bool(TEMPORARY_OWNER_BYPASS and usuario_proprietario())


def _registrar_decisao(decisao, *, modulo, recurso, acao, obra_id):
    st.session_state[CHAVE_ULTIMA_DECISAO] = {
        "usuario": str(st.session_state.get("usuario") or ""),
        "modulo": str(modulo or ""), "recurso": str(recurso or ""),
        "acao": str(acao or ""), "obra_id": str(obra_id or ""),
        "permitido": bool(decisao.permitido), "codigo": decisao.codigo,
        "roles": tuple(decisao.roles), "origens": tuple(decisao.origens),
    }


def possui_privilegio_administrativo():
    """No corte RBAC, somente o proprietário canônico mantém bypass administrativo."""
    if not autenticado():
        return False
    if modo_autorizacao() == MODO_LEGACY:
        return eh_administrador_sistema() or recuperacao_administrativa_ativa()
    return temporary_owner_bypass()


def pode_gerenciar_administracao():
    """Custódia temporária exclusiva do proprietário durante a migração RBAC."""
    if modo_autorizacao() == MODO_LEGACY:
        return usuario_superadmin() or recuperacao_administrativa_ativa()
    return temporary_owner_bypass()


def pode_gerenciar_usuarios_operacionais():
    """Restringe a gestão interna à mesma custódia administrativa homologada."""
    return pode_gerenciar_administracao()


def pode_gerenciar_usuarios_roles():
    """Restringe associações documentais à custódia administrativa."""
    return pode_gerenciar_administracao()


def pode_gerenciar_roles():
    """Restringe o catálogo RBAC à custódia administrativa homologada."""
    return pode_gerenciar_administracao()


def pode_gerenciar_catalogo_permissoes():
    """Restringe a manutenção do catálogo canônico à custódia administrativa."""
    return pode_gerenciar_administracao()


def possui_perfil(perfil):
    """Centraliza consultas de identidade que não representam uma permissão."""
    return autenticado() and str(perfil_global()).strip().lower() == str(perfil).strip().lower()


def pode_acessar(modulo):
    """Decide acesso de módulo usando uma única autoridade por vez."""
    if not autenticado():
        return False
    if temporary_owner_bypass():
        return True
    modo = modo_autorizacao()
    if modo == MODO_LEGACY:
        return pode_acessar_modulo(modulo)
    if modo != MODO_RBAC:
        return False
    decisao = rbac_authority.avaliar_modulo(
        usuario=st.session_state.get("usuario", ""), modulo=modulo,
    )
    _registrar_decisao(
        decisao, modulo=modulo, recurso="*", acao="*", obra_id=None,
    )
    return decisao.permitido


def pode(*, modulo, recurso="todos", acao="todos", obra_id=None):
    """Decide por RBAC ou rollback legado, sem fallback entre os modos."""
    if not autenticado():
        return False
    if temporary_owner_bypass():
        return True
    modo = modo_autorizacao()
    if modo == MODO_LEGACY:
        return bool(pode_executar(
            modulo,
            recurso=recurso,
            permissao=acao,
            obra_id="todas" if obra_id is None else obra_id,
        ))
    if modo != MODO_RBAC:
        return False
    decisao = rbac_authority.avaliar(
        usuario=st.session_state.get("usuario", ""), modulo=modulo,
        recurso=recurso, acao=acao, obra_id=obra_id,
    )
    _registrar_decisao(
        decisao, modulo=modulo, recurso=recurso, acao=acao, obra_id=obra_id,
    )
    return decisao.permitido


def pode_operar_obra(*, modulo, obra_id, recurso="todos", acao="todos"):
    """Forma explícita da decisão vinculada a uma obra."""
    if not obra_id:
        return False
    return pode(modulo=modulo, recurso=recurso, acao=acao, obra_id=obra_id)


def listar_obras_permitidas(*, modulo, recurso="todos", acao="todos"):
    """Lista escopos pela autoridade exclusiva configurada."""
    if not autenticado():
        return []
    if temporary_owner_bypass():
        return ["todas"]
    modo = modo_autorizacao()
    if modo == MODO_LEGACY:
        return obras_permitidas(modulo, recurso=recurso, permissao=acao)
    if modo != MODO_RBAC:
        return []
    return rbac_authority.listar_obras(
        usuario=st.session_state.get("usuario", ""), modulo=modulo,
        recurso=recurso, acao=acao,
    )


def pode_acessar_rota(tela):
    """Decide toda entrada de rota; rotas desconhecidas são negadas."""
    if not autenticado():
        return False

    tela = str(tela or "").strip()
    if not tela:
        return False

    if modo_autorizacao() == MODO_LEGACY and possui_perfil("funcionario") and tela not in ROTAS_FUNCIONARIO:
        return False

    if tela == "menu":
        return True

    if tela == "administracao":
        return pode_gerenciar_administracao()

    modulo = ROTAS_POR_MODULO.get(tela)
    if modulo is None:
        return False

    return pode_acessar(modulo)
