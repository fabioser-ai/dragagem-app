import pandas as pd
import streamlit as st
from datetime import datetime
from uuid import uuid4

from services.github import StatusLeitura
from services.dados_persistencia import (
    carregar_cadastro_resultado,
    salvar_cadastro_seguro,
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


def detalhes_resultado(resultado, mensagem_padrao):
    detalhes = resultado.erro or mensagem_padrao

    if resultado.http_status:
        detalhes = f"{detalhes} (HTTP {resultado.http_status})"

    return detalhes


def carregar_locais_resultado():
    return carregar_cadastro_resultado(
        ARQUIVO,
        COLUNAS,
        TOKEN,
        REPO,
    )


def salvar_locais_seguro(df, resultado_leitura):
    return salvar_cadastro_seguro(
        df,
        ARQUIVO,
        COLUNAS,
        TOKEN,
        REPO,
        resultado_leitura=resultado_leitura,
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

    resultado_leitura = carregar_locais_resultado()
    locais = resultado_leitura.dados
    escrita_liberada = (
        resultado_leitura.pode_sobrescrever
        or resultado_leitura.status == StatusLeitura.ARQUIVO_INEXISTENTE
    )

    if not escrita_liberada:
        st.error(
            "As alterações estão bloqueadas para preservar os dados. "
            + detalhes_resultado(
                resultado_leitura,
                "Não foi possível confirmar a leitura dos locais de trabalho.",
            )
        )

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
        disabled=not escrita_liberada,
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

        resultado_escrita = salvar_locais_seguro(
            locais,
            resultado_leitura,
        )

        if resultado_escrita.sucesso:
            st.success(
                "Local cadastrado com sucesso."
            )
            st.rerun()

        st.error(
            detalhes_resultado(
                resultado_escrita,
                "Não foi possível cadastrar o local.",
            )
        )
