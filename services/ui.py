import streamlit as st

from services.loading_fos import _LOGO_FOS


def _renderizar_marca_login():
    """Renderiza somente a identidade visual do login, sem tocar na autenticação."""
    if st.session_state.get("autenticado"):
        return

    st.markdown(
        f"""
        <style>
        .fos-login-brand {{
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            text-align:center;
            padding: 2.6rem 0 1.4rem;
            animation: fosLoginEnter .75s cubic-bezier(.2,.75,.25,1) both;
        }}
        .fos-login-symbol-wrap {{
            position:relative;
            display:flex;
            align-items:center;
            justify-content:center;
            width:180px;
            height:150px;
            margin-bottom:.8rem;
        }}
        .fos-login-symbol-wrap::before {{
            content:"";
            position:absolute;
            width:132px;
            height:132px;
            border-radius:50%;
            background:rgba(169,80,53,.10);
            filter:blur(1px);
            animation:fosLoginHalo 3.8s ease-in-out infinite;
        }}
        .fos-login-symbol {{
            position:relative;
            z-index:1;
            width:150px;
            max-width:38vw;
            filter: drop-shadow(0 12px 18px rgba(38,52,69,.13));
            animation:fosLoginFloat 4.6s ease-in-out infinite;
        }}
        .fos-login-title {{
            color:#263445;
            font-size:2rem;
            line-height:1.15;
            font-weight:760;
            letter-spacing:-.02em;
            margin:.15rem 0 .45rem;
        }}
        .fos-login-subtitle {{
            color:#718096;
            font-size:1rem;
            margin:0;
        }}
        @keyframes fosLoginEnter {{
            from {{ opacity:0; transform:translateY(14px) scale(.985); }}
            to {{ opacity:1; transform:translateY(0) scale(1); }}
        }}
        @keyframes fosLoginFloat {{
            0%,100% {{ transform:translateY(0); }}
            50% {{ transform:translateY(-6px); }}
        }}
        @keyframes fosLoginHalo {{
            0%,100% {{ transform:scale(.92); opacity:.45; }}
            50% {{ transform:scale(1.08); opacity:.9; }}
        }}
        @media (prefers-reduced-motion: reduce) {{
            .fos-login-brand,
            .fos-login-symbol,
            .fos-login-symbol-wrap::before {{
                animation:none !important;
            }}
        }}
        </style>
        <div class="fos-login-brand">
            <div class="fos-login-symbol-wrap">
                <img class="fos-login-symbol" src="{_LOGO_FOS}" alt="FOS Engenharia">
            </div>
            <div class="fos-login-title">Acesso ao APP FOS</div>
            <p class="fos-login-subtitle">Sistema interno • FOS Engenharia LTDA</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# app.py importa este módulo antes de verificar_login(). Isso permite inserir a
# identidade visual acima do formulário sem alterar services/auth.py, que é um
# contrato protegido por testes de regressão.
_renderizar_marca_login()


def aplicar_estilo_global():

    st.markdown("""
    <style>

    :root {
        color-scheme: light !important;
    }

    html, body, [class*="css"] {
        color: #1e293b !important;
    }

    [data-testid="stAppViewContainer"] {
        background: #e9eef3 !important;
        color: #1e293b !important;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid #1e293b;
    }

    [data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #0f172a !important;
    }

    p, label {
        color: #0f172a !important;
    }

    .stButton > button {
        background-color: #1e3a5f !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: none !important;
        height: 42px;
        font-weight: 600 !important;
    }

    .stButton > button p,
    .stButton > button span,
    .stButton > button div {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    .stButton > button:hover {
        background-color: #2c5282 !important;
        color: #ffffff !important;
    }

    .stButton > button:hover p,
    .stButton > button:hover span,
    .stButton > button:hover div {
        color: #ffffff !important;
    }

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

    [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #1e293b !important;
        border-radius: 8px !important;
    }

    [data-baseweb="select"] * {
        color: #1e293b !important;
    }

    [data-testid="stDataFrame"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #cbd5e1 !important;
        overflow: hidden !important;
    }

    [data-testid="stDataFrame"] [role="gridcell"] {
        color: #111827 !important;
        background-color: #ffffff !important;
    }

    [data-testid="stDataFrame"] [role="gridcell"] * {
        color: #111827 !important;
    }

    [data-testid="stDataFrame"] [role="columnheader"] {
        background-color: #1e3a5f !important;
    }

    [data-testid="stDataFrame"] [role="columnheader"] * {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    [data-testid="stDataFrame"] [role="rowheader"] {
        background-color: #f1f5f9 !important;
    }

    [data-testid="stDataFrame"] [role="rowheader"] * {
        color: #334155 !important;
    }

    table {
        background-color: #ffffff !important;
        color: #111827 !important;
    }

    table th {
        background-color: #1e3a5f !important;
        color: #ffffff !important;
    }

    table th * {
        color: #ffffff !important;
    }

    table td {
        background-color: #ffffff !important;
        color: #111827 !important;
    }

    table td * {
        color: #111827 !important;
    }

    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        padding: 1rem;
        border-radius: 12px;
    }

    div[data-testid="stMetric"] * {
        color: #0f172a !important;
    }

    div[data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 12px !important;
    }

    div[data-testid="stExpander"] * {
        color: #0f172a !important;
    }

    button[data-baseweb="tab"] {
        color: #0f172a !important;
        font-weight: 600 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #1e3a5f !important;
        border-bottom-color: #1e3a5f !important;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    </style>
    """, unsafe_allow_html=True)
