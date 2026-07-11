import base64
from dataclasses import dataclass
from enum import Enum
from io import StringIO
from typing import Optional

import pandas as pd
import requests


DEFAULT_REQUEST_TIMEOUT = (5, 20)


class StatusLeitura(str, Enum):
    SUCESSO_COM_DADOS = "sucesso_com_dados"
    SUCESSO_VAZIO = "sucesso_vazio"
    ARQUIVO_INEXISTENTE = "arquivo_inexistente"
    NAO_AUTORIZADO = "nao_autorizado"
    CONFLITO_OU_LIMITE = "conflito_ou_limite"
    FALHA_TEMPORARIA = "falha_temporaria"
    CONTEUDO_INVALIDO = "conteudo_invalido"
    ERRO_DESCONHECIDO = "erro_desconhecido"


@dataclass(frozen=True)
class ResultadoLeituraCSV:
    status: StatusLeitura
    dados: pd.DataFrame
    arquivo: str
    http_status: Optional[int] = None
    sha: Optional[str] = None
    erro: Optional[str] = None

    @property
    def leitura_confirmada(self) -> bool:
        return self.status in {
            StatusLeitura.SUCESSO_COM_DADOS,
            StatusLeitura.SUCESSO_VAZIO,
            StatusLeitura.ARQUIVO_INEXISTENTE,
        }

    @property
    def pode_sobrescrever(self) -> bool:
        return self.status in {
            StatusLeitura.SUCESSO_COM_DADOS,
            StatusLeitura.SUCESSO_VAZIO,
        }


def _resultado_leitura(
    *,
    status,
    arquivo,
    dados=None,
    http_status=None,
    sha=None,
    erro=None,
):
    return ResultadoLeituraCSV(
        status=status,
        dados=dados if dados is not None else pd.DataFrame(),
        arquivo=arquivo,
        http_status=http_status,
        sha=sha,
        erro=erro,
    )


def ler_csv_github(
    arquivo,
    token,
    repo,
    timeout=DEFAULT_REQUEST_TIMEOUT,
):
    """Lê um CSV do GitHub e retorna um resultado explícito e classificado.

    Esta função não substitui ainda ``carregar_github``. Ela existe para a
    migração gradual dos chamadores que precisam distinguir arquivo vazio de
    falha de leitura e preservar o SHA observado para escrita concorrente.
    """

    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"
    headers = {"Authorization": f"token {token}"}

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
    except (requests.Timeout, requests.ConnectionError) as exc:
        return _resultado_leitura(
            status=StatusLeitura.FALHA_TEMPORARIA,
            arquivo=arquivo,
            erro=f"Falha temporária ao ler o arquivo: {exc.__class__.__name__}",
        )
    except requests.RequestException as exc:
        return _resultado_leitura(
            status=StatusLeitura.ERRO_DESCONHECIDO,
            arquivo=arquivo,
            erro=f"Erro de comunicação ao ler o arquivo: {exc.__class__.__name__}",
        )
    except Exception as exc:
        return _resultado_leitura(
            status=StatusLeitura.ERRO_DESCONHECIDO,
            arquivo=arquivo,
            erro=f"Erro inesperado ao ler o arquivo: {exc.__class__.__name__}",
        )

    http_status = response.status_code

    if http_status == 404:
        return _resultado_leitura(
            status=StatusLeitura.ARQUIVO_INEXISTENTE,
            arquivo=arquivo,
            http_status=http_status,
        )

    if http_status in (401, 403):
        return _resultado_leitura(
            status=StatusLeitura.NAO_AUTORIZADO,
            arquivo=arquivo,
            http_status=http_status,
            erro="Leitura não autorizada pelo GitHub.",
        )

    if http_status in (409, 422, 429):
        return _resultado_leitura(
            status=StatusLeitura.CONFLITO_OU_LIMITE,
            arquivo=arquivo,
            http_status=http_status,
            erro="O GitHub recusou temporariamente a leitura por conflito ou limite.",
        )

    if 500 <= http_status <= 599:
        return _resultado_leitura(
            status=StatusLeitura.FALHA_TEMPORARIA,
            arquivo=arquivo,
            http_status=http_status,
            erro="O GitHub está temporariamente indisponível para esta leitura.",
        )

    if http_status != 200:
        return _resultado_leitura(
            status=StatusLeitura.ERRO_DESCONHECIDO,
            arquivo=arquivo,
            http_status=http_status,
            erro="Resposta HTTP inesperada ao ler o arquivo.",
        )

    try:
        payload = response.json()
    except ValueError:
        return _resultado_leitura(
            status=StatusLeitura.CONTEUDO_INVALIDO,
            arquivo=arquivo,
            http_status=http_status,
            erro="Resposta JSON inválida recebida do GitHub.",
        )

    if not isinstance(payload, dict):
        return _resultado_leitura(
            status=StatusLeitura.CONTEUDO_INVALIDO,
            arquivo=arquivo,
            http_status=http_status,
            erro="Estrutura de resposta inesperada recebida do GitHub.",
        )

    sha = payload.get("sha")
    content = payload.get("content")
    size = payload.get("size")

    if not content:
        if size == 0:
            return _resultado_leitura(
                status=StatusLeitura.SUCESSO_VAZIO,
                arquivo=arquivo,
                http_status=http_status,
                sha=sha,
            )

        return _resultado_leitura(
            status=StatusLeitura.CONTEUDO_INVALIDO,
            arquivo=arquivo,
            http_status=http_status,
            sha=sha,
            erro="Conteúdo ausente em resposta de arquivo não vazio.",
        )

    try:
        decoded_bytes = base64.b64decode(content, validate=True)
        decoded = decoded_bytes.decode("utf-8")
    except (ValueError, UnicodeDecodeError, base64.binascii.Error):
        return _resultado_leitura(
            status=StatusLeitura.CONTEUDO_INVALIDO,
            arquivo=arquivo,
            http_status=http_status,
            sha=sha,
            erro="Conteúdo base64 ou UTF-8 inválido.",
        )

    if decoded.strip() == "":
        return _resultado_leitura(
            status=StatusLeitura.SUCESSO_VAZIO,
            arquivo=arquivo,
            http_status=http_status,
            sha=sha,
        )

    try:
        dados = pd.read_csv(StringIO(decoded))
    except (pd.errors.ParserError, pd.errors.EmptyDataError, UnicodeDecodeError, ValueError):
        return _resultado_leitura(
            status=StatusLeitura.CONTEUDO_INVALIDO,
            arquivo=arquivo,
            http_status=http_status,
            sha=sha,
            erro="CSV inválido ou incompatível com a leitura esperada.",
        )
    except Exception as exc:
        return _resultado_leitura(
            status=StatusLeitura.ERRO_DESCONHECIDO,
            arquivo=arquivo,
            http_status=http_status,
            sha=sha,
            erro=f"Erro inesperado ao interpretar o CSV: {exc.__class__.__name__}",
        )

    status = (
        StatusLeitura.SUCESSO_VAZIO
        if dados.empty
        else StatusLeitura.SUCESSO_COM_DADOS
    )

    return _resultado_leitura(
        status=status,
        arquivo=arquivo,
        dados=dados,
        http_status=http_status,
        sha=sha,
    )


# =========================
# SALVAR CSV NO GITHUB
# =========================
def salvar_github(df, arquivo, token, repo):
    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)
    sha = response.json().get("sha") if response.status_code == 200 else None

    csv_string = df.to_csv(index=False)
    content = base64.b64encode(csv_string.encode()).decode()

    data = {
        "message": f"Update {arquivo}",
        "content": content,
    }

    if sha:
        data["sha"] = sha

    put_response = requests.put(url, headers=headers, json=data)

    if put_response.status_code not in [200, 201]:
        raise Exception(f"Erro ao salvar CSV no GitHub: {put_response.text}")


# =========================
# CARREGAR CSV DO GITHUB
# Adaptador legado: retorna DataFrame diretamente.
# Não é seguro para novos fluxos que regravam após leitura ambígua.
# =========================
def carregar_github(arquivo, token, repo):
    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return pd.DataFrame()

    content = response.json().get("content")

    if not content:
        return pd.DataFrame()

    decoded = base64.b64decode(content).decode()

    return pd.read_csv(StringIO(decoded))


# =========================
# SALVAR ARQUIVO BINÁRIO NO GITHUB
# Imagens, PDFs, comprovantes etc.
# =========================
def salvar_arquivo_github(conteudo_bytes, arquivo, token, repo, mensagem=None):
    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)
    sha = response.json().get("sha") if response.status_code == 200 else None

    content = base64.b64encode(conteudo_bytes).decode()

    data = {
        "message": mensagem or f"Upload {arquivo}",
        "content": content,
    }

    if sha:
        data["sha"] = sha

    put_response = requests.put(url, headers=headers, json=data)

    if put_response.status_code not in [200, 201]:
        raise Exception(f"Erro ao salvar arquivo no GitHub: {put_response.text}")

    return arquivo


# =========================
# CARREGAR ARQUIVO BINÁRIO DO GITHUB
# Imagens, PDFs, comprovantes etc.
# =========================
def carregar_arquivo_github(arquivo, token, repo):
    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    dados = response.json()

    # Caminho mais confiável para imagem/PDF:
    # baixa o arquivo bruto pelo download_url.
    download_url = dados.get("download_url")

    if download_url:
        raw_response = requests.get(download_url, headers=headers)

        if raw_response.status_code == 200:
            return raw_response.content

    # Fallback: usa o conteúdo base64 retornado pela API.
    content = dados.get("content")

    if content:
        return base64.b64decode(content)

    return None
