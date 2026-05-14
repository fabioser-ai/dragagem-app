import streamlit as st

from pages.crm.repositorio import carregar_clientes, carregar_contatos, carregar_interacoes
from pages.crm.navegacao import menu_crm
from pages.crm.etapa1_clientes import tela_clientes
from pages.crm.etapa2_contatos import tela_contatos
from pages.crm.etapa3_interacoes import tela_interacoes
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

    busca = st.text_input("Busca rápida", placeholder="Empresa, cidade, responsável, necessidade...")

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


def crm():
    st.title("CRM FOS")
    st.caption("Relacionamento comercial, prospecção e histórico de contatos.")

    pagina = menu_crm()

    if pagina == "clientes":
        tela_clientes()
    elif pagina == "contatos":
        tela_contatos()
    elif pagina == "interacoes":
        tela_interacoes()
    elif pagina == "consulta":
        tela_consulta_geral()


if __name__ == "__main__":
    crm()
