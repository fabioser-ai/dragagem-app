import streamlit as st

def etapa3():

    st.header("Custos do Barrilete")

    st.subheader("Equipe selecionada")

    equipe = st.session_state.orcamento.get("equipe", [])

    if not equipe:
        st.warning("Nenhuma equipe selecionada na etapa 2")
    else:
        st.dataframe(equipe)

    st.subheader("Materiais do Barrilete")

    materiais = [
        "Tubo ferro 6m 8\"",
        "Toco 0,50m",
        "Joelho 90°",
        "Tee 6x4 flangeado",
        "Ponteira 4\"",
        "Cap 6\"",
        "Válvula gaveta 4\"",
        "Válvula gaveta 3\"",
        "Mangueira água",
        "Abraçadeiras",
        "Curva PVC 4\"",
        "Válvula esfera 2\"",
        "Bomba lameira"
    ]

    consumo = {}

    for m in materiais:
        consumo[m] = st.number_input(f"{m}", value=0, step=1)

    dias = st.number_input("Dias necessários", value=1)

    if st.button("Finalizar etapa 3"):

        st.session_state.orcamento["barrilete"] = {
            "consumo": consumo,
            "dias": dias
        }

        st.success("Etapa 3 concluída")
