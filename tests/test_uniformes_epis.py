import sys
import types
import unittest
from pathlib import Path

import pandas as pd


sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))

from services.uniformes_epis import (  # noqa: E402
    COLUNAS_COMPRAS,
    COLUNAS_ITENS,
    COLUNAS_MOVIMENTACOES,
    cadastrar_item,
    calcular_estoque,
    registrar_compra,
    registrar_movimentacao,
)


ROOT = Path(__file__).resolve().parents[1]


class TestUniformesEpis(unittest.TestCase):
    def setUp(self):
        self.itens = pd.DataFrame(columns=COLUNAS_ITENS)
        self.compras = pd.DataFrame(columns=COLUNAS_COMPRAS)
        self.movimentacoes = pd.DataFrame(columns=COLUNAS_MOVIMENTACOES)
        self.itens = cadastrar_item(
            self.itens,
            categoria="EPI",
            nome="Capacete",
            ca="12345",
            unidade="un",
            item_id="ITEM_1",
            instante="2026-07-29T10:00:00",
        )

    def test_cadastra_item_com_identidade_estavel(self):
        item = self.itens.iloc[0]
        self.assertEqual(item["item_id"], "ITEM_1")
        self.assertEqual(item["categoria"], "EPI")
        self.assertEqual(item["ativo"], "sim")

    def test_impede_item_ativo_duplicado(self):
        with self.assertRaisesRegex(ValueError, "Já existe"):
            cadastrar_item(
                self.itens,
                categoria="EPI",
                nome=" capacete ",
                ca="12345",
                unidade="un",
            )

    def test_compra_cria_saldo_na_localizacao_inicial(self):
        compras = registrar_compra(
            self.compras,
            self.itens,
            item_id="ITEM_1",
            data_compra="2026-07-20",
            fornecedor="Fornecedor",
            quantidade=10,
            valor_unitario=25.5,
            local_inicial="Almoxarifado Santos",
            compra_id="COMPRA_1",
            instante="2026-07-29T10:00:00",
        )
        estoque = calcular_estoque(self.itens, compras, self.movimentacoes)
        self.assertEqual(estoque.iloc[0]["quantidade"], 10)
        self.assertEqual(
            estoque.iloc[0]["localizacao"], "Almoxarifado Santos"
        )

    def test_movimentacao_transfere_saldo_sem_apagar_historico(self):
        compras = registrar_compra(
            self.compras,
            self.itens,
            item_id="ITEM_1",
            data_compra="2026-07-20",
            fornecedor="Fornecedor",
            quantidade=10,
            valor_unitario=25.5,
            local_inicial="Almoxarifado Santos",
        )
        estoque = calcular_estoque(self.itens, compras, self.movimentacoes)
        movimentos = registrar_movimentacao(
            self.movimentacoes,
            estoque,
            item_id="ITEM_1",
            data_movimentacao="2026-07-29",
            quantidade=4,
            local_origem="Almoxarifado Santos",
            local_destino="Obra Cubatão",
            obra_destino_id="OBRA_01",
            movimentacao_id="MOV_1",
            instante="2026-07-29T10:00:00",
        )
        atualizado = calcular_estoque(self.itens, compras, movimentos)
        saldos = {
            (linha["localizacao"], linha["obra_id"]): linha["quantidade"]
            for _, linha in atualizado.iterrows()
        }
        self.assertEqual(saldos[("Almoxarifado Santos", "")], 6)
        self.assertEqual(saldos[("Obra Cubatão", "OBRA_01")], 4)
        self.assertEqual(len(movimentos), 1)

    def test_bloqueia_movimentacao_acima_do_saldo(self):
        compras = registrar_compra(
            self.compras,
            self.itens,
            item_id="ITEM_1",
            data_compra="2026-07-20",
            fornecedor="Fornecedor",
            quantidade=2,
            valor_unitario=25.5,
            local_inicial="Almoxarifado",
        )
        estoque = calcular_estoque(self.itens, compras, self.movimentacoes)
        with self.assertRaisesRegex(ValueError, "Saldo insuficiente"):
            registrar_movimentacao(
                self.movimentacoes,
                estoque,
                item_id="ITEM_1",
                data_movimentacao="2026-07-29",
                quantidade=3,
                local_origem="Almoxarifado",
                local_destino="Obra",
            )

    def test_bloqueia_origem_igual_ao_destino(self):
        compras = registrar_compra(
            self.compras,
            self.itens,
            item_id="ITEM_1",
            data_compra="2026-07-20",
            fornecedor="Fornecedor",
            quantidade=2,
            valor_unitario=25.5,
            local_inicial="Almoxarifado",
        )
        estoque = calcular_estoque(self.itens, compras, self.movimentacoes)
        with self.assertRaisesRegex(ValueError, "devem ser diferentes"):
            registrar_movimentacao(
                self.movimentacoes,
                estoque,
                item_id="ITEM_1",
                data_movimentacao="2026-07-29",
                quantidade=1,
                local_origem="Almoxarifado",
                local_destino="Almoxarifado",
            )

    def test_modulo_integrado_com_rota_menu_permissao_e_tres_csvs(self):
        app = (ROOT / "app.py").read_text(encoding="utf-8")
        menu = (ROOT / "pages" / "menu.py").read_text(encoding="utf-8")
        pagina = (ROOT / "pages" / "uniformes_epis.py").read_text(
            encoding="utf-8"
        )
        self.assertIn('tela == "uniformes_epis"', app)
        self.assertIn('pode_acessar_modulo("uniformes_epis")', menu)
        self.assertIn('pode_acessar_modulo("uniformes_epis")', pagina)
        for arquivo in [
            "uniformes_epis_itens.csv",
            "uniformes_epis_compras.csv",
            "uniformes_epis_movimentacoes.csv",
        ]:
            self.assertTrue((ROOT / "data" / arquivo).exists())

    def test_telas_existentes_permanecem_roteadas(self):
        app = (ROOT / "app.py").read_text(encoding="utf-8")
        for rota in [
            "dados",
            "ferias",
            "prestacao_contas",
            "medicoes",
            "crm",
            "novo_orcamento",
            "orcamento",
        ]:
            self.assertIn(f'"{rota}"', app)


if __name__ == "__main__":
    unittest.main()
