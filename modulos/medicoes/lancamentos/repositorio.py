from io import StringIO

import pandas as pd
import streamlit as st

from services.github import carregar_github, salvar_github

from modulos.medicoes.lancamentos.config import (
    ARQ_LANCAMENTOS_PRODUCAO,
    ARQ_LOCAIS_TRABALHO,
    ARQ_USUARIOS_OBRAS,
    COL_LANCAMENTOS_PRODUCAO,
    COL_LOCAIS_TRABALHO,
    COL_USUARIOS_OBRAS,
)


def carregar_csv(caminho, colunas):
    try:
        df = carregar_github(
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )

        if isinstance(df, str):
            df = pd.read_csv(StringIO(df))

        if df is None:
            df = pd.DataFrame(columns=colunas)

    except Exception:
        df = pd.DataFrame(columns=colunas)

    for coluna in colunas:
        if coluna not in df.columns:
            df[coluna] = ""

    return df[colunas]


def salvar_csv(caminho, df):
    try:
        salvar_github(
            df,
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )
        return True

    except Exception as e:
        st.error(f"Erro ao salvar {caminho}: {e}")
        return False


def carregar_lancamentos_trabalho():
    return carregar_csv(
        ARQ_LANCAMENTOS_PRODUCAO,
        COL_LANCAMENTOS_PRODUCAO,
    )


def salvar_lancamentos_trabalho(df):
    return salvar_csv(
        ARQ_LANCAMENTOS_PRODUCAO,
        df[COL_LANCAMENTOS_PRODUCAO],
    )


def carregar_locais_trabalho():
    return carregar_csv(
        ARQ_LOCAIS_TRABALHO,
        COL_LOCAIS_TRABALHO,
    )


def salvar_locais_trabalho(df):
    return salvar_csv(
        ARQ_LOCAIS_TRABALHO,
        df[COL_LOCAIS_TRABALHO],
    )


def carregar_usuarios_obras():
    return carregar_csv(
        ARQ_USUARIOS_OBRAS,
        COL_USUARIOS_OBRAS,
    )


def salvar_usuarios_obras(df):
    return salvar_csv(
        ARQ_USUARIOS_OBRAS,
        df[COL_USUARIOS_OBRAS],
    )
