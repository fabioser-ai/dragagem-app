"""Página informativa inicial do Novo Sistema de Orçamentos.

Esta fronteira não lê dados, não executa cálculos e não persiste estado de domínio.
"""

import streamlit as st


def _voltar_ao_menu():
    st.session_state.tela = "menu"
    st.rerun()


def render(*, autorizado):
    """Apresenta a fronteira inicial, respeitando a autorização recebida."""
    if not autorizado:
        st.error("Você não possui acesso ao módulo de Orçamentos.")
        if st.button("Voltar ao menu", key="novo_orcamento_sem_acesso_voltar"):
            _voltar_ao_menu()
        return

    st.title("Novo Sistema de Orçamentos")
    st.info(
        "Esta é a nova fronteira do sistema orçamentário da FOS, "
        "que será construída progressivamente por Kid Steps."
    )

    st.markdown(
        """
        - A criação de orçamentos ainda não está disponível.
        - Nenhum dado de orçamento foi carregado nesta página.
        - Nenhum cálculo ou persistência é executado aqui.
        - O módulo legado de Orçamentos permanece disponível no menu.
        - Próximo marco: Kid Step 002 — núcleo do domínio em memória.
        """
    )

    if st.button("Voltar ao menu", key="novo_orcamento_voltar_menu"):
        _voltar_ao_menu()
