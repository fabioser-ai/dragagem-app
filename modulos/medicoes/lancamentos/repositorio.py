from io import StringIO
from uuid import uuid4
from datetime import datetime

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


# =========================================================
# UTILITÁRIOS
# =========================================================

def agora_iso():
    return datetime.now().isoformat(timespec="seconds")


def gerar_id(prefixo):
    return f"{prefixo}_{uuid4().hex[:8]}"


# =========================================================
# CSV GENÉRICO
# =========================================================

def carregar_csv(caminho, colunas):
    try:
        df = carregar_github(
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )

        if isinstance(df, str):
            df = pd.read_csv(
                StringIO(df),
                dtype=str,
            )

        if df is None:
            df = pd.DataFrame(columns=colunas)

    except Exception:
        df = pd.DataFrame(columns=colunas)

    df = df.fillna("")

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


# =========================================================
# LANÇAMENTOS DE TRABALHO
# =========================================================

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


# =========================================================
# LOCAIS DE TRABALHO
# =========================================================

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


def listar_locais_por_obra(obra_id):
    df = carregar_locais_trabalho()

    if df.empty:
        return df

    df = df.fillna("").copy()

    locais = df[
        (df["obra_id"].astype(str) == str(obra_id))
        &
        (
            df["ativo"]
            .astype(str)
            .str.strip()
            .str.lower()
            .isin(["sim", "s", "true", "1", "ativo", ""])
        )
    ].copy()

    if not locais.empty:
        locais = locais.sort_values("nome_local")

    return locais


def buscar_local_por_id(local_id):
    df = carregar_locais_trabalho()

    if df.empty:
        return None

    filtro = (
        df["local_id"]
        .astype(str)
        == str(local_id)
    )

    if not filtro.any():
        return None

    return df.loc[filtro].iloc[0].to_dict()


def criar_local_trabalho(
    obra_id,
    nome_local,
    observacoes="",
):
    nome_local = str(nome_local).strip()

    if not nome_local:
        return False, "Informe o nome do local."

    df = carregar_locais_trabalho()

    if not df.empty:

        duplicado = df[
            (df["obra_id"].astype(str) == str(obra_id))
            &
            (
                df["nome_local"]
                .astype(str)
                .str.strip()
                .str.lower()
                == nome_local.lower()
            )
        ]

        if not duplicado.empty:
            return True, duplicado.iloc[0].to_dict()

    novo_local = {
        "local_id": gerar_id("LOC"),
        "obra_id": str(obra_id),
        "nome_local": nome_local,
        "ativo": "sim",
        "observacoes": str(observacoes).strip(),
        "criado_em": agora_iso(),
        "atualizado_em": agora_iso(),
    }

    df = pd.concat(
        [
            df,
            pd.DataFrame([novo_local]),
        ],
        ignore_index=True,
    )

    sucesso = salvar_locais_trabalho(df)

    if not sucesso:
        return False, "Erro ao salvar local."

    return True, novo_local


# =========================================================
# USUÁRIOS x OBRAS
# =========================================================

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
