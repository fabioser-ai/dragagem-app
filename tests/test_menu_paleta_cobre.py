from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MENU = ROOT / "pages" / "menu.py"


class MenuPaletaCobreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = MENU.read_text(encoding="utf-8")

    def test_header_usa_paleta_cobre_fos(self):
        self.assertIn("#c45d35", self.source)
        self.assertIn("#ab4527", self.source)
        self.assertNotIn("#1e3a5f", self.source)

    def test_botoes_usam_cobre_sem_azul_de_destaque(self):
        self.assertIn("linear-gradient(135deg, #c45d35 0%, #ab4527 100%)", self.source)
        self.assertNotIn("#2c5282", self.source)
        self.assertNotIn("#3b82f6", self.source)

    def test_neutros_do_menu_sao_preservados(self):
        self.assertIn("#0f172a", self.source)
        self.assertIn("#334155", self.source)
        self.assertIn("#64748b", self.source)
        self.assertIn("#cbd5e1", self.source)


if __name__ == "__main__":
    unittest.main()
