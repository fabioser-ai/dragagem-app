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
from modulos.orcamentos.aplicacao.mobilizacao_draga import salvar_mobilizacao_draga
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.mobilizacao_draga import (
    MobilizacaoDraga,
    calcular_mobilizacao_draga,
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


class StreamlitMobilizacaoFalso:
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
        return self.salvar and texto == "Salvar Mobilização da Draga"

    def subheader(self, texto):
        pass

    def markdown(self, texto):
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


class TestCalculosMobilizacaoDraga(unittest.TestCase):
    def test_fotografia_inicial_tem_tres_linhas_e_oito_itens(self):
        mobilizacao = MobilizacaoDraga()
        self.assertEqual([linha.descricao for linha in mobilizacao.equipe], [
            "Operador Líder", "Operador de Draga", "Ajudante Geral"
        ])
        self.assertEqual(len(mobilizacao.itens), 8)
        self.assertEqual([item.quantidade for item in mobilizacao.itens], [1, None, None, 1, 1, 1, None, 5])
        self.assertEqual(mobilizacao.custo_refeicao, 40)
        self.assertEqual(mobilizacao.custo_transporte, 10)
        self.assertIsNone(mobilizacao.bdi)

    def test_custos_horarios_horas_e_encargos_reproduzem_excel(self):
        equipe = MobilizacaoDraga().equipe
        self.assertEqual(equipe[0].custo_hora, 18)
        self.assertAlmostEqual(equipe[1].custo_hora, 22.68 * 1.25)
        self.assertEqual(equipe[2].custo_hora, 11.13)
        resultado = calcular_mobilizacao_draga(MobilizacaoDraga())
        self.assertEqual([item.horas_dia for item in resultado.mao_obra], [9, 9, 9])
        self.assertEqual(resultado.mao_obra[0].total, 0)
        self.assertAlmostEqual(resultado.mao_obra[1].total, 1071.63)
        self.assertAlmostEqual(resultado.mao_obra[2].total, 420.714)

    def test_refeicoes_transporte_e_custo_diario_reproduzem_excel(self):
        resultado = calcular_mobilizacao_draga(MobilizacaoDraga())
        self.assertEqual(resultado.quantidade_refeicoes, 4)
        self.assertEqual(resultado.quantidade_transportes, 4)
        self.assertEqual(resultado.total_refeicoes, 160)
        self.assertEqual(resultado.total_transportes, 40)
        self.assertAlmostEqual(resultado.custo_por_dia, 1692.344)

    def test_so_linhas_com_formula_sao_multiplicadas(self):
        resultado = calcular_mobilizacao_draga(MobilizacaoDraga())
        totais = {item.id: item.preco_total for item in resultado.itens}
        self.assertEqual(totais["guindaste-carregamento"], 1200)
        self.assertEqual(totais["guindaste-descarregamento"], 5000)
        self.assertEqual(totais["frete"], 1000)
        self.assertEqual(totais["treinamentos"], 0)
        self.assertEqual(totais["mobiliario-canteiro"], 0)
        self.assertEqual(totais["carreta-carga-seca"], 1300)
        self.assertEqual(totais["trator-d4"], 0)
        self.assertAlmostEqual(totais["mao-obra-carga-montagem"], 8461.72)

    def test_mao_obra_composicao_tem_unitario_derivado_e_total_informado(self):
        resultado = calcular_mobilizacao_draga(MobilizacaoDraga())
        linha = next(item for item in resultado.itens if item.id == "mao-obra-carga-montagem")
        self.assertAlmostEqual(linha.preco_unitario, 1692.344)
        self.assertAlmostEqual(linha.preco_total, 8461.72)

    def test_total_bdi_preco_final_e_repeticao_reproduzem_excel(self):
        resultado = calcular_mobilizacao_draga(MobilizacaoDraga())
        self.assertAlmostEqual(resultado.total_composicao, 16961.72)
        self.assertEqual(resultado.valor_bdi, 0)
        self.assertAlmostEqual(resultado.preco_final, 16961.72)
        self.assertEqual(resultado.preco_final_repetido, resultado.preco_final)
        com_bdi = calcular_mobilizacao_draga(replace(MobilizacaoDraga(), bdi=10))
        self.assertAlmostEqual(com_bdi.valor_bdi, 1696.172)
        self.assertAlmostEqual(com_bdi.preco_final, 18657.892)

    def test_ausentes_e_zeros_nao_geram_nan_ou_infinito(self):
        mobilizacao = MobilizacaoDraga(
            tuple(
                replace(
                    linha,
                    quantidade=None,
                    custo_hora_manual=None if linha.custo_hora_base is None else linha.custo_hora_manual,
                    horas_dia_manual=None,
                    horas_referencia_id=None,
                    encargos_sociais=None,
                )
                for linha in MobilizacaoDraga().equipe
            ),
            None,
            0,
            tuple(
                replace(
                    item,
                    quantidade=None,
                    preco_unitario_manual=None,
                    preco_unitario_custo_diario=False,
                    preco_total_calculado=False,
                    preco_total_manual=None,
                )
                for item in MobilizacaoDraga().itens
            ),
            None,
        )
        resultado = calcular_mobilizacao_draga(mobilizacao)
        for valor in (
            resultado.quantidade_refeicoes,
            resultado.total_refeicoes,
            resultado.quantidade_transportes,
            resultado.total_transportes,
            resultado.custo_por_dia,
            resultado.total_composicao,
            resultado.valor_bdi,
            resultado.preco_final,
        ):
            self.assertTrue(math.isfinite(valor))
            self.assertEqual(valor, 0)

    def test_negativo_nan_e_infinito_sao_rejeitados(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                MobilizacaoDraga(custo_refeicao=valor)

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        resultado = salvar_mobilizacao_draga(versao, MobilizacaoDraga())
        self.assertFalse(resultado.sucesso)


class TestPersistenciaMobilizacaoDraga(unittest.TestCase):
    def test_round_trip_persiste_entradas_preserva_telas_e_nao_persiste_resultados(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_dados_obra(DadosObra(objeto="Obra"))
        anteriores = (
            asdict(versao.dados_obra),
            asdict(versao.cotacoes),
            asdict(versao.producao),
            asdict(versao.barrilete),
        )
        alterada = replace(
            MobilizacaoDraga(),
            custo_refeicao=45.75,
            bdi=12.5,
            itens=(
                replace(MobilizacaoDraga().itens[0], quantidade=2.5, observacao="Fonte A"),
            ) + MobilizacaoDraga().itens[1:],
        )
        versao.registrar_mobilizacao_draga(alterada)
        documento = serializar_versao(orcamento, versao)
        resultado = desserializar_versao(documento)
        self.assertTrue(resultado.sucesso)
        carregada = resultado.valor[1]
        self.assertEqual(asdict(carregada.mobilizacao_draga), asdict(alterada))
        self.assertEqual(
            (asdict(carregada.dados_obra), asdict(carregada.cotacoes), asdict(carregada.producao), asdict(carregada.barrilete)),
            anteriores,
        )
        dados = json.loads(documento)["versao"]["mobilizacao_draga"]
        for derivado in ("custo_por_dia", "total_composicao", "valor_bdi", "preco_final"):
            self.assertNotIn(derivado, dados)

    def test_schema_8_sem_mobilizacao_continua_legivel(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 8
        documento["versao"].pop("mobilizacao_draga")
        documento["versao"].pop("mobilizacao_equipamento_polimero")
        documento["versao"].pop("canteiro")
        documento["versao"].pop("preparacao_celula")
        documento["versao"].pop("fornecimento_bag")
        documento["versao"].pop("operacao_sistema")
        documento["versao"].pop("dragagem")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(asdict(resultado.valor[1].mobilizacao_draga), asdict(MobilizacaoDraga()))

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["mobilizacao_draga"]["equipe"][0]["quantidade"] = -1
        resultado = desserializar_versao(json.dumps(documento))
        self.assertEqual(resultado.status, StatusPersistencia.DADO_CORROMPIDO)


class TestTelaMobilizacaoDraga(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.mobilizacao_draga")

    def _dominio(self):
        return criar_orcamento_vazio("Fabio").valor

    def test_dois_blocos_oito_itens_e_um_formulario(self):
        orcamento, versao = self._dominio()
        falso = StreamlitMobilizacaoFalso()
        repositorio = Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )
        self.assertEqual(falso.formularios, ["mobilizacao_draga_formulario"])
        observacoes = [item for item in falso.campos if item[0] == "Observação/Fonte"]
        self.assertEqual(len(observacoes), 8)
        self.assertIn(("Custo por dia", "R$ 1.692,34"), falso.metricas)

    def test_edicao_sem_envio_faz_zero_operacoes_remotas_e_reruns(self):
        orcamento, versao = self._dominio()
        falso = StreamlitMobilizacaoFalso()
        repositorio = Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )
        repositorio.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_json_uma_vez_sem_indice_e_preserva_telas(self):
        orcamento, versao = self._dominio()
        anteriores = (
            asdict(versao.dados_obra) if versao.dados_obra else None,
            asdict(versao.cotacoes),
            asdict(versao.producao),
            asdict(versao.barrilete),
        )
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="commit-mob-draga"
        )
        falso = StreamlitMobilizacaoFalso(
            salvar=True,
            valores={"mob_draga_refeicao": 47.5, "mob_draga_bdi": 8.25},
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
        self.assertEqual(salva.mobilizacao_draga.custo_refeicao, 47.5)
        self.assertEqual(salva.mobilizacao_draga.bdi, 8.25)
        self.assertEqual(
            (
                asdict(salva.dados_obra) if salva.dados_obra else None,
                asdict(salva.cotacoes), asdict(salva.producao), asdict(salva.barrilete),
            ),
            anteriores,
        )
        repositorio.carregar_indice.assert_not_called()
        repositorio.carregar_indice_bruto.assert_not_called()
        repositorio.carregar_snapshot.assert_not_called()
        repositorio.carregar_versao.assert_not_called()
        self.assertEqual(falso.reruns, 1)


if __name__ == "__main__":
    unittest.main()
