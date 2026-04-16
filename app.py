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

# segurança
if not os.path.exists(ARQUIVO_FERIAS):
    pd.DataFrame(columns=["Nome", "Data"]).to_csv(ARQUIVO_FERIAS, index=False)

if not os.path.exists(ARQUIVO_EQUIP):
    pd.DataFrame(columns=["Equipamento", "Vazao", "Consumo", "Valor"]).to_csv(ARQUIVO_EQUIP, index=False)

# =========================
# MENU
# =========================
if st.session_state.etapa == 0:

    st.header("Menu Principal")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("📊 Orçamento"):
        st.session_state.etapa = 1

    if col2.button("⚙️ Base de Dados"):
        st.session_state.etapa = 100

    if col3.button("📅 Férias"):
        st.session_state.etapa = 200

    if col4.button("🚜 Equipamentos"):
        st.session_state.etapa = 300

# =========================
# BASE DE DADOS
# =========================
elif st.session_state.etapa == 100:

    st.header("Base de Dados")

    diesel = st.number_input("Preço Diesel (R$/L)", value=6.0)
    operador = st.number_input("Operador (R$/h)", value=23.0)
    ajudante = st.number_input("Ajudante (R$/h)", value=11.0)
    qtd_ajudantes = st.number_input("Qtd ajudantes", value=2)

    if st.button("Salvar"):
        st.session_state.base = {
            "diesel": diesel,
            "operador": operador,
            "ajudante": ajudante,
            "qtd_ajudantes": qtd_ajudantes
        }
        st.success("Salvo!")

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# FÉRIAS
# =========================
elif st.session_state.etapa == 200:

    st.header("Férias")

    nome = st.text_input("Nome")
    data = st.date_input("Data")

    if st.button("Salvar"):
        df = pd.read_csv(ARQUIVO_FERIAS)
        novo = pd.DataFrame([[nome, data]], columns=["Nome", "Data"])
        df = pd.concat([df, novo], ignore_index=True)
        df.to_csv(ARQUIVO_FERIAS, index=False)
        st.success("Salvo!")
        st.rerun()

    st.dataframe(pd.read_csv(ARQUIVO_FERIAS))

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# EQUIPAMENTOS
# =========================
elif st.session_state.etapa == 300:

    st.header("Equipamentos")

    df = pd.read_csv(ARQUIVO_EQUIP)
    st.dataframe(df)

    if st.button("🔄 Atualizar tabela"):
        st.rerun()

    st.divider()

    if not df.empty:

        sel = st.selectbox("Selecionar", df["Equipamento"])
        linha = df[df["Equipamento"] == sel].iloc[0]

        nome = st.text_input("Nome", value=linha["Equipamento"])
        vazao = st.number_input("Vazão (m³/h)", value=float(linha["Vazao"]))
        consumo = st.number_input("Consumo (L/h)", value=float(linha["Consumo"]))
        valor = st.number_input("Valor (R$)", value=float(linha["Valor"]))

        col1, col2 = st.columns(2)

        if col1.button("Salvar"):
            idx = df["Equipamento"] == sel

            df.loc[idx, "Equipamento"] = nome
            df.loc[idx, "Vazao"] = vazao
            df.loc[idx, "Consumo"] = consumo
            df.loc[idx, "Valor"] = valor

            df.to_csv(ARQUIVO_EQUIP, index=False)
            st.success("Atualizado!")
            st.rerun()

        if col2.button("Excluir"):
            df = df[df["Equipamento"] != sel]
            df.to_csv(ARQUIVO_EQUIP, index=False)
            st.warning("Removido!")
            st.rerun()

    st.divider()

    st.subheader("Novo equipamento")

    nome_n = st.text_input("Nome novo")
    vazao_n = st.number_input("Vazão nova", value=1000.0)
    consumo_n = st.number_input("Consumo novo", value=60.0)
    valor_n = st.number_input("Valor novo", value=1000000.0)

    if st.button("Adicionar"):
        novo = pd.DataFrame([[nome_n, vazao_n, consumo_n, valor_n]],
                            columns=["Equipamento", "Vazao", "Consumo", "Valor"])

        df = pd.concat([df, novo], ignore_index=True)
        df.to_csv(ARQUIVO_EQUIP, index=False)

        st.success("Adicionado!")
        st.rerun()

    if st.button("Voltar"):
        st.session_state.etapa = 0

# =========================
# TIPO OPERAÇÃO
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
# INPUTS
# =========================
elif st.session_state.etapa == 2:

    st.header("Parâmetros")

    df = pd.read_csv(ARQUIVO_EQUIP)

    equipamento = st.selectbox("Equipamento", df["Equipamento"])
    eq = df[df["Equipamento"] == equipamento].iloc[0]

    st.write(f"Vazão: {eq['Vazao']} m³/h")
    st.write(f"Consumo: {eq['Consumo']} L/h")
    st.write(f"Valor: R$ {eq['Valor']:,.2f}")

    volume = st.number_input("Volume (m³)", value=10000.0)
    distancia = st.number_input("Distância (m)", value=2000.0)
    preco = st.number_input("Preço (R$/m³)", value=16.18)
    horas_dia = st.number_input("Horas/dia", value=20)

    if st.button("Calcular"):
        st.session_state.calc = {
            "volume": volume,
            "distancia": distancia,
            "preco": preco,
            "vazao": eq["Vazao"],
            "consumo": eq["Consumo"],
            "horas_dia": horas_dia
        }
        st.session_state.etapa = 3

    if st.button("Voltar"):
        st.session_state.etapa = 1

# =========================
# RESULTADO
# =========================
elif st.session_state.etapa == 3:

    d = st.session_state.calc

    prod = d["vazao"]

    if d["distancia"] <= 1000:
        fator = 1
    elif d["distancia"] <= 3000:
        fator = 0.75
    else:
        fator = 0.55

    prod_real = prod * fator
    tempo_h = d["volume"] / prod_real
    dias = tempo_h / d["horas_dia"]

    preco_diesel = st.session_state.get("base", {}).get("diesel", 6.0)
    custo_diesel = d["consumo"] * tempo_h * preco_diesel

    receita = d["volume"] * d["preco"]
    lucro = receita - custo_diesel

    st.header("Resultado")

    st.write(f"Produtividade: {prod_real:.2f} m³/h")
    st.write(f"Tempo: {tempo_h:.2f} h")
    st.write(f"Duração: {dias:.2f} dias")

    st.write(f"Custo diesel: R$ {custo_diesel:,.2f}")
    st.write(f"Receita: R$ {receita:,.2f}")

    st.success(f"Lucro: R$ {lucro:,.2f}")

    if st.button("Novo"):
        st.session_state.etapa = 0
