import streamlit as st
import pandas as pd
import uuid
from datetime import date
from services.github import carregar_github, salvar_github

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"
ARQ_HOR = "data/horarios.csv"
ARQ_DIAS = "data/dias.csv"
ARQ_SAL = "data/salarios.csv"

ARQ_ATESTADOS = "data/atestados.csv"
ARQ_ATESTADOS_SERVICOS = "data/atestados_servicos.csv"


def formatar_real(valor):
    try:
        return f"R$ {float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return "R$ 0,00"


def parse_moeda(valor):
    if pd.isna(valor) or valor == "":
        return None

    valor = str(valor).strip()
    valor = valor.replace("R$", "").replace(" ", "")
    valor = valor.replace(".", "").replace(",", ".")

    try:
        return float(valor)
    except:
        return None


def converter_valores(colunas, valores):
    valores_convertidos = []

    for i, c in enumerate(colunas):
        valor = valores[i]

        if c.lower() in [
            "vazao",
            "consumo",
            "valor",
            "valor_hora",
            "solidos_insitu",
            "solidos_desaguado"
        ]:
            convertido = parse_moeda(valor)

            if convertido is None:
                st.error(f"Valor inválido para '{c}': {valor}")
                return None

            valor = convertido

        valores_convertidos.append(valor)

    return valores_convertidos


def crud(arquivo, colunas, titulo, chave):
    st.subheader(titulo)

    df = carregar_github(arquivo, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=colunas)

    for col in df.columns:
        if col.lower() in ["valor", "valor_hora", "vazao", "consumo"]:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)

    df_display = df.copy()

    for col in df_display.columns:
        if col.lower() in ["valor", "valor_hora", "consumo"]:
            df_display[col] = df_display[col].apply(formatar_real)

    st.dataframe(df_display, use_container_width=True, hide_index=True)

    if not df.empty:
        st.divider()
        st.write("Editar registro")

        idx = st.selectbox("Selecionar para editar", df.index, key=f"sel_{chave}")
        linha = df.loc[idx]

        novos = []

        for c in colunas:
            if c.lower() in ["valor", "valor_hora", "consumo"]:
                valor_atual = formatar_real(linha[c])
            else:
                valor_atual = str(linha[c])

            novos.append(st.text_input(c, value=valor_atual, key=f"{chave}_{c}"))

        col1, col2 = st.columns(2)

        if col1.button("Salvar", key=f"save_{chave}", use_container_width=True):
            novos_convertidos = converter_valores(colunas, novos)

            if novos_convertidos is None:
                return

            for i, c in enumerate(colunas):
                df.at[idx, c] = novos_convertidos[i]

            salvar_github(df, arquivo, TOKEN, REPO)
            st.success("Atualizado com sucesso!")
            st.rerun()

        if col2.button("Excluir", key=f"del_{chave}", use_container_width=True):
            df = df.drop(idx).reset_index(drop=True)
            salvar_github(df, arquivo, TOKEN, REPO)

            st.warning("Removido!")
            st.rerun()

    st.divider()
    st.write("Adicionar novo")

    valores = []

    for c in colunas:
        valores.append(st.text_input(c, key=f"new_{chave}_{c}"))

    if st.button("Adicionar", key=f"add_{chave}", use_container_width=True):
        valores_convertidos = converter_valores(colunas, valores)

        if valores_convertidos is None:
            return

        df.loc[len(df)] = valores_convertidos

        salvar_github(df, arquivo, TOKEN, REPO)

        st.success("Adicionado com sucesso!")
        st.rerun()


def garantir_estrutura_atestados():
    col_atestados = [
        "id_atestado",
        "cliente",
        "contrato",
        "obra",
        "local",
        "ano",
        "data_inicio",
        "data_fim",
        "descricao",
        "observacoes"
    ]

    col_servicos = [
        "id_servico",
        "id_atestado",
        "servico",
        "unidade",
        "quantidade",
        "observacoes"
    ]

    df_atestados = carregar_github(ARQ_ATESTADOS, TOKEN, REPO)
    df_servicos = carregar_github(ARQ_ATESTADOS_SERVICOS, TOKEN, REPO)

    if df_atestados.empty:
        df_atestados = pd.DataFrame(columns=col_atestados)

    if df_servicos.empty:
        df_servicos = pd.DataFrame(columns=col_servicos)

    for col in col_atestados:
        if col not in df_atestados.columns:
            df_atestados[col] = ""

    for col in col_servicos:
        if col not in df_servicos.columns:
            df_servicos[col] = ""

    df_atestados = df_atestados[col_atestados].fillna("")
    df_servicos = df_servicos[col_servicos].fillna("")

    return df_atestados, df_servicos


def filtrar_atestados_por_busca(df_atestados, df_servicos, busca):
    if not busca or busca.strip() == "":
        return df_atestados.copy()

    termo = busca.strip().lower()

    servicos_filtrados = df_servicos[
        df_servicos.apply(
            lambda row: termo in " ".join([str(v).lower() for v in row.values]),
            axis=1
        )
    ]

    ids_por_servico = servicos_filtrados["id_atestado"].unique().tolist()

    atestados_filtrados = df_atestados[
        df_atestados.apply(
            lambda row: (
                termo in " ".join([str(v).lower() for v in row.values])
                or row["id_atestado"] in ids_por_servico
            ),
            axis=1
        )
    ]

    return atestados_filtrados.copy()


def render_atestados():
    st.subheader("Atestados")

    df_atestados, df_servicos = garantir_estrutura_atestados()

    aba1, aba2, aba3 = st.tabs([
        "Listar Atestados",
        "Novo Atestado",
        "Serviços Vinculados"
    ])

    with aba1:
        st.write("Atestados cadastrados")

        busca = st.text_input(
            "Buscar por palavra-chave",
            placeholder="Ex: con, concreto, dragagem, tubo, geotêxtil, lodo..."
        )

        df_atestados_filtrado = filtrar_atestados_por_busca(
            df_atestados,
            df_servicos,
            busca
        )

        if df_atestados.empty:
            st.info("Nenhum atestado cadastrado.")

        elif df_atestados_filtrado.empty:
            st.warning("Nenhum atestado encontrado para essa busca.")

        else:
            st.caption(
                f"Exibindo {len(df_atestados_filtrado)} de {len(df_atestados)} atestados cadastrados."
            )

            colunas_exibir = [
                "cliente",
                "contrato",
                "obra",
                "local",
                "ano",
                "data_inicio",
                "data_fim"
            ]

            st.dataframe(
                df_atestados_filtrado[colunas_exibir],
                use_container_width=True,
                hide_index=True
            )

            st.divider()
            st.write("Detalhes do atestado")

            opcoes = {
                f"{row['cliente']} | {row['obra']} | {row['contrato']}": row["id_atestado"]
                for _, row in df_atestados_filtrado.iterrows()
            }

            escolha = st.selectbox(
                "Selecionar atestado",
                list(opcoes.keys()),
                key="sel_visualizar_atestado"
            )

            id_atestado = opcoes[escolha]

            atestado = df_atestados[
                df_atestados["id_atestado"] == id_atestado
            ].iloc[0]

            st.write("**Cliente:**", atestado["cliente"])
            st.write("**Contrato:**", atestado["contrato"])
            st.write("**Obra:**", atestado["obra"])
            st.write("**Local:**", atestado["local"])
            st.write("**Ano:**", atestado["ano"])
            st.write("**Data início:**", atestado["data_inicio"])
            st.write("**Data fim:**", atestado["data_fim"])
            st.write("**Descrição:**", atestado["descricao"])
            st.write("**Observações:**", atestado["observacoes"])

            st.divider()
            st.write("Serviços vinculados")

            servicos = df_servicos[df_servicos["id_atestado"] == id_atestado]

            if busca and busca.strip() != "":
                termo = busca.strip().lower()
                servicos_display = servicos[
                    servicos.apply(
                        lambda row: termo in " ".join([str(v).lower() for v in row.values]),
                        axis=1
                    )
                ]

                if servicos_display.empty:
                    servicos_display = servicos.copy()
                    st.caption("O atestado foi encontrado pelos dados principais. Exibindo todos os serviços vinculados.")
                else:
                    st.caption("Exibindo serviços que bateram com a busca.")
            else:
                servicos_display = servicos.copy()

            if servicos_display.empty:
                st.info("Nenhum serviço vinculado a este atestado.")
            else:
                st.dataframe(
                    servicos_display[["servico", "unidade", "quantidade", "observacoes"]],
                    use_container_width=True,
                    hide_index=True
                )

            st.divider()

            col_editar, col_excluir = st.columns(2)

            with col_editar:
                if st.button("Editar este atestado", key="btn_editar_atestado", use_container_width=True):
                    st.session_state.atestado_em_edicao = id_atestado

            with col_excluir:
                if st.button("Excluir este atestado", key="btn_excluir_atestado", use_container_width=True):
                    df_atestados = df_atestados[
                        df_atestados["id_atestado"] != id_atestado
                    ].reset_index(drop=True)

                    df_servicos = df_servicos[
                        df_servicos["id_atestado"] != id_atestado
                    ].reset_index(drop=True)

                    salvar_github(df_atestados, ARQ_ATESTADOS, TOKEN, REPO)
                    salvar_github(df_servicos, ARQ_ATESTADOS_SERVICOS, TOKEN, REPO)

                    st.warning("Atestado e serviços vinculados foram excluídos.")
                    st.rerun()

            if "atestado_em_edicao" in st.session_state:
                id_edicao = st.session_state.atestado_em_edicao

                if id_edicao == id_atestado:
                    st.divider()
                    st.write("Editar atestado")

                    idx = df_atestados[
                        df_atestados["id_atestado"] == id_edicao
                    ].index[0]

                    linha = df_atestados.loc[idx]

                    with st.form("form_editar_atestado"):
                        cliente = st.text_input("Cliente", value=linha["cliente"])
                        contrato = st.text_input("Contrato", value=linha["contrato"])
                        obra = st.text_input("Obra", value=linha["obra"])
                        local = st.text_input("Local", value=linha["local"])
                        ano = st.text_input("Ano", value=linha["ano"])
                        data_inicio = st.text_input("Data início", value=linha["data_inicio"])
                        data_fim = st.text_input("Data fim", value=linha["data_fim"])
                        descricao = st.text_area("Descrição", value=linha["descricao"])
                        observacoes = st.text_area("Observações", value=linha["observacoes"])

                        salvar_edicao = st.form_submit_button("Salvar alterações")

                        if salvar_edicao:
                            df_atestados.at[idx, "cliente"] = cliente
                            df_atestados.at[idx, "contrato"] = contrato
                            df_atestados.at[idx, "obra"] = obra
                            df_atestados.at[idx, "local"] = local
                            df_atestados.at[idx, "ano"] = ano
                            df_atestados.at[idx, "data_inicio"] = data_inicio
                            df_atestados.at[idx, "data_fim"] = data_fim
                            df_atestados.at[idx, "descricao"] = descricao
                            df_atestados.at[idx, "observacoes"] = observacoes

                            salvar_github(df_atestados, ARQ_ATESTADOS, TOKEN, REPO)

                            del st.session_state.atestado_em_edicao

                            st.success("Atestado atualizado com sucesso!")
                            st.rerun()

    with aba2:
        st.write("Cadastrar novo atestado")

        with st.form("form_novo_atestado"):
            cliente = st.text_input("Cliente")
            contrato = st.text_input("Contrato")
            obra = st.text_input("Obra")
            local = st.text_input("Local")
            ano = st.text_input("Ano", value=str(date.today().year))
            data_inicio = st.date_input("Data início", value=date.today())
            data_fim = st.date_input("Data fim", value=date.today())
            descricao = st.text_area("Descrição")
            observacoes = st.text_area("Observações")

            salvar = st.form_submit_button("Salvar atestado")

            if salvar:
                if not cliente or not obra:
                    st.error("Cliente e obra são campos obrigatórios.")
                    return

                novo = {
                    "id_atestado": str(uuid.uuid4()),
                    "cliente": cliente,
                    "contrato": contrato,
                    "obra": obra,
                    "local": local,
                    "ano": ano,
                    "data_inicio": str(data_inicio),
                    "data_fim": str(data_fim),
                    "descricao": descricao,
                    "observacoes": observacoes
                }

                df_atestados = pd.concat(
                    [df_atestados, pd.DataFrame([novo])],
                    ignore_index=True
                )

                salvar_github(df_atestados, ARQ_ATESTADOS, TOKEN, REPO)

                st.success("Atestado cadastrado com sucesso!")
                st.rerun()

    with aba3:
        st.write("Adicionar serviços vinculados")

        if df_atestados.empty:
            st.info("Cadastre primeiro um atestado.")
        else:
            opcoes = {
                f"{row['cliente']} | {row['obra']} | {row['contrato']}": row["id_atestado"]
                for _, row in df_atestados.iterrows()
            }

            escolha = st.selectbox(
                "Selecionar atestado",
                list(opcoes.keys()),
                key="sel_atestado_servico"
            )

            id_atestado = opcoes[escolha]

            st.divider()

            with st.form("form_novo_servico_atestado"):
                servico = st.text_input("Serviço")
                unidade = st.text_input("Unidade", placeholder="m³, m², m, un, mês...")
                quantidade = st.number_input("Quantidade", min_value=0.0, step=0.01)
                observacoes = st.text_area("Observações")

                salvar_servico = st.form_submit_button("Adicionar serviço")

                if salvar_servico:
                    if not servico:
                        st.error("Informe o serviço.")
                        return

                    novo_servico = {
                        "id_servico": str(uuid.uuid4()),
                        "id_atestado": id_atestado,
                        "servico": servico,
                        "unidade": unidade,
                        "quantidade": quantidade,
                        "observacoes": observacoes
                    }

                    df_servicos = pd.concat(
                        [df_servicos, pd.DataFrame([novo_servico])],
                        ignore_index=True
                    )

                    salvar_github(df_servicos, ARQ_ATESTADOS_SERVICOS, TOKEN, REPO)

                    st.success("Serviço vinculado com sucesso!")
                    st.rerun()

            st.divider()
            st.write("Serviços já vinculados")

            servicos_atestado = df_servicos[
                df_servicos["id_atestado"] == id_atestado
            ].reset_index(drop=True)

            if servicos_atestado.empty:
                st.info("Nenhum serviço vinculado a este atestado.")
            else:
                st.dataframe(
                    servicos_atestado[["servico", "unidade", "quantidade", "observacoes"]],
                    use_container_width=True,
                    hide_index=True
                )

                st.divider()

                idx_servico = st.selectbox(
                    "Selecionar serviço para excluir",
                    servicos_atestado.index,
                    key="sel_excluir_servico_atestado"
                )

                if st.button("Excluir serviço selecionado", key="btn_excluir_servico_atestado", use_container_width=True):
                    id_servico = servicos_atestado.loc[idx_servico, "id_servico"]

                    df_servicos = df_servicos[
                        df_servicos["id_servico"] != id_servico
                    ].reset_index(drop=True)

                    salvar_github(df_servicos, ARQ_ATESTADOS_SERVICOS, TOKEN, REPO)

                    st.warning("Serviço excluído.")
                    st.rerun()


def render():
    st.title("Dados")

    if "subdados" not in st.session_state:
        st.session_state.subdados = "equip"

    st.markdown("### Selecione uma base de dados")

    opcoes = {
        "Equipamentos": "equip",
        "Materiais": "mat",
        "Desaguamento": "desag",
        "Horários": "hor",
        "Dias": "dias",
        "Salários": "sal",
        "Atestados": "atestados"
    }

    escolha = st.radio(
        "Menu de Dados",
        list(opcoes.keys()),
        index=list(opcoes.values()).index(st.session_state.subdados)
        if st.session_state.subdados in opcoes.values()
        else 0,
        label_visibility="collapsed"
    )

    st.session_state.subdados = opcoes[escolha]

    st.divider()

    if st.session_state.subdados == "equip":
        crud(ARQ_EQUIP, ["Equipamento", "Vazao", "Consumo", "Valor"], "Equipamentos", "equip")

    elif st.session_state.subdados == "mat":
        crud(ARQ_MAT, ["Material", "Solidos_InSitu", "Solidos_Desaguado"], "Materiais", "mat")

    elif st.session_state.subdados == "desag":
        crud(ARQ_DESAG, ["Tipo"], "Desaguamento", "desag")

    elif st.session_state.subdados == "hor":
        crud(ARQ_HOR, ["Inicio", "Fim"], "Horários", "hor")

    elif st.session_state.subdados == "dias":
        crud(ARQ_DIAS, ["Descricao"], "Dias", "dias")

    elif st.session_state.subdados == "sal":
        crud(ARQ_SAL, ["Posicao", "Valor_Hora"], "Salários", "sal")

    elif st.session_state.subdados == "atestados":
        render_atestados()

    st.divider()

    if st.button("⬅ Voltar", use_container_width=True):
        st.session_state.tela = "menu"
        st.rerun()
