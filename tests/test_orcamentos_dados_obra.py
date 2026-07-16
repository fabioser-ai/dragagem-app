import json
import unittest
from dataclasses import asdict
from datetime import date

from modulos.orcamentos.aplicacao.dados_obra import salvar_dados_obra
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.identidades import CenarioId, OrcamentoId, VersaoId
from modulos.orcamentos.dominio.modelos import Cenario, Orcamento, VersaoOrcamento
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao


def contexto():
    orcamento = Orcamento(OrcamentoId("orc-1"), "Dragagem", "Proposta", "Fabio")
    versao = VersaoOrcamento(VersaoId("ver-1"), orcamento.id, 1, "Fabio")
    versao.adicionar_cenario(Cenario(CenarioId("cen-1"), versao.id, "Principal"))
    orcamento.adicionar_versao(versao)
    return orcamento, versao


class TestEquivalenciaDadosObra(unittest.TestCase):
    def test_modelo_inicial_reproduz_celulas_do_excel(self):
        dados = DadosObra()
        self.assertEqual(dados.proposta, "Proposta D_055_2021")
        self.assertEqual(dados.data, date(2021, 5, 28))
        self.assertEqual(dados.cliente, "SABESP - CUBATAO ETA 3")
        self.assertEqual(dados.objeto, "Dragagem ETEL ETA3")
        self.assertEqual(dados.volume_dragagem, 5000.0)
        self.assertEqual(dados.tipo_material, "Areia + Lodo + Antracito")
        self.assertEqual(dados.tipo_bota_fora, "Bag")
        self.assertEqual(dados.sistema_medicao, "preços unitários de serviços")
        self.assertEqual(dados.horario_trabalho, 9.0)
        self.assertEqual(dados.dias_trabalho, 22.0)

    def test_h16_soma_distancia_e_seio(self):
        dados = DadosObra(distancia_recalque=210.5, seio_recalque=9.5)
        self.assertEqual(dados.total_recalque, 220.0)

    def test_h17_soma_linha_flutuante_e_seio(self):
        dados = DadosObra(linha_flutuante=100.0, seio_linha_flutuante=12.25)
        self.assertEqual(dados.total_linha_flutuante, 112.25)

    def test_g21_multiplica_dimensoes_e_espessura(self):
        dados = DadosObra(area_comprimento=25.0, area_largura=8.0, espessura_media=1.5)
        self.assertEqual(dados.volume_geometrico, 300.0)

    def test_celulas_vazias_produzem_zero_nas_formulas(self):
        dados = DadosObra(
            distancia_recalque=None,
            seio_recalque=None,
            linha_flutuante=None,
            seio_linha_flutuante=None,
        )
        self.assertEqual(dados.total_recalque, 0.0)
        self.assertEqual(dados.total_linha_flutuante, 0.0)
        self.assertEqual(dados.volume_geometrico, 0.0)

    def test_round_trip_preserva_todos_os_campos(self):
        orcamento, versao = contexto()
        dados = DadosObra(
            proposta="Proposta D_004_2026",
            data=date(2026, 7, 16),
            cliente="Cliente teste",
            contato="Maria",
            email="maria@example.com",
            objeto="Objeto teste",
            local="Local teste",
            volume_dragagem=1234.5,
            tipo_material="Material teste",
            distancia_recalque=250.0,
            seio_recalque=12.0,
            linha_flutuante=140.0,
            seio_linha_flutuante=7.0,
            linha_terra=110.0,
            profundidade_dragagem=4.2,
            espessura_media=1.1,
            area_comprimento=30.0,
            area_largura=12.0,
            tipo_bota_fora="Bag teste",
            sistema_medicao="Medição teste",
            canteiro_obras="Cliente",
            mobilizacao="FOS teste",
            horario_trabalho=8.5,
            dias_trabalho=20.0,
        )
        self.assertTrue(salvar_dados_obra(versao, dados).sucesso)
        resultado = desserializar_versao(serializar_versao(orcamento, versao))
        self.assertTrue(resultado.sucesso)
        _, carregada = resultado.valor
        self.assertEqual(asdict(carregada.dados_obra), asdict(dados))

    def test_documento_rejeita_dados_obra_incompletos(self):
        orcamento, versao = contexto()
        salvar_dados_obra(versao, DadosObra())
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["dados_obra"].pop("cliente")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertFalse(resultado.sucesso)

    def test_versao_congelada_nao_pode_salvar(self):
        _, versao = contexto()
        versao.congelar()
        resultado = salvar_dados_obra(versao, DadosObra())
        self.assertFalse(resultado.sucesso)
        self.assertIsNone(versao.dados_obra)


class TestTelaDadosObra(unittest.TestCase):
    def test_tela_contem_todos_os_rotulos_e_so_tres_resultados(self):
        from pathlib import Path

        fonte = (
            Path(__file__).resolve().parents[1]
            / "modulos/orcamentos/apresentacao/dados_obra.py"
        ).read_text(encoding="utf-8")
        rotulos = (
            "Proposta", "Data", "Cliente", "Contato", "e-mail", "Objeto", "Local",
            "Volume dragagem (m³)", "Tipo de material", "Distância de Recalque (m)",
            "Linha Flutuante (m)", "Linha de terra (m)",
            "Profundidade de dragagem (m)", "Espessura média de dragagem (m)",
            "Área de Dragagem (m² ou L x C)", "Tipo de Bota Fora",
            "Sistema de Medição", "Canteiro de obras", "Mobilização",
            "Horário de Trabalho  (das 7 as 17h)", "Dias de Trabalho (2ª a 6ª)",
        )
        for rotulo in rotulos:
            with self.subTest(rotulo=rotulo):
                self.assertIn(rotulo, fonte)
        for aba_proibida in ("Produção", "Bags", "Planta", "BDI", "Planilha Final"):
            self.assertNotIn(aba_proibida, fonte)


if __name__ == "__main__":
    unittest.main()
