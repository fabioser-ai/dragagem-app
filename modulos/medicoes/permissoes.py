import streamlit as st
import pandas as pd

from modulos.medicoes.repositorio import carregar_usuarios_obras


def _normalizar_texto(valor):
    if valor is None:
        return ""
    return str(valor).strip().lower()


def obter_usuario_logado():
    """
    Tenta identificar o usuário logado usando as chaves já existentes no app.
    """
    possiveis_chaves = [
        "usuario",
        "email",
        "usuario_email",
        "user_email",
        "login",
    ]

    for chave in possiveis_chaves:
        valor = st.session_state.get(chave)
        if valor:
            return _normalizar_texto(valor)

    return ""


def carregar_vinculos_usuario():
    """
    Carrega vínculos ativos do usuário logado em usuarios_obras.csv.
    Aceita correspondência por usuario_id, email ou nome.
    """
    usuario = obter_usuario_logado()

    if not usuario:
        return pd.DataFrame()

    df = carregar_usuarios_obras()

    if df is None or df.empty:
        return pd.DataFrame()

    df = df.copy()

    for coluna in ["usuario_id", "email", "nome", "perfil_medicao", "ativo", "obra_id"]:
        if coluna not in df.columns:
            df[coluna] = ""

    df["usuario_id"] = df["usuario_id"].apply(_normalizar_texto)
    df["email"] = df["email"].apply(_normalizar_texto)
    df["nome"] = df["nome"].apply(_normalizar_texto)
    df["perfil_medicao"] = df["perfil_medicao"].apply(_normalizar_texto)
    df["ativo"] = df["ativo"].apply(_normalizar_texto)
    df["obra_id"] = df["obra_id"].apply(_normalizar_texto)

    df_ativo = df[
        (
            (df["usuario_id"] == usuario)
            | (df["email"] == usuario)
            | (df["nome"] == usuario)
        )
        & (df["ativo"].isin(["sim", "s", "true", "1", "ativo"]))
    ].copy()

    return df_ativo


def obter_perfil_medicao():
    """
    Retorna o maior perfil de medição do usuário.
    Ordem de prioridade:
    admin > aprovador > encarregado > funcionario
    """
    vinculos = carregar_vinculos_usuario()

    if vinculos.empty:
        return None

    perfis = set(vinculos["perfil_medicao"].dropna().astype(str).str.lower().str.strip())

    if "admin" in perfis:
        return "admin"
    if "aprovador" in perfis:
        return "aprovador"
    if "encarregado" in perfis:
        return "encarregado"
    if "funcionario" in perfis:
        return "funcionario"

    return None


def tem_acesso_medicoes():
    return obter_perfil_medicao() is not None


def pode_lancar_trabalho():
    return obter_perfil_medicao() in [
        "funcionario",
        "encarregado",
        "aprovador",
        "admin",
    ]


def pode_visualizar_lancamentos():
    return obter_perfil_medicao() in [
        "encarregado",
        "aprovador",
        "admin",
    ]


def pode_aprovar_lancamentos():
    return obter_perfil_medicao() in [
        "aprovador",
        "admin",
    ]


def pode_criar_medicao():
    return obter_perfil_medicao() in [
        "admin",
    ]


def acesso_total_medicoes():
    return obter_perfil_medicao() == "admin"
