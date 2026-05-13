import streamlit as st

from modulos.medicoes.config import (
    ETAPAS_MODELO,
)
from modulos.medicoes.utils import ir_para


LABELS_ETAPAS = {
    "obra": "1. Obra",
    "bm": "2. BM",
    "frentes": "3. Frentes",
    "mc": "4. MC",
    "medicao": "5. Medição",
    "resumo": "6. Resumo",
}


def obter_etapas():
    modelo = st.session_state.get(
        "modelo_medicao",
        "padrao_fos",
    )

    return ETAPAS_MODELO.get(
        modelo,
        ETAPAS_MODELO["padrao_fos"],
    )


def navegacao():
    etapa = st.session_state.get(
        "etapa_medicoes",
        "obra",
    )

    ordem = obter_etapas()

    if etapa not in ordem:
        etapa = ordem[0]
        st.session_state.etapa_medicoes = etapa

    st.markdown("### Fluxo da medição")

    cols = st.columns(len(ordem))

    for i, etapa_nome in enumerate(ordem):
        with cols[i]:

            ativo = etapa_nome == etapa

            st.button(
                f"{'✅ ' if ativo else ''}{LABELS_ETAPAS[etapa_nome]}",
                disabled=ativo,
                use_container_width=True,
                key=f"barra_medicoes_{etapa_nome}",
            )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        idx = ordem.index(etapa)

        if idx > 0:
            if st.button(
                "← Voltar",
                use_container_width=True,
            ):
                ir_para(ordem[idx - 1])

    with c2:
        if st.button(
            "⬅ Menu",
            use_container_width=True,
        ):
            st.session_state.tela = "menu"
            st.rerun()

    with c3:
        idx = ordem.index(etapa)

        if idx < len(ordem) - 1:
            if st.button(
                "Próximo →",
                use_container_width=True,
            ):
                ir_para(ordem[idx + 1])
