import streamlit as st

from pages.crm.config import (
    TIPOS_CLIENTE,
    STATUS_RELACIONAMENTO,
    ORIGENS_CLIENTE,
    TIPOS_CONTATO,
    RESULTADOS_INTERACAO,
)
from pages.crm.repositorio import (
    carregar_clientes,
    carregar_contatos,
    cadastrar_cliente,
    atualizar_cliente,
    cadastrar_contato,
    atualizar_contato,
    cadastro_interacao_liberado,
    cadastrar_interacao_composta,
    carregar_contexto_interacao_resultado,
)
from pages.crm.utils import filtrar_dataframe, preparar_dataframe_para_exibicao


def novo_cliente():
    st.subheader("Nova empresa / cliente")
    with st.form("crm_novo_cliente_puro"):
        col1, col2 = st.columns(2)
        with col1:
            nome_empresa = st.text_input("Nome da empresa *")
            tipo_cliente = st.selectbox("Tipo de cliente", TIPOS_CLIENTE)
            documento = st.text_input("Documento / CNPJ")
            cidade = st.text_input("Cidade")
            estado = st.text_input("Estado")
        with col2:
            endereco_local = st.text_input("Endereço / Local")
            setor_atividade = st.text_input("Setor de atividade")
            origem_cliente = st.selectbox("Origem do cliente", ORIGENS_CLIENTE)
            status_relacionamento = st.selectbox("Status do relacionamento", STATUS_RELACIONAMENTO)
            responsavel = st.text_input("Responsável pelo atendimento")
        necessidade_cliente = st.text_area("Necessidade do cliente")
        proxima_acao = st.text_input("Próxima ação")
        data_proxima_acao = st.date_input("Data da próxima ação", value=None)
        observacoes_gerais = st.text_area("Observações gerais")
        salvar = st.form_submit_button("Salvar cliente")
        if salvar:
            if not nome_empresa.strip():
                st.error("Informe o nome da empresa.")
                return
            cadastrar_cliente({
                "nome_empresa": nome_empresa.strip(),
                "tipo_cliente": tipo_cliente,
                "documento": documento.strip(),
                "cidade": cidade.strip(),
                "estado": estado.strip(),
                "endereco_local": endereco_local.strip(),
                "setor_atividade": setor_atividade.strip(),
                "origem_cliente": origem_cliente,
                "status_relacionamento": status_relacionamento,
                "responsavel": responsavel.strip(),
                "necessidade_cliente": necessidade_cliente.strip(),
                "ultimo_contato": "",
                "proxima_acao": proxima_acao.strip(),
                "data_proxima_acao": str(data_proxima_acao) if data_proxima_acao else "",
                "observacoes_gerais": observacoes_gerais.strip(),
            })
            st.success("Cliente cadastrado com sucesso.")
            st.rerun()


def novo_contato():
    st.subheader("Novo contato de pessoa")
    clientes = carregar_clientes()
    if clientes.empty:
        st.warning("Cadastre pelo menos um cliente antes de cadastrar contatos.")
        return
    clientes_opcoes = {row["nome_empresa"]: row["id_cliente"] for _, row in clientes.sort_values("nome_empresa").iterrows()}
    with st.form("crm_novo_contato_puro"):
        cliente_nome = st.selectbox("Cliente / Empresa", list(clientes_opcoes.keys()))
        id_cliente = clientes_opcoes[cliente_nome]
        col1, col2 = st.columns(2)
        with col1:
            nome_contato = st.text_input("Nome do contato *")
            cargo = st.text_input("Cargo")
            telefone = st.text_input("Telefone")
        with col2:
            whatsapp = st.text_input("WhatsApp")
            email = st.text_input("Email")
            contato_principal = st.checkbox("Contato principal")
        observacoes = st.text_area("Observações")
        salvar = st.form_submit_button("Salvar contato")
        if salvar:
            if not nome_contato.strip():
                st.error("Informe o nome do contato.")
                return
            cadastrar_contato({
                "id_cliente": id_cliente,
                "nome_contato": nome_contato.strip(),
                "cargo": cargo.strip(),
                "telefone": telefone.strip(),
                "whatsapp": whatsapp.strip(),
                "email": email.strip(),
                "contato_principal": "Sim" if contato_principal else "Não",
                "observacoes": observacoes.strip(),
            })
            st.success("Contato cadastrado com sucesso.")
            st.rerun()


def nova_interacao():
    st.subheader("Nova interação")
    resultado_clientes, resultado_interacoes, snapshot_comum = carregar_contexto_interacao_resultado()
    clientes = resultado_clientes.dados
    contatos = carregar_contatos()
    if clientes.empty:
        st.warning("Cadastre pelo menos um cliente antes de registrar interações.")
        return
    clientes_opcoes = {row["nome_empresa"]: row["id_cliente"] for _, row in clientes.sort_values("nome_empresa").iterrows()}
    liberado = cadastro_interacao_liberado(resultado_clientes, resultado_interacoes, snapshot_comum)
    if not liberado:
        st.error("O cadastro de interação está temporariamente bloqueado para preservar os dados.")
    with st.form("crm_nova_interacao_pura"):
        cliente_nome = st.selectbox("Cliente / Empresa", list(clientes_opcoes.keys()))
        id_cliente = clientes_opcoes[cliente_nome]
        contatos_cliente = contatos[contatos["id_cliente"] == id_cliente].copy()
        opcoes_contato = {"Sem contato específico": ""}
        for _, row in contatos_cliente.iterrows():
            opcoes_contato[row["nome_contato"]] = row["id_contato"]
        contato_nome = st.selectbox("Contato", list(opcoes_contato.keys()))
        col1, col2 = st.columns(2)
        with col1:
            data_interacao = st.date_input("Data da interação")
            tipo_contato = st.selectbox("Tipo de contato", TIPOS_CONTATO)
            responsavel = st.text_input("Responsável")
        with col2:
            resultado = st.selectbox("Resultado", RESULTADOS_INTERACAO)
            proxima_acao = st.text_input("Próxima ação")
            data_proxima_acao = st.date_input("Data da próxima ação", value=None)
        descricao = st.text_area("Descrição da interação *")
        salvar = st.form_submit_button("Salvar interação", disabled=not liberado)
        if salvar:
            if not descricao.strip():
                st.error("Informe a descrição da interação.")
                return
            retorno = cadastrar_interacao_composta({
                "id_cliente": id_cliente,
                "id_contato": opcoes_contato[contato_nome],
                "data_interacao": str(data_interacao),
                "tipo_contato": tipo_contato,
                "descricao": descricao.strip(),
                "responsavel": responsavel.strip(),
                "resultado": resultado,
                "proxima_acao": proxima_acao.strip(),
                "data_proxima_acao": str(data_proxima_acao) if data_proxima_acao else "",
            }, resultado_clientes, resultado_interacoes, snapshot_comum)
            if retorno.sucesso:
                st.success("Interação registrada com sucesso.")
                st.rerun()
            st.error(retorno.erro or "Não foi possível registrar a interação.")


def consultar_clientes():
    st.subheader("Consultar clientes / empresas")
    clientes = carregar_clientes()
    if clientes.empty:
        st.info("Nenhum cliente cadastrado.")
        return
    busca = st.text_input("Buscar cliente", placeholder="Empresa, cidade, responsável, status...")
    df = filtrar_dataframe(clientes, busca, ["nome_empresa", "cidade", "estado", "responsavel", "status_relacionamento", "necessidade_cliente", "observacoes_gerais"])
    st.dataframe(preparar_dataframe_para_exibicao(df), use_container_width=True, hide_index=True)


def consultar_contatos():
    st.subheader("Consultar contatos")
    clientes = carregar_clientes()
    contatos = carregar_contatos()
    if contatos.empty:
        st.info("Nenhum contato cadastrado.")
        return
    df = contatos.merge(clientes[["id_cliente", "nome_empresa"]], on="id_cliente", how="left") if not clientes.empty else contatos.copy()
    busca = st.text_input("Buscar contato", placeholder="Nome, empresa, telefone, email...")
    df = filtrar_dataframe(df, busca, [c for c in ["nome_empresa", "nome_contato", "cargo", "telefone", "whatsapp", "email", "observacoes"] if c in df.columns])
    st.dataframe(preparar_dataframe_para_exibicao(df), use_container_width=True, hide_index=True)


def consultar_interacoes():
    st.subheader("Consultar interações")
    resultado_clientes, resultado_interacoes, _ = carregar_contexto_interacao_resultado()
    clientes = resultado_clientes.dados
    interacoes = resultado_interacoes.dados
    contatos = carregar_contatos()
    if interacoes.empty:
        st.info("Nenhuma interação registrada.")
        return
    df = interacoes.merge(clientes[["id_cliente", "nome_empresa"]], on="id_cliente", how="left")
    if not contatos.empty:
        df = df.merge(contatos[["id_contato", "nome_contato"]], on="id_contato", how="left")
    df = df.sort_values("data_interacao", ascending=False)
    st.dataframe(preparar_dataframe_para_exibicao(df), use_container_width=True, hide_index=True)


def atualizar_cliente_tela():
    st.subheader("Atualizar cliente / empresa")
    clientes = carregar_clientes()
    if clientes.empty:
        st.info("Nenhum cliente cadastrado.")
        return
    busca = st.text_input("Localizar cliente", placeholder="Digite parte do nome da empresa")
    df = filtrar_dataframe(clientes, busca, ["nome_empresa", "cidade", "responsavel"])
    if df.empty:
        st.info("Nenhum cliente encontrado.")
        return
    nome = st.selectbox("Selecione o cliente", df["nome_empresa"].tolist())
    cliente = df[df["nome_empresa"] == nome].iloc[0]
    with st.form("crm_atualizar_cliente_puro"):
        col1, col2 = st.columns(2)
        with col1:
            nome_empresa = st.text_input("Nome da empresa", value=cliente["nome_empresa"])
            tipo_cliente = st.selectbox("Tipo de cliente", TIPOS_CLIENTE, index=TIPOS_CLIENTE.index(cliente["tipo_cliente"]) if cliente["tipo_cliente"] in TIPOS_CLIENTE else 0)
            documento = st.text_input("Documento / CNPJ", value=cliente["documento"])
            cidade = st.text_input("Cidade", value=cliente["cidade"])
            estado = st.text_input("Estado", value=cliente["estado"])
        with col2:
            endereco_local = st.text_input("Endereço / Local", value=cliente["endereco_local"])
            setor_atividade = st.text_input("Setor de atividade", value=cliente["setor_atividade"])
            origem_cliente = st.selectbox("Origem do cliente", ORIGENS_CLIENTE, index=ORIGENS_CLIENTE.index(cliente["origem_cliente"]) if cliente["origem_cliente"] in ORIGENS_CLIENTE else 0)
            status_relacionamento = st.selectbox("Status do relacionamento", STATUS_RELACIONAMENTO, index=STATUS_RELACIONAMENTO.index(cliente["status_relacionamento"]) if cliente["status_relacionamento"] in STATUS_RELACIONAMENTO else 0)
            responsavel = st.text_input("Responsável pelo atendimento", value=cliente["responsavel"])
        necessidade_cliente = st.text_area("Necessidade do cliente", value=cliente["necessidade_cliente"])
        proxima_acao = st.text_input("Próxima ação", value=cliente["proxima_acao"])
        data_proxima_acao = st.text_input("Data da próxima ação", value=cliente["data_proxima_acao"])
        observacoes_gerais = st.text_area("Observações gerais", value=cliente["observacoes_gerais"])
        if st.form_submit_button("Atualizar cliente"):
            atualizar_cliente(cliente["id_cliente"], {"nome_empresa": nome_empresa.strip(), "tipo_cliente": tipo_cliente, "documento": documento.strip(), "cidade": cidade.strip(), "estado": estado.strip(), "endereco_local": endereco_local.strip(), "setor_atividade": setor_atividade.strip(), "origem_cliente": origem_cliente, "status_relacionamento": status_relacionamento, "responsavel": responsavel.strip(), "necessidade_cliente": necessidade_cliente.strip(), "proxima_acao": proxima_acao.strip(), "data_proxima_acao": data_proxima_acao.strip(), "observacoes_gerais": observacoes_gerais.strip()})
            st.success("Cliente atualizado com sucesso.")
            st.rerun()


def atualizar_contato_tela():
    st.subheader("Atualizar contato")
    clientes = carregar_clientes()
    contatos = carregar_contatos()
    if contatos.empty or clientes.empty:
        st.info("Nenhum contato disponível para atualização.")
        return
    clientes_opcoes = {row["nome_empresa"]: row["id_cliente"] for _, row in clientes.sort_values("nome_empresa").iterrows()}
    df = contatos.merge(clientes[["id_cliente", "nome_empresa"]], on="id_cliente", how="left")
    busca = st.text_input("Localizar contato", placeholder="Nome, empresa, telefone ou email")
    df = filtrar_dataframe(df, busca, ["nome_contato", "nome_empresa", "telefone", "email"])
    if df.empty:
        st.info("Nenhum contato encontrado.")
        return
    df = df.copy()
    df["label"] = df["nome_contato"].fillna("") + " - " + df["nome_empresa"].fillna("")
    label = st.selectbox("Selecione o contato", df["label"].tolist())
    contato = df[df["label"] == label].iloc[0]
    with st.form("crm_atualizar_contato_puro"):
        nomes = list(clientes_opcoes.keys())
        cliente_nome = st.selectbox("Cliente / Empresa", nomes, index=nomes.index(contato["nome_empresa"]) if contato["nome_empresa"] in nomes else 0)
        col1, col2 = st.columns(2)
        with col1:
            nome_contato = st.text_input("Nome do contato", value=contato["nome_contato"])
            cargo = st.text_input("Cargo", value=contato["cargo"])
            telefone = st.text_input("Telefone", value=contato["telefone"])
        with col2:
            whatsapp = st.text_input("WhatsApp", value=contato["whatsapp"])
            email = st.text_input("Email", value=contato["email"])
            contato_principal = st.checkbox("Contato principal", value=contato["contato_principal"] == "Sim")
        observacoes = st.text_area("Observações", value=contato["observacoes"])
        if st.form_submit_button("Atualizar contato"):
            atualizar_contato(contato["id_contato"], {"id_cliente": clientes_opcoes[cliente_nome], "nome_contato": nome_contato.strip(), "cargo": cargo.strip(), "telefone": telefone.strip(), "whatsapp": whatsapp.strip(), "email": email.strip(), "contato_principal": "Sim" if contato_principal else "Não", "observacoes": observacoes.strip()})
            st.success("Contato atualizado com sucesso.")
            st.rerun()
