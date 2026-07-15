"""Entrada do Novo Sistema de Orçamentos."""

import streamlit as st

from modulos.orcamentos.apresentacao import painel
from modulos.orcamentos.persistencia.github_repositorio import RepositorioOrcamentosGitHub


def _voltar_ao_menu():
    st.session_state.tela = "menu"
    st.rerun()


def render(*, autorizado):
    """Apresenta o painel rápido, respeitando a autorização recebida."""
    if not autorizado:
        st.error("Você não possui acesso ao módulo de Orçamentos.")
        if st.button("Voltar ao menu", key="novo_orcamento_sem_acesso_voltar"):
            _voltar_ao_menu()
        return

    repositorio = RepositorioOrcamentosGitHub(
        st.secrets["GITHUB_TOKEN"],
        st.secrets["REPO"],
    )
    painel.render(repositorio=repositorio, ao_voltar=_voltar_ao_menu)
