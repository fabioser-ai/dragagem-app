import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestDadosSalariosOrdemAZ(unittest.TestCase):
    def test_salarios_tem_ordenacao_alfabetica_canonica(self):
        fonte = (ROOT / "pages/dados_hub.py").read_text(encoding="utf-8")
        self.assertIn("def _ordenar_salarios(df):", fonte)
        self.assertIn("str.casefold()", fonte)
        self.assertIn('exibicao = _ordenar_salarios(df)', fonte)
        self.assertIn('opcoes = [str(v) for v in _ordenar_salarios(df)["Posicao"].tolist()]', fonte)

    def test_criacao_e_edicao_persistem_ordenadas(self):
        fonte = (ROOT / "pages/dados_hub.py").read_text(encoding="utf-8")
        self.assertGreaterEqual(fonte.count("candidato = _ordenar_salarios(candidato)"), 2)


if __name__ == "__main__":
    unittest.main()
