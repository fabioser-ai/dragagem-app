from datetime import datetime
import re

def gerar_codigo_obra(df):

    ano = datetime.now().year

    if df.empty:
        return f"D_001_{ano}"

    numeros = []

    for val in df["Codigo"]:
        match = re.search(r"D_(\d+)_", str(val))
        if match:
            numeros.append(int(match.group(1)))

    proximo = max(numeros) + 1 if numeros else 1

    return f"D_{str(proximo).zfill(3)}_{ano}"
