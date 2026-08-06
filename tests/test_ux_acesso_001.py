import hashlib
import unittest
from pathlib import Path

from pages import administracao


ROOT = Path(__file__).resolve().parents[1]
PAGINA = ROOT / "pages/administracao.py"


class TestUXAcesso001(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fonte = PAGINA.read_text(encoding="utf-8")

    def test_protecao_administrativa_e_autoridades_nao_mudaram(self):
        trecho = self.fonte[self.fonte.index("def render():"):]
        self.assertIn("if not pode_gerenciar_administracao():", trecho)
        self.assertIn("st.stop()", trecho)
        self.assertNotIn('perfil == "admin"', self.fonte)
        self.assertNotIn('perfil == "superadmin"', self.fonte)

    def test_navegacao_prioriza_usuario_e_separa_areas(self):
        self.assertIn('"USUÁRIOS", "ROLES", "PERMISSÕES", "DIAGNÓSTICO", "AVANÇADO"', self.fonte)
        render = self.fonte[self.fonte.index("def render():"):]
        self.assertLess(render.index("_render_usuarios()"), render.index("_render_roles()"))
        self.assertIn("def _render_permissoes_legadas", self.fonte)

    def test_ficha_consolidada_reune_identidade_estado_roles_acesso_e_auditoria(self):
        for secao in (
            "### Identidade", "### Estado", "### Funções atribuídas ao usuário",
            "### Acesso e diagnóstico", "### Auditoria",
        ):
            self.assertIn(secao, self.fonte)
        for campo in (
            "Nome", "Login", "Matrícula", "E-mail cadastral", "Perfil-base",
            "usuario_id", "criado_em", "criado_por", "atualizado_em", "atualizado_por",
        ):
            self.assertIn(campo, self.fonte)

    def test_mensagens_nao_prometem_credencial_convite_ou_autenticacao(self):
        for mensagem in (
            "O e-mail é apenas cadastral",
            "Nenhum convite será enviado",
            "senha será gerada",
            "ainda não pode entrar no APP",
            "não criam credencial",
            "Nenhum e-mail foi enviado",
        ):
            self.assertIn(mensagem, self.fonte)
        for proibido in ("enviar_email", "smtp", "criar_credencial", "gerar_senha"):
            self.assertNotIn(proibido, self.fonte.casefold())

    def test_roles_permanecem_documentais_e_historico_e_preservado(self):
        self.assertIn("Uma função atribuída ainda não altera o acesso real", self.fonte)
        self.assertIn("Retirada — histórico preservado", self.fonte)
        self.assertIn("Esta função está vazia", self.fonte)
        self.assertIn("atribuir_role(", self.fonte)
        self.assertIn("retirar_role(", self.fonte)
        self.assertIn("usuario_id=usuario_id", self.fonte)
        self.assertIn("role_id=role_id", self.fonte)

    def test_shadow_distingue_acesso_atual_e_calculado_em_linguagem_clara(self):
        self.assertIn("O cálculo por Roles está em modo de diagnóstico", self.fonte)
        self.assertIn("Acesso efetivo atual", self.fonte)
        self.assertIn("Acesso calculado pelas funções", self.fonte)
        self.assertIn("O acesso por Roles concederia", self.fonte)
        self.assertIn("O acesso atual possui, mas as Roles não concedem", self.fonte)
        self.assertEqual(
            administracao._status_diagnostico("DIVERGENTE"),
            "Há diferenças entre o acesso atual e o calculado pelas Roles",
        )
        self.assertEqual(
            administracao._rotulo_chave("prestacao_contas / despesa / criar"),
            "Prestação de Contas — Despesa: Criar",
        )

    def test_falha_de_leitura_bloqueia_ficha_e_acoes(self):
        self.assertIn("Leitura bloqueada", self.fonte)
        self.assertIn("all(item.leitura_confirmada", self.fonte)
        self.assertIn("disabled=not leitura.pode_sobrescrever", self.fonte)
        self.assertIn("disabled=not confirmar", self.fonte)

    def test_autenticacao_dados_rbac_e_medicoes_permanecem_inalterados(self):
        esperados = {
            "services/auth.py": "b8f864ed3c9a892f53280e28ee56b78f5c979cee62d253923f88b55b477caec0",
            "services/autorizacao.py": "3062e25a6d1a6afce9ee0d1a3cc9832a0edc111f3e1378cc4de29bbf23e59b66",
            "data/permissoes_usuarios.csv": "23b33a97d78c41f217e7bcdae397e5fcb555f72c344974adb3b1550cad2dca5e",
            "data/roles_permissoes.csv": "8ad445f518c3c72900aa32b7385c0d8350630af408dcded9218e8ad8813cdc7a",
            "pages/medicoes.py": "f23a8cf9d1c7e01f94a93447c1f924dbc2dfd80b1bb904a1a9ff3e64e496257f",
            "modulos/medicoes/permissoes.py": "a72195e98268a7b76f220a6b0873816e1d46363cd015c5fe673e02f175ea7643",
        }
        for caminho, esperado in esperados.items():
            atual = hashlib.sha256((ROOT / caminho).read_bytes()).hexdigest()
            self.assertEqual(atual, esperado, caminho)
        self.assertNotIn("SYSTEM_OWNER_ID", self.fonte)

    def test_bases_operacionais_so_sao_referenciadas_pelos_servicos_existentes(self):
        usuarios = (ROOT / "data/usuarios_operacionais.csv").read_bytes()
        associacoes = (ROOT / "data/usuarios_roles.csv").read_bytes()
        administracao._linhas_permissoes(("dados / atestado / visualizar",))
        self.assertEqual((ROOT / "data/usuarios_operacionais.csv").read_bytes(), usuarios)
        self.assertEqual((ROOT / "data/usuarios_roles.csv").read_bytes(), associacoes)
        self.assertNotIn("salvar_csv_github", self.fonte)

    def test_documentacao_registra_limites_e_homologacao(self):
        documento = (ROOT / "docs/UX_ACESSO_001.md").read_text(encoding="utf-8")
        self.assertIn("não cria credenciais nem altera acesso efetivo", documento)
        self.assertIn("continua sem capacidade de login", documento)
        self.assertIn("Roteiro de homologação visual", documento)
        self.assertIn("Pendências para AUTH-002", documento)


if __name__ == "__main__":
    unittest.main()
