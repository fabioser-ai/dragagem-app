"""Credenciais bcrypt separadas da identidade operacional (AUTH-002)."""

from dataclasses import dataclass
from datetime import datetime, timezone
import re

import bcrypt
import pandas as pd
import streamlit as st

from services.autorizacao import pode_gerenciar_usuarios_operacionais
from services.github import ResultadoLeituraCSV, StatusLeitura, ler_csv_github
from services.persistencia_multi_arquivo import (
    AlteracaoArquivoConteudo,
    publicar_arquivos_em_commit,
    resolver_snapshot_branch,
)
from services.usuarios_operacionais import (
    ARQUIVO as ARQUIVO_USUARIOS,
    COLUNAS as COLUNAS_USUARIOS,
    PERFIS_PERMITIDOS,
    _logins_protegidos,
)

ARQUIVO = "data/credenciais_operacionais.csv"
COLUNAS = [
    "usuario_id", "password_hash", "algoritmo", "configurada_em",
    "configurada_por", "atualizada_em", "atualizada_por",
]
ALGORITMO = "bcrypt"
BRANCH_PADRAO = "main"
_HASH_BCRYPT = re.compile(r"^\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}$")


@dataclass(frozen=True)
class ResultadoCredencial:
    sucesso: bool
    codigo: str
    mensagem: str
    escrita: object = None


@dataclass(frozen=True)
class DiagnosticoCredencial:
    disponivel: bool
    codigo: str


def hash_bcrypt_estruturalmente_valido(password_hash):
    """Valida somente o formato público do hash; não tenta validar uma senha."""
    return bool(
        isinstance(password_hash, str)
        and _HASH_BCRYPT.fullmatch(password_hash.strip())
    )


def diagnosticar_credencial(usuario, leitura_credenciais):
    """Determina o estado observável da credencial para diagnóstico administrativo."""
    try:
        if str(usuario["credencial_configurada"]).strip().casefold() != "sim":
            return DiagnosticoCredencial(False, "nao_configurada")
        if not leitura_credenciais.leitura_confirmada:
            return DiagnosticoCredencial(False, "leitura_nao_confirmada")

        usuario_id = str(usuario["usuario_id"])
        registros = _df(leitura_credenciais.dados)
        registros = registros[
            registros["usuario_id"].astype(str) == usuario_id
        ]
        if len(registros) != 1:
            return DiagnosticoCredencial(False, "registro_inconsistente")

        credencial = registros.iloc[0]
        if str(credencial["algoritmo"]).strip().casefold() != ALGORITMO:
            return DiagnosticoCredencial(False, "algoritmo_invalido")
        if not hash_bcrypt_estruturalmente_valido(str(credencial["password_hash"])):
            return DiagnosticoCredencial(False, "hash_invalido")
        return DiagnosticoCredencial(True, "disponivel")
    except Exception:
        return DiagnosticoCredencial(False, "estado_inconsistente")


def _df(dados=None):
    base = pd.DataFrame() if dados is None else dados.copy()
    for coluna in COLUNAS:
        if coluna not in base.columns:
            base[coluna] = ""
    return base[COLUNAS].fillna("")


def _df_usuarios(dados=None):
    base = pd.DataFrame() if dados is None else dados.copy()
    for coluna in COLUNAS_USUARIOS:
        if coluna not in base.columns:
            base[coluna] = ""
    return base[COLUNAS_USUARIOS].fillna("")


def gerar_hash(senha):
    if not isinstance(senha, str) or not senha:
        raise ValueError("senha inválida")
    return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("ascii")


def verificar_hash(senha, password_hash):
    try:
        if not isinstance(senha, str) or not isinstance(password_hash, str):
            return False
        if not password_hash.startswith(("$2a$", "$2b$", "$2y$")):
            return False
        return bcrypt.checkpw(senha.encode("utf-8"), password_hash.encode("ascii"))
    except (ValueError, TypeError, UnicodeError):
        return False


def carregar_credenciais_resultado(*, ref=None):
    try:
        resultado = ler_csv_github(
            ARQUIVO, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"], ref=ref
        )
    except Exception:
        return ResultadoLeituraCSV(
            StatusLeitura.ERRO_DESCONHECIDO, _df(), ARQUIVO,
            erro="Configuração indisponível para leitura da base de credenciais.",
        )
    dados = _df(resultado.dados) if resultado.leitura_confirmada else _df()
    return ResultadoLeituraCSV(
        resultado.status, dados, ARQUIVO, resultado.http_status,
        resultado.sha, resultado.erro,
    )


def autenticar_usuario_operacional(*, login, senha, usuarios_protegidos):
    """Retorna dados de sessão ou ``None`` sem revelar a causa da negação."""
    try:
        if not isinstance(usuarios_protegidos, dict):
            return None
        login_norm = str(login or "").strip().casefold()
        protegidos = {str(item).strip().casefold() for item in usuarios_protegidos}
        if not login_norm or login_norm in protegidos:
            return None

        usuarios = ler_csv_github(
            ARQUIVO_USUARIOS, st.secrets["GITHUB_TOKEN"], st.secrets["REPO"]
        )
        credenciais = carregar_credenciais_resultado()
        if not usuarios.leitura_confirmada or not credenciais.leitura_confirmada:
            return None
        identidades = _df_usuarios(usuarios.dados)
        encontrados = identidades[
            identidades["login"].astype(str).str.strip().str.casefold() == login_norm
        ]
        if len(encontrados) != 1:
            return None
        identidade = encontrados.iloc[0]
        perfil = str(identidade["perfil_base"]).strip().casefold()
        if str(identidade["ativo"]).strip().casefold() != "sim":
            return None
        if str(identidade["credencial_configurada"]).strip().casefold() != "sim":
            return None
        if perfil not in PERFIS_PERMITIDOS:
            return None

        registros = credenciais.dados[
            credenciais.dados["usuario_id"].astype(str) == str(identidade["usuario_id"])
        ]
        if len(registros) != 1:
            return None
        credencial = registros.iloc[0]
        if str(credencial["algoritmo"]).strip().casefold() != ALGORITMO:
            return None
        if not verificar_hash(senha, str(credencial["password_hash"])):
            return None
        return {
            "usuario": str(identidade["login"]),
            "perfil": perfil,
            "matricula": str(identidade["matricula"]),
            "nome": str(identidade["nome"]),
        }
    except Exception:
        return None


def configurar_credencial(*, usuario_id, senha):
    """Configura credencial e marcador de identidade em um único commit Git."""
    if not pode_gerenciar_usuarios_operacionais():
        return ResultadoCredencial(False, "nao_autorizado", "Alteração não autorizada.")
    try:
        token = st.secrets["GITHUB_TOKEN"]
        repo = st.secrets["REPO"]
        branch = st.secrets.get("GITHUB_BRANCH", BRANCH_PADRAO)
    except Exception:
        return ResultadoCredencial(False, "configuracao_indisponivel", "Configuração indisponível.")

    snapshot = resolver_snapshot_branch(token, repo, branch)
    if not hasattr(snapshot, "commit_sha"):
        return ResultadoCredencial(False, "leitura_nao_confirmada", "Não foi possível confirmar as bases.")
    try:
        usuarios = ler_csv_github(ARQUIVO_USUARIOS, token, repo, ref=snapshot.commit_sha)
        credenciais = carregar_credenciais_resultado(ref=snapshot.commit_sha)
    except Exception:
        return ResultadoCredencial(False, "leitura_nao_confirmada", "Não foi possível confirmar as bases.")
    if not usuarios.pode_sobrescrever or not credenciais.leitura_confirmada:
        return ResultadoCredencial(False, "leitura_nao_confirmada", "Não foi possível confirmar as bases.")

    identidades = _df_usuarios(usuarios.dados)
    indices = identidades.index[
        identidades["usuario_id"].astype(str) == str(usuario_id)
    ].tolist()
    if len(indices) != 1:
        return ResultadoCredencial(False, "usuario_nao_encontrado", "Usuário operacional não encontrado.")
    indice = indices[0]
    perfil = str(identidades.at[indice, "perfil_base"]).strip().casefold()
    if perfil not in PERFIS_PERMITIDOS:
        return ResultadoCredencial(False, "perfil_negado", "Credencial não configurada.")
    protegidos, erro_protegidos = _logins_protegidos()
    login = str(identidades.at[indice, "login"]).strip().casefold()
    if erro_protegidos or not login or login in protegidos:
        return ResultadoCredencial(False, "login_protegido", "Credencial não configurada.")
    try:
        password_hash = gerar_hash(senha)
    except (ValueError, TypeError):
        return ResultadoCredencial(False, "senha_invalida", "Senha não informada.")

    agora = datetime.now(timezone.utc).isoformat()
    autor = str(st.session_state.get("usuario") or "")
    base_credenciais = _df(credenciais.dados)
    existentes = base_credenciais.index[
        base_credenciais["usuario_id"].astype(str) == str(usuario_id)
    ].tolist()
    if len(existentes) > 1:
        return ResultadoCredencial(False, "credencial_inconsistente", "Credencial não configurada.")
    if existentes:
        ci = existentes[0]
        configurada_em = base_credenciais.at[ci, "configurada_em"] or agora
        configurada_por = base_credenciais.at[ci, "configurada_por"] or autor
        base_credenciais.loc[ci] = [
            str(usuario_id), password_hash, ALGORITMO, configurada_em,
            configurada_por, agora, autor,
        ]
    else:
        base_credenciais = pd.concat([base_credenciais, pd.DataFrame([{
            "usuario_id": str(usuario_id), "password_hash": password_hash,
            "algoritmo": ALGORITMO, "configurada_em": agora,
            "configurada_por": autor, "atualizada_em": agora,
            "atualizada_por": autor,
        }])], ignore_index=True)
    identidades.at[indice, "credencial_configurada"] = "sim"
    identidades.at[indice, "atualizado_em"] = agora
    identidades.at[indice, "atualizado_por"] = autor

    # Revalida a autoridade imediatamente antes da publicação.
    if not pode_gerenciar_usuarios_operacionais():
        return ResultadoCredencial(False, "nao_autorizado", "Alteração não autorizada.")
    escrita = publicar_arquivos_em_commit(
        [
            AlteracaoArquivoConteudo(
                ARQUIVO_USUARIOS, identidades.to_csv(index=False).encode("utf-8")
            ),
            AlteracaoArquivoConteudo(
                ARQUIVO, base_credenciais.to_csv(index=False).encode("utf-8")
            ),
        ], token, repo, branch, "AUTH-002: configurar credencial operacional",
        snapshot_esperado=snapshot.commit_sha,
    )
    return ResultadoCredencial(
        escrita.sucesso,
        "salvo" if escrita.sucesso else "falha_persistencia",
        "Credencial configurada." if escrita.sucesso else "Credencial não configurada.",
        escrita,
    )
