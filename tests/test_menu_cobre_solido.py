import unittest
from pathlib import Path


MENU = Path(__file__).resolve().parents[1] / "pages" / "menu.py"


class TestMenuCobreSolido(unittest.TestCase):
    def test_cabecalho_principal_usa_cobre_solido_e_moldura_preta(self):
        fonte = MENU.read_text(encoding="utf-8")
        bloco = fonte.split(".main-header {", 1)[1].split("}", 1)[0]

        self.assertIn("background: #c45d35;", bloco)
        self.assertIn("border: 2px solid #000000;", bloco)
        self.assertNotIn("linear-gradient", bloco)


if __name__ == "__main__":
    unittest.main()
