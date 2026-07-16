import importlib
import sys
import types
import unittest
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.persistencia.contratos import (
    ResultadoPersistencia,
    StatusPersistencia,
)


class StreamlitFalso:
    def __init__(self, *, criar=False, abrir=False):
        self.criar = criar
        self.abrir = abrir
        self.session_state = {"usuario": "fabio"}
        self.erros = []
        self.reruns = 0

    def title(self, texto): pass
    def info(self, texto): pass
    def error(self, texto): self.erros.append(texto)
    def warning(self, texto): pass
    def subheader(self, texto): pass
    def caption(self, texto): pass
    def write(self, texto): pass
    def divider(self): pass
    def dataframe(self, dados, **kwargs): pass
    def text_input(self, *args, **kwargs): return ""
    def selectbox(self, *args, **kwargs): return kwargs["options"][0]

    def button(self, texto, **kwargs):
        if texto == "Novo orçamento":
            return self.criar
        if texto == "Abrir versão":
            return self.abrir
        return False

    def rerun(self):
        self.reruns += 1


class TestCriacaoEstrutural(unittest.TestCase):
    def test_cria_orcamento_vazio_com_versao_um_e_cenario_principal(self):
        resultado = criar_orcamento_vazio("fabio")
        self.assertTrue(resultado.sucesso)
        orcamento, versao = resultado.valor
        self.assertEqual(orcamento.objeto, "Novo orçamento")
        self.assertEqual(orcamento.responsavel, "fabio")
        self.assertEqual(versao.numero, 1)
        self.assertEqual(len(orcamento.versoes), 1)
        self.assertEqual(len(versao.cenarios), 1)
        self.assertEqual(versao.cenarios[0].nome, "Cenário Principal")
        self.assertIsNone(versao.dados_obra)

    def test_autor_vazio_e_recusado_sem_criar_estrutura(self):
        resultado = criar_orcamento_vazio(" ")
        self.assertFalse(resultado.sucesso)
        self.assertIsNone(resultado.valor)


class TestFluxoMinimoPainel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.painel = importlib.import_module("modulos.orcamentos.apresentacao.painel")

    def test_criacao_persiste_e_abre_dados_obra_automaticamente(self):
        repositorio = Mock()
        repositorio.carregar_snapshot.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, "snapshot"
        )
        repositorio.carregar_indice_bruto.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO,
            "orcamento_id,versao_id,numero,objeto,finalidade,responsavel,estado\n",
        )
        repositorio.persistir_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="commit-criacao"
        )
        falso = StreamlitFalso(criar=True)

        with patch.object(self.painel, "st", falso):
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())

        repositorio.persistir_versao.assert_called_once()
        orcamento, versao, indice, snapshot = repositorio.persistir_versao.call_args.args
        self.assertEqual(versao.numero, 1)
        self.assertEqual(versao.cenarios[0].nome, "Cenário Principal")
        self.assertIn("orcamento_id", indice)
        self.assertEqual(snapshot, "snapshot")
        self.assertEqual(falso.session_state["novo_orcamento_detalhe"], (orcamento, versao))
        self.assertEqual(falso.session_state["novo_orcamento_snapshot"], "commit-criacao")
        self.assertEqual(falso.reruns, 1)
        repositorio.carregar_indice.assert_not_called()

    def test_reabertura_carrega_versao_e_abre_dados_obra(self):
        resumo = Mock(orcamento_id="orc-1", versao_id="ver-1")
        orcamento, versao = criar_orcamento_vazio("fabio").valor
        repositorio = Mock()
        repositorio.carregar_indice.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, [resumo]
        )
        repositorio.carregar_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, (orcamento, versao)
        )
        repositorio.carregar_snapshot.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, "snapshot-reabertura"
        )
        falso = StreamlitFalso(abrir=True)

        with patch.object(self.painel, "st", falso):
            self.painel.render(repositorio=repositorio, ao_voltar=Mock())

        repositorio.carregar_versao.assert_called_once_with("orc-1", "ver-1")
        self.assertEqual(falso.session_state["novo_orcamento_detalhe"], (orcamento, versao))
        self.assertEqual(
            falso.session_state["novo_orcamento_snapshot"], "snapshot-reabertura"
        )
        self.assertEqual(falso.reruns, 1)


if __name__ == "__main__":
    unittest.main()
