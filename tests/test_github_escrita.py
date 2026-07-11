import base64
import unittest
from unittest.mock import patch

import pandas as pd
import requests

from services.github import StatusEscrita, salvar_csv_github


class RespostaFake:
    def __init__(self, status_code, payload=None, json_error=None):
        self.status_code = status_code
        self._payload = payload
        self._json_error = json_error

    def json(self):
        if self._json_error is not None:
            raise self._json_error
        return self._payload


class TestSalvarCsvGithub(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame([{"nome": "A", "valor": 10}])

    def chamar(self, **kwargs):
        return salvar_csv_github(
            self.df,
            "data/teste.csv",
            "token-teste",
            "fabioser-ai/dragagem-app",
            **kwargs,
        )

    @patch("services.github.requests.put")
    def test_atualizacao_usa_sha_esperado_sem_get(self, put):
        put.return_value = RespostaFake(
            200,
            {"content": {"sha": "sha-novo"}},
        )

        resultado = self.chamar(sha_esperado="sha-lido")

        self.assertEqual(resultado.status, StatusEscrita.SUCESSO_ATUALIZADO)
        self.assertTrue(resultado.sucesso)
        self.assertEqual(resultado.sha, "sha-novo")

        put.assert_called_once()
        chamada = put.call_args
        self.assertEqual(chamada.kwargs["json"]["sha"], "sha-lido")
        self.assertIn("timeout", chamada.kwargs)

        csv_enviado = base64.b64decode(
            chamada.kwargs["json"]["content"]
        ).decode("utf-8")
        self.assertEqual(csv_enviado, "nome,valor\nA,10\n")

    @patch("services.github.requests.put")
    def test_criacao_nao_envia_sha(self, put):
        put.return_value = RespostaFake(
            201,
            {"content": {"sha": "sha-criado"}},
        )

        resultado = self.chamar(criar=True)

        self.assertEqual(resultado.status, StatusEscrita.SUCESSO_CRIADO)
        self.assertTrue(resultado.sucesso)
        self.assertEqual(resultado.sha, "sha-criado")
        self.assertNotIn("sha", put.call_args.kwargs["json"])

    @patch("services.github.requests.put")
    def test_atualizacao_sem_sha_e_requisicao_invalida(self, put):
        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusEscrita.REQUISICAO_INVALIDA)
        self.assertFalse(resultado.sucesso)
        put.assert_not_called()

    @patch("services.github.requests.put")
    def test_criacao_com_sha_e_requisicao_invalida(self, put):
        resultado = self.chamar(criar=True, sha_esperado="sha-invalido")

        self.assertEqual(resultado.status, StatusEscrita.REQUISICAO_INVALIDA)
        self.assertFalse(resultado.sucesso)
        put.assert_not_called()

    @patch("services.github.requests.put")
    def test_401_e_nao_autorizado(self, put):
        put.return_value = RespostaFake(401, {})

        resultado = self.chamar(sha_esperado="sha-lido")

        self.assertEqual(resultado.status, StatusEscrita.NAO_AUTORIZADO)
        self.assertFalse(resultado.sucesso)

    @patch("services.github.requests.put")
    def test_409_e_conflito(self, put):
        put.return_value = RespostaFake(409, {})

        resultado = self.chamar(sha_esperado="sha-antigo")

        self.assertEqual(resultado.status, StatusEscrita.CONFLITO)
        self.assertFalse(resultado.sucesso)

    @patch("services.github.requests.put")
    def test_422_e_limite_ou_validacao(self, put):
        put.return_value = RespostaFake(422, {})

        resultado = self.chamar(sha_esperado="sha-lido")

        self.assertEqual(resultado.status, StatusEscrita.LIMITE_OU_VALIDACAO)

    @patch("services.github.requests.put")
    def test_500_e_falha_temporaria(self, put):
        put.return_value = RespostaFake(500, {})

        resultado = self.chamar(sha_esperado="sha-lido")

        self.assertEqual(resultado.status, StatusEscrita.FALHA_TEMPORARIA)
        self.assertFalse(resultado.sucesso)

    @patch("services.github.requests.put")
    def test_timeout_e_falha_temporaria(self, put):
        put.side_effect = requests.Timeout("timeout de teste")

        resultado = self.chamar(sha_esperado="sha-lido")

        self.assertEqual(resultado.status, StatusEscrita.FALHA_TEMPORARIA)
        self.assertIsNone(resultado.http_status)

    @patch("services.github.requests.put")
    def test_sucesso_com_json_invalido_permanece_sucesso_sem_sha(self, put):
        put.return_value = RespostaFake(
            200,
            json_error=ValueError("json inválido"),
        )

        resultado = self.chamar(sha_esperado="sha-lido")

        self.assertEqual(resultado.status, StatusEscrita.SUCESSO_ATUALIZADO)
        self.assertTrue(resultado.sucesso)
        self.assertIsNone(resultado.sha)


if __name__ == "__main__":
    unittest.main()
