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
from modulos.orcamentos.aplicacao.preparacao_celula import salvar_preparacao_celula
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.preparacao_celula import (
    ComposicaoRealPreparacaoCelula, PreparacaoCelula, calcular_preparacao_celula,
)
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao


class ColunaFalsa:
    def __enter__(self): return self
    def __exit__(self, *args): return False


class StreamlitPreparacaoFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar, self.valores = salvar, valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios, self.campos, self.metricas, self.erros = [], [], [], []
        self.reruns = 0
    def form(self, chave): self.formularios.append(chave); return nullcontext()
    def form_submit_button(self, texto): return self.salvar and texto == "Salvar Preparação da Célula"
    def subheader(self, texto): pass
    def markdown(self, texto): pass
    def caption(self, texto): pass
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


class TestCalculosPreparacaoCelula(unittest.TestCase):
    def calcular(self, preparacao=None, horas=9):
        return calcular_preparacao_celula(preparacao or PreparacaoCelula(), horas)

    def test_fotografia_inicial_reproduz_tres_linhas_doze_itens_e_repeticao(self):
        p = PreparacaoCelula()
        self.assertEqual([x.descricao for x in p.equipe], ["Operador Líder", "Operador de Draga", "Ajudante Geral"])
        self.assertEqual(len(p.itens), 12)
        self.assertEqual(p.quantidade_repeticoes, 1)
        self.assertEqual(p.equipe[0].quantidade, 0)

    def test_horas_referenciam_dados_obra_e_d6_reproduz_d5(self):
        r = self.calcular(horas=8.5)
        self.assertEqual([x.horas_dia for x in r.mao_obra], [8.5, 8.5, 8.5])
        self.assertAlmostEqual(r.mao_obra[1].total, 1012.095)

    def test_mao_obra_refeicoes_transporte_e_custo_diario(self):
        r = self.calcular()
        self.assertEqual(r.mao_obra[0].total, 0)
        self.assertAlmostEqual(r.mao_obra[1].total, 1071.63)
        self.assertAlmostEqual(r.mao_obra[2].total, 420.714)
        self.assertEqual((r.quantidade_pessoas, r.total_refeicoes, r.total_transportes), (4, 120, 40))
        self.assertAlmostEqual(r.custo_por_dia, 1652.344)

    def test_composicao_real_reproduz_todas_as_relacoes_internas(self):
        c = self.calcular().composicao_real
        self.assertEqual(c.soma_pead, 1787)
        self.assertEqual(c.area_total, 2509)
        self.assertEqual(c.quantidade_pead, 2990)
        self.assertAlmostEqual(c.quantidade_bidim, 3713.32)
        self.assertAlmostEqual(c.quantidade_brita_base, 376.35)
        self.assertAlmostEqual(c.horas_retro, 57.707)
        self.assertAlmostEqual(c.horas_mao_obra, 57.707)
        self.assertAlmostEqual(c.dias_mao_obra, 5.7707)

    def test_quantidades_d20_d21_d23_d24_reproduzem_excel(self):
        itens = {x.id: x for x in self.calcular().itens}
        self.assertEqual(itens["pead"].quantidade, 2990)
        self.assertEqual(itens["mao-obra-pead"].quantidade, 2990)
        self.assertAlmostEqual(itens["bidim"].quantidade, 3713.32)
        self.assertAlmostEqual(itens["brita"].quantidade, 432.8025)

    def test_apenas_f15_f21_f22_calculam_quantidade_vezes_preco(self):
        itens = {x.id: x for x in self.calcular().itens}
        self.assertEqual(itens["preparo-terreno"].preco_total, 0)
        self.assertEqual(itens["mao-obra-pead"].preco_total, 11960)
        self.assertEqual(itens["taxa-mobilizacao-pead"].preco_total, 5000)
        for item in PreparacaoCelula().itens:
            if not item.preco_total_calculado:
                self.assertEqual(itens[item.id].preco_total, item.preco_total_manual)

    def test_f19_e_f26_sao_manuais_embora_e19_e_e26_referenciem_f10(self):
        base = PreparacaoCelula()
        alterada = replace(base, custo_refeicao=100)
        itens = {x.id: x for x in self.calcular(alterada).itens}
        self.assertNotEqual(itens["regularizacao-manual"].preco_unitario, 1652.344)
        self.assertEqual(itens["regularizacao-manual"].preco_total, 8261.72)
        self.assertEqual(itens["mao-obra-bidim-brita"].preco_total, 8261.72)

    def test_coincidencias_f17_f18_f20_f23_f24_f25_permanecem_manuais(self):
        base = PreparacaoCelula()
        alterados = tuple(
            replace(x, preco_unitario_manual=999) if x.id in {"aluguel-retro", "pead", "bidim", "brita"} else x
            for x in base.itens
        )
        r = {x.id: x for x in self.calcular(replace(base, itens=alterados)).itens}
        self.assertEqual(r["aluguel-retro"].preco_total, 3000)
        self.assertEqual(r["pead"].preco_total, 65780)
        self.assertEqual(r["bidim"].preco_total, 22279.92)
        self.assertEqual(r["brita"].preco_total, 43280.25)

    def test_total_repeticoes_e_preco_final(self):
        r = self.calcular()
        self.assertAlmostEqual(r.total, 177323.61)
        self.assertAlmostEqual(r.total_repeticoes, 177323.61)
        self.assertAlmostEqual(r.preco_final, 177323.61)
        r2 = self.calcular(replace(PreparacaoCelula(), quantidade_repeticoes=2.5))
        self.assertAlmostEqual(r2.preco_final, 443309.025)

    def test_entradas_vazias_e_decimais_sao_seguras(self):
        base = PreparacaoCelula()
        vazia = PreparacaoCelula(
            tuple(replace(x, quantidade=None, custo_hora=None, encargos_sociais=None) for x in base.equipe),
            None, None, ComposicaoRealPreparacaoCelula(**{x: None for x in ComposicaoRealPreparacaoCelula.__dataclass_fields__}),
            tuple(replace(x, quantidade_manual=None, preco_unitario_manual=None, preco_unitario_custo_diario=False, preco_total_calculado=False, preco_total_manual=None) for x in base.itens), None,
        )
        r = self.calcular(vazia, horas=None)
        for valor in (r.custo_por_dia, r.total, r.total_repeticoes, r.preco_final):
            self.assertTrue(math.isfinite(valor)); self.assertEqual(valor, 0)

    def test_invalidos_e_origens_duplicadas_sao_rejeitados(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                PreparacaoCelula(quantidade_repeticoes=valor)
        with self.assertRaises(ValueError):
            replace(PreparacaoCelula().itens[5], quantidade_manual=1)

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(salvar_preparacao_celula(versao, PreparacaoCelula()).sucesso)


class TestPersistenciaPreparacaoCelula(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_preserva_telas_anteriores(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        anteriores = tuple(asdict(x) for x in (
            versao.mobilizacao_draga, versao.mobilizacao_equipamento_polimero, versao.canteiro,
        ))
        alterada = replace(PreparacaoCelula(), custo_refeicao=45.75, quantidade_repeticoes=2.5)
        versao.registrar_preparacao_celula(alterada)
        carregada = desserializar_versao(serializar_versao(orcamento, versao)).valor[1]
        self.assertEqual(asdict(carregada.preparacao_celula), asdict(alterada))
        self.assertEqual(tuple(asdict(x) for x in (
            carregada.mobilizacao_draga, carregada.mobilizacao_equipamento_polimero, carregada.canteiro,
        )), anteriores)

    def test_serializacao_nao_persiste_resultados_derivados(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = json.loads(serializar_versao(orcamento, versao))["versao"]["preparacao_celula"]
        for nome in ("custo_por_dia", "area_total", "quantidade_pead", "total", "preco_final"):
            self.assertNotIn(nome, dados)

    def test_schema_11_sem_nova_aba_continua_legivel(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 11
        documento["versao"].pop("preparacao_celula")
        documento["versao"].pop("fornecimento_bag")
        documento["versao"].pop("operacao_sistema")
        documento["versao"].pop("dragagem")
        documento["versao"].pop("desmobilizacao_draga")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(asdict(resultado.valor[1].preparacao_celula), asdict(PreparacaoCelula()))

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["preparacao_celula"]["composicao_real"]["fator_pead"] = -1
        self.assertEqual(desserializar_versao(json.dumps(documento)).status, StatusPersistencia.DADO_CORROMPIDO)


class TestTelaPreparacaoCelula(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.preparacao_celula")

    def test_formulario_unico_renderiza_doze_itens_sem_operacao_remota(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra())
        falso, repositorio = StreamlitPreparacaoFalso(), Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repositorio, orcamento=orcamento, versao=versao, snapshot_esperado="s")
        self.assertEqual(falso.formularios, ["preparacao_celula_formulario"])
        self.assertEqual(len([x for x in falso.campos if x[0] == "Observação/Fonte"]), 12)
        repositorio.assert_not_called(); self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_uma_vez_preserva_canteiro_e_faz_um_rerun(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        canteiro = asdict(versao.canteiro)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(StatusPersistencia.SUCESSO, commit_sha="c")
        falso = StreamlitPreparacaoFalso(salvar=True, valores={"prep_celula_refeicao": 47.5, "prep_celula_quantidade_repeticoes": 2.0})
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repositorio, orcamento=orcamento, versao=versao, snapshot_esperado="original")
        repositorio.persistir_documento_versao.assert_called_once()
        _, salva, snapshot = repositorio.persistir_documento_versao.call_args.args
        self.assertEqual(snapshot, "original")
        self.assertEqual(salva.preparacao_celula.quantidade_repeticoes, 2)
        self.assertEqual(asdict(salva.canteiro), canteiro)
        self.assertEqual(falso.reruns, 1)


if __name__ == "__main__": unittest.main()
