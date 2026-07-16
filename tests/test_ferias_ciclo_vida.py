from datetime import date, datetime
import unittest

import pandas as pd

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


class TestCicloVidaFeriasFolgas(unittest.TestCase):
    def test_registro_legado_recebe_colunas_e_defaults_seguros(self):
        legado = pd.DataFrame(
            [{"Data_Saida": "2026-08-01", "Data_Retorno": "2026-08-07"}]
        )
        resultado = normalizar_ciclo_vida_dataframe(
            legado,
            coluna_inicio="Data_Saida",
            coluna_termino="Data_Retorno",
            hoje=date(2026, 7, 16),
        )

        self.assertTrue(set(COLUNAS_CICLO_VIDA).issubset(resultado.columns))
        self.assertEqual(resultado.loc[0, "Estado_Ciclo"], "programada")
        self.assertEqual(resultado.loc[0, "Data_Prevista_Inicio"], "2026-08-01")
        self.assertEqual(resultado.loc[0, "Confirmado_Inicio_Por"], "")

    def test_legado_ja_terminado_vai_para_historico_sem_ser_apagado(self):
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

        self.assertTrue(operacao.empty)
        self.assertEqual(len(historico), len(legado))
        self.assertEqual(len(historico), 1)
        self.assertEqual(historico.iloc[0]["Estado_Ciclo"], "concluida")

    def test_transicoes_validas(self):
        casos = [
            ("pendente", "programada"),
            ("programada", "em_gozo"),
            ("em_gozo", "concluida"),
            ("pendente", "cancelada"),
            ("programada", "cancelada"),
        ]
        for origem, destino in casos:
            with self.subTest(origem=origem, destino=destino):
                resultado = transicionar_ciclo_vida(
                    _registro(origem),
                    destino,
                    usuario="Fabio",
                    autorizado=True,
                    agora=AGORA,
                )
                self.assertEqual(resultado["Estado_Ciclo"], destino)

    def test_transicoes_invalidas_sao_rejeitadas(self):
        casos = [
            ("pendente", "concluida"),
            ("programada", "concluida"),
            ("em_gozo", "programada"),
            ("concluida", "em_gozo"),
            ("cancelada", "programada"),
        ]
        for origem, destino in casos:
            with self.subTest(origem=origem, destino=destino):
                with self.assertRaises(TransicaoCicloInvalida):
                    transicionar_ciclo_vida(
                        _registro(origem),
                        destino,
                        usuario="Fabio",
                        autorizado=True,
                        agora=AGORA,
                    )

    def test_confirmacao_inicio_registra_data_usuario_e_timestamp(self):
        resultado = transicionar_ciclo_vida(
            _registro("programada"),
            "em_gozo",
            usuario="Karina",
            autorizado=True,
            agora=AGORA,
            data_efetiva=date(2026, 7, 15),
        )

        self.assertEqual(resultado["Data_Efetiva_Inicio"], "2026-07-15")
        self.assertEqual(resultado["Confirmado_Inicio_Por"], "Karina")
        self.assertEqual(resultado["Confirmado_Inicio_Em"], "2026-07-16T18:30:00")

    def test_confirmacao_termino_registra_data_usuario_e_timestamp(self):
        resultado = transicionar_ciclo_vida(
            _registro("em_gozo"),
            "concluida",
            usuario="Ana",
            autorizado=True,
            agora=AGORA,
        )

        self.assertEqual(resultado["Data_Efetiva_Termino"], "2026-07-16")
        self.assertEqual(resultado["Confirmado_Termino_Por"], "Ana")
        self.assertEqual(resultado["Confirmado_Termino_Em"], "2026-07-16T18:30:00")

    def test_cancelamento_registra_responsavel_sem_remover_registro(self):
        original = _registro("programada")
        resultado = transicionar_ciclo_vida(
            original,
            "cancelada",
            usuario="Fabio",
            autorizado=True,
            agora=AGORA,
        )

        self.assertGreaterEqual(len(resultado), len(original))
        self.assertEqual(resultado["Cancelado_Por"], "Fabio")
        self.assertEqual(resultado["Cancelado_Em"], "2026-07-16T18:30:00")

    def test_chamada_indireta_sem_permissao_nao_altera_estado(self):
        original = _registro("programada")
        with self.assertRaises(TransicaoNaoAutorizada):
            transicionar_ciclo_vida(
                original,
                "em_gozo",
                usuario="intruso",
                autorizado=False,
                agora=AGORA,
            )

        self.assertEqual(original["Estado_Ciclo"], "programada")

    def test_painel_e_historico_sao_separados_sem_perda(self):
        df = pd.DataFrame(
            {"Estado_Ciclo": ["pendente", "programada", "em_gozo", "concluida", "cancelada"]}
        )
        operacao, historico = separar_operacao_historico(df)

        self.assertEqual(
            operacao["Estado_Ciclo"].tolist(),
            ["pendente", "programada", "em_gozo"],
        )
        self.assertEqual(
            historico["Estado_Ciclo"].tolist(),
            ["concluida", "cancelada"],
        )
        self.assertEqual(len(operacao) + len(historico), len(df))

    def test_normalizacao_nao_modifica_dataframe_original(self):
        original = pd.DataFrame(
            [{"Data_Saida": "2026-08-01", "Data_Retorno": "2026-08-07"}]
        )
        normalizar_ciclo_vida_dataframe(
            original,
            coluna_inicio="Data_Saida",
            coluna_termino="Data_Retorno",
        )

        self.assertNotIn("Estado_Ciclo", original.columns)


if __name__ == "__main__":
    unittest.main()
