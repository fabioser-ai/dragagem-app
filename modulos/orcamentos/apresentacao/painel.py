"""Painel rápido do Novo Sistema de Orçamentos."""

import streamlit as st

from modulos.orcamentos.aplicacao.consultas import filtrar_resumos
from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.apresentacao import dados_obra
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _rotulo(resumo):
    return f"{resumo.objeto} · v{resumo.numero} · {resumo.responsavel}"


def _mostrar_detalhe(repositorio):
    detalhe = st.session_state.get("novo_orcamento_detalhe")
    if not detalhe:
        return
    orcamento, versao = detalhe
    st.divider()
    st.subheader(orcamento.objeto)
    st.caption(
        f"Versão {versao.numero} · {versao.estado.value} · "
        f"{len(versao.cenarios)} cenário(s)"
    )
    st.write(f"Finalidade: {orcamento.finalidade}")
    st.write(f"Responsável: {orcamento.responsavel}")

    snapshot = st.session_state.get("novo_orcamento_snapshot")
    if snapshot:
        dados_obra.render(
            repositorio=repositorio,
            orcamento=orcamento,
            versao=versao,
            snapshot_esperado=snapshot,
        )
    elif versao.editavel and st.button(
        "Abrir Dados Obra",
        key="novo_orcamento_iniciar_edicao",
    ):
        resultado = repositorio.carregar_snapshot()
        if resultado.sucesso:
            st.session_state["novo_orcamento_snapshot"] = resultado.valor
            st.rerun()
        else:
            st.error("Não foi possível iniciar uma edição segura.")


def _criar_e_abrir(repositorio):
    autor = st.session_state.get("usuario", "")
    criacao = criar_orcamento_vazio(autor)
    if not criacao.sucesso:
        st.error(criacao.erro)
        return False

    snapshot = repositorio.carregar_snapshot()
    if not snapshot.sucesso:
        st.error("Não foi possível iniciar a criação segura do orçamento.")
        return False
    indice = repositorio.carregar_indice_bruto()
    if not indice.sucesso:
        st.error("Não foi possível preparar o índice para criação.")
        return False

    orcamento, versao = criacao.valor
    persistencia = repositorio.persistir_versao(
        orcamento, versao, indice.valor, snapshot.valor
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (orcamento, versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.rerun()
        return True
    if persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("A base avançou durante a criação. Tente novamente.")
    else:
        st.error("Não foi possível criar o orçamento.")
    return False


def render(*, repositorio, ao_voltar):
    """Lista o índice em uma leitura e abre uma versão somente sob demanda."""

    st.title("Novo Sistema de Orçamentos")

    if st.session_state.get("novo_orcamento_detalhe") and st.session_state.get(
        "novo_orcamento_snapshot"
    ):
        _mostrar_detalhe(repositorio)
        if st.button("Voltar ao menu", key="novo_orcamento_voltar_menu"):
            ao_voltar()
        return

    if st.button("Novo orçamento", key="novo_orcamento_criar"):
        if _criar_e_abrir(repositorio):
            return

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
                snapshot = repositorio.carregar_snapshot()
                if snapshot.sucesso:
                    st.session_state["novo_orcamento_detalhe"] = detalhe.valor
                    st.session_state["novo_orcamento_snapshot"] = snapshot.valor
                    st.rerun()
                    return
                else:
                    st.error("Não foi possível abrir uma edição segura.")
            elif detalhe.status is StatusPersistencia.DADO_INEXISTENTE:
                st.error("A versão selecionada não foi encontrada.")
            else:
                st.error("Não foi possível abrir a versão selecionada.")

    _mostrar_detalhe(repositorio)

    if st.button("Voltar ao menu", key="novo_orcamento_voltar_menu"):
        ao_voltar()
