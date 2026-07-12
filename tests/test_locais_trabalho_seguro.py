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


def carregar_modulo():
    streamlit = types.ModuleType("streamlit")
    streamlit.secrets = {
        "GITHUB_TOKEN": "token-teste",
        "REPO": "repo-teste",
    }

    repositorio = types.ModuleType("modulos.medicoes.repositorio")
    repositorio.carregar_bases = Mock()

    with patch.dict(
        sys.modules,
        {
            "streamlit": streamlit,
            "modulos.medicoes.repositorio": repositorio,
        },
    ):
        sys.modules.pop("pages.dados_detalhados.locais_trabalho", None)
        return importlib.import_module(
            "pages.dados_detalhados.locais_trabalho"
        )


locais = carregar_modulo()


def resultado_leitura(status, *, erro=None, http_status=None, sha=None):
    return ResultadoLeituraCSV(
        status=status,
        dados=pd.DataFrame(columns=locais.COLUNAS),
        arquivo=locais.ARQUIVO,
        erro=erro,
        http_status=http_status,
        sha=sha,
    )


class TestAdaptadoresLocais(unittest.TestCase):
    @patch.object(locais, "carregar_cadastro_resultado")
    def test_carregar_locais_usa_arquivo_schema_e_credenciais(self, carregar):
        esperado = resultado_leitura(
            StatusLeitura.SUCESSO_VAZIO,
            sha="sha-lido",
        )
        carregar.return_value = esperado

        resultado = locais.carregar_locais_resultado()

        self.assertIs(resultado, esperado)
        carregar.assert_called_once_with(
            locais.ARQUIVO,
            locais.COLUNAS,
            "token-teste",
            "repo-teste",
        )

    @patch.object(locais, "salvar_cadastro_seguro")
    def test_salvar_locais_encaminha_resultado_original(self, salvar):
        leitura = resultado_leitura(
            StatusLeitura.SUCESSO_COM_DADOS,
            sha="sha-original",
        )
        esperado = ResultadoEscritaCSV(
            status=StatusEscrita.SUCESSO_ATUALIZADO,
            arquivo=locais.ARQUIVO,
        )
        salvar.return_value = esperado
        df = pd.DataFrame(columns=locais.COLUNAS)

        resultado = locais.salvar_locais_seguro(df, leitura)

        self.assertIs(resultado, esperado)
        salvar.assert_called_once_with(
            df,
            locais.ARQUIVO,
            locais.COLUNAS,
            "token-teste",
            "repo-teste",
            resultado_leitura=leitura,
        )


class TestDecisaoEscrita(unittest.TestCase):
    def test_leitura_confirmada_autoriza_atualizacao(self):
        resultado = resultado_leitura(
            StatusLeitura.SUCESSO_COM_DADOS,
            sha="sha",
        )

        self.assertTrue(resultado.pode_sobrescrever)

    def test_arquivo_inexistente_autoriza_criacao(self):
        resultado = resultado_leitura(
            StatusLeitura.ARQUIVO_INEXISTENTE
        )
        escrita_liberada = (
            resultado.pode_sobrescrever
            or resultado.status == StatusLeitura.ARQUIVO_INEXISTENTE
        )

        self.assertTrue(escrita_liberada)

    def test_falha_temporaria_bloqueia_escrita(self):
        resultado = resultado_leitura(
            StatusLeitura.FALHA_TEMPORARIA,
            erro="GitHub indisponível",
            http_status=500,
        )
        escrita_liberada = (
            resultado.pode_sobrescrever
            or resultado.status == StatusLeitura.ARQUIVO_INEXISTENTE
        )

        self.assertFalse(escrita_liberada)

    def test_nao_autorizado_bloqueia_escrita(self):
        resultado = resultado_leitura(
            StatusLeitura.NAO_AUTORIZADO,
            http_status=401,
        )
        escrita_liberada = (
            resultado.pode_sobrescrever
            or resultado.status == StatusLeitura.ARQUIVO_INEXISTENTE
        )

        self.assertFalse(escrita_liberada)


class TestFeedback(unittest.TestCase):
    def test_detalhes_inclui_erro_e_http(self):
        resultado = resultado_leitura(
            StatusLeitura.FALHA_TEMPORARIA,
            erro="Falha temporária",
            http_status=503,
        )

        self.assertEqual(
            locais.detalhes_resultado(resultado, "Falha padrão"),
            "Falha temporária (HTTP 503)",
        )

    def test_detalhes_usa_mensagem_padrao_sem_erro(self):
        resultado = resultado_leitura(
            StatusLeitura.CONTEUDO_INVALIDO
        )

        self.assertEqual(
            locais.detalhes_resultado(resultado, "Leitura inválida"),
            "Leitura inválida",
        )


class TestRegrasPreservadas(unittest.TestCase):
    def test_schema_permanece_inalterado(self):
        self.assertEqual(
            locais.COLUNAS,
            [
                "local_id",
                "obra_id",
                "nome_local",
                "ativo",
                "observacoes",
                "criado_em",
                "atualizado_em",
            ],
        )

    def test_identificador_mantem_formato(self):
        identificador = locais.gerar_local_id()

        self.assertTrue(identificador.startswith("LOC_"))
        self.assertEqual(len(identificador), 12)


if __name__ == "__main__":
    unittest.main()
