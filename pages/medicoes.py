import streamlit as st

from modulos.medicoes.repositorio import carregar_bases
from modulos.medicoes.navegacao import navegacao
from modulos.medicoes.etapa1_obra import tela_obras
from modulos.medicoes.etapa2_bm import tela_bm
from modulos.medicoes.etapa3_frentes import tela_frentes
from modulos.medicoes.etapa4_mc import tela_mc
from modulos.medicoes.etapa5_itens import tela_medicao
from modulos.medicoes.etapa6_resumo import tela_resumo


def medicoes():
    st.title("Medições")
    st.caption("Controle técnico e financeiro de medições.")

    if "etapa_medicoes" not in st.session_state:
        st.session_state.etapa_medicoes = "obra"

    obras, medicoes_df, frentes, mc, itens, servicos = carregar_bases()

    navegacao()

    etapa = st.session_state.etapa_medicoes

    if etapa == "obra":
        tela_obras(obras)

    elif etapa == "bm":
        tela_bm(obras, medicoes_df)

    elif etapa == "frentes":
        tela_frentes(frentes)

    elif etapa == "mc":
        tela_mc(frentes, mc)

    elif etapa == "medicao":
        tela_medicao(frentes, mc, itens, servicos)

    elif etapa == "resumo":
        tela_resumo(frentes, itens, medicoes_df)


def render():
    medicoes()


if __name__ == "__main__":
    medicoes()
