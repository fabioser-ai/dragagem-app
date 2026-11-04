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


def _renderizar_guia_etapas():
    """Guia compacto: 17 etapas numa linha, sem simular etapas concluídas."""
    numeros = "".join(
        '<span class="fos-etapa fos-etapa-atual" aria-current="step" '
        'title="Etapa 1: Identificação da obra">1</span>'
        if numero == 1 else
        f'<span class="fos-etapa fos-etapa-futura" '
        f'title="Etapa {numero}: ainda não disponível">{numero}</span>'
        for numero in range(1, 18)
    )
    st.markdown(
        """
        <style>
        .fos-guia {max-width: 900px; margin: 0.5rem 0 1rem;}
        .fos-etapas {display: flex; flex-wrap: nowrap; gap: 4px; width: 100%;}
        .fos-etapa {flex: 1 1 0; min-width: 0; text-align: center;
            border: 1px solid #c5cbd1; border-radius: 5px;
            padding: 8px 0; font-size: 0.85rem; font-weight: 600;}
        .fos-etapa-atual {background: #176a4d; color: white;
            border-color: #176a4d;}
        .fos-etapa-futura {background: transparent; color: inherit; opacity: .55;}
        .fos-guia-legenda {margin-top: 8px; font-size: .95rem;}
        </style>
        <div class="fos-guia" aria-label="Progresso da composição de orçamento">
          <div class="fos-etapas">
        """ + numeros + """
          </div>
          <div class="fos-guia-legenda"><strong>Etapa 1 de 17 —
          Identificação da obra</strong></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render():
    renderizar_cabecalho_modulo(
        "Composição de Orçamento",
        "← TELA INICIAL",
        _voltar_menu,
        key="composicao_orcamento_voltar_menu",
    )
    _renderizar_guia_etapas()
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
    col_anterior, col_proxima = st.columns(2)
    with col_anterior:
        st.button("← Etapa anterior", disabled=True, use_container_width=True)
    with col_proxima:
        st.button(
            "Próxima etapa →", disabled=True, use_container_width=True,
            help="A Etapa 2 será habilitada quando sua interface estiver pronta.",
        )
    st.divider()
    st.caption(
        "Próximas etapas e exportação Excel com fórmulas serão liberadas "
        "gradualmente, após validação das regras de cálculo."
    )
