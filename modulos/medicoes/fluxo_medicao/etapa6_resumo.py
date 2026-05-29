import pandas as pd
import streamlit as st

from modulos.medicoes.utils import moeda


def tela_resumo(frentes, itens, medicoes):
    st.subheader("6. Conferência / Resumo Financeiro")

    medicao_id = st.session_state.get("medicao_id")

    if not medicao_id:
        st.warning("Selecione um BM.")
        return

    itens_bm = itens[
        itens["medicao_id"].astype(str) == str(medicao_id)
    ].copy()

    if itens_bm.empty:
        st.info("Nenhum item medido.")
        return

    itens_bm["total"] = pd.to_numeric(
        itens_bm["total"],
        errors="coerce",
    ).fillna(0.0)

    mapa_frentes = {
        r["frente_id"]: r["nome_frente"]
        for _, r in frentes.iterrows()
    }

    itens_bm["frente"] = itens_bm["frente_id"].map(mapa_frentes)

    resumo = (
        itens_bm
        .groupby("frente", dropna=False)["total"]
        .sum()
        .reset_index()
    )

    subtotal = resumo["total"].sum()

    med_row = medicoes[
        medicoes["medicao_id"].astype(str) == str(medicao_id)
    ]

    apost = 0.0

    if not med_row.empty:
        try:
            apost = float(
                med_row.iloc[0]["apostilamento_percentual"]
            )
        except Exception:
            apost = 0.0

    valor_apost = subtotal * (apost / 100)
    total_final = subtotal + valor_apost

    resumo["valor"] = resumo["total"].apply(moeda)

    st.dataframe(
        resumo[["frente", "valor"]],
        use_container_width=True,
        hide_index=True,
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Subtotal", moeda(subtotal))
    c2.metric("Apostilamento", moeda(valor_apost))
    c3.metric("Total Final", moeda(total_final))
