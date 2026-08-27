from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "services" / "ui.py"
APP = ROOT / "app.py"


class LoginFosFullscreenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ui_source = UI.read_text(encoding="utf-8")
        cls.app_source = APP.read_text(encoding="utf-8")

    def test_login_visual_fica_na_camada_de_ui(self):
        self.assertIn("def renderizar_login_fos", self.ui_source)
        self.assertNotIn("st.text_input(", self.ui_source)
        self.assertNotIn("def verificar_login", self.ui_source)

    def test_renderer_nao_executa_como_side_effect_do_import(self):
        self.assertNotIn("\nrenderizar_login_fos()\n", self.ui_source)
        self.assertNotIn("\n_renderizar_marca_login()\n", self.ui_source)
        self.assertIn("from services.ui import aplicar_estilo_global, renderizar_login_fos", self.app_source)

    def test_app_renderiza_login_explicitamente_em_cada_execucao_deslogada(self):
        self.assertIn("autenticado_antes = bool(st.session_state.get(\"autenticado\"))", self.app_source)
        self.assertIn("if not autenticado_antes:", self.app_source)
        self.assertIn("renderizar_login_fos()", self.app_source)
        self.assertIn("if not verificar_login():", self.app_source)

    def test_login_bem_sucedido_forca_rerun_limpo(self):
        self.assertIn("if not autenticado_antes and st.session_state.get(\"autenticado\"):", self.app_source)
        self.assertIn("st.rerun()", self.app_source)

    def test_fullscreen_nao_depende_de_has_dom(self):
        self.assertNotIn(':has(input[type="password"])', self.ui_source)
        self.assertIn('[data-testid="stAppViewContainer"]', self.ui_source)
        self.assertIn("position:fixed", self.ui_source)
        self.assertIn("min-height:100vh", self.ui_source)
        self.assertIn("Acesso ao <strong>APP FOS</strong>", self.ui_source)
        self.assertIn("Entre com suas credenciais para continuar", self.ui_source)

    def test_background_nao_bloqueia_widgets(self):
        self.assertIn("pointer-events:none", self.ui_source)
        self.assertIn("z-index:3", self.ui_source)
        self.assertIn(".block-container input", self.ui_source)
        self.assertIn(".stButton > button", self.ui_source)

    def test_responsivo_e_reduced_motion(self):
        self.assertIn("@media (max-width: 640px)", self.ui_source)
        self.assertIn("@media (max-height: 690px)", self.ui_source)
        self.assertIn("@media (prefers-reduced-motion: reduce)", self.ui_source)
        self.assertIn("animation:none !important", self.ui_source)


if __name__ == "__main__":
    unittest.main()
