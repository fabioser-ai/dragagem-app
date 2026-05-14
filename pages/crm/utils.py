import uuid
from datetime import datetime
import pandas as pd


def gerar_id() -> str:
    return str(uuid.uuid4())


def agora_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def data_hoje() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def normalizar_texto(valor) -> str:
    if pd.isna(valor):
        return ""
    return str(valor).strip()


def dataframe_vazio(colunas: list[str]) -> pd.DataFrame:
    return pd.DataFrame(columns=colunas)


def preparar_dataframe_para_exibicao(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    df = df.copy()

    for coluna in df.columns:
        df[coluna] = df[coluna].fillna("").astype(str)

    return df


def filtrar_dataframe(df: pd.DataFrame, termo_busca: str, colunas_busca: list[str]) -> pd.DataFrame:
    if df.empty or not termo_busca:
        return df

    termo = termo_busca.lower().strip()

    mascara = pd.Series(False, index=df.index)

    for coluna in colunas_busca:
        if coluna in df.columns:
            mascara = mascara | df[coluna].fillna("").astype(str).str.lower().str.contains(termo, na=False)

    return df[mascara]
