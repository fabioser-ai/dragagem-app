"""Representação funcional mínima da aba 8. Carga e Transporte."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.carga_transporte import salvar_carga_transporte
from modulos.orcamentos.dominio.carga_transporte import (
    CargaTransporte,
    ItemCargaTransporte,
    LinhaMaoObraCargaTransporte,
    calcular_carga_transporte,
)
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _numero(rotulo, valor, chave):
    return st.number_input(rotulo, value=valor, min_value=0.0, key=chave)


def _moeda(valor):
    texto = f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {texto}"


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_carga_transporte_salva", False):
        st.success("Carga e Transporte salva.")

    atual = versao.carga_transporte
    resultados = calcular_carga_transporte(atual)
    mao_obra = {item.id: item for item in resultados.mao_obra}
    itens = {item.id: item for item in resultados.itens}

    with st.form("carga_transporte_formulario"):
        st.subheader("8 - Medição")
        st.markdown(
            "**Aba Excel: 8. Carga e Transporte · "
            "intervalo físico A1:J23 · funcional A1:F23**"
        )

        equipe_editada = []
        for linha in atual.equipe:
            st.markdown(f"**{linha.descricao}**")
            colunas = st.columns(5)
            with colunas[0]:
                quantidade = _numero(
                    "Nº Func.",
                    linha.quantidade,
                    f"carga_transporte_{linha.id}_quantidade",
                )
            with colunas[1]:
                custo_hora = _numero(
                    "R$/h",
                    linha.custo_hora,
                    f"carga_transporte_{linha.id}_custo_hora",
                )
            with colunas[2]:
                if linha.horas_referencia_id is None:
                    horas = _numero(
                        "Hrs/dia",
                        linha.horas_dia_manual,
                        f"carga_transporte_{linha.id}_horas",
                    )
                else:
                    horas = None
                    st.metric(
                        "Hrs/dia",
                        f"{mao_obra[linha.id].horas_dia or 0:g}",
                        help="Fórmula do Excel: D6=D5",
                    )
            with colunas[3]:
                encargos = _numero(
                    "L.Sociais (%)",
                    linha.encargos_sociais,
                    f"carga_transporte_{linha.id}_encargos",
                )
            with colunas[4]:
                st.metric("Total", _moeda(mao_obra[linha.id].total))
            equipe_editada.append(
                LinhaMaoObraCargaTransporte(
                    linha.id,
                    linha.descricao,
                    quantidade,
                    custo_hora,
                    horas,
                    linha.horas_referencia_id,
                    encargos,
                )
            )

        apoio = st.columns(3)
        with apoio[0]:
            custo_refeicao = _numero(
                "Refeições — R$/un.",
                atual.custo_refeicao,
                "carga_transporte_custo_refeicao",
            )
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[1]:
            custo_transporte = _numero(
                "Transporte — R$/un.",
                atual.custo_transporte,
                "carga_transporte_custo_transporte",
            )
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[2]:
            st.metric("Custo por dia", _moeda(resultados.custo_por_dia))

        st.markdown("**Descrição dos serviços**")
        itens_editados = []
        for item in atual.itens:
            st.markdown(f"{item.numero}. {item.descricao} — {item.unidade}")
            colunas = st.columns(3)
            with colunas[0]:
                quantidade = _numero(
                    "Quantidade",
                    item.quantidade,
                    f"carga_transporte_{item.id}_quantidade",
                )
            with colunas[1]:
                if item.preco_unitario_custo_diario:
                    preco_unitario = None
                    st.metric(
                        "Preço Unit.",
                        _moeda(itens[item.id].preco_unitario or 0),
                        help="Fórmula do Excel: E17=F10.",
                    )
                else:
                    preco_unitario = _numero(
                        "Preço Unit.",
                        item.preco_unitario_manual,
                        f"carga_transporte_{item.id}_preco_unitario",
                    )
            with colunas[2]:
                st.metric("Preço Total", _moeda(itens[item.id].preco_total))
            itens_editados.append(
                ItemCargaTransporte(
                    item.id,
                    item.numero,
                    item.descricao,
                    item.unidade,
                    quantidade,
                    preco_unitario,
                    item.preco_unitario_custo_diario,
                )
            )

        bdi_principal = _numero(
            "BDI principal (%)",
            atual.bdi_principal,
            "carga_transporte_bdi_principal",
        )
        principal = st.columns(3)
        with principal[0]:
            st.metric("TOTAL", _moeda(resultados.total))
        with principal[1]:
            st.metric("Valor BDI", _moeda(resultados.valor_bdi_principal))
        with principal[2]:
            st.metric("Preço Final", _moeda(resultados.preco_final))

        st.markdown("**Segundo bloco preservado das linhas 21–23**")
        segundo = st.columns(2)
        with segundo[0]:
            st.metric(
                "Base F21",
                "Vazia",
                help="A célula F21 não existe no XML e permanece vazia.",
            )
        with segundo[1]:
            bdi_secundario = _numero(
                "BDI secundário (%)",
                atual.bdi_secundario,
                "carga_transporte_bdi_secundario",
            )
            st.metric(
                "Preço Final secundário",
                _moeda(resultados.preco_final_secundario),
            )

        submetido = st.form_submit_button("Salvar Carga e Transporte")

    if not submetido:
        return
    try:
        carga_transporte = CargaTransporte(
            tuple(equipe_editada),
            custo_refeicao,
            custo_transporte,
            tuple(itens_editados),
            bdi_principal,
            bdi_secundario,
        )
    except ValueError as erro:
        st.error(str(erro))
        return

    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_carga_transporte(copia_versao, carga_transporte)
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
        st.session_state["novo_orcamento_carga_transporte_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error(
            "O orçamento foi alterado por outra operação. "
            "Reabra a versão antes de salvar."
        )
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
