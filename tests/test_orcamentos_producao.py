import importlib
import json
import math
import sys
import types
import unittest
from contextlib import nullcontext
from dataclasses import asdict
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.dominio.cotacoes import Cotacoes, ItemCotacao
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.producao import Producao, calcular_producao
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


class StreamlitProducaoFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar = salvar
        self.valores = valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios = []
        self.campos = []
        self.padroes = {}
        self.metricas = []
        self.erros = []
        self.sucessos = []
        self.reruns = 0

    def form(self, chave):
        self.formularios.append(chave)
        return nullcontext()

    def form_submit_button(self, texto):
        return self.salvar and texto == "Salvar Produção"

    def subheader(self, texto):
        pass

    def columns(self, quantidade):
        return tuple(ColunaFalsa() for _ in range(quantidade))

    def number_input(self, rotulo, **kwargs):
        chave = kwargs["key"]
        self.campos.append((rotulo, chave))
        self.padroes[chave] = kwargs.get("value")
        return self.valores.get(chave, kwargs.get("value"))

    def metric(self, rotulo, valor):
        self.metricas.append((rotulo, valor))

    def error(self, texto):
        self.erros.append(texto)

    def success(self, texto):
        self.sucessos.append(texto)

    def rerun(self):
        self.reruns += 1


class TestCalculosProducao(unittest.TestCase):
    def test_valores_iniciais_correspondem_ao_excel(self):
        producao = Producao()
        self.assertEqual((producao.vazao, producao.eficiencia, producao.concentracao), (120, 60, 15))

    def test_caso_numerico_reproduz_quatro_formulas_do_excel(self):
        resultado = calcular_producao(Producao(120, 60, 15), 9, 22, 5000)
        self.assertAlmostEqual(resultado.producao_horaria, 10.8)
        self.assertAlmostEqual(resultado.horas_mensais, 198)
        self.assertAlmostEqual(resultado.producao_mensal, 2138.4)
        self.assertAlmostEqual(resultado.prazo_meses, 5000 / 2138.4)
        self.assertAlmostEqual(resultado.prazo_meses, 2.3381967826412273)

    def test_percentuais_sao_divididos_por_cem(self):
        resultado = calcular_producao(Producao(100, 50, 20), 1, 1, 10)
        self.assertEqual(resultado.producao_horaria, 10)

    def test_ausencia_e_zero_nao_geram_divisao_infinito_ou_nan(self):
        casos = (
            (Producao(None, 60, 15), 9, 22, 5000),
            (Producao(0, 60, 15), 9, 22, 5000),
            (Producao(), None, 22, 5000),
            (Producao(), 0, 22, 5000),
            (Producao(), 9, 22, None),
            (Producao(), 9, 22, 0),
        )
        for argumentos in casos:
            with self.subTest(argumentos=argumentos):
                resultado = calcular_producao(*argumentos)
                self.assertIsNone(resultado.prazo_meses)
                for valor in asdict(resultado).values():
                    self.assertFalse(valor is not None and (math.isnan(valor) or math.isinf(valor)))


class TestPersistenciaProducao(unittest.TestCase):
    def test_round_trip_persiste_so_entradas_e_preserva_outros_dados(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = DadosObra(objeto="Obra", horario_trabalho=9, dias_trabalho=22)
        cotacoes = Cotacoes((ItemCotacao.novo("Transporte", "Preço por viagem"),))
        versao.registrar_dados_obra(dados)
        versao.registrar_cotacoes(cotacoes)
        versao.registrar_producao(Producao(130.25, 62.5, 17.75))

        documento = serializar_versao(orcamento, versao)
        resultado = desserializar_versao(documento)

        self.assertTrue(resultado.sucesso)
        carregada = resultado.valor[1]
        self.assertEqual(asdict(carregada.producao), asdict(versao.producao))
        self.assertEqual(asdict(carregada.dados_obra), asdict(dados))
        self.assertEqual(asdict(carregada.cotacoes), asdict(cotacoes))
        dados_producao = json.loads(documento)["versao"]["producao"]
        self.assertEqual(set(dados_producao), {"vazao", "eficiencia", "concentracao"})
        self.assertNotIn("producao_mensal", dados_producao)
        self.assertNotIn("prazo", dados_producao)

    def test_schema_anterior_sem_producao_recebe_padrao_sem_migracao_manual(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 6
        documento["versao"].pop("producao")
        documento["versao"].pop("barrilete")
        documento["versao"].pop("mobilizacao_draga")
        documento["versao"].pop("mobilizacao_equipamento_polimero")
        documento["versao"].pop("canteiro")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(asdict(resultado.valor[1].producao), asdict(Producao()))


class TestTelaProducao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.producao")

    def _dominio(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(
            DadosObra(volume_dragagem=5000, horario_trabalho=9, dias_trabalho=22)
        )
        return orcamento, versao

    def test_tres_campos_em_um_formulario_e_premissas_vem_de_dados_obra(self):
        orcamento, versao = self._dominio()
        repositorio = Mock()
        falso = StreamlitProducaoFalso()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )
        self.assertEqual(falso.formularios, ["producao_formulario"])
        self.assertEqual(len(falso.campos), 3)
        self.assertEqual(falso.padroes, {
            "producao_vazao": 120.0,
            "producao_eficiencia": 60.0,
            "producao_concentracao": 15.0,
        })
        metricas = dict(falso.metricas)
        self.assertEqual(metricas["Horas por dia"], "9.00 h/dia")
        self.assertEqual(metricas["Dias por mês"], "22.00 dias/mês")
        self.assertEqual(metricas["Volume total a dragar"], "5000.00 m³")
        self.assertEqual(metricas["Produção horária"], "10.80 m³/h")
        self.assertEqual(metricas["Produção mensal"], "2138.40 m³/mês")
        repositorio.assert_not_called()

    def test_edicao_sem_envio_faz_zero_leituras_persistencias_e_reruns(self):
        orcamento, versao = self._dominio()
        repositorio = Mock()
        falso = StreamlitProducaoFalso()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )
        repositorio.carregar_indice.assert_not_called()
        repositorio.carregar_indice_bruto.assert_not_called()
        repositorio.carregar_snapshot.assert_not_called()
        repositorio.carregar_versao.assert_not_called()
        repositorio.persistir_documento_versao.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_uma_vez_e_reabertura_preserva_entradas(self):
        orcamento, versao = self._dominio()
        dados_antes = asdict(versao.dados_obra)
        cotacoes_antes = asdict(versao.cotacoes)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="commit-producao"
        )
        estado = {}
        falso = StreamlitProducaoFalso(
            salvar=True,
            valores={
                "producao_vazao": 140.5,
                "producao_eficiencia": 65.25,
                "producao_concentracao": 18.75,
            },
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
        _, salva_versao, snapshot = repositorio.persistir_documento_versao.call_args.args
        self.assertEqual(snapshot, "snapshot-original")
        self.assertEqual(asdict(salva_versao.producao), {
            "vazao": 140.5,
            "eficiencia": 65.25,
            "concentracao": 18.75,
        })
        self.assertEqual(asdict(salva_versao.dados_obra), dados_antes)
        self.assertEqual(asdict(salva_versao.cotacoes), cotacoes_antes)
        self.assertEqual(falso.reruns, 1)
        repositorio.carregar_indice_bruto.assert_not_called()
        repositorio.carregar_snapshot.assert_not_called()
        repositorio.carregar_versao.assert_not_called()

        documento = serializar_versao(orcamento, salva_versao)
        reaberta = desserializar_versao(documento).valor[1]
        self.assertEqual(asdict(reaberta.producao), asdict(salva_versao.producao))


if __name__ == "__main__":
    unittest.main()
