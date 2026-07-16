"""Representação funcional mínima da aba 1. Mob. Draga."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.mobilizacao_draga import salvar_mobilizacao_draga
from modulos.orcamentos.dominio.mobilizacao_draga import (
    ItemMobilizacaoDraga,
    LinhaMaoObraMobilizacao,
    MobilizacaoDraga,
    calcular_mobilizacao_draga,
)
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _numero(rotulo, valor, chave):
    return st.number_input(rotulo, value=valor, min_value=0.0, key=chave)


def _moeda(valor):
    if valor is None:
        return "Pendente"
    formatado = f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {formatado}"


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_mob_draga_salva", False):
        st.success("Mobilização da Draga salva.")

    atual = versao.mobilizacao_draga
    resultados = calcular_mobilizacao_draga(atual)
    resultados_mao_obra = {item.id: item for item in resultados.mao_obra}
    resultados_itens = {item.id: item for item in resultados.itens}

    with st.form("mobilizacao_draga_formulario"):
        st.subheader('1 - Mobilização da Draga 6"')
        st.markdown("**Mão de obra p/carga e montagem / dia**")
        equipe_editada = []
        for linha in atual.equipe:
            st.markdown(f"**{linha.descricao}**")
            colunas = st.columns(5)
            with colunas[0]:
                quantidade = _numero(
                    "Nº Func.", linha.quantidade, f"mob_draga_{linha.id}_quantidade"
                )
            with colunas[1]:
                if linha.custo_hora_base is None:
                    custo_manual = _numero(
                        "R$/h", linha.custo_hora_manual, f"mob_draga_{linha.id}_custo"
                    )
                else:
                    custo_manual = None
                    st.metric("R$/h", _moeda(linha.custo_hora))
            with colunas[2]:
                if linha.horas_referencia_id is None:
                    horas_manual = _numero(
                        "Hrs/dia", linha.horas_dia_manual, f"mob_draga_{linha.id}_horas"
                    )
                else:
                    horas_manual = None
                    horas = resultados_mao_obra[linha.id].horas_dia
                    st.metric("Hrs/dia", "Pendente" if horas is None else f"{horas:g} h")
            with colunas[3]:
                encargos = _numero(
                    "L.Sociais (%)",
                    linha.encargos_sociais,
                    f"mob_draga_{linha.id}_encargos",
                )
            with colunas[4]:
                st.metric("Total", _moeda(resultados_mao_obra[linha.id].total))
            equipe_editada.append(
                LinhaMaoObraMobilizacao(
                    linha.id,
                    linha.descricao,
                    quantidade,
                    custo_manual,
                    linha.custo_hora_base,
                    linha.multiplicador_custo,
                    horas_manual,
                    linha.horas_referencia_id,
                    encargos,
                )
            )

        apoio = st.columns(3)
        with apoio[0]:
            custo_refeicao = _numero(
                "Refeições — R$/un.", atual.custo_refeicao, "mob_draga_refeicao"
            )
            st.metric("Quantidade de refeições", f"{resultados.quantidade_refeicoes:g}")
        with apoio[1]:
            custo_transporte = _numero(
                "Transporte — R$/un.", atual.custo_transporte, "mob_draga_transporte"
            )
            st.metric("Quantidade de transportes", f"{resultados.quantidade_transportes:g}")
        with apoio[2]:
            st.metric("Custo por dia", _moeda(resultados.custo_por_dia))

        st.markdown("**Descrição dos serviços**")
        itens_editados = []
        for numero, item in enumerate(atual.itens, start=1):
            st.markdown(f"{numero}. {item.descricao} — {item.unidade}")
            colunas = st.columns(4)
            with colunas[0]:
                quantidade = _numero(
                    "Quantidade", item.quantidade, f"mob_draga_{item.id}_quantidade"
                )
            with colunas[1]:
                if item.preco_unitario_custo_diario:
                    preco_unitario_manual = None
                    st.metric("Preço Unit.", _moeda(resultados_itens[item.id].preco_unitario))
                else:
                    preco_unitario_manual = _numero(
                        "Preço Unit.",
                        item.preco_unitario_manual,
                        f"mob_draga_{item.id}_preco_unitario",
                    )
            with colunas[2]:
                if item.preco_total_calculado:
                    preco_total_manual = None
                    st.metric("Preço Total", _moeda(resultados_itens[item.id].preco_total))
                else:
                    preco_total_manual = _numero(
                        "Preço Total",
                        item.preco_total_manual,
                        f"mob_draga_{item.id}_preco_total",
                    )
            with colunas[3]:
                observacao = st.text_input(
                    "Observação/Fonte",
                    value=item.observacao,
                    key=f"mob_draga_{item.id}_observacao",
                )
            itens_editados.append(
                ItemMobilizacaoDraga(
                    item.id,
                    item.descricao,
                    item.unidade,
                    quantidade,
                    preco_unitario_manual,
                    item.preco_unitario_custo_diario,
                    item.preco_total_calculado,
                    preco_total_manual,
                    observacao,
                )
            )

        bdi = _numero("BDI (%)", atual.bdi, "mob_draga_bdi")
        metricas = st.columns(4)
        with metricas[0]:
            st.metric("TOTAL", _moeda(resultados.total_composicao))
        with metricas[1]:
            st.metric("Valor BDI", _moeda(resultados.valor_bdi))
        with metricas[2]:
            st.metric("Preço Final", _moeda(resultados.preco_final))
        with metricas[3]:
            st.metric("Preço Final — repetição da planilha", _moeda(resultados.preco_final_repetido))
        submetido = st.form_submit_button("Salvar Mobilização da Draga")

    if not submetido:
        return

    try:
        mobilizacao = MobilizacaoDraga(
            tuple(equipe_editada),
            custo_refeicao,
            custo_transporte,
            tuple(itens_editados),
            bdi,
        )
    except ValueError as erro:
        st.error(str(erro))
        return

    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_mobilizacao_draga(copia_versao, mobilizacao)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_mob_draga_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
