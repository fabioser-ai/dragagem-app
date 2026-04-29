import streamlit as st
import pandas as pd
from datetime import date, timedelta
from services.github import carregar_github, salvar_github

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

ARQ_FERIAS = "data/ferias.csv"

COLUNAS = [
    "Matricula",
    "Funcionario",
    "Unidade",
    "Departamento",
    "Periodo_Aquisitivo_Inicio",
    "Periodo_Aquisitivo_Fim",
    "Situacao_Ferias",
    "Limite_Gozo",
    "Periodo_Gozo",
    "Situacao_Prazo",
    "Observacoes",
]


def calcular_status(periodo_fim, limite_gozo):
    hoje = date.today()

    try:
        periodo_fim = pd.to_datetime(periodo_fim).date()
    except Exception:
        return "Indefinido", "Indefinido"

    try:
        limite_gozo = pd.to_datetime(limite_gozo).date()
    except Exception:
        limite_gozo = periodo_fim + timedelta(days=335)

    if hoje >= periodo_fim:
        situacao_ferias = "Férias Vencidas"
    else:
        situacao_ferias = "Férias Não Vencidas"

    if hoje > limite_gozo:
        situacao_prazo = "Férias em Dobro"
    elif (limite_gozo - hoje).days <= 60:
        situacao_prazo = "Atenção"
    else:
        situacao_prazo = "Dentro do Prazo"

    return situacao_ferias, situacao_prazo


def normalizar_dataframe(df):
    if df.empty:
        return pd.DataFrame(columns=COLUNAS)

    for col in COLUNAS:
        if col not in df.columns:
            df[col] = ""

    return df[COLUNAS]


def render():
    st.title("Controle de Férias")

    df = carregar_github(ARQ_FERIAS, TOKEN, REPO)
    df = normalizar_dataframe(df)

    st.subheader("Resumo")

    total = len(df)
    vencidas = len(df[df["Situacao_Ferias"] == "Férias Vencidas"])
    dobro = len(df[df["Situacao_Prazo"] == "Férias em Dobro"])
    atencao = len(df[df["Situacao_Prazo"] == "Atenção"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Funcionários", total)
    col2.metric("Férias vencidas", vencidas)
    col3.metric("Atenção", atencao)
    col4.metric("Férias em dobro", dobro)

    st.divider()

    st.subheader("Lista de Controle")

    if df.empty:
        st.warning("Nenhum registro de férias cadastrado ainda.")
    else:
        st.dataframe(df, use_container_width=True)

    st.divider()

    aba1, aba2 = st.tabs(["Adicionar novo registro", "Editar / Excluir"])

    with aba1:
        st.subheader("Novo registro")

        matricula = st.text_input("Matrícula")
        funcionario = st.text_input("Funcionário")
        unidade = st.text_input("Unidade / Local", placeholder="Ex: OFICINA - CUBATÃO/SP")
        departamento = st.text_input("Departamento", value="Operacional")

        col_aq1, col_aq2 = st.columns(2)
        with col_aq1:
            periodo_inicio = st.date_input("Início do período aquisitivo", value=date.today())
        with col_aq2:
            periodo_fim = st.date_input(
                "Fim do período aquisitivo",
                value=date.today() + timedelta(days=365),
            )

        limite_gozo = st.date_input(
            "Limite de gozo",
            value=periodo_fim + timedelta(days=335),
        )

        periodo_gozo = st.text_input(
            "Período de gozo de férias",
            placeholder="Ex: 18/05 a 16/06/2026 ou Previsão 13/07 a 11/08",
        )

        observacoes = st.text_area("Observações")

        if st.button("Adicionar registro", use_container_width=True):
            situacao_ferias, situacao_prazo = calcular_status(periodo_fim, limite_gozo)

            novo = {
                "Matricula": matricula,
                "Funcionario": funcionario,
                "Unidade": unidade,
                "Departamento": departamento,
                "Periodo_Aquisitivo_Inicio": periodo_inicio,
                "Periodo_Aquisitivo_Fim": periodo_fim,
                "Situacao_Ferias": situacao_ferias,
                "Limite_Gozo": limite_gozo,
                "Periodo_Gozo": periodo_gozo,
                "Situacao_Prazo": situacao_prazo,
                "Observacoes": observacoes,
            }

            df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
            salvar_github(df, ARQ_FERIAS, TOKEN, REPO)

            st.success("Registro adicionado com sucesso!")
            st.rerun()

    with aba2:
        st.subheader("Editar registro existente")

        if df.empty:
            st.info("Nenhum registro disponível para edição.")
        else:
            opcoes = df.index.astype(str) + " - " + df["Funcionario"].astype(str)
            escolha = st.selectbox("Selecionar funcionário", opcoes)

            idx = int(escolha.split(" - ")[0])
            linha = df.loc[idx]

            matricula = st.text_input("Matrícula", value=str(linha["Matricula"]))
            funcionario = st.text_input("Funcionário", value=str(linha["Funcionario"]))
            unidade = st.text_input("Unidade / Local", value=str(linha["Unidade"]))
            departamento = st.text_input("Departamento", value=str(linha["Departamento"]))

            data_inicio = pd.to_datetime(
                linha["Periodo_Aquisitivo_Inicio"],
                errors="coerce",
            )
            data_fim = pd.to_datetime(
                linha["Periodo_Aquisitivo_Fim"],
                errors="coerce",
            )
            data_limite = pd.to_datetime(
                linha["Limite_Gozo"],
                errors="coerce",
            )

            if pd.isna(data_inicio):
                data_inicio = pd.Timestamp(date.today())

            if pd.isna(data_fim):
                data_fim = pd.Timestamp(date.today() + timedelta(days=365))

            if pd.isna(data_limite):
                data_limite = data_fim + pd.Timedelta(days=335)

            col_ed1, col_ed2 = st.columns(2)
            with col_ed1:
                periodo_inicio = st.date_input(
                    "Início do período aquisitivo",
                    value=data_inicio.date(),
                    key="edit_inicio",
                )
            with col_ed2:
                periodo_fim = st.date_input(
                    "Fim do período aquisitivo",
                    value=data_fim.date(),
                    key="edit_fim",
                )

            limite_gozo = st.date_input(
                "Limite de gozo",
                value=data_limite.date(),
                key="edit_limite",
            )

            periodo_gozo = st.text_input(
                "Período de gozo de férias",
                value=str(linha["Periodo_Gozo"]),
            )

            observacoes = st.text_area(
                "Observações",
                value=str(linha["Observacoes"]),
            )

            col_salvar, col_excluir = st.columns(2)

            if col_salvar.button("Salvar alterações", use_container_width=True):
                situacao_ferias, situacao_prazo = calcular_status(periodo_fim, limite_gozo)

                df.loc[idx, "Matricula"] = matricula
                df.loc[idx, "Funcionario"] = funcionario
                df.loc[idx, "Unidade"] = unidade
                df.loc[idx, "Departamento"] = departamento
                df.loc[idx, "Periodo_Aquisitivo_Inicio"] = periodo_inicio
                df.loc[idx, "Periodo_Aquisitivo_Fim"] = periodo_fim
                df.loc[idx, "Situacao_Ferias"] = situacao_ferias
                df.loc[idx, "Limite_Gozo"] = limite_gozo
                df.loc[idx, "Periodo_Gozo"] = periodo_gozo
                df.loc[idx, "Situacao_Prazo"] = situacao_prazo
                df.loc[idx, "Observacoes"] = observacoes

                salvar_github(df, ARQ_FERIAS, TOKEN, REPO)

                st.success("Registro atualizado com sucesso!")
                st.rerun()

            if col_excluir.button("Excluir registro", use_container_width=True):
                df = df.drop(idx).reset_index(drop=True)
                salvar_github(df, ARQ_FERIAS, TOKEN, REPO)

                st.warning("Registro excluído.")
                st.rerun()

    st.divider()

    if st.button("⬅ Voltar", use_container_width=True):
        st.session_state.tela = "menu"
        st.rerun()
