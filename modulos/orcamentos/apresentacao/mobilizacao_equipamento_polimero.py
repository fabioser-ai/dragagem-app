"""Representação funcional mínima da aba 2. Mob. Eq. Polimero."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.mobilizacao_equipamento_polimero import (
    salvar_mobilizacao_equipamento_polimero,
)
from modulos.orcamentos.dominio.barrilete import calcular_barrilete
from modulos.orcamentos.dominio.mobilizacao_equipamento_polimero import (
    ItemMobilizacaoEquipamentoPolimero,
    LinhaMaoObraPolimero,
    MobilizacaoEquipamentoPolimero,
    calcular_mobilizacao_equipamento_polimero,
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
    if st.session_state.pop("novo_orcamento_mob_eq_polimero_salva", False):
        st.success("Mobilização do equipamento de polímero salva.")

    atual = versao.mobilizacao_equipamento_polimero
    horas = versao.dados_obra.horario_trabalho if versao.dados_obra is not None else None
    preco_barrilete = calcular_barrilete(versao.barrilete, horas).preco_final
    resultados = calcular_mobilizacao_equipamento_polimero(
        atual, horas, preco_barrilete
    )
    resultados_mao_obra = {item.id: item for item in resultados.mao_obra}
    resultados_itens = {item.id: item for item in resultados.itens}

    with st.form("mobilizacao_equipamento_polimero_formulario"):
        st.subheader("2 - MOBILIZAÇÃO E MONTAGEM DE EQUIP. POLÍMERO")
        st.markdown("**Mão de obra montagem canteiro**")
        equipe_editada = []
        for linha in atual.equipe:
            st.markdown(f"**{linha.descricao}**")
            colunas = st.columns(5)
            with colunas[0]:
                quantidade = _numero(
                    "Nº Func.", linha.quantidade, f"mob_eq_polimero_{linha.id}_quantidade"
                )
            with colunas[1]:
                custo_hora = _numero(
                    "R$/h", linha.custo_hora, f"mob_eq_polimero_{linha.id}_custo"
                )
            with colunas[2]:
                st.metric("Hrs/dia", "Pendente" if horas is None else f"{horas:g} h")
            with colunas[3]:
                encargos = _numero(
                    "L.Sociais (%)", linha.encargos_sociais,
                    f"mob_eq_polimero_{linha.id}_encargos",
                )
            with colunas[4]:
                st.metric("Total", _moeda(resultados_mao_obra[linha.id].total))
            equipe_editada.append(
                LinhaMaoObraPolimero(
                    linha.id, linha.descricao, quantidade, custo_hora, encargos
                )
            )

        apoio = st.columns(3)
        with apoio[0]:
            custo_refeicao = _numero(
                "Refeições — R$/un.", atual.custo_refeicao, "mob_eq_polimero_refeicao"
            )
            st.metric("Quantidade de refeições", f"{resultados.quantidade_apoio:g}")
        with apoio[1]:
            custo_transporte = _numero(
                "Transporte — R$/un.", atual.custo_transporte, "mob_eq_polimero_transporte"
            )
            st.metric("Quantidade de transportes", f"{resultados.quantidade_apoio:g}")
        with apoio[2]:
            st.metric("Custo por dia", _moeda(resultados.custo_por_dia))

        st.caption(
            "Referências auxiliares preservadas do Excel: Operador — R$ 28,35; "
            "ajudante — R$ 11,13; Operador sistema de desidratação — R$ 15,15."
        )
        st.markdown("**Descrição dos serviços**")
        itens_editados = []
        for item in atual.itens:
            st.markdown(f"{item.numero}. {item.descricao} — {item.unidade}")
            colunas = st.columns(4)
            with colunas[0]:
                quantidade = _numero(
                    "Quantidade", item.quantidade, f"mob_eq_polimero_{item.id}_quantidade"
                )
            with colunas[1]:
                if item.preco_unitario_barrilete or item.preco_unitario_custo_diario:
                    preco_unitario_manual = None
                    st.metric("Preço Unit.", _moeda(resultados_itens[item.id].preco_unitario))
                else:
                    preco_unitario_manual = _numero(
                        "Preço Unit.", item.preco_unitario_manual,
                        f"mob_eq_polimero_{item.id}_preco_unitario",
                    )
            with colunas[2]:
                if item.preco_total_calculado:
                    preco_total_manual = None
                    st.metric("Preço Total", _moeda(resultados_itens[item.id].preco_total))
                else:
                    preco_total_manual = _numero(
                        "Preço Total", item.preco_total_manual,
                        f"mob_eq_polimero_{item.id}_preco_total",
                    )
            with colunas[3]:
                observacao = st.text_input(
                    "Observação/Fonte", value=item.observacao,
                    key=f"mob_eq_polimero_{item.id}_observacao",
                )
            itens_editados.append(
                ItemMobilizacaoEquipamentoPolimero(
                    item.id, item.numero, item.descricao, item.unidade, quantidade,
                    preco_unitario_manual, item.preco_unitario_barrilete,
                    item.preco_unitario_custo_diario, item.preco_total_calculado,
                    preco_total_manual, observacao,
                )
            )

        bdi = _numero("BDI (%)", atual.bdi, "mob_eq_polimero_bdi")
        metricas = st.columns(3)
        with metricas[0]:
            st.metric("TOTAL", _moeda(resultados.total_composicao))
        with metricas[1]:
            st.metric("Valor BDI", _moeda(resultados.valor_bdi))
        with metricas[2]:
            st.metric("Preço Final", _moeda(resultados.preco_final))
        submetido = st.form_submit_button("Salvar Mobilização do Equipamento de Polímero")

    if not submetido:
        return

    try:
        mobilizacao = MobilizacaoEquipamentoPolimero(
            tuple(equipe_editada), custo_refeicao, custo_transporte,
            tuple(itens_editados), bdi,
        )
    except ValueError as erro:
        st.error(str(erro))
        return

    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_mobilizacao_equipamento_polimero(copia_versao, mobilizacao)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_mob_eq_polimero_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
