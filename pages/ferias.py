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

        matricula_novo = st.text_input("Matrícula", key="novo_matricula")
        funcionario_novo = st.text_input("Funcionário", key="novo_funcionario")
        unidade_novo = st.text_input(
            "Unidade / Local",
            placeholder="Ex: OFICINA - CUBATÃO/SP",
            key="novo_unidade",
        )
        departamento_novo = st.text_input(
            "Departamento",
            value="Operacional",
            key="novo_departamento",
        )

        col_aq1, col_aq2 = st.columns(2)

        with col_aq1:
            periodo_inicio_novo = st.date_input(
                "Início do período aquisitivo",
                value=date.today(),
                key="novo_periodo_inicio",
            )

        with col_aq2:
            periodo_fim_novo = st.date_input(
                "Fim do período aquisitivo",
                value=date.today() + timedelta(days=365),
                key="novo_periodo_fim",
            )

        limite_gozo_novo = st.date_input(
            "Limite de gozo",
            value=periodo_fim_novo + timedelta(days=335),
            key="novo_limite_gozo",
        )

        periodo_gozo_novo = st.text_input(
            "Período de gozo de férias",
            placeholder="Ex: 18/05 a 16/06/2026 ou Previsão 13/07 a 11/08",
            key="novo_periodo_gozo",
        )

        observacoes_novo = st.text_area("Observações", key="novo_observacoes")

        if st.button("Adicionar registro", use_container_width=True, key="btn_adicionar_ferias"):
            if not funcionario_novo.strip():
                st.error("Informe o nome do funcionário.")
            else:
                situacao_ferias, situacao_prazo = calcular_status(
                    periodo_fim_novo,
                    limite_gozo_novo,
                )

                novo = {
                    "Matricula": matricula_novo,
                    "Funcionario": funcionario_novo,
                    "Unidade": unidade_novo,
                    "Departamento": departamento_novo,
                    "Periodo_Aquisitivo_Inicio": periodo_inicio_novo,
                    "Periodo_Aquisitivo_Fim": periodo_fim_novo,
                    "Situacao_Ferias": situacao_ferias,
                    "Limite_Gozo": limite_gozo_novo,
                    "Periodo_Gozo": periodo_gozo_novo,
                    "Situacao_Prazo": situacao_prazo,
                    "Observacoes": observacoes_novo,
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
            escolha = st.selectbox(
                "Selecionar funcionário",
                opcoes,
                key="edit_selecionar_funcionario",
            )

            idx = int(escolha.split(" - ")[0])
            linha = df.loc[idx]

            matricula_edit = st.text_input(
                "Matrícula",
                value=str(linha["Matricula"]),
                key=f"edit_matricula_{idx}",
            )

            funcionario_edit = st.text_input(
                "Funcionário",
                value=str(linha["Funcionario"]),
                key=f"edit_funcionario_{idx}",
            )

            unidade_edit = st.text_input(
                "Unidade / Local",
                value=str(linha["Unidade"]),
                key=f"edit_unidade_{idx}",
            )

            departamento_edit = st.text_input(
                "Departamento",
                value=str(linha["Departamento"]),
                key=f"edit_departamento_{idx}",
            )

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
                periodo_inicio_edit = st.date_input(
                    "Início do período aquisitivo",
                    value=data_inicio.date(),
                    key=f"edit_inicio_{idx}",
                )

            with col_ed2:
                periodo_fim_edit = st.date_input(
                    "Fim do período aquisitivo",
                    value=data_fim.date(),
                    key=f"edit_fim_{idx}",
                )

            limite_gozo_edit = st.date_input(
                "Limite de gozo",
                value=data_limite.date(),
                key=f"edit_limite_{idx}",
            )

            periodo_gozo_edit = st.text_input(
                "Período de gozo de férias",
                value=str(linha["Periodo_Gozo"]),
                key=f"edit_periodo_gozo_{idx}",
            )

            observacoes_edit = st.text_area(
                "Observações",
                value=str(linha["Observacoes"]),
                key=f"edit_observacoes_{idx}",
            )

            col_salvar, col_excluir = st.columns(2)

            if col_salvar.button(
                "Salvar alterações",
                use_container_width=True,
                key=f"btn_salvar_ferias_{idx}",
            ):
                if not funcionario_edit.strip():
                    st.error("Informe o nome do funcionário.")
                else:
                    situacao_ferias, situacao_prazo = calcular_status(
                        periodo_fim_edit,
                        limite_gozo_edit,
                    )

                    df.loc[idx, "Matricula"] = matricula_edit
                    df.loc[idx, "Funcionario"] = funcionario_edit
                    df.loc[idx, "Unidade"] = unidade_edit
                    df.loc[idx, "Departamento"] = departamento_edit
                    df.loc[idx, "Periodo_Aquisitivo_Inicio"] = periodo_inicio_edit
                    df.loc[idx, "Periodo_Aquisitivo_Fim"] = periodo_fim_edit
                    df.loc[idx, "Situacao_Ferias"] = situacao_ferias
                    df.loc[idx, "Limite_Gozo"] = limite_gozo_edit
                    df.loc[idx, "Periodo_Gozo"] = periodo_gozo_edit
                    df.loc[idx, "Situacao_Prazo"] = situacao_prazo
                    df.loc[idx, "Observacoes"] = observacoes_edit

                    salvar_github(df, ARQ_FERIAS, TOKEN, REPO)

                    st.success("Registro atualizado com sucesso!")
                    st.rerun()

            if col_excluir.button(
                "Excluir registro",
                use_container_width=True,
                key=f"btn_excluir_ferias_{idx}",
            ):
                df = df.drop(idx).reset_index(drop=True)
                salvar_github(df, ARQ_FERIAS, TOKEN, REPO)

                st.warning("Registro excluído.")
                st.rerun()

    st.divider()

    if st.button("⬅ Voltar", use_container_width=True, key="btn_voltar_ferias"):
        st.session_state.tela = "menu"
        st.rerun()
