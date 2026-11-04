"""Permissão de consulta restrita ao orçamento, sem acesso geral a CRM/Dados."""
import unittest
from unittest.mock import patch

from services import autorizacao


class TestComposicaoAutorizacao(unittest.TestCase):
    def test_consulta_fonte_exige_acesso_ao_orcamento(self):
        with patch.object(autorizacao, "pode_acessar", side_effect=lambda modulo: modulo == "orcamento"):
            self.assertTrue(autorizacao.pode_consultar_fonte_composicao("clientes"))
            self.assertTrue(autorizacao.pode_consultar_fonte_composicao("materiais"))
            self.assertFalse(autorizacao.pode_consultar_fonte_composicao("salarios"))
            self.assertFalse(autorizacao.pode_consultar_fonte_composicao("interacoes"))

    def test_consulta_fonte_nega_sem_orcamento(self):
        with patch.object(autorizacao, "pode_acessar", return_value=False):
            for fonte in ("clientes", "contatos", "materiais", "horarios", "regimes"):
                with self.subTest(fonte=fonte):
                    self.assertFalse(autorizacao.pode_consultar_fonte_composicao(fonte))


if __name__ == "__main__":
    unittest.main()
