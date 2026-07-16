"""Representação funcional da aba Produção do Excel oficial."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.producao import salvar_producao
from modulos.orcamentos.dominio.producao import Producao, calcular_producao
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _numero(rotulo, valor, unidade, chave):
    return st.number_input(
        f"{rotulo} ({unidade})",
        value=valor,
        min_value=0.0,
        key=chave,
    )


def _exibir_valor(valor, unidade, casas=2):
    if valor is None:
        return "Pendente"
    return f"{valor:.{casas}f} {unidade}"


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_producao_salva", False):
        st.success("Produção salva.")
    atual = versao.producao
    dados_obra = versao.dados_obra
    horas_dia = dados_obra.horario_trabalho if dados_obra else None
    dias_mes = dados_obra.dias_trabalho if dados_obra else None
    volume = dados_obra.volume_dragagem if dados_obra else None
    resultados = calcular_producao(atual, horas_dia, dias_mes, volume)

    with st.form("producao_formulario"):
        st.subheader("Cálculo de Produção da Draga")
        vazao = _numero("Vazão", atual.vazao, "m³/h", "producao_vazao")
        eficiencia = _numero(
            "Eficiência", atual.eficiencia, "%", "producao_eficiencia"
        )
        concentracao = _numero(
            "Concentração", atual.concentracao, "%", "producao_concentracao"
        )

        st.subheader("Horas Trabalhadas por mês")
        premissas = st.columns(3)
        with premissas[0]:
            st.metric("Horas por dia", _exibir_valor(horas_dia, "h/dia"))
        with premissas[1]:
            st.metric("Dias por mês", _exibir_valor(dias_mes, "dias/mês"))
        with premissas[2]:
            st.metric("Volume total a dragar", _exibir_valor(volume, "m³"))

        st.subheader("Resultados")
        metricas = st.columns(4)
        with metricas[0]:
            st.metric(
                "Produção horária",
                _exibir_valor(resultados.producao_horaria, "m³/h"),
            )
        with metricas[1]:
            st.metric(
                "Total de horas por mês",
                _exibir_valor(resultados.horas_mensais, "h/mês"),
            )
        with metricas[2]:
            st.metric(
                "Produção mensal",
                _exibir_valor(resultados.producao_mensal, "m³/mês"),
            )
        with metricas[3]:
            st.metric(
                "Prazo de execução",
                _exibir_valor(resultados.prazo_meses, "meses", casas=6),
            )
        submetido = st.form_submit_button("Salvar Produção")

    if not submetido:
        return

    try:
        producao = Producao(vazao, eficiencia, concentracao)
    except ValueError as erro:
        st.error(str(erro))
        return
    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_producao(copia_versao, producao)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_producao_salva"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
