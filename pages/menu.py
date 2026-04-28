import streamlit as st


def render():
    st.markdown(
        """
        <style>
            [data-testid="stAppViewContainer"] {
                background: radial-gradient(circle at top, #1d4ed8 0%, #0f172a 55%, #020617 100%);
            }

            [data-testid="stHeader"] {
                background: transparent;
            }

            .menu-hero {
                background: rgba(15, 23, 42, 0.78);
                border: 1px solid rgba(148, 163, 184, 0.45);
                border-radius: 20px;
                padding: 1.5rem 1.2rem;
                margin: 0.4rem 0 1.2rem 0;
                box-shadow: 0 16px 40px rgba(2, 6, 23, 0.35);
            }

            .menu-hero h1 {
                text-align: center;
                color: #f8fafc;
                margin: 0;
                font-size: 2.1rem;
                letter-spacing: 0.03em;
            }

            .menu-hero p {
                text-align: center;
                color: #cbd5e1;
                margin-top: 0.5rem;
                margin-bottom: 0;
                font-size: 1rem;
            }

            .menu-subtitle {
                text-align: center;
                color: #e2e8f0;
                margin-bottom: 1rem;
                font-weight: 600;
                letter-spacing: 0.02em;
            }

            .stButton > button {
                min-height: 84px;
                width: 100%;
                border-radius: 14px;
                border: 1px solid rgba(125, 211, 252, 0.7);
                background: rgba(15, 23, 42, 0.8);
                color: #f8fafc;
                font-size: 1.03rem;
                font-weight: 700;
                box-shadow: 0 6px 16px rgba(15, 23, 42, 0.25);
            }

            .stButton > button:hover {
                border-color: #38bdf8;
                background: rgba(30, 41, 59, 0.95);
                transform: translateY(-2px);
                box-shadow: 0 14px 24px rgba(14, 116, 144, 0.28);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="menu-hero">
            <h1>FOS ENGENHARIA - FABIO</h1>
            <p>Painel central para orçamento, obras, férias e base de dados</p>
        </div>
        <div class="menu-subtitle">Selecione um módulo para continuar</div>
        """,
        unsafe_allow_html=True,
    )

    st.info("✅ BUILD MENU: 2026-04-28 / commit afbedad")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        if st.button("📊 ORÇAMENTO", use_container_width=True):
            st.session_state.tela = "orcamento"

        if st.button("📅 FÉRIAS", use_container_width=True):
            st.session_state.tela = "ferias"

    with col2:
        if st.button("📈 OBRAS", use_container_width=True):
            st.session_state.tela = "obras"

        if st.button("📁 DADOS", use_container_width=True):
            st.session_state.tela = "dados"
