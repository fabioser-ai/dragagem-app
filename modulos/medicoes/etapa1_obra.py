import pandas as pd
import streamlit as st

from modulos.medicoes.config import ARQ_OBRAS, MODELOS_MEDICAO
from modulos.medicoes.repositorio import salvar_csv
from modulos.medicoes.utils import agora, novo_id


def normalizar_modelo(modelo):
    if pd.isna(modelo) or not str(modelo).strip():
        return "padrao_fos"

    return str(modelo).strip()


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

        obra_sel = obras_validas[
            obras_validas["obra_id"].astype(str)
            == str(st.session_state.obra_id)
        ]

        if not obra_sel.empty:
            modelo = normalizar_modelo(
                obra_sel.iloc[0].get("modelo_medicao", "padrao_fos")
            )

            arquivo_tabela_servicos = obra_sel.iloc[0].get(
                "arquivo_tabela_servicos",
                "",
            )

            if pd.isna(arquivo_tabela_servicos):
                arquivo_tabela_servicos = ""

            arquivo_tabela_servicos = str(
                arquivo_tabela_servicos
            ).strip()

            st.session_state.modelo_medicao = modelo
            st.session_state.arquivo_tabela_servicos = (
                arquivo_tabela_servicos
            )

            nome_modelo = MODELOS_MEDICAO.get(
                modelo,
                "Modelo não identificado",
            )

            st.info(f"Modelo de medição desta obra: {nome_modelo}")

            if arquivo_tabela_servicos:
                st.caption(
                    f"Tabela contratual vinculada: {arquivo_tabela_servicos}"
                )
            else:
                st.warning(
                    "Esta obra ainda não possui tabela contratual "
                    "de serviços vinculada."
                )

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

            modelo_label = st.selectbox(
                "Modelo de medição",
                list(MODELOS_MEDICAO.values()),
            )

            modelo_medicao = {
                v: k for k, v in MODELOS_MEDICAO.items()
            }[modelo_label]

            arquivo_tabela_servicos = st.text_input(
                "Arquivo da tabela contratual de serviços",
                value="",
                placeholder=(
                    "Ex: contrato_2026_curitiba_servicos_bombas.csv"
                ),
                help=(
                    "Arquivo CSV específico do contrato/obra. "
                    "Exemplo: data/medicoes_tabelas/"
                    "contrato_2026_curitiba_servicos_bombas.csv"
                ),
            )

            observacoes = st.text_area("Observações")

            ok = st.form_submit_button("Salvar obra")

        if ok:
            if not nome.strip():
                st.error("Informe o nome da obra.")
                return

            arquivo_tabela_servicos = str(
                arquivo_tabela_servicos
            ).strip()

            nova = {
                "obra_id": novo_id("obra"),
                "nome_obra": nome,
                "contratante": contratante,
                "contrato": contrato,
                "objeto": objeto,
                "cidade": cidade,
                "status": status,
                "modelo_medicao": modelo_medicao,
                "arquivo_tabela_servicos": arquivo_tabela_servicos,
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
                st.session_state.modelo_medicao = modelo_medicao
                st.session_state.arquivo_tabela_servicos = (
                    arquivo_tabela_servicos
                )
                st.success("Obra cadastrada.")
                st.rerun()

    if not obras_validas.empty:
        df_visual = obras_validas.copy()

        df_visual["modelo_medicao_nome"] = df_visual[
            "modelo_medicao"
        ].map(MODELOS_MEDICAO)

        if "arquivo_tabela_servicos" not in df_visual.columns:
            df_visual["arquivo_tabela_servicos"] = ""

        st.dataframe(
            df_visual[
                [
                    "nome_obra",
                    "contratante",
                    "contrato",
                    "cidade",
                    "status",
                    "modelo_medicao_nome",
                    "arquivo_tabela_servicos",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )
