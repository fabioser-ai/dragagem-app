import streamlit as st

from modulos.medicoes.lancamentos.repositorio import (
    carregar_lancamentos_trabalho,
)


def tela_lancamentos():
    st.subheader("Selecionar Lançamentos Aprovados")

    obra_id = st.session_state.get("obra_id")

    if not obra_id:
        st.warning("Selecione uma obra primeiro.")
        return

    df = carregar_lancamentos_trabalho()

    if df.empty:
        st.info("Nenhum lançamento encontrado.")
        return

    df = df.fillna("").copy()

    lancamentos = df[
        (df["obra_id"].astype(str) == str(obra_id))
        &
        (
            df["status_aprovacao"]
            .astype(str)
            .str.lower()
            == "aprovado"
        )
        &
        (
            df["status_medicao"]
            .astype(str)
            .str.lower()
            == "nao_medido"
        )
    ].copy()

    if lancamentos.empty:
        st.info(
            "Não existem lançamentos aprovados "
            "aguardando medição para esta obra."
        )
        return

    selecionados = []

    st.caption(
        f"{len(lancamentos)} lançamento(s) elegível(is)."
    )

    for _, row in lancamentos.iterrows():

        descricao = (
            f"{row['data_servico']} | "
            f"{row['nome_local']} | "
            f"{row['codigo_item']} | "
            f"{row['quantidade_executada']} {row['unidade']}"
        )

        marcado = st.checkbox(
            descricao,
            key=f"sel_{row['lancamento_id']}",
        )

        if marcado:
            selecionados.append(
                row["lancamento_id"]
            )

    st.session_state[
        "lancamentos_selecionados"
    ] = selecionados

    st.info(
        f"{len(selecionados)} lançamento(s) selecionado(s)."
    )
