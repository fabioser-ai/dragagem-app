from datetime import date, timedelta

import pandas as pd


DIAS_ALERTA_FERIAS = 60


def para_data(valor):
    data = pd.to_datetime(valor, errors="coerce")
    if pd.isna(data):
        return None
    return data.date()


def calcular_status_ferias(
    periodo_fim,
    limite_gozo,
    *,
    hoje=None,
    dias_alerta=DIAS_ALERTA_FERIAS,
):
    """Calcula o status vigente sem depender do texto persistido no CSV."""
    hoje = hoje or date.today()
    periodo_fim = para_data(periodo_fim)
    limite_gozo = para_data(limite_gozo)

    if periodo_fim is None:
        return "Indefinido", "Indefinido"

    if limite_gozo is None:
        limite_gozo = periodo_fim + timedelta(days=335)

    situacao_ferias = (
        "Férias Vencidas"
        if hoje >= periodo_fim
        else "Férias Não Vencidas"
    )

    if hoje > limite_gozo:
        situacao_prazo = "Férias em Dobro"
    elif 0 <= (limite_gozo - hoje).days <= dias_alerta:
        situacao_prazo = "Atenção"
    else:
        situacao_prazo = "Dentro do Prazo"

    return situacao_ferias, situacao_prazo


def recalcular_status_dataframe(df, *, hoje=None):
    """Retorna cópia com os status derivados novamente das datas vigentes."""
    if df.empty:
        return df.copy()

    resultado = df.copy()

    status = resultado.apply(
        lambda linha: calcular_status_ferias(
            linha.get("Periodo_Aquisitivo_Fim"),
            linha.get("Limite_Gozo"),
            hoje=hoje,
        ),
        axis=1,
    )

    resultado["Situacao_Ferias"] = status.apply(lambda valor: valor[0])
    resultado["Situacao_Prazo"] = status.apply(lambda valor: valor[1])
    return resultado


def validar_registro_ferias(
    df,
    *,
    matricula,
    funcionario,
    periodo_inicio,
    periodo_fim,
    inicio_gozo=None,
    fim_gozo=None,
    ignorar_indice=None,
):
    """Valida identidade mínima e coerência cronológica do registro."""
    erros = []
    matricula_normalizada = str(matricula or "").strip()
    funcionario_normalizado = str(funcionario or "").strip()

    if not matricula_normalizada:
        erros.append("Informe a matrícula do funcionário.")

    if not funcionario_normalizado:
        erros.append("Informe o nome do funcionário.")

    if matricula_normalizada and not df.empty and "Matricula" in df.columns:
        candidatos = df
        if ignorar_indice is not None and ignorar_indice in candidatos.index:
            candidatos = candidatos.drop(index=ignorar_indice)

        matriculas = candidatos["Matricula"].fillna("").astype(str).str.strip()
        if matriculas.eq(matricula_normalizada).any():
            erros.append("Já existe um funcionário cadastrado com esta matrícula.")

    inicio_aquisitivo = para_data(periodo_inicio)
    fim_aquisitivo = para_data(periodo_fim)
    inicio_gozo = para_data(inicio_gozo)
    fim_gozo = para_data(fim_gozo)

    if inicio_aquisitivo and fim_aquisitivo and fim_aquisitivo < inicio_aquisitivo:
        erros.append("O fim do período aquisitivo não pode ser anterior ao início.")

    if bool(inicio_gozo) != bool(fim_gozo):
        erros.append("Informe conjuntamente o início e o fim do gozo.")

    if inicio_gozo and fim_gozo and fim_gozo < inicio_gozo:
        erros.append("O fim do gozo não pode ser anterior ao início.")

    return erros
