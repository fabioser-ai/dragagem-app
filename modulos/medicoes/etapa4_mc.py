import pandas as pd
import streamlit as st

from modulos.medicoes.config import ARQ_FRENTES, ARQ_MC, COL_FRENTES, COL_MC
from modulos.medicoes.repositorio import salvar_csv
from modulos.medicoes.utils import agora, novo_id


def obter_frente_padrao(frentes):
    medicao_id = st.session_state.get("medicao_id")

    if not medicao_id:
        return None, frentes

    df = frentes[
        frentes["medicao_id"].astype(str) == str(medicao_id)
    ].copy()

    if not df.empty:
        frente_id = df.iloc[0]["frente_id"]
        st.session_state.frente_id = frente_id
        return frente_id, frentes

    nova = {
        "frente_id": novo_id("frente"),
        "medicao_id": medicao_id,
        "nome_frente": "MEDIÇÃO GERAL",
        "dias_trabalhados": 0.0,
        "observacoes": "Frente padrão criada automaticamente para modelo sem etapa de frentes.",
        "criado_em": agora(),
        "atualizado_em": agora(),
    }

    frentes = pd.concat(
        [frentes, pd.DataFrame([nova])],
        ignore_index=True,
    )

    if salvar_csv(ARQ_FRENTES, frentes):
        st.session_state.frente_id = nova["frente_id"]
        return nova["frente_id"], frentes

    return None, frentes


def tela_mc(frentes, mc):
    st.subheader("4. Memória de Cálculo")

    modelo = st.session_state.get("modelo_medicao", "padrao_fos")

    if modelo == "padrao_fos":
        frente_id, frentes = obter_frente_padrao(frentes)
    else:
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
                    "tipo": "Padrão FOS",
                    "descricao": "Medição principal",
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

    if st.button(
        "Salvar memória de cálculo",
        use_container_width=True,
    ):
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
