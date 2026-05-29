import pandas as pd
import streamlit as st

from modulos.medicoes.config import ARQ_FRENTES
from modulos.medicoes.repositorio import salvar_csv
from modulos.medicoes.utils import agora, novo_id


def tela_frentes(frentes):
    st.subheader("3. Frentes / Locais de Medição")

    medicao_id = st.session_state.get("medicao_id")

    if not medicao_id:
        st.warning("Selecione ou cadastre um BM antes de criar frentes.")
        return

    df = frentes[
        frentes["medicao_id"].astype(str) == str(medicao_id)
    ]

    if not df.empty:
        mapa = {
            f"{r['nome_frente']} | {r['dias_trabalhados']} dias": r["frente_id"]
            for _, r in df.iterrows()
        }

        frente_label = st.selectbox(
            "Selecionar frente",
            list(mapa.keys()),
            key="select_frente_medicoes",
        )

        st.session_state.frente_id = mapa[frente_label]

    with st.expander(
        "Cadastrar nova frente",
        expanded=df.empty,
    ):
        with st.form("nova_frente"):
            nome = st.text_input("Nome da frente / local")

            dias = st.number_input(
                "Dias trabalhados",
                min_value=0.0,
                value=0.0,
                step=0.5,
            )

            observacoes = st.text_area("Observações")

            ok = st.form_submit_button("Salvar frente")

        if ok:
            if not nome.strip():
                st.error("Informe o nome da frente.")
                return

            nova = {
                "frente_id": novo_id("frente"),
                "medicao_id": medicao_id,
                "nome_frente": nome,
                "dias_trabalhados": dias,
                "observacoes": observacoes,
                "criado_em": agora(),
                "atualizado_em": agora(),
            }

            frentes = pd.concat(
                [frentes, pd.DataFrame([nova])],
                ignore_index=True,
            )

            if salvar_csv(ARQ_FRENTES, frentes):
                st.session_state.frente_id = nova["frente_id"]
                st.success("Frente cadastrada.")
                st.rerun()

    if not df.empty:
        st.dataframe(
            df[
                [
                    "nome_frente",
                    "dias_trabalhados",
                    "observacoes",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )
