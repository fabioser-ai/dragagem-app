"""Compatibilidade de Medições com a autoridade central de autorização."""

import pandas as pd
import streamlit as st

from services.autorizacao import listar_obras_permitidas, pode, pode_acessar


def obter_usuario_logado():
    return str(st.session_state.get("usuario") or "").strip().casefold()


def carregar_vinculos_usuario():
    """Visão compatível derivada da autoridade; nunca consulta usuarios_obras."""
    obras = listar_obras_permitidas(
        modulo="medicoes", recurso="lancamento", acao="visualizar"
    )
    return pd.DataFrame([
        {"usuario_id": obter_usuario_logado(), "obra_id": obra,
         "perfil_medicao": obter_perfil_medicao(), "ativo": "sim"}
        for obra in obras
    ])


def obter_perfil_medicao():
    """Rótulo visual compatível, inferido das concessões efetivas."""
    if acesso_total_medicoes() or pode_criar_medicao():
        return "admin"
    if pode_aprovar_lancamentos():
        return "aprovador"
    if pode_visualizar_lancamentos():
        return "encarregado"
    if pode_lancar_trabalho():
        return "funcionario"
    return None


def tem_acesso_medicoes():
    return pode_acessar("medicoes")


def pode_lancar_trabalho(obra_id=None):
    return pode(modulo="medicoes", recurso="lancamento", acao="criar", obra_id=obra_id)


def pode_visualizar_lancamentos(obra_id=None):
    return pode(modulo="medicoes", recurso="lancamento", acao="visualizar", obra_id=obra_id)


def pode_aprovar_lancamentos(obra_id=None):
    return pode(modulo="medicoes", recurso="lancamento", acao="aprovar", obra_id=obra_id)


def pode_criar_medicao(obra_id=None):
    return pode(modulo="medicoes", recurso="medicao", acao="criar", obra_id=obra_id)


def acesso_total_medicoes(obra_id=None):
    return pode(modulo="medicoes", recurso="medicao", acao="editar", obra_id=obra_id)
