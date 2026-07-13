import importlib
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import pandas as pd

from services.github import ResultadoLeituraCSV, StatusLeitura
from services.persistencia_multi_arquivo import (
    ResultadoPersistenciaMultiArquivo,
    SnapshotBranch,
    StatusPersistenciaMultiArquivo,
)


def carregar_repositorio():
    streamlit = types.ModuleType("streamlit")
    streamlit.secrets = {"GITHUB_TOKEN": "token-teste", "REPO": "repo-teste"}
    streamlit.error = Mock()
    streamlit.exception = Mock()

    with patch.dict(sys.modules, {"streamlit": streamlit}):
        sys.modules.pop("pages.crm.repositorio", None)
        return importlib.import_module("pages.crm.repositorio")


repositorio = carregar_repositorio()
ETAPA_INTERACOES = Path("pages/crm/etapa3_interacoes.py")


def resultado_leitura(status, arquivo, dados):
    return ResultadoLeituraCSV(
        status=status,
        dados=dados,
        arquivo=arquivo,
        sha="sha-lido",
    )


class TestInteracaoAtomicaCRM(unittest.TestCase):
    def setUp(self):
        self.snapshot = SnapshotBranch("main", "commit-base", "tree-base")
        self.clientes = pd.DataFrame(
            [
                {
                    **{coluna: "" for coluna in repositorio.COLUNAS_CLIENTES},
                    "id_cliente": "cliente-1",
                    "nome_empresa": "Empresa selecionada",
                    "responsavel": "Responsável anterior",
                    "ultimo_contato": "2026-01-01",
                    "proxima_acao": "Ação anterior",
                    "data_proxima_acao": "2026-01-02",
                    "updated_at": "2026-01-01 10:00:00",
                },
                {
                    **{coluna: "" for coluna in repositorio.COLUNAS_CLIENTES},
                    "id_cliente": "cliente-2",
                    "nome_empresa": "Empresa preservada",
                    "responsavel": "Outro responsável",
                    "ultimo_contato": "2026-02-01",
                    "proxima_acao": "Outra ação",
                    "data_proxima_acao": "2026-02-02",
                    "updated_at": "2026-02-01 10:00:00",
                },
            ]
        )
        self.interacoes = pd.DataFrame(
            [
                {
                    **{coluna: "" for coluna in repositorio.COLUNAS_INTERACOES},
                    "id_interacao": "interacao-existente",
                    "id_cliente": "cliente-2",
                    "descricao": "Interação preservada",
                }
            ]
        )
        self.resultado_clientes = resultado_leitura(
            StatusLeitura.SUCESSO_COM_DADOS,
            repositorio.ARQ_CLIENTES,
            self.clientes,
        )
        self.resultado_interacoes = resultado_leitura(
            StatusLeitura.SUCESSO_COM_DADOS,
            repositorio.ARQ_INTERACOES,
            self.interacoes,
        )
        self.dados = {
            "id_cliente": "cliente-1",
            "id_contato": "contato-1",
            "data_interacao": "2026-07-13",
            "tipo_contato": "Telefone",
            "descricao": "Nova interação",
            "responsavel": "Novo responsável",
            "resultado": "Contato realizado",
            "proxima_acao": "Enviar proposta",
            "data_proxima_acao": "2026-07-20",
        }

    def resultado_publicacao(self, status, *, erro=None, http_status=None):
        return ResultadoPersistenciaMultiArquivo(
            status=status,
            branch="main",
            arquivos=(repositorio.ARQ_INTERACOES, repositorio.ARQ_CLIENTES),
            erro=erro,
            http_status=http_status,
        )

    def test_bloqueia_quando_leitura_de_clientes_falha(self):
        falha = resultado_leitura(
            StatusLeitura.FALHA_TEMPORARIA,
            repositorio.ARQ_CLIENTES,
            pd.DataFrame(columns=repositorio.COLUNAS_CLIENTES),
        )

        self.assertFalse(
            repositorio.cadastro_interacao_liberado(
                falha,
                self.resultado_interacoes,
                self.snapshot,
            )
        )

    def test_bloqueia_quando_leitura_de_interacoes_falha(self):
        falha = resultado_leitura(
            StatusLeitura.NAO_AUTORIZADO,
            repositorio.ARQ_INTERACOES,
            pd.DataFrame(columns=repositorio.COLUNAS_INTERACOES),
        )

        self.assertFalse(
            repositorio.cadastro_interacao_liberado(
                self.resultado_clientes,
                falha,
                self.snapshot,
            )
        )

    def test_bloqueia_quando_snapshot_comum_nao_esta_disponivel(self):
        falha_snapshot = self.resultado_publicacao(
            StatusPersistenciaMultiArquivo.FALHA_TEMPORARIA
        )

        self.assertFalse(
            repositorio.cadastro_interacao_liberado(
                self.resultado_clientes,
                self.resultado_interacoes,
                falha_snapshot,
            )
        )

    @patch.object(repositorio, "publicar_csvs_em_commit")
    @patch.object(repositorio, "agora_iso", side_effect=["created", "updated"])
    @patch.object(repositorio, "gerar_id", return_value="interacao-nova")
    def test_cria_interacao_e_atualiza_somente_cliente_selecionado(
        self,
        gerar_id,
        agora_iso,
        publicar,
    ):
        publicar.return_value = self.resultado_publicacao(
            StatusPersistenciaMultiArquivo.SUCESSO
        )

        resultado = repositorio.cadastrar_interacao_composta(
            self.dados,
            self.resultado_clientes,
            self.resultado_interacoes,
            self.snapshot,
        )

        self.assertTrue(resultado.sucesso)
        gerar_id.assert_called_once()
        self.assertEqual(agora_iso.call_count, 2)
        alteracoes, token, repo, branch, mensagem = publicar.call_args.args
        self.assertEqual(token, "token-teste")
        self.assertEqual(repo, "repo-teste")
        self.assertEqual(branch, "main")
        self.assertEqual(mensagem, "Registrar interação CRM e atualizar cliente")
        self.assertEqual(
            [alteracao.arquivo for alteracao in alteracoes],
            [repositorio.ARQ_INTERACOES, repositorio.ARQ_CLIENTES],
        )

        interacoes_novas = alteracoes[0].dados
        clientes_novos = alteracoes[1].dados
        self.assertListEqual(
            interacoes_novas["id_interacao"].tolist(),
            ["interacao-existente", "interacao-nova"],
        )
        nova_interacao = interacoes_novas.iloc[1]
        self.assertEqual(nova_interacao["id_cliente"], "cliente-1")
        self.assertEqual(nova_interacao["id_contato"], "contato-1")
        self.assertEqual(nova_interacao["descricao"], "Nova interação")
        self.assertEqual(nova_interacao["created_at"], "created")

        cliente_selecionado = clientes_novos[clientes_novos["id_cliente"] == "cliente-1"].iloc[0]
        self.assertEqual(cliente_selecionado["ultimo_contato"], "2026-07-13")
        self.assertEqual(cliente_selecionado["proxima_acao"], "Enviar proposta")
        self.assertEqual(cliente_selecionado["data_proxima_acao"], "2026-07-20")
        self.assertEqual(cliente_selecionado["responsavel"], "Novo responsável")
        self.assertEqual(cliente_selecionado["updated_at"], "updated")

        cliente_preservado = clientes_novos[clientes_novos["id_cliente"] == "cliente-2"].iloc[0]
        self.assertEqual(cliente_preservado["responsavel"], "Outro responsável")
        self.assertEqual(cliente_preservado["ultimo_contato"], "2026-02-01")
        self.assertEqual(cliente_preservado["proxima_acao"], "Outra ação")

    @patch.object(repositorio, "publicar_csvs_em_commit")
    def test_cliente_ausente_no_snapshot_bloqueia_sem_publicar(self, publicar):
        dados = {**self.dados, "id_cliente": "cliente-ausente"}

        resultado = repositorio.cadastrar_interacao_composta(
            dados,
            self.resultado_clientes,
            self.resultado_interacoes,
            self.snapshot,
        )

        self.assertEqual(resultado.status, StatusPersistenciaMultiArquivo.REQUISICAO_INVALIDA)
        self.assertIn("não existe mais", resultado.erro)
        publicar.assert_not_called()

    def test_tela_so_apresenta_sucesso_e_rerun_apos_resultado_confirmado(self):
        fonte = ETAPA_INTERACOES.read_text()

        self.assertIn("if resultado.sucesso:", fonte)
        self.assertIn('st.success("Interação registrada com sucesso.")', fonte)
        self.assertIn("st.rerun()", fonte)
        self.assertIn("else:", fonte)

    def test_conflito_e_falha_temporaria_nao_produzem_falso_sucesso(self):
        fonte = ETAPA_INTERACOES.read_text()

        self.assertNotIn("cadastrar_interacao(dados)", fonte)
        self.assertIn("st.error(detalhes)", fonte)
        self.assertIn("cadastrar_interacao_composta(", fonte)

    def test_demais_operacoes_do_crm_permanecem_disponiveis(self):
        fonte = Path("pages/crm/repositorio.py").read_text()

        self.assertIn("def cadastrar_cliente(", fonte)
        self.assertIn("def atualizar_cliente(", fonte)
        self.assertIn("def cadastrar_contato(", fonte)
        self.assertIn("def atualizar_contato(", fonte)


if __name__ == "__main__":
    unittest.main()
