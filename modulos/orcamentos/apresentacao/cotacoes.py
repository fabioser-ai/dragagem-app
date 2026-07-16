"""Representação funcional da aba ``Cotaçoes`` do Excel oficial."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.cotacoes import salvar_cotacoes
from modulos.orcamentos.dominio.cotacoes import (
    CotacaoContainer,
    CotacaoGuindaste,
    CotacaoMensal,
    Cotacoes,
)
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _texto(rotulo, valor, chave):
    return st.text_input(rotulo, value=valor, key=chave, label_visibility="collapsed")


def _dinheiro(rotulo, valor, chave):
    return st.number_input(
        rotulo,
        value=valor,
        min_value=0.0,
        step=0.01,
        format="%.2f",
        key=chave,
        label_visibility="collapsed",
    )


def _cabecalho(colunas):
    celulas = st.columns(len(colunas))
    for celula, titulo in zip(celulas, colunas):
        with celula:
            st.markdown(f"**{titulo}**")


def _guindastes(linhas):
    st.markdown("### GUINDASTE")
    _cabecalho(("NOME", "CONTATO", "TELEFONE", "DETALHE", "PREÇO (hora)", "PREÇO (DIÁRIA)"))
    resultado = []
    for indice, linha in enumerate(linhas):
        colunas = st.columns(6)
        with colunas[0]:
            nome = _texto("Nome", linha.nome, f"cot_guindaste_{indice}_nome")
        with colunas[1]:
            contato = _texto("Contato", linha.contato, f"cot_guindaste_{indice}_contato")
        with colunas[2]:
            telefone = _texto("Telefone", linha.telefone, f"cot_guindaste_{indice}_telefone")
        with colunas[3]:
            detalhe = _texto("Detalhe", linha.detalhe, f"cot_guindaste_{indice}_detalhe")
        with colunas[4]:
            preco_hora = _dinheiro("Preço (hora)", linha.preco_hora, f"cot_guindaste_{indice}_hora")
        with colunas[5]:
            preco_diaria = _dinheiro(
                "Preço (diária)", linha.preco_diaria, f"cot_guindaste_{indice}_diaria"
            )
        resultado.append(CotacaoGuindaste(nome, contato, telefone, detalhe, preco_hora, preco_diaria))
    return tuple(resultado)


def _containers(linhas):
    st.markdown("### CONTAINER")
    _cabecalho(("NOME", "CONTATO", "TELEFONE", "DETALHE", "PREÇO / MÊS", "FRETE / HORA"))
    resultado = []
    for indice, linha in enumerate(linhas):
        colunas = st.columns(6)
        with colunas[0]:
            nome = _texto("Nome", linha.nome, f"cot_container_{indice}_nome")
        with colunas[1]:
            contato = _texto("Contato", linha.contato, f"cot_container_{indice}_contato")
        with colunas[2]:
            telefone = _texto("Telefone", linha.telefone, f"cot_container_{indice}_telefone")
        with colunas[3]:
            detalhe = _texto("Detalhe", linha.detalhe, f"cot_container_{indice}_detalhe")
        with colunas[4]:
            preco_mes = _dinheiro("Preço / mês", linha.preco_mes, f"cot_container_{indice}_mes")
        with colunas[5]:
            frete_hora = _dinheiro("Frete / hora", linha.frete_hora, f"cot_container_{indice}_frete")
        resultado.append(CotacaoContainer(nome, contato, telefone, detalhe, preco_mes, frete_hora))
    return tuple(resultado)


def _mensais(titulo, prefixo, linhas):
    st.markdown(f"### {titulo}")
    _cabecalho(("NOME", "CONTATO", "TELEFONE", "DETALHE", "PREÇO / MÊS"))
    resultado = []
    for indice, linha in enumerate(linhas):
        colunas = st.columns(5)
        with colunas[0]:
            nome = _texto("Nome", linha.nome, f"cot_{prefixo}_{indice}_nome")
        with colunas[1]:
            contato = _texto("Contato", linha.contato, f"cot_{prefixo}_{indice}_contato")
        with colunas[2]:
            telefone = _texto("Telefone", linha.telefone, f"cot_{prefixo}_{indice}_telefone")
        with colunas[3]:
            detalhe = _texto("Detalhe", linha.detalhe, f"cot_{prefixo}_{indice}_detalhe")
        with colunas[4]:
            preco_mes = _dinheiro("Preço / mês", linha.preco_mes, f"cot_{prefixo}_{indice}_mes")
        resultado.append(CotacaoMensal(nome, contato, telefone, detalhe, preco_mes))
    return tuple(resultado)


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_cotacoes_salvas", False):
        st.success("Cotações salvas.")
    atuais = versao.cotacoes or Cotacoes()
    with st.form("cotacoes_formulario"):
        st.subheader("COTAÇÕES")
        cotacoes = Cotacoes(
            guindaste=_guindastes(atuais.guindaste),
            container=_containers(atuais.container),
            banheiro_quimico=_mensais(
                "BANHEIRO QUIMICO", "banheiro", atuais.banheiro_quimico
            ),
            destinacao=_mensais("DESTINAÇÃO", "destinacao", atuais.destinacao),
        )
        submetido = st.form_submit_button("Salvar Cotações")

    if not submetido:
        return

    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_cotacoes(copia_versao, cotacoes)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_cotacoes_salvas"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
