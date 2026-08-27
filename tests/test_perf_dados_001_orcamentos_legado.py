import inspect
import unittest
from unittest.mock import Mock, patch

import pandas as pd

from services import orcamentos_legado_operacional as persistencia
from services.github import (
    ResultadoEscritaCSV,
    ResultadoLeituraCSV,
    StatusEscrita,
    StatusLeitura,
)


class TestOrcamentosLegadoOperacional(unittest.TestCase):
    def leitura(self, caminho, status, *, dados=None, sha=None, erro=None):
        return ResultadoLeituraCSV(
            status=status,
            dados=dados if dados is not None else pd.DataFrame(),
            arquivo=caminho,
            sha=sha,
            erro=erro,
        )

    def test_classificacao_operacional_e_explicita(self):
        self.assertEqual(
            persistencia.ARQUIVOS_OPERACIONAIS,
            {
                "data/orcamentos.csv",
                "data/clientes.csv",
                "data/insumos.csv",
            },
        )

    def test_leitura_operacional_nao_consulta_main(self):
        resultado = self.leitura(
            "data/orcamentos.csv",
            StatusLeitura.SUCESSO_COM_DADOS,
            dados=pd.DataFrame([{"Codigo": "D_001"}]),
            sha="sha",
        )
        with patch.object(
            persistencia, "ler_csv_operacional", return_value=resultado
        ) as ler, patch.object(persistencia, "carregar_github_main") as ler_main:
            dados = persistencia.carregar_github(
                "data/orcamentos.csv", "token", "repo"
            )

        self.assertEqual(dados.iloc[0]["Codigo"], "D_001")
        ler.assert_called_once_with("data/orcamentos.csv", "token", "repo")
        ler_main.assert_not_called()

    def test_atualizacao_preserva_sha_da_leitura_operacional(self):
        leitura = self.leitura(
            "data/orcamentos.csv", StatusLeitura.SUCESSO_COM_DADOS, sha="sha-atual"
        )
        escrita = ResultadoEscritaCSV(
            StatusEscrita.SUCESSO_ATUALIZADO, "data/orcamentos.csv"
        )
        dados = pd.DataFrame([{"Codigo": "D_001"}])
        with patch.object(
            persistencia, "ler_csv_operacional", return_value=leitura
        ), patch.object(
            persistencia, "salvar_csv_operacional", return_value=escrita
        ) as salvar:
            persistencia.salvar_github(
                dados, "data/orcamentos.csv", "token", "repo"
            )

        salvar.assert_called_once_with(
            dados,
            "data/orcamentos.csv",
            "token",
            "repo",
            sha_esperado="sha-atual",
        )

    def test_ausencia_confirmada_permite_criacao_explicita(self):
        leitura = self.leitura(
            "data/clientes.csv", StatusLeitura.ARQUIVO_INEXISTENTE
        )
        escrita = ResultadoEscritaCSV(
            StatusEscrita.SUCESSO_CRIADO, "data/clientes.csv"
        )
        dados = pd.DataFrame([{"Cliente": "Cliente Novo"}])
        with patch.object(
            persistencia, "ler_csv_operacional", return_value=leitura
        ), patch.object(
            persistencia, "salvar_csv_operacional", return_value=escrita
        ) as salvar:
            persistencia.salvar_github(
                dados, "data/clientes.csv", "token", "repo"
            )

        self.assertEqual(salvar.call_args.kwargs, {"criar": True})

    def test_falha_de_leitura_bloqueia_criacao_e_escrita(self):
        falha = self.leitura(
            "data/insumos.csv",
            StatusLeitura.FALHA_TEMPORARIA,
            erro="timeout",
        )
        with patch.object(
            persistencia, "ler_csv_operacional", return_value=falha
        ), patch.object(persistencia, "salvar_csv_operacional") as salvar:
            with self.assertRaisesRegex(RuntimeError, "não autorizou a escrita"):
                persistencia.salvar_github(
                    pd.DataFrame(), "data/insumos.csv", "token", "repo"
                )
        salvar.assert_not_called()

    def test_conflito_remoto_nao_e_mascarado(self):
        leitura = self.leitura(
            "data/orcamentos.csv", StatusLeitura.SUCESSO_COM_DADOS, sha="sha"
        )
        conflito = ResultadoEscritaCSV(
            StatusEscrita.CONFLITO,
            "data/orcamentos.csv",
            erro="arquivo alterado",
        )
        with patch.object(
            persistencia, "ler_csv_operacional", return_value=leitura
        ), patch.object(
            persistencia, "salvar_csv_operacional", return_value=conflito
        ):
            with self.assertRaisesRegex(RuntimeError, "arquivo alterado"):
                persistencia.salvar_github(
                    pd.DataFrame(), "data/orcamentos.csv", "token", "repo"
                )

    def test_catalogos_estruturais_continuam_lidos_da_main(self):
        catalogo = pd.DataFrame([{"Material": "Areia"}])
        with patch.object(
            persistencia, "carregar_github_main", return_value=catalogo
        ) as ler_main, patch.object(persistencia, "ler_csv_operacional") as ler_op:
            resultado = persistencia.carregar_github(
                "data/materiais.csv", "token", "repo"
            )

        self.assertIs(resultado, catalogo)
        ler_main.assert_called_once()
        ler_op.assert_not_called()

    def test_fluxo_ativo_inteiro_importa_backend_operacional(self):
        caminhos = (
            "app.py",
            "pages/orcamento/dashboard.py",
            "pages/orcamento/etapa0.py",
            "pages/orcamento/etapa1.py",
            "pages/orcamento/etapa2.py",
            "pages/orcamento/etapa3.py",
        )
        for caminho in caminhos:
            with self.subTest(caminho=caminho), open(caminho, encoding="utf-8") as arquivo:
                fonte = arquivo.read()
            self.assertIn("services.orcamentos_legado_operacional", fonte)

    def test_backend_nao_possui_fallback_de_escrita_para_main(self):
        fonte = inspect.getsource(persistencia.salvar_github)
        self.assertNotIn("salvar_github_main", fonte)


if __name__ == "__main__":
    unittest.main()
