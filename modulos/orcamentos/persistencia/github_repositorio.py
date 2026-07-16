"""Adaptador GitHub mínimo para índice e documento de versão."""

import base64

import requests

from modulos.orcamentos.dominio.modelos import Orcamento, VersaoOrcamento
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.indice import (
    atualizar_resumo, desserializar_indice, resumo_de, serializar_indice,
)
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao
from services.github import DEFAULT_REQUEST_TIMEOUT
from services.persistencia_multi_arquivo import (
    AlteracaoArquivoConteudo, StatusPersistenciaMultiArquivo, publicar_arquivos_em_commit,
)

RAIZ = "data/orcamentos_v2"
CAMINHO_INDICE = f"{RAIZ}/indice.csv"


def caminho_versao(orcamento_id: str, versao_id: str) -> str:
    return f"{RAIZ}/orcamentos/{orcamento_id}/versoes/{versao_id}.json"


class RepositorioOrcamentosGitHub:
    def __init__(self, token: str, repo: str, branch: str = "main", *, timeout=DEFAULT_REQUEST_TIMEOUT):
        self.token, self.repo, self.branch, self.timeout = token, repo, branch, timeout

    def carregar_snapshot(self):
        """Captura a cabeça da branch somente quando uma edição vai começar."""
        try:
            resposta = requests.get(
                f"https://api.github.com/repos/{self.repo}/git/ref/heads/{self.branch}",
                headers=self._headers(), timeout=self.timeout,
            )
        except requests.RequestException:
            return ResultadoPersistencia(StatusPersistencia.ERRO_REMOTO)
        if resposta.status_code != 200:
            return ResultadoPersistencia(StatusPersistencia.ERRO_REMOTO)
        try:
            sha = resposta.json()["object"]["sha"]
        except (KeyError, TypeError, ValueError):
            return ResultadoPersistencia(StatusPersistencia.DADO_CORROMPIDO)
        return ResultadoPersistencia(StatusPersistencia.SUCESSO, sha)

    def carregar_indice_bruto(self):
        """Carrega o CSV do índice para uma gravação composta explícita."""
        resultado = self._carregar_conteudo(CAMINHO_INDICE)
        if resultado.status is StatusPersistencia.DADO_INEXISTENTE:
            return ResultadoPersistencia(StatusPersistencia.SUCESSO, serializar_indice([]))
        return resultado

    def carregar_indice(self):
        """Carrega somente o índice resumido em uma requisição remota."""
        bruto = self._carregar_conteudo(CAMINHO_INDICE)
        if not bruto.sucesso:
            return bruto
        resultado = desserializar_indice(bruto.valor)
        return ResultadoPersistencia(
            resultado.status, resultado.valor, arquivos=(CAMINHO_INDICE,), erro=resultado.erro
        )

    def carregar_versao(self, orcamento_id: str, versao_id: str):
        """Carrega orçamento+versão em exatamente uma requisição remota."""
        caminho = caminho_versao(orcamento_id, versao_id)
        bruto = self._carregar_conteudo(caminho)
        if not bruto.sucesso:
            return bruto
        resultado = desserializar_versao(bruto.valor)
        if not resultado.sucesso:
            return ResultadoPersistencia(resultado.status, erro=resultado.erro, arquivos=(caminho,))
        orcamento, versao = resultado.valor
        if str(orcamento.id) != orcamento_id or str(versao.id) != versao_id:
            return ResultadoPersistencia(
                StatusPersistencia.DADO_CORROMPIDO, arquivos=(caminho,),
                erro="Identidades do documento divergem do caminho solicitado.",
            )
        return ResultadoPersistencia(StatusPersistencia.SUCESSO, resultado.valor, arquivos=(caminho,))

    def persistir_versao(
        self, orcamento: Orcamento, versao: VersaoOrcamento,
        indice_atual: str, snapshot_esperado: str,
    ):
        indice = desserializar_indice(indice_atual)
        if not indice.sucesso:
            return ResultadoPersistencia(StatusPersistencia.DADO_CORROMPIDO, erro=indice.erro)
        try:
            resumo = resumo_de(orcamento, versao)
            documento = serializar_versao(orcamento, versao)
            caminho = caminho_versao(str(orcamento.id), str(versao.id))
        except (AttributeError, TypeError, ValueError):
            return ResultadoPersistencia(
                StatusPersistencia.REQUISICAO_INVALIDA,
                erro="Orçamento ou versão inválidos para persistência.",
            )
        resumos = atualizar_resumo(indice.valor, resumo)
        arquivos = (
            AlteracaoArquivoConteudo(CAMINHO_INDICE, serializar_indice(resumos).encode("utf-8")),
            AlteracaoArquivoConteudo(caminho, documento.encode("utf-8")),
        )
        remoto = publicar_arquivos_em_commit(
            arquivos, self.token, self.repo, self.branch,
            "Persistir identificação e premissas do orçamento",
            snapshot_esperado, timeout=self.timeout,
        )
        status = self._mapear_status(remoto, snapshot_esperado)
        return ResultadoPersistencia(
            status, (orcamento, versao) if status is StatusPersistencia.SUCESSO else None,
            snapshot_esperado, remoto.snapshot_commit_sha, remoto.commit_sha,
            tuple(item.arquivo for item in arquivos), remoto.erro,
        )

    def _carregar_conteudo(self, caminho):
        try:
            resposta = requests.get(
                f"https://api.github.com/repos/{self.repo}/contents/{caminho}",
                headers=self._headers(), params={"ref": self.branch}, timeout=self.timeout,
            )
        except requests.RequestException:
            return ResultadoPersistencia(StatusPersistencia.ERRO_REMOTO, arquivos=(caminho,))
        if resposta.status_code == 404:
            return ResultadoPersistencia(StatusPersistencia.DADO_INEXISTENTE, arquivos=(caminho,))
        if resposta.status_code != 200:
            return ResultadoPersistencia(StatusPersistencia.ERRO_REMOTO, arquivos=(caminho,))
        try:
            conteudo = base64.b64decode(
                resposta.json()["content"], validate=True
            ).decode("utf-8")
        except (KeyError, TypeError, ValueError, UnicodeDecodeError):
            return ResultadoPersistencia(StatusPersistencia.DADO_CORROMPIDO, arquivos=(caminho,))
        return ResultadoPersistencia(StatusPersistencia.SUCESSO, conteudo, arquivos=(caminho,))

    def _mapear_status(self, remoto, snapshot_esperado):
        if remoto.status is StatusPersistenciaMultiArquivo.SUCESSO:
            return StatusPersistencia.SUCESSO
        if remoto.status is StatusPersistenciaMultiArquivo.REQUISICAO_INVALIDA:
            return StatusPersistencia.OPERACAO_PARCIAL_RECUSADA
        if remoto.status is StatusPersistenciaMultiArquivo.CONFLITO:
            if remoto.snapshot_commit_sha and remoto.snapshot_commit_sha != snapshot_esperado:
                return StatusPersistencia.BRANCH_AVANCADA
            return StatusPersistencia.CONFLITO
        return StatusPersistencia.ERRO_REMOTO

    def _headers(self):
        return {"Authorization": f"token {self.token}", "Accept": "application/vnd.github+json"}
