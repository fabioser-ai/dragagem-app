"""Representação funcional mínima da worksheet Planilha1."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.planilha1 import salvar_planilha1
from modulos.orcamentos.aplicacao.planilha_precos import (
    compor_referencias_planilha_precos,
)
from modulos.orcamentos.dominio.planilha1 import (
    EntradaLinhaPlanilha1,
    Planilha1,
    calcular_planilha1,
)
from modulos.orcamentos.dominio.planilha_precos import calcular_planilha_precos
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _formatar_numero(valor):
    if valor is None:
        return "Pendente"
    return f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")


def _moeda(valor):
    return "Pendente" if valor is None else f"R$ {_formatar_numero(valor)}"


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_planilha1_salva", False):
        st.success("Planilha1 salva.")

    atual = versao.planilha1
    referencias = compor_referencias_planilha_precos(versao)
    precos = calcular_planilha_precos(versao.planilha_precos, referencias)
    resultados = calcular_planilha1(atual, precos)

    with st.form("planilha1_formulario"):
        st.subheader("Planilha1")
        st.markdown(
            "**Worksheet Excel: Planilha1 · posição 17 · dimensão e intervalo "
            "funcional A2:F7**"
        )
        st.caption(
            "As quatro quantidades permanecem manuais. Preços unitários, "
            "preços totais e TOTAL GERAL reproduzem somente as nove fórmulas do Excel."
        )

        entradas = []
        for entrada, resultado in zip(atual.linhas, resultados.linhas):
            st.markdown(
                f"**{resultado.numero}. {resultado.descricao} — "
                f"{resultado.unidade}**"
            )
            colunas = st.columns(3)
            with colunas[0]:
                quantidade = st.number_input(
                    "QUANT",
                    value=entrada.quantidade,
                    min_value=0.0,
                    key=f"planilha1_{entrada.id}_quantidade",
                )
            with colunas[1]:
                st.metric("PREÇO UNITÁRIO", _moeda(resultado.preco_unitario))
            with colunas[2]:
                st.metric("PREÇO TOTAL", _moeda(resultado.preco_total))
            entradas.append(EntradaLinhaPlanilha1(entrada.id, quantidade))

        st.metric("TOTAL GERAL", _moeda(resultados.total_geral))
        submetido = st.form_submit_button("Salvar Planilha1")

    if not submetido:
        return
    try:
        planilha = Planilha1(tuple(entradas))
    except ValueError as erro:
        st.error(str(erro))
        return

    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_planilha1(copia_versao, planilha)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (
            copia_orcamento,
            copia_versao,
        )
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_planilha1_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error(
            "O orçamento foi alterado por outra operação. "
            "Reabra a versão antes de salvar."
        )
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
