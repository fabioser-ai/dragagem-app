"""Representação funcional mínima da aba 10. Plan. Preços."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.planilha_precos import (
    compor_referencias_planilha_precos,
    salvar_planilha_precos,
)
from modulos.orcamentos.dominio.planilha_precos import (
    EntradaLinhaPlanilhaPrecos,
    PlanilhaPrecos,
    calcular_planilha_precos,
)
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _numero(rotulo, valor, chave):
    return st.number_input(rotulo, value=valor, min_value=0.0, key=chave)


def _formatar_numero(valor):
    if valor is None:
        return "Pendente"
    return (
        f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    )


def _moeda(valor):
    return "Pendente" if valor is None else f"R$ {_formatar_numero(valor)}"


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_planilha_precos_salva", False):
        st.success("Planilha de Preços salva.")

    atual = versao.planilha_precos
    referencias = compor_referencias_planilha_precos(versao)
    resultados = calcular_planilha_precos(atual, referencias)

    with st.form("planilha_precos_formulario"):
        st.subheader("PLANILHA DETALHADA PREÇOS DE CUSTO E VENDA")
        st.markdown(
            "**Aba Excel: 10. Plan. Preços · dimensão A1:K20 · "
            "intervalo funcional A1:J18**"
        )
        st.caption(
            "Os custos e as três quantidades calculadas reproduzem somente as "
            "referências explícitas do Excel. Quantidades azuis e BDIs azuis "
            "permanecem entradas manuais."
        )

        entradas_editadas = []
        for entrada, resultado in zip(atual.linhas, resultados.linhas):
            st.markdown(
                f"**{resultado.numero}. {resultado.descricao} — "
                f"{resultado.unidade}**"
            )
            colunas = st.columns(6)
            with colunas[0]:
                st.metric("Custo Total", _moeda(resultado.custo_total))
            with colunas[1]:
                if entrada.quantidade_manual is None:
                    quantidade = None
                    st.metric(
                        "Quantidade",
                        _formatar_numero(resultado.quantidade),
                        help="Quantidade referenciada por fórmula no Excel.",
                    )
                else:
                    quantidade = _numero(
                        "Quantidade",
                        entrada.quantidade_manual,
                        f"planilha_precos_{entrada.id}_quantidade",
                    )
            with colunas[2]:
                st.metric("Custo Unitário", _moeda(resultado.custo_unitario))
            with colunas[3]:
                bdi = _numero(
                    "BDI (%)",
                    entrada.bdi,
                    f"planilha_precos_{entrada.id}_bdi",
                )
            with colunas[4]:
                st.metric("Preço Unitário", _moeda(resultado.preco_unitario))
            with colunas[5]:
                st.metric("Preço Total", _moeda(resultado.preco_total))
            entradas_editadas.append(
                EntradaLinhaPlanilhaPrecos(entrada.id, quantidade, bdi)
            )

        resumo = st.columns(3)
        with resumo[0]:
            st.metric(
                "Custo Total — C12",
                _moeda(resultados.custo_total),
                help="Fórmula preservada: SUM(C5:C11), que exclui C4.",
            )
        with resumo[1]:
            st.metric("Preço de Venda — J12", _moeda(resultados.preco_venda))
        with resumo[2]:
            st.metric(
                "Valor auxiliar — J18",
                _moeda(resultados.valor_auxiliar_j18),
                help="Fórmula preservada: (SUM(J6:J9))/E8.",
            )

        submetido = st.form_submit_button("Salvar Planilha de Preços")

    if not submetido:
        return
    try:
        planilha = PlanilhaPrecos(tuple(entradas_editadas))
    except ValueError as erro:
        st.error(str(erro))
        return

    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_planilha_precos(copia_versao, planilha)
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
        st.session_state["novo_orcamento_planilha_precos_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error(
            "O orçamento foi alterado por outra operação. "
            "Reabra a versão antes de salvar."
        )
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
