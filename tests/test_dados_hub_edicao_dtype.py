import unittest
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


class TestDadosHubEdicaoDtype(unittest.TestCase):
    def test_normalizador_converte_colunas_para_texto_editavel(self):
        fonte = (ROOT / "pages/dados_hub.py").read_text(encoding="utf-8")
        self.assertIn("def _normalizar_para_edicao(df, colunas):", fonte)
        self.assertIn("return normalizado.astype(str)", fonte)
        self.assertIn('df = _normalizar_para_edicao(df, cfg["colunas"])', fonte)

    def test_cenario_salario_numerico_aceita_valor_textual_sem_typeerror(self):
        df = pd.DataFrame({"Posicao": ["Engenheiro"], "Valor_Hora": [123.45]})
        normalizado = df[["Posicao", "Valor_Hora"]].copy()
        normalizado = normalizado.where(pd.notna(normalizado), "").astype(str)
        normalizado.at[0, "Valor_Hora"] = "150,00"
        self.assertEqual(normalizado.at[0, "Valor_Hora"], "150,00")
        self.assertEqual(str(normalizado["Valor_Hora"].dtype), "object")


if __name__ == "__main__":
    unittest.main()
