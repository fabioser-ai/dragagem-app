from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MENU = ROOT / "pages" / "menu.py"
UI = ROOT / "services" / "ui.py"


class MenuPaletaCobreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = MENU.read_text(encoding="utf-8")
        cls.ui_source = UI.read_text(encoding="utf-8")

    def test_header_usa_cobre_solido_com_moldura_preta(self):
        self.assertIn("background: #c45d35", self.source)
        self.assertIn("border: 2px solid #000000", self.source)
        self.assertNotIn(
            "linear-gradient(135deg, #0f172a 0%, #8f4229 58%, #c45d35 100%)",
            self.source,
        )

    def test_botoes_do_menu_usam_cobre_sem_azul_de_destaque(self):
        self.assertIn("linear-gradient(135deg, #c45d35 0%, #ab4527 100%)", self.source)
        self.assertNotIn("#2c5282", self.source)
        self.assertNotIn("#3b82f6", self.source)

    def test_estilo_global_replica_cobre_em_botoes_tabelas_tabs_e_foco(self):
        self.assertIn("--fos-copper: #c45d35", self.ui_source)
        self.assertIn("--fos-copper-dark: #ab4527", self.ui_source)
        self.assertIn("background-color: var(--fos-copper) !important", self.ui_source)
        self.assertIn("background-color: var(--fos-copper-dark) !important", self.ui_source)
        self.assertIn("border-color: var(--fos-copper) !important", self.ui_source)
        self.assertIn("color: var(--fos-copper-dark) !important", self.ui_source)
        self.assertNotIn("background-color: #1e3a5f !important", self.ui_source)
        self.assertNotIn("background-color: #2c5282 !important", self.ui_source)

    def test_neutros_globais_sao_preservados(self):
        self.assertIn("#0f172a", self.ui_source)
        self.assertIn("#334155", self.ui_source)
        self.assertIn("#cbd5e1", self.ui_source)
        self.assertIn("#f1f5f9", self.ui_source)
        self.assertIn("#64748b", self.source)


if __name__ == "__main__":
    unittest.main()
