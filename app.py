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
# FUNÇÃO CRUD GENÉRICA
# =========================
def tela_crud_simples(arquivo, colunas, titulo, voltar, chave):

    st.header(titulo)

    df = carregar_github(arquivo, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=colunas)

    st.dataframe(df)

    st.divider()

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
# FUNÇÃO EDIÇÃO GENÉRICA
# =========================
def tela_edicao_simples(arquivo, colunas, titulo, voltar, chave):

    st.header(f"{titulo} - Edição")

    df = carregar_github(arquivo, TOKEN, REPO)

    if df.empty:
        st.warning("Sem dados")
    else:
        idx_sel = st.selectbox("Selecione", df.index)

        novos = []
        for c in colunas:
            novos.append(
                st.text_input(c, value=str(df.loc[idx_sel, c]), key=f"edit_{chave}_{c}")
            )

        col1, col2 = st.columns(2)

        if col1.button("Salvar"):
            for i, c in enumerate(colunas):
                df.loc[idx_sel, c] = novos[i]

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
# EQUIPAMENTOS (COM TIPAGEM CORRETA)
# =========================
elif st.session_state.tela == "equip":

    st.header("Equipamentos")

    df = carregar_github(ARQ_EQUIP, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Equipamento","Vazao","Consumo","Valor"])

    st.dataframe(df)

    st.divider()

    if st.button("✏️ Editar / Excluir"):
        st.session_state.tela = "edit_equip"
        st.rerun()

    st.subheader("Adicionar novo")

    nome = st.text_input("Nome")
    vazao = st.number_input("Vazão", value=1000.0)
    consumo = st.number_input("Consumo", value=60.0)
    valor = st.number_input("Valor", value=1000000.0)

    if st.button("Adicionar"):
        novo = pd.DataFrame([[nome, vazao, consumo, valor]], columns=df.columns)
        df = pd.concat([df, novo], ignore_index=True)
        salvar_github(df, ARQ_EQUIP, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "dados"

# =========================
# EDIÇÃO EQUIPAMENTOS (FIX DO ERRO)
# =========================
elif st.session_state.tela == "edit_equip":

    st.header("Equipamentos - Edição")

    df = carregar_github(ARQ_EQUIP, TOKEN, REPO)

    if df.empty:
        st.warning("Sem dados")
    else:
        equipamento = st.selectbox("Selecione", df["Equipamento"])
        linha = df[df["Equipamento"] == equipamento].iloc[0]

        nome = st.text_input("Nome", value=linha["Equipamento"])
        vazao = st.number_input("Vazão", value=float(linha["Vazao"]))
        consumo = st.number_input("Consumo", value=float(linha["Consumo"]))
        valor = st.number_input("Valor", value=float(linha["Valor"]))

        col1, col2 = st.columns(2)

        if col1.button("Salvar"):
            idx = df["Equipamento"] == equipamento

            df.loc[idx, "Equipamento"] = nome
            df.loc[idx, "Vazao"] = float(vazao)
            df.loc[idx, "Consumo"] = float(consumo)
            df.loc[idx, "Valor"] = float(valor)

            salvar_github(df, ARQ_EQUIP, TOKEN, REPO)
            st.success("Atualizado!")
            st.rerun()

        if col2.button("Excluir"):
            df = df[df["Equipamento"] != equipamento]
            salvar_github(df, ARQ_EQUIP, TOKEN, REPO)
            st.warning("Removido!")
            st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "equip"

# =========================
# OUTROS DADOS (GENÉRICO)
# =========================
elif st.session_state.tela == "mat":
    tela_crud_simples(ARQ_MAT, ["Material","Solidos_InSitu","Solidos_Desaguado"], "Materiais", "dados", "mat")

elif st.session_state.tela == "desag":
    tela_crud_simples(ARQ_DESAG, ["Tipo"], "Desaguamento", "dados", "desag")

elif st.session_state.tela == "hor":
    tela_crud_simples(ARQ_HOR, ["Inicio","Fim"], "Horários", "dados", "hor")

elif st.session_state.tela == "dias":
    tela_crud_simples(ARQ_DIAS, ["Descricao"], "Dias", "dados", "dias")

elif st.session_state.tela == "edit_mat":
    tela_edicao_simples(ARQ_MAT, ["Material","Solidos_InSitu","Solidos_Desaguado"], "Materiais", "mat", "mat")

elif st.session_state.tela == "edit_desag":
    tela_edicao_simples(ARQ_DESAG, ["Tipo"], "Desaguamento", "desag", "desag")

elif st.session_state.tela == "edit_hor":
    tela_edicao_simples(ARQ_HOR, ["Inicio","Fim"], "Horários", "hor", "hor")

elif st.session_state.tela == "edit_dias":
    tela_edicao_simples(ARQ_DIAS, ["Descricao"], "Dias", "dias", "dias")

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
