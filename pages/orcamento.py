import streamlit as st
import pandas as pd
from datetime import datetime
from services.github import carregar_github, salvar_github

# =========================
# ARQUIVOS
# =========================
ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"
ARQ_CLIENTES = "data/clientes.csv"
ARQ_OBRAS = "data/orcamentos.csv"
ARQ_SAL = "data/salarios.csv"

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

    df_clientes = carregar_github(ARQ_CLIENTES, TOKEN, REPO)
    if df_clientes.empty:
        df_clientes = pd.DataFrame(columns=["Cliente"])

    cliente = st.selectbox("Cliente", df_clientes["Cliente"])
    novo_cliente = st.text_input("Ou adicionar novo cliente")

    nome_obra = st.text_input("Nome da obra")
    local = st.text_input("Local de execução")
    data = st.date_input("Data", value=datetime.now())

    st.write(f"Data selecionada: {data.strftime('%d/%m/%Y')}")
    st.info(f"Código: {codigo}")

    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)
    df_desag = carregar_github(ARQ_DESAG, TOKEN, REPO)
    df_med = carregar_github("data/medicao.csv", TOKEN, REPO)
    df_hor = carregar_github("data/horarios.csv", TOKEN, REPO)
    df_dias = carregar_github("data/dias.csv", TOKEN, REPO)

    volume = st.number_input("Volume a ser dragado")

    material = st.selectbox("Tipo de material", df_mat["Material"])
    desag = st.selectbox("Tipo de desaguamento", df_desag["Tipo"])

    col1, col2 = st.columns(2)
    flutuante = col1.number_input("Linha flutuante (m)")
    terrestre = col2.number_input("Linha terrestre (m)")

    sistema_med = st.selectbox("Sistema de medição", df_med["Sistema"])

    horario = st.selectbox(
        "Horário de trabalho",
        df_hor.apply(lambda x: f"{x['Inicio']} - {x['Fim']}", axis=1)
    )

    dias = st.selectbox("Dias de trabalho", df_dias["Descricao"])

    if st.button("Continuar", key="cont_etapa0"):

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

# =========================
# ETAPA 1
# =========================
def etapa1():

    st.header("Cálculo de Produção da Draga")

    dados = st.session_state.orcamento

    df_equip = carregar_github(ARQ_EQUIP, TOKEN, REPO)
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)

    draga = st.selectbox("Selecionar draga", df_equip["Equipamento"])
    linha_equip = df_equip[df_equip["Equipamento"] == draga].iloc[0]

    vazao = st.number_input("Vazão (m³/h)", value=float(linha_equip["Vazao"]))

    linha_mat = df_mat[df_mat["Material"] == dados["material"]].iloc[0]
    concentracao = st.number_input("Concentração", value=float(linha_mat["Solidos_InSitu"]) / 100)

    eficiencia_map = {
        "Geobag": 0.85,
        "Centrífuga": 0.90,
        "Bombeamento direto": 0.95,
        "Bacia ecológica": 0.80
    }

    eficiencia = st.number_input("Eficiência", value=eficiencia_map.get(dados["desag"], 0.85))

    producao_hora = vazao * eficiencia * concentracao

    st.success(f"Produção por hora: {producao_hora:.2f} m³/h")

    # HORAS
    try:
        inicio, fim = dados["horario"].split(" - ")
        horas_dia = max(int(fim[:2]) - int(inicio[:2]) - 1, 0)
    except:
        horas_dia = 7

    mapa_dias = {"Segunda a Sexta": 22, "Segunda a Sábado": 26, "Segunda a Domingo": 30}
    horas_mes = horas_dia * mapa_dias.get(dados["dias"], 22)

    producao_mensal = producao_hora * horas_mes
    prazo = dados["volume"] / producao_mensal if producao_mensal else 0

    st.success(f"Produção mensal: {producao_mensal:.2f}")
    st.success(f"Prazo: {prazo:.2f} meses")

    st.session_state.orcamento.update({
        "producao_mensal": producao_mensal,
        "horas_dia": horas_dia
    })

    if st.button("Continuar"):
        st.session_state.tela = "orcamento2"
        st.rerun()

# =========================
# ETAPA 2
# =========================
def etapa2():

    st.header("Dimensionamento de Equipe")

    df_sal = carregar_github(ARQ_SAL, TOKEN, REPO)

    leis = st.number_input("Leis Sociais (%)", value=110.0)
    fator = 1 + leis / 100

    df = df_sal.copy()
    df["Qtd"] = 0
    df["Adicional 25%"] = False
    df["Valor c/ Leis"] = df["Valor_Hora"] * fator

    df_editado = st.data_editor(df, use_container_width=True)

    df_calc = df_editado.copy()
    df_calc["Valor Final"] = df_calc.apply(
        lambda x: x["Valor c/ Leis"] * (1.25 if x["Adicional 25%"] else 1),
        axis=1
    )

    equipe = df_calc.to_dict("records")

    st.session_state.orcamento["equipe"] = equipe

    if st.button("Continuar"):
        st.session_state.tela = "orcamento3"
        st.rerun()

# =========================
# ETAPA 3 - BARRILETE
# =========================
def etapa3():

    st.header("Custo do Barrilete")

    dados = st.session_state.orcamento

    dias = st.number_input("Dias", value=5)
    horas = dias * dados.get("horas_dia", 7)

    st.info(f"Horas totais: {horas}")

    custo_mo = 0

    for i, func in enumerate(dados.get("equipe", [])):

        usar = st.checkbox(func["Posicao"], key=f"barr_{i}")

        if usar:
            custo = func["Valor Final"] * func["Qtd"] * horas
            custo_mo += custo

    st.success(f"Mão de obra: R$ {custo_mo:,.2f}")

    custo_mat = 0

    itens = ["Tubo 8\"", "Toco", "Joelho", "Tee", "Ponteira", "Cap"]

    for item in itens:
        q = st.number_input(f"{item} qtd", key=f"q_{item}")
        v = st.number_input(f"{item} valor", key=f"v_{item}")
        custo_mat += q * v

    st.success(f"Materiais: R$ {custo_mat:,.2f}")

    total = custo_mo + custo_mat

    st.header(f"Total: R$ {total:,.2f}")

    if st.button("Finalizar"):
        st.session_state.tela = "menu"
