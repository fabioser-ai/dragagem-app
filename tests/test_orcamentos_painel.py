import base64
import importlib
import sys
import types
import unittest
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.consultas import filtrar_resumos
from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia
from modulos.orcamentos.persistencia.github_repositorio import RepositorioOrcamentosGitHub
from modulos.orcamentos.persistencia.indice import ResumoIndice, serializar_indice


class StreamlitFalso:
    def __init__(self, *, abrir=False, editar=False, criar=False, session_state=None):
        self.abrir = abrir
        self.editar = editar
        self.criar = criar
        self.erros = []
        self.infos = []
        self.avisos = []
        self.tabelas = []
        self.session_state = session_state if session_state is not None else {"usuario": "fabio"}
        self.reruns = 0

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
    def rerun(self): self.reruns += 1


class ColunaFalsa:
    def __enter__(self): return self
    def __exit__(self, *args): return False


class StreamlitDadosObraFalso(StreamlitFalso):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subtitulos = []

    def subheader(self, texto): self.subtitulos.append(texto)
    def markdown(self, *args, **kwargs): pass
    def columns(self, especificacao):
        quantidade = especificacao if isinstance(especificacao, int) else len(especificacao)
        return tuple(ColunaFalsa() for _ in range(quantidade))
    def date_input(self, *args, **kwargs): return kwargs.get("value")
    def text_area(self, *args, **kwargs): return kwargs.get("value", "")
    def number_input(self, *args, **kwargs): return kwargs.get("value")
    def metric(self, *args, **kwargs): pass
    def success(self, *args, **kwargs): pass


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

    def test_fluxo_completo_renderiza_dados_obra_na_segunda_passagem(self):
        resumo = ResumoIndice("o1", "v1", 1, "Objeto", "Proposta", "Fabio", "elaboracao")
        versao = Mock(numero=1, estado=Mock(value="elaboracao"), cenarios=(), editavel=True)
        orcamento = Mock(objeto="Objeto", finalidade="Proposta", responsavel="Fabio")
        repositorio = Mock()
        repositorio.carregar_indice.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, [resumo]
        )
        repositorio.carregar_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, (orcamento, versao)
        )
        repositorio.carregar_snapshot.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, "snapshot-correto"
        )
        estado = {"usuario": "fabio"}

        primeira = StreamlitFalso(abrir=True, session_state=estado)
        with patch.object(self.painel, "st", primeira), patch.object(
            self.painel.dados_obra, "render"
        ) as render_dados:
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())
            render_dados.assert_not_called()

        self.assertEqual(primeira.reruns, 1)
        self.assertEqual(estado["novo_orcamento_detalhe"], (orcamento, versao))
        self.assertEqual(estado["novo_orcamento_snapshot"], "snapshot-correto")

        segunda = StreamlitFalso(session_state=estado)
        with patch.object(self.painel, "st", segunda), patch.object(
            self.painel.dados_obra, "render"
        ) as render_dados:
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())

        render_dados.assert_called_once_with(
            repositorio=repositorio,
            orcamento=orcamento,
            versao=versao,
            snapshot_esperado="snapshot-correto",
        )
        repositorio.carregar_indice.assert_called_once()
        repositorio.carregar_versao.assert_called_once_with("o1", "v1")
        repositorio.carregar_snapshot.assert_called_once()

    def test_segunda_passagem_renderiza_widgets_reais_de_dados_obra(self):
        resumo = ResumoIndice("o1", "v1", 1, "Objeto", "Proposta", "Fabio", "elaboracao")
        orcamento, versao = criar_orcamento_vazio("fabio").valor
        repositorio = Mock()
        repositorio.carregar_indice.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, [resumo]
        )
        repositorio.carregar_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, (orcamento, versao)
        )
        repositorio.carregar_snapshot.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, "snapshot-real"
        )
        estado = {"usuario": "fabio"}

        primeira = StreamlitDadosObraFalso(abrir=True, session_state=estado)
        with patch.object(self.painel, "st", primeira):
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())

        segunda = StreamlitDadosObraFalso(session_state=estado)
        with patch.object(self.painel, "st", segunda), patch.object(
            self.painel.dados_obra, "st", segunda
        ):
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())

        self.assertIn("Dados Obra", segunda.subtitulos)
        self.assertEqual(segunda.erros, [])
        repositorio.carregar_indice.assert_called_once()

    def test_falha_ao_carregar_versao_exibe_etapa_status_e_erro(self):
        resumo = ResumoIndice("o1", "v1", 1, "Objeto", "Proposta", "Fabio", "elaboracao")
        repositorio = Mock()
        repositorio.carregar_indice.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, [resumo]
        )
        repositorio.carregar_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.DADO_CORROMPIDO, erro="Documento JSON inválido."
        )
        falso = StreamlitFalso(abrir=True)

        with patch.object(self.painel, "st", falso):
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())

        self.assertEqual(len(falso.erros), 1)
        self.assertIn("carregar versão", falso.erros[0])
        self.assertIn("dado_corrompido", falso.erros[0])
        self.assertIn("Documento JSON inválido", falso.erros[0])
        repositorio.carregar_snapshot.assert_not_called()

    def test_falha_ao_carregar_snapshot_exibe_etapa_status_e_erro(self):
        resumo = ResumoIndice("o1", "v1", 1, "Objeto", "Proposta", "Fabio", "elaboracao")
        repositorio = Mock()
        repositorio.carregar_indice.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, [resumo]
        )
        repositorio.carregar_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, (Mock(), Mock())
        )
        repositorio.carregar_snapshot.return_value = ResultadoPersistencia(
            StatusPersistencia.ERRO_REMOTO, erro="GitHub indisponível (HTTP 503)."
        )
        falso = StreamlitFalso(abrir=True)

        with patch.object(self.painel, "st", falso):
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())

        self.assertEqual(len(falso.erros), 1)
        self.assertIn("carregar snapshot", falso.erros[0])
        self.assertIn("erro_remoto", falso.erros[0])
        self.assertIn("HTTP 503", falso.erros[0])

    def test_excecao_ao_renderizar_dados_obra_exibe_erro_seguro(self):
        versao = Mock(numero=1, estado=Mock(value="elaboracao"), cenarios=(), editavel=True)
        orcamento = Mock(objeto="Objeto", finalidade="Proposta", responsavel="Fabio")
        repositorio = Mock()
        falso = StreamlitFalso()
        falso.session_state["novo_orcamento_detalhe"] = (orcamento, versao)
        falso.session_state["novo_orcamento_snapshot"] = "snapshot"

        with patch.object(self.painel, "st", falso), patch.object(
            self.painel.dados_obra, "render", side_effect=RuntimeError("token secreto")
        ):
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())

        self.assertEqual(len(falso.erros), 1)
        self.assertIn("renderizar Dados Obra", falso.erros[0])
        self.assertIn("erro_interno", falso.erros[0])
        self.assertIn("RuntimeError", falso.erros[0])
        self.assertNotIn("token secreto", falso.erros[0])
        repositorio.carregar_indice.assert_not_called()

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
