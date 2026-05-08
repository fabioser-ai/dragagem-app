import uuid
from datetime import date, datetime

import pandas as pd
import streamlit as st

from services.auth import exigir_admin
from services.github import (
    carregar_github,
    salvar_github,
    salvar_arquivo_github,
    carregar_arquivo_github,
)


TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

ARQ_TIPOS = "data/tipos_despesa.csv"
ARQ_DESPESAS = "data/prestacao_contas.csv"
PASTA_COMPROVANTES = "data/comprovantes"


COLUNAS_TIPOS = [
    "Tipo_Despesa",
    "Descricao",
    "Ativo",
    "Criado_Por",
    "Data_Registro",
]

COLUNAS_DESPESAS = [
    "ID",
    "Matricula",
    "Funcionario",
    "Unidade",
    "Departamento",
    "Data_Despesa",
    "Tipo_Despesa",
    "Descricao",
    "Valor",
    "Arquivo_Comprovante",
    "Status",
    "Criado_Por",
    "Data_Registro",
    "Aprovado_Por",
    "Data_Aprovacao",
    "Observacoes_Aprovacao",
]


def normalizar_dataframe(df, colunas):
    if df.empty:
        df = pd.DataFrame(columns=colunas)

    for col in colunas:
        if col not in df.columns:
            df[col] = ""

    df = df[colunas].copy()

    for col in df.columns:
        df[col] = df[col].astype("object")

    return df


def formatar_data_br(valor):
    try:
        data = pd.to_datetime(valor, errors="coerce")
        if pd.isna(data):
            return ""
        return data.strftime("%d/%m/%Y")
    except Exception:
        return ""


def formatar_datetime_br(valor):
    try:
        data = pd.to_datetime(valor, errors="coerce")
        if pd.isna(data):
            return ""
        return data.strftime("%d/%m/%Y %H:%M:%S")
    except Exception:
        return ""


def formatar_moeda(valor):
    try:
        numero = float(valor)
    except Exception:
        numero = 0.0

    return f"R$ {numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def preparar_exibicao(df):
    df_exibir = df.copy()

    if "Data_Despesa" in df_exibir.columns:
        df_exibir["Data_Despesa"] = df_exibir["Data_Despesa"].apply(formatar_data_br)

    if "Data_Registro" in df_exibir.columns:
        df_exibir["Data_Registro"] = df_exibir["Data_Registro"].apply(formatar_datetime_br)

    if "Data_Aprovacao" in df_exibir.columns:
        df_exibir["Data_Aprovacao"] = df_exibir["Data_Aprovacao"].apply(formatar_datetime_br)

    if "Valor" in df_exibir.columns:
        df_exibir["Valor"] = df_exibir["Valor"].apply(formatar_moeda)

    return df_exibir


def carregar_tipos():
    df = carregar_github(ARQ_TIPOS, TOKEN, REPO)
    return normalizar_dataframe(df, COLUNAS_TIPOS)


def carregar_despesas():
    df = carregar_github(ARQ_DESPESAS, TOKEN, REPO)
    return normalizar_dataframe(df, COLUNAS_DESPESAS)


def obter_dados_funcionario():
    matricula = st.session_state.get("matricula", "")
    nome = st.session_state.get("nome", "")
    usuario = st.session_state.get("usuario", "")

    try:
        from pages import ferias

        df_ferias = carregar_github(
            ferias.ARQ_FERIAS,
            TOKEN,
            REPO,
        )

        if not df_ferias.empty:
            df_func = df_ferias[
                df_ferias["Matricula"].astype(str) == str(matricula)
            ]

            if not df_func.empty:
                linha = df_func.iloc[0]

                return {
                    "Matricula": matricula,
                    "Funcionario": linha.get("Funcionario", nome),
                    "Unidade": linha.get("Unidade", ""),
                    "Departamento": linha.get("Departamento", ""),
                    "Usuario": usuario,
                }

    except Exception:
        pass

    return {
        "Matricula": matricula,
        "Funcionario": nome,
        "Unidade": "",
        "Departamento": "",
        "Usuario": usuario,
    }


def salvar_comprovante(upload, id_despesa):
    if upload is None:
        return ""

    extensao = upload.name.split(".")[-1].lower()

    nome_limpo = upload.name.replace(" ", "_").replace("/", "_").replace("\\", "_")

    nome_arquivo = (
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_"
        f"{id_despesa}_{nome_limpo}"
    )

    caminho = f"{PASTA_COMPROVANTES}/{nome_arquivo}"

    salvar_arquivo_github(
        upload.getvalue(),
        caminho,
        TOKEN,
        REPO,
        mensagem=f"Upload comprovante {id_despesa}",
    )

    return caminho


def render_comprovante(caminho):
    if not caminho or str(caminho).strip() == "":
        st.info("Esta despesa não possui comprovante anexado.")
        return

    try:
        arquivo_bytes = carregar_arquivo_github(caminho, TOKEN, REPO)

        if arquivo_bytes is None:
            st.warning("Comprovante não encontrado no GitHub.")
            return

        extensao = str(caminho).split(".")[-1].lower()

        if extensao in ["png", "jpg", "jpeg"]:
            st.image(arquivo_bytes, caption=caminho, use_container_width=True)

        elif extensao == "pdf":
            st.download_button(
                "Baixar comprovante PDF",
                data=arquivo_bytes,
                file_name=str(caminho).split("/")[-1],
                mime="application/pdf",
                use_container_width=True,
            )
            st.info("PDF disponível para download.")

        else:
            st.download_button(
                "Baixar comprovante",
                data=arquivo_bytes,
                file_name=str(caminho).split("/")[-1],
                use_container_width=True,
            )

    except Exception as erro:
        st.error(f"Erro ao carregar comprovante: {erro}")


def render_nova_despesa():
    st.subheader("Nova Despesa")

    dados_func = obter_dados_funcionario()

    col1, col2 = st.columns(2)

    with col1:
        st.text_input(
            "Funcionário",
            value=str(dados_func["Funcionario"]),
            disabled=True,
            key="nova_funcionario",
        )

    with col2:
        st.text_input(
            "Matrícula",
            value=str(dados_func["Matricula"]),
            disabled=True,
            key="nova_matricula",
        )

    col3, col4 = st.columns(2)

    with col3:
        st.text_input(
            "Unidade",
            value=str(dados_func["Unidade"]),
            disabled=True,
            key="nova_unidade",
        )

    with col4:
        st.text_input(
            "Departamento",
            value=str(dados_func["Departamento"]),
            disabled=True,
            key="nova_departamento",
        )

    df_tipos = carregar_tipos()

    tipos_ativos = (
        df_tipos[df_tipos["Ativo"].astype(str).str.lower() == "sim"]["Tipo_Despesa"]
        .dropna()
        .astype(str)
        .tolist()
    )

    tipos_ativos = sorted(tipos_ativos)

    if not tipos_ativos:
        st.error("Nenhum tipo de despesa ativo cadastrado.")
        return

    data_despesa = st.date_input(
        "Data da despesa",
        value=date.today(),
        format="DD/MM/YYYY",
        key="nova_data_despesa",
    )

    tipo_despesa = st.selectbox(
        "Tipo de despesa",
        tipos_ativos,
        key="nova_tipo_despesa",
    )

    valor = st.number_input(
        "Valor da despesa (R$)",
        min_value=0.0,
        step=10.0,
        format="%.2f",
        key="nova_valor",
    )

    descricao = st.text_area(
        "Descrição / Observações",
        key="nova_descricao",
    )

    comprovante = st.file_uploader(
        "Anexar comprovante",
        type=["png", "jpg", "jpeg", "pdf"],
        key="nova_comprovante",
    )

    if comprovante:
        st.success(f"Arquivo selecionado: {comprovante.name}")

    if st.button("Enviar prestação de contas", use_container_width=True, key="btn_enviar_prestacao"):
        if valor <= 0:
            st.error("Informe um valor válido.")
            return

        id_despesa = str(uuid.uuid4())

        try:
            caminho_comprovante = salvar_comprovante(comprovante, id_despesa)
        except Exception as erro:
            st.error(f"Erro ao salvar comprovante: {erro}")
            return

        nova_despesa = {
            "ID": id_despesa,
            "Matricula": str(dados_func["Matricula"]),
            "Funcionario": str(dados_func["Funcionario"]),
            "Unidade": str(dados_func["Unidade"]),
            "Departamento": str(dados_func["Departamento"]),
            "Data_Despesa": data_despesa,
            "Tipo_Despesa": str(tipo_despesa),
            "Descricao": str(descricao),
            "Valor": float(valor),
            "Arquivo_Comprovante": caminho_comprovante,
            "Status": "Pendente",
            "Criado_Por": str(dados_func["Usuario"]),
            "Data_Registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Aprovado_Por": "",
            "Data_Aprovacao": "",
            "Observacoes_Aprovacao": "",
        }

        df_despesas = carregar_despesas()

        df_despesas = pd.concat(
            [df_despesas, pd.DataFrame([nova_despesa])],
            ignore_index=True,
        )

        df_despesas = normalizar_dataframe(
            df_despesas,
            COLUNAS_DESPESAS,
        )

        salvar_github(
            df_despesas,
            ARQ_DESPESAS,
            TOKEN,
            REPO,
        )

        st.success("Despesa registrada com sucesso.")
        st.rerun()


def render_minhas_despesas():
    st.subheader("Minhas Despesas")

    usuario = st.session_state.get("usuario", "")

    df = carregar_despesas()

    if df.empty:
        st.info("Nenhuma despesa registrada.")
        return

    df = df[df["Criado_Por"].astype(str) == str(usuario)]

    if df.empty:
        st.info("Você ainda não possui despesas registradas.")
        return

    df = df.sort_values(by="Data_Registro", ascending=False)

    total = pd.to_numeric(
        df["Valor"],
        errors="coerce",
    ).fillna(0).sum()

    st.metric(
        "Total lançado",
        formatar_moeda(total),
    )

    df_exibir = preparar_exibicao(df)

    st.dataframe(
        df_exibir,
        use_container_width=True,
    )

    st.markdown("### Ver comprovante")

    opcoes = []

    for idx, linha in df.iterrows():
        opcoes.append(
            f"{idx} - {linha.get('Data_Despesa', '')} | "
            f"{linha.get('Tipo_Despesa', '')} | "
            f"{formatar_moeda(linha.get('Valor', 0))} | "
            f"{linha.get('Status', '')}"
        )

    escolha = st.selectbox(
        "Selecionar despesa",
        opcoes,
        key="minhas_select_comprovante",
    )

    idx_escolhido = int(escolha.split(" - ")[0])
    linha_escolhida = df.loc[idx_escolhido]

    render_comprovante(linha_escolhida.get("Arquivo_Comprovante", ""))


def render_todas_despesas():
    exigir_admin()

    st.subheader("Todas as Despesas")

    df = carregar_despesas()

    if df.empty:
        st.info("Nenhuma despesa registrada.")
        return

    col1, col2, col3 = st.columns(3)

    with col1:
        filtro_status = st.selectbox(
            "Status",
            ["Todos"] + sorted(df["Status"].dropna().astype(str).unique().tolist()),
            key="admin_filtro_status",
        )

    with col2:
        filtro_funcionario = st.selectbox(
            "Funcionário",
            ["Todos"] + sorted(df["Funcionario"].dropna().astype(str).unique().tolist()),
            key="admin_filtro_funcionario",
        )

    with col3:
        filtro_tipo = st.selectbox(
            "Tipo",
            ["Todos"] + sorted(df["Tipo_Despesa"].dropna().astype(str).unique().tolist()),
            key="admin_filtro_tipo",
        )

    df_filtrado = df.copy()

    if filtro_status != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Status"].astype(str) == filtro_status]

    if filtro_funcionario != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Funcionario"].astype(str) == filtro_funcionario]

    if filtro_tipo != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Tipo_Despesa"].astype(str) == filtro_tipo]

    if df_filtrado.empty:
        st.warning("Nenhuma despesa encontrada com os filtros selecionados.")
        return

    total = pd.to_numeric(
        df_filtrado["Valor"],
        errors="coerce",
    ).fillna(0).sum()

    pendentes = len(df_filtrado[df_filtrado["Status"].astype(str) == "Pendente"])
    aprovadas = len(df_filtrado[df_filtrado["Status"].astype(str) == "Aprovado"])
    reprovadas = len(df_filtrado[df_filtrado["Status"].astype(str) == "Reprovado"])

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total filtrado", formatar_moeda(total))
    m2.metric("Pendentes", pendentes)
    m3.metric("Aprovadas", aprovadas)
    m4.metric("Reprovadas", reprovadas)

    df_filtrado = df_filtrado.sort_values(by="Data_Registro", ascending=False)

    df_exibir = preparar_exibicao(df_filtrado)

    st.dataframe(
        df_exibir,
        use_container_width=True,
    )

    st.divider()
    st.markdown("### Analisar despesa")

    opcoes = []

    for idx, linha in df_filtrado.iterrows():
        opcoes.append(
            f"{idx} - {linha.get('Funcionario', '')} | "
            f"{linha.get('Data_Despesa', '')} | "
            f"{linha.get('Tipo_Despesa', '')} | "
            f"{formatar_moeda(linha.get('Valor', 0))} | "
            f"{linha.get('Status', '')}"
        )

    escolha = st.selectbox(
        "Selecionar despesa para análise",
        opcoes,
        key="admin_select_despesa",
    )

    idx_escolhido = int(escolha.split(" - ")[0])
    linha = df.loc[idx_escolhido]

    st.markdown("#### Detalhes")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.write(f"**Funcionário:** {linha.get('Funcionario', '')}")
        st.write(f"**Matrícula:** {linha.get('Matricula', '')}")

    with c2:
        st.write(f"**Tipo:** {linha.get('Tipo_Despesa', '')}")
        st.write(f"**Valor:** {formatar_moeda(linha.get('Valor', 0))}")

    with c3:
        st.write(f"**Status:** {linha.get('Status', '')}")
        st.write(f"**Data:** {formatar_data_br(linha.get('Data_Despesa', ''))}")

    st.write(f"**Descrição:** {linha.get('Descricao', '')}")

    st.markdown("#### Comprovante")
    render_comprovante(linha.get("Arquivo_Comprovante", ""))

    st.divider()

    st.markdown("#### Aprovação")

    observacao_aprovacao = st.text_area(
        "Observações da análise",
        value=str(linha.get("Observacoes_Aprovacao", "")),
        key=f"obs_aprovacao_{idx_escolhido}",
    )

    col_aprovar, col_reprovar, col_pago = st.columns(3)

    if col_aprovar.button(
        "Aprovar",
        use_container_width=True,
        key=f"btn_aprovar_{idx_escolhido}",
    ):
        df.loc[idx_escolhido, "Status"] = "Aprovado"
        df.loc[idx_escolhido, "Aprovado_Por"] = str(st.session_state.get("usuario", ""))
        df.loc[idx_escolhido, "Data_Aprovacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df.loc[idx_escolhido, "Observacoes_Aprovacao"] = str(observacao_aprovacao)

        df = normalizar_dataframe(df, COLUNAS_DESPESAS)
        salvar_github(df, ARQ_DESPESAS, TOKEN, REPO)

        st.success("Despesa aprovada.")
        st.rerun()

    if col_reprovar.button(
        "Reprovar",
        use_container_width=True,
        key=f"btn_reprovar_{idx_escolhido}",
    ):
        df.loc[idx_escolhido, "Status"] = "Reprovado"
        df.loc[idx_escolhido, "Aprovado_Por"] = str(st.session_state.get("usuario", ""))
        df.loc[idx_escolhido, "Data_Aprovacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df.loc[idx_escolhido, "Observacoes_Aprovacao"] = str(observacao_aprovacao)

        df = normalizar_dataframe(df, COLUNAS_DESPESAS)
        salvar_github(df, ARQ_DESPESAS, TOKEN, REPO)

        st.warning("Despesa reprovada.")
        st.rerun()

    if col_pago.button(
        "Marcar como Pago",
        use_container_width=True,
        key=f"btn_pago_{idx_escolhido}",
    ):
        df.loc[idx_escolhido, "Status"] = "Pago"
        df.loc[idx_escolhido, "Aprovado_Por"] = str(st.session_state.get("usuario", ""))
        df.loc[idx_escolhido, "Data_Aprovacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df.loc[idx_escolhido, "Observacoes_Aprovacao"] = str(observacao_aprovacao)

        df = normalizar_dataframe(df, COLUNAS_DESPESAS)
        salvar_github(df, ARQ_DESPESAS, TOKEN, REPO)

        st.success("Despesa marcada como paga.")
        st.rerun()


def render_tipos_despesa():
    exigir_admin()

    st.subheader("Tipos de Despesa")

    df_tipos = carregar_tipos()

    st.markdown("### Tipos cadastrados")

    if df_tipos.empty:
        st.warning("Nenhum tipo cadastrado.")
    else:
        st.dataframe(
            df_tipos,
            use_container_width=True,
        )

    st.divider()

    st.markdown("### Novo tipo")

    novo_tipo = st.text_input(
        "Tipo de despesa",
        key="novo_tipo_despesa",
    )

    descricao = st.text_input(
        "Descrição",
        key="descricao_tipo_despesa",
    )

    if st.button("Adicionar tipo", use_container_width=True, key="btn_add_tipo_despesa"):
        if not novo_tipo.strip():
            st.error("Informe o tipo.")
            return

        existe = (
            df_tipos["Tipo_Despesa"]
            .astype(str)
            .str.lower()
            .eq(novo_tipo.strip().lower())
            .any()
        )

        if existe:
            st.error("Este tipo já existe.")
            return

        novo = {
            "Tipo_Despesa": str(novo_tipo),
            "Descricao": str(descricao),
            "Ativo": "Sim",
            "Criado_Por": str(st.session_state.get("usuario", "")),
            "Data_Registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        df_tipos = pd.concat(
            [df_tipos, pd.DataFrame([novo])],
            ignore_index=True,
        )

        df_tipos = normalizar_dataframe(
            df_tipos,
            COLUNAS_TIPOS,
        )

        salvar_github(
            df_tipos,
            ARQ_TIPOS,
            TOKEN,
            REPO,
        )

        st.success("Tipo adicionado com sucesso.")
        st.rerun()


def render():
    st.title("Prestação de Contas")

    perfil = st.session_state.get("perfil", "")

    if perfil == "funcionario":
        aba_nova, aba_minhas = st.tabs(
            ["Nova Despesa", "Minhas Despesas"]
        )

        with aba_nova:
            render_nova_despesa()

        with aba_minhas:
            render_minhas_despesas()

    elif perfil == "admin":
        aba_todas, aba_nova, aba_minhas, aba_tipos = st.tabs(
            ["Todas as Despesas", "Nova Despesa", "Minhas Despesas", "Tipos de Despesa"]
        )

        with aba_todas:
            render_todas_despesas()

        with aba_nova:
            render_nova_despesa()

        with aba_minhas:
            render_minhas_despesas()

        with aba_tipos:
            render_tipos_despesa()

    else:
        aba_nova, aba_minhas = st.tabs(
            ["Nova Despesa", "Minhas Despesas"]
        )

        with aba_nova:
            render_nova_despesa()

        with aba_minhas:
            render_minhas_despesas()

    st.divider()

    if perfil == "funcionario":
        if st.button("Sair", use_container_width=True, key="btn_sair_funcionario_prestacao"):
            from services.auth import logout
            logout()
    else:
        if st.button("⬅ Voltar", use_container_width=True, key="btn_voltar_prestacao"):
            st.session_state.tela = "menu"
            st.rerun()

