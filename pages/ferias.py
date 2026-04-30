import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
from services.github import carregar_github, salvar_github


TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

ARQ_FERIAS = "data/ferias.csv"
ARQ_FOLGAS = "data/folgas.csv"

DIAS_INTERVALO_FOLGA = 60

COLUNAS_FERIAS = [
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
]

COLUNAS_FOLGAS = [
    "Matricula",
    "Funcionario",
    "Unidade",
    "Departamento",
    "Data_Saida",
    "Data_Retorno",
    "Dias_Folga",
    "Observacoes",
    "Criado_Por",
    "Data_Registro",
]


def normalizar_dataframe(df, colunas):
    if df.empty:
        return pd.DataFrame(columns=colunas)

    for col in colunas:
        if col not in df.columns:
            df[col] = ""

    return df[colunas]


def para_data(valor):
    data = pd.to_datetime(valor, errors="coerce")
    if pd.isna(data):
        return None
    return data.date()


def formatar_data_br(valor):
    data = para_data(valor)
    if data is None:
        return ""
    return data.strftime("%d/%m/%Y")


def formatar_datetime_br(valor):
    data = pd.to_datetime(valor, errors="coerce")
    if pd.isna(data):
        return ""
    return data.strftime("%d/%m/%Y %H:%M:%S")


def calcular_status(periodo_fim, limite_gozo):
    hoje = date.today()

    periodo_fim = para_data(periodo_fim)
    limite_gozo = para_data(limite_gozo)

    if periodo_fim is None:
        return "Indefinido", "Indefinido"

    if limite_gozo is None:
        limite_gozo = periodo_fim + timedelta(days=335)

    situacao_ferias = "Férias Vencidas" if hoje >= periodo_fim else "Férias Não Vencidas"

    if hoje > limite_gozo:
        situacao_prazo = "Férias em Dobro"
    elif (limite_gozo - hoje).days <= 60:
        situacao_prazo = "Atenção"
    else:
        situacao_prazo = "Dentro do Prazo"

    return situacao_ferias, situacao_prazo


def calcular_dias(data_inicio, data_fim):
    if data_inicio is None or data_fim is None:
        return ""

    try:
        return (pd.to_datetime(data_fim).date() - pd.to_datetime(data_inicio).date()).days + 1
    except Exception:
        return ""


def preparar_exibicao_ferias(df):
    df_exibir = df.copy()

    for col in [
        "Periodo_Aquisitivo_Inicio",
        "Periodo_Aquisitivo_Fim",
        "Data_Inicio_Gozo",
        "Data_Fim_Gozo",
        "Limite_Gozo",
    ]:
        if col in df_exibir.columns:
            df_exibir[col] = df_exibir[col].apply(formatar_data_br)

    return df_exibir


def preparar_exibicao_folgas(df):
    df_exibir = df.copy()

    for col in ["Data_Saida", "Data_Retorno"]:
        if col in df_exibir.columns:
            df_exibir[col] = df_exibir[col].apply(formatar_data_br)

    if "Data_Registro" in df_exibir.columns:
        df_exibir["Data_Registro"] = df_exibir["Data_Registro"].apply(formatar_datetime_br)

    return df_exibir


def cor_linha_ferias(row):
    if row.get("Situacao_Prazo") == "Férias em Dobro":
        return ["background-color: #fee2e2"] * len(row)

    if row.get("Situacao_Prazo") == "Atenção":
        return ["background-color: #fef3c7"] * len(row)

    if row.get("Situacao_Ferias") == "Férias Vencidas":
        return ["background-color: #fff7ed"] * len(row)

    return ["background-color: #ecfdf5"] * len(row)


def cor_linha_folgas(row):
    retorno = para_data(row.get("Data_Retorno"))

    if retorno and retorno >= date.today():
        return ["background-color: #dbeafe"] * len(row)

    return [""] * len(row)


def mostrar_alertas_ferias(df):
    if df.empty:
        return

    df_alerta = df.copy()
    df_alerta["Limite_Gozo_Data"] = df_alerta["Limite_Gozo"].apply(para_data)

    ferias_dobro = df_alerta[df_alerta["Situacao_Prazo"] == "Férias em Dobro"]

    hoje = date.today()

    proximos_60 = df_alerta[
        df_alerta["Limite_Gozo_Data"].apply(
            lambda x: x is not None and 0 <= (x - hoje).days <= 60
        )
    ].copy()

    if not ferias_dobro.empty:
        st.error(f"🚨 {len(ferias_dobro)} funcionário(s) com férias em dobro:")

        for nome in ferias_dobro["Funcionario"].dropna().astype(str):
            st.markdown(f"- 🔴 **{nome}**")

    if not proximos_60.empty:
        proximos_60["Dias_Para_Limite"] = proximos_60["Limite_Gozo_Data"].apply(
            lambda x: (x - hoje).days if x else None
        )

        proximos_60 = proximos_60.sort_values(by="Dias_Para_Limite")

        st.warning("⚠️ Funcionários próximos do limite de férias:")

        for _, linha in proximos_60.iterrows():
            nome = linha.get("Funcionario", "")
            limite = linha.get("Limite_Gozo_Data")
            dias = linha.get("Dias_Para_Limite")

            if limite:
                st.markdown(
                    f"- 🟡 **{nome}** → precisa sair de férias até "
                    f"**{limite.strftime('%d/%m/%Y')}** "
                    f"(**{dias} dias restantes**)"
                )

    if ferias_dobro.empty and proximos_60.empty:
        st.success("✅ Nenhum funcionário em situação crítica de férias no momento.")


def mostrar_alertas_folgas(df_folgas):
    if df_folgas.empty:
        st.info("Nenhuma folga registrada ainda.")
        return

    hoje = date.today()
    df_tmp = df_folgas.copy()
    df_tmp["Data_Retorno_Data"] = df_tmp["Data_Retorno"].apply(para_data)

    folgas_ativas = df_tmp[
        df_tmp["Data_Retorno_Data"].apply(lambda x: x is not None and x >= hoje)
    ]

    if not folgas_ativas.empty:
        st.info(f"ℹ️ {len(folgas_ativas)} funcionário(s) com folga ativa ou retorno futuro.")


def render_ferias(df_ferias):
    st.subheader("Resumo de Férias")

    mostrar_alertas_ferias(df_ferias)

    total = len(df_ferias)
    vencidas = len(df_ferias[df_ferias["Situacao_Ferias"] == "Férias Vencidas"])
    dobro = len(df_ferias[df_ferias["Situacao_Prazo"] == "Férias em Dobro"])
    atencao = len(df_ferias[df_ferias["Situacao_Prazo"] == "Atenção"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Funcionários",
        total,
        help="Total de funcionários cadastrados no controle de férias.",
    )

    col2.metric(
        "Férias vencidas",
        vencidas,
        help="Funcionários que já possuem direito a férias porque o período aquisitivo foi concluído.",
    )

    col3.metric(
        "Atenção",
        atencao,
        help="Funcionários próximos do limite legal de gozo das férias. Hoje o sistema considera Atenção quando faltam 60 dias ou menos para o limite.",
    )

    col4.metric(
        "Férias em dobro",
        dobro,
        help="Funcionários que ultrapassaram o prazo legal de gozo. Essa situação pode gerar pagamento em dobro das férias.",
    )

    st.divider()

    st.subheader("Lista de Controle de Férias")

    if df_ferias.empty:
        st.warning("Nenhum registro de férias cadastrado.")
    else:
        df_exibir = preparar_exibicao_ferias(df_ferias)
        st.dataframe(
            df_exibir.style.apply(cor_linha_ferias, axis=1),
            use_container_width=True,
        )

    st.divider()

    aba_add, aba_edit = st.tabs(["Adicionar novo registro", "Editar / Excluir"])

    with aba_add:
        st.subheader("Novo registro")

        matricula = st.text_input("Matrícula", key="ferias_novo_matricula")
        funcionario = st.text_input("Funcionário", key="ferias_novo_funcionario")
        unidade = st.text_input("Unidade / Local", key="ferias_novo_unidade")
        departamento = st.text_input("Departamento", value="Operacional", key="ferias_novo_departamento")

        col1, col2 = st.columns(2)
        with col1:
            periodo_inicio = st.date_input(
                "Início do período aquisitivo",
                value=date.today(),
                format="DD/MM/YYYY",
                key="ferias_novo_inicio",
            )
        with col2:
            periodo_fim = st.date_input(
                "Fim do período aquisitivo",
                value=date.today() + timedelta(days=365),
                format="DD/MM/YYYY",
                key="ferias_novo_fim",
            )

        col3, col4 = st.columns(2)
        with col3:
            data_inicio_gozo = st.date_input(
                "Início do gozo",
                value=None,
                format="DD/MM/YYYY",
                key="ferias_novo_inicio_gozo",
            )
        with col4:
            data_fim_gozo = st.date_input(
                "Fim do gozo",
                value=None,
                format="DD/MM/YYYY",
                key="ferias_novo_fim_gozo",
            )

        dias_gozo = calcular_dias(data_inicio_gozo, data_fim_gozo)

        limite_gozo = st.date_input(
            "Limite de gozo",
            value=periodo_fim + timedelta(days=335),
            format="DD/MM/YYYY",
            key="ferias_novo_limite",
        )

        periodo_gozo = st.text_input("Período de gozo", key="ferias_novo_periodo_gozo")

        if st.button("Adicionar férias", use_container_width=True, key="btn_add_ferias"):
            if not funcionario.strip():
                st.error("Informe o nome do funcionário.")
            else:
                situacao_ferias, situacao_prazo = calcular_status(periodo_fim, limite_gozo)

                novo = {
                    "Matricula": matricula,
                    "Funcionario": funcionario,
                    "Unidade": unidade,
                    "Departamento": departamento,
                    "Periodo_Aquisitivo_Inicio": periodo_inicio,
                    "Periodo_Aquisitivo_Fim": periodo_fim,
                    "Data_Inicio_Gozo": data_inicio_gozo or "",
                    "Data_Fim_Gozo": data_fim_gozo or "",
                    "Dias_Gozo": dias_gozo,
                    "Limite_Gozo": limite_gozo,
                    "Periodo_Gozo": periodo_gozo,
                    "Situacao_Ferias": situacao_ferias,
                    "Situacao_Prazo": situacao_prazo,
                }

                df_ferias = pd.concat([df_ferias, pd.DataFrame([novo])], ignore_index=True)
                salvar_github(df_ferias, ARQ_FERIAS, TOKEN, REPO)
                st.success("Registro de férias adicionado.")
                st.rerun()

    with aba_edit:
        st.subheader("Editar registro existente")

        if df_ferias.empty:
            st.info("Nenhum registro disponível.")
        else:
            opcoes = df_ferias.index.astype(str) + " - " + df_ferias["Funcionario"].astype(str)
            escolha = st.selectbox("Selecionar funcionário", opcoes, key="ferias_edit_select")
            idx = int(escolha.split(" - ")[0])
            linha = df_ferias.loc[idx]

            matricula = st.text_input("Matrícula", value=str(linha["Matricula"]), key=f"ferias_edit_matricula_{idx}")
            funcionario = st.text_input("Funcionário", value=str(linha["Funcionario"]), key=f"ferias_edit_funcionario_{idx}")
            unidade = st.text_input("Unidade / Local", value=str(linha["Unidade"]), key=f"ferias_edit_unidade_{idx}")
            departamento = st.text_input("Departamento", value=str(linha["Departamento"]), key=f"ferias_edit_departamento_{idx}")

            periodo_inicio_val = para_data(linha["Periodo_Aquisitivo_Inicio"]) or date.today()
            periodo_fim_val = para_data(linha["Periodo_Aquisitivo_Fim"]) or date.today() + timedelta(days=365)
            inicio_gozo_val = para_data(linha["Data_Inicio_Gozo"])
            fim_gozo_val = para_data(linha["Data_Fim_Gozo"])
            limite_val = para_data(linha["Limite_Gozo"]) or periodo_fim_val + timedelta(days=335)

            col1, col2 = st.columns(2)
            with col1:
                periodo_inicio = st.date_input(
                    "Início do período aquisitivo",
                    value=periodo_inicio_val,
                    format="DD/MM/YYYY",
                    key=f"ferias_edit_inicio_{idx}",
                )
            with col2:
                periodo_fim = st.date_input(
                    "Fim do período aquisitivo",
                    value=periodo_fim_val,
                    format="DD/MM/YYYY",
                    key=f"ferias_edit_fim_{idx}",
                )

            col3, col4 = st.columns(2)
            with col3:
                data_inicio_gozo = st.date_input(
                    "Início do gozo",
                    value=inicio_gozo_val,
                    format="DD/MM/YYYY",
                    key=f"ferias_edit_inicio_gozo_{idx}",
                )
            with col4:
                data_fim_gozo = st.date_input(
                    "Fim do gozo",
                    value=fim_gozo_val,
                    format="DD/MM/YYYY",
                    key=f"ferias_edit_fim_gozo_{idx}",
                )

            dias_gozo = calcular_dias(data_inicio_gozo, data_fim_gozo)

            limite_gozo = st.date_input(
                "Limite de gozo",
                value=limite_val,
                format="DD/MM/YYYY",
                key=f"ferias_edit_limite_{idx}",
            )

            periodo_gozo = st.text_input(
                "Período de gozo",
                value=str(linha["Periodo_Gozo"]),
                key=f"ferias_edit_periodo_gozo_{idx}",
            )

            col_salvar, col_excluir = st.columns(2)

            if col_salvar.button("Salvar alterações", use_container_width=True, key=f"btn_salvar_ferias_{idx}"):
                situacao_ferias, situacao_prazo = calcular_status(periodo_fim, limite_gozo)

                df_ferias.loc[idx, "Matricula"] = matricula
                df_ferias.loc[idx, "Funcionario"] = funcionario
                df_ferias.loc[idx, "Unidade"] = unidade
                df_ferias.loc[idx, "Departamento"] = departamento
                df_ferias.loc[idx, "Periodo_Aquisitivo_Inicio"] = periodo_inicio
                df_ferias.loc[idx, "Periodo_Aquisitivo_Fim"] = periodo_fim
                df_ferias.loc[idx, "Data_Inicio_Gozo"] = data_inicio_gozo or ""
                df_ferias.loc[idx, "Data_Fim_Gozo"] = data_fim_gozo or ""
                df_ferias.loc[idx, "Dias_Gozo"] = dias_gozo
                df_ferias.loc[idx, "Limite_Gozo"] = limite_gozo
                df_ferias.loc[idx, "Periodo_Gozo"] = periodo_gozo
                df_ferias.loc[idx, "Situacao_Ferias"] = situacao_ferias
                df_ferias.loc[idx, "Situacao_Prazo"] = situacao_prazo

                salvar_github(df_ferias, ARQ_FERIAS, TOKEN, REPO)
                st.success("Registro atualizado.")
                st.rerun()

            if col_excluir.button("Excluir registro", use_container_width=True, key=f"btn_excluir_ferias_{idx}"):
                df_ferias = df_ferias.drop(idx).reset_index(drop=True)
                salvar_github(df_ferias, ARQ_FERIAS, TOKEN, REPO)
                st.warning("Registro excluído.")
                st.rerun()


def render_folgas(df_ferias):
    st.subheader("Controle de Folgas")

    df_folgas = carregar_github(ARQ_FOLGAS, TOKEN, REPO)
    df_folgas = normalizar_dataframe(df_folgas, COLUNAS_FOLGAS)

    mostrar_alertas_folgas(df_folgas)

    if df_ferias.empty:
        st.warning("Cadastre funcionários em férias primeiro para usar o controle de folgas.")
        return

    st.markdown("### Nova folga")

    opcoes = df_ferias.index.astype(str) + " - " + df_ferias["Funcionario"].astype(str)
    escolha = st.selectbox("Selecionar funcionário", opcoes, key="folga_funcionario_select")

    idx = int(escolha.split(" - ")[0])
    funcionario_base = df_ferias.loc[idx]
    funcionario_nome = str(funcionario_base["Funcionario"])

    df_func = df_folgas[df_folgas["Funcionario"].astype(str) == funcionario_nome].copy()
    ultima_saida = None

    if not df_func.empty:
        df_func["Data_Saida_Data"] = df_func["Data_Saida"].apply(para_data)
        df_func = df_func.dropna(subset=["Data_Saida_Data"])
        if not df_func.empty:
            ultima_saida = df_func["Data_Saida_Data"].max()
            dias_desde = (date.today() - ultima_saida).days

            if dias_desde < DIAS_INTERVALO_FOLGA:
                st.warning(
                    f"⚠️ Última folga de {funcionario_nome}: {ultima_saida.strftime('%d/%m/%Y')} "
                    f"({dias_desde} dias atrás). Regra sugerida: intervalo mínimo de 60 dias."
                )
            else:
                st.success(
                    f"✅ Última folga de {funcionario_nome}: {ultima_saida.strftime('%d/%m/%Y')} "
                    f"({dias_desde} dias atrás)."
                )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.text_input("Matrícula", value=str(funcionario_base["Matricula"]), disabled=True, key="folga_matricula_view")
    with col2:
        st.text_input("Unidade", value=str(funcionario_base["Unidade"]), disabled=True, key="folga_unidade_view")
    with col3:
        st.text_input("Departamento", value=str(funcionario_base["Departamento"]), disabled=True, key="folga_departamento_view")

    data_saida = st.date_input(
        "Data de saída para folga",
        value=date.today(),
        format="DD/MM/YYYY",
        key="folga_data_saida",
    )

    dias_folga = st.number_input(
        "Dias de folga",
        min_value=1,
        max_value=30,
        value=7,
        step=1,
        key="folga_dias",
    )

    data_retorno = data_saida + timedelta(days=int(dias_folga))

    st.info(f"Data de retorno calculada: **{data_retorno.strftime('%d/%m/%Y')}**")

    if ultima_saida:
        intervalo = (data_saida - ultima_saida).days
        if intervalo < DIAS_INTERVALO_FOLGA:
            st.error(
                f"🚨 Atenção: esta nova folga está apenas {intervalo} dias após a última. "
                f"O recomendado é no mínimo 60 dias."
            )

    observacoes = st.text_area("Observações", key="folga_observacoes")

    if st.button("Registrar folga", use_container_width=True, key="btn_registrar_folga"):
        novo = {
            "Matricula": funcionario_base["Matricula"],
            "Funcionario": funcionario_base["Funcionario"],
            "Unidade": funcionario_base["Unidade"],
            "Departamento": funcionario_base["Departamento"],
            "Data_Saida": data_saida,
            "Data_Retorno": data_retorno,
            "Dias_Folga": int(dias_folga),
            "Observacoes": observacoes,
            "Criado_Por": st.session_state.get("usuario", ""),
            "Data_Registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        df_folgas = pd.concat([df_folgas, pd.DataFrame([novo])], ignore_index=True)
        salvar_github(df_folgas, ARQ_FOLGAS, TOKEN, REPO)

        st.success("Folga registrada com sucesso.")
        st.rerun()

    st.divider()

    st.markdown("### Histórico de folgas")

    filtro = st.selectbox(
        "Filtrar histórico",
        ["Todos"] + sorted(df_folgas["Funcionario"].dropna().astype(str).unique().tolist()),
        key="folga_filtro_historico",
    )

    df_exibir = df_folgas.copy()

    if filtro != "Todos":
        df_exibir = df_exibir[df_exibir["Funcionario"] == filtro]

    if df_exibir.empty:
        st.info("Nenhuma folga registrada ainda.")
    else:
        df_exibir = df_exibir.sort_values(by="Data_Saida", ascending=False)
        df_exibir_br = preparar_exibicao_folgas(df_exibir)

        st.dataframe(
            df_exibir_br.style.apply(cor_linha_folgas, axis=1),
            use_container_width=True,
        )


def render():
    st.title("Férias e Folgas")

    df_ferias = carregar_github(ARQ_FERIAS, TOKEN, REPO)
    df_ferias = normalizar_dataframe(df_ferias, COLUNAS_FERIAS)

    aba_ferias, aba_folgas = st.tabs(["Controle de Férias", "Controle de Folgas"])

    with aba_ferias:
        render_ferias(df_ferias)

    with aba_folgas:
        render_folgas(df_ferias)

    st.divider()

    if st.button("⬅ Voltar", use_container_width=True, key="btn_voltar_ferias"):
        st.session_state.tela = "menu"
        st.rerun()
