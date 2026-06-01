import streamlit as st

from services.auth import logout
from services.permissoes import pode_acessar_modulo, eh_superadmin


def render_card(titulo, descricao, botao, tela_destino):
    st.markdown(
        f"""
        <div class="module-card">
            <h3>{titulo}</h3>
            <p>{descricao}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(botao, use_container_width=True, key=f"btn_{tela_destino}"):
        st.session_state.tela = tela_destino
        st.rerun()


def render_card_medicoes():
    st.markdown(
        """
        <div class="module-card">
            <h3>Medições</h3>
            <p>Controle de boletins de medição, lançamentos de campo, aprovações e totais por obra.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("ABRIR MEDIÇÕES", use_container_width=True, key="btn_medicoes"):
        st.session_state.tela = "carregando_medicoes"
        st.session_state.pop("medicoes_carregadas", None)
        st.rerun()


def render():
    st.markdown(
        """
        <style>
            .main-header {
                background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 55%, #334155 100%);
                border: 1px solid rgba(148, 163, 184, 0.25);
                border-radius: 24px;
                padding: 2.5rem 2rem;
                margin-top: 0.5rem;
                margin-bottom: 1.5rem;
                box-shadow: 0 18px 45px rgba(15, 23, 42, 0.20);
                text-align: center;
            }

            .main-header h1 {
                color: #ffffff !important;
                margin: 0;
                font-size: 3.2rem;
                font-weight: 800;
                letter-spacing: 0.04em;
            }

            .main-header p {
                color: #dbeafe !important;
                margin-top: 0.9rem;
                margin-bottom: 0;
                font-size: 1.08rem;
                font-weight: 500;
            }

            .user-bar {
                background: rgba(255, 255, 255, 0.92);
                border: 1px solid #cbd5e1;
                border-radius: 16px;
                padding: 0.85rem 1rem;
                margin-bottom: 1.5rem;
                color: #334155;
                font-size: 0.95rem;
                font-weight: 600;
                box-shadow: 0 6px 18px rgba(15, 23, 42, 0.05);
            }

            .section-title {
                color: #0f172a;
                font-size: 1.30rem;
                font-weight: 800;
                margin-top: 0.5rem;
                margin-bottom: 1rem;
            }

            .module-card {
                background: rgba(255, 255, 255, 0.96);
                border: 1px solid #cbd5e1;
                border-radius: 22px;
                padding: 1.5rem;
                margin-bottom: 1rem;
                box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
                transition: 0.2s ease-in-out;
            }

            .module-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 18px 32px rgba(15, 23, 42, 0.12);
            }

            .module-card h3 {
                color: #0f172a !important;
                margin: 0 0 0.45rem 0;
                font-size: 1.25rem;
                font-weight: 800;
            }

            .module-card p {
                color: #64748b !important;
                margin: 0;
                font-size: 0.98rem;
                line-height: 1.5;
            }

            .stButton > button {
                min-height: 68px;
                width: 100%;
                border-radius: 18px !important;
                border: none !important;
                background: linear-gradient(135deg, #1e3a5f 0%, #2c5282 100%) !important;
                color: #ffffff !important;
                font-size: 1rem;
                font-weight: 800;
                letter-spacing: 0.02em;
                box-shadow: 0 10px 22px rgba(15, 23, 42, 0.16);
                transition: 0.2s ease-in-out;
            }

            .stButton > button:hover {
                transform: translateY(-2px);
                background: linear-gradient(135deg, #2c5282 0%, #3b82f6 100%) !important;
                color: #ffffff !important;
                box-shadow: 0 18px 30px rgba(15, 23, 42, 0.20);
            }

            .footer-note {
                text-align: center;
                color: #64748b;
                margin-top: 1.8rem;
                font-size: 0.90rem;
                font-weight: 500;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="main-header">
            <h1>FOS ENGENHARIA LTDA</h1>
            <p>Plataforma interna de gestão operacional, orçamentária e administrativa</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_user, col_logout = st.columns([4, 1])

    with col_user:
        st.markdown(
            f"""
            <div class="user-bar">
                Usuário: {st.session_state.get("usuario", "-")} &nbsp;&nbsp;|&nbsp;&nbsp;
                Perfil: {st.session_state.get("perfil", "-")}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_logout:
        if st.button("SAIR", use_container_width=True, key="btn_sair"):
            logout()

    st.markdown(
        '<div class="section-title">Módulos disponíveis</div>',
        unsafe_allow_html=True,
    )

    modulos_renderizados = 0

    col1, col2 = st.columns(2, gap="large")

    with col1:
        if pode_acessar_modulo("orcamento"):
            render_card(
                "Orçamento",
                "Elaboração, consolidação e análise de custos de obras de dragagem.",
                "ABRIR ORÇAMENTO",
                "orcamento",
            )
            modulos_renderizados += 1

        if pode_acessar_modulo("ferias"):
            render_card(
                "Férias",
                "Controle interno de períodos aquisitivos, vencimentos e programação.",
                "ABRIR FÉRIAS",
                "ferias",
            )
            modulos_renderizados += 1

        if pode_acessar_modulo("prestacao_contas"):
            render_card(
                "Prestação de Contas",
                "Gestão de despesas, comprovantes, reembolsos e acompanhamento financeiro.",
                "ABRIR PRESTAÇÃO DE CONTAS",
                "prestacao_contas",
            )
            modulos_renderizados += 1

        if pode_acessar_modulo("crm"):
            render_card(
                "CRM",
                "Cadastro de clientes, contatos, histórico comercial e prospecção de oportunidades.",
                "ABRIR CRM",
                "crm",
            )
            modulos_renderizados += 1

    with col2:
        if pode_acessar_modulo("obras"):
            render_card(
                "Obras",
                "Acompanhamento operacional, histórico e gestão de obras cadastradas.",
                "ABRIR OBRAS",
                "obras",
            )
            modulos_renderizados += 1

        if pode_acessar_modulo("dados"):
            render_card(
                "Dados",
                "Base técnica de insumos, equipes, equipamentos e parâmetros do sistema.",
                "ABRIR DADOS",
                "dados",
            )
            modulos_renderizados += 1

        if pode_acessar_modulo("medicoes"):
            render_card_medicoes()
            modulos_renderizados += 1

        if eh_superadmin():
            render_card(
                "Administração",
                "Gestão de permissões e acessos dos usuários.",
                "ABRIR ADMINISTRAÇÃO",
                "administracao",
            )
            modulos_renderizados += 1

    if modulos_renderizados == 0:
        st.warning("Nenhum módulo disponível para seu usuário.")

    st.markdown(
        """
        <div class="footer-note">
            FOS Engenharia LTDA • Plataforma interna de gestão operacional
        </div>
        """,
        unsafe_allow_html=True,
    )
