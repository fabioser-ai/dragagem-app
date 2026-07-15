import unittest

from modulos.orcamentos.dominio.estados import EstadoCenario, EstadoVersao
from modulos.orcamentos.dominio.identidades import CenarioId, OrcamentoId, VersaoId
from modulos.orcamentos.dominio.modelos import Cenario, Orcamento, VersaoOrcamento


class TestNucleoDominioOrcamentos(unittest.TestCase):
    def criar_orcamento(self):
        return Orcamento(OrcamentoId.nova(), "Dragagem", "Proposta", "Fabio")

    def criar_versao(self, orcamento, numero=1, anterior=None):
        return VersaoOrcamento(
            VersaoId.nova(),
            orcamento.id,
            numero,
            "Fabio",
            versao_anterior_id=anterior,
        )

    def test_identidades_sao_unicas_e_validam_vazio(self):
        self.assertNotEqual(OrcamentoId.nova(), OrcamentoId.nova())
        with self.assertRaises(ValueError):
            OrcamentoId("  ")

    def test_propriedade_e_unicidade_de_versao(self):
        orcamento = self.criar_orcamento()
        versao = self.criar_versao(orcamento)
        self.assertTrue(orcamento.adicionar_versao(versao).sucesso)
        duplicada = VersaoOrcamento(VersaoId.nova(), orcamento.id, 1, "Outro")
        self.assertFalse(orcamento.adicionar_versao(duplicada).sucesso)
        estrangeira = VersaoOrcamento(
            VersaoId.nova(), OrcamentoId.nova(), 2, "Outro"
        )
        self.assertFalse(orcamento.adicionar_versao(estrangeira).sucesso)

    def test_cenario_fica_isolado_na_versao_proprietaria(self):
        orcamento = self.criar_orcamento()
        v1 = self.criar_versao(orcamento, 1)
        v2 = self.criar_versao(orcamento, 2)
        cenario = Cenario(CenarioId.nova(), v1.id, "Solução A")
        self.assertTrue(v1.adicionar_cenario(cenario).sucesso)
        self.assertFalse(v2.adicionar_cenario(cenario).sucesso)
        self.assertEqual(v2.cenarios, ())

    def test_transicao_elaboracao_congelada_aprovada(self):
        orcamento = self.criar_orcamento()
        versao = self.criar_versao(orcamento)
        cenario = Cenario(CenarioId.nova(), versao.id, "Solução A")
        versao.adicionar_cenario(cenario)
        versao.adotar_cenario(cenario.id)
        self.assertTrue(versao.congelar().sucesso)
        self.assertEqual(versao.estado, EstadoVersao.CONGELADA)
        self.assertTrue(versao.aprovar().sucesso)
        self.assertEqual(versao.estado, EstadoVersao.APROVADA)

    def test_transicoes_invalidas_sao_explicitas(self):
        orcamento = self.criar_orcamento()
        versao = self.criar_versao(orcamento)
        self.assertFalse(versao.congelar().sucesso)
        self.assertFalse(versao.aprovar().sucesso)
        cenario = Cenario(CenarioId.nova(), versao.id, "Solução A")
        versao.adicionar_cenario(cenario)
        self.assertTrue(cenario.descartar().sucesso)
        self.assertEqual(cenario.estado, EstadoCenario.DESCARTADO)
        self.assertFalse(versao.adotar_cenario(cenario.id).sucesso)

    def test_congelamento_impede_mutacao_estrutural(self):
        orcamento = self.criar_orcamento()
        versao = self.criar_versao(orcamento)
        cenario = Cenario(CenarioId.nova(), versao.id, "Solução A")
        versao.adicionar_cenario(cenario)
        versao.adotar_cenario(cenario.id)
        versao.congelar()
        novo = Cenario(CenarioId.nova(), versao.id, "Solução B")
        self.assertFalse(versao.adicionar_cenario(novo).sucesso)
        self.assertFalse(versao.adotar_cenario(cenario.id).sucesso)

    def test_cliente_nao_participa_do_nucleo_tecnico(self):
        campos = set(Orcamento.__dataclass_fields__)
        campos |= set(VersaoOrcamento.__dataclass_fields__)
        campos |= set(Cenario.__dataclass_fields__)
        proibidos = {
            "cliente",
            "tecnologia",
            "familia",
            "pacotes",
            "equipamentos",
            "formulas",
        }
        self.assertTrue(campos.isdisjoint(proibidos))


if __name__ == "__main__":
    unittest.main()
