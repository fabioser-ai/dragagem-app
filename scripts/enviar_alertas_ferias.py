import os
import sys
import pandas as pd
from datetime import date, datetime
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from services.github import carregar_github, salvar_github
from services.email_service import enviar_email_smtp


ARQ_FERIAS = "data/ferias.csv"
ARQ_HISTORICO = "data/alertas_ferias_enviados.csv"

MARCOS_ALERTA = [60, 50, 40, 30, 20, 10, 0]

COLUNAS_HISTORICO = [
    "ID_Alerta",
    "Matricula",
    "Funcionario",
    "Limite_Gozo",
    "Dias_Restantes",
    "Marco_Alerta",
    "Email_Destino",
    "Data_Envio",
]


def para_data(valor):
    data = pd.to_datetime(valor, errors="coerce")
    if pd.isna(data):
        return None
    return data.date()


def normalizar_historico(df):
    if df.empty:
        df = pd.DataFrame(columns=COLUNAS_HISTORICO)

    for col in COLUNAS_HISTORICO:
        if col not in df.columns:
            df[col] = ""

    return df[COLUNAS_HISTORICO].copy()


def ferias_ja_marcadas(linha):
    inicio_gozo = str(linha.get("Data_Inicio_Gozo", "")).strip()
    fim_gozo = str(linha.get("Data_Fim_Gozo", "")).strip()
    periodo_gozo = str(linha.get("Periodo_Gozo", "")).strip()

    return bool(inicio_gozo or fim_gozo or periodo_gozo)


def definir_marco_alerta(dias_restantes):
    for marco in MARCOS_ALERTA:
        if dias_restantes <= marco:
            return marco
    return None


def montar_id_alerta(matricula, limite_gozo, marco):
    return f"{matricula}_{limite_gozo}_{marco}"


def montar_corpo_email(alertas):
    hoje = date.today()

    linhas = []
    linhas.append("ALERTA AUTOMÁTICO - CONTROLE DE FÉRIAS")
    linhas.append("")
    linhas.append(f"Data da verificação: {hoje.strftime('%d/%m/%Y')}")
    linhas.append("")
    linhas.append("Funcionários com férias próximas do limite:")
    linhas.append("")

    for alerta in alertas:
        linhas.append(
            f"- {alerta['Funcionario']} | "
            f"Matrícula: {alerta['Matricula']} | "
            f"Unidade: {alerta['Unidade']} | "
            f"Departamento: {alerta['Departamento']} | "
            f"Limite: {alerta['Limite_Gozo_BR']} | "
            f"Dias restantes: {alerta['Dias_Restantes']}"
        )

    linhas.append("")
    linhas.append("Mensagem gerada automaticamente pelo sistema FOS Engenharia.")
    linhas.append("Favor avaliar o agendamento das férias.")

    return "\n".join(linhas)


def main():
    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ["REPO"]

    email_destino = os.environ["EMAIL_DESTINO_ALERTAS"]

    df_ferias = carregar_github(ARQ_FERIAS, token, repo)
    df_historico = carregar_github(ARQ_HISTORICO, token, repo)
    df_historico = normalizar_historico(df_historico)

    if df_ferias.empty:
        print("Nenhum registro de férias encontrado.")
        return

    hoje = date.today()
    alertas_para_enviar = []
    novos_historicos = []

    ids_ja_enviados = set(df_historico["ID_Alerta"].astype(str).tolist())

    for _, linha in df_ferias.iterrows():
        if ferias_ja_marcadas(linha):
            continue

        limite_gozo = para_data(linha.get("Limite_Gozo"))

        if limite_gozo is None:
            continue

        dias_restantes = (limite_gozo - hoje).days

        if dias_restantes < 0 or dias_restantes > 60:
            continue

        marco = definir_marco_alerta(dias_restantes)

        if marco is None:
            continue

        matricula = str(linha.get("Matricula", "")).strip()
        funcionario = str(linha.get("Funcionario", "")).strip()

        id_alerta = montar_id_alerta(matricula, limite_gozo.isoformat(), marco)

        if id_alerta in ids_ja_enviados:
            continue

        alerta = {
            "ID_Alerta": id_alerta,
            "Matricula": matricula,
            "Funcionario": funcionario,
            "Unidade": str(linha.get("Unidade", "")),
            "Departamento": str(linha.get("Departamento", "")),
            "Limite_Gozo": limite_gozo.isoformat(),
            "Limite_Gozo_BR": limite_gozo.strftime("%d/%m/%Y"),
            "Dias_Restantes": dias_restantes,
            "Marco_Alerta": marco,
        }

        alertas_para_enviar.append(alerta)

        novos_historicos.append({
            "ID_Alerta": id_alerta,
            "Matricula": matricula,
            "Funcionario": funcionario,
            "Limite_Gozo": limite_gozo.isoformat(),
            "Dias_Restantes": dias_restantes,
            "Marco_Alerta": marco,
            "Email_Destino": email_destino,
            "Data_Envio": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

    if not alertas_para_enviar:
        print("Nenhum alerta novo para enviar.")
        return

    corpo = montar_corpo_email(alertas_para_enviar)

    enviar_email_smtp(
        smtp_host=os.environ["EMAIL_SMTP_HOST"],
        smtp_port=os.environ["EMAIL_SMTP_PORT"],
        smtp_usuario=os.environ["EMAIL_USUARIO"],
        smtp_senha=os.environ["EMAIL_SENHA"],
        email_origem=os.environ["EMAIL_ORIGEM"],
        email_destino=email_destino,
        assunto="Alerta automático de férias - FOS Engenharia",
        corpo=corpo,
    )

    df_novos = pd.DataFrame(novos_historicos)
    df_historico = pd.concat([df_historico, df_novos], ignore_index=True)
    df_historico = normalizar_historico(df_historico)

    salvar_github(df_historico, ARQ_HISTORICO, token, repo)

    print(f"{len(alertas_para_enviar)} alerta(s) enviado(s) com sucesso.")


if __name__ == "__main__":
    main()
