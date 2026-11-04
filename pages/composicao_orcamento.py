"""Primeira tela da composição: identificação, sem alterar módulos legados.

Nesta entrega, os dados ficam apenas na sessão Streamlit. Persistência e
duplicação de propostas serão implementadas após validar o armazenamento.
"""

from datetime import date
from modulos.composicao_orcamento import cotacoes_etapa2

import streamlit as st
from services.ui import renderizar_cabecalho_modulo
from services.autorizacao import pode_consultar_fonte_composicao
from services.composicao_fontes import consultar_catalogo, listar_opcoes, contatos_do_cliente


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
CHAVE_ETAPA = "_composicao_orcamento_etapa_atual"


def _voltar_menu():
    st.session_state.tela = "menu"
    st.rerun()


def _renderizar_guia_etapas(etapa=1):
    """Guia compacto: 17 etapas numa linha, sem simular etapas concluídas."""
    numeros = "".join(
        '<span class="fos-etapa fos-etapa-atual" aria-current="step" '
        f'title="Etapa {etapa}: atual">{etapa}</span>'
        if numero == etapa else
        f'<span class="fos-etapa fos-etapa-futura" '
        f'title="Etapa {numero}: ainda não disponível">{numero}</span>'
        for numero in range(1, 18)
    )
    legenda = ("Identificação da obra" if etapa == 1 else "Cotações")
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
          <div class="fos-guia-legenda"><strong>Etapa """ + str(etapa) + """ de 17 —
          """ + legenda + """</strong></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _fontes_autorizadas():
    """Permissão de leitura restrita ao fluxo de composição de orçamento."""
    return {fonte: pode_consultar_fonte_composicao(fonte)
            for fonte in ("clientes", "contatos", "materiais", "horarios", "regimes")}


def _carregar_fontes():
    autorizadas = _fontes_autorizadas()
    try:
        token, repo = st.secrets["GITHUB_TOKEN"], st.secrets["REPO"]
    except (KeyError, AttributeError):
        st.error("Configuração de consulta indisponível.")
        return {}
    leituras = {}
    for fonte, permitido in autorizadas.items():
        if not permitido:
            st.warning(f"Sem permissão de leitura para o cadastro: {fonte}.")
            continue
        try:
            resultado = consultar_catalogo(fonte, token, repo)
        except Exception:
            st.warning(f"Não foi possível consultar o cadastro {fonte}.")
            continue
        if not resultado.disponivel:
            st.warning(f"Cadastro {fonte} indisponível: {resultado.erro}")
        else:
            leituras[fonte] = resultado
    return leituras


def _selecionar_catalogo(rotulo, fonte, coluna, leituras, valor_anterior, chave):
    catalogo = leituras.get(fonte)
    if catalogo is None:
        st.text_input(rotulo, value=str(valor_anterior or ""), disabled=True,
                      help="Cadastro indisponível ou sem autorização.")
        return str(valor_anterior or "")
    opcoes = listar_opcoes(catalogo, coluna)
    if valor_anterior and valor_anterior not in opcoes:
        st.warning(f"{rotulo}: valor anterior não está mais no cadastro. Revise antes de salvar.")
        opcoes = [valor_anterior] + opcoes
    opcoes = [""] + [v for v in opcoes if v]
    return st.selectbox(rotulo, opcoes,
                        index=opcoes.index(valor_anterior) if valor_anterior in opcoes else 0,
                        format_func=lambda v: v or "Selecione...")


def _selecionar_cliente_contato(leituras, anterior):
    clientes, contatos = leituras.get("clientes"), leituras.get("contatos")
    if clientes is None:
        st.text_input("Cliente (CRM)", value=str(anterior.get("cliente", "")), disabled=True)
        st.text_input("Contato (CRM)", value=str(anterior.get("contato", "")), disabled=True)
        return {"cliente": anterior.get("cliente", ""), "contato": anterior.get("contato", ""),
                "id_cliente": anterior.get("id_cliente", ""), "id_contato": anterior.get("id_contato", "")}, False
    df = clientes.dados
    ids = [str(v).strip() for v in df["id_cliente"]]
    if not all(ids) or len(ids) != len(set(ids)):
        st.error("CRM com IDs de cliente vazios ou duplicados. Corrija o cadastro antes de selecionar.")
        return {}, False
    nomes = dict(zip(ids, df["nome_empresa"].astype(str)))
    selecionados = [""] + sorted(ids, key=lambda v: nomes[v].casefold())
    id_anterior = str(anterior.get("id_cliente", ""))
    if id_anterior and id_anterior not in selecionados:
        st.error("Cliente do rascunho não está mais disponível no CRM.")
        return {}, False
    id_cliente = st.selectbox("Cliente (CRM oficial)", selecionados,
        index=selecionados.index(id_anterior), format_func=lambda v: nomes.get(v, "Selecione..."),
         )
    id_contato, nome_contato = "", ""
    if id_cliente and contatos is not None:
        df_contatos = contatos_do_cliente(clientes, contatos, id_cliente)
        contato_ids = [str(v).strip() for v in df_contatos["id_contato"]]
        if not all(contato_ids) or len(contato_ids) != len(set(contato_ids)):
            st.error("CRM com IDs de contato vazios ou duplicados.")
            return {}, False
        nomes_contatos = dict(zip(contato_ids, df_contatos["nome_contato"].astype(str)))
        opcoes = [""] + sorted(contato_ids, key=lambda v: nomes_contatos[v].casefold())
        anterior_contato = str(anterior.get("id_contato", ""))
        # Troca de cliente limpa o contato anterior, sem reutilizar contato de outra empresa.
        if anterior_contato not in opcoes:
            anterior_contato = ""
        id_contato = st.selectbox("Contato (CRM)", opcoes,
            index=opcoes.index(anterior_contato),
            format_func=lambda v: nomes_contatos.get(v, "Sem contato selecionado"),
             )
        nome_contato = nomes_contatos.get(id_contato, "")
    else:
        st.caption("Selecione o cliente para consultar seus contatos.")
    return {"cliente": nomes.get(id_cliente, ""), "contato": nome_contato,
            "id_cliente": id_cliente, "id_contato": id_contato}, bool(id_cliente)


def render():
    renderizar_cabecalho_modulo(
        "Composição de Orçamento",
        "← TELA INICIAL",
        _voltar_menu,
        key="composicao_orcamento_voltar_menu",
    )
    etapa = st.session_state.get(CHAVE_ETAPA, 1)
    _renderizar_guia_etapas(etapa)
    if etapa == 2:
        cotacoes_etapa2.render()
        if st.button("← Voltar à Etapa 1", use_container_width=True):
            st.session_state[CHAVE_ETAPA] = 1
            st.rerun()
        return
    st.info(
        "Primeira versão para validação. Os dados são mantidos somente nesta "
        "sessão do navegador; ainda não são gravados no banco operacional."
    )
    anterior = st.session_state.get(CHAVE_RASCUNHO, {})
    leituras = _carregar_fontes()
    st.markdown("### Cliente e contato — CRM")
    dados_crm, cliente_valido = _selecionar_cliente_contato(leituras, anterior)
    st.markdown(
        "<style>div[data-testid='stForm'] {max-width: 760px;}"
        "div[data-testid='stForm'] label {font-size: 1.05rem;}"
        "</style>",
        unsafe_allow_html=True,
    )
    with st.form("composicao_etapa1_formulario"):
        valores = dict(dados_crm)
        for titulo, campos in SECOES:
            st.markdown(f"### {titulo}")
            for chave, rotulo, tipo in campos:
                if chave in {"cliente", "contato"}:
                    continue
                if chave == "tipo_material":
                    valores[chave] = _selecionar_catalogo(rotulo, "materiais", "Material", leituras,
                        anterior.get(chave, ""), "composicao_material")
                elif chave == "horario_trabalho":
                    horarios = leituras.get("horarios")
                    if horarios is not None:
                        opcoes_horario = [f"{linha.Inicio} - {linha.Fim}" for linha in horarios.dados.itertuples(index=False)]
                        opcoes_horario = sorted(set(opcoes_horario))
                        anterior_horario = str(anterior.get(chave, ""))
                        if anterior_horario and anterior_horario not in opcoes_horario:
                            opcoes_horario.insert(0, anterior_horario)
                        opcoes_horario = [""] + opcoes_horario
                        valores[chave] = st.selectbox(rotulo, opcoes_horario,
                            index=opcoes_horario.index(anterior_horario) if anterior_horario in opcoes_horario else 0,
                             )
                    else:
                        valores[chave] = st.text_input(rotulo, value=str(anterior.get(chave, "")), disabled=True)
                elif tipo == "data":
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
            if titulo.startswith("5."):
                valores["regime_trabalho"] = _selecionar_catalogo(
                    "Regime de trabalho", "regimes", "Descricao", leituras,
                    anterior.get("regime_trabalho", ""), "composicao_regime")
            if titulo.startswith("3."):
                recalque_total = (
                    valores["recalque_terra"] + valores["recalque_flutuante"]
                )
                st.metric("Distância total de recalque (m)", f"{recalque_total:,.2f}")
            st.divider()
        salvar = st.form_submit_button(
            "Guardar rascunho nesta sessão", use_container_width=True
        )
    if salvar and not cliente_valido:
        st.error("Selecione um cliente válido do CRM antes de guardar o rascunho.")
    elif salvar:
        valores["origem_cliente"] = "crm"
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
            "Próxima etapa →", disabled=not bool(st.session_state.get(CHAVE_RASCUNHO)),
            on_click=lambda: st.session_state.__setitem__(CHAVE_ETAPA, 2),
            use_container_width=True,
            help="Guarde o rascunho da Etapa 1 para avançar.",
        )
    st.divider()
    st.caption(
        "Próximas etapas e exportação Excel com fórmulas serão liberadas "
        "gradualmente, após validação das regras de cálculo."
    )
