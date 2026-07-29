import sys
import types
import unittest
from pathlib import Path

import pandas as pd


sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))

from services.uniformes_epis import (  # noqa: E402
    COLUNAS_COMPRAS,
    COLUNAS_ENTREGAS,
    COLUNAS_ITENS,
    COLUNAS_MOVIMENTACOES,
    cadastrar_item,
    calcular_estoque,
    calcular_posse_funcionarios,
    historico_funcionario,
    registrar_baixa,
    registrar_compra,
    registrar_devolucao,
    registrar_entrega,
)


ROOT = Path(__file__).resolve().parents[1]


class TestControleEntregasUniformesEpis(unittest.TestCase):
    def setUp(self):
        itens = pd.DataFrame(columns=COLUNAS_ITENS)
        self.itens = cadastrar_item(
            itens,
            categoria="Uniforme",
            nome="Camisa operacional",
            tamanho="M",
            unidade="un",
            item_id="ITEM_1",
            instante="2026-07-29T10:00:00",
        )
        compras = pd.DataFrame(columns=COLUNAS_COMPRAS)
        self.compras = registrar_compra(
            compras,
            self.itens,
            item_id="ITEM_1",
            data_compra="2026-07-20",
            fornecedor="Fornecedor",
            quantidade=10,
            valor_unitario=30,
            local_inicial="Almoxarifado Santos",
            compra_id="COMPRA_1",
            instante="2026-07-29T10:00:00",
        )
        self.movimentacoes = pd.DataFrame(
            columns=COLUNAS_MOVIMENTACOES
        )
        self.entregas = pd.DataFrame(columns=COLUNAS_ENTREGAS)

    def _estoque(self, entregas=None):
        return calcular_estoque(
            self.itens,
            self.compras,
            self.movimentacoes,
            self.entregas if entregas is None else entregas,
        )

    def _entregar(self, quantidade=4):
        return registrar_entrega(
            self.entregas,
            self.itens,
            self._estoque(),
            matricula="2175",
            funcionario="Fabio Pereira Serafini",
            item_id="ITEM_1",
            quantidade=quantidade,
            data_entrega="2026-07-29",
            local_estoque="Almoxarifado Santos",
            responsavel="Karina",
            evento_id="ENT_1",
            instante="2026-07-29T11:00:00",
        )

    def test_entrega_reduz_estoque_e_cria_posse_do_funcionario(self):
        entregas = self._entregar(4)
        estoque = self._estoque(entregas)
        posses = calcular_posse_funcionarios(self.itens, entregas)

        self.assertEqual(estoque.iloc[0]["quantidade"], 6)
        self.assertEqual(posses.iloc[0]["quantidade"], 4)
        self.assertEqual(posses.iloc[0]["matricula"], "2175")
        self.assertEqual(posses.iloc[0]["tamanho"], "M")

    def test_entrega_acima_do_estoque_e_rejeitada_antes_de_persistir(self):
        with self.assertRaisesRegex(ValueError, "Saldo insuficiente"):
            self._entregar(11)
        self.assertTrue(self.entregas.empty)

    def test_devolucao_parcial_retorna_ao_estoque(self):
        entregas = self._entregar(4)
        posses = calcular_posse_funcionarios(self.itens, entregas)
        entregas = registrar_devolucao(
            entregas,
            self.itens,
            posses,
            matricula="2175",
            funcionario="Fabio Pereira Serafini",
            item_id="ITEM_1",
            quantidade=2,
            data_devolucao="2026-07-30",
            local_estoque="Almoxarifado Santos",
            responsavel="Karina",
            evento_id="DEV_1",
            instante="2026-07-30T10:00:00",
        )

        estoque = self._estoque(entregas)
        posses = calcular_posse_funcionarios(self.itens, entregas)
        self.assertEqual(estoque.iloc[0]["quantidade"], 8)
        self.assertEqual(posses.iloc[0]["quantidade"], 2)

    def test_devolucao_superior_a_posse_e_rejeitada(self):
        entregas = self._entregar(2)
        posses = calcular_posse_funcionarios(self.itens, entregas)
        with self.assertRaisesRegex(ValueError, "superior à posse"):
            registrar_devolucao(
                entregas,
                self.itens,
                posses,
                matricula="2175",
                funcionario="Fabio Pereira Serafini",
                item_id="ITEM_1",
                quantidade=3,
                data_devolucao="2026-07-30",
                local_estoque="Almoxarifado Santos",
                responsavel="Karina",
            )

    def test_baixa_reduz_posse_sem_retornar_ao_estoque(self):
        entregas = self._entregar(4)
        posses = calcular_posse_funcionarios(self.itens, entregas)
        entregas = registrar_baixa(
            entregas,
            self.itens,
            posses,
            matricula="2175",
            funcionario="Fabio Pereira Serafini",
            item_id="ITEM_1",
            quantidade=3,
            data_baixa="2026-07-31",
            motivo="Dano",
            responsavel="Karina",
            evento_id="BAIXA_1",
            instante="2026-07-31T10:00:00",
        )

        estoque = self._estoque(entregas)
        posses = calcular_posse_funcionarios(self.itens, entregas)
        self.assertEqual(estoque.iloc[0]["quantidade"], 6)
        self.assertEqual(posses.iloc[0]["quantidade"], 1)

    def test_baixa_exige_motivo(self):
        entregas = self._entregar(1)
        posses = calcular_posse_funcionarios(self.itens, entregas)
        with self.assertRaisesRegex(ValueError, "motivo"):
            registrar_baixa(
                entregas,
                self.itens,
                posses,
                matricula="2175",
                funcionario="Fabio Pereira Serafini",
                item_id="ITEM_1",
                quantidade=1,
                data_baixa="2026-07-31",
                motivo="",
                responsavel="Karina",
            )

    def test_historico_mostra_entrega_devolucao_baixa_e_situacao(self):
        entregas = self._entregar(4)
        posses = calcular_posse_funcionarios(self.itens, entregas)
        entregas = registrar_devolucao(
            entregas,
            self.itens,
            posses,
            matricula="2175",
            funcionario="Fabio Pereira Serafini",
            item_id="ITEM_1",
            quantidade=1,
            data_devolucao="2026-07-30",
            local_estoque="Almoxarifado Santos",
            responsavel="Karina",
            evento_id="DEV_1",
            instante="2026-07-30T10:00:00",
        )
        posses = calcular_posse_funcionarios(self.itens, entregas)
        entregas = registrar_baixa(
            entregas,
            self.itens,
            posses,
            matricula="2175",
            funcionario="Fabio Pereira Serafini",
            item_id="ITEM_1",
            quantidade=1,
            data_baixa="2026-07-31",
            motivo="Extravio",
            responsavel="Karina",
            evento_id="BAIXA_1",
            instante="2026-07-31T10:00:00",
        )

        historico = historico_funcionario(
            entregas, self.itens, "2175"
        )
        self.assertEqual(
            historico["quantidade_entregue"].tolist(), [4, 0, 0]
        )
        self.assertEqual(
            historico["quantidade_devolvida"].tolist(), [0, 1, 0]
        )
        self.assertEqual(
            historico["quantidade_baixada"].tolist(), [0, 0, 1]
        )
        self.assertEqual(
            historico["situacao_apos_evento"].tolist(), [4, 3, 2]
        )

    def test_calculo_anterior_sem_entregas_permanece_compativel(self):
        anterior = calcular_estoque(
            self.itens, self.compras, self.movimentacoes
        )
        novo = self._estoque()
        pd.testing.assert_frame_equal(anterior, novo)

    def test_csv_e_telas_do_ciclo_estao_integrados(self):
        self.assertTrue(
            (ROOT / "data" / "uniformes_epis_entregas.csv").exists()
        )
        pagina = (ROOT / "pages" / "uniformes_epis.py").read_text(
            encoding="utf-8"
        )
        for texto in [
            '"Entregas"',
            '"Históricos"',
            '"Entrega"',
            '"Devolução"',
            '"Baixa"',
            "historico_funcionario",
        ]:
            self.assertIn(texto, pagina)


if __name__ == "__main__":
    unittest.main()
