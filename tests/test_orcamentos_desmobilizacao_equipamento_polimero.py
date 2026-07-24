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
from modulos.orcamentos.aplicacao.desmobilizacao_equipamento_polimero import (
    salvar_desmobilizacao_equipamento_polimero,
)
from modulos.orcamentos.dominio.barrilete import Barrilete, calcular_barrilete
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.desmobilizacao_equipamento_polimero import (
    DesmobilizacaoEquipamentoPolimero,
    FORMULAS_DESMOBILIZACAO_EQUIPAMENTO_POLIMERO,
    calcular_desmobilizacao_equipamento_polimero,
)
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao


class ColunaFalsa:
    def __enter__(self): return self
    def __exit__(self, *args): return False


class StreamlitDesmobilizacaoPolimeroFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar, self.valores = salvar, valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios, self.campos, self.metricas, self.erros = [], [], [], []
        self.reruns = 0
    def form(self, chave): self.formularios.append(chave); return nullcontext()
    def form_submit_button(self, texto):
        return (
            self.salvar
            and texto == "Salvar Desmobilização do Equipamento de Polímero"
        )
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


class TestCalculosDesmobilizacaoEquipamentoPolimero(unittest.TestCase):
    def calcular(self, desmobilizacao=None, horas=9, barrilete=5923.36):
        return calcular_desmobilizacao_equipamento_polimero(
            desmobilizacao or DesmobilizacaoEquipamentoPolimero(),
            horas,
            barrilete,
        )

    def test_fotografia_inicial_preserva_dois_funcionarios_e_nove_itens(self):
        d = DesmobilizacaoEquipamentoPolimero()
        self.assertEqual(len(d.equipe), 2)
        self.assertEqual(len(d.itens), 9)
        self.assertEqual([x.numero for x in d.itens], list(range(1, 10)))
        self.assertEqual(d.equipe[0].custo_hora, 15.15)
        self.assertEqual(d.itens[3].descricao, "Frete para mobilização do equipamento")
        self.assertEqual(d.itens[2].descricao, "Concreto para piso")
        self.assertEqual(d.bdi, 0)

    def test_lista_completa_das_vinte_e_tres_formulas(self):
        formulas = FORMULAS_DESMOBILIZACAO_EQUIPAMENTO_POLIMERO
        self.assertEqual(len(formulas), 23)
        self.assertEqual(formulas[0], ("D5", "='Dados Obra '!B26"))
        por_celula = dict(formulas)
        self.assertEqual(
            tuple((f"F{linha}", por_celula[f"F{linha}"]) for linha in range(14, 23)),
            tuple((f"F{linha}", f"=D{linha}*E{linha}") for linha in range(14, 23)),
        )
        self.assertIn(("E21", "=Barrilete!F31"), formulas)
        self.assertIn(("E22", "=F9"), formulas)
        self.assertEqual(formulas[-1], ("F26", "=SUM(F24:F25)"))

    def test_mao_de_obra_refeicoes_transporte_e_custo_diario(self):
        r = self.calcular()
        self.assertEqual([x.horas_dia for x in r.mao_obra], [9, 9])
        self.assertAlmostEqual(r.mao_obra[0].total, 572.67)
        self.assertAlmostEqual(r.mao_obra[1].total, 1051.785)
        self.assertEqual(r.quantidade_pessoas, 7)
        self.assertEqual(r.total_refeicoes, 210)
        self.assertEqual(r.total_transportes, 70)
        self.assertAlmostEqual(r.custo_por_dia, 1904.455)

    def test_formula_compartilhada_calcula_todos_os_nove_itens(self):
        itens = {x.id: x for x in self.calcular().itens}
        for id_ in (
            "cobertura-equipamento", "brita-piso", "concreto-piso",
            "instalacoes-hidraulicas", "instalacoes-eletricas",
            "maquina-wap", "barrilete",
        ):
            self.assertEqual(itens[id_].preco_total, 0)
        self.assertEqual(itens["frete-equipamento"].preco_total, 3000)
        self.assertAlmostEqual(itens["mao-obra-apoio"].preco_total, 3808.91)

    def test_referencias_externas_dados_obra_e_barrilete(self):
        base = self.calcular(horas=9, barrilete=5923.36)
        horas = self.calcular(horas=8.5, barrilete=5923.36)
        self.assertNotEqual(base.custo_por_dia, horas.custo_por_dia)
        self.assertNotEqual(base.itens[8].preco_total, horas.itens[8].preco_total)
        com_quantidade = replace(
            DesmobilizacaoEquipamentoPolimero(),
            itens=tuple(
                replace(x, quantidade=2) if x.id == "barrilete" else x
                for x in DesmobilizacaoEquipamentoPolimero().itens
            ),
        )
        r = self.calcular(com_quantidade, barrilete=7000)
        self.assertEqual(r.itens[7].preco_unitario, 7000)
        self.assertEqual(r.itens[7].preco_total, 14000)

    def test_totais_bdi_e_preco_final(self):
        r = self.calcular()
        self.assertAlmostEqual(r.total_composicao, 6808.91)
        self.assertEqual(r.valor_bdi, 0)
        self.assertAlmostEqual(r.preco_final, 6808.91)
        com_bdi = self.calcular(replace(DesmobilizacaoEquipamentoPolimero(), bdi=7.5))
        self.assertAlmostEqual(com_bdi.valor_bdi, com_bdi.total_composicao * .075)
        self.assertAlmostEqual(com_bdi.preco_final, com_bdi.total_composicao * 1.075)

    def test_vazios_manuais_permanecem_vazios_e_geram_zero_nas_formulas(self):
        d = DesmobilizacaoEquipamentoPolimero()
        for item in d.itens[:3]:
            self.assertIsNone(item.quantidade)
            self.assertIsNone(item.preco_unitario_manual)
        for item in d.itens[4:8]:
            self.assertIsNone(item.quantidade)
        r = self.calcular(d, horas=None, barrilete=None)
        self.assertTrue(all(math.isfinite(x.preco_total) for x in r.itens))

    def test_decimais_e_entradas_vazias_sao_seguras(self):
        base = DesmobilizacaoEquipamentoPolimero()
        vazio = DesmobilizacaoEquipamentoPolimero(
            tuple(
                replace(x, quantidade=None, custo_hora=None, encargos_sociais=None)
                for x in base.equipe
            ),
            None, None,
            tuple(
                replace(
                    x, quantidade=None, preco_unitario_manual=None,
                    preco_unitario_barrilete=False,
                    preco_unitario_custo_diario=False,
                )
                for x in base.itens
            ),
            None,
        )
        r = self.calcular(vazio, horas=None, barrilete=None)
        self.assertEqual((r.custo_por_dia, r.total_composicao, r.preco_final), (0, 0, 0))

    def test_invalidos_e_origens_duplicadas_sao_rejeitados(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                DesmobilizacaoEquipamentoPolimero(custo_refeicao=valor)
        with self.assertRaises(ValueError):
            replace(
                DesmobilizacaoEquipamentoPolimero().itens[7],
                preco_unitario_manual=1,
            )

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(salvar_desmobilizacao_equipamento_polimero(
            versao, DesmobilizacaoEquipamentoPolimero()
        ).sucesso)


class TestPersistenciaDesmobilizacaoEquipamentoPolimero(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_preserva_desmob_draga(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        desmob_draga = asdict(versao.desmobilizacao_draga)
        alterada = replace(
            DesmobilizacaoEquipamentoPolimero(), custo_refeicao=35.75
        )
        versao.registrar_desmobilizacao_equipamento_polimero(alterada)
        carregada = desserializar_versao(
            serializar_versao(orcamento, versao)
        ).valor[1]
        self.assertEqual(
            asdict(carregada.desmobilizacao_equipamento_polimero),
            asdict(alterada),
        )
        self.assertEqual(asdict(carregada.desmobilizacao_draga), desmob_draga)

    def test_serializacao_persiste_somente_entradas(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = json.loads(serializar_versao(
            orcamento, versao
        ))["versao"]["desmobilizacao_equipamento_polimero"]
        for nome in ("custo_por_dia", "total_composicao", "valor_bdi", "preco_final"):
            self.assertNotIn(nome, dados)

    def test_schema_16_sem_nova_aba_continua_legivel(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 16
        documento["versao"].pop("desmobilizacao_equipamento_polimero")
        documento["versao"].pop("medicao_orcamento")
        documento["versao"].pop("carga_transporte")
        documento["versao"].pop("planilha_precos")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(
            asdict(resultado.valor[1].desmobilizacao_equipamento_polimero),
            asdict(DesmobilizacaoEquipamentoPolimero()),
        )

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["desmobilizacao_equipamento_polimero"]["equipe"][0][
            "quantidade"
        ] = -1
        self.assertEqual(
            desserializar_versao(json.dumps(documento)).status,
            StatusPersistencia.DADO_CORROMPIDO,
        )


class TestTelaDesmobilizacaoEquipamentoPolimero(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module(
            "modulos.orcamentos.apresentacao.desmobilizacao_equipamento_polimero"
        )

    def _dominio(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra())
        return orcamento, versao

    def test_formulario_unico_sem_leitura_persistencia_ou_rerun_na_edicao(self):
        orcamento, versao = self._dominio()
        falso, repositorio = StreamlitDesmobilizacaoPolimeroFalso(), Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio, orcamento=orcamento, versao=versao,
                snapshot_esperado="s",
            )
        self.assertEqual(
            falso.formularios,
            ["desmobilizacao_equipamento_polimero_formulario"],
        )
        repositorio.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_referencias_externas_sao_calculadas_localmente(self):
        orcamento, versao = self._dominio()
        preco_barrilete = calcular_barrilete(
            Barrilete(), versao.dados_obra.horario_trabalho
        ).preco_final
        falso = StreamlitDesmobilizacaoPolimeroFalso()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=Mock(), orcamento=orcamento, versao=versao,
                snapshot_esperado="s",
            )
        self.assertIn(("Preço Unit.", f"R$ {preco_barrilete:,.2f}".replace(
            ",", "_"
        ).replace(".", ",").replace("_", ".")), falso.metricas)

    def test_salvar_persiste_uma_vez_preserva_desmob_draga_e_faz_rerun(self):
        orcamento, versao = self._dominio()
        desmob_draga = asdict(versao.desmobilizacao_draga)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="c"
        )
        falso = StreamlitDesmobilizacaoPolimeroFalso(
            salvar=True, valores={"desmob_eq_polimero_refeicao": 37.5}
        )
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio, orcamento=orcamento, versao=versao,
                snapshot_esperado="original",
            )
        repositorio.persistir_documento_versao.assert_called_once()
        _, salva, snapshot = repositorio.persistir_documento_versao.call_args.args
        self.assertEqual(snapshot, "original")
        self.assertEqual(
            salva.desmobilizacao_equipamento_polimero.custo_refeicao, 37.5
        )
        self.assertEqual(asdict(salva.desmobilizacao_draga), desmob_draga)
        self.assertEqual(falso.reruns, 1)

    def test_conflito_nao_atualiza_estado_nem_executa_rerun(self):
        orcamento, versao = self._dominio()
        estado = {}
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.BRANCH_AVANCADA
        )
        falso = StreamlitDesmobilizacaoPolimeroFalso(
            salvar=True, session_state=estado
        )
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio, orcamento=orcamento, versao=versao,
                snapshot_esperado="original",
            )
        self.assertEqual(falso.reruns, 0)
        self.assertNotIn("novo_orcamento_detalhe", estado)
        self.assertEqual(len(falso.erros), 1)


if __name__ == "__main__":
    unittest.main()
