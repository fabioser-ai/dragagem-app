"""Edição explícita de identificação e premissas, sem rede durante digitação."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.premissas import (
    RascunhoPremissa,
    aplicar_rascunho,
    atualizar_identificacao,
)
from modulos.orcamentos.dominio.estados import EstadoCenario
from modulos.orcamentos.dominio.premissas import OrigemPremissa
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _rotulo_cenario(cenario):
    return cenario.nome


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    """Renderiza rascunho local e persiste apenas na confirmação explícita."""

    ativos = [item for item in versao.cenarios if item.estado is EstadoCenario.ATIVO]
    st.subheader("Identificação e premissas")

    if versao.premissas:
        st.dataframe(
            [
                {
                    "Cenário": str(cenario_id),
                    "Premissa": premissa.conceito,
                    "Sugerido": premissa.sugerido.valor if premissa.sugerido else "",
                    "Adotado": premissa.adotado.valor if premissa.adotado else "Pendente",
                    "Unidade": (
                        premissa.adotado.unidade
                        if premissa.adotado
                        else premissa.sugerido.unidade
                    ),
                    "Origem": premissa.adotado.origem.value if premissa.adotado else "sugestão",
                }
                for cenario_id, premissa in versao.premissas
            ],
            hide_index=True,
            use_container_width=True,
        )

    with st.form("novo_orcamento_form_premissas"):
        objeto = st.text_input("Objeto", value=orcamento.objeto)
        finalidade = st.text_input("Finalidade", value=orcamento.finalidade)
        responsavel = st.text_input("Responsável", value=orcamento.responsavel)

        st.markdown("**Nova revisão de premissa — opcional**")
        cenario = st.selectbox(
            "Cenário",
            options=ativos,
            format_func=_rotulo_cenario,
            disabled=not ativos,
        )
        conceito = st.text_input("Conceito da premissa")
        unidade = st.text_input("Unidade")
        sugerido = st.text_input("Valor sugerido")
        adotado = st.text_input("Valor adotado")
        origem = st.selectbox(
            "Origem do valor adotado",
            options=[
                OrigemPremissa.ENGENHARIA,
                OrigemPremissa.CLIENTE,
                OrigemPremissa.MANUAL,
            ],
            format_func=lambda item: item.value.title(),
        )
        vigencia = st.text_input("Vigência ou data-base")
        justificativa = st.text_area("Justificativa")
        salvar = st.form_submit_button("Salvar identificação e premissas")

    if not salvar:
        return

    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    identificacao = atualizar_identificacao(
        copia_orcamento,
        copia_versao,
        objeto=objeto,
        finalidade=finalidade,
        responsavel=responsavel,
    )
    if not identificacao.sucesso:
        st.error(identificacao.erro)
        return

    informou_premissa = any(
        isinstance(valor, str) and valor.strip()
        for valor in (conceito, unidade, sugerido, adotado, vigencia, justificativa)
    )
    if informou_premissa:
        if not ativos or cenario is None:
            st.error("A versão precisa possuir um cenário ativo para receber premissas.")
            return
        resultado_premissa = aplicar_rascunho(
            copia_versao,
            cenario.id,
            RascunhoPremissa(
                conceito=conceito,
                unidade=unidade,
                autor=copia_versao.autor,
                valor_sugerido=sugerido or None,
                valor_adotado=adotado or None,
                origem_adotada=origem,
                vigencia=vigencia or None,
                justificativa=justificativa or None,
            ),
        )
        if not resultado_premissa.sucesso:
            st.error(resultado_premissa.erro)
            return

    indice = repositorio.carregar_indice_bruto()
    if not indice.sucesso:
        st.error("Não foi possível preparar o índice para salvamento.")
        return
    persistencia = repositorio.persistir_versao(
        copia_orcamento,
        copia_versao,
        indice.valor,
        snapshot_esperado,
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.success("Identificação e premissas salvas.")
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. O rascunho remoto não foi alterado.")
