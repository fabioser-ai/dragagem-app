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
from modulos.orcamentos.aplicacao.operacao_sistema import salvar_operacao_sistema
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.fornecimento_bag import FornecimentoBag, MemorialFisicoBag
from modulos.orcamentos.dominio.operacao_sistema import OperacaoSistema, calcular_operacao_sistema
from modulos.orcamentos.dominio.producao import Producao
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao


class ColunaFalsa:
    def __enter__(self): return self
    def __exit__(self, *args): return False


class StreamlitOperacaoFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar, self.valores = salvar, valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios, self.campos, self.metricas, self.erros = [], [], [], []
        self.reruns = 0
    def form(self, chave): self.formularios.append(chave); return nullcontext()
    def form_submit_button(self, texto): return self.salvar and texto == "Salvar Operação do Sistema"
    def subheader(self, texto): pass
    def markdown(self, texto): pass
    def success(self, texto): pass
    def error(self, texto): self.erros.append(texto)
    def columns(self, n): return tuple(ColunaFalsa() for _ in range(n))
    def number_input(self, rotulo, **kwargs):
        chave = kwargs["key"]; self.campos.append((rotulo, chave, kwargs.get("value")))
        return self.valores.get(chave, kwargs.get("value"))
    def text_input(self, rotulo, **kwargs):
        chave = kwargs["key"]; self.campos.append((rotulo, chave, kwargs.get("value")))
        return self.valores.get(chave, kwargs.get("value", ""))
    def metric(self, rotulo, valor): self.metricas.append((rotulo, valor))
    def rerun(self): self.reruns += 1


class TestCalculosOperacaoSistema(unittest.TestCase):
    def calcular(self, operacao=None, horas=9, tonelada=500, prazo=2.3381967826):
        return calcular_operacao_sistema(operacao or OperacaoSistema(), horas, tonelada, prazo)

    def test_fotografia_inicial_reproduz_duas_linhas_e_oito_itens(self):
        o = OperacaoSistema()
        self.assertEqual(len(o.equipe), 2)
        self.assertEqual(len(o.itens), 8)
        self.assertEqual([x.numero for x in o.itens], list(range(1, 9)))
        self.assertEqual(o.itens[3].observacao, "Fornecido pela Contratante")

    def test_c5_reproduz_formula_literal_e_horas_referenciam_dados_obra(self):
        r = self.calcular(horas=8.5)
        self.assertEqual(r.mao_obra[0].custo_hora, 15.15 * 1.25)
        self.assertEqual([x.horas_dia for x in r.mao_obra], [8.5, 8.5])

    def test_mao_obra_refeicoes_transporte_e_custo_diario(self):
        r = self.calcular()
        self.assertAlmostEqual(r.mao_obra[0].total, 357.91875)
        self.assertAlmostEqual(r.mao_obra[1].total, 210.357)
        self.assertEqual((r.quantidade_pessoas, r.total_refeicoes, r.total_transportes), (2, 60, 20))
        self.assertAlmostEqual(r.custo_por_dia, 648.27575)

    def test_memorial_polimero_reproduz_base_seca_dosagem_e_acrescimo(self):
        m = self.calcular(tonelada=500).memorial_polimero
        self.assertEqual(m.tonelada_seca, 500)
        self.assertEqual(m.dosagem_kg_por_tonelada, 3)
        self.assertEqual(m.acrescimo, 1.05)
        self.assertEqual(m.quantidade_polimero, 1575)

    def test_referencia_externa_fornecimento_bag_altera_somente_quantidade_derivada(self):
        base = self.calcular(tonelada=500)
        alterado = self.calcular(tonelada=800)
        itens_base = {x.id: x for x in base.itens}
        itens_alt = {x.id: x for x in alterado.itens}
        self.assertEqual(itens_alt["polimero"].quantidade, 2520)
        self.assertNotEqual(itens_base["polimero"].preco_total, itens_alt["polimero"].preco_total)
        self.assertEqual(itens_base["energia-diesel"].preco_total, itens_alt["energia-diesel"].preco_total)

    def test_equipamento_polimero_e_frete_sao_totais_calculados(self):
        itens = {x.id: x for x in self.calcular().itens}
        self.assertEqual(itens["equipamento-polimero"].preco_total, 25000)
        self.assertEqual(itens["polimero"].preco_total, 34650)
        self.assertEqual(itens["frete-polimero"].preco_total, 3000)

    def test_agua_energia_e_wap_permanecem_manuais_e_zerados(self):
        itens = {x.id: x for x in self.calcular().itens}
        for id_ in ("agua-operacao", "energia-diesel", "maquina-wap"):
            self.assertEqual(itens[id_].preco_total, 0)
            self.assertIsNone(itens[id_].quantidade)

    def test_instalacoes_e_mao_obra_total_permanecem_manuais(self):
        base = OperacaoSistema()
        alterado = replace(base, custo_refeicao=100)
        itens = {x.id: x for x in self.calcular(alterado).itens}
        self.assertEqual(itens["instalacoes-hidraulicas"].preco_total, 2000)
        self.assertNotEqual(itens["mao-obra-operacao"].preco_unitario, 648.27575)
        self.assertEqual(itens["mao-obra-operacao"].preco_total, 58344.8175)

    def test_prazo_arredondado_dias_e_custo_mensal(self):
        r = self.calcular(prazo=2.3381967826)
        self.assertEqual(r.prazo_execucao_meses, 3)
        self.assertEqual(r.dias_operacao, 90)
        self.assertAlmostEqual(r.total, 122994.8175)
        self.assertAlmostEqual(r.custo_mensal, 40998.2725)

    def test_arredondamento_ocorre_somente_no_prazo(self):
        r = self.calcular(tonelada=123.456, prazo=1.01)
        self.assertEqual(r.prazo_execucao_meses, 2)
        self.assertAlmostEqual(r.memorial_polimero.quantidade_polimero, 123.456 * 3 * 1.05)

    def test_ausencia_e_zero_no_prazo_nao_geram_divisao_invalida(self):
        for prazo in (None, 0):
            with self.subTest(prazo=prazo):
                r = self.calcular(prazo=prazo)
                self.assertIsNone(r.custo_mensal)
                self.assertTrue(math.isfinite(r.total))

    def test_entradas_vazias_e_decimais_sao_seguras(self):
        base = OperacaoSistema()
        vazio = OperacaoSistema(
            tuple(replace(x, quantidade=None, custo_hora_manual=None, custo_hora_operador_calculado=False, encargos_sociais=None) for x in base.equipe),
            None, None,
            tuple(replace(x, quantidade_manual=None, quantidade_polimero=False, quantidade_dias_operacao=False, preco_unitario_manual=None, preco_unitario_custo_diario=False, preco_total_calculado=False, preco_total_manual=None) for x in base.itens),
        )
        r = self.calcular(vazio, horas=None, tonelada=None, prazo=None)
        for valor in (r.custo_por_dia, r.total, r.memorial_polimero.quantidade_polimero):
            self.assertTrue(math.isfinite(valor)); self.assertEqual(valor, 0)

    def test_invalidos_e_origens_duplicadas_sao_rejeitados(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError): OperacaoSistema(custo_refeicao=valor)
        with self.assertRaises(ValueError):
            replace(OperacaoSistema().itens[1], quantidade_manual=1)

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(salvar_operacao_sistema(versao, OperacaoSistema()).sucesso)


class TestPersistenciaOperacaoSistema(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_preserva_telas_anteriores(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        anteriores = tuple(asdict(x) for x in (
            versao.producao, versao.canteiro, versao.preparacao_celula, versao.fornecimento_bag,
        ))
        alterada = replace(OperacaoSistema(), custo_refeicao=45.75)
        versao.registrar_operacao_sistema(alterada)
        carregada = desserializar_versao(serializar_versao(orcamento, versao)).valor[1]
        self.assertEqual(asdict(carregada.operacao_sistema), asdict(alterada))
        self.assertEqual(tuple(asdict(x) for x in (
            carregada.producao, carregada.canteiro, carregada.preparacao_celula, carregada.fornecimento_bag,
        )), anteriores)

    def test_serializacao_nao_persiste_resultados_derivados(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = json.loads(serializar_versao(orcamento, versao))["versao"]["operacao_sistema"]
        for nome in ("quantidade_polimero", "prazo_execucao", "dias_operacao", "total", "custo_mensal"):
            self.assertNotIn(nome, dados)

    def test_schema_13_sem_nova_aba_continua_legivel(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 13
        documento["versao"].pop("operacao_sistema")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(asdict(resultado.valor[1].operacao_sistema), asdict(OperacaoSistema()))

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["operacao_sistema"]["equipe"][0]["quantidade"] = -1
        self.assertEqual(desserializar_versao(json.dumps(documento)).status, StatusPersistencia.DADO_CORROMPIDO)


class TestTelaOperacaoSistema(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.operacao_sistema")

    def _dominio(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra())
        return orcamento, versao

    def test_formulario_unico_renderiza_oito_itens_sem_operacao_remota(self):
        orcamento, versao = self._dominio()
        falso, repositorio = StreamlitOperacaoFalso(), Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repositorio, orcamento=orcamento, versao=versao, snapshot_esperado="s")
        self.assertEqual(falso.formularios, ["operacao_sistema_formulario"])
        self.assertEqual(len([x for x in falso.campos if x[0] == "Observação/Fonte"]), 8)
        repositorio.assert_not_called(); self.assertEqual(falso.reruns, 0)

    def test_referencias_externas_reproduzem_producao_e_fornecimento_bag(self):
        orcamento, versao = self._dominio()
        versao.registrar_fornecimento_bag(replace(
            FornecimentoBag(), memorial_fisico=MemorialFisicoBag(8000, 0.1, 0.2)
        ))
        falso = StreamlitOperacaoFalso()
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=Mock(), orcamento=orcamento, versao=versao, snapshot_esperado="s")
        self.assertIn(("Polímero", "2520 kg"), falso.metricas)
        self.assertIn(("Prazo de Execução", "3 mês(es)"), falso.metricas)

    def test_salvar_persiste_uma_vez_preserva_fornecimento_bag_e_faz_um_rerun(self):
        orcamento, versao = self._dominio()
        bag = asdict(versao.fornecimento_bag)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(StatusPersistencia.SUCESSO, commit_sha="c")
        falso = StreamlitOperacaoFalso(salvar=True, valores={"op_sistema_refeicao": 47.5})
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repositorio, orcamento=orcamento, versao=versao, snapshot_esperado="original")
        repositorio.persistir_documento_versao.assert_called_once()
        _, salva, snapshot = repositorio.persistir_documento_versao.call_args.args
        self.assertEqual(snapshot, "original")
        self.assertEqual(salva.operacao_sistema.custo_refeicao, 47.5)
        self.assertEqual(asdict(salva.fornecimento_bag), bag)
        self.assertEqual(falso.reruns, 1)


if __name__ == "__main__": unittest.main()
