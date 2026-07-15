"""Painel rápido do Novo Sistema de Orçamentos."""

import streamlit as st

from modulos.orcamentos.aplicacao.consultas import filtrar_resumos
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _rotulo(resumo):
    return f"{resumo.objeto} · v{resumo.numero} · {resumo.responsavel}"


def render(*, repositorio, ao_voltar):
    """Lista o índice em uma leitura e abre uma versão somente sob demanda."""

    st.title("Novo Sistema de Orçamentos")

    resultado_indice = repositorio.carregar_indice()
    if resultado_indice.status is StatusPersistencia.DADO_INEXISTENTE:
        st.info("Ainda não existem orçamentos no novo sistema.")
        if st.button("Voltar ao menu", key="novo_orcamento_voltar_menu"):
            ao_voltar()
        return
    if not resultado_indice.sucesso:
        st.error("Não foi possível carregar o painel de orçamentos.")
        if st.button("Tentar novamente", key="novo_orcamento_tentar_novamente"):
            st.rerun()
        if st.button("Voltar ao menu", key="novo_orcamento_voltar_menu"):
            ao_voltar()
        return

    resumos = resultado_indice.valor
    busca = st.text_input(
        "Buscar",
        placeholder="Objeto, finalidade, responsável ou identificador",
        key="novo_orcamento_busca",
    )
    estados = sorted({item.estado for item in resumos})
    estado = st.selectbox(
        "Estado",
        options=[""] + estados,
        format_func=lambda valor: "Todos" if not valor else valor.replace("_", " ").title(),
        key="novo_orcamento_filtro_estado",
    )
    filtrados = filtrar_resumos(resumos, busca=busca, estado=estado)

    if not filtrados:
        st.warning("Nenhum orçamento corresponde aos filtros informados.")
    else:
        st.dataframe(
            [
                {
                    "Objeto": item.objeto,
                    "Versão": item.numero,
                    "Finalidade": item.finalidade,
                    "Responsável": item.responsavel,
                    "Estado": item.estado,
                }
                for item in filtrados
            ],
            use_container_width=True,
            hide_index=True,
        )
        selecionado = st.selectbox(
            "Abrir orçamento",
            options=filtrados,
            format_func=_rotulo,
            key="novo_orcamento_selecao",
        )
        if st.button("Abrir versão", key="novo_orcamento_abrir_versao"):
            detalhe = repositorio.carregar_versao(
                selecionado.orcamento_id,
                selecionado.versao_id,
            )
            if detalhe.sucesso:
                orcamento, versao = detalhe.valor
                st.subheader(orcamento.objeto)
                st.caption(
                    f"Versão {versao.numero} · {versao.estado.value} · "
                    f"{len(versao.cenarios)} cenário(s)"
                )
                st.write(f"Finalidade: {orcamento.finalidade}")
                st.write(f"Responsável: {orcamento.responsavel}")
            elif detalhe.status is StatusPersistencia.DADO_INEXISTENTE:
                st.error("A versão selecionada não foi encontrada.")
            else:
                st.error("Não foi possível abrir a versão selecionada.")

    if st.button("Voltar ao menu", key="novo_orcamento_voltar_menu"):
        ao_voltar()
