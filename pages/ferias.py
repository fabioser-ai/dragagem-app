import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
from services.github import ler_csv_github, salvar_csv_github
from services.ferias_regras import (
    COLUNAS_CICLO_VIDA,
    TransicaoCicloInvalida,
    TransicaoNaoAutorizada,
    calcular_status_ferias,
    normalizar_ciclo_vida_dataframe,
    recalcular_status_dataframe,
    separar_operacao_historico,
    transicionar_ciclo_vida,
    validar_registro_ferias,
)
from services.permissoes import pode_acessar_modulo, pode_executar

try:
    from services.email_service import enviar_email_smtp
except Exception:
    enviar_email_smtp = None


TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

ARQ_FERIAS = "data/ferias.csv"
ARQ_FOLGAS = "data/folgas.csv"

DIAS_INTERVALO_FOLGA = 60
DIAS_ALERTA_FOLGA = 20
DIAS_ALERTA_FERIAS = 60

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
] + COLUNAS_CICLO_VIDA

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
] + COLUNAS_CICLO_VIDA


# =========================
# FUNÇÕES AUXILIARES
# =========================
def carregar_csv_seguro(arquivo):
    resultado = ler_csv_github(arquivo, TOKEN, REPO)

    if not resultado.pode_sobrescrever:
        detalhe = resultado.erro or resultado.status.value
        st.error(
            f"Não foi possível confirmar a leitura de {arquivo}. "
            f"Nenhuma alteração será permitida. Detalhe: {detalhe}"
        )
        return None, None

    return resultado.dados, resultado.sha


def salvar_csv_seguro(df, arquivo, sha_esperado):
    resultado = salvar_csv_github(
        df,
        arquivo,
        TOKEN,
        REPO,
        sha_esperado=sha_esperado,
    )

    if resultado.sucesso:
        return True

    if resultado.erro:
        st.error(resultado.erro)
    else:
        st.error(f"Não foi possível salvar {arquivo}: {resultado.status.value}")

    return False


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


def aplicar_transicao(
    df,
    *,
    indice,
    novo_estado,
    arquivo,
    sha_esperado,
    data_efetiva=None,
):
    """Revalida permissão no ponto sensível e persiste somente se tudo for válido."""
    try:
        atualizado = transicionar_ciclo_vida(
            df.loc[indice],
            novo_estado,
            usuario=st.session_state.get("usuario", ""),
            autorizado=pode_executar("ferias", "ciclo_vida", "alterar"),
            data_efetiva=data_efetiva,
        )
    except (TransicaoCicloInvalida, TransicaoNaoAutorizada) as erro:
        st.error(str(erro))
        return False

    candidato = df.copy()
    for coluna, valor in atualizado.items():
        candidato.at[indice, coluna] = valor
    candidato = normalizar_dataframe(candidato, list(df.columns))
    return salvar_csv_seguro(candidato, arquivo, sha_esperado)


def render_acoes_ciclo_vida(df, *, arquivo, sha_esperado, prefixo):
    operacao, _ = separar_operacao_historico(df)
    if operacao.empty:
        st.info("Nenhum registro operacional disponível para transição.")
        return

    opcoes = {
        f"{idx} - {linha.get('Funcionario', '')} | {linha.get('Estado_Ciclo', '')}": idx
        for idx, linha in operacao.iterrows()
    }
    escolha = st.selectbox(
        "Registro para acompanhamento",
        list(opcoes),
        key=f"{prefixo}_ciclo_registro",
    )
    indice = opcoes[escolha]
    estado = str(df.at[indice, "Estado_Ciclo"])
    data_efetiva = st.date_input(
        "Data efetiva da confirmação",
        value=date.today(),
        format="DD/MM/YYYY",
        key=f"{prefixo}_ciclo_data_{indice}",
    )

    destinos = {
        "pendente": [("Programar", "programada"), ("Cancelar", "cancelada")],
        "programada": [("Confirmar início", "em_gozo"), ("Cancelar", "cancelada")],
        "em_gozo": [("Confirmar término", "concluida")],
    }.get(estado, [])

    if not destinos:
        st.info("Este registro não possui transições disponíveis.")
        return

    st.caption(f"Estado atual: `{estado}`. A ação registra usuário, data e horário.")
    confirmar = st.checkbox(
        "Confirmo esta alteração de estado.",
        key=f"{prefixo}_ciclo_confirmar_{indice}_{estado}",
    )
    colunas = st.columns(len(destinos))
    for coluna, (rotulo, destino) in zip(colunas, destinos):
        if coluna.button(
            rotulo,
            use_container_width=True,
            disabled=not confirmar,
            key=f"{prefixo}_ciclo_{indice}_{destino}",
        ):
            if aplicar_transicao(
                df,
                indice=indice,
                novo_estado=destino,
                arquivo=arquivo,
                sha_esperado=sha_esperado,
                data_efetiva=data_efetiva,
            ):
                st.success("Ciclo de vida atualizado com sucesso.")
                st.rerun()


def filtrar_historico(df, *, prefixo):
    _, historico = separar_operacao_historico(df)
    if historico.empty:
        return historico

    col1, col2, col3 = st.columns(3)
    funcionarios = ["Todos"] + sorted(
        historico["Funcionario"].fillna("").astype(str).unique().tolist()
    )
    estados = ["Todos"] + sorted(
        historico["Estado_Ciclo"].fillna("").astype(str).unique().tolist()
    )
    responsaveis = sorted(set(
        historico["Confirmado_Termino_Por"].fillna("").astype(str).tolist()
        + historico["Cancelado_Por"].fillna("").astype(str).tolist()
    ) - {""})
    funcionario = col1.selectbox("Funcionário", funcionarios, key=f"{prefixo}_hist_func")
    estado = col2.selectbox("Estado", estados, key=f"{prefixo}_hist_estado")
    responsavel = col3.selectbox(
        "Responsável", ["Todos"] + responsaveis, key=f"{prefixo}_hist_resp"
    )
    col4, col5 = st.columns(2)
    matriculas = ["Todas"] + sorted(
        set(historico["Matricula"].fillna("").astype(str).tolist()) - {""}
    )
    anos = set()
    for coluna_data in ("Data_Prevista_Inicio", "Data_Efetiva_Inicio"):
        datas = pd.to_datetime(historico[coluna_data], errors="coerce").dropna()
        anos.update(datas.dt.year.astype(str).tolist())
    matricula = col4.selectbox("Matrícula", matriculas, key=f"{prefixo}_hist_mat")
    ano = col5.selectbox("Ano/período", ["Todos"] + sorted(anos), key=f"{prefixo}_hist_ano")

    if funcionario != "Todos":
        historico = historico[historico["Funcionario"].astype(str) == funcionario]
    if estado != "Todos":
        historico = historico[historico["Estado_Ciclo"].astype(str) == estado]
    if responsavel != "Todos":
        historico = historico[
            (historico["Confirmado_Termino_Por"].astype(str) == responsavel)
            | (historico["Cancelado_Por"].astype(str) == responsavel)
        ]
    if matricula != "Todas":
        historico = historico[historico["Matricula"].astype(str) == matricula]
    if ano != "Todos":
        prevista = pd.to_datetime(historico["Data_Prevista_Inicio"], errors="coerce")
        efetiva = pd.to_datetime(historico["Data_Efetiva_Inicio"], errors="coerce")
        historico = historico[
            prevista.dt.year.eq(int(ano)) | efetiva.dt.year.eq(int(ano))
        ]
    return historico


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
    return calcular_status_ferias(periodo_fim, limite_gozo)


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

    # Evita Pandas Styler, que pode gerar texto branco/ilegível no Safari mobile.
    df_exibir.insert(
        0,
        "Status",
        df_exibir.apply(status_visual_ferias, axis=1),
    )

    return df_exibir


def preparar_exibicao_folgas(df):
    df_exibir = df.copy()

    for col in ["Data_Saida", "Data_Retorno"]:
        if col in df_exibir.columns:
            df_exibir[col] = df_exibir[col].apply(formatar_data_br)

    if "Data_Registro" in df_exibir.columns:
        df_exibir["Data_Registro"] = df_exibir["Data_Registro"].apply(formatar_datetime_br)

    df_exibir.insert(
        0,
        "Status",
        df_exibir.apply(status_visual_folgas, axis=1),
    )

    return df_exibir


def status_visual_ferias(row):
    situacao_prazo = row.get("Situacao_Prazo", "")
    situacao_ferias = row.get("Situacao_Ferias", "")

    if situacao_prazo == "Férias em Dobro":
        return "🔴 Em Dobro"

    if situacao_prazo == "Atenção":
        return "🟡 Atenção"

    if situacao_ferias == "Férias Vencidas":
        return "🟠 Vencidas"

    if situacao_prazo == "Dentro do Prazo":
        return "🟢 OK"

    return "⚪ Indefinido"


def status_visual_folgas(row):
    retorno = para_data(row.get("Data_Retorno"))

    if retorno and retorno >= date.today():
        return "🔵 Ativa/Futura"

    return "⚪ Histórico"


# Mantidas por compatibilidade, mas não usadas na exibição mobile.
# Evitamos df.style.apply(...) porque no Safari/iPhone pode deixar texto branco.
def cor_linha_ferias(row):
    if row.get("Situacao_Prazo") == "Férias em Dobro":
        return ["background-color: #fee2e2; color: #111827"] * len(row)

    if row.get("Situacao_Prazo") == "Atenção":
        return ["background-color: #fef3c7; color: #111827"] * len(row)

    if row.get("Situacao_Ferias") == "Férias Vencidas":
        return ["background-color: #fff7ed; color: #111827"] * len(row)

    return ["background-color: #ecfdf5; color: #111827"] * len(row)


def cor_linha_folgas(row):
    retorno = para_data(row.get("Data_Retorno"))

    if retorno and retorno >= date.today():
        return ["background-color: #dbeafe; color: #111827"] * len(row)

    return ["color: #111827"] * len(row)


# =========================
# ALERTAS POR E-MAIL
# =========================
def secrets_email_configurados():
    chaves = [
        "EMAIL_SMTP_HOST",
        "EMAIL_SMTP_PORT",
        "EMAIL_USUARIO",
        "EMAIL_SENHA",
        "EMAIL_ORIGEM",
        "EMAIL_DESTINO_ALERTAS",
    ]

    ausentes = []

    for chave in chaves:
        try:
            valor = st.secrets[chave]
            if valor is None or str(valor).strip() == "":
                ausentes.append(chave)
        except Exception:
            ausentes.append(chave)

    return len(ausentes) == 0, ausentes


def obter_alertas_ferias(df_ferias):
    hoje = date.today()

    if df_ferias.empty:
        return pd.DataFrame(), pd.DataFrame()

    df_alerta = df_ferias.copy()
    df_alerta["Limite_Gozo_Data"] = df_alerta["Limite_Gozo"].apply(para_data)

    ferias_dobro = df_alerta[df_alerta["Situacao_Prazo"] == "Férias em Dobro"].copy()

    proximos_limite = df_alerta[
        df_alerta["Limite_Gozo_Data"].apply(
            lambda x: x is not None and 0 <= (x - hoje).days <= DIAS_ALERTA_FERIAS
        )
    ].copy()

    if not proximos_limite.empty:
        proximos_limite["Dias_Para_Limite"] = proximos_limite["Limite_Gozo_Data"].apply(
            lambda x: (x - hoje).days if x else None
        )
        proximos_limite = proximos_limite.sort_values(by="Dias_Para_Limite")

    return ferias_dobro, proximos_limite


def montar_corpo_email_alerta_ferias(df_ferias):
    hoje = date.today()
    ferias_dobro, proximos_limite = obter_alertas_ferias(df_ferias)

    if ferias_dobro.empty and proximos_limite.empty:
        return None

    linhas = []
    linhas.append("ALERTA AUTOMÁTICO - CONTROLE DE FÉRIAS")
    linhas.append("")
    linhas.append(f"Data da verificação: {hoje.strftime('%d/%m/%Y')}")
    linhas.append("")

    if not ferias_dobro.empty:
        linhas.append("FÉRIAS EM DOBRO")
        linhas.append("----------------")

        for _, linha in ferias_dobro.iterrows():
            linhas.append(
                f"- {linha.get('Funcionario', '')} | "
                f"Matrícula: {linha.get('Matricula', '')} | "
                f"Unidade: {linha.get('Unidade', '')} | "
                f"Departamento: {linha.get('Departamento', '')} | "
                f"Limite de gozo: {formatar_data_br(linha.get('Limite_Gozo'))}"
            )

        linhas.append("")

    if not proximos_limite.empty:
        linhas.append(f"FÉRIAS PRÓXIMAS DO LIMITE - ATÉ {DIAS_ALERTA_FERIAS} DIAS")
        linhas.append("------------------------------------------------")

        for _, linha in proximos_limite.iterrows():
            limite = linha.get("Limite_Gozo_Data")
            dias = linha.get("Dias_Para_Limite")

            linhas.append(
                f"- {linha.get('Funcionario', '')} | "
                f"Matrícula: {linha.get('Matricula', '')} | "
                f"Unidade: {linha.get('Unidade', '')} | "
                f"Departamento: {linha.get('Departamento', '')} | "
                f"Limite de gozo: {limite.strftime('%d/%m/%Y') if limite else ''} | "
                f"Dias restantes: {dias}"
            )

        linhas.append("")

    linhas.append("Mensagem gerada automaticamente pelo sistema FOS Engenharia.")
    linhas.append("Favor verificar o planejamento de férias e tomar as providências necessárias.")

    return "\n".join(linhas)


def enviar_alerta_ferias_por_email(df_ferias):
    if enviar_email_smtp is None:
        return False, "Arquivo services/email_service.py não encontrado ou com erro de importação."

    configurado, ausentes = secrets_email_configurados()

    if not configurado:
        return False, "Configurações de e-mail ausentes no secrets.toml: " + ", ".join(ausentes)

    corpo = montar_corpo_email_alerta_ferias(df_ferias)

    if not corpo:
        return False, "Nenhum alerta crítico de férias encontrado para envio."

    enviar_email_smtp(
        smtp_host=st.secrets["EMAIL_SMTP_HOST"],
        smtp_port=st.secrets["EMAIL_SMTP_PORT"],
        smtp_usuario=st.secrets["EMAIL_USUARIO"],
        smtp_senha=st.secrets["EMAIL_SENHA"],
        email_origem=st.secrets["EMAIL_ORIGEM"],
        email_destino=st.secrets["EMAIL_DESTINO_ALERTAS"],
        assunto="Alerta de férias - FOS Engenharia",
        corpo=corpo,
    )

    return True, "E-mail de alerta de férias enviado com sucesso."


# =========================
# REGRAS DE FOLGAS
# =========================
def existe_sobreposicao_folga(df_folgas, matricula, data_saida, data_retorno, ignorar_idx=None):
    if df_folgas.empty:
        return False, None

    df_tmp = df_folgas.copy()
    df_tmp["Data_Saida_Data"] = df_tmp["Data_Saida"].apply(para_data)
    df_tmp["Data_Retorno_Data"] = df_tmp["Data_Retorno"].apply(para_data)

    df_tmp = df_tmp[df_tmp["Matricula"].astype(str) == str(matricula)]

    if ignorar_idx is not None and ignorar_idx in df_tmp.index:
        df_tmp = df_tmp.drop(index=ignorar_idx)

    for _, linha in df_tmp.iterrows():
        saida_existente = linha.get("Data_Saida_Data")
        retorno_existente = linha.get("Data_Retorno_Data")

        if saida_existente is None or retorno_existente is None:
            continue

        sobrepoe = data_saida <= retorno_existente and data_retorno >= saida_existente

        if sobrepoe:
            return True, linha

    return False, None


def ordenar_folgas_por_data(df):
    if df.empty:
        return df

    df_tmp = df.copy()
    df_tmp["_Data_Saida_Ordenacao"] = df_tmp["Data_Saida"].apply(para_data)
    df_tmp = df_tmp.sort_values(by="_Data_Saida_Ordenacao", ascending=False)
    df_tmp = df_tmp.drop(columns=["_Data_Saida_Ordenacao"])

    return df_tmp


# =========================
# ALERTAS NA TELA
# =========================
def mostrar_alertas_ferias(df):
    if df.empty:
        return

    ferias_dobro, proximos_60 = obter_alertas_ferias(df)

    if not ferias_dobro.empty:
        st.error(f"🚨 {len(ferias_dobro)} funcionário(s) com férias em dobro:")

        for nome in ferias_dobro["Funcionario"].dropna().astype(str):
            st.markdown(f"- 🔴 **{nome}**")

    if not proximos_60.empty:
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


def mostrar_alertas_proximas_folgas(df_ferias, df_folgas):
    if df_ferias.empty:
        return

    hoje = date.today()

    if df_folgas.empty:
        st.info("ℹ️ Ainda não há histórico de folgas registrado.")
        return

    alertas_vencidos = []
    alertas_proximos = []
    sem_historico = []

    for _, funcionario in df_ferias.iterrows():
        matricula = str(funcionario.get("Matricula", ""))
        nome = str(funcionario.get("Funcionario", ""))

        if not nome.strip():
            continue

        df_func = df_folgas[df_folgas["Matricula"].astype(str) == matricula].copy()

        if df_func.empty:
            sem_historico.append(nome)
            continue

        df_func["Data_Saida_Data"] = df_func["Data_Saida"].apply(para_data)
        df_func = df_func.dropna(subset=["Data_Saida_Data"])

        if df_func.empty:
            sem_historico.append(nome)
            continue

        ultima_saida = df_func["Data_Saida_Data"].max()
        data_recomendada = ultima_saida + timedelta(days=DIAS_INTERVALO_FOLGA)
        dias_para_limite = (data_recomendada - hoje).days

        if dias_para_limite < 0:
            alertas_vencidos.append({
                "Funcionario": nome,
                "Ultima_Saida": ultima_saida,
                "Data_Recomendada": data_recomendada,
                "Dias": dias_para_limite,
            })

        elif dias_para_limite <= DIAS_ALERTA_FOLGA:
            alertas_proximos.append({
                "Funcionario": nome,
                "Ultima_Saida": ultima_saida,
                "Data_Recomendada": data_recomendada,
                "Dias": dias_para_limite,
            })

    if not alertas_vencidos and not alertas_proximos:
        st.success("✅ Nenhum funcionário próximo da data recomendada de folga.")

    if alertas_vencidos:
        st.error("🚨 Funcionários com data recomendada de folga vencida:")

        alertas_vencidos = sorted(alertas_vencidos, key=lambda x: x["Dias"])

        for alerta in alertas_vencidos:
            st.markdown(
                f"- **{alerta['Funcionario']}** → data recomendada era "
                f"**{alerta['Data_Recomendada'].strftime('%d/%m/%Y')}** "
                f"({abs(alerta['Dias'])} dias atrás). "
                f"Última saída: **{alerta['Ultima_Saida'].strftime('%d/%m/%Y')}**."
            )

    if alertas_proximos:
        st.warning(
            f"⚠️ Funcionários que entram na janela de alerta de {DIAS_ALERTA_FOLGA} dias:"
        )

        alertas_proximos = sorted(alertas_proximos, key=lambda x: x["Dias"])

        for alerta in alertas_proximos:
            st.markdown(
                f"- **{alerta['Funcionario']}** → próxima folga recomendada em "
                f"**{alerta['Data_Recomendada'].strftime('%d/%m/%Y')}** "
                f"({alerta['Dias']} dias restantes). "
                f"Última saída: **{alerta['Ultima_Saida'].strftime('%d/%m/%Y')}**."
            )

    if sem_historico:
        with st.expander("Funcionários sem histórico de folga"):
            for nome in sorted(sem_historico):
                st.markdown(f"- ℹ️ **{nome}**")


# =========================
# TELA DE FÉRIAS
# =========================
def render_ferias(df_ferias, sha_ferias, pode_enviar_alerta, pode_excluir):
    st.subheader("Resumo de Férias")

    df_operacao, df_historico = separar_operacao_historico(df_ferias)

    mostrar_alertas_ferias(df_operacao)

    if pode_enviar_alerta:
        email_container = st.expander("📧 Envio de alerta por e-mail", expanded=False)
    else:
        email_container = st.container()
        st.caption("Envio de alertas disponível somente para usuários autorizados.")

    with email_container:
        if pode_enviar_alerta:
            st.caption(
                "Este envio usa as configurações de e-mail cadastradas no secrets.toml. "
                "Nesta fase, o disparo é manual para teste e validação."
            )

            configurado, ausentes = secrets_email_configurados()

            if configurado:
                st.success("Configurações de e-mail encontradas.")
            else:
                st.warning("Configurações de e-mail incompletas.")
                st.markdown("Chaves ausentes ou vazias:")
                for chave in ausentes:
                    st.markdown(f"- `{chave}`")

            corpo_preview = montar_corpo_email_alerta_ferias(df_operacao)

            if corpo_preview:
                with st.expander("Pré-visualizar conteúdo do e-mail"):
                    st.code(corpo_preview, language="text")
            else:
                st.info("Nenhum alerta crítico encontrado para montar e-mail neste momento.")

            if st.button("📧 Enviar alerta de férias por e-mail", use_container_width=True, key="btn_enviar_alerta_ferias_email"):
                try:
                    enviado, mensagem = enviar_alerta_ferias_por_email(df_operacao)

                    if enviado:
                        st.success(mensagem)
                    else:
                        st.info(mensagem)

                except Exception as e:
                    st.error(f"Erro ao enviar e-mail de alerta: {e}")

    total = len(df_operacao)
    vencidas = len(df_operacao[df_operacao["Situacao_Ferias"] == "Férias Vencidas"])
    dobro = len(df_operacao[df_operacao["Situacao_Prazo"] == "Férias em Dobro"])
    atencao = len(df_operacao[df_operacao["Situacao_Prazo"] == "Atenção"])

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
        help=f"Funcionários próximos do limite legal de gozo das férias. Hoje o sistema considera Atenção quando faltam {DIAS_ALERTA_FERIAS} dias ou menos para o limite.",
    )

    col4.metric(
        "Férias em dobro",
        dobro,
        help="Funcionários que ultrapassaram o prazo legal de gozo. Essa situação pode gerar pagamento em dobro das férias.",
    )

    st.divider()

    st.subheader("Lista de Controle de Férias")

    if df_operacao.empty:
        st.info("Nenhum registro exige acompanhamento operacional.")
    else:
        df_exibir = preparar_exibicao_ferias(df_operacao)

        # Importante:
        # Não usamos df.style.apply(...) aqui, pois no Safari/iPhone pode deixar os textos ilegíveis.
        st.dataframe(
            df_exibir,
            use_container_width=True,
            hide_index=True,
        )

    with st.expander("Acompanhamento do ciclo de vida", expanded=False):
        render_acoes_ciclo_vida(
            df_ferias,
            arquivo=ARQ_FERIAS,
            sha_esperado=sha_ferias,
            prefixo="ferias",
        )

    with st.expander(f"Histórico de férias ({len(df_historico)})", expanded=False):
        historico_filtrado = filtrar_historico(df_ferias, prefixo="ferias")
        if historico_filtrado.empty:
            st.info("Nenhum registro encontrado no histórico.")
        else:
            st.dataframe(
                preparar_exibicao_ferias(historico_filtrado),
                use_container_width=True,
                hide_index=True,
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
            erros = validar_registro_ferias(
                df_ferias,
                matricula=matricula,
                funcionario=funcionario,
                periodo_inicio=periodo_inicio,
                periodo_fim=periodo_fim,
                inicio_gozo=data_inicio_gozo,
                fim_gozo=data_fim_gozo,
            )

            if erros:
                for erro in erros:
                    st.error(erro)
            else:
                situacao_ferias, situacao_prazo = calcular_status(periodo_fim, limite_gozo)

                novo = {
                    "Matricula": str(matricula),
                    "Funcionario": str(funcionario),
                    "Unidade": str(unidade),
                    "Departamento": str(departamento),
                    "Periodo_Aquisitivo_Inicio": periodo_inicio,
                    "Periodo_Aquisitivo_Fim": periodo_fim,
                    "Data_Inicio_Gozo": data_inicio_gozo or "",
                    "Data_Fim_Gozo": data_fim_gozo or "",
                    "Dias_Gozo": dias_gozo,
                    "Limite_Gozo": limite_gozo,
                    "Periodo_Gozo": str(periodo_gozo),
                    "Situacao_Ferias": situacao_ferias,
                    "Situacao_Prazo": situacao_prazo,
                    "Estado_Ciclo": "programada" if data_inicio_gozo else "pendente",
                    "Data_Prevista_Inicio": data_inicio_gozo or "",
                    "Data_Prevista_Termino": data_fim_gozo or "",
                }

                df_ferias = pd.concat([df_ferias, pd.DataFrame([novo])], ignore_index=True)
                df_ferias = normalizar_dataframe(df_ferias, COLUNAS_FERIAS)
                if not salvar_csv_seguro(df_ferias, ARQ_FERIAS, sha_ferias):
                    return

                st.success("Registro de férias adicionado.")
                st.rerun()

    with aba_edit:
        st.subheader("Editar registro existente")

        if df_operacao.empty:
            st.info("Nenhum registro disponível.")
        else:
            opcoes = df_operacao.index.astype(str) + " - " + df_operacao["Funcionario"].astype(str)

            escolha = st.selectbox(
                "Selecionar funcionário",
                opcoes,
                key="ferias_edit_select",
            )

            idx = int(escolha.split(" - ")[0])
            linha = df_ferias.loc[idx]

            matricula = st.text_input(
                "Matrícula",
                value=str(linha["Matricula"]),
                key=f"ferias_edit_matricula_{idx}",
            )

            funcionario = st.text_input(
                "Funcionário",
                value=str(linha["Funcionario"]),
                key=f"ferias_edit_funcionario_{idx}",
            )

            unidade = st.text_input(
                "Unidade / Local",
                value=str(linha["Unidade"]),
                key=f"ferias_edit_unidade_{idx}",
            )

            departamento = st.text_input(
                "Departamento",
                value=str(linha["Departamento"]),
                key=f"ferias_edit_departamento_{idx}",
            )

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

            confirmar_exclusao = st.checkbox(
                "Confirmo a exclusão definitiva deste registro de férias.",
                key=f"confirmar_exclusao_ferias_{idx}",
                disabled=not pode_excluir,
            )
            col_salvar, col_excluir = st.columns(2)

            if col_salvar.button(
                "Salvar alterações",
                use_container_width=True,
                key=f"btn_salvar_ferias_{idx}",
            ):
                erros = validar_registro_ferias(
                    df_ferias,
                    matricula=matricula,
                    funcionario=funcionario,
                    periodo_inicio=periodo_inicio,
                    periodo_fim=periodo_fim,
                    inicio_gozo=data_inicio_gozo,
                    fim_gozo=data_fim_gozo,
                    ignorar_indice=idx,
                )

                if erros:
                    for erro in erros:
                        st.error(erro)
                else:
                    situacao_ferias, situacao_prazo = calcular_status(periodo_fim, limite_gozo)

                    df_ferias.loc[idx, "Matricula"] = str(matricula)
                    df_ferias.loc[idx, "Funcionario"] = str(funcionario)
                    df_ferias.loc[idx, "Unidade"] = str(unidade)
                    df_ferias.loc[idx, "Departamento"] = str(departamento)
                    df_ferias.loc[idx, "Periodo_Aquisitivo_Inicio"] = periodo_inicio
                    df_ferias.loc[idx, "Periodo_Aquisitivo_Fim"] = periodo_fim
                    df_ferias.loc[idx, "Data_Inicio_Gozo"] = data_inicio_gozo or ""
                    df_ferias.loc[idx, "Data_Fim_Gozo"] = data_fim_gozo or ""
                    df_ferias.loc[idx, "Dias_Gozo"] = dias_gozo
                    df_ferias.loc[idx, "Limite_Gozo"] = limite_gozo
                    df_ferias.loc[idx, "Periodo_Gozo"] = str(periodo_gozo)
                    df_ferias.loc[idx, "Situacao_Ferias"] = situacao_ferias
                    df_ferias.loc[idx, "Situacao_Prazo"] = situacao_prazo
                    df_ferias.loc[idx, "Data_Prevista_Inicio"] = data_inicio_gozo or ""
                    df_ferias.loc[idx, "Data_Prevista_Termino"] = data_fim_gozo or ""

                    df_ferias = normalizar_dataframe(df_ferias, COLUNAS_FERIAS)
                    if not salvar_csv_seguro(df_ferias, ARQ_FERIAS, sha_ferias):
                        return

                    st.success("Registro atualizado.")
                    st.rerun()

            if col_excluir.button(
                "Excluir registro",
                use_container_width=True,
                key=f"btn_excluir_ferias_{idx}",
                disabled=not pode_excluir or not confirmar_exclusao,
            ):
                df_ferias = df_ferias.drop(idx).reset_index(drop=True)
                df_ferias = normalizar_dataframe(df_ferias, COLUNAS_FERIAS)
                if not salvar_csv_seguro(df_ferias, ARQ_FERIAS, sha_ferias):
                    return

                st.warning("Registro excluído.")
                st.rerun()


# =========================
# TELA DE FOLGAS
# =========================
def render_folgas(df_ferias, pode_excluir):
    st.subheader("Controle de Folgas")

    df_folgas, sha_folgas = carregar_csv_seguro(ARQ_FOLGAS)
    if df_folgas is None:
        return
    df_folgas = normalizar_dataframe(df_folgas, COLUNAS_FOLGAS)
    df_folgas = normalizar_ciclo_vida_dataframe(
        df_folgas,
        coluna_inicio="Data_Saida",
        coluna_termino="Data_Retorno",
    )
    df_operacao, df_historico = separar_operacao_historico(df_folgas)

    mostrar_alertas_folgas(df_operacao)
    mostrar_alertas_proximas_folgas(df_ferias, df_folgas)

    if df_ferias.empty:
        st.warning("Cadastre funcionários em férias primeiro para usar o controle de folgas.")
        return

    aba_painel, aba_hist, aba_nova, aba_edit = st.tabs(
        ["Painel atual", "Histórico", "Nova folga", "Editar / Excluir"]
    )

    with aba_painel:
        st.markdown("### Folgas em acompanhamento")
        if df_operacao.empty:
            st.info("Nenhuma folga exige acompanhamento operacional.")
        else:
            st.dataframe(
                preparar_exibicao_folgas(ordenar_folgas_por_data(df_operacao)),
                use_container_width=True,
                hide_index=True,
            )
        st.markdown("### Confirmar andamento")
        render_acoes_ciclo_vida(
            df_folgas,
            arquivo=ARQ_FOLGAS,
            sha_esperado=sha_folgas,
            prefixo="folgas",
        )

    with aba_hist:
        st.markdown("### Histórico de folgas")
        df_exibir = filtrar_historico(df_folgas, prefixo="folgas")

        if df_exibir.empty:
            st.info("Nenhuma folga registrada ainda.")
        else:
            df_exibir = ordenar_folgas_por_data(df_exibir)
            df_exibir_br = preparar_exibicao_folgas(df_exibir)

            # Importante:
            # Não usamos df.style.apply(...) aqui, pois no Safari/iPhone pode deixar os textos ilegíveis.
            st.dataframe(
                df_exibir_br,
                use_container_width=True,
                hide_index=True,
            )

    with aba_nova:
        st.markdown("### Nova folga")

        opcoes = df_ferias.index.astype(str) + " - " + df_ferias["Funcionario"].astype(str)

        escolha = st.selectbox(
            "Selecionar funcionário",
            opcoes,
            key="folga_funcionario_select",
        )

        idx = int(escolha.split(" - ")[0])
        funcionario_base = df_ferias.loc[idx]
        funcionario_nome = str(funcionario_base["Funcionario"])
        matricula_base = str(funcionario_base["Matricula"])

        df_func = df_folgas[df_folgas["Matricula"].astype(str) == matricula_base].copy()
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
            st.text_input(
                "Matrícula",
                value=str(funcionario_base["Matricula"]),
                disabled=True,
                key="folga_matricula_view",
            )

        with col2:
            st.text_input(
                "Unidade",
                value=str(funcionario_base["Unidade"]),
                disabled=True,
                key="folga_unidade_view",
            )

        with col3:
            st.text_input(
                "Departamento",
                value=str(funcionario_base["Departamento"]),
                disabled=True,
                key="folga_departamento_view",
            )

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

        sobrepoe, linha_conflito = existe_sobreposicao_folga(
            df_folgas,
            matricula_base,
            data_saida,
            data_retorno,
        )

        if sobrepoe:
            st.error(
                "🚨 Já existe uma folga cadastrada para este funcionário dentro desse período: "
                f"{formatar_data_br(linha_conflito.get('Data_Saida'))} até "
                f"{formatar_data_br(linha_conflito.get('Data_Retorno'))}."
            )

        observacoes = st.text_area("Observações", key="folga_observacoes")

        if st.button("Registrar folga", use_container_width=True, key="btn_registrar_folga"):
            if sobrepoe:
                st.error("Não foi possível registrar. Existe sobreposição com outra folga.")
            else:
                novo = {
                    "Matricula": str(funcionario_base["Matricula"]),
                    "Funcionario": str(funcionario_base["Funcionario"]),
                    "Unidade": str(funcionario_base["Unidade"]),
                    "Departamento": str(funcionario_base["Departamento"]),
                    "Data_Saida": data_saida,
                    "Data_Retorno": data_retorno,
                    "Dias_Folga": int(dias_folga),
                    "Observacoes": str(observacoes),
                    "Criado_Por": str(st.session_state.get("usuario", "")),
                    "Data_Registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Estado_Ciclo": "programada",
                    "Data_Prevista_Inicio": data_saida,
                    "Data_Prevista_Termino": data_retorno,
                }

                df_folgas = pd.concat([df_folgas, pd.DataFrame([novo])], ignore_index=True)
                df_folgas = normalizar_dataframe(df_folgas, COLUNAS_FOLGAS)
                if not salvar_csv_seguro(df_folgas, ARQ_FOLGAS, sha_folgas):
                    return

                st.success("Folga registrada com sucesso.")
                st.rerun()

    with aba_edit:
        st.markdown("### Editar / Excluir folga")

        if df_operacao.empty:
            st.info("Nenhuma folga registrada para editar.")
        else:
            df_opcoes = df_operacao.copy()
            df_opcoes["Data_Saida_Formatada"] = df_opcoes["Data_Saida"].apply(formatar_data_br)
            df_opcoes["Data_Retorno_Formatada"] = df_opcoes["Data_Retorno"].apply(formatar_data_br)

            opcoes_edit = []

            for idx_linha, linha in df_opcoes.iterrows():
                texto = (
                    f"{idx_linha} - {linha.get('Funcionario', '')} | "
                    f"{linha.get('Data_Saida_Formatada', '')} até "
                    f"{linha.get('Data_Retorno_Formatada', '')}"
                )
                opcoes_edit.append(texto)

            escolha_edit = st.selectbox(
                "Selecionar folga",
                opcoes_edit,
                key="folga_edit_select",
            )

            idx_edit = int(escolha_edit.split(" - ")[0])
            linha = df_folgas.loc[idx_edit]

            matricula_edit = str(linha.get("Matricula", ""))
            funcionario_edit = str(linha.get("Funcionario", ""))
            unidade_edit = str(linha.get("Unidade", ""))
            departamento_edit = str(linha.get("Departamento", ""))

            col1, col2, col3 = st.columns(3)

            with col1:
                st.text_input(
                    "Matrícula",
                    value=matricula_edit,
                    disabled=True,
                    key=f"folga_edit_matricula_{idx_edit}",
                )

            with col2:
                st.text_input(
                    "Unidade",
                    value=unidade_edit,
                    disabled=True,
                    key=f"folga_edit_unidade_{idx_edit}",
                )

            with col3:
                st.text_input(
                    "Departamento",
                    value=departamento_edit,
                    disabled=True,
                    key=f"folga_edit_departamento_{idx_edit}",
                )

            st.text_input(
                "Funcionário",
                value=funcionario_edit,
                disabled=True,
                key=f"folga_edit_funcionario_{idx_edit}",
            )

            data_saida_atual = para_data(linha.get("Data_Saida")) or date.today()
            dias_atual = linha.get("Dias_Folga", 1)

            try:
                dias_atual = int(dias_atual)
            except Exception:
                dias_atual = 1

            data_saida_edit = st.date_input(
                "Data de saída para folga",
                value=data_saida_atual,
                format="DD/MM/YYYY",
                key=f"folga_edit_data_saida_{idx_edit}",
            )

            dias_folga_edit = st.number_input(
                "Dias de folga",
                min_value=1,
                max_value=30,
                value=max(1, dias_atual),
                step=1,
                key=f"folga_edit_dias_{idx_edit}",
            )

            data_retorno_edit = data_saida_edit + timedelta(days=int(dias_folga_edit))

            st.info(
                f"Data de retorno recalculada: **{data_retorno_edit.strftime('%d/%m/%Y')}**"
            )

            sobrepoe_edit, linha_conflito_edit = existe_sobreposicao_folga(
                df_folgas,
                matricula_edit,
                data_saida_edit,
                data_retorno_edit,
                ignorar_idx=idx_edit,
            )

            if sobrepoe_edit:
                st.error(
                    "🚨 Esta alteração gera sobreposição com outra folga: "
                    f"{formatar_data_br(linha_conflito_edit.get('Data_Saida'))} até "
                    f"{formatar_data_br(linha_conflito_edit.get('Data_Retorno'))}."
                )

            observacoes_edit = st.text_area(
                "Observações",
                value=str(linha.get("Observacoes", "")),
                key=f"folga_edit_observacoes_{idx_edit}",
            )

            confirmar_exclusao_folga = st.checkbox(
                "Confirmo a exclusão definitiva desta folga.",
                key=f"confirmar_exclusao_folga_{idx_edit}",
                disabled=not pode_excluir,
            )
            col_salvar, col_excluir = st.columns(2)

            if col_salvar.button(
                "Salvar alterações",
                use_container_width=True,
                key=f"btn_salvar_folga_{idx_edit}",
            ):
                if sobrepoe_edit:
                    st.error("Não foi possível salvar. Existe sobreposição com outra folga.")
                else:
                    df_folgas.loc[idx_edit, "Data_Saida"] = data_saida_edit
                    df_folgas.loc[idx_edit, "Data_Retorno"] = data_retorno_edit
                    df_folgas.loc[idx_edit, "Dias_Folga"] = int(dias_folga_edit)
                    df_folgas.loc[idx_edit, "Observacoes"] = str(observacoes_edit)
                    df_folgas.loc[idx_edit, "Data_Prevista_Inicio"] = data_saida_edit
                    df_folgas.loc[idx_edit, "Data_Prevista_Termino"] = data_retorno_edit

                    df_folgas = normalizar_dataframe(df_folgas, COLUNAS_FOLGAS)
                    if not salvar_csv_seguro(df_folgas, ARQ_FOLGAS, sha_folgas):
                        return

                    st.success("Folga atualizada com sucesso.")
                    st.rerun()

            if col_excluir.button(
                "Excluir folga",
                use_container_width=True,
                key=f"btn_excluir_folga_{idx_edit}",
                disabled=not pode_excluir or not confirmar_exclusao_folga,
            ):
                df_folgas = df_folgas.drop(idx_edit).reset_index(drop=True)
                df_folgas = normalizar_dataframe(df_folgas, COLUNAS_FOLGAS)
                if not salvar_csv_seguro(df_folgas, ARQ_FOLGAS, sha_folgas):
                    return

                st.warning("Folga excluída.")
                st.rerun()


# =========================
# RENDER PRINCIPAL
# =========================
def render():
    if not pode_acessar_modulo("ferias"):
        st.error("Você não possui permissão para acessar Férias e Folgas.")
        st.stop()

    pode_enviar_alerta = pode_executar("ferias", "alertas", "enviar")
    pode_excluir = pode_executar("ferias", "registros", "excluir")

    st.title("Férias e Folgas")

    df_ferias, sha_ferias = carregar_csv_seguro(ARQ_FERIAS)
    if df_ferias is None:
        return
    df_ferias = normalizar_dataframe(df_ferias, COLUNAS_FERIAS)
    df_ferias = normalizar_ciclo_vida_dataframe(
        df_ferias,
        coluna_inicio="Data_Inicio_Gozo",
        coluna_termino="Data_Fim_Gozo",
    )
    # Status são derivados das datas vigentes a cada abertura. Os textos
    # persistidos permanecem compatíveis, mas não são tratados como verdade.
    df_ferias = recalcular_status_dataframe(df_ferias)

    aba_ferias, aba_folgas = st.tabs(["Controle de Férias", "Controle de Folgas"])

    with aba_ferias:
        render_ferias(df_ferias, sha_ferias, pode_enviar_alerta, pode_excluir)

    with aba_folgas:
        render_folgas(df_ferias, pode_excluir)

    st.divider()

    if st.button("⬅ Voltar", use_container_width=True, key="btn_voltar_ferias"):
        st.session_state.tela = "menu"
        st.rerun()
