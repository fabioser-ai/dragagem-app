import pandas as pd
import streamlit as st

from pages.crm.config import (
    COLUNAS_CLIENTES,
    COLUNAS_CONTATOS,
    COLUNAS_INTERACOES,
)
from pages.crm.utils import gerar_id, agora_iso, dataframe_vazio
from services.github import carregar_github, salvar_github


ARQ_CLIENTES = "data/crm/clientes.csv"
ARQ_CONTATOS = "data/crm/contatos.csv"
ARQ_INTERACOES = "data/crm/interacoes.csv"


def get_github_config():
    token = st.secrets["GITHUB_TOKEN"]
    repo = st.secrets["REPO"]
    return token, repo


def carregar_csv_github(caminho: str, colunas: list[str]) -> pd.DataFrame:
    token, repo = get_github_config()

    try:
        df = carregar_github(caminho, token, repo)
    except Exception as e:
        st.error(f"Erro ao carregar arquivo do GitHub: {caminho}")
        st.exception(e)
        return dataframe_vazio(colunas)

    if df is None or df.empty:
        df = dataframe_vazio(colunas)

    for coluna in colunas:
        if coluna not in df.columns:
            df[coluna] = ""

    df = df[colunas]
    return df.fillna("").astype(str)


def salvar_csv_github(df: pd.DataFrame, caminho: str, colunas: list[str]):
    token, repo = get_github_config()

    for coluna in colunas:
        if coluna not in df.columns:
            df[coluna] = ""

    df = df[colunas].fillna("").astype(str)

    try:
        salvar_github(
            df,
            caminho,
            token,
            repo,
            mensagem_commit=f"Atualiza CRM: {caminho}",
        )
    except TypeError:
        salvar_github(
            df,
            caminho,
            token,
            repo,
        )
    except Exception as e:
        st.error(f"Erro ao salvar arquivo no GitHub: {caminho}")
        st.exception(e)
        raise e


def carregar_clientes() -> pd.DataFrame:
    return carregar_csv_github(ARQ_CLIENTES, COLUNAS_CLIENTES)


def salvar_clientes(df: pd.DataFrame):
    salvar_csv_github(df, ARQ_CLIENTES, COLUNAS_CLIENTES)


def carregar_contatos() -> pd.DataFrame:
    return carregar_csv_github(ARQ_CONTATOS, COLUNAS_CONTATOS)


def salvar_contatos(df: pd.DataFrame):
    salvar_csv_github(df, ARQ_CONTATOS, COLUNAS_CONTATOS)


def carregar_interacoes() -> pd.DataFrame:
    return carregar_csv_github(ARQ_INTERACOES, COLUNAS_INTERACOES)


def salvar_interacoes(df: pd.DataFrame):
    salvar_csv_github(df, ARQ_INTERACOES, COLUNAS_INTERACOES)


def cadastrar_cliente(dados: dict):
    df = carregar_clientes()

    novo = {
        "id_cliente": gerar_id(),
        "created_at": agora_iso(),
        "updated_at": agora_iso(),
    }

    novo.update(dados)

    df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
    salvar_clientes(df)


def atualizar_cliente(id_cliente: str, dados: dict):
    df = carregar_clientes()

    if df.empty:
        return

    idx = df.index[df["id_cliente"] == id_cliente]

    if len(idx) == 0:
        return

    idx = idx[0]

    for chave, valor in dados.items():
        if chave in df.columns:
            df.loc[idx, chave] = valor

    df.loc[idx, "updated_at"] = agora_iso()

    salvar_clientes(df)


def cadastrar_contato(dados: dict):
    df = carregar_contatos()

    novo = {
        "id_contato": gerar_id(),
        "created_at": agora_iso(),
        "updated_at": agora_iso(),
    }

    novo.update(dados)

    df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
    salvar_contatos(df)


def atualizar_contato(id_contato: str, dados: dict):
    df = carregar_contatos()

    if df.empty:
        return

    idx = df.index[df["id_contato"] == id_contato]

    if len(idx) == 0:
        return

    idx = idx[0]

    for chave, valor in dados.items():
        if chave in df.columns:
            df.loc[idx, chave] = valor

    df.loc[idx, "updated_at"] = agora_iso()

    salvar_contatos(df)


def cadastrar_interacao(dados: dict):
    df = carregar_interacoes()

    novo = {
        "id_interacao": gerar_id(),
        "created_at": agora_iso(),
    }

    novo.update(dados)

    df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
    salvar_interacoes(df)

    atualizar_cliente_apos_interacao(dados)


def atualizar_cliente_apos_interacao(dados_interacao: dict):
    id_cliente = dados_interacao.get("id_cliente", "")

    if not id_cliente:
        return

    clientes = carregar_clientes()

    idx = clientes.index[clientes["id_cliente"] == id_cliente]

    if len(idx) == 0:
        return

    idx = idx[0]

    clientes.loc[idx, "ultimo_contato"] = dados_interacao.get("data_interacao", "")
    clientes.loc[idx, "proxima_acao"] = dados_interacao.get("proxima_acao", "")
    clientes.loc[idx, "data_proxima_acao"] = dados_interacao.get("data_proxima_acao", "")

    if dados_interacao.get("responsavel"):
        clientes.loc[idx, "responsavel"] = dados_interacao.get("responsavel")

    clientes.loc[idx, "updated_at"] = agora_iso()

    salvar_clientes(clientes)
