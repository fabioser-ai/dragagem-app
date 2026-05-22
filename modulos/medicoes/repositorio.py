import pandas as pd
import streamlit as st
import os

from services.github import carregar_github, salvar_github

from modulos.medicoes.config import (
    ARQ_OBRAS,
    ARQ_MEDICOES,
    ARQ_FRENTES,
    ARQ_MC,
    ARQ_ITENS,
    ARQ_SERVICOS,
    COL_OBRAS,
    COL_MEDICOES,
    COL_FRENTES,
    COL_MC,
    COL_ITENS,
    COL_SERVICOS,
)

from modulos.medicoes.config import (
    ARQ_TABELAS_SERVICOS_DIR,
    COL_TABELA_SERVICOS_CONTRATO,
)

# ============================================================
# CSV
# ============================================================

def carregar_csv(caminho, colunas):
    try:
        df = carregar_github(
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )

        if isinstance(df, str):
            from io import StringIO
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
# BASES
# ============================================================

def carregar_bases():
    obras = carregar_csv(ARQ_OBRAS, COL_OBRAS)

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
# Carregar tabela contrato
# ============================================================


def carregar_tabela_contrato(nome_arquivo):
    if not nome_arquivo:
        return pd.DataFrame(
            columns=COL_TABELA_SERVICOS_CONTRATO
        )

    caminho = (
        f"{ARQ_TABELAS_SERVICOS_DIR}/{nome_arquivo}"
    )

    if not os.path.exists(caminho):
        return pd.DataFrame(
            columns=COL_TABELA_SERVICOS_CONTRATO
        )

    try:
        df = pd.read_csv(caminho)

        for c in COL_TABELA_SERVICOS_CONTRATO:
            if c not in df.columns:
                df[c] = None

        return df[COL_TABELA_SERVICOS_CONTRATO]

    except Exception as e:
        st.error(
            f"Erro ao carregar tabela contratual: {e}"
        )

        return pd.DataFrame(
            columns=COL_TABELA_SERVICOS_CONTRATO
        )
from pathlib import Path
from datetime import datetime
import pandas as pd
import uuid


PASTA_DADOS_MEDICOES = Path("data/medicoes")
PASTA_FOTOS_LANCAMENTOS = PASTA_DADOS_MEDICOES / "fotos_lancamentos"
ARQUIVO_LANCAMENTOS_PRODUCAO = PASTA_DADOS_MEDICOES / "lancamentos_producao.csv"


COLUNAS_LANCAMENTOS_PRODUCAO = [
    "id_lancamento",
    "obra",
    "local_trabalho",
    "data_servico",
    "atividade_executada",
    "observacao",
    "foto_arquivo",
    "usuario",
    "data_hora_lancamento",
    "status",
]

def garantir_estrutura_lancamentos_producao():
    PASTA_DADOS_MEDICOES.mkdir(parents=True, exist_ok=True)
    PASTA_FOTOS_LANCAMENTOS.mkdir(parents=True, exist_ok=True)

    if not ARQUIVO_LANCAMENTOS_PRODUCAO.exists():
        df = pd.DataFrame(columns=COLUNAS_LANCAMENTOS_PRODUCAO)
        df.to_csv(ARQUIVO_LANCAMENTOS_PRODUCAO, index=False, encoding="utf-8-sig")


def salvar_foto_lancamento(id_lancamento, foto):
    if foto is None:
        return ""

    extensao = Path(foto.name).suffix.lower()
    nome_arquivo = f"{id_lancamento}{extensao}"
    caminho_foto = PASTA_FOTOS_LANCAMENTOS / nome_arquivo

    with open(caminho_foto, "wb") as f:
        f.write(foto.getbuffer())

    return str(caminho_foto)


def salvar_lancamento_producao(dados, foto=None):
    garantir_estrutura_lancamentos_producao()

    id_lancamento = f"LP-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"

    foto_arquivo = salvar_foto_lancamento(id_lancamento, foto)

    novo_registro = {
        "id_lancamento": id_lancamento,
        "obra": dados.get("obra", ""),
        "local_trabalho": dados.get("local_trabalho", ""),
        "data_servico": dados.get("data_servico", ""),
        "atividade_executada": dados.get("atividade_executada", ""),
        "observacao": dados.get("observacao", ""),
        "foto_arquivo": foto_arquivo,
        "usuario": dados.get("usuario", ""),
        "data_hora_lancamento": dados.get("data_hora_lancamento", ""),
        "status": dados.get("status", "PENDENTE_ANALISE"),
    }

    df = pd.read_csv(ARQUIVO_LANCAMENTOS_PRODUCAO, dtype=str, encoding="utf-8-sig")
    df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
    df.to_csv(ARQUIVO_LANCAMENTOS_PRODUCAO, index=False, encoding="utf-8-sig")

