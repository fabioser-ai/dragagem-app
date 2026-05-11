import uuid
from datetime import date, datetime

import pandas as pd
import streamlit as st

from services.github import carregar_github, salvar_github


# ============================================================
# ARQUIVOS
# ============================================================

ARQ_OBRAS = "data/obras.csv"
ARQ_MEDICOES = "data/medicoes.csv"
ARQ_FRENTES = "data/medicoes_frentes.csv"
ARQ_ITENS = "data/medicoes_itens.csv"
ARQ_SERVICOS = "data/medicoes_servicos.csv"


# ============================================================
# COLUNAS
# ============================================================

COL_OBRAS = [
    "obra_id",
    "nome_obra",
    "contratante",
    "contrato",
    "objeto",
    "cidade",
    "status",
    "observacoes",
    "criado_em",
    "atualizado_em",
]

COL_MEDICOES = [
    "medicao_id",
    "obra_id",
    "numero_bm",
    "aditivo",
    "periodo_inicio",
    "periodo_fim",
    "data_bm",
    "dias_uteis_mes",
    "apostilamento_percentual",
    "status",
    "observacoes",
    "criado_em",
    "atualizado_em",
]

COL_FRENTES = [
    "frente_id",
    "medicao_id",
    "nome_frente",
    "dias_trabalhados",
    "observacoes",
    "criado_em",
    "atualizado_em",
]

COL_ITENS = [
    "item_id",
    "medicao_id",
    "frente_id",
    "codigo",
    "descricao",
    "unidade",
    "quantidade",
    "valor_unitario",
    "total",
]

COL_SERVICOS = [
    "codigo",
    "descricao",
    "unidade",
]


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def agora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def novo_id(prefixo):
    return f"{prefixo}_{uuid.uuid4().hex[:10]}"


def moeda(valor):
    try:
        valor = float(valor)
    except:
        valor = 0

    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def carregar_csv(caminho, colunas):
    try:
        df = carregar_github(
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )

        if isinstance(df, str):
            from io import StringIO
            df = pd.read_csv(StringIO(df))

        if df is None:
            df = pd.DataFrame(columns=colunas)

    except:
        df = pd.DataFrame(columns=colunas)

    for c in colunas:
        if c not in df.columns:
            df[c] = None

    return df[colunas]


def salvar_csv(caminho, df):
    try:
        salvar_github(
            df,
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )
        return True

    except Exception as e:
        st.error(f"Erro ao salvar {caminho}: {e}")
        return False


# ============================================================
# CARREGAMENTO
# ============================================================

def carregar_bases():

    obras = carregar_csv(ARQ_OBRAS, COL_OBRAS)

    medicoes = carregar_csv(ARQ_MEDICOES, COL_MEDICOES)

    frentes = carregar_csv(ARQ_FRENTES, COL_FRENTES)

    itens = carregar_csv(ARQ_ITENS, COL_ITENS)

    servicos = carregar_csv(ARQ_SERVICOS, COL_SERVICOS)

    return obras, medicoes, frentes, itens, servicos


# ============================================================
# FLUXO
# ============================================================

def ir_para(etapa):
    st.session_state.etapa_medicoes = etapa
    st.rerun()


# ============================================================
# OBRA
# ============================================================

def tela_obras(obras):

    st.subheader("1. Obra")

    obras_validas = obras.dropna(subset=["obra_id"])

    if not obras_validas.empty:

        mapa = {
            f"{r['nome_obra']} | {r['contrato']}": r["obra_id"]
            for _, r in obras_validas.iterrows()
        }

        obra_label = st.selectbox(
            "Selecionar obra",
            list(mapa.keys()),
        )

        st.session_state.obra_id = mapa[obra_label]

    with st.expander("Cadastrar nova obra"):

        with st.form("nova_obra"):

            nome = st.text_input(
                "Nome da obra",
                value="Contrato 26.171 - Curitiba"
            )

            contratante = st.text_input(
                "Contratante",
                value="Prefeitura Municipal de Curitiba"
            )

            contrato = st.text_input(
                "Contrato",
                value="26.171 - Aditivo 01"
            )

            objeto = st.text_area("Objeto")

            cidade = st.text_input(
                "Cidade",
                value="Curitiba/PR"
            )

            status = st.selectbox(
                "Status",
                ["Ativa", "Concluída", "Suspensa"]
            )

            observacoes = st.text_area("Observações")

            ok = st.form_submit_button("Salvar obra")

        if ok:

            nova = {
                "obra_id": novo_id("obra"),
                "nome_obra": nome,
                "contratante": contratante,
                "contrato": contrato,
                "objeto": objeto,
                "cidade": cidade,
                "status": status,
                "observacoes": observacoes,
                "criado_em": agora(),
                "atualizado_em": agora(),
            }

            obras = pd.concat(
                [obras, pd.DataFrame([nova])],
                ignore_index=True,
            )

            salvar_csv(ARQ_OBRAS, obras)

            st.session_state.obra_id = nova["obra_id"]

            st.success("Obra cadastrada.")

            st.rerun()

    if not obras.empty:

        st.dataframe(
            obras[
                [
                    "nome_obra",
                    "contratante",
                    "contrato",
                    "cidade",
                    "status",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )


# ============================================================
# BM
# ============================================================

def tela_bm(obras, medicoes):

    st.subheader("2. BM")

    obra_id = st.session_state.get("obra_id")

    if not obra_id:
        st.warning("Selecione uma obra.")
        return

    df_obra = medicoes[
        medicoes["obra_id"].astype(str) == str(obra_id)
    ]

    if not df_obra.empty:

        mapa = {
            f"BM {r['numero_bm']}": r["medicao_id"]
            for _, r in df_obra.iterrows()
        }

        bm_label = st.selectbox(
            "Selecionar BM",
            list(mapa.keys()),
        )

        st.session_state.medicao_id = mapa[bm_label]

    with st.expander("Cadastrar novo BM"):

        with st.form("novo_bm"):

            c1, c2, c3 = st.columns(3)

            with c1:
                numero_bm = st.text_input("Número BM", value="04")

            with c2:
                periodo_inicio = st.date_input(
                    "Período início",
                    value=date(2025, 11, 22)
                )

            with c3:
                periodo_fim = st.date_input(
                    "Período fim",
                    value=date(2025, 12, 21)
                )

            dias_uteis = st.number_input(
                "Dias úteis",
                min_value=1,
                value=20,
            )

            apost = st.number_input(
                "Apostilamento (%)",
                value=5.53,
                step=0.01,
            )

            status = st.selectbox(
                "Status",
                ["Rascunho", "Fechado", "Enviado"]
            )

            observacoes = st.text_area("Observações")

            ok = st.form_submit_button("Salvar BM")

        if ok:

            nova = {
                "medicao_id": novo_id("bm"),
                "obra_id": obra_id,
                "numero_bm": numero_bm,
                "aditivo": "",
                "periodo_inicio": str(periodo_inicio),
                "periodo_fim": str(periodo_fim),
                "data_bm": str(periodo_fim),
                "dias_uteis_mes": dias_uteis,
                "apostilamento_percentual": apost,
                "status": status,
                "observacoes": observacoes,
                "criado_em": agora(),
                "atualizado_em": agora(),
            }

            medicoes = pd.concat(
                [medicoes, pd.DataFrame([nova])],
                ignore_index=True,
            )

            salvar_csv(ARQ_MEDICOES, medicoes)

            st.session_state.medicao_id = nova["medicao_id"]

            st.success("BM cadastrado.")

            st.rerun()

    if not df_obra.empty:

        st.dataframe(
            df_obra[
                [
                    "numero_bm",
                    "periodo_inicio",
                    "periodo_fim",
                    "status",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )


# ============================================================
# FRENTES
# ============================================================

def tela_frentes(frentes):

    st.subheader("3. Frentes / Parques")

    medicao_id = st.session_state.get("medicao_id")

    if not medicao_id:
        st.warning("Selecione um BM.")
        return

    df = frentes[
        frentes["medicao_id"].astype(str) == str(medicao_id)
    ]

    if not df.empty:

        mapa = {
            r["nome_frente"]: r["frente_id"]
            for _, r in df.iterrows()
        }

        frente_label = st.selectbox(
            "Selecionar frente",
            list(mapa.keys()),
        )

        st.session_state.frente_id = mapa[frente_label]

    with st.expander("Cadastrar nova frente"):

        with st.form("nova_frente"):

            nome = st.text_input(
                "Nome da frente",
                value="PARQUE BARIGUI"
            )

            dias = st.number_input(
                "Dias trabalhados",
                value=19.0,
            )

            observacoes = st.text_area("Observações")

            ok = st.form_submit_button("Salvar frente")

        if ok:

            nova = {
                "frente_id": novo_id("frente"),
                "medicao_id": medicao_id,
                "nome_frente": nome,
                "dias_trabalhados": dias,
                "observacoes": observacoes,
                "criado_em": agora(),
                "atualizado_em": agora(),
            }

            frentes = pd.concat(
                [frentes, pd.DataFrame([nova])],
                ignore_index=True,
            )

            salvar_csv(ARQ_FRENTES, frentes)

            st.session_state.frente_id = nova["frente_id"]

            st.success("Frente cadastrada.")

            st.rerun()

    if not df.empty:

        st.dataframe(
            df[
                [
                    "nome_frente",
                    "dias_trabalhados",
                    "observacoes",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )


# ============================================================
# MEDIÇÃO VISUAL
# ============================================================

def tela_medicao_visual(frentes, itens, servicos):

    st.subheader("4. Medição")

    frente_id = st.session_state.get("frente_id")

    if not frente_id:
        st.warning("Selecione uma frente.")
        return

    frente_nome = frentes.loc[
        frentes["frente_id"].astype(str) == str(frente_id),
        "nome_frente"
    ]

    if not frente_nome.empty:
        st.info(f"Frente selecionada: {frente_nome.iloc[0]}")

    df_existente = itens[
        itens["frente_id"].astype(str) == str(frente_id)
    ].copy()

    if df_existente.empty:

        df_editor = servicos.copy()

        df_editor["item_id"] = [
            novo_id("item")
            for _ in range(len(df_editor))
        ]

        df_editor["medicao_id"] = st.session_state.get("medicao_id")
        df_editor["frente_id"] = frente_id

        df_editor["quantidade"] = 0.0
        df_editor["valor_unitario"] = 0.0
        df_editor["total"] = 0.0

    else:

        df_editor = df_existente.copy()

    st.markdown("### Planilha de Medição")

    df_editado = st.data_editor(
        df_editor,
        use_container_width=True,
        num_rows="dynamic",
        hide_index=True,
        column_config={
            "item_id": None,
            "medicao_id": None,
            "frente_id": None,

            "codigo": st.column_config.TextColumn(
                "Código"
            ),

            "descricao": st.column_config.TextColumn(
                "Serviço"
            ),

            "unidade": st.column_config.TextColumn(
                "Un"
            ),

            "quantidade": st.column_config.NumberColumn(
                "Quantidade",
                format="%.2f",
            ),

            "valor_unitario": st.column_config.NumberColumn(
                "V.Unit",
                format="%.2f",
            ),

            "total": st.column_config.NumberColumn(
                "Total",
                format="%.2f",
                disabled=True,
            ),
        }
    )

    df_editado["quantidade"] = pd.to_numeric(
        df_editado["quantidade"],
        errors="coerce",
    ).fillna(0)

    df_editado["valor_unitario"] = pd.to_numeric(
        df_editado["valor_unitario"],
        errors="coerce",
    ).fillna(0)

    df_editado["total"] = (
        df_editado["quantidade"]
        * df_editado["valor_unitario"]
    )

    total_frente = df_editado["total"].sum()

    st.metric(
        "Total da frente",
        moeda(total_frente)
    )

    if st.button(
        "Salvar medição",
        use_container_width=True,
    ):

        itens = itens[
            itens["frente_id"].astype(str) != str(frente_id)
        ]

        itens = pd.concat(
            [itens, df_editado[COL_ITENS]],
            ignore_index=True,
        )

        salvar_csv(ARQ_ITENS, itens)

        st.success("Medição salva.")

        st.rerun()


# ============================================================
# RESUMO
# ============================================================

def tela_resumo(frentes, itens, medicoes):

    st.subheader("5. Resumo Financeiro")

    medicao_id = st.session_state.get("medicao_id")

    if not medicao_id:
        st.warning("Selecione um BM.")
        return

    itens_bm = itens[
        itens["medicao_id"].astype(str) == str(medicao_id)
    ].copy()

    if itens_bm.empty:
        st.info("Nenhum item medido.")
        return

    mapa_frentes = {
        r["frente_id"]: r["nome_frente"]
        for _, r in frentes.iterrows()
    }

    itens_bm["frente"] = itens_bm["frente_id"].map(
        mapa_frentes
    )

    resumo = (
        itens_bm
        .groupby("frente")["total"]
        .sum()
        .reset_index()
    )

    subtotal = resumo["total"].sum()

    med_row = medicoes[
        medicoes["medicao_id"].astype(str) == str(medicao_id)
    ]

    apost = 0

    if not med_row.empty:
        apost = float(
            med_row.iloc[0]["apostilamento_percentual"]
        )

    valor_apost = subtotal * (apost / 100)

    total_final = subtotal + valor_apost

    resumo["valor"] = resumo["total"].apply(moeda)

    st.markdown("### Totais por frente")

    st.dataframe(
        resumo[
            [
                "frente",
                "valor",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Subtotal",
        moeda(subtotal)
    )

    c2.metric(
        "Apostilamento",
        moeda(valor_apost)
    )

    c3.metric(
        "Total Final",
        moeda(total_final)
    )


# ============================================================
# NAVEGAÇÃO
# ============================================================

def navegacao():

    etapa = st.session_state.get(
        "etapa_medicoes",
        "obra"
    )

    ordem = [
        "obra",
        "bm",
        "frentes",
        "medicao",
        "resumo",
    ]

    labels = {
        "obra": "1. Obra",
        "bm": "2. BM",
        "frentes": "3. Frentes",
        "medicao": "4. Medição",
        "resumo": "5. Resumo",
    }

    cols = st.columns(len(ordem))

    for i, etapa_nome in enumerate(ordem):

        with cols[i]:

            if etapa_nome == etapa:

                st.button(
                    f"✅ {labels[etapa_nome]}",
                    disabled=True,
                    use_container_width=True,
                )

            else:

                if st.button(
                    labels[etapa_nome],
                    use_container_width=True,
                ):
                    ir_para(etapa_nome)

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        if etapa != "obra":

            idx = ordem.index(etapa)

            if st.button(
                "← Voltar",
                use_container_width=True,
            ):
                ir_para(ordem[idx - 1])

    with c2:

        if st.button(
            "⬅ Menu",
            use_container_width=True,
        ):
            st.session_state.tela = "menu"
            st.rerun()

    with c3:

        if etapa != "resumo":

            idx = ordem.index(etapa)

            if st.button(
                "Próximo →",
                use_container_width=True,
            ):
                ir_para(ordem[idx + 1])


# ============================================================
# PRINCIPAL
# ============================================================

def medicoes():

    st.title("Medições")

    st.caption(
        "Controle de boletins de medição e memória operacional."
    )

    if "etapa_medicoes" not in st.session_state:
        st.session_state.etapa_medicoes = "obra"

    obras, medicoes_df, frentes, itens, servicos = carregar_bases()

    navegacao()

    etapa = st.session_state.etapa_medicoes

    if etapa == "obra":
        tela_obras(obras)

    elif etapa == "bm":
        tela_bm(obras, medicoes_df)

    elif etapa == "frentes":
        tela_frentes(frentes)

    elif etapa == "medicao":
        tela_medicao_visual(
            frentes,
            itens,
            servicos,
        )

    elif etapa == "resumo":
        tela_resumo(
            frentes,
            itens,
            medicoes_df,
        )


def render():
    medicoes()


if __name__ == "__main__":
    medicoes()
