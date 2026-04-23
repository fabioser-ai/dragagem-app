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

    st.info(f"Código: {codigo}")

    # =========================
    # DATABASES
    # =========================
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)
    df_desag = carregar_github(ARQ_DESAG, TOKEN, REPO)
    df_med = carregar_github("data/medicao.csv", TOKEN, REPO)
    df_hor = carregar_github("data/horarios.csv", TOKEN, REPO)
    df_dias = carregar_github("data/dias.csv", TOKEN, REPO)

    # =========================
    # DADOS TÉCNICOS
    # =========================
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

        st.session_state.orcamento = {
            "codigo": codigo,
            "nome_obra": nome_obra,
            "cliente": cliente_final,
            "data": str(data),
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

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
        st.rerun()

# =========================
# ETAPA 1
# =========================
def etapa1():

    st.header("Cálculo de Produção da Draga")

    dados = st.session_state.orcamento

    df_equip = carregar_github(ARQ_EQUIP, TOKEN, REPO)
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)

    # =========================
    # PRODUÇÃO POR HORA
    # =========================
    st.subheader("Produção por Hora")

    draga = st.selectbox("Selecionar draga", df_equip["Equipamento"])
    linha_equip = df_equip[df_equip["Equipamento"] == draga].iloc[0]

    # VAZÃO EDITÁVEL
    vazao_base = float(linha_equip["Vazao"])
    vazao = st.number_input("Vazão da draga (m³/h)", value=vazao_base)

    if vazao != vazao_base:
        st.warning("*Vazão alterada manualmente")

    # CONCENTRAÇÃO EDITÁVEL
    linha_mat = df_mat[df_mat["Material"] == dados["material"]].iloc[0]
    conc_base = float(linha_mat["Solidos_InSitu"]) / 100

    concentracao = st.number_input("Concentração", value=conc_base)

    if concentracao != conc_base:
        st.warning("*Concentração alterada manualmente")

    # EFICIÊNCIA EDITÁVEL
    eficiencia_map = {
        "Geobag": 0.85,
        "Centrífuga": 0.90,
        "Bombeamento direto": 0.95,
        "Bacia ecológica": 0.80
    }

    ef_base = eficiencia_map.get(dados["desag"], 0.85)

    eficiencia = st.number_input("Eficiência", value=ef_base)

    if eficiencia != ef_base:
        st.warning("*Eficiência alterada manualmente")

    # CÁLCULO PRODUÇÃO
    producao_hora = vazao * eficiencia * concentracao

    st.code(f"{vazao} × {eficiencia} × {concentracao}")
    st.success(f"Produção por hora: {producao_hora:.2f} m³/h")

    # =========================
    # HORAS MENSAIS
    # =========================
    st.subheader("Horas Trabalhadas no Mês")

    try:
        inicio, fim = dados["horario"].split(" - ")
        h1 = int(inicio.split(":")[0])
        h2 = int(fim.split(":")[0])

        horas_dia_bruto = h2 - h1
        horas_dia = max(horas_dia_bruto - 1, 0)

    except:
        horas_dia_bruto = 8
        horas_dia = 7

    st.write(f"Horas por dia (bruto): {horas_dia_bruto}")
    st.write("(-1h almoço)")
    st.success(f"Horas líquidas por dia: {horas_dia}")

    # DIAS NO MÊS
    mapa_dias = {
        "Segunda a Sexta": 22,
        "Segunda a Sábado": 26,
        "Segunda a Domingo": 30
    }

    dias_mes = mapa_dias.get(dados["dias"], 22)

    st.write(f"Dias trabalhados no mês: {dias_mes}")

    horas_mes = horas_dia * dias_mes

    st.code(f"{horas_dia} × {dias_mes}")
    st.success(f"Horas mensais: {horas_mes} h")

    # =========================
    # PRODUÇÃO MENSAL
    # =========================
    st.subheader("Produção Mensal da Draga")

    producao_mensal = producao_hora * horas_mes

    st.code(f"{producao_hora:.2f} × {horas_mes}")
    st.success(f"Produção mensal: {producao_mensal:.2f} m³/mês")

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

# =========================
# ETAPA 2
# =========================
def etapa2():

    st.header("Dimensionamento de Equipe")

    dados = st.session_state.orcamento

    ARQ_SAL = "data/salarios.csv"

    df_sal = carregar_github(ARQ_SAL, TOKEN, REPO)

    if df_sal.empty:
        st.warning("Base de salários vazia")
        return

    # =========================
    # LEIS SOCIAIS
    # =========================
    leis = st.number_input("Leis Sociais (%)", value=110.0)

    fator_leis = 1 + (leis / 100)

    st.info(f"Fator aplicado: {fator_leis:.2f}")

    st.divider()

    # =========================
    # TABELA DE EQUIPE
    # =========================
    st.subheader("Equipe")

    total_mensal = 0

    resultados = []

    for i, row in df_sal.iterrows():

        col1, col2, col3, col4 = st.columns([2,2,1,2])

        posicao = row["Posicao"]
        salario_base = float(row["Valor_Hora"])

        col1.write(posicao)
        col2.write(f"{salario_base:.2f}")

        qtd = col3.number_input(
            f"Qtd {posicao}",
            min_value=0,
            step=1,
            key=f"qtd_{i}"
        )

        salario_com_leis = salario_base * fator_leis

        col4.write(f"{salario_com_leis:.2f}")

        total = qtd * salario_com_leis
        total_mensal += total

        resultados.append({
            "Posicao": posicao,
            "Qtd": qtd,
            "Salario_Base": salario_base,
            "Salario_Leis": salario_com_leis,
            "Total": total
        })

    st.divider()

    st.success(f"Custo total mensal da equipe: R$ {total_mensal:,.2f}")

    # =========================
    # SALVAR
    # =========================
    st.session_state.orcamento.update({
        "equipe": resultados,
        "custo_mensal_equipe": total_mensal,
        "leis_sociais": leis
    })

    # =========================
    # NAVEGAÇÃO
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento1"
        st.rerun()

    if col2.button("Continuar"):
        st.success("Próxima etapa: custos operacionais")

    # =========================
    # SALVAR ORÇAMENTO
    # =========================
    if st.button("💾 Salvar orçamento"):

        try:
            df = carregar_github(ARQ_OBRAS, TOKEN, REPO)
        except:
            df = pd.DataFrame(columns=[
                "Codigo","Nome_Obra","Cliente","Data",
                "Vazao","Volume","Material","Desaguamento",
                "Distancia","Vazao_Real"
            ])

        novo = {
            "Codigo": dados["codigo"],
            "Nome_Obra": dados["nome_obra"],
            "Cliente": dados["cliente"],
            "Data": dados["data"],
            "Vazao": dados["vazao"],
            "Volume": dados["volume"],
            "Material": dados["material"],
            "Desaguamento": dados["desag"],
            "Distancia": distancia_total,
            "Vazao_Real": vazao_real
        }

        df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)

        salvar_github(df, ARQ_OBRAS, TOKEN, REPO)

        st.success("Orçamento salvo com sucesso!")

    # navegação
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento1"
        st.rerun()
