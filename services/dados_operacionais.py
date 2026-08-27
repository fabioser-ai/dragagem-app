import base64

import pandas as pd
import requests

from services.github import (
    DEFAULT_REQUEST_TIMEOUT,
    ResultadoEscritaCSV,
    StatusEscrita,
    ler_csv_github,
)


DATA_BRANCH = "data-operacional"


def ler_csv_operacional(arquivo, token, repo, timeout=DEFAULT_REQUEST_TIMEOUT):
    """Lê dados mutáveis exclusivamente da branch operacional."""
    return ler_csv_github(
        arquivo,
        token,
        repo,
        timeout=timeout,
        ref=DATA_BRANCH,
    )


def salvar_csv_operacional(
    df,
    arquivo,
    token,
    repo,
    *,
    sha_esperado=None,
    criar=False,
    mensagem=None,
    timeout=DEFAULT_REQUEST_TIMEOUT,
):
    """Cria/atualiza CSV na branch operacional sem tocar a branch de deploy."""
    if criar and sha_esperado:
        return ResultadoEscritaCSV(
            status=StatusEscrita.REQUISICAO_INVALIDA,
            arquivo=arquivo,
            erro="Criação não aceita SHA esperado.",
        )
    if not criar and not sha_esperado:
        return ResultadoEscritaCSV(
            status=StatusEscrita.REQUISICAO_INVALIDA,
            arquivo=arquivo,
            erro="Atualização exige SHA esperado da leitura confirmada.",
        )

    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"
    headers = {"Authorization": f"token {token}"}
    csv_string = df.to_csv(index=False)
    content = base64.b64encode(csv_string.encode("utf-8")).decode("ascii")
    data = {
        "message": mensagem or (f"Create {arquivo}" if criar else f"Update {arquivo}"),
        "content": content,
        "branch": DATA_BRANCH,
    }
    if sha_esperado:
        data["sha"] = sha_esperado

    try:
        response = requests.put(url, headers=headers, json=data, timeout=timeout)
    except (requests.Timeout, requests.ConnectionError) as exc:
        return ResultadoEscritaCSV(
            status=StatusEscrita.FALHA_TEMPORARIA,
            arquivo=arquivo,
            erro=f"Falha temporária ao salvar o arquivo: {exc.__class__.__name__}",
        )
    except requests.RequestException as exc:
        return ResultadoEscritaCSV(
            status=StatusEscrita.ERRO_DESCONHECIDO,
            arquivo=arquivo,
            erro=f"Erro de comunicação ao salvar o arquivo: {exc.__class__.__name__}",
        )
    except Exception as exc:
        return ResultadoEscritaCSV(
            status=StatusEscrita.ERRO_DESCONHECIDO,
            arquivo=arquivo,
            erro=f"Erro inesperado ao salvar o arquivo: {exc.__class__.__name__}",
        )

    http_status = response.status_code
    if http_status in (200, 201):
        sha_resultante = None
        try:
            payload = response.json()
            conteudo = payload.get("content") if isinstance(payload, dict) else None
            if isinstance(conteudo, dict):
                sha_resultante = conteudo.get("sha")
        except ValueError:
            pass
        return ResultadoEscritaCSV(
            status=(StatusEscrita.SUCESSO_CRIADO if http_status == 201 else StatusEscrita.SUCESSO_ATUALIZADO),
            arquivo=arquivo,
            http_status=http_status,
            sha=sha_resultante,
        )
    if http_status in (401, 403):
        return ResultadoEscritaCSV(
            status=StatusEscrita.NAO_AUTORIZADO,
            arquivo=arquivo,
            http_status=http_status,
            erro="Escrita não autorizada pelo GitHub.",
        )
    if http_status == 409:
        return ResultadoEscritaCSV(
            status=StatusEscrita.CONFLITO,
            arquivo=arquivo,
            http_status=http_status,
            erro="O arquivo foi alterado desde a leitura confirmada.",
        )
    if http_status in (422, 429):
        return ResultadoEscritaCSV(
            status=StatusEscrita.LIMITE_OU_VALIDACAO,
            arquivo=arquivo,
            http_status=http_status,
            erro="O GitHub recusou a escrita por validação ou limite.",
        )
    if 500 <= http_status <= 599:
        return ResultadoEscritaCSV(
            status=StatusEscrita.FALHA_TEMPORARIA,
            arquivo=arquivo,
            http_status=http_status,
            erro="O GitHub está temporariamente indisponível para esta escrita.",
        )
    return ResultadoEscritaCSV(
        status=StatusEscrita.ERRO_DESCONHECIDO,
        arquivo=arquivo,
        http_status=http_status,
        erro="Resposta HTTP inesperada ao salvar o arquivo.",
    )
