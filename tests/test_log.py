import unittest
from unittest.mock import patch

import pandas as pd

from services.github import (
    ResultadoEscritaCSV,
    ResultadoLeituraCSV,
    StatusEscrita,
    StatusLeitura,
)
from services.log import ARQUIVO_LOG, COLUNAS_LOG, registrar_log


class TestRegistrarLog(unittest.TestCase):
    @patch("services.log.st.secrets", {"GITHUB_TOKEN": "token", "REPO": "repo"})
    @patch("services.log.salvar_csv_github")
    @patch("services.log.ler_csv_github")
    def test_sucesso_com_dados_acrescenta_registro_e_usa_sha(self, ler, salvar):
        ler.return_value = ResultadoLeituraCSV(
            status=StatusLeitura.SUCESSO_COM_DADOS,
            dados=pd.DataFrame([
                {
                    "data_hora": "2026-07-10 10:00:00",
                    "usuario": "ana",
                    "perfil": "user",
                    "acao": "login",
                }
            ]),
            arquivo=ARQUIVO_LOG,
            sha="sha-lido",
        )
        salvar.return_value = ResultadoEscritaCSV(
            status=StatusEscrita.SUCESSO_ATUALIZADO,
            arquivo=ARQUIVO_LOG,
            sha="sha-novo",
        )

        resultado = registrar_log("fabio", "superadmin", "logout")

        self.assertTrue(resultado.sucesso)
        salvar.assert_called_once()
        chamada = salvar.call_args
        df_enviado = chamada.args[0]
        self.assertEqual(len(df_enviado), 2)
        self.assertEqual(df_enviado.iloc[-1]["usuario"], "fabio")
        self.assertEqual(df_enviado.iloc[-1]["perfil"], "superadmin")
        self.assertEqual(df_enviado.iloc[-1]["acao"], "logout")
        self.assertEqual(chamada.kwargs["sha_esperado"], "sha-lido")
        self.assertNotIn("criar", chamada.kwargs)

    @patch("services.log.st.secrets", {"GITHUB_TOKEN": "token", "REPO": "repo"})
    @patch("services.log.salvar_csv_github")
    @patch("services.log.ler_csv_github")
    def test_sucesso_vazio_atualiza_com_sha(self, ler, salvar):
        ler.return_value = ResultadoLeituraCSV(
            status=StatusLeitura.SUCESSO_VAZIO,
            dados=pd.DataFrame(columns=COLUNAS_LOG),
            arquivo=ARQUIVO_LOG,
            sha="sha-vazio",
        )
        salvar.return_value = ResultadoEscritaCSV(
            status=StatusEscrita.SUCESSO_ATUALIZADO,
            arquivo=ARQUIVO_LOG,
        )

        registrar_log("fabio", "superadmin", "login")

        chamada = salvar.call_args
        self.assertEqual(len(chamada.args[0]), 1)
        self.assertEqual(chamada.kwargs["sha_esperado"], "sha-vazio")

    @patch("services.log.st.secrets", {"GITHUB_TOKEN": "token", "REPO": "repo"})
    @patch("services.log.salvar_csv_github")
    @patch("services.log.ler_csv_github")
    def test_arquivo_inexistente_cria_explicitamente_sem_sha(self, ler, salvar):
        ler.return_value = ResultadoLeituraCSV(
            status=StatusLeitura.ARQUIVO_INEXISTENTE,
            dados=pd.DataFrame(),
            arquivo=ARQUIVO_LOG,
            http_status=404,
        )
        salvar.return_value = ResultadoEscritaCSV(
            status=StatusEscrita.SUCESSO_CRIADO,
            arquivo=ARQUIVO_LOG,
        )

        resultado = registrar_log("fabio", "superadmin", "login")

        self.assertTrue(resultado.sucesso)
        chamada = salvar.call_args
        self.assertEqual(chamada.kwargs["criar"], True)
        self.assertNotIn("sha_esperado", chamada.kwargs)
        self.assertEqual(chamada.args[0].columns.tolist(), COLUNAS_LOG)
        self.assertEqual(len(chamada.args[0]), 1)

    @patch("services.log.st.secrets", {"GITHUB_TOKEN": "token", "REPO": "repo"})
    @patch("services.log.salvar_csv_github")
    @patch("services.log.ler_csv_github")
    def test_falha_de_leitura_bloqueia_escrita(self, ler, salvar):
        falha = ResultadoLeituraCSV(
            status=StatusLeitura.FALHA_TEMPORARIA,
            dados=pd.DataFrame(),
            arquivo=ARQUIVO_LOG,
            http_status=500,
            erro="GitHub indisponível",
        )
        ler.return_value = falha

        resultado = registrar_log("fabio", "superadmin", "login")

        self.assertIs(resultado, falha)
        salvar.assert_not_called()

    @patch("services.log.st.secrets", {"GITHUB_TOKEN": "token", "REPO": "repo"})
    @patch("services.log.salvar_csv_github")
    @patch("services.log.ler_csv_github")
    def test_normaliza_colunas_ausentes_sem_mudar_schema_final(self, ler, salvar):
        ler.return_value = ResultadoLeituraCSV(
            status=StatusLeitura.SUCESSO_COM_DADOS,
            dados=pd.DataFrame([{"usuario": "ana"}]),
            arquivo=ARQUIVO_LOG,
            sha="sha-lido",
        )
        salvar.return_value = ResultadoEscritaCSV(
            status=StatusEscrita.SUCESSO_ATUALIZADO,
            arquivo=ARQUIVO_LOG,
        )

        registrar_log("fabio", "superadmin", "logout")

        df_enviado = salvar.call_args.args[0]
        self.assertEqual(df_enviado.columns.tolist(), COLUNAS_LOG)
        self.assertEqual(len(df_enviado), 2)
        self.assertEqual(df_enviado.iloc[0]["usuario"], "ana")


if __name__ == "__main__":
    unittest.main()
