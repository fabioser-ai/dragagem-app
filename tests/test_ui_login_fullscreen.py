from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "services" / "ui.py"


class LoginFosFullscreenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = UI.read_text(encoding="utf-8")

    def test_login_visual_fica_na_camada_de_ui(self):
        self.assertIn("def _renderizar_marca_login", self.source)
        self.assertNotIn("st.text_input(", self.source)
        self.assertNotIn("def verificar_login", self.source)

    def test_fullscreen_e_ancorado_no_password_real(self):
        self.assertIn('[data-testid="stAppViewContainer"]:has(input[type="password"])', self.source)
        self.assertIn("position:fixed", self.source)
        self.assertIn("min-height:100vh", self.source)
        self.assertIn("Acesso ao <strong>APP FOS</strong>", self.source)
        self.assertIn("Entre com suas credenciais para continuar", self.source)

    def test_background_nao_bloqueia_widgets(self):
        self.assertIn("pointer-events:none", self.source)
        self.assertIn("z-index:3", self.source)
        self.assertIn(".block-container input", self.source)
        self.assertIn(".stButton > button", self.source)

    def test_responsivo_e_reduced_motion(self):
        self.assertIn("@media (max-width: 640px)", self.source)
        self.assertIn("@media (max-height: 690px)", self.source)
        self.assertIn("@media (prefers-reduced-motion: reduce)", self.source)
        self.assertIn("animation:none !important", self.source)


if __name__ == "__main__":
    unittest.main()
