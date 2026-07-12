import unittest
from unittest.mock import patch

import pandas as pd

from services.dados_persistencia import (
    carregar_cadastro_resultado,
    normalizar_dataframe,
    salvar_cadastro_seguro,
)
from services.github import (
    ResultadoEscritaCSV,
    ResultadoLeituraCSV,
    StatusEscrita,
    StatusLeitura,
)


ARQUIVO = "data/equipamentos.csv"
COLUNAS = ["Equipamento", "Vazao", "Valor"]
TOKEN = "token-teste"
REPO = "fabioser-ai/dragagem-app"


def resultado_leitura(status, dados=None, sha=None):
    return ResultadoLeituraCSV(
        status=status,
        dados=dados if dados is not None else pd.DataFrame(),
        arquivo=ARQUIVO,
        sha=sha,
    )


class TestNormalizarDataframe(unittest.TestCase):
    def test_adiciona_colunas_ausentes(self):
        dados = pd.DataFrame([{"Equipamento": "Bomba"}])

        resultado = normalizar_dataframe(dados, COLUNAS)

        self.assertListEqual(resultado.columns.tolist(), COLUNAS)
        self.assertEqual(resultado.loc[0, "Vazao"], "")
        self.assertEqual(resultado.loc[0, "Valor"], "")

    def test_preserva_somente_schema_informado(self):
        dados = pd.DataFrame(
            [{"Equipamento": "Bomba", "Valor": "10", "Extra": "ignorar"}]
        )

        resultado = normalizar_dataframe(dados, COLUNAS)

        self.assertListEqual(resultado.columns.tolist(), COLUNAS)
        self.assertNotIn("Extra", resultado.columns)


class TestCarregarCadastroResultado(unittest.TestCase):
    @patch("services.dados_persistencia.ler_csv_github")
    def test_leitura_com_dados_preserva_status_e_sha(self, ler):
        ler.return_value = resultado_leitura(
            StatusLeitura.SUCESSO_COM_DADOS,
            pd.DataFrame([{"Equipamento": "Bomba"}]),
            sha="sha-confirmado",
        )

        resultado = carregar_cadastro_resultado(ARQUIVO, COLUNAS, TOKEN, REPO)

        self.assertEqual(resultado.status, StatusLeitura.SUCESSO_COM_DADOS)
        self.assertEqual(resultado.sha, "sha-confirmado")
        self.assertListEqual(resultado.dados.columns.tolist(), COLUNAS)
        ler.assert_called_once_with(ARQUIVO, TOKEN, REPO)

    @patch("services.dados_persistencia.ler_csv_github")
    def test_leitura_vazia_preserva_schema(self, ler):
        ler.return_value = resultado_leitura(
            StatusLeitura.SUCESSO_VAZIO,
            pd.DataFrame(),
            sha="sha-vazio",
        )

        resultado = carregar_cadastro_resultado(ARQUIVO, COLUNAS, TOKEN, REPO)

        self.assertEqual(resultado.status, StatusLeitura.SUCESSO_VAZIO)
        self.assertEqual(resultado.sha, "sha-vazio")
        self.assertListEqual(resultado.dados.columns.tolist(), COLUNAS)

    @patch("services.dados_persistencia.ler_csv_github")
    def test_arquivo_inexistente_devolve_resultado_explicito(self, ler):
        ler.return_value = resultado_leitura(StatusLeitura.ARQUIVO_INEXISTENTE)

        resultado = carregar_cadastro_resultado(ARQUIVO, COLUNAS, TOKEN, REPO)

        self.assertEqual(resultado.status, StatusLeitura.ARQUIVO_INEXISTENTE)
        self.assertTrue(resultado.leitura_confirmada)
        self.assertListEqual(resultado.dados.columns.tolist(), COLUNAS)


class TestSalvarCadastroSeguro(unittest.TestCase):
    def setUp(self):
        self.dados = pd.DataFrame([{"Equipamento": "Bomba"}])

    @patch("services.dados_persistencia.salvar_csv_github")
    def test_atualizacao_usa_sha_da_leitura(self, salvar):
        salvar.return_value = ResultadoEscritaCSV(
            status=StatusEscrita.SUCESSO_ATUALIZADO,
            arquivo=ARQUIVO,
        )
        leitura = resultado_leitura(StatusLeitura.SUCESSO_COM_DADOS, sha="sha-lido")

        resultado = salvar_cadastro_seguro(
            self.dados,
            ARQUIVO,
            COLUNAS,
            TOKEN,
            REPO,
            resultado_leitura=leitura,
        )

        self.assertTrue(resultado.sucesso)
        salvar.assert_called_once()
        args, kwargs = salvar.call_args
        self.assertListEqual(args[0].columns.tolist(), COLUNAS)
        self.assertEqual(args[1:], (ARQUIVO, TOKEN, REPO))
        self.assertEqual(kwargs["sha_esperado"], "sha-lido")
        self.assertNotIn("criar", kwargs)

    @patch("services.dados_persistencia.salvar_csv_github")
    def test_criacao_apos_arquivo_inexistente_usa_criar_sem_sha(self, salvar):
        salvar.return_value = ResultadoEscritaCSV(
            status=StatusEscrita.SUCESSO_CRIADO,
            arquivo=ARQUIVO,
        )
        leitura = resultado_leitura(StatusLeitura.ARQUIVO_INEXISTENTE)

        resultado = salvar_cadastro_seguro(
            self.dados,
            ARQUIVO,
            COLUNAS,
            TOKEN,
            REPO,
            resultado_leitura=leitura,
        )

        self.assertTrue(resultado.sucesso)
        salvar.assert_called_once()
        _, kwargs = salvar.call_args
        self.assertTrue(kwargs["criar"])
        self.assertNotIn("sha_esperado", kwargs)

    @patch("services.dados_persistencia.salvar_csv_github")
    def test_falha_temporaria_bloqueia_escrita(self, salvar):
        leitura = resultado_leitura(StatusLeitura.FALHA_TEMPORARIA)

        resultado = salvar_cadastro_seguro(
            self.dados,
            ARQUIVO,
            COLUNAS,
            TOKEN,
            REPO,
            resultado_leitura=leitura,
        )

        self.assertEqual(resultado.status, StatusEscrita.REQUISICAO_INVALIDA)
        self.assertIn("não autorizou", resultado.erro)
        salvar.assert_not_called()

    @patch("services.dados_persistencia.salvar_csv_github")
    def test_nao_autorizado_bloqueia_escrita_sem_chamar_salvar(self, salvar):
        leitura = resultado_leitura(StatusLeitura.NAO_AUTORIZADO)

        resultado = salvar_cadastro_seguro(
            self.dados,
            ARQUIVO,
            COLUNAS,
            TOKEN,
            REPO,
            resultado_leitura=leitura,
        )

        self.assertEqual(resultado.status, StatusEscrita.REQUISICAO_INVALIDA)
        salvar.assert_not_called()


if __name__ == "__main__":
    unittest.main()
