import importlib
import json
import sys
import types
import unittest
from contextlib import nullcontext
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.persistencia.contratos import (
    ResultadoPersistencia,
    StatusPersistencia,
)
from modulos.orcamentos.persistencia.github_repositorio import (
    RepositorioOrcamentosGitHub,
)
from modulos.orcamentos.persistencia.indice import desserializar_indice, serializar_indice
from services.persistencia_multi_arquivo import (
    ResultadoPersistenciaMultiArquivo,
    StatusPersistenciaMultiArquivo,
)


class ColunaFalsa:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class StreamlitFormularioFalso:
    def __init__(self, *, enviar=False, valores=None):
        self.enviar = enviar
        self.valores = valores or {}
        self.session_state = {}
        self.formularios = []
        self.campos = []
        self.padroes = {}
        self.metricas = []
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

    def markdown(self, *args, **kwargs):
        pass

    def columns(self, especificacao):
        quantidade = especificacao if isinstance(especificacao, int) else len(especificacao)
        return tuple(ColunaFalsa() for _ in range(quantidade))

    def _valor(self, rotulo, padrao):
        self.campos.append(rotulo)
        self.padroes[rotulo] = padrao
        return self.valores.get(rotulo, padrao)

    def text_input(self, rotulo, **kwargs):
        return self._valor(rotulo, kwargs.get("value", ""))

    def text_area(self, rotulo, **kwargs):
        return self._valor(rotulo, kwargs.get("value", ""))

    def date_input(self, rotulo, **kwargs):
        return self._valor(rotulo, kwargs.get("value"))

    def number_input(self, rotulo, **kwargs):
        return self._valor(rotulo, kwargs.get("value"))

    def metric(self, rotulo, valor):
        self.metricas.append((rotulo, valor))

    def caption(self, texto):
        pass

    def success(self, texto):
        self.sucessos.append(texto)

    def error(self, texto):
        self.erros.append(texto)

    def rerun(self):
        self.reruns += 1


class TestFormularioDadosObra(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module(
            "modulos.orcamentos.apresentacao.dados_obra"
        )

    def _dominio(self):
        return criar_orcamento_vazio("Fabio").valor

    def test_24_campos_estao_em_um_unico_formulario_sem_acesso_remoto(self):
        orcamento, versao = self._dominio()
        repositorio = Mock()
        falso = StreamlitFormularioFalso()

        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )

        self.assertEqual(falso.formularios, ["dados_obra_formulario"])
        self.assertEqual(len(falso.campos), 24)
        self.assertEqual(falso.reruns, 0)
        repositorio.carregar_indice.assert_not_called()
        repositorio.carregar_indice_bruto.assert_not_called()
        repositorio.carregar_snapshot.assert_not_called()
        repositorio.carregar_versao.assert_not_called()
        repositorio.persistir_versao.assert_not_called()

    def test_envio_atualiza_titulo_e_persiste_uma_unica_vez(self):
        orcamento, versao = self._dominio()
        repositorio = Mock()
        repositorio.carregar_indice_bruto.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, serializar_indice([])
        )
        repositorio.persistir_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="commit-novo"
        )
        falso = StreamlitFormularioFalso(
            enviar=True, valores={"Objeto": "  Dragagem ETEL ETA3  "}
        )

        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot-original",
            )

        repositorio.carregar_indice_bruto.assert_called_once()
        repositorio.persistir_versao.assert_called_once()
        salvo_orcamento, salvo_versao, _, snapshot = (
            repositorio.persistir_versao.call_args.args
        )
        self.assertEqual(salvo_orcamento.objeto, "Dragagem ETEL ETA3")
        self.assertEqual(salvo_versao.dados_obra.objeto, "  Dragagem ETEL ETA3  ")
        self.assertEqual(snapshot, "snapshot-original")
        self.assertEqual(
            falso.session_state["novo_orcamento_detalhe"],
            (salvo_orcamento, salvo_versao),
        )
        self.assertEqual(falso.session_state["novo_orcamento_snapshot"], "commit-novo")
        self.assertEqual(falso.sucessos, [])
        self.assertEqual(falso.reruns, 1)
        repositorio.carregar_indice.assert_not_called()
        repositorio.carregar_snapshot.assert_not_called()
        repositorio.carregar_versao.assert_not_called()

        reabertura = StreamlitFormularioFalso()
        reabertura.session_state = falso.session_state
        with patch.object(self.tela, "st", reabertura):
            self.tela.render(
                repositorio=repositorio,
                orcamento=salvo_orcamento,
                versao=salvo_versao,
                snapshot_esperado="commit-novo",
            )
        self.assertEqual(reabertura.sucessos, ["Dados Obra salvos."])
        repositorio.carregar_indice_bruto.assert_called_once()
        repositorio.persistir_versao.assert_called_once()

    def test_objeto_vazio_mantem_titulo_seguro(self):
        orcamento, versao = self._dominio()
        repositorio = Mock()
        repositorio.carregar_indice_bruto.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, serializar_indice([])
        )
        repositorio.persistir_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="commit-novo"
        )
        falso = StreamlitFormularioFalso(enviar=True, valores={"Objeto": "   "})

        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )

        salvo = repositorio.persistir_versao.call_args.args[0]
        self.assertEqual(salvo.objeto, "Novo orçamento")

    def test_reabertura_exibe_dados_salvos_e_calculos_homologados(self):
        orcamento, versao = self._dominio()
        dados = DadosObra(
            objeto="Obra salva",
            distancia_recalque=200,
            seio_recalque=10,
            linha_flutuante=100,
            seio_linha_flutuante=5,
            area_comprimento=40,
            area_largura=25,
            espessura_media=1,
        )
        versao.registrar_dados_obra(dados)
        falso = StreamlitFormularioFalso()

        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=Mock(),
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )

        self.assertEqual(falso.padroes["Objeto"], "Obra salva")
        self.assertEqual(
            falso.metricas,
            [("Total", "210.00"), ("Total", "105.00"), ("Volume (m³) =", "1000.00")],
        )


class TestCommitCompostoDoTitulo(unittest.TestCase):
    @patch(
        "modulos.orcamentos.persistencia.github_repositorio.publicar_arquivos_em_commit"
    )
    def test_indice_e_json_recebem_titulo_no_mesmo_commit(self, publicar):
        publicar.return_value = ResultadoPersistenciaMultiArquivo(
            StatusPersistenciaMultiArquivo.SUCESSO,
            branch="main",
            arquivos=(),
            commit_sha="commit-remoto",
            snapshot_commit_sha="snapshot",
        )
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        orcamento.objeto = "Dragagem ETEL ETA3"
        versao.registrar_dados_obra(DadosObra(objeto="Dragagem ETEL ETA3"))
        repositorio = RepositorioOrcamentosGitHub("token", "org/repo")

        resultado = repositorio.persistir_versao(
            orcamento, versao, serializar_indice([]), "snapshot"
        )

        self.assertTrue(resultado.sucesso)
        publicar.assert_called_once()
        arquivos = publicar.call_args.args[0]
        self.assertEqual(len(arquivos), 2)
        indice = desserializar_indice(arquivos[0].conteudo.decode())
        documento = json.loads(arquivos[1].conteudo.decode())
        self.assertEqual(indice.valor[0].objeto, "Dragagem ETEL ETA3")
        self.assertEqual(documento["orcamento"]["objeto"], "Dragagem ETEL ETA3")


if __name__ == "__main__":
    unittest.main()
