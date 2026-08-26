"""Catálogo canônico e não efetivo de capacidades do RBAC-002."""

from dataclasses import dataclass
import re

import pandas as pd
import streamlit as st

from services.autorizacao import pode_gerenciar_catalogo_permissoes
from services.github import ResultadoLeituraCSV, StatusLeitura, ler_csv_github, salvar_csv_github


ARQUIVO = "data/permissoes_catalogo.csv"
COLUNAS = [
    "permissao_id", "modulo", "recurso", "acao", "nome", "descricao",
    "sensibilidade", "escopo_obra", "estado_protecao", "evidencia", "ativo",
    "criado_em", "criado_por", "atualizado_em", "atualizado_por",
]
MODULOS = {
    "administracao", "dados", "ferias", "prestacao_contas", "medicoes",
    "crm", "uniformes_epis", "obras", "orcamento",
}
ACOES = {
    "visualizar", "criar", "editar", "excluir", "aprovar", "cancelar", "administrar", "alterar",
}
SENSIBILIDADES = {"baixa", "média", "alta", "crítica"}
ESTADOS_PROTECAO = {
    "completa", "parcial", "inexistente", "específica de Medições", "não aplicável",
}
_IDENTIFICADOR = re.compile(r"^[a-z][a-z0-9_]{1,63}$")


@dataclass(frozen=True)
class ResultadoCatalogo:
    sucesso: bool
    codigo: str
    mensagem: str
    escrita: object = None


def _df(dados=None):
    base = pd.DataFrame() if dados is None else dados.copy()
    for coluna in COLUNAS:
        if coluna not in base.columns:
            base[coluna] = ""
    return base[COLUNAS].fillna("")


def carregar_catalogo_resultado():
    try:
        resultado = ler_csv_github(
            ARQUIVO, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"]
        )
    except Exception:
        return ResultadoLeituraCSV(
            StatusLeitura.ERRO_DESCONHECIDO, _df(), ARQUIVO,
            erro="Configuração indisponível para leitura do catálogo de permissões.",
        )
    dados = _df(resultado.dados) if resultado.leitura_confirmada else _df()
    return ResultadoLeituraCSV(
        resultado.status, dados, ARQUIVO, resultado.http_status,
        resultado.sha, resultado.erro,
    )


def validar_catalogo(dados):
    df = _df(dados)
    erros = []
    if df["permissao_id"].astype(str).duplicated().any():
        erros.append("permissao_id_duplicada")
    combinacoes = df[["modulo", "recurso", "acao"]].astype(str)
    if combinacoes.duplicated().any():
        erros.append("combinacao_duplicada")
    for indice, linha in df.iterrows():
        modulo = str(linha["modulo"]).strip()
        recurso = str(linha["recurso"]).strip()
        acao = str(linha["acao"]).strip()
        if modulo not in MODULOS:
            erros.append(f"modulo_invalido:{indice}")
        if not _IDENTIFICADOR.fullmatch(recurso):
            erros.append(f"recurso_invalido:{indice}")
        if acao not in ACOES:
            erros.append(f"acao_invalida:{indice}")
        if str(linha["sensibilidade"]).strip() not in SENSIBILIDADES:
            erros.append(f"sensibilidade_invalida:{indice}")
        if str(linha["estado_protecao"]).strip() not in ESTADOS_PROTECAO:
            erros.append(f"estado_protecao_invalido:{indice}")
        if str(linha["ativo"]).strip() not in {"sim", "nao"}:
            erros.append(f"ativo_invalido:{indice}")
    return erros


def salvar_catalogo_seguro(dados, *, leitura):
    """Ponto protegido para regeneração técnica; não é exposto pela interface."""
    if not pode_gerenciar_catalogo_permissoes():
        return ResultadoCatalogo(False, "nao_autorizado", "Alteração não autorizada.")
    if not leitura.pode_sobrescrever:
        return ResultadoCatalogo(False, "leitura_nao_confirmada", "Leitura do catálogo não confirmada.")
    erros = validar_catalogo(dados)
    atuais = _df(leitura.dados)
    propostos = _df(dados)
    ids_propostos = set(propostos["permissao_id"].astype(str))
    for _, atual in atuais.iterrows():
        permissao_id = str(atual["permissao_id"])
        if permissao_id not in ids_propostos:
            erros.append(f"exclusao_fisica_negada:{permissao_id}")
            continue
        proposta = propostos[propostos["permissao_id"].astype(str) == permissao_id].iloc[0]
        identidade_atual = tuple(str(atual[c]) for c in ("modulo", "recurso", "acao"))
        identidade_proposta = tuple(str(proposta[c]) for c in ("modulo", "recurso", "acao"))
        if identidade_atual != identidade_proposta:
            erros.append(f"identidade_imutavel:{permissao_id}")
    ids_atuais = set(atuais["permissao_id"].astype(str))
    novas = propostos[~propostos["permissao_id"].astype(str).isin(ids_atuais)]
    if (novas["ativo"].astype(str) != "nao").any():
        erros.append("permissao_nova_deve_nascer_inativa")
    if erros:
        return ResultadoCatalogo(False, "catalogo_invalido", "; ".join(erros))
    # Revalidação deliberadamente imediata antes da escrita remota.
    if not pode_gerenciar_catalogo_permissoes():
        return ResultadoCatalogo(False, "nao_autorizado", "Alteração não autorizada.")
    escrita = salvar_csv_github(
        _df(dados), ARQUIVO, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"],
        sha_esperado=leitura.sha,
    )
    return ResultadoCatalogo(
        escrita.sucesso,
        "salvo" if escrita.sucesso else "falha_persistencia",
        "Catálogo salvo." if escrita.sucesso else (escrita.erro or "Catálogo não salvo."),
        escrita,
    )
