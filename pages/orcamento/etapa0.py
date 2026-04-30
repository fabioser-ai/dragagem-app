import streamlit as st
import pandas as pd
from datetime import datetime
from services.github import carregar_github, salvar_github

ARQ_CLIENTES = "data/clientes.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"
ARQ_OBRAS = "data/orcamentos.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# GERAR CÓDIGO
# =========================
def gerar_codigo():

    try:
        df = carregar_github(ARQ_OBRAS, TOKEN, REPO)
    except:
        df = pd.DataFrame()

    ano = datetime.now().year

    if df.empty or "Codigo" not in df.columns:
        seq = 1
    else:
        df_ano = df[df["Codigo"].astype(str).str.contains(str(ano), na=False)]

        if df_ano.empty:
            seq = 1
        else:
            ult = df_ano["Codigo"].iloc[-1]
            seq = int(str(ult).split("_")[1]) + 1

    return f"D_{seq:03d}_{ano}"

# =========================
# SALVAR RASCUNHO
# =========================
def salvar_rascunho(dados):

    try:
        df = carregar_github(ARQ_OBRAS, TOKEN, REPO)
    except:
        df = pd.DataFrame()

    if df.empty:
        df = pd.DataFrame()

    codigo = dados["Codigo"]

    if "Codigo" in df.columns and codigo in df["Codigo"].values:
        idx = df[df["Codigo"] == codigo].index[0]
        for k, v in dados.items():
            df.loc[idx, k] = v
    else:
        df = pd.concat([df, pd.DataFrame([dados])], ignore_index=True)

    salvar_github(df, ARQ_OBRAS, TOKEN, REPO)

# =========================
# ETAPA 0
# =========================
def etapa0():

    st.header("Informações da Obra")

    if st.button("⬅ Voltar ao início"):
        st.session_state.tela = "menu"
        st.rerun()

    # =========================
    # DEFINE ORÇAMENTO
    # =========================
    if "orcamento" in st.session_state:
        dados_existentes = st.session_state.orcamento
        codigo = dados_existentes.get("Codigo") or dados_existentes.get("codigo")
    else:
        codigo = gerar_codigo()
        dados_existentes = {}

    st.info(f"Código: {codigo}")

    # =========================
    # CLIENTES
    # =========================
    df_clientes = carregar_github(ARQ_CLIENTES, TOKEN, REPO)
    if df_clientes.empty:
        df_clientes = pd.DataFrame(columns=["Cliente"])

    cliente_default = dados_existentes.get("Cliente", "")

    cliente = st.selectbox(
        "Cliente",
        df_clientes["Cliente"],
        index=df_clientes["Cliente"].tolist().index(cliente_default)
        if cliente_default in df_clientes["Cliente"].tolist()
        else 0
    )

    novo_cliente = st.text_input("Ou adicionar novo cliente")

    # =========================
    # CAMPOS
    # =========================
    nome_obra = st.text_input(
        "Nome da obra",
        value=dados_existentes.get("Nome_Obra", "")
    )

    local = st.text_input(
        "Local de execução",
        value=dados_existentes.get("Local", "")
    )

    data_val = dados_existentes.get("Data", datetime.now().strftime("%d/%m/%Y"))

    data = st.date_input(
        "Data",
        value=datetime.strptime(data_val, "%d/%m/%Y"),
        format="DD/MM/YYYY"
    )

    # =========================
    # BASES
    # =========================
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)
    df_desag = carregar_github(ARQ_DESAG, TOKEN, REPO)
    df_med = carregar_github("data/medicao.csv", TOKEN, REPO)
    df_hor = carregar_github("data/horarios.csv", TOKEN, REPO)
    df_dias = carregar_github("data/dias.csv", TOKEN, REPO)

    volume = st.number_input(
        "Volume a ser dragado (m³)",
        value=float(dados_existentes.get("Volume", 0))
    )

    material = st.selectbox(
        "Tipo de material",
        df_mat["Material"],
        index=df_mat["Material"].tolist().index(dados_existentes.get("Material"))
        if dados_existentes.get("Material") in df_mat["Material"].tolist()
        else 0
    )

    desag = st.selectbox(
        "Tipo de desaguamento",
        df_desag["Tipo"],
        index=df_desag["Tipo"].tolist().index(dados_existentes.get("Desag"))
        if dados_existentes.get("Desag") in df_desag["Tipo"].tolist()
        else 0
    )

    col1, col2 = st.columns(2)

    flutuante = col1.number_input(
        "Distância de recalque - Flutuante (m)",
        value=float(dados_existentes.get("Flutuante", 0))
    )

    terrestre = col2.number_input(
        "Distância de recalque - Terrestre (m)",
        value=float(dados_existentes.get("Terrestre", 0))
    )

    desnivel = st.number_input(
        "Desnível de Bombeamento (m)",
        value=float(dados_existentes.get("Desnivel_Bombeamento", 0))
    )

    sistema_med = st.selectbox(
        "Sistema de medição",
        df_med["Sistema"],
        index=df_med["Sistema"].tolist().index(dados_existentes.get("Medicao"))
        if dados_existentes.get("Medicao") in df_med["Sistema"].tolist()
        else 0
    )

    horario = st.selectbox(
        "Horário de trabalho",
        df_hor.apply(lambda x: f"{x['Inicio']} - {x['Fim']}", axis=1),
        index=0
    )

    dias = st.selectbox(
        "Dias de trabalho",
        df_dias["Descricao"],
        index=df_dias["Descricao"].tolist().index(dados_existentes.get("Dias"))
        if dados_existentes.get("Dias") in df_dias["Descricao"].tolist()
        else 0
    )

    # =========================
    # SALVAR
    # =========================
    if st.button("Continuar"):

        if novo_cliente:
            cliente_final = novo_cliente
            df_clientes.loc[len(df_clientes)] = [novo_cliente]
            salvar_github(df_clientes, ARQ_CLIENTES, TOKEN, REPO)
        else:
            cliente_final = cliente

        dados = {
            "Codigo": codigo,
            "Status": "Rascunho",
            "Etapa_Atual": "Etapa 0",
            "Data_Criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Ultima_Atualizacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Cliente": cliente_final,
            "Nome_Obra": nome_obra,
            "Local": local,
            "Data": data.strftime("%d/%m/%Y"),
            "Volume": volume,
            "Material": material,
            "Desag": desag,
            "Flutuante": flutuante,
            "Terrestre": terrestre,
            "Desnivel_Bombeamento": desnivel,
            "Medicao": sistema_med,
            "Horario": horario,
            "Dias": dias,
        }

        salvar_rascunho(dados)

        st.session_state.orcamento = dados
        st.session_state.tela = "orcamento1"
        st.rerun()
