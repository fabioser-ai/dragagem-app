"""Autoridade central de identidade e autorização do APP FOS.

Os módulos informam o contexto da decisão; somente esta camada interpreta a
sessão e delega a avaliação das permissões persistidas ao modelo legado.
"""

import streamlit as st

from services.permissoes import (
    eh_administrador_sistema,
    eh_superadmin,
    obras_permitidas,
    perfil_global,
    pode_acessar_modulo,
    pode_executar,
)


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


def autenticado():
    """Retorna se há uma identidade autenticada válida na sessão corrente."""
    return bool(st.session_state.get("autenticado", False))


def usuario_superadmin():
    """Reconhece o superadmin somente dentro de uma sessão autenticada."""
    return autenticado() and eh_superadmin()


def possui_privilegio_administrativo():
    """Reconhece admin operacional e superadmin, preservando sua distinção."""
    return autenticado() and eh_administrador_sistema()


def possui_perfil(perfil):
    """Centraliza consultas de identidade que não representam uma permissão."""
    return autenticado() and str(perfil_global()).strip().lower() == str(perfil).strip().lower()


def pode_acessar(modulo):
    """Decide o acesso global a um módulo, com negação por padrão."""
    return autenticado() and pode_acessar_modulo(modulo)


def pode(*, modulo, recurso="todos", acao="todos", obra_id=None):
    """Decide uma autorização de ação/recurso/obra pela fonte de verdade atual."""
    if not autenticado():
        return False
    return bool(
        pode_executar(
            modulo,
            recurso=recurso,
            permissao=acao,
            obra_id="todas" if obra_id is None else obra_id,
        )
    )


def pode_operar_obra(*, modulo, obra_id, recurso="todos", acao="todos"):
    """Forma explícita da decisão vinculada a uma obra."""
    if not obra_id:
        return False
    return pode(modulo=modulo, recurso=recurso, acao=acao, obra_id=obra_id)


def listar_obras_permitidas(*, modulo, recurso="todos", acao="todos"):
    """Expõe o recorte legado por obra sem duplicar sua interpretação."""
    if not autenticado():
        return []
    return obras_permitidas(modulo, recurso=recurso, permissao=acao)


def pode_acessar_rota(tela):
    """Decide toda entrada de rota; rotas desconhecidas são negadas."""
    if not autenticado():
        return False

    tela = str(tela or "").strip()
    if not tela:
        return False

    if possui_perfil("funcionario") and tela not in ROTAS_FUNCIONARIO:
        return False

    if tela == "menu":
        return True

    if tela == "administracao":
        return usuario_superadmin()

    modulo = ROTAS_POR_MODULO.get(tela)
    if modulo is None:
        return False

    return pode_acessar(modulo)
