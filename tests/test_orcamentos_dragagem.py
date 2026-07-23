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
from modulos.orcamentos.aplicacao.dragagem import salvar_dragagem
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.dragagem import (
    Dragagem, EntradaDragagem, FORMULAS_DRAGAGEM, calcular_dragagem,
)
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao


class ColunaFalsa:
    def __enter__(self): return self
    def __exit__(self, *args): return False


class StreamlitDragagemFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar, self.valores = salvar, valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios, self.campos, self.metricas, self.erros = [], [], [], []
        self.reruns = 0
    def form(self, chave): self.formularios.append(chave); return nullcontext()
    def form_submit_button(self, texto): return self.salvar and texto == "Salvar Dragagem"
    def subheader(self, texto): pass
    def markdown(self, texto): pass
    def success(self, texto): pass
    def error(self, texto): self.erros.append(texto)
    def columns(self, n): return tuple(ColunaFalsa() for _ in range(n))
    def number_input(self, rotulo, **kwargs):
        chave = kwargs["key"]; self.campos.append((rotulo, chave, kwargs.get("value")))
        return self.valores.get(chave, kwargs.get("value"))
    def metric(self, rotulo, valor): self.metricas.append((rotulo, valor))
    def rerun(self): self.reruns += 1


class TestCalculosDragagem(unittest.TestCase):
    def calcular(self, dragagem=None, canteiro=9674.301159999999, operacao=40998.2725, prazo=2.3381967826):
        return calcular_dragagem(dragagem or Dragagem(), canteiro, operacao, prazo)

    def test_fotografia_inicial_preserva_entradas_informativas_e_blocos_vazios(self):
        d = Dragagem()
        self.assertEqual(len(d.entradas), 104)
        valores = {x.celula: x.valor for x in d.entradas}
        self.assertEqual(valores["F7"], 150000)
        self.assertIsNone(valores["E28"])
        self.assertIsNone(valores["E53"])
        self.assertIsNone(valores["E177"])
        self.assertEqual(len([x for x in d.entradas if "prêmios" in x.bloco]), 12)
        self.assertEqual((valores["P12"], valores["P13"], valores["P14"]), (28.35, 11.13, 15.15))
        self.assertIsNone(valores["E187"])

    def test_as_84_formulas_reproduzem_a_fotografia_do_excel(self):
        esperados = {
            'F10':11226.6,'F11':1122.66,'E15':14849.26,'A20':238.6999,'E20':0,'L20':11,
            'A21':238.6999,'E21':0,'L21':0,'A22':238.6999,'E22':6767.142165,
            'A23':238.6999,'E23':2656.729887,'L23':219.9999,'A24':238.6999,'E24':0,
            'L24':238.6999,'A25':238.6999,'E25':0,'A26':238.6999,'E26':0,'A27':238.6999,
            'E27':0,'E31':9423.872052,'C37':9423.872052,'E37':10366.2592572,
            'E46':1490,'G52':1050,'G53':440,'E62':100,'E69':0,'E71':0,
            'G87':21380.1313092,'E139':900,'E140':1500,'E144':2900,'H146':2900,
            'E150':4519.666666666667,'K151':37500,'J152':3125,'J153':375,'J154':3500,
            'K156':7500,'J157':625,'E158':9674.30116,'J158':75,'J159':700,
            'D161':18193.967826666667,'I161':22.833333333333332,'K161':3425,
            'J162':285.4166666666667,'J163':34.25,'J164':319.6666666666667,
            'H167':3500,'I167':700,'J167':319.6666666666667,'K167':4519.666666666667,
            'E178':500,'G181':57823.35913586667,'E185':2891.1679567933334,
            'E186':2891.1679567933334,'E189':5782.335913586667,'E192':2500,
            'E193':1500,'E194':289.11679567933334,'E196':4289.116795679333,
            'D215':57823.35913586667,'D218':5782.335913586667,'D220':4289.116795679333,
            'D222':67894.81184513267,'D231':0,'D234':545.5653518705636,'J235':198,
            'D244':67894.81184513267,'D245':40998.2725,'D246':108893.08434513267,
            'D247':3,'J247':108893.08434513267,'D248':326679.25303539797,
            'J249':174228.93495221226,'L249':879.9441159202639,
            'L251':527.9664695521583,'J252':118.8,'J253':1466.5735265337732,
        }
        resultado = self.calcular()
        self.assertEqual(len(FORMULAS_DRAGAGEM), 84)
        self.assertEqual(set(esperados), {x[0] for x in FORMULAS_DRAGAGEM})
        for celula, esperado in esperados.items():
            with self.subTest(celula=celula):
                self.assertAlmostEqual(resultado.valor(celula), esperado, places=7)

    def test_formula_textual_preserva_referencias_fatores_e_ordem_do_excel(self):
        formulas = dict(FORMULAS_DRAGAGEM)
        self.assertEqual(formulas["E158"], "=Canteiro!F32")
        self.assertEqual(formulas["D245"], "='5. Operação Sistema'!F24")
        self.assertEqual(formulas["D247"], "=ROUNDUP(Produção!D24,0)")
        self.assertEqual(formulas["D234"], "=J253*0.6*0.62")
        self.assertEqual(formulas["I161"], "=(I151/12)+2")

    def test_operacao_combustivel_lubrificantes_fretes_e_seguranca(self):
        r = self.calcular()
        self.assertEqual(r.valor("F10"), 198 * .9 * 7 * 9)
        self.assertEqual(r.valor("F11"), r.valor("F10") * .1)
        self.assertEqual(r.valor("E15"), r.valor("F10") + r.valor("F11") + 2000 + 500)

    def test_pessoal_encargos_refeicoes_alojamento_e_viagens(self):
        r = self.calcular()
        self.assertAlmostEqual(r.valor("L24"), .5 * 22 * 1.7 + 7.33333 * 30)
        self.assertAlmostEqual(r.valor("E31"), 9423.872052)
        self.assertAlmostEqual(r.valor("E37"), r.valor("E31") * 1.1)
        self.assertEqual((r.valor("G52"), r.valor("G53"), r.valor("E62"), r.valor("E71")), (1050, 440, 100, 0))

    def test_premios_sao_bloco_manual_sem_saida_no_total_de_pessoal(self):
        base = Dragagem()
        entradas = tuple(replace(x, valor=999) if x.celula == "E82" else x for x in base.entradas)
        antes, depois = self.calcular(base), self.calcular(Dragagem(entradas))
        self.assertEqual(antes.valor("G87"), depois.valor("G87"))

    def test_manutencao_depreciacao_e_apropriacoes(self):
        r = self.calcular()
        self.assertEqual((r.valor("E139"), r.valor("E140"), r.valor("E144")), (900, 1500, 2900))
        self.assertEqual((r.valor("E192"), r.valor("E193")), (2500, 1500))
        self.assertAlmostEqual(r.valor("E194"), r.valor("G181") * .005)

    def test_linha_recalque_tubulacao_flutuante_e_acoplamento(self):
        r = self.calcular()
        self.assertEqual((r.valor("K151"), r.valor("J154")), (37500, 3500))
        self.assertEqual((r.valor("K156"), r.valor("J159")), (7500, 700))
        self.assertAlmostEqual(r.valor("I161"), 250 / 12 + 2)
        self.assertAlmostEqual(r.valor("K167"), 4519.666666666667)

    def test_referencias_externas_afetam_somente_formulas_explicitas(self):
        base = self.calcular()
        alterado = self.calcular(canteiro=12000, operacao=50000, prazo=4.1)
        self.assertEqual(alterado.valor("E158"), 12000)
        self.assertEqual(alterado.valor("D245"), 50000)
        self.assertEqual(alterado.valor("D247"), 5)
        self.assertEqual(base.valor("D225"), alterado.valor("D225"))

    def test_arredondamento_aplica_se_somente_ao_prazo(self):
        r = self.calcular(prazo=3.0001)
        self.assertEqual(r.valor("D247"), 4)
        self.assertAlmostEqual(r.valor("I161"), 250 / 12 + 2)

    def test_divisoes_por_zero_e_entradas_incompletas_sao_seguras(self):
        entradas = tuple(replace(x, valor=0) if x.celula in {"I152", "I157", "I162", "J250", "J251"} else x for x in Dragagem().entradas)
        r = self.calcular(Dragagem(entradas), canteiro=None, operacao=None, prazo=None)
        for celula in ("J152", "J157", "J162", "L249", "J253", "D234"):
            self.assertIsNone(r.valor(celula))
        self.assertTrue(math.isfinite(r.valor("D222")))

    def test_valores_manuais_e_coincidencias_nao_sao_recalculados(self):
        entradas = tuple(replace(x, valor=321) if x.celula in {"D225", "D227", "D229", "E82"} else x for x in Dragagem().entradas)
        r = self.calcular(Dragagem(entradas))
        self.assertEqual(r.valor("D225"), 321)
        self.assertEqual(r.valor("D231"), 642)
        self.assertEqual(r.valor("E82"), 321)

    def test_invalidos_e_celulas_duplicadas_sao_rejeitados(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                EntradaDragagem("A1", "B", "D", valor)
        with self.assertRaises(ValueError):
            Dragagem((EntradaDragagem("A1", "B", "D", 1), EntradaDragagem("A1", "B", "E", 2)))

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(salvar_dragagem(versao, Dragagem()).sucesso)


class TestPersistenciaDragagem(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_preserva_telas_anteriores(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        anteriores = tuple(asdict(x) for x in (versao.canteiro, versao.fornecimento_bag, versao.operacao_sistema))
        alterada = Dragagem(tuple(replace(x, valor=321.5) if x.celula == "F12" else x for x in Dragagem().entradas))
        versao.registrar_dragagem(alterada)
        carregada = desserializar_versao(serializar_versao(orcamento, versao)).valor[1]
        self.assertEqual(asdict(carregada.dragagem), asdict(alterada))
        self.assertEqual(tuple(asdict(x) for x in (carregada.canteiro, carregada.fornecimento_bag, carregada.operacao_sistema)), anteriores)

    def test_serializacao_nao_persiste_resultados_derivados(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = json.loads(serializar_versao(orcamento, versao))["versao"]["dragagem"]
        self.assertEqual(set(dados), {"entradas"})
        persistidas = {item["celula"] for item in dados["entradas"]}
        self.assertTrue(persistidas.isdisjoint({celula for celula, _ in FORMULAS_DRAGAGEM}))

    def test_schema_14_sem_dragagem_continua_legivel(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 14
        documento["versao"].pop("dragagem")
        documento["versao"].pop("desmobilizacao_draga")
        documento["versao"].pop("desmobilizacao_equipamento_polimero")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(asdict(resultado.valor[1].dragagem), asdict(Dragagem()))

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["dragagem"]["entradas"][0]["valor"] = -1
        self.assertEqual(desserializar_versao(json.dumps(documento)).status, StatusPersistencia.DADO_CORROMPIDO)


class TestTelaDragagem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.dragagem")

    def _dominio(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra())
        return orcamento, versao

    def test_formulario_unico_renderiza_todos_os_campos_sem_operacao_remota(self):
        orcamento, versao = self._dominio(); falso, repositorio = StreamlitDragagemFalso(), Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repositorio, orcamento=orcamento, versao=versao, snapshot_esperado="s")
        self.assertEqual(falso.formularios, ["dragagem_formulario"])
        self.assertEqual(len(falso.campos), 104)
        self.assertGreaterEqual(len(falso.metricas), 88)
        repositorio.assert_not_called(); self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_uma_vez_e_faz_um_rerun(self):
        orcamento, versao = self._dominio(); falso = StreamlitDragagemFalso(salvar=True, valores={"dragagem_F12": 4321.5})
        repo = Mock(); repo.persistir_documento_versao.return_value = ResultadoPersistencia(StatusPersistencia.SUCESSO, commit_sha="novo")
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repo, orcamento=orcamento, versao=versao, snapshot_esperado="antigo")
        repo.persistir_documento_versao.assert_called_once()
        salva = repo.persistir_documento_versao.call_args.args[1]
        self.assertEqual({x.celula:x.valor for x in salva.dragagem.entradas}["F12"], 4321.5)
        self.assertEqual(falso.reruns, 1)

    def test_conflito_nao_atualiza_estado_nem_executa_rerun(self):
        orcamento, versao = self._dominio(); estado = {}; falso = StreamlitDragagemFalso(salvar=True, session_state=estado)
        repo = Mock(); repo.persistir_documento_versao.return_value = ResultadoPersistencia(StatusPersistencia.BRANCH_AVANCADA)
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repo, orcamento=orcamento, versao=versao, snapshot_esperado="antigo")
        self.assertEqual(falso.reruns, 0); self.assertNotIn("novo_orcamento_detalhe", estado)
