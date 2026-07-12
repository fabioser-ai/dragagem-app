import importlib
import sys
import types
import unittest
from unittest.mock import Mock, patch

import pandas as pd

from services.github import (
    ResultadoEscritaCSV,
    ResultadoLeituraCSV,
    StatusEscrita,
    StatusLeitura,
)


def carregar_dados():
    streamlit = types.ModuleType("streamlit")
    streamlit.secrets = {"GITHUB_TOKEN": "token-teste", "REPO": "repo-teste"}
    locais = types.ModuleType("pages.dados_detalhados.locais_trabalho")
    locais.render_locais_trabalho = Mock()

    with patch.dict(
        sys.modules,
        {
            "streamlit": streamlit,
            "pages.dados_detalhados.locais_trabalho": locais,
        },
    ):
        sys.modules.pop("pages.dados", None)
        return importlib.import_module("pages.dados")


dados = carregar_dados()
COLUNAS = ["Equipamento", "Vazao"]
ARQUIVO = "data/equipamentos.csv"


def leitura(status, *, erro=None, http_status=None, sha=None):
    return ResultadoLeituraCSV(
        status=status,
        dados=pd.DataFrame(columns=COLUNAS),
        arquivo=ARQUIVO,
        erro=erro,
        http_status=http_status,
        sha=sha,
    )


class TestSalvarCadastro(unittest.TestCase):
    def setUp(self):
        dados.st.success = Mock()
        dados.st.error = Mock()
        dados.st.rerun = Mock()

    @patch.object(dados, "salvar_cadastro_seguro")
    def test_sucesso_apresenta_mensagem_e_executa_rerun(self, salvar):
        salvar.return_value = ResultadoEscritaCSV(
            status=StatusEscrita.SUCESSO_ATUALIZADO,
            arquivo=ARQUIVO,
        )
        resultado_leitura = leitura(StatusLeitura.SUCESSO_COM_DADOS, sha="sha-lido")

        dados._salvar_cadastro(
            pd.DataFrame(), ARQUIVO, COLUNAS, resultado_leitura, "Sucesso", "Falha"
        )

        dados.st.success.assert_called_once_with("Sucesso")
        dados.st.rerun.assert_called_once()

    @patch.object(dados, "salvar_cadastro_seguro")
    def test_falha_apresenta_erro_sem_rerun_e_com_http(self, salvar):
        salvar.return_value = ResultadoEscritaCSV(
            status=StatusEscrita.CONFLITO,
            arquivo=ARQUIVO,
            erro="Conflito detectado",
            http_status=409,
        )

        dados._salvar_cadastro(
            pd.DataFrame(),
            ARQUIVO,
            COLUNAS,
            leitura(StatusLeitura.SUCESSO_COM_DADOS),
            "Sucesso",
            "Falha",
        )

        dados.st.error.assert_called_once_with("Conflito detectado (HTTP 409)")
        dados.st.rerun.assert_not_called()

    @patch.object(dados, "salvar_cadastro_seguro")
    def test_encaminha_resultado_leitura_arquivo_e_schema(self, salvar):
        salvar.return_value = ResultadoEscritaCSV(
            status=StatusEscrita.SUCESSO_ATUALIZADO,
            arquivo=ARQUIVO,
        )
        resultado_leitura = leitura(StatusLeitura.SUCESSO_COM_DADOS, sha="sha-original")

        dados._salvar_cadastro(
            pd.DataFrame(), ARQUIVO, COLUNAS, resultado_leitura, "Sucesso", "Falha"
        )

        args, kwargs = salvar.call_args
        self.assertEqual(args[1:], (ARQUIVO, COLUNAS, "token-teste", "repo-teste"))
        self.assertIs(kwargs["resultado_leitura"], resultado_leitura)


class TestDecisaoLeitura(unittest.TestCase):
    def test_leitura_confirmada_libera_escrita(self):
        resultado = leitura(StatusLeitura.SUCESSO_VAZIO, sha="sha")

        self.assertTrue(resultado.pode_sobrescrever)

    def test_arquivo_inexistente_libera_criacao(self):
        resultado = leitura(StatusLeitura.ARQUIVO_INEXISTENTE)
        escrita_liberada = (
            resultado.pode_sobrescrever
            or resultado.status == StatusLeitura.ARQUIVO_INEXISTENTE
        )

        self.assertTrue(escrita_liberada)

    def test_falha_de_leitura_gera_mensagem_de_bloqueio(self):
        resultado = leitura(
            StatusLeitura.FALHA_TEMPORARIA,
            erro="GitHub indisponível",
            http_status=500,
        )

        mensagem = (
            "As alterações estão bloqueadas para preservar os dados. "
            + dados._detalhes_resultado(resultado, "Leitura não confirmada")
        )

        self.assertEqual(
            mensagem,
            "As alterações estão bloqueadas para preservar os dados. GitHub indisponível (HTTP 500)",
        )


class TestConversoesLegadas(unittest.TestCase):
    def test_parse_moeda_mantem_comportamento_atual(self):
        self.assertEqual(dados.parse_moeda("1.234,50"), 1234.5)

    def test_converter_valores_mantem_comportamento_atual(self):
        self.assertEqual(
            dados.converter_valores(["Vazao", "Nome"], ["1,5", "Bomba"]),
            [1.5, "Bomba"],
        )


if __name__ == "__main__":
    unittest.main()
