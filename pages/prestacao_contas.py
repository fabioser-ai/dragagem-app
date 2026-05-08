import os
import uuid
from datetime import date, datetime

import pandas as pd
import streamlit as st

from services.auth import exigir_admin
from services.github import carregar_github, salvar_github


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
        return pd.to_datetime(valor).strftime("%d/%m/%Y")
    except Exception:
        return ""


def formatar_datetime_br(valor):
    try:
        return pd.to_datetime(valor).strftime("%d/%m/%Y %H:%M:%S")
    except Exception:
        return ""


def preparar_exibicao(df):
    df_exibir = df.copy()

    if "Data_Despesa" in df_exibir.columns:
        df_exibir["Data_Despesa"] = df_exibir["Data_Despesa"].apply(formatar_data_br)

    if "Data_Registro" in df_exibir.columns:
        df_exibir["Data_Registro"] = df_exibir["Data_Registro"].apply(formatar_datetime_br)

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
            REPO
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


def salvar_comprovante(upload):
    if upload is None:
        return ""

    extensao = upload.name.split(".")[-1].lower()

    nome_arquivo = (
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_"
        f"{uuid.uuid4().hex[:8]}.{extensao}"
    )

    caminho = f"{PASTA_COMPROVANTES}/{nome_arquivo}"

    return caminho


def render_nova_despesa():
    st.subheader("Nova Despesa")

    dados_func = obter_dados_funcionario()

    col1, col2 = st.columns(2)

    with col1:
        st.text_input(
            "Funcionário",
            value=str(dados_func["Funcionario"]),
            disabled=True,
        )

    with col2:
        st.text_input(
            "Matrícula",
            value=str(dados_func["Matricula"]),
            disabled=True,
        )

    col3, col4 = st.columns(2)

    with col3:
        st.text_input(
            "Unidade",
            value=str(dados_func["Unidade"]),
            disabled=True,
        )

    with col4:
        st.text_input(
            "Departamento",
            value=str(dados_func["Departamento"]),
            disabled=True,
        )

    df_tipos = carregar_tipos()

    tipos_ativos = (
        df_tipos[df_tipos["Ativo"] == "Sim"]["Tipo_Despesa"]
        .dropna()
        .astype(str)
        .tolist()
    )

    tipos_ativos = sorted(tipos_ativos)

    data_despesa = st.date_input(
        "Data da despesa",
        value=date.today(),
        format="DD/MM/YYYY",
    )

    tipo_despesa = st.selectbox(
        "Tipo de despesa",
        tipos_ativos,
    )

    valor = st.number_input(
        "Valor da despesa (R$)",
        min_value=0.0,
        step=10.0,
        format="%.2f",
    )

    descricao = st.text_area(
        "Descrição / Observações"
    )

    comprovante = st.file_uploader(
        "Anexar comprovante",
        type=["png", "jpg", "jpeg", "pdf"],
    )

    if comprovante:
        st.success(f"Arquivo selecionado: {comprovante.name}")

    if st.button("Enviar prestação de contas", use_container_width=True):
        if valor <= 0:
            st.error("Informe um valor válido.")
            return

        caminho_comprovante = salvar_comprovante(comprovante)

        nova_despesa = {
            "ID": str(uuid.uuid4()),
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
        errors="coerce"
    ).fillna(0).sum()

    st.metric(
        "Total lançado",
        f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

    df_exibir = preparar_exibicao(df)

    st.dataframe(
        df_exibir,
        use_container_width=True,
    )


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

    if st.button("Adicionar tipo", use_container_width=True):
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

    else:
        aba_nova, aba_minhas, aba_tipos = st.tabs(
            ["Nova Despesa", "Minhas Despesas", "Tipos de Despesa"]
        )

        with aba_nova:
            render_nova_despesa()

        with aba_minhas:
            render_minhas_despesas()

        with aba_tipos:
            render_tipos_despesa()

    st.divider()

    if st.button("⬅ Voltar", use_container_width=True):
        st.session_state.tela = "menu"
        st.rerun()
