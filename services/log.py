import base64
from datetime import datetime

import pandas as pd
import requests
import streamlit as st

from services.github import (
    ResultadoEscritaCSV,
    ResultadoLeituraCSV,
    StatusEscrita,
    StatusLeitura,
    ler_csv_github,
)


ARQUIVO_LOG = "data/log_acessos.csv"
BRANCH_LOG = "runtime/audit-log"
COLUNAS_LOG = ["data_hora", "usuario", "perfil", "acao"]


def _dataframe_log(df):
    if df is None:
        df = pd.DataFrame(columns=COLUNAS_LOG)

    df = df.copy()

    for coluna in COLUNAS_LOG:
        if coluna not in df.columns:
            df[coluna] = ""

    return df[COLUNAS_LOG]


def carregar_logs_resultado():
    resultado = ler_csv_github(
        ARQUIVO_LOG,
        st.secrets["GITHUB_TOKEN"],
        st.secrets["REPO"],
        ref=BRANCH_LOG,
    )
    dados = (
        _dataframe_log(resultado.dados)
        if resultado.leitura_confirmada
        else pd.DataFrame(columns=COLUNAS_LOG)
    )
    return ResultadoLeituraCSV(
        status=resultado.status,
        dados=dados,
        arquivo=resultado.arquivo,
        http_status=resultado.http_status,
        sha=resultado.sha,
        erro=resultado.erro,
    )


def _salvar_log_runtime(df, *, sha_esperado=None, criar=False):
    if criar and sha_esperado:
        return ResultadoEscritaCSV(
            StatusEscrita.REQUISICAO_INVALIDA,
            ARQUIVO_LOG,
            erro="Criação não aceita SHA esperado.",
        )
    if not criar and not sha_esperado:
        return ResultadoEscritaCSV(
            StatusEscrita.REQUISICAO_INVALIDA,
            ARQUIVO_LOG,
            erro="Atualização exige SHA esperado.",
        )

    url = f"https://api.github.com/repos/{st.secrets['REPO']}/contents/{ARQUIVO_LOG}"
    headers = {"Authorization": f"token {st.secrets['GITHUB_TOKEN']}"}
    content = base64.b64encode(df.to_csv(index=False).encode("utf-8")).decode("ascii")
    payload = {
        "message": f"Audit log: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "content": content,
        "branch": BRANCH_LOG,
    }
    if sha_esperado:
        payload["sha"] = sha_esperado

    try:
        response = requests.put(url, headers=headers, json=payload, timeout=(5, 20))
    except (requests.Timeout, requests.ConnectionError) as exc:
        return ResultadoEscritaCSV(
            StatusEscrita.FALHA_TEMPORARIA,
            ARQUIVO_LOG,
            erro=f"Falha temporária ao salvar log: {exc.__class__.__name__}",
        )
    except requests.RequestException as exc:
        return ResultadoEscritaCSV(
            StatusEscrita.ERRO_DESCONHECIDO,
            ARQUIVO_LOG,
            erro=f"Erro de comunicação ao salvar log: {exc.__class__.__name__}",
        )

    http_status = response.status_code
    if http_status in (200, 201):
        sha_resultante = None
        try:
            payload_resposta = response.json()
            conteudo = payload_resposta.get("content") if isinstance(payload_resposta, dict) else None
            if isinstance(conteudo, dict):
                sha_resultante = conteudo.get("sha")
        except ValueError:
            pass
        return ResultadoEscritaCSV(
            StatusEscrita.SUCESSO_CRIADO if http_status == 201 else StatusEscrita.SUCESSO_ATUALIZADO,
            ARQUIVO_LOG,
            http_status=http_status,
            sha=sha_resultante,
        )
    if http_status in (401, 403):
        return ResultadoEscritaCSV(
            StatusEscrita.NAO_AUTORIZADO,
            ARQUIVO_LOG,
            http_status=http_status,
            erro="Escrita do log não autorizada pelo GitHub.",
        )
    if http_status == 409:
        return ResultadoEscritaCSV(
            StatusEscrita.CONFLITO,
            ARQUIVO_LOG,
            http_status=http_status,
            erro="O log foi alterado desde a leitura confirmada.",
        )
    if http_status in (422, 429):
        return ResultadoEscritaCSV(
            StatusEscrita.LIMITE_OU_VALIDACAO,
            ARQUIVO_LOG,
            http_status=http_status,
            erro="O GitHub recusou a escrita do log por validação ou limite.",
        )
    if 500 <= http_status <= 599:
        return ResultadoEscritaCSV(
            StatusEscrita.FALHA_TEMPORARIA,
            ARQUIVO_LOG,
            http_status=http_status,
            erro="GitHub temporariamente indisponível para escrita do log.",
        )
    return ResultadoEscritaCSV(
        StatusEscrita.ERRO_DESCONHECIDO,
        ARQUIVO_LOG,
        http_status=http_status,
        erro="Resposta HTTP inesperada ao salvar log.",
    )


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
        ref=BRANCH_LOG,
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
        return _salvar_log_runtime(
            df_atualizado,
            sha_esperado=resultado_leitura.sha,
        )

    if resultado_leitura.status == StatusLeitura.ARQUIVO_INEXISTENTE:
        df_inicial = pd.DataFrame([registro], columns=COLUNAS_LOG)
        return _salvar_log_runtime(df_inicial, criar=True)

    return resultado_leitura
