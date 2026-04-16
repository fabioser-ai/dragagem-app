import requests
import base64
import pandas as pd
from io import StringIO

# =========================
# SALVAR NO GITHUB
# =========================
def salvar_github(df, arquivo, token, repo):

    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)

    sha = response.json().get("sha") if response.status_code == 200 else None

    csv_string = df.to_csv(index=False)
    content = base64.b64encode(csv_string.encode()).decode()

    data = {
        "message": f"Update {arquivo}",
        "content": content
    }

    if sha:
        data["sha"] = sha

    requests.put(url, headers=headers, json=data)


# =========================
# CARREGAR DO GITHUB
# =========================
def carregar_github(arquivo, token, repo):

    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return pd.DataFrame()

    content = response.json()["content"]
    decoded = base64.b64decode(content).decode()

    return pd.read_csv(StringIO(decoded))
