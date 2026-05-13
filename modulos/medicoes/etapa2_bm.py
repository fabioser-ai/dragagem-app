from datetime import date

import pandas as pd
import streamlit as st

from modulos.medicoes.config import (
    ARQ_MEDICOES,
    CONFIG_MODELOS_MEDICAO,
    MODELOS_MEDICAO,
)
from modulos.medicoes.repositorio import salvar_csv
from modulos.medicoes.utils import agora, novo_id


def obter_config_modelo():
    modelo = st.session_state.get("modelo_medicao", "padrao_fos")

    return CONFIG_MODELOS_MEDICAO.get(
        modelo,
        CONFIG_MODELOS_MEDICAO["padrao_fos"],
    )


def tela_bm(obras, medicoes):
    st.subheader("2. BM / Período de Medição")

    obra_id = st.session_state.get("obra_id")

    if not obra_id:
        st.warning("Selecione ou cadastre uma obra antes de criar o BM.")
        return

    modelo = st.session_state.get("modelo_medicao", "padrao_fos")
    config_modelo = obter_config_modelo()

    obra_nome = obras.loc[
        obras["obra_id"].astype(str) == str(obra_id),
        "nome_obra",
    ]

    if not obra_nome.empty:
        st.info(f"Obra selecionada: {obra_nome.iloc[0]}")

    nome_modelo = MODELOS_MEDICAO.get(
        modelo,
        "Padrão FOS",
    )

    st.caption(f"Modelo de medição: {nome_modelo}")

    df_obra = medicoes[
        medicoes["obra_id"].astype(str) == str(obra_id)
    ]

    if not df_obra.empty:
        mapa = {
            f"BM {r['numero_bm']} | {r['periodo_inicio']}": r["medicao_id"]
            for _, r in df_obra.iterrows()
        }

        bm_label = st.selectbox(
            "Selecionar BM existente",
            list(mapa.keys()),
            key="select_bm_medicoes",
        )

        st.session_state.medicao_id = mapa[bm_label]

    with st.expander(
        "Cadastrar novo BM",
        expanded=df_obra.empty,
    ):
        with st.form("novo_bm"):
            c1, c2, c3 = st.columns(3)

            with c1:
                numero_bm = st.text_input("Número BM", value="01")

                if config_modelo["usa_aditivo"]:
                    aditivo = st.text_input("Aditivo", value="00")
                else:
                    aditivo = ""

            with c2:
                periodo_inicio = st.date_input(
                    "Período de medição",
                    value=date.today(),
                )

                if config_modelo["usa_periodo_fim"]:
                    periodo_fim = st.date_input(
                        "Período fim",
                        value=date.today(),
                    )
                else:
                    periodo_fim = periodo_inicio

            with c3:
                data_bm = st.date_input(
                    "Data BM",
                    value=date.today(),
                )

                dias_uteis = st.number_input(
                    "Dias úteis",
                    min_value=1,
                    value=20,
                )

            if config_modelo["usa_apostilamento"]:
                apost = st.number_input(
                    "Apostilamento (%)",
                    value=0.00,
                    step=0.01,
                )
            else:
                apost = 0.0

            status = st.selectbox(
                "Status",
                [
                    "Rascunho",
                    "Fechado",
                    "Enviado",
                    "Aprovado",
                    "Pago",
                ],
            )

            observacoes = st.text_area("Observações")

            ok = st.form_submit_button("Salvar BM")

        if ok:
            if periodo_fim < periodo_inicio:
                st.error("A data final não pode ser anterior à data inicial.")
                return

            nova = {
                "medicao_id": novo_id("bm"),
                "obra_id": obra_id,
                "numero_bm": numero_bm,
                "aditivo": aditivo,
                "periodo_inicio": str(periodo_inicio),
                "periodo_fim": str(periodo_fim),
                "data_bm": str(data_bm),
                "dias_uteis_mes": dias_uteis,
                "apostilamento_percentual": apost,
                "status": status,
                "observacoes": observacoes,
                "criado_em": agora(),
                "atualizado_em": agora(),
            }

            medicoes = pd.concat(
                [medicoes, pd.DataFrame([nova])],
                ignore_index=True,
            )

            if salvar_csv(ARQ_MEDICOES, medicoes):
                st.session_state.medicao_id = nova["medicao_id"]
                st.success("BM cadastrado.")
                st.rerun()

    if not df_obra.empty:
        colunas_visual = [
            "numero_bm",
            "periodo_inicio",
            "data_bm",
            "dias_uteis_mes",
            "status",
        ]

        if config_modelo["usa_aditivo"]:
            colunas_visual.insert(1, "aditivo")

        if config_modelo["usa_periodo_fim"]:
            colunas_visual.insert(3, "periodo_fim")

        st.dataframe(
            df_obra[colunas_visual],
            use_container_width=True,
            hide_index=True,
        )
