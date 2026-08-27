import unittest
from unittest.mock import patch

import pandas as pd

from services import dados_operacionais
from services.github import StatusEscrita, StatusLeitura


class _Resposta:
    def __init__(self, status_code=200, payload=None):
        self.status_code = status_code
        self._payload = payload or {"content": {"sha": "novo-sha"}}

    def json(self):
        return self._payload


class TestPerfDados001DataBranch(unittest.TestCase):
    def test_branch_operacional_nao_e_main(self):
        self.assertEqual(dados_operacionais.DATA_BRANCH, "data-operacional")
        self.assertNotEqual(dados_operacionais.DATA_BRANCH, "main")

    @patch("services.dados_operacionais.ler_csv_github")
    def test_leitura_informa_ref_operacional(self, mock_ler):
        mock_ler.return_value.status = StatusLeitura.SUCESSO_VAZIO
        dados_operacionais.ler_csv_operacional("data/salarios.csv", "token", "repo")
        _, kwargs = mock_ler.call_args
        self.assertEqual(kwargs["ref"], "data-operacional")

    @patch("services.dados_operacionais.requests.put")
    def test_escrita_informa_branch_operacional(self, mock_put):
        mock_put.return_value = _Resposta()
        df = pd.DataFrame([{"Posicao": "Ajudante", "Valor_Hora": "25.00"}])
        resultado = dados_operacionais.salvar_csv_operacional(
            df,
            "data/salarios.csv",
            "token",
            "owner/repo",
            sha_esperado="sha-atual",
        )
        self.assertEqual(resultado.status, StatusEscrita.SUCESSO_ATUALIZADO)
        payload = mock_put.call_args.kwargs["json"]
        self.assertEqual(payload["branch"], "data-operacional")
        self.assertNotEqual(payload["branch"], "main")
        self.assertEqual(payload["sha"], "sha-atual")


if __name__ == "__main__":
    unittest.main()
