from datetime import date, datetime, timedelta

import pandas as pd


DIAS_ALERTA_FERIAS = 60

ESTADOS_ATIVOS = ("pendente", "programada", "em_gozo")
ESTADOS_HISTORICOS = ("concluida", "cancelada")
TRANSICOES_PERMITIDAS = {
    "pendente": ("programada", "cancelada"),
    "programada": ("em_gozo", "cancelada"),
    "em_gozo": ("concluida",),
    "concluida": (),
    "cancelada": (),
}

COLUNAS_CICLO_VIDA = [
    "Estado_Ciclo",
    "Data_Prevista_Inicio",
    "Data_Efetiva_Inicio",
    "Data_Prevista_Termino",
    "Data_Efetiva_Termino",
    "Confirmado_Inicio_Por",
    "Confirmado_Inicio_Em",
    "Confirmado_Termino_Por",
    "Confirmado_Termino_Em",
    "Cancelado_Por",
    "Cancelado_Em",
]


class TransicaoCicloInvalida(ValueError):
    pass


class TransicaoNaoAutorizada(PermissionError):
    pass


def _texto(valor):
    if valor is None or pd.isna(valor):
        return ""
    return str(valor).strip()


def normalizar_ciclo_vida_dataframe(
    df,
    *,
    coluna_inicio,
    coluna_termino,
    hoje=None,
):
    """Adiciona o contrato de ciclo de vida sem exigir migração prévia do CSV."""
    resultado = df.copy()
    hoje = hoje or date.today()

    for coluna in COLUNAS_CICLO_VIDA:
        if coluna not in resultado.columns:
            resultado[coluna] = ""

    for indice, linha in resultado.iterrows():
        inicio = para_data(linha.get(coluna_inicio))
        termino = para_data(linha.get(coluna_termino))

        if not _texto(linha.get("Data_Prevista_Inicio")) and inicio:
            resultado.at[indice, "Data_Prevista_Inicio"] = inicio.isoformat()
        if not _texto(linha.get("Data_Prevista_Termino")) and termino:
            resultado.at[indice, "Data_Prevista_Termino"] = termino.isoformat()

        estado = _texto(linha.get("Estado_Ciclo")).lower()
        if estado not in TRANSICOES_PERMITIDAS:
            # Compatibilidade: períodos legados já terminados entram no histórico;
            # os demais continuam exigindo confirmação operacional explícita.
            if termino and termino < hoje:
                estado = "concluida"
            elif inicio:
                estado = "programada"
            else:
                estado = "pendente"
            resultado.at[indice, "Estado_Ciclo"] = estado

    return resultado


def separar_operacao_historico(df):
    estados = df.get("Estado_Ciclo", pd.Series("pendente", index=df.index))
    estados = estados.fillna("").astype(str).str.strip().str.lower()
    operacao = df[estados.isin(ESTADOS_ATIVOS)].copy()
    historico = df[estados.isin(ESTADOS_HISTORICOS)].copy()
    return operacao, historico


def transicionar_ciclo_vida(
    registro,
    novo_estado,
    *,
    usuario,
    autorizado,
    agora=None,
    data_efetiva=None,
):
    """Valida autorização e transição antes de produzir uma cópia auditada."""
    if not autorizado:
        raise TransicaoNaoAutorizada("Usuário sem permissão para alterar o ciclo de vida.")

    atual = _texto(registro.get("Estado_Ciclo")).lower() or "pendente"
    destino = _texto(novo_estado).lower()
    permitidos = TRANSICOES_PERMITIDAS.get(atual, ())
    if destino not in permitidos:
        raise TransicaoCicloInvalida(
            f"Transição inválida: {atual} → {destino}."
        )

    usuario = _texto(usuario)
    if not usuario:
        raise TransicaoCicloInvalida("Não foi possível identificar o usuário responsável.")

    agora = agora or datetime.now()
    efetiva = para_data(data_efetiva) or agora.date()
    resultado = registro.copy()
    resultado["Estado_Ciclo"] = destino

    if destino == "em_gozo":
        resultado["Data_Efetiva_Inicio"] = efetiva.isoformat()
        resultado["Confirmado_Inicio_Por"] = usuario
        resultado["Confirmado_Inicio_Em"] = agora.isoformat(timespec="seconds")
    elif destino == "concluida":
        resultado["Data_Efetiva_Termino"] = efetiva.isoformat()
        resultado["Confirmado_Termino_Por"] = usuario
        resultado["Confirmado_Termino_Em"] = agora.isoformat(timespec="seconds")
    elif destino == "cancelada":
        resultado["Cancelado_Por"] = usuario
        resultado["Cancelado_Em"] = agora.isoformat(timespec="seconds")

    return resultado


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
