import streamlit as st
import pandas as pd
import os

st.title("FOS ENGENHARIA LTDA")

# =========================
# CONTROLE DE ETAPA
# =========================
if "etapa" not in st.session_state:
    st.session_state.etapa = 0

# =========================
# ARQUIVOS
# =========================
ARQUIVO_FERIAS = "ferias.csv"
ARQUIVO_EQUIP = "equipamentos.csv"

# cria arquivos se não existirem (segurança)
if not os.path.exists(ARQUIVO_FERIAS):
    pd.DataFrame(columns=["Nome", "Data"]).to_csv(ARQUIVO_FERIAS, index=False)

if not os.path.exists(ARQUIVO_EQUIP):
    pd.DataFrame(columns=["Equipamento", "Vazao", "Concentracao", "Eficiencia", "Horas_dia"]).to_csv(ARQUIVO_EQUIP, index=False)

# =========================
# ETAPA 0 - MENU
# =========================
if st.session_state.etapa == 0:

    st.header("Menu Principal")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📊 Orçamento"):
            st.session_state.etapa = 1

    with col2:
        if st.button("⚙️ Base de Dados"):
            st.session_state.etapa = 100

    with col3:
        if st.button("📅 Férias"):
            st.session_state.etapa = 200

    with col4:
        if st.button("🚜 Equipamentos"):
            st.session_state.etapa = 300

# =========================
# ETAPA 100 - BASE DE DADOS
# =========================
elif st.session_state.etapa == 100:

    st.header("Base de Dados")

    diesel = st.number_input("Preço Diesel (R$/L)", value=6.0)
    consumo = st.number_input("Consumo (L/h)", value=65.0)

    operador = st.number_input("Operador (R$/h)", value=23.0)
    ajudante = st.number_input("Ajudante (R$/h)", value=11.0)
    qtd_ajudantes = st.number_input("Qtd ajudantes", value=2)

    vazao = st.number_input("Vazão padrão", value=850.0)
    concentracao = st.number_input("Concentração (%)", value=15.0)

    if st.button("Salvar"):
        st.session_state.base_dados = {
            "diesel": diesel,
            "consumo": consumo,
            "operador": operador,
            "ajudante": ajudante,
            "qtd_ajudantes": qtd_ajudantes,
            "vazao": vazao,
            "concentracao": concentracao / 100
        }
        st.success("Salvo!")

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# ETAPA 200 - FÉRIAS
# =========================
elif st.session_state.etapa == 200:

    st.header("Férias / Folgas")

    nome = st.text_input("Nome")
    data = st.date_input("Data")

    if st.button("Salvar"):
        df = pd.read_csv(ARQUIVO_FERIAS)
        novo = pd.DataFrame([[nome, data]], columns=["Nome", "Data"])
        df = pd.concat([df, novo], ignore_index=True)
        df.to_csv(ARQUIVO_FERIAS, index=False)
        st.success("Salvo!")

    st.subheader("Histórico")
    st.dataframe(pd.read_csv(ARQUIVO_FERIAS))

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# ETAPA 300 - EQUIPAMENTOS
# =========================
elif st.session_state.etapa == 300:

    st.header("Equipamentos")

    df = pd.read_csv(ARQUIVO_EQUIP)

    st.subheader("Lista")
    st.dataframe(df)

    st.subheader("Adicionar novo")

    nome = st.text_input("Nome equipamento")
    vazao = st.number_input("Vazão (m³/h)", value=1000.0)
    concentracao = st.number_input("Concentração (%)", value=15.0)
    eficiencia = st.number_input("Eficiência (%)", value=70.0)
    horas_dia = st.number_input("Horas/dia", value=20)

    if st.button("Adicionar"):
        novo = pd.DataFrame([[
            nome,
            vazao,
            concentracao / 100,
            eficiencia / 100,
            horas_dia
        ]], columns=["Equipamento", "Vazao", "Concentracao", "Eficiencia", "Horas_dia"])

        df = pd.concat([df, novo], ignore_index=True)
        df.to_csv(ARQUIVO_EQUIP, index=False)

        st.success("Equipamento adicionado!")

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# ETAPA 1 - TIPO OPERAÇÃO
# =========================
elif st.session_state.etapa == 1:

    st.header("Tipo de Operação")

    tipo = st.selectbox("Escolha", [
        "Bombeamento direto",
        "Geobag",
        "Centrífuga",
        "Bacia"
    ])

    if st.button("Próximo"):
        st.session_state.tipo = tipo
        st.session_state.etapa = 2

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# ETAPA 2 - INPUTS
# =========================
elif st.session_state.etapa == 2:

    st.header("Parâmetros")

    df = pd.read_csv(ARQUIVO_EQUIP)

    equipamento = st.selectbox("Equipamento", df["Equipamento"])
    eq = df[df["Equipamento"] == equipamento].iloc[0]

    st.write(f"Vazão: {eq['Vazao']}")
    st.write(f"Concentração: {eq['Concentracao']*100:.1f}%")
    st.write(f"Eficiência: {eq['Eficiencia']*100:.1f}%")

    volume = st.number_input("Volume (m³)", value=10000.0)
    distancia = st.number_input("Distância (m)", value=2000.0)
    preco = st.number_input("Preço (R$/m³)", value=16.18)

    if st.button("Calcular"):
        st.session_state.calc = {
            "volume": volume,
            "distancia": distancia,
            "preco": preco,
            "vazao": eq["Vazao"],
            "conc": eq["Concentracao"],
            "ef": eq["Eficiencia"]
        }
        st.session_state.etapa = 3

    if st.button("Voltar"):
        st.session_state.etapa = 1

# =========================
# ETAPA 3 - RESULTADO
# =========================
elif st.session_state.etapa == 3:

    d = st.session_state.calc

    prod = d["vazao"] * d["conc"] * d["ef"]

    if d["distancia"] <= 1000:
        fator = 1
    elif d["distancia"] <= 3000:
        fator = 0.75
    else:
        fator = 0.55

    prod_real = prod * fator
    tempo = d["volume"] / prod_real

    receita = d["volume"] * d["preco"]

    st.header("Resultado")

    st.write(f"Produtividade: {prod_real:.2f} m³/h")
    st.write(f"Tempo: {tempo:.2f} h")
    st.write(f"Receita: R$ {receita:,.2f}")

    if st.button("Novo"):
        st.session_state.etapa = 0
