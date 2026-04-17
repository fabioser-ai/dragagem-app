import streamlit as st
import pandas as pd
from datetime import datetime
from services.github import carregar_github, salvar_github

ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"
ARQ_CLIENTES = "data/clientes.csv"
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

    st.header("Orçamento - Identificação")

    codigo = gerar_codigo()

    # CLIENTES
    df_clientes = carregar_github(ARQ_CLIENTES, TOKEN, REPO)
    if df_clientes.empty:
        df_clientes = pd.DataFrame(columns=["Cliente"])

    lista_clientes = df_clientes["Cliente"].tolist()

    cliente = st.selectbox("Cliente", lista_clientes)
    novo_cliente = st.text_input("Ou adicionar novo cliente")

    nome_obra = st.text_input("Nome da obra")
    data = st.date_input("Data", value=datetime.now())

    st.info(f"Código gerado: {codigo}")

    if st.button("Continuar"):

        # define cliente final
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
            "data": str(data)
        }

        st.session_state.tela = "orcamento1"
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
        st.rerun()

# =========================
# ETAPA 1
# =========================
def etapa1():

    st.header("Orçamento - Etapa 1")

    df_equip = carregar_github(ARQ_EQUIP, TOKEN, REPO)
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)
    df_desag = carregar_github(ARQ_DESAG, TOKEN, REPO)

    draga = st.selectbox("Draga", df_equip["Equipamento"])
    dados = df_equip[df_equip["Equipamento"] == draga].iloc[0]

    vazao = st.number_input("Vazão", value=float(dados["Vazao"]))
    volume = st.number_input("Volume")

    material = st.selectbox("Material", df_mat["Material"])
    desag = st.selectbox("Desaguamento", df_desag["Tipo"])

    col1, col2 = st.columns(2)
    flutuante = col1.number_input("Linha flutuante")
    terrestre = col2.number_input("Linha terrestre")

    if st.button("Continuar"):

        st.session_state.orcamento.update({
            "vazao": vazao,
            "volume": volume,
            "material": material,
            "desag": desag,
            "flutuante": flutuante,
            "terrestre": terrestre
        })

        st.session_state.tela = "orcamento2"
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "orcamento"
        st.rerun()

# =========================
# ETAPA 2
# =========================
def etapa2():

    st.header("Orçamento - Produção")

    dados = st.session_state.orcamento
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)

    col1, col2 = st.columns(2)

    flutuante = col1.number_input("Linha flutuante", value=float(dados["flutuante"]))
    terrestre = col2.number_input("Linha terrestre", value=float(dados["terrestre"]))

    distancia_total = flutuante + terrestre
    st.info(f"Distância total: {distancia_total:.0f} m")

    linha = df_mat[df_mat["Material"] == dados["material"]].iloc[0]
    concentracao = float(linha["Solidos_InSitu"]) / 100

    eficiencia_map = {
        "Geobag": 0.85,
        "Centrífuga": 0.90,
        "Bombeamento direto": 0.95,
        "Bacia ecológica": 0.80
    }

    eficiencia = eficiencia_map.get(dados["desag"], 0.85)

    vazao_real = dados["vazao"] * eficiencia * concentracao

    st.subheader("Cálculo")

    st.write(f"Vazão: {dados['vazao']}")
    st.write(f"Eficiência: {eficiencia}")
    st.write(f"Concentração: {concentracao}")

    st.code(f"{dados['vazao']} × {eficiencia} × {concentracao}")

    st.success(f"Vazão real: {vazao_real:.2f} m³/h")

    st.session_state.orcamento.update({
        "flutuante": flutuante,
        "terrestre": terrestre,
        "vazao_real": vazao_real
    })

    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento1"
        st.rerun()

    if col2.button("Continuar"):
        st.success("Próxima etapa em construção")
