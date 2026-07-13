import inspect
import unittest
from unittest.mock import Mock, patch

import pandas as pd

from services.github import ResultadoEscritaCSV, ResultadoLeituraCSV, StatusEscrita, StatusLeitura
from tests.test_dados_crud_seguro import dados


class TestAtestadosPersistenciaSegura(unittest.TestCase):
    def resultado(self, status, sha=None, arquivo="teste.csv"):
        return ResultadoLeituraCSV(status=status, dados=pd.DataFrame(), arquivo=arquivo, sha=sha)

    def test_leitura_confirmada_libera_escrita(self):
        resultado = self.resultado(StatusLeitura.SUCESSO_VAZIO, "sha")
        self.assertTrue(resultado.pode_sobrescrever)

    def test_arquivo_inexistente_permite_criacao(self):
        resultado = self.resultado(StatusLeitura.ARQUIVO_INEXISTENTE)
        self.assertTrue(resultado.leitura_confirmada)

    def test_schemas_permanecem_exatos(self):
        self.assertEqual(dados.COLUNAS_ATESTADOS, ["id_atestado", "cliente", "contrato", "obra", "local", "ano", "data_inicio", "data_fim", "descricao", "observacoes"])
        self.assertEqual(dados.COLUNAS_ATESTADOS_SERVICOS, ["id_servico", "id_atestado", "servico", "unidade", "quantidade", "observacoes"])

    @patch.object(dados, "carregar_cadastro_resultado")
    def test_garantir_estrutura_faz_duas_leituras_e_preserva_resultados(self, carregar):
        atestados = self.resultado(StatusLeitura.SUCESSO_COM_DADOS, "sha-atestados", dados.ARQ_ATESTADOS)
        atestados = atestados.__class__(atestados.status, pd.DataFrame([{coluna: "" for coluna in dados.COLUNAS_ATESTADOS}]), atestados.arquivo, sha=atestados.sha)
        servicos = ResultadoLeituraCSV(StatusLeitura.SUCESSO_VAZIO, pd.DataFrame(columns=dados.COLUNAS_ATESTADOS_SERVICOS), dados.ARQ_ATESTADOS_SERVICOS, sha="sha-servicos")
        carregar.side_effect = [atestados, servicos]
        df_at, df_se, res_at, res_se = dados.garantir_estrutura_atestados()
        self.assertEqual(carregar.call_args_list[0].args[:2], (dados.ARQ_ATESTADOS, dados.COLUNAS_ATESTADOS))
        self.assertEqual(carregar.call_args_list[1].args[:2], (dados.ARQ_ATESTADOS_SERVICOS, dados.COLUNAS_ATESTADOS_SERVICOS))
        self.assertEqual(res_at.sha, "sha-atestados")
        self.assertEqual(res_se.sha, "sha-servicos")
        self.assertListEqual(df_at.columns.tolist(), dados.COLUNAS_ATESTADOS)
        self.assertListEqual(df_se.columns.tolist(), dados.COLUNAS_ATESTADOS_SERVICOS)

    def test_decisao_de_escrita_cobre_estados(self):
        self.assertTrue(dados.escrita_liberada(self.resultado(StatusLeitura.SUCESSO_COM_DADOS, "a")))
        self.assertTrue(dados.escrita_liberada(self.resultado(StatusLeitura.SUCESSO_VAZIO, "a")))
        self.assertTrue(dados.escrita_liberada(self.resultado(StatusLeitura.ARQUIVO_INEXISTENTE)))
        self.assertFalse(dados.escrita_liberada(self.resultado(StatusLeitura.FALHA_TEMPORARIA)))
        self.assertFalse(dados.escrita_liberada(self.resultado(StatusLeitura.NAO_AUTORIZADO)))

    @patch.object(dados, "_salvar_cadastro")
    def test_helpers_encaminham_resultados_independentes(self, salvar):
        at = self.resultado(StatusLeitura.SUCESSO_COM_DADOS, "sha-at")
        se = self.resultado(StatusLeitura.SUCESSO_COM_DADOS, "sha-se")
        dados._salvar_atestados_seguro(pd.DataFrame(), at, "ok", "erro")
        self.assertEqual(salvar.call_args.args[1:4], (dados.ARQ_ATESTADOS, dados.COLUNAS_ATESTADOS, at))
        dados._salvar_servicos_seguro(pd.DataFrame(), se, "ok", "erro")
        self.assertEqual(salvar.call_args.args[1:4], (dados.ARQ_ATESTADOS_SERVICOS, dados.COLUNAS_ATESTADOS_SERVICOS, se))

    def test_feedback_sucesso_e_falha(self):
        dados.st.success = Mock(); dados.st.error = Mock(); dados.st.rerun = Mock()
        with patch.object(dados, "salvar_cadastro_seguro", return_value=ResultadoEscritaCSV(StatusEscrita.SUCESSO_ATUALIZADO, dados.ARQ_ATESTADOS)):
            dados._salvar_atestados_seguro(pd.DataFrame(), self.resultado(StatusLeitura.SUCESSO_COM_DADOS, "a"), "ok", "erro")
        dados.st.rerun.assert_called_once()
        dados.st.rerun.reset_mock()
        with patch.object(dados, "salvar_cadastro_seguro", return_value=ResultadoEscritaCSV(StatusEscrita.CONFLITO, dados.ARQ_ATESTADOS, http_status=409, erro="conflito")):
            dados._salvar_servicos_seguro(pd.DataFrame(), self.resultado(StatusLeitura.SUCESSO_COM_DADOS, "s"), "ok", "erro")
        dados.st.rerun.assert_not_called()
        dados.st.error.assert_called_with("conflito (HTTP 409)")

    def test_fluxos_preservados_por_fonte(self):
        fonte = inspect.getsource(dados)
        self.assertIn('publicar_csvs_em_commit(', fonte)
        self.assertNotIn('salvar_github(df_atestados, ARQ_ATESTADOS, TOKEN, REPO)', fonte)
        self.assertNotIn('salvar_github(df_servicos, ARQ_ATESTADOS_SERVICOS, TOKEN, REPO)', fonte)
        self.assertIn('str(uuid.uuid4())', fonte)
        self.assertIn('disabled=not escrita_atestados_liberada', fonte)
        self.assertIn('disabled=not escrita_servicos_liberada', fonte)


if __name__ == "__main__":
    unittest.main()
