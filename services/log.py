import pandas as pd
import streamlit as st
from datetime import datetime
from services.github import carregar_github, salvar_github


ARQUIVO_LOG = "data/log_acessos.csv"


def registrar_log(usuario, perfil, acao):
    registro = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario": usuario,
        "perfil": perfil,
        "acao": acao,
    }

    try:
        df = carregar_github(
            ARQUIVO_LOG,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )
    except Exception:
        df = pd.DataFrame(columns=["data_hora", "usuario", "perfil", "acao"])

    df_novo = pd.DataFrame([registro])
    df = pd.concat([df, df_novo], ignore_index=True)

    salvar_github(
        df,
        ARQUIVO_LOG,
        st.secrets["GITHUB_TOKEN"],
        st.secrets["REPO"],
        mensagem_commit="log: atualização automática de acessos",
    )
