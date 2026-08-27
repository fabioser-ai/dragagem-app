import streamlit as st

from services.auth import processar_log_pendente, verificar_login
from services.loading_fos import processar_carregamento_pendente
from services.ui import aplicar_estilo_global


st.set_page_config(layout="wide")


if not verificar_login():
    st.stop()


aplicar_estilo_global()

# Uma transição já preparada tem prioridade sobre a renderização do módulo.
if processar_carregamento_pendente():
    st.stop()

from services.autorizacao import iniciar_execucao_autorizacao, pode_acessar_rota

# Cada execução/rerun recebe fontes RBAC novas; todas as decisões feitas abaixo
# compartilham esse único snapshot consistente.
iniciar_execucao_autorizacao()

if "tela" not in st.session_state:
    st.session_state.tela = "menu"


tela = st.session_state.tela

if not pode_acessar_rota(tela):
    st.session_state.tela = "menu"
    st.error("Você não possui permissão para acessar esta área.")
    st.stop()

# Detecta genericamente a saída do menu para qualquer módulo. Assim todos os
# cards atuais e futuros recebem a mesma transição sem duplicar lógica no menu.
_rotulos_loading = {
    "dados": "Dados",
    "administracao": "Administração",
    "ferias": "Férias e Folgas",
    "prestacao_contas": "Prestação de Contas",
    "medicoes": "Medições",
    "carregando_medicoes": "Medições",
    "crm": "CRM",
    "uniformes_epis": "Uniformes e EPIs",
    "novo_orcamento": "Novo Sistema de Orçamentos",
    "obras": "Obras",
    "orcamento": "Orçamento",
    "orcamento_lista": "Orçamento",
}
_tela_anterior = st.session_state.get("_fos_tela_anterior")
if _tela_anterior == "menu" and tela != "menu" and tela in _rotulos_loading:
    destino = "medicoes" if tela == "carregando_medicoes" else tela
    st.session_state["carregamento_fos"] = {
        "destino": destino,
        "rotulo": _rotulos_loading[tela],
    }
    st.session_state["_fos_tela_anterior"] = destino
    st.rerun()

st.session_state["_fos_tela_anterior"] = tela

if tela == "menu":
    from pages import menu

    menu.render()

elif tela == "dados":
    from pages import dados_hub

    dados_hub.render()

elif tela == "administracao":
    from pages import administracao

    administracao.render()

elif tela == "ferias":
    from pages import ferias_hub

    ferias_hub.render()

elif tela == "prestacao_contas":
    from pages import prestacao_contas

    prestacao_contas.render()

elif tela == "carregando_medicoes":
    # Compatibilidade defensiva; a transição genérica acima normalmente
    # converte esta rota antiga diretamente para Medições.
    st.session_state["carregamento_fos"] = {"destino": "medicoes", "rotulo": "Medições"}
    st.session_state["_fos_tela_anterior"] = "medicoes"
    st.rerun()

elif tela == "medicoes":
    from pages import medicoes

    medicoes.medicoes()

elif tela == "crm":
    from pages.crm.crm import crm

    crm()

elif tela == "uniformes_epis":
    from pages import uniformes_epis

    uniformes_epis.render()

elif tela == "novo_orcamento":
    from modulos.orcamentos.apresentacao import entrada as novo_orcamento

    novo_orcamento.render(autorizado=True)

elif tela == "obras":
    import pandas as pd

    from services.orcamentos_legado_operacional import carregar_github

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
    # Toda rota conhecida está declarada na fronteira central e no roteador.
    st.error("Rota indisponível.")
    st.stop()


# O menu já foi enviado ao navegador antes da escrita remota do log.
processar_log_pendente()