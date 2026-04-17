import streamlit as st
import pandas as pd

from services.github import salvar_github, carregar_github

st.set_page_config(layout="wide")
st.title("FOS ENGENHARIA LTDA")

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
# FUNÇÕES CRUD
# =========================
def tela_crud_simples(arquivo, colunas, titulo, voltar, chave):
    st.header(titulo)
    df = carregar_github(arquivo, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=colunas)

    st.dataframe(df)

    if st.button("✏️ Editar / Excluir", key=f"edit_{chave}"):
        st.session_state.tela = f"edit_{chave}"
        st.rerun()

    st.subheader("Adicionar novo")
    valores = [st.text_input(c, key=f"{chave}_{c}") for c in colunas]

    if st.button("Adicionar", key=f"add_{chave}"):
        df.loc[len(df)] = valores
        salvar_github(df, arquivo, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = voltar


def tela_edicao_simples(arquivo, colunas, titulo, voltar, chave):
    st.header(f"{titulo} - Edição")
    df = carregar_github(arquivo, TOKEN, REPO)

    if df.empty:
        st.warning("Sem dados")
        return

    idx = st.selectbox("Selecione", df.index)
    linha = df.loc[idx]

    novos = [st.text_input(c, value=str(linha[c]), key=f"edit_{chave}_{c}") for c in colunas]

    col1, col2 = st.columns(2)

    if col1.button("Salvar"):
        df.loc[idx] = novos
        salvar_github(df, arquivo, TOKEN, REPO)
        st.success("Atualizado!")
        st.rerun()

    if col2.button("Excluir"):
        df = df.drop(idx).reset_index(drop=True)
        salvar_github(df, arquivo, TOKEN, REPO)
        st.warning("Removido!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = voltar

# =========================
# MENU
# =========================
if st.session_state.tela == "menu":

    col1, col2, col3 = st.columns(3)

    if col1.button("📊 ORÇAMENTO"):
        st.session_state.tela = "orcamento"

    if col1.button("📅 FÉRIAS"):
        st.session_state.tela = "ferias"

    if col2.button("📈 OBRAS"):
        st.session_state.tela = "obras"

    if col3.button("📁 DADOS"):
        st.session_state.tela = "dados"

# =========================
# DADOS
# =========================
elif st.session_state.tela == "dados":

    col1, col2, col3 = st.columns(3)

    if col1.button("Equipamentos"):
        st.session_state.tela = "equip"

    if col1.button("Materiais"):
        st.session_state.tela = "mat"

    if col2.button("Desaguamento"):
        st.session_state.tela = "desag"

    if col2.button("Horários"):
        st.session_state.tela = "hor"

    if col3.button("Dias"):
        st.session_state.tela = "dias"

    if st.button("⬅ Voltar"):
        st.session_state.tela = "menu"

# =========================
# EQUIPAMENTOS
# =========================
elif st.session_state.tela == "equip":
    st.header("Equipamentos")
    df = carregar_github(ARQ_EQUIP, TOKEN, REPO)

    if df.empty:
        df = pd.DataFrame(columns=["Equipamento","Vazao","Consumo","Valor"])

    st.dataframe(df)

    if st.button("✏️ Editar / Excluir"):
        st.session_state.tela = "edit_equip"
        st.rerun()

    nome = st.text_input("Nome")
    vazao = st.number_input("Vazão", value=1000.0)
    consumo = st.number_input("Consumo", value=60.0)
    valor = st.number_input("Valor", value=1000000.0)

    if st.button("Adicionar"):
        df.loc[len(df)] = [nome, vazao, consumo, valor]
        salvar_github(df, ARQ_EQUIP, TOKEN, REPO)
        st.success("Salvo!")
        st.rerun()

    if st.button("⬅ Voltar"):
        st.session_state.tela = "dados"

elif st.session_state.tela == "edit_equip":
    st.header("Equipamentos - Edição")
    df = carregar_github(ARQ_EQUIP, TOKEN, REPO)

    equipamento = st.selectbox("Selecione", df["Equipamento"])
    linha = df[df["Equipamento"] == equipamento].iloc[0]

    nome = st.text_input("Nome", value=linha["Equipamento"])
    vazao = st.number_input("Vazão", value=float(linha["Vazao"]))
    consumo = st.number_input("Consumo", value=float(linha["Consumo"]))
    valor = st.number_input("Valor", value=float(linha["Valor"]))

    if st.button("Salvar"):
        idx = df["Equipamento"] == equipamento
        df.loc[idx] = [nome, vazao, consumo, valor]
        salvar_github(df, ARQ_EQUIP, TOKEN, REPO)
        st.success("Atualizado!")
        st.rerun()

    if st.button("Excluir"):
        df = df[df["Equipamento"] != equipamento]
        salvar_github(df, ARQ_EQUIP, TOKEN, REPO)
        st.warning("Removido!")
        st.rerun()

# =========================
# ORÇAMENTO ETAPA 1
# =========================
elif st.session_state.tela == "orcamento":

    st.header("Orçamento - Etapa 1")

    df_equip = carregar_github(ARQ_EQUIP, TOKEN, REPO)
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)
    df_desag = carregar_github(ARQ_DESAG, TOKEN, REPO)

    draga = st.selectbox("Draga", df_equip["Equipamento"])
    dados = df_equip[df_equip["Equipamento"] == draga].iloc[0]

    vazao = st.number_input("Vazão", value=float(dados["Vazao"]))
    volume = st.number_input("Volume")

    material = st.selectbox("Material", df_mat["Material"])
    desag = st.selectbox("Desaguamento", df_desag["Tipo"])

    if st.button("Continuar"):
        st.session_state.orcamento = {
            "vazao": vazao,
            "volume": volume,
            "material": material,
            "desag": desag
        }
        st.session_state.tela = "orcamento2"
        st.rerun()

# =========================
# ORÇAMENTO ETAPA 2 (COM CÁLCULO EXPLICADO)
# =========================
elif st.session_state.tela == "orcamento2":

    st.header("Orçamento - Produção")

    dados = st.session_state.orcamento
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)

    linha = df_mat[df_mat["Material"] == dados["material"]].iloc[0]
    concentracao = float(linha["Solidos_InSitu"]) / 100

    eficiencia_map = {
        "Geobag": 0.85,
        "Centrífuga": 0.90,
        "Bombeamento direto": 0.95,
        "Bacia ecológica": 0.80
    }

    eficiencia = eficiencia_map.get(dados["desag"], 0.85)

    vazao_real = dados["vazao"] * eficiencia * concentracao

    # =========================
    # EXIBIÇÃO
    # =========================
    st.subheader("Cálculo da Vazão Real")

    st.write(f"Vazão da draga: {dados['vazao']:.2f} m³/h")
    st.write(f"Eficiência: {eficiencia:.2f}")
    st.write(f"Concentração: {concentracao:.2f}")

    st.markdown("### Fórmula aplicada")
    st.code("Vazão Real = Vazão × Eficiência × Concentração")

    st.markdown("### Substituindo valores")
    st.code(f"{dados['vazao']:.2f} × {eficiencia:.2f} × {concentracao:.2f}")

    st.markdown("### Resultado final")
    st.success(f"Vazão Real = {vazao_real:.2f} m³/h")

    if st.button("⬅ Voltar"):
        st.session_state.tela = "orcamento"
        st.rerun()
