import pandas as pd
import streamlit as st

from modulos.medicoes.config import ARQ_ITENS, COL_ITENS
from modulos.medicoes.repositorio import salvar_csv
from modulos.medicoes.utils import moeda, novo_id


def tela_medicao(frentes, mc, itens, servicos):
    st.subheader("5. Lançamento de Itens")

    frente_id = st.session_state.get("frente_id")

    if not frente_id:
        st.warning("Selecione uma frente.")
        return

    df_mc = mc[
        mc["frente_id"].astype(str) == str(frente_id)
    ].copy()

    if df_mc.empty:
        st.info("Cadastre primeiro a memória de cálculo.")
        return

    frente_nome = frentes.loc[
        frentes["frente_id"].astype(str) == str(frente_id),
        "nome_frente",
    ]

    if not frente_nome.empty:
        st.info(f"Frente selecionada: {frente_nome.iloc[0]}")

    df_mc["resultado"] = pd.to_numeric(
        df_mc["resultado"],
        errors="coerce",
    ).fillna(0.0)

    quantidade_total = df_mc["resultado"].sum()

    df_existente = itens[
        itens["frente_id"].astype(str) == str(frente_id)
    ].copy()

    if df_existente.empty:
        df_editor = servicos.copy()

        df_editor["item_id"] = [
            novo_id("item")
            for _ in range(len(df_editor))
        ]

        df_editor["medicao_id"] = st.session_state.get("medicao_id")
        df_editor["frente_id"] = frente_id
        df_editor["origem_mc"] = "MC"
        df_editor["quantidade"] = quantidade_total
        df_editor["valor_unitario"] = 0.0
        df_editor["total"] = 0.0

    else:
        df_editor = df_existente.copy()

    if df_editor.empty:
        st.warning(
            "Nenhum serviço cadastrado em data/medicoes_servicos.csv."
        )
        return

    for col in ["quantidade", "valor_unitario", "total"]:
        df_editor[col] = pd.to_numeric(
            df_editor[col],
            errors="coerce",
        ).fillna(0.0)

    df_editado = st.data_editor(
        df_editor,
        use_container_width=True,
        num_rows="dynamic",
        hide_index=True,
        key=f"medicao_{frente_id}",
        column_config={
            "item_id": None,
            "medicao_id": None,
            "frente_id": None,
            "codigo": st.column_config.TextColumn("Código"),
            "descricao": st.column_config.TextColumn("Serviço"),
            "unidade": st.column_config.TextColumn("Un"),
            "origem_mc": st.column_config.TextColumn("Origem"),
            "quantidade": st.column_config.NumberColumn(
                "Quantidade",
                format="%.2f",
                disabled=True,
            ),
            "valor_unitario": st.column_config.NumberColumn(
                "V.Unit",
                format="%.2f",
            ),
            "total": st.column_config.NumberColumn(
                "Total",
                format="%.2f",
                disabled=True,
            ),
        },
    )

    df_editado["valor_unitario"] = pd.to_numeric(
        df_editado["valor_unitario"],
        errors="coerce",
    ).fillna(0.0)

    df_editado["quantidade"] = pd.to_numeric(
        df_editado["quantidade"],
        errors="coerce",
    ).fillna(0.0)

    df_editado["total"] = (
        df_editado["quantidade"]
        * df_editado["valor_unitario"]
    )

    total_frente = df_editado["total"].sum()

    st.metric("Total da frente", moeda(total_frente))

    if st.button(
        "Salvar itens da medição",
        use_container_width=True,
    ):
        itens = itens[
            itens["frente_id"].astype(str) != str(frente_id)
        ]

        mc_ids = [
            novo_id("item")
            for _ in range(len(df_editado))
        ]

        df_editado["item_id"] = df_editado["item_id"].fillna(
            pd.Series(mc_ids)
        )

        itens = pd.concat(
            [itens, df_editado[COL_ITENS]],
            ignore_index=True,
        )

        if salvar_csv(ARQ_ITENS, itens):
            st.success("Itens da medição salvos.")
            st.rerun()
