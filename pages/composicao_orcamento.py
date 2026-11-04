"""Primeira tela da composição: identificação, sem alterar módulos legados.

Nesta entrega, os dados ficam apenas na sessão Streamlit. Persistência e
duplicação de propostas serão implementadas após validar o armazenamento.
"""

from datetime import date

import streamlit as st
from services.ui import renderizar_cabecalho_modulo


CAMPOS_TEXTO = (
    ("numero_proposta", "Número da proposta"),
    ("cliente", "Cliente"),
    ("contato", "Contato"),
    ("local", "Local da obra"),
    ("tipo_material", "Tipo de material"),
    ("tipo_bota_fora", "Tipo de bota-fora"),
    ("sistema_medicao", "Sistema de medição"),
    ("canteiro_obra", "Canteiro de obra"),
    ("mobilizacao", "Mobilização"),
    ("horario_trabalho", "Horário de trabalho"),
)
CAMPOS_NUMERICOS = (
    ("volume_dragagem", "Volume de dragagem (m³)"),
    ("recalque_terra", "Recalque em terra (m)"),
    ("recalque_flutuante", "Recalque flutuante (m)"),
    ("profundidade_dragagem", "Profundidade de dragagem (m)"),
    ("espessura_media", "Espessura média do material (m)"),
    ("dias_trabalho", "Dias de trabalho"),
)
CHAVE_RASCUNHO = "_composicao_orcamento_etapa1_rascunho"


def _voltar_menu():
    st.session_state.tela = "menu"
    st.rerun()


def render():
    renderizar_cabecalho_modulo(
        "Composição de Orçamento",
        "← TELA INICIAL",
        _voltar_menu,
        key="composicao_orcamento_voltar_menu",
    )
    st.caption("Etapa 1 de 17 · Identificação da obra")
    st.info(
        "Primeira versão para validação. Os dados são mantidos somente nesta "
        "sessão do navegador; ainda não são gravados no banco operacional."
    )
    anterior = st.session_state.get(CHAVE_RASCUNHO, {})
    with st.form("composicao_etapa1_formulario"):
        data_composicao = st.date_input(
            "Data da composição",
            value=date.fromisoformat(anterior["data_composicao"])
            if anterior.get("data_composicao") else date.today(),
        )
        valores = {}
        col1, col2 = st.columns(2)
        for indice, (chave, rotulo) in enumerate(CAMPOS_TEXTO):
            with (col1 if indice % 2 == 0 else col2):
                valores[chave] = st.text_input(
                    rotulo, value=str(anterior.get(chave, ""))
                )
        valores["objeto_obra"] = st.text_area(
            "Objeto da obra", value=str(anterior.get("objeto_obra", ""))
        )
        st.markdown("#### Parâmetros técnicos")
        col1, col2 = st.columns(2)
        for indice, (chave, rotulo) in enumerate(CAMPOS_NUMERICOS):
            with (col1 if indice % 2 == 0 else col2):
                valores[chave] = st.number_input(
                    rotulo,
                    min_value=0.0,
                    value=float(anterior.get(chave, 0.0)),
                    step=1.0,
                    format="%.2f",
                )
        recalque_total = (
            valores["recalque_terra"] + valores["recalque_flutuante"]
        )
        st.metric("Distância de recalque total (m)", f"{recalque_total:,.2f}")
        salvar = st.form_submit_button(
            "Guardar rascunho nesta sessão", use_container_width=True
        )
    if salvar:
        valores["data_composicao"] = data_composicao.isoformat()
        valores["distancia_recalque_total"] = recalque_total
        st.session_state[CHAVE_RASCUNHO] = valores
        st.success(
            "Rascunho guardado nesta sessão. Ainda não há salvamento permanente."
        )
    if st.session_state.get(CHAVE_RASCUNHO):
        st.caption(
            "Rascunho disponível nesta sessão. Fechar a sessão ou reiniciar "
            "o servidor pode eliminar os dados."
        )
    st.divider()
    st.caption(
        "Próximas etapas e exportação Excel com fórmulas serão liberadas "
        "gradualmente, após validação das regras de cálculo."
    )
