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
from modulos.orcamentos.aplicacao.fornecimento_bag import salvar_fornecimento_bag
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.fornecimento_bag import (
    FornecimentoBag, MemorialFisicoBag, calcular_fornecimento_bag,
)
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao


class ColunaFalsa:
    def __enter__(self): return self
    def __exit__(self, *args): return False


class StreamlitBagFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar, self.valores = salvar, valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios, self.campos, self.metricas, self.erros = [], [], [], []
        self.reruns = 0
    def form(self, chave): self.formularios.append(chave); return nullcontext()
    def form_submit_button(self, texto): return self.salvar and texto == "Salvar Fornecimento de Bag"
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


class TestCalculosFornecimentoBag(unittest.TestCase):
    def calcular(self, fornecimento=None, horas=9):
        return calcular_fornecimento_bag(fornecimento or FornecimentoBag(), horas)

    def test_fotografia_inicial_reproduz_tres_linhas_onze_opcoes_e_doze_itens(self):
        f = FornecimentoBag()
        self.assertEqual(len(f.equipe), 3)
        self.assertEqual(len(f.opcoes), 11)
        self.assertEqual(len(f.itens), 12)
        self.assertEqual([x.numero for x in f.itens[:7]], [1, None, None, None, None, None, 2])
        self.assertIsNone(f.fator_preco_bag_6x30)

    def test_horas_referenciam_dados_obra_e_d6_reproduz_d5(self):
        r = self.calcular(horas=8.5)
        self.assertEqual([x.horas_dia for x in r.mao_obra], [8.5, 8.5, 8.5])

    def test_mao_obra_refeicoes_transporte_e_custo_diario(self):
        r = self.calcular()
        self.assertEqual(r.mao_obra[0].total, 0)
        self.assertAlmostEqual(r.mao_obra[1].total, 1071.63)
        self.assertAlmostEqual(r.mao_obra[2].total, 1051.785)
        self.assertEqual((r.quantidade_pessoas, r.total_refeicoes, r.total_transportes), (7, 210, 70))
        self.assertAlmostEqual(r.custo_por_dia, 2403.415)

    def test_memorial_fisico_calcula_tonelada_seca_e_volume(self):
        m = self.calcular().memorial_fisico
        self.assertEqual(m.tonelada_seca, 500)
        self.assertEqual(m.volume_material_bags, 2500)

    def test_memorial_fisico_nao_alimenta_quantidade_comercial(self):
        alterado = replace(FornecimentoBag(), memorial_fisico=MemorialFisicoBag(9999, 0.35, 0.42))
        antes = self.calcular()
        depois = self.calcular(alterado)
        self.assertNotEqual(antes.memorial_fisico.volume_material_bags, depois.memorial_fisico.volume_material_bags)
        self.assertEqual([x.quantidade for x in antes.itens], [x.quantidade for x in depois.itens])

    def test_somente_d41_d46_d47_e_f41_f46_f47_sao_calculados(self):
        r = {x.id: x for x in self.calcular().opcoes}
        self.assertEqual(r["bag-6x50"].volume_total, 0)
        self.assertEqual(r["bag-8x10"].volume_total, 0)
        self.assertEqual(r["bag-8x13"].volume_final, 0)
        self.assertEqual(r["bag-8x30"].volume_total, 2300)
        self.assertEqual(r["bag-8x15"].volume_final, 2250)

    def test_d42_f42_d49_f49_permanecem_manuais(self):
        base = FornecimentoBag()
        opcoes = tuple(
            replace(x, capacidade=999, quantidade_area=99, reinicio_celula=9)
            if x.id in {"bag-8x30", "bag-8x15"} else x for x in base.opcoes
        )
        r = {x.id: x for x in self.calcular(replace(base, opcoes=opcoes)).opcoes}
        self.assertEqual((r["bag-8x30"].volume_total, r["bag-8x30"].volume_final), (2300, 2300))
        self.assertEqual((r["bag-8x15"].volume_total, r["bag-8x15"].volume_final), (2250, 2250))

    def test_totais_do_memorial_reproduzem_excel(self):
        r = self.calcular()
        self.assertEqual(r.total_quantidade_area, 15)
        self.assertEqual(r.total_volume, 4550)
        self.assertEqual(r.total_volume_final, 4550)

    def test_quantidades_comerciais_e_unico_roundup(self):
        base = FornecimentoBag()
        opcoes = tuple(
            replace(x, quantidade_area=2.1, reinicio_celula=1.5)
            if x.id in {"bag-8x30", "bag-8x25"} else x for x in base.opcoes
        )
        itens = {x.id: x for x in self.calcular(replace(base, opcoes=opcoes)).itens}
        self.assertEqual(itens["bag-comercial-8x30"].quantidade, 4)
        self.assertAlmostEqual(itens["bag-comercial-8x25"].quantidade, 3.15)

    def test_precos_derivados_do_memorial_comercial(self):
        itens = {x.id: x for x in self.calcular().itens}
        self.assertEqual(itens["bag-comercial-8x10"].preco_unitario, 8550)
        self.assertEqual(itens["bag-comercial-8x13"].preco_unitario, 10830)
        self.assertEqual(itens["bag-comercial-8x30"].preco_unitario, 34500)
        self.assertEqual(itens["bag-comercial-8x25"].preco_unitario, 19500)

    def test_e23_preserva_referencia_a_h15_vazia_e_fator_1_1(self):
        itens = {x.id: x for x in self.calcular().itens}
        self.assertEqual(itens["bag-comercial-6x30"].preco_unitario, 0)
        alterado = replace(FornecimentoBag(), fator_preco_bag_6x30=2.5)
        itens = {x.id: x for x in self.calcular(alterado).itens}
        self.assertAlmostEqual(itens["bag-comercial-6x30"].preco_unitario, 340 * 2.5 * 1.1)

    def test_somente_f15_calcula_quantidade_vezes_preco(self):
        itens = {x.id: x for x in self.calcular().itens}
        self.assertEqual(itens["bag-comercial-8x10"].preco_total, 0)
        for item in FornecimentoBag().itens[1:]:
            self.assertEqual(itens[item.id].preco_total, item.preco_total_manual)

    def test_totais_manuais_nao_mudam_com_quantidade_ou_preco(self):
        base = FornecimentoBag()
        alterados = tuple(
            replace(x, quantidade_manual=99, preco_unitario_manual=999)
            if x.id == "bag-comercial-8x15" else x for x in base.itens
        )
        item = next(x for x in self.calcular(replace(base, itens=alterados)).itens if x.id == "bag-comercial-8x15")
        self.assertEqual(item.preco_total, 168750)

    def test_total_bdi_e_preco_final(self):
        r = self.calcular()
        self.assertAlmostEqual(r.total, 355460.245)
        self.assertEqual(r.valor_bdi, 0)
        self.assertAlmostEqual(r.preco_final, 355460.245)
        r2 = self.calcular(replace(FornecimentoBag(), bdi=10))
        self.assertAlmostEqual(r2.preco_final, 391006.2695)

    def test_entradas_vazias_e_decimais_sao_seguras(self):
        base = FornecimentoBag()
        vazio = FornecimentoBag(
            tuple(replace(x, quantidade=None, custo_hora=None, encargos_sociais=None) for x in base.equipe),
            None, None, MemorialFisicoBag(None, None, None),
            tuple(replace(x, capacidade=None, quantidade_area=None, volume_total_calculado=False, volume_total_manual=None, reinicio_celula=None, volume_final_calculado=False, volume_final_manual=None, preco_por_m3=None) for x in base.opcoes),
            None,
            tuple(replace(x, quantidade_manual=None, quantidade_opcao_id=None, preco_unitario_manual=None, preco_unitario_opcao_id=None, preco_unitario_bag_6x30=False, preco_unitario_custo_diario=False, preco_total_calculado=False, preco_total_manual=None) for x in base.itens),
            None,
        )
        r = self.calcular(vazio, horas=None)
        for valor in (r.custo_por_dia, r.total_volume, r.total, r.valor_bdi, r.preco_final):
            self.assertTrue(math.isfinite(valor)); self.assertEqual(valor, 0)
        self.assertIsNone(r.memorial_fisico.volume_material_bags)

    def test_valores_invalidos_e_origens_duplicadas_sao_rejeitados(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError): FornecimentoBag(bdi=valor)
        with self.assertRaises(ValueError):
            replace(FornecimentoBag().itens[0], quantidade_manual=1)

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(salvar_fornecimento_bag(versao, FornecimentoBag()).sucesso)


class TestPersistenciaFornecimentoBag(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_preserva_telas_anteriores(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        anteriores = tuple(asdict(x) for x in (
            versao.mobilizacao_equipamento_polimero, versao.canteiro, versao.preparacao_celula,
        ))
        alterado = replace(FornecimentoBag(), custo_refeicao=45.75, bdi=12.5)
        versao.registrar_fornecimento_bag(alterado)
        carregada = desserializar_versao(serializar_versao(orcamento, versao)).valor[1]
        self.assertEqual(asdict(carregada.fornecimento_bag), asdict(alterado))
        self.assertEqual(tuple(asdict(x) for x in (
            carregada.mobilizacao_equipamento_polimero, carregada.canteiro, carregada.preparacao_celula,
        )), anteriores)

    def test_serializacao_nao_persiste_resultados_derivados(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = json.loads(serializar_versao(orcamento, versao))["versao"]["fornecimento_bag"]
        for nome in ("tonelada_seca", "volume_material_bags", "total_volume", "total", "preco_final"):
            self.assertNotIn(nome, dados)

    def test_schema_12_sem_nova_aba_continua_legivel(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 12
        documento["versao"].pop("fornecimento_bag")
        documento["versao"].pop("operacao_sistema")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(asdict(resultado.valor[1].fornecimento_bag), asdict(FornecimentoBag()))

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["fornecimento_bag"]["memorial_fisico"]["volume"] = -1
        self.assertEqual(desserializar_versao(json.dumps(documento)).status, StatusPersistencia.DADO_CORROMPIDO)


class TestTelaFornecimentoBag(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.fornecimento_bag")

    def test_formulario_unico_renderiza_memoriais_sem_operacao_remota(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra())
        falso, repositorio = StreamlitBagFalso(), Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repositorio, orcamento=orcamento, versao=versao, snapshot_esperado="s")
        self.assertEqual(falso.formularios, ["fornecimento_bag_formulario"])
        self.assertTrue(any(x[0] == "Volume" for x in falso.campos))
        self.assertTrue(any(x[0] == "Capacidade" for x in falso.campos))
        repositorio.assert_not_called(); self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_uma_vez_preserva_preparacao_e_faz_um_rerun(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        preparacao = asdict(versao.preparacao_celula)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(StatusPersistencia.SUCESSO, commit_sha="c")
        falso = StreamlitBagFalso(salvar=True, valores={"forn_bag_refeicao": 47.5, "forn_bag_bdi": 8.25})
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repositorio, orcamento=orcamento, versao=versao, snapshot_esperado="original")
        repositorio.persistir_documento_versao.assert_called_once()
        _, salva, snapshot = repositorio.persistir_documento_versao.call_args.args
        self.assertEqual(snapshot, "original")
        self.assertEqual(salva.fornecimento_bag.bdi, 8.25)
        self.assertEqual(asdict(salva.preparacao_celula), preparacao)
        self.assertEqual(falso.reruns, 1)


if __name__ == "__main__": unittest.main()
