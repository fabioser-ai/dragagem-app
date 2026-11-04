"""Primeira tela da composição: identificação, sem alterar módulos legados.

Nesta entrega, os dados ficam apenas na sessão Streamlit. Persistência e
duplicação de propostas serão implementadas após validar o armazenamento.
"""

from datetime import date

import streamlit as st
from services.ui import renderizar_cabecalho_modulo


SECOES = (
    ("1. Dados da proposta", (
        ("numero_proposta", "Número da proposta", "texto"),
        ("data_composicao", "Data da composição", "data"),
        ("cliente", "Cliente", "texto"),
        ("contato", "Contato", "texto"),
    )),
    ("2. Características da obra", (
        ("objeto_obra", "Objeto da obra", "longo"),
        ("local", "Local da obra", "texto"),
        ("tipo_material", "Tipo de material", "texto"),
    )),
    ("3. Parâmetros de dragagem", (
        ("volume_dragagem", "Volume de dragagem (m³)", "numero"),
        ("profundidade_dragagem", "Profundidade de dragagem (m)", "numero"),
        ("espessura_media", "Espessura média do material (m)", "numero"),
        ("recalque_terra", "Recalque em terra (m)", "numero"),
        ("recalque_flutuante", "Recalque flutuante (m)", "numero"),
    )),
    ("4. Condições de execução", (
        ("tipo_bota_fora", "Tipo de bota-fora", "texto"),
        ("sistema_medicao", "Sistema de medição", "texto"),
        ("canteiro_obra", "Canteiro de obra", "texto"),
        ("mobilizacao", "Mobilização", "texto"),
    )),
    ("5. Jornada e prazo", (
        ("horario_trabalho", "Horário de trabalho", "texto"),
        ("dias_trabalho", "Dias de trabalho", "numero"),
    )),
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
    st.markdown(
        "<style>div[data-testid='stForm'] {max-width: 760px;}"
        "div[data-testid='stForm'] label {font-size: 1.05rem;}"
        "</style>",
        unsafe_allow_html=True,
    )
    with st.form("composicao_etapa1_formulario"):
        valores = {}
        for titulo, campos in SECOES:
            st.markdown(f"### {titulo}")
            for chave, rotulo, tipo in campos:
                if tipo == "data":
                    valores[chave] = st.date_input(
                        rotulo,
                        value=date.fromisoformat(anterior["data_composicao"])
                        if anterior.get("data_composicao") else date.today(),
                    )
                elif tipo == "texto":
                    valores[chave] = st.text_input(
                        rotulo, value=str(anterior.get(chave, ""))
                    )
                elif tipo == "longo":
                    valores[chave] = st.text_area(
                        rotulo, value=str(anterior.get(chave, "")), height=100
                    )
                else:
                    valores[chave] = st.number_input(
                        rotulo, min_value=0.0,
                        value=float(anterior.get(chave, 0.0)),
                        step=1.0, format="%.2f",
                    )
            if titulo.startswith("3."):
                recalque_total = (
                    valores["recalque_terra"] + valores["recalque_flutuante"]
                )
                st.metric("Distância total de recalque (m)", f"{recalque_total:,.2f}")
            st.divider()
        salvar = st.form_submit_button(
            "Guardar rascunho nesta sessão", use_container_width=True
        )
    if salvar:
        valores["data_composicao"] = valores["data_composicao"].isoformat()
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
