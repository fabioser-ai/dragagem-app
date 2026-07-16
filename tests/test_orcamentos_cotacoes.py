import importlib
import json
import sys
import types
import unittest
from contextlib import nullcontext
from dataclasses import asdict
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.dominio.cotacoes import (
    CotacaoContainer,
    CotacaoGuindaste,
    CotacaoMensal,
    Cotacoes,
)
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.persistencia.contratos import (
    ResultadoPersistencia,
    StatusPersistencia,
)
from modulos.orcamentos.persistencia.github_repositorio import (
    RepositorioOrcamentosGitHub,
)
from modulos.orcamentos.persistencia.serializacao import (
    desserializar_versao,
    serializar_versao,
)
from services.persistencia_multi_arquivo import (
    ResultadoPersistenciaMultiArquivo,
    StatusPersistenciaMultiArquivo,
)


class ColunaFalsa:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class StreamlitCotacoesFalso:
    def __init__(self, *, enviar=False, valores=None):
        self.enviar = enviar
        self.valores = valores or {}
        self.session_state = {}
        self.formularios = []
        self.textos = []
        self.monetarios = []
        self.padroes = {}
        self.sucessos = []
        self.erros = []
        self.reruns = 0

    def form(self, chave):
        self.formularios.append(chave)
        return nullcontext()

    def form_submit_button(self, texto):
        return self.enviar

    def subheader(self, texto):
        pass

    def markdown(self, texto, **kwargs):
        pass

    def columns(self, quantidade):
        return tuple(ColunaFalsa() for _ in range(quantidade))

    def text_input(self, rotulo, **kwargs):
        chave = kwargs["key"]
        self.textos.append(chave)
        self.padroes[chave] = kwargs.get("value")
        return self.valores.get(chave, kwargs.get("value", ""))

    def number_input(self, rotulo, **kwargs):
        chave = kwargs["key"]
        self.monetarios.append(chave)
        self.padroes[chave] = kwargs.get("value")
        self.assert_configuracao_monetaria(kwargs)
        return self.valores.get(chave, kwargs.get("value"))

    @staticmethod
    def assert_configuracao_monetaria(kwargs):
        if kwargs.get("min_value") != 0.0 or kwargs.get("step") != 0.01:
            raise AssertionError("Campo monetário sem limite não negativo ou centavos.")

    def success(self, texto):
        self.sucessos.append(texto)

    def error(self, texto):
        self.erros.append(texto)

    def rerun(self):
        self.reruns += 1


def cotacoes_preenchidas():
    return Cotacoes(
        guindaste=(
            CotacaoGuindaste("G1", "A", "1", "D", 10.25, 100.50),
            CotacaoGuindaste(),
            CotacaoGuindaste(),
            CotacaoGuindaste(),
        ),
        container=(
            CotacaoContainer("C1", "B", "2", "D", 200.75, 15.30),
            CotacaoContainer(),
            CotacaoContainer(),
        ),
        banheiro_quimico=(
            CotacaoMensal("B1", "C", "3", "D", 90.10),
            CotacaoMensal(),
            CotacaoMensal(),
        ),
        destinacao=(
            CotacaoMensal("D1", "D", "4", "D", 300.99),
            CotacaoMensal(),
            CotacaoMensal(),
        ),
    )


class TestDominioESerializacaoCotacoes(unittest.TestCase):
    def test_quantidade_de_linhas_reproduz_excel(self):
        cotacoes = Cotacoes()
        self.assertEqual(
            tuple(map(len, (
                cotacoes.guindaste,
                cotacoes.container,
                cotacoes.banheiro_quimico,
                cotacoes.destinacao,
            ))),
            (4, 3, 3, 3),
        )

    def test_valores_monetarios_nao_negativos_e_com_centavos(self):
        self.assertEqual(CotacaoGuindaste(preco_hora=10.25).preco_hora, 10.25)
        with self.assertRaises(ValueError):
            CotacaoMensal(preco_mes=-0.01)

    def test_round_trip_preserva_cotacoes_e_dados_obra(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados_obra = DadosObra(objeto="Obra preservada")
        versao.registrar_dados_obra(dados_obra)
        versao.registrar_cotacoes(cotacoes_preenchidas())

        resultado = desserializar_versao(serializar_versao(orcamento, versao))

        self.assertTrue(resultado.sucesso)
        _, carregada = resultado.valor
        self.assertEqual(asdict(carregada.cotacoes), asdict(versao.cotacoes))
        self.assertEqual(asdict(carregada.dados_obra), asdict(dados_obra))

    def test_documento_nao_contem_formula_ou_resultado_inventado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_cotacoes(cotacoes_preenchidas())
        documento = json.loads(serializar_versao(orcamento, versao))
        texto = json.dumps(documento["versao"]["cotacoes"])
        self.assertNotIn("formula", texto.lower())
        self.assertNotIn("media", texto.lower())
        self.assertNotIn("selecion", texto.lower())


class TestTelaCotacoes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.cotacoes")

    def _dominio(self):
        return criar_orcamento_vazio("Fabio").valor

    def test_um_formulario_13_linhas_72_campos_e_zero_operacoes_sem_envio(self):
        orcamento, versao = self._dominio()
        repositorio = Mock()
        falso = StreamlitCotacoesFalso()

        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )

        self.assertEqual(falso.formularios, ["cotacoes_formulario"])
        self.assertEqual(len(falso.textos), 52)
        self.assertEqual(len(falso.monetarios), 20)
        self.assertEqual(len(falso.textos) + len(falso.monetarios), 72)
        self.assertEqual(falso.reruns, 0)
        repositorio.carregar_indice.assert_not_called()
        repositorio.carregar_indice_bruto.assert_not_called()
        repositorio.carregar_snapshot.assert_not_called()
        repositorio.carregar_versao.assert_not_called()
        repositorio.persistir_versao.assert_not_called()
        repositorio.persistir_documento_versao.assert_not_called()

    def test_salvar_persiste_uma_vez_sem_indice_e_preserva_dados_obra(self):
        orcamento, versao = self._dominio()
        dados = DadosObra(objeto="Dados Obra intactos")
        versao.registrar_dados_obra(dados)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="commit-cotacoes"
        )
        falso = StreamlitCotacoesFalso(
            enviar=True,
            valores={
                "cot_guindaste_0_nome": "Fornecedor A",
                "cot_guindaste_0_hora": 123.45,
            },
        )

        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot-abertura",
            )

        repositorio.persistir_documento_versao.assert_called_once()
        salvo_orcamento, salva_versao, snapshot = (
            repositorio.persistir_documento_versao.call_args.args
        )
        self.assertEqual(snapshot, "snapshot-abertura")
        self.assertEqual(salva_versao.cotacoes.guindaste[0].nome, "Fornecedor A")
        self.assertEqual(salva_versao.cotacoes.guindaste[0].preco_hora, 123.45)
        self.assertEqual(asdict(salva_versao.dados_obra), asdict(dados))
        self.assertEqual(salvo_orcamento.objeto, orcamento.objeto)
        repositorio.carregar_indice_bruto.assert_not_called()
        repositorio.persistir_versao.assert_not_called()
        self.assertEqual(falso.reruns, 1)

    def test_reabertura_mostra_todas_as_cotacoes_salvas(self):
        orcamento, versao = self._dominio()
        versao.registrar_cotacoes(cotacoes_preenchidas())
        falso = StreamlitCotacoesFalso()

        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=Mock(),
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )

        self.assertEqual(falso.padroes["cot_guindaste_0_nome"], "G1")
        self.assertEqual(falso.padroes["cot_guindaste_0_hora"], 10.25)
        self.assertEqual(falso.padroes["cot_container_0_mes"], 200.75)
        self.assertEqual(falso.padroes["cot_banheiro_0_mes"], 90.10)
        self.assertEqual(falso.padroes["cot_destinacao_0_mes"], 300.99)


class TestPersistenciaSomenteDocumento(unittest.TestCase):
    @patch(
        "modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit"
    )
    def test_publica_somente_json_da_versao_no_commit(self, publicar):
        publicar.return_value = ResultadoPersistenciaMultiArquivo(
            StatusPersistenciaMultiArquivo.SUCESSO,
            branch="main",
            arquivos=(),
            snapshot_commit_sha="snapshot",
            commit_sha="commit",
        )
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_cotacoes(cotacoes_preenchidas())
        repositorio = RepositorioOrcamentosGitHub("token", "org/repo")

        resultado = repositorio.persistir_documento_versao(
            orcamento, versao, "snapshot"
        )

        self.assertTrue(resultado.sucesso)
        arquivos = publicar.call_args.args[0]
        self.assertEqual(len(arquivos), 1)
        self.assertTrue(arquivos[0].arquivo.endswith(f"/{versao.id}.json"))
        self.assertNotIn("indice.csv", arquivos[0].arquivo)


if __name__ == "__main__":
    unittest.main()
