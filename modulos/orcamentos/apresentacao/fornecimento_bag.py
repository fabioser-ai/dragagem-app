"""Representação funcional mínima da aba 4. Forn. Bag."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.fornecimento_bag import salvar_fornecimento_bag
from modulos.orcamentos.dominio.fornecimento_bag import (
    FornecimentoBag, ItemFornecimentoBag, LinhaMaoObraFornecimentoBag,
    MemorialFisicoBag, OpcaoDimensionamentoBag, calcular_fornecimento_bag,
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
    if st.session_state.pop("novo_orcamento_fornecimento_bag_salvo", False):
        st.success("Fornecimento de Bag salvo.")
    atual = versao.fornecimento_bag
    horas = versao.dados_obra.horario_trabalho if versao.dados_obra is not None else None
    resultados = calcular_fornecimento_bag(atual, horas)
    mao_obra = {x.id: x for x in resultados.mao_obra}
    opcoes_resultado = {x.id: x for x in resultados.opcoes}
    itens_resultado = {x.id: x for x in resultados.itens}

    with st.form("fornecimento_bag_formulario"):
        st.subheader("4. Fornecimento de Bag")
        st.markdown("**Mão de obra montagem canteiro**")
        equipe_editada = []
        for linha in atual.equipe:
            st.markdown(f"**{linha.descricao}**")
            colunas = st.columns(5)
            with colunas[0]:
                quantidade = _numero("Nº Func.", linha.quantidade, f"forn_bag_{linha.id}_quantidade")
            with colunas[1]:
                custo = _numero("R$/h", linha.custo_hora, f"forn_bag_{linha.id}_custo")
            with colunas[2]:
                horas_linha = mao_obra[linha.id].horas_dia
                st.metric("Hrs/dia", "Pendente" if horas_linha is None else f"{horas_linha:g} h")
            with colunas[3]:
                encargos = _numero("L.Sociais (%)", linha.encargos_sociais, f"forn_bag_{linha.id}_encargos")
            with colunas[4]:
                st.metric("Total", _moeda(mao_obra[linha.id].total))
            equipe_editada.append(LinhaMaoObraFornecimentoBag(
                linha.id, linha.descricao, quantidade, custo, linha.horas_dados_obra,
                linha.horas_referencia_id, encargos,
            ))
        apoio = st.columns(3)
        with apoio[0]:
            refeicao = _numero("Refeições — R$/un.", atual.custo_refeicao, "forn_bag_refeicao")
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[1]:
            transporte = _numero("Transporte — R$/un.", atual.custo_transporte, "forn_bag_transporte")
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[2]:
            st.metric("Custo por dia", _moeda(resultados.custo_por_dia))

        st.markdown("**Memória de dimensionamento**")
        m = atual.memorial_fisico
        memoria_colunas = st.columns(3)
        with memoria_colunas[0]:
            volume = _numero("Volume", m.volume, "forn_bag_memorial_volume")
        with memoria_colunas[1]:
            situ = _numero("% Solidos situ", m.percentual_solidos_situ, "forn_bag_memorial_situ")
        with memoria_colunas[2]:
            desagua = _numero("% Solidos Desagua", m.percentual_solidos_desagua, "forn_bag_memorial_desagua")
        memorial_editado = MemorialFisicoBag(volume, situ, desagua)
        memoria_resultados = st.columns(2)
        with memoria_resultados[0]:
            st.metric("Tonelada Seca", f"{resultados.memorial_fisico.tonelada_seca:g}")
        with memoria_resultados[1]:
            material = resultados.memorial_fisico.volume_material_bags
            st.metric("Volume de material a ser acomodado em bags", "Pendente" if material is None else f"{material:g}")

        st.markdown("**Memorial comercial de bags**")
        opcoes_editadas = []
        for opcao in atual.opcoes:
            resultado = opcoes_resultado[opcao.id]
            st.markdown(f"**{opcao.descricao}**")
            colunas = st.columns(6)
            with colunas[0]:
                capacidade = _numero("Capacidade", opcao.capacidade, f"forn_bag_{opcao.id}_capacidade")
            with colunas[1]:
                quantidade_area = _numero("Possivel colocar em área", opcao.quantidade_area, f"forn_bag_{opcao.id}_quantidade_area")
            with colunas[2]:
                if opcao.volume_total_calculado:
                    volume_total_manual = None
                    st.metric("Volume total", f"{resultado.volume_total:g}")
                else:
                    volume_total_manual = _numero("Volume total", opcao.volume_total_manual, f"forn_bag_{opcao.id}_volume_total")
            with colunas[3]:
                reinicio = _numero("Reinicio Celula", opcao.reinicio_celula, f"forn_bag_{opcao.id}_reinicio")
            with colunas[4]:
                if opcao.volume_final_calculado:
                    volume_final_manual = None
                    st.metric("Volume Final", f"{resultado.volume_final:g}")
                else:
                    volume_final_manual = _numero("Volume Final", opcao.volume_final_manual, f"forn_bag_{opcao.id}_volume_final")
            with colunas[5]:
                preco_m3 = _numero("Preço /m3", opcao.preco_por_m3, f"forn_bag_{opcao.id}_preco_m3")
            opcoes_editadas.append(OpcaoDimensionamentoBag(
                opcao.id, opcao.descricao, capacidade, quantidade_area,
                opcao.volume_total_calculado, volume_total_manual, reinicio,
                opcao.volume_final_calculado, volume_final_manual, preco_m3,
                opcao.unidade_preco,
            ))
        totais_memorial = st.columns(3)
        with totais_memorial[0]: st.metric("TOTAL — quantidade", f"{resultados.total_quantidade_area:g}")
        with totais_memorial[1]: st.metric("TOTAL — volume", f"{resultados.total_volume:g}")
        with totais_memorial[2]: st.metric("TOTAL — volume final", f"{resultados.total_volume_final:g}")
        fator_6x30 = _numero(
            "H15 — fator vazio usado no preço do Bag 6,00 x 30,00m",
            atual.fator_preco_bag_6x30, "forn_bag_fator_preco_6x30",
        )

        st.markdown("**Descrição dos serviços**")
        itens_editados = []
        for item in atual.itens:
            resultado = itens_resultado[item.id]
            prefixo = "" if item.numero is None else f"{item.numero}. "
            st.markdown(f"{prefixo}{item.descricao}{' — ' + item.unidade if item.unidade else ''}")
            colunas = st.columns(3)
            with colunas[0]:
                if item.quantidade_opcao_id is not None:
                    quantidade_manual = None
                    st.metric("Quantidade", f"{resultado.quantidade:g}")
                else:
                    quantidade_manual = _numero("Quantidade", item.quantidade_manual, f"forn_bag_{item.id}_quantidade")
            with colunas[1]:
                derivado_preco = any((item.preco_unitario_opcao_id is not None, item.preco_unitario_bag_6x30, item.preco_unitario_custo_diario))
                if derivado_preco:
                    unitario_manual = None
                    st.metric("Preço Unit.", _moeda(resultado.preco_unitario))
                else:
                    unitario_manual = _numero("Preço Unit.", item.preco_unitario_manual, f"forn_bag_{item.id}_unitario")
            with colunas[2]:
                if item.preco_total_calculado:
                    total_manual = None
                    st.metric("Preço Total", _moeda(resultado.preco_total))
                else:
                    total_manual = _numero("Preço Total", item.preco_total_manual, f"forn_bag_{item.id}_total")
            itens_editados.append(ItemFornecimentoBag(
                item.id, item.numero, item.descricao, item.unidade, quantidade_manual,
                item.quantidade_opcao_id, item.quantidade_multiplica_reinicio,
                item.quantidade_arredondada, unitario_manual,
                item.preco_unitario_opcao_id, item.preco_unitario_bag_6x30,
                item.preco_unitario_custo_diario, item.preco_total_calculado,
                total_manual,
            ))

        bdi = _numero("BDI (%)", atual.bdi, "forn_bag_bdi")
        finais = st.columns(3)
        with finais[0]: st.metric("TOTAL", _moeda(resultados.total))
        with finais[1]: st.metric("Valor BDI", _moeda(resultados.valor_bdi))
        with finais[2]: st.metric("Preço Final", _moeda(resultados.preco_final))
        submetido = st.form_submit_button("Salvar Fornecimento de Bag")

    if not submetido:
        return
    try:
        fornecimento = FornecimentoBag(
            tuple(equipe_editada), refeicao, transporte, memorial_editado,
            tuple(opcoes_editadas), fator_6x30, tuple(itens_editados), bdi,
        )
    except ValueError as erro:
        st.error(str(erro))
        return
    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_fornecimento_bag(copia_versao, fornecimento)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_fornecimento_bag_salvo"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
