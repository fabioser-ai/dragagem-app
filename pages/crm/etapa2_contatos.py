import streamlit as st

from pages.crm.repositorio import (
    carregar_clientes,
    carregar_contatos,
    cadastrar_contato,
    atualizar_contato,
)
from pages.crm.utils import filtrar_dataframe, preparar_dataframe_para_exibicao


def tela_contatos():
    st.subheader("Contatos dos Clientes")

    clientes = carregar_clientes()
    contatos = carregar_contatos()

    if clientes.empty:
        st.warning("Cadastre pelo menos um cliente antes de cadastrar contatos.")
        return

    clientes_opcoes = {
        row["nome_empresa"]: row["id_cliente"]
        for _, row in clientes.sort_values("nome_empresa").iterrows()
    }

    with st.expander("Novo contato", expanded=False):
        with st.form("form_novo_contato"):
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
                else:
                    dados = {
                        "id_cliente": id_cliente,
                        "nome_contato": nome_contato.strip(),
                        "cargo": cargo.strip(),
                        "telefone": telefone.strip(),
                        "whatsapp": whatsapp.strip(),
                        "email": email.strip(),
                        "contato_principal": "Sim" if contato_principal else "Não",
                        "observacoes": observacoes.strip(),
                    }

                    cadastrar_contato(dados)
                    st.success("Contato cadastrado com sucesso.")
                    st.rerun()

    st.markdown("---")
    st.subheader("Contatos cadastrados")

    if contatos.empty:
        st.info("Nenhum contato cadastrado.")
        return

    contatos_view = contatos.merge(
        clientes[["id_cliente", "nome_empresa"]],
        on="id_cliente",
        how="left",
    )

    busca = st.text_input("Buscar contato", placeholder="Digite nome, empresa, telefone, email...")

    contatos_filtrados = filtrar_dataframe(
        contatos_view,
        busca,
        [
            "nome_empresa",
            "nome_contato",
            "cargo",
            "telefone",
            "whatsapp",
            "email",
            "observacoes",
        ],
    )

    st.dataframe(
        preparar_dataframe_para_exibicao(
            contatos_filtrados[
                [
                    "nome_empresa",
                    "nome_contato",
                    "cargo",
                    "telefone",
                    "whatsapp",
                    "email",
                    "contato_principal",
                ]
            ]
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")
    st.subheader("Editar contato")

    contatos_filtrados["label_contato"] = (
        contatos_filtrados["nome_contato"].fillna("")
        + " - "
        + contatos_filtrados["nome_empresa"].fillna("")
    )

    contato_label = st.selectbox("Selecione o contato", contatos_filtrados["label_contato"].tolist())

    contato = contatos_filtrados[contatos_filtrados["label_contato"] == contato_label].iloc[0]

    with st.form("form_editar_contato"):
        cliente_nome_atual = contato["nome_empresa"]

        cliente_nome = st.selectbox(
            "Cliente / Empresa",
            list(clientes_opcoes.keys()),
            index=list(clientes_opcoes.keys()).index(cliente_nome_atual)
            if cliente_nome_atual in clientes_opcoes
            else 0,
        )

        id_cliente = clientes_opcoes[cliente_nome]

        col1, col2 = st.columns(2)

        with col1:
            nome_contato = st.text_input("Nome do contato", value=contato["nome_contato"])
            cargo = st.text_input("Cargo", value=contato["cargo"])
            telefone = st.text_input("Telefone", value=contato["telefone"])

        with col2:
            whatsapp = st.text_input("WhatsApp", value=contato["whatsapp"])
            email = st.text_input("Email", value=contato["email"])
            contato_principal = st.checkbox(
                "Contato principal",
                value=True if contato["contato_principal"] == "Sim" else False,
            )

        observacoes = st.text_area("Observações", value=contato["observacoes"])

        atualizar = st.form_submit_button("Atualizar contato")

        if atualizar:
            dados = {
                "id_cliente": id_cliente,
                "nome_contato": nome_contato.strip(),
                "cargo": cargo.strip(),
                "telefone": telefone.strip(),
                "whatsapp": whatsapp.strip(),
                "email": email.strip(),
                "contato_principal": "Sim" if contato_principal else "Não",
                "observacoes": observacoes.strip(),
            }

            atualizar_contato(contato["id_contato"], dados)
            st.success("Contato atualizado com sucesso.")
            st.rerun()
