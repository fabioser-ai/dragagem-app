import streamlit as st

# Módulos principais
from pages import menu, dados, ferias, prestacao_contas, medicoes, administracao
from pages.crm.crm import crm

# Serviços
from services.auth import verificar_login
from services.ui import aplicar_estilo_global

# Módulo orçamento
from pages.orcamento.dashboard import dashboard_orcamento
from pages.orcamento.etapa0 import etapa0
from pages.orcamento.etapa1 import etapa1
from pages.orcamento.etapa2 import etapa2
from pages.orcamento.etapa3 import etapa3
from modulos.orcamentos.apresentacao import entrada as novo_orcamento
from services.permissoes import pode_acessar_modulo


# =========================
# CONFIGURAÇÃO
# =========================
st.set_page_config(layout="wide")


# =========================
# AUTENTICAÇÃO
# =========================
if not verificar_login():
    st.stop()


# =========================
# ESTILO GLOBAL
# =========================
aplicar_estilo_global()


# =========================
# ESTADO INICIAL
# =========================
if "tela" not in st.session_state:
        st.session_state.tela = "menu"


# =========================
# BLOQUEIO DE ACESSO PARA FUNCIONÁRIO
# =========================
if st.session_state.get("perfil") == "funcionario":
    telas_permitidas_funcionario = [
        "menu",
        "prestacao_contas",
        "carregando_medicoes",
        "medicoes",
    ]

    if st.session_state.tela not in telas_permitidas_funcionario:
        st.session_state.tela = "menu"
        st.rerun()


# =========================
# ROTEADOR
# =========================
if st.session_state.tela == "menu":
    menu.render()


elif st.session_state.tela == "dados":
    dados.render()

elif st.session_state.tela == "administracao":
    administracao.render()

elif st.session_state.tela == "ferias":
    ferias.render()


elif st.session_state.tela == "prestacao_contas":
    prestacao_contas.render()


elif st.session_state.tela == "carregando_medicoes":
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 55%, #334155 100%);
            border-radius: 24px;
            padding: 2.5rem 2rem;
            margin-top: 1rem;
            margin-bottom: 1.5rem;
            text-align: center;
            box-shadow: 0 18px 45px rgba(15, 23, 42, 0.20);
        ">
            <h1 style="color: white; margin-bottom: 0.7rem;">
                Carregando Medições
            </h1>
            <p style="color: #dbeafe; font-size: 1.05rem; margin: 0;">
                Preparando obras, BMs, frentes, memórias de cálculo e resumo financeiro.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.session_state.tela = "medicoes"
    st.rerun()


elif st.session_state.tela == "medicoes":
    medicoes.medicoes()


elif st.session_state.tela == "crm":
    crm()


# =========================
# NOVO SISTEMA DE ORÇAMENTOS - FRONTEIRA
# =========================
elif st.session_state.tela == "novo_orcamento":
    novo_orcamento.render(
        autorizado=pode_acessar_modulo("orcamento"),
    )


# =========================
# MÓDULO OBRAS
# =========================
elif st.session_state.tela == "obras":
    import pandas as pd
    from services.github import carregar_github

    st.title("📊 Obras")

    ARQ_OBRAS = "data/orcamentos.csv"

    try:
        df = carregar_github(
            ARQ_OBRAS,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )
    except Exception:
        df = pd.DataFrame()

    if df.empty:
        st.warning("Nenhuma obra cadastrada ainda.")
    else:
        st.subheader("Lista de Obras")
        st.dataframe(df, use_container_width=True)

    if st.button("⬅ Voltar", key="voltar_obras"):
        st.session_state.tela = "menu"
        st.rerun()


# =========================
# ORÇAMENTO - DASHBOARD
# =========================
elif st.session_state.tela == "orcamento":
    dashboard_orcamento()


elif st.session_state.tela == "orcamento_lista":
    dashboard_orcamento()


# =========================
# ORÇAMENTO - ETAPAS
# =========================
elif st.session_state.tela == "orcamento_etapa0":
    etapa0()


elif st.session_state.tela == "orcamento1":
    etapa1()


elif st.session_state.tela == "orcamento2":
    etapa2()


elif st.session_state.tela == "orcamento3":
    etapa3()


# =========================
# FALLBACK
# =========================
else:
    st.session_state.tela = "menu"
    st.rerun()
