import ast
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


ROOT = Path(__file__).resolve().parents[1]


class SessionState(dict):
    def __getattr__(self, nome):
        return self[nome]

    def __setattr__(self, nome, valor):
        self[nome] = valor


streamlit = sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
streamlit.session_state = SessionState()
streamlit.secrets = {}

from services import autorizacao  # noqa: E402
from services import auth  # noqa: E402
from services import permissoes  # noqa: E402


def rotas_do_roteador():
    arvore = ast.parse((ROOT / "app.py").read_text(encoding="utf-8"))
    rotas = set()
    for no in ast.walk(arvore):
        if not isinstance(no, ast.Compare) or not isinstance(no.left, ast.Name):
            continue
        if no.left.id != "tela":
            continue
        for comparador in no.comparators:
            if isinstance(comparador, ast.Constant) and isinstance(comparador.value, str):
                rotas.add(comparador.value)
            elif isinstance(comparador, (ast.Set, ast.Tuple, ast.List)):
                rotas.update(
                    item.value
                    for item in comparador.elts
                    if isinstance(item, ast.Constant) and isinstance(item.value, str)
                )
    return rotas


class TestFronteiraCentralAutorizacao(unittest.TestCase):
    def setUp(self):
        streamlit.session_state.clear()

    def autenticar(self, *, perfil="user", usuario="usuario"):
        streamlit.session_state.update(
            autenticado=True,
            perfil=perfil,
            usuario=usuario,
            tela="menu",
        )

    def test_usuario_sem_login_e_negado(self):
        self.assertFalse(autorizacao.pode_acessar_rota("menu"))
        self.assertFalse(autorizacao.pode_acessar_rota("dados"))

    def test_usuario_autenticado_sem_permissao_e_negado(self):
        self.autenticar()
        with patch.object(autorizacao, "pode_acessar_modulo", return_value=False):
            self.assertFalse(autorizacao.pode_acessar_rota("dados"))

    def test_usuario_autorizado_acessa_modulo(self):
        self.autenticar()
        with patch.object(autorizacao, "pode_acessar_modulo", return_value=True) as decidir:
            self.assertTrue(autorizacao.pode_acessar_rota("crm"))
        decidir.assert_called_once_with("crm")

    def test_superadmin_acessa_todas_as_rotas_conhecidas(self):
        self.autenticar(perfil="superadmin", usuario="fabio")
        with patch.object(autorizacao, "eh_superadmin", return_value=True), patch.object(
            autorizacao, "pode_acessar_modulo", return_value=True
        ):
            for tela in {"menu", "administracao", *autorizacao.ROTAS_POR_MODULO}:
                with self.subTest(tela=tela):
                    self.assertTrue(autorizacao.pode_acessar_rota(tela))

    def test_rota_direta_e_alteracao_de_tela_nao_contornam_permissao(self):
        self.autenticar()
        streamlit.session_state.tela = "dados"
        with patch.object(autorizacao, "pode_acessar_modulo", return_value=False):
            self.assertFalse(
                autorizacao.pode_acessar_rota(streamlit.session_state.tela)
            )

    def test_modulo_desconhecido_e_negado_por_padrao(self):
        self.autenticar()
        self.assertFalse(autorizacao.pode_acessar_rota("modulo_inexistente"))
        self.assertFalse(autorizacao.pode_acessar_rota(""))

    def test_restricao_existente_de_funcionario_e_preservada(self):
        self.autenticar(perfil="funcionario")
        with patch.object(autorizacao, "pode_acessar_modulo", return_value=True):
            self.assertFalse(autorizacao.pode_acessar_rota("dados"))
            self.assertTrue(autorizacao.pode_acessar_rota("prestacao_contas"))

    def test_toda_rota_despachada_possui_decisao_central(self):
        rotas = rotas_do_roteador()
        declaradas = {"menu", "administracao", *autorizacao.ROTAS_POR_MODULO}
        self.assertEqual(rotas, declaradas)
        fonte = (ROOT / "app.py").read_text(encoding="utf-8")
        self.assertIn("if not pode_acessar_rota(tela):", fonte)

    def test_admin_e_superadmin_passam_na_verificacao_administrativa(self):
        for perfil in ("admin", "superadmin"):
            with self.subTest(perfil=perfil):
                streamlit.session_state["perfil"] = perfil
                self.assertTrue(permissoes.eh_administrador_sistema())

    def test_exigir_admin_nao_bloqueia_superadmin(self):
        streamlit.error = Mock()
        streamlit.stop = Mock()
        with patch.object(
            permissoes, "eh_administrador_sistema", return_value=True
        ):
            auth.exigir_admin()
        streamlit.error.assert_not_called()
        streamlit.stop.assert_not_called()

    def test_perfis_comuns_nao_passam_na_verificacao_administrativa(self):
        for perfil in ("user", "funcionario", ""):
            with self.subTest(perfil=perfil):
                streamlit.session_state["perfil"] = perfil
                self.assertFalse(permissoes.eh_administrador_sistema())


if __name__ == "__main__":
    unittest.main()
