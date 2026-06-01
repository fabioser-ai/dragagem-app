import pandas as pd
import streamlit as st

from services.permissoes import (
    eh_superadmin,
    carregar_permissoes,
    salvar_permissoes,
)


MODULOS_DISPONIVEIS = [
    "medicoes",
    "ferias",
    "prestacao_contas",
    "orcamento",
    "crm",
    "obras",
    "dados",
    "todos",
]

RECURSOS_POR_MODULO = {
    "medicoes": [
        "lancamentos",
        "aprovacao",
        "gestao",
        "todos",
    ],
    "ferias": [
        "todos",
    ],
    "prestacao_contas": [
        "todos",
    ],
    "orcamento": [
        "todos",
    ],
    "crm": [
        "todos",
    ],
    "obras": [
        "todos",
    ],
    "dados": [
        "todos",
    ],
    "todos": [
        "todos",
    ],
}

PERMISSOES_DISPONIVEIS = [
    "visualizar",
    "lancar",
    "criar",
    "editar",
    "aprovar",
    "excluir",
    "todos",
]


def render():
    st.title("Administração")
    st.caption("Gestão de permissões de usuários do sistema FOS.")

    if not eh_superadmin():
        st.error("Acesso restrito ao SuperAdmin.")
        st.stop()

    df = carregar_permissoes()

    st.subheader("Permissões cadastradas")

    if df.empty:
        st.info("Nenhuma permissão cadastrada ainda.")
    else:
        st.dataframe(df, use_container_width=True)

    st.divider()

    st.subheader("Adicionar nova permissão")

    with st.form("form_nova_permissao"):
        usuario = st.text_input("Usuário")

        modulo = st.selectbox(
            "Módulo",
            MODULOS_DISPONIVEIS,
        )

        recurso = st.selectbox(
            "Recurso",
            RECURSOS_POR_MODULO.get(modulo, ["todos"]),
        )

        permissao = st.selectbox(
            "Permissão",
            PERMISSOES_DISPONIVEIS,
        )

        obra_id = st.text_input(
            "Obra ID",
            value="todas",
            help="Use 'todas' para permissão sem restrição por obra.",
        )

        ativo = st.selectbox(
            "Ativo",
            ["sim", "nao"],
        )

        salvar = st.form_submit_button("Salvar permissão")

    if salvar:
        if not usuario.strip():
            st.error("Informe o usuário.")
            return

        nova_linha = {
            "usuario": usuario.strip(),
            "modulo": modulo,
            "recurso": recurso,
            "permissao": permissao,
            "obra_id": obra_id.strip() or "todas",
            "ativo": ativo,
        }

        df = pd.concat(
            [
                df,
                pd.DataFrame([nova_linha]),
            ],
            ignore_index=True,
        )

        try:
            salvar_permissoes(df)
            st.success("Permissão salva com sucesso.")
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao salvar permissão: {e}")

    st.divider()

    st.subheader("Remover / desativar permissões")

    if not df.empty:
        opcoes = [
            f"{i} | {row['usuario']} | {row['modulo']} | {row['recurso']} | {row['permissao']} | {row['obra_id']} | {row['ativo']}"
            for i, row in df.iterrows()
        ]

        escolha = st.selectbox(
            "Selecione uma permissão",
            opcoes,
        )

        indice = int(escolha.split("|")[0].strip())

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Desativar permissão", use_container_width=True):
                df.loc[indice, "ativo"] = "nao"
                salvar_permissoes(df)
                st.success("Permissão desativada.")
                st.rerun()

        with col2:
            if st.button("Excluir linha", use_container_width=True):
                df = df.drop(index=indice).reset_index(drop=True)
                salvar_permissoes(df)
                st.success("Permissão excluída.")
                st.rerun()
