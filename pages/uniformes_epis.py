from datetime import date

import pandas as pd
import streamlit as st

from services.github import StatusLeitura
from services.permissoes import pode_acessar_modulo, pode_executar
from services.uniformes_epis import (
    ARQ_COMPRAS,
    ARQ_ITENS,
    ARQ_MOVIMENTACOES,
    COLUNAS_COMPRAS,
    COLUNAS_ITENS,
    COLUNAS_MOVIMENTACOES,
    cadastrar_item,
    calcular_estoque,
    carregar_bases,
    registrar_compra,
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
    token, repo = _configuracao()
    resultado = salvar_base(
        df, arquivo, colunas, token, repo, resultado_leitura
    )
    if resultado.sucesso:
        st.success(mensagem)
        st.rerun()
    else:
        st.error(_detalhes(resultado))


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


def render():
    if not pode_acessar_modulo("uniformes_epis"):
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
    estoque = calcular_estoque(itens, compras, movimentacoes)
    pode_editar = pode_executar(
        "uniformes_epis", recurso="cadastros", permissao="editar"
    )

    resumo, cadastro, aba_compras, aba_movimentos = st.tabs(
        ["Visão geral", "Itens", "Compras", "Movimentações"]
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
