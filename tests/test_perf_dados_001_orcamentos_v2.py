import base64
import inspect
import unittest
from unittest.mock import patch

from modulos.orcamentos.persistencia.contratos import StatusPersistencia
from modulos.orcamentos.persistencia.github_repositorio import (
    CAMINHO_INDICE,
    ORCAMENTOS_BRANCH,
    RepositorioOrcamentosGitHub,
    caminho_versao,
)
from modulos.orcamentos.persistencia.indice import serializar_indice
from services.dados_operacionais import DATA_BRANCH
from services.persistencia_multi_arquivo import (
    ResultadoPersistenciaMultiArquivo,
    StatusPersistenciaMultiArquivo,
)
from tests.test_orcamentos_persistencia import Resposta, criar_dominio


class TestOrcamentosV2BranchOperacional(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioOrcamentosGitHub("token", "org/repo")
        self.orcamento, self.versao = criar_dominio()

    def test_branch_e_fixa_e_nao_admite_fallback_para_main(self):
        self.assertEqual(ORCAMENTOS_BRANCH, DATA_BRANCH)
        self.assertEqual(self.repositorio.branch, "data-operacional")
        self.assertNotIn("branch", inspect.signature(RepositorioOrcamentosGitHub).parameters)

    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_snapshot_operacional_controla_criacao_e_atualizacao(self, get):
        get.return_value = Resposta(200, {"object": {"sha": "snapshot"}})

        resultado = self.repositorio.carregar_snapshot()

        self.assertTrue(resultado.sucesso)
        self.assertIn("heads/data-operacional", get.call_args.args[0])

    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_indice_e_lido_da_branch_operacional(self, get):
        conteudo = base64.b64encode(serializar_indice([]).encode()).decode()
        get.return_value = Resposta(200, {"content": conteudo})

        resultado = self.repositorio.carregar_indice()

        self.assertTrue(resultado.sucesso)
        self.assertEqual(get.call_args.kwargs["params"], {"ref": "data-operacional"})
        self.assertIn(CAMINHO_INDICE, get.call_args.args[0])

    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_documento_e_aberto_da_mesma_fonte_operacional(self, get):
        from modulos.orcamentos.persistencia.serializacao import serializar_versao

        conteudo = base64.b64encode(
            serializar_versao(self.orcamento, self.versao).encode()
        ).decode()
        get.return_value = Resposta(200, {"content": conteudo})

        resultado = self.repositorio.carregar_versao("orc-1", "ver-1")

        self.assertTrue(resultado.sucesso)
        self.assertEqual(get.call_args.kwargs["params"], {"ref": "data-operacional"})
        self.assertIn(caminho_versao("orc-1", "ver-1"), get.call_args.args[0])

    @patch("modulos.orcamentos.persistencia.github_repositorio.pode", return_value=True)
    @patch("modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit")
    def test_criacao_e_versionamento_publicam_indice_e_json_atomicamente_na_operacional(
        self, publicar, _pode
    ):
        publicar.return_value = ResultadoPersistenciaMultiArquivo(
            StatusPersistenciaMultiArquivo.SUCESSO,
            "data-operacional",
            (CAMINHO_INDICE, caminho_versao("orc-1", "ver-1")),
            snapshot_commit_sha="snapshot",
            commit_sha="novo",
        )

        resultado = self.repositorio.persistir_versao(
            self.orcamento, self.versao, serializar_indice([]), "snapshot"
        )

        self.assertTrue(resultado.sucesso)
        self.assertEqual(publicar.call_args.args[3], "data-operacional")
        self.assertEqual(
            [alteracao.arquivo for alteracao in publicar.call_args.args[0]],
            [CAMINHO_INDICE, caminho_versao("orc-1", "ver-1")],
        )
        self.assertEqual(publicar.call_args.args[5], "snapshot")

    @patch("modulos.orcamentos.persistencia.github_repositorio.pode", return_value=True)
    @patch("modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit")
    def test_atualizacao_do_documento_preserva_snapshot_e_branch(self, publicar, _pode):
        publicar.return_value = ResultadoPersistenciaMultiArquivo(
            StatusPersistenciaMultiArquivo.SUCESSO,
            "data-operacional",
            (caminho_versao("orc-1", "ver-1"),),
            snapshot_commit_sha="snapshot",
            commit_sha="novo",
        )

        resultado = self.repositorio.persistir_documento_versao(
            self.orcamento, self.versao, "snapshot"
        )

        self.assertTrue(resultado.sucesso)
        self.assertEqual(publicar.call_args.args[3], "data-operacional")
        self.assertEqual(publicar.call_args.args[5], "snapshot")

    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_ausencia_confirmada_do_indice_permite_inicializacao(self, get):
        get.return_value = Resposta(404)

        resultado = self.repositorio.carregar_indice_bruto()

        self.assertTrue(resultado.sucesso)
        self.assertEqual(resultado.valor, serializar_indice([]))

    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_falha_de_leitura_nao_e_interpretada_como_indice_vazio(self, get):
        get.return_value = Resposta(503)

        resultado = self.repositorio.carregar_indice_bruto()

        self.assertEqual(resultado.status, StatusPersistencia.ERRO_REMOTO)
        self.assertIsNone(resultado.valor)

    def test_catalogos_legados_nao_fazem_parte_do_repositorio_v2(self):
        fonte = inspect.getsource(
            __import__(
                "modulos.orcamentos.persistencia.github_repositorio",
                fromlist=["github_repositorio"],
            )
        )
        for catalogo in (
            "data/equipamentos.csv",
            "data/materiais.csv",
            "data/insumos.csv",
            "data/dias.csv",
            "data/horarios.csv",
        ):
            self.assertNotIn(catalogo, fonte)


if __name__ == "__main__":
    unittest.main()
