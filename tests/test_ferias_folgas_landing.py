import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestFeriasFolgasLanding(unittest.TestCase):
    def test_menu_principal_exibe_nome_completo(self):
        fonte = (ROOT / "pages/menu.py").read_text(encoding="utf-8")
        self.assertIn('"Férias e Folgas"', fonte)
        self.assertIn('"ABRIR FÉRIAS E FOLGAS"', fonte)

    def test_app_roteia_ferias_para_hub(self):
        fonte = (ROOT / "app.py").read_text(encoding="utf-8")
        self.assertIn("from pages import ferias_hub", fonte)
        self.assertIn("ferias_hub.render()", fonte)

    def test_landing_tem_duas_areas_claras(self):
        fonte = (ROOT / "pages/ferias_hub.py").read_text(encoding="utf-8")
        self.assertIn('"Férias"', fonte)
        self.assertIn('"Folgas"', fonte)
        self.assertIn('"ABRIR FÉRIAS"', fonte)
        self.assertIn('"ABRIR FOLGAS"', fonte)

    def test_cards_dependem_de_visualizacao_por_recurso(self):
        fonte = (ROOT / "pages/ferias_hub.py").read_text(encoding="utf-8")
        self.assertIn('_pode_visualizar("ferias")', fonte)
        self.assertIn('_pode_visualizar("folga")', fonte)
        self.assertIn('pode(modulo="ferias", recurso=recurso, acao="visualizar")', fonte)

    def test_fluxos_reutilizam_regras_legadas_sem_duplicar_motor(self):
        fonte = (ROOT / "pages/ferias_hub.py").read_text(encoding="utf-8")
        self.assertIn("legado.render_ferias", fonte)
        self.assertIn("legado.render_folgas", fonte)
        self.assertNotIn("def validar_registro_ferias", fonte)
        self.assertNotIn("def existe_sobreposicao_folga", fonte)


if __name__ == "__main__":
    unittest.main()
