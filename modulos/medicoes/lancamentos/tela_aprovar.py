import streamlit as st
from datetime import datetime

from modulos.medicoes.lancamentos.repositorio import (
    carregar_lancamentos_trabalho,
    salvar_lancamentos_trabalho,
)


def _usuario_logado():
    for chave in ["usuario", "email", "login", "usuario_logado"]:
        valor = st.session_state.get(chave)
        if isinstance(valor, str) and valor.strip():
            return valor.strip().lower()
    return ""


def tela_aprovar_lancamentos():
    st.markdown("## ✅ Aprovar Lançamentos")
    st.caption("Revise os lançamentos operacionais antes de liberá-los para medição.")

    df = carregar_lancamentos_trabalho()

    if df.empty:
        st.info("Nenhum lançamento encontrado.")
        return

    df = df.fillna("").copy()

    if "status_aprovacao" not in df.columns:
        df["status_aprovacao"] = "pendente"

    pendentes = df[
        df["status_aprovacao"].astype(str).str.lower().str.strip() == "pendente"
    ].copy()

    if pendentes.empty:
        st.success("Não há lançamentos pendentes de aprovação.")
        return

    obras = ["Todas"] + sorted(pendentes["nome_obra"].dropna().unique().tolist())

    obra_filtro = st.selectbox(
        "Filtrar por obra",
        options=obras,
        key="filtro_aprovacao_obra",
    )

    if obra_filtro != "Todas":
        pendentes = pendentes[pendentes["nome_obra"] == obra_filtro].copy()

    st.info(f"{len(pendentes)} lançamento(s) pendente(s).")

    for idx, row in pendentes.iterrows():
        lancamento_id = row.get("lancamento_id", "")

        with st.expander(
            f"{row.get('data_servico', '')} | {row.get('nome_obra', '')} | "
            f"{row.get('nome_local', '')} | {row.get('codigo_item', '')}",
            expanded=False,
        ):
            st.write(f"**Lançamento:** {lancamento_id}")
            st.write(f"**Obra:** {row.get('nome_obra', '')}")
            st.write(f"**Local:** {row.get('nome_local', '')}")
            st.write(f"**Item:** {row.get('codigo_item', '')} - {row.get('descricao_item', '')}")
            st.write(f"**Quantidade:** {row.get('quantidade_executada', '')} {row.get('unidade', '')}")
            st.write(f"**Data:** {row.get('data_servico', '')}")
            st.write(f"**Observação:** {row.get('observacao', '')}")
            st.write(f"**Foto:** {row.get('foto_url', '')}")
            st.write(f"**Criado por:** {row.get('criado_por', '')}")

            col1, col2 = st.columns(2)

            with col1:
                if st.button(
                    "✅ Aprovar",
                    key=f"aprovar_{lancamento_id}",
                    use_container_width=True,
                ):
                    df.loc[
                        df["lancamento_id"] == lancamento_id,
                        "status_aprovacao",
                    ] = "aprovado"

                    df.loc[
                        df["lancamento_id"] == lancamento_id,
                        "aprovado_por",
                    ] = _usuario_logado()

                    df.loc[
                        df["lancamento_id"] == lancamento_id,
                        "aprovado_em",
                    ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    df.loc[
                        df["lancamento_id"] == lancamento_id,
                        "atualizado_em",
                    ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    salvar_lancamentos_trabalho(df)
                    st.success("Lançamento aprovado.")
                    st.rerun()

            with col2:
                if st.button(
                    "❌ Reprovar",
                    key=f"reprovar_{lancamento_id}",
                    use_container_width=True,
                ):
                    df.loc[
                        df["lancamento_id"] == lancamento_id,
                        "status_aprovacao",
                    ] = "reprovado"

                    df.loc[
                        df["lancamento_id"] == lancamento_id,
                        "aprovado_por",
                    ] = _usuario_logado()

                    df.loc[
                        df["lancamento_id"] == lancamento_id,
                        "aprovado_em",
                    ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    df.loc[
                        df["lancamento_id"] == lancamento_id,
                        "atualizado_em",
                    ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    salvar_lancamentos_trabalho(df)
                    st.warning("Lançamento reprovado.")
                    st.rerun()
