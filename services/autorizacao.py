"""Fronteira central de autorização das rotas do APP FOS."""

import streamlit as st

from services.permissoes import eh_superadmin, pode_acessar_modulo


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


def pode_acessar_rota(tela):
    """Decide toda entrada de rota; rotas desconhecidas são negadas."""
    if not st.session_state.get("autenticado", False):
        return False

    tela = str(tela or "").strip()
    if not tela:
        return False

    if st.session_state.get("perfil") == "funcionario" and tela not in ROTAS_FUNCIONARIO:
        return False

    if tela == "menu":
        return True

    if tela == "administracao":
        return eh_superadmin()

    modulo = ROTAS_POR_MODULO.get(tela)
    if modulo is None:
        return False

    return pode_acessar_modulo(modulo)
