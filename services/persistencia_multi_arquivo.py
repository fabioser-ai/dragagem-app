"""Contrato explícito para publicar CSVs relacionados em um único commit Git.

Esta fundação não conhece nenhum fluxo de interface. Ela cria objetos Git
intermediários e só torna a alteração visível quando atualiza a referência da
branch, sem força, a partir do snapshot observado.
"""

import base64
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence

import pandas as pd
import requests

from services.github import DEFAULT_REQUEST_TIMEOUT


class StatusPersistenciaMultiArquivo(str, Enum):
    SUCESSO = "sucesso"
    REQUISICAO_INVALIDA = "requisicao_invalida"
    NAO_AUTORIZADO = "nao_autorizado"
    CONFLITO = "conflito"
    LIMITE_OU_VALIDACAO = "limite_ou_validacao"
    FALHA_TEMPORARIA = "falha_temporaria"
    ERRO_DESCONHECIDO = "erro_desconhecido"


@dataclass(frozen=True)
class AlteracaoArquivoConteudo:
    """Alteração genérica para publicação atômica de texto ou bytes."""

    arquivo: str
    conteudo: bytes


@dataclass(frozen=True)
class AlteracaoArquivoCSV:
    arquivo: str
    dados: pd.DataFrame


@dataclass(frozen=True)
class SnapshotBranch:
    branch: str
    commit_sha: str
    tree_sha: str


@dataclass(frozen=True)
class ResultadoPersistenciaMultiArquivo:
    status: StatusPersistenciaMultiArquivo
    branch: str
    arquivos: tuple[str, ...]
    http_status: Optional[int] = None
    snapshot_commit_sha: Optional[str] = None
    commit_sha: Optional[str] = None
    erro: Optional[str] = None

    @property
    def sucesso(self) -> bool:
        return self.status == StatusPersistenciaMultiArquivo.SUCESSO


def _resultado(
    *,
    status,
    branch,
    arquivos=(),
    http_status=None,
    snapshot_commit_sha=None,
    commit_sha=None,
    erro=None,
):
    return ResultadoPersistenciaMultiArquivo(
        status=status,
        branch=branch,
        arquivos=tuple(arquivos),
        http_status=http_status,
        snapshot_commit_sha=snapshot_commit_sha,
        commit_sha=commit_sha,
        erro=erro,
    )


def _headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }


def _erro_de_requisicao(exc, *, branch, arquivos, snapshot_commit_sha=None):
    if isinstance(exc, (requests.Timeout, requests.ConnectionError)):
        status = StatusPersistenciaMultiArquivo.FALHA_TEMPORARIA
        descricao = "Falha temporária de comunicação com o GitHub"
    elif isinstance(exc, requests.RequestException):
        status = StatusPersistenciaMultiArquivo.ERRO_DESCONHECIDO
        descricao = "Erro de comunicação com o GitHub"
    else:
        status = StatusPersistenciaMultiArquivo.ERRO_DESCONHECIDO
        descricao = "Erro inesperado ao comunicar com o GitHub"

    return _resultado(
        status=status,
        branch=branch,
        arquivos=arquivos,
        snapshot_commit_sha=snapshot_commit_sha,
        erro=f"{descricao}: {exc.__class__.__name__}",
    )


def _resultado_http(
    http_status,
    *,
    branch,
    arquivos,
    snapshot_commit_sha=None,
    conflito_422=False,
):
    if http_status in (401, 403):
        status = StatusPersistenciaMultiArquivo.NAO_AUTORIZADO
        erro = "Operação Git não autorizada pelo GitHub."
    elif http_status == 409 or (conflito_422 and http_status == 422):
        status = StatusPersistenciaMultiArquivo.CONFLITO
        erro = "A branch avançou desde o snapshot observado."
    elif http_status in (422, 429):
        status = StatusPersistenciaMultiArquivo.LIMITE_OU_VALIDACAO
        erro = "O GitHub recusou a operação por validação ou limite."
    elif 500 <= http_status <= 599:
        status = StatusPersistenciaMultiArquivo.FALHA_TEMPORARIA
        erro = "O GitHub está temporariamente indisponível."
    else:
        status = StatusPersistenciaMultiArquivo.ERRO_DESCONHECIDO
        erro = "Resposta HTTP inesperada do GitHub."

    return _resultado(
        status=status,
        branch=branch,
        arquivos=arquivos,
        http_status=http_status,
        snapshot_commit_sha=snapshot_commit_sha,
        erro=erro,
    )


def _validar_entrada(arquivos, token, repo, branch, mensagem):
    if not isinstance(arquivos, Sequence) or isinstance(arquivos, (str, bytes)):
        return "As alterações devem ser fornecidas como uma sequência."
    if len(arquivos) < 2:
        return "A persistência multi-arquivo exige ao menos dois arquivos."
    if not all(isinstance(item, AlteracaoArquivoCSV) for item in arquivos):
        return "Cada alteração deve ser uma AlteracaoArquivoCSV."

    caminhos = [item.arquivo for item in arquivos]
    if any(not isinstance(caminho, str) or not caminho.strip() for caminho in caminhos):
        return "Cada arquivo deve possuir um caminho não vazio."
    if len(set(caminhos)) != len(caminhos):
        return "Os caminhos dos arquivos devem ser únicos."
    if any(not isinstance(item.dados, pd.DataFrame) for item in arquivos):
        return "Cada alteração deve conter um DataFrame."
    if not all(isinstance(valor, str) and valor.strip() for valor in (token, repo, branch, mensagem)):
        return "Token, repositório, branch e mensagem são obrigatórios."
    return None


def resolver_snapshot_branch(
    token,
    repo,
    branch,
    *,
    timeout=DEFAULT_REQUEST_TIMEOUT,
):
    """Resolve o commit e a árvore de um único snapshot da branch."""

    arquivos = ()
    if not all(isinstance(valor, str) and valor.strip() for valor in (token, repo, branch)):
        return _resultado(
            status=StatusPersistenciaMultiArquivo.REQUISICAO_INVALIDA,
            branch=branch if isinstance(branch, str) else "",
            arquivos=arquivos,
            erro="Token, repositório e branch são obrigatórios.",
        )

    base_url = f"https://api.github.com/repos/{repo}/git"
    try:
        resposta_ref = requests.get(
            f"{base_url}/ref/heads/{branch}",
            headers=_headers(token),
            timeout=timeout,
        )
    except Exception as exc:
        return _erro_de_requisicao(exc, branch=branch, arquivos=arquivos)

    if resposta_ref.status_code != 200:
        return _resultado_http(
            resposta_ref.status_code,
            branch=branch,
            arquivos=arquivos,
        )

    try:
        commit_sha = resposta_ref.json()["object"]["sha"]
    except (KeyError, TypeError, ValueError):
        return _resultado(
            status=StatusPersistenciaMultiArquivo.ERRO_DESCONHECIDO,
            branch=branch,
            arquivos=arquivos,
            http_status=resposta_ref.status_code,
            erro="Resposta inválida ao resolver a referência da branch.",
        )

    try:
        resposta_commit = requests.get(
            f"{base_url}/commits/{commit_sha}",
            headers=_headers(token),
            timeout=timeout,
        )
    except Exception as exc:
        return _erro_de_requisicao(
            exc,
            branch=branch,
            arquivos=arquivos,
            snapshot_commit_sha=commit_sha,
        )

    if resposta_commit.status_code != 200:
        return _resultado_http(
            resposta_commit.status_code,
            branch=branch,
            arquivos=arquivos,
            snapshot_commit_sha=commit_sha,
        )

    try:
        tree_sha = resposta_commit.json()["tree"]["sha"]
    except (KeyError, TypeError, ValueError):
        return _resultado(
            status=StatusPersistenciaMultiArquivo.ERRO_DESCONHECIDO,
            branch=branch,
            arquivos=arquivos,
            http_status=resposta_commit.status_code,
            snapshot_commit_sha=commit_sha,
            erro="Resposta inválida ao resolver a árvore do commit.",
        )

    return SnapshotBranch(branch=branch, commit_sha=commit_sha, tree_sha=tree_sha)


def publicar_csvs_em_commit(
    arquivos,
    token,
    repo,
    branch,
    mensagem,
    *,
    timeout=DEFAULT_REQUEST_TIMEOUT,
):
    """Publica vários CSVs em um commit e atualiza a branch sem força.

    Objetos Git criados antes da atualização final não ficam visíveis na branch.
    A atualização usa ``force=False`` e o commit criado referencia somente a
    cabeça observada, portanto uma branch avançada é classificada como conflito.
    """

    erro_validacao = _validar_entrada(arquivos, token, repo, branch, mensagem)
    caminhos = tuple(item.arquivo for item in arquivos) if isinstance(arquivos, Sequence) and not isinstance(arquivos, (str, bytes)) else ()
    if erro_validacao:
        return _resultado(
            status=StatusPersistenciaMultiArquivo.REQUISICAO_INVALIDA,
            branch=branch if isinstance(branch, str) else "",
            arquivos=caminhos,
            erro=erro_validacao,
        )

    conteudos = tuple(
        AlteracaoArquivoConteudo(
            item.arquivo, item.dados.to_csv(index=False).encode("utf-8")
        )
        for item in arquivos
    )
    return _publicar_conteudos(
        conteudos, token, repo, branch, mensagem, None, timeout=timeout
    )


def _publicar_conteudos(
    arquivos,
    token,
    repo,
    branch,
    mensagem,
    snapshot_esperado,
    *,
    timeout=DEFAULT_REQUEST_TIMEOUT,
):
    """Publica conteúdos genéricos atomicamente usando snapshot obrigatório.

    A função preserva a fundação Git existente: blobs, árvore, commit com um
    único pai e atualização da referência sem força. Nenhum objeto parcial se
    torna visível antes da atualização final da branch.
    """

    if not isinstance(arquivos, Sequence) or isinstance(arquivos, (str, bytes)):
        arquivos = ()
    caminhos = tuple(
        item.arquivo for item in arquivos if isinstance(item, AlteracaoArquivoConteudo)
    )
    entrada_valida = (
        len(arquivos) >= 2
        and len(caminhos) == len(arquivos)
        and len(set(caminhos)) == len(caminhos)
        and all(item.arquivo.strip() and isinstance(item.conteudo, bytes) for item in arquivos)
        and all(
            isinstance(valor, str) and valor.strip()
            for valor in (token, repo, branch, mensagem)
        )
        and (
            snapshot_esperado is None
            or (isinstance(snapshot_esperado, str) and snapshot_esperado.strip())
        )
    )
    if not entrada_valida:
        return _resultado(
            status=StatusPersistenciaMultiArquivo.REQUISICAO_INVALIDA,
            branch=branch if isinstance(branch, str) else "",
            arquivos=caminhos,
            erro="A publicação exige ao menos dois conteúdos, caminhos únicos e snapshot esperado.",
        )

    snapshot = resolver_snapshot_branch(token, repo, branch, timeout=timeout)
    if isinstance(snapshot, ResultadoPersistenciaMultiArquivo):
        return _resultado(
            status=snapshot.status,
            branch=branch,
            arquivos=caminhos,
            http_status=snapshot.http_status,
            snapshot_commit_sha=snapshot.snapshot_commit_sha,
            erro=snapshot.erro,
        )
    if snapshot_esperado is not None and snapshot.commit_sha != snapshot_esperado:
        return _resultado(
            status=StatusPersistenciaMultiArquivo.CONFLITO,
            branch=branch,
            arquivos=caminhos,
            snapshot_commit_sha=snapshot.commit_sha,
            erro="A branch avançou desde o snapshot esperado.",
        )

    base_url = f"https://api.github.com/repos/{repo}/git"
    headers = _headers(token)
    blobs = []
    for alteracao in arquivos:
        conteudo = base64.b64encode(alteracao.conteudo).decode("ascii")
        try:
            resposta_blob = requests.post(
                f"{base_url}/blobs",
                headers=headers,
                json={"content": conteudo, "encoding": "base64"},
                timeout=timeout,
            )
        except Exception as exc:
            return _erro_de_requisicao(
                exc, branch=branch, arquivos=caminhos,
                snapshot_commit_sha=snapshot.commit_sha,
            )
        if resposta_blob.status_code != 201:
            return _resultado_http(
                resposta_blob.status_code, branch=branch, arquivos=caminhos,
                snapshot_commit_sha=snapshot.commit_sha,
            )
        try:
            blobs.append(resposta_blob.json()["sha"])
        except (KeyError, TypeError, ValueError):
            return _resultado(
                status=StatusPersistenciaMultiArquivo.ERRO_DESCONHECIDO,
                branch=branch, arquivos=caminhos,
                snapshot_commit_sha=snapshot.commit_sha,
                erro="Resposta inválida ao criar o blob.",
            )

    tree = [
        {"path": item.arquivo, "mode": "100644", "type": "blob", "sha": sha}
        for item, sha in zip(arquivos, blobs)
    ]
    try:
        resposta_tree = requests.post(
            f"{base_url}/trees", headers=headers,
            json={"base_tree": snapshot.tree_sha, "tree": tree}, timeout=timeout,
        )
    except Exception as exc:
        return _erro_de_requisicao(
            exc, branch=branch, arquivos=caminhos,
            snapshot_commit_sha=snapshot.commit_sha,
        )
    if resposta_tree.status_code != 201:
        return _resultado_http(
            resposta_tree.status_code, branch=branch, arquivos=caminhos,
            snapshot_commit_sha=snapshot.commit_sha,
        )
    try:
        tree_sha = resposta_tree.json()["sha"]
    except (KeyError, TypeError, ValueError):
        return _resultado(
            status=StatusPersistenciaMultiArquivo.ERRO_DESCONHECIDO,
            branch=branch, arquivos=caminhos,
            snapshot_commit_sha=snapshot.commit_sha,
            erro="Resposta inválida ao criar a árvore.",
        )

    try:
        resposta_commit = requests.post(
            f"{base_url}/commits", headers=headers,
            json={"message": mensagem, "tree": tree_sha, "parents": [snapshot.commit_sha]},
            timeout=timeout,
        )
    except Exception as exc:
        return _erro_de_requisicao(
            exc, branch=branch, arquivos=caminhos,
            snapshot_commit_sha=snapshot.commit_sha,
        )
    if resposta_commit.status_code != 201:
        return _resultado_http(
            resposta_commit.status_code, branch=branch, arquivos=caminhos,
            snapshot_commit_sha=snapshot.commit_sha,
        )
    try:
        commit_sha = resposta_commit.json()["sha"]
    except (KeyError, TypeError, ValueError):
        return _resultado(
            status=StatusPersistenciaMultiArquivo.ERRO_DESCONHECIDO,
            branch=branch, arquivos=caminhos,
            snapshot_commit_sha=snapshot.commit_sha,
            erro="Resposta inválida ao criar o commit.",
        )

    try:
        resposta_ref = requests.patch(
            f"{base_url}/refs/heads/{branch}", headers=headers,
            json={"sha": commit_sha, "force": False}, timeout=timeout,
        )
    except Exception as exc:
        return _erro_de_requisicao(
            exc, branch=branch, arquivos=caminhos,
            snapshot_commit_sha=snapshot.commit_sha,
        )
    if resposta_ref.status_code != 200:
        return _resultado_http(
            resposta_ref.status_code, branch=branch, arquivos=caminhos,
            snapshot_commit_sha=snapshot.commit_sha, conflito_422=True,
        )
    return _resultado(
        status=StatusPersistenciaMultiArquivo.SUCESSO,
        branch=branch, arquivos=caminhos,
        http_status=resposta_ref.status_code,
        snapshot_commit_sha=snapshot.commit_sha,
        commit_sha=commit_sha,
    )


def publicar_arquivos_em_commit(
    arquivos,
    token,
    repo,
    branch,
    mensagem,
    snapshot_esperado,
    *,
    timeout=DEFAULT_REQUEST_TIMEOUT,
):
    """Publica conteúdos genéricos com snapshot esperado obrigatório."""

    if not isinstance(snapshot_esperado, str) or not snapshot_esperado.strip():
        caminhos = tuple(
            item.arquivo
            for item in arquivos
            if isinstance(item, AlteracaoArquivoConteudo)
        ) if isinstance(arquivos, Sequence) else ()
        return _resultado(
            status=StatusPersistenciaMultiArquivo.REQUISICAO_INVALIDA,
            branch=branch if isinstance(branch, str) else "",
            arquivos=caminhos,
            erro="Snapshot esperado é obrigatório.",
        )
    return _publicar_conteudos(
        arquivos, token, repo, branch, mensagem, snapshot_esperado, timeout=timeout
    )
