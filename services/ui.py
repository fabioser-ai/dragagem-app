import streamlit as st

from services.loading_fos import _LOGO_FOS
from services.login_visual import FOS_LOGIN_BACKGROUND


def renderizar_login_fos():
    """Renderiza somente a identidade visual do login, sem tocar na autenticação."""
    st.markdown(
        f"""
        <style>
        /* LOGIN FOS FULL-SCREEN: injetado explicitamente apenas no fluxo deslogado. */
        [data-testid="stAppViewContainer"] {{
            position:relative;
            min-height:100vh;
            overflow:hidden;
            background:linear-gradient(132deg, #fcfaf8 0%, #f3ece7 52%, #fbf7f4 100%) !important;
        }}
        [data-testid="stAppViewContainer"]::before {{
            content:""; position:fixed; inset:-8vh -6vw; z-index:0; pointer-events:none;
            background-image:url("{FOS_LOGIN_BACKGROUND}"); background-repeat:no-repeat; background-position:center;
            background-size:min(82vw, 1280px) auto; opacity:.66;
            image-rendering:auto;
            filter:drop-shadow(0 35px 50px rgba(116,54,31,.08));
            transform:translate3d(0,0,0) scale(1.01);
            animation:fosLoginBackground 20s cubic-bezier(.45,.05,.55,.95) infinite alternate;
        }}
        [data-testid="stAppViewContainer"]::after {{
            content:""; position:fixed; inset:-12vh -12vw; z-index:1; pointer-events:none; opacity:.42;
            background:
                linear-gradient(120deg, transparent 0 40%, rgba(255,255,255,.72) 44%, transparent 48%),
                linear-gradient(154deg, transparent 0 58%, rgba(207,102,59,.08) 61%, transparent 64%);
            mask-image:linear-gradient(120deg, transparent 5%, #000 35%, #000 82%, transparent 98%);
            -webkit-mask-image:linear-gradient(120deg, transparent 5%, #000 35%, #000 82%, transparent 98%);
            animation:fosLoginLight 17s ease-in-out infinite alternate;
        }}
        [data-testid="stHeader"] {{ background:transparent !important; }}
        [data-testid="stSidebar"] {{ display:none !important; }}
        .block-container {{
            position:fixed; z-index:3; left:50%; top:50%; transform:translate(-50%, -50%);
            width:min(92vw, 460px) !important; max-width:460px !important; max-height:calc(100vh - 2rem);
            overflow-y:auto; padding:2.05rem 2.2rem 1.85rem !important; margin:0 !important;
            border:1px solid rgba(255,255,255,.92); border-radius:24px; background:rgba(255,255,255,.93);
            box-shadow:0 30px 70px rgba(76,48,38,.17),0 8px 24px rgba(76,48,38,.08),inset 0 1px 0 rgba(255,255,255,.96);
            backdrop-filter:blur(18px) saturate(1.08); -webkit-backdrop-filter:blur(18px) saturate(1.08);
            animation:fosLoginCardEnter .72s cubic-bezier(.2,.75,.25,1) both;
        }}
        .fos-login-brand {{ display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; margin:0 0 1.2rem; }}
        .fos-login-symbol-wrap {{ display:flex; align-items:center; justify-content:center; width:116px; height:84px; margin:0 auto .68rem; }}
        .fos-login-symbol {{ width:108px; max-height:80px; object-fit:contain; mix-blend-mode:multiply; filter:sepia(.12) saturate(1.05) drop-shadow(0 10px 15px rgba(80,48,35,.10)); }}
        .fos-login-title {{ color:#2b3440; font-size:1.72rem; line-height:1.18; font-weight:760; letter-spacing:-.025em; margin:0 0 .38rem; }}
        .fos-login-title strong {{ color:#b64f2b; font-weight:800; }}
        .fos-login-subtitle {{ color:#6f7075; font-size:.98rem; line-height:1.45; margin:0; }}
        .block-container h2, .block-container [data-testid="stCaptionContainer"] {{ display:none !important; }}
        .block-container label {{ color:#56585c !important; font-size:.9rem !important; font-weight:620 !important; }}
        .block-container input {{ min-height:50px !important; background:rgba(255,255,255,.97) !important; color:#27313c !important; border:1px solid #d7d2cf !important; border-radius:10px !important; box-shadow:inset 0 1px 2px rgba(31,41,55,.025) !important; }}
        .block-container input:focus {{ border-color:#bd5a35 !important; box-shadow:0 0 0 3px rgba(189,90,53,.12) !important; }}
        .block-container .stButton > button {{ width:100% !important; min-height:50px !important; margin-top:.35rem !important; border:0 !important; border-radius:10px !important; background:linear-gradient(135deg, #c45d35 0%, #ab4527 100%) !important; color:#fff !important; font-weight:720 !important; font-size:1.02rem !important; box-shadow:0 9px 20px rgba(155,65,36,.19) !important; transition:transform .18s ease, box-shadow .18s ease, filter .18s ease !important; }}
        .block-container .stButton > button:hover {{ color:#fff !important; filter:brightness(1.035); transform:translateY(-1px); box-shadow:0 11px 23px rgba(155,65,36,.24) !important; }}
        .block-container .stButton > button:active {{ transform:translateY(0); }}
        .block-container .stButton > button p, .block-container .stButton > button span, .block-container .stButton > button div {{ color:#fff !important; }}
        [data-testid="stAlert"] {{ position:relative; z-index:4; border-radius:10px !important; margin-top:.7rem; }}
        @keyframes fosLoginCardEnter {{ from {{ opacity:0; transform:translate(-50%, calc(-50% + 18px)) scale(.985); }} to {{ opacity:1; transform:translate(-50%, -50%) scale(1); }} }}
        @keyframes fosLoginBackground {{ 0% {{ transform:translate3d(-.5%, .35%, 0) scale(1.005); }} 100% {{ transform:translate3d(.5%, -.35%, 0) scale(1.018); }} }}
        @keyframes fosLoginLight {{ 0% {{ transform:translate3d(-1.5%, 1%, 0); opacity:.34; }} 100% {{ transform:translate3d(1.5%, -1%, 0); opacity:.48; }} }}
        @media (max-width: 640px) {{
            [data-testid="stAppViewContainer"]::before {{ background-size:auto 72vh; opacity:.38; }}
            .block-container {{ width:calc(100vw - 1.5rem) !important; max-width:430px !important; padding:1.6rem 1.35rem 1.45rem !important; border-radius:20px; }}
            .fos-login-symbol-wrap {{ width:96px; height:70px; margin-bottom:.55rem; }}
            .fos-login-symbol {{ width:92px; max-height:68px; }} .fos-login-title {{ font-size:1.45rem; }} .fos-login-subtitle {{ font-size:.9rem; }}
        }}
        @media (max-height: 690px) {{
            .block-container {{ padding-top:1.25rem !important; padding-bottom:1.2rem !important; }}
            .fos-login-symbol-wrap {{ height:58px; margin-bottom:.3rem; }} .fos-login-symbol {{ width:78px; max-height:56px; }} .fos-login-brand {{ margin-bottom:.8rem; }}
        }}
        @media (prefers-reduced-motion: reduce) {{
            [data-testid="stAppViewContainer"]::before, [data-testid="stAppViewContainer"]::after, .block-container {{ animation:none !important; }}
            .block-container .stButton > button {{ transition:none !important; }}
        }}
        </style>
        <div class="fos-login-brand">
            <div class="fos-login-symbol-wrap"><img class="fos-login-symbol" src="{_LOGO_FOS}" alt="FOS Engenharia"></div>
            <div class="fos-login-title">Acesso ao <strong>APP FOS</strong></div>
            <p class="fos-login-subtitle">Entre com suas credenciais para continuar</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def aplicar_estilo_global():
    st.markdown("""
    <style>
    :root { color-scheme: light !important; }
    html, body, [class*="css"] { color: #1e293b !important; }
    [data-testid="stAppViewContainer"] { background: #e9eef3 !important; color: #1e293b !important; }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] { background-color: #0f172a !important; border-right: 1px solid #1e293b; }
    [data-testid="stSidebar"] * { color: #f8fafc !important; }
    h1, h2, h3, h4, h5, h6 { color: #0f172a !important; }
    p, label { color: #0f172a !important; }
    .stButton > button { background-color: #1e3a5f !important; color: #ffffff !important; border-radius: 10px !important; border: none !important; height: 42px; font-weight: 600 !important; }
    .stButton > button p, .stButton > button span, .stButton > button div { color: #ffffff !important; font-weight: 600 !important; }
    .stButton > button:hover { background-color: #2c5282 !important; color: #ffffff !important; }
    .stButton > button:hover p, .stButton > button:hover span, .stButton > button:hover div { color: #ffffff !important; }
    input, textarea { background-color: #ffffff !important; color: #1e293b !important; border: 1px solid #cbd5e1 !important; border-radius: 8px !important; }
    input::placeholder, textarea::placeholder { color: #64748b !important; }
    [data-baseweb="select"] > div { background-color: #ffffff !important; color: #1e293b !important; border-radius: 8px !important; }
    [data-baseweb="select"] * { color: #1e293b !important; }
    [data-testid="stDataFrame"] { background-color: #ffffff !important; border-radius: 12px !important; border: 1px solid #cbd5e1 !important; overflow: hidden !important; }
    [data-testid="stDataFrame"] [role="gridcell"] { color: #111827 !important; background-color: #ffffff !important; }
    [data-testid="stDataFrame"] [role="gridcell"] * { color: #111827 !important; }
    [data-testid="stDataFrame"] [role="columnheader"] { background-color: #1e3a5f !important; }
    [data-testid="stDataFrame"] [role="columnheader"] * { color: #ffffff !important; font-weight: 700 !important; }
    [data-testid="stDataFrame"] [role="rowheader"] { background-color: #f1f5f9 !important; }
    [data-testid="stDataFrame"] [role="rowheader"] * { color: #334155 !important; }
    table { background-color: #ffffff !important; color: #111827 !important; }
    table th { background-color: #1e3a5f !important; color: #ffffff !important; }
    table th * { color: #ffffff !important; }
    table td { background-color: #ffffff !important; color: #111827 !important; }
    table td * { color: #111827 !important; }
    div[data-testid="stMetric"] { background-color: #ffffff !important; border: 1px solid #cbd5e1 !important; padding: 1rem; border-radius: 12px; }
    div[data-testid="stMetric"] * { color: #0f172a !important; }
    div[data-testid="stExpander"] { background-color: #ffffff !important; border: 1px solid #cbd5e1 !important; border-radius: 12px !important; }
    div[data-testid="stExpander"] * { color: #0f172a !important; }
    button[data-baseweb="tab"] { color: #0f172a !important; font-weight: 600 !important; }
    button[data-baseweb="tab"][aria-selected="true"] { color: #1e3a5f !important; border-bottom-color: #1e3a5f !important; }
    .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
    </style>
    """, unsafe_allow_html=True)
