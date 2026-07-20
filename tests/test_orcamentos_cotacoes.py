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
    Cotacoes,
    ItemCotacao,
    PropostaFornecedor,
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
    def __init__(self, *, acoes=(), valores=None, marcacoes=None, session_state=None):
        self.acoes = set(acoes)
        self.valores = valores or {}
        self.marcacoes = marcacoes or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios = []
        self.textos = []
        self.monetarios = []
        self.padroes = {}
        self.sucessos = []
        self.erros = []
        self.avisos = []
        self.reruns = 0

    def form(self, chave):
        self.formularios.append(chave)
        return nullcontext()

    def form_submit_button(self, texto):
        return texto in self.acoes

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
        if kwargs.get("min_value") != 0.0 or kwargs.get("step") != 0.01:
            raise AssertionError("Campo monetário sem suporte a centavos não negativos.")
        return self.valores.get(chave, kwargs.get("value"))

    def checkbox(self, rotulo, **kwargs):
        return self.marcacoes.get(kwargs["key"], False)

    def success(self, texto):
        self.sucessos.append(texto)

    def error(self, texto):
        self.erros.append(texto)

    def warning(self, texto):
        self.avisos.append(texto)

    def rerun(self):
        self.reruns += 1


def item_preenchido():
    return ItemCotacao(
        "item-transporte",
        "Transporte",
        "Preço por viagem",
        "Preço por quilômetro",
        (PropostaFornecedor("Fornecedor", "Ana", "123", "Detalhe", 10.25, 2.50),),
    )


class TestModeloGenericoCotacoes(unittest.TestCase):
    def test_versao_nova_recebe_quatro_itens_iniciais_removiveis(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        self.assertEqual(
            [item.nome for item in versao.cotacoes.itens],
            ["Guindaste", "Container", "Banheiro Químico", "Destinação"],
        )
        self.assertEqual([len(item.propostas) for item in versao.cotacoes.itens], [4, 3, 3, 3])
        self.assertEqual(Cotacoes(()).itens, ())

    def test_item_novo_aceita_nome_rotulos_e_tres_propostas(self):
        item = ItemCotacao.novo(
            "Transporte de equipamento", "Preço por viagem", "Preço por quilômetro"
        )
        self.assertTrue(item.id)
        self.assertEqual(item.nome, "Transporte de equipamento")
        self.assertEqual(item.rotulo_primeiro_valor, "Preço por viagem")
        self.assertEqual(item.rotulo_segundo_valor, "Preço por quilômetro")
        self.assertEqual(len(item.propostas), 3)

    def test_segundo_valor_e_opcional_e_valor_negativo_e_rejeitado(self):
        item = ItemCotacao.novo("Destinação", "Preço por mês")
        self.assertIsNone(item.rotulo_segundo_valor)
        with self.assertRaises(ValueError):
            PropostaFornecedor(primeiro_valor=-0.01)

    def test_centavos_e_identificador_sobrevivem_ao_round_trip(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        item = item_preenchido()
        versao.registrar_cotacoes(Cotacoes((item,)))

        resultado = desserializar_versao(serializar_versao(orcamento, versao))

        self.assertTrue(resultado.sucesso)
        carregado = resultado.valor[1].cotacoes.itens[0]
        self.assertEqual(carregado.id, "item-transporte")
        self.assertEqual(carregado.propostas[0].primeiro_valor, 10.25)
        self.assertEqual(carregado.propostas[0].segundo_valor, 2.50)

    def test_dados_obra_permanece_intacto_no_round_trip(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = DadosObra(objeto="Obra preservada")
        versao.registrar_dados_obra(dados)
        versao.registrar_cotacoes(Cotacoes((item_preenchido(),)))
        carregada = desserializar_versao(serializar_versao(orcamento, versao)).valor[1]
        self.assertEqual(asdict(carregada.dados_obra), asdict(dados))


class TestCompatibilidadeSchemaCinco(unittest.TestCase):
    def test_quatro_grupos_antigos_sao_migrados_sem_perda(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 5
        documento["versao"].pop("producao")
        documento["versao"].pop("barrilete")
        documento["versao"].pop("mobilizacao_draga")
        documento["versao"].pop("mobilizacao_equipamento_polimero")
        documento["versao"].pop("canteiro")
        documento["versao"].pop("preparacao_celula")
        documento["versao"]["cotacoes"] = {
            "guindaste": [
                {
                    "nome": "G1", "contato": "A", "telefone": "1", "detalhe": "D",
                    "preco_hora": 10.25, "preco_diaria": 100.50,
                },
                *[
                    {"nome": "", "contato": "", "telefone": "", "detalhe": "", "preco_hora": None, "preco_diaria": None}
                    for _ in range(3)
                ],
            ],
            "container": [
                {"nome": "C1", "contato": "B", "telefone": "2", "detalhe": "D", "preco_mes": 20.75, "frete_hora": 3.30},
                *[
                    {"nome": "", "contato": "", "telefone": "", "detalhe": "", "preco_mes": None, "frete_hora": None}
                    for _ in range(2)
                ],
            ],
            "banheiro_quimico": [
                {"nome": "B1", "contato": "C", "telefone": "3", "detalhe": "D", "preco_mes": 30.10},
                *[
                    {"nome": "", "contato": "", "telefone": "", "detalhe": "", "preco_mes": None}
                    for _ in range(2)
                ],
            ],
            "destinacao": [
                {"nome": "D1", "contato": "D", "telefone": "4", "detalhe": "D", "preco_mes": 40.99},
                *[
                    {"nome": "", "contato": "", "telefone": "", "detalhe": "", "preco_mes": None}
                    for _ in range(2)
                ],
            ],
        }

        resultado = desserializar_versao(json.dumps(documento))

        self.assertTrue(resultado.sucesso)
        itens = resultado.valor[1].cotacoes.itens
        self.assertEqual([len(item.propostas) for item in itens], [4, 3, 3, 3])
        self.assertEqual(itens[0].propostas[0].nome, "G1")
        self.assertEqual(itens[0].propostas[0].primeiro_valor, 10.25)
        self.assertEqual(itens[0].propostas[0].segundo_valor, 100.50)
        self.assertEqual(itens[3].propostas[0].primeiro_valor, 40.99)
        self.assertFalse(itens[0].propostas[1].preenchida)

    def test_schema_anterior_sem_cotacoes_recebe_itens_iniciais(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 4
        documento["versao"].pop("cotacoes")
        documento["versao"].pop("producao")
        documento["versao"].pop("barrilete")
        documento["versao"].pop("mobilizacao_draga")
        documento["versao"].pop("mobilizacao_equipamento_polimero")
        documento["versao"].pop("canteiro")
        documento["versao"].pop("preparacao_celula")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(len(resultado.valor[1].cotacoes.itens), 4)


class TestTelaMutavelCotacoes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module("modulos.orcamentos.apresentacao.cotacoes")

    def _render(self, falso, repositorio=None, dominio=None):
        orcamento, versao = dominio or criar_orcamento_vazio("Fabio").valor
        repositorio = repositorio or Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="snapshot",
            )
        return orcamento, versao, repositorio

    def test_editar_sem_enviar_tem_zero_operacoes_remotas_e_zero_rerun(self):
        falso = StreamlitCotacoesFalso()
        _, _, repositorio = self._render(falso)
        self.assertEqual(falso.formularios, ["cotacoes_formulario"])
        self.assertEqual(falso.reruns, 0)
        repositorio.carregar_indice.assert_not_called()
        repositorio.carregar_indice_bruto.assert_not_called()
        repositorio.carregar_snapshot.assert_not_called()
        repositorio.carregar_versao.assert_not_called()
        repositorio.persistir_documento_versao.assert_not_called()

    def test_adicionar_item_aplica_localmente_sem_persistir(self):
        estado = {}
        falso = StreamlitCotacoesFalso(
            acoes={"Aplicar alterações"},
            valores={
                "cot_novo_item_nome": "Transporte",
                "cot_novo_item_primeiro": "Preço por viagem",
                "cot_novo_item_segundo": "Preço por km",
            },
            marcacoes={"cot_adicionar_item": True},
            session_state=estado,
        )
        _, _, repositorio = self._render(falso)
        editadas = estado["novo_orcamento_cotacoes_edicao"]
        self.assertEqual(editadas.itens[-1].nome, "Transporte")
        self.assertEqual(len(editadas.itens[-1].propostas), 3)
        self.assertTrue(editadas.itens[-1].id)
        self.assertEqual(falso.reruns, 1)
        repositorio.persistir_documento_versao.assert_not_called()

    def test_adicionar_e_remover_proposta_sao_acoes_explicitas(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_cotacoes(Cotacoes((item_preenchido(),)))
        estado = {}
        adicionar = StreamlitCotacoesFalso(
            acoes={"Aplicar alterações"},
            marcacoes={"cot_item-transporte_adicionar_proposta": True},
            session_state=estado,
        )
        self._render(adicionar, dominio=(orcamento, versao))
        self.assertEqual(len(estado["novo_orcamento_cotacoes_edicao"].itens[0].propostas), 2)

        remover = StreamlitCotacoesFalso(
            acoes={"Aplicar alterações"},
            marcacoes={
                "cot_item-transporte_0_remover": True,
                "cot_item-transporte_0_confirmar": True,
            },
            session_state=estado,
        )
        detalhe = estado["novo_orcamento_detalhe"]
        self._render(remover, dominio=detalhe)
        self.assertEqual(len(estado["novo_orcamento_cotacoes_edicao"].itens[0].propostas), 1)

    def test_dado_preenchido_nao_e_removido_sem_confirmacao(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        versao.registrar_cotacoes(Cotacoes((item_preenchido(),)))
        falso = StreamlitCotacoesFalso(
            acoes={"Aplicar alterações"},
            marcacoes={"cot_item-transporte_0_remover": True},
        )
        self._render(falso, dominio=(orcamento, versao))
        self.assertTrue(falso.avisos)
        self.assertEqual(falso.reruns, 0)

    def test_quatro_itens_iniciais_podem_ser_removidos(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        marcacoes = {
            f"cot_{item.id}_remover_item": True for item in versao.cotacoes.itens
        }
        estado = {}
        falso = StreamlitCotacoesFalso(
            acoes={"Aplicar alterações"}, marcacoes=marcacoes, session_state=estado
        )
        self._render(falso, dominio=(criar_orcamento_vazio("Fabio").valor))
        self.assertEqual(estado["novo_orcamento_cotacoes_edicao"].itens, ())

    def test_salvar_faz_uma_persistencia_sem_indice_e_preserva_dados_obra(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = DadosObra(objeto="Preservado")
        versao.registrar_dados_obra(dados)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="commit"
        )
        falso = StreamlitCotacoesFalso(acoes={"Salvar Cotações"})
        self._render(falso, repositorio, (orcamento, versao))
        repositorio.persistir_documento_versao.assert_called_once()
        salva_versao = repositorio.persistir_documento_versao.call_args.args[1]
        self.assertEqual(asdict(salva_versao.dados_obra), asdict(dados))
        repositorio.carregar_indice.assert_not_called()
        repositorio.carregar_indice_bruto.assert_not_called()
        repositorio.persistir_versao.assert_not_called()
        self.assertEqual(falso.reruns, 1)


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
        versao.registrar_cotacoes(Cotacoes((item_preenchido(),)))
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
