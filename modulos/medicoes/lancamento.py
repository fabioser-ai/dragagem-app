import streamlit as st
from datetime import datetime

from modulos.medicoes.repositorio import (
    carregar_bases,
    carregar_tabela_contrato,
    carregar_locais_trabalho,
    salvar_lancamento_producao,
)


def tela_lancamento_producao():
    st.markdown("## 📝 Lançar Trabalho Executado")
    st.caption("Registre rapidamente o serviço executado em campo.")

    st.divider()

    obras, _, _, _, _, _ = carregar_bases()
    locais = carregar_locais_trabalho()

    obras_ativas = obras[obras["status"].fillna("").str.lower() != "inativa"].copy()

    if obras_ativas.empty:
        st.warning("Nenhuma obra cadastrada para lançamento.")
        return

    obras_ativas["label_obra"] = obras_ativas["nome_obra"].fillna("") + " — " + obras_ativas["contrato"].fillna("")

    obra_label = st.selectbox(
        "Obra *",
        obras_ativas["label_obra"].tolist(),
    )

    obra = obras_ativas[obras_ativas["label_obra"] == obra_label].iloc[0]
    obra_id = obra["obra_id"]
    nome_obra = obra["nome_obra"]
    arquivo_tabela = obra.get("arquivo_tabela_servicos", "")

    locais_obra = locais[
        (locais["obra_id"] == obra_id)
        & (locais["ativo"].fillna("").str.lower().isin(["sim", "s", "ativo", "true", "1"]))
    ].copy()

    if locais_obra.empty:
        st.warning("Nenhum local de trabalho cadastrado para esta obra. Solicite ao ADMIN incluir o local.")
        return

    locais_obra["label_local"] = locais_obra["nome_local"].fillna("")

    tabela_itens = carregar_tabela_contrato(arquivo_tabela)

    if tabela_itens.empty:
        st.warning("Nenhuma tabela de serviços vinculada a esta obra.")
        return

    tabela_itens = tabela_itens[
        tabela_itens["ativo"].fillna("").str.lower().isin(["sim", "s", "ativo", "true", "1"])
    ].copy()

    if tabela_itens.empty:
        st.warning("Nenhum item ativo encontrado na tabela contratual desta obra.")
        return

    tabela_itens["label_item"] = (
        tabela_itens["codigo"].fillna("")
        + " — "
        + tabela_itens["descricao"].fillna("")
    )

    with st.form("form_lancar_trabalho_executado", clear_on_submit=True):
        local_label = st.selectbox(
            "Local de trabalho *",
            locais_obra["label_local"].tolist(),
        )

        item_label = st.selectbox(
            "Item executado *",
            tabela_itens["label_item"].tolist(),
        )

        item = tabela_itens[tabela_itens["label_item"] == item_label].iloc[0]
        unidade = item.get("unidade", "")

        st.info(f"Unidade: **{unidade}**")

        quantidade = st.number_input(
            f"Quantidade executada ({unidade}) *",
            min_value=0.0,
            step=0.01,
            format="%.2f",
        )

        data_servico = st.date_input("Data do serviço")

        foto = st.file_uploader(
            "Foto do serviço concluído",
            type=["png", "jpg", "jpeg"],
        )

        observacao = st.text_area(
            "Observações",
            placeholder="Opcional: detalhe alguma condição especial do serviço.",
        )

        enviado = st.form_submit_button(
            "Salvar trabalho executado",
            use_container_width=True,
        )

    if enviado:
        if quantidade <= 0:
            st.error("Informe uma quantidade maior que zero.")
            return

        local = locais_obra[locais_obra["label_local"] == local_label].iloc[0]
        usuario = st.session_state.get("usuario", "usuario_nao_identificado")

        dados = {
            "obra_id": obra_id,
            "nome_obra": nome_obra,
            "local_id": local["local_id"],
            "nome_local": local["nome_local"],
            "codigo_item": item["codigo"],
            "descricao_item": item["descricao"],
            "unidade": unidade,
            "quantidade": quantidade,
            "data_servico": str(data_servico),
            "observacao": observacao,
            "usuario": usuario,
            "data_hora_lancamento": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "PENDENTE_ANALISE",
        }

        salvar_lancamento_producao(dados, foto)

        st.success("Trabalho executado salvo com sucesso.")

    st.divider()

    if st.button("⬅ Voltar ao início das Medições", use_container_width=True):
        st.session_state["fluxo_medicoes"] = "inicio"
        st.rerun()
