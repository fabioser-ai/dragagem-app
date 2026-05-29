import uuid
from datetime import datetime

import pandas as pd
import streamlit as st


def agora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def agora_iso():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def novo_id(prefixo):
    return f"{prefixo}_{uuid.uuid4().hex[:10]}"


def dataframe_vazio(colunas):
    return pd.DataFrame(columns=colunas)


def moeda(valor):
    try:
        valor = float(valor)
    except Exception:
        valor = 0

    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def ir_para(etapa):
    st.session_state.etapa_medicoes = etapa
    st.rerun()
