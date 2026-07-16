from datetime import date

import pandas as pd

from services.ferias_regras import (
    calcular_status_ferias,
    recalcular_status_dataframe,
)


def test_status_vencido_e_em_dobro_e_recalculado():
    status = calcular_status_ferias(
        "2025-08-05",
        "2026-07-07",
        hoje=date(2026, 7, 16),
    )

    assert status == ("Férias Vencidas", "Férias em Dobro")


def test_status_futuro_corrige_classificacao_persistida_incorreta():
    df = pd.DataFrame(
        [
            {
                "Periodo_Aquisitivo_Fim": "2027-03-03",
                "Limite_Gozo": "",
                "Situacao_Ferias": "Férias Vencidas",
                "Situacao_Prazo": "Dentro do Prazo",
            }
        ]
    )

    resultado = recalcular_status_dataframe(df, hoje=date(2026, 7, 16))

    assert resultado.loc[0, "Situacao_Ferias"] == "Férias Não Vencidas"
    assert resultado.loc[0, "Situacao_Prazo"] == "Dentro do Prazo"


def test_limite_ausente_usa_regra_de_335_dias():
    status = calcular_status_ferias(
        "2025-08-05",
        "",
        hoje=date(2026, 7, 1),
    )

    assert status == ("Férias Vencidas", "Atenção")


def test_dataframe_original_nao_e_modificado():
    df = pd.DataFrame(
        [
            {
                "Periodo_Aquisitivo_Fim": "2025-01-01",
                "Limite_Gozo": "2026-01-01",
                "Situacao_Ferias": "antigo",
                "Situacao_Prazo": "antigo",
            }
        ]
    )

    recalcular_status_dataframe(df, hoje=date(2026, 7, 16))

    assert df.loc[0, "Situacao_Ferias"] == "antigo"
    assert df.loc[0, "Situacao_Prazo"] == "antigo"
