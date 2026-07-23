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
from modulos.orcamentos.aplicacao.desmobilizacao_draga import salvar_desmobilizacao_draga
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.desmobilizacao_draga import (
    DesmobilizacaoDraga,
    FORMULAS_DESMOBILIZACAO_DRAGA,
    calcular_desmobilizacao_draga,
)
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.serializacao import desserializar_versao, serializar_versao


class ColunaFalsa:
    def __enter__(self): return self
    def __exit__(self, *args): return False


class StreamlitDesmobilizacaoFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar, self.valores = salvar, valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios, self.campos, self.metricas, self.erros = [], [], [], []
        self.reruns = 0
    def form(self, chave): self.formularios.append(chave); return nullcontext()
    def form_submit_button(self, texto):
        return self.salvar and texto == "Salvar Desmobilização da Draga"
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


class TestCalculosDesmobilizacaoDraga(unittest.TestCase):
    def calcular(self, desmobilizacao=None, horas=9):
        return calcular_desmobilizacao_draga(
            desmobilizacao or DesmobilizacaoDraga(), horas
        )

    def test_fotografia_inicial_preserva_estrutura_e_particularidades(self):
        d = DesmobilizacaoDraga()
        self.assertEqual(len(d.equipe), 2)
        self.assertEqual(len(d.itens), 5)
        self.assertEqual([x.numero for x in d.itens], [1, 2, 3, 5, None])
        self.assertIsNone(d.itens[0].quantidade)
        self.assertIsNone(d.itens[0].preco_unitario_manual)
        self.assertEqual(d.itens[1].observacao, "Fabiano 23/03/2026")
        self.assertEqual(d.itens[1].descricao, d.itens[4].descricao)
        self.assertEqual(d.bdi, 0)

    def test_lista_completa_das_dezoito_formulas_e_exata(self):
        self.assertEqual(len(FORMULAS_DESMOBILIZACAO_DRAGA), 18)
        self.assertEqual(FORMULAS_DESMOBILIZACAO_DRAGA[0], ("D5", "='Dados Obra '!B26"))
        self.assertEqual(FORMULAS_DESMOBILIZACAO_DRAGA[-1], ("F21", "=SUM(F19:F20)"))
        self.assertEqual(len({celula for celula, _ in FORMULAS_DESMOBILIZACAO_DRAGA}), 18)

    def test_referencia_externa_horas_e_formulas_da_mao_de_obra(self):
        r = self.calcular(horas=9)
        self.assertEqual([x.horas_dia for x in r.mao_obra], [9, 9])
        self.assertAlmostEqual(r.mao_obra[0].total, 1071.63)
        self.assertAlmostEqual(r.mao_obra[1].total, 1051.785)

    def test_refeicoes_transporte_e_custo_por_dia(self):
        r = self.calcular()
        self.assertEqual(r.quantidade_pessoas, 7)
        self.assertEqual(r.total_refeicoes, 210)
        self.assertEqual(r.total_transportes, 70)
        self.assertAlmostEqual(r.custo_por_dia, 2403.415)

    def test_todas_as_formulas_dos_itens_totais_e_bdi(self):
        r = self.calcular()
        itens = {x.id: x for x in r.itens}
        self.assertEqual(itens["cobertura-equipamento"].preco_total, 0)
        self.assertEqual(itens["frete-equipamento"].preco_total, 2600)
        self.assertAlmostEqual(itens["mao-obra-desmontagem"].preco_unitario, 2403.415)
        self.assertAlmostEqual(itens["mao-obra-desmontagem"].preco_total, 7210.245)
        self.assertEqual(itens["guindaste-desmontagem"].preco_total, 3500)
        self.assertEqual(itens["frete-repetido"].preco_total, 4000)
        self.assertAlmostEqual(r.total_composicao, 17310.245)
        self.assertEqual(r.valor_bdi, 0)
        self.assertAlmostEqual(r.preco_final, 17310.245)

    def test_bdi_manual_decimal_recalcula_somente_acrescimo_e_final(self):
        base = DesmobilizacaoDraga()
        r = self.calcular(replace(base, bdi=7.5))
        self.assertAlmostEqual(r.valor_bdi, r.total_composicao * .075)
        self.assertAlmostEqual(r.preco_final, r.total_composicao * 1.075)

    def test_referencia_externa_altera_somente_derivados_dependentes(self):
        base, alterado = self.calcular(horas=9), self.calcular(horas=8.5)
        self.assertNotEqual(base.custo_por_dia, alterado.custo_por_dia)
        self.assertNotEqual(
            base.itens[2].preco_total, alterado.itens[2].preco_total
        )
        self.assertEqual(base.itens[1].preco_total, alterado.itens[1].preco_total)

    def test_entradas_vazias_e_decimais_sao_seguras(self):
        base = DesmobilizacaoDraga()
        vazio = DesmobilizacaoDraga(
            tuple(replace(x, quantidade=None, custo_hora=None, encargos_sociais=None) for x in base.equipe),
            None, None,
            tuple(replace(
                x, quantidade=None, preco_unitario_manual=None,
                preco_unitario_custo_diario=False,
            ) for x in base.itens),
            None,
        )
        r = self.calcular(vazio, horas=None)
        for valor in (r.custo_por_dia, r.total_composicao, r.preco_final):
            self.assertEqual(valor, 0)
            self.assertTrue(math.isfinite(valor))

    def test_valores_invalidos_sao_rejeitados(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                DesmobilizacaoDraga(custo_refeicao=valor)
        with self.assertRaises(ValueError):
            replace(DesmobilizacaoDraga().itens[2], preco_unitario_manual=1)

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(
            salvar_desmobilizacao_draga(versao, DesmobilizacaoDraga()).sucesso
        )


class TestPersistenciaDesmobilizacaoDraga(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_preserva_dragagem(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dragagem = asdict(versao.dragagem)
        alterada = replace(DesmobilizacaoDraga(), custo_refeicao=35.75)
        versao.registrar_desmobilizacao_draga(alterada)
        carregada = desserializar_versao(
            serializar_versao(orcamento, versao)
        ).valor[1]
        self.assertEqual(asdict(carregada.desmobilizacao_draga), asdict(alterada))
        self.assertEqual(asdict(carregada.dragagem), dragagem)

    def test_serializacao_persiste_somente_entradas(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = json.loads(serializar_versao(
            orcamento, versao
        ))["versao"]["desmobilizacao_draga"]
        for nome in ("custo_por_dia", "total_composicao", "valor_bdi", "preco_final"):
            self.assertNotIn(nome, dados)

    def test_schema_15_sem_nova_aba_continua_legivel(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 15
        documento["versao"].pop("desmobilizacao_draga")
        documento["versao"].pop("desmobilizacao_equipamento_polimero")
        documento["versao"].pop("medicao_orcamento")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(
            asdict(resultado.valor[1].desmobilizacao_draga),
            asdict(DesmobilizacaoDraga()),
        )

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["desmobilizacao_draga"]["equipe"][0]["quantidade"] = -1
        self.assertEqual(
            desserializar_versao(json.dumps(documento)).status,
            StatusPersistencia.DADO_CORROMPIDO,
        )


class TestTelaDesmobilizacaoDraga(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module(
            "modulos.orcamentos.apresentacao.desmobilizacao_draga"
        )

    def _dominio(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra())
        return orcamento, versao

    def test_formulario_unico_sem_persistencia_ou_rerun_durante_edicao(self):
        orcamento, versao = self._dominio()
        falso, repositorio = StreamlitDesmobilizacaoFalso(), Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio, orcamento=orcamento, versao=versao,
                snapshot_esperado="s",
            )
        self.assertEqual(falso.formularios, ["desmobilizacao_draga_formulario"])
        self.assertEqual(len([x for x in falso.campos if x[0] == "Observação/Fonte"]), 5)
        repositorio.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_uma_vez_preserva_dragagem_e_faz_um_rerun(self):
        orcamento, versao = self._dominio()
        dragagem = asdict(versao.dragagem)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="c"
        )
        falso = StreamlitDesmobilizacaoFalso(
            salvar=True, valores={"desmob_draga_refeicao": 37.5}
        )
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio, orcamento=orcamento, versao=versao,
                snapshot_esperado="original",
            )
        repositorio.persistir_documento_versao.assert_called_once()
        _, salva, snapshot = repositorio.persistir_documento_versao.call_args.args
        self.assertEqual(snapshot, "original")
        self.assertEqual(salva.desmobilizacao_draga.custo_refeicao, 37.5)
        self.assertEqual(asdict(salva.dragagem), dragagem)
        self.assertEqual(falso.reruns, 1)

    def test_conflito_nao_atualiza_estado_nem_executa_rerun(self):
        orcamento, versao = self._dominio()
        estado = {}
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.BRANCH_AVANCADA
        )
        falso = StreamlitDesmobilizacaoFalso(salvar=True, session_state=estado)
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
