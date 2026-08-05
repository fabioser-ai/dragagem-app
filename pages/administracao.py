import pandas as pd
import streamlit as st

from services.autorizacao import pode_gerenciar_administracao
from services.permissoes import carregar_permissoes_resultado, salvar_permissoes_seguro
from services.permissoes_catalogo import carregar_catalogo_resultado
from services.roles import (
    carregar_roles_permissoes_resultado,
    carregar_roles_resultado,
    criar_role,
    editar_role,
)
from services.usuarios_operacionais import (
    PERFIS_PERMITIDOS,
    carregar_usuarios_operacionais_resultado,
    criar_usuario,
    editar_usuario,
)
from services.usuarios_roles import (
    atribuir_role,
    carregar_usuarios_roles_resultado,
    retirar_role,
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


def _render_catalogo_permissoes():
    st.subheader("CATÁLOGO DE PERMISSÕES")
    st.caption(
        "Este catálogo não concede acesso. Ele apenas define as capacidades "
        "reconhecidas pelo RBAC."
    )
    resultado = carregar_catalogo_resultado()
    if not resultado.leitura_confirmada:
        st.error("Não foi possível confirmar a leitura do catálogo canônico.")
        st.divider()
        return

    catalogo = resultado.dados.copy()
    if catalogo.empty:
        st.info("O catálogo canônico está vazio.")
        st.divider()
        return

    col1, col2, col3, col4 = st.columns(4)
    modulo = col1.selectbox(
        "Módulo", ["Todos"] + sorted(catalogo["modulo"].unique().tolist()),
        key="catalogo_filtro_modulo",
    )
    acao = col2.selectbox(
        "Ação", ["Todas"] + sorted(catalogo["acao"].unique().tolist()),
        key="catalogo_filtro_acao",
    )
    sensibilidade = col3.selectbox(
        "Sensibilidade",
        ["Todas"] + sorted(catalogo["sensibilidade"].unique().tolist()),
        key="catalogo_filtro_sensibilidade",
    )
    protecao = col4.selectbox(
        "Estado da proteção",
        ["Todos"] + sorted(catalogo["estado_protecao"].unique().tolist()),
        key="catalogo_filtro_protecao",
    )

    filtrado = catalogo.copy()
    if modulo != "Todos":
        filtrado = filtrado[filtrado["modulo"] == modulo]
    if acao != "Todas":
        filtrado = filtrado[filtrado["acao"] == acao]
    if sensibilidade != "Todas":
        filtrado = filtrado[filtrado["sensibilidade"] == sensibilidade]
    if protecao != "Todos":
        filtrado = filtrado[filtrado["estado_protecao"] == protecao]

    st.dataframe(
        filtrado[[
            "modulo", "recurso", "acao", "nome", "descricao",
            "sensibilidade", "escopo_obra", "estado_protecao", "evidencia",
        ]],
        use_container_width=True,
        hide_index=True,
    )
    st.divider()


def _render_roles():
    st.subheader("Roles")
    st.caption(
        "Catálogo RBAC reutilizável. Roles ainda não estão conectadas a usuários."
    )
    leitura = carregar_roles_resultado()
    leitura_permissoes = carregar_roles_permissoes_resultado()
    liberada = leitura.pode_sobrescrever
    if not liberada:
        st.error("Alterações bloqueadas: a leitura do catálogo de Roles não foi confirmada.")

    roles = leitura.dados.copy()
    if roles.empty:
        st.info("Nenhuma Role cadastrada.")
    else:
        roles["estado"] = roles["ativo"].map(
            {"sim": "🟢 Ativa", "nao": "⚪ Inativa"}
        ).fillna("⚠️ Estado inválido")
        st.dataframe(
            roles[[
                "codigo", "nome", "descricao", "estado", "versao",
                "criado_em", "criado_por", "atualizado_em", "atualizado_por",
            ]],
            use_container_width=True,
        )

    with st.expander("Criar Role"):
        with st.form("form_role_nova"):
            codigo = st.text_input("Código da Role")
            nome = st.text_input("Nome da Role")
            descricao = st.text_area("Descrição da Role")
            criar = st.form_submit_button("Criar Role inativa", disabled=not liberada)
        if criar:
            _informar_operacao(criar_role(
                leitura=leitura, codigo=codigo, nome=nome, descricao=descricao,
            ))

    if not roles.empty:
        opcoes = {
            f"{row['codigo']} — {row['nome']} ({row['ativo']})": row["role_id"]
            for _, row in roles.iterrows()
        }
        selecionada = st.selectbox("Selecionar Role", list(opcoes))
        role_id = opcoes[selecionada]
        atual = roles[roles["role_id"] == role_id].iloc[0]
        with st.form("form_role_edicao"):
            st.text_input("Código imutável", value=atual["codigo"], disabled=True)
            nome_edicao = st.text_input("Nome", value=atual["nome"])
            descricao_edicao = st.text_area("Descrição", value=atual["descricao"])
            ativo_edicao = st.selectbox(
                "Estado", ("nao", "sim"),
                index=0 if atual["ativo"] != "sim" else 1,
            )
            atualizar = st.form_submit_button("Salvar Role", disabled=not liberada)
        if atualizar:
            _informar_operacao(editar_role(
                leitura=leitura, role_id=role_id, nome=nome_edicao,
                descricao=descricao_edicao, ativo=ativo_edicao,
            ))

        st.markdown("#### Permissões da Role")
        if not leitura_permissoes.leitura_confirmada:
            st.error("Não foi possível confirmar a leitura do catálogo de permissões das Roles.")
        else:
            permissoes = leitura_permissoes.dados
            vinculadas = permissoes[
                permissoes["role_id"].astype(str) == str(role_id)
            ]
            if vinculadas.empty:
                st.info("Esta Role ainda não possui permissões.")
            else:
                st.dataframe(
                    vinculadas[["modulo", "recurso", "acao", "efeito"]],
                    use_container_width=True,
                )

    st.info("Roles não podem ser excluídas; somente ativadas ou inativadas.")
    st.divider()


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


def _render_usuarios_roles():
    st.subheader("ROLES DOS USUÁRIOS")
    st.caption("Estas associações ainda não alteram o acesso efetivo do usuário.")
    leitura = carregar_usuarios_roles_resultado()
    leitura_usuarios = carregar_usuarios_operacionais_resultado()
    leitura_roles = carregar_roles_resultado()
    leitura_permissoes = carregar_roles_permissoes_resultado()
    liberada = all(item.pode_sobrescrever for item in (
        leitura, leitura_usuarios, leitura_roles,
    ))
    if not liberada:
        st.error("Alterações bloqueadas: usuários, Roles e associações exigem leitura confirmada.")
        st.divider()
        return

    usuarios = leitura_usuarios.dados.copy()
    roles = leitura_roles.dados.copy()
    associacoes = leitura.dados.copy()
    if usuarios.empty:
        st.info("Nenhum usuário operacional disponível para associação.")
        st.divider()
        return

    opcoes_usuarios = {
        f"{row['nome']} — {row['login']} — matrícula {row['matricula']} ({row['ativo']})": row["usuario_id"]
        for _, row in usuarios.iterrows()
    }
    escolhido = st.selectbox("Usuário operacional", list(opcoes_usuarios), key="usuario_role_usuario")
    usuario_id = opcoes_usuarios[escolhido]
    usuario = usuarios[usuarios["usuario_id"] == usuario_id].iloc[0]
    st.write(
        f"**Nome:** {usuario['nome']}  |  **Login:** {usuario['login']}  |  "
        f"**Matrícula:** {usuario['matricula']}  |  **Ativo:** {usuario['ativo']}"
    )

    historico = associacoes[associacoes["usuario_id"].astype(str) == str(usuario_id)].copy()
    if historico.empty:
        st.info("Este usuário ainda não possui histórico de Roles.")
    else:
        nomes = roles.set_index("role_id")["codigo"].to_dict()
        historico["role"] = historico["role_id"].map(nomes).fillna("Role não localizada")
        st.dataframe(
            historico[[
                "role", "ativo", "criado_em", "criado_por",
                "atualizado_em", "atualizado_por",
            ]], use_container_width=True, hide_index=True,
        )

    roles_ativas = roles[roles["ativo"].astype(str).str.casefold() == "sim"]
    if str(usuario["ativo"]).casefold() == "sim" and not roles_ativas.empty:
        opcoes_roles = {
            f"{row['codigo']} — {row['nome']}": row["role_id"]
            for _, row in roles_ativas.iterrows()
        }
        role_escolhida = st.selectbox("Role ativa", list(opcoes_roles), key="usuario_role_role")
        role_id = opcoes_roles[role_escolhida]
        col_atribuir, col_retirar = st.columns(2)
        if col_atribuir.button("Atribuir ou reativar Role", use_container_width=True):
            _informar_operacao(atribuir_role(
                leitura=leitura, leitura_usuarios=leitura_usuarios,
                leitura_roles=leitura_roles, usuario_id=usuario_id, role_id=role_id,
            ))
        if col_retirar.button("Retirar Role", use_container_width=True):
            _informar_operacao(retirar_role(
                leitura=leitura, leitura_usuarios=leitura_usuarios,
                leitura_roles=leitura_roles, usuario_id=usuario_id, role_id=role_id,
            ))
        if leitura_permissoes.leitura_confirmada:
            permissoes = leitura_permissoes.dados
            vinculadas = permissoes[permissoes["role_id"].astype(str) == str(role_id)]
            st.markdown("#### Permissões documentais da Role")
            if vinculadas.empty:
                st.info("Esta Role é válida e está vazia.")
            else:
                st.dataframe(
                    vinculadas[["modulo", "recurso", "acao", "efeito"]],
                    use_container_width=True, hide_index=True,
                )
    else:
        st.info("Usuário inativo não pode receber nova Role; associações existentes podem ser consultadas e retiradas.")
        ativas = historico[historico["ativo"].astype(str).str.casefold() == "sim"]
        if not ativas.empty:
            opcoes_retirada = {
                roles.set_index("role_id")["codigo"].to_dict().get(row["role_id"], row["role_id"]): row["role_id"]
                for _, row in ativas.iterrows()
            }
            selecionada = st.selectbox("Role ativa para retirada", list(opcoes_retirada), key="usuario_role_retirada")
            if st.button("Retirar Role ativa", use_container_width=True):
                _informar_operacao(retirar_role(
                    leitura=leitura, leitura_usuarios=leitura_usuarios,
                    leitura_roles=leitura_roles, usuario_id=usuario_id,
                    role_id=opcoes_retirada[selecionada],
                ))
    st.divider()


def render():
    st.title("Administração")
    st.caption("Gestão de permissões de usuários do sistema FOS.")

    if not pode_gerenciar_administracao():
        st.error("Acesso restrito à custódia administrativa.")
        st.stop()

    _render_catalogo_permissoes()
    _render_roles()
    _render_usuarios_operacionais()
    _render_usuarios_roles()

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
