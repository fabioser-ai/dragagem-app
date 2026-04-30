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

    # Atualizar ou criar
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

    # Se já existe orçamento em andamento, reutiliza
    if "orcamento" not in st.session_state:
        codigo = gerar_codigo()
        st.session_state.orcamento = {"codigo": codigo}
    else:
        codigo = st.session_state.orcamento["codigo"]

    # =========================
    # CLIENTES
    # =========================
    df_clientes = carregar_github(ARQ_CLIENTES, TOKEN, REPO)
    if df_clientes.empty:
        df_clientes = pd.DataFrame(columns=["Cliente"])

    cliente = st.selectbox("Cliente", df_clientes["Cliente"])
    novo_cliente = st.text_input("Ou adicionar novo cliente")

    # =========================
    # DADOS
    # =========================
    nome_obra = st.text_input("Nome da obra")
    local = st.text_input("Local de execução")

    data = st.date_input(
        "Data",
        value=datetime.now(),
        format="DD/MM/YYYY"
    )

    st.info(f"Código: {codigo}")

    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)
    df_desag = carregar_github(ARQ_DESAG, TOKEN, REPO)
    df_med = carregar_github("data/medicao.csv", TOKEN, REPO)
    df_hor = carregar_github("data/horarios.csv", TOKEN, REPO)
    df_dias = carregar_github("data/dias.csv", TOKEN, REPO)

    volume = st.number_input("Volume a ser dragado (m³)")
    material = st.selectbox("Tipo de material", df_mat["Material"])
    desag = st.selectbox("Tipo de desaguamento", df_desag["Tipo"])

    col1, col2 = st.columns(2)
    flutuante = col1.number_input("Distância de recalque - Flutuante (m)")
    terrestre = col2.number_input("Distância de recalque - Terrestre (m)")

    desnivel = st.number_input("Desnível de Bombeamento (m)")

    sistema_med = st.selectbox("Sistema de medição", df_med["Sistema"])

    horario = st.selectbox(
        "Horário de trabalho",
        df_hor.apply(lambda x: f"{x['Inicio']} - {x['Fim']}", axis=1)
    )

    dias = st.selectbox("Dias de trabalho", df_dias["Descricao"])

    # =========================
    # CONTINUAR
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

        st.session_state.orcamento.update(dados)

        st.session_state.tela = "orcamento1"
        st.rerun()
