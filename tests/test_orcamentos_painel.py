import base64
import importlib
import sys
import types
import unittest
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.consultas import filtrar_resumos
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.github_repositorio import RepositorioOrcamentosGitHub
from modulos.orcamentos.persistencia.indice import ResumoIndice, serializar_indice


class StreamlitFalso:
    def __init__(self, *, abrir=False, editar=False, criar=False):
        self.abrir = abrir
        self.editar = editar
        self.criar = criar
        self.erros = []
        self.infos = []
        self.avisos = []
        self.tabelas = []
        self.session_state = {"usuario": "fabio"}

    def title(self, texto): pass
    def info(self, texto): self.infos.append(texto)
    def error(self, texto): self.erros.append(texto)
    def warning(self, texto): self.avisos.append(texto)
    def subheader(self, texto): pass
    def caption(self, texto): pass
    def write(self, texto): pass
    def divider(self): pass
    def text_input(self, *args, **kwargs): return ""
    def selectbox(self, *args, **kwargs): return kwargs["options"][0]
    def dataframe(self, dados, **kwargs): self.tabelas.append(dados)
    def button(self, texto, **kwargs):
        if texto == "Novo orçamento":
            return self.criar
        if texto == "Abrir versão":
            return self.abrir
        if texto == "Abrir Dados Obra":
            return self.editar
        return False
    def rerun(self): pass


class TestConsultasPainel(unittest.TestCase):
    def setUp(self):
        self.resumos = [
            ResumoIndice("o2", "v2", 2, "Dragagem Beta", "Proposta", "Bruno", "congelada"),
            ResumoIndice("o1", "v1", 1, "Dragagem Alfa", "Estudo", "Ana", "elaboracao"),
        ]

    def test_filtros_sao_locais_e_combinaveis(self):
        resultado = filtrar_resumos(self.resumos, busca="ana", estado="elaboracao")
        self.assertEqual([item.orcamento_id for item in resultado], ["o1"])

    def test_resultado_e_ordenado_sem_alterar_origem(self):
        resultado = filtrar_resumos(self.resumos)
        self.assertEqual([item.orcamento_id for item in resultado], ["o1", "o2"])
        self.assertEqual(self.resumos[0].orcamento_id, "o2")


class TestRepositorioIndice(unittest.TestCase):
    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_indice_e_carregado_em_uma_requisicao(self, get):
        conteudo = serializar_indice([
            ResumoIndice("o1", "v1", 1, "Objeto", "Proposta", "Fabio", "elaboracao")
        ]).encode()
        get.return_value = Mock(
            status_code=200,
            json=lambda: {"content": base64.b64encode(conteudo).decode()},
        )
        resultado = RepositorioOrcamentosGitHub("token", "org/repo").carregar_indice()
        self.assertTrue(resultado.sucesso)
        self.assertEqual(len(resultado.valor), 1)
        get.assert_called_once()

    @patch("modulos.orcamentos.persistencia.github_repositorio.requests.get")
    def test_indice_inexistente_tem_resultado_explicito(self, get):
        get.return_value = Mock(status_code=404)
        resultado = RepositorioOrcamentosGitHub("token", "org/repo").carregar_indice()
        self.assertEqual(resultado.status, StatusPersistencia.DADO_INEXISTENTE)
        get.assert_called_once()


class TestPainel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.painel = importlib.import_module("modulos.orcamentos.apresentacao.painel")

    def test_lista_nao_carrega_detalhes(self):
        resumo = ResumoIndice("o1", "v1", 1, "Objeto", "Proposta", "Fabio", "elaboracao")
        repositorio = Mock()
        repositorio.carregar_indice.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, [resumo]
        )
        falso = StreamlitFalso()
        with patch.object(self.painel, "st", falso):
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())
        repositorio.carregar_indice.assert_called_once()
        repositorio.carregar_versao.assert_not_called()
        self.assertEqual(len(falso.tabelas), 1)

    def test_detalhe_so_abre_sob_demanda(self):
        resumo = ResumoIndice("o1", "v1", 1, "Objeto", "Proposta", "Fabio", "elaboracao")
        versao = Mock(numero=1, estado=Mock(value="elaboracao"), cenarios=(), editavel=False)
        orcamento = Mock(objeto="Objeto", finalidade="Proposta", responsavel="Fabio")
        repositorio = Mock()
        repositorio.carregar_indice.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, [resumo]
        )
        repositorio.carregar_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, (orcamento, versao)
        )
        falso = StreamlitFalso(abrir=True)
        with patch.object(self.painel, "st", falso):
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())
        repositorio.carregar_indice.assert_called_once()
        repositorio.carregar_versao.assert_called_once_with("o1", "v1")
        self.assertIn("novo_orcamento_detalhe", falso.session_state)

    def test_edicao_captura_snapshot_somente_sob_demanda(self):
        resumo = ResumoIndice("o1", "v1", 1, "Objeto", "Proposta", "Fabio", "elaboracao")
        versao = Mock(numero=1, estado=Mock(value="elaboracao"), cenarios=(), editavel=True)
        orcamento = Mock(objeto="Objeto", finalidade="Proposta", responsavel="Fabio")
        repositorio = Mock()
        repositorio.carregar_indice.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, [resumo]
        )
        repositorio.carregar_snapshot.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, "commit-atual"
        )
        falso = StreamlitFalso(editar=True)
        falso.session_state["novo_orcamento_detalhe"] = (orcamento, versao)
        with patch.object(self.painel, "st", falso):
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())
        repositorio.carregar_snapshot.assert_called_once()
        self.assertEqual(falso.session_state["novo_orcamento_snapshot"], "commit-atual")

    def test_edicao_nao_rele_indice_a_cada_calculo(self):
        versao = Mock(numero=1, estado=Mock(value="elaboracao"), cenarios=(), editavel=True)
        orcamento = Mock(objeto="Objeto", finalidade="Proposta", responsavel="Fabio")
        repositorio = Mock()
        falso = StreamlitFalso()
        falso.session_state["novo_orcamento_detalhe"] = (orcamento, versao)
        falso.session_state["novo_orcamento_snapshot"] = "commit-atual"
        with patch.object(self.painel, "st", falso), patch.object(
            self.painel.dados_obra, "render"
        ) as render_dados:
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())
        repositorio.carregar_indice.assert_not_called()
        render_dados.assert_called_once()

    def test_vazio_e_erro_sao_explicitos(self):
        for status in (StatusPersistencia.DADO_INEXISTENTE, StatusPersistencia.ERRO_REMOTO):
            with self.subTest(status=status):
                repositorio = Mock()
                repositorio.carregar_indice.return_value = ResultadoPersistencia(status)
                falso = StreamlitFalso()
                with patch.object(self.painel, "st", falso):
                    self.painel.render(repositorio=repositorio, ao_voltar=Mock())
                self.assertTrue(falso.infos or falso.erros)


if __name__ == "__main__":
    unittest.main()
