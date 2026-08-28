import streamlit as st

from services.autorizacao import pode, pode_acessar
from services.ferias_regras import normalizar_ciclo_vida_dataframe, recalcular_status_dataframe
from services.ui import renderizar_cabecalho_modulo
from pages import ferias as legado


FLUXO_KEY = "ferias_folgas_fluxo"


def _pode_visualizar(recurso: str) -> bool:
    return pode(modulo="ferias", recurso="registro", acao="visualizar")


def _voltar_landing():
    st.session_state.pop(FLUXO_KEY, None)
    st.rerun()


def _voltar_menu():
    st.session_state.pop(FLUXO_KEY, None)
    st.session_state.tela = "menu"
    st.rerun()


def _card(titulo: str, descricao: str, botao: str, fluxo: str):
    st.markdown(
        f"""
        <div style="
            border: 1px solid #cbd5e1;
            border-radius: 22px;
            padding: 1.5rem;
            min-height: 155px;
            background: rgba(255,255,255,.96);
            box-shadow: 0 10px 25px rgba(15,23,42,.08);
            margin-bottom: .75rem;
        ">
            <h3 style="margin:0 0 .5rem 0; color:#0f172a;">{titulo}</h3>
            <p style="margin:0; color:#64748b; line-height:1.5;">{descricao}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button(botao, use_container_width=True, key=f"ferias_hub_{fluxo}"):
        st.session_state[FLUXO_KEY] = fluxo
        st.rerun()


def _carregar_base_ferias():
    df_ferias, sha_ferias = legado.carregar_csv_seguro(legado.ARQ_FERIAS)
    if df_ferias is None:
        return None, None

    df_ferias = legado.normalizar_dataframe(df_ferias, legado.COLUNAS_FERIAS)
    df_ferias = normalizar_ciclo_vida_dataframe(
        df_ferias,
        coluna_inicio="Data_Inicio_Gozo",
        coluna_termino="Data_Fim_Gozo",
    )
    df_ferias = recalcular_status_dataframe(df_ferias)
    return df_ferias, sha_ferias


def _render_landing():
    renderizar_cabecalho_modulo(
        "Férias e Folgas", "← TELA INICIAL", _voltar_menu, key="ferias_header_menu"
    )
    st.caption("Escolha a área que deseja consultar ou administrar.")

    pode_ferias = _pode_visualizar("ferias")
    pode_folga = _pode_visualizar("folga")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        if pode_ferias:
            _card(
                "Férias",
                "Períodos aquisitivos, programação, vencimentos, histórico e acompanhamento do ciclo de vida.",
                "ABRIR FÉRIAS",
                "ferias",
            )

    with col2:
        if pode_folga:
            _card(
                "Folgas",
                "Programação de folgas, acompanhamento, histórico, intervalos e manutenção dos registros.",
                "ABRIR FOLGAS",
                "folgas",
            )

    if not pode_ferias and not pode_folga:
        st.warning("Nenhuma área de Férias e Folgas está disponível para seu usuário.")


def _render_ferias():
    if not _pode_visualizar("ferias"):
        st.error("Você não possui permissão para visualizar Férias.")
        return

    renderizar_cabecalho_modulo(
        "Férias", "← FÉRIAS E FOLGAS", _voltar_landing, key="ferias_header_areas"
    )
    st.caption("Consulta, programação e gestão do ciclo de férias.")

    df_ferias, sha_ferias = _carregar_base_ferias()
    if df_ferias is None:
        return

    legado.render_ferias(
        df_ferias,
        sha_ferias,
        pode(modulo="ferias", recurso="alertas", acao="enviar"),
        pode(modulo="ferias", recurso="ferias", acao="excluir"),
    )


def _render_folgas():
    if not _pode_visualizar("folga"):
        st.error("Você não possui permissão para visualizar Folgas.")
        return

    renderizar_cabecalho_modulo(
        "Folgas", "← FÉRIAS E FOLGAS", _voltar_landing, key="folgas_header_areas"
    )
    st.caption("Programação, acompanhamento e histórico de folgas.")

    df_ferias, _ = _carregar_base_ferias()
    if df_ferias is None:
        return

    legado.render_folgas(
        df_ferias,
        pode(modulo="ferias", recurso="folga", acao="excluir"),
    )


def render():
    if not pode_acessar("ferias"):
        st.error("Você não possui permissão para acessar Férias e Folgas.")
        st.stop()

    fluxo = st.session_state.get(FLUXO_KEY)

    if fluxo == "ferias":
        _render_ferias()
    elif fluxo == "folgas":
        _render_folgas()
    else:
        _render_landing()
