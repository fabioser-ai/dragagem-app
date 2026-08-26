import unittest
from unittest.mock import patch

from pages import menu


class TestUXRBACRoleHeader(unittest.TestCase):
    def setUp(self):
        menu.st.session_state.clear()

    def test_role_operacional_substitui_perfil_legado(self):
        menu.st.session_state.update(usuario="teste", perfil="funcionario")
        with patch.object(
            menu,
            "listar_permissoes",
            return_value=[
                {"role": "ENGENHARIA"},
                {"role": "ENGENHARIA"},
            ],
        ):
            self.assertEqual(menu._rotulo_funcao_usuario(), "Função: Engenharia")

    def test_multiplas_roles_sao_exibidas_sem_duplicidade(self):
        menu.st.session_state.update(usuario="teste", perfil="funcionario")
        with patch.object(
            menu,
            "listar_permissoes",
            return_value=[
                {"role": "RH"},
                {"role": "APROVADOR"},
                {"role": "RH"},
            ],
        ):
            self.assertEqual(menu._rotulo_funcao_usuario(), "Funções: Aprovador, Rh")

    def test_sem_concessao_nao_exibe_perfil_legado(self):
        menu.st.session_state.update(usuario="teste", perfil="funcionario")
        with patch.object(menu, "listar_permissoes", return_value=[]):
            self.assertEqual(menu._rotulo_funcao_usuario(), "Nenhuma função atribuída")

    def test_conta_administrativa_protegida_nao_e_tratada_como_role(self):
        for perfil in ("admin", "superadmin"):
            with self.subTest(perfil=perfil):
                menu.st.session_state.clear()
                menu.st.session_state.update(usuario="fabio", perfil=perfil)
                with patch.object(menu, "listar_permissoes") as listar:
                    self.assertEqual(menu._rotulo_funcao_usuario(), "Administrador do sistema")
                    listar.assert_not_called()


if __name__ == "__main__":
    unittest.main()
