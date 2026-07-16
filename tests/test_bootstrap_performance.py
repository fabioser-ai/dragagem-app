import ast
import importlib.util
import json
import sys
import types
import unittest
from contextlib import nullcontext
from pathlib import Path
from unittest.mock import Mock


ROOT = Path(__file__).resolve().parents[1]


class SessionState(dict):
    def __getattr__(self, nome):
        return self[nome]

    def __setattr__(self, nome, valor):
        self[nome] = valor


class AreaLogin:
    def __init__(self):
        self.removida = False

    def container(self):
        return nullcontext()

    def empty(self):
        self.removida = True


class StreamlitFalso:
    def __init__(self, *, usuario="fabio", senha="segredo", entrar=False):
        self.session_state = SessionState()
        self.secrets = {
            "APP_USERS": json.dumps({
                "fabio": {
                    "password": "segredo",
                    "role": "superadmin",
                    "matricula": "1",
                    "nome": "Fabio",
                }
            })
        }
        self._entrar = entrar
        self._textos = iter((usuario, senha))
        self.area = AreaLogin()
        self.erros = []
        self.avisos = []
        self.reruns = 0

    def empty(self):
        return self.area

    def markdown(self, *args, **kwargs):
        pass

    def caption(self, *args, **kwargs):
        pass

    def text_input(self, *args, **kwargs):
        return next(self._textos)

    def button(self, *args, **kwargs):
        return self._entrar

    def error(self, texto):
        self.erros.append(texto)

    def warning(self, texto):
        self.avisos.append(texto)

    def rerun(self):
        self.reruns += 1

    def stop(self):
        pass


def carregar_auth(streamlit_falso, registrar_log=None):
    modulo_streamlit = types.ModuleType("streamlit")
    for nome in dir(streamlit_falso):
        if not nome.startswith("__"):
            setattr(modulo_streamlit, nome, getattr(streamlit_falso, nome))

    modulo_log = types.ModuleType("services.log")
    modulo_log.registrar_log = registrar_log or Mock()
    anteriores = {
        "streamlit": sys.modules.get("streamlit"),
        "services.log": sys.modules.get("services.log"),
    }
    sys.modules["streamlit"] = modulo_streamlit
    sys.modules["services.log"] = modulo_log
    try:
        spec = importlib.util.spec_from_file_location(
            "auth_sob_teste", ROOT / "services" / "auth.py"
        )
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        return modulo
    finally:
        for nome, anterior in anteriores.items():
            if anterior is None:
                sys.modules.pop(nome, None)
            else:
                sys.modules[nome] = anterior


class TestBootstrapPerformance(unittest.TestCase):
    def test_app_nao_importa_modulos_funcionais_antes_do_login(self):
        arvore = ast.parse((ROOT / "app.py").read_text(encoding="utf-8"))
        imports = [
            no for no in arvore.body if isinstance(no, (ast.Import, ast.ImportFrom))
        ]
        modulos = {alias.name for no in imports for alias in no.names}
        self.assertNotIn("pages", modulos)
        self.assertFalse(any(modulo.startswith("pages.") for modulo in modulos))
        self.assertFalse(any(modulo.startswith("modulos.") for modulo in modulos))

    def test_login_valido_abre_menu_sem_rerun_e_agenda_log(self):
        falso = StreamlitFalso(entrar=True)
        auth = carregar_auth(falso)
        self.assertTrue(auth.verificar_login())
        self.assertTrue(falso.session_state.autenticado)
        self.assertEqual(falso.session_state.tela, "menu")
        self.assertEqual(
            falso.session_state[auth.CHAVE_LOG_PENDENTE],
            ("fabio", "superadmin", "login"),
        )
        self.assertTrue(falso.area.removida)
        self.assertEqual(falso.reruns, 0)

    def test_login_invalido_permanece_bloqueado(self):
        falso = StreamlitFalso(senha="errada", entrar=True)
        auth = carregar_auth(falso)
        self.assertFalse(auth.verificar_login())
        self.assertFalse(falso.session_state.autenticado)
        self.assertTrue(falso.erros)
        self.assertNotIn(auth.CHAVE_LOG_PENDENTE, falso.session_state)

    def test_sessao_valida_nao_exibe_formulario(self):
        falso = StreamlitFalso()
        auth = carregar_auth(falso)
        falso.session_state.update(
            autenticado=True,
            usuario="fabio",
            perfil="superadmin",
            ultimo_acesso=auth.time.time(),
        )
        self.assertTrue(auth.verificar_login())
        self.assertFalse(falso.area.removida)

    def test_sessao_expirada_limpa_estado_e_registra_log(self):
        falso = StreamlitFalso()
        log = Mock()
        auth = carregar_auth(falso, log)
        falso.session_state.update(
            autenticado=True,
            usuario="fabio",
            perfil="superadmin",
            ultimo_acesso=auth.time.time() - auth.SESSION_TIMEOUT_SECONDS - 1,
        )
        self.assertFalse(auth.verificar_login())
        log.assert_called_once_with("fabio", "superadmin", "sessao_expirada")
        self.assertNotIn("autenticado", falso.session_state)
        self.assertTrue(falso.avisos)

    def test_log_pendente_e_gravado_uma_unica_vez(self):
        falso = StreamlitFalso()
        log = Mock(return_value="ok")
        auth = carregar_auth(falso, log)
        falso.session_state[auth.CHAVE_LOG_PENDENTE] = (
            "fabio", "superadmin", "login"
        )
        self.assertEqual(auth.processar_log_pendente(), "ok")
        self.assertIsNone(auth.processar_log_pendente())
        log.assert_called_once_with("fabio", "superadmin", "login")


if __name__ == "__main__":
    unittest.main()
