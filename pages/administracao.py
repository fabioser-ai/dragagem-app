import pandas as pd
import streamlit as st

from services.autorizacao import pode_gerenciar_administracao
from services.permissoes import carregar_permissoes_resultado, salvar_permissoes_seguro
from services.permissoes_catalogo import carregar_catalogo_resultado
from services.rbac_shadow import calcular_usuario, diagnosticar_usuarios
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


ROTULOS_ACOES = {
    "visualizar": "Visualizar",
    "criar": "Criar",
    "editar": "Editar",
    "excluir": "Excluir",
    "aprovar": "Aprovar",
    "cancelar": "Cancelar",
    "administrar": "Administrar",
    "lancar": "Lançar",
    "todos": "Todas as ações",
}
ROTULOS_MODULOS = {
    "prestacao_contas": "Prestação de Contas",
    "uniformes_epis": "Uniformes e EPIs",
    "ferias": "Férias e Folgas",
    "orcamento": "Orçamento",
    "medicoes": "Medições",
    "dados": "Dados",
    "obras": "Obras",
    "crm": "CRM",
}
ROTULOS_RECURSOS = {
    "decisao_despesa": "Decisão de despesa",
    "tipo_despesa": "Tipo de despesa",
    "local_trabalho": "Local de trabalho",
}


def _rotulo_chave(chave):
    partes = [parte.strip() for parte in str(chave or "").split("/")]
    if len(partes) != 3:
        return str(chave or "")
    modulo, recurso, acao = partes
    modulo = ROTULOS_MODULOS.get(modulo.casefold(), modulo.replace("_", " ").title())
    recurso = ROTULOS_RECURSOS.get(recurso.casefold(), recurso.replace("_", " ").title())
    acao = ROTULOS_ACOES.get(acao.casefold(), acao.replace("_", " ").title())
    return f"{modulo} — {recurso}: {acao}"


def _linhas_permissoes(permissoes):
    return [_rotulo_chave(item) for item in permissoes]


def _status_diagnostico(status):
    return {
        "IGUAL": "O acesso atual coincide com o calculado pelas Roles",
        "DIVERGENTE": "Há diferenças entre o acesso atual e o calculado pelas Roles",
        "SEM ROLE": "O usuário ainda não possui função atribuída",
        "ROLE VAZIA": "A função atribuída ainda não possui permissões",
    }.get(str(status), str(status))


AJUDA_COLUNAS = {
    "Usuário": "Pessoa à qual a informação se refere. Não define credencial ou acesso por si só.",
    "Login": "Nome que identifica a pessoa. Para usuários operacionais, ainda não autentica no APP.",
    "Perfil-base": "Classificação cadastral inicial. Não substitui Roles nem concede acesso.",
    "Cadastro": "Estado do registro operacional. Ativo ainda não significa entrada disponível.",
    "Credencial": "Indica se existe credencial operacional funcional. Ela ainda não foi implementada.",
    "Troca de senha": "Campo reservado ao futuro ciclo de credenciais; hoje não possui efeito.",
    "Role / função": "Função institucional atribuível. No Shadow Mode, não altera o acesso real.",
    "Estado da Role": "Indica se a Role pode ser usada em novas associações; não é acesso efetivo.",
    "Permissões atuais": "Autorizações efetivamente usadas hoje pelo APP.",
    "Permissões pelas Roles": "Autorizações que o novo modelo calcularia; ainda não têm efeito real.",
    "O novo modelo concederia": "Permissões das Roles ausentes no acesso efetivo atual.",
    "O acesso atual possui, mas as Roles não concedem": "Permissões efetivas não cobertas pelas Roles atribuídas.",
    "Status da comparação": "Resultado da comparação entre o acesso atual e o cálculo em Shadow Mode.",
    "Criado por": "Usuário administrativo que criou o registro.",
    "Atualizado por": "Usuário administrativo responsável pela última alteração.",
    "Criado em": "Data e hora de criação do registro.",
    "Atualizado em": "Data e hora da última alteração.",
}


def _config_colunas(*nomes):
    return {
        nome: st.column_config.TextColumn(nome, help=AJUDA_COLUNAS[nome])
        for nome in nomes if nome in AJUDA_COLUNAS
    }


def _render_ajuda_controle_acesso():
    with st.expander("Mais informações"):
        st.markdown("### Administração de acesso")
        st.markdown("#### Como funciona o controle de acesso?")
        st.write(
            "Use este módulo para cadastrar pessoas, organizar funções, consultar "
            "o acesso atual e comparar o novo modelo RBAC antes de sua ativação."
        )
        st.info(
            "Hoje, o acesso real ainda é definido pelo modelo atual. O novo modelo "
            "de usuários operacionais, Roles e permissões está em preparação e "
            "ainda não substitui a autorização existente."
        )
        st.markdown(
            """
**ACESSO EM USO HOJE**

- **APP_USERS:** contém as contas protegidas que autenticam atualmente e continua
  sendo a fonte das credenciais existentes. Não é administrado pelos usuários
  operacionais.
- **Permissões efetivas atuais:** são as autorizações realmente usadas hoje pelo APP.

**NOVO MODELO POR ROLES — EM PREPARAÇÃO**

- **Usuários operacionais:** representam pessoas cadastradas no novo modelo. Podem
  ser ativadas e associadas a Roles, mas ainda não possuem login funcional.
- **Roles:** representam funções institucionais e agrupam permissões. Não concedem
  acesso real enquanto o RBAC estiver em modo de diagnóstico.
- **Permissões pelas Roles:** representam o acesso que o novo modelo calcularia;
  ainda não liberam nem bloqueiam operações.
- **Diagnóstico (Shadow Mode):** compara os dois modelos e não altera o acesso.
- **Credenciais:** ainda não foram implementadas para usuários operacionais.
  Nenhum e-mail, senha ou convite é gerado atualmente.

**Fluxo recomendado**

1. Cadastre a pessoa — o cadastro nasce inativo e sem credencial.
2. Revise os dados e ative o registro operacional.
3. Atribua uma Role institucional.
4. Consulte o Shadow Mode para comparar o cálculo com o acesso atual.
5. Não considere o acesso migrado: a autorização efetiva continua no modelo atual.

**O que ainda não está disponível**

Login operacional, senha, convite, primeiro acesso, reset, ativação do RBAC e
migração automática de permissões ainda não foram implementados.

**Glossário**

- **Cadastro:** registro da pessoa no novo modelo.
- **Credencial:** mecanismo que permitiria autenticar; ainda não existe para o cadastro operacional.
- **Role:** função institucional que agrupa permissões.
- **Permissão:** decisão sobre o que pode ser feito em um recurso.
- **Shadow Mode:** comparação sem efeito na autorização.
"""
        )


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
        column_config={
            "modulo": st.column_config.TextColumn("Módulo", help="Área funcional à qual a capacidade pertence."),
            "recurso": st.column_config.TextColumn("Recurso", help="Objeto protegido dentro do módulo."),
            "acao": st.column_config.TextColumn("Ação", help="Operação administrativa representada pela permissão."),
            "sensibilidade": st.column_config.TextColumn("Sensibilidade", help="Classificação documental do impacto da capacidade."),
            "estado_protecao": st.column_config.TextColumn("Proteção", help="Estado comprovado da guarda no código atual."),
        },
    )
    st.divider()


def _render_roles():
    st.subheader("Modelo por Roles — em preparação")
    st.caption(
        "Funções institucionais reutilizáveis. Elas podem ser atribuídas, mas "
        "ainda não alteram o acesso efetivo."
    )
    st.warning("As Roles ainda não alteram o acesso real.")
    leitura = carregar_roles_resultado()
    leitura_permissoes = carregar_roles_permissoes_resultado()
    leitura_associacoes = carregar_usuarios_roles_resultado()
    liberada = leitura.pode_sobrescrever
    if not liberada:
        st.error("Alterações bloqueadas: a leitura do catálogo de Roles não foi confirmada.")

    roles = leitura.dados.copy()
    if roles.empty:
        st.info("Nenhuma Role cadastrada.")
    else:
        associacoes_ativas = leitura_associacoes.dados[
            leitura_associacoes.dados["ativo"].astype(str).str.casefold() == "sim"
        ] if leitura_associacoes.leitura_confirmada else pd.DataFrame()
        permissoes = (
            leitura_permissoes.dados
            if leitura_permissoes.leitura_confirmada else pd.DataFrame()
        )
        roles["usuários vinculados"] = roles["role_id"].map(
            associacoes_ativas.groupby("role_id").size() if not associacoes_ativas.empty else {}
        ).fillna(0).astype(int)
        roles["permissões"] = roles["role_id"].map(
            permissoes.groupby("role_id").size() if not permissoes.empty else {}
        ).fillna(0).astype(int)
        roles["estado"] = roles["ativo"].map(
            {"sim": "🟢 Ativa", "nao": "⚪ Inativa"}
        ).fillna("⚠️ Estado inválido")
        exibicao_roles = roles[[
                "codigo", "nome", "descricao", "estado",
                "usuários vinculados", "permissões", "versao",
                "criado_em", "criado_por", "atualizado_em", "atualizado_por",
            ]].rename(columns={
                "codigo": "Código", "nome": "Role / função", "descricao": "Finalidade",
                "estado": "Estado da Role", "usuários vinculados": "Pessoas vinculadas",
                "permissões": "Permissões calculadas", "versao": "Versão",
                "criado_em": "Criada em", "criado_por": "Criada por",
                "atualizado_em": "Atualizada em", "atualizado_por": "Atualizada por",
            })
        st.caption(
            "Role é uma função institucional. Pessoas vinculadas indica quantos "
            "cadastros possuem a função; permissões calculadas ainda não são acesso real."
        )
        st.dataframe(
            exibicao_roles,
            use_container_width=True,
            hide_index=True,
            column_config={
                **_config_colunas("Role / função", "Estado da Role", "Criada por", "Atualizada por"),
                "Pessoas vinculadas": st.column_config.NumberColumn(
                    "Pessoas vinculadas", help="Quantidade de associações ativas; não significa acesso liberado."
                ),
                "Permissões calculadas": st.column_config.NumberColumn(
                    "Permissões calculadas", help="Capacidades documentadas na Role; ainda sem efeito real."
                ),
                "Criada em": st.column_config.TextColumn("Criada em", help=AJUDA_COLUNAS["Criado em"]),
                "Atualizada em": st.column_config.TextColumn("Atualizada em", help=AJUDA_COLUNAS["Atualizado em"]),
            },
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
                st.info("Esta Role está vazia e ainda não calcula permissões.")
            else:
                st.dataframe(
                    vinculadas[["modulo", "recurso", "acao", "efeito"]],
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "modulo": st.column_config.TextColumn("Módulo", help="Área funcional protegida."),
                        "recurso": st.column_config.TextColumn("Recurso", help="Objeto ao qual a permissão se aplica."),
                        "acao": st.column_config.TextColumn("Ação", help="Operação agrupada pela Role."),
                        "efeito": st.column_config.TextColumn("Efeito", help="Decisão documental allow/deny; ainda não participa da autorização."),
                    },
                )
                st.caption(
                    "Esta função não concede administração do sistema, custódia, "
                    "superadmin ou gestão de contas protegidas."
                )

    st.info("Roles não podem ser excluídas; somente ativadas ou inativadas.")
    st.divider()


def _render_criacao_usuario(leitura):
    with st.expander("Criar novo usuário operacional"):
        st.info(
            "O e-mail é apenas cadastral. Nenhum convite será enviado, nenhuma "
            "senha será gerada e o cadastro será criado inicialmente inativo."
        )
        with st.form("form_usuario_operacional_novo"):
            login = st.text_input(
                "Login *",
                help=("Nome utilizado para identificar a pessoa. Usuários operacionais "
                      "ainda não autenticam com este login."),
            )
            nome = st.text_input("Nome *")
            matricula = st.text_input("Matrícula *")
            email = st.text_input("E-mail cadastral *")
            perfil = st.selectbox(
                "Perfil base *", PERFIS_PERMITIDOS, index=0,
                help=("Classificação cadastral inicial. Não substitui as Roles e não "
                      "concede acesso por si só."),
            )
            enviar = st.form_submit_button(
                "Criar usuário inativo", disabled=not leitura.pode_sobrescrever
            )
        if enviar:
            resultado = criar_usuario(
                leitura=leitura, login=login, nome=nome, matricula=matricula,
                email=email, perfil_base=perfil,
            )
            if resultado.sucesso:
                st.success(
                    "Usuário criado como inativo. Próximos passos: revisar o "
                    "cadastro, ativar e atribuir uma função. Nenhum e-mail foi enviado."
                )
                st.rerun()
            else:
                st.error(resultado.mensagem)


def _render_estado_usuario(usuario, leitura_usuarios):
    ativo = str(usuario["ativo"]).strip().casefold() == "sim"
    col_estado, col_login, col_credencial = st.columns(3)
    col_estado.metric("Estado do cadastro", "Ativo" if ativo else "Inativo")
    col_login.metric("Pode entrar no APP?", "Não")
    col_credencial.metric("Credencial configurada", "Não")
    st.warning(
        "Este usuário operacional ainda não pode entrar no APP. Ativação e "
        "atribuição de função não criam credencial nem alteram o login atual."
    )
    st.caption(
        f"Exige troca de senha: {usuario['exige_troca_senha'] or 'não'} — "
        "campo reservado para o futuro ciclo de credenciais; ainda não possui "
        "efeito funcional."
    )

    if ativo:
        confirmar = st.checkbox(
            "Confirmo a inativação deste cadastro operacional.",
            key=f"confirmar_inativacao_{usuario['usuario_id']}",
        )
        if st.button(
            "Inativar usuário", disabled=not confirmar or not leitura_usuarios.pode_sobrescrever,
            key=f"inativar_{usuario['usuario_id']}",
        ):
            _informar_operacao(editar_usuario(
                leitura=leitura_usuarios, usuario_id=usuario["usuario_id"],
                nome=usuario["nome"], matricula=usuario["matricula"],
                email=usuario["email"], perfil_base=usuario["perfil_base"], ativo="nao",
            ))
        st.caption(
            "Inativar este cadastro ainda não revoga uma sessão de APP_USERS, "
            "pois usuários operacionais ainda não autenticam."
        )
    elif st.button(
        "Ativar usuário", disabled=not leitura_usuarios.pode_sobrescrever,
        key=f"ativar_{usuario['usuario_id']}",
    ):
        _informar_operacao(editar_usuario(
            leitura=leitura_usuarios, usuario_id=usuario["usuario_id"],
            nome=usuario["nome"], matricula=usuario["matricula"],
            email=usuario["email"], perfil_base=usuario["perfil_base"], ativo="sim",
        ))


def _render_identidade_usuario(usuario, leitura_usuarios):
    st.markdown("### Identidade")
    col1, col2 = st.columns(2)
    col1.write(f"**Nome:** {usuario['nome']}")
    col1.write(f"**Login:** {usuario['login']}")
    col1.write(f"**Matrícula:** {usuario['matricula']}")
    col2.write(f"**E-mail cadastral:** {usuario['email']}")
    col2.write(f"**Perfil-base:** {usuario['perfil_base']}")
    col2.caption("O e-mail é apenas cadastral; nenhum convite será enviado.")
    st.caption(
        "Login identifica o cadastro, mas ainda não autentica. Perfil-base é uma "
        "classificação cadastral e não concede acesso nem substitui as Roles."
    )
    with st.expander("Editar dados"):
        with st.form(f"form_usuario_edicao_{usuario['usuario_id']}"):
            st.text_input(
                "Login reservado", value=usuario["login"], disabled=True,
                help=("Nome utilizado para identificar a pessoa. Usuários operacionais "
                      "ainda não autenticam com este login."),
            )
            nome = st.text_input("Nome", value=usuario["nome"])
            matricula = st.text_input("Matrícula", value=usuario["matricula"])
            email = st.text_input("E-mail cadastral", value=usuario["email"])
            perfil = st.selectbox(
                "Perfil base", PERFIS_PERMITIDOS,
                index=(PERFIS_PERMITIDOS.index(usuario["perfil_base"])
                       if usuario["perfil_base"] in PERFIS_PERMITIDOS else 0),
                help=("Classificação cadastral inicial. Não substitui as Roles e não "
                      "concede acesso por si só."),
            )
            salvar = st.form_submit_button(
                "Salvar dados", disabled=not leitura_usuarios.pode_sobrescrever
            )
        if salvar:
            _informar_operacao(editar_usuario(
                leitura=leitura_usuarios, usuario_id=usuario["usuario_id"],
                nome=nome, matricula=matricula, email=email,
                perfil_base=perfil, ativo=usuario["ativo"],
            ))


def _render_roles_usuario(usuario, leituras):
    st.markdown("### Funções atribuídas ao usuário")
    st.caption(
        "Role é uma função institucional atribuída à pessoa. Reúne permissões, "
        "mas ainda não altera o acesso real."
    )
    associacoes = leituras["associacoes"].dados.copy()
    roles = leituras["roles"].dados.copy()
    matriz = leituras["matriz"].dados.copy()
    usuario_id = str(usuario["usuario_id"])
    historico = associacoes[
        associacoes["usuario_id"].astype(str) == usuario_id
    ].copy()
    nomes = roles.set_index("role_id").to_dict("index") if not roles.empty else {}

    if historico.empty:
        st.info("Este usuário ainda não possui funções atribuídas.")
    else:
        historico["Função"] = historico["role_id"].map(
            lambda role_id: nomes.get(role_id, {}).get("nome", "Função não localizada")
        )
        historico["Código"] = historico["role_id"].map(
            lambda role_id: nomes.get(role_id, {}).get("codigo", role_id)
        )
        historico["Estado"] = historico["ativo"].map(
            {"sim": "Ativa", "nao": "Retirada — histórico preservado"}
        ).fillna("Estado desconhecido")
        st.dataframe(
            historico[["Função", "Código", "Estado", "atualizado_em", "atualizado_por"]]
            .rename(columns={
                "atualizado_em": "Última alteração",
                "atualizado_por": "Alterada por",
            }),
            use_container_width=True, hide_index=True,
            column_config={
                "Função": st.column_config.TextColumn("Role / função", help=AJUDA_COLUNAS["Role / função"]),
                "Estado": st.column_config.TextColumn("Estado da Role", help=AJUDA_COLUNAS["Estado da Role"]),
                "Última alteração": st.column_config.TextColumn("Última alteração", help=AJUDA_COLUNAS["Atualizado em"]),
                "Alterada por": st.column_config.TextColumn("Alterada por", help=AJUDA_COLUNAS["Atualizado por"]),
            },
        )

    roles_ativas = roles[roles["ativo"].astype(str).str.casefold() == "sim"]
    if str(usuario["ativo"]).casefold() != "sim":
        st.info("Usuário inativo não pode receber nova função.")
    elif roles_ativas.empty:
        st.info("Não há funções ativas disponíveis.")
    else:
        opcoes = {
            f"{row['nome']} ({row['codigo']})": row["role_id"]
            for _, row in roles_ativas.iterrows()
        }
        escolhida = st.selectbox(
            "Função disponível", list(opcoes), key=f"role_ficha_{usuario_id}"
        )
        role_id = opcoes[escolhida]
        role = roles_ativas[roles_ativas["role_id"].astype(str) == str(role_id)].iloc[0]
        permissoes = matriz[matriz["role_id"].astype(str) == str(role_id)]
        st.write(f"**Objetivo:** {role['descricao'] or role['nome']}")
        st.write(f"**Permissões documentais:** {len(permissoes)}")
        if permissoes.empty:
            st.info("Esta função está vazia e não calcula permissões.")
        else:
            st.caption("Resumo: " + "; ".join(
                _rotulo_chave(f"{row['modulo']} / {row['recurso']} / {row['acao']}")
                for _, row in permissoes.iterrows()
            ))
        if st.button("Atribuir ou reativar função", key=f"atribuir_{usuario_id}_{role_id}"):
            _informar_operacao(atribuir_role(
                leitura=leituras["associacoes"], leitura_usuarios=leituras["usuarios"],
                leitura_roles=leituras["roles"], usuario_id=usuario_id, role_id=role_id,
            ))

    ativas = historico[historico["ativo"].astype(str).str.casefold() == "sim"]
    if not ativas.empty:
        opcoes_retirada = {
            f"{nomes.get(row['role_id'], {}).get('nome', row['role_id'])}": row["role_id"]
            for _, row in ativas.iterrows()
        }
        retirada = st.selectbox(
            "Função ativa para retirada", list(opcoes_retirada),
            key=f"retirar_role_{usuario_id}",
        )
        confirmar = st.checkbox(
            "Confirmo a retirada. O histórico será preservado.",
            key=f"confirmar_retirada_{usuario_id}",
        )
        if st.button(
            "Retirar função", disabled=not confirmar,
            key=f"retirar_{usuario_id}_{opcoes_retirada[retirada]}",
        ):
            _informar_operacao(retirar_role(
                leitura=leituras["associacoes"], leitura_usuarios=leituras["usuarios"],
                leitura_roles=leituras["roles"], usuario_id=usuario_id,
                role_id=opcoes_retirada[retirada],
            ))
    st.info("Uma função atribuída ainda não altera o acesso real do usuário.")

    if not ativas.empty:
        nomes_ativas = [
            nomes.get(row["role_id"], {}).get("codigo", row["role_id"])
            for _, row in ativas.iterrows()
        ]
        st.caption(
            "Estado desta pessoa: " + ", ".join(nomes_ativas)
            + (" está atribuída." if len(nomes_ativas) == 1 else " estão atribuídas.")
            + " Essas funções seriam usadas pelo novo modelo, mas ainda não concedem acesso real."
        )


def _render_acesso_usuario(usuario, leituras):
    st.markdown("### Acesso e diagnóstico")
    diagnostico = calcular_usuario(
        usuario=usuario, associacoes=leituras["associacoes"].dados,
        roles=leituras["roles"].dados,
        roles_permissoes=leituras["matriz"].dados,
        catalogo_permissoes=leituras["catalogo"].dados,
        permissoes_atuais=leituras["atuais"].dados,
    )
    st.info(_status_diagnostico(diagnostico.status))
    st.warning(
        "O cálculo por Roles está em modo de diagnóstico e ainda não altera o acesso real."
    )
    col_atual, col_roles = st.columns(2)
    with col_atual:
        st.markdown("#### Permissões atuais — em uso hoje")
        st.caption("Autorizações efetivas utilizadas atualmente pelo APP.")
        linhas = _linhas_permissoes(diagnostico.permissoes_atuais)
        st.write("\n".join(f"- {item}" for item in linhas) if linhas else "Nenhum")
    with col_roles:
        st.markdown("#### Permissões pelas Roles — em preparação")
        st.caption("Autorizações que o novo modelo calcularia caso fosse ativado.")
        linhas = _linhas_permissoes(diagnostico.permissoes_rbac)
        st.write("\n".join(f"- {item}" for item in linhas) if linhas else "Nenhum")
    if diagnostico.rbac_a_mais:
        st.markdown("**O novo modelo concederia:**")
        st.caption("Permissões presentes nas Roles, mas ainda ausentes no acesso atual.")
        st.write("\n".join(f"- {item}" for item in _linhas_permissoes(diagnostico.rbac_a_mais)))
    if diagnostico.rbac_a_menos:
        st.markdown("**O acesso atual possui, mas as Roles não concedem:**")
        st.caption("Permissões em uso hoje que não aparecem nas Roles atribuídas.")
        st.write("\n".join(f"- {item}" for item in _linhas_permissoes(diagnostico.rbac_a_menos)))
    with st.expander("Detalhes técnicos do diagnóstico"):
        st.write("Status técnico:", diagnostico.status)
        st.write("Ocorrências:", list(diagnostico.ocorrencias) or ["Nenhuma"])


def _render_resumo_usuario(usuario, leituras):
    diagnostico = calcular_usuario(
        usuario=usuario, associacoes=leituras["associacoes"].dados,
        roles=leituras["roles"].dados,
        roles_permissoes=leituras["matriz"].dados,
        catalogo_permissoes=leituras["catalogo"].dados,
        permissoes_atuais=leituras["atuais"].dados,
    )
    associacoes = leituras["associacoes"].dados
    roles_ativas = associacoes[
        (associacoes["usuario_id"].astype(str) == str(usuario["usuario_id"]))
        & (associacoes["ativo"].astype(str).str.casefold() == "sim")
    ]
    ativo = str(usuario["ativo"]).strip().casefold() == "sim"
    credencial = str(usuario["credencial_configurada"]).strip().casefold() == "sim"
    primeira_linha = st.columns(3)
    primeira_linha[0].metric(
        "Cadastro", "Ativo" if ativo else "Inativo",
        help=("Indica se o cadastro operacional está ativo. Atualmente isso não "
              "significa que a pessoa consiga entrar no APP."),
    )
    primeira_linha[1].metric(
        "Entrada no APP", "Indisponível",
        help="Cadastro ativo não significa login disponível.",
    )
    primeira_linha[2].metric(
        "Credencial", "Configurada" if credencial else "Não configurada",
        help=("Indica se existe credencial operacional funcional. Atualmente permanece "
              "como não, pois a autenticação operacional ainda não foi implementada."),
    )
    segunda_linha = st.columns(3)
    segunda_linha[0].metric(
        "Roles", len(roles_ativas),
        help="Role atribuída não significa acesso liberado.",
    )
    segunda_linha[1].metric(
        "Acesso real", "Modelo atual",
        help="As permissões efetivas atuais continuam controlando o acesso.",
    )
    segunda_linha[2].metric(
        "Novo RBAC", "Igual" if diagnostico.status == "IGUAL" else "Divergente",
        help="Compara o modelo atual com as Roles; não altera o acesso.",
    )
    st.caption(
        "Cadastro ativo não significa que a pessoa pode entrar. Role atribuída "
        "não significa acesso liberado."
    )
    st.markdown("#### Por que estes estados aparecem?")
    st.write(
        "- **Cadastro:** "
        + ("o registro operacional está ativo. Isso ainda não permite login."
           if ativo else "o registro operacional está inativo e não pode receber nova função.")
    )
    st.write(
        "- **Entrada no APP:** indisponível porque usuários operacionais ainda não "
        "autenticam no APP."
    )
    st.write(
        "- **Credencial:** "
        + ("o cadastro informa uma credencial configurada."
           if credencial else "nenhuma credencial operacional foi criada para esta pessoa.")
    )
    st.write(
        f"- **Roles:** {len(roles_ativas)} função(ões) ativa(s) atribuída(s). "
        "Elas ainda não concedem acesso real."
    )
    if diagnostico.status == "IGUAL":
        st.write("- **Novo RBAC:** o cálculo coincide com o acesso atual.")
    else:
        motivos = []
        if diagnostico.rbac_a_mais:
            motivos.append(
                "o novo modelo concederia permissão que não existe no acesso atual"
            )
        if diagnostico.rbac_a_menos:
            motivos.append(
                "o acesso atual possui permissão que as Roles não concedem"
            )
        st.write(
            "- **Novo RBAC:** há diferenças porque "
            + " e ".join(motivos or ["existem ocorrências técnicas na comparação"])
            + "."
        )


def _render_detalhes_usuario(usuario, associacoes):
    st.markdown("### Detalhes técnicos")
    st.caption("Identificador interno e imutável do cadastro. Não é o login.")
    st.code(str(usuario["usuario_id"]), language=None)
    st.write(f"**Perfil-base:** {usuario['perfil_base']}")
    st.caption(
        "Classificação cadastral inicial. Não substitui as Roles e não concede acesso por si só."
    )
    st.write(f"**Credencial configurada:** {usuario['credencial_configurada'] or 'não'}")
    st.write(f"**Exige troca de senha:** {usuario['exige_troca_senha'] or 'não'}")
    st.caption(
        "Os campos de credencial e troca de senha estão reservados ao futuro ciclo "
        "de autenticação operacional e ainda não possuem efeito funcional."
    )
    historico = associacoes[
        associacoes["usuario_id"].astype(str) == str(usuario["usuario_id"])
    ]
    if not historico.empty:
        with st.expander("Dados técnicos das associações"):
            st.dataframe(historico, use_container_width=True, hide_index=True)


def _render_auditoria_usuario(usuario, associacoes):
    st.markdown("### Auditoria")
    st.write(f"**Criado em:** {usuario['criado_em'] or 'não informado'}")
    st.write(f"**Criado por:** {usuario['criado_por'] or 'não informado'}")
    st.write(f"**Última atualização:** {usuario['atualizado_em'] or 'não informada'}")
    st.write(f"**Atualizado por:** {usuario['atualizado_por'] or 'não informado'}")
    historico = associacoes[
        associacoes["usuario_id"].astype(str) == str(usuario["usuario_id"])
    ]
    if not historico.empty:
        with st.expander("Histórico técnico das funções"):
            st.dataframe(historico, use_container_width=True, hide_index=True)


def _render_usuarios():
    st.subheader("Pessoas e acesso")
    st.caption("Selecione uma pessoa para administrar cadastro, funções e acesso no mesmo contexto.")
    leituras = {
        "usuarios": carregar_usuarios_operacionais_resultado(),
        "associacoes": carregar_usuarios_roles_resultado(),
        "roles": carregar_roles_resultado(),
        "matriz": carregar_roles_permissoes_resultado(),
        "catalogo": carregar_catalogo_resultado(),
        "atuais": carregar_permissoes_resultado(),
    }
    _render_criacao_usuario(leituras["usuarios"])
    if not all(item.leitura_confirmada for item in leituras.values()):
        st.error(
            "Leitura bloqueada. A ficha e suas ações só ficam disponíveis quando "
            "todas as fontes de identidade e acesso são confirmadas."
        )
        return

    usuarios = leituras["usuarios"].dados.copy()
    if usuarios.empty:
        st.info("Nenhum usuário operacional cadastrado.")
        return

    filtro = st.radio("Mostrar", ("Todos", "Ativos", "Inativos"), horizontal=True)
    filtrados = usuarios
    if filtro == "Ativos":
        filtrados = usuarios[usuarios["ativo"].astype(str).str.casefold() == "sim"]
    elif filtro == "Inativos":
        filtrados = usuarios[usuarios["ativo"].astype(str).str.casefold() != "sim"]
    busca = st.text_input("Buscar por nome, login ou matrícula")
    if busca.strip():
        termo = busca.strip().casefold()
        mascara = filtrados[["nome", "login", "matricula"]].astype(str).apply(
            lambda coluna: coluna.str.casefold().str.contains(termo, regex=False)
        ).any(axis=1)
        filtrados = filtrados[mascara]
    if filtrados.empty:
        st.info("Nenhum usuário corresponde aos filtros.")
        return

    resumo = filtrados[["nome", "login", "matricula", "ativo"]].copy()
    resumo["ativo"] = resumo["ativo"].map(
        {"sim": "Ativo", "nao": "Inativo"}
    ).fillna("Estado desconhecido")
    resumo = resumo.rename(columns={
        "nome": "Nome", "login": "Login", "matricula": "Matrícula",
        "ativo": "Estado",
    })
    st.caption(
        "Entenda as colunas: Login identifica o cadastro, mas ainda não autentica; "
        "Estado informa apenas se o registro operacional está ativo."
    )
    st.dataframe(
        resumo, use_container_width=True, hide_index=True,
        column_config={
            "Nome": st.column_config.TextColumn("Usuário", help=AJUDA_COLUNAS["Usuário"]),
            "Login": st.column_config.TextColumn("Login", help=AJUDA_COLUNAS["Login"]),
            "Estado": st.column_config.TextColumn("Cadastro", help=AJUDA_COLUNAS["Cadastro"]),
        },
    )

    opcoes = {
        f"{row['nome']} — {row['login']} — {'ativo' if str(row['ativo']).casefold() == 'sim' else 'inativo'}": row["usuario_id"]
        for _, row in filtrados.iterrows()
    }
    escolhido = st.selectbox("Usuário selecionado", list(opcoes), key="usuario_ficha")
    usuario_id = opcoes[escolhido]
    usuario = usuarios[usuarios["usuario_id"].astype(str) == str(usuario_id)].iloc[0]

    st.divider()
    st.header(usuario["nome"] or usuario["login"])
    st.caption(f"Login: {usuario['login']} · Matrícula: {usuario['matricula']}")
    _render_resumo_usuario(usuario, leituras)
    secao = st.radio(
        "Seção da ficha",
        ("Visão geral", "Funções", "Acesso", "Histórico", "Detalhes técnicos"),
        horizontal=True,
        key=f"secao_ficha_{usuario_id}",
        help="Navegue pela ficha sem selecionar a pessoa novamente.",
    )
    st.divider()
    if secao == "Visão geral":
        _render_identidade_usuario(usuario, leituras["usuarios"])
        st.markdown("### Estado e ações principais")
        _render_estado_usuario(usuario, leituras["usuarios"])
    elif secao == "Funções":
        _render_roles_usuario(usuario, leituras)
    elif secao == "Acesso":
        _render_acesso_usuario(usuario, leituras)
    elif secao == "Histórico":
        _render_auditoria_usuario(usuario, leituras["associacoes"].dados)
    else:
        _render_detalhes_usuario(usuario, leituras["associacoes"].dados)
    st.info(
        "Contas protegidas permanecem exclusivamente em APP_USERS e não são "
        "editáveis nesta interface. A exclusão física não está disponível."
    )


def _render_diagnostico_rbac():
    st.subheader("DIAGNÓSTICO RBAC")
    st.caption(
        "Shadow Mode compara o acesso em uso hoje com o modelo por Roles em "
        "preparação, sem liberar ou bloquear qualquer operação."
    )
    leituras = {
        "usuarios": carregar_usuarios_operacionais_resultado(),
        "associacoes": carregar_usuarios_roles_resultado(),
        "roles": carregar_roles_resultado(),
        "matriz": carregar_roles_permissoes_resultado(),
        "catalogo": carregar_catalogo_resultado(),
        "atuais": carregar_permissoes_resultado(),
    }
    if not all(item.leitura_confirmada for item in leituras.values()):
        st.error("Diagnóstico indisponível: todas as fontes exigem leitura confirmada.")
        st.divider()
        return

    diagnosticos = diagnosticar_usuarios(
        usuarios=leituras["usuarios"].dados,
        associacoes=leituras["associacoes"].dados,
        roles=leituras["roles"].dados,
        roles_permissoes=leituras["matriz"].dados,
        catalogo_permissoes=leituras["catalogo"].dados,
        permissoes_atuais=leituras["atuais"].dados,
    )
    if not diagnosticos:
        st.info("Nenhum usuário operacional disponível para comparação.")
        st.divider()
        return

    linhas = [{
        "Usuário": item.nome or item.login,
        "Login": item.login,
        "Roles": ", ".join(item.roles) or "—",
        "Permissões atuais": len(item.permissoes_atuais),
        "Permissões pelas Roles": len(item.permissoes_rbac),
        "O novo modelo concederia": "\n".join(
            _linhas_permissoes(item.rbac_a_mais)
        ) or "—",
        "O acesso atual possui, mas as Roles não concedem": "\n".join(
            _linhas_permissoes(item.rbac_a_menos)
        ) or "—",
        "Status": _status_diagnostico(item.status),
    } for item in diagnosticos]
    st.caption(
        "Passe o cursor sobre os cabeçalhos para entender o efeito atual de cada coluna."
    )
    st.dataframe(
        pd.DataFrame(linhas), use_container_width=True, hide_index=True,
        column_config={
            "Usuário": st.column_config.TextColumn("Usuário", help=AJUDA_COLUNAS["Usuário"]),
            "Login": st.column_config.TextColumn("Login", help=AJUDA_COLUNAS["Login"]),
            "Roles": st.column_config.TextColumn("Role / função", help=AJUDA_COLUNAS["Role / função"]),
            "Permissões atuais": st.column_config.NumberColumn(
                "Permissões atuais", help=AJUDA_COLUNAS["Permissões atuais"]
            ),
            "Permissões pelas Roles": st.column_config.NumberColumn(
                "Permissões pelas Roles", help=AJUDA_COLUNAS["Permissões pelas Roles"]
            ),
            "O novo modelo concederia": st.column_config.TextColumn(
                "O novo modelo concederia", help=AJUDA_COLUNAS["O novo modelo concederia"]
            ),
            "O acesso atual possui, mas as Roles não concedem": st.column_config.TextColumn(
                "O acesso atual possui, mas as Roles não concedem",
                help=AJUDA_COLUNAS["O acesso atual possui, mas as Roles não concedem"],
            ),
            "Status": st.column_config.TextColumn(
                "Status da comparação", help=AJUDA_COLUNAS["Status da comparação"]
            ),
        },
    )
    divergentes = sum(item.status != "IGUAL" for item in diagnosticos)
    st.caption(
        f"{len(diagnosticos)} usuário(s) comparado(s); "
        f"{divergentes} diagnóstico(s) diferente(s) de IGUAL."
    )
    st.info("Esta seção é exclusivamente diagnóstica e não permite alterações.")
    st.divider()


def _render_permissoes_legadas():
    st.subheader("Modelo de acesso em uso hoje")
    st.caption(
        "Estas são as permissões efetivas atuais e continuam sendo a fonte da "
        "autorização enquanto o RBAC permanece em modo de diagnóstico."
    )
    resultado_leitura = carregar_permissoes_resultado()
    df = resultado_leitura.dados
    persistencia_liberada = resultado_leitura.pode_sobrescrever

    if not persistencia_liberada:
        _mostrar_erro_leitura(resultado_leitura)

    st.markdown("#### Permissões cadastradas")

    if df.empty:
        if persistencia_liberada:
            st.info("Nenhuma permissão cadastrada ainda.")
        else:
            st.info("A lista não está disponível porque a leitura não foi confirmada.")
    else:
        exibicao = df.rename(columns={
            "usuario": "Usuário", "modulo": "Módulo", "recurso": "Recurso",
            "permissao": "Permissão", "obra_id": "Escopo da obra", "ativo": "Ativa",
        })
        st.caption(
            "Escopo da obra indica onde a autorização vale; 'todas' significa "
            "ausência de restrição por obra. Ativa informa se a regra está em uso."
        )
        st.dataframe(
            exibicao, use_container_width=True, hide_index=True,
            column_config={
                "Usuário": st.column_config.TextColumn("Usuário", help=AJUDA_COLUNAS["Usuário"]),
                "Módulo": st.column_config.TextColumn("Módulo", help="Área funcional autorizada por esta regra efetiva."),
                "Recurso": st.column_config.TextColumn("Recurso", help="Objeto sobre o qual a autorização efetiva se aplica."),
                "Permissão": st.column_config.TextColumn("Permissão", help=AJUDA_COLUNAS["Permissões atuais"]),
                "Escopo da obra": st.column_config.TextColumn("Escopo da obra", help="Obra específica ou 'todas' quando não há restrição por obra."),
                "Ativa": st.column_config.TextColumn("Ativa", help="Indica se a regra participa da autorização efetiva atual."),
            },
        )

    st.divider()

    edicao_habilitada = st.checkbox(
        "Habilitar alterações nas permissões efetivas atuais",
        help="Mantenha desmarcado para consultar sem risco de edição acidental.",
    )
    escrita_liberada = persistencia_liberada and edicao_habilitada
    if not edicao_habilitada:
        st.info("Modo consulta. Marque a opção acima somente quando precisar alterar o acesso atual.")

    st.markdown("#### Adicionar nova permissão")

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

    st.markdown("#### Remover / desativar permissões")

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


def render():
    if st.button("← Voltar ao menu inicial", key="administracao_voltar_menu"):
        st.session_state.tela = "menu"
        st.rerun()

    st.title("Administração de acesso")
    st.caption("Gerencie pessoas, funções e permissões do APP.")

    if not pode_gerenciar_administracao():
        st.error("Acesso restrito à custódia administrativa.")
        st.stop()

    _render_ajuda_controle_acesso()
    col_atual, col_novo = st.columns(2)
    col_atual.info(
        "**ACESSO EM USO HOJE**\n\nAPP_USERS autentica as contas protegidas e "
        "as permissões efetivas atuais controlam a autorização."
    )
    col_novo.warning(
        "**NOVO MODELO POR ROLES — EM PREPARAÇÃO**\n\nUsuários operacionais, "
        "Roles e Shadow Mode ainda não alteram o acesso real."
    )

    usuarios, roles, permissoes, diagnostico, avancado = st.tabs([
        "USUÁRIOS", "ROLES", "PERMISSÕES RBAC", "DIAGNÓSTICO", "ACESSO ATUAL",
    ])
    with usuarios:
        _render_usuarios()
    with roles:
        _render_roles()
    with permissoes:
        _render_catalogo_permissoes()
    with diagnostico:
        _render_diagnostico_rbac()
    with avancado:
        st.info(
            "Modelo efetivo em uso hoje. A consulta é segura; alterações exigem "
            "habilitação explícita dentro da seção."
        )
        _render_permissoes_legadas()
