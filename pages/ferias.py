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
    "Data_Inicio_Gozo",
    "Data_Fim_Gozo",
    "Dias_Gozo",
    "Limite_Gozo",
    "Periodo_Gozo",
    "Situacao_Ferias",
    "Situacao_Prazo",
    "Observacoes",
]


def data_valida(valor, padrao=None):
    try:
        data = pd.to_datetime(valor, errors="coerce")
        if pd.isna(data):
            return padrao
        return data.date()
    except Exception:
        return padrao


def calcular_dias_gozo(data_inicio, data_fim):
    if not data_inicio or not data_fim:
        return ""

    try:
        dias = (data_fim - data_inicio).days + 1
        return dias if dias > 0 else ""
    except Exception:
        return ""


def montar_periodo_gozo(data_inicio, data_fim, texto_manual=""):
    if texto_manual and str(texto_manual).strip():
        return str(texto_manual).strip()

    if data_inicio and data_fim:
        return f"{data_inicio.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')}"

    return ""


def calcular_status(periodo_fim, limite_gozo):
    hoje = date.today()

    periodo_fim = data_valida(periodo_fim)
    limite_gozo = data_valida(limite_gozo)

    if not periodo_fim:
        return "Indefinido", "Indefinido"

    if not limite_gozo:
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

    df = df[COLUNAS].copy()

    for col in [
        "Periodo_Aquisitivo_Inicio",
        "Periodo_Aquisitivo_Fim",
        "Data_Inicio_Gozo",
        "Data_Fim_Gozo",
        "Limite_Gozo",
    ]:
        df[col] = pd.to_datetime(df[col], errors="coerce").dt.date.astype("string").fillna("")

    df["Dias_Gozo"] = pd.to_numeric(df["Dias_Gozo"], errors="coerce").fillna("").astype(str)
    df["Dias_Gozo"] = df["Dias_Gozo"].str.replace(".0", "", regex=False)

    return df


def aplicar_estilo_status(row):
    prazo = row.get("Situacao_Prazo", "")
    ferias = row.get("Situacao_Ferias", "")

    if prazo == "Férias em Dobro":
        return ["background-color: #fee2e2; color: #991b1b; font-weight: 600"] * len(row)

    if prazo == "Atenção":
        return ["background-color: #fef3c7; color: #92400e; font-weight: 600"] * len(row)

    if ferias == "Férias Vencidas":
        return ["background-color: #fff7ed; color: #9a3412"] * len(row)

    return [""] * len(row)


def salvar_df(df):
    df_salvar = df.copy()
    salvar_github(df_salvar, ARQ_FERIAS, TOKEN, REPO)


def render():
    st.title("Controle de Férias")

    df = carregar_github(ARQ_FERIAS, TOKEN, REPO)
    df = normalizar_dataframe(df)

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
        col_filtro1, col_filtro2, col_filtro3 = st.columns(3)

        with col_filtro1:
            filtro_unidade = st.selectbox(
                "Filtrar unidade",
                ["Todas"] + sorted(df["Unidade"].dropna().astype(str).unique().tolist()),
                key="ferias_filtro_unidade",
            )

        with col_filtro2:
            filtro_prazo = st.selectbox(
                "Filtrar prazo",
                ["Todos"] + sorted(df["Situacao_Prazo"].dropna().astype(str).unique().tolist()),
                key="ferias_filtro_prazo",
            )

        with col_filtro3:
            busca = st.text_input("Buscar funcionário", key="ferias_busca")

        df_visual = df.copy()

        if filtro_unidade != "Todas":
            df_visual = df_visual[df_visual["Unidade"] == filtro_unidade]

        if filtro_prazo != "Todos":
            df_visual = df_visual[df_visual["Situacao_Prazo"] == filtro_prazo]

        if busca.strip():
            df_visual = df_visual[
                df_visual["Funcionario"].astype(str).str.contains(busca.strip(), case=False, na=False)
            ]

        st.dataframe(
            df_visual.style.apply(aplicar_estilo_status, axis=1),
            use_container_width=True,
            hide_index=True,
        )

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

        informar_gozo_novo = st.checkbox(
            "Informar período de gozo agora",
            value=False,
            key="novo_informar_gozo",
        )

        data_inicio_gozo_novo = ""
        data_fim_gozo_novo = ""
        dias_gozo_novo = ""

        if informar_gozo_novo:
            col_gozo1, col_gozo2, col_gozo3 = st.columns(3)

            with col_gozo1:
                data_inicio_gozo_novo = st.date_input(
                    "Início do gozo",
                    value=date.today(),
                    key="novo_data_inicio_gozo",
                )

            with col_gozo2:
                data_fim_gozo_novo = st.date_input(
                    "Fim do gozo",
                    value=date.today() + timedelta(days=29),
                    key="novo_data_fim_gozo",
                )

            dias_gozo_novo = calcular_dias_gozo(data_inicio_gozo_novo, data_fim_gozo_novo)

            with col_gozo3:
                st.metric("Dias de gozo", dias_gozo_novo if dias_gozo_novo else "-")

        periodo_gozo_manual_novo = st.text_input(
            "Descrição do período de gozo",
            placeholder="Ex: Previsão 13/07 a 11/08",
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

                periodo_gozo_novo = montar_periodo_gozo(
                    data_inicio_gozo_novo,
                    data_fim_gozo_novo,
                    periodo_gozo_manual_novo,
                )

                novo = {
                    "Matricula": matricula_novo,
                    "Funcionario": funcionario_novo,
                    "Unidade": unidade_novo,
                    "Departamento": departamento_novo,
                    "Periodo_Aquisitivo_Inicio": periodo_inicio_novo,
                    "Periodo_Aquisitivo_Fim": periodo_fim_novo,
                    "Data_Inicio_Gozo": data_inicio_gozo_novo,
                    "Data_Fim_Gozo": data_fim_gozo_novo,
                    "Dias_Gozo": dias_gozo_novo,
                    "Limite_Gozo": limite_gozo_novo,
                    "Periodo_Gozo": periodo_gozo_novo,
                    "Situacao_Ferias": situacao_ferias,
                    "Situacao_Prazo": situacao_prazo,
                    "Observacoes": observacoes_novo,
                }

                df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
                salvar_df(df)

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

            data_inicio = data_valida(linha["Periodo_Aquisitivo_Inicio"], date.today())
            data_fim = data_valida(linha["Periodo_Aquisitivo_Fim"], date.today() + timedelta(days=365))
            data_limite = data_valida(linha["Limite_Gozo"], data_fim + timedelta(days=335))

            col_ed1, col_ed2 = st.columns(2)

            with col_ed1:
                periodo_inicio_edit = st.date_input(
                    "Início do período aquisitivo",
                    value=data_inicio,
                    key=f"edit_inicio_{idx}",
                )

            with col_ed2:
                periodo_fim_edit = st.date_input(
                    "Fim do período aquisitivo",
                    value=data_fim,
                    key=f"edit_fim_{idx}",
                )

            limite_gozo_edit = st.date_input(
                "Limite de gozo",
                value=data_limite,
                key=f"edit_limite_{idx}",
            )

            data_inicio_gozo_atual = data_valida(linha["Data_Inicio_Gozo"])
            data_fim_gozo_atual = data_valida(linha["Data_Fim_Gozo"])

            informar_gozo_edit = st.checkbox(
                "Informar período de gozo",
                value=bool(data_inicio_gozo_atual and data_fim_gozo_atual),
                key=f"edit_informar_gozo_{idx}",
            )

            data_inicio_gozo_edit = ""
            data_fim_gozo_edit = ""
            dias_gozo_edit = ""

            if informar_gozo_edit:
                col_gozo_ed1, col_gozo_ed2, col_gozo_ed3 = st.columns(3)

                with col_gozo_ed1:
                    data_inicio_gozo_edit = st.date_input(
                        "Início do gozo",
                        value=data_inicio_gozo_atual or date.today(),
                        key=f"edit_data_inicio_gozo_{idx}",
                    )

                with col_gozo_ed2:
                    data_fim_gozo_edit = st.date_input(
                        "Fim do gozo",
                        value=data_fim_gozo_atual or date.today() + timedelta(days=29),
                        key=f"edit_data_fim_gozo_{idx}",
                    )

                dias_gozo_edit = calcular_dias_gozo(data_inicio_gozo_edit, data_fim_gozo_edit)

                with col_gozo_ed3:
                    st.metric("Dias de gozo", dias_gozo_edit if dias_gozo_edit else "-")

            periodo_gozo_edit = st.text_input(
                "Descrição do período de gozo",
                value=str(linha["Periodo_Gozo"]) if str(linha["Periodo_Gozo"]) != "nan" else "",
                key=f"edit_periodo_gozo_{idx}",
            )

            observacoes_edit = st.text_area(
                "Observações",
                value=str(linha["Observacoes"]) if str(linha["Observacoes"]) != "nan" else "",
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

                    periodo_gozo_final = montar_periodo_gozo(
                        data_inicio_gozo_edit,
                        data_fim_gozo_edit,
                        periodo_gozo_edit,
                    )

                    df.loc[idx, "Matricula"] = matricula_edit
                    df.loc[idx, "Funcionario"] = funcionario_edit
                    df.loc[idx, "Unidade"] = unidade_edit
                    df.loc[idx, "Departamento"] = departamento_edit
                    df.loc[idx, "Periodo_Aquisitivo_Inicio"] = periodo_inicio_edit
                    df.loc[idx, "Periodo_Aquisitivo_Fim"] = periodo_fim_edit
                    df.loc[idx, "Data_Inicio_Gozo"] = data_inicio_gozo_edit
                    df.loc[idx, "Data_Fim_Gozo"] = data_fim_gozo_edit
                    df.loc[idx, "Dias_Gozo"] = dias_gozo_edit
                    df.loc[idx, "Limite_Gozo"] = limite_gozo_edit
                    df.loc[idx, "Periodo_Gozo"] = periodo_gozo_final
                    df.loc[idx, "Situacao_Ferias"] = situacao_ferias
                    df.loc[idx, "Situacao_Prazo"] = situacao_prazo
                    df.loc[idx, "Observacoes"] = observacoes_edit

                    salvar_df(df)

                    st.success("Registro atualizado com sucesso!")
                    st.rerun()

            if col_excluir.button(
                "Excluir registro",
                use_container_width=True,
                key=f"btn_excluir_ferias_{idx}",
            ):
                df = df.drop(idx).reset_index(drop=True)
                salvar_df(df)

                st.warning("Registro excluído.")
                st.rerun()

    st.divider()

    if st.button("⬅ Voltar", use_container_width=True, key="btn_voltar_ferias"):
        st.session_state.tela = "menu"
        st.rerun()
