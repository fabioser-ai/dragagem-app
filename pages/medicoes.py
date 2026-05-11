import json
import uuid
from datetime import date, datetime

import pandas as pd
import streamlit as st

from services.github import carregar_github, salvar_github


ARQ_OBRAS = "data/obras.csv"
ARQ_MEDICOES = "data/medicoes.csv"
ARQ_FRENTES = "data/medicoes_frentes.csv"
ARQ_ITENS = "data/medicoes_itens.csv"


COL_OBRAS = [
    "obra_id", "nome_obra", "contratante", "contrato", "objeto", "cidade",
    "status", "observacoes", "criado_em", "atualizado_em",
]

COL_MEDICOES = [
    "medicao_id", "obra_id", "numero_bm", "aditivo", "periodo_inicio",
    "periodo_fim", "data_bm", "dias_uteis_mes", "apostilamento_percentual",
    "status", "observacoes", "criado_em", "atualizado_em",
]

COL_FRENTES = [
    "frente_id", "medicao_id", "nome_frente", "dias_trabalhados",
    "observacoes", "criado_em", "atualizado_em",
]

COL_ITENS = [
    "item_id", "medicao_id", "frente_id", "codigo", "descricao", "unidade",
    "valor_unitario", "tipo_calculo", "quantidade_manual", "comprimento_total",
    "dias_uteis_mes", "dias_trabalhados", "horas_dia", "volume_desaguado",
    "st_des", "st_br", "volume_anterior", "custo_nf", "bdi_percentual",
    "reajuste_percentual", "parametros_json", "quantidade_calculada",
    "quantidade_medida", "valor_total", "observacoes", "criado_em", "atualizado_em",
]


TIPOS_CALCULO = {
    "manual": "Manual: quantidade informada diretamente",
    "proporcional_dias": "Proporcional por dias: base ÷ dias úteis × dias trabalhados",
    "horas": "Horas: dias trabalhados × horas/dia",
    "volume_bag": "Volume de bag: comprimento × AST",
    "volume_lodo_dragado": "Volume lodo dragado: VLdes × %STdes ÷ %STbr - volume anterior",
    "custo_para_quantidade": "Custo convertido em quantidade: custo final ÷ valor unitário",
}


def agora_iso():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def novo_id(prefixo):
    return f"{prefixo}_{uuid.uuid4().hex[:10]}"


def _df_vazio(colunas):
    return pd.DataFrame(columns=colunas)


def num(v, padrao=0.0):
    try:
        if v is None or v == "":
            return padrao
        if pd.isna(v):
            return padrao
        return float(v)
    except Exception:
        return padrao


def moeda(v):
    return f"R$ {num(v):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def normalizar_colunas(df, tipo):
    if df is None or not isinstance(df, pd.DataFrame):
        return df

    mapas = {
        "obras": {
            "id_obra": "obra_id",
            "nome": "nome_obra",
        },
        "medicoes": {
            "id_medicao": "medicao_id",
            "id_obra": "obra_id",
            "bm": "numero_bm",
            "data_emissao": "data_bm",
        },
        "frentes": {
            "id_frente": "frente_id",
            "id_medicao": "medicao_id",
        },
        "itens": {
            "id_item": "item_id",
            "id_frente": "frente_id",
            "codigo_item": "codigo",
            "custo_unitario": "valor_unitario",
            "metragem": "comprimento_total",
            "vl_des": "volume_desaguado",
            "perc_st_des": "st_des",
            "perc_st_br": "st_br",
            "bdi": "bdi_percentual",
        },
    }

    for antiga, nova in mapas.get(tipo, {}).items():
        if antiga in df.columns and nova not in df.columns:
            df[nova] = df[antiga]

    return df


def carregar_csv(caminho, colunas, tipo):
    try:
        df = carregar_github(
            caminho,
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )
    except Exception:
        df = _df_vazio(colunas)

    if df is None:
        df = _df_vazio(colunas)

    if isinstance(df, str):
        try:
            from io import StringIO
            df = pd.read_csv(StringIO(df))
        except Exception:
            df = _df_vazio(colunas)

    if not isinstance(df, pd.DataFrame):
        df = _df_vazio(colunas)

    df = normalizar_colunas(df, tipo)

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


def calcular_item(row):
    tipo = row.get("tipo_calculo", "manual")
    valor_unitario = num(row.get("valor_unitario"))
    quantidade = 0.0

    if tipo == "manual":
        quantidade = num(row.get("quantidade_manual"))

    elif tipo == "proporcional_dias":
        base = num(row.get("comprimento_total")) or num(row.get("quantidade_manual"))
        dias_uteis = num(row.get("dias_uteis_mes"), 1)
        dias_trab = num(row.get("dias_trabalhados"))
        quantidade = (base / dias_uteis * dias_trab) if dias_uteis else 0.0

    elif tipo == "horas":
        quantidade = num(row.get("dias_trabalhados")) * num(row.get("horas_dia"))

    elif tipo == "volume_bag":
        total = 0.0
        try:
            params = json.loads(row.get("parametros_json") or "[]")
            if isinstance(params, list):
                for b in params:
                    total += num(b.get("comprimento")) * num(b.get("ast"))
        except Exception:
            total = 0.0
        quantidade = total

    elif tipo == "volume_lodo_dragado":
        vl_des = num(row.get("volume_desaguado"))
        st_des = num(row.get("st_des"))
        st_br = num(row.get("st_br"))
        anterior = num(row.get("volume_anterior"))
        vld_total = (vl_des * st_des / st_br) if st_br else 0.0
        quantidade = max(vld_total - anterior, 0.0)

    elif tipo == "custo_para_quantidade":
        custo_nf = num(row.get("custo_nf"))
        bdi = num(row.get("bdi_percentual"))
        reajuste = num(row.get("reajuste_percentual"))
        custo_com_bdi = custo_nf * (1 + bdi)
        custo_final = custo_com_bdi * (1 - reajuste)
        quantidade = (custo_final / valor_unitario) if valor_unitario else 0.0

    valor_total = quantidade * valor_unitario
    return quantidade, valor_total


def recalcular_itens(df_itens):
    if df_itens.empty:
        return df_itens

    df = df_itens.copy()
    quantidades = []
    totais = []

    for _, row in df.iterrows():
        q, vt = calcular_item(row)
        quantidades.append(q)
        totais.append(vt)

    df["quantidade_calculada"] = quantidades
    df["quantidade_medida"] = quantidades
    df["valor_total"] = totais

    return df


def carregar_bases():
    obras = carregar_csv(ARQ_OBRAS, COL_OBRAS, "obras")
    medicoes = carregar_csv(ARQ_MEDICOES, COL_MEDICOES, "medicoes")
    frentes = carregar_csv(ARQ_FRENTES, COL_FRENTES, "frentes")
    itens = carregar_csv(ARQ_ITENS, COL_ITENS, "itens")
    return obras, medicoes, frentes, recalcular_itens(itens)


def salvar_bases(obras=None, medicoes=None, frentes=None, itens=None):
    ok = True

    if obras is not None:
        ok = salvar_csv(ARQ_OBRAS, obras) and ok
    if medicoes is not None:
        ok = salvar_csv(ARQ_MEDICOES, medicoes) and ok
    if frentes is not None:
        ok = salvar_csv(ARQ_FRENTES, frentes) and ok
    if itens is not None:
        ok = salvar_csv(ARQ_ITENS, recalcular_itens(itens)) and ok

    return ok


def opcoes_obras(obras):
    if obras.empty:
        return {}

    obras_validas = obras[obras["obra_id"].notna()].copy()

    if obras_validas.empty:
        return {}

    return {
        f"{r['nome_obra']} | {r['contrato']}": r["obra_id"]
        for _, r in obras_validas.iterrows()
    }


def opcoes_medicoes(medicoes, obra_id):
    if not obra_id:
        return {}

    df = medicoes[medicoes["obra_id"].astype(str) == str(obra_id)]

    if df.empty:
        return {}

    return {
        f"BM {r['numero_bm']} | {r['periodo_inicio']} a {r['periodo_fim']}": r["medicao_id"]
        for _, r in df.iterrows()
    }


def opcoes_frentes(frentes, medicao_id):
    if not medicao_id:
        return {}

    df = frentes[frentes["medicao_id"].astype(str) == str(medicao_id)]

    if df.empty:
        return {}

    return {
        f"{r['nome_frente']} | {r['dias_trabalhados']} dias": r["frente_id"]
        for _, r in df.iterrows()
    }


def ir_para_etapa(etapa):
    st.session_state.etapa_medicoes = etapa
    st.rerun()


def guardar_obra(obra_id):
    st.session_state.medicao_obra_id = obra_id


def guardar_bm(medicao_id):
    st.session_state.medicao_bm_id = medicao_id


def tela_obras(obras):
    st.subheader("1. Obra")

    obras_opts = opcoes_obras(obras)

    if obras_opts:
        obra_label = st.selectbox(
            "Selecionar obra existente",
            list(obras_opts.keys()),
            key="select_obra_fluxo",
        )
        obra_id = obras_opts[obra_label]
        guardar_obra(obra_id)
    else:
        obra_id = None
        st.info("Nenhuma obra cadastrada ainda.")

    with st.expander("Cadastrar nova obra", expanded=obras.empty):
        with st.form("form_nova_obra", clear_on_submit=False):
            nome_obra = st.text_input("Nome da obra", value="Contrato 26.171 - Curitiba")
            contratante = st.text_input("Contratante", value="Prefeitura Municipal de Curitiba - SMMA")
            contrato = st.text_input("Contrato", value="26.171 - Aditivo 01")
            objeto = st.text_area(
                "Objeto",
                value="Execução de serviços contínuos de engenharia para manutenção e execução de dragagem nos lagos e rios dos parques e bosques no município de Curitiba",
            )
            cidade = st.text_input("Cidade", value="Curitiba/PR")
            status = st.selectbox("Status", ["Ativa", "Concluída", "Suspensa", "Arquivada"])
            observacoes = st.text_area("Observações")
            ok = st.form_submit_button("Salvar obra")

        if ok:
            if not nome_obra.strip():
                st.error("Informe o nome da obra.")
                return obras, obra_id

            nova = {
                "obra_id": novo_id("obra"),
                "nome_obra": nome_obra,
                "contratante": contratante,
                "contrato": contrato,
                "objeto": objeto,
                "cidade": cidade,
                "status": status,
                "observacoes": observacoes,
                "criado_em": agora_iso(),
                "atualizado_em": agora_iso(),
            }

            obras = pd.concat([obras, pd.DataFrame([nova])], ignore_index=True)
            guardar_obra(nova["obra_id"])

            if salvar_bases(obras=obras):
                st.success("Obra cadastrada com sucesso.")
                st.rerun()

    if not obras.empty:
        st.dataframe(
            obras[["nome_obra", "contratante", "contrato", "cidade", "status"]],
            use_container_width=True,
            hide_index=True,
        )

    return obras, st.session_state.get("medicao_obra_id", obra_id)


def tela_medicoes(obras, medicoes):
    st.subheader("2. Boletim de Medição")

    obra_id = st.session_state.get("medicao_obra_id")

    if not obra_id:
        st.warning("Selecione ou cadastre uma obra primeiro.")
        return medicoes, None

    obra_nome = obras.loc[obras["obra_id"].astype(str) == str(obra_id), "nome_obra"]
    if not obra_nome.empty:
        st.info(f"Obra selecionada: {obra_nome.iloc[0]}")

    med_opts = opcoes_medicoes(medicoes, obra_id)

    if med_opts:
        med_label = st.selectbox(
            "Selecionar BM existente",
            list(med_opts.keys()),
            key="select_bm_fluxo",
        )
        guardar_bm(med_opts[med_label])
    else:
        st.info("Nenhum BM cadastrado para esta obra.")

    df_obra = medicoes[medicoes["obra_id"].astype(str) == str(obra_id)]

    with st.expander("Cadastrar novo BM", expanded=df_obra.empty):
        with st.form("form_novo_bm", clear_on_submit=False):
            c1, c2, c3 = st.columns(3)

            with c1:
                numero_bm = st.text_input("Número do BM", value="04")
                aditivo = st.text_input("Aditivo", value="01")

            with c2:
                periodo_inicio = st.date_input("Início do período", value=date(2025, 11, 22))
                periodo_fim = st.date_input("Fim do período", value=date(2025, 12, 21))

            with c3:
                data_bm = st.date_input("Data do BM", value=date(2025, 12, 21))
                dias_uteis_mes = st.number_input("Dias úteis no mês", min_value=1, value=20, step=1)

            apost = st.number_input(
                "Apostilamento / reajuste (%)",
                min_value=0.0,
                value=5.53,
                step=0.01,
            ) / 100

            status = st.selectbox("Status do BM", ["Rascunho", "Fechado", "Enviado", "Aprovado", "Pago"])
            observacoes = st.text_area("Observações do BM")
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
                "dias_uteis_mes": dias_uteis_mes,
                "apostilamento_percentual": apost,
                "status": status,
                "observacoes": observacoes,
                "criado_em": agora_iso(),
                "atualizado_em": agora_iso(),
            }

            medicoes = pd.concat([medicoes, pd.DataFrame([nova])], ignore_index=True)
            guardar_bm(nova["medicao_id"])

            if salvar_bases(medicoes=medicoes):
                st.success("BM cadastrado com sucesso.")
                st.rerun()

    df = medicoes[medicoes["obra_id"].astype(str) == str(obra_id)]

    if not df.empty:
        st.dataframe(
            df[["numero_bm", "aditivo", "periodo_inicio", "periodo_fim", "dias_uteis_mes", "status"]],
            use_container_width=True,
            hide_index=True,
        )

    return medicoes, st.session_state.get("medicao_bm_id")


def tela_frentes(medicoes, frentes):
    st.subheader("3. Frentes / Parques")

    medicao_id = st.session_state.get("medicao_bm_id")

    if not medicao_id:
        st.warning("Selecione ou cadastre um BM primeiro.")
        return frentes, None

    fr_opts = opcoes_frentes(frentes, medicao_id)

    if fr_opts:
        frente_label = st.selectbox(
            "Selecionar frente/parque existente",
            list(fr_opts.keys()),
            key="select_frente_fluxo",
        )
        st.session_state.medicao_frente_id = fr_opts[frente_label]
    else:
        st.info("Nenhuma frente/parque cadastrada para este BM.")

    df_med = frentes[frentes["medicao_id"].astype(str) == str(medicao_id)]

    with st.expander("Cadastrar frente/parque", expanded=df_med.empty):
        with st.form("form_nova_frente", clear_on_submit=False):
            nome_frente = st.text_input("Nome da frente/parque", value="PARQUE BARIGUI")
            dias_trabalhados = st.number_input(
                "Dias trabalhados nesta frente",
                min_value=0.0,
                value=19.0,
                step=0.5,
            )
            observacoes = st.text_area("Observações")
            ok = st.form_submit_button("Salvar frente")

        if ok:
            nova = {
                "frente_id": novo_id("frente"),
                "medicao_id": medicao_id,
                "nome_frente": nome_frente,
                "dias_trabalhados": dias_trabalhados,
                "observacoes": observacoes,
                "criado_em": agora_iso(),
                "atualizado_em": agora_iso(),
            }

            frentes = pd.concat([frentes, pd.DataFrame([nova])], ignore_index=True)
            st.session_state.medicao_frente_id = nova["frente_id"]

            if salvar_bases(frentes=frentes):
                st.success("Frente cadastrada com sucesso.")
                st.rerun()

    df = frentes[frentes["medicao_id"].astype(str) == str(medicao_id)]

    if not df.empty:
        st.dataframe(
            df[["nome_frente", "dias_trabalhados", "observacoes"]],
            use_container_width=True,
            hide_index=True,
        )

    return frentes, medicao_id


def tela_itens(medicoes, frentes, itens):
    st.subheader("4. Itens medidos e memória de cálculo")

    medicao_id = st.session_state.get("medicao_bm_id")

    if not medicao_id:
        st.warning("Selecione ou cadastre um BM primeiro.")
        return itens

    fr_opts = opcoes_frentes(frentes, medicao_id)

    if not fr_opts:
        st.info("Cadastre uma frente/parque antes de lançar itens.")
        return itens

    frente_label = st.selectbox(
        "Frente/parque",
        list(fr_opts.keys()),
        key="frente_item_fluxo",
    )
    frente_id = fr_opts[frente_label]

    med_row = medicoes[medicoes["medicao_id"].astype(str) == str(medicao_id)]
    dias_uteis_padrao = int(num(med_row.iloc[0]["dias_uteis_mes"], 20)) if not med_row.empty else 20

    frente_row = frentes[frentes["frente_id"].astype(str) == str(frente_id)]
    dias_trab_padrao = float(num(frente_row.iloc[0]["dias_trabalhados"], 0)) if not frente_row.empty else 0

    with st.expander("Cadastrar item medido", expanded=True):
        with st.form("form_novo_item", clear_on_submit=False):
            c1, c2, c3 = st.columns([1, 3, 1])

            with c1:
                codigo = st.text_input("Código", value="DR-31")

            with c2:
                descricao = st.text_input("Descrição", value="Locação e Montagem de Tubulação de Recalque")

            with c3:
                unidade = st.text_input("Unidade", value="m")

            c4, c5 = st.columns(2)

            with c4:
                valor_unitario = st.number_input(
                    "Valor unitário",
                    min_value=0.0,
                    value=0.0,
                    step=0.01,
                    format="%.4f",
                )

            with c5:
                tipo_calculo = st.selectbox(
                    "Tipo de cálculo",
                    list(TIPOS_CALCULO.keys()),
                    format_func=lambda x: TIPOS_CALCULO[x],
                )

            st.markdown("**Parâmetros de cálculo**")

            quantidade_manual = 0.0
            comprimento_total = 0.0
            dias_uteis_mes = dias_uteis_padrao
            dias_trabalhados = dias_trab_padrao
            horas_dia = 0.0
            volume_desaguado = 0.0
            st_des = 0.0
            st_br = 0.0
            volume_anterior = 0.0
            custo_nf = 0.0
            bdi_percentual = 0.0
            reajuste_percentual = 0.0
            parametros_json = ""

            if tipo_calculo == "manual":
                quantidade_manual = st.number_input(
                    "Quantidade medida",
                    min_value=0.0,
                    value=0.0,
                    step=0.01,
                    format="%.6f",
                )

            elif tipo_calculo == "proporcional_dias":
                c6, c7, c8 = st.columns(3)

                with c6:
                    comprimento_total = st.number_input(
                        "Comprimento/base total",
                        min_value=0.0,
                        value=0.0,
                        step=0.01,
                        format="%.6f",
                    )

                with c7:
                    dias_uteis_mes = st.number_input(
                        "Dias úteis no mês",
                        min_value=1.0,
                        value=float(dias_uteis_padrao),
                        step=1.0,
                    )

                with c8:
                    dias_trabalhados = st.number_input(
                        "Dias trabalhados",
                        min_value=0.0,
                        value=dias_trab_padrao,
                        step=0.5,
                    )

            elif tipo_calculo == "horas":
                c6, c7 = st.columns(2)

                with c6:
                    dias_trabalhados = st.number_input(
                        "Dias trabalhados",
                        min_value=0.0,
                        value=dias_trab_padrao,
                        step=0.5,
                    )

                with c7:
                    horas_dia = st.number_input(
                        "Horas por dia",
                        min_value=0.0,
                        value=9.0,
                        step=0.5,
                    )

            elif tipo_calculo == "volume_bag":
                st.caption('Exemplo: [{"bag":"Bag 01","comprimento":45,"ast":14.6}]')
                parametros_json = st.text_area(
                    "Bags / AST",
                    value='[{"bag":"Bag 01","comprimento":45,"ast":14.6}]',
                )

            elif tipo_calculo == "volume_lodo_dragado":
                c6, c7, c8, c9 = st.columns(4)

                with c6:
                    volume_desaguado = st.number_input(
                        "VLdes - volume desaguado",
                        min_value=0.0,
                        value=0.0,
                        step=0.01,
                        format="%.6f",
                    )

                with c7:
                    st_des = st.number_input(
                        "% ST des",
                        min_value=0.0,
                        value=0.0,
                        step=0.01,
                        format="%.6f",
                    )

                with c8:
                    st_br = st.number_input(
                        "% ST bruto",
                        min_value=0.0,
                        value=0.0,
                        step=0.01,
                        format="%.6f",
                    )

                with c9:
                    volume_anterior = st.number_input(
                        "Volume anterior",
                        min_value=0.0,
                        value=0.0,
                        step=0.01,
                        format="%.6f",
                    )

            elif tipo_calculo == "custo_para_quantidade":
                c6, c7, c8 = st.columns(3)

                with c6:
                    custo_nf = st.number_input(
                        "Custo NF / serviços",
                        min_value=0.0,
                        value=0.0,
                        step=0.01,
                        format="%.2f",
                    )

                with c7:
                    bdi_percentual = st.number_input(
                        "BDI (%)",
                        min_value=0.0,
                        value=29.98,
                        step=0.01,
                    ) / 100

                with c8:
                    reajuste_percentual = st.number_input(
                        "Reajuste a retirar (%)",
                        min_value=0.0,
                        value=5.53,
                        step=0.01,
                    ) / 100

            observacoes = st.text_area("Observações do item")
            ok = st.form_submit_button("Salvar item")

        if ok:
            nova = {
                "item_id": novo_id("item"),
                "medicao_id": medicao_id,
                "frente_id": frente_id,
                "codigo": codigo,
                "descricao": descricao,
                "unidade": unidade,
                "valor_unitario": valor_unitario,
                "tipo_calculo": tipo_calculo,
                "quantidade_manual": quantidade_manual,
                "comprimento_total": comprimento_total,
                "dias_uteis_mes": dias_uteis_mes,
                "dias_trabalhados": dias_trabalhados,
                "horas_dia": horas_dia,
                "volume_desaguado": volume_desaguado,
                "st_des": st_des,
                "st_br": st_br,
                "volume_anterior": volume_anterior,
                "custo_nf": custo_nf,
                "bdi_percentual": bdi_percentual,
                "reajuste_percentual": reajuste_percentual,
                "parametros_json": parametros_json,
                "quantidade_calculada": 0,
                "quantidade_medida": 0,
                "valor_total": 0,
                "observacoes": observacoes,
                "criado_em": agora_iso(),
                "atualizado_em": agora_iso(),
            }

            itens = pd.concat([itens, pd.DataFrame([nova])], ignore_index=True)
            itens = recalcular_itens(itens)

            if salvar_bases(itens=itens):
                st.success("Item cadastrado e calculado com sucesso.")
                st.rerun()

    df = recalcular_itens(itens[itens["medicao_id"].astype(str) == str(medicao_id)].copy())

    if not df.empty:
        fr_map = frentes.set_index("frente_id")["nome_frente"].to_dict()
        df["frente"] = df["frente_id"].map(fr_map)

        st.dataframe(
            df[
                [
                    "frente", "codigo", "descricao", "unidade", "tipo_calculo",
                    "quantidade_medida", "valor_unitario", "valor_total",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )

    return itens


def tela_resumo(medicoes, frentes, itens):
    st.subheader("5. Resumo do BM")

    medicao_id = st.session_state.get("medicao_bm_id")

    if not medicao_id:
        st.warning("Selecione ou cadastre um BM primeiro.")
        return

    df = recalcular_itens(itens[itens["medicao_id"].astype(str) == str(medicao_id)].copy())

    if df.empty:
        st.info("Ainda não há itens medidos neste BM.")
        return

    fr_map = frentes.set_index("frente_id")["nome_frente"].to_dict()
    df["frente"] = df["frente_id"].map(fr_map)

    resumo = df.groupby("frente", dropna=False)["valor_total"].sum().reset_index()
    total_geral = resumo["valor_total"].sum()

    med_row = medicoes[medicoes["medicao_id"].astype(str) == str(medicao_id)]
    apost = num(med_row.iloc[0]["apostilamento_percentual"]) if not med_row.empty else 0.0

    valor_apost = total_geral * apost
    total_com_apost = total_geral + valor_apost

    c1, c2, c3 = st.columns(3)
    c1.metric("Total geral da medição", moeda(total_geral))
    c2.metric("Apostilamento / reajuste", moeda(valor_apost))
    c3.metric("Valor total do BM", moeda(total_com_apost))

    resumo["valor_total_formatado"] = resumo["valor_total"].apply(moeda)

    st.dataframe(
        resumo[["frente", "valor_total_formatado"]],
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("**Itens consolidados**")

    df_view = df[
        [
            "frente", "codigo", "descricao", "unidade", "quantidade_medida",
            "valor_unitario", "valor_total", "observacoes",
        ]
    ].copy()

    st.dataframe(df_view, use_container_width=True, hide_index=True)

    csv = df_view.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        "Baixar itens do BM em CSV",
        data=csv,
        file_name="itens_medicao.csv",
        mime="text/csv",
    )


def barra_fluxo():
    etapas = {
        "obra": "1. Obra",
        "bm": "2. BM",
        "frentes": "3. Frentes",
        "itens": "4. Itens",
        "resumo": "5. Resumo",
    }

    etapa_atual = st.session_state.get("etapa_medicoes", "obra")

    st.markdown("### Fluxo da medição")
    cols = st.columns(len(etapas))

    for i, (etapa, label) in enumerate(etapas.items()):
        with cols[i]:
            if etapa == etapa_atual:
                st.button(f"✅ {label}", key=f"fluxo_{etapa}", disabled=True, use_container_width=True)
            else:
                if st.button(label, key=f"fluxo_{etapa}", use_container_width=True):
                    ir_para_etapa(etapa)


def navegacao_etapas():
    etapa = st.session_state.get("etapa_medicoes", "obra")

    st.divider()
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if etapa != "obra":
            if st.button("← Voltar", use_container_width=True):
                ordem = ["obra", "bm", "frentes", "itens", "resumo"]
                idx = ordem.index(etapa)
                ir_para_etapa(ordem[idx - 1])

    with col2:
        if st.button("⬅ Voltar ao menu", use_container_width=True):
            st.session_state.tela = "menu"
            st.rerun()

    with col3:
        ordem = ["obra", "bm", "frentes", "itens", "resumo"]
        if etapa != "resumo":
            idx = ordem.index(etapa)
            proxima = ordem[idx + 1]

            label = {
                "bm": "Próximo: BM →",
                "frentes": "Próximo: Frentes →",
                "itens": "Próximo: Itens →",
                "resumo": "Próximo: Resumo →",
            }.get(proxima, "Próximo →")

            if st.button(label, use_container_width=True):
                ir_para_etapa(proxima)


def medicoes():
    st.title("Medições")
    st.caption("Boletins de medição, frentes/parques, memória de cálculo e totais por BM.")

    if "etapa_medicoes" not in st.session_state:
        st.session_state.etapa_medicoes = "obra"

    obras, medicoes_df, frentes, itens = carregar_bases()

    barra_fluxo()
    st.divider()

    etapa = st.session_state.etapa_medicoes

    if etapa == "obra":
        obras, obra_id = tela_obras(obras)

    elif etapa == "bm":
        medicoes_df, medicao_id = tela_medicoes(obras, medicoes_df)

    elif etapa == "frentes":
        frentes, medicao_id = tela_frentes(medicoes_df, frentes)

    elif etapa == "itens":
        itens = tela_itens(medicoes_df, frentes, itens)

    elif etapa == "resumo":
        tela_resumo(medicoes_df, frentes, itens)

    navegacao_etapas()


def render():
    medicoes()


if __name__ == "__main__":
    medicoes()
