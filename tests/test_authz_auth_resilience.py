import unittest
from contextlib import nullcontext
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

import pandas as pd

from pages import administracao
from services.github import ResultadoLeituraCSV, StatusLeitura
from tests.test_bootstrap_performance import StreamlitFalso, carregar_auth


ROOT = Path(__file__).resolve().parents[1]


class TestUXResilienciaAutenticacao(unittest.TestCase):
    def test_login_invalido_mantem_mensagem_generica(self):
        falso = StreamlitFalso(usuario="operador", senha="errada", entrar=True)
        modulo = carregar_auth(falso)
        with patch.object(
            modulo, "_autenticar_operacional",
            return_value=SimpleNamespace(dados=None, indisponivel=False),
        ):
            self.assertFalse(modulo.verificar_login())
        self.assertIn("Usuário ou senha incorretos", falso.erros[0])

    def test_backend_indisponivel_tem_mensagem_segura_distinta(self):
        falso = StreamlitFalso(usuario="operador", senha="qualquer", entrar=True)
        modulo = carregar_auth(falso)
        with patch.object(
            modulo, "_autenticar_operacional",
            return_value=SimpleNamespace(dados=None, indisponivel=True),
        ):
            self.assertFalse(modulo.verificar_login())
        mensagem = falso.erros[0]
        self.assertIn("Não foi possível validar seu acesso", mensagem)
        self.assertNotIn("operador", mensagem)
        self.assertNotIn("qualquer", mensagem)

    def test_superadmin_continua_autenticando_sem_backend_operacional(self):
        falso = StreamlitFalso(entrar=True)
        modulo = carregar_auth(falso)
        with patch.object(modulo, "_autenticar_operacional") as operacional:
            self.assertTrue(modulo.verificar_login())
        operacional.assert_not_called()

    def test_administracao_exibe_rate_limit_sem_dado_sensivel(self):
        resultado = ResultadoLeituraCSV(
            StatusLeitura.RATE_LIMIT_PRIMARIO,
            pd.DataFrame(),
            "data/usuarios_operacionais.csv",
            http_status=403,
            erro="erro interno",
            rate_limit_limit=5000,
            rate_limit_remaining=0,
            rate_limit_reset=1787742000,
        )
        falso = Mock()
        falso.expander.return_value = nullcontext()
        with patch.object(administracao, "st", falso):
            administracao._render_diagnostico_leitura_github(
                resultado, fonte="usuários operacionais"
            )
        mensagem = falso.error.call_args.args[0]
        escritos = " ".join(str(c.args[0]) for c in falso.write.call_args_list)
        self.assertIn("temporariamente limitada", mensagem)
        self.assertIn("rate_limit_primario", escritos)
        self.assertIn("Restante informado: 0", escritos)
        self.assertNotIn("token", (mensagem + escritos).casefold())

    def test_rbac_e_bcrypt_nao_foram_alterados(self):
        github = (ROOT / "services/github.py").read_text(encoding="utf-8")
        credenciais = (ROOT / "services/credenciais_operacionais.py").read_text(encoding="utf-8")
        self.assertNotIn("sleep(", github)
        self.assertIn("bcrypt.checkpw", credenciais)
        self.assertIn("from services import rbac_authority", (ROOT / "services/autorizacao.py").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
