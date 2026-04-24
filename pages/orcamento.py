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

    data_formatada = data.strftime("%d/%m/%Y")

    st.write(f"Data selecionada: {data_formatada}")

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

    st.subheader("Produção por Hora")

    draga = st.selectbox("Selecionar draga", df_equip["Equipamento"])
    linha_equip = df_equip[df_equip["Equipamento"] == draga].iloc[0]

    # VAZÃO EDITÁVEL
    vazao_base = float(linha_equip["Vazao"])
    vazao = st.number_input("Vazão (m³/h)", value=vazao_base)

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

    producao_hora = vazao * eficiencia * concentracao

    st.code(f"{vazao} × {eficiencia} × {concentracao}")
    st.success(f"Produção por hora: {producao_hora:.2f} m³/h")

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

    st.write(f"Horas brutas/dia: {horas_dia_bruto}")
    st.write("(-1h almoço)")
    st.success(f"Horas líquidas/dia: {horas_dia}")

    mapa_dias = {
        "Segunda a Sexta": 22,
        "Segunda a Sábado": 26,
        "Segunda a Domingo": 30
    }

    dias_mes = mapa_dias.get(dados["dias"], 22)

    horas_mes = horas_dia * dias_mes

    st.success(f"Horas mensais: {horas_mes}")

    st.subheader("Produção Mensal")

    producao_mensal = producao_hora * horas_mes

    st.success(f"Produção mensal: {producao_mensal:.2f} m³")

    st.subheader("Prazo")

    volume = dados["volume"]
    meses = volume / producao_mensal if producao_mensal > 0 else 0

    st.success(f"Prazo: {meses:.2f} meses")

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

    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar", key="voltar1"):
        st.session_state.tela = "orcamento"
        st.rerun()

    if col2.button("Continuar", key="cont1"):
        st.session_state.tela = "orcamento2"
        st.rerun()

# =========================
# ETAPA 2
# =========================
def etapa2():

    st.header("Dimensionamento de Equipe")

    # =========================
    # CARREGAR DADOS
    # =========================
    df_sal = carregar_github(ARQ_SAL, TOKEN, REPO)

    if df_sal.empty:
        st.warning("Base de salários vazia")
        return

    # =========================
    # LEIS SOCIAIS
    # =========================
    leis = st.number_input("Leis Sociais (%)", value=110.0)
    fator_leis = 1 + leis / 100

    st.info(f"Fator leis sociais: {fator_leis:.2f}")

    # =========================
    # MONTA TABELA BASE
    # =========================
    df = df_sal.copy()

    df["Qtd"] = 0
    df["Adicional 25%"] = False
    df["Valor c/ Leis"] = df["Valor_Hora"] * fator_leis

    df = df[["Qtd", "Posicao", "Valor_Hora", "Adicional 25%", "Valor c/ Leis"]]

    # =========================
    # EDITOR
    # =========================
    df_editado = st.data_editor(
        df,
        use_container_width=True,
        num_rows="fixed",
        column_config={
            "Qtd": st.column_config.NumberColumn("Qtd", step=1, min_value=0),
            "Posicao": st.column_config.TextColumn("Posição", disabled=True),
            "Valor_Hora": st.column_config.NumberColumn("Valor Hora (R$)", disabled=True),
            "Adicional 25%": st.column_config.CheckboxColumn("Adic. 25%"),
            "Valor c/ Leis": st.column_config.NumberColumn("C/ Leis (R$)", disabled=True),
        }
    )

    # =========================
    # CÁLCULO FINAL
    # =========================
    df_editado["Fator_Adicional"] = df_editado["Adicional 25%"].apply(lambda x: 1.25 if x else 1.0)

    df_editado["Valor Final"] = df_editado["Valor c/ Leis"] * df_editado["Fator_Adicional"]

    df_editado["Total"] = df_editado["Qtd"] * df_editado["Valor Final"]

    total_mensal = df_editado["Total"].sum()

    # =========================
    # EXIBIÇÃO
    # =========================
    st.success(f"Custo mensal da equipe: R$ {total_mensal:,.2f}")

    # =========================
    # SALVAR
    # =========================
    st.session_state.orcamento.update({
        "equipe": df_editado.to_dict(orient="records"),
        "custo_mensal_equipe": total_mensal,
        "leis_sociais": leis
    })

    # =========================
    # NAVEGAÇÃO
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar", key="voltar_etapa2"):
        st.session_state.tela = "orcamento1"
        st.rerun()

    if col2.button("Continuar", key="continuar_etapa2"):
        st.success("Próxima etapa: custos operacionais")
