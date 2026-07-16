"""Edição local dos itens mutáveis da aba Cotações."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.cotacoes import salvar_cotacoes
from modulos.orcamentos.dominio.cotacoes import (
    Cotacoes,
    ItemCotacao,
    PropostaFornecedor,
)
from modulos.orcamentos.persistencia.contratos import StatusPersistencia

CHAVE_EDICAO = "novo_orcamento_cotacoes_edicao"
CHAVE_VERSAO = "novo_orcamento_cotacoes_versao_id"


def _texto(rotulo, valor, chave, *, oculto=False):
    return st.text_input(
        rotulo,
        value=valor,
        key=chave,
        label_visibility="collapsed" if oculto else "visible",
    )


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


def _cotacoes_em_edicao(versao):
    versao_id = str(versao.id)
    if st.session_state.get(CHAVE_VERSAO) != versao_id:
        st.session_state[CHAVE_VERSAO] = versao_id
        st.session_state[CHAVE_EDICAO] = versao.cotacoes
    return st.session_state[CHAVE_EDICAO]


def _cabecalho(item):
    colunas = ("NOME", "CONTATO", "TELEFONE", "DETALHE", item.rotulo_primeiro_valor)
    if item.rotulo_segundo_valor:
        colunas += (item.rotulo_segundo_valor,)
    colunas += ("AÇÕES",)
    celulas = st.columns(len(colunas))
    for celula, titulo in zip(celulas, colunas):
        with celula:
            st.markdown(f"**{titulo}**")
    return len(colunas)


def _proposta(item, indice, proposta, quantidade_colunas):
    prefixo = f"cot_{item.id}_{indice}"
    colunas = st.columns(quantidade_colunas)
    with colunas[0]:
        nome = _texto("Nome", proposta.nome, f"{prefixo}_nome", oculto=True)
    with colunas[1]:
        contato = _texto("Contato", proposta.contato, f"{prefixo}_contato", oculto=True)
    with colunas[2]:
        telefone = _texto("Telefone", proposta.telefone, f"{prefixo}_telefone", oculto=True)
    with colunas[3]:
        detalhe = _texto("Detalhe", proposta.detalhe, f"{prefixo}_detalhe", oculto=True)
    with colunas[4]:
        primeiro = _dinheiro(
            item.rotulo_primeiro_valor,
            proposta.primeiro_valor,
            f"{prefixo}_primeiro",
        )
    proxima = 5
    segundo = None
    if item.rotulo_segundo_valor:
        with colunas[proxima]:
            segundo = _dinheiro(
                item.rotulo_segundo_valor,
                proposta.segundo_valor,
                f"{prefixo}_segundo",
            )
        proxima += 1
    with colunas[proxima]:
        remover = st.checkbox("Remover", key=f"{prefixo}_remover")
        confirmar = True
        if proposta.preenchida:
            confirmar = st.checkbox(
                "Confirmar exclusão dos dados",
                key=f"{prefixo}_confirmar",
            )
    return (
        PropostaFornecedor(nome, contato, telefone, detalhe, primeiro, segundo),
        remover,
        confirmar,
    )


def _item(item):
    st.markdown(f"### {item.nome}")
    metadados = st.columns(3)
    with metadados[0]:
        nome = _texto("Nome do item", item.nome, f"cot_{item.id}_nome_item")
    with metadados[1]:
        primeiro = _texto(
            "Rótulo do primeiro valor",
            item.rotulo_primeiro_valor,
            f"cot_{item.id}_rotulo_primeiro",
        )
    with metadados[2]:
        segundo = _texto(
            "Rótulo do segundo valor (opcional)",
            item.rotulo_segundo_valor or "",
            f"cot_{item.id}_rotulo_segundo",
        )
    quantidade_colunas = _cabecalho(item)
    propostas = []
    bloqueios = []
    for indice, proposta in enumerate(item.propostas):
        editada, remover, confirmar = _proposta(
            item, indice, proposta, quantidade_colunas
        )
        if remover:
            if proposta.preenchida and not confirmar:
                bloqueios.append(
                    f"Confirme a remoção da proposta preenchida em {item.nome}."
                )
            else:
                continue
        propostas.append(editada)

    adicionar_proposta = st.checkbox(
        "Adicionar proposta de fornecedor",
        key=f"cot_{item.id}_adicionar_proposta",
    )
    if adicionar_proposta:
        propostas.append(PropostaFornecedor())

    remover_item = st.checkbox(
        "Remover item de cotação",
        key=f"cot_{item.id}_remover_item",
    )
    confirmar_item = True
    if item.preenchido:
        confirmar_item = st.checkbox(
            "Confirmar exclusão do item e de suas propostas preenchidas",
            key=f"cot_{item.id}_confirmar_item",
        )
    if remover_item and item.preenchido and not confirmar_item:
        bloqueios.append(f"Confirme a remoção do item preenchido {item.nome}.")

    editado = (
        item
        if remover_item
        else ItemCotacao(item.id, nome, primeiro, segundo or None, tuple(propostas))
    )
    return editado, remover_item, bloqueios


def _formulario(cotacoes):
    itens = []
    bloqueios = []
    for item in cotacoes.itens:
        editado, remover, erros = _item(item)
        bloqueios.extend(erros)
        if not remover:
            itens.append(editado)

    st.markdown("### Adicionar item de cotação")
    colunas = st.columns(3)
    with colunas[0]:
        novo_nome = _texto("Nome do item", "", "cot_novo_item_nome")
    with colunas[1]:
        novo_primeiro = _texto(
            "Rótulo do primeiro valor", "", "cot_novo_item_primeiro"
        )
    with colunas[2]:
        novo_segundo = _texto(
            "Rótulo do segundo valor (opcional)", "", "cot_novo_item_segundo"
        )
    adicionar_item = st.checkbox("Adicionar este item", key="cot_adicionar_item")
    if adicionar_item:
        try:
            itens.append(ItemCotacao.novo(novo_nome, novo_primeiro, novo_segundo or None))
        except ValueError as erro:
            bloqueios.append(str(erro))

    aplicar = st.form_submit_button("Aplicar alterações")
    salvar = st.form_submit_button("Salvar Cotações")
    return Cotacoes(tuple(itens)), bloqueios, aplicar, salvar


def _atualizar_localmente(orcamento, versao, cotacoes):
    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    resultado = salvar_cotacoes(copia_versao, cotacoes)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return None
    st.session_state[CHAVE_EDICAO] = cotacoes
    st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
    return copia_orcamento, copia_versao


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    if st.session_state.pop("novo_orcamento_cotacoes_salvas", False):
        st.success("Cotações salvas.")
    atuais = _cotacoes_em_edicao(versao)
    with st.form("cotacoes_formulario"):
        st.subheader("COTAÇÕES")
        cotacoes, bloqueios, aplicar, salvar = _formulario(atuais)

    if not aplicar and not salvar:
        return
    if bloqueios:
        for mensagem in bloqueios:
            st.warning(mensagem)
        return

    atualizado = _atualizar_localmente(orcamento, versao, cotacoes)
    if atualizado is None:
        return
    copia_orcamento, copia_versao = atualizado

    if aplicar and not salvar:
        st.rerun()
        return

    persistencia = repositorio.persistir_documento_versao(
        copia_orcamento, copia_versao, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_cotacoes_salvas"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
