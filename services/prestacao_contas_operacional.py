import base64

import requests

from services.dados_operacionais import ler_csv_operacional, salvar_csv_operacional
from services.github import DEFAULT_REQUEST_TIMEOUT


DATA_BRANCH = "data-operacional"


def carregar_csv(arquivo, token, repo):
    resultado = ler_csv_operacional(arquivo, token, repo)
    return resultado.dados if resultado.leitura_confirmada else None


def salvar_csv(df, arquivo, token, repo):
    leitura = ler_csv_operacional(arquivo, token, repo)
    if leitura.pode_sobrescrever:
        resultado = salvar_csv_operacional(df, arquivo, token, repo, sha_esperado=leitura.sha)
    elif leitura.status.value == "arquivo_inexistente":
        resultado = salvar_csv_operacional(df, arquivo, token, repo, criar=True)
    else:
        return False
    return resultado.sucesso


def salvar_arquivo(conteudo_bytes, arquivo, token, repo, mensagem=None, timeout=DEFAULT_REQUEST_TIMEOUT):
    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"
    headers = {"Authorization": f"token {token}"}
    atual = requests.get(url, headers=headers, params={"ref": DATA_BRANCH}, timeout=timeout)
    sha = atual.json().get("sha") if atual.status_code == 200 else None
    data = {
        "message": mensagem or f"Upload {arquivo}",
        "content": base64.b64encode(conteudo_bytes).decode("ascii"),
        "branch": DATA_BRANCH,
    }
    if sha:
        data["sha"] = sha
    response = requests.put(url, headers=headers, json=data, timeout=timeout)
    if response.status_code not in (200, 201):
        raise RuntimeError("Erro ao salvar comprovante na branch operacional.")
    return arquivo


def carregar_arquivo(arquivo, token, repo, timeout=DEFAULT_REQUEST_TIMEOUT):
    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers, params={"ref": DATA_BRANCH}, timeout=timeout)
    if response.status_code != 200:
        return None
    dados = response.json()
    content = dados.get("content")
    if content:
        return base64.b64decode(content)
    download_url = dados.get("download_url")
    if download_url:
        raw = requests.get(download_url, headers=headers, timeout=timeout)
        if raw.status_code == 200:
            return raw.content
    return None
