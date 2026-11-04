"""Permissão de consulta restrita ao orçamento, sem acesso geral a CRM/Dados."""
from services import autorizacao


def test_consulta_fonte_exige_acesso_ao_orcamento(monkeypatch):
    monkeypatch.setattr(autorizacao, "pode_acessar", lambda modulo: modulo == "orcamento")
    assert autorizacao.pode_consultar_fonte_composicao("clientes")
    assert autorizacao.pode_consultar_fonte_composicao("materiais")
    assert not autorizacao.pode_consultar_fonte_composicao("salarios")
    assert not autorizacao.pode_consultar_fonte_composicao("interacoes")


def test_consulta_fonte_nega_sem_orcamento(monkeypatch):
    monkeypatch.setattr(autorizacao, "pode_acessar", lambda modulo: False)
    for fonte in ("clientes", "contatos", "materiais", "horarios", "regimes"):
        assert not autorizacao.pode_consultar_fonte_composicao(fonte)
