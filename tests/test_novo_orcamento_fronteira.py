import importlib
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "app.py"
MENU = ROOT / "pages" / "menu.py"


class SessionState(dict):
    def __getattr__(self, nome):
        return self[nome]

    def __setattr__(self, nome, valor):
        self[nome] = valor


class StreamlitFalso:
    def __init__(self, *, botao=False):
        self.session_state = SessionState(tela="novo_orcamento")
        self.secrets = {"GITHUB_TOKEN": "token", "REPO": "org/repo"}
        self.botao = botao
        self.erros = []
        self.reruns = 0

    def error(self, texto):
        self.erros.append(texto)

    def button(self, *args, **kwargs):
        return self.botao

    def rerun(self):
        self.reruns += 1


class TestFronteiraNovoOrcamento(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.entrada = importlib.import_module(
            "modulos.orcamentos.apresentacao.entrada"
        )

    def test_novo_pacote_pode_ser_importado(self):
        self.assertIsNotNone(importlib.import_module("modulos.orcamentos"))

    def test_usuario_autorizado_abre_painel_com_repositorio_configurado(self):
        falso = StreamlitFalso()
        painel = Mock()
        repositorio = Mock()
        with patch.object(self.entrada, "st", falso), patch.object(
            self.entrada, "painel", painel
        ), patch.object(
            self.entrada, "RepositorioOrcamentosGitHub", return_value=repositorio
        ) as classe_repositorio:
            self.entrada.render(autorizado=True)
        classe_repositorio.assert_called_once_with("token", "org/repo")
        painel.render.assert_called_once_with(
            repositorio=repositorio,
            ao_voltar=self.entrada._voltar_ao_menu,
        )
        self.assertFalse(falso.erros)

    def test_usuario_nao_autorizado_nao_cria_repositorio(self):
        falso = StreamlitFalso()
        with patch.object(self.entrada, "st", falso), patch.object(
            self.entrada, "RepositorioOrcamentosGitHub"
        ) as classe_repositorio:
            self.entrada.render(autorizado=False)
        self.assertTrue(falso.erros)
        classe_repositorio.assert_not_called()

    def test_retorno_ao_menu_faz_um_unico_rerun(self):
        falso = StreamlitFalso()
        with patch.object(self.entrada, "st", falso):
            self.entrada._voltar_ao_menu()
        self.assertEqual(falso.session_state.tela, "menu")
        self.assertEqual(falso.reruns, 1)

    def test_rota_nova_e_guarda_de_permissao_estao_no_roteador(self):
        fonte = APP.read_text(encoding="utf-8")
        self.assertIn('st.session_state.tela == "novo_orcamento"', fonte)
        self.assertIn('pode_acessar_modulo("orcamento")', fonte)
        self.assertIn("novo_orcamento.render", fonte)

    def test_menu_exibe_nova_entrada_sob_mesma_permissao(self):
        fonte = MENU.read_text(encoding="utf-8")
        self.assertIn('pode_orcamento = pode_acessar_modulo("orcamento")', fonte)
        self.assertIn('"Novo Sistema de Orçamentos"', fonte)
        self.assertIn('"novo_orcamento"', fonte)

    def test_legado_e_obras_continuam_inalterados(self):
        fonte = APP.read_text(encoding="utf-8")
        for rota in (
            "orcamento", "orcamento_lista", "orcamento_etapa0",
            "orcamento1", "orcamento2", "orcamento3", "obras",
        ):
            self.assertIn(f'st.session_state.tela == "{rota}"', fonte)
        self.assertIn('ARQ_OBRAS = "data/orcamentos.csv"', fonte)

    def test_modulo_nao_contem_arquivo_de_dados(self):
        arquivos = [
            p for p in (ROOT / "modulos" / "orcamentos").rglob("*") if p.is_file()
        ]
        self.assertFalse([p for p in arquivos if p.suffix.lower() in {".csv", ".json"}])


if __name__ == "__main__":
    unittest.main()
