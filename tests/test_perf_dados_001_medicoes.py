import unittest
from unittest.mock import Mock, patch

import pandas as pd

from modulos.medicoes import persistencia
from modulos.medicoes import repositorio as repositorio_medicoes
from modulos.medicoes.lancamentos import repositorio as repositorio_lancamentos
from modulos.medicoes.config import (
    ARQ_FRENTES,
    ARQ_ITENS,
    ARQ_LANCAMENTOS_PRODUCAO,
    ARQ_LOCAIS_TRABALHO,
    ARQ_MC,
    ARQ_MEDICAO,
    ARQ_MEDICOES,
    ARQ_OBRAS,
    ARQ_SERVICOS,
    ARQ_TABELAS_SERVICOS_DIR,
    ARQ_USUARIOS_OBRAS,
)
from services.github import StatusLeitura


OPERACIONAIS = {
    ARQ_OBRAS,
    ARQ_MEDICOES,
    ARQ_FRENTES,
    ARQ_MC,
    ARQ_ITENS,
    ARQ_LOCAIS_TRABALHO,
    ARQ_LANCAMENTOS_PRODUCAO,
}


class TestPerfDados001Medicoes(unittest.TestCase):
    def test_classificacao_operacional_e_exata(self):
        self.assertEqual(persistencia.ARQUIVOS_OPERACIONAIS, OPERACIONAIS)
        self.assertNotIn(ARQ_MEDICAO, persistencia.ARQUIVOS_OPERACIONAIS)
        self.assertNotIn(ARQ_SERVICOS, persistencia.ARQUIVOS_OPERACIONAIS)
        self.assertNotIn(ARQ_USUARIOS_OBRAS, persistencia.ARQUIVOS_OPERACIONAIS)
        self.assertFalse(
            persistencia.arquivo_operacional(
                f"{ARQ_TABELAS_SERVICOS_DIR}/contrato.csv"
            )
        )

    def test_repositorios_do_fluxo_compartilham_o_mesmo_roteador(self):
        self.assertIs(repositorio_medicoes.carregar_github, persistencia.carregar_github)
        self.assertIs(repositorio_medicoes.salvar_github, persistencia.salvar_github)
        self.assertIs(
            repositorio_lancamentos.carregar_github,
            persistencia.carregar_github,
        )
        self.assertIs(
            repositorio_lancamentos.salvar_github,
            persistencia.salvar_github,
        )

    @patch("modulos.medicoes.persistencia.ler_csv_operacional")
    def test_todo_fluxo_encadeado_le_na_mesma_branch_operacional(self, ler):
        ler.return_value = Mock(
            leitura_confirmada=True,
            dados=pd.DataFrame([{"id": "1"}]),
        )

        for caminho in OPERACIONAIS:
            persistencia.carregar_github(caminho, "token", "repo")

        self.assertEqual(
            [chamada.args[0] for chamada in ler.call_args_list],
            list(OPERACIONAIS),
        )
        self.assertEqual(persistencia.DATA_BRANCH, "data-operacional")

    @patch("modulos.medicoes.persistencia.salvar_csv_operacional")
    @patch("modulos.medicoes.persistencia.ler_csv_operacional")
    def test_todo_fluxo_encadeado_escreve_com_sha_na_branch_operacional(
        self, ler, salvar
    ):
        ler.return_value = Mock(
            pode_sobrescrever=True,
            sha="sha-observado",
            status=StatusLeitura.SUCESSO_COM_DADOS,
        )
        salvar.return_value = Mock(sucesso=True)

        for caminho in OPERACIONAIS:
            persistencia.salvar_github(
                pd.DataFrame([{"id": "1"}]), caminho, "token", "repo"
            )

        self.assertEqual(
            [chamada.args[1] for chamada in salvar.call_args_list],
            list(OPERACIONAIS),
        )
        for chamada in salvar.call_args_list:
            self.assertEqual(chamada.kwargs["sha_esperado"], "sha-observado")

    @patch("modulos.medicoes.persistencia.salvar_csv_operacional")
    @patch("modulos.medicoes.persistencia.ler_csv_operacional")
    def test_falha_de_leitura_bloqueia_escrita_sem_fallback(self, ler, salvar):
        ler.return_value = Mock(
            pode_sobrescrever=False,
            status=StatusLeitura.FALHA_TEMPORARIA,
        )

        with patch.object(persistencia, "salvar_github_main") as salvar_main:
            with self.assertRaises(RuntimeError):
                persistencia.salvar_github(
                    pd.DataFrame(), ARQ_MEDICOES, "token", "repo"
                )

        salvar.assert_not_called()
        salvar_main.assert_not_called()

    @patch("modulos.medicoes.persistencia.ler_csv_operacional")
    def test_falha_de_leitura_nao_consulta_main(self, ler):
        ler.return_value = Mock(
            leitura_confirmada=False,
            status=StatusLeitura.FALHA_TEMPORARIA,
        )

        with patch.object(persistencia, "carregar_github_main") as carregar_main:
            with self.assertRaises(RuntimeError):
                persistencia.carregar_github(ARQ_MEDICOES, "token", "repo")

        carregar_main.assert_not_called()

    def test_catalogos_e_seguranca_permanecem_na_main(self):
        for caminho in (ARQ_MEDICAO, ARQ_SERVICOS, ARQ_USUARIOS_OBRAS):
            with self.subTest(caminho=caminho), patch.object(
                persistencia, "carregar_github_main", return_value=pd.DataFrame()
            ) as carregar:
                persistencia.carregar_github(caminho, "token", "repo")
                carregar.assert_called_once_with(caminho, "token", "repo")

            with self.subTest(caminho=caminho), patch.object(
                persistencia, "salvar_github_main"
            ) as salvar:
                persistencia.salvar_github(
                    pd.DataFrame(), caminho, "token", "repo"
                )
                salvar.assert_called_once()

    @patch("modulos.medicoes.persistencia.requests.put")
    @patch("modulos.medicoes.persistencia.requests.get")
    def test_foto_de_lancamento_usa_branch_operacional(self, get, put):
        get.return_value = Mock(status_code=404)
        put.return_value = Mock(status_code=201)

        persistencia.salvar_arquivo_github(
            b"foto",
            "data/medicoes/fotos_lancamentos/LAN-1.jpg",
            "token",
            "repo",
        )

        self.assertEqual(get.call_args.kwargs["params"], {"ref": "data-operacional"})
        self.assertEqual(put.call_args.kwargs["json"]["branch"], "data-operacional")


if __name__ == "__main__":
    unittest.main()
