import importlib
import json
import math
import sys
import types
import unittest
from contextlib import nullcontext
from dataclasses import asdict, replace
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.canteiro import salvar_canteiro
from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.dominio.canteiro import Canteiro, calcular_canteiro
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.producao import calcular_producao
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao


class ColunaFalsa:
    def __enter__(self): return self
    def __exit__(self, *args): return False


class StreamlitCanteiroFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar = salvar
        self.valores = valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios, self.campos, self.metricas, self.erros = [], [], [], []
        self.reruns = 0

    def form(self, chave): self.formularios.append(chave); return nullcontext()
    def form_submit_button(self, texto): return self.salvar and texto == "Salvar Canteiro"
    def subheader(self, texto): pass
    def markdown(self, texto): pass
    def caption(self, texto): pass
    def success(self, texto): pass
    def error(self, texto): self.erros.append(texto)
    def columns(self, quantidade): return tuple(ColunaFalsa() for _ in range(quantidade))
    def number_input(self, rotulo, **kwargs):
        chave = kwargs["key"]
        self.campos.append((rotulo, chave, kwargs.get("value")))
        return self.valores.get(chave, kwargs.get("value"))
    def text_input(self, rotulo, **kwargs):
        chave = kwargs["key"]
        self.campos.append((rotulo, chave, kwargs.get("value")))
        return self.valores.get(chave, kwargs.get("value", ""))
    def metric(self, rotulo, valor): self.metricas.append((rotulo, valor))
    def rerun(self): self.reruns += 1


class TestCalculosCanteiro(unittest.TestCase):
    def calcular(self, canteiro=None, prazo=2.33819678265058):
        return calcular_canteiro(canteiro or Canteiro(), prazo)

    def test_fotografia_inicial_reproduz_tres_linhas_e_treze_itens(self):
        canteiro = Canteiro()
        self.assertEqual([x.descricao for x in canteiro.equipe], ["", "Operador de Draga", "Ajudante Geral"])
        self.assertEqual(len(canteiro.itens), 13)
        self.assertEqual(canteiro.equipe[0].quantidade, None)
        self.assertEqual(canteiro.equipe[0].custo_hora, 30)
        self.assertEqual(canteiro.bdi, 1)

    def test_formulas_de_mao_de_obra_refeicoes_transporte_e_total_diario(self):
        resultado = self.calcular()
        self.assertEqual(resultado.mao_obra[0].total, 0)
        self.assertAlmostEqual(resultado.mao_obra[1].total, 1071.63)
        self.assertAlmostEqual(resultado.mao_obra[2].total, 420.714)
        self.assertEqual(resultado.quantidade_pessoas, 4)
        self.assertEqual(resultado.total_refeicoes, 120)
        self.assertEqual(resultado.total_transportes, 40)
        self.assertAlmostEqual(resultado.custo_por_dia, 1652.344)

    def test_referencia_externa_producao_d24_e_arredondada_para_cima(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra())
        dados = versao.dados_obra
        prazo = calcular_producao(
            versao.producao, dados.horario_trabalho, dados.dias_trabalho, dados.volume_dragagem
        ).prazo_meses
        resultado = self.calcular(prazo=prazo)
        self.assertEqual(resultado.prazo_arredondado, 3)
        itens = {x.id: x for x in resultado.itens}
        self.assertEqual(itens["container-almoxarifado"].quantidade, 3)

    def test_referencias_internas_de_quantidade_reproduzem_excel(self):
        itens = {x.id: x for x in self.calcular().itens}
        self.assertEqual(itens["agua-potavel"].quantidade, 12)
        self.assertEqual(itens["material-escritorio"].quantidade, 3)
        self.assertEqual(itens["banheiro-quimico"].quantidade, 3)
        self.assertEqual(itens["exames-medicos"].quantidade, 4)

    def test_somente_container_almoxarifado_calcula_quantidade_vezes_preco(self):
        itens = {x.id: x for x in self.calcular().itens}
        self.assertEqual(itens["container-almoxarifado"].preco_total, 3000)
        for item in Canteiro().itens[1:]:
            self.assertEqual(itens[item.id].preco_total, item.preco_total_manual)

    def test_coincidencias_numericas_permanecem_manuais(self):
        base = Canteiro()
        alterados = tuple(
            replace(x, preco_unitario_manual=999) if x.id == "agua-potavel" else x
            for x in base.itens
        )
        resultado = self.calcular(replace(base, itens=alterados))
        agua = next(x for x in resultado.itens if x.id == "agua-potavel")
        self.assertEqual(agua.preco_total, 240)

    def test_integracao_referencia_f10_apenas_no_preco_unitario(self):
        resultado = self.calcular()
        integracao = next(x for x in resultado.itens if x.id == "mao-obra-integracao")
        self.assertAlmostEqual(integracao.preco_unitario, 1652.344)
        self.assertEqual(integracao.preco_total, 4957.032)

    def test_total_prazo_preco_unitario_bdi_e_final_reproduzem_excel(self):
        resultado = self.calcular()
        self.assertAlmostEqual(resultado.total_composicao, 19157.032)
        self.assertEqual(resultado.prazo_operacao, 2)
        self.assertAlmostEqual(resultado.preco_unitario, 9578.516)
        self.assertAlmostEqual(resultado.valor_bdi, 95.78516)
        self.assertAlmostEqual(resultado.preco_final, 9674.30116)

    def test_entradas_vazias_e_decimais_sao_seguras(self):
        base = Canteiro()
        vazio = Canteiro(
            tuple(replace(x, quantidade=None, custo_hora=None, horas_dia=None, encargos_sociais=None) for x in base.equipe),
            None, None,
            tuple(replace(x, quantidade_manual=None, preco_unitario_manual=None, preco_total_manual=None, preco_total_calculado=False, preco_unitario_custo_diario=False) for x in base.itens),
            None,
        )
        resultado = self.calcular(vazio, prazo=None)
        for valor in (resultado.custo_por_dia, resultado.total_composicao, resultado.valor_bdi, resultado.preco_final):
            self.assertTrue(math.isfinite(valor))
            self.assertEqual(valor, 0)
        self.assertIsNone(resultado.preco_unitario)

    def test_valores_invalidos_e_origens_duplicadas_sao_rejeitados(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                Canteiro(bdi=valor)
        with self.assertRaises(ValueError):
            replace(Canteiro().itens[0], quantidade_manual=1)

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(salvar_canteiro(versao, Canteiro()).sucesso)


class TestPersistenciaCanteiro(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_preserva_telas_anteriores(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        anteriores = tuple(asdict(x) for x in (
            versao.cotacoes, versao.producao, versao.barrilete,
            versao.mobilizacao_draga, versao.mobilizacao_equipamento_polimero,
        ))
        alterado = replace(Canteiro(), custo_refeicao=45.75, bdi=12.5)
        versao.registrar_canteiro(alterado)
        resultado = desserializar_versao(serializar_versao(orcamento, versao))
        self.assertTrue(resultado.sucesso)
        carregada = resultado.valor[1]
        self.assertEqual(asdict(carregada.canteiro), asdict(alterado))
        self.assertEqual(tuple(asdict(x) for x in (
            carregada.cotacoes, carregada.producao, carregada.barrilete,
            carregada.mobilizacao_draga, carregada.mobilizacao_equipamento_polimero,
        )), anteriores)

    def test_serializacao_nao_persiste_resultados_derivados(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = json.loads(serializar_versao(orcamento, versao))["versao"]["canteiro"]
        for derivado in ("prazo_arredondado", "custo_por_dia", "total_composicao", "preco_final"):
            self.assertNotIn(derivado, dados)

    def test_schema_10_sem_canteiro_continua_legivel_com_padrao(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 10
        documento["versao"].pop("canteiro")
        documento["versao"].pop("preparacao_celula")
        documento["versao"].pop("fornecimento_bag")
        documento["versao"].pop("operacao_sistema")
        documento["versao"].pop("dragagem")
        documento["versao"].pop("desmobilizacao_draga")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(asdict(resultado.valor[1].canteiro), asdict(Canteiro()))

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["canteiro"]["equipe"][0]["horas_dia"] = -1
        self.assertEqual(
            desserializar_versao(json.dumps(documento)).status,
            StatusPersistencia.DADO_CORROMPIDO,
        )


class TestTelaCanteiro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.canteiro")

    def test_formulario_renderiza_treze_itens_sem_operacao_remota(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra())
        falso, repositorio = StreamlitCanteiroFalso(), Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repositorio, orcamento=orcamento, versao=versao, snapshot_esperado="s")
        self.assertEqual(falso.formularios, ["canteiro_formulario"])
        self.assertEqual(len([x for x in falso.campos if x[0] == "Observação/Fonte"]), 13)
        repositorio.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_uma_vez_preserva_polimero_e_faz_um_rerun(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        polimero = asdict(versao.mobilizacao_equipamento_polimero)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="commit-canteiro"
        )
        falso = StreamlitCanteiroFalso(salvar=True, valores={"canteiro_refeicao": 47.5, "canteiro_bdi": 8.25})
        with patch.object(self.tela, "st", falso):
            self.tela.render(repositorio=repositorio, orcamento=orcamento, versao=versao, snapshot_esperado="original")
        repositorio.persistir_documento_versao.assert_called_once()
        _, salva, snapshot = repositorio.persistir_documento_versao.call_args.args
        self.assertEqual(snapshot, "original")
        self.assertEqual(salva.canteiro.custo_refeicao, 47.5)
        self.assertEqual(asdict(salva.mobilizacao_equipamento_polimero), polimero)
        self.assertEqual(falso.reruns, 1)


if __name__ == "__main__":
    unittest.main()
