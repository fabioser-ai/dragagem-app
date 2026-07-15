import base64
import json
import unittest
from unittest.mock import Mock, patch

from modulos.orcamentos.dominio.estados import EstadoCenario, EstadoVersao
from modulos.orcamentos.dominio.identidades import CenarioId, OrcamentoId, VersaoId
from modulos.orcamentos.dominio.modelos import Cenario, Orcamento, VersaoOrcamento
from modulos.orcamentos.persistencia.contratos import StatusPersistencia
from modulos.orcamentos.persistencia.github_repositorio import (
    CAMINHO_INDICE, RepositorioOrcamentosGitHub, caminho_versao,
)
from modulos.orcamentos.persistencia.indice import (
    CAMPOS_INDICE, desserializar_indice, serializar_indice,
)
from modulos.orcamentos.persistencia.serializacao import (
    desserializar_versao, serializar_versao,
)
from services.persistencia_multi_arquivo import (
    ResultadoPersistenciaMultiArquivo, StatusPersistenciaMultiArquivo,
)


class Resposta:
    def __init__(self, status_code, payload=None):
        self.status_code = status_code
        self._payload = payload or {}

    def json(self):
        return self._payload


def criar_dominio(estado=EstadoVersao.ELABORACAO):
    orcamento = Orcamento(OrcamentoId("orc-1"), "Dragagem", "Proposta", "Fabio")
    versao = VersaoOrcamento(
        VersaoId("ver-1"), orcamento.id, 2, "Autor",
        versao_anterior_id=VersaoId("ver-0"),
    )
    ativo = Cenario(CenarioId("cen-1"), versao.id, "Alternativa A")
    descartado = Cenario(
        CenarioId("cen-2"), versao.id, "Alternativa B", EstadoCenario.DESCARTADO
    )
    versao.adicionar_cenario(ativo)
    versao.adicionar_cenario(descartado)
    versao.adotar_cenario(ativo.id)
    if estado is EstadoVersao.CONGELADA:
        versao.congelar()
    elif estado is EstadoVersao.APROVADA:
        versao.congelar()
        versao.aprovar()
    orcamento._versoes[versao.id] = versao
    return orcamento, versao


class TestSerializacaoOrcamentos(unittest.TestCase):
    def test_round_trip_preserva_todo_nucleo_homologado(self):
        original_o, original_v = criar_dominio(EstadoVersao.APROVADA)
        resultado = desserializar_versao(serializar_versao(original_o, original_v))
        self.assertTrue(resultado.sucesso)
        orcamento, versao = resultado.valor
        self.assertEqual(orcamento.id, original_o.id)
        self.assertEqual((orcamento.objeto, orcamento.finalidade, orcamento.responsavel),
                         (original_o.objeto, original_o.finalidade, original_o.responsavel))
        self.assertEqual(versao.id, original_v.id)
        self.assertEqual(versao.orcamento_id, original_v.orcamento_id)
        self.assertEqual(versao.numero, 2)
        self.assertEqual(versao.autor, "Autor")
        self.assertEqual(versao.estado, EstadoVersao.APROVADA)
        self.assertEqual(versao.versao_anterior_id, VersaoId("ver-0"))
        self.assertEqual(versao.cenario_adotado_id, CenarioId("cen-1"))
        self.assertEqual(versao.cenarios, original_v.cenarios)

    def test_schema_invalido(self):
        documento = json.loads(serializar_versao(*criar_dominio()))
        documento["schema_version"] = 2
        self.assertEqual(
            desserializar_versao(json.dumps(documento)).status,
            StatusPersistencia.DADO_CORROMPIDO,
        )

    def test_json_invalido(self):
        self.assertEqual(desserializar_versao("{").status, StatusPersistencia.DADO_CORROMPIDO)

    def test_propriedade_invalida(self):
        documento = json.loads(serializar_versao(*criar_dominio()))
        documento["versao"]["orcamento_id"] = "outro"
        self.assertEqual(
            desserializar_versao(json.dumps(documento)).status,
            StatusPersistencia.DADO_CORROMPIDO,
        )

    def test_cenario_invalido(self):
        documento = json.loads(serializar_versao(*criar_dominio()))
        documento["versao"]["cenarios"][0]["versao_id"] = "outra-versao"
        self.assertEqual(
            desserializar_versao(json.dumps(documento)).status,
            StatusPersistencia.DADO_CORROMPIDO,
        )

    def test_schema_contem_somente_campos_do_kid_step(self):
        documento = json.loads(serializar_versao(*criar_dominio()))
        texto = json.dumps(documento).lower()
        for proibido in ("cliente", "familia", "equipamento", "parametro", "pacote", "formula"):
            self.assertNotIn(proibido, texto)


class TestIndiceOrcamentos(unittest.TestCase):
    def test_indice_tem_somente_sete_campos(self):
        self.assertEqual(len(CAMPOS_INDICE), 7)
        self.assertEqual(
            CAMPOS_INDICE,
            ("orcamento_id", "versao_id", "numero", "objeto", "finalidade", "responsavel", "estado"),
        )

    def test_indice_invalido_e_recusado(self):
        self.assertEqual(
            desserializar_indice("orcamento_id,detalhe\na,b\n").status,
            StatusPersistencia.DADO_CORROMPIDO,
        )


class TestRepositorioOrcamentos(unittest.TestCase):
    def setUp(self):
        self.repo = RepositorioOrcamentosGitHub("token", "org/repo")
        self.orcamento, self.versao = criar_dominio()
        self.indice_vazio = serializar_indice([])

    @patch("modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit")
    def test_criacao_composta_publica_indice_e_json(self, publicar):
        publicar.return_value = ResultadoPersistenciaMultiArquivo(
            StatusPersistenciaMultiArquivo.SUCESSO, "main",
            (CAMINHO_INDICE, caminho_versao("orc-1", "ver-1")),
            snapshot_commit_sha="snap", commit_sha="novo",
        )
        resultado = self.repo.persistir_versao(
            self.orcamento, self.versao, self.indice_vazio, "snap"
        )
        self.assertTrue(resultado.sucesso)
        alteracoes = publicar.call_args.args[0]
        self.assertEqual([a.arquivo for a in alteracoes], [
            CAMINHO_INDICE, caminho_versao("orc-1", "ver-1")
        ])
        self.assertIn(b"schema_version", alteracoes[1].conteudo)

    @patch("modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit")
    def test_conflito_sem_branch_avancada(self, publicar):
        publicar.return_value = ResultadoPersistenciaMultiArquivo(
            StatusPersistenciaMultiArquivo.CONFLITO, "main", (), snapshot_commit_sha="snap"
        )
        resultado = self.repo.persistir_versao(
            self.orcamento, self.versao, self.indice_vazio, "snap"
        )
        self.assertEqual(resultado.status, StatusPersistencia.CONFLITO)

    @patch("modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit")
    def test_branch_avancada(self, publicar):
        publicar.return_value = ResultadoPersistenciaMultiArquivo(
            StatusPersistenciaMultiArquivo.CONFLITO, "main", (), snapshot_commit_sha="outro"
        )
        resultado = self.repo.persistir_versao(
            self.orcamento, self.versao, self.indice_vazio, "snap"
        )
        self.assertEqual(resultado.status, StatusPersistencia.BRANCH_AVANCADA)

    @patch("modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit")
    def test_indice_invalido_nao_inicia_publicacao(self, publicar):
        resultado = self.repo.persistir_versao(self.orcamento, self.versao, "invalido", "snap")
        self.assertEqual(resultado.status, StatusPersistencia.DADO_CORROMPIDO)
        publicar.assert_not_called()

    @patch("modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit")
    def test_propriedade_invalida_retorna_contrato_sem_exception(self, publicar):
        estrangeira = VersaoOrcamento(
            VersaoId("estrangeira"), OrcamentoId("outro"), 1, "Autor"
        )
        resultado = self.repo.persistir_versao(
            self.orcamento, estrangeira, self.indice_vazio, "snap"
        )
        self.assertEqual(resultado.status, StatusPersistencia.REQUISICAO_INVALIDA)
        publicar.assert_not_called()

    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_json_inexistente(self, get):
        get.return_value = Resposta(404)
        resultado = self.repo.carregar_versao("orc-1", "ver-1")
        self.assertEqual(resultado.status, StatusPersistencia.DADO_INEXISTENTE)
        get.assert_called_once()

    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_json_corrompido(self, get):
        get.return_value = Resposta(200, {"content": base64.b64encode(b"{").decode()})
        resultado = self.repo.carregar_versao("orc-1", "ver-1")
        self.assertEqual(resultado.status, StatusPersistencia.DADO_CORROMPIDO)
        get.assert_called_once()

    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_leitura_reconstroi_em_uma_unica_operacao_remota(self, get):
        conteudo = serializar_versao(self.orcamento, self.versao).encode()
        get.return_value = Resposta(200, {"content": base64.b64encode(conteudo).decode()})
        resultado = self.repo.carregar_versao("orc-1", "ver-1")
        self.assertTrue(resultado.sucesso)
        get.assert_called_once()

    @patch("modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit")
    def test_ausencia_de_parcialidade(self, publicar):
        publicar.return_value = ResultadoPersistenciaMultiArquivo(
            StatusPersistenciaMultiArquivo.REQUISICAO_INVALIDA, "main", (),
            erro="operação recusada",
        )
        resultado = self.repo.persistir_versao(
            self.orcamento, self.versao, self.indice_vazio, "snap"
        )
        self.assertEqual(resultado.status, StatusPersistencia.OPERACAO_PARCIAL_RECUSADA)
        self.assertIsNone(resultado.valor)


if __name__ == "__main__":
    unittest.main()
