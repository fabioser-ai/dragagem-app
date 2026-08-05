import unittest
from unittest.mock import Mock, patch

import pandas as pd

from services import autorizacao, permissoes
from modulos.orcamentos.persistencia.contratos import StatusPersistencia
from modulos.orcamentos.persistencia.github_repositorio import RepositorioOrcamentosGitHub
from pages.crm import repositorio as crm_repositorio
from tests.test_dados_crud_seguro import dados, leitura
from services.github import StatusLeitura


class SessionState(dict):
    def __getattr__(self, nome):
        return self[nome]

    def __setattr__(self, nome, valor):
        self[nome] = valor


class TestAutoridadeUnicaAC002(unittest.TestCase):
    def setUp(self):
        if not hasattr(autorizacao.st, "session_state"):
            autorizacao.st.session_state = SessionState()
        autorizacao.st.session_state.clear()

    def autenticar(self, perfil="user", usuario="usuario"):
        autorizacao.st.session_state.update(
            autenticado=True, perfil=perfil, usuario=usuario, tela="menu"
        )

    def test_sem_login_todas_as_acoes_sao_negadas(self):
        for acao in ("criar", "editar", "excluir", "aprovar"):
            with self.subTest(acao=acao):
                self.assertFalse(
                    autorizacao.pode(modulo="dados", recurso="cadastros", acao=acao)
                )

    def test_sem_permissao_nao_cria_edita_exclui_nem_aprova(self):
        self.autenticar()
        with patch.object(autorizacao, "pode_executar", return_value=False):
            for acao in ("criar", "editar", "excluir", "aprovar"):
                with self.subTest(acao=acao):
                    self.assertFalse(
                        autorizacao.pode(
                            modulo="ferias", recurso="registros", acao=acao
                        )
                    )

    def test_usuario_autorizado_executa_acao(self):
        self.autenticar()
        with patch.object(autorizacao, "pode_executar", return_value=True) as decidir:
            self.assertTrue(
                autorizacao.pode(
                    modulo="crm", recurso="clientes", acao="editar"
                )
            )
        decidir.assert_called_once_with(
            "crm", recurso="clientes", permissao="editar", obra_id="todas"
        )

    def test_superadmin_executa_acoes_globais(self):
        self.autenticar(perfil="superadmin")
        self.assertTrue(autorizacao.usuario_superadmin())
        with patch.object(autorizacao, "pode_executar", return_value=True):
            self.assertTrue(
                autorizacao.pode(
                    modulo="administracao", recurso="permissoes", acao="editar"
                )
            )

    def test_admin_nao_recebe_privilegio_de_superadmin(self):
        self.autenticar(perfil="admin")
        self.assertTrue(autorizacao.possui_privilegio_administrativo())
        self.assertFalse(autorizacao.usuario_superadmin())

    def test_falha_de_leitura_resulta_em_negacao(self):
        self.autenticar()
        permissoes.st.secrets = {"GITHUB_TOKEN": "x", "REPO": "org/repo"}
        with patch.object(permissoes, "carregar_github", side_effect=RuntimeError("falha")):
            self.assertFalse(
                autorizacao.pode(
                    modulo="dados", recurso="cadastros", acao="editar"
                )
            )

    def test_permissao_por_obra_e_respeitada(self):
        self.autenticar()
        concessoes = pd.DataFrame(
            [{
                "usuario": "usuario", "modulo": "obras", "recurso": "documentos",
                "permissao": "editar", "obra_id": "obra-1", "ativo": "sim",
            }]
        )
        with patch.object(permissoes, "permissoes_usuario", return_value=concessoes):
            self.assertTrue(
                autorizacao.pode_operar_obra(
                    modulo="obras", recurso="documentos", acao="editar", obra_id="obra-1"
                )
            )
            self.assertFalse(
                autorizacao.pode_operar_obra(
                    modulo="obras", recurso="documentos", acao="editar", obra_id="obra-2"
                )
            )

    def test_controle_visual_nao_substitui_guarda_de_persistencia(self):
        dados.st.error = Mock()
        with patch.object(dados, "pode", return_value=False), patch.object(
            dados, "salvar_cadastro_seguro"
        ) as gravar:
            resultado = dados._salvar_cadastro(
                pd.DataFrame(), "data/teste.csv", ["x"],
                leitura(StatusLeitura.SUCESSO_COM_DADOS), "ok", "erro", acao="criar"
            )
        self.assertIsNone(resultado)
        gravar.assert_not_called()

    def test_chamada_direta_do_crm_negada_sem_gravacao_remota(self):
        crm_repositorio.st.error = Mock()
        with patch.object(crm_repositorio, "pode", return_value=False), patch.object(
            crm_repositorio, "salvar_github"
        ) as gravar:
            self.assertFalse(
                crm_repositorio.salvar_csv_github(
                    pd.DataFrame(), "data/crm/x.csv", [], acao="excluir"
                )
            )
        gravar.assert_not_called()

    def test_chamada_direta_do_novo_orcamento_e_negada(self):
        repositorio = RepositorioOrcamentosGitHub("token", "org/repo")
        with patch(
            "modulos.orcamentos.persistencia.github_repositorio.pode",
            return_value=False,
        ), patch(
            "modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit"
        ) as gravar:
            resultado = repositorio.persistir_versao(None, None, "", "snapshot")
        self.assertEqual(resultado.status, StatusPersistencia.REQUISICAO_INVALIDA)
        gravar.assert_not_called()



if __name__ == "__main__":
    unittest.main()
