import unittest
from datetime import date as data_real
from unittest.mock import Mock, call, patch

import pandas as pd

import scripts.enviar_alertas_ferias as alertas
from services import dados_operacionais
from services.github import (
    ResultadoEscritaCSV,
    ResultadoLeituraCSV,
    StatusEscrita,
    StatusLeitura,
)


class DataFixa:
    @classmethod
    def today(cls):
        return data_real(2026, 8, 27)


class TestAlertasFeriasOperacionais(unittest.TestCase):
    def setUp(self):
        self.ambiente = {
            "GITHUB_TOKEN": "token",
            "REPO": "fabioser-ai/dragagem-app",
            "EMAIL_DESTINO_ALERTAS": "destino@example.com",
            "EMAIL_SMTP_HOST": "smtp.example.com",
            "EMAIL_SMTP_PORT": "587",
            "EMAIL_USUARIO": "usuario",
            "EMAIL_SENHA": "senha",
            "EMAIL_ORIGEM": "origem@example.com",
        }
        self.ferias = pd.DataFrame(
            [
                {
                    "Matricula": "123",
                    "Funcionario": "Pessoa Teste",
                    "Unidade": "U1",
                    "Departamento": "D1",
                    "Limite_Gozo": "2026-09-26",
                    "Data_Inicio_Gozo": "",
                    "Data_Fim_Gozo": "",
                    "Periodo_Gozo": "",
                }
            ]
        )

    def leitura(self, arquivo, dados=None, *, status=StatusLeitura.SUCESSO_COM_DADOS, sha="sha-lido", erro=None):
        return ResultadoLeituraCSV(
            status=status,
            dados=dados if dados is not None else pd.DataFrame(),
            arquivo=arquivo,
            sha=sha,
            erro=erro,
        )

    def executar(self, resultado_historico, *, resultado_ferias=None, escrita=None):
        resultado_ferias = resultado_ferias or self.leitura(
            alertas.ARQ_FERIAS, self.ferias, sha="sha-ferias"
        )
        escrita = escrita or ResultadoEscritaCSV(
            status=StatusEscrita.SUCESSO_ATUALIZADO,
            arquivo=alertas.ARQ_HISTORICO,
        )
        with patch.dict(alertas.os.environ, self.ambiente, clear=True), patch.object(
            alertas, "date", DataFixa
        ), patch.object(
            alertas,
            "carregar_github",
            side_effect=[resultado_ferias, resultado_historico],
        ) as carregar, patch.object(
            alertas, "salvar_github", return_value=escrita
        ) as salvar, patch.object(
            alertas, "enviar_email_smtp"
        ) as smtp:
            alertas.main()
        return carregar, salvar, smtp

    def test_aliases_usam_backend_operacional_sem_fallback_para_main(self):
        self.assertIs(alertas.carregar_github, dados_operacionais.ler_csv_operacional)
        self.assertIs(alertas.salvar_github, dados_operacionais.salvar_csv_operacional)
        self.assertEqual(dados_operacionais.DATA_BRANCH, "data-operacional")

    def test_le_as_duas_bases_operacionais_e_atualiza_historico_com_sha(self):
        historico = self.leitura(
            alertas.ARQ_HISTORICO,
            pd.DataFrame(columns=alertas.COLUNAS_HISTORICO),
            status=StatusLeitura.SUCESSO_VAZIO,
            sha="sha-historico",
        )

        carregar, salvar, smtp = self.executar(historico)

        self.assertEqual(
            carregar.call_args_list,
            [
                call(alertas.ARQ_FERIAS, "token", self.ambiente["REPO"]),
                call(alertas.ARQ_HISTORICO, "token", self.ambiente["REPO"]),
            ],
        )
        smtp.assert_called_once()
        self.assertEqual(salvar.call_args.kwargs, {"sha_esperado": "sha-historico"})

    def test_historico_inexistente_usa_criacao_explicita(self):
        historico = self.leitura(
            alertas.ARQ_HISTORICO,
            status=StatusLeitura.ARQUIVO_INEXISTENTE,
            sha=None,
        )

        _, salvar, smtp = self.executar(historico)

        smtp.assert_called_once()
        self.assertEqual(salvar.call_args.kwargs, {"criar": True})

    def test_falha_na_leitura_de_ferias_aborta_antes_do_historico_e_smtp(self):
        falha = self.leitura(
            alertas.ARQ_FERIAS,
            status=StatusLeitura.FALHA_TEMPORARIA,
            sha=None,
            erro="timeout",
        )
        carregar = Mock(return_value=falha)
        smtp = Mock()

        with patch.dict(alertas.os.environ, self.ambiente, clear=True), patch.object(
            alertas, "date", DataFixa
        ), patch.object(alertas, "carregar_github", carregar), patch.object(
            alertas, "enviar_email_smtp", smtp
        ), self.assertRaisesRegex(RuntimeError, "Leitura de data/ferias.csv não confirmada"):
            alertas.main()

        carregar.assert_called_once_with(alertas.ARQ_FERIAS, "token", self.ambiente["REPO"])
        smtp.assert_not_called()

    def test_falha_na_leitura_do_historico_aborta_antes_do_smtp(self):
        falha = self.leitura(
            alertas.ARQ_HISTORICO,
            status=StatusLeitura.NAO_AUTORIZADO,
            sha=None,
            erro="sem autorização",
        )
        with patch.dict(alertas.os.environ, self.ambiente, clear=True), patch.object(
            alertas, "date", DataFixa
        ), patch.object(
            alertas,
            "carregar_github",
            side_effect=[self.leitura(alertas.ARQ_FERIAS, self.ferias), falha],
        ), patch.object(alertas, "enviar_email_smtp") as smtp, patch.object(
            alertas, "salvar_github"
        ) as salvar, self.assertRaisesRegex(RuntimeError, "Leitura de data/alertas_ferias_enviados.csv não confirmada"):
            alertas.main()

        smtp.assert_not_called()
        salvar.assert_not_called()

    def test_id_alerta_existente_mantem_idempotencia(self):
        id_alerta = alertas.montar_id_alerta("123", "2026-09-26", 30)
        linha = {coluna: "" for coluna in alertas.COLUNAS_HISTORICO}
        linha["ID_Alerta"] = id_alerta
        historico = self.leitura(alertas.ARQ_HISTORICO, pd.DataFrame([linha]))

        _, salvar, smtp = self.executar(historico)

        smtp.assert_not_called()
        salvar.assert_not_called()

    def test_falha_de_escrita_pos_envio_e_explicita(self):
        historico = self.leitura(
            alertas.ARQ_HISTORICO,
            pd.DataFrame(columns=alertas.COLUNAS_HISTORICO),
            status=StatusLeitura.SUCESSO_VAZIO,
        )
        falha = ResultadoEscritaCSV(
            status=StatusEscrita.CONFLITO,
            arquivo=alertas.ARQ_HISTORICO,
            erro="conflito",
        )

        with self.assertRaisesRegex(RuntimeError, "Falha ao atualizar"):
            self.executar(historico, escrita=falha)

    def test_marcos_permanecem_inalterados(self):
        self.assertEqual(alertas.MARCOS_ALERTA, [60, 50, 40, 30, 20, 10, 0])
        for marco in alertas.MARCOS_ALERTA:
            self.assertEqual(alertas.definir_marco_alerta(marco), marco)
        self.assertIsNone(alertas.definir_marco_alerta(1))


if __name__ == "__main__":
    unittest.main()
