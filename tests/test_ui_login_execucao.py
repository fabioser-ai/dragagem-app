from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TestLoginFullscreenExecution(unittest.TestCase):
    def test_renderer_runs_on_every_app_execution_before_login_check(self):
        app_source = (ROOT / "app.py").read_text(encoding="utf-8")
        ui_source = (ROOT / "services" / "ui.py").read_text(encoding="utf-8")

        self.assertIn(
            "from services.ui import aplicar_estilo_global, _renderizar_marca_login",
            app_source,
        )

        page_config_pos = app_source.index("st.set_page_config")
        render_pos = app_source.index("_renderizar_marca_login()")
        login_pos = app_source.index("if not verificar_login():")

        self.assertLess(page_config_pos, render_pos)
        self.assertLess(render_pos, login_pos)

        definition_end = ui_source.index("\ndef aplicar_estilo_global")
        before_global_style = ui_source[:definition_end]
        self.assertEqual(before_global_style.count("_renderizar_marca_login()"), 1)


if __name__ == "__main__":
    unittest.main()
