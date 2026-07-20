import importlib
import json
import sys
import types
import unittest
from contextlib import nullcontext
from dataclasses import asdict, replace
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.barrilete import salvar_barrilete
from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.dominio.barrilete import (
    Barrilete,
    ItemBarrilete,
    calcular_barrilete,
)
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.producao import Producao
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


class StreamlitBarrileteFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar = salvar
        self.valores = valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios = []
        self.campos = []
        self.metricas = []
        self.erros = []
        self.sucessos = []
        self.reruns = 0

    def form(self, chave):
        self.formularios.append(chave)
        return nullcontext()

    def form_submit_button(self, texto):
        return self.salvar and texto == "Salvar Barrilete"

    def subheader(self, texto):
        pass

    def markdown(self, texto):
        pass

    def caption(self, texto):
        pass

    def columns(self, quantidade):
        return tuple(ColunaFalsa() for _ in range(quantidade))

    def number_input(self, rotulo, **kwargs):
        chave = kwargs["key"]
        self.campos.append((rotulo, chave, kwargs.get("value")))
        return self.valores.get(chave, kwargs.get("value"))

    def metric(self, rotulo, valor):
        self.metricas.append((rotulo, valor))

    def error(self, texto):
        self.erros.append(texto)

    def success(self, texto):
        self.sucessos.append(texto)

    def rerun(self):
        self.reruns += 1


class TestDominioBarrilete(unittest.TestCase):
    def test_valores_iniciais_reproduzem_celulas_do_excel(self):
        barrilete = Barrilete()
        self.assertEqual(
            (
                barrilete.quantidade_operadores,
                barrilete.custo_hora_operador,
                barrilete.encargos_operador,
                barrilete.quantidade_ajudantes,
                barrilete.custo_hora_ajudante,
                barrilete.encargos_ajudante,
                barrilete.custo_refeicao,
                barrilete.custo_transporte,
                barrilete.bdi,
            ),
            (2, 23, 110, 2, 10, 110, 30, 10, None),
        )
        self.assertEqual(len(barrilete.itens), 13)
        self.assertEqual([item.quantidade for item in barrilete.itens], [6, 8, 8, 6, 6, 1, 1, 4, 200, 24, 4, 2, 1])

    def test_precos_unitarios_reproduzem_formulas_e_valores_do_excel(self):
        precos = [item.preco_unitario for item in Barrilete().itens]
        esperados = [560, 231, 231, 308, 77, 49, 2800, 1540, 30, 19.6, 49, 84, 3000]
        for obtido, esperado in zip(precos, esperados):
            self.assertAlmostEqual(obtido, esperado)

    def test_formulas_de_mao_de_obra_totais_depreciacao_bdi_e_preco_final(self):
        resultado = calcular_barrilete(Barrilete(), 9)
        self.assertAlmostEqual(resultado.total_operadores, 869.4)
        self.assertAlmostEqual(resultado.total_ajudantes, 378)
        self.assertEqual(resultado.quantidade_apoio, 4)
        self.assertEqual(resultado.total_refeicoes, 120)
        self.assertEqual(resultado.total_transporte, 40)
        self.assertAlmostEqual(resultado.custo_por_dia, 1407.4)
        self.assertAlmostEqual(resultado.total_composicao, 29616.8)
        self.assertAlmostEqual(resultado.depreciacao, 5923.36)
        self.assertEqual(resultado.valor_bdi, 0)
        self.assertAlmostEqual(resultado.preco_final, 5923.36)

    def test_bdi_reproduz_f30_e_f31(self):
        resultado = calcular_barrilete(replace(Barrilete(), bdi=10), 9)
        self.assertAlmostEqual(resultado.valor_bdi, 592.336)
        self.assertAlmostEqual(resultado.preco_final, 6515.696)

    def test_dados_ausentes_e_zerados_nao_quebram(self):
        vazio = Barrilete(
            None, None, None, None, None, None, None, None,
            tuple(replace(item, quantidade=None, preco_total_informado=None) for item in Barrilete().itens),
            None,
        )
        resultado = calcular_barrilete(vazio, None)
        self.assertEqual(tuple(asdict(resultado).values()), (0,) * 11)

    def test_valores_negativos_sao_rejeitados(self):
        with self.assertRaises(ValueError):
            Barrilete(custo_hora_operador=-1)
        with self.assertRaises(ValueError):
            replace(Barrilete().itens[0], quantidade=-1)

    def test_versao_nao_editavel_recusa_alteracao(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        resultado = salvar_barrilete(versao, Barrilete())
        self.assertFalse(resultado.sucesso)
        self.assertIn("congelada ou aprovada", resultado.erro)


class TestPersistenciaBarrilete(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_nao_resultados(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra(objeto="Obra", horario_trabalho=9))
        versao.registrar_producao(Producao(140, 65, 18))
        alterado = replace(
            Barrilete(),
            custo_hora_operador=25.75,
            itens=(replace(Barrilete().itens[0], quantidade=7.5),) + Barrilete().itens[1:],
            bdi=12.5,
        )
        versao.registrar_barrilete(alterado)

        documento = serializar_versao(orcamento, versao)
        carregado = desserializar_versao(documento)
        self.assertTrue(carregado.sucesso)
        self.assertEqual(asdict(carregado.valor[1].barrilete), asdict(alterado))
        self.assertEqual(asdict(carregado.valor[1].dados_obra), asdict(versao.dados_obra))
        self.assertEqual(asdict(carregado.valor[1].producao), asdict(versao.producao))
        dados = json.loads(documento)["versao"]["barrilete"]
        for derivado in ("custo_por_dia", "total_composicao", "depreciacao", "valor_bdi", "preco_final"):
            self.assertNotIn(derivado, dados)

    def test_schema_7_sem_barrilete_continua_legivel_com_padrao_em_memoria(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 7
        documento["versao"].pop("barrilete")
        documento["versao"].pop("mobilizacao_draga")
        documento["versao"].pop("mobilizacao_equipamento_polimero")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(asdict(resultado.valor[1].barrilete), asdict(Barrilete()))

    def test_documento_barrilete_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["barrilete"]["itens"][0]["quantidade"] = -1
        resultado = desserializar_versao(json.dumps(documento))
        self.assertEqual(resultado.status, StatusPersistencia.DADO_CORROMPIDO)


class TestTelaBarrilete(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.barrilete")

    def _dominio(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra(objeto="Obra", horario_trabalho=9))
        return orcamento, versao

    def test_um_formulario_contem_entradas_e_horas_vem_de_dados_obra(self):
        orcamento, versao = self._dominio()
        repositorio = Mock()
        falso = StreamlitBarrileteFalso()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )
        self.assertEqual(falso.formularios, ["barrilete_formulario"])
        self.assertIn(("Custo por dia", "R$ 1.407,40"), falso.metricas)
        self.assertFalse(any("Hrs/dia" in rotulo for rotulo, _, _ in falso.campos))

    def test_edicao_sem_envio_faz_zero_operacoes_remotas_e_reruns(self):
        orcamento, versao = self._dominio()
        repositorio = Mock()
        falso = StreamlitBarrileteFalso()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )
        repositorio.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_so_json_uma_vez_preserva_anteriores_e_faz_um_rerun(self):
        orcamento, versao = self._dominio()
        anteriores = (
            asdict(versao.dados_obra),
            asdict(versao.cotacoes),
            asdict(versao.producao),
        )
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="commit-barrilete"
        )
        estado = {}
        falso = StreamlitBarrileteFalso(
            salvar=True,
            valores={"barrilete_custo_operador": 27.25, "barrilete_bdi": 5.5},
            session_state=estado,
        )
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot-original",
            )
        repositorio.persistir_documento_versao.assert_called_once()
        _, salva, snapshot = repositorio.persistir_documento_versao.call_args.args
        self.assertEqual(snapshot, "snapshot-original")
        self.assertEqual(salva.barrilete.custo_hora_operador, 27.25)
        self.assertEqual(salva.barrilete.bdi, 5.5)
        self.assertEqual((asdict(salva.dados_obra), asdict(salva.cotacoes), asdict(salva.producao)), anteriores)
        repositorio.carregar_indice.assert_not_called()
        repositorio.carregar_indice_bruto.assert_not_called()
        repositorio.carregar_snapshot.assert_not_called()
        repositorio.carregar_versao.assert_not_called()
        self.assertEqual(falso.reruns, 1)


if __name__ == "__main__":
    unittest.main()
