import base64
import unittest
from unittest.mock import Mock, patch

import pandas as pd
import requests

from services.github import StatusLeitura, ler_csv_github


class RespostaFake:
    def __init__(self, status_code, payload=None, json_error=None):
        self.status_code = status_code
        self._payload = payload
        self._json_error = json_error

    def json(self):
        if self._json_error is not None:
            raise self._json_error
        return self._payload


def payload_csv(conteudo, sha="sha-teste", com_quebras=False):
    codificado = base64.b64encode(conteudo.encode("utf-8")).decode("ascii")
    if com_quebras:
        codificado = "\n".join(
            codificado[i:i + 12]
            for i in range(0, len(codificado), 12)
        )
    return {
        "sha": sha,
        "size": len(conteudo.encode("utf-8")),
        "content": codificado,
    }


class TestLerCsvGithub(unittest.TestCase):
    def chamar(self):
        return ler_csv_github(
            "data/teste.csv",
            "token-teste",
            "fabioser-ai/dragagem-app",
        )

    @patch("services.github.requests.get")
    def test_sucesso_com_dados_preserva_sha_e_normaliza_base64(self, get):
        get.return_value = RespostaFake(
            200,
            payload_csv("nome,valor\nA,10\n", com_quebras=True),
        )

        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusLeitura.SUCESSO_COM_DADOS)
        self.assertTrue(resultado.leitura_confirmada)
        self.assertTrue(resultado.pode_sobrescrever)
        self.assertEqual(resultado.sha, "sha-teste")
        self.assertEqual(resultado.dados.to_dict(orient="records"), [{"nome": "A", "valor": 10}])
        get.assert_called_once()
        self.assertIn("timeout", get.call_args.kwargs)

    @patch("services.github.requests.get")
    def test_csv_apenas_com_cabecalho_e_sucesso_vazio(self, get):
        get.return_value = RespostaFake(200, payload_csv("nome,valor\n"))

        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusLeitura.SUCESSO_VAZIO)
        self.assertTrue(resultado.leitura_confirmada)
        self.assertTrue(resultado.pode_sobrescrever)
        self.assertListEqual(resultado.dados.columns.tolist(), ["nome", "valor"])

    @patch("services.github.requests.get")
    def test_arquivo_fisicamente_vazio_e_sucesso_vazio(self, get):
        get.return_value = RespostaFake(
            200,
            {"sha": "sha-vazio", "size": 0, "content": ""},
        )

        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusLeitura.SUCESSO_VAZIO)
        self.assertEqual(resultado.sha, "sha-vazio")

    @patch("services.github.requests.get")
    def test_404_e_arquivo_inexistente_sem_autorizar_sobrescrita(self, get):
        get.return_value = RespostaFake(404, {})

        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusLeitura.ARQUIVO_INEXISTENTE)
        self.assertTrue(resultado.leitura_confirmada)
        self.assertFalse(resultado.pode_sobrescrever)
        self.assertEqual(resultado.http_status, 404)

    @patch("services.github.requests.get")
    def test_401_e_nao_autorizado(self, get):
        get.return_value = RespostaFake(401, {})

        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusLeitura.NAO_AUTORIZADO)
        self.assertFalse(resultado.leitura_confirmada)
        self.assertFalse(resultado.pode_sobrescrever)

    @patch("services.github.requests.get")
    def test_429_e_conflito_ou_limite(self, get):
        get.return_value = RespostaFake(429, {})

        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusLeitura.CONFLITO_OU_LIMITE)
        self.assertFalse(resultado.pode_sobrescrever)

    @patch("services.github.requests.get")
    def test_500_e_falha_temporaria(self, get):
        get.return_value = RespostaFake(500, {})

        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusLeitura.FALHA_TEMPORARIA)
        self.assertFalse(resultado.leitura_confirmada)

    @patch("services.github.requests.get")
    def test_timeout_e_falha_temporaria(self, get):
        get.side_effect = requests.Timeout("timeout de teste")

        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusLeitura.FALHA_TEMPORARIA)
        self.assertIsNone(resultado.http_status)
        self.assertFalse(resultado.pode_sobrescrever)

    @patch("services.github.requests.get")
    def test_json_invalido_e_conteudo_invalido(self, get):
        get.return_value = RespostaFake(200, json_error=ValueError("json inválido"))

        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusLeitura.CONTEUDO_INVALIDO)
        self.assertFalse(resultado.leitura_confirmada)

    @patch("services.github.requests.get")
    def test_base64_invalido_e_conteudo_invalido(self, get):
        get.return_value = RespostaFake(
            200,
            {"sha": "sha-invalido", "size": 10, "content": "%%%invalido%%%"},
        )

        resultado = self.chamar()

        self.assertEqual(resultado.status, StatusLeitura.CONTEUDO_INVALIDO)
        self.assertEqual(resultado.sha, "sha-invalido")
        self.assertFalse(resultado.pode_sobrescrever)


if __name__ == "__main__":
    unittest.main()
