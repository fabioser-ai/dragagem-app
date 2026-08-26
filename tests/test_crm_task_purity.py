import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestCRMTaskPurity(unittest.TestCase):
    def test_dispatch_separa_novo_consultar_e_atualizar(self):
        fonte = (ROOT / "pages/crm/crm.py").read_text(encoding="utf-8")
        self.assertIn('if fluxo == "novo":', fonte)
        self.assertIn('if fluxo == "consultar":', fonte)
        self.assertIn('if fluxo == "atualizar":', fonte)
        self.assertIn("novo_cliente()", fonte)
        self.assertIn("novo_contato()", fonte)
        self.assertIn("nova_interacao()", fonte)
        self.assertIn("consultar_clientes()", fonte)
        self.assertIn("consultar_contatos()", fonte)
        self.assertIn("consultar_interacoes()", fonte)
        self.assertIn("atualizar_cliente_tela()", fonte)
        self.assertIn("atualizar_contato_tela()", fonte)

    def test_novo_nao_renderiza_consulta_ou_edicao(self):
        fonte = (ROOT / "pages/crm/fluxos_tarefa.py").read_text(encoding="utf-8")
        bloco_novo_cliente = fonte.split("def novo_cliente():", 1)[1].split("def novo_contato():", 1)[0]
        bloco_novo_contato = fonte.split("def novo_contato():", 1)[1].split("def nova_interacao():", 1)[0]
        bloco_nova_interacao = fonte.split("def nova_interacao():", 1)[1].split("def consultar_clientes():", 1)[0]
        for bloco in (bloco_novo_cliente, bloco_novo_contato, bloco_nova_interacao):
            self.assertNotIn("Atualizar", bloco)
            self.assertNotIn("st.dataframe", bloco)

    def test_consulta_nao_persiste(self):
        fonte = (ROOT / "pages/crm/fluxos_tarefa.py").read_text(encoding="utf-8")
        bloco = fonte.split("def consultar_clientes():", 1)[1].split("def atualizar_cliente_tela():", 1)[0]
        self.assertIn("st.dataframe", bloco)
        self.assertNotIn("cadastrar_cliente(", bloco)
        self.assertNotIn("cadastrar_contato(", bloco)
        self.assertNotIn("atualizar_cliente(", bloco)
        self.assertNotIn("atualizar_contato(", bloco)

    def test_atualizar_nao_oferece_criacao(self):
        fonte = (ROOT / "pages/crm/fluxos_tarefa.py").read_text(encoding="utf-8")
        bloco = fonte.split("def atualizar_cliente_tela():", 1)[1]
        self.assertIn("atualizar_cliente(", bloco)
        self.assertIn("atualizar_contato(", bloco)
        self.assertNotIn("cadastrar_cliente(", bloco)
        self.assertNotIn("cadastrar_contato(", bloco)


if __name__ == "__main__":
    unittest.main()
