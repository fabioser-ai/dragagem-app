"""Representação funcional mínima da aba Canteiro."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.canteiro import salvar_canteiro
from modulos.orcamentos.dominio.canteiro import (
    Canteiro, ItemCanteiro, LinhaMaoObraCanteiro, calcular_canteiro,
)
from modulos.orcamentos.dominio.producao import calcular_producao
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _numero(rotulo, valor, chave):
    return st.number_input(rotulo, value=valor, min_value=0.0, key=chave)


def _moeda(valor):
    if valor is None:
        return "Pendente"
    formatado = f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {formatado}"


def _prazo_producao(versao):
    dados = versao.dados_obra
    if dados is None:
        return None
    return calcular_producao(
        versao.producao, dados.horario_trabalho, dados.dias_trabalho,
        dados.volume_dragagem,
    ).prazo_meses


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_canteiro_salvo", False):
        st.success("Canteiro salvo.")

    atual = versao.canteiro
    resultados = calcular_canteiro(atual, _prazo_producao(versao))
    mao_obra = {item.id: item for item in resultados.mao_obra}
    itens_resultado = {item.id: item for item in resultados.itens}

    with st.form("canteiro_formulario"):
        st.subheader("CANTEIRO DE OBRAS : subitem da Dragagem")
        st.markdown("**Mão de obra**")
        equipe_editada = []
        for linha in atual.equipe:
            st.markdown(f"**{linha.descricao or '(linha sem descrição no Excel)'}**")
            colunas = st.columns(5)
            with colunas[0]:
                quantidade = _numero("Nº Func.", linha.quantidade, f"canteiro_{linha.id}_quantidade")
            with colunas[1]:
                custo_hora = _numero("R$/h", linha.custo_hora, f"canteiro_{linha.id}_custo")
            with colunas[2]:
                horas_dia = _numero("Hrs/dia", linha.horas_dia, f"canteiro_{linha.id}_horas")
            with colunas[3]:
                encargos = _numero("L.Sociais (%)", linha.encargos_sociais, f"canteiro_{linha.id}_encargos")
            with colunas[4]:
                st.metric("Total", _moeda(mao_obra[linha.id].total))
            equipe_editada.append(LinhaMaoObraCanteiro(
                linha.id, linha.descricao, quantidade, custo_hora, horas_dia, encargos,
            ))

        apoio = st.columns(3)
        with apoio[0]:
            custo_refeicao = _numero("Refeições — R$/un.", atual.custo_refeicao, "canteiro_refeicao")
            st.metric("Quantidade de refeições", f"{resultados.quantidade_pessoas:g}")
        with apoio[1]:
            custo_transporte = _numero("Transporte — R$/un.", atual.custo_transporte, "canteiro_transporte")
            st.metric("Quantidade de transportes", f"{resultados.quantidade_pessoas:g}")
        with apoio[2]:
            st.metric("Custo por dia", _moeda(resultados.custo_por_dia))

        st.caption(
            "Referências auxiliares preservadas do Excel: Operador — R$ 28,35; "
            "ajudante — R$ 11,13; Operador sistema de desidratação — R$ 15,15."
        )
        st.markdown("**Descrição dos serviços**")
        itens_editados = []
        for item in atual.itens:
            resultado = itens_resultado[item.id]
            st.markdown(f"{item.numero}. {item.descricao} — {item.unidade}")
            colunas = st.columns(4)
            quantidade_derivada = any((
                item.quantidade_prazo, item.quantidade_quatro_prazos, item.quantidade_pessoas,
            ))
            with colunas[0]:
                if quantidade_derivada:
                    quantidade_manual = None
                    st.metric("Quantidade", "Pendente" if resultado.quantidade is None else f"{resultado.quantidade:g}")
                else:
                    quantidade_manual = _numero("Quantidade", item.quantidade_manual, f"canteiro_{item.id}_quantidade")
            with colunas[1]:
                if item.preco_unitario_custo_diario:
                    preco_unitario_manual = None
                    st.metric("Preço Unit.", _moeda(resultado.preco_unitario))
                else:
                    preco_unitario_manual = _numero("Preço Unit.", item.preco_unitario_manual, f"canteiro_{item.id}_unitario")
            with colunas[2]:
                if item.preco_total_calculado:
                    preco_total_manual = None
                    st.metric("Preço Total", _moeda(resultado.preco_total))
                else:
                    preco_total_manual = _numero("Preço Total", item.preco_total_manual, f"canteiro_{item.id}_total")
            with colunas[3]:
                observacao = st.text_input(
                    "Observação/Fonte", value=item.observacao, key=f"canteiro_{item.id}_observacao"
                )
            itens_editados.append(ItemCanteiro(
                item.id, item.numero, item.descricao, item.unidade, quantidade_manual,
                item.quantidade_prazo, item.quantidade_quatro_prazos,
                item.quantidade_pessoas, preco_unitario_manual,
                item.preco_unitario_custo_diario, item.preco_total_calculado,
                preco_total_manual, observacao,
            ))

        bdi = _numero("BDI (%)", atual.bdi, "canteiro_bdi")
        metricas = st.columns(5)
        valores = (
            ("TOTAL", _moeda(resultados.total_composicao)),
            ("Prazo de Operação", "Pendente" if resultados.prazo_operacao is None else f"{resultados.prazo_operacao:g} mês(es)"),
            ("Preço unitário", _moeda(resultados.preco_unitario)),
            ("Valor BDI", _moeda(resultados.valor_bdi)),
            ("Preço Final", _moeda(resultados.preco_final)),
        )
        for coluna, (rotulo, valor) in zip(metricas, valores):
            with coluna:
                st.metric(rotulo, valor)
        submetido = st.form_submit_button("Salvar Canteiro")

    if not submetido:
        return
    try:
        canteiro = Canteiro(
            tuple(equipe_editada), custo_refeicao, custo_transporte,
            tuple(itens_editados), bdi,
        )
    except ValueError as erro:
        st.error(str(erro))
        return
    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_canteiro(copia_versao, canteiro)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_canteiro_salvo"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
