"""Testes isolados: nenhum acesso ao GitHub operacional."""
from types import SimpleNamespace

import pandas as pd
import pytest

from services import composicao_fontes as fontes
from services.github import StatusLeitura


def _resposta(status, dados=None, erro=None):
    return SimpleNamespace(status=status, dados=dados, erro=erro, sha="sha-teste")


def test_cliente_oficial_e_crm(monkeypatch):
    chamados = []
    def ler(arquivo, token, repo):
        chamados.append(arquivo)
        return _resposta(StatusLeitura.SUCESSO_COM_DADOS,
                         pd.DataFrame([{"id_cliente": "c1", "nome_empresa": "Empresa"}]))
    monkeypatch.setattr(fontes, "ler_csv_operacional", ler)
    resultado = fontes.consultar_catalogo("clientes", "token", "repo")
    # Um esquema incompleto deve falhar fechado, sem inventar colunas.
    assert not resultado.disponivel
    assert "Colunas obrigatórias" in resultado.erro
    assert chamados == ["data/crm/clientes.csv"]


def test_indisponibilidade_nao_equivale_a_vazio(monkeypatch):
    monkeypatch.setattr(fontes, "ler_csv_operacional",
                        lambda *args: _resposta(StatusLeitura.ARQUIVO_INEXISTENTE))
    resultado = fontes.consultar_catalogo("materiais", "token", "repo")
    assert not resultado.disponivel
    assert resultado.dados.empty
    with pytest.raises(ValueError):
        fontes.listar_opcoes(resultado, "Material")


def test_catalogo_valido_e_opcoes(monkeypatch):
    dados = pd.DataFrame({"Material": ["Areia", " Argila ", "Areia"],
                          "Solidos_InSitu": ["10", "20", "10"],
                          "Solidos_Desaguado": ["15", "25", "15"]})
    monkeypatch.setattr(fontes, "ler_csv_operacional",
                        lambda *args: _resposta(StatusLeitura.SUCESSO_COM_DADOS, dados))
    resultado = fontes.consultar_catalogo("materiais", "token", "repo")
    assert resultado.disponivel
    assert fontes.listar_opcoes(resultado, "Material") == ["Areia", "Argila"]


def test_contatos_somente_do_cliente_escolhido():
    clientes = fontes.LeituraCatalogo("clientes", "a", True,
        pd.DataFrame({"id_cliente": ["1", "2"]}), "sucesso")
    contatos = fontes.LeituraCatalogo("contatos", "b", True,
        pd.DataFrame({"id_cliente": ["1", "2", "1"],
                      "id_contato": ["a", "b", "c"]}), "sucesso")
    encontrados = fontes.contatos_do_cliente(clientes, contatos, "1")
    assert encontrados["id_contato"].tolist() == ["a", "c"]
    with pytest.raises(ValueError):
        fontes.contatos_do_cliente(clientes, contatos, "inexistente")


def test_fonte_desconhecida_rejeitada():
    with pytest.raises(ValueError):
        fontes.consultar_catalogo("clientes_legado", "token", "repo")
