import streamlit as st
import pandas as pd

# =========================
# FORMATADOR
# =========================
def formatar_real(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# =========================
# ETAPA 3
# =========================
def etapa3():

    st.header("Custo do Barrilete")

    if "orcamento" not in st.session_state:
        st.warning("Volte para etapas anteriores.")
        return

    # =========================
    # ITENS BASE
    # =========================
    itens = [
        "Tubo 6m 8\"",
        "Toco 0,50m",
        "Joelho 90°",
        "Tee 6x4",
        "Ponteira 4\"",
        "Cap 6\"",
        "Válvula Gaveta 4\"",
        "Válvula Gaveta 3\"",
        "Mangueira",
        "Abraçadeiras",
        "Curva PVC 4\"",
        "Válvula esfera 2\"",
        "Bomba lameira"
    ]

    # =========================
    # SESSION STATE
    # =========================
    if "df_barrilete" not in st.session_state:
        df_init = pd.DataFrame({
            "Item": itens,
            "Qtd": 0,
            "Preço Unitário": 0.0
        })
        st.session_state.df_barrilete = df_init

    # =========================
    # FORM
    # =========================
    with st.form("form_barrilete"):

        df_editado = st.data_editor(
            st.session_state.df_barrilete,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Item": st.column_config.TextColumn(disabled=True),
                "Qtd": st.column_config.NumberColumn("Qtd", min_value=0),
                "Preço Unitário": st.column_config.NumberColumn("Preço Unitário (R$)", min_value=0.0),
            }
        )

        dias = st.number_input("Número de dias da atividade", min_value=1, value=1)

        calcular = st.form_submit_button("Calcular custo")

    # =========================
    # CÁLCULO
    # =========================
    if calcular:

        st.session_state.df_barrilete = df_editado.copy()

        df_calc = df_editado.copy()

        df_calc["Total"] = df_calc["Qtd"] * df_calc["Preço Unitário"]

        # =========================
        # FILTRO
        # =========================
        df_display = df_calc[df_calc["Qtd"] > 0].copy()

        if df_display.empty:
            st.info("Nenhum item informado.")
        else:
            df_display["Preço Unitário"] = df_display["Preço Unitário"].apply(formatar_real)
            df_display["Total"] = df_display["Total"].apply(formatar_real)

            st.subheader("Materiais")

            st.dataframe(
                df_display[["Item", "Qtd", "Preço Unitário", "Total"]],
                use_container_width=True,
                hide_index=True
            )

        total_materiais = df_calc["Total"].sum()

        # =========================
        # CUSTO EQUIPE
        # =========================
        custo_hora = st.session_state.orcamento.get("custo_hora_equipe", 0)

        horas_dia = 8  # padrão simples (pode melhorar depois)

        custo_dia = custo_hora * horas_dia
        custo_total_equipe = custo_dia * dias

        st.subheader("Mão de Obra")

        st.write(f"Custo hora equipe: R$ {formatar_real(custo_hora)}")
        st.write(f"Custo por dia: R$ {formatar_real(custo_dia)}")
        st.write(f"Dias: {dias}")

        st.success(f"Custo total equipe: R$ {formatar_real(custo_total_equipe)}")

        # =========================
        # TOTAL GERAL
        # =========================
        total_geral = total_materiais + custo_total_equipe

        st.subheader("Resumo Final")

        st.write(f"Materiais: R$ {formatar_real(total_materiais)}")
        st.write(f"Mão de obra: R$ {formatar_real(custo_total_equipe)}")

        st.success(f"💰 CUSTO TOTAL: R$ {formatar_real(total_geral)}")

        # =========================
        # SALVAR
        # =========================
        st.session_state.orcamento.update({
            "barrilete": df_calc.to_dict(orient="records"),
            "custo_materiais": total_materiais,
            "custo_equipe_total": custo_total_equipe,
            "custo_total": total_geral,
            "dias_barrilete": dias
        })

    # =========================
    # NAVEGAÇÃO
    # =========================
    col1, col2 = st.columns(2)

    if col1.button("⬅ Voltar"):
        st.session_state.tela = "orcamento2"
        st.rerun()

    if col2.button("Finalizar"):
        st.success("Orçamento finalizado (próxima etapa: salvar/exportar)")
