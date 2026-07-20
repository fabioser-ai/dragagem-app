"""Representação funcional mínima da aba 3. Prep. Célula."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.preparacao_celula import salvar_preparacao_celula
from modulos.orcamentos.dominio.preparacao_celula import (
    ComposicaoRealPreparacaoCelula, ItemPreparacaoCelula,
    LinhaMaoObraPreparacaoCelula, PreparacaoCelula, calcular_preparacao_celula,
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
    if st.session_state.pop("novo_orcamento_preparacao_celula_salva", False):
        st.success("Preparação da célula salva.")
    atual = versao.preparacao_celula
    horas = versao.dados_obra.horario_trabalho if versao.dados_obra is not None else None
    resultados = calcular_preparacao_celula(atual, horas)
    mao_obra = {x.id: x for x in resultados.mao_obra}
    itens_resultado = {x.id: x for x in resultados.itens}

    with st.form("preparacao_celula_formulario"):
        st.subheader("3. PREPARO DE CÉLULA - Manta PEAD")
        st.markdown("**Mão de obra montagem canteiro**")
        equipe_editada = []
        for linha in atual.equipe:
            st.markdown(f"**{linha.descricao}**")
            colunas = st.columns(5)
            with colunas[0]:
                quantidade = _numero("Nº Func.", linha.quantidade, f"prep_celula_{linha.id}_quantidade")
            with colunas[1]:
                custo = _numero("R$/h", linha.custo_hora, f"prep_celula_{linha.id}_custo")
            with colunas[2]:
                horas_linha = mao_obra[linha.id].horas_dia
                st.metric("Hrs/dia", "Pendente" if horas_linha is None else f"{horas_linha:g} h")
            with colunas[3]:
                encargos = _numero("L.Sociais (%)", linha.encargos_sociais, f"prep_celula_{linha.id}_encargos")
            with colunas[4]:
                st.metric("Total", _moeda(mao_obra[linha.id].total))
            equipe_editada.append(LinhaMaoObraPreparacaoCelula(
                linha.id, linha.descricao, quantidade, custo, linha.horas_dados_obra,
                linha.horas_referencia_id, encargos,
            ))

        apoio = st.columns(3)
        with apoio[0]:
            refeicao = _numero("Refeições — R$/un.", atual.custo_refeicao, "prep_celula_refeicao")
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[1]:
            transporte = _numero("Transporte — R$/un.", atual.custo_transporte, "prep_celula_transporte")
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[2]:
            st.metric("Custo por dia", _moeda(resultados.custo_por_dia))

        st.markdown("**Composição Real**")
        c = atual.composicao_real
        campos = (
            ("Manta PEAD — m²/m² de Célula", "fator_pead"),
            ("Bidim — m²/m² de Célula", "fator_bidim"),
            ("Brita — m³/m² de Célula", "fator_brita"),
            ("Retro escavadeira — h/m² de Célula", "fator_retro"),
            ("Mão de Obra — h/m² de Célula", "fator_mao_obra"),
            ("PEAD — parcela 1", "parcela_pead_1"),
            ("PEAD — parcela 2", "parcela_pead_2"),
            ("PEAD — parcela 3", "parcela_pead_3"),
            ("PEAD — parcela 4", "parcela_pead_4"),
            ("Célua — área base", "area_celula_pead"),
            ("BRITA — parcela", "parcela_brita"),
        )
        valores_composicao = {}
        for rotulo, campo in campos:
            valores_composicao[campo] = _numero(
                rotulo, getattr(c, campo), f"prep_celula_composicao_{campo}"
            )
        composicao_editada = ComposicaoRealPreparacaoCelula(**valores_composicao)
        metricas_composicao = st.columns(4)
        with metricas_composicao[0]:
            st.metric("Área total", f"{resultados.composicao_real.area_total:g} m²")
        with metricas_composicao[1]:
            st.metric("Manta PEAD", f"{resultados.composicao_real.quantidade_pead:g} m²")
        with metricas_composicao[2]:
            st.metric("Bidim", f"{resultados.composicao_real.quantidade_bidim:g} m²")
        with metricas_composicao[3]:
            st.metric("Brita base", f"{resultados.composicao_real.quantidade_brita_base:g} m³")
        st.caption(
            "Referências auxiliares preservadas: (4 oficiais + 6 ajudantes); "
            "Operador — R$ 22,68; ajudante — R$ 11,13; "
            "Operador sistema de desidratação — R$ 15,15."
        )

        st.markdown("**Descrição dos serviços**")
        itens_editados = []
        for item in atual.itens:
            resultado = itens_resultado[item.id]
            st.markdown(f"{item.numero}. {item.descricao} — {item.unidade}")
            colunas = st.columns(4)
            derivada = any((item.quantidade_pead, item.quantidade_referencia_pead, item.quantidade_bidim, item.quantidade_brita))
            with colunas[0]:
                if derivada:
                    quantidade_manual = None
                    st.metric("Quantidade", "Pendente" if resultado.quantidade is None else f"{resultado.quantidade:g}")
                else:
                    quantidade_manual = _numero("Quantidade", item.quantidade_manual, f"prep_celula_{item.id}_quantidade")
            with colunas[1]:
                if item.preco_unitario_custo_diario:
                    unitario_manual = None
                    st.metric("Preço Unit.", _moeda(resultado.preco_unitario))
                else:
                    unitario_manual = _numero("Preço Unit.", item.preco_unitario_manual, f"prep_celula_{item.id}_unitario")
            with colunas[2]:
                if item.preco_total_calculado:
                    total_manual = None
                    st.metric("Preço Total", _moeda(resultado.preco_total))
                else:
                    total_manual = _numero("Preço Total", item.preco_total_manual, f"prep_celula_{item.id}_total")
            with colunas[3]:
                observacao = st.text_input(
                    "Observação/Fonte", value=item.observacao,
                    key=f"prep_celula_{item.id}_observacao",
                )
            itens_editados.append(ItemPreparacaoCelula(
                item.id, item.numero, item.descricao, item.unidade, quantidade_manual,
                item.quantidade_pead, item.quantidade_referencia_pead,
                item.quantidade_bidim, item.quantidade_brita, unitario_manual,
                item.preco_unitario_custo_diario, item.preco_total_calculado,
                total_manual, observacao,
            ))

        repeticoes = _numero(
            "Quantidade de Repetiçoes", atual.quantidade_repeticoes,
            "prep_celula_quantidade_repeticoes",
        )
        finais = st.columns(3)
        with finais[0]: st.metric("TOTAL", _moeda(resultados.total))
        with finais[1]: st.metric("Total das repetições", _moeda(resultados.total_repeticoes))
        with finais[2]: st.metric("Preço Final", _moeda(resultados.preco_final))
        submetido = st.form_submit_button("Salvar Preparação da Célula")

    if not submetido:
        return
    try:
        preparacao = PreparacaoCelula(
            tuple(equipe_editada), refeicao, transporte, composicao_editada,
            tuple(itens_editados), repeticoes,
        )
    except ValueError as erro:
        st.error(str(erro))
        return
    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_preparacao_celula(copia_versao, preparacao)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_preparacao_celula_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
