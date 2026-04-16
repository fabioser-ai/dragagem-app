import streamlit as st


st.title("FOS ENGENHARIA LTDA")

# CONTROLE DE ETAPA
if "etapa" not in st.session_state:
    st.session_state.etapa = 0

# =========================
# ETAPA 0 - MENU PRINCIPAL
# =========================
if st.session_state.etapa == 0:

    st.header("Menu Principal")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Orçamento")
        st.write("Criar novo orçamento de dragagem")
        if st.button("📊 Criar Orçamento"):
            st.session_state.etapa = 1

    with col2:
        st.subheader("Base de Dados")
        st.write("Atualizar custos e parâmetros")
        if st.button("⚙️ Atualizar Dados"):
            st.session_state.etapa = 100

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

    col1, col2 = st.columns(2)

    if col1.button("Voltar"):
        st.session_state.etapa = 0

    if col2.button("Próximo"):
        st.session_state.tipo_operacao = tipo_operacao
        st.session_state.etapa = 2

# =========================
# ETAPA 100 - BASE DE DADOS
# =========================
elif st.session_state.etapa == 100:

    st.header("Atualização de Base de Dados")

    st.write("Aqui você poderá definir custos padrão do sistema")

    diesel = st.number_input("Preço Diesel (R$/L)", value=6.0)
    operador = st.number_input("Salário operador (R$/h)", value=23.0)
    ajudante = st.number_input("Salário ajudante (R$/h)", value=11.0)

    if st.button("Salvar dados"):
        st.session_state.base_dados = {
            "diesel": diesel,
            "operador": operador,
            "ajudante": ajudante
        }
        st.success("Dados salvos com sucesso!")

    if st.button("Voltar ao menu"):
        st.session_state.etapa = 0

# =========================
# ETAPA 2 - INPUTS ORÇAMENTO
# =========================
elif st.session_state.etapa == 2:

    st.header(f"Parâmetros - {st.session_state.tipo_operacao}")

    base = st.session_state.get("base_dados", {})

    volume = st.number_input("Volume (m³)", value=10000)
    distancia = st.number_input("Distância (m)", value=2000)
    diesel = st.number_input("Preço Diesel (R$/L)", value=base.get("diesel", 6.0))
    preco_m3 = st.number_input("Preço por m³ (R$)", value=16.18)

    salario_operador = st.number_input("Salário operador (R$/h)", value=base.get("operador", 23.0))
    salario_ajudante = st.number_input("Salário ajudante (R$/h)", value=base.get("ajudante", 11.0))

    col1, col2 = st.columns(2)

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
# ETAPA 3 - RESULTADOS
# =========================
elif st.session_state.etapa == 3:

    st.header("Resultados")

    dados = st.session_state.dados

    vazao = 850
    concentracao = 0.15
    prod_base = vazao * concentracao
    consumo_diesel = 65

    distancia = dados["distancia"]

    if distancia <= 1000:
        fator = 1.0
    elif distancia <= 3000:
        fator = 0.75
    else:
        fator = 0.55

    produtividade = prod_base * fator
    tempo = dados["volume"] / produtividade

    custo_diesel_h = consumo_diesel * dados["diesel"]
    custo_mao_obra_h = dados["salario_operador"] + (2 * dados["salario_ajudante"])
    custo_hora = custo_diesel_h + custo_mao_obra_h

    custo_total = tempo * custo_hora
    receita = dados["volume"] * dados["preco_m3"]

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
