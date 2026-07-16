from datetime import date, datetime

import pandas as pd
import pytest

from services.ferias_regras import (
    COLUNAS_CICLO_VIDA,
    TransicaoCicloInvalida,
    TransicaoNaoAutorizada,
    normalizar_ciclo_vida_dataframe,
    separar_operacao_historico,
    transicionar_ciclo_vida,
)


AGORA = datetime(2026, 7, 16, 18, 30, 0)


def _registro(estado):
    return pd.Series({"Estado_Ciclo": estado, "Funcionario": "Teste"})


def test_registro_legado_recebe_colunas_e_defaults_seguros():
    legado = pd.DataFrame(
        [{"Data_Saida": "2026-08-01", "Data_Retorno": "2026-08-07"}]
    )

    resultado = normalizar_ciclo_vida_dataframe(
        legado,
        coluna_inicio="Data_Saida",
        coluna_termino="Data_Retorno",
        hoje=date(2026, 7, 16),
    )

    assert set(COLUNAS_CICLO_VIDA).issubset(resultado.columns)
    assert resultado.loc[0, "Estado_Ciclo"] == "programada"
    assert resultado.loc[0, "Data_Prevista_Inicio"] == "2026-08-01"
    assert resultado.loc[0, "Confirmado_Inicio_Por"] == ""


def test_legado_ja_terminado_vai_para_historico_sem_ser_apagado():
    legado = pd.DataFrame(
        [{"Data_Saida": "2026-01-01", "Data_Retorno": "2026-01-07"}]
    )
    resultado = normalizar_ciclo_vida_dataframe(
        legado,
        coluna_inicio="Data_Saida",
        coluna_termino="Data_Retorno",
        hoje=date(2026, 7, 16),
    )

    operacao, historico = separar_operacao_historico(resultado)

    assert operacao.empty
    assert len(historico) == len(legado) == 1
    assert historico.iloc[0]["Estado_Ciclo"] == "concluida"


@pytest.mark.parametrize(
    ("origem", "destino"),
    [
        ("pendente", "programada"),
        ("programada", "em_gozo"),
        ("em_gozo", "concluida"),
        ("pendente", "cancelada"),
        ("programada", "cancelada"),
    ],
)
def test_transicoes_validas(origem, destino):
    resultado = transicionar_ciclo_vida(
        _registro(origem),
        destino,
        usuario="Fabio",
        autorizado=True,
        agora=AGORA,
    )

    assert resultado["Estado_Ciclo"] == destino


@pytest.mark.parametrize(
    ("origem", "destino"),
    [
        ("pendente", "concluida"),
        ("programada", "concluida"),
        ("em_gozo", "programada"),
        ("concluida", "em_gozo"),
        ("cancelada", "programada"),
    ],
)
def test_transicoes_invalidas_sao_rejeitadas(origem, destino):
    with pytest.raises(TransicaoCicloInvalida):
        transicionar_ciclo_vida(
            _registro(origem),
            destino,
            usuario="Fabio",
            autorizado=True,
            agora=AGORA,
        )


def test_confirmacao_inicio_registra_data_usuario_e_timestamp():
    resultado = transicionar_ciclo_vida(
        _registro("programada"),
        "em_gozo",
        usuario="Karina",
        autorizado=True,
        agora=AGORA,
        data_efetiva=date(2026, 7, 15),
    )

    assert resultado["Data_Efetiva_Inicio"] == "2026-07-15"
    assert resultado["Confirmado_Inicio_Por"] == "Karina"
    assert resultado["Confirmado_Inicio_Em"] == "2026-07-16T18:30:00"


def test_confirmacao_termino_registra_data_usuario_e_timestamp():
    resultado = transicionar_ciclo_vida(
        _registro("em_gozo"),
        "concluida",
        usuario="Ana",
        autorizado=True,
        agora=AGORA,
    )

    assert resultado["Data_Efetiva_Termino"] == "2026-07-16"
    assert resultado["Confirmado_Termino_Por"] == "Ana"
    assert resultado["Confirmado_Termino_Em"] == "2026-07-16T18:30:00"


def test_cancelamento_registra_responsavel_sem_remover_registro():
    original = _registro("programada")
    resultado = transicionar_ciclo_vida(
        original,
        "cancelada",
        usuario="Fabio",
        autorizado=True,
        agora=AGORA,
    )

    assert len(resultado) >= len(original)
    assert resultado["Cancelado_Por"] == "Fabio"
    assert resultado["Cancelado_Em"] == "2026-07-16T18:30:00"


def test_chamada_indireta_sem_permissao_nao_altera_estado():
    original = _registro("programada")

    with pytest.raises(TransicaoNaoAutorizada):
        transicionar_ciclo_vida(
            original,
            "em_gozo",
            usuario="intruso",
            autorizado=False,
            agora=AGORA,
        )

    assert original["Estado_Ciclo"] == "programada"


def test_painel_e_historico_sao_separados_sem_perda():
    df = pd.DataFrame(
        {"Estado_Ciclo": ["pendente", "programada", "em_gozo", "concluida", "cancelada"]}
    )

    operacao, historico = separar_operacao_historico(df)

    assert operacao["Estado_Ciclo"].tolist() == ["pendente", "programada", "em_gozo"]
    assert historico["Estado_Ciclo"].tolist() == ["concluida", "cancelada"]
    assert len(operacao) + len(historico) == len(df)


def test_normalizacao_nao_modifica_dataframe_original():
    original = pd.DataFrame([{"Data_Saida": "2026-08-01", "Data_Retorno": "2026-08-07"}])
    normalizar_ciclo_vida_dataframe(
        original,
        coluna_inicio="Data_Saida",
        coluna_termino="Data_Retorno",
    )

    assert "Estado_Ciclo" not in original.columns
