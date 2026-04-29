import streamlit as st


def render():
    st.markdown(
        """
        <style>
            [data-testid="stAppViewContainer"] {
                background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 45%, #cbd5e1 100%);
            }

            [data-testid="stHeader"] {
                background: transparent;
            }

            .main-header {
                background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
                border: 1px solid rgba(148, 163, 184, 0.35);
                border-radius: 24px;
                padding: 2.4rem 2rem;
                margin: 0.6rem 0 1.8rem 0;
                box-shadow: 0 18px 45px rgba(15, 23, 42, 0.12);
                text-align: center;
            }

            .main-header h1 {
                color: #0f172a;
                margin: 0;
                font-size: 3.6rem;
                font-weight: 800;
                letter-spacing: 0.04em;
            }

            .main-header p {
                color: #475569;
                margin-top: 0.75rem;
                margin-bottom: 0;
                font-size: 1.15rem;
                font-weight: 500;
            }

            .section-title {
                color: #0f172a;
                font-size: 1.25rem;
                font-weight: 800;
                margin-bottom: 0.8rem;
            }

            .module-card {
                background: rgba(255, 255, 255, 0.92);
                border: 1px solid rgba(148, 163, 184, 0.35);
                border-radius: 22px;
                padding: 1.4rem;
                margin-bottom: 1rem;
                box-shadow: 0 12px 28px rgba(15, 23, 42, 0.10);
            }

            .module-card h3 {
                color: #0f172a;
                margin: 0 0 0.35rem 0;
                font-size: 1.25rem;
                font-weight: 800;
            }

            .module-card p {
                color: #64748b;
                margin: 0;
                font-size: 0.98rem;
            }

            .stButton > button {
                min-height: 72px;
                width: 100%;
                border-radius: 18px;
                border: 1px solid rgba(15, 23, 42, 0.12);
                background: #0f172a;
                color: #ffffff;
                font-size: 1.05rem;
                font-weight: 800;
                box-shadow: 0 10px 22px rgba(15, 23, 42, 0.18);
            }

            .stButton > button:hover {
                background: #1e293b;
                border-color: #334155;
                transform: translateY(-2px);
                box-shadow: 0 16px 30px rgba(15, 23, 42, 0.22);
            }

            .footer-note {
                text-align: center;
                color: #64748b;
                margin-top: 1.4rem;
                font-size: 0.9rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="main-header">
            <h1>FOS ENGENHARIA LTDA</h1>
            <p>Sistema interno de gestão para orçamento, obras, férias e base de dados</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">Módulos principais</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="module-card">
                <h3>Orçamento</h3>
                <p>Elaboração e consolidação de custos de obras de dragagem.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("ABRIR ORÇAMENTO", use_container_width=True):
            st.session_state.tela = "orcamento"

        st.markdown(
            """
            <div class="module-card">
                <h3>Férias</h3>
                <p>Controle interno de períodos, vencimentos e programação.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("ABRIR FÉRIAS", use_container_width=True):
            st.session_state.tela = "ferias"

    with col2:
        st.markdown(
            """
            <div class="module-card">
                <h3>Obras</h3>
                <p>Acompanhamento de obras cadastradas e histórico operacional.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("ABRIR OBRAS", use_container_width=True):
            st.session_state.tela = "obras"

        st.markdown(
            """
            <div class="module-card">
                <h3>Dados</h3>
                <p>Base de insumos, equipes, equipamentos e parâmetros do sistema.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("ABRIR DADOS", use_container_width=True):
            st.session_state.tela = "dados"

    st.markdown(
        """
        <div class="footer-note">
            FOS Engenharia LTDA • Plataforma interna de gestão operacional
        </div>
        """,
        unsafe_allow_html=True,
    )
