import streamlit as st

from services.auth import processar_log_pendente, verificar_login
from services.ui import aplicar_estilo_global


st.set_page_config(layout="wide")


if not verificar_login():
    st.stop()


aplicar_estilo_global()

if "tela" not in st.session_state:
    st.session_state.tela = "menu"


if st.session_state.get("perfil") == "funcionario":
    telas_permitidas_funcionario = {
        "menu",
        "prestacao_contas",
        "carregando_medicoes",
        "medicoes",
    }

    if st.session_state.tela not in telas_permitidas_funcionario:
        st.session_state.tela = "menu"


tela = st.session_state.tela

if tela == "menu":
    from pages import menu

    menu.render()

elif tela == "dados":
    from pages import dados

    dados.render()

elif tela == "administracao":
    from pages import administracao

    administracao.render()

elif tela == "ferias":
    from pages import ferias

    ferias.render()

elif tela == "prestacao_contas":
    from pages import prestacao_contas

    prestacao_contas.render()

elif tela == "carregando_medicoes":
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
            <h1 style="color: white; margin-bottom: 0.7rem;">Carregando Medições</h1>
            <p style="color: #dbeafe; font-size: 1.05rem; margin: 0;">
                Preparando obras, BMs, frentes, memórias de cálculo e resumo financeiro.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.session_state.tela = "medicoes"
    st.rerun()

elif tela == "medicoes":
    from pages import medicoes

    medicoes.medicoes()

elif tela == "crm":
    from pages.crm.crm import crm

    crm()

elif tela == "novo_orcamento":
    from modulos.orcamentos.apresentacao import entrada as novo_orcamento
    from services.permissoes import pode_acessar_modulo

    novo_orcamento.render(autorizado=pode_acessar_modulo("orcamento"))

elif tela == "obras":
    import pandas as pd

    from services.github import carregar_github

    st.title("📊 Obras")
    try:
        df = carregar_github(
            "data/orcamentos.csv",
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

elif tela in {"orcamento", "orcamento_lista"}:
    from pages.orcamento.dashboard import dashboard_orcamento

    dashboard_orcamento()

elif tela == "orcamento_etapa0":
    from pages.orcamento.etapa0 import etapa0

    etapa0()

elif tela == "orcamento1":
    from pages.orcamento.etapa1 import etapa1

    etapa1()

elif tela == "orcamento2":
    from pages.orcamento.etapa2 import etapa2

    etapa2()

elif tela == "orcamento3":
    from pages.orcamento.etapa3 import etapa3

    etapa3()

else:
    st.session_state.tela = "menu"
    st.rerun()


# O menu já foi enviado ao navegador antes da escrita remota do log.
processar_log_pendente()
