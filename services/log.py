import pandas as pd
from datetime import datetime
import os

ARQUIVO_LOG = "data/log_acessos.csv"


def registrar_log(usuario, perfil, acao):
    registro = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario": usuario,
        "perfil": perfil,
        "acao": acao,
    }

    df_novo = pd.DataFrame([registro])

    if os.path.exists(ARQUIVO_LOG):
        df = pd.read_csv(ARQUIVO_LOG)
        df = pd.concat([df, df_novo], ignore_index=True)
    else:
        df = df_novo

    df.to_csv(ARQUIVO_LOG, index=False)
