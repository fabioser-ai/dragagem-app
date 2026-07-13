import inspect
import unittest
from unittest.mock import Mock, patch

import pandas as pd

from services.github import ResultadoLeituraCSV, StatusLeitura
from services.persistencia_multi_arquivo import (
    ResultadoPersistenciaMultiArquivo,
    SnapshotBranch,
    StatusPersistenciaMultiArquivo,
)
from tests.test_dados_crud_seguro import dados


def leitura(status, arquivo):
    return ResultadoLeituraCSV(
        status=status,
        dados=pd.DataFrame(),
        arquivo=arquivo,
        sha="sha-lido",
    )


class TestExclusaoCompostaAtestados(unittest.TestCase):
    def setUp(self):
        dados.st.success = Mock()
        dados.st.error = Mock()
        dados.st.rerun = Mock()
        self.snapshot = SnapshotBranch("main", "commit-base", "tree-base")
        self.atestados = leitura(StatusLeitura.SUCESSO_COM_DADOS, dados.ARQ_ATESTADOS)
        self.servicos = leitura(
            StatusLeitura.SUCESSO_COM_DADOS,
            dados.ARQ_ATESTADOS_SERVICOS,
        )

    def resultado_publicacao(self, status, *, erro=None, http_status=None):
        return ResultadoPersistenciaMultiArquivo(
            status=status,
            branch="main",
            arquivos=(dados.ARQ_ATESTADOS, dados.ARQ_ATESTADOS_SERVICOS),
            erro=erro,
            http_status=http_status,
        )

    def test_bloqueia_quando_leitura_de_atestados_falha(self):
        falha = leitura(StatusLeitura.FALHA_TEMPORARIA, dados.ARQ_ATESTADOS)

        self.assertFalse(
            dados.exclusao_composta_liberada(falha, self.servicos, self.snapshot)
        )

    def test_bloqueia_quando_leitura_de_servicos_falha(self):
        falha = leitura(StatusLeitura.NAO_AUTORIZADO, dados.ARQ_ATESTADOS_SERVICOS)

        self.assertFalse(
            dados.exclusao_composta_liberada(self.atestados, falha, self.snapshot)
        )

    def test_bloqueia_sem_snapshot_comum_confirmado(self):
        falha_snapshot = self.resultado_publicacao(
            StatusPersistenciaMultiArquivo.FALHA_TEMPORARIA
        )

        self.assertFalse(
            dados.exclusao_composta_liberada(
                self.atestados,
                self.servicos,
                falha_snapshot,
            )
        )

    def test_prepara_apenas_o_atestado_e_servicos_vinculados_selecionados(self):
        atestados = pd.DataFrame(
            [
                {"id_atestado": "at-1", "cliente": "Cliente 1"},
                {"id_atestado": "at-2", "cliente": "Cliente 2"},
            ]
        )
        servicos = pd.DataFrame(
            [
                {"id_servico": "s-1", "id_atestado": "at-1"},
                {"id_servico": "s-2", "id_atestado": "at-2"},
                {"id_servico": "s-3", "id_atestado": "at-1"},
            ]
        )

        atestados_novos, servicos_novos = dados.preparar_exclusao_composta(
            atestados,
            servicos,
            "at-1",
        )

        self.assertListEqual(atestados_novos["id_atestado"].tolist(), ["at-2"])
        self.assertListEqual(servicos_novos["id_servico"].tolist(), ["s-2"])
        self.assertListEqual(atestados["id_atestado"].tolist(), ["at-1", "at-2"])
        self.assertListEqual(servicos["id_servico"].tolist(), ["s-1", "s-2", "s-3"])

    @patch.object(dados, "publicar_csvs_em_commit")
    def test_encaminha_os_dois_arquivos_ao_contrato_multi_arquivo(self, publicar):
        publicar.return_value = self.resultado_publicacao(
            StatusPersistenciaMultiArquivo.SUCESSO
        )
        atestados = pd.DataFrame(columns=dados.COLUNAS_ATESTADOS)
        servicos = pd.DataFrame(columns=dados.COLUNAS_ATESTADOS_SERVICOS)

        dados._publicar_exclusao_composta(atestados, servicos)

        alteracoes, token, repo, branch, mensagem = publicar.call_args.args
        self.assertEqual(token, "token-teste")
        self.assertEqual(repo, "repo-teste")
        self.assertEqual(branch, "main")
        self.assertEqual(mensagem, "Excluir atestado e serviços vinculados")
        self.assertEqual(
            [alteracao.arquivo for alteracao in alteracoes],
            [dados.ARQ_ATESTADOS, dados.ARQ_ATESTADOS_SERVICOS],
        )
        self.assertIs(alteracoes[0].dados, atestados)
        self.assertIs(alteracoes[1].dados, servicos)

    @patch.object(dados, "publicar_csvs_em_commit")
    def test_sucesso_apresenta_feedback_e_executa_rerun(self, publicar):
        publicar.return_value = self.resultado_publicacao(
            StatusPersistenciaMultiArquivo.SUCESSO
        )

        resultado = dados._publicar_exclusao_composta(pd.DataFrame(), pd.DataFrame())

        self.assertTrue(resultado.sucesso)
        dados.st.success.assert_called_once_with(
            "Atestado e serviços vinculados foram excluídos."
        )
        dados.st.rerun.assert_called_once()
        dados.st.error.assert_not_called()

    @patch.object(dados, "publicar_csvs_em_commit")
    def test_conflito_nao_apresenta_falso_sucesso_nem_rerun(self, publicar):
        publicar.return_value = self.resultado_publicacao(
            StatusPersistenciaMultiArquivo.CONFLITO,
            erro="A branch avançou desde o snapshot observado.",
            http_status=422,
        )

        dados._publicar_exclusao_composta(pd.DataFrame(), pd.DataFrame())

        dados.st.success.assert_not_called()
        dados.st.rerun.assert_not_called()
        dados.st.error.assert_called_once_with(
            "A branch avançou desde o snapshot observado. (HTTP 422)"
        )

    @patch.object(dados, "publicar_csvs_em_commit")
    def test_falha_temporaria_nao_apresenta_falso_sucesso_nem_rerun(self, publicar):
        publicar.return_value = self.resultado_publicacao(
            StatusPersistenciaMultiArquivo.FALHA_TEMPORARIA,
            erro="GitHub indisponível.",
            http_status=503,
        )

        dados._publicar_exclusao_composta(pd.DataFrame(), pd.DataFrame())

        dados.st.success.assert_not_called()
        dados.st.rerun.assert_not_called()
        dados.st.error.assert_called_once_with("GitHub indisponível. (HTTP 503)")

    def test_confirmacao_explicita_e_fluxo_legado_removido_da_exclusao(self):
        fonte = inspect.getsource(dados)

        self.assertIn(
            "Confirmo a exclusão deste atestado e de todos os serviços vinculados.",
            fonte,
        )
        self.assertIn("disabled=not (exclusao_liberada and confirmar_exclusao)", fonte)
        self.assertIn("publicar_csvs_em_commit(", fonte)
        self.assertNotIn(
            "salvar_github(df_atestados, ARQ_ATESTADOS, TOKEN, REPO)",
            fonte,
        )
        self.assertNotIn(
            "salvar_github(df_servicos, ARQ_ATESTADOS_SERVICOS, TOKEN, REPO)",
            fonte,
        )

    def test_demais_operacoes_de_atestados_permanecem_no_contrato_por_arquivo(self):
        fonte = inspect.getsource(dados)

        self.assertIn("_salvar_atestados_seguro(", fonte)
        self.assertIn("_salvar_servicos_seguro(", fonte)
        self.assertIn("str(uuid.uuid4())", fonte)


if __name__ == "__main__":
    unittest.main()
