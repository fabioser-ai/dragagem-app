import streamlit as st
import pandas as pd
from services.github import carregar_github

ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"
ARQ_SAL = "data/salarios.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# ETAPA 0 - OBRA
# =========================
def etapa0():

    st.header("Informações da Obra")

    obra = st.text_input("Nome da Obra")
    cliente = st.text_input("Cliente")
    volume = st.number_input("Volume (m³)")
    horas_dia = st.number_input("Horas por dia", value=8)
    dias_mes = st.number_input("Dias por mês", value=26)

    if st.button("Continuar"):
        st.session_state.orcamento = {
            "obra": obra,
            "cliente": cliente,
            "volume": volume,
            "horas_dia": horas_dia,
            "dias_mes": dias_mes
        }
        st.session_state.tela = "orcamento"
        st.rerun()

# =========================
# ETAPA 1 - PRODUÇÃO
# =========================
def etapa1():

    st.header("Produção da Draga")

    dados = st.session_state.orcamento

    df_equip = carregar_github(ARQ_EQUIP, TOKEN, REPO)
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)

    draga = st.selectbox("Draga", df_equip["Equipamento"])
    mat = st.selectbox("Material", df_mat["Material"])

    vazao = st.number_input("Vazão", value=100.0)
    eficiencia = st.number_input("Eficiência", value=0.85)
    concentracao = st.number_input("Concentração", value=0.20)

    prod_h = vazao * eficiencia * concentracao

    horas_mes = dados["dias_mes"] * max(dados["horas_dia"] - 1, 0)
    prod_mes = prod_h * horas_mes

    prazo = dados["volume"] / prod_mes if prod_mes > 0 else 0

    st.success(f"Produção por hora: {prod_h:.2f}")
    st.success(f"Produção mensal: {prod_mes:.2f}")
    st.success(f"Prazo (meses): {prazo:.2f}")

    st.session_state.orcamento["producao_mes"] = prod_mes

    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento0"
        st.rerun()

    if col2.button("Continuar"):
        st.session_state.tela = "orcamento2"
        st.rerun()

# =========================
# ETAPA 2 - EQUIPE
# =========================
def etapa2():

    st.header("Equipe")

    df_sal = carregar_github(ARQ_SAL, TOKEN, REPO)

    leis = st.number_input("Leis sociais (%)", value=110.0)

    equipe = []

    for i, row in df_sal.iterrows():

        col1, col2, col3 = st.columns([1,3,2])

        qtd = col1.number_input("", min_value=0, step=1, key=f"qtd_{i}")
        col2.write(row["Posicao"])
        col3.write(f"R$ {row['Valor_Hora']:.2f}")

        if qtd > 0:
            valor = row["Valor_Hora"] * (1 + leis/100)

            equipe.append({
                "posicao": row["Posicao"],
                "valor_hora": valor,
                "quantidade": qtd
            })

    st.session_state.equipe = equipe

    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento"
        st.rerun()

    if col2.button("Continuar"):
        st.session_state.tela = "orcamento3"
        st.rerun()

# =========================
# ETAPA 3 - BARRILETE
# =========================
def etapa3():

    st.header("Custo do Barrilete")

    dados = st.session_state.orcamento

    dias = st.number_input("Dias", value=5)
    horas = dias * max(dados["horas_dia"] - 1, 0)

    st.info(f"Horas totais: {horas}")

    # MÃO DE OBRA
    custo_mo = 0

    for func in st.session_state.get("equipe", []):
        custo = func["valor_hora"] * horas * func["quantidade"]
        custo_mo += custo

    st.success(f"Mão de obra: R$ {custo_mo:.2f}")

    # MATERIAIS
    materiais = [
        "Tubo 8\"", "Toco 0,5m", "Joelho 90°", "Tee",
        "Ponteira", "Cap", "Válvula 4\"", "Válvula 3\"",
        "Mangueira", "Abraçadeiras", "Curva PVC",
        "Válvula esfera", "Bomba lameira"
    ]

    custo_mat = 0

    for mat in materiais:
        qtd = st.number_input(f"{mat} qtd", key=f"q_{mat}")
        val = st.number_input(f"{mat} valor", key=f"v_{mat}")
        custo_mat += qtd * val

    st.success(f"Materiais: R$ {custo_mat:.2f}")

    total = custo_mo + custo_mat

    st.header(f"Total Barrilete: R$ {total:.2f}")

    st.session_state.orcamento["barrilete"] = total

    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento2"
        st.rerun()

    if col2.button("Continuar"):
        st.session_state.tela = "menu"
        st.rerun()
