"""Representação funcional mínima da aba 5. Operação Sistema."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.operacao_sistema import salvar_operacao_sistema
from modulos.orcamentos.dominio.fornecimento_bag import calcular_fornecimento_bag
from modulos.orcamentos.dominio.operacao_sistema import (
    ItemOperacaoSistema, LinhaMaoObraOperacaoSistema, OperacaoSistema,
    calcular_operacao_sistema,
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


def _referencias_externas(versao):
    dados = versao.dados_obra
    horas = dados.horario_trabalho if dados is not None else None
    tonelada_seca = calcular_fornecimento_bag(
        versao.fornecimento_bag, horas
    ).memorial_fisico.tonelada_seca
    prazo = None
    if dados is not None:
        prazo = calcular_producao(
            versao.producao, dados.horario_trabalho, dados.dias_trabalho,
            dados.volume_dragagem,
        ).prazo_meses
    return horas, tonelada_seca, prazo


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_operacao_sistema_salva", False):
        st.success("Operação do Sistema salva.")
    atual = versao.operacao_sistema
    horas, tonelada_seca, prazo = _referencias_externas(versao)
    resultados = calcular_operacao_sistema(atual, horas, tonelada_seca, prazo)
    mao_obra = {x.id: x for x in resultados.mao_obra}
    itens_resultado = {x.id: x for x in resultados.itens}

    with st.form("operacao_sistema_formulario"):
        st.subheader("Operação do Sistema de Desidratação - Subitem da Dragagem")
        st.markdown("**Mão de obra montagem canteiro**")
        equipe_editada = []
        for linha in atual.equipe:
            resultado = mao_obra[linha.id]
            st.markdown(f"**{linha.descricao}**")
            colunas = st.columns(5)
            with colunas[0]:
                quantidade = _numero("Nº Func.", linha.quantidade, f"op_sistema_{linha.id}_quantidade")
            with colunas[1]:
                if linha.custo_hora_operador_calculado:
                    custo_manual = None
                    st.metric("R$/h", _moeda(resultado.custo_hora))
                else:
                    custo_manual = _numero("R$/h", linha.custo_hora_manual, f"op_sistema_{linha.id}_custo")
            with colunas[2]:
                st.metric("Hrs/dia", "Pendente" if resultado.horas_dia is None else f"{resultado.horas_dia:g} h")
            with colunas[3]:
                encargos = _numero("L.Sociais (%)", linha.encargos_sociais, f"op_sistema_{linha.id}_encargos")
            with colunas[4]:
                st.metric("Total", _moeda(resultado.total))
            equipe_editada.append(LinhaMaoObraOperacaoSistema(
                linha.id, linha.descricao, quantidade, custo_manual,
                linha.custo_hora_operador_calculado, encargos,
            ))
        apoio = st.columns(3)
        with apoio[0]:
            refeicao = _numero("Refeições — R$/un.", atual.custo_refeicao, "op_sistema_refeicao")
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[1]:
            transporte = _numero("Transporte — R$/un.", atual.custo_transporte, "op_sistema_transporte")
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[2]:
            st.metric("Custo por dia", _moeda(resultados.custo_por_dia))

        st.markdown("**Memorial de consumo de polímero**")
        memorial = st.columns(4)
        with memorial[0]:
            st.metric("Tonelada seca — 4. Forn. Bag!B35", "Pendente" if tonelada_seca is None else f"{tonelada_seca:g} t")
        with memorial[1]: st.metric("Dosagem", "3 kg/t seca")
        with memorial[2]: st.metric("Fator", "1,05")
        with memorial[3]: st.metric("Polímero", f"{resultados.memorial_polimero.quantidade_polimero:g} kg")

        st.markdown("**Descrição dos serviços**")
        itens_editados = []
        for item in atual.itens:
            resultado = itens_resultado[item.id]
            st.markdown(f"{item.numero}. {item.descricao} — {item.unidade}")
            colunas = st.columns(4)
            with colunas[0]:
                if item.quantidade_polimero or item.quantidade_dias_operacao:
                    quantidade_manual = None
                    st.metric("Quantidade", f"{resultado.quantidade:g}")
                else:
                    quantidade_manual = _numero("Quantidade", item.quantidade_manual, f"op_sistema_{item.id}_quantidade")
            with colunas[1]:
                if item.preco_unitario_custo_diario:
                    unitario_manual = None
                    st.metric("Preço Unit.", _moeda(resultado.preco_unitario))
                else:
                    unitario_manual = _numero("Preço Unit.", item.preco_unitario_manual, f"op_sistema_{item.id}_unitario")
            with colunas[2]:
                if item.preco_total_calculado:
                    total_manual = None
                    st.metric("Preço Total", _moeda(resultado.preco_total))
                else:
                    total_manual = _numero("Preço Total", item.preco_total_manual, f"op_sistema_{item.id}_total")
            with colunas[3]:
                observacao = st.text_input(
                    "Observação/Fonte", value=item.observacao,
                    key=f"op_sistema_{item.id}_observacao",
                )
            itens_editados.append(ItemOperacaoSistema(
                item.id, item.numero, item.descricao, item.unidade,
                quantidade_manual, item.quantidade_polimero,
                item.quantidade_dias_operacao, unitario_manual,
                item.preco_unitario_custo_diario, item.preco_total_calculado,
                total_manual, observacao,
            ))

        finais = st.columns(3)
        with finais[0]: st.metric("TOTAL", _moeda(resultados.total))
        with finais[1]:
            prazo_texto = "Pendente" if resultados.prazo_execucao_meses is None else f"{resultados.prazo_execucao_meses} mês(es)"
            st.metric("Prazo de Execução", prazo_texto)
        with finais[2]: st.metric("Custo Mensal", _moeda(resultados.custo_mensal))
        submetido = st.form_submit_button("Salvar Operação do Sistema")

    if not submetido:
        return
    try:
        operacao = OperacaoSistema(
            tuple(equipe_editada), refeicao, transporte, tuple(itens_editados)
        )
    except ValueError as erro:
        st.error(str(erro))
        return
    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_operacao_sistema(copia_versao, operacao)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_operacao_sistema_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
