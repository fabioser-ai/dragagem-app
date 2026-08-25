"""Identidade e persistência dos usuários operacionais (AUTH-001/002)."""

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

import pandas as pd
import streamlit as st

from services.autorizacao import pode_gerenciar_usuarios_operacionais
from services.github import ResultadoLeituraCSV, StatusLeitura, ler_csv_github, salvar_csv_github


ARQUIVO = "data/usuarios_operacionais.csv"
COLUNAS = [
    "usuario_id", "login", "nome", "matricula", "email", "perfil_base",
    "ativo", "criado_em", "criado_por", "atualizado_em", "atualizado_por",
    "exige_troca_senha", "credencial_configurada",
]
PERFIS_PERMITIDOS = ("user", "funcionario", "encarregado", "aprovador")
_LOGIN = re.compile(r"^[a-z0-9_.@+-]{1,128}$")
_EMAIL = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


@dataclass(frozen=True)
class ResultadoOperacao:
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


def carregar_usuarios_operacionais_resultado():
    try:
        resultado = ler_csv_github(ARQUIVO, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"])
    except Exception:
        return ResultadoLeituraCSV(
            StatusLeitura.ERRO_DESCONHECIDO, _df(), ARQUIVO,
            erro="Configuração indisponível para leitura da base operacional.",
        )
    dados = _df(resultado.dados) if resultado.leitura_confirmada else _df()
    return ResultadoLeituraCSV(
        resultado.status, dados, ARQUIVO, resultado.http_status,
        resultado.sha, resultado.erro,
    )


def _logins_protegidos():
    """Retorna apenas identificadores normalizados; nunca retorna dados das contas."""
    try:
        bruto = st.secrets["APP_USERS"]
        usuarios = json.loads(bruto) if isinstance(bruto, str) else bruto
        if not isinstance(usuarios, dict):
            raise ValueError("estrutura inválida")
        logins = {str(login).strip().casefold() for login in usuarios}
        if "" in logins:
            raise ValueError("identificador inválido")
        return logins, None
    except Exception:
        return None, "app_users_indisponivel"


def _normalizar_login(valor):
    login = str(valor or "").strip().casefold()
    return login if _LOGIN.fullmatch(login) else None


def _validar_campos(df, *, login, nome, matricula, email, perfil_base, ignorar_id=None):
    login_norm = _normalizar_login(login)
    if login_norm is None:
        return None, ResultadoOperacao(False, "login_invalido", "Login inválido.")
    nome_norm = str(nome or "").strip()
    if not nome_norm:
        return None, ResultadoOperacao(False, "nome_invalido", "Nome é obrigatório.")
    perfil_norm = str(perfil_base or "").strip().casefold()
    if perfil_norm not in PERFIS_PERMITIDOS:
        return None, ResultadoOperacao(False, "perfil_negado", "Perfil base não permitido.")
    matricula_norm = str(matricula or "").strip()
    email_norm = str(email or "").strip().casefold()
    if email_norm and not _EMAIL.fullmatch(email_norm):
        return None, ResultadoOperacao(False, "email_invalido", "E-mail inválido.")

    protegidos, erro = _logins_protegidos()
    if erro:
        return None, ResultadoOperacao(False, erro, "Não foi possível validar os identificadores protegidos.")
    if login_norm in protegidos:
        return None, ResultadoOperacao(False, "login_protegido", "Identificador reservado por conta protegida.")

    outros = df[df["usuario_id"].astype(str) != str(ignorar_id)] if ignorar_id else df
    if login_norm in set(outros["login"].astype(str).str.strip().str.casefold()):
        return None, ResultadoOperacao(False, "login_duplicado", "Login já cadastrado.")
    if matricula_norm and matricula_norm.casefold() in set(
        outros["matricula"].astype(str).str.strip().str.casefold()
    ):
        return None, ResultadoOperacao(False, "matricula_duplicada", "Matrícula já cadastrada.")
    return {
        "login": login_norm, "nome": nome_norm, "matricula": matricula_norm,
        "email": email_norm, "perfil_base": perfil_norm,
    }, None


def _persistir(df, leitura):
    if not pode_gerenciar_usuarios_operacionais():
        return ResultadoOperacao(False, "nao_autorizado", "Alteração não autorizada.")
    if not leitura.pode_sobrescrever:
        return ResultadoOperacao(False, "leitura_nao_confirmada", "A base operacional não pode ser alterada sem leitura confirmada.")
    escrita = salvar_csv_github(
        _df(df), ARQUIVO, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"],
        sha_esperado=leitura.sha,
    )
    return ResultadoOperacao(
        escrita.sucesso,
        "salvo" if escrita.sucesso else "falha_persistencia",
        "Alteração salva." if escrita.sucesso else (escrita.erro or "Alteração não salva."),
        escrita,
    )


def criar_usuario(*, leitura, login, nome, matricula="", email="", perfil_base="user"):
    if not pode_gerenciar_usuarios_operacionais():
        return ResultadoOperacao(False, "nao_autorizado", "Alteração não autorizada.")
    if not leitura.pode_sobrescrever:
        return ResultadoOperacao(False, "leitura_nao_confirmada", "Leitura da base não confirmada.")
    dados = _df(leitura.dados)
    campos, erro = _validar_campos(
        dados, login=login, nome=nome, matricula=matricula, email=email,
        perfil_base=perfil_base,
    )
    if erro:
        return erro
    agora = datetime.now(timezone.utc).isoformat()
    autor = str(st.session_state.get("usuario") or "")
    registro = {
        "usuario_id": str(uuid4()), **campos, "ativo": "nao",
        "criado_em": agora, "criado_por": autor, "atualizado_em": agora,
        "atualizado_por": autor, "exige_troca_senha": "nao",
        "credencial_configurada": "nao",
    }
    return _persistir(pd.concat([dados, pd.DataFrame([registro])], ignore_index=True), leitura)


def editar_usuario(*, leitura, usuario_id, nome, matricula="", email="", perfil_base="user", ativo="nao"):
    if not pode_gerenciar_usuarios_operacionais():
        return ResultadoOperacao(False, "nao_autorizado", "Alteração não autorizada.")
    if not leitura.pode_sobrescrever:
        return ResultadoOperacao(False, "leitura_nao_confirmada", "Leitura da base não confirmada.")
    dados = _df(leitura.dados)
    indices = dados.index[dados["usuario_id"].astype(str) == str(usuario_id)].tolist()
    if len(indices) != 1:
        return ResultadoOperacao(False, "usuario_nao_encontrado", "Usuário operacional não encontrado.")
    indice = indices[0]
    login = dados.at[indice, "login"]
    campos, erro = _validar_campos(
        dados, login=login, nome=nome, matricula=matricula, email=email,
        perfil_base=perfil_base, ignorar_id=usuario_id,
    )
    if erro:
        return erro
    ativo_norm = str(ativo).strip().casefold()
    if ativo_norm not in {"sim", "nao"}:
        return ResultadoOperacao(False, "estado_invalido", "Estado inválido.")
    atualizado = dados.copy()
    for chave, valor in campos.items():
        atualizado.at[indice, chave] = valor
    atualizado.at[indice, "ativo"] = ativo_norm
    atualizado.at[indice, "atualizado_em"] = datetime.now(timezone.utc).isoformat()
    atualizado.at[indice, "atualizado_por"] = str(st.session_state.get("usuario") or "")
    return _persistir(atualizado, leitura)
