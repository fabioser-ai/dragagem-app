import hashlib
import unittest
from pathlib import Path

import pandas as pd

from services import roles


ROOT = Path(__file__).resolve().parents[1]


def carregar(caminho):
    return pd.read_csv(ROOT / caminho, dtype=str).fillna("")


class TestConcessaoInicialRolesRBAC004(unittest.TestCase):
    def setUp(self):
        self.catalogo_roles = carregar("data/roles.csv")
        self.catalogo_permissoes = carregar("data/permissoes_catalogo.csv")
        self.matriz = carregar("data/roles_permissoes.csv")

    def validar(self, matriz=None, catalogo_roles=None, catalogo_permissoes=None):
        return roles.validar_roles_permissoes(
            self.matriz if matriz is None else matriz,
            self.catalogo_roles if catalogo_roles is None else catalogo_roles,
            self.catalogo_permissoes if catalogo_permissoes is None else catalogo_permissoes,
        )

    def test_matriz_mutavel_permanece_valida_e_referencialmente_integra(self):
        self.assertEqual(self.validar(), [])
        self.assertEqual(self.matriz.columns.tolist(), roles.COLUNAS_PERMISSOES)
        self.assertTrue(set(self.matriz["role_id"]) <= set(self.catalogo_roles["role_id"]))
        self.assertTrue(set(self.matriz["efeito"]) <= set(roles.EFEITOS))
        chaves_catalogo = set(
            self.catalogo_permissoes[["modulo", "recurso", "acao"]].itertuples(
                index=False, name=None
            )
        )
        chaves_matriz = set(
            self.matriz[["modulo", "recurso", "acao"]].itertuples(index=False, name=None)
        )
        self.assertTrue(chaves_matriz <= chaves_catalogo)
        duplicadas = self.matriz.duplicated(
            subset=["role_id", "modulo", "recurso", "acao", "efeito"], keep=False
        )
        self.assertFalse(duplicadas.any())

    def test_funcionario_possui_somente_criar_despesa(self):
        role_id = self.catalogo_roles.loc[
            self.catalogo_roles["codigo"] == "FUNCIONARIO", "role_id"
        ].iloc[0]
        permissoes = self.matriz[self.matriz["role_id"] == role_id]
        self.assertEqual(
            permissoes[["modulo", "recurso", "acao", "efeito"]].values.tolist(),
            [["prestacao_contas", "despesa", "criar", "allow"]],
        )

    def test_matriz_nao_concede_administracao_ou_permissoes_criticas(self):
        self.assertNotIn("administracao", set(self.matriz["modulo"]))
        catalogo = self.catalogo_permissoes.copy()
        criticas = catalogo[
            catalogo["sensibilidade"].astype(str).str.strip().str.casefold() == "critica"
        ]
        chaves_criticas = set(
            criticas[["modulo", "recurso", "acao"]].itertuples(index=False, name=None)
        )
        chaves_matriz = set(
            self.matriz[["modulo", "recurso", "acao"]].itertuples(index=False, name=None)
        )
        self.assertTrue(chaves_matriz.isdisjoint(chaves_criticas))

    def test_roles_vazias_sao_validas(self):
        nova_role = pd.DataFrame([{
            "role_id": "role-vazia-teste",
            "codigo": "ROLE_VAZIA_TESTE",
            "nome": "Role vazia de teste",
            "descricao": "",
            "ativo": "sim",
            "versao": "1",
            "criado_em": "",
            "criado_por": "",
            "atualizado_em": "",
            "atualizado_por": "",
        }])
        catalogo = pd.concat([self.catalogo_roles, nova_role], ignore_index=True)
        self.assertEqual(self.validar(catalogo_roles=catalogo), [])
        self.assertNotIn("role-vazia-teste", set(self.matriz["role_id"]))

    def test_role_inexistente_e_negada(self):
        matriz = self.matriz.iloc[[0]].copy()
        matriz.loc[:, "role_id"] = "role-inexistente"
        self.assertIn("role_inexistente:0", self.validar(matriz=matriz))

    def test_permissao_inexistente_e_negada(self):
        matriz = self.matriz.iloc[[0]].copy()
        matriz.loc[:, ["modulo", "recurso", "acao"]] = ["dados", "nao_existe", "criar"]
        self.assertIn("permissao_inexistente:0", self.validar(matriz=matriz))

    def test_duplicidade_e_negada(self):
        matriz = pd.concat([self.matriz.iloc[[0]], self.matriz.iloc[[0]]], ignore_index=True)
        erros = self.validar(matriz=matriz)
        self.assertIn("duplicidade:0", erros)
        self.assertIn("duplicidade:1", erros)

    def test_combinacao_critica_e_administrativa_e_negada(self):
        matriz = self.matriz.iloc[[0]].copy()
        matriz.loc[:, ["modulo", "recurso", "acao"]] = [
            "administracao", "role", "editar"
        ]
        self.assertIn("permissao_critica_proibida:0", self.validar(matriz=matriz))

    def test_efeito_invalido_e_negado(self):
        matriz = self.matriz.iloc[[0]].copy()
        matriz.loc[:, "efeito"] = "talvez"
        self.assertIn("efeito_invalido:0", self.validar(matriz=matriz))

    def test_nenhuma_permissao_nova_foi_criada(self):
        chaves_catalogo = set(
            self.catalogo_permissoes[["modulo", "recurso", "acao"]].itertuples(
                index=False, name=None
            )
        )
        chaves_matriz = set(
            self.matriz[["modulo", "recurso", "acao"]].itertuples(index=False, name=None)
        )
        self.assertTrue(chaves_matriz <= chaves_catalogo)
        self.assertEqual(len(self.catalogo_permissoes), 61)

    def test_proprietario_superadmin_e_pessoas_permanecem_fora_do_rbac(self):
        codigos = set(self.catalogo_roles["codigo"])
        proibidos = {"SYSTEM_OWNER", "SUPERADMIN", "OWNER", "PROPRIETARIO", "FABIO"}
        self.assertTrue(codigos.isdisjoint(proibidos))
        colunas = set(self.matriz.columns)
        self.assertNotIn("usuario", colunas)
        self.assertNotIn("email", colunas)
        self.assertNotIn("system_owner_id", {c.casefold() for c in colunas})

    def test_autenticacao_usuarios_catalogo_e_permissoes_vigentes_inalterados(self):
        caminho_usuarios = ROOT / "data/usuarios_operacionais.csv"
        usuarios_antes = caminho_usuarios.read_bytes()
        usuarios = carregar("data/usuarios_operacionais.csv")
        self.assertEqual(
            usuarios.columns.tolist(),
            [
                "usuario_id", "login", "nome", "matricula", "email",
                "perfil_base", "ativo", "criado_em", "criado_por",
                "atualizado_em", "atualizado_por", "exige_troca_senha",
                "credencial_configurada",
            ],
        )
        self.assertEqual(self.validar(), [])
        self.assertEqual(caminho_usuarios.read_bytes(), usuarios_antes)

        esperados = {
            "services/auth.py": "b7f39fb59dd3a9f31689a12f7b7718d5951ccb91f4ff96ad0a30ef5fd54bf06e",
            "data/permissoes_usuarios.csv": "23b33a97d78c41f217e7bcdae397e5fcb555f72c344974adb3b1550cad2dca5e",
            "data/permissoes_catalogo.csv": "e2d3471e08dc7abfe13c9d46d95cd70a38cb712757a95dc2eb3efcb584908376",
        }
        for caminho, esperado in esperados.items():
            self.assertEqual(
                hashlib.sha256((ROOT / caminho).read_bytes()).hexdigest(), esperado, caminho
            )

    def test_matriz_permanece_fora_do_calculo_efetivo(self):
        self.assertFalse(hasattr(roles, "calcular_permissoes"))
        autorizacao = (ROOT / "services/autorizacao.py").read_text(encoding="utf-8")
        permissoes = (ROOT / "services/permissoes.py").read_text(encoding="utf-8")
        self.assertNotIn("roles_permissoes", autorizacao)
        self.assertNotIn("roles_permissoes", permissoes)


if __name__ == "__main__":
    unittest.main()
