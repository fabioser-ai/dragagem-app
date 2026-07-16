import base64
import unittest
from unittest.mock import patch

from modulos.orcamentos.aplicacao.premissas import (
    RascunhoPremissa,
    aplicar_rascunho,
    atualizar_identificacao,
)
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.identidades import CenarioId, OrcamentoId, VersaoId
from modulos.orcamentos.dominio.modelos import Cenario, Orcamento, VersaoOrcamento
from modulos.orcamentos.dominio.premissas import OrigemPremissa
from modulos.orcamentos.persistencia.contratos import StatusPersistencia
from modulos.orcamentos.persistencia.github_repositorio import RepositorioOrcamentosGitHub
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao


class Resposta:
    def __init__(self, status_code, payload=None):
        self.status_code = status_code
        self._payload = payload or {}

    def json(self):
        return self._payload


def criar_contexto():
    orcamento = Orcamento(OrcamentoId("orc-1"), "Dragagem", "Proposta", "Fabio")
    versao = VersaoOrcamento(VersaoId("ver-1"), orcamento.id, 1, "Fabio")
    cenario = Cenario(CenarioId("cen-1"), versao.id, "Alternativa principal")
    versao.adicionar_cenario(cenario)
    orcamento.adicionar_versao(versao)
    return orcamento, versao, cenario


class TestPremissas(unittest.TestCase):
    def test_sugestao_pode_ficar_pendente(self):
        _, versao, cenario = criar_contexto()
        resultado = aplicar_rascunho(
            versao,
            cenario.id,
            RascunhoPremissa("Volume", "m³", "Fabio", valor_sugerido="1000"),
        )
        self.assertTrue(resultado.sucesso)
        self.assertTrue(resultado.valor.pendente)
        self.assertEqual(resultado.valor.sugerido.origem, OrigemPremissa.SUGESTAO)

    def test_manual_exige_justificativa(self):
        _, versao, cenario = criar_contexto()
        resultado = aplicar_rascunho(
            versao,
            cenario.id,
            RascunhoPremissa(
                "Volume", "m³", "Fabio", valor_adotado="1200",
                origem_adotada=OrigemPremissa.MANUAL,
            ),
        )
        self.assertFalse(resultado.sucesso)
        self.assertEqual(versao.premissas, ())

    def test_nova_sugestao_nao_substitui_adotado(self):
        _, versao, cenario = criar_contexto()
        primeiro = RascunhoPremissa(
            "Volume", "m³", "Fabio", valor_sugerido="1000", valor_adotado="1100"
        )
        segundo = RascunhoPremissa("Volume", "m³", "Fabio", valor_sugerido="1050")
        self.assertTrue(aplicar_rascunho(versao, cenario.id, primeiro).sucesso)
        self.assertTrue(aplicar_rascunho(versao, cenario.id, segundo).sucesso)
        historico = versao.historico_premissa(cenario.id, "Volume")
        self.assertEqual(len(historico), 2)
        self.assertEqual(historico[-1].adotado.valor, "1100")
        self.assertEqual(historico[-1].sugerido.valor, "1050")

    def test_versao_congelada_recusa_premissa(self):
        _, versao, cenario = criar_contexto()
        versao.congelar()
        resultado = aplicar_rascunho(
            versao, cenario.id,
            RascunhoPremissa("Volume", "m³", "Fabio", valor_adotado="1000"),
        )
        self.assertFalse(resultado.sucesso)

    def test_identificacao_exige_versao_editavel(self):
        orcamento, versao, _ = criar_contexto()
        versao.congelar()
        resultado = atualizar_identificacao(
            orcamento, versao,
            objeto="Novo", finalidade="Proposta", responsavel="Fabio",
        )
        self.assertFalse(resultado.sucesso)
        self.assertEqual(orcamento.objeto, "Dragagem")

    def test_round_trip_preserva_historico(self):
        orcamento, versao, cenario = criar_contexto()
        aplicar_rascunho(
            versao, cenario.id,
            RascunhoPremissa(
                "Teor de sólidos", "%", "Fabio", valor_sugerido="20",
                valor_adotado="22", origem_adotada=OrigemPremissa.ENGENHARIA,
                vigencia="2026-07", justificativa="Amostra mais recente",
            ),
        )
        resultado = desserializar_versao(serializar_versao(orcamento, versao))
        self.assertTrue(resultado.sucesso)
        _, carregada = resultado.valor
        historico = carregada.historico_premissa(cenario.id, "Teor de sólidos")
        self.assertEqual(len(historico), 1)
        self.assertEqual(historico[0].adotado.valor, "22")
        self.assertEqual(historico[0].adotado.vigencia, "2026-07")

    def test_schema_legado_sem_premissas_continua_legivel(self):
        orcamento, versao, _ = criar_contexto()
        import json
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 1
        documento["versao"].pop("premissas")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(resultado.valor[1].premissas, ())


class TestSnapshotEdicao(unittest.TestCase):
    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_snapshot_e_capturado_em_uma_requisicao(self, get):
        get.return_value = Resposta(200, {"object": {"sha": "commit-atual"}})
        resultado = RepositorioOrcamentosGitHub("token", "org/repo").carregar_snapshot()
        self.assertTrue(resultado.sucesso)
        self.assertEqual(resultado.valor, "commit-atual")
        get.assert_called_once()

    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_indice_inexistente_vira_indice_vazio_no_salvamento(self, get):
        get.return_value = Resposta(404)
        resultado = RepositorioOrcamentosGitHub("token", "org/repo").carregar_indice_bruto()
        self.assertEqual(resultado.status, StatusPersistencia.SUCESSO)
        self.assertIn("orcamento_id", resultado.valor)


if __name__ == "__main__":
    unittest.main()
