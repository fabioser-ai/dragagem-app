import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestDadosSalariosUXPerf(unittest.TestCase):
    def setUp(self):
        self.fonte = (ROOT / "pages/dados_hub.py").read_text(encoding="utf-8")

    def test_salarios_tem_fluxo_segregado(self):
        self.assertIn("def _render_salarios(cfg):", self.fonte)
        self.assertIn('st.button("➕ Nova entrada"', self.fonte)
        self.assertIn('st.button("✏️ Atualizar dado existente"', self.fonte)
        self.assertIn('elif chave == "sal":\n        _render_salarios(cfg)', self.fonte)

    def test_atualizacao_seleciona_posicao_e_nao_indice(self):
        self.assertIn('st.selectbox("Posição", opcoes, key="sal_editar_posicao")', self.fonte)
        self.assertNotIn('st.selectbox("Selecionar registro", df.index, key="sal_editar_idx")', self.fonte)

    def test_moeda_ptbr_e_entrada_com_virgula(self):
        self.assertIn("def _formatar_brl(valor):", self.fonte)
        self.assertIn('return f"R$ {formatado}"', self.fonte)
        self.assertIn('placeholder="Ex.: 25,50"', self.fonte)
        self.assertIn('texto = texto.replace(".", "").replace(",", ".")', self.fonte)

    def test_salvar_salario_nao_forca_rerun_imediato(self):
        self.assertIn('def _salvar(df, cfg, leitura, acao, *, rerun=True):', self.fonte)
        self.assertIn('_salvar(candidato, cfg, leitura, "editar", rerun=False)', self.fonte)
        self.assertIn('_salvar(candidato, cfg, leitura, "criar", rerun=False)', self.fonte)


if __name__ == "__main__":
    unittest.main()
