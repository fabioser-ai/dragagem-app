import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestCRMTaskLanding(unittest.TestCase):
    def test_landing_possui_tres_fluxos_principais(self):
        fonte = (ROOT / "pages/crm/navegacao.py").read_text(encoding="utf-8")
        for titulo in ("Novo contato", "Consultar", "Atualizar"):
            self.assertIn(titulo, fonte)
        self.assertIn('st.columns(3)', fonte)

    def test_atividades_sao_filtradas_por_permissao_canonica(self):
        fonte = (ROOT / "pages/crm/navegacao.py").read_text(encoding="utf-8")
        self.assertIn('pode(modulo="crm", recurso=opcao[2], acao=opcao[3])', fonte)
        for recurso in ("cliente", "contato", "interacao"):
            self.assertIn(f'"{recurso}"', fonte)

    def test_repositorio_usa_recursos_singulares_do_catalogo(self):
        fonte = (ROOT / "pages/crm/repositorio.py").read_text(encoding="utf-8")
        self.assertIn('recurso="cliente"', fonte)
        self.assertIn('recurso="contato"', fonte)
        self.assertIn('recurso="interacao"', fonte)
        self.assertNotIn('recurso="clientes"', fonte)
        self.assertNotIn('recurso="contatos"', fonte)
        self.assertNotIn('recurso="interacoes"', fonte)

    def test_saida_para_menu_limpa_estado_interno_crm(self):
        fonte = (ROOT / "pages/crm/crm.py").read_text(encoding="utf-8")
        self.assertIn("st.session_state.crm_fluxo = None", fonte)
        self.assertIn("st.session_state.crm_pagina = None", fonte)


if __name__ == "__main__":
    unittest.main()
