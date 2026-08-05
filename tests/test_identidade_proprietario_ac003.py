import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from services import auth, autorizacao


ROOT = Path(__file__).resolve().parents[1]
OWNER = "owner.canonical"


class TestIdentidadeProprietarioAC003(unittest.TestCase):
    def setUp(self):
        if not hasattr(autorizacao.st, "session_state"):
            autorizacao.st.session_state = {}
        autorizacao.st.session_state.clear()
        autorizacao.st.secrets = {"SYSTEM_OWNER_ID": OWNER}

    def autenticar(self, usuario=OWNER, perfil="user"):
        autorizacao.st.session_state.update(
            autenticado=True,
            usuario=usuario,
            perfil=perfil,
            tela="menu",
        )

    def test_proprietario_e_identidade_valida_sao_reconhecidos(self):
        self.autenticar()
        self.assertEqual(autorizacao.identificador_proprietario(), OWNER)
        self.assertTrue(autorizacao.identidade_proprietario_valida())
        self.assertTrue(autorizacao.usuario_proprietario())

    def test_usuario_comum_admin_e_superadmin_nao_viram_proprietario(self):
        for perfil in ("user", "admin", "superadmin"):
            with self.subTest(perfil=perfil):
                self.autenticar(usuario="outro.usuario", perfil=perfil)
                self.assertFalse(autorizacao.usuario_proprietario())
                if perfil == "superadmin":
                    self.assertTrue(autorizacao.usuario_superadmin())

    def test_secret_ausente_gera_negacao_e_diagnostico_seguro(self):
        autorizacao.st.secrets = {}
        self.autenticar()
        self.assertFalse(autorizacao.identidade_proprietario_valida())
        self.assertFalse(autorizacao.usuario_proprietario())
        diagnostico = autorizacao.diagnostico_identidade_proprietario()
        self.assertEqual(diagnostico["codigo"], "secret_ausente")
        self.assertNotIn(OWNER, repr(diagnostico))

    def test_secrets_invalidos_geram_negacao_segura(self):
        for valor in (None, "", " owner", "owner ", "owner inválido", [OWNER]):
            with self.subTest(valor=valor):
                autorizacao.st.secrets = {"SYSTEM_OWNER_ID": valor}
                self.autenticar()
                self.assertFalse(autorizacao.identidade_proprietario_valida())
                self.assertFalse(autorizacao.usuario_proprietario())
                self.assertEqual(
                    autorizacao.diagnostico_identidade_proprietario()["codigo"],
                    "secret_invalido",
                )

    def test_app_users_nao_define_nem_altera_propriedade(self):
        self.autenticar()
        autorizacao.st.secrets["APP_USERS"] = '{"outro.usuario":{"role":"superadmin"}}'
        self.assertTrue(autorizacao.usuario_proprietario())
        autorizacao.st.secrets["APP_USERS"] = '{}'
        self.assertTrue(autorizacao.usuario_proprietario())

    def test_promocao_para_superadmin_nao_cria_proprietario(self):
        self.autenticar(usuario="promovido", perfil="superadmin")
        self.assertTrue(autorizacao.usuario_superadmin())
        self.assertFalse(autorizacao.usuario_proprietario())
        self.assertFalse(autorizacao.pode_recuperar_administracao())

    def test_proprietario_sem_superadmin_tem_diagnostico_consistente(self):
        self.autenticar(perfil="funcionario")
        diagnostico = autorizacao.diagnostico_identidade_proprietario()
        self.assertEqual(diagnostico["codigo"], "proprietario_sem_superadmin")
        self.assertTrue(diagnostico["sessao_proprietario"])
        self.assertFalse(diagnostico["recuperacao_ativa"])

    def test_recuperacao_exclusiva_do_proprietario(self):
        self.autenticar(perfil="user")
        with patch.object(autorizacao, "_registrar_recuperacao", return_value=True) as log:
            resultado = autorizacao.recuperar_administracao()
        self.assertTrue(resultado["sucesso"])
        self.assertTrue(autorizacao.recuperacao_administrativa_ativa())
        self.assertTrue(autorizacao.possui_privilegio_administrativo())
        self.assertTrue(autorizacao.pode_gerenciar_administracao())
        self.assertFalse(autorizacao.usuario_superadmin())
        log.assert_called_once_with("concedida")

    def test_resultado_da_tentativa_e_registrado_sem_incluir_secret_na_acao(self):
        self.autenticar()
        with patch("services.log.registrar_log", return_value=object()) as registrar:
            self.assertTrue(autorizacao._registrar_recuperacao("concedida"))
        registrar.assert_called_once_with(
            OWNER,
            "user",
            "recuperacao_administracao_concedida",
        )
        self.assertNotIn(OWNER, registrar.call_args.args[2])

    def test_recuperacao_negada_a_admin_e_superadmin_nao_proprietarios(self):
        for perfil in ("admin", "superadmin"):
            with self.subTest(perfil=perfil):
                self.autenticar(usuario="outro", perfil=perfil)
                with patch.object(
                    autorizacao, "_registrar_recuperacao", return_value=True
                ) as log:
                    resultado = autorizacao.recuperar_administracao()
                self.assertFalse(resultado["sucesso"])
                self.assertFalse(autorizacao.recuperacao_administrativa_ativa())
                log.assert_called_once_with("negada")

    def test_identidade_e_revalidada_imediatamente_antes_da_recuperacao(self):
        self.autenticar()
        with patch.object(
            autorizacao, "usuario_proprietario", side_effect=(True, False)
        ), patch.object(autorizacao, "_registrar_recuperacao", return_value=True):
            resultado = autorizacao.recuperar_administracao()
        self.assertFalse(resultado["sucesso"])
        self.assertNotIn(
            autorizacao.CHAVE_RECUPERACAO_ADMIN,
            autorizacao.st.session_state,
        )

    def test_marca_de_recuperacao_isolada_nao_concede_autoridade(self):
        self.autenticar(usuario="outro", perfil="user")
        autorizacao.st.session_state[autorizacao.CHAVE_RECUPERACAO_ADMIN] = True
        self.assertFalse(autorizacao.recuperacao_administrativa_ativa())
        self.assertFalse(autorizacao.possui_privilegio_administrativo())
        self.assertFalse(autorizacao.pode_gerenciar_administracao())

    def test_logout_remove_recuperacao_da_sessao(self):
        self.autenticar()
        autorizacao.st.session_state[autorizacao.CHAVE_RECUPERACAO_ADMIN] = True
        auth.st.session_state = autorizacao.st.session_state
        auth.limpar_sessao()
        self.assertNotIn(
            autorizacao.CHAVE_RECUPERACAO_ADMIN,
            autorizacao.st.session_state,
        )

    def test_interface_administrativa_nao_le_nem_altera_secret(self):
        fonte = (ROOT / "pages" / "administracao.py").read_text(encoding="utf-8")
        self.assertNotIn("SYSTEM_OWNER_ID", fonte)
        self.assertNotIn("st.secrets", fonte)

    def test_secret_canônico_tem_uma_unica_fonte_no_codigo_funcional(self):
        ocorrencias = []
        for raiz in (ROOT / "services", ROOT / "pages", ROOT / "modulos"):
            for arquivo in raiz.rglob("*.py"):
                if "SYSTEM_OWNER_ID" in arquivo.read_text(encoding="utf-8"):
                    ocorrencias.append(arquivo.relative_to(ROOT).as_posix())
        self.assertEqual(ocorrencias, ["services/autorizacao.py"])

    def test_diagnostico_e_resultado_nao_expoem_identidade(self):
        self.autenticar()
        diagnostico = autorizacao.diagnostico_identidade_proprietario()
        with patch.object(autorizacao, "_registrar_recuperacao", return_value=True):
            resultado = autorizacao.recuperar_administracao()
        self.assertNotIn(OWNER, repr(diagnostico))
        self.assertNotIn(OWNER, repr(resultado))


if __name__ == "__main__":
    unittest.main()
