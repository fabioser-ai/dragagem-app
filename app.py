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
# ARQUIVO DE DADOS
# =========================
ARQUIVO_FERIAS = "ferias.csv"

if not os.path.exists(ARQUIVO_FERIAS):
    df_init = pd.DataFrame(columns=["Nome", "Data"])
    df_init.to_csv(ARQUIVO_FERIAS, index=False)

# =========================
# ETAPA 0 - MENU PRINCIPAL
# =========================
if st.session_state.etapa == 0:

    st.header("Menu Principal")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Orçamento")
        if st.button("📊 Criar Orçamento"):
            st.session_state.etapa = 1

    with col2:
        st.subheader("Base de Dados")
        if st.button("⚙️ Atualizar Dados"):
            st.session_state.etapa = 100

    with col3:
        st.subheader("Férias / Folgas")
        if st.button("📅 Gerenciar"):
            st.session_state.etapa = 200

# =========================
# ETAPA 200 - FÉRIAS
# =========================
elif st.session_state.etapa == 200:

    st.header("Gestão de Férias / Folgas")

    nome = st.text_input("Nome do funcionário")
    data = st.date_input("Data")

    if st.button("Salvar"):
        novo = pd.DataFrame([[nome, data]], columns=["Nome", "Data"])
        df = pd.read_csv(ARQUIVO_FERIAS)
        df = pd.concat([df, novo], ignore_index=True)
        df.to_csv(ARQUIVO_FERIAS, index=False)
        st.success("Registro salvo!")

    st.subheader("Histórico")

    df = pd.read_csv(ARQUIVO_FERIAS)
    st.dataframe(df)

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# ETAPA 100 - BASE DE DADOS
# =========================
elif st.session_state.etapa == 100:

    st.header("Base de Dados")

    st.subheader("Custos Operacionais")
    diesel = st.number_input("Preço Diesel (R$/L)", value=6.0)
    consumo = st.number_input("Consumo da draga (L/h)", value=65.0)

    st.subheader("Mão de Obra")
    operador = st.number_input("Salário operador (R$/h)", value=23.0)
    ajudante = st.number_input("Salário ajudante (R$/h)", value=11.0)
    qtd_ajudantes = st.number_input("Quantidade de ajudantes", value=2)

    st.subheader("Equipamento")
    vazao = st.number_input("Vazão nominal (m³/h)", value=850.0)
    concentracao = st.number_input("Concentração (%)", value=15.0)

    if st.button("Salvar dados"):
        st.session_state.base_dados = {
            "diesel": diesel,
            "consumo": consumo,
            "operador": operador,
            "ajudante": ajudante,
            "qtd_ajudantes": qtd_ajudantes,
            "vazao": vazao,
            "concentracao": concentracao / 100
        }
        st.success("Dados salvos!")

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# ETAPA 1 - ESCOLHA OPERAÇÃO
# =========================
elif st.session_state.etapa == 1:

    st.header("Escolha o tipo de operação")

    tipo_operacao = st.selectbox(
        "Selecione:",
        [
            "Bombeamento direto",
            "Desaguamento em geobags",
            "Desaguamento em centrífuga",
            "Desaguamento em bacia ecológica"
        ]
    )

    if st.button("Próximo"):
        st.session_state.tipo_operacao = tipo_operacao
        st.session_state.etapa = 2

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# ETAPA 2 - INPUTS
# =========================
elif st.session_state.etapa == 2:

    st.header(f"Parâmetros - {st.session_state.tipo_operacao}")

    base = st.session_state.get("base_dados", {})

    volume = st.number_input("Volume (m³)", value=10000.0)
    distancia = st.number_input("Distância (m)", value=2000.0)
    preco_m3 = st.number_input("Preço por m³ (R$)", value=16.18)

    diesel = st.number_input("Preço Diesel (R$/L)", value=base.get("diesel", 6.0))
    consumo = base.get("consumo", 65.0)

    salario_operador = st.number_input("Salário operador (R$/h)", value=base.get("operador", 23.0))
    salario_ajudante = st.number_input("Salário ajudante (R$/h)", value=base.get("ajudante", 11.0))
    qtd_ajudantes = base.get("qtd_ajudantes", 2)

    vazao = base.get("vazao", 850.0)
    concentracao = base.get("concentracao", 0.15)

    if st.button("Calcular"):
        st.session_state.dados = {
            "volume": volume,
            "distancia": distancia,
            "preco_m3": preco_m3,
            "diesel": diesel,
            "consumo": consumo,
            "salario_operador": salario_operador,
            "salario_ajudante": salario_ajudante,
            "qtd_ajudantes": qtd_ajudantes,
            "vazao": vazao,
            "concentracao": concentracao
        }
        st.session_state.etapa = 3

    if st.button("Voltar"):
        st.session_state.etapa = 1

# =========================
# ETAPA 3 - RESULTADOS
# =========================
elif st.session_state.etapa == 3:

    st.header("Resultados")

    d = st.session_state.dados

    prod_base = d["vazao"] * d["concentracao"]

    if d["distancia"] <= 1000:
        fator = 1.0
    elif d["distancia"] <= 3000:
        fator = 0.75
    else:
        fator = 0.55

    produtividade = prod_base * fator
    tempo = d["volume"] / produtividade

    custo_diesel_h = d["consumo"] * d["diesel"]
    custo_mao_obra_h = d["salario_operador"] + (d["qtd_ajudantes"] * d["salario_ajudante"])
    custo_hora = custo_diesel_h + custo_mao_obra_h

    custo_total = tempo * custo_hora
    receita = d["volume"] * d["preco_m3"]

    lucro = receita - custo_total
    margem = (lucro / receita) * 100 if receita != 0 else 0

    st.write(f"Produtividade: {produtividade:.2f} m³/h")
    st.write(f"Tempo de obra: {tempo:.2f} horas")
    st.write(f"Custo total: R$ {custo_total:,.2f}")
    st.write(f"Receita: R$ {receita:,.2f}")

    st.success(f"Lucro: R$ {lucro:,.2f}")
    st.info(f"Margem: {margem:.2f}%")

    if st.button("Novo orçamento"):
        st.session_state.etapa = 0
