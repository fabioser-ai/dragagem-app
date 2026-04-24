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
# FORMATAR MOEDA BR
# =========================
def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# =========================
# PARSE MOEDA (BR → FLOAT)
# =========================
def parse_moeda(valor):

    if pd.isna(valor) or valor == "":
        return None

    valor = str(valor).strip()
    valor = valor.replace("R$", "").replace(" ", "")
    valor = valor.replace(".", "").replace(",", ".")

    try:
        return float(valor)
    except:
        return None

# =========================
# CONVERSÃO COM VALIDAÇÃO
# =========================
def converter_valores(colunas, valores):

    valores_convertidos = []

    for i, c in enumerate(colunas):
        valor = valores[i]

        if c.lower() in [
            "vazao",
            "consumo",
            "valor",
            "valor_hora",
            "solidos_insitu",
            "solidos_desaguado"
        ]:
            convertido = parse_moeda(valor)

            if convertido is None:
                st.error(f"Valor inválido para '{c}': {valor}")
                return None

            valor = convertido

        valores_convertidos.append(valor)

    return valores_convertidos

# =========================
# CRUD GENÉRICO
# =========================
def crud(arquivo, colunas, titulo, chave):

    st.subheader(titulo)

    df = carregar_github(arquivo, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=colunas)

    # garante tipo numérico
    for col in df.columns:
        if col.lower() in ["valor", "valor_hora", "vazao", "consumo"]:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)

    # exibição formatada
    df_display = df.copy()
    for col in df_display.columns:
        if col.lower() in ["valor", "valor_hora", "consumo"]:
            df_display[col] = df_display[col].apply(formatar_real)

    st.dataframe(df_display, use_container_width=True)

    # =========================
    # EDITAR
    # =========================
    if not df.empty:

        idx = st.selectbox("Selecionar para editar", df.index, key=f"sel_{chave}")
        linha = df.loc[idx]

        novos = []

        for c in colunas:

            if c.lower() in ["valor", "valor_hora", "consumo"]:
                valor_atual = formatar_real(linha[c])
            else:
                valor_atual = str(linha[c])

            novos.append(
                st.text_input(c, value=valor_atual, key=f"{chave}_{c}")
            )

        col1, col2 = st.columns(2)

        if col1.button("Salvar", key=f"save_{chave}"):

            novos_convertidos = converter_valores(colunas, novos)

            if novos_convertidos is None:
                return

            for i, c in enumerate(colunas):
                df.at[idx, c] = novos_convertidos[i]

            salvar_github(df, arquivo, TOKEN, REPO)

            st.success("Atualizado com sucesso!")
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

        valores_convertidos = converter_valores(colunas, valores)

        if valores_convertidos is None:
            return

        df.loc[len(df)] = valores_convertidos

        salvar_github(df, arquivo, TOKEN, REPO)

        st.success("Adicionado com sucesso!")
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
