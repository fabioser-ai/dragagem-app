import streamlit as st


def aplicar_estilo_global():

    st.markdown("""
    <style>

    :root {
        color-scheme: light !important;
    }

    html, body, [class*="css"] {
        color: #1e293b !important;
    }

    /* ===== FUNDO ===== */

    [data-testid="stAppViewContainer"] {
        background: #e9eef3 !important;
        color: #1e293b !important;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    /* ===== SIDEBAR ===== */

    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid #1e293b;
    }

    [data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }

    /* ===== TÍTULOS ===== */

    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #0f172a !important;
    }

    /* ===== BOTÕES ===== */

    .stButton > button {
        background-color: #1e3a5f !important;
        color: white !important;
        border-radius: 10px;
        border: none;
        height: 42px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #2c5282 !important;
        color: white !important;
    }

    /* ===== INPUTS ===== */

    input, textarea {
        background-color: #ffffff !important;
        color: #1e293b !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
    }

    input::placeholder,
    textarea::placeholder {
        color: #64748b !important;
    }

    /* ===== SELECTBOX ===== */

    [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #1e293b !important;
        border-radius: 8px !important;
    }

    [data-baseweb="select"] * {
        color: #1e293b !important;
    }

    /* ===== TABELAS / DATAFRAMES ===== */

    [data-testid="stDataFrame"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #cbd5e1 !important;
        overflow: hidden !important;
    }

    [data-testid="stDataFrame"] * {
        color: #111827 !important;
    }

    [data-testid="stDataFrame"] [role="gridcell"] {
        color: #111827 !important;
        background-color: #ffffff !important;
    }

    [data-testid="stDataFrame"] [role="columnheader"] {
        background-color: #0f172a !important;
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    [data-testid="stDataFrame"] [role="rowheader"] {
        background-color: #f1f5f9 !important;
        color: #334155 !important;
    }

    /* Compatibilidade extra com tabelas HTML / Pandas Styler */

    table {
        background-color: #ffffff !important;
        color: #111827 !important;
    }

    table th {
        background-color: #0f172a !important;
        color: #ffffff !important;
    }

    table td {
        background-color: #ffffff !important;
        color: #111827 !important;
    }

    /* ===== MÉTRICAS / CARDS ===== */

    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        padding: 1rem;
        border-radius: 12px;
    }

    div[data-testid="stMetric"] * {
        color: #0f172a !important;
    }

    /* ===== ESPAÇAMENTO ===== */

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    </style>
    """, unsafe_allow_html=True)
