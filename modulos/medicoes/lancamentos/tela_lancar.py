import streamlit as st

from modulos.medicoes.repositorio import (
    carregar_bases,
    carregar_tabela_contrato,
)

from modulos.medicoes.lancamentos.repositorio import (
    carregar_usuarios_obras,
    listar_locais_por_obra,
)

from modulos.medicoes.lancamentos.servicos import criar_lancamento_trabalho


def _obter_usuario_logado():
    for chave in [
        "email",
        "usuario_email",
        "user_email",
        "usuario_logado",
        "usuario",
        "login",
    ]:
        valor = st.session_state.get(chave)

        if isinstance(valor, dict):
            email = valor.get("email") or valor.get("usuario") or valor.get("login")
            if email:
                return str(email).strip().lower()

        if isinstance(valor, str) and valor.strip():
            return valor.strip().lower()

    return ""


def _obter_nome_obra(linha_obra):
    for coluna in ["nome_obra", "obra_nome", "nome", "descricao"]:
        if coluna in linha_obra and linha_obra[coluna]:
            return linha_obra[coluna]

    return linha_obra.get("obra_id", "Obra sem nome")


def _filtrar_obras_por_usuario(obras):
    email_usuario = _obter_usuario_logado()

    if not email_usuario:
        st.warning(
            "Não consegui identificar o usuário logado. "
            "Por segurança, nenhuma obra foi liberada para lançamento."
        )
        return obras.iloc[0:0].copy(), email_usuario, ""

    usuarios_obras = carregar_usuarios_obras()

    if usuarios_obras.empty:
        st.warning("Nenhum vínculo usuário/obra cadastrado.")
        return obras.iloc[0:0].copy(), email_usuario, ""

    usuarios_obras = usuarios_obras.fillna("").copy()

    for coluna in [
        "usuario_id",
        "email",
        "nome",
        "perfil_medicao",
        "ativo",
        "obra_id",
    ]:
        if coluna not in usuarios_obras.columns:
            usuarios_obras[coluna] = ""

        usuarios_obras[coluna] = (
            usuarios_obras[coluna]
            .astype(str)
            .str.strip()
            .str.lower()
        )

    vinculos = usuarios_obras[
        (
            (usuarios_obras["usuario_id"] == email_usuario)
            | (usuarios_obras["email"] == email_usuario)
            | (usuarios_obras["nome"] == email_usuario)
        )
        & (
            usuarios_obras["ativo"].isin(
                ["sim", "s", "true", "1", "ativo"]
            )
        )
    ].copy()

    if vinculos.empty:
        st.warning(f"O usuário {email_usuario} não possui obra ativa vinculada.")
        return obras.iloc[0:0].copy(), email_usuario, ""

    perfil = vinculos["perfil_medicao"].iloc[0].strip().lower()

    if perfil in ["admin", "aprovador"]:
        return obras.copy(), email_usuario, perfil

    obras_permitidas = vinculos["obra_id"].dropna().astype(str).tolist()

    obras_filtradas = obras[
        obras["obra_id"]
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(obras_permitidas)
    ].copy()

    return obras_filtradas, email_usuario, perfil


def _filtrar_servicos_ativos(servicos_obra):
    if "ativo" not in servicos_obra.columns:
        return servicos_obra

    return servicos_obra[
        servicos_obra["ativo"]
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["sim", "s", "true", "1", "ativo", ""])
    ].copy()


def _montar_label_servico(row):
    codigo = row.get("codigo", "")
    descricao = row.get("descricao", "")
    unidade = row.get("unidade", "")

    return f"{codigo} - {descricao} ({unidade})"


def _selecionar_local_trabalho(obra_id):
    st.markdown("### Local de trabalho")

    locais_df = listar_locais_por_obra(obra_id)

    if locais_df.empty:
        st.warning(
            "Esta obra não possui locais cadastrados. "
            "Solicite ao administrador o cadastro dos locais."
        )
        return "", ""

    locais_df = locais_df.fillna("").copy()

    local_escolhido = st.selectbox(
        "Local de Trabalho",
        options=locais_df["nome_local"].tolist(),
        key=f"lancamento_local_{obra_id}",
    )

    linha_local = locais_df[
        locais_df["nome_local"] == local_escolhido
    ].iloc[0]

    local_id = linha_local["local_id"]
    nome_local = linha_local["nome_local"]

    return local_id, nome_local


def tela_lancar_producao():
    st.markdown("## 📝 Lançar Trabalho Executado")
    st.caption(
        "Registre serviços executados em campo. "
        "Este lançamento ainda não está vinculado a nenhuma medição."
    )

    if st.button(
        "⬅ Voltar ao início das Medições",
        use_container_width=True,
        key="btn_voltar_inicio_lancar_producao",
    ):
        st.session_state["fluxo_medicoes"] = "inicio"
        st.rerun()

    st.divider()

    (
        obras,
        medicoes_df,
        frentes,
        mc,
        itens,
        servicos_genericos,
    ) = carregar_bases()

    if obras.empty:
        st.warning("Nenhuma obra cadastrada.")
        return

    obras = obras.fillna("").copy()

    obras, email_usuario, perfil_usuario = _filtrar_obras_por_usuario(obras)

    if obras.empty:
        return

    st.caption(
        f"Usuário: {email_usuario} | Perfil: {perfil_usuario or 'não identificado'}"
    )

    obras["label_obra"] = obras.apply(
        lambda row: f"{row.get('obra_id', '')} - {_obter_nome_obra(row)}",
        axis=1,
    )

    if len(obras) == 1:
        obra_selecionada = obras.iloc[0]
        st.info(f"Obra vinculada: {obra_selecionada['label_obra']}")
    else:
        label_obra = st.selectbox(
            "Obra",
            options=obras["label_obra"].tolist(),
            key="lancamento_obra_label",
        )

        obra_selecionada = obras[obras["label_obra"] == label_obra].iloc[0]

    obra_id = obra_selecionada["obra_id"]
    nome_obra = _obter_nome_obra(obra_selecionada)

    st.info(
        "O lançamento será salvo como evidência operacional. "
        "A vinculação com medição será feita depois."
    )

    st.divider()

    local_id, nome_local = _selecionar_local_trabalho(obra_id)

    st.divider()

    st.markdown("### Item contratual")

    arquivo_tabela = obra_selecionada.get("arquivo_tabela_servicos", "")

    if not arquivo_tabela:
        st.warning("Esta obra não possui tabela contratual vinculada.")
        return

    servicos_obra = carregar_tabela_contrato(arquivo_tabela)

    if servicos_obra.empty:
        st.warning("A tabela contratual da obra está vazia ou não foi encontrada.")
        return

    servicos_obra = servicos_obra.fillna("").copy()
    servicos_obra = _filtrar_servicos_ativos(servicos_obra)

    if servicos_obra.empty:
        st.warning("Nenhum item contratual ativo encontrado para esta obra.")
        return

    servicos_obra["label_servico"] = servicos_obra.apply(
        _montar_label_servico,
        axis=1,
    )

    label_servico = st.selectbox(
        "Serviço executado",
        options=servicos_obra["label_servico"].tolist(),
        key="lancamento_servico_label",
    )

    servico_selecionado = servicos_obra[
        servicos_obra["label_servico"] == label_servico
    ].iloc[0]

    codigo_item = servico_selecionado.get("codigo", "")
    descricao_item = servico_selecionado.get("descricao", "")
    unidade = servico_selecionado.get("unidade", "")
    item_id = codigo_item

    st.markdown("### Quantidade e data")

    col1, col2 = st.columns(2)

    with col1:
        quantidade_executada = st.number_input(
            f"Quantidade executada ({unidade})",
            min_value=0.0,
            step=0.01,
            key="lancamento_quantidade_executada",
        )

    with col2:
        data_servico = st.date_input(
            "Data do serviço",
            key="lancamento_data_servico",
        )

    observacao = st.text_area(
        "Observação opcional",
        placeholder=(
            "Ex.: serviço executado parcialmente, aguardando conferência, "
            "condição do local, etc."
        ),
        key="lancamento_observacao",
    )

    foto = st.file_uploader(
        "Foto comprobatória",
        type=["png", "jpg", "jpeg"],
        key="lancamento_foto",
    )

    foto_url = ""

    if foto:
        st.caption(
            "Foto carregada na tela. Próximo passo: salvar o arquivo no GitHub."
        )
        foto_url = foto.name

    st.divider()

    if st.button(
        "💾 Salvar lançamento",
        use_container_width=True,
        key="btn_salvar_lancamento_trabalho",
    ):
        if not nome_local:
            st.error("Selecione um local de trabalho.")
            return

        if quantidade_executada <= 0:
            st.error("Informe uma quantidade executada maior que zero.")
            return

        novo = criar_lancamento_trabalho(
            obra_id=obra_id,
            nome_obra=nome_obra,
            local_id=local_id,
            nome_local=nome_local,
            item_id=item_id,
            codigo_item=codigo_item,
            descricao_item=descricao_item,
            unidade=unidade,
            quantidade_executada=quantidade_executada,
            data_servico=data_servico,
            observacao=observacao,
            foto_url=foto_url,
            criado_por=email_usuario,
        )

        st.success(f"Lançamento salvo com sucesso: {novo['lancamento_id']}")
