import streamlit as st
import pandas as pd
import os
import requests
import base64
from datetime import datetime
import re

st.title("FOS ENGENHARIA LTDA")

# =========================
# ESTADO
# =========================
if "etapa" not in st.session_state:
    st.session_state.etapa = 0

if "equipamento_sel" not in st.session_state:
    st.session_state.equipamento_sel = None

if "codigo_obra" not in st.session_state:
    st.session_state.codigo_obra = None

# =========================
# ARQUIVOS
# =========================
ARQUIVO_FERIAS = "ferias.csv"
ARQUIVO_EQUIP = "equipamentos.csv"
ARQUIVO_ORC = "orcamentos.csv"

# =========================
# GITHUB SAVE
# =========================
def salvar_github(df, arquivo):

    token = st.secrets["GITHUB_TOKEN"]
    repo = st.secrets["REPO"]

    url = f"https://api.github.com/repos/{repo}/contents/{arquivo}"

    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        sha = response.json()["sha"]
    else:
        sha = None

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
# GERADOR DE CÓDIGO OBRA
# =========================
def gerar_codigo_obra(df):

    ano = datetime.now().year

    if df.empty:
        return f"D_001_{ano}"

    padrao = r"D_(\d+)_"

    numeros = []

    for val in df["Codigo"]:
        match = re.search(padrao, str(val))
        if match:
            numeros.append(int(match.group(1)))

    proximo = max(numeros) + 1 if numeros else 1

    return f"D_{str(proximo).zfill(3)}_{ano}"

# =========================
# CRIAÇÃO DE ARQUIVOS
# =========================
if not os.path.exists(ARQUIVO_FERIAS):
    pd.DataFrame(columns=["Nome", "Data"]).to_csv(ARQUIVO_FERIAS, index=False)

if not os.path.exists(ARQUIVO_EQUIP):
    pd.DataFrame(columns=["Equipamento", "Vazao", "Consumo", "Valor"]).to_csv(ARQUIVO_EQUIP, index=False)

if not os.path.exists(ARQUIVO_ORC):
    pd.DataFrame(columns=[
        "Codigo",
        "Data",
        "Tipo",
        "Equipamento",
        "Volume",
        "Distancia",
        "Produtividade",
        "Tempo_h",
        "Dias",
        "Custo_Diesel",
        "Receita",
        "Lucro"
    ]).to_csv(ARQUIVO_ORC, index=False)

# =========================
# MENU PRINCIPAL
# =========================
if st.session_state.etapa == 0:

    st.header("Menu Principal")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("📊 Orçamento"):
        st.session_state.etapa = 1

    if col2.button("⚙️ Base de Dados"):
        st.session_state.etapa = 100

    if col3.button("📅 Férias"):
        st.session_state.etapa = 200

    if col4.button("🚜 Equipamentos"):
        st.session_state.etapa = 300

# =========================
# BASE DE DADOS
# =========================
elif st.session_state.etapa == 100:

    st.header("Base de Dados")

    diesel = st.number_input("Preço Diesel (R$/L)", value=6.0)
    operador = st.number_input("Operador (R$/h)", value=23.0)
    ajudante = st.number_input("Ajudante (R$/h)", value=11.0)
    qtd_ajudantes = st.number_input("Qtd ajudantes", value=2)

    if st.button("Salvar"):
        st.session_state.base = {
            "diesel": diesel,
            "operador": operador,
            "ajudante": ajudante,
            "qtd_ajudantes": qtd_ajudantes
        }
        st.success("Salvo!")

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# FÉRIAS
# =========================
elif st.session_state.etapa == 200:

    st.header("Férias")

    nome = st.text_input("Nome")
    data = st.date_input("Data")

    if st.button("Salvar"):
        df = pd.read_csv(ARQUIVO_FERIAS)
        novo = pd.DataFrame([[nome, data]], columns=["Nome", "Data"])
        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_FERIAS)

        st.success("Salvo!")
        st.rerun()

    st.dataframe(pd.read_csv(ARQUIVO_FERIAS))

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# EQUIPAMENTOS
# =========================
elif st.session_state.etapa == 300:

    st.header("Equipamentos")

    df = pd.read_csv(ARQUIVO_EQUIP)
    st.dataframe(df)

    if st.button("🔄 Atualizar"):
        st.rerun()

    st.divider()

    if not df.empty:

        sel = st.selectbox("Selecionar", df["Equipamento"])
        linha = df[df["Equipamento"] == sel].iloc[0]

        nome = st.text_input("Nome", value=linha["Equipamento"])
        vazao = st.number_input("Vazão (m³/h)", value=float(linha["Vazao"]))
        consumo = st.number_input("Consumo (L/h)", value=float(linha["Consumo"]))
        valor = st.number_input("Valor (R$)", value=float(linha["Valor"]))

        col1, col2 = st.columns(2)

        if col1.button("Salvar"):
            idx = df["Equipamento"] == sel

            df.loc[idx, "Equipamento"] = nome
            df.loc[idx, "Vazao"] = vazao
            df.loc[idx, "Consumo"] = consumo
            df.loc[idx, "Valor"] = valor

            salvar_github(df, ARQUIVO_EQUIP)

            st.success("Atualizado!")
            st.rerun()

        if col2.button("Excluir"):
            df = df[df["Equipamento"] != sel]

            salvar_github(df, ARQUIVO_EQUIP)

            st.warning("Removido!")
            st.rerun()

    st.divider()

    st.subheader("Novo equipamento")

    nome_n = st.text_input("Nome novo")
    vazao_n = st.number_input("Vazão nova", value=1000.0)
    consumo_n = st.number_input("Consumo novo", value=60.0)
    valor_n = st.number_input("Valor novo", value=1000000.0)

    if st.button("Adicionar"):
        novo = pd.DataFrame([[nome_n, vazao_n, consumo_n, valor_n]],
                            columns=["Equipamento", "Vazao", "Consumo", "Valor"])

        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_EQUIP)

        st.success("Adicionado!")
        st.rerun()

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# ORÇAMENTO - ETAPA 1
# =========================
elif st.session_state.etapa == 1:

    st.header("Selecionar Equipamento")

    df = pd.read_csv(ARQUIVO_EQUIP)

    equipamento = st.selectbox("Equipamento", df["Equipamento"])
    eq = df[df["Equipamento"] == equipamento].iloc[0]

    st.write(f"Vazão: {eq['Vazao']} m³/h")
    st.write(f"Consumo: {eq['Consumo']} L/h")
    st.write(f"Valor: R$ {eq['Valor']:,.2f}")

    if st.button("Continuar"):
        st.session_state.equipamento_sel = equipamento
        st.session_state.etapa = 2

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# ORÇAMENTO - ETAPA 2
# =========================
elif st.session_state.etapa == 2:

    st.header("Parâmetros da Obra")

    df = pd.read_csv(ARQUIVO_EQUIP)
    equipamento = st.session_state.equipamento_sel

    eq = df[df["Equipamento"] == equipamento].iloc[0]

    # gerar código da obra
    df_orc = pd.read_csv(ARQUIVO_ORC)
    codigo = gerar_codigo_obra(df_orc)

    st.session_state.codigo_obra = codigo

    st.info(f"📌 Código da obra: {codigo}")

    volume = st.number_input("Volume (m³)", value=10000.0)
    distancia = st.number_input("Distância (m)", value=2000.0)
    preco = st.number_input("Preço (R$/m³)", value=16.18)
    horas_dia = st.number_input("Horas/dia", value=20)

    if st.button("Calcular"):
        st.session_state.calc = {
            "volume": volume,
            "distancia": distancia,
            "preco": preco,
            "vazao": eq["Vazao"],
            "consumo": eq["Consumo"],
            "horas_dia": horas_dia,
            "equipamento": equipamento,
            "codigo": codigo
        }
        st.session_state.etapa = 3

    if st.button("Voltar"):
        st.session_state.etapa = 1

# =========================
# RESULTADO + HISTÓRICO
# =========================
elif st.session_state.etapa == 3:

    d = st.session_state.calc

    prod = d["vazao"]

    if d["distancia"] <= 1000:
        fator = 1
    elif d["distancia"] <= 3000:
        fator = 0.75
    else:
        fator = 0.55

    prod_real = prod * fator
    tempo_h = d["volume"] / prod_real
    dias = tempo_h / d["horas_dia"]

    diesel = st.session_state.get("base", {}).get("diesel", 6.0)
    custo_diesel = d["consumo"] * tempo_h * diesel

    receita = d["volume"] * d["preco"]
    lucro = receita - custo_diesel

    st.header("Resultado")

    st.write(f"📌 Código: {d['codigo']}")
    st.write(f"Equipamento: {d['equipamento']}")
    st.write(f"Produtividade: {prod_real:.2f} m³/h")
    st.write(f"Tempo: {tempo_h:.2f} h")
    st.write(f"Dias: {dias:.2f}")

    st.write(f"Custo Diesel: R$ {custo_diesel:,.2f}")
    st.write(f"Receita: R$ {receita:,.2f}")

    st.success(f"Lucro: R$ {lucro:,.2f}")

    # =========================
    # SALVAR HISTÓRICO
    # =========================
    if st.button("💾 Salvar orçamento no histórico"):

        df = pd.read_csv(ARQUIVO_ORC)

        novo = pd.DataFrame([[
            d["codigo"],
            pd.Timestamp.now(),
            st.session_state.tipo,
            d["equipamento"],
            d["volume"],
            d["distancia"],
            prod_real,
            tempo_h,
            dias,
            custo_diesel,
            receita,
            lucro
        ]], columns=df.columns)

        df = pd.concat([df, novo], ignore_index=True)

        salvar_github(df, ARQUIVO_ORC)

        st.success("Orçamento salvo no histórico!")
        st.rerun()

    if st.button("Novo orçamento"):
        st.session_state.etapa = 0
