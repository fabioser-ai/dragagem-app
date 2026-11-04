"""Regressão da estrutura de itens da Etapa 2."""
import unittest

from modulos.composicao_orcamento.cotacoes_etapa2 import _novo_item, SEMENTES, COLUNAS


class TestCotacoesEtapa2(unittest.TestCase):
    def test_sementes_iniciais(self):
        self.assertEqual([item[0] for item in SEMENTES],
                         ["Guindaste", "Container", "Banheiro químico", "Destinação"])

    def test_item_livre_tem_identidade_propria(self):
        primeiro = _novo_item("  Tubo PEAD  ", " metro ", "Preço unitário")
        segundo = _novo_item("Tubo PEAD", "metro", "Preço unitário")
        self.assertNotEqual(primeiro["id"], segundo["id"])
        self.assertEqual(primeiro["nome"], "Tubo PEAD")
        self.assertEqual(primeiro["unidade"], "metro")
        self.assertEqual(primeiro["propostas"], [])
        self.assertIsNone(primeiro["catalogo_id"])

    def test_item_catalogado_preserva_referencia(self):
        item = _novo_item("Guindaste", "hora", "Preço por hora",
                          "Preço por diária", "catalogo", "inicial-0")
        self.assertEqual(item["catalogo_id"], "inicial-0")
        self.assertEqual(item["origem"], "catalogo")
        self.assertEqual(len(COLUNAS), 6)


if __name__ == "__main__":
    unittest.main()
