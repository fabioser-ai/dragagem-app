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

    def test_matriz_valida_todas_as_seis_roles_e_somente_allow(self):
        self.assertEqual(self.validar(), [])
        codigos = dict(zip(self.catalogo_roles["role_id"], self.catalogo_roles["codigo"]))
        contagens = self.matriz.assign(
            codigo=self.matriz["role_id"].map(codigos)
        ).groupby("codigo").size().to_dict()
        self.assertEqual(
            contagens,
            {
                "FUNCIONARIO": 2,
                "ENCARREGADO": 5,
                "APROVADOR": 2,
                "ENGENHARIA": 18,
                "FINANCEIRO": 4,
                "RH": 12,
            },
        )
        self.assertEqual(set(self.matriz["efeito"]), {"allow"})

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
        esperados = {
            "services/auth.py": "b8f864ed3c9a892f53280e28ee56b78f5c979cee62d253923f88b55b477caec0",
            "services/autorizacao.py": "ceb618911b47eb8cfaf5452033fd85cc8def55e55484fe23a5a807f5315cd9de",
            "data/permissoes_usuarios.csv": "23b33a97d78c41f217e7bcdae397e5fcb555f72c344974adb3b1550cad2dca5e",
            "data/usuarios_operacionais.csv": "ce72411b6c49e15814fea35d285ee291ba7282fba2ee807db6a7e1b70a3dbb79",
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
