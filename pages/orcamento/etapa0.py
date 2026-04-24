import streamlit as st
import pandas as pd
from datetime import datetime
from services.github import carregar_github, salvar_github

# =========================
# ARQUIVOS
# =========================
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
        df_ano = df[df["Codigo"].str.contains(str(ano), na=False)]

        if df_ano.empty:
            seq = 1
        else:
            ult = df_ano["Codigo"].iloc[-1]
            seq = int(ult.split("_")[1]) + 1

    return f"D_{seq:03d}_{ano}"

# =========================
# ETAPA 0
# =========================
def etapa0():

    st.header("Informações da Obra")

    codigo = gerar_codigo()

    # =========================
    # CLIENTES
    # =========================
    df_clientes = carregar_github(ARQ_CLIENTES, TOKEN, REPO)
    if df_clientes.empty:
        df_clientes = pd.DataFrame(columns=["Cliente"])

    cliente = st.selectbox("Cliente", df_clientes["Cliente"])
    novo_cliente = st.text_input("Ou adicionar novo cliente")

    # =========================
    # DADOS BÁSICOS
    # =========================
    nome_obra = st.text_input("Nome da obra")
    local = st.text_input("Local de execução")

    data = st.date_input("Data", value=datetime.now())
    st.write(f"Data selecionada: {data.strftime('%d/%m/%Y')}")

    st.info(f"Código: {codigo}")

    # =========================
    # BASES
    # =========================
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)
    df_desag = carregar_github(ARQ_DESAG, TOKEN, REPO)
    df_med = carregar_github("data/medicao.csv", TOKEN, REPO)
    df_hor = carregar_github("data/horarios.csv", TOKEN, REPO)
    df_dias = carregar_github("data/dias.csv", TOKEN, REPO)

    # =========================
    # NOVOS CAMPOS (IMPORTANTE)
    # =========================
    volume = st.number_input("Volume a ser dragado (m³)")

    material = st.selectbox("Tipo de material", df_mat["Material"])

    desag = st.selectbox("Tipo de desaguamento", df_desag["Tipo"])

    col1, col2 = st.columns(2)
    flutuante = col1.number_input("Distância flutuante (m)")
    terrestre = col2.number_input("Distância terrestre (m)")

    sistema_med = st.selectbox("Sistema de medição", df_med["Sistema"])

    horario = st.selectbox(
        "Horário de trabalho",
        df_hor.apply(lambda x: f"{x['Inicio']} - {x['Fim']}", axis=1)
    )

    dias = st.selectbox("Dias de trabalho", df_dias["Descricao"])

    # =========================
    # SALVAR
    # =========================
    if st.button("Continuar", key="cont_etapa0"):

        # Cliente novo
        if novo_cliente:
            cliente_final = novo_cliente
            df_clientes.loc[len(df_clientes)] = [novo_cliente]
            salvar_github(df_clientes, ARQ_CLIENTES, TOKEN, REPO)
        else:
            cliente_final = cliente

        st.session_state.orcamento = {
            "codigo": codigo,
            "nome_obra": nome_obra,
            "cliente": cliente_final,
            "data": data.strftime("%d/%m/%Y"),
            "local": local,
            "volume": volume,
            "material": material,
            "desag": desag,
            "flutuante": flutuante,
            "terrestre": terrestre,
            "medicao": sistema_med,
            "horario": horario,
            "dias": dias
        }

        st.session_state.tela = "orcamento1"
        st.rerun()
