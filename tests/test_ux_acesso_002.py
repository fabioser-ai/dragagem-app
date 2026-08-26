import hashlib
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pandas as pd

from pages import administracao
from services import log as log_service
from services.github import StatusLeitura


ROOT = Path(__file__).resolve().parents[1]
PAGINA = ROOT / "pages/administracao.py"


class TestUXAcesso002(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fonte = PAGINA.read_text(encoding="utf-8")

    def trecho(self, inicio, fim):
        return self.fonte[self.fonte.index(inicio):self.fonte.index(fim)]

    def test_entrada_principal_apresenta_cinco_areas_orientadas_a_tarefas(self):
        self.assertEqual(
            administracao.AREAS_ADMINISTRACAO,
            (
                ("Pessoas", "Cadastrar e administrar usuários"),
                ("Acessos", "Controlar o que cada pessoa pode fazer hoje"),
                ("Roles", "Administrar funções institucionais"),
                ("Diagnóstico", "Comparar o acesso atual com o modelo por Roles"),
                ("Auditoria", "Consultar histórico e eventos"),
            ),
        )
        self.assertIn("O que você deseja fazer?", self.fonte)
        self.assertNotIn("st.tabs(", self.trecho("def render():", "if __name__") if "if __name__" in self.fonte else self.fonte[self.fonte.index("def render():"):])

    def test_navegacao_abre_area_e_oferece_retorno_simples(self):
        self.assertIn("st.session_state[AREA_ADMINISTRACAO] = nome", self.fonte)
        self.assertIn("st.session_state[AREA_ADMINISTRACAO] = None", self.fonte)
        self.assertIn("← Voltar para Administração", self.fonte)
        render = self.fonte[self.fonte.index("def render():"):]
        for chamada in (
            "_render_usuarios()", "_render_area_acessos()", "_render_area_roles()",
            "_render_area_diagnostico()", "_render_area_auditoria()",
        ):
            self.assertIn(chamada, render)

    def test_pessoas_preserva_cadastro_edicao_estado_e_credencial_sem_rbac(self):
        trecho = self.trecho("def _render_usuarios():", "def _render_diagnostico_rbac():")
        for chamada in (
            "_render_criacao_usuario", "_render_identidade_usuario",
            "_render_resumo_usuario", "_render_estado_usuario",
        ):
            self.assertIn(chamada, trecho)
        for chamada in (
            "_render_roles_usuario", "_render_acesso_usuario",
            "_render_auditoria_usuario", "calcular_usuario(",
        ):
            self.assertNotIn(chamada, trecho)
        for acao in (
            "Criar usuário inativo", "Salvar dados", "Ativar usuário",
            "Inativar usuário", "Configurar ou redefinir credencial",
        ):
            self.assertIn(acao, self.fonte)
        self.assertIn("diagnosticar_credencial(usuario, leituras[\"credenciais\"])", self.fonte)

    def test_acessos_exibe_e_mantem_somente_autoridade_real(self):
        trecho = self.trecho("def _render_area_acessos():", "def _render_associacoes_roles():")
        self.assertIn("rbac_authority.listar_permissoes(usuario=login)", trecho)
        self.assertIn("ACESSO REAL ATUAL", self.fonte)
        self.assertIn("carregar_permissoes_resultado()", self.fonte)
        self.assertIn("salvar_permissoes_seguro", self.fonte)
        self.assertIn("Habilitar alterações nas permissões efetivas atuais", self.fonte)

    def test_resumo_de_modulos_reflete_regras_efetivas_e_fail_closed(self):
        regras = pd.DataFrame([
            {"usuario": "teste", "modulo": "crm", "ativo": "sim"},
            {"usuario": "teste", "modulo": "dados", "ativo": "nao"},
        ])
        permitidos, negados = administracao._resumo_modulos_acesso(regras, "TESTE")
        self.assertEqual(permitidos, ("crm",))
        self.assertIn("dados", negados)
        permitidos, negados = administracao._resumo_modulos_acesso(
            pd.DataFrame(columns=("usuario", "modulo", "ativo")), "sem-regra"
        )
        self.assertEqual(permitidos, ())
        self.assertTrue(negados)

    def test_roles_preserva_catalogo_associacao_e_aviso_shadow(self):
        trecho = self.trecho("def _render_area_roles():", "def _render_diagnostico_individual():")
        self.assertIn("Função de uma pessoa", trecho)
        self.assertIn("Catálogo de Roles", trecho)
        self.assertIn("_render_associacoes_roles()", trecho)
        self.assertIn("_render_roles()", trecho)
        self.assertIn("Roles ativas controlam o acesso real", trecho)
        self.assertIn("atribuir_role(", self.fonte)
        self.assertIn("retirar_role(", self.fonte)

    def test_shadow_catalogo_e_detalhes_tecnicos_ficam_no_diagnostico(self):
        trecho = self.trecho("def _render_area_diagnostico():", "def _render_area_auditoria():")
        self.assertIn("_render_diagnostico_rbac()", trecho)
        self.assertIn("_render_diagnostico_individual()", trecho)
        self.assertIn("_render_catalogo_permissoes()", trecho)
        self.assertIn("Compara o RBAC em uso", self.fonte)

    def test_auditoria_preserva_historico_existente_sem_criar_novo_sistema(self):
        trecho = self.trecho("def _render_area_auditoria():", "def render():")
        self.assertIn("_render_auditoria_usuario", trecho)
        self.assertIn("Nenhum novo sistema", trecho)
        self.assertIn("de auditoria foi criado", trecho)
        self.assertIn("Histórico técnico das funções", self.fonte)
        self.assertIn("carregar_logs_resultado()", trecho)
        self.assertIn("Eventos de acesso", trecho)

    def test_leitura_de_eventos_existentes_e_somente_consulta(self):
        origem = SimpleNamespace(
            leitura_confirmada=True,
            dados=pd.DataFrame([{
                "data_hora": "2026-08-25 10:00:00", "usuario": "teste",
                "perfil": "funcionario", "acao": "login",
            }]),
            status=StatusLeitura.SUCESSO_COM_DADOS,
            arquivo=log_service.ARQUIVO_LOG,
            http_status=200,
            sha="abc",
            erro=None,
        )
        with patch.object(log_service, "ler_csv_github", return_value=origem), patch.object(
            log_service.st, "secrets", {"GITHUB_TOKEN": "x", "REPO": "org/repo"}
        ):
            resultado = log_service.carregar_logs_resultado()
        self.assertTrue(resultado.leitura_confirmada)
        self.assertEqual(resultado.dados.iloc[0]["acao"], "login")

    def test_falha_na_leitura_de_eventos_nao_inventa_historico(self):
        origem = SimpleNamespace(
            leitura_confirmada=False,
            dados=pd.DataFrame(),
            status=StatusLeitura.FALHA_TEMPORARIA,
            arquivo=log_service.ARQUIVO_LOG,
            http_status=500,
            sha=None,
            erro="falha",
        )
        with patch.object(log_service, "ler_csv_github", return_value=origem), patch.object(
            log_service.st, "secrets", {"GITHUB_TOKEN": "x", "REPO": "org/repo"}
        ):
            resultado = log_service.carregar_logs_resultado()
        self.assertFalse(resultado.leitura_confirmada)
        self.assertTrue(resultado.dados.empty)

    def test_auth_app_users_autorizacao_e_shadow_permanecem_intactos(self):
        esperados = {
            "services/auth.py": "f1d69b8e69d24c829b31558ebbdfa0fe21ebe909aca7aee2fbcabeab22c843bf",
            "services/rbac_shadow.py": "a023e1dec34178b56733e2eb279216f6ddf3612b189b3d2739ce0751b15356b1",
            "data/permissoes_usuarios.csv": "23b33a97d78c41f217e7bcdae397e5fcb555f72c344974adb3b1550cad2dca5e",
        }
        for caminho, esperado in esperados.items():
            self.assertEqual(hashlib.sha256((ROOT / caminho).read_bytes()).hexdigest(), esperado)
        self.assertNotIn("APP_USERS =", self.fonte)


if __name__ == "__main__":
    unittest.main()
