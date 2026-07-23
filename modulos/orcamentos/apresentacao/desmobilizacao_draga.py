"""Representação funcional mínima da aba 8. Desmob. Draga."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.desmobilizacao_draga import salvar_desmobilizacao_draga
from modulos.orcamentos.dominio.desmobilizacao_draga import (
    DesmobilizacaoDraga,
    ItemDesmobilizacaoDraga,
    LinhaMaoObraDesmobilizacao,
    calcular_desmobilizacao_draga,
)
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _numero(rotulo, valor, chave):
    return st.number_input(rotulo, value=valor, min_value=0.0, key=chave)


def _moeda(valor):
    texto = f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {texto}"


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_desmob_draga_salva", False):
        st.success("Desmobilização da Draga salva.")

    atual = versao.desmobilizacao_draga
    horas = versao.dados_obra.horario_trabalho if versao.dados_obra is not None else None
    resultados = calcular_desmobilizacao_draga(atual, horas)
    mao_obra = {x.id: x for x in resultados.mao_obra}
    itens = {x.id: x for x in resultados.itens}

    with st.form("desmobilizacao_draga_formulario"):
        st.subheader("7 - DESMOBILIZAÇÃO E MONTAGEM DRAGA")
        st.markdown("**Aba Excel: 8. Desmob. Draga · intervalo A1:G21**")
        st.markdown("Referência explícita: `'Dados Obra '!B26` para as horas/dia.")

        equipe_editada = []
        for linha in atual.equipe:
            st.markdown(f"**{linha.descricao}**")
            colunas = st.columns(5)
            with colunas[0]:
                quantidade = _numero(
                    "Nº Func.", linha.quantidade, f"desmob_draga_{linha.id}_quantidade"
                )
            with colunas[1]:
                custo = _numero("R$/h", linha.custo_hora, f"desmob_draga_{linha.id}_custo")
            with colunas[2]:
                st.metric("Hrs/dia", "Pendente" if horas is None else f"{horas:g} h")
            with colunas[3]:
                encargos = _numero(
                    "L.Sociais (%)", linha.encargos_sociais,
                    f"desmob_draga_{linha.id}_encargos",
                )
            with colunas[4]:
                st.metric("Total", _moeda(mao_obra[linha.id].total))
            equipe_editada.append(LinhaMaoObraDesmobilizacao(
                linha.id, linha.descricao, quantidade, custo, encargos
            ))

        apoio = st.columns(3)
        with apoio[0]:
            custo_refeicao = _numero(
                "Refeições — R$/un.", atual.custo_refeicao, "desmob_draga_refeicao"
            )
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[1]:
            custo_transporte = _numero(
                "Transporte — R$/un.", atual.custo_transporte, "desmob_draga_transporte"
            )
            st.metric("Quantidade", f"{resultados.quantidade_pessoas:g}")
        with apoio[2]:
            st.metric("Custo por dia", _moeda(resultados.custo_por_dia))

        st.markdown("**Descrição dos serviços**")
        itens_editados = []
        for item in atual.itens:
            numero = "" if item.numero is None else f"{item.numero}. "
            st.markdown(f"{numero}{item.descricao} — {item.unidade}")
            colunas = st.columns(4)
            with colunas[0]:
                quantidade = _numero(
                    "Quantidade", item.quantidade, f"desmob_draga_{item.id}_quantidade"
                )
            with colunas[1]:
                if item.preco_unitario_custo_diario:
                    preco = None
                    st.metric("Preço Unit.", _moeda(itens[item.id].preco_unitario or 0))
                else:
                    preco = _numero(
                        "Preço Unit.", item.preco_unitario_manual,
                        f"desmob_draga_{item.id}_preco_unitario",
                    )
            with colunas[2]:
                st.metric("Preço Total", _moeda(itens[item.id].preco_total))
            with colunas[3]:
                observacao = st.text_input(
                    "Observação/Fonte", value=item.observacao,
                    key=f"desmob_draga_{item.id}_observacao",
                )
            itens_editados.append(ItemDesmobilizacaoDraga(
                item.id, item.numero, item.descricao, item.unidade,
                quantidade, preco, item.preco_unitario_custo_diario, observacao,
            ))

        bdi = _numero("BDI (%)", atual.bdi, "desmob_draga_bdi")
        metricas = st.columns(3)
        with metricas[0]:
            st.metric("TOTAL", _moeda(resultados.total_composicao))
        with metricas[1]:
            st.metric("Valor BDI", _moeda(resultados.valor_bdi))
        with metricas[2]:
            st.metric("Preço Final", _moeda(resultados.preco_final))
        submetido = st.form_submit_button("Salvar Desmobilização da Draga")

    if not submetido:
        return
    try:
        desmobilizacao = DesmobilizacaoDraga(
            tuple(equipe_editada), custo_refeicao, custo_transporte,
            tuple(itens_editados), bdi,
        )
    except ValueError as erro:
        st.error(str(erro))
        return
    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_desmobilizacao_draga(copia_versao, desmobilizacao)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_desmob_draga_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
