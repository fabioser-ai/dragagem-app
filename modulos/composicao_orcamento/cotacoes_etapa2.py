"""Etapa 2: cotações livres e catálogo inicial, isolados na sessão Streamlit.

O catálogo aqui é provisório: não altera cadastros operacionais nem grava preços.
"""
from copy import deepcopy
from uuid import uuid4

import pandas as pd
import streamlit as st

CHAVE_COTACOES = "_composicao_etapa2_cotacoes"
CHAVE_CATALOGO = "_composicao_etapa2_catalogo"
SEMENTES = (
    ("Guindaste", "hora", "Preço por hora", "Preço por diária"),
    ("Container", "mês", "Preço por mês", "Frete por hora"),
    ("Banheiro químico", "mês", "Preço por mês", ""),
    ("Destinação", "mês", "Preço por mês", ""),
)
COLUNAS = ["Fornecedor", "Contato", "Telefone", "Detalhe", "Preço principal (R$)", "Preço alternativo (R$)"]


def _novo_item(nome, unidade, primeiro, segundo="", origem="livre", catalogo_id=None):
    return {
        "id": uuid4().hex, "nome": nome.strip(), "unidade": unidade.strip(),
        "rotulo_primeiro": primeiro.strip(), "rotulo_segundo": segundo.strip(),
        "origem": origem, "catalogo_id": catalogo_id, "propostas": [],
    }


def _inicializar():
    if CHAVE_CATALOGO not in st.session_state:
        st.session_state[CHAVE_CATALOGO] = [
            {"id": f"inicial-{i}", "nome": nome, "unidade": unidade,
             "rotulo_primeiro": primeiro, "rotulo_segundo": segundo}
            for i, (nome, unidade, primeiro, segundo) in enumerate(SEMENTES)
        ]
    if CHAVE_COTACOES not in st.session_state:
        st.session_state[CHAVE_COTACOES] = [
            _novo_item(c["nome"], c["unidade"], c["rotulo_primeiro"],
                       c["rotulo_segundo"], "catalogo", c["id"])
            for c in st.session_state[CHAVE_CATALOGO]
        ]


def _adicionar_catalogo():
    catalogo = st.session_state[CHAVE_CATALOGO]
    cotacoes = st.session_state[CHAVE_COTACOES]
    ids_existentes = {item["catalogo_id"] for item in cotacoes}
    disponiveis = [item for item in catalogo if item["id"] not in ids_existentes]
    if not disponiveis:
        st.caption("Todos os itens do catálogo já foram incluídos nesta cotação.")
        return
    opcoes = {item["id"]: item for item in disponiveis}
    with st.form("cotacoes_incluir_catalogo"):
        escolhido = st.selectbox(
            "Pesquisar e selecionar item do catálogo",
            list(opcoes), format_func=lambda chave: (
                f'{opcoes[chave]["nome"]} — {opcoes[chave]["unidade"]}'
            ),
        )
        incluir = st.form_submit_button("Adicionar item selecionado")
    if incluir:
        item = opcoes[escolhido]
        cotacoes.append(_novo_item(item["nome"], item["unidade"],
                                   item["rotulo_primeiro"], item["rotulo_segundo"],
                                   "catalogo", item["id"]))
        st.rerun()


def _adicionar_livre():
    with st.form("cotacoes_incluir_livre", clear_on_submit=True):
        nome = st.text_input("Nome do item *")
        unidade = st.text_input("Unidade (ex.: hora, mês, m³) *")
        primeiro = st.text_input("Descrição do preço principal *", value="Preço unitário")
        segundo = st.text_input("Descrição do preço alternativo (opcional)")
        adicionar = st.form_submit_button("Criar item livre")
    if adicionar:
        if not nome.strip() or not unidade.strip() or not primeiro.strip():
            st.error("Informe nome, unidade e descrição do preço principal.")
        else:
            st.session_state[CHAVE_COTACOES].append(
                _novo_item(nome, unidade, primeiro, segundo)
            )
            st.rerun()


def _tabela_propostas(item):
    linhas = item["propostas"]
    quadro = pd.DataFrame(linhas, columns=COLUNAS)
    with st.form(f'cotacoes_editar_{item["id"]}'):
        nome = st.text_input("Descrição", value=item["nome"], key=f'nome_{item["id"]}')
        unidade = st.text_input("Unidade", value=item["unidade"], key=f'unidade_{item["id"]}')
        primeiro = st.text_input("Preço principal — rótulo",
                                 value=item["rotulo_primeiro"], key=f'primeiro_{item["id"]}')
        segundo = st.text_input("Preço alternativo — rótulo",
                                value=item["rotulo_segundo"], key=f'segundo_{item["id"]}')
        st.caption("Adicione ou remova linhas para comparar fornecedores. Valores em reais.")
        editado = st.data_editor(
            quadro, num_rows="dynamic", hide_index=True, use_container_width=True,
            key=f'tabela_{item["id"]}',
            column_config={
                "Preço principal (R$)": st.column_config.NumberColumn(
                    "Preço principal (R$)", min_value=0, format="R$ %.2f"),
                "Preço alternativo (R$)": st.column_config.NumberColumn(
                    "Preço alternativo (R$)", min_value=0, format="R$ %.2f"),
            },
        )
        salvar = st.form_submit_button("Aplicar alterações neste item")
    if salvar:
        if not nome.strip() or not unidade.strip() or not primeiro.strip():
            st.error("Descrição, unidade e rótulo principal são obrigatórios.")
            return
        propostas = editado.where(pd.notnull(editado), None).to_dict("records")
        for proposta in propostas:
            for coluna in COLUNAS[4:]:
                valor = proposta.get(coluna)
                if valor is not None:
                    try:
                        numero = float(valor)
                    except (TypeError, ValueError):
                        st.error("Os preços devem ser numéricos.")
                        return
                    if not 0 <= numero < float("inf"):
                        st.error("Os preços devem ser finitos e não negativos.")
                        return
                    proposta[coluna] = numero
            for coluna in COLUNAS[:4]:
                proposta[coluna] = str(proposta.get(coluna) or "")
        item.update(nome=nome.strip(), unidade=unidade.strip(),
                    rotulo_primeiro=primeiro.strip(), rotulo_segundo=segundo.strip(),
                    propostas=propostas)
        st.success("Item atualizado no rascunho desta sessão.")
    if item["propostas"]:
        valores = [p.get(COLUNAS[4]) for p in item["propostas"]
                   if isinstance(p.get(COLUNAS[4]), (int, float))]
        if valores:
            st.caption(f"Menor preço principal informado: R$ {min(valores):,.2f}")


def render():
    _inicializar()
    st.subheader("Etapa 2 — Cotações")
    st.info("Rascunho temporário nesta sessão. Nenhum preço ou item é gravado no banco operacional.")
    st.markdown("### Incluir itens")
    aba_catalogo, aba_livre = st.tabs(["Selecionar do catálogo", "Criar item livre"])
    with aba_catalogo:
        _adicionar_catalogo()
    with aba_livre:
        _adicionar_livre()

    st.markdown("### Itens da cotação")
    cotacoes = st.session_state[CHAVE_COTACOES]
    if not cotacoes:
        st.caption("Nenhum item incluído. Adicione um item acima.")
    for item in list(cotacoes):
        with st.expander(f'{item["nome"]} ({item["unidade"]}) — {len(item["propostas"])} fornecedor(es)'):
            _tabela_propostas(item)
            if item["origem"] == "livre":
                if st.button("Adicionar modelo ao catálogo desta sessão",
                             key=f'catalogar_{item["id"]}'):
                    nomes = {c["nome"].strip().casefold()
                             for c in st.session_state[CHAVE_CATALOGO]}
                    if item["nome"].strip().casefold() in nomes:
                        st.warning("Já existe item com esse nome no catálogo.")
                    else:
                        st.session_state[CHAVE_CATALOGO].append({
                            "id": uuid4().hex, "nome": item["nome"],
                            "unidade": item["unidade"],
                            "rotulo_primeiro": item["rotulo_primeiro"],
                            "rotulo_segundo": item["rotulo_segundo"],
                        })
                        st.success("Modelo incluído no catálogo temporário, sem preços.")
            if st.button("Remover item desta cotação", key=f'remover_{item["id"]}'):
                st.session_state[CHAVE_COTACOES] = [
                    outro for outro in cotacoes if outro["id"] != item["id"]
                ]
                st.rerun()
    st.caption("Catálogo inicial provisório. A persistência e o cadastro mestre com aprovação serão definidos em etapa própria.")
