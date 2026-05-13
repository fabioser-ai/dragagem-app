import pandas as pd
import streamlit as st
import os

from services.github import carregar_github, salvar_github

from modulos.medicoes.config import (
    ARQ_OBRAS,
    ARQ_MEDICOES,
    ARQ_FRENTES,
    ARQ_MC,
    ARQ_ITENS,
    ARQ_SERVICOS,
    COL_OBRAS,
    COL_MEDICOES,
    COL_FRENTES,
    COL_MC,
    COL_ITENS,
    COL_SERVICOS,
)

from modulos.medicoes.config import (
    ARQ_TABELAS_SERVICOS_DIR,
    COL_TABELA_SERVICOS_CONTRATO,
)

# ============================================================
# CSV
# ============================================================

def carregar_csv(caminho, colunas):
    try:
        df = carregar_github(
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )

        if isinstance(df, str):
            from io import StringIO
            df = pd.read_csv(StringIO(df))

        if df is None:
            df = pd.DataFrame(columns=colunas)

    except Exception:
        df = pd.DataFrame(columns=colunas)

    for c in colunas:
        if c not in df.columns:
            df[c] = None

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


# ============================================================
# BASES
# ============================================================

def carregar_bases():
    obras = carregar_csv(ARQ_OBRAS, COL_OBRAS)

    medicoes = carregar_csv(
        ARQ_MEDICOES,
        COL_MEDICOES,
    )

    frentes = carregar_csv(
        ARQ_FRENTES,
        COL_FRENTES,
    )

    mc = carregar_csv(
        ARQ_MC,
        COL_MC,
    )

    itens = carregar_csv(
        ARQ_ITENS,
        COL_ITENS,
    )

    servicos = carregar_csv(
        ARQ_SERVICOS,
        COL_SERVICOS,
    )

    return (
        obras,
        medicoes,
        frentes,
        mc,
        itens,
        servicos,
    )

# ============================================================
# Carregar tabela contrato
# ============================================================


def carregar_tabela_contrato(nome_arquivo):
    if not nome_arquivo:
        return pd.DataFrame(
            columns=COL_TABELA_SERVICOS_CONTRATO
        )

    caminho = (
        f"{ARQ_TABELAS_SERVICOS_DIR}/{nome_arquivo}"
    )

    if not os.path.exists(caminho):
        return pd.DataFrame(
            columns=COL_TABELA_SERVICOS_CONTRATO
        )

    try:
        df = pd.read_csv(caminho)

        for c in COL_TABELA_SERVICOS_CONTRATO:
            if c not in df.columns:
                df[c] = None

        return df[COL_TABELA_SERVICOS_CONTRATO]

    except Exception as e:
        st.error(
            f"Erro ao carregar tabela contratual: {e}"
        )

        return pd.DataFrame(
            columns=COL_TABELA_SERVICOS_CONTRATO
        )
