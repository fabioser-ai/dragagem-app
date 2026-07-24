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
from modulos.orcamentos.aplicacao.mobilizacao_equipamento_polimero import (
    salvar_mobilizacao_equipamento_polimero,
)
from modulos.orcamentos.dominio.barrilete import calcular_barrilete
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.mobilizacao_draga import MobilizacaoDraga
from modulos.orcamentos.dominio.mobilizacao_equipamento_polimero import (
    MobilizacaoEquipamentoPolimero,
    calcular_mobilizacao_equipamento_polimero,
)
from modulos.orcamentos.persistencia.contratos import (
    ResultadoPersistencia,
    StatusPersistencia,
)
from modulos.orcamentos.persistencia.serializacao import (
    desserializar_versao,
    serializar_versao,
)


class ColunaFalsa:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class StreamlitPolimeroFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar = salvar
        self.valores = valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios = []
        self.campos = []
        self.metricas = []
        self.erros = []
        self.reruns = 0

    def form(self, chave):
        self.formularios.append(chave)
        return nullcontext()

    def form_submit_button(self, texto):
        return self.salvar and texto == "Salvar Mobilização do Equipamento de Polímero"

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

    def columns(self, quantidade):
        return tuple(ColunaFalsa() for _ in range(quantidade))

    def number_input(self, rotulo, **kwargs):
        chave = kwargs["key"]
        self.campos.append((rotulo, chave, kwargs.get("value")))
        return self.valores.get(chave, kwargs.get("value"))

    def text_input(self, rotulo, **kwargs):
        chave = kwargs["key"]
        self.campos.append((rotulo, chave, kwargs.get("value")))
        return self.valores.get(chave, kwargs.get("value", ""))

    def metric(self, rotulo, valor):
        self.metricas.append((rotulo, valor))

    def rerun(self):
        self.reruns += 1


class TestCalculosMobilizacaoEquipamentoPolimero(unittest.TestCase):
    def calcular(self, mobilizacao=None, horas=9, barrilete=5923.36):
        return calcular_mobilizacao_equipamento_polimero(
            mobilizacao or MobilizacaoEquipamentoPolimero(), horas, barrilete
        )

    def test_fotografia_inicial_reproduz_duas_linhas_e_dez_itens(self):
        mobilizacao = MobilizacaoEquipamentoPolimero()
        self.assertEqual(
            [linha.descricao for linha in mobilizacao.equipe],
            ["Operador de Polimero", "Ajudante Geral"],
        )
        self.assertEqual(len(mobilizacao.itens), 10)
        self.assertEqual([item.numero for item in mobilizacao.itens], [1, 2, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(mobilizacao.custo_refeicao, 30)
        self.assertEqual(mobilizacao.custo_transporte, 10)
        self.assertEqual(mobilizacao.bdi, 0)

    def test_horas_referenciam_dados_obra_e_totais_de_mao_de_obra(self):
        resultado = self.calcular(horas=9)
        self.assertEqual([item.horas_dia for item in resultado.mao_obra], [9, 9])
        self.assertAlmostEqual(resultado.mao_obra[0].total, 1071.63)
        self.assertAlmostEqual(resultado.mao_obra[1].total, 420.714)

    def test_refeicoes_transporte_e_custo_diario_reproduzem_excel(self):
        resultado = self.calcular()
        self.assertEqual(resultado.quantidade_apoio, 4)
        self.assertEqual(resultado.total_refeicoes, 120)
        self.assertEqual(resultado.total_transportes, 40)
        self.assertAlmostEqual(resultado.custo_por_dia, 1652.344)

    def test_somente_f14_multiplica_quantidade_por_preco(self):
        resultado = self.calcular()
        totais = {item.id: item.preco_total for item in resultado.itens}
        self.assertEqual(totais["cobertura-equipamento"], 15000)
        for item in MobilizacaoEquipamentoPolimero().itens[1:]:
            self.assertEqual(totais[item.id], item.preco_total_manual)

    def test_coincidencias_numericas_permanecem_totais_manuais(self):
        itens = MobilizacaoEquipamentoPolimero().itens
        alterados = tuple(
            replace(item, quantidade=99, preco_unitario_manual=999)
            if item.id == "munck-cobertura" else item
            for item in itens
        )
        resultado = self.calcular(replace(MobilizacaoEquipamentoPolimero(), itens=alterados))
        munck = next(item for item in resultado.itens if item.id == "munck-cobertura")
        self.assertEqual(munck.preco_total, 2000)

    def test_barrilete_e_custo_diario_sao_referencias_externas_sem_recalcular_totais(self):
        resultado = self.calcular(horas=8.5, barrilete=1234.56)
        itens = {item.id: item for item in resultado.itens}
        self.assertEqual(itens["barrilete"].preco_unitario, 1234.56)
        self.assertEqual(itens["barrilete"].preco_total, 5923.36)
        self.assertAlmostEqual(itens["mao-obra-apoio"].preco_unitario, resultado.custo_por_dia)
        self.assertEqual(itens["mao-obra-apoio"].preco_total, 8261.72)

    def test_total_bdi_e_preco_final_reproduzem_excel(self):
        resultado = self.calcular()
        self.assertAlmostEqual(resultado.total_composicao, 39925.08)
        self.assertEqual(resultado.valor_bdi, 0)
        self.assertAlmostEqual(resultado.preco_final, 39925.08)
        com_bdi = self.calcular(replace(MobilizacaoEquipamentoPolimero(), bdi=10))
        self.assertAlmostEqual(com_bdi.valor_bdi, 3992.508)
        self.assertAlmostEqual(com_bdi.preco_final, 43917.588)

    def test_entradas_vazias_e_decimais_nao_geram_nan_ou_infinito(self):
        base = MobilizacaoEquipamentoPolimero()
        vazia = MobilizacaoEquipamentoPolimero(
            tuple(replace(item, quantidade=None, custo_hora=None, encargos_sociais=None) for item in base.equipe),
            None,
            0,
            tuple(
                replace(
                    item, quantidade=None, preco_unitario_manual=None,
                    preco_unitario_barrilete=False, preco_unitario_custo_diario=False,
                    preco_total_calculado=False, preco_total_manual=None,
                )
                for item in base.itens
            ),
            None,
        )
        resultado = self.calcular(vazia, horas=None, barrilete=None)
        for valor in (
            resultado.quantidade_apoio, resultado.total_refeicoes,
            resultado.total_transportes, resultado.custo_por_dia,
            resultado.total_composicao, resultado.valor_bdi, resultado.preco_final,
        ):
            self.assertTrue(math.isfinite(valor))
            self.assertEqual(valor, 0)

    def test_negativo_nan_infinito_e_origens_duplicadas_sao_rejeitados(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                MobilizacaoEquipamentoPolimero(custo_refeicao=valor)
        with self.assertRaises(ValueError):
            replace(
                MobilizacaoEquipamentoPolimero().itens[0],
                preco_unitario_barrilete=True,
            )

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        resultado = salvar_mobilizacao_equipamento_polimero(
            versao, MobilizacaoEquipamentoPolimero()
        )
        self.assertFalse(resultado.sucesso)


class TestPersistenciaMobilizacaoEquipamentoPolimero(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_preserva_telas_anteriores(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra(objeto="Obra"))
        anteriores = (
            asdict(versao.dados_obra), asdict(versao.cotacoes),
            asdict(versao.producao), asdict(versao.barrilete),
            asdict(versao.mobilizacao_draga),
        )
        base = MobilizacaoEquipamentoPolimero()
        alterada = replace(
            base, custo_refeicao=45.75, bdi=12.5,
            itens=(replace(base.itens[0], quantidade=2.5, observacao="Fonte A"),) + base.itens[1:],
        )
        versao.registrar_mobilizacao_equipamento_polimero(alterada)
        resultado = desserializar_versao(serializar_versao(orcamento, versao))
        self.assertTrue(resultado.sucesso)
        carregada = resultado.valor[1]
        self.assertEqual(asdict(carregada.mobilizacao_equipamento_polimero), asdict(alterada))
        self.assertEqual(
            (
                asdict(carregada.dados_obra), asdict(carregada.cotacoes),
                asdict(carregada.producao), asdict(carregada.barrilete),
                asdict(carregada.mobilizacao_draga),
            ),
            anteriores,
        )

    def test_serializacao_nao_persiste_resultados_derivados(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = json.loads(serializar_versao(orcamento, versao))["versao"][
            "mobilizacao_equipamento_polimero"
        ]
        for derivado in ("horas_dia", "custo_por_dia", "total_composicao", "valor_bdi", "preco_final"):
            self.assertNotIn(derivado, dados)

    def test_schema_9_sem_nova_aba_continua_legivel_com_padrao(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 9
        documento["versao"].pop("mobilizacao_equipamento_polimero")
        documento["versao"].pop("canteiro")
        documento["versao"].pop("preparacao_celula")
        documento["versao"].pop("fornecimento_bag")
        documento["versao"].pop("operacao_sistema")
        documento["versao"].pop("dragagem")
        documento["versao"].pop("desmobilizacao_draga")
        documento["versao"].pop("desmobilizacao_equipamento_polimero")
        documento["versao"].pop("medicao_orcamento")
        documento["versao"].pop("carga_transporte")
        documento["versao"].pop("planilha_precos")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(
            asdict(resultado.valor[1].mobilizacao_equipamento_polimero),
            asdict(MobilizacaoEquipamentoPolimero()),
        )

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["mobilizacao_equipamento_polimero"]["equipe"][0]["quantidade"] = -1
        resultado = desserializar_versao(json.dumps(documento))
        self.assertEqual(resultado.status, StatusPersistencia.DADO_CORROMPIDO)


class TestTelaMobilizacaoEquipamentoPolimero(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module(
            "modulos.orcamentos.apresentacao.mobilizacao_equipamento_polimero"
        )

    def _dominio(self):
        return criar_orcamento_vazio("Fabio").valor

    def test_um_formulario_dez_itens_e_referencias_externas_renderizadas(self):
        orcamento, versao = self._dominio()
        versao.registrar_dados_obra(DadosObra())
        falso = StreamlitPolimeroFalso()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=Mock(), orcamento=orcamento, versao=versao,
                snapshot_esperado="snapshot",
            )
        self.assertEqual(falso.formularios, ["mobilizacao_equipamento_polimero_formulario"])
        observacoes = [item for item in falso.campos if item[0] == "Observação/Fonte"]
        self.assertEqual(len(observacoes), 10)
        self.assertIn(("Custo por dia", "R$ 1.652,34"), falso.metricas)
        self.assertTrue(any(rotulo == "Preço Unit." and valor == "R$ 5.923,36" for rotulo, valor in falso.metricas))

    def test_edicao_sem_envio_faz_zero_operacoes_remotas_e_reruns(self):
        orcamento, versao = self._dominio()
        falso = StreamlitPolimeroFalso()
        repositorio = Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio, orcamento=orcamento, versao=versao,
                snapshot_esperado="snapshot",
            )
        repositorio.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_uma_vez_preserva_mob_draga_e_faz_um_rerun(self):
        orcamento, versao = self._dominio()
        mob_draga_anterior = asdict(versao.mobilizacao_draga)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="commit-polimero"
        )
        falso = StreamlitPolimeroFalso(
            salvar=True,
            valores={"mob_eq_polimero_refeicao": 47.5, "mob_eq_polimero_bdi": 8.25},
        )
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio, orcamento=orcamento, versao=versao,
                snapshot_esperado="snapshot-original",
            )
        repositorio.persistir_documento_versao.assert_called_once()
        _, salva, snapshot = repositorio.persistir_documento_versao.call_args.args
        self.assertEqual(snapshot, "snapshot-original")
        self.assertEqual(salva.mobilizacao_equipamento_polimero.custo_refeicao, 47.5)
        self.assertEqual(salva.mobilizacao_equipamento_polimero.bdi, 8.25)
        self.assertEqual(asdict(salva.mobilizacao_draga), mob_draga_anterior)
        repositorio.carregar_indice.assert_not_called()
        repositorio.carregar_indice_bruto.assert_not_called()
        repositorio.carregar_snapshot.assert_not_called()
        repositorio.carregar_versao.assert_not_called()
        self.assertEqual(falso.reruns, 1)


if __name__ == "__main__":
    unittest.main()
