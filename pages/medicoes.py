import streamlit as st

from modulos.medicoes.repositorio import carregar_bases
from modulos.medicoes.navegacao import navegacao

from modulos.medicoes.permissoes import (
    tem_acesso_medicoes,
    obter_perfil_medicao,
    pode_criar_medicao,
)

from modulos.medicoes.fluxo_medicao.etapa1_obra import tela_obras
from modulos.medicoes.fluxo_medicao.etapa2_bm import tela_bm
from modulos.medicoes.fluxo_medicao.etapa3_frentes import tela_frentes
from modulos.medicoes.fluxo_medicao.etapa4_mc import tela_mc
from modulos.medicoes.fluxo_medicao.etapa5_lancamentos import (
    tela_lancamentos,
)
from modulos.medicoes.fluxo_medicao.etapa6_resumo import tela_resumo


def medicoes():
    st.title("Medições")
    st.caption("Controle técnico, operacional e financeiro de medições.")

    if not tem_acesso_medicoes():
        st.warning("Você não possui acesso ao módulo de Medições.")
        return

    perfil_medicao = obter_perfil_medicao()

    if "fluxo_medicoes" not in st.session_state:
        st.session_state["fluxo_medicoes"] = "inicio"

    if "etapa_medicoes" not in st.session_state:
        st.session_state["etapa_medicoes"] = "obra"

    # Funcionário entra direto no fluxo operacional de lançamento
    if perfil_medicao == "funcionario":
        if st.session_state.get("fluxo_medicoes") != "lancamento":
            st.session_state["fluxo_medicoes"] = "lancamento"

    # Proteção contra acesso indevido ao fluxo de gestão
    if (
        st.session_state.get("fluxo_medicoes") == "gestao"
        and not pode_criar_medicao()
    ):
        st.session_state["fluxo_medicoes"] = "inicio"
        st.warning("Seu perfil não possui acesso à criação ou gestão de medições.")

    navegacao()

    fluxo = st.session_state.get("fluxo_medicoes", "inicio")

    if fluxo != "gestao":
        return

    if not pode_criar_medicao():
        st.warning("Seu perfil não possui permissão para gerenciar medições.")
        return

    (
        obras,
        medicoes_df,
        frentes,
        mc,
        itens,
        servicos,
    ) = carregar_bases()

    etapa = st.session_state.etapa_medicoes

    if etapa == "obra":
        tela_obras(obras)

    elif etapa == "bm":
        tela_bm(obras, medicoes_df)

    elif etapa == "frentes":
        tela_frentes(frentes)

    elif etapa == "mc":
        tela_mc(frentes, mc)

    elif etapa == "lancamentos":
        tela_lancamentos()

    elif etapa == "resumo":
        tela_resumo(frentes, itens, medicoes_df)


def render():
    medicoes()


if __name__ == "__main__":
    medicoes()
