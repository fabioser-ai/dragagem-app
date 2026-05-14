import streamlit as st
import pandas as pd

from pages.crm.config import (
    TIPOS_CLIENTE,
    STATUS_RELACIONAMENTO,
    ORIGENS_CLIENTE,
)
from pages.crm.repositorio import (
    carregar_clientes,
    cadastrar_cliente,
    atualizar_cliente,
)
from pages.crm.utils import filtrar_dataframe, preparar_dataframe_para_exibicao


def tela_clientes():
    st.subheader("Cadastro de Clientes / Empresas")

    clientes = carregar_clientes()

    with st.expander("Novo cliente", expanded=False):
        with st.form("form_novo_cliente"):
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
                else:
                    dados = {
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
                    }

                    cadastrar_cliente(dados)
                    st.success("Cliente cadastrado com sucesso.")
                    st.rerun()

    st.markdown("---")
    st.subheader("Clientes cadastrados")

    busca = st.text_input("Buscar cliente", placeholder="Digite empresa, cidade, responsável, status...")

    clientes_filtrados = filtrar_dataframe(
        clientes,
        busca,
        [
            "nome_empresa",
            "cidade",
            "estado",
            "responsavel",
            "status_relacionamento",
            "necessidade_cliente",
            "observacoes_gerais",
        ],
    )

    if clientes_filtrados.empty:
        st.info("Nenhum cliente cadastrado ou encontrado.")
        return

    col1, col2, col3 = st.columns(3)

    with col1:
        status_filtro = st.selectbox(
            "Filtrar por status",
            ["Todos"] + sorted(clientes_filtrados["status_relacionamento"].dropna().unique().tolist()),
        )

    with col2:
        estado_filtro = st.selectbox(
            "Filtrar por estado",
            ["Todos"] + sorted(clientes_filtrados["estado"].dropna().unique().tolist()),
        )

    with col3:
        responsavel_filtro = st.selectbox(
            "Filtrar por responsável",
            ["Todos"] + sorted(clientes_filtrados["responsavel"].dropna().unique().tolist()),
        )

    if status_filtro != "Todos":
        clientes_filtrados = clientes_filtrados[clientes_filtrados["status_relacionamento"] == status_filtro]

    if estado_filtro != "Todos":
        clientes_filtrados = clientes_filtrados[clientes_filtrados["estado"] == estado_filtro]

    if responsavel_filtro != "Todos":
        clientes_filtrados = clientes_filtrados[clientes_filtrados["responsavel"] == responsavel_filtro]

    st.dataframe(
        preparar_dataframe_para_exibicao(
            clientes_filtrados[
                [
                    "nome_empresa",
                    "cidade",
                    "estado",
                    "status_relacionamento",
                    "responsavel",
                    "ultimo_contato",
                    "proxima_acao",
                    "data_proxima_acao",
                ]
            ]
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")
    st.subheader("Editar cliente")

    opcoes = clientes_filtrados["nome_empresa"].tolist()

    cliente_nome = st.selectbox("Selecione o cliente", opcoes)

    cliente = clientes_filtrados[clientes_filtrados["nome_empresa"] == cliente_nome].iloc[0]

    with st.form("form_editar_cliente"):
        col1, col2 = st.columns(2)

        with col1:
            nome_empresa = st.text_input("Nome da empresa", value=cliente["nome_empresa"])
            tipo_cliente = st.selectbox(
                "Tipo de cliente",
                TIPOS_CLIENTE,
                index=TIPOS_CLIENTE.index(cliente["tipo_cliente"]) if cliente["tipo_cliente"] in TIPOS_CLIENTE else 0,
            )
            documento = st.text_input("Documento / CNPJ", value=cliente["documento"])
            cidade = st.text_input("Cidade", value=cliente["cidade"])
            estado = st.text_input("Estado", value=cliente["estado"])

        with col2:
            endereco_local = st.text_input("Endereço / Local", value=cliente["endereco_local"])
            setor_atividade = st.text_input("Setor de atividade", value=cliente["setor_atividade"])
            origem_cliente = st.selectbox(
                "Origem do cliente",
                ORIGENS_CLIENTE,
                index=ORIGENS_CLIENTE.index(cliente["origem_cliente"]) if cliente["origem_cliente"] in ORIGENS_CLIENTE else 0,
            )
            status_relacionamento = st.selectbox(
                "Status do relacionamento",
                STATUS_RELACIONAMENTO,
                index=STATUS_RELACIONAMENTO.index(cliente["status_relacionamento"])
                if cliente["status_relacionamento"] in STATUS_RELACIONAMENTO
                else 0,
            )
            responsavel = st.text_input("Responsável pelo atendimento", value=cliente["responsavel"])

        necessidade_cliente = st.text_area("Necessidade do cliente", value=cliente["necessidade_cliente"])
        proxima_acao = st.text_input("Próxima ação", value=cliente["proxima_acao"])
        data_proxima_acao = st.text_input("Data da próxima ação", value=cliente["data_proxima_acao"])
        observacoes_gerais = st.text_area("Observações gerais", value=cliente["observacoes_gerais"])

        atualizar = st.form_submit_button("Atualizar cliente")

        if atualizar:
            dados = {
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
                "proxima_acao": proxima_acao.strip(),
                "data_proxima_acao": data_proxima_acao.strip(),
                "observacoes_gerais": observacoes_gerais.strip(),
            }

            atualizar_cliente(cliente["id_cliente"], dados)
            st.success("Cliente atualizado com sucesso.")
            st.rerun()
