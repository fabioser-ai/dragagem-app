import streamlit as st
from datetime import datetime

from modulos.medicoes.repositorio import (
    carregar_bases,
    carregar_tabela_contrato,
    carregar_locais_trabalho,
    salvar_lancamento_producao,
)


def _valor_ativo(valor):
    return str(valor).strip().lower() in [
        "sim",
        "s",
        "ativo",
        "true",
        "1",
    ]


def _montar_label_obra(row):
    nome = str(row.get("nome_obra", "") or "").strip()
    contrato = str(row.get("contrato", "") or "").strip()

    if contrato:
        return f"{nome} — Contrato: {contrato}"

    return nome


def _montar_label_item(row):
    codigo = str(row.get("codigo", "") or "").strip()
    descricao = str(row.get("descricao", "") or "").strip()
    unidade = str(row.get("unidade", "") or "").strip()

    texto = f"{codigo} — {descricao}"

    if unidade:
        texto += f" ({unidade})"

    return texto


def tela_lancamento_producao():
    st.markdown("## 📝 Lançar Trabalho Executado")
    st.caption(
        "Selecione o serviço realizado, informe a quantidade, "
        "o local e anexe uma foto de comprovação."
    )

    st.divider()

    obras, _, _, _, _, _ = carregar_bases()
    locais = carregar_locais_trabalho()

    if obras.empty:
        st.warning("Nenhuma obra cadastrada. Cadastre uma obra antes de lançar trabalho executado.")
        return

    obras = obras.copy()
    obras["status_normalizado"] = obras["status"].fillna("").astype(str).str.lower()

    obras_ativas = obras[
        ~obras["status_normalizado"].isin(["inativa", "inativo", "encerrada", "encerrado"])
    ].copy()

    if obras_ativas.empty:
        st.warning("Nenhuma obra ativa disponível para lançamento.")
        return

    obras_ativas["label_obra"] = obras_ativas.apply(_montar_label_obra, axis=1)

    obra_label = st.selectbox(
        "Obra *",
        obras_ativas["label_obra"].tolist(),
        index=0,
    )

    obra = obras_ativas[obras_ativas["label_obra"] == obra_label].iloc[0]

    obra_id = str(obra.get("obra_id", "") or "").strip()
    nome_obra = str(obra.get("nome_obra", "") or "").strip()
    arquivo_tabela_servicos = str(obra.get("arquivo_tabela_servicos", "") or "").strip()

    if not obra_id:
        st.error("A obra selecionada não possui obra_id. Verifique o cadastro da obra.")
        return

    if not arquivo_tabela_servicos:
        st.warning(
            "Esta obra não possui tabela de serviços vinculada. "
            "Não é possível lançar trabalho executado sem itens contratuais."
        )
        return

    locais = locais.copy()

    if not locais.empty:
        locais["obra_id"] = locais["obra_id"].fillna("").astype(str).str.strip()
        locais["ativo_bool"] = locais["ativo"].apply(_valor_ativo)

    locais_obra = locais[
        (locais["obra_id"] == obra_id)
        & (locais["ativo_bool"] == True)
    ].copy() if not locais.empty else locais.copy()

    if locais_obra.empty:
        st.warning(
            "Nenhum local de trabalho ativo cadastrado para esta obra. "
            "Peça ao ADMIN para cadastrar o local antes do lançamento."
        )
        return

    locais_obra["nome_local"] = locais_obra["nome_local"].fillna("").astype(str).str.strip()
    locais_obra = locais_obra[locais_obra["nome_local"] != ""].copy()

    if locais_obra.empty:
        st.warning(
            "Os locais cadastrados para esta obra estão sem nome. "
            "Revise a tabela de locais de trabalho."
        )
        return

    tabela_itens = carregar_tabela_contrato(arquivo_tabela_servicos)

    if tabela_itens.empty:
        st.warning("A tabela contratual vinculada a esta obra está vazia ou não foi encontrada.")
        return

    tabela_itens = tabela_itens.copy()

    if "ativo" in tabela_itens.columns:
        tabela_itens = tabela_itens[tabela_itens["ativo"].apply(_valor_ativo)].copy()

    tabela_itens["codigo"] = tabela_itens["codigo"].fillna("").astype(str).str.strip()
    tabela_itens["descricao"] = tabela_itens["descricao"].fillna("").astype(str).str.strip()
    tabela_itens["unidade"] = tabela_itens["unidade"].fillna("").astype(str).str.strip()

    tabela_itens = tabela_itens[
        (tabela_itens["codigo"] != "")
        & (tabela_itens["descricao"] != "")
    ].copy()

    if tabela_itens.empty:
        st.warning("Nenhum item ativo válido foi encontrado na tabela contratual desta obra.")
        return

    locais_obra["label_local"] = locais_obra["nome_local"]
    tabela_itens["label_item"] = tabela_itens.apply(_montar_label_item, axis=1)

    with st.form("form_lancar_trabalho_executado", clear_on_submit=True):
        local_label = st.selectbox(
            "Local de trabalho *",
            locais_obra["label_local"].tolist(),
        )

        item_label = st.selectbox(
            "Serviço executado *",
            tabela_itens["label_item"].tolist(),
        )

        item = tabela_itens[tabela_itens["label_item"] == item_label].iloc[0]
        unidade = str(item.get("unidade", "") or "").strip()

        st.info(f"Unidade do item selecionado: **{unidade or 'não informada'}**")

        quantidade = st.number_input(
            f"Quantidade executada ({unidade or 'unidade não informada'}) *",
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
            placeholder="Opcional: detalhe alguma condição especial, interferência ou observação do campo.",
        )

        enviado = st.form_submit_button(
            "Salvar trabalho executado",
            use_container_width=True,
        )

    if enviado:
        if quantidade <= 0:
            st.error("Informe uma quantidade executada maior que zero.")
            return

        local = locais_obra[locais_obra["label_local"] == local_label].iloc[0]
        usuario = st.session_state.get("usuario", "usuario_nao_identificado")

        dados = {
            "obra_id": obra_id,
            "nome_obra": nome_obra,
            "local_id": str(local.get("local_id", "") or "").strip(),
            "nome_local": str(local.get("nome_local", "") or "").strip(),
            "codigo_item": str(item.get("codigo", "") or "").strip(),
            "descricao_item": str(item.get("descricao", "") or "").strip(),
            "unidade": unidade,
            "quantidade": quantidade,
            "data_servico": str(data_servico),
            "observacao": observacao,
            "usuario": usuario,
            "data_hora_lancamento": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "PENDENTE_ANALISE",
        }

        sucesso = salvar_lancamento_producao(dados, foto)

        if sucesso:
            st.success("Trabalho executado salvo com sucesso.")
        else:
            st.error("Não foi possível salvar o trabalho executado.")

    st.divider()

    if st.button("⬅ Voltar ao início das Medições", use_container_width=True):
        st.session_state["fluxo_medicoes"] = "inicio"
        st.rerun()
