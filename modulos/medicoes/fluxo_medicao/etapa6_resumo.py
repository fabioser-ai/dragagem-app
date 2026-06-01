import pandas as pd
import streamlit as st

from modulos.medicoes.lancamentos.repositorio import (
    carregar_lancamentos_trabalho,
)
from modulos.medicoes.utils import moeda


def _carregar_lancamentos_selecionados():
    df_session = st.session_state.get("df_lancamentos_selecionados")

    if df_session is not None and not df_session.empty:
        return df_session.copy()

    ids = st.session_state.get("lancamentos_selecionados", [])

    if not ids:
        return pd.DataFrame()

    df = carregar_lancamentos_trabalho()

    if df.empty:
        return pd.DataFrame()

    df = df.fillna("").copy()

    return df[
        df["lancamento_id"].astype(str).isin([str(x) for x in ids])
    ].copy()


def tela_resumo(frentes, itens, medicoes):
    st.subheader("Resumo da Medição")

    medicao_id = st.session_state.get("medicao_id")

    if not medicao_id:
        st.warning("Selecione um BM.")
        return

    lancamentos = _carregar_lancamentos_selecionados()

    if lancamentos.empty:
        st.info("Nenhum lançamento selecionado para esta medição.")
        return

    lancamentos["quantidade_executada"] = pd.to_numeric(
        lancamentos["quantidade_executada"],
        errors="coerce",
    ).fillna(0.0)

    st.markdown("### Lançamentos selecionados")

    colunas_visual = [
        "data_servico",
        "nome_local",
        "codigo_item",
        "descricao_item",
        "unidade",
        "quantidade_executada",
    ]

    colunas_existentes = [
        c for c in colunas_visual if c in lancamentos.columns
    ]

    st.dataframe(
        lancamentos[colunas_existentes],
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("### Resumo por item")

    resumo = (
        lancamentos
        .groupby(
            ["codigo_item", "descricao_item", "unidade"],
            dropna=False,
        )["quantidade_executada"]
        .sum()
        .reset_index()
    )

    st.dataframe(
        resumo,
        use_container_width=True,
        hide_index=True,
    )

    total_lancamentos = len(lancamentos)
    total_quantidade = resumo["quantidade_executada"].sum()

    c1, c2 = st.columns(2)

    c1.metric("Lançamentos selecionados", total_lancamentos)
    c2.metric("Quantidade total", f"{total_quantidade:,.2f}")

    st.info(
        "Nesta versão, o resumo está consolidando quantidades dos lançamentos. "
        "O cálculo financeiro por preço unitário será conectado depois à tabela contratual da obra."
    )
