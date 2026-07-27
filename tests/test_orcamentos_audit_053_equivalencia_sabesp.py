"""Caracterização integrada da equivalência do orçamento SABESP."""

import json
import sys
import types
import unittest
from dataclasses import asdict, replace
from unittest.mock import patch

from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.planilha1 import calcular_planilha1
from modulos.orcamentos.dominio.planilha_precos import calcular_planilha_precos
from modulos.orcamentos.persistencia.contratos import StatusPersistencia
from modulos.orcamentos.persistencia.github_repositorio import (
    RepositorioOrcamentosGitHub,
)
from modulos.orcamentos.persistencia.serializacao import (
    SCHEMA_VERSION,
    desserializar_versao,
    serializar_versao,
)
from services.persistencia_multi_arquivo import (
    ResultadoPersistenciaMultiArquivo,
    StatusPersistenciaMultiArquivo,
)

sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
from modulos.orcamentos.apresentacao.planilha_precos import (  # noqa: E402
    _referencias_externas,
)


WORKSHEETS_OFICIAIS = (
    ("Dados Obra ", 3),
    ("Cotaçoes", 0),
    ("Produção", 9),
    ("Barrilete", 39),
    ("1. Mob. Draga", 24),
    ("2. Mob. Eq. Polimero", 24),
    ("Canteiro", 32),
    ("3. Prep. Célula", 45),
    ("4. Forn. Bag", 71),
    ("5. Operação Sistema", 24),
    ("6. Dragagem", 84),
    ("7. Medição", 19),
    ("8. Carga e Transporte", 18),
    ("8. Desmob. Draga", 18),
    ("9. Desmob. Eq. Polimero ", 23),
    ("10. Plan. Preços", 38),
    ("Planilha1", 9),
)

REFERENCIAS_OFICIAIS = {
    "mobilizacao_draga_f27": 16961.72,
    "mobilizacao_polimero_f27": 39925.08,
    "preparacao_celula_f29": 177323.61,
    "preparacao_celula_n7": 2509.0,
    "fornecimento_bag_f29": 355460.245,
    "fornecimento_bag_d15_d23": 15.0,
    "dragagem_d248": 326679.25303539797,
    "fornecimento_bag_b33": 5000.0,
    "medicao_f20": 14204.144,
    "desmobilizacao_draga_f21": 17310.245,
    "desmobilizacao_polimero_f26": 6808.91,
}


def criar_caso_oficial():
    orcamento, versao = criar_orcamento_vazio("AUDIT_053").valor
    resultado = versao.registrar_dados_obra(DadosObra())
    if not resultado.sucesso:
        raise AssertionError(resultado.erro)
    return orcamento, versao


def calcular_fechamento(versao):
    referencias = _referencias_externas(versao)
    precos = calcular_planilha_precos(versao.planilha_precos, referencias)
    final = calcular_planilha1(versao.planilha1, precos)
    return referencias, precos, final


class TestAudit053Inventario(unittest.TestCase):
    def test_dezessete_worksheets_e_480_formulas_expandidas(self):
        self.assertEqual(len(WORKSHEETS_OFICIAIS), 17)
        self.assertEqual(sum(total for _, total in WORKSHEETS_OFICIAIS), 480)
        self.assertEqual(WORKSHEETS_OFICIAIS[0][0], "Dados Obra ")
        self.assertEqual(WORKSHEETS_OFICIAIS[14][0], "9. Desmob. Eq. Polimero ")


class TestAudit053GoldenIntegrado(unittest.TestCase):
    def test_reproduz_intermediarios_e_total_final_oficiais_sem_rede(self):
        _, versao = criar_caso_oficial()
        with patch("requests.get") as leitura, patch(
            "modulos.orcamentos.persistencia.github_repositorio."
            "publicar_arquivos_em_commit"
        ) as escrita:
            referencias, precos, final = calcular_fechamento(versao)
        leitura.assert_not_called()
        escrita.assert_not_called()
        for campo, esperado in REFERENCIAS_OFICIAIS.items():
            self.assertAlmostEqual(getattr(referencias, campo), esperado)
        self.assertAlmostEqual(precos.custo_total, 937711.487035398)
        self.assertAlmostEqual(precos.preco_venda, 1474158.0945066367)
        self.assertAlmostEqual(precos.valor_auxiliar_j18, 268.9097133013273)
        self.assertAlmostEqual(final.total_geral, 1474158.0945066367)

    def test_alteracao_de_volume_recalcula_dependentes_e_preserva_fixos(self):
        _, versao = criar_caso_oficial()
        referencias_antes, _, final_antes = calcular_fechamento(versao)
        versao.registrar_dados_obra(
            replace(versao.dados_obra, volume_dragagem=10000.0)
        )
        referencias_depois, _, final_depois = calcular_fechamento(versao)
        self.assertEqual(
            referencias_depois.mobilizacao_draga_f27,
            referencias_antes.mobilizacao_draga_f27,
        )
        self.assertNotEqual(
            referencias_depois.dragagem_d248,
            referencias_antes.dragagem_d248,
        )
        self.assertNotEqual(final_depois.total_geral, final_antes.total_geral)


class TestAudit053PersistenciaIntegrada(unittest.TestCase):
    def test_salvar_fechar_reabrir_preserva_entradas_e_recalcula_resultados(self):
        orcamento, versao = criar_caso_oficial()
        _, _, antes = calcular_fechamento(versao)
        documento = serializar_versao(orcamento, versao)
        bruto = json.loads(documento)
        self.assertEqual(bruto["schema_version"], SCHEMA_VERSION)
        self.assertNotIn("resultados", bruto["versao"])
        self.assertNotIn("preco_venda", json.dumps(bruto))
        reaberto = desserializar_versao(documento)
        self.assertTrue(reaberto.sucesso)
        _, versao_reaberta = reaberto.valor
        self.assertEqual(
            asdict(versao_reaberta.dados_obra), asdict(versao.dados_obra)
        )
        _, _, depois = calcular_fechamento(versao_reaberta)
        self.assertAlmostEqual(depois.total_geral, antes.total_geral)

    @patch(
        "modulos.orcamentos.persistencia.github_repositorio."
        "publicar_arquivos_em_commit"
    )
    def test_snapshot_divergente_recusa_sobrescrita(self, publicar):
        publicar.return_value = ResultadoPersistenciaMultiArquivo(
            StatusPersistenciaMultiArquivo.CONFLITO,
            "main",
            (),
            snapshot_commit_sha="snapshot-remoto-novo",
        )
        orcamento, versao = criar_caso_oficial()
        repositorio = RepositorioOrcamentosGitHub("token-falso", "org/repo")
        resultado = repositorio.persistir_documento_versao(
            orcamento, versao, "snapshot-local-antigo"
        )
        self.assertEqual(resultado.status, StatusPersistencia.BRANCH_AVANCADA)
        self.assertIsNone(resultado.commit_sha)


if __name__ == "__main__":
    unittest.main()
