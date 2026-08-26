import unittest
from unittest.mock import patch

import pandas as pd

from services import autorizacao, rbac_authority as rbac


def fontes(*, identidade_ativa="sim", associacoes=None, roles=None, matriz=None,
           catalogo=None):
    return {
        "usuarios": pd.DataFrame([{"usuario_id": "u1", "login": "teste", "ativo": identidade_ativa}]),
        "associacoes": pd.DataFrame(associacoes if associacoes is not None else [
            {"usuario_id": "u1", "role_id": "r1", "obra_id": "todas", "ativo": "sim"}
        ]),
        "roles": pd.DataFrame(roles if roles is not None else [
            {"role_id": "r1", "codigo": "OPERADOR", "ativo": "sim"}
        ]),
        "matriz": pd.DataFrame(matriz if matriz is not None else [
            {"role_id": "r1", "modulo": "medicoes", "recurso": "lancamento", "acao": "criar", "efeito": "allow"}
        ]),
        "catalogo": pd.DataFrame(catalogo if catalogo is not None else [
            {"modulo": "medicoes", "recurso": "lancamento", "acao": "criar", "escopo_obra": "sim", "ativo": "sim"}
        ]),
    }


class TestAutoridadeRBAC(unittest.TestCase):
    def test_sem_role_nega(self):
        f = fontes(associacoes=[])
        f["associacoes"] = pd.DataFrame(columns=["usuario_id", "role_id", "obra_id", "ativo"])
        self.assertEqual(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", fontes=f).codigo, "sem_role_ativa")

    def test_role_ativa_concede_e_inativa_nao(self):
        self.assertTrue(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", fontes=fontes()).permitido)
        f = fontes(roles=[{"role_id": "r1", "codigo": "OPERADOR", "ativo": "nao"}])
        self.assertFalse(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", fontes=f).permitido)

    def test_multiplas_roles_e_origem(self):
        f = fontes(
            associacoes=[{"usuario_id": "u1", "role_id": r, "obra_id": "todas", "ativo": "sim"} for r in ("r1", "r2")],
            roles=[{"role_id": "r1", "codigo": "A", "ativo": "sim"}, {"role_id": "r2", "codigo": "B", "ativo": "sim"}],
            matriz=[{"role_id": r, "modulo": "medicoes", "recurso": "lancamento", "acao": "criar", "efeito": "allow"} for r in ("r1", "r2")],
        )
        decisao = rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", fontes=f)
        self.assertEqual(decisao.roles, ("A", "B"))
        self.assertEqual(decisao.origens, ("A@todas", "B@todas"))

    def test_escopo_todas_e_especifico(self):
        global_ = fontes()
        self.assertTrue(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", obra_id="obra-a", fontes=global_).permitido)
        especifico = fontes(associacoes=[{"usuario_id": "u1", "role_id": "r1", "obra_id": "obra-a", "ativo": "sim"}])
        self.assertTrue(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", obra_id="obra-a", fontes=especifico).permitido)
        self.assertFalse(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", obra_id="obra-b", fontes=especifico).permitido)
        self.assertEqual(rbac.listar_obras(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", fontes=especifico), ["obra-a"])

    def test_deny_explicito_prevalece(self):
        f = fontes(matriz=[
            {"role_id": "r1", "modulo": "medicoes", "recurso": "lancamento", "acao": "criar", "efeito": "allow"},
            {"role_id": "r1", "modulo": "medicoes", "recurso": "lancamento", "acao": "criar", "efeito": "deny"},
        ])
        self.assertEqual(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", fontes=f).codigo, "negada_explicitamente")

    def test_inativo_desconhecido_fonte_invalida_negam(self):
        self.assertFalse(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", fontes=fontes(identidade_ativa="nao")).permitido)
        self.assertEqual(rbac.avaliar(usuario="teste", modulo="x", recurso="x", acao="x", fontes=fontes()).codigo, "permissao_desconhecida")
        self.assertEqual(rbac.avaliar(usuario="teste", modulo="x", recurso="x", acao="x", fontes={}).codigo, "leitura_nao_confirmada")


class TestFronteiraModos(unittest.TestCase):
    def setUp(self):
        autorizacao.st.session_state.clear()
        autorizacao.st.session_state.update(
            autenticado=True, usuario="teste", perfil="superadmin"
        )

    def test_rbac_padrao_sem_fallback_legado(self):
        autorizacao.st.secrets = {}
        with patch.object(autorizacao.rbac_authority, "avaliar_modulo", return_value=rbac.DecisaoRBAC(False, "sem_role_ativa")), patch.object(autorizacao, "pode_acessar_modulo") as legado:
            self.assertFalse(autorizacao.pode_acessar("crm"))
            legado.assert_not_called()

    def test_rollback_legacy_exclusivo(self):
        autorizacao.st.secrets = {"AUTHORIZATION_MODE": "LEGACY"}
        with patch.object(autorizacao, "pode_acessar_modulo", return_value=True), patch.object(autorizacao.rbac_authority, "avaliar_modulo") as novo:
            self.assertTrue(autorizacao.pode_acessar("crm"))
            novo.assert_not_called()

    def test_modo_invalido_nega(self):
        autorizacao.st.secrets = {"AUTHORIZATION_MODE": "HIBRIDO"}
        self.assertFalse(autorizacao.pode_acessar("crm"))

    def test_bypass_somente_owner_canonico(self):
        autorizacao.st.secrets = {"SYSTEM_OWNER_ID": "fabio", "AUTHORIZATION_MODE": "RBAC"}
        self.assertFalse(autorizacao.temporary_owner_bypass())
        autorizacao.st.session_state["usuario"] = "fabio"
        self.assertTrue(autorizacao.temporary_owner_bypass())
        self.assertTrue(autorizacao.pode_acessar("qualquer_modulo"))


if __name__ == "__main__":
    unittest.main()
