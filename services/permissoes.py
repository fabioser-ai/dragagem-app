from io import StringIO

import pandas as pd
import streamlit as st

from services.github import carregar_github, salvar_github


ARQ_PERMISSOES = "data/permissoes_usuarios.csv"

COL_PERMISSOES = [
    "usuario",
    "modulo",
    "recurso",
    "permissao",
    "obra_id",
    "ativo",
]


def _normalizar(valor):
    if valor is None:
        return ""
    return str(valor).strip().lower()


def carregar_permissoes():
    try:
        df = carregar_github(
            ARQ_PERMISSOES,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )

        if isinstance(df, str):
            df = pd.read_csv(StringIO(df))

        if df is None:
            df = pd.DataFrame(columns=COL_PERMISSOES)

    except Exception:
        df = pd.DataFrame(columns=COL_PERMISSOES)

    for coluna in COL_PERMISSOES:
        if coluna not in df.columns:
            df[coluna] = ""

    return df[COL_PERMISSOES]


def salvar_permissoes(df):
    return salvar_github(
        df[COL_PERMISSOES],
        ARQ_PERMISSOES,
        st.secrets["GITHUB_TOKEN"],
        st.secrets["REPO"],
    )


def usuario_logado():
    return st.session_state.get("usuario", "")


def perfil_global():
    return st.session_state.get("perfil", "")


def eh_superadmin():
    return _normalizar(perfil_global()) == "superadmin"


def permissoes_usuario(usuario=None):
    if usuario is None:
        usuario = usuario_logado()

    df = carregar_permissoes()

    if df.empty:
        return df

    usuario_norm = _normalizar(usuario)

    df = df.copy()
    df["usuario_norm"] = df["usuario"].apply(_normalizar)
    df["ativo_norm"] = df["ativo"].apply(_normalizar)

    return df[
        (df["usuario_norm"] == usuario_norm)
        & (df["ativo_norm"].isin(["sim", "s", "true", "1", "ativo"]))
    ].copy()


def pode_acessar_modulo(modulo):
    if eh_superadmin():
        return True

    df = permissoes_usuario()

    if df.empty:
        return False

    modulo = _normalizar(modulo)

    df["modulo_norm"] = df["modulo"].apply(_normalizar)

    return (
        ((df["modulo_norm"] == "todos") | (df["modulo_norm"] == modulo))
        .any()
    )


def pode_executar(modulo, recurso="todos", permissao="todos", obra_id="todas"):
    if eh_superadmin():
        return True

    df = permissoes_usuario()

    if df.empty:
        return False

    modulo = _normalizar(modulo)
    recurso = _normalizar(recurso)
    permissao = _normalizar(permissao)
    obra_id = _normalizar(obra_id)

    df = df.copy()
    df["modulo_norm"] = df["modulo"].apply(_normalizar)
    df["recurso_norm"] = df["recurso"].apply(_normalizar)
    df["permissao_norm"] = df["permissao"].apply(_normalizar)
    df["obra_norm"] = df["obra_id"].apply(_normalizar)

    filtro_modulo = (df["modulo_norm"] == "todos") | (df["modulo_norm"] == modulo)
    filtro_recurso = (df["recurso_norm"] == "todos") | (df["recurso_norm"] == recurso)
    filtro_permissao = (df["permissao_norm"] == "todos") | (df["permissao_norm"] == permissao)
    filtro_obra = (df["obra_norm"] == "todas") | (df["obra_norm"] == obra_id)

    return (filtro_modulo & filtro_recurso & filtro_permissao & filtro_obra).any()


def obras_permitidas(modulo, recurso="todos", permissao="todos"):
    if eh_superadmin():
        return ["todas"]

    df = permissoes_usuario()

    if df.empty:
        return []

    modulo = _normalizar(modulo)
    recurso = _normalizar(recurso)
    permissao = _normalizar(permissao)

    df = df.copy()
    df["modulo_norm"] = df["modulo"].apply(_normalizar)
    df["recurso_norm"] = df["recurso"].apply(_normalizar)
    df["permissao_norm"] = df["permissao"].apply(_normalizar)
    df["obra_norm"] = df["obra_id"].apply(_normalizar)

    filtro = (
        ((df["modulo_norm"] == "todos") | (df["modulo_norm"] == modulo))
        & ((df["recurso_norm"] == "todos") | (df["recurso_norm"] == recurso))
        & ((df["permissao_norm"] == "todos") | (df["permissao_norm"] == permissao))
    )

    obras = df.loc[filtro, "obra_id"].dropna().astype(str).str.strip().unique().tolist()

    return obras
