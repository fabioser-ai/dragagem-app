"""Associação administrativa Usuário operacional → Role, sem efeito de acesso."""

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

import pandas as pd
import streamlit as st

from services.autorizacao import identificador_proprietario, pode_gerenciar_usuarios_roles
from services.github import ResultadoLeituraCSV, StatusLeitura, ler_csv_github, salvar_csv_github
from services.usuarios_operacionais import _logins_protegidos


ARQUIVO = "data/usuarios_roles.csv"
COLUNAS = [
    "usuario_role_id", "usuario_id", "role_id", "ativo",
    "criado_em", "criado_por", "atualizado_em", "atualizado_por",
]


@dataclass(frozen=True)
class ResultadoAssociacao:
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


def carregar_usuarios_roles_resultado():
    try:
        resultado = ler_csv_github(ARQUIVO, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"])
    except Exception:
        return ResultadoLeituraCSV(
            StatusLeitura.ERRO_DESCONHECIDO, _df(), ARQUIVO,
            erro="Configuração indisponível para leitura das associações.",
        )
    dados = _df(resultado.dados) if resultado.leitura_confirmada else _df()
    return ResultadoLeituraCSV(
        resultado.status, dados, ARQUIVO, resultado.http_status,
        resultado.sha, resultado.erro,
    )


def _erro(codigo, mensagem):
    return ResultadoAssociacao(False, codigo, mensagem)


def _leituras_validas(leitura, leitura_usuarios, leitura_roles):
    return all(item is not None and item.pode_sobrescrever for item in (
        leitura, leitura_usuarios, leitura_roles,
    ))


def _validar_usuario_role(*, usuario_id, role_id, leitura_usuarios, leitura_roles):
    usuarios = leitura_usuarios.dados.fillna("")
    roles = leitura_roles.dados.fillna("")
    encontrados = usuarios[usuarios["usuario_id"].astype(str) == str(usuario_id)]
    if len(encontrados) != 1:
        return None, None, _erro("usuario_inexistente", "Usuário operacional não encontrado.")
    usuario = encontrados.iloc[0]
    if str(usuario["ativo"]).strip().casefold() != "sim":
        return None, None, _erro("usuario_inativo", "Usuário inativo não pode receber nova Role.")
    login = str(usuario["login"]).strip().casefold()
    protegidos, falha = _logins_protegidos()
    if falha:
        return None, None, _erro(falha, "Não foi possível validar contas protegidas.")
    if login in protegidos or login == str(identificador_proprietario() or "").casefold():
        return None, None, _erro("conta_protegida", "Conta protegida não pode receber Role.")

    encontradas = roles[roles["role_id"].astype(str) == str(role_id)]
    if len(encontradas) != 1:
        return None, None, _erro("role_inexistente", "Role não encontrada.")
    role = encontradas.iloc[0]
    if str(role["ativo"]).strip().casefold() != "sim":
        return None, None, _erro("role_inativa", "Role inativa não pode ser atribuída.")
    return usuario, role, None


def _persistir(dados, leitura):
    if not pode_gerenciar_usuarios_roles():
        return _erro("nao_autorizado", "Alteração não autorizada.")
    if not leitura.pode_sobrescrever:
        return _erro("leitura_nao_confirmada", "Associações sem leitura confirmada.")
    escrita = salvar_csv_github(
        _df(dados), ARQUIVO, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"],
        sha_esperado=leitura.sha,
    )
    return ResultadoAssociacao(
        escrita.sucesso, "salvo" if escrita.sucesso else "falha_persistencia",
        "Associação salva." if escrita.sucesso else (escrita.erro or "Associação não salva."),
        escrita,
    )


def atribuir_role(*, leitura, leitura_usuarios, leitura_roles, usuario_id, role_id):
    if not pode_gerenciar_usuarios_roles():
        return _erro("nao_autorizado", "Alteração não autorizada.")
    if not _leituras_validas(leitura, leitura_usuarios, leitura_roles):
        return _erro("leitura_nao_confirmada", "Todas as bases devem ter leitura confirmada.")
    _, _, erro = _validar_usuario_role(
        usuario_id=usuario_id, role_id=role_id,
        leitura_usuarios=leitura_usuarios, leitura_roles=leitura_roles,
    )
    if erro:
        return erro
    dados = _df(leitura.dados)
    iguais = dados[
        (dados["usuario_id"].astype(str) == str(usuario_id))
        & (dados["role_id"].astype(str) == str(role_id))
    ]
    ativas = iguais[iguais["ativo"].astype(str).str.casefold() == "sim"]
    if not ativas.empty:
        return _erro("associacao_duplicada", "Associação ativa já existe.")
    agora = datetime.now(timezone.utc).isoformat()
    autor = str(st.session_state.get("usuario") or "")
    atualizado = dados.copy()
    if not iguais.empty:
        indice = iguais.index[-1]
        atualizado.at[indice, "ativo"] = "sim"
        atualizado.at[indice, "atualizado_em"] = agora
        atualizado.at[indice, "atualizado_por"] = autor
    else:
        registro = {
            "usuario_role_id": str(uuid4()), "usuario_id": str(usuario_id),
            "role_id": str(role_id), "ativo": "sim", "criado_em": agora,
            "criado_por": autor, "atualizado_em": agora, "atualizado_por": autor,
        }
        atualizado = pd.concat([atualizado, pd.DataFrame([registro])], ignore_index=True)
    return _persistir(atualizado, leitura)


def retirar_role(*, leitura, leitura_usuarios, leitura_roles, usuario_id, role_id):
    if not pode_gerenciar_usuarios_roles():
        return _erro("nao_autorizado", "Alteração não autorizada.")
    if not _leituras_validas(leitura, leitura_usuarios, leitura_roles):
        return _erro("leitura_nao_confirmada", "Todas as bases devem ter leitura confirmada.")
    dados = _df(leitura.dados)
    indices = dados.index[
        (dados["usuario_id"].astype(str) == str(usuario_id))
        & (dados["role_id"].astype(str) == str(role_id))
        & (dados["ativo"].astype(str).str.casefold() == "sim")
    ].tolist()
    if len(indices) != 1:
        return _erro("associacao_ativa_inexistente", "Associação ativa não encontrada.")
    atualizado = dados.copy()
    indice = indices[0]
    atualizado.at[indice, "ativo"] = "nao"
    atualizado.at[indice, "atualizado_em"] = datetime.now(timezone.utc).isoformat()
    atualizado.at[indice, "atualizado_por"] = str(st.session_state.get("usuario") or "")
    return _persistir(atualizado, leitura)
