import base64
import unittest
from unittest.mock import Mock, patch

import pandas as pd
import requests

from services.persistencia_multi_arquivo import (
    AlteracaoArquivoCSV,
    StatusPersistenciaMultiArquivo,
    publicar_csvs_em_commit,
    resolver_snapshot_branch,
)


class Resposta:
    def __init__(self, status_code, payload=None):
        self.status_code = status_code
        self._payload = payload if payload is not None else {}

    def json(self):
        return self._payload


class TestPersistenciaMultiArquivo(unittest.TestCase):
    def setUp(self):
        self.arquivos = [
            AlteracaoArquivoCSV("data/atestados.csv", pd.DataFrame([{"id": "a1"}])),
            AlteracaoArquivoCSV(
                "data/atestados_servicos.csv", pd.DataFrame([{"id": "s1"}])
            ),
        ]
        self.args = (self.arquivos, "token", "org/repo", "main", "Excluir atestado")

    def respostas_sucesso(self):
        return (
            [
                Resposta(200, {"object": {"sha": "commit-base"}}),
                Resposta(200, {"tree": {"sha": "tree-base"}}),
            ],
            [
                Resposta(201, {"sha": "blob-atestados"}),
                Resposta(201, {"sha": "blob-servicos"}),
                Resposta(201, {"sha": "tree-nova"}),
                Resposta(201, {"sha": "commit-novo"}),
            ],
            Resposta(200, {"object": {"sha": "commit-novo"}}),
        )

    def publicar(self, get_respostas=None, post_respostas=None, patch_resposta=None):
        get_padrao, post_padrao, patch_padrao = self.respostas_sucesso()
        with patch("services.persistencia_multi_arquivo.requests.get") as mock_get, patch(
            "services.persistencia_multi_arquivo.requests.post"
        ) as mock_post, patch("services.persistencia_multi_arquivo.requests.patch") as mock_patch:
            mock_get.side_effect = get_respostas if get_respostas is not None else get_padrao
            mock_post.side_effect = post_respostas if post_respostas is not None else post_padrao
            mock_patch.return_value = patch_resposta if patch_resposta is not None else patch_padrao
            resultado = publicar_csvs_em_commit(*self.args)
            return resultado, mock_get, mock_post, mock_patch

    def test_sucesso_publica_dois_arquivos_no_mesmo_commit(self):
        resultado, mock_get, mock_post, mock_patch = self.publicar()

        self.assertTrue(resultado.sucesso)
        self.assertEqual(resultado.status, StatusPersistenciaMultiArquivo.SUCESSO)
        self.assertEqual(resultado.snapshot_commit_sha, "commit-base")
        self.assertEqual(resultado.commit_sha, "commit-novo")
        self.assertEqual(mock_get.call_count, 2)
        self.assertEqual(mock_post.call_count, 4)
        self.assertEqual(mock_patch.call_count, 1)

        primeira_arvore = mock_post.call_args_list[2].kwargs["json"]
        self.assertEqual(primeira_arvore["base_tree"], "tree-base")
        self.assertEqual(
            [item["path"] for item in primeira_arvore["tree"]],
            ["data/atestados.csv", "data/atestados_servicos.csv"],
        )
        commit = mock_post.call_args_list[3].kwargs["json"]
        self.assertEqual(commit["parents"], ["commit-base"])
        self.assertEqual(commit["tree"], "tree-nova")
        self.assertEqual(
            base64.b64decode(mock_post.call_args_list[0].kwargs["json"]["content"]),
            b"id\na1\n",
        )

    def test_ocorre_uma_unica_atualizacao_da_branch_sem_forca(self):
        _, _, _, mock_patch = self.publicar()

        mock_patch.assert_called_once()
        self.assertEqual(mock_patch.call_args.kwargs["json"], {"sha": "commit-novo", "force": False})
        self.assertEqual(
            mock_patch.call_args.args[0],
            "https://api.github.com/repos/org/repo/git/refs/heads/main",
        )

    def test_conflito_por_avanco_da_branch_nao_rele_nem_sobrescreve(self):
        resultado, mock_get, mock_post, mock_patch = self.publicar(
            patch_resposta=Resposta(422)
        )

        self.assertEqual(resultado.status, StatusPersistenciaMultiArquivo.CONFLITO)
        self.assertEqual(resultado.http_status, 422)
        self.assertEqual(mock_get.call_count, 2)
        self.assertEqual(mock_post.call_count, 4)
        mock_patch.assert_called_once()

    def test_falha_no_primeiro_blob_nao_atualiza_branch(self):
        resultado, _, mock_post, mock_patch = self.publicar(
            post_respostas=[Resposta(500)]
        )

        self.assertEqual(resultado.status, StatusPersistenciaMultiArquivo.FALHA_TEMPORARIA)
        mock_post.assert_called_once()
        mock_patch.assert_not_called()

    def test_falha_no_segundo_blob_nao_atualiza_branch(self):
        resultado, _, mock_post, mock_patch = self.publicar(
            post_respostas=[Resposta(201, {"sha": "blob-1"}), Resposta(401)]
        )

        self.assertEqual(resultado.status, StatusPersistenciaMultiArquivo.NAO_AUTORIZADO)
        self.assertEqual(mock_post.call_count, 2)
        mock_patch.assert_not_called()

    def test_falha_ao_criar_arvore_nao_atualiza_branch(self):
        resultado, _, mock_post, mock_patch = self.publicar(
            post_respostas=[
                Resposta(201, {"sha": "blob-1"}),
                Resposta(201, {"sha": "blob-2"}),
                Resposta(422),
            ]
        )

        self.assertEqual(resultado.status, StatusPersistenciaMultiArquivo.LIMITE_OU_VALIDACAO)
        self.assertEqual(mock_post.call_count, 3)
        mock_patch.assert_not_called()

    def test_falha_ao_criar_commit_nao_atualiza_branch(self):
        resultado, _, mock_post, mock_patch = self.publicar(
            post_respostas=[
                Resposta(201, {"sha": "blob-1"}),
                Resposta(201, {"sha": "blob-2"}),
                Resposta(201, {"sha": "tree-1"}),
                Resposta(429),
            ]
        )

        self.assertEqual(resultado.status, StatusPersistenciaMultiArquivo.LIMITE_OU_VALIDACAO)
        self.assertEqual(mock_post.call_count, 4)
        mock_patch.assert_not_called()

    def test_falha_ao_atualizar_branch_e_classificada(self):
        resultado, _, _, mock_patch = self.publicar(patch_resposta=Resposta(500))

        self.assertEqual(resultado.status, StatusPersistenciaMultiArquivo.FALHA_TEMPORARIA)
        mock_patch.assert_called_once()

    def test_classifica_401_403_e_409(self):
        for status_http, esperado in (
            (401, StatusPersistenciaMultiArquivo.NAO_AUTORIZADO),
            (403, StatusPersistenciaMultiArquivo.NAO_AUTORIZADO),
            (409, StatusPersistenciaMultiArquivo.CONFLITO),
        ):
            with self.subTest(status_http=status_http):
                resultado, _, _, mock_patch = self.publicar(
                    post_respostas=[Resposta(status_http)]
                )
                self.assertEqual(resultado.status, esperado)
                mock_patch.assert_not_called()

    def test_classifica_422_429_e_5xx(self):
        for status_http, esperado in (
            (422, StatusPersistenciaMultiArquivo.LIMITE_OU_VALIDACAO),
            (429, StatusPersistenciaMultiArquivo.LIMITE_OU_VALIDACAO),
            (503, StatusPersistenciaMultiArquivo.FALHA_TEMPORARIA),
        ):
            with self.subTest(status_http=status_http):
                resultado, _, _, mock_patch = self.publicar(
                    post_respostas=[Resposta(status_http)]
                )
                self.assertEqual(resultado.status, esperado)
                mock_patch.assert_not_called()

    @patch("services.persistencia_multi_arquivo.requests.get")
    def test_timeout_e_erro_de_conexao_sao_falhas_temporarias(self, mock_get):
        for erro in (requests.Timeout(), requests.ConnectionError()):
            with self.subTest(erro=erro.__class__.__name__):
                mock_get.side_effect = erro
                resultado = publicar_csvs_em_commit(*self.args)
                self.assertEqual(
                    resultado.status, StatusPersistenciaMultiArquivo.FALHA_TEMPORARIA
                )

    def test_entrada_invalida_nao_chama_http(self):
        with patch("services.persistencia_multi_arquivo.requests.get") as mock_get:
            resultado = publicar_csvs_em_commit(
                [self.arquivos[0]], "token", "org/repo", "main", "mensagem"
            )

        self.assertEqual(resultado.status, StatusPersistenciaMultiArquivo.REQUISICAO_INVALIDA)
        mock_get.assert_not_called()

    @patch("services.persistencia_multi_arquivo.requests.get")
    def test_resolver_snapshot_usa_ref_e_commit_observados(self, mock_get):
        mock_get.side_effect = [
            Resposta(200, {"object": {"sha": "commit-base"}}),
            Resposta(200, {"tree": {"sha": "tree-base"}}),
        ]

        snapshot = resolver_snapshot_branch("token", "org/repo", "main")

        self.assertEqual(snapshot.commit_sha, "commit-base")
        self.assertEqual(snapshot.tree_sha, "tree-base")
        self.assertEqual(
            mock_get.call_args_list[0].args[0],
            "https://api.github.com/repos/org/repo/git/ref/heads/main",
        )
        self.assertEqual(
            mock_get.call_args_list[1].args[0],
            "https://api.github.com/repos/org/repo/git/commits/commit-base",
        )
