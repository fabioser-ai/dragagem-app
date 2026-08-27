"""Roteamento de persistência do módulo Medições por classificação de dado."""

import base64

import requests

from modulos.medicoes.config import (
    ARQ_FRENTES,
    ARQ_ITENS,
    ARQ_LANCAMENTOS_PRODUCAO,
    ARQ_LOCAIS_TRABALHO,
    ARQ_MC,
    ARQ_MEDICOES,
    ARQ_OBRAS,
)
from services.dados_operacionais import ler_csv_operacional, salvar_csv_operacional
from services.github import (
    DEFAULT_REQUEST_TIMEOUT,
    StatusLeitura,
    carregar_github as carregar_github_main,
    salvar_github as salvar_github_main,
)


DATA_BRANCH = "data-operacional"

ARQUIVOS_OPERACIONAIS = frozenset({
    ARQ_OBRAS,
    ARQ_MEDICOES,
    ARQ_FRENTES,
    ARQ_MC,
    ARQ_ITENS,
    ARQ_LOCAIS_TRABALHO,
    ARQ_LANCAMENTOS_PRODUCAO,
})


def arquivo_operacional(caminho):
    return caminho in ARQUIVOS_OPERACIONAIS


def carregar_github(caminho, token, repo):
    if not arquivo_operacional(caminho):
        return carregar_github_main(caminho, token, repo)

    resultado = ler_csv_operacional(caminho, token, repo)
    if resultado.leitura_confirmada:
        return resultado.dados
    if resultado.status == StatusLeitura.ARQUIVO_INEXISTENTE:
        return None
    raise RuntimeError(
        f"Leitura operacional de {caminho} não confirmada; escrita bloqueada."
    )


def salvar_github(df, caminho, token, repo):
    if not arquivo_operacional(caminho):
        return salvar_github_main(df, caminho, token, repo)

    leitura = ler_csv_operacional(caminho, token, repo)
    if leitura.pode_sobrescrever:
        resultado = salvar_csv_operacional(
            df,
            caminho,
            token,
            repo,
            sha_esperado=leitura.sha,
        )
    elif leitura.status == StatusLeitura.ARQUIVO_INEXISTENTE:
        resultado = salvar_csv_operacional(
            df,
            caminho,
            token,
            repo,
            criar=True,
        )
    else:
        raise RuntimeError(
            f"Leitura operacional de {caminho} não autorizou a escrita."
        )

    if not resultado.sucesso:
        raise RuntimeError(resultado.erro or f"Erro ao salvar {caminho}.")
    return resultado


def salvar_arquivo_github(
    conteudo_bytes,
    caminho,
    token,
    repo,
    mensagem=None,
    timeout=DEFAULT_REQUEST_TIMEOUT,
):
    url = f"https://api.github.com/repos/{repo}/contents/{caminho}"
    headers = {"Authorization": f"token {token}"}
    atual = requests.get(
        url,
        headers=headers,
        params={"ref": DATA_BRANCH},
        timeout=timeout,
    )
    sha = atual.json().get("sha") if atual.status_code == 200 else None
    payload = {
        "message": mensagem or f"Upload {caminho}",
        "content": base64.b64encode(conteudo_bytes).decode("ascii"),
        "branch": DATA_BRANCH,
    }
    if sha:
        payload["sha"] = sha

    resposta = requests.put(
        url,
        headers=headers,
        json=payload,
        timeout=timeout,
    )
    if resposta.status_code not in (200, 201):
        raise RuntimeError("Erro ao salvar foto na branch operacional.")
    return caminho
