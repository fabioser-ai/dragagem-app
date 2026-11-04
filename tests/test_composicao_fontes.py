"""Testes isolados, sem acesso ao GitHub operacional (unittest oficial)."""
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import pandas as pd

from services import composicao_fontes as fontes
from services.github import StatusLeitura


def _resposta(status, dados=None, erro=None):
    return SimpleNamespace(status=status, dados=dados, erro=erro, sha="sha-teste")


class TestComposicaoFontes(unittest.TestCase):
    def test_cliente_oficial_e_crm(self):
        chamados = []

        def ler(arquivo, token, repo):
            chamados.append(arquivo)
            return _resposta(
                StatusLeitura.SUCESSO_COM_DADOS,
                pd.DataFrame([{"id_cliente": "c1", "nome_empresa": "Empresa"}]),
            )

        with patch.object(fontes, "ler_csv_operacional", side_effect=ler):
            resultado = fontes.consultar_catalogo("clientes", "token", "repo")
        self.assertFalse(resultado.disponivel)
        self.assertIn("Colunas obrigatórias", resultado.erro)
        self.assertEqual(chamados, ["data/crm/clientes.csv"])

    def test_indisponibilidade_nao_equivale_a_vazio(self):
        with patch.object(fontes, "ler_csv_operacional",
                          return_value=_resposta(StatusLeitura.ARQUIVO_INEXISTENTE)):
            resultado = fontes.consultar_catalogo("materiais", "token", "repo")
        self.assertFalse(resultado.disponivel)
        self.assertTrue(resultado.dados.empty)
        with self.assertRaises(ValueError):
            fontes.listar_opcoes(resultado, "Material")

    def test_catalogo_valido_e_opcoes(self):
        dados = pd.DataFrame({
            "Material": ["Areia", " Argila ", "Areia"],
            "Solidos_InSitu": ["10", "20", "10"],
            "Solidos_Desaguado": ["15", "25", "15"],
        })
        with patch.object(fontes, "ler_csv_operacional",
                          return_value=_resposta(StatusLeitura.SUCESSO_COM_DADOS, dados)):
            resultado = fontes.consultar_catalogo("materiais", "token", "repo")
        self.assertTrue(resultado.disponivel)
        self.assertEqual(fontes.listar_opcoes(resultado, "Material"), ["Areia", "Argila"])

    def test_contatos_somente_do_cliente_escolhido(self):
        clientes = fontes.LeituraCatalogo(
            "clientes", "a", True, pd.DataFrame({"id_cliente": ["1", "2"]}), "sucesso"
        )
        contatos = fontes.LeituraCatalogo(
            "contatos", "b", True,
            pd.DataFrame({"id_cliente": ["1", "2", "1"], "id_contato": ["a", "b", "c"]}),
            "sucesso",
        )
        encontrados = fontes.contatos_do_cliente(clientes, contatos, "1")
        self.assertEqual(encontrados["id_contato"].tolist(), ["a", "c"])
        with self.assertRaises(ValueError):
            fontes.contatos_do_cliente(clientes, contatos, "inexistente")

    def test_fonte_desconhecida_rejeitada(self):
        with self.assertRaises(ValueError):
            fontes.consultar_catalogo("clientes_legado", "token", "repo")


if __name__ == "__main__":
    unittest.main()
