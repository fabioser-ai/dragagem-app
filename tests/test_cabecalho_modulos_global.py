from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def fonte(caminho):
    return (ROOT / caminho).read_text(encoding="utf-8")


class CabecalhoModulosGlobalTests(unittest.TestCase):
    def test_dados_usa_titulo_contextual_do_recurso(self):
        dados = fonte("pages/dados_hub.py")
        self.assertIn('renderizar_cabecalho_modulo(cfg["titulo"]', dados)
        self.assertIn('"← DADOS"', dados)
        self.assertNotIn('renderizar_cabecalho_modulo("Dados", "← DADOS"', dados)

    def test_ferias_padroniza_raiz_e_subfluxos(self):
        ferias = fonte("pages/ferias_hub.py")
        self.assertGreaterEqual(ferias.count("renderizar_cabecalho_modulo("), 3)
        self.assertIn('"Férias e Folgas"', ferias)
        self.assertIn('"Férias"', ferias)
        self.assertIn('"Folgas"', ferias)
        self.assertNotIn('st.title("Férias e Folgas")', ferias)

    def test_crm_usa_titulo_contextual_conforme_fluxo_e_pagina(self):
        crm = fonte("pages/crm/crm.py")
        self.assertIn("renderizar_cabecalho_modulo", crm)
        self.assertIn("titulo_cabecalho", crm)
        self.assertIn('"← CRM"', crm)
        self.assertIn('"← TELA INICIAL"', crm)
        self.assertNotIn('st.title("CRM FOS")', crm)

    def test_modulos_principais_usam_componente_padrao(self):
        arquivos = {
            "pages/prestacao_contas_hub.py": "Prestação de Contas",
            "pages/medicoes.py": "Medições",
            "pages/uniformes_epis_hub.py": "Uniformes e EPIs",
            "pages/administracao_hub.py": "Administração",
            "pages/orcamento/dashboard.py": "Orçamentos",
        }
        for caminho, titulo in arquivos.items():
            with self.subTest(caminho=caminho):
                src = fonte(caminho)
                self.assertIn("renderizar_cabecalho_modulo", src)
                self.assertIn(titulo, src)

    def test_app_roteia_modulos_grandes_pelos_hubs(self):
        app = fonte("app.py")
        self.assertIn("from pages import administracao_hub", app)
        self.assertIn("from pages import prestacao_contas_hub", app)
        self.assertIn("from pages import uniformes_epis_hub", app)


if __name__ == "__main__":
    unittest.main()
