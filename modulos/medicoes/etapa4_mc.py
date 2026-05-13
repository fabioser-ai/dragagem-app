import pandas as pd
import streamlit as st

from modulos.medicoes.config import (
    ARQ_FRENTES,
    ARQ_MC,
    COL_MC,
)
from modulos.medicoes.repositorio import (
    carregar_tabela_contrato,
    salvar_csv,
)
from modulos.medicoes.utils import agora, moeda, novo_id


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
        "observacoes": (
            "Frente padrão criada automaticamente para modelo "
            "sem etapa de frentes."
        ),
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


def tela_mc_padrao_fos(frentes, mc):
    st.subheader("4. MC - Itens Contratuais")

    frente_id, frentes = obter_frente_padrao(frentes)

    if not frente_id:
        st.warning("Não foi possível criar a frente padrão da medição.")
        return

    arquivo_tabela = st.session_state.get("arquivo_tabela_servicos", "")

    if not arquivo_tabela:
        st.warning(
            "Esta obra não possui tabela contratual de serviços vinculada."
        )
        return

    tabela = carregar_tabela_contrato(arquivo_tabela)

    if tabela.empty:
        st.warning(
            "A tabela contratual vinculada não foi encontrada "
            "ou está vazia."
        )
        st.caption(f"Arquivo esperado: {arquivo_tabela}")
        return

    st.info(f"Tabela contratual carregada: {arquivo_tabela}")

    tabela = tabela.copy()

    if "ativo" in tabela.columns:
        tabela = tabela[
            tabela["ativo"].astype(str).str.lower().isin(
                ["true", "1", "sim", "s", "yes"]
            )
        ]

    for col in [
        "quantidade_base",
        "preco_unitario_com_bdi",
        "preco_total",
    ]:
        tabela[col] = pd.to_numeric(
            tabela[col],
            errors="coerce",
        ).fillna(0.0)

    df_existente = mc[
        mc["frente_id"].astype(str) == str(frente_id)
    ].copy()

    if df_existente.empty:
        df_editor = tabela[
            [
                "fonte",
                "codigo",
                "item",
                "descricao",
                "unidade",
                "preco_unitario_com_bdi",
            ]
        ].copy()

        df_editor["mc_id"] = [
            novo_id("mc") for _ in range(len(df_editor))
        ]
        df_editor["medicao_id"] = st.session_state.get("medicao_id")
        df_editor["frente_id"] = frente_id
        df_editor["quantidade_executada"] = 0.0
        df_editor["total"] = 0.0

    else:
        df_editor = df_existente.copy()

        if "quantidade_executada" not in df_editor.columns:
            df_editor["quantidade_executada"] = pd.to_numeric(
                df_editor.get("resultado", 0),
                errors="coerce",
            ).fillna(0.0)

        if "preco_unitario_com_bdi" not in df_editor.columns:
            df_editor["preco_unitario_com_bdi"] = 0.0

        if "total" not in df_editor.columns:
            df_editor["total"] = 0.0

    df_editor["quantidade_executada"] = pd.to_numeric(
        df_editor["quantidade_executada"],
        errors="coerce",
    ).fillna(0.0)

    df_editor["preco_unitario_com_bdi"] = pd.to_numeric(
        df_editor["preco_unitario_com_bdi"],
        errors="coerce",
    ).fillna(0.0)

    st.caption(
        "Informe a quantidade executada somente nos itens que serão "
        "medidos neste BM."
    )

    df_editado = st.data_editor(
        df_editor,
        use_container_width=True,
        num_rows="fixed",
        hide_index=True,
        key=f"mc_padrao_fos_{frente_id}",
        column_config={
            "mc_id": None,
            "medicao_id": None,
            "frente_id": None,
            "fonte": st.column_config.TextColumn(
                "Fonte",
                disabled=True,
            ),
            "codigo": st.column_config.TextColumn(
                "Código",
                disabled=True,
            ),
            "item": st.column_config.NumberColumn(
                "Item",
                disabled=True,
            ),
            "descricao": st.column_config.TextColumn(
                "Descrição",
                disabled=True,
                width="large",
            ),
            "unidade": st.column_config.TextColumn(
                "Un.",
                disabled=True,
            ),
            "preco_unitario_com_bdi": st.column_config.NumberColumn(
                "Preço unit. c/ BDI",
                format="%.2f",
                disabled=True,
            ),
            "quantidade_executada": st.column_config.NumberColumn(
                "Quantidade executada",
                format="%.2f",
                min_value=0.0,
            ),
            "total": st.column_config.NumberColumn(
                "Total",
                format="%.2f",
                disabled=True,
            ),
        },
    )

    df_editado["quantidade_executada"] = pd.to_numeric(
        df_editado["quantidade_executada"],
        errors="coerce",
    ).fillna(0.0)

    df_editado["preco_unitario_com_bdi"] = pd.to_numeric(
        df_editado["preco_unitario_com_bdi"],
        errors="coerce",
    ).fillna(0.0)

    df_editado["total"] = (
        df_editado["quantidade_executada"]
        * df_editado["preco_unitario_com_bdi"]
    )

    total_mc = df_editado["total"].sum()

    st.metric("Total desta MC", moeda(total_mc))

    somente_medidos = df_editado[
        df_editado["quantidade_executada"] > 0
    ].copy()

    st.caption(
        f"Itens com quantidade lançada: {len(somente_medidos)}"
    )

    if st.button("Salvar MC", use_container_width=True):
        mc = mc[
            mc["frente_id"].astype(str) != str(frente_id)
        ]

        # Compatibilidade com a estrutura antiga COL_MC:
        # descricao recebe a descrição contratual
        # comprimento recebe quantidade executada
        # ast recebe preço unitário
        # resultado recebe total
        df_salvar = pd.DataFrame()

        df_salvar["mc_id"] = df_editado["mc_id"]
        df_salvar["medicao_id"] = df_editado["medicao_id"]
        df_salvar["frente_id"] = df_editado["frente_id"]
        df_salvar["tipo"] = "Item Contratual"
        df_salvar["descricao"] = (
            df_editado["item"].astype(str)
            + " - "
            + df_editado["codigo"].astype(str)
            + " - "
            + df_editado["descricao"].astype(str)
        )
        df_salvar["comprimento"] = df_editado["quantidade_executada"]
        df_salvar["ast"] = df_editado["preco_unitario_com_bdi"]
        df_salvar["resultado"] = df_editado["total"]

        mc = pd.concat(
            [mc, df_salvar[COL_MC]],
            ignore_index=True,
        )

        if salvar_csv(ARQ_MC, mc):
            st.success("MC salva com sucesso.")
            st.rerun()


def tela_mc_ast(frentes, mc):
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


def tela_mc(frentes, mc):
    modelo = st.session_state.get("modelo_medicao", "padrao_fos")

    if modelo == "padrao_fos":
        tela_mc_padrao_fos(frentes, mc)
    else:
        tela_mc_ast(frentes, mc)
