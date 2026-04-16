import streamlit as st

st.title("Orçamento de Dragagem - Draga 14\"")

# INPUTS
volume = st.number_input("Volume (m³)", value=10000)
distancia = st.number_input("Distância (m)", value=2000)
diesel = st.number_input("Preço Diesel (R$/L)", value=6.0)
preco_m3 = st.number_input("Preço por m³ (R$)", value=16.18)

salario_operador = st.number_input("Salário operador (R$/h)", value=23)
salario_ajudante = st.number_input("Salário ajudante (R$/h)", value=11)

# CONSTANTES
vazao = 850
concentracao = 0.15
prod_base = vazao * concentracao  # 127.5 m³/h

consumo_diesel = 65

# FATOR DISTÂNCIA
if distancia <= 1000:
    fator = 1.0
elif distancia <= 3000:
    fator = 0.75
else:
    fator = 0.55

produtividade = prod_base * fator

# TEMPO
tempo = volume / produtividade

# CUSTOS
custo_diesel_h = consumo_diesel * diesel
custo_mao_obra_h = salario_operador + (2 * salario_ajudante)
custo_hora = custo_diesel_h + custo_mao_obra_h

custo_total = tempo * custo_hora

# RECEITA
receita = volume * preco_m3

# RESULTADOS
lucro = receita - custo_total
margem = (lucro / receita) * 100 if receita != 0 else 0

st.subheader("Resultados")

st.write(f"Produtividade: {produtividade:.2f} m³/h")
st.write(f"Tempo de obra: {tempo:.2f} horas")
st.write(f"Custo total: R$ {custo_total:,.2f}")
st.write(f"Receita: R$ {receita:,.2f}")

st.success(f"Lucro: R$ {lucro:,.2f}")
st.info(f"Margem: {margem:.2f}%")
