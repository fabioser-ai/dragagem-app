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
    data = pd.to_datetime(valor, errors="coerce", dayfirst=True)

    if pd.isna(data):
        return None

    return data.date()


def normalizar_historico(df):
    if df is None or df.empty:
        df = pd.DataFrame(columns=COLUNAS_HISTORICO)

    for col in COLUNAS_HISTORICO:
        if col not in df.columns:
            df[col] = ""

    return df[COLUNAS_HISTORICO].copy()


def texto_preenchido(valor):
    if pd.isna(valor):
        return False

    texto = str(valor).strip()

    if texto.lower() in ["", "nan", "none", "nat"]:
        return False

    return True


def ferias_ja_marcadas(linha):
    inicio_gozo = linha.get("Data_Inicio_Gozo", "")
    fim_gozo = linha.get("Data_Fim_Gozo", "")
    periodo_gozo = linha.get("Periodo_Gozo", "")

    return (
        texto_preenchido(inicio_gozo)
        or texto_preenchido(fim_gozo)
        or texto_preenchido(periodo_gozo)
    )


def definir_marco_alerta(dias_restantes):
    """
    Envia alerta somente nos marcos exatos:
    60, 50, 40, 30, 20, 10 e 0 dias.

    Exemplo:
    - 60 dias: envia
    - 57 dias: não envia
    - 50 dias: envia
    """

    if dias_restantes in MARCOS_ALERTA:
        return dias_restantes

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
            f"Dias restantes: {alerta['Dias_Restantes']} | "
            f"Marco: {alerta['Marco_Alerta']} dias"
        )

    linhas.append("")
    linhas.append("Mensagem gerada automaticamente pelo sistema FOS Engenharia.")
    linhas.append("Favor avaliar o agendamento das férias.")

    return "\n".join(linhas)


def validar_variaveis_ambiente():
    variaveis = [
        "GITHUB_TOKEN",
        "REPO",
        "EMAIL_DESTINO_ALERTAS",
        "EMAIL_SMTP_HOST",
        "EMAIL_SMTP_PORT",
        "EMAIL_USUARIO",
        "EMAIL_SENHA",
        "EMAIL_ORIGEM",
    ]

    faltando = []

    for var in variaveis:
        if not os.environ.get(var):
            faltando.append(var)

    if faltando:
        raise RuntimeError(
            "Variáveis de ambiente ausentes: " + ", ".join(faltando)
        )


def main():
    print("==================================================")
    print("INICIANDO ROTINA DE ALERTAS DE FÉRIAS")
    print("==================================================")

    validar_variaveis_ambiente()

    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ["REPO"]
    email_destino = os.environ["EMAIL_DESTINO_ALERTAS"]

    hoje = date.today()

    print(f"Data da execução: {hoje.strftime('%d/%m/%Y')}")
    print(f"Arquivo férias: {ARQ_FERIAS}")
    print(f"Arquivo histórico: {ARQ_HISTORICO}")
    print(f"E-mail destino: {email_destino}")
    print("--------------------------------------------------")

    df_ferias = carregar_github(ARQ_FERIAS, token, repo)
    df_historico = carregar_github(ARQ_HISTORICO, token, repo)
    df_historico = normalizar_historico(df_historico)

    if df_ferias is None or df_ferias.empty:
        print("Nenhum registro de férias encontrado.")
        return

    print(f"Total de registros em férias: {len(df_ferias)}")
    print(f"Total de alertas no histórico: {len(df_historico)}")
    print("--------------------------------------------------")

    alertas_para_enviar = []
    novos_historicos = []

    ids_ja_enviados = set(df_historico["ID_Alerta"].astype(str).tolist())

    for idx, linha in df_ferias.iterrows():
        matricula = str(linha.get("Matricula", "")).strip()
        funcionario = str(linha.get("Funcionario", "")).strip()

        print(f"Analisando linha {idx}: {funcionario} | Matrícula: {matricula}")

        if ferias_ja_marcadas(linha):
            print(" - Ignorado: férias já possuem gozo marcado.")
            continue

        limite_gozo = para_data(linha.get("Limite_Gozo"))

        if limite_gozo is None:
            print(" - Ignorado: Limite_Gozo vazio ou inválido.")
            continue

        dias_restantes = (limite_gozo - hoje).days

        print(f" - Limite gozo: {limite_gozo.strftime('%d/%m/%Y')}")
        print(f" - Dias restantes: {dias_restantes}")

        if dias_restantes < 0:
            print(" - Ignorado: férias já passaram do limite.")
            continue

        if dias_restantes > 60:
            print(" - Ignorado: ainda faltam mais de 60 dias.")
            continue

        marco = definir_marco_alerta(dias_restantes)

        if marco is None:
            print(" - Ignorado: não está em um marco exato de alerta.")
            continue

        id_alerta = montar_id_alerta(
            matricula=matricula,
            limite_gozo=limite_gozo.isoformat(),
            marco=marco,
        )

        if id_alerta in ids_ja_enviados:
            print(f" - Ignorado: alerta já enviado anteriormente. ID: {id_alerta}")
            continue

        alerta = {
            "ID_Alerta": id_alerta,
            "Matricula": matricula,
            "Funcionario": funcionario,
            "Unidade": str(linha.get("Unidade", "")).strip(),
            "Departamento": str(linha.get("Departamento", "")).strip(),
            "Limite_Gozo": limite_gozo.isoformat(),
            "Limite_Gozo_BR": limite_gozo.strftime("%d/%m/%Y"),
            "Dias_Restantes": dias_restantes,
            "Marco_Alerta": marco,
        }

        alertas_para_enviar.append(alerta)

        novos_historicos.append(
            {
                "ID_Alerta": id_alerta,
                "Matricula": matricula,
                "Funcionario": funcionario,
                "Limite_Gozo": limite_gozo.isoformat(),
                "Dias_Restantes": dias_restantes,
                "Marco_Alerta": marco,
                "Email_Destino": email_destino,
                "Data_Envio": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

        print(f" - ALERTA GERADO: marco {marco} dias.")

    print("--------------------------------------------------")
    print(f"Total de alertas novos encontrados: {len(alertas_para_enviar)}")

    if not alertas_para_enviar:
        print("Nenhum alerta novo para enviar.")
        print("Rotina finalizada sem envio de e-mail.")
        return

    corpo = montar_corpo_email(alertas_para_enviar)

    print("--------------------------------------------------")
    print("Corpo do e-mail:")
    print(corpo)
    print("--------------------------------------------------")

    print("Enviando e-mail SMTP...")

    enviar_email_smtp(
        smtp_host=os.environ["EMAIL_SMTP_HOST"],
        smtp_port=int(os.environ["EMAIL_SMTP_PORT"]),
        smtp_usuario=os.environ["EMAIL_USUARIO"],
        smtp_senha=os.environ["EMAIL_SENHA"],
        email_origem=os.environ["EMAIL_ORIGEM"],
        email_destino=email_destino,
        assunto="Alerta automático de férias - FOS Engenharia",
        corpo=corpo,
    )

    print("E-mail enviado com sucesso.")

    df_novos = pd.DataFrame(novos_historicos)
    df_historico = pd.concat([df_historico, df_novos], ignore_index=True)
    df_historico = normalizar_historico(df_historico)

    salvar_github(df_historico, ARQ_HISTORICO, token, repo)

    print("Histórico de alertas atualizado com sucesso.")
    print(f"{len(alertas_para_enviar)} alerta(s) enviado(s) com sucesso.")
    print("==================================================")
    print("ROTINA FINALIZADA")
    print("==================================================")


if __name__ == "__main__":
    main()
