import pandas as pd
import streamlit as st
from datetime import datetime
from uuid import uuid4

from services.github import (
    carregar_github,
    salvar_github,
)

from modulos.medicoes.repositorio import carregar_bases


TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

ARQUIVO = "data/medicoes/locais_trabalho.csv"


COLUNAS = [
    "local_id",
    "obra_id",
    "nome_local",
    "ativo",
    "observacoes",
    "criado_em",
    "atualizado_em",
]


def agora():
    return datetime.now().isoformat(timespec="seconds")


def gerar_local_id():
    return f"LOC_{uuid4().hex[:8]}"


def carregar_locais():

    df = carregar_github(
        ARQUIVO,
        TOKEN,
        REPO,
    )

    if df.empty:
        df = pd.DataFrame(columns=COLUNAS)

    for coluna in COLUNAS:
        if coluna not in df.columns:
            df[coluna] = ""

    return df[COLUNAS].fillna("")


def salvar_locais(df):

    salvar_github(
        df,
        ARQUIVO,
        TOKEN,
        REPO,
    )


def render_locais_trabalho():

    st.subheader("Locais de Trabalho")

    (
        obras,
        medicoes,
        frentes,
        mc,
        itens,
        servicos,
    ) = carregar_bases()

    if obras.empty:
        st.warning("Nenhuma obra cadastrada.")
        return

    obras = obras.fillna("").copy()

    obras["label"] = obras.apply(
        lambda row:
        f"{row['obra_id']} - "
        f"{row.get('nome_obra', row.get('nome', ''))}",
        axis=1,
    )

    obra_label = st.selectbox(
        "Obra",
        obras["label"].tolist(),
    )

    obra = obras[
        obras["label"] == obra_label
    ].iloc[0]

    obra_id = obra["obra_id"]

    locais = carregar_locais()

    locais_obra = locais[
        locais["obra_id"].astype(str)
        == str(obra_id)
    ].copy()

    st.divider()

    st.write("Locais cadastrados")

    if locais_obra.empty:

        st.info(
            "Nenhum local cadastrado para esta obra."
        )

    else:

        st.dataframe(
            locais_obra[
                [
                    "nome_local",
                    "ativo",
                    "observacoes",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )

    st.divider()

    st.write("Cadastrar novo local")

    nome_local = st.text_input(
        "Nome do Local"
    )

    observacoes = st.text_area(
        "Observações"
    )

    if st.button(
        "Adicionar Local",
        use_container_width=True,
    ):

        if not nome_local.strip():
            st.error(
                "Informe o nome do local."
            )
            return

        duplicado = locais[
            (locais["obra_id"].astype(str) == str(obra_id))
            &
            (
                locais["nome_local"]
                .astype(str)
                .str.lower()
                .str.strip()
                ==
                nome_local.lower().strip()
            )
        ]

        if not duplicado.empty:

            st.error(
                "Já existe um local com esse nome nesta obra."
            )

            return

        novo = {
            "local_id": gerar_local_id(),
            "obra_id": obra_id,
            "nome_local": nome_local.strip(),
            "ativo": "sim",
            "observacoes": observacoes,
            "criado_em": agora(),
            "atualizado_em": agora(),
        }

        locais = pd.concat(
            [
                locais,
                pd.DataFrame([novo]),
            ],
            ignore_index=True,
        )

        salvar_locais(locais)

        st.success(
            "Local cadastrado com sucesso."
        )

        st.rerun()
