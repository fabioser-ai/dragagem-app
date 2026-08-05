import pandas as pd
import streamlit as st

from services.autorizacao import pode_gerenciar_administracao
from services.permissoes import carregar_permissoes_resultado, salvar_permissoes_seguro
from services.usuarios_operacionais import (
    PERFIS_PERMITIDOS,
    carregar_usuarios_operacionais_resultado,
    criar_usuario,
    editar_usuario,
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
    if not pode_gerenciar_administracao():
        st.error("Alteração não autorizada.")
        return False

    resultado = salvar_permissoes_seguro(
        df,
        sha_esperado=sha_esperado,
    )

    if resultado.sucesso:
        st.success(mensagem_sucesso)
        st.rerun()
        return True

    detalhes = resultado.erro or "O GitHub não confirmou a gravação."

    if resultado.http_status:
        detalhes = f"{detalhes} (HTTP {resultado.http_status})"

    st.error(f"Alteração não salva. {detalhes}")
    return False


def _informar_operacao(resultado):
    if resultado.sucesso:
        st.success(resultado.mensagem)
        st.rerun()
    else:
        st.error(resultado.mensagem)


def _render_usuarios_operacionais():
    st.subheader("Usuários operacionais")
    st.caption(
        "Base interna separada. Estes usuários ainda não podem autenticar no APP."
    )
    leitura = carregar_usuarios_operacionais_resultado()
    liberada = leitura.pode_sobrescrever
    if not liberada:
        st.error(
            "Alterações bloqueadas: a leitura da base operacional não foi confirmada."
        )

    exibicao = leitura.dados.copy()
    if exibicao.empty:
        st.info("Nenhum usuário operacional cadastrado.")
    else:
        exibicao["estado"] = exibicao["ativo"].map(
            {"sim": "🟢 Operacional ativo", "nao": "⚪ Operacional inativo"}
        ).fillna("⚠️ Estado inválido")
        st.dataframe(
            exibicao[[
                "login", "nome", "matricula", "perfil_base", "estado",
                "credencial_configurada", "criado_em", "criado_por",
                "atualizado_em", "atualizado_por",
            ]],
            use_container_width=True,
        )

    with st.expander("Cadastrar usuário operacional"):
        with st.form("form_usuario_operacional_novo"):
            login = st.text_input("Login")
            nome = st.text_input("Nome")
            matricula = st.text_input("Matrícula")
            email = st.text_input("E-mail")
            perfil = st.selectbox("Perfil base", PERFIS_PERMITIDOS, index=0)
            enviar = st.form_submit_button("Cadastrar inativo", disabled=not liberada)
        if enviar:
            _informar_operacao(criar_usuario(
                leitura=leitura, login=login, nome=nome, matricula=matricula,
                email=email, perfil_base=perfil,
            ))

    if not exibicao.empty:
        opcoes = {
            f"{row['login']} — {row['nome']} ({row['ativo']})": row["usuario_id"]
            for _, row in exibicao.iterrows()
        }
        selecionado = st.selectbox("Editar usuário operacional", list(opcoes))
        usuario_id = opcoes[selecionado]
        atual = exibicao[exibicao["usuario_id"] == usuario_id].iloc[0]
        with st.form("form_usuario_operacional_edicao"):
            st.text_input("Login reservado", value=atual["login"], disabled=True)
            nome_edicao = st.text_input("Nome", value=atual["nome"])
            matricula_edicao = st.text_input("Matrícula", value=atual["matricula"])
            email_edicao = st.text_input("E-mail", value=atual["email"])
            perfil_edicao = st.selectbox(
                "Perfil base", PERFIS_PERMITIDOS,
                index=(
                    PERFIS_PERMITIDOS.index(atual["perfil_base"])
                    if atual["perfil_base"] in PERFIS_PERMITIDOS else 0
                ),
            )
            ativo_edicao = st.selectbox(
                "Estado", ("nao", "sim"),
                index=0 if atual["ativo"] != "sim" else 1,
            )
            atualizar = st.form_submit_button("Salvar alteração", disabled=not liberada)
        if atualizar:
            _informar_operacao(editar_usuario(
                leitura=leitura, usuario_id=usuario_id, nome=nome_edicao,
                matricula=matricula_edicao, email=email_edicao,
                perfil_base=perfil_edicao, ativo=ativo_edicao,
            ))

    st.info(
        "Contas protegidas permanecem exclusivamente em APP_USERS e não são "
        "editáveis nesta interface. A exclusão física não está disponível."
    )
    st.divider()


def render():
    st.title("Administração")
    st.caption("Gestão de permissões de usuários do sistema FOS.")

    if not pode_gerenciar_administracao():
        st.error("Acesso restrito à custódia administrativa.")
        st.stop()

    _render_usuarios_operacionais()

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
