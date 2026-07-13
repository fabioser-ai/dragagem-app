import streamlit as st

from pages.crm.config import TIPOS_CONTATO, RESULTADOS_INTERACAO
from pages.crm.repositorio import (
    cadastro_interacao_liberado,
    cadastrar_interacao_composta,
    carregar_contexto_interacao_resultado,
    carregar_contatos,
)
from pages.crm.utils import preparar_dataframe_para_exibicao


def tela_interacoes():
    st.subheader("Histórico de Interações")

    resultado_clientes, resultado_interacoes, snapshot_comum = (
        carregar_contexto_interacao_resultado()
    )
    clientes = resultado_clientes.dados
    contatos = carregar_contatos()
    interacoes = resultado_interacoes.dados

    if clientes.empty:
        st.warning("Cadastre pelo menos um cliente antes de registrar interações.")
        return

    clientes_opcoes = {
        row["nome_empresa"]: row["id_cliente"]
        for _, row in clientes.sort_values("nome_empresa").iterrows()
    }
    cadastro_liberado = cadastro_interacao_liberado(
        resultado_clientes,
        resultado_interacoes,
        snapshot_comum,
    )

    if not cadastro_liberado:
        resultado_bloqueio = (
            resultado_clientes
            if not resultado_clientes.pode_sobrescrever
            else resultado_interacoes
            if not resultado_interacoes.pode_sobrescrever
            else snapshot_comum
        )
        detalhes = resultado_bloqueio.erro or (
            "Não foi possível confirmar o snapshot comum da branch."
        )
        if resultado_bloqueio.http_status:
            detalhes = f"{detalhes} (HTTP {resultado_bloqueio.http_status})"
        st.error(
            "O cadastro de interação está bloqueado para preservar os dados. "
            + detalhes
        )

    with st.expander("Nova interação", expanded=False):
        with st.form("form_nova_interacao"):
            cliente_nome = st.selectbox("Cliente / Empresa", list(clientes_opcoes.keys()))
            id_cliente = clientes_opcoes[cliente_nome]

            contatos_cliente = contatos[contatos["id_cliente"] == id_cliente].copy()

            opcoes_contato = {"Sem contato específico": ""}

            for _, row in contatos_cliente.iterrows():
                opcoes_contato[row["nome_contato"]] = row["id_contato"]

            contato_nome = st.selectbox("Contato", list(opcoes_contato.keys()))
            id_contato = opcoes_contato[contato_nome]

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

            salvar = st.form_submit_button(
                "Salvar interação",
                disabled=not cadastro_liberado,
            )

            if salvar:
                if not descricao.strip():
                    st.error("Informe a descrição da interação.")
                else:
                    dados = {
                        "id_cliente": id_cliente,
                        "id_contato": id_contato,
                        "data_interacao": str(data_interacao),
                        "tipo_contato": tipo_contato,
                        "descricao": descricao.strip(),
                        "responsavel": responsavel.strip(),
                        "resultado": resultado,
                        "proxima_acao": proxima_acao.strip(),
                        "data_proxima_acao": str(data_proxima_acao) if data_proxima_acao else "",
                    }

                    resultado = cadastrar_interacao_composta(
                        dados,
                        resultado_clientes,
                        resultado_interacoes,
                        snapshot_comum,
                    )

                    if resultado.sucesso:
                        st.success("Interação registrada com sucesso.")
                        st.rerun()
                    else:
                        detalhes = resultado.erro or (
                            "Não foi possível registrar a interação."
                        )
                        if resultado.http_status:
                            detalhes = f"{detalhes} (HTTP {resultado.http_status})"
                        st.error(detalhes)

    st.markdown("---")
    st.subheader("Histórico registrado")

    if interacoes.empty:
        st.info("Nenhuma interação registrada.")
        return

    interacoes_view = interacoes.merge(
        clientes[["id_cliente", "nome_empresa"]],
        on="id_cliente",
        how="left",
    )

    if not contatos.empty:
        interacoes_view = interacoes_view.merge(
            contatos[["id_contato", "nome_contato"]],
            on="id_contato",
            how="left",
        )
    else:
        interacoes_view["nome_contato"] = ""

    busca_cliente = st.selectbox(
        "Filtrar por cliente",
        ["Todos"] + sorted(interacoes_view["nome_empresa"].dropna().unique().tolist()),
    )

    if busca_cliente != "Todos":
        interacoes_view = interacoes_view[interacoes_view["nome_empresa"] == busca_cliente]

    interacoes_view = interacoes_view.sort_values("data_interacao", ascending=False)

    st.dataframe(
        preparar_dataframe_para_exibicao(
            interacoes_view[
                [
                    "data_interacao",
                    "nome_empresa",
                    "nome_contato",
                    "tipo_contato",
                    "responsavel",
                    "resultado",
                    "proxima_acao",
                    "data_proxima_acao",
                    "descricao",
                ]
            ]
        ),
        use_container_width=True,
        hide_index=True,
    )
