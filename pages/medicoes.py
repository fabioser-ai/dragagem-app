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
ARQ_MC = "data/medicoes_mc.csv"
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

COL_MC = [
    "mc_id",
    "medicao_id",
    "frente_id",
    "tipo",
    "descricao",
    "comprimento",
    "ast",
    "resultado",
]

COL_ITENS = [
    "item_id",
    "medicao_id",
    "frente_id",
    "codigo",
    "descricao",
    "unidade",
    "origem_mc",
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
# AUXILIARES
# ============================================================

def agora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def novo_id(prefixo):
    return f"{prefixo}_{uuid.uuid4().hex[:10]}"


def moeda(valor):
    try:
        valor = float(valor)
    except Exception:
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

    except Exception:
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


def carregar_bases():
    obras = carregar_csv(ARQ_OBRAS, COL_OBRAS)
    medicoes = carregar_csv(ARQ_MEDICOES, COL_MEDICOES)
    frentes = carregar_csv(ARQ_FRENTES, COL_FRENTES)
    mc = carregar_csv(ARQ_MC, COL_MC)
    itens = carregar_csv(ARQ_ITENS, COL_ITENS)
    servicos = carregar_csv(ARQ_SERVICOS, COL_SERVICOS)

    return obras, medicoes, frentes, mc, itens, servicos


def ir_para(etapa):
    st.session_state.etapa_medicoes = etapa
    st.rerun()


# ============================================================
# ETAPA 1 — OBRA
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
            key="select_obra_medicoes",
        )

        st.session_state.obra_id = mapa[obra_label]

    with st.expander("Cadastrar nova obra", expanded=obras_validas.empty):
        with st.form("nova_obra"):
            nome = st.text_input("Nome da obra")
            contratante = st.text_input("Contratante")
            contrato = st.text_input("Contrato")
            objeto = st.text_area("Objeto")
            cidade = st.text_input("Cidade")

            status = st.selectbox(
                "Status",
                ["Ativa", "Concluída", "Suspensa"],
            )

            observacoes = st.text_area("Observações")
            ok = st.form_submit_button("Salvar obra")

        if ok:
            if not nome.strip():
                st.error("Informe o nome da obra.")
                return

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

            if salvar_csv(ARQ_OBRAS, obras):
                st.session_state.obra_id = nova["obra_id"]
                st.success("Obra cadastrada.")
                st.rerun()

    if not obras_validas.empty:
        st.dataframe(
            obras_validas[
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
# ETAPA 2 — BM
# ============================================================

def tela_bm(obras, medicoes):
    st.subheader("2. BM")

    obra_id = st.session_state.get("obra_id")

    if not obra_id:
        st.warning("Selecione ou cadastre uma obra antes de criar o BM.")
        return

    obra_nome = obras.loc[
        obras["obra_id"].astype(str) == str(obra_id),
        "nome_obra",
    ]

    if not obra_nome.empty:
        st.info(f"Obra selecionada: {obra_nome.iloc[0]}")

    df_obra = medicoes[
        medicoes["obra_id"].astype(str) == str(obra_id)
    ]

    if not df_obra.empty:
        mapa = {
            f"BM {r['numero_bm']} | {r['periodo_inicio']} a {r['periodo_fim']}": r["medicao_id"]
            for _, r in df_obra.iterrows()
        }

        bm_label = st.selectbox(
            "Selecionar BM",
            list(mapa.keys()),
            key="select_bm_medicoes",
        )

        st.session_state.medicao_id = mapa[bm_label]

    with st.expander("Cadastrar novo BM", expanded=df_obra.empty):
        with st.form("novo_bm"):
            c1, c2, c3 = st.columns(3)

            with c1:
                numero_bm = st.text_input("Número BM", value="04")
                aditivo = st.text_input("Aditivo", value="01")

            with c2:
                periodo_inicio = st.date_input(
                    "Período início",
                    value=date.today(),
                )
                periodo_fim = st.date_input(
                    "Período fim",
                    value=date.today(),
                )

            with c3:
                data_bm = st.date_input(
                    "Data BM",
                    value=date.today(),
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
                ["Rascunho", "Fechado", "Enviado", "Aprovado", "Pago"],
            )

            observacoes = st.text_area("Observações")
            ok = st.form_submit_button("Salvar BM")

        if ok:
            nova = {
                "medicao_id": novo_id("bm"),
                "obra_id": obra_id,
                "numero_bm": numero_bm,
                "aditivo": aditivo,
                "periodo_inicio": str(periodo_inicio),
                "periodo_fim": str(periodo_fim),
                "data_bm": str(data_bm),
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

            if salvar_csv(ARQ_MEDICOES, medicoes):
                st.session_state.medicao_id = nova["medicao_id"]
                st.success("BM cadastrado.")
                st.rerun()

    if not df_obra.empty:
        st.dataframe(
            df_obra[
                [
                    "numero_bm",
                    "aditivo",
                    "periodo_inicio",
                    "periodo_fim",
                    "dias_uteis_mes",
                    "status",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )


# ============================================================
# ETAPA 3 — FRENTES
# ============================================================

def tela_frentes(frentes):
    st.subheader("3. Frentes / Parques")

    medicao_id = st.session_state.get("medicao_id")

    if not medicao_id:
        st.warning("Selecione ou cadastre um BM antes de criar frentes.")
        return

    df = frentes[
        frentes["medicao_id"].astype(str) == str(medicao_id)
    ]

    if not df.empty:
        mapa = {
            f"{r['nome_frente']} | {r['dias_trabalhados']} dias": r["frente_id"]
            for _, r in df.iterrows()
        }

        frente_label = st.selectbox(
            "Selecionar frente",
            list(mapa.keys()),
            key="select_frente_medicoes",
        )

        st.session_state.frente_id = mapa[frente_label]

    with st.expander("Cadastrar nova frente", expanded=df.empty):
        with st.form("nova_frente"):
            nome = st.text_input("Nome da frente", value="PARQUE BARIGUI")
            dias = st.number_input(
                "Dias trabalhados",
                min_value=0.0,
                value=19.0,
                step=0.5,
            )
            observacoes = st.text_area("Observações")
            ok = st.form_submit_button("Salvar frente")

        if ok:
            if not nome.strip():
                st.error("Informe o nome da frente.")
                return

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

            if salvar_csv(ARQ_FRENTES, frentes):
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
# ETAPA 4 — MC
# ============================================================

def tela_mc(frentes, mc):
    st.subheader("4. Memória de Cálculo")

    frente_id = st.session_state.get("frente_id")

    if not frente_id:
        st.warning("Selecione ou cadastre uma frente antes de criar a MC.")
        return

    frente_nome = frentes.loc[
        frentes["frente_id"].astype(str) == str(frente_id),
        "nome_frente",
    ]

    if not frente_nome.empty:
        st.info(f"MC - {frente_nome.iloc[0]}")

    df_mc = mc[
        mc["frente_id"].astype(str) == str(frente_id)
    ].copy()

    if df_mc.empty:
        df_mc = pd.DataFrame(
            [
                {
                    "mc_id": novo_id("mc"),
                    "medicao_id": st.session_state.get("medicao_id"),
                    "frente_id": frente_id,
                    "tipo": "Bag AST",
                    "descricao": "Bag 01",
                    "comprimento": 0.0,
                    "ast": 0.0,
                    "resultado": 0.0,
                }
            ]
        )

    for col in ["comprimento", "ast", "resultado"]:
        df_mc[col] = pd.to_numeric(
            df_mc[col],
            errors="coerce",
        ).fillna(0.0)

    df_editado = st.data_editor(
        df_mc,
        use_container_width=True,
        num_rows="dynamic",
        hide_index=True,
        key=f"mc_{frente_id}",
        column_config={
            "mc_id": None,
            "medicao_id": None,
            "frente_id": None,
            "tipo": st.column_config.TextColumn("Tipo"),
            "descricao": st.column_config.TextColumn("Descrição"),
            "comprimento": st.column_config.NumberColumn(
                "Comprimento",
                format="%.2f",
            ),
            "ast": st.column_config.NumberColumn(
                "AST",
                format="%.2f",
            ),
            "resultado": st.column_config.NumberColumn(
                "Resultado",
                format="%.2f",
                disabled=True,
            ),
        },
    )

    df_editado["comprimento"] = pd.to_numeric(
        df_editado["comprimento"],
        errors="coerce",
    ).fillna(0.0)

    df_editado["ast"] = pd.to_numeric(
        df_editado["ast"],
        errors="coerce",
    ).fillna(0.0)

    df_editado["resultado"] = (
        df_editado["comprimento"]
        * df_editado["ast"]
    )

    total_mc = df_editado["resultado"].sum()

    st.metric("Resultado total MC", f"{total_mc:,.2f}")

    if st.button("Salvar memória de cálculo", use_container_width=True):
        mc = mc[
            mc["frente_id"].astype(str) != str(frente_id)
        ]

        mc = pd.concat(
            [mc, df_editado[COL_MC]],
            ignore_index=True,
        )

        if salvar_csv(ARQ_MC, mc):
            st.success("MC salva com sucesso.")
            st.rerun()


# ============================================================
# ETAPA 5 — MEDIÇÃO FINANCEIRA
# ============================================================

def tela_medicao(frentes, mc, itens, servicos):
    st.subheader("5. Medição Financeira")

    frente_id = st.session_state.get("frente_id")

    if not frente_id:
        st.warning("Selecione uma frente.")
        return

    df_mc = mc[
        mc["frente_id"].astype(str) == str(frente_id)
    ].copy()

    if df_mc.empty:
        st.info("Cadastre primeiro a memória de cálculo.")
        return

    df_mc["resultado"] = pd.to_numeric(
        df_mc["resultado"],
        errors="coerce",
    ).fillna(0.0)

    quantidade_total = df_mc["resultado"].sum()

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
        df_editor["origem_mc"] = "MC"
        df_editor["quantidade"] = quantidade_total
        df_editor["valor_unitario"] = 0.0
        df_editor["total"] = 0.0

    else:
        df_editor = df_existente.copy()

    for col in ["quantidade", "valor_unitario", "total"]:
        df_editor[col] = pd.to_numeric(
            df_editor[col],
            errors="coerce",
        ).fillna(0.0)

    df_editado = st.data_editor(
        df_editor,
        use_container_width=True,
        num_rows="dynamic",
        hide_index=True,
        key=f"medicao_{frente_id}",
        column_config={
            "item_id": None,
            "medicao_id": None,
            "frente_id": None,
            "codigo": st.column_config.TextColumn("Código"),
            "descricao": st.column_config.TextColumn("Serviço"),
            "unidade": st.column_config.TextColumn("Un"),
            "origem_mc": st.column_config.TextColumn("Origem"),
            "quantidade": st.column_config.NumberColumn(
                "Quantidade",
                format="%.2f",
                disabled=True,
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
        },
    )

    df_editado["valor_unitario"] = pd.to_numeric(
        df_editado["valor_unitario"],
        errors="coerce",
    ).fillna(0.0)

    df_editado["quantidade"] = pd.to_numeric(
        df_editado["quantidade"],
        errors="coerce",
    ).fillna(0.0)

    df_editado["total"] = (
        df_editado["quantidade"]
        * df_editado["valor_unitario"]
    )

    total_frente = df_editado["total"].sum()

    st.metric("Total da frente", moeda(total_frente))

    if st.button("Salvar medição financeira", use_container_width=True):
        itens = itens[
            itens["frente_id"].astype(str) != str(frente_id)
        ]

        itens = pd.concat(
            [itens, df_editado[COL_ITENS]],
            ignore_index=True,
        )

        if salvar_csv(ARQ_ITENS, itens):
            st.success("Medição salva.")
            st.rerun()


# ============================================================
# ETAPA 6 — RESUMO
# ============================================================

def tela_resumo(frentes, itens, medicoes):
    st.subheader("6. Resumo Financeiro")

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

    itens_bm["total"] = pd.to_numeric(
        itens_bm["total"],
        errors="coerce",
    ).fillna(0.0)

    mapa_frentes = {
        r["frente_id"]: r["nome_frente"]
        for _, r in frentes.iterrows()
    }

    itens_bm["frente"] = itens_bm["frente_id"].map(mapa_frentes)

    resumo = (
        itens_bm
        .groupby("frente", dropna=False)["total"]
        .sum()
        .reset_index()
    )

    subtotal = resumo["total"].sum()

    med_row = medicoes[
        medicoes["medicao_id"].astype(str) == str(medicao_id)
    ]

    apost = 0.0

    if not med_row.empty:
        try:
            apost = float(med_row.iloc[0]["apostilamento_percentual"])
        except Exception:
            apost = 0.0

    valor_apost = subtotal * (apost / 100)
    total_final = subtotal + valor_apost

    resumo["valor"] = resumo["total"].apply(moeda)

    st.dataframe(
        resumo[["frente", "valor"]],
        use_container_width=True,
        hide_index=True,
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Subtotal", moeda(subtotal))
    c2.metric("Apostilamento", moeda(valor_apost))
    c3.metric("Total Final", moeda(total_final))


# ============================================================
# NAVEGAÇÃO
# ============================================================

def navegacao():
    etapa = st.session_state.get("etapa_medicoes", "obra")

    ordem = [
        "obra",
        "bm",
        "frentes",
        "mc",
        "medicao",
        "resumo",
    ]

    labels = {
        "obra": "1. Obra",
        "bm": "2. BM",
        "frentes": "3. Frentes",
        "mc": "4. MC",
        "medicao": "5. Medição",
        "resumo": "6. Resumo",
    }

    st.markdown("### Fluxo da medição")

    cols = st.columns(len(ordem))

    for i, etapa_nome in enumerate(ordem):
        with cols[i]:
            ativo = etapa_nome == etapa

            st.button(
                f"{'✅ ' if ativo else ''}{labels[etapa_nome]}",
                disabled=ativo,
                use_container_width=True,
                key=f"barra_medicoes_{etapa_nome}",
            )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        if etapa != "obra":
            idx = ordem.index(etapa)

            if st.button("← Voltar", use_container_width=True):
                ir_para(ordem[idx - 1])

    with c2:
        if st.button("⬅ Menu", use_container_width=True):
            st.session_state.tela = "menu"
            st.rerun()

    with c3:
        if etapa != "resumo":
            idx = ordem.index(etapa)

            if st.button("Próximo →", use_container_width=True):
                ir_para(ordem[idx + 1])


# ============================================================
# PRINCIPAL
# ============================================================

def medicoes():
    st.title("Medições")

    st.caption(
        "Controle técnico e financeiro de medições."
    )

    if "etapa_medicoes" not in st.session_state:
        st.session_state.etapa_medicoes = "obra"

    (
        obras,
        medicoes_df,
        frentes,
        mc,
        itens,
        servicos,
    ) = carregar_bases()

    navegacao()

    etapa = st.session_state.etapa_medicoes

    if etapa == "obra":
        tela_obras(obras)

    elif etapa == "bm":
        tela_bm(obras, medicoes_df)

    elif etapa == "frentes":
        tela_frentes(frentes)

    elif etapa == "mc":
        tela_mc(frentes, mc)

    elif etapa == "medicao":
        tela_medicao(
            frentes,
            mc,
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
