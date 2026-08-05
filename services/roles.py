"""Catálogo isolado de Roles e permissões do RBAC-001.

O catálogo ainda não participa da autenticação, dos usuários nem do cálculo de
permissões da aplicação.
"""

import re
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

import pandas as pd
import streamlit as st

from services.autorizacao import pode_gerenciar_roles
from services.github import ResultadoLeituraCSV, StatusLeitura, ler_csv_github, salvar_csv_github


ARQUIVO_ROLES = "data/roles.csv"
ARQUIVO_PERMISSOES = "data/roles_permissoes.csv"
COLUNAS_ROLES = [
    "role_id", "codigo", "nome", "descricao", "ativo", "versao",
    "criado_em", "criado_por", "atualizado_em", "atualizado_por",
]
COLUNAS_PERMISSOES = ["role_id", "modulo", "recurso", "acao", "efeito"]
ACOES_PADRONIZADAS = (
    "visualizar", "criar", "editar", "excluir", "aprovar", "cancelar", "administrar",
)
EFEITOS = ("allow", "deny")
_CODIGO = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
_ROLES_PROTEGIDAS = {
    "SUPERADMIN", "OWNER", "PROPRIETARIO", "ROOT", "SYSTEM",
    "CUSTODIANTE", "CUSTODIAN",
}


@dataclass(frozen=True)
class ResultadoRole:
    sucesso: bool
    codigo: str
    mensagem: str
    escrita: object = None


def _df(dados, colunas):
    base = pd.DataFrame() if dados is None else dados.copy()
    for coluna in colunas:
        if coluna not in base.columns:
            base[coluna] = ""
    return base[colunas].fillna("")


def _resultado_leitura(arquivo, colunas):
    try:
        resultado = ler_csv_github(
            arquivo, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"]
        )
    except Exception:
        return ResultadoLeituraCSV(
            StatusLeitura.ERRO_DESCONHECIDO, _df(None, colunas), arquivo,
            erro="Configuração indisponível para leitura do catálogo RBAC.",
        )
    dados = _df(resultado.dados, colunas) if resultado.leitura_confirmada else _df(None, colunas)
    return ResultadoLeituraCSV(
        resultado.status, dados, arquivo, resultado.http_status,
        resultado.sha, resultado.erro,
    )


def carregar_roles_resultado():
    return _resultado_leitura(ARQUIVO_ROLES, COLUNAS_ROLES)


def carregar_roles_permissoes_resultado():
    return _resultado_leitura(ARQUIVO_PERMISSOES, COLUNAS_PERMISSOES)


def normalizar_codigo(valor):
    texto = unicodedata.normalize("NFKD", str(valor or "").strip())
    texto = "".join(c for c in texto if not unicodedata.combining(c)).upper()
    texto = re.sub(r"[\s-]+", "_", texto)
    return texto if _CODIGO.fullmatch(texto) else None


def validar_roles_permissoes(dados, catalogo_roles, catalogo_permissoes):
    """Valida a matriz documental sem calcular ou conceder acesso a usuários."""
    matriz = _df(dados, COLUNAS_PERMISSOES)
    roles_ativos = _df(catalogo_roles, COLUNAS_ROLES)
    roles_ativos = roles_ativos[
        roles_ativos["ativo"].astype(str).str.strip().str.casefold() == "sim"
    ]
    ids_roles = set(roles_ativos["role_id"].astype(str))

    permissoes = pd.DataFrame() if catalogo_permissoes is None else catalogo_permissoes.copy()
    for coluna in ("modulo", "recurso", "acao", "sensibilidade", "ativo"):
        if coluna not in permissoes.columns:
            permissoes[coluna] = ""
    permissoes = permissoes[
        permissoes["ativo"].astype(str).str.strip().str.casefold() == "sim"
    ]
    chaves_permissoes = {
        (str(linha.modulo), str(linha.recurso), str(linha.acao))
        for linha in permissoes.itertuples(index=False)
    }
    criticas = {
        (str(linha.modulo), str(linha.recurso), str(linha.acao))
        for linha in permissoes.itertuples(index=False)
        if str(linha.sensibilidade).strip().casefold() == "crítica"
    }

    erros = []
    identidades = ["role_id", "modulo", "recurso", "acao"]
    for indice, linha in matriz.iterrows():
        chave = (str(linha["modulo"]), str(linha["recurso"]), str(linha["acao"]))
        if str(linha["role_id"]) not in ids_roles:
            erros.append(f"role_inexistente:{indice}")
        if chave not in chaves_permissoes:
            erros.append(f"permissao_inexistente:{indice}")
        if chave in criticas or chave[0] == "administracao":
            erros.append(f"permissao_critica_proibida:{indice}")
        if str(linha["efeito"]).strip().casefold() not in EFEITOS:
            erros.append(f"efeito_invalido:{indice}")
    for indice in matriz.index[matriz.duplicated(identidades, keep=False)]:
        erros.append(f"duplicidade:{indice}")
    return erros


def _codigo_protegido(codigo):
    return codigo.replace("_", "") in {item.replace("_", "") for item in _ROLES_PROTEGIDAS}


def _validar(dados, *, codigo, nome, descricao, ignorar_id=None):
    codigo_norm = normalizar_codigo(codigo)
    if codigo_norm is None:
        return None, ResultadoRole(False, "codigo_invalido", "Código de Role inválido.")
    if _codigo_protegido(codigo_norm):
        return None, ResultadoRole(False, "role_protegida", "Esta Role é reservada ao sistema.")
    nome_norm = str(nome or "").strip()
    if not nome_norm:
        return None, ResultadoRole(False, "nome_invalido", "Nome é obrigatório.")
    outros = dados[
        dados["role_id"].astype(str) != str(ignorar_id)
    ] if ignorar_id else dados
    existentes = set(outros["codigo"].astype(str).str.strip().str.upper())
    if codigo_norm in existentes:
        return None, ResultadoRole(False, "codigo_duplicado", "Código de Role já cadastrado.")
    return {
        "codigo": codigo_norm,
        "nome": nome_norm,
        "descricao": str(descricao or "").strip(),
    }, None


def _persistir(dados, leitura):
    # Revalidação deliberadamente imediata antes da chamada de escrita.
    if not pode_gerenciar_roles():
        return ResultadoRole(False, "nao_autorizado", "Alteração não autorizada.")
    if not leitura.pode_sobrescrever:
        return ResultadoRole(False, "leitura_nao_confirmada", "Catálogo não pode ser alterado sem leitura confirmada.")
    escrita = salvar_csv_github(
        _df(dados, COLUNAS_ROLES), ARQUIVO_ROLES,
        st.secrets["GITHUB_TOKEN"], st.secrets["REPO"],
        sha_esperado=leitura.sha,
    )
    return ResultadoRole(
        escrita.sucesso,
        "salvo" if escrita.sucesso else "falha_persistencia",
        "Role salva." if escrita.sucesso else (escrita.erro or "Role não salva."),
        escrita,
    )


def criar_role(*, leitura, codigo, nome, descricao=""):
    if not pode_gerenciar_roles():
        return ResultadoRole(False, "nao_autorizado", "Alteração não autorizada.")
    if not leitura.pode_sobrescrever:
        return ResultadoRole(False, "leitura_nao_confirmada", "Leitura do catálogo não confirmada.")
    dados = _df(leitura.dados, COLUNAS_ROLES)
    campos, erro = _validar(dados, codigo=codigo, nome=nome, descricao=descricao)
    if erro:
        return erro
    agora = datetime.now(timezone.utc).isoformat()
    autor = str(st.session_state.get("usuario") or "")
    registro = {
        "role_id": str(uuid4()), **campos, "ativo": "nao", "versao": 1,
        "criado_em": agora, "criado_por": autor,
        "atualizado_em": agora, "atualizado_por": autor,
    }
    return _persistir(pd.concat([dados, pd.DataFrame([registro])], ignore_index=True), leitura)


def editar_role(*, leitura, role_id, nome, descricao="", ativo="nao"):
    if not pode_gerenciar_roles():
        return ResultadoRole(False, "nao_autorizado", "Alteração não autorizada.")
    if not leitura.pode_sobrescrever:
        return ResultadoRole(False, "leitura_nao_confirmada", "Leitura do catálogo não confirmada.")
    dados = _df(leitura.dados, COLUNAS_ROLES)
    indices = dados.index[dados["role_id"].astype(str) == str(role_id)].tolist()
    if len(indices) != 1:
        return ResultadoRole(False, "role_nao_encontrada", "Role não encontrada.")
    indice = indices[0]
    campos, erro = _validar(
        dados, codigo=dados.at[indice, "codigo"], nome=nome,
        descricao=descricao, ignorar_id=role_id,
    )
    if erro:
        return erro
    ativo_norm = str(ativo).strip().casefold()
    if ativo_norm not in {"sim", "nao"}:
        return ResultadoRole(False, "estado_invalido", "Estado inválido.")
    atualizado = dados.copy()
    atualizado.at[indice, "nome"] = campos["nome"]
    atualizado.at[indice, "descricao"] = campos["descricao"]
    atualizado.at[indice, "ativo"] = ativo_norm
    try:
        versao = int(atualizado.at[indice, "versao"])
    except (TypeError, ValueError):
        versao = 0
    atualizado.at[indice, "versao"] = versao + 1
    atualizado.at[indice, "atualizado_em"] = datetime.now(timezone.utc).isoformat()
    atualizado.at[indice, "atualizado_por"] = str(st.session_state.get("usuario") or "")
    return _persistir(atualizado, leitura)
