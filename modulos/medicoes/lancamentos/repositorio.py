import pandas as pd

from modulos.medicoes.lancamentos.config import (
    ARQUIVO_LANCAMENTOS_TRABALHO,
    ARQUIVO_LOCAIS_TRABALHO,
    COLUNAS_LANCAMENTOS_TRABALHO,
    COLUNAS_LOCAIS_TRABALHO,
)
from modulos.medicoes.utils import dataframe_vazio

try:
    from core.github_storage import carregar_csv_github, salvar_csv_github
except ImportError:
    carregar_csv_github = None
    salvar_csv_github = None


def carregar_csv(caminho, colunas):
    if carregar_csv_github:
        return carregar_csv_github(caminho, colunas)

    try:
        return pd.read_csv(caminho, dtype=str, encoding="utf-8-sig")
    except FileNotFoundError:
        return dataframe_vazio(colunas)
    except pd.errors.EmptyDataError:
        return dataframe_vazio(colunas)


def salvar_csv(df, caminho):
    if salvar_csv_github:
        salvar_csv_github(df, caminho)
        return

    df.to_csv(caminho, index=False, encoding="utf-8-sig")


def carregar_lancamentos_trabalho():
    return carregar_csv(
        ARQUIVO_LANCAMENTOS_TRABALHO,
        COLUNAS_LANCAMENTOS_TRABALHO,
    )


def salvar_lancamentos_trabalho(df):
    salvar_csv(
        df,
        ARQUIVO_LANCAMENTOS_TRABALHO,
    )


def carregar_locais_trabalho():
    return carregar_csv(
        ARQUIVO_LOCAIS_TRABALHO,
        COLUNAS_LOCAIS_TRABALHO,
    )


def salvar_locais_trabalho(df):
    salvar_csv(
        df,
        ARQUIVO_LOCAIS_TRABALHO,
    )
