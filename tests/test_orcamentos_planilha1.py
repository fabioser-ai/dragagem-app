import importlib
import json
import math
import sys
import types
import unittest
from contextlib import nullcontext
from dataclasses import asdict, replace
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.aplicacao.planilha1 import salvar_planilha1
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.planilha1 import (
    DIMENSAO_WORKSHEET_PLANILHA1,
    FORMULAS_PLANILHA1,
    INDICE_WORKSHEET_PLANILHA1,
    LINHAS_PLANILHA1,
    WORKSHEET_ORIGEM_PLANILHA1,
    EntradaLinhaPlanilha1,
    Planilha1,
    calcular_planilha1,
)
from modulos.orcamentos.dominio.planilha_precos import (
    PlanilhaPrecos,
    ReferenciasPlanilhaPrecos,
    calcular_planilha_precos,
)
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao


def referencias_excel():
    return ReferenciasPlanilhaPrecos(
        16961.72, 39925.08, 177323.61, 2509, 355460.245, 15,
        326679.25303539797, 5000, 14204.144, 17310.245, 6808.91,
    )


def resultados_precos():
    return calcular_planilha_precos(PlanilhaPrecos(), referencias_excel())


class ColunaFalsa:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class StreamlitFalso:
    def __init__(self, salvar=False, valores=None):
        self.salvar = salvar
        self.valores = valores or {}
        self.session_state = {}
        self.formularios, self.erros, self.reruns = [], [], 0

    def form(self, chave):
        self.formularios.append(chave)
        return nullcontext()

    def form_submit_button(self, texto):
        return self.salvar and texto == "Salvar Planilha1"

    def subheader(self, texto): pass
    def markdown(self, texto): pass
    def caption(self, texto): pass
    def success(self, texto): pass
    def metric(self, rotulo, valor, **kwargs): pass

    def error(self, texto):
        self.erros.append(texto)

    def columns(self, n):
        return tuple(ColunaFalsa() for _ in range(n))

    def number_input(self, rotulo, **kwargs):
        return self.valores.get(kwargs["key"], kwargs["value"])

    def rerun(self):
        self.reruns += 1


class TestEstruturaPlanilha1(unittest.TestCase):
    def test_metadados_e_estrutura(self):
        self.assertEqual(WORKSHEET_ORIGEM_PLANILHA1, "Planilha1")
        self.assertEqual(INDICE_WORKSHEET_PLANILHA1, 16)
        self.assertEqual(DIMENSAO_WORKSHEET_PLANILHA1, "A2:F7")
        self.assertEqual(len(LINHAS_PLANILHA1), 4)
        self.assertEqual([x.quantidade for x in Planilha1().linhas], [1, 2496, 5000, 1])
        self.assertEqual([x[3] for x in LINHAS_PLANILHA1], ["vb", "m2", "m3", "vb"])
        self.assertTrue(LINHAS_PLANILHA1[-1][2].endswith(" "))

    def test_nove_formulas_exatas(self):
        self.assertEqual(FORMULAS_PLANILHA1, (
            ("E3", "=SUM('10. Plan. Preços'!J4:J5)"),
            ("F3", "=D3*E3"),
            ("E4", "=F4/D4"),
            ("F4", "=SUM('10. Plan. Preços'!J6)"),
            ("E5", "=F5/D5"),
            ("F5", "=SUM('10. Plan. Preços'!J7:J9)"),
            ("E6", "=F6"),
            ("F6", "=SUM('10. Plan. Preços'!J10:J11)"),
            ("F7", "=SUM(F3:F6)"),
        ))


class TestCalculosPlanilha1(unittest.TestCase):
    def test_cache_do_excel(self):
        r = calcular_planilha1(Planilha1(), resultados_precos())
        esperados = (
            (91018.88, 91018.88),
            (113.66898076923076, 283717.77599999995),
            (212.16615810132734, 1060830.7905066367),
            (38590.648, 38590.648),
        )
        for linha, (unitario, total) in zip(r.linhas, esperados):
            self.assertAlmostEqual(linha.preco_unitario, unitario)
            self.assertAlmostEqual(linha.preco_total, total)
        self.assertAlmostEqual(r.total_geral, 1474158.0945066367)

    def test_quantidades_manuais_e_formula_e6(self):
        p = replace(Planilha1(), linhas=tuple(
            replace(x, quantidade=2) if x.id == "mobilizacao" else
            replace(x, quantidade=7) if x.id == "desmobilizacao" else x
            for x in Planilha1().linhas
        ))
        r = calcular_planilha1(p, resultados_precos())
        self.assertAlmostEqual(r.linhas[0].preco_total, 182037.76)
        self.assertEqual(r.linhas[3].preco_unitario, r.linhas[3].preco_total)

    def test_zero_e_invalidos(self):
        p = replace(Planilha1(), linhas=tuple(
            replace(x, quantidade=0) if x.id == "preparo-celula" else x
            for x in Planilha1().linhas
        ))
        self.assertIsNone(calcular_planilha1(p, resultados_precos()).linhas[1].preco_unitario)
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                EntradaLinhaPlanilha1("x", valor)

    def test_versao_congelada(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(salvar_planilha1(versao, Planilha1()).sucesso)


class TestPersistenciaPlanilha1(unittest.TestCase):
    def test_round_trip_somente_entradas(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        alterada = replace(Planilha1(), linhas=tuple(
            replace(x, quantidade=123.45) if x.id == "preparo-celula" else x
            for x in Planilha1().linhas
        ))
        versao.registrar_planilha1(alterada)
        documento = json.loads(serializar_versao(orcamento, versao))
        self.assertEqual(set(documento["versao"]["planilha1"]), {"linhas"})
        self.assertNotIn("total_geral", documento["versao"]["planilha1"])
        carregada = desserializar_versao(json.dumps(documento)).valor[1]
        self.assertEqual(asdict(carregada.planilha1), asdict(alterada))

    def test_schema_20_e_corrupcao(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 20
        documento["versao"].pop("planilha1")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(asdict(resultado.valor[1].planilha1), asdict(Planilha1()))
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["planilha1"]["linhas"][0]["quantidade"] = -1
        self.assertEqual(desserializar_versao(json.dumps(documento)).status, StatusPersistencia.DADO_CORROMPIDO)


class TestTelaPlanilha1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.planilha1")

    def render(self, falso, repositorio):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        with patch.object(self.tela, "st", falso), patch.object(
            self.tela, "_referencias_externas", return_value=referencias_excel()
        ):
            self.tela.render(
                repositorio=repositorio, orcamento=orcamento, versao=versao,
                snapshot_esperado="anterior",
            )

    def test_edicao_sem_persistencia_ou_rerun(self):
        falso, repositorio = StreamlitFalso(), Mock()
        self.render(falso, repositorio)
        self.assertEqual(falso.formularios, ["planilha1_formulario"])
        repositorio.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_salvar_uma_vez_e_conflito(self):
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="novo"
        )
        falso = StreamlitFalso(True, {"planilha1_preparo-celula_quantidade": 321.5})
        self.render(falso, repositorio)
        repositorio.persistir_documento_versao.assert_called_once()
        self.assertEqual(
            repositorio.persistir_documento_versao.call_args.args[1].planilha1.linhas[1].quantidade,
            321.5,
        )
        self.assertEqual(falso.reruns, 1)

        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.BRANCH_AVANCADA
        )
        falso = StreamlitFalso(True)
        self.render(falso, repositorio)
        self.assertEqual(falso.reruns, 0)
        self.assertTrue(falso.erros)
