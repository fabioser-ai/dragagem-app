"""Representação funcional da aba ``Dados Obra`` do Excel oficial."""

from copy import deepcopy

import streamlit as st

from modulos.orcamentos.aplicacao.dados_obra import salvar_dados_obra
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.persistencia.contratos import StatusPersistencia


def _numero(rotulo, valor, *, key):
    return st.number_input(rotulo, value=valor, format="%.2f", key=key)


def _montar_dados(valores):
    return DadosObra(**valores)


def _preencher_formulario(atual):
    st.subheader("Dados Obra")
    st.markdown(
        '<span style="color:#0000ff">Azul: Dados a serem preenchidos</span><br>'
        '<span style="color:#ff0000">Vermelho: Informações pendentes</span><br>'
        '<span style="color:#000000">Preto: resultados automáticos</span>',
        unsafe_allow_html=True,
    )

    proposta_col, data_col = st.columns([3, 1])
    with proposta_col:
        proposta = st.text_input("Proposta", value=atual.proposta, key="dados_obra_proposta")
    with data_col:
        data = st.date_input("Data", value=atual.data, key="dados_obra_data")

    cliente = st.text_input("Cliente", value=atual.cliente, key="dados_obra_cliente")
    contato_col, email_col = st.columns(2)
    with contato_col:
        contato = st.text_input("Contato", value=atual.contato, key="dados_obra_contato")
    with email_col:
        email = st.text_input("e-mail", value=atual.email, key="dados_obra_email")

    st.markdown("**Dados da obra**")
    objeto = st.text_area("Objeto", value=atual.objeto, key="dados_obra_objeto")
    local = st.text_input("Local", value=atual.local, key="dados_obra_local")
    volume_dragagem = _numero(
        "Volume dragagem (m³)", atual.volume_dragagem, key="dados_obra_volume_dragagem"
    )
    tipo_material = st.text_input(
        "Tipo de material", value=atual.tipo_material, key="dados_obra_tipo_material"
    )

    recalque, seio_recalque_col, total_recalque_col = st.columns([2, 2, 1])
    with recalque:
        distancia_recalque = _numero(
            "Distância de Recalque (m)",
            atual.distancia_recalque,
            key="dados_obra_distancia_recalque",
        )
    with seio_recalque_col:
        seio_recalque = _numero(
            "Seio da linha  =", atual.seio_recalque, key="dados_obra_seio_recalque"
        )

    flutuante, seio_flutuante_col, total_flutuante_col = st.columns([2, 2, 1])
    with flutuante:
        linha_flutuante = _numero(
            "Linha Flutuante (m)", atual.linha_flutuante, key="dados_obra_linha_flutuante"
        )
    with seio_flutuante_col:
        seio_linha_flutuante = _numero(
            "Seio da linha  =",
            atual.seio_linha_flutuante,
            key="dados_obra_seio_linha_flutuante",
        )

    linha_terra = _numero(
        "Linha de terra (m)", atual.linha_terra, key="dados_obra_linha_terra"
    )
    profundidade_dragagem = _numero(
        "Profundidade de dragagem (m)",
        atual.profundidade_dragagem,
        key="dados_obra_profundidade_dragagem",
    )
    espessura_media = _numero(
        "Espessura média de dragagem (m)",
        atual.espessura_media,
        key="dados_obra_espessura_media",
    )
    comprimento_col, x_col, largura_col, volume_col = st.columns([2, 0.4, 2, 1.4])
    with comprimento_col:
        area_comprimento = _numero(
            "Área de Dragagem (m² ou L x C)",
            atual.area_comprimento,
            key="dados_obra_area_comprimento",
        )
    with x_col:
        st.markdown("<br><div style='text-align:center'>X</div>", unsafe_allow_html=True)
    with largura_col:
        area_largura = _numero(" ", atual.area_largura, key="dados_obra_area_largura")

    valores = {
        "proposta": proposta,
        "data": data,
        "cliente": cliente,
        "contato": contato,
        "email": email,
        "objeto": objeto,
        "local": local,
        "volume_dragagem": volume_dragagem,
        "tipo_material": tipo_material,
        "distancia_recalque": distancia_recalque,
        "seio_recalque": seio_recalque,
        "linha_flutuante": linha_flutuante,
        "seio_linha_flutuante": seio_linha_flutuante,
        "linha_terra": linha_terra,
        "profundidade_dragagem": profundidade_dragagem,
        "espessura_media": espessura_media,
        "area_comprimento": area_comprimento,
        "area_largura": area_largura,
        "tipo_bota_fora": None,
        "sistema_medicao": None,
        "canteiro_obras": None,
        "mobilizacao": None,
        "horario_trabalho": None,
        "dias_trabalho": None,
    }
    parcial = _montar_dados(
        {
            **valores,
            "tipo_bota_fora": atual.tipo_bota_fora,
            "sistema_medicao": atual.sistema_medicao,
            "canteiro_obras": atual.canteiro_obras,
            "mobilizacao": atual.mobilizacao,
            "horario_trabalho": atual.horario_trabalho,
            "dias_trabalho": atual.dias_trabalho,
        }
    )
    with total_recalque_col:
        st.metric("Total", f"{parcial.total_recalque:.2f}")
    with total_flutuante_col:
        st.metric("Total", f"{parcial.total_linha_flutuante:.2f}")
    with volume_col:
        st.metric("Volume (m³) =", f"{parcial.volume_geometrico:.2f}")

    tipo_bota_fora = st.text_input(
        "Tipo de Bota Fora", value=atual.tipo_bota_fora, key="dados_obra_tipo_bota_fora"
    )
    sistema_medicao = st.text_input(
        "Sistema de Medição", value=atual.sistema_medicao, key="dados_obra_sistema_medicao"
    )
    canteiro_obras = st.text_input(
        "Canteiro de obras", value=atual.canteiro_obras, key="dados_obra_canteiro_obras"
    )
    mobilizacao = st.text_input(
        "Mobilização", value=atual.mobilizacao, key="dados_obra_mobilizacao"
    )
    horario_col, dias_col = st.columns(2)
    with horario_col:
        horario_trabalho = _numero(
            "Horário de Trabalho  (das 7 as 17h)",
            atual.horario_trabalho,
            key="dados_obra_horario_trabalho",
        )
        st.caption("h/dia")
    with dias_col:
        dias_trabalho = _numero(
            "Dias de Trabalho (2ª a 6ª)",
            atual.dias_trabalho,
            key="dados_obra_dias_trabalho",
        )
        st.caption("dias/mês")

    submetido = st.form_submit_button("Salvar Dados Obra")

    dados = _montar_dados(
        {
            **valores,
            "tipo_bota_fora": tipo_bota_fora,
            "sistema_medicao": sistema_medicao,
            "canteiro_obras": canteiro_obras,
            "mobilizacao": mobilizacao,
            "horario_trabalho": horario_trabalho,
            "dias_trabalho": dias_trabalho,
        }
    )
    return submetido, dados


def render(*, repositorio, orcamento, versao, snapshot_esperado):
    """Exibe somente os campos e os três cálculos existentes na planilha."""
    if st.session_state.pop("novo_orcamento_dados_obra_salvos", False):
        st.success("Dados Obra salvos.")
    atual = versao.dados_obra or DadosObra()
    with st.form("dados_obra_formulario"):
        submetido, dados = _preencher_formulario(atual)

    if not submetido:
        return

    copia_orcamento, copia_versao = deepcopy((orcamento, versao))
    copia_orcamento.objeto = dados.objeto.strip() or "Novo orçamento"
    resultado = salvar_dados_obra(copia_versao, dados)
    if not resultado.sucesso:
        st.error(resultado.erro)
        return
    indice = repositorio.carregar_indice_bruto()
    if not indice.sucesso:
        st.error("Não foi possível preparar o índice para salvamento.")
        return
    persistencia = repositorio.persistir_versao(
        copia_orcamento, copia_versao, indice.valor, snapshot_esperado
    )
    if persistencia.sucesso:
        st.session_state["novo_orcamento_detalhe"] = (copia_orcamento, copia_versao)
        st.session_state["novo_orcamento_snapshot"] = persistencia.commit_sha
        st.session_state["novo_orcamento_dados_obra_salvos"] = True
        st.rerun()
    elif persistencia.status is StatusPersistencia.BRANCH_AVANCADA:
        st.error("O orçamento foi alterado por outra operação. Reabra a versão antes de salvar.")
    else:
        st.error("Não foi possível salvar. A versão remota não foi alterada.")
