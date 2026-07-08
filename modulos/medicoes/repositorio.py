import os
import uuid
from datetime import datetime
from io import StringIO
from pathlib import Path

import pandas as pd
import streamlit as st

from services.github import (
    carregar_github,
    salvar_github,
    salvar_arquivo_github,
)

from modulos.medicoes.config import (
    ARQ_OBRAS,
    ARQ_MEDICOES,
    ARQ_FRENTES,
    ARQ_MC,
    ARQ_ITENS,
    ARQ_SERVICOS,
    ARQ_TABELAS_SERVICOS_DIR,
    ARQ_LOCAIS_TRABALHO,
    ARQ_LANCAMENTOS_PRODUCAO,
    COL_OBRAS,
    COL_MEDICOES,
    COL_FRENTES,
    COL_MC,
    COL_ITENS,
    COL_SERVICOS,
    COL_TABELA_SERVICOS_CONTRATO,
    COL_LOCAIS_TRABALHO,
    COL_LANCAMENTOS_PRODUCAO,
    ARQ_USUARIOS_OBRAS,
    COL_USUARIOS_OBRAS,
)

# ============================================================
# CSV — BASE GITHUB
# ============================================================

def carregar_csv(caminho, colunas):
    try:
        df = carregar_github(
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )

        if isinstance(df, str):
            df = pd.read_csv(StringIO(df))

        if df is None:
            df = pd.DataFrame(columns=colunas)

    except Exception:
        df = pd.DataFrame(columns=colunas)

    for c in colunas:
        if c not in df.columns:
            df[c] = None

    return df[colunas]


def salvar_csv(caminho, df):
    try:
        salvar_github(
            df,
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )

        return True

    except Exception as e:
        st.error(f"Erro ao salvar {caminho}: {e}")
        return False


# ============================================================
# BASES PRINCIPAIS
# ============================================================

def carregar_bases():
    obras = carregar_csv(
        ARQ_OBRAS,
        COL_OBRAS,
    )

    medicoes = carregar_csv(
        ARQ_MEDICOES,
        COL_MEDICOES,
    )

    frentes = carregar_csv(
        ARQ_FRENTES,
        COL_FRENTES,
    )

    mc = carregar_csv(
        ARQ_MC,
        COL_MC,
    )

    itens = carregar_csv(
        ARQ_ITENS,
        COL_ITENS,
    )

    servicos = carregar_csv(
        ARQ_SERVICOS,
        COL_SERVICOS,
    )

    return (
        obras,
        medicoes,
        frentes,
        mc,
        itens,
        servicos,
    )

# ============================================================
# USUÁRIOS x OBRAS — PERMISSÕES MEDIÇÕES
# ============================================================

def carregar_usuarios_obras():

    return carregar_csv(
        ARQ_USUARIOS_OBRAS,
        COL_USUARIOS_OBRAS,
    )


# ============================================================
# TABELA CONTRATUAL DA OBRA
# ============================================================

def carregar_tabela_contrato(nome_arquivo):

    if not nome_arquivo:
        return pd.DataFrame(
            columns=COL_TABELA_SERVICOS_CONTRATO
        )

    caminho = (
        f"{ARQ_TABELAS_SERVICOS_DIR}/{nome_arquivo}"
    )

    try:

        df = carregar_github(
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )

        if isinstance(df, str):
            df = pd.read_csv(StringIO(df))

        if df is None:
            df = pd.DataFrame(
                columns=COL_TABELA_SERVICOS_CONTRATO
            )

    except Exception:

        try:

            if not os.path.exists(caminho):
                return pd.DataFrame(
                    columns=COL_TABELA_SERVICOS_CONTRATO
                )

            df = pd.read_csv(caminho)

        except Exception as e:

            st.error(
                f"Erro ao carregar tabela contratual: {e}"
            )

            return pd.DataFrame(
                columns=COL_TABELA_SERVICOS_CONTRATO
            )

    for c in COL_TABELA_SERVICOS_CONTRATO:
        if c not in df.columns:
            df[c] = None

    return df[COL_TABELA_SERVICOS_CONTRATO]


# ============================================================
# LOCAIS DE TRABALHO
# ============================================================

def carregar_locais_trabalho():

    return carregar_csv(
        ARQ_LOCAIS_TRABALHO,
        COL_LOCAIS_TRABALHO,
    )


def salvar_locais_trabalho(df):

    return salvar_csv(
        ARQ_LOCAIS_TRABALHO,
        df[COL_LOCAIS_TRABALHO],
    )


# ============================================================
# LANÇAMENTOS DE PRODUÇÃO
# ============================================================

def carregar_lancamentos_producao():

    return carregar_csv(
        ARQ_LANCAMENTOS_PRODUCAO,
        COL_LANCAMENTOS_PRODUCAO,
    )


# ============================================================
# FOTO LANÇAMENTO
# ============================================================

def salvar_foto_lancamento(id_lancamento, foto):

    if foto is None:
        return ""

    extensao = Path(foto.name).suffix.lower()

    nome_arquivo = (
        f"{id_lancamento}{extensao}"
    )

    caminho = (
        f"data/medicoes/fotos_lancamentos/{nome_arquivo}"
    )

    try:

        salvar_arquivo_github(
            foto.getvalue(),
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
            mensagem=(
                f"Upload foto lançamento "
                f"{id_lancamento}"
            ),
        )

        return caminho

    except Exception as e:

        st.warning(
            f"Não foi possível salvar a foto: {e}"
        )

        return ""


# ============================================================
# LEGADO — SALVAR LANÇAMENTO DE PRODUÇÃO
# ============================================================
# ATENÇÃO:
# Esta função pertence ao fluxo antigo de lançamentos e monta campos que
# não correspondem integralmente ao schema atual de COL_LANCAMENTOS_PRODUCAO.
#
# O fluxo oficial atual deve usar:
# modulos.medicoes.lancamentos.servicos.criar_lancamento_trabalho
#
# Mantida temporariamente para evitar quebra de imports ou chamadas antigas.
# Não usar em novas telas ou novas regras de negócio.
# ============================================================

def salvar_lancamento_producao(
    dados,
    foto=None,
):

    id_lancamento = (
        f"LP-"
        f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-"
        f"{uuid.uuid4().hex[:6]}"
    )

    foto_arquivo = salvar_foto_lancamento(
        id_lancamento,
        foto,
    )

    novo_registro = {

        "id_lancamento":
            id_lancamento,

        "obra_id":
            dados.get("obra_id", ""),

        "nome_obra":
            dados.get("nome_obra", ""),

        "local_id":
            dados.get("local_id", ""),

        "nome_local":
            dados.get("nome_local", ""),

        "codigo_item":
            dados.get("codigo_item", ""),

        "descricao_item":
            dados.get("descricao_item", ""),

        "unidade":
            dados.get("unidade", ""),

        "quantidade":
            dados.get("quantidade", ""),

        "data_servico":
            dados.get("data_servico", ""),

        "observacao":
            dados.get("observacao", ""),

        "foto_arquivo":
            foto_arquivo,

        "usuario":
            dados.get("usuario", ""),

        "data_hora_lancamento":
            dados.get(
                "data_hora_lancamento",
                "",
            ),

        "status":
            dados.get(
                "status",
                "PENDENTE_ANALISE",
            ),
    }

    df = carregar_lancamentos_producao()

    df = pd.concat(
        [
            df,
            pd.DataFrame([novo_registro]),
        ],
        ignore_index=True,
    )

    return salvar_csv(
        ARQ_LANCAMENTOS_PRODUCAO,
        df[COL_LANCAMENTOS_PRODUCAO],
    )
