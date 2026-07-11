from datetime import datetime

import pandas as pd
import streamlit as st

from services.github import (
    StatusLeitura,
    ler_csv_github,
    salvar_csv_github,
)


ARQUIVO_LOG = "data/log_acessos.csv"
COLUNAS_LOG = ["data_hora", "usuario", "perfil", "acao"]


def _dataframe_log(df):
    if df is None:
        df = pd.DataFrame(columns=COLUNAS_LOG)

    df = df.copy()

    for coluna in COLUNAS_LOG:
        if coluna not in df.columns:
            df[coluna] = ""

    return df[COLUNAS_LOG]


def registrar_log(usuario, perfil, acao):
    registro = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario": usuario,
        "perfil": perfil,
        "acao": acao,
    }

    resultado_leitura = ler_csv_github(
        ARQUIVO_LOG,
        st.secrets["GITHUB_TOKEN"],
        st.secrets["REPO"],
    )

    if resultado_leitura.status in {
        StatusLeitura.SUCESSO_COM_DADOS,
        StatusLeitura.SUCESSO_VAZIO,
    }:
        df = _dataframe_log(resultado_leitura.dados)
        df_atualizado = pd.concat(
            [df, pd.DataFrame([registro])],
            ignore_index=True,
        )

        return salvar_csv_github(
            df_atualizado,
            ARQUIVO_LOG,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
            sha_esperado=resultado_leitura.sha,
        )

    if resultado_leitura.status == StatusLeitura.ARQUIVO_INEXISTENTE:
        df_inicial = pd.DataFrame([registro], columns=COLUNAS_LOG)

        return salvar_csv_github(
            df_inicial,
            ARQUIVO_LOG,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
            criar=True,
        )

    return resultado_leitura
