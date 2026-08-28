import streamlit as st

from services.autorizacao import pode


FLUXOS = {
    "novo": {
        "titulo": "Novo contato",
        "descricao": "Cadastrar empresa, pessoa de contato ou registrar uma nova interação comercial.",
        "opcoes": (
            ("Nova empresa / cliente", "clientes", "cliente", "criar"),
            ("Novo contato de pessoa", "contatos", "contato", "criar"),
            ("Nova interação", "interacoes", "interacao", "criar"),
        ),
    },
    "consultar": {
        "titulo": "Consultar",
        "descricao": "Pesquisar clientes, contatos e histórico comercial conforme seu acesso.",
        "opcoes": (
            ("Consulta geral", "consulta", "cliente", "visualizar"),
            ("Clientes / empresas", "clientes", "cliente", "visualizar"),
            ("Contatos", "contatos", "contato", "visualizar"),
            ("Interações", "interacoes", "interacao", "visualizar"),
        ),
    },
    "atualizar": {
        "titulo": "Atualizar",
        "descricao": "Atualizar dados comerciais e informações de contatos existentes.",
        "opcoes": (
            ("Atualizar cliente / empresa", "clientes", "cliente", "editar"),
            ("Atualizar contato", "contatos", "contato", "editar"),
        ),
    },
}


def _opcoes_autorizadas(fluxo):
    return [
        opcao
        for opcao in FLUXOS[fluxo]["opcoes"]
        if pode(modulo="crm", recurso=opcao[2], acao=opcao[3])
    ]


def _abrir_fluxo(fluxo):
    st.session_state.crm_fluxo = fluxo
    st.session_state.crm_pagina = None
    st.rerun()


def _abrir_pagina(pagina):
    st.session_state.crm_pagina = pagina
    st.rerun()


def render_landing():
    st.subheader("O que você quer fazer?")
    colunas = st.columns(3)

    for coluna, fluxo in zip(colunas, ("novo", "consultar", "atualizar")):
        dados = FLUXOS[fluxo]
        opcoes = _opcoes_autorizadas(fluxo)
        if not opcoes:
            continue
        with coluna:
            with st.container(border=True):
                st.markdown(f"### {dados['titulo']}")
                st.caption(dados["descricao"])
                st.write("")
                if st.button("Abrir", key=f"crm_fluxo_{fluxo}", use_container_width=True):
                    _abrir_fluxo(fluxo)


def render_fluxo(fluxo):
    dados = FLUXOS[fluxo]
    opcoes = _opcoes_autorizadas(fluxo)

    st.caption(dados["descricao"])

    if not opcoes:
        st.warning("Nenhuma atividade disponível para seu acesso.")
        return None

    cols = st.columns(min(3, len(opcoes)))
    for idx, (rotulo, pagina, _recurso, _acao) in enumerate(opcoes):
        with cols[idx % len(cols)]:
            if st.button(rotulo, key=f"crm_atividade_{fluxo}_{pagina}_{idx}", use_container_width=True):
                _abrir_pagina(pagina)

    return st.session_state.get("crm_pagina")
