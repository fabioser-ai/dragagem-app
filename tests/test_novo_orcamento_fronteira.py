import ast
import importlib
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "app.py"
MENU = ROOT / "pages" / "menu.py"
ENTRADA = ROOT / "modulos" / "orcamentos" / "apresentacao" / "entrada.py"


class SessionState(dict):
    def __getattr__(self, nome):
        return self[nome]

    def __setattr__(self, nome, valor):
        self[nome] = valor


class StreamlitFalso:
    def __init__(self, *, botao=False):
        self.session_state = SessionState(tela="novo_orcamento")
        self.botao = botao
        self.titulos = []
        self.infos = []
        self.erros = []
        self.markdowns = []
        self.reruns = 0

    def title(self, texto):
        self.titulos.append(texto)

    def info(self, texto):
        self.infos.append(texto)

    def error(self, texto):
        self.erros.append(texto)

    def markdown(self, texto):
        self.markdowns.append(texto)

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

    def renderizar(self, *, autorizado, botao=False):
        falso = StreamlitFalso(botao=botao)
        with patch.object(self.entrada, "st", falso):
            self.entrada.render(autorizado=autorizado)
        return falso

    def test_novo_pacote_pode_ser_importado(self):
        pacote = importlib.import_module("modulos.orcamentos")
        self.assertIsNotNone(pacote)

    def test_usuario_autorizado_visualiza_pagina_informativa(self):
        st = self.renderizar(autorizado=True)
        self.assertEqual(st.titulos, ["Novo Sistema de Orçamentos"])
        self.assertFalse(st.erros)
        self.assertIn("Nenhum dado de orçamento", st.markdowns[0])
        self.assertEqual(st.reruns, 0)

    def test_usuario_nao_autorizado_nao_visualiza_conteudo(self):
        st = self.renderizar(autorizado=False)
        self.assertTrue(st.erros)
        self.assertFalse(st.titulos)
        self.assertFalse(st.infos)
        self.assertEqual(st.reruns, 0)

    def test_retorno_ao_menu_faz_um_unico_rerun(self):
        st = self.renderizar(autorizado=True, botao=True)
        self.assertEqual(st.session_state.tela, "menu")
        self.assertEqual(st.reruns, 1)

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

    def test_legado_continua_roteado(self):
        fonte = APP.read_text(encoding="utf-8")
        for rota in (
            "orcamento",
            "orcamento_lista",
            "orcamento_etapa0",
            "orcamento1",
            "orcamento2",
            "orcamento3",
        ):
            self.assertIn(f'st.session_state.tela == "{rota}"', fonte)

    def test_rota_obras_permanece_com_fonte_legada(self):
        fonte = APP.read_text(encoding="utf-8")
        self.assertIn('st.session_state.tela == "obras"', fonte)
        self.assertIn('ARQ_OBRAS = "data/orcamentos.csv"', fonte)

    def test_pagina_nao_importa_ou_chama_leitura_remota(self):
        arvore = ast.parse(ENTRADA.read_text(encoding="utf-8"))
        imports = {
            alias.name
            for no in ast.walk(arvore)
            if isinstance(no, ast.Import)
            for alias in no.names
        }
        imports_de = {
            no.module
            for no in ast.walk(arvore)
            if isinstance(no, ast.ImportFrom)
        }
        self.assertEqual(imports, {"streamlit"})
        self.assertEqual(imports_de, set())
        fonte = ENTRADA.read_text(encoding="utf-8")
        for proibido in ("carregar_github", "ler_csv_github", "requests", ".csv", ".json"):
            self.assertNotIn(proibido, fonte)

    def test_nao_existe_loop_de_navegacao(self):
        fonte = ENTRADA.read_text(encoding="utf-8")
        self.assertEqual(fonte.count("st.rerun()"), 1)
        st = self.renderizar(autorizado=True, botao=False)
        self.assertEqual(st.reruns, 0)

    def test_modulo_nao_contem_arquivo_de_dados(self):
        arquivos = [
            p
            for p in (ROOT / "modulos" / "orcamentos").rglob("*")
            if p.is_file()
        ]
        self.assertFalse(
            [p for p in arquivos if p.suffix.lower() in {".csv", ".json"}]
        )


if __name__ == "__main__":
    unittest.main()
