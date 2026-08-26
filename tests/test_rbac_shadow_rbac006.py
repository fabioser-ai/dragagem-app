import hashlib
from pathlib import Path
import unittest

import pandas as pd

from services.rbac_shadow import calcular_usuario, diagnosticar_usuarios


ROOT = Path(__file__).resolve().parents[1]


def df(linhas, colunas):
    return pd.DataFrame(linhas, columns=colunas)


USUARIO = {"usuario_id": "u1", "login": "joao", "nome": "João"}
ASSOCIACOES = [
    {"usuario_id": "u1", "role_id": "r1", "ativo": "sim"},
]
ROLES = [
    {"role_id": "r1", "codigo": "FUNCIONARIO", "ativo": "sim"},
    {"role_id": "r2", "codigo": "FINANCEIRO", "ativo": "sim"},
]
MATRIZ = [
    {"role_id": "r1", "modulo": "prestacao_contas", "recurso": "despesa", "acao": "criar", "efeito": "allow"},
]
CATALOGO = [
    {"modulo": "prestacao_contas", "recurso": "despesa", "acao": "criar", "ativo": "sim"},
    {"modulo": "prestacao_contas", "recurso": "pagamento", "acao": "editar", "ativo": "sim"},
]
ATUAIS = [
    {"usuario": "joao", "modulo": "prestacao_contas", "recurso": "despesa", "permissao": "criar", "obra_id": "todas", "ativo": "sim"},
]


class TestShadowModeRBAC006(unittest.TestCase):
    def calcular(self, **trocas):
        dados = {
            "usuario": USUARIO,
            "associacoes": ASSOCIACOES,
            "roles": ROLES,
            "roles_permissoes": MATRIZ,
            "catalogo_permissoes": CATALOGO,
            "permissoes_atuais": ATUAIS,
        }
        dados.update(trocas)
        return calcular_usuario(**dados)

    def test_comparacao_igual(self):
        resultado = self.calcular()
        self.assertEqual(resultado.status, "IGUAL")
        self.assertFalse(resultado.ocorrencias)

    def test_usuario_sem_role(self):
        resultado = self.calcular(associacoes=[])
        self.assertEqual(resultado.status, "SEM ROLE")
        self.assertIn("Usuário sem Role", resultado.ocorrencias)

    def test_role_vazia(self):
        resultado = self.calcular(roles_permissoes=[], permissoes_atuais=[])
        self.assertEqual(resultado.status, "ROLE VAZIA")
        self.assertIn("Role vazia: FUNCIONARIO", resultado.ocorrencias)

    def test_multiplas_roles_e_permissoes_duplicadas_sao_deduplicadas(self):
        associacoes = ASSOCIACOES + [{"usuario_id": "u1", "role_id": "r2", "ativo": "sim"}]
        matriz = MATRIZ + [
            {**MATRIZ[0], "role_id": "r2"},
            {"role_id": "r2", "modulo": "prestacao_contas", "recurso": "pagamento", "acao": "editar", "efeito": "allow"},
        ]
        atuais = ATUAIS + [
            {"usuario": "joao", "modulo": "prestacao_contas", "recurso": "pagamento", "permissao": "editar", "obra_id": "todas", "ativo": "sim"},
        ]
        resultado = self.calcular(
            associacoes=associacoes, roles_permissoes=matriz,
            permissoes_atuais=atuais,
        )
        self.assertEqual(resultado.status, "IGUAL")
        self.assertEqual(len(resultado.permissoes_rbac), 2)
        self.assertEqual(resultado.roles, ("FINANCEIRO", "FUNCIONARIO"))

    def test_permissao_inexistente_e_role_inexistente(self):
        matriz = MATRIZ + [
            {"role_id": "r1", "modulo": "fantasma", "recurso": "x", "acao": "criar", "efeito": "allow"},
        ]
        associacoes = ASSOCIACOES + [{"usuario_id": "u1", "role_id": "ausente", "ativo": "sim"}]
        resultado = self.calcular(associacoes=associacoes, roles_permissoes=matriz)
        self.assertEqual(resultado.status, "DIVERGENTE")
        self.assertTrue(any(item.startswith("Permissão inexistente") for item in resultado.ocorrencias))
        self.assertTrue(any(item.startswith("Role inexistente") for item in resultado.ocorrencias))

    def test_rbac_concede_mais(self):
        resultado = self.calcular(permissoes_atuais=[])
        self.assertEqual(resultado.status, "DIVERGENTE")
        self.assertEqual(len(resultado.rbac_a_mais), 1)
        self.assertIn("RBAC possui permissões a mais", resultado.ocorrencias)

    def test_rbac_concede_menos(self):
        atuais = ATUAIS + [
            {"usuario": "joao", "modulo": "prestacao_contas", "recurso": "pagamento", "permissao": "editar", "obra_id": "todas", "ativo": "sim"},
        ]
        resultado = self.calcular(permissoes_atuais=atuais)
        self.assertEqual(resultado.status, "DIVERGENTE")
        self.assertEqual(len(resultado.rbac_a_menos), 1)
        self.assertIn("RBAC possui permissões a menos", resultado.ocorrencias)

    def test_diagnostica_todos_sem_estado_global(self):
        usuarios = pd.DataFrame([USUARIO, {"usuario_id": "u2", "login": "maria", "nome": "Maria"}])
        resultados = diagnosticar_usuarios(
            usuarios=usuarios, associacoes=ASSOCIACOES, roles=ROLES,
            roles_permissoes=MATRIZ, catalogo_permissoes=CATALOGO,
            permissoes_atuais=ATUAIS,
        )
        self.assertEqual([item.status for item in resultados], ["IGUAL", "SEM ROLE"])

    def test_servico_nao_importa_streamlit_persistencia_ou_autorizacao(self):
        fonte = (ROOT / "services/rbac_shadow.py").read_text(encoding="utf-8")
        for proibido in ("streamlit", "session_state", "salvar_", "pode_", "services.autorizacao"):
            self.assertNotIn(proibido, fonte)

    def test_login_rotas_e_fontes_efetivas_nao_importam_shadow(self):
        for caminho in (
            "app.py", "services/auth.py", "services/autorizacao.py",
            "services/permissoes.py", "pages/medicoes.py",
        ):
            self.assertNotIn(
                "rbac_shadow", (ROOT / caminho).read_text(encoding="utf-8"), caminho,
            )

    def test_bases_efetivas_e_rbac005_permanecem_inalteradas(self):
        caminho_usuarios = ROOT / "data/usuarios_operacionais.csv"
        caminho_associacoes = ROOT / "data/usuarios_roles.csv"
        usuarios_antes = caminho_usuarios.read_bytes()
        associacoes_antes = caminho_associacoes.read_bytes()
        usuarios = pd.read_csv(caminho_usuarios, dtype=str).fillna("")
        associacoes = pd.read_csv(caminho_associacoes, dtype=str).fillna("")
        self.assertEqual(
            usuarios.columns.tolist(),
            [
                "usuario_id", "login", "nome", "matricula", "email",
                "perfil_base", "ativo", "criado_em", "criado_por",
                "atualizado_em", "atualizado_por", "exige_troca_senha",
                "credencial_configurada",
            ],
        )
        self.assertEqual(
            associacoes.columns.tolist(),
            [
                "usuario_role_id", "usuario_id", "role_id", "obra_id", "ativo",
                "criado_em", "criado_por", "atualizado_em", "atualizado_por",
            ],
        )
        self.calcular()
        self.assertEqual(caminho_usuarios.read_bytes(), usuarios_antes)
        self.assertEqual(caminho_associacoes.read_bytes(), associacoes_antes)

        esperados = {
            "data/permissoes_usuarios.csv": "23b33a97d78c41f217e7bcdae397e5fcb555f72c344974adb3b1550cad2dca5e",
            "data/roles.csv": "3879bc730c293b1eedda6b1baf12b945fef5789187e6f80d2e941fcd75780002",
            "data/roles_permissoes.csv": "8ad445f518c3c72900aa32b7385c0d8350630af408dcded9218e8ad8813cdc7a",
        }
        for caminho, esperado in esperados.items():
            atual = hashlib.sha256((ROOT / caminho).read_bytes()).hexdigest()
            self.assertEqual(atual, esperado, caminho)

    def test_interface_e_documentacao_explicitam_modo_sombra(self):
        interface = (ROOT / "pages/administracao.py").read_text(encoding="utf-8")
        docs = (ROOT / "docs/RBAC006_SHADOW_MODE.md").read_text(encoding="utf-8")
        self.assertIn('st.subheader("DIAGNÓSTICO RBAC")', interface)
        self.assertNotIn(
            "st.form",
            interface[
                interface.index("def _render_diagnostico_rbac"):
                interface.index("def _render_permissoes_legadas")
            ],
        )
        self.assertIn(
            "O Shadow Mode calcula permissões, mas não participa da autorização do APP.",
            docs,
        )


if __name__ == "__main__":
    unittest.main()
