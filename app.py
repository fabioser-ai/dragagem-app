import streamlit as st
import pandas as pd

from services.github import salvar_github, carregar_github

st.set_page_config(layout="wide")
st.title("FOS ENGENHARIA LTDA")

# =========================
# ESTILO
# =========================
st.markdown("""
<style>
button[kind="secondary"] {
    height: 80px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# ARQUIVOS
# =========================
ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_DESAG = "data/desaguamento.csv"
ARQ_HOR = "data/horarios.csv"
ARQ_DIAS = "data/dias.csv"
ARQ_FERIAS = "data/ferias.csv"
ARQ_OBRAS = "data/orcamentos.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

# =========================
# ESTADO
# =========================
if "tela" not in st.session_state:
    st.session_state.tela = "menu"

# =========================
# FUNÇÃO CRUD COMPLETA
# =========================
def tela_crud_completa(arquivo, colunas, titulo, voltar, chave):

    st.header(titulo)

    df = carregar_github(arquivo, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=colunas)

    st.dataframe(df)

    st.divider()

    # BOTÃO EDITAR
    if st.button("✏️ Editar / Excluir", key=f"edit_{chave}"):
        st.session_state.tela = f"edit_{chave}"
        return

    st.subheader("Adicionar novo")

    valores = []
    for c in colunas:
        valores.append(st.text_input(c, key=f"{chave}_{c}"))

    if st.button("Adicionar", key=f"add_{chave}"):
        novo = pd.DataFrame([valores], columns=colunas)
        df = pd.concat([df, novo], ignore_index=True)
        salvar_github(df, arquivo, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = voltar


# =========================
# FUNÇÃO TELA EDIÇÃO
# =========================
def tela_edicao(arquivo, colunas, titulo, voltar, chave):

    st.header(f"{titulo} - Edição")

    df = carregar_github(arquivo, TOKEN, REPO)

    if df.empty:
        st.warning("Sem dados")
    else:

        idx_sel = st.selectbox("Selecione", df.index)

        novos_valores = []
        for c in colunas:
            novos_valores.append(
                st.text_input(c, value=str(df.loc[idx_sel, c]), key=f"edit_{chave}_{c}")
            )

        col1, col2 = st.columns(2)

        if col1.button("Salvar"):
            for i, c in enumerate(colunas):
                df.loc[idx_sel, c] = novos_valores[i]

            salvar_github(df, arquivo, TOKEN, REPO)
            st.success("Atualizado!")
            st.rerun()

        if col2.button("Excluir"):
            df = df.drop(idx_sel).reset_index(drop=True)
            salvar_github(df, arquivo, TOKEN, REPO)
            st.warning("Removido!")
            st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = voltar


# =========================
# MENU PRINCIPAL
# =========================
if st.session_state.tela == "menu":

    col1, col2, col3 = st.columns(3)

    if col1.button("📊 ORÇAMENTO", use_container_width=True):
        st.session_state.tela = "orcamento"

    if col1.button("📅 FÉRIAS", use_container_width=True):
        st.session_state.tela = "ferias"

    if col2.button("📈 OBRAS", use_container_width=True):
        st.session_state.tela = "obras"

    if col3.button("📁 DADOS", use_container_width=True):
        st.session_state.tela = "dados"

# =========================
# MENU DADOS
# =========================
elif st.session_state.tela == "dados":

    col1, col2, col3 = st.columns(3)

    if col1.button("🚜 Equipamentos", use_container_width=True):
        st.session_state.tela = "equip"

    if col1.button("🧱 Materiais", use_container_width=True):
        st.session_state.tela = "mat"

    if col2.button("💧 Desaguamento", use_container_width=True):
        st.session_state.tela = "desag"

    if col2.button("⏱ Horários", use_container_width=True):
        st.session_state.tela = "hor"

    if col3.button("📅 Dias", use_container_width=True):
        st.session_state.tela = "dias"

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# CRUD TELAS
# =========================
elif st.session_state.tela == "equip":
    tela_crud_completa(ARQ_EQUIP, ["Equipamento","Vazao","Consumo","Valor"], "Equipamentos", "dados", "equip")

elif st.session_state.tela == "mat":
    tela_crud_completa(ARQ_MAT, ["Material","Solidos_InSitu","Solidos_Desaguado"], "Materiais", "dados", "mat")

elif st.session_state.tela == "desag":
    tela_crud_completa(ARQ_DESAG, ["Tipo"], "Desaguamento", "dados", "desag")

elif st.session_state.tela == "hor":
    tela_crud_completa(ARQ_HOR, ["Inicio","Fim"], "Horários", "dados", "hor")

elif st.session_state.tela == "dias":
    tela_crud_completa(ARQ_DIAS, ["Descricao"], "Dias", "dados", "dias")

# =========================
# TELAS DE EDIÇÃO
# =========================
elif st.session_state.tela == "edit_equip":
    tela_edicao(ARQ_EQUIP, ["Equipamento","Vazao","Consumo","Valor"], "Equipamentos", "equip", "equip")

elif st.session_state.tela == "edit_mat":
    tela_edicao(ARQ_MAT, ["Material","Solidos_InSitu","Solidos_Desaguado"], "Materiais", "mat", "mat")

elif st.session_state.tela == "edit_desag":
    tela_edicao(ARQ_DESAG, ["Tipo"], "Desaguamento", "desag", "desag")

elif st.session_state.tela == "edit_hor":
    tela_edicao(ARQ_HOR, ["Inicio","Fim"], "Horários", "hor", "hor")

elif st.session_state.tela == "edit_dias":
    tela_edicao(ARQ_DIAS, ["Descricao"], "Dias", "dias", "dias")

# =========================
# FÉRIAS
# =========================
elif st.session_state.tela == "ferias":
    st.header("Férias")
    df = carregar_github(ARQ_FERIAS, TOKEN, REPO)
    st.dataframe(df)

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# OBRAS
# =========================
elif st.session_state.tela == "obras":
    st.header("Obras")
    df = carregar_github(ARQ_OBRAS, TOKEN, REPO)
    st.dataframe(df)

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# ORÇAMENTO
# =========================
elif st.session_state.tela == "orcamento":
    st.header("Orçamento (em evolução)")
    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"
