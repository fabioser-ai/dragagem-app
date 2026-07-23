"""Representação funcional mínima da aba 9. Desmob. Eq. Polimero."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.desmobilizacao_equipamento_polimero import (
    salvar_desmobilizacao_equipamento_polimero,
)
from modulos.orcamentos.dominio.barrilete import calcular_barrilete
from modulos.orcamentos.dominio.desmobilizacao_equipamento_polimero import (
    DesmobilizacaoEquipamentoPolimero,
    ItemDesmobilizacaoEquipamentoPolimero,
    LinhaMaoObraDesmobilizacaoPolimero,
    calcular_desmobilizacao_equipamento_polimero,
)
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _numero(rotulo, valor, chave):
    return st.number_input(rotulo, value=valor, min_value=0.0, key=chave)


def _moeda(valor):
    texto = f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {texto}"


def _referencias_externas(versao):
    horas = versao.dados_obra.horario_trabalho if versao.dados_obra is not None else None
    preco_barrilete = calcular_barrilete(versao.barrilete, horas).preco_final
    return horas, preco_barrilete


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_desmob_eq_polimero_salva", False):
        st.success("Desmobilização do Equipamento de Polímero salva.")

    atual = versao.desmobilizacao_equipamento_polimero
    horas, preco_barrilete = _referencias_externas(versao)
    resultados = calcular_desmobilizacao_equipamento_polimero(
        atual, horas, preco_barrilete
    )
    mao_obra = {x.id: x for x in resultados.mao_obra}
    itens = {x.id: x for x in resultados.itens}

    with st.form("desmobilizacao_equipamento_polimero_formulario"):
        st.subheader("2 - DESMOBILIZAÇÃO E MONTAGEM DE EQUIP. POLÍMERO")
        st.markdown("**Aba Excel: 9. Desmob. Eq. Polimero · intervalo A1:F26**")
        st.markdown(
            "Referências explícitas: `'Dados Obra '!B26` e `Barrilete!F31`."
        )

        equipe_editada = []
        for linha in atual.equipe:
            st.markdown(f"**{linha.descricao}**")
            colunas = st.columns(5)
            with colunas[0]:
                quantidade = _numero(
                    "Nº Func.", linha.quantidade,
                    f"desmob_eq_polimero_{linha.id}_quantidade",
                )
            with colunas[1]:
                custo = _numero(
                    "R$/h", linha.custo_hora,
                    f"desmob_eq_polimero_{linha.id}_custo",
                )
            with colunas[2]:
                st.metric("Hrs/dia", "Pendente" if horas is None else f"{horas:g} h")
            with colunas[3]:
                encargos = _numero(
                    "L.Sociais (%)", linha.encargos_sociais,
                    f"desmob_eq_polimero_{linha.id}_encargos",
                )
            with colunas[4]:
                st.metric("Total", _moeda(mao_obra[linha.id].total))
            equipe_editada.append(LinhaMaoObraDesmobilizacaoPolimero(
                linha.id, linha.descricao, quantidade, custo, encargos
            ))

        apoio = st.columns(3)
        with apoio[0]:
            custo_refeicao = _numero(
                "Refeições — R$/un.", atual.custo_refeicao,
                "desmob_eq_polimero_refeicao",
            )
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[1]:
            custo_transporte = _numero(
                "Transporte — R$/un.", atual.custo_transporte,
                "desmob_eq_polimero_transporte",
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
                    "Quantidade", item.quantidade,
                    f"desmob_eq_polimero_{item.id}_quantidade",
                )
            with colunas[1]:
                if item.preco_unitario_barrilete or item.preco_unitario_custo_diario:
                    preco = None
                    st.metric("Preço Unit.", _moeda(itens[item.id].preco_unitario or 0))
                else:
                    preco = _numero(
                        "Preço Unit.", item.preco_unitario_manual,
                        f"desmob_eq_polimero_{item.id}_preco_unitario",
                    )
            with colunas[2]:
                st.metric("Preço Total", _moeda(itens[item.id].preco_total))
            itens_editados.append(ItemDesmobilizacaoEquipamentoPolimero(
                item.id, item.numero, item.descricao, item.unidade,
                quantidade, preco, item.preco_unitario_barrilete,
                item.preco_unitario_custo_diario,
            ))

        bdi = _numero("BDI (%)", atual.bdi, "desmob_eq_polimero_bdi")
        metricas = st.columns(3)
        with metricas[0]:
            st.metric("TOTAL", _moeda(resultados.total_composicao))
        with metricas[1]:
            st.metric("Valor BDI", _moeda(resultados.valor_bdi))
        with metricas[2]:
            st.metric("Preço Final", _moeda(resultados.preco_final))
        submetido = st.form_submit_button(
            "Salvar Desmobilização do Equipamento de Polímero"
        )

    if not submetido:
        return
    try:
        desmobilizacao = DesmobilizacaoEquipamentoPolimero(
            tuple(equipe_editada), custo_refeicao, custo_transporte,
            tuple(itens_editados), bdi,
        )
    except ValueError as erro:
        st.error(str(erro))
        return
    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_desmobilizacao_equipamento_polimero(
        copia_versao, desmobilizacao
    )
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_desmob_eq_polimero_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
