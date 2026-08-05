from datetime import date

import pandas as pd
import streamlit as st

from services.github import StatusLeitura
from services.autorizacao import pode, pode_acessar
from services.uniformes_epis import (
    ARQ_COMPRAS,
    ARQ_ENTREGAS,
    ARQ_ITENS,
    ARQ_MOVIMENTACOES,
    COLUNAS_COMPRAS,
    COLUNAS_ENTREGAS,
    COLUNAS_ITENS,
    COLUNAS_MOVIMENTACOES,
    cadastrar_item,
    calcular_estoque,
    calcular_posse_funcionarios,
    carregar_bases,
    historico_funcionario,
    registrar_baixa,
    registrar_compra,
    registrar_devolucao,
    registrar_entrega,
    registrar_movimentacao,
    salvar_base,
)


def _configuracao():
    return st.secrets["GITHUB_TOKEN"], st.secrets["REPO"]


def _escrita_liberada(resultado):
    return (
        resultado.pode_sobrescrever
        or resultado.status == StatusLeitura.ARQUIVO_INEXISTENTE
    )


def _detalhes(resultado):
    detalhes = resultado.erro or "Não foi possível concluir a operação."
    if resultado.http_status:
        detalhes += f" (HTTP {resultado.http_status})"
    return detalhes


def _salvar(df, arquivo, colunas, resultado_leitura, mensagem):
    if not pode(modulo="uniformes_epis", recurso="cadastros", acao="editar"):
        st.error("Operação não autorizada.")
        return False

    token, repo = _configuracao()
    resultado = salvar_base(
        df, arquivo, colunas, token, repo, resultado_leitura
    )
    if resultado.sucesso:
        st.success(mensagem)
        st.rerun()
        return True
    else:
        st.error(_detalhes(resultado))
        return False


def _rotulo_item(linha):
    detalhes = " · ".join(
        valor for valor in [
            str(linha.get("tamanho", "")).strip(),
            (
                f"CA {linha.get('ca', '')}".strip()
                if str(linha.get("ca", "")).strip()
                else ""
            ),
        ] if valor
    )
    sufixo = f" — {detalhes}" if detalhes else ""
    return f"{linha['categoria']} · {linha['nome']}{sufixo}"


def _itens_ativos(itens):
    ativos = itens[
        itens["ativo"].astype(str).str.lower().isin(["sim", "s", "1", "true"])
    ].copy()
    if not ativos.empty:
        ativos["rotulo"] = ativos.apply(_rotulo_item, axis=1)
    return ativos


def _mapa_itens(itens):
    return {
        str(linha["item_id"]): _rotulo_item(linha)
        for _, linha in itens.iterrows()
    }


def _render_resumo(itens, compras, movimentacoes, estoque):
    total_investido = (
        pd.to_numeric(compras["quantidade"], errors="coerce").fillna(0)
        * pd.to_numeric(compras["valor_unitario"], errors="coerce").fillna(0)
    ).sum()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Itens cadastrados", len(itens))
    col2.metric("Compras registradas", len(compras))
    col3.metric("Movimentações", len(movimentacoes))
    col4.metric(
        "Valor comprado",
        f"R$ {total_investido:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", "."),
    )

    st.subheader("Posição física atual")
    if estoque.empty:
        st.info("Nenhum saldo disponível. Cadastre um item e registre a primeira compra.")
        return
    st.dataframe(
        estoque[
            [
                "categoria",
                "nome",
                "tamanho",
                "ca",
                "quantidade",
                "unidade",
                "localizacao",
                "obra_id",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )


def _render_itens(itens, resultado, pode_editar):
    st.subheader("Catálogo")
    if itens.empty:
        st.info("Nenhum uniforme ou EPI cadastrado.")
    else:
        st.dataframe(
            itens[
                [
                    "categoria",
                    "nome",
                    "descricao",
                    "tamanho",
                    "ca",
                    "unidade",
                    "ativo",
                    "observacoes",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )

    with st.form("form_novo_uniforme_epi", clear_on_submit=True):
        categoria = st.selectbox("Tipo", ["Uniforme", "EPI"])
        nome = st.text_input("Nome do item")
        descricao = st.text_input("Descrição")
        col1, col2, col3 = st.columns(3)
        tamanho = col1.text_input("Tamanho")
        ca = col2.text_input("CA (Certificado de Aprovação)")
        unidade = col3.text_input("Unidade", value="un")
        observacoes = st.text_area("Observações")
        salvar = st.form_submit_button(
            "Cadastrar item",
            disabled=not pode_editar or not _escrita_liberada(resultado),
            use_container_width=True,
        )
    if salvar:
        try:
            atualizados = cadastrar_item(
                itens,
                categoria=categoria,
                nome=nome,
                descricao=descricao,
                tamanho=tamanho,
                ca=ca,
                unidade=unidade,
                observacoes=observacoes,
            )
        except ValueError as exc:
            st.error(str(exc))
        else:
            _salvar(
                atualizados,
                ARQ_ITENS,
                COLUNAS_ITENS,
                resultado,
                "Item cadastrado com sucesso.",
            )


def _render_compras(itens, compras, resultado, pode_editar):
    st.subheader("Compras")
    mapa = _mapa_itens(itens)
    exibicao = compras.copy()
    if not exibicao.empty:
        exibicao["item"] = (
            exibicao["item_id"].astype(str).map(mapa).fillna(exibicao["item_id"])
        )
        exibicao["valor_total"] = (
            pd.to_numeric(exibicao["quantidade"], errors="coerce").fillna(0)
            * pd.to_numeric(exibicao["valor_unitario"], errors="coerce").fillna(0)
        )
        st.dataframe(
            exibicao[
                [
                    "data_compra",
                    "item",
                    "fornecedor",
                    "quantidade",
                    "valor_unitario",
                    "valor_total",
                    "local_inicial",
                    "obra_id",
                    "nota_fiscal",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Nenhuma compra registrada.")

    ativos = _itens_ativos(itens)
    if ativos.empty:
        st.warning("Cadastre ao menos um item ativo antes de registrar compras.")
        return
    opcoes = ativos["item_id"].astype(str).tolist()
    rotulos = dict(zip(ativos["item_id"].astype(str), ativos["rotulo"]))
    with st.form("form_nova_compra", clear_on_submit=True):
        item_id = st.selectbox("Item", opcoes, format_func=rotulos.get)
        col1, col2 = st.columns(2)
        data_compra = col1.date_input("Data da compra", value=date.today())
        fornecedor = col2.text_input("Fornecedor")
        col3, col4 = st.columns(2)
        quantidade = col3.number_input("Quantidade", min_value=0.01, step=1.0)
        valor_unitario = col4.number_input(
            "Valor unitário (R$)", min_value=0.01, step=1.0
        )
        col5, col6 = st.columns(2)
        local_inicial = col5.text_input("Localização inicial")
        obra_id = col6.text_input("Obra / código (opcional)")
        nota_fiscal = st.text_input("Nota fiscal")
        observacoes = st.text_area("Observações")
        salvar = st.form_submit_button(
            "Registrar compra",
            disabled=not pode_editar or not _escrita_liberada(resultado),
            use_container_width=True,
        )
    if salvar:
        try:
            atualizadas = registrar_compra(
                compras,
                itens,
                item_id=item_id,
                data_compra=data_compra.isoformat(),
                fornecedor=fornecedor,
                quantidade=quantidade,
                valor_unitario=valor_unitario,
                local_inicial=local_inicial,
                obra_id=obra_id,
                nota_fiscal=nota_fiscal,
                observacoes=observacoes,
                criado_por=st.session_state.get("usuario", ""),
            )
        except ValueError as exc:
            st.error(str(exc))
        else:
            _salvar(
                atualizadas,
                ARQ_COMPRAS,
                COLUNAS_COMPRAS,
                resultado,
                "Compra registrada com sucesso.",
            )


def _render_movimentacoes(
    itens, movimentacoes, estoque, resultado, pode_editar
):
    st.subheader("Movimentações")
    mapa = _mapa_itens(itens)
    exibicao = movimentacoes.copy()
    if not exibicao.empty:
        exibicao["item"] = (
            exibicao["item_id"].astype(str).map(mapa).fillna(exibicao["item_id"])
        )
        st.dataframe(
            exibicao[
                [
                    "data_movimentacao",
                    "item",
                    "quantidade",
                    "local_origem",
                    "obra_origem_id",
                    "local_destino",
                    "obra_destino_id",
                    "responsavel",
                    "observacoes",
                ]
            ].sort_values("data_movimentacao", ascending=False),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Nenhuma movimentação registrada.")

    posicoes = estoque[estoque["quantidade"] > 1e-9].copy()
    if posicoes.empty:
        st.warning("Não há saldo disponível para movimentar.")
        return
    posicoes["rotulo"] = posicoes.apply(
        lambda linha: (
            f"{mapa.get(str(linha['item_id']), linha['item_id'])} · "
            f"{linha['quantidade']:g} em {linha['localizacao']}"
            + (
                f" · obra {linha['obra_id']}"
                if str(linha["obra_id"]).strip()
                else ""
            )
        ),
        axis=1,
    )
    opcoes = posicoes.index.tolist()
    rotulos = dict(zip(posicoes.index, posicoes["rotulo"]))
    with st.form("form_nova_movimentacao", clear_on_submit=True):
        origem_indice = st.selectbox(
            "Saldo de origem", opcoes, format_func=rotulos.get
        )
        origem = posicoes.loc[origem_indice]
        origem_item = str(origem["item_id"])
        origem_local = str(origem["localizacao"])
        origem_obra = str(origem["obra_id"])
        col1, col2 = st.columns(2)
        data_movimentacao = col1.date_input(
            "Data da movimentação", value=date.today()
        )
        quantidade = col2.number_input(
            "Quantidade movimentada", min_value=0.01, step=1.0
        )
        col3, col4 = st.columns(2)
        local_destino = col3.text_input("Local de destino")
        obra_destino = col4.text_input("Obra / código de destino (opcional)")
        responsavel = st.text_input("Responsável pelo recebimento")
        observacoes = st.text_area("Observações")
        salvar = st.form_submit_button(
            "Registrar movimentação",
            disabled=not pode_editar or not _escrita_liberada(resultado),
            use_container_width=True,
        )
    if salvar:
        try:
            atualizadas = registrar_movimentacao(
                movimentacoes,
                estoque,
                item_id=origem_item,
                data_movimentacao=data_movimentacao.isoformat(),
                quantidade=quantidade,
                local_origem=origem_local,
                obra_origem_id=origem_obra,
                local_destino=local_destino,
                obra_destino_id=obra_destino,
                responsavel=responsavel,
                observacoes=observacoes,
                criado_por=st.session_state.get("usuario", ""),
            )
        except ValueError as exc:
            st.error(str(exc))
        else:
            _salvar(
                atualizadas,
                ARQ_MOVIMENTACOES,
                COLUNAS_MOVIMENTACOES,
                resultado,
                "Movimentação registrada com sucesso.",
            )


def _rotulo_posse(linha):
    tamanho = (
        f" · tam. {linha['tamanho']}"
        if str(linha["tamanho"]).strip()
        else ""
    )
    return (
        f"{linha['matricula']} · {linha['funcionario']} · "
        f"{linha['item']}{tamanho} · posse {linha['quantidade']:g}"
    )


def _render_entrega(itens, entregas, estoque, resultado, pode_editar):
    posicoes = estoque[estoque["quantidade"] > 1e-9].copy()
    if posicoes.empty:
        st.warning("Não há saldo disponível para entregar.")
        return
    mapa = _mapa_itens(itens)
    posicoes["rotulo"] = posicoes.apply(
        lambda linha: (
            f"{mapa.get(str(linha['item_id']), linha['item_id'])} · "
            f"{linha['quantidade']:g} em {linha['localizacao']}"
            + (
                f" · obra {linha['obra_id']}"
                if str(linha["obra_id"]).strip()
                else ""
            )
        ),
        axis=1,
    )
    opcoes = posicoes.index.tolist()
    rotulos = dict(zip(posicoes.index, posicoes["rotulo"]))
    with st.form("form_entrega_funcionario", clear_on_submit=True):
        origem_indice = st.selectbox(
            "Saldo de origem", opcoes, format_func=rotulos.get
        )
        origem = posicoes.loc[origem_indice]
        col1, col2 = st.columns(2)
        matricula = col1.text_input("Matrícula")
        funcionario = col2.text_input("Funcionário")
        col3, col4 = st.columns(2)
        quantidade = col3.number_input(
            "Quantidade entregue", min_value=0.01, step=1.0
        )
        data_entrega = col4.date_input("Data da entrega", value=date.today())
        responsavel = st.text_input("Responsável pela entrega")
        observacoes = st.text_area("Observações")
        salvar = st.form_submit_button(
            "Registrar entrega",
            disabled=not pode_editar or not _escrita_liberada(resultado),
            use_container_width=True,
        )
    if salvar:
        try:
            atualizadas = registrar_entrega(
                entregas,
                itens,
                estoque,
                matricula=matricula,
                funcionario=funcionario,
                item_id=str(origem["item_id"]),
                quantidade=quantidade,
                data_entrega=data_entrega.isoformat(),
                local_estoque=str(origem["localizacao"]),
                obra_id=str(origem["obra_id"]),
                responsavel=responsavel,
                observacoes=observacoes,
                criado_por=st.session_state.get("usuario", ""),
            )
        except ValueError as exc:
            st.error(str(exc))
        else:
            _salvar(
                atualizadas,
                ARQ_ENTREGAS,
                COLUNAS_ENTREGAS,
                resultado,
                "Entrega registrada com sucesso.",
            )


def _selecionar_posse(posses, chave):
    if posses.empty:
        st.warning("Nenhum funcionário possui itens neste momento.")
        return None
    opcoes = posses.index.tolist()
    rotulos = {
        indice: _rotulo_posse(linha)
        for indice, linha in posses.iterrows()
    }
    indice = st.selectbox(
        "Funcionário e item", opcoes, format_func=rotulos.get, key=chave
    )
    return posses.loc[indice]


def _render_devolucao(
    itens, entregas, posses, resultado, pode_editar
):
    with st.form("form_devolucao_funcionario", clear_on_submit=True):
        posse = _selecionar_posse(posses, "posse_devolucao")
        col1, col2 = st.columns(2)
        quantidade = col1.number_input(
            "Quantidade devolvida", min_value=0.01, step=1.0
        )
        data_devolucao = col2.date_input(
            "Data da devolução", value=date.today()
        )
        col3, col4 = st.columns(2)
        local_estoque = col3.text_input("Local de retorno ao estoque")
        obra_id = col4.text_input("Obra / código do estoque (opcional)")
        responsavel = st.text_input("Responsável pelo recebimento")
        observacoes = st.text_area("Observações")
        salvar = st.form_submit_button(
            "Registrar devolução",
            disabled=(
                posse is None
                or not pode_editar
                or not _escrita_liberada(resultado)
            ),
            use_container_width=True,
        )
    if salvar and posse is not None:
        try:
            atualizadas = registrar_devolucao(
                entregas,
                itens,
                posses,
                matricula=str(posse["matricula"]),
                funcionario=str(posse["funcionario"]),
                item_id=str(posse["item_id"]),
                quantidade=quantidade,
                data_devolucao=data_devolucao.isoformat(),
                local_estoque=local_estoque,
                obra_id=obra_id,
                responsavel=responsavel,
                observacoes=observacoes,
                criado_por=st.session_state.get("usuario", ""),
            )
        except ValueError as exc:
            st.error(str(exc))
        else:
            _salvar(
                atualizadas,
                ARQ_ENTREGAS,
                COLUNAS_ENTREGAS,
                resultado,
                "Devolução registrada com sucesso.",
            )


def _render_baixa(itens, entregas, posses, resultado, pode_editar):
    with st.form("form_baixa_funcionario", clear_on_submit=True):
        posse = _selecionar_posse(posses, "posse_baixa")
        col1, col2 = st.columns(2)
        quantidade = col1.number_input(
            "Quantidade baixada", min_value=0.01, step=1.0
        )
        data_baixa = col2.date_input("Data da baixa", value=date.today())
        motivo = st.selectbox(
            "Motivo", ["Perda", "Dano", "Descarte", "Extravio", "Outro"]
        )
        responsavel = st.text_input("Responsável pela baixa")
        observacoes = st.text_area("Observações")
        salvar = st.form_submit_button(
            "Registrar baixa",
            disabled=(
                posse is None
                or not pode_editar
                or not _escrita_liberada(resultado)
            ),
            use_container_width=True,
        )
    if salvar and posse is not None:
        try:
            atualizadas = registrar_baixa(
                entregas,
                itens,
                posses,
                matricula=str(posse["matricula"]),
                funcionario=str(posse["funcionario"]),
                item_id=str(posse["item_id"]),
                quantidade=quantidade,
                data_baixa=data_baixa.isoformat(),
                motivo=motivo,
                responsavel=responsavel,
                observacoes=observacoes,
                criado_por=st.session_state.get("usuario", ""),
            )
        except ValueError as exc:
            st.error(str(exc))
        else:
            _salvar(
                atualizadas,
                ARQ_ENTREGAS,
                COLUNAS_ENTREGAS,
                resultado,
                "Baixa registrada com sucesso.",
            )


def _render_ciclo_funcionario(
    itens, entregas, estoque, posses, resultado, pode_editar
):
    entrega, devolucao, baixa = st.tabs(["Entrega", "Devolução", "Baixa"])
    with entrega:
        _render_entrega(
            itens, entregas, estoque, resultado, pode_editar
        )
    with devolucao:
        _render_devolucao(
            itens, entregas, posses, resultado, pode_editar
        )
    with baixa:
        _render_baixa(
            itens, entregas, posses, resultado, pode_editar
        )


def _historico_item(
    item_id, compras, movimentacoes, entregas
):
    linhas = []
    for _, compra in compras[
        compras["item_id"].astype(str) == str(item_id)
    ].iterrows():
        linhas.append(
            {
                "data": compra["data_compra"],
                "evento": "COMPRA",
                "quantidade": compra["quantidade"],
                "origem": compra["fornecedor"],
                "destino": compra["local_inicial"],
                "funcionario": "",
                "responsavel": compra["criado_por"],
                "motivo": "",
                "observacoes": compra["observacoes"],
            }
        )
    for _, movimento in movimentacoes[
        movimentacoes["item_id"].astype(str) == str(item_id)
    ].iterrows():
        linhas.append(
            {
                "data": movimento["data_movimentacao"],
                "evento": "TRANSFERENCIA",
                "quantidade": movimento["quantidade"],
                "origem": movimento["local_origem"],
                "destino": movimento["local_destino"],
                "funcionario": "",
                "responsavel": movimento["responsavel"],
                "motivo": "",
                "observacoes": movimento["observacoes"],
            }
        )
    for _, evento in entregas[
        entregas["item_id"].astype(str) == str(item_id)
    ].iterrows():
        tipo = str(evento["tipo_evento"])
        linhas.append(
            {
                "data": evento["data_evento"],
                "evento": tipo,
                "quantidade": evento["quantidade"],
                "origem": (
                    evento["local_estoque"] if tipo == "ENTREGA" else ""
                ),
                "destino": (
                    evento["local_estoque"] if tipo == "DEVOLUCAO" else ""
                ),
                "funcionario": (
                    f"{evento['matricula']} · {evento['funcionario']}"
                ),
                "responsavel": evento["responsavel"],
                "motivo": evento["motivo"],
                "observacoes": evento["observacoes"],
            }
        )
    colunas = [
        "data",
        "evento",
        "quantidade",
        "origem",
        "destino",
        "funcionario",
        "responsavel",
        "motivo",
        "observacoes",
    ]
    if not linhas:
        return pd.DataFrame(columns=colunas)
    return (
        pd.DataFrame(linhas, columns=colunas)
        .sort_values("data", ascending=False)
        .reset_index(drop=True)
    )


def _render_historicos(
    itens, compras, movimentacoes, entregas, posses
):
    funcionarios, itens_aba = st.tabs(
        ["Por funcionário", "Por item"]
    )
    with funcionarios:
        if entregas.empty:
            st.info("Nenhuma entrega registrada.")
        else:
            pessoas = (
                entregas[["matricula", "funcionario"]]
                .drop_duplicates("matricula", keep="last")
                .sort_values("funcionario")
            )
            opcoes = pessoas["matricula"].astype(str).tolist()
            rotulos = dict(
                zip(
                    pessoas["matricula"].astype(str),
                    pessoas.apply(
                        lambda linha: (
                            f"{linha['matricula']} · {linha['funcionario']}"
                        ),
                        axis=1,
                    ),
                )
            )
            matricula = st.selectbox(
                "Funcionário", opcoes, format_func=rotulos.get
            )
            st.markdown("**Itens atualmente em posse**")
            atuais = posses[
                posses["matricula"].astype(str) == matricula
            ]
            if atuais.empty:
                st.info("Este funcionário não possui itens atualmente.")
            else:
                st.dataframe(
                    atuais[
                        [
                            "categoria",
                            "item",
                            "tamanho",
                            "quantidade",
                            "unidade",
                        ]
                    ],
                    use_container_width=True,
                    hide_index=True,
                )
            st.markdown("**Histórico completo**")
            st.dataframe(
                historico_funcionario(entregas, itens, matricula),
                use_container_width=True,
                hide_index=True,
            )

    with itens_aba:
        if itens.empty:
            st.info("Nenhum item cadastrado.")
        else:
            mapa = _mapa_itens(itens)
            opcoes = itens["item_id"].astype(str).tolist()
            item_id = st.selectbox(
                "Item", opcoes, format_func=mapa.get
            )
            historico = _historico_item(
                item_id, compras, movimentacoes, entregas
            )
            if historico.empty:
                st.info("Este item ainda não possui histórico.")
            else:
                st.dataframe(
                    historico, use_container_width=True, hide_index=True
                )


def render():
    if not pode_acessar("uniformes_epis"):
        st.error("Você não possui permissão para acessar Uniformes e EPIs.")
        return

    st.title("Uniformes e EPIs")
    st.caption(
        "Controle de catálogo, compras, valores e localização física por obra."
    )
    if st.button("⬅ Voltar ao menu", key="voltar_uniformes_epis"):
        st.session_state.tela = "menu"
        st.rerun()

    token, repo = _configuracao()
    bases = carregar_bases(token, repo)
    falhas = [
        resultado
        for resultado in bases.values()
        if not resultado.leitura_confirmada
    ]
    if falhas:
        st.error(
            "A leitura dos dados não foi confirmada. O módulo foi bloqueado "
            "para evitar perda de informações: " + _detalhes(falhas[0])
        )
        return

    itens = bases["itens"].dados
    compras = bases["compras"].dados
    movimentacoes = bases["movimentacoes"].dados
    entregas = bases["entregas"].dados
    estoque = calcular_estoque(
        itens, compras, movimentacoes, entregas
    )
    posses = calcular_posse_funcionarios(itens, entregas)
    pode_editar = pode(modulo="uniformes_epis", recurso="cadastros", acao="editar")

    (
        resumo,
        cadastro,
        aba_compras,
        aba_movimentos,
        aba_entregas,
        aba_historicos,
    ) = st.tabs(
        [
            "Visão geral",
            "Itens",
            "Compras",
            "Movimentações",
            "Entregas",
            "Históricos",
        ]
    )
    with resumo:
        _render_resumo(itens, compras, movimentacoes, estoque)
    with cadastro:
        _render_itens(itens, bases["itens"], pode_editar)
    with aba_compras:
        _render_compras(itens, compras, bases["compras"], pode_editar)
    with aba_movimentos:
        _render_movimentacoes(
            itens,
            movimentacoes,
            estoque,
            bases["movimentacoes"],
            pode_editar,
        )
    with aba_entregas:
        _render_ciclo_funcionario(
            itens,
            entregas,
            estoque,
            posses,
            bases["entregas"],
            pode_editar,
        )
    with aba_historicos:
        _render_historicos(
            itens, compras, movimentacoes, entregas, posses
        )
