"""Representação funcional mínima da aba Barrilete do Excel oficial."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.barrilete import salvar_barrilete
from modulos.orcamentos.dominio.barrilete import Barrilete, ItemBarrilete, calcular_barrilete
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _numero(rotulo, valor, chave):
    return st.number_input(rotulo, value=valor, min_value=0.0, key=chave)


def _moeda(valor):
    formatado = f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {formatado}"


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_barrilete_salvo", False):
        st.success("Barrilete salvo.")

    atual = versao.barrilete
    horas_por_dia = (
        versao.dados_obra.horario_trabalho if versao.dados_obra else None
    )
    resultados = calcular_barrilete(atual, horas_por_dia)

    with st.form("barrilete_formulario"):
        st.subheader("Composição - BARRILETE - unidade: Global")
        st.markdown("**Mão de obra montagem canteiro**")
        colunas = st.columns(4)
        with colunas[0]:
            quantidade_operadores = _numero(
                "Nº Func. — Operador de Draga + técnico operação polím.",
                atual.quantidade_operadores,
                "barrilete_quantidade_operadores",
            )
            quantidade_ajudantes = _numero(
                "Nº Func. — Ajudante Geral",
                atual.quantidade_ajudantes,
                "barrilete_quantidade_ajudantes",
            )
        with colunas[1]:
            custo_hora_operador = _numero(
                "R$/h — Operador", atual.custo_hora_operador, "barrilete_custo_operador"
            )
            custo_hora_ajudante = _numero(
                "R$/h — Ajudante", atual.custo_hora_ajudante, "barrilete_custo_ajudante"
            )
        with colunas[2]:
            encargos_operador = _numero(
                "L.Sociais (%) — Operador",
                atual.encargos_operador,
                "barrilete_encargos_operador",
            )
            encargos_ajudante = _numero(
                "L.Sociais (%) — Ajudante",
                atual.encargos_ajudante,
                "barrilete_encargos_ajudante",
            )
        with colunas[3]:
            custo_refeicao = _numero(
                "R$/un. — Refeições", atual.custo_refeicao, "barrilete_refeicao"
            )
            custo_transporte = _numero(
                "R$/un. — Transporte", atual.custo_transporte, "barrilete_transporte"
            )

        st.caption(
            "Hrs/dia: "
            + (f"{horas_por_dia:g}" if horas_por_dia is not None else "não informado em Dados Obra")
        )
        st.metric("Custo por dia", _moeda(resultados.custo_por_dia))

        st.markdown("**Descrição dos serviços**")
        itens_editados = []
        for numero, item in enumerate(atual.itens, start=1):
            st.markdown(f"{numero}. {item.descricao} — {item.unidade}")
            colunas_item = st.columns(3)
            with colunas_item[0]:
                quantidade = _numero(
                    "Quantidade", item.quantidade, f"barrilete_{item.id}_quantidade"
                )
            with colunas_item[1]:
                if item.preco_base is not None:
                    st.metric("Preço Unit.", _moeda(item.preco_unitario))
                    preco_manual = None
                else:
                    preco_manual = _numero(
                        "Preço Unit.",
                        item.preco_unitario_manual,
                        f"barrilete_{item.id}_preco_unitario",
                    )
            with colunas_item[2]:
                preco_total = _numero(
                    "Preço Total",
                    item.preco_total_informado,
                    f"barrilete_{item.id}_preco_total",
                )
            itens_editados.append(
                ItemBarrilete(
                    item.id,
                    item.descricao,
                    item.unidade,
                    quantidade,
                    item.preco_base,
                    item.multiplicador_preco,
                    preco_manual,
                    preco_total,
                )
            )

        st.markdown("**Mão de obra de montagem — dia**")
        st.metric("Preço Unit. e Preço Total", _moeda(resultados.preco_mao_obra_montagem))
        bdi = _numero("BDI (%)", atual.bdi, "barrilete_bdi")

        st.markdown("**Resultados salvos anteriormente**")
        metricas = st.columns(4)
        with metricas[0]:
            st.metric("TOTAL", _moeda(resultados.total_composicao))
        with metricas[1]:
            st.metric("20 % de depreciação", _moeda(resultados.depreciacao))
        with metricas[2]:
            st.metric("Valor BDI", _moeda(resultados.valor_bdi))
        with metricas[3]:
            st.metric("Preço Final", _moeda(resultados.preco_final))
        submetido = st.form_submit_button("Salvar Barrilete")

    if not submetido:
        return

    try:
        barrilete = Barrilete(
            quantidade_operadores,
            custo_hora_operador,
            encargos_operador,
            quantidade_ajudantes,
            custo_hora_ajudante,
            encargos_ajudante,
            custo_refeicao,
            custo_transporte,
            tuple(itens_editados),
            bdi,
        )
    except ValueError as erro:
        st.error(str(erro))
        return

    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_barrilete(copia_versao, barrilete)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_barrilete_salvo"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
