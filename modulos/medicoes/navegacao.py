import streamlit as st

from modulos.medicoes.config import ETAPAS_MODELO
from modulos.medicoes.utils import ir_para

from modulos.medicoes.permissoes import (
    obter_perfil_medicao,
    pode_lancar_trabalho,
    pode_visualizar_lancamentos,
    pode_aprovar_lancamentos,
    pode_criar_medicao,
)

from modulos.medicoes.lancamentos.tela_lancar import (
    tela_lancar_producao,
)


LABELS_ETAPAS = {
    "obra": "1. Obra",
    "bm": "2. BM",
    "frentes": "3. Frentes",
    "mc": "4. MC",
    "medicao": "5. Medição",
    "resumo": "6. Resumo",
}


def obter_etapas():
    modelo = st.session_state.get(
        "modelo_medicao",
        "padrao_fos",
    )

    return ETAPAS_MODELO.get(
        modelo,
        ETAPAS_MODELO["padrao_fos"],
    )


def tela_inicial_medicoes():
    perfil = obter_perfil_medicao()

    st.markdown("## 📏 Módulo de Medições")

    if perfil == "funcionario":
        st.caption("Lançamento operacional de trabalho executado.")
    else:
        st.caption("Escolha qual fluxo de trabalho deseja acessar.")

    st.divider()

    opcoes_disponiveis = []

    if pode_criar_medicao():
        opcoes_disponiveis.append("gestao")

    if pode_lancar_trabalho():
        opcoes_disponiveis.append("lancamento")

    if pode_aprovar_lancamentos():
        opcoes_disponiveis.append("aprovacao")

    if not opcoes_disponiveis:
        st.warning("Nenhuma função disponível para seu perfil.")
        return

    # Funcionário não escolhe fluxo. Vai direto para lançamento.
    if perfil == "funcionario":
        st.session_state["fluxo_medicoes"] = "lancamento"
        st.rerun()

    qtd_colunas = len(opcoes_disponiveis)
    cols = st.columns(qtd_colunas)

    idx = 0

    if "gestao" in opcoes_disponiveis:
        with cols[idx]:
            st.markdown("### 🧾 Criar / Gerenciar Medição")

            st.write(
                "Criar nova medição, selecionar obra, BM, "
                "frentes, MC, itens e revisar o resumo."
            )

            if st.button(
                "Acessar Gestão da Medição",
                use_container_width=True,
                key="btn_acessar_gestao_medicao",
            ):
                st.session_state["fluxo_medicoes"] = "gestao"
                st.session_state["etapa_medicoes"] = "obra"
                st.rerun()

        idx += 1

    if "lancamento" in opcoes_disponiveis:
        with cols[idx]:
            st.markdown("### 📝 Lançar Trabalho Executado")

            st.write(
                "Registrar serviços executados em campo, "
                "quantidades, fotos e observações."
            )

            if st.button(
                "Acessar Lançamentos",
                use_container_width=True,
                key="btn_acessar_lancamentos_medicao",
            ):
                st.session_state["fluxo_medicoes"] = "lancamento"
                st.rerun()

        idx += 1

    if "aprovacao" in opcoes_disponiveis:
        with cols[idx]:
            st.markdown("### ✅ Aprovar Lançamentos")

            st.write(
                "Revisar lançamentos realizados pelos "
                "encarregados e equipes de campo."
            )

            if st.button(
                "Acessar Aprovação",
                use_container_width=True,
                key="btn_acessar_aprovacao_medicao",
            ):
                st.session_state["fluxo_medicoes"] = "aprovacao"
                st.rerun()

    st.divider()

    if st.button(
        "⬅ Voltar ao Menu Principal",
        use_container_width=True,
        key="btn_voltar_menu_medicoes",
    ):
        st.session_state["tela"] = "menu"
        st.rerun()


def navegacao_gestao():
    if not pode_criar_medicao():
        st.warning("Seu perfil não possui acesso à gestão de medições.")
        st.session_state["fluxo_medicoes"] = "inicio"
        st.rerun()

    etapa = st.session_state.get(
        "etapa_medicoes",
        "obra",
    )

    ordem = obter_etapas()

    if etapa not in ordem:
        etapa = ordem[0]
        st.session_state.etapa_medicoes = etapa

    st.markdown("### Fluxo da Medição")

    cols = st.columns(len(ordem))

    for i, etapa_nome in enumerate(ordem):
        with cols[i]:
            ativo = etapa_nome == etapa

            st.button(
                f"{'✅ ' if ativo else ''}{LABELS_ETAPAS[etapa_nome]}",
                disabled=ativo,
                use_container_width=True,
                key=f"barra_medicoes_{etapa_nome}",
            )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        idx = ordem.index(etapa)

        if idx > 0:
            if st.button(
                "← Voltar",
                use_container_width=True,
                key="btn_voltar_etapa_medicoes",
            ):
                ir_para(ordem[idx - 1])

    with c2:
        if st.button(
            "⬅ Início Medições",
            use_container_width=True,
            key="btn_inicio_medicoes",
        ):
            st.session_state["fluxo_medicoes"] = "inicio"
            st.rerun()

    with c3:
        idx = ordem.index(etapa)

        if idx < len(ordem) - 1:
            if st.button(
                "Próximo →",
                use_container_width=True,
                key="btn_proxima_etapa_medicoes",
            ):
                ir_para(ordem[idx + 1])


def tela_aprovacao_placeholder():
    if not pode_aprovar_lancamentos():
        st.warning("Seu perfil não possui acesso à aprovação de lançamentos.")
        st.session_state["fluxo_medicoes"] = "inicio"
        st.rerun()

    st.markdown("## ✅ Aprovação de Lançamentos")

    st.info(
        "Tela de aprovação ainda será implementada."
    )

    if st.button(
        "⬅ Voltar ao início das Medições",
        use_container_width=True,
        key="btn_voltar_inicio_aprovacao",
    ):
        st.session_state["fluxo_medicoes"] = "inicio"
        st.rerun()


def navegacao_lancamento():
    if not pode_lancar_trabalho():
        st.warning("Seu perfil não possui acesso ao lançamento de trabalho executado.")
        st.session_state["fluxo_medicoes"] = "inicio"
        st.rerun()

    tela_lancar_producao()


def navegacao():
    if "fluxo_medicoes" not in st.session_state:
        st.session_state["fluxo_medicoes"] = "inicio"

    fluxo = st.session_state["fluxo_medicoes"]

    if fluxo == "inicio":
        tela_inicial_medicoes()

    elif fluxo == "gestao":
        navegacao_gestao()

    elif fluxo == "lancamento":
        navegacao_lancamento()

    elif fluxo == "aprovacao":
        tela_aprovacao_placeholder()

    else:
        st.session_state["fluxo_medicoes"] = "inicio"
        st.rerun()
