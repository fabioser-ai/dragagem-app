import pandas as pd
import streamlit as st

from modulos.medicoes.config import ARQ_OBRAS
from modulos.medicoes.repositorio import salvar_csv
from modulos.medicoes.utils import agora, novo_id


def tela_obras(obras):
    st.subheader("1. Obra")

    obras_validas = obras.dropna(subset=["obra_id"])

    if not obras_validas.empty:
        mapa = {
            f"{r['nome_obra']} | {r['contrato']}": r["obra_id"]
            for _, r in obras_validas.iterrows()
        }

        obra_label = st.selectbox(
            "Selecionar obra",
            list(mapa.keys()),
            key="select_obra_medicoes",
        )

        st.session_state.obra_id = mapa[obra_label]

    with st.expander(
        "Cadastrar nova obra",
        expanded=obras_validas.empty,
    ):
        with st.form("nova_obra"):
            nome = st.text_input("Nome da obra")
            contratante = st.text_input("Contratante")
            contrato = st.text_input("Contrato")
            objeto = st.text_area("Objeto")
            cidade = st.text_input("Cidade")

            status = st.selectbox(
                "Status",
                ["Ativa", "Concluída", "Suspensa"],
            )

            observacoes = st.text_area("Observações")

            ok = st.form_submit_button("Salvar obra")

        if ok:
            if not nome.strip():
                st.error("Informe o nome da obra.")
                return

            nova = {
                "obra_id": novo_id("obra"),
                "nome_obra": nome,
                "contratante": contratante,
                "contrato": contrato,
                "objeto": objeto,
                "cidade": cidade,
                "status": status,
                "observacoes": observacoes,
                "criado_em": agora(),
                "atualizado_em": agora(),
            }

            obras = pd.concat(
                [obras, pd.DataFrame([nova])],
                ignore_index=True,
            )

            if salvar_csv(ARQ_OBRAS, obras):
                st.session_state.obra_id = nova["obra_id"]
                st.success("Obra cadastrada.")
                st.rerun()

    if not obras_validas.empty:
        st.dataframe(
            obras_validas[
                [
                    "nome_obra",
                    "contratante",
                    "contrato",
                    "cidade",
                    "status",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )
