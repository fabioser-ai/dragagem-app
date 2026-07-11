import pandas as pd
import streamlit as st

from services.permissoes import (
    carregar_permissoes_resultado,
    eh_superadmin,
    salvar_permissoes_seguro,
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


def _mostrar_erro_leitura(resultado):
    detalhes = resultado.erro or "Não foi possível confirmar a leitura do arquivo de permissões."

    if resultado.http_status:
        detalhes = f"{detalhes} (HTTP {resultado.http_status})"

    st.error(
        "As alterações estão bloqueadas para preservar os dados. "
        f"{detalhes}"
    )


def _salvar_alteracao(df, sha_esperado, mensagem_sucesso):
    resultado = salvar_permissoes_seguro(
        df,
        sha_esperado=sha_esperado,
    )

    if resultado.sucesso:
        st.success(mensagem_sucesso)
        st.rerun()

    detalhes = resultado.erro or "O GitHub não confirmou a gravação."

    if resultado.http_status:
        detalhes = f"{detalhes} (HTTP {resultado.http_status})"

    st.error(f"Alteração não salva. {detalhes}")


def render():
    st.title("Administração")
    st.caption("Gestão de permissões de usuários do sistema FOS.")

    if not eh_superadmin():
        st.error("Acesso restrito ao SuperAdmin.")
        st.stop()

    resultado_leitura = carregar_permissoes_resultado()
    df = resultado_leitura.dados
    escrita_liberada = resultado_leitura.pode_sobrescrever

    if not escrita_liberada:
        _mostrar_erro_leitura(resultado_leitura)

    st.subheader("Permissões cadastradas")

    if df.empty:
        if escrita_liberada:
            st.info("Nenhuma permissão cadastrada ainda.")
        else:
            st.info("A lista não está disponível porque a leitura não foi confirmada.")
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

        salvar = st.form_submit_button(
            "Salvar permissão",
            disabled=not escrita_liberada,
        )

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

        df_atualizado = pd.concat(
            [
                df,
                pd.DataFrame([nova_linha]),
            ],
            ignore_index=True,
        )

        _salvar_alteracao(
            df_atualizado,
            resultado_leitura.sha,
            "Permissão salva com sucesso.",
        )

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
            desativar = st.button(
                "Desativar permissão",
                use_container_width=True,
                disabled=not escrita_liberada,
            )

            if desativar:
                df_atualizado = df.copy()
                df_atualizado.loc[indice, "ativo"] = "nao"
                _salvar_alteracao(
                    df_atualizado,
                    resultado_leitura.sha,
                    "Permissão desativada.",
                )

        with col2:
            excluir = st.button(
                "Excluir linha",
                use_container_width=True,
                disabled=not escrita_liberada,
            )

            if excluir:
                df_atualizado = df.drop(index=indice).reset_index(drop=True)
                _salvar_alteracao(
                    df_atualizado,
                    resultado_leitura.sha,
                    "Permissão excluída.",
                )
