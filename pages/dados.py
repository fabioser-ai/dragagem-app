import streamlit as st
import pandas as pd
from services.github import carregar_github, salvar_github

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"
ARQ_HOR = "data/horarios.csv"
ARQ_DIAS = "data/dias.csv"
ARQ_SAL = "data/salarios.csv"

# =========================
# CONVERSÃO MONETÁRIA (BR)
# =========================
def converter_valor_monetario(valor):
    try:
        valor = str(valor).replace(".", "").replace(",", ".")
        return float(valor)
    except:
        return 0.0

# =========================
# CRUD GENÉRICO
# =========================
def crud(arquivo, colunas, titulo, chave):

    st.subheader(titulo)

    df = carregar_github(arquivo, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=colunas)

    st.dataframe(df, use_container_width=True)

    # =========================
    # EDITAR
    # =========================
    if not df.empty:

        label_col = colunas[0]

        opcoes = df[label_col].astype(str).tolist()
        selecionado = st.selectbox(
            "Selecionar para editar",
            opcoes,
            key=f"sel_{chave}"
        )

        idx = df[df[label_col].astype(str) == selecionado].index[0]
        linha = df.loc[idx]

        novos = []

        for c in colunas:
            valor_padrao = str(linha[c])

            novos.append(
                st.text_input(
                    c,
                    value=valor_padrao,
                    key=f"{chave}_{c}_{idx}"
                )
            )

        col1, col2 = st.columns(2)

        if col1.button("Salvar", key=f"save_{chave}"):

            novos_convertidos = []

            for i, c in enumerate(colunas):
                v = novos[i]

                if c.lower() in [
                    "vazao",
                    "consumo",
                    "valor",
                    "solidos_insitu",
                    "solidos_desaguado",
                    "valor_hora",
                ]:
                    v = converter_valor_monetario(v)

                novos_convertidos.append(v)

            df.loc[idx] = novos_convertidos
            salvar_github(df, arquivo, TOKEN, REPO)

            st.success("Atualizado!")
            st.rerun()

        if col2.button("Excluir", key=f"del_{chave}"):

            df = df.drop(idx).reset_index(drop=True)
            salvar_github(df, arquivo, TOKEN, REPO)

            st.warning("Removido!")
            st.rerun()

    st.divider()

    # =========================
    # NOVO
    # =========================
    st.write("Adicionar novo")

    valores = []

    for c in colunas:
        valores.append(st.text_input(c, key=f"new_{chave}_{c}"))

    if st.button("Adicionar", key=f"add_{chave}"):

        valores_convertidos = []

        for i, c in enumerate(colunas):
            v = valores[i]

            if c.lower() in [
                "vazao",
                "consumo",
                "valor",
                "solidos_insitu",
                "solidos_desaguado",
                "valor_hora",
            ]:
                v = converter_valor_monetario(v)

            valores_convertidos.append(v)

        df.loc[len(df)] = valores_convertidos
        salvar_github(df, arquivo, TOKEN, REPO)

        st.success("Adicionado!")
        st.rerun()

# =========================
# TELA PRINCIPAL
# =========================
def render():

    st.title("Dados")

    if "subdados" not in st.session_state:
        st.session_state.subdados = None

    col1, col2, col3 = st.columns(3)

    if col1.button("Equipamentos"):
        st.session_state.subdados = "equip"

    if col1.button("Materiais"):
        st.session_state.subdados = "mat"

    if col2.button("Desaguamento"):
        st.session_state.subdados = "desag"

    if col2.button("Horários"):
        st.session_state.subdados = "hor"

    if col3.button("Dias"):
        st.session_state.subdados = "dias"

    if col3.button("Salários"):
        st.session_state.subdados = "sal"

    st.divider()

    if st.session_state.subdados == "equip":
        crud(ARQ_EQUIP, ["Equipamento","Vazao","Consumo","Valor"], "Equipamentos", "equip")

    elif st.session_state.subdados == "mat":
        crud(ARQ_MAT, ["Material","Solidos_InSitu","Solidos_Desaguado"], "Materiais", "mat")

    elif st.session_state.subdados == "desag":
        crud(ARQ_DESAG, ["Tipo"], "Desaguamento", "desag")

    elif st.session_state.subdados == "hor":
        crud(ARQ_HOR, ["Inicio","Fim"], "Horários", "hor")

    elif st.session_state.subdados == "dias":
        crud(ARQ_DIAS, ["Descricao"], "Dias", "dias")

    elif st.session_state.subdados == "sal":
        crud(ARQ_SAL, ["Posicao","Valor_Hora"], "Salários", "sal")

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
        st.rerun()
