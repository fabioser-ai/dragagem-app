from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "services" / "ui.py"
DADOS = ROOT / "pages" / "dados_hub.py"


class CabecalhoModulosTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ui_source = UI.read_text(encoding="utf-8")
        cls.dados_source = DADOS.read_text(encoding="utf-8")

    def test_ui_oferece_cabecalho_padronizado(self):
        self.assertIn("def renderizar_cabecalho_modulo(", self.ui_source)
        self.assertIn("fos_module_header", self.ui_source)
        self.assertIn("background: #ffffff", self.ui_source)
        self.assertIn("color: #0f172a", self.ui_source)

    def test_cabecalho_posiciona_acao_de_retorno_a_direita(self):
        self.assertIn("st.columns([5, 1]", self.ui_source)
        self.assertIn("use_container_width=True", self.ui_source)

    def test_dados_adota_cabecalho_e_remove_retorno_inferior(self):
        self.assertIn("renderizar_cabecalho_modulo", self.dados_source)
        self.assertNotIn('st.title("Dados")', self.dados_source)
        self.assertNotIn('"← Voltar ao menu"', self.dados_source)
        self.assertNotIn('"← Voltar para Dados"', self.dados_source)


if __name__ == "__main__":
    unittest.main()
