import streamlit as st
from datetime import datetime
from pathlib import Path

from modulos.medicoes.repositorio import salvar_lancamento_producao


def tela_lancamento_producao():
    st.markdown("## 📝 Lançamento de Produção")
    st.caption("Registro simples de produção executada em campo.")

    st.divider()

    with st.form("form_lancamento_producao", clear_on_submit=True):
        obra = st.text_input("Obra *")
        local_trabalho = st.text_input("Local de trabalho *")

        data_servico = st.date_input("Data do serviço")

        atividade_executada = st.text_area(
            "Atividade executada *",
            placeholder="Descreva o serviço executado em campo...",
        )

        foto = st.file_uploader(
            "Foto comprobatória",
            type=["png", "jpg", "jpeg"],
        )

        observacao = st.text_area(
            "Observações",
            placeholder="Informações adicionais, dificuldades, condições do local etc.",
        )

        enviado = st.form_submit_button(
            "Salvar lançamento",
            use_container_width=True,
        )

    if enviado:
        if not obra or not local_trabalho or not atividade_executada:
            st.error("Preencha os campos obrigatórios: Obra, Local de trabalho e Atividade executada.")
            return

        usuario = st.session_state.get("usuario", "usuario_nao_identificado")

        dados = {
            "obra": obra,
            "local_trabalho": local_trabalho,
            "data_servico": str(data_servico),
            "atividade_executada": atividade_executada,
            "observacao": observacao,
            "usuario": usuario,
            "data_hora_lancamento": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "PENDENTE_ANALISE",
        }

        salvar_lancamento_producao(dados, foto)

        st.success("Lançamento de produção salvo com sucesso.")

    st.divider()

    if st.button("⬅ Voltar ao início das Medições", use_container_width=True):
        st.session_state["fluxo_medicoes"] = "inicio"
        st.rerun()
