import streamlit as st
import pandas as pd
from services.github import carregar_github

# =========================
# ARQUIVOS
# =========================
ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# ETAPA 1
# =========================
def etapa1():

    st.header("Cálculo de Produção da Draga")

    if "orcamento" not in st.session_state:
        st.warning("Volte para a etapa anterior.")
        return

    dados = st.session_state.orcamento

    # =========================
    # CARREGAR BASES
    # =========================
    df_equip = carregar_github(ARQ_EQUIP, TOKEN, REPO)
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)

    if df_equip.empty or df_mat.empty:
        st.error("Bases de equipamentos ou materiais vazias.")
        return

    # =========================
    # PRODUÇÃO POR HORA
    # =========================
    st.subheader("Produção por Hora")

    draga = st.selectbox("Selecionar draga", df_equip["Equipamento"])

    linha_equip = df_equip[df_equip["Equipamento"] == draga].iloc[0]

    # Vazão
    vazao_base = float(linha_equip["Vazao"])
    vazao = st.number_input("Vazão (m³/h)", value=vazao_base)

    if vazao != vazao_base:
        st.warning("Vazão alterada manualmente")

    # Concentração
    linha_mat = df_mat[df_mat["Material"] == dados["material"]].iloc[0]
    conc_base = float(linha_mat["Solidos_InSitu"]) / 100

    concentracao = st.number_input("Concentração", value=conc_base)

    if concentracao != conc_base:
        st.warning("Concentração alterada manualmente")

    # Eficiência
    eficiencia_map = {
        "Geobag": 0.85,
        "Centrífuga": 0.90,
        "Bombeamento direto": 0.95,
        "Bacia ecológica": 0.80
    }

    ef_base = eficiencia_map.get(dados["desag"], 0.85)

    eficiencia = st.number_input("Eficiência", value=ef_base)

    if eficiencia != ef_base:
        st.warning("Eficiência alterada manualmente")

    # Cálculo produção hora
    producao_hora = vazao * eficiencia * concentracao

    st.code(f"{vazao} × {eficiencia} × {concentracao}")
    st.success(f"Produção por hora: {producao_hora:.2f} m³/h")

    # =========================
    # HORAS TRABALHADAS
    # =========================
    st.subheader("Horas Trabalhadas no Mês")

    try:
        inicio, fim = dados["horario"].split(" - ")
        h1 = int(inicio.split(":")[0])
        h2 = int(fim.split(":")[0])

        horas_dia_bruto = h2 - h1
        horas_dia = max(horas_dia_bruto - 1, 0)  # desconto almoço

    except:
        horas_dia_bruto = 8
        horas_dia = 7

    st.write(f"Horas brutas/dia: {horas_dia_bruto}")
    st.write("(-1h almoço)")
    st.success(f"Horas líquidas/dia: {horas_dia}")

    mapa_dias = {
        "Segunda a Sexta": 22,
        "Segunda a Sábado": 26,
        "Segunda a Domingo": 30
    }

    dias_mes = mapa_dias.get(dados["dias"], 22)

    st.write(f"Dias trabalhados no mês: {dias_mes}")

    horas_mes = horas_dia * dias_mes

    st.success(f"Horas mensais disponíveis: {horas_mes}")

    # =========================
    # PRODUÇÃO MENSAL
    # =========================
    st.subheader("Produção Mensal da Draga")

    producao_mensal = producao_hora * horas_mes

    st.code(f"{producao_hora:.2f} × {horas_mes}")
    st.success(f"Produção mensal: {producao_mensal:.2f} m³")

    # =========================
    # PRAZO
    # =========================
    st.subheader("Prazo da Obra")

    volume = dados["volume"]

    if producao_mensal > 0:
        meses = volume / producao_mensal
    else:
        meses = 0

    st.code(f"{volume} ÷ {producao_mensal:.2f}")
    st.success(f"Prazo estimado: {meses:.2f} meses")

    # =========================
    # SALVAR
    # =========================
    st.session_state.orcamento.update({
        "draga": draga,
        "vazao": vazao,
        "eficiencia": eficiencia,
        "concentracao": concentracao,
        "producao_hora": producao_hora,
        "horas_dia": horas_dia,
        "dias_mes": dias_mes,
        "horas_mes": horas_mes,
        "producao_mensal": producao_mensal,
        "prazo_meses": meses
    })

    # =========================
    # NAVEGAÇÃO
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento"
        st.rerun()

    if col2.button("Continuar"):
        st.session_state.tela = "orcamento2"
        st.rerun()
