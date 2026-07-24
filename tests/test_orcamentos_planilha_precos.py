import importlib
import json
import math
import sys
import types
import unittest
from contextlib import nullcontext
from dataclasses import asdict, replace
from pathlib import Path
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.aplicacao.planilha_precos import salvar_planilha_precos
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.planilha_precos import (
    FORMULAS_PLANILHA_PRECOS,
    INDICE_WORKSHEET_PLANILHA_PRECOS,
    WORKSHEET_ORIGEM_PLANILHA_PRECOS,
    EntradaLinhaPlanilhaPrecos,
    PlanilhaPrecos,
    ReferenciasPlanilhaPrecos,
    calcular_planilha_precos,
)
from modulos.orcamentos.persistencia.contratos import (
    ResultadoPersistencia,
    StatusPersistencia,
)
from modulos.orcamentos.persistencia.serializacao import (
    desserializar_versao,
    serializar_versao,
)


def referencias_excel():
    return ReferenciasPlanilhaPrecos(
        16961.72,
        39925.08,
        177323.61,
        2509,
        355460.245,
        15,
        326679.25303539797,
        5000,
        14204.144,
        17310.245,
        6808.91,
    )


class ColunaFalsa:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class StreamlitPlanilhaPrecosFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar = salvar
        self.valores = valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios = []
        self.erros = []
        self.reruns = 0

    def form(self, chave):
        self.formularios.append(chave)
        return nullcontext()

    def form_submit_button(self, texto):
        return self.salvar and texto == "Salvar Planilha de Preços"

    def subheader(self, texto):
        pass

    def markdown(self, texto):
        pass

    def caption(self, texto):
        pass

    def success(self, texto):
        pass

    def error(self, texto):
        self.erros.append(texto)

    def columns(self, n):
        return tuple(ColunaFalsa() for _ in range(n))

    def number_input(self, rotulo, **kwargs):
        return self.valores.get(kwargs["key"], kwargs.get("value"))

    def metric(self, rotulo, valor, **kwargs):
        pass

    def rerun(self):
        self.reruns += 1


class TestEstruturaPlanilhaPrecos(unittest.TestCase):
    def test_nome_posicao_e_planilha1_fora_do_escopo(self):
        self.assertEqual(WORKSHEET_ORIGEM_PLANILHA_PRECOS, "10. Plan. Preços")
        self.assertEqual(INDICE_WORKSHEET_PLANILHA_PRECOS, 15)
        self.assertFalse(
            Path("modulos/orcamentos/dominio/planilha1.py").exists()
        )

    def test_estrutura_e_valores_manuais_iniciais(self):
        planilha = PlanilhaPrecos()
        self.assertEqual(
            [item.id for item in planilha.linhas],
            [
                "mobilizacao-draga",
                "mobilizacao-polimero",
                "preparo-celula",
                "fornecimento-bags",
                "dragagem-operacao",
                "medicao",
                "desmobilizacao-draga",
                "desmobilizacao-polimero",
            ],
        )
        self.assertEqual(
            [item.quantidade_manual for item in planilha.linhas],
            [1, 1, None, None, None, 1, 1, 1],
        )
        self.assertEqual(
            [item.bdi for item in planilha.linhas],
            [60, 60, 60, 45, 60, 60, 60, 60],
        )

    def test_lista_completa_das_trinta_e_oito_formulas(self):
        self.assertEqual(len(FORMULAS_PLANILHA_PRECOS), 38)
        self.assertEqual(FORMULAS_PLANILHA_PRECOS[0], ("C4", "='1. Mob. Draga'!F27"))
        self.assertEqual(
            FORMULAS_PLANILHA_PRECOS[31],
            ("C11", "='9. Desmob. Eq. Polimero '!F26"),
        )
        self.assertEqual(FORMULAS_PLANILHA_PRECOS[-3], ("C12", "=SUM(C5:C11)"))
        self.assertEqual(FORMULAS_PLANILHA_PRECOS[-2], ("J12", "=SUM(J4:J11)"))
        self.assertEqual(
            FORMULAS_PLANILHA_PRECOS[-1], ("J18", "=(SUM(J6:J9))/E8")
        )

    def test_referencias_entre_abas_sao_exatamente_as_do_excel(self):
        externas = tuple(
            formula
            for _, formula in FORMULAS_PLANILHA_PRECOS
            if "!" in formula
        )
        self.assertEqual(
            externas,
            (
                "='1. Mob. Draga'!F27",
                "='2. Mob. Eq. Polimero'!F27",
                "='3. Prep. Célula'!F29",
                "='3. Prep. Célula'!N7",
                "='4. Forn. Bag'!F29",
                "=SUM('4. Forn. Bag'!D15:D23)",
                "='6. Dragagem'!D248",
                "='4. Forn. Bag'!B33",
                "='7. Medição'!F20",
                "='8. Desmob. Draga'!F21",
                "='9. Desmob. Eq. Polimero '!F26",
            ),
        )
        self.assertFalse(any("[" in formula for formula in externas))


class TestCalculosPlanilhaPrecos(unittest.TestCase):
    def calcular(self, planilha=None, referencias=None):
        return calcular_planilha_precos(
            planilha or PlanilhaPrecos(),
            referencias or referencias_excel(),
        )

    def test_resultados_iniciais_reproduzem_valores_armazenados(self):
        resultado = self.calcular()
        self.assertAlmostEqual(resultado.linhas[0].preco_total, 27138.752)
        self.assertAlmostEqual(resultado.linhas[2].custo_unitario, 70.67501394978078)
        self.assertAlmostEqual(resultado.linhas[3].preco_total, 515417.35525)
        self.assertAlmostEqual(resultado.linhas[4].preco_total, 522686.8048566368)
        self.assertAlmostEqual(resultado.custo_total, 937711.487035398)
        self.assertAlmostEqual(resultado.preco_venda, 1474158.0945066367)
        self.assertAlmostEqual(resultado.valor_auxiliar_j18, 268.9097133013273)

    def test_custo_total_exclui_deliberadamente_primeira_linha(self):
        resultado = self.calcular()
        soma_completa = sum(item.custo_total or 0 for item in resultado.linhas)
        self.assertAlmostEqual(
            soma_completa - resultado.custo_total,
            referencias_excel().mobilizacao_draga_f27,
        )

    def test_quantidades_manuais_e_bdi_permanecem_editaveis(self):
        base = PlanilhaPrecos()
        alterada = replace(
            base,
            linhas=tuple(
                replace(item, quantidade_manual=2, bdi=10)
                if item.id == "mobilizacao-draga"
                else item
                for item in base.linhas
            ),
        )
        resultado = self.calcular(alterada)
        self.assertEqual(resultado.linhas[0].quantidade, 2)
        self.assertAlmostEqual(resultado.linhas[0].custo_unitario, 8480.86)
        self.assertAlmostEqual(resultado.linhas[0].preco_total, 18657.892)

    def test_quantidades_referenciadas_nao_viram_entradas(self):
        base = PlanilhaPrecos()
        referencias = replace(
            referencias_excel(),
            preparacao_celula_n7=100,
            fornecimento_bag_d15_d23=4,
            fornecimento_bag_b33=200,
        )
        resultado = self.calcular(base, referencias)
        self.assertEqual(
            [resultado.linhas[i].quantidade for i in (2, 3, 4)],
            [100, 4, 200],
        )
        self.assertIsNone(base.linhas[2].quantidade_manual)

    def test_vazios_e_divisao_por_zero_preservam_resultado_pendente(self):
        referencias = ReferenciasPlanilhaPrecos(*([None] * 11))
        resultado = self.calcular(referencias=referencias)
        self.assertIsNone(resultado.linhas[2].custo_unitario)
        self.assertEqual(resultado.linhas[2].preco_total, 0)
        self.assertIsNone(resultado.valor_auxiliar_j18)
        self.assertTrue(math.isfinite(resultado.preco_venda))

    def test_entradas_invalidas_sao_rejeitadas(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                EntradaLinhaPlanilhaPrecos("x", 1, valor)
        with self.assertRaises(ValueError):
            PlanilhaPrecos(PlanilhaPrecos().linhas[:-1])

    def test_versao_congelada_recusa_alteracao(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(
            salvar_planilha_precos(versao, PlanilhaPrecos()).sucesso
        )


class TestPersistenciaPlanilhaPrecos(unittest.TestCase):
    def test_round_trip_persiste_somente_entradas(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        alterada = replace(
            PlanilhaPrecos(),
            linhas=tuple(
                replace(item, bdi=17.5) if item.id == "medicao" else item
                for item in PlanilhaPrecos().linhas
            ),
        )
        versao.registrar_planilha_precos(alterada)
        documento = json.loads(serializar_versao(orcamento, versao))
        dados = documento["versao"]["planilha_precos"]
        self.assertEqual(set(dados), {"linhas"})
        self.assertNotIn("preco_venda", dados)
        carregada = desserializar_versao(json.dumps(documento)).valor[1]
        self.assertEqual(asdict(carregada.planilha_precos), asdict(alterada))

    def test_schema_19_sem_nova_aba_continua_legivel(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 19
        documento["versao"].pop("planilha_precos")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(
            asdict(resultado.valor[1].planilha_precos),
            asdict(PlanilhaPrecos()),
        )

    def test_documento_corrompido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["planilha_precos"]["linhas"][0]["bdi"] = -1
        self.assertEqual(
            desserializar_versao(json.dumps(documento)).status,
            StatusPersistencia.DADO_CORROMPIDO,
        )


class TestTelaPlanilhaPrecos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module(
            "modulos.orcamentos.apresentacao.planilha_precos"
        )

    def test_formulario_unico_sem_leitura_persistencia_ou_rerun_na_edicao(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        falso, repositorio = StreamlitPlanilhaPrecosFalso(), Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="s",
            )
        self.assertEqual(falso.formularios, ["planilha_precos_formulario"])
        repositorio.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_uma_vez_e_faz_rerun(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="novo"
        )
        falso = StreamlitPlanilhaPrecosFalso(
            salvar=True,
            valores={"planilha_precos_medicao_bdi": 12.5},
        )
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="anterior",
            )
        repositorio.persistir_documento_versao.assert_called_once()
        salvo = repositorio.persistir_documento_versao.call_args.args[1]
        self.assertEqual(salvo.planilha_precos.linhas[5].bdi, 12.5)
        self.assertEqual(falso.reruns, 1)

    def test_conflito_nao_faz_rerun(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.BRANCH_AVANCADA
        )
        falso = StreamlitPlanilhaPrecosFalso(salvar=True)
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="anterior",
            )
        self.assertEqual(falso.reruns, 0)
        self.assertTrue(falso.erros)
