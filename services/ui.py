import streamlit as st


def aplicar_estilo_global():

    st.markdown("""
    <style>

    /* ===== FUNDO ===== */

    [data-testid="stAppViewContainer"] {
        background: #e9eef3;
        color: #1e293b;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    /* ===== SIDEBAR ===== */

    [data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #1e293b;
    }

    [data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }

    /* ===== TÍTULOS ===== */

    h1, h2, h3 {
        color: #0f172a;
        font-weight: 700;
    }

    /* ===== BOTÕES ===== */

    .stButton > button {
        background-color: #1e3a5f;
        color: white !important;
        border-radius: 10px;
        border: none;
        height: 42px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #2c5282;
        color: white !important;
    }

    /* ===== INPUTS ===== */

    input, textarea {
        background-color: white !important;
        color: #1e293b !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
    }

    /* ===== SELECTBOX ===== */

    [data-baseweb="select"] > div {
        background-color: white !important;
        color: #1e293b !important;
        border-radius: 8px !important;
    }

    /* ===== TABELAS ===== */

    .stDataFrame {
        background-color: white;
        border-radius: 12px;
        border: 1px solid #cbd5e1;
        overflow: hidden;
    }

    /* ===== CARDS ===== */

    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #cbd5e1;
        padding: 1rem;
        border-radius: 12px;
    }

    /* ===== ESPAÇAMENTO ===== */

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    </style>
    """, unsafe_allow_html=True)
