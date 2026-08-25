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
        for area in ("Pessoas", "Acessos", "Roles", "Diagnóstico", "Auditoria"):
            self.assertIn(f'("{area}",', self.fonte)
        render = self.fonte[self.fonte.index("def render():"):]
        self.assertIn("_render_inicio_administracao()", render)
        self.assertIn("_render_area_acessos()", render)
        self.assertIn("def _render_permissoes_legadas", self.fonte)

    def test_cabecalho_retorna_pelo_fluxo_atual_e_oferece_documentacao(self):
        trecho = self.fonte[self.fonte.index("def render():"):]
        self.assertIn("← Voltar ao menu inicial", trecho)
        self.assertIn('st.session_state.tela = "menu"', trecho)
        self.assertIn("st.rerun()", trecho)
        self.assertIn('st.title("Administração")', trecho)
        self.assertIn("Gerencie pessoas, acessos, funções e histórico em um só lugar.", trecho)
        self.assertIn('st.expander("Mais informações")', self.fonte)

    def test_documentacao_interna_cobre_finalidade_fluxo_limites_e_glossario(self):
        for texto in (
            "Use este módulo para cadastrar pessoas",
            "Fluxo recomendado",
            "O que ainda não está disponível",
            "Glossário",
            "Cadastro:",
            "Credencial:",
            "Role:",
            "Permissão:",
            "Shadow Mode:",
        ):
            self.assertIn(texto, self.fonte)

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

    def test_mensagens_auth002_nao_prometem_convite_ou_recuperacao(self):
        for mensagem in (
            "O e-mail é apenas cadastral",
            "Nenhum convite será enviado",
            "senha será gerada",
            "Configurar ou redefinir credencial",
            "hash bcrypt",
            "Nenhum e-mail foi enviado",
        ):
            self.assertIn(mensagem, self.fonte)
        for proibido in ("enviar_email", "smtp", "gerar_senha", "recuperar_senha"):
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
        self.assertIn("Permissões atuais — em uso hoje", self.fonte)
        self.assertIn("Permissões pelas Roles — em preparação", self.fonte)
        self.assertIn("O novo modelo concederia", self.fonte)
        self.assertIn("O acesso atual possui, mas as Roles não concedem", self.fonte)
        self.assertEqual(
            administracao._status_diagnostico("DIVERGENTE"),
            "Há diferenças entre o acesso atual e o calculado pelas Roles",
        )
        self.assertEqual(
            administracao._rotulo_chave("prestacao_contas / despesa / criar"),
            "Prestação de Contas — Despesa: Criar",
        )

    def test_ajuda_geral_explica_os_dois_modelos_e_credenciais(self):
        for texto in (
            "Como funciona o controle de acesso?",
            "Hoje, o acesso real ainda é definido pelo modelo atual",
            "APP_USERS",
            "Usuários operacionais",
            "Roles",
            "Permissões efetivas atuais",
            "Permissões pelas Roles",
            "Diagnóstico (Shadow Mode)",
            "a senha original não pode ser recuperada",
        ):
            self.assertIn(texto, self.fonte)

    def test_modelo_atual_e_novo_rbac_sao_separados_visualmente(self):
        self.assertIn("ACESSO EM USO HOJE", self.fonte)
        self.assertIn("NOVO MODELO POR ROLES — EM PREPARAÇÃO", self.fonte)
        self.assertIn("ACESSO REAL ATUAL", self.fonte)
        self.assertIn("As Roles ainda não alteram o acesso real", self.fonte)
        self.assertIn("Habilitar alterações nas permissões efetivas atuais", self.fonte)
        self.assertIn("Modo consulta", self.fonte)

    def test_resumo_nao_confunde_cadastro_role_e_entrada(self):
        for rotulo in ('"Cadastro"', '"Entrada no APP"', '"Credencial"'):
            self.assertIn(rotulo, self.fonte)
        self.assertIn("Cadastro ativo e credencial configurada permitem autenticar", self.fonte)
        self.assertIn("Uma função atribuída ainda não altera o acesso real", self.fonte)
        self.assertIn("Entenda estes estados", self.fonte)
        self.assertIn("A credencial observável está indisponível ou inconsistente", self.fonte)
        self.assertIn("O novo modelo concederia", self.fonte)

    def test_ficha_tem_navegacao_interna_sem_duplicar_seletor(self):
        trecho = self.fonte[
            self.fonte.index("def _render_usuarios():"):
            self.fonte.index("def _render_diagnostico_rbac():")
        ]
        self.assertEqual(self.fonte.count('key="usuario_ficha"'), 1)
        self.assertNotIn("_render_roles_usuario", trecho)
        self.assertNotIn("_render_acesso_usuario", trecho)
        self.assertNotIn("_render_auditoria_usuario", trecho)

    def test_tabelas_obrigatorias_possuem_tooltips_por_coluna(self):
        self.assertIn("AJUDA_COLUNAS", self.fonte)
        self.assertIn("column_config=", self.fonte)
        for coluna in (
            "Usuário", "Login", "Perfil-base", "Cadastro", "Credencial",
            "Troca de senha", "Role / função", "Estado da Role",
            "Permissões atuais", "Permissões pelas Roles",
            "O novo modelo concederia",
            "O acesso atual possui, mas as Roles não concedem",
            "Status da comparação", "Criado por", "Atualizado por",
            "Criado em", "Atualizado em",
        ):
            self.assertIn(f'"{coluna}":', self.fonte)

    def test_consulta_e_padrao_e_edicao_exige_acao_explicita(self):
        self.assertIn("Habilitar alterações nas permissões efetivas atuais", self.fonte)
        self.assertIn("escrita_liberada = persistencia_liberada and edicao_habilitada", self.fonte)
        self.assertIn('with st.expander("Editar dados")', self.fonte)
        self.assertIn("Ativar usuário", self.fonte)
        self.assertIn("Inativar usuário", self.fonte)
        self.assertIn("Atribuir ou reativar função", self.fonte)
        self.assertIn("Retirar função", self.fonte)

    def test_campos_tecnicos_principais_possuem_explicacao(self):
        for explicacao in (
            "Identificador interno e imutável do cadastro. Não é o login.",
            "pode autenticar após ativação e configuração da credencial",
            "Classificação cadastral inicial. Não substitui as Roles",
            "Indica se o cadastro operacional está apto a autenticar",
            "Indica se existe credencial operacional bcrypt configurada",
            "campo reservado para o futuro ciclo de credenciais",
            "Permissões presentes nas Roles, mas ainda ausentes no acesso atual.",
            "Permissões em uso hoje que não aparecem nas Roles atribuídas.",
        ):
            self.assertIn(explicacao, self.fonte)

    def test_falha_de_leitura_bloqueia_ficha_e_acoes(self):
        self.assertIn("Leitura bloqueada", self.fonte)
        self.assertIn("all(item.leitura_confirmada", self.fonte)
        self.assertIn("disabled=not leitura.pode_sobrescrever", self.fonte)
        self.assertIn("disabled=not confirmar", self.fonte)

    def test_autenticacao_dados_rbac_e_medicoes_permanecem_inalterados(self):
        esperados = {
            "services/auth.py": "b7f39fb59dd3a9f31689a12f7b7718d5951ccb91f4ff96ad0a30ef5fd54bf06e",
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
