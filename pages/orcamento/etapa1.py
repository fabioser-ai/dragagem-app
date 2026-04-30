import streamlit as st
import pandas as pd
from datetime import datetime
from services.github import carregar_github, salvar_github

# =========================
# ARQUIVOS
# =========================
ARQ_EQUIP = "data/equipamentos.csv"
ARQ_MAT = "data/materiais.csv"
ARQ_OBRAS = "data/orcamentos.csv"

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]


# =========================
# FUNÇÕES AUXILIARES
# =========================
def salvar_rascunho_orcamento(dados):
    try:
        df = carregar_github(ARQ_OBRAS, TOKEN, REPO)
    except Exception:
        df = pd.DataFrame()

    if df.empty:
        df = pd.DataFrame()

    codigo = dados.get("Codigo")

    if not codigo:
        st.error("Código do orçamento não encontrado. Volte para a Etapa 0.")
        st.stop()

    if "Codigo" in df.columns and codigo in df["Codigo"].astype(str).values:
        idx = df[df["Codigo"].astype(str) == str(codigo)].index[0]

        for k, v in dados.items():
            df.loc[idx, k] = v
    else:
        df = pd.concat([df, pd.DataFrame([dados])], ignore_index=True)

    salvar_github(df, ARQ_OBRAS, TOKEN, REPO)


def obter(dados, chave, padrao=None):
    return dados.get(chave, dados.get(chave.lower(), padrao))


# =========================
# ETAPA 1
# =========================
def etapa1():

    st.header("Cálculo de Produção da Draga")

    if "orcamento" not in st.session_state:
        st.warning("Volte para a etapa anterior.")
        return

    dados = st.session_state.orcamento

    # =========================
    # CARREGAR BASES
    # =========================
    df_equip = carregar_github(ARQ_EQUIP, TOKEN, REPO)
    df_mat = carregar_github(ARQ_MAT, TOKEN, REPO)

    if df_equip.empty or df_mat.empty:
        st.error("Bases de equipamentos ou materiais vazias.")
        return

    # =========================
    # VALIDAÇÕES DE CAMPOS DA ETAPA 0
    # =========================
    material_orcamento = obter(dados, "Material")
    desag_orcamento = obter(dados, "Desag")
    horario_orcamento = obter(dados, "Horario")
    dias_orcamento = obter(dados, "Dias")
    volume_orcamento = float(obter(dados, "Volume", 0) or 0)
    desnivel_bombeamento = float(obter(dados, "Desnivel_Bombeamento", 0) or 0)
    flutuante = float(obter(dados, "Flutuante", 0) or 0)
    terrestre = float(obter(dados, "Terrestre", 0) or 0)

    if not material_orcamento:
        st.error("Material não encontrado no orçamento. Volte para a Etapa 0.")
        return

    if not desag_orcamento:
        st.error("Tipo de desaguamento não encontrado no orçamento. Volte para a Etapa 0.")
        return

    if not horario_orcamento:
        st.error("Horário de trabalho não encontrado no orçamento. Volte para a Etapa 0.")
        return

    if not dias_orcamento:
        st.error("Dias de trabalho não encontrados no orçamento. Volte para a Etapa 0.")
        return

    st.info(
        f"Material: {material_orcamento} | "
        f"Desaguamento: {desag_orcamento} | "
        f"Distância total: {flutuante + terrestre:.0f} m | "
        f"Desnível: {desnivel_bombeamento:.1f} m"
    )

    # =========================
    # PRODUÇÃO POR HORA
    # =========================
    st.subheader("Produção por Hora")

    draga_default = obter(dados, "Draga", "")

    lista_dragas = df_equip["Equipamento"].astype(str).tolist()
    idx_draga = lista_dragas.index(draga_default) if draga_default in lista_dragas else 0

    draga = st.selectbox(
        "Selecionar draga",
        df_equip["Equipamento"],
        index=idx_draga,
    )

    linha_equip_df = df_equip[df_equip["Equipamento"].astype(str) == str(draga)]

    if linha_equip_df.empty:
        st.error("Draga selecionada não encontrada na base de equipamentos.")
        return

    linha_equip = linha_equip_df.iloc[0]

    # =========================
    # VAZÃO
    # =========================
    vazao_base = float(linha_equip["Vazao"])
    draga_salva = obter(dados, "Draga", "")

    if str(draga_salva) == str(draga):
        vazao_valor = float(obter(dados, "Vazao", vazao_base) or vazao_base)
    else:
        vazao_valor = vazao_base

    vazao = st.number_input(
        "Vazão (m³/h)",
        value=vazao_valor,
        key=f"vazao_{draga}",
    )

    if vazao != vazao_base:
        st.warning("Vazão alterada manualmente.")

    # =========================
    # CONCENTRAÇÃO
    # =========================
    linha_mat_df = df_mat[df_mat["Material"].astype(str) == str(material_orcamento)]

    if linha_mat_df.empty:
        st.error(f"Material '{material_orcamento}' não encontrado na base de materiais.")
        return

    linha_mat = linha_mat_df.iloc[0]
    conc_base = float(linha_mat["Solidos_InSitu"]) / 100
    concentracao_valor = float(obter(dados, "Concentracao", conc_base) or conc_base)

    concentracao = st.number_input(
        "Concentração",
        value=concentracao_valor,
        key="concentracao_etapa1",
    )

    if concentracao != conc_base:
        st.warning("Concentração alterada manualmente.")

    # =========================
    # EFICIÊNCIA
    # =========================
    eficiencia_map = {
        "Geobag": 0.85,
        "Centrífuga": 0.90,
        "Bombeamento direto": 0.95,
        "Bacia ecológica": 0.80,
    }

    ef_base = eficiencia_map.get(str(desag_orcamento), 0.85)
    eficiencia_valor = float(obter(dados, "Eficiencia", ef_base) or ef_base)

    eficiencia = st.number_input(
        "Eficiência",
        value=eficiencia_valor,
        key="eficiencia_etapa1",
    )

    if eficiencia != ef_base:
        st.warning("Eficiência alterada manualmente.")

    # Cálculo produção hora
    producao_hora = vazao * eficiencia * concentracao

    st.code(f"{vazao} × {eficiencia} × {concentracao}")
    st.success(f"Produção por hora: {producao_hora:.2f} m³/h")

    # =========================
    # HORAS TRABALHADAS
    # =========================
    st.subheader("Horas Trabalhadas no Mês")

    try:
        inicio, fim = str(horario_orcamento).split(" - ")
        h1 = int(inicio.split(":")[0])
        h2 = int(fim.split(":")[0])

        horas_dia_bruto = h2 - h1
        horas_dia = max(horas_dia_bruto - 1, 0)  # desconto almoço

    except Exception:
        horas_dia_bruto = 8
        horas_dia = 7

    st.write(f"Horas brutas/dia: {horas_dia_bruto}")
    st.write("(-1h almoço)")
    st.success(f"Horas líquidas/dia: {horas_dia}")

    mapa_dias = {
        "Segunda a Sexta": 22,
        "Segunda a Sábado": 26,
        "Segunda a Domingo": 30,
    }

    dias_mes = mapa_dias.get(str(dias_orcamento), 22)

    st.write(f"Dias trabalhados no mês: {dias_mes}")

    horas_mes = horas_dia * dias_mes

    st.success(f"Horas mensais disponíveis: {horas_mes}")

    # =========================
    # PRODUÇÃO MENSAL
    # =========================
    st.subheader("Produção Mensal da Draga")

    producao_mensal = producao_hora * horas_mes

    st.code(f"{producao_hora:.2f} × {horas_mes}")
    st.success(f"Produção mensal: {producao_mensal:.2f} m³")

    # =========================
    # PRAZO
    # =========================
    st.subheader("Prazo da Obra")

    if producao_mensal > 0:
        meses = volume_orcamento / producao_mensal
    else:
        meses = 0

    st.code(f"{volume_orcamento} ÷ {producao_mensal:.2f}")
    st.success(f"Prazo estimado: {meses:.2f} meses")

    # =========================
    # ATUALIZA SESSION STATE
    # =========================
    dados_atualizados = {
        "Draga": draga,
        "Vazao": vazao,
        "Eficiencia": eficiencia,
        "Concentracao": concentracao,
        "Producao_Hora": producao_hora,
        "Horas_Dia": horas_dia,
        "Dias_Mes": dias_mes,
        "Horas_Mes": horas_mes,
        "Producao_Mensal": producao_mensal,
        "Prazo_Meses": meses,
        "Status": "Rascunho",
        "Etapa_Atual": "Etapa 1",
        "Ultima_Atualizacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    st.session_state.orcamento.update(dados_atualizados)

    # =========================
    # NAVEGAÇÃO
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar", key="voltar_etapa1"):
        st.session_state.tela = "orcamento_etapa0"
        st.rerun()

    if col2.button("Salvar e continuar", key="continuar_etapa1"):
        salvar_rascunho_orcamento(st.session_state.orcamento)
        st.session_state.tela = "orcamento2"
        st.rerun()
