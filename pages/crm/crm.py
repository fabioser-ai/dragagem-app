import streamlit as st

from pages.crm.repositorio import (
    carregar_clientes,
    carregar_contatos,
    carregar_interacoes,
)
from pages.crm.navegacao import render_fluxo, render_landing
from pages.crm.fluxos_tarefa import (
    novo_cliente,
    novo_contato,
    nova_interacao,
    consultar_clientes,
    consultar_contatos,
    consultar_interacoes,
    atualizar_cliente_tela,
    atualizar_contato_tela,
)
from pages.crm.utils import preparar_dataframe_para_exibicao


def tela_consulta_geral():
    st.subheader("Consulta Geral CRM")

    clientes = carregar_clientes()
    contatos = carregar_contatos()
    interacoes = carregar_interacoes()

    col1, col2, col3 = st.columns(3)
    col1.metric("Clientes", len(clientes))
    col2.metric("Contatos", len(contatos))
    col3.metric("Interações", len(interacoes))

    st.markdown("---")

    if clientes.empty:
        st.info("Nenhum cliente cadastrado ainda.")
        return

    busca = st.text_input(
        "Busca rápida",
        placeholder="Empresa, cidade, responsável, necessidade...",
    )

    df = clientes.copy()

    if busca:
        termo = busca.lower().strip()
        mascara = (
            df["nome_empresa"].fillna("").str.lower().str.contains(termo, na=False)
            | df["cidade"].fillna("").str.lower().str.contains(termo, na=False)
            | df["estado"].fillna("").str.lower().str.contains(termo, na=False)
            | df["responsavel"].fillna("").str.lower().str.contains(termo, na=False)
            | df["necessidade_cliente"].fillna("").str.lower().str.contains(termo, na=False)
            | df["observacoes_gerais"].fillna("").str.lower().str.contains(termo, na=False)
        )
        df = df[mascara]

    st.dataframe(
        preparar_dataframe_para_exibicao(
            df[
                [
                    "nome_empresa",
                    "cidade",
                    "estado",
                    "status_relacionamento",
                    "responsavel",
                    "necessidade_cliente",
                    "ultimo_contato",
                    "proxima_acao",
                    "data_proxima_acao",
                ]
            ]
        ),
        use_container_width=True,
        hide_index=True,
    )


def _render_pagina_por_fluxo(fluxo, pagina):
    if fluxo == "novo":
        if pagina == "clientes":
            novo_cliente()
        elif pagina == "contatos":
            novo_contato()
        elif pagina == "interacoes":
            nova_interacao()
        return

    if fluxo == "consultar":
        if pagina == "consulta":
            tela_consulta_geral()
        elif pagina == "clientes":
            consultar_clientes()
        elif pagina == "contatos":
            consultar_contatos()
        elif pagina == "interacoes":
            consultar_interacoes()
        return

    if fluxo == "atualizar":
        if pagina == "clientes":
            atualizar_cliente_tela()
        elif pagina == "contatos":
            atualizar_contato_tela()


def crm():
    col1, col2 = st.columns([6, 1])

    with col1:
        st.title("CRM FOS")
        st.caption("Relacionamento comercial, prospecção e histórico de contatos.")

    with col2:
        st.write("")
        st.write("")
        if st.button("⬅ MENU", use_container_width=True):
            st.session_state.crm_fluxo = None
            st.session_state.crm_pagina = None
            st.session_state.tela = "menu"
            st.rerun()

    st.markdown("---")

    if "crm_fluxo" not in st.session_state:
        st.session_state.crm_fluxo = None
    if "crm_pagina" not in st.session_state:
        st.session_state.crm_pagina = None

    fluxo = st.session_state.crm_fluxo
    if not fluxo:
        render_landing()
        return

    pagina = render_fluxo(fluxo)
    if not pagina:
        return

    st.markdown("---")
    _render_pagina_por_fluxo(fluxo, pagina)


if __name__ == "__main__":
    crm()
