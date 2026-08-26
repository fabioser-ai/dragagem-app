import importlib
import sys
import types
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

import pandas as pd

from services.github import ResultadoEscritaCSV, StatusEscrita


ROOT = Path(__file__).resolve().parents[1]


def carregar_pagina(nome):
    st = types.ModuleType("streamlit")
    st.secrets = {"GITHUB_TOKEN": "token-teste", "REPO": "repo-teste"}
    st.session_state = {"autenticado": True, "usuario": "usuario-teste"}
    for atributo in ("error", "success", "rerun"):
        setattr(st, atributo, Mock())

    with patch.dict(sys.modules, {"streamlit": st}):
        sys.modules.pop(nome, None)
        modulo = importlib.import_module(nome)
    return modulo


prestacao = carregar_pagina("pages.prestacao_contas")
uniformes = carregar_pagina("pages.uniformes_epis")


class TestPrestacaoContasRBAC003(unittest.TestCase):
    def setUp(self):
        prestacao.st.error.reset_mock()

    def test_sem_autorizacao_nao_grava_comprovante(self):
        upload = SimpleNamespace(name="nota.pdf", getvalue=lambda: b"pdf")
        with patch.object(prestacao, "pode", return_value=False), patch.object(
            prestacao, "salvar_arquivo_github"
        ) as salvar:
            with self.assertRaises(PermissionError):
                prestacao.salvar_comprovante(upload, "despesa-1")
        salvar.assert_not_called()

    def test_sem_autorizacao_nao_grava_csv(self):
        with patch.object(prestacao, "pode", return_value=False), patch.object(
            prestacao, "salvar_github"
        ) as salvar:
            self.assertFalse(prestacao.salvar_despesas_seguro(pd.DataFrame()))
        salvar.assert_not_called()

    def test_usuario_autorizado_revalida_antes_das_duas_persistencias(self):
        upload = SimpleNamespace(name="nota.pdf", getvalue=lambda: b"pdf")
        with patch.object(prestacao, "pode", return_value=True) as autorizar, patch.object(
            prestacao, "salvar_arquivo_github"
        ) as salvar_arquivo, patch.object(prestacao, "salvar_github") as salvar_csv:
            caminho = prestacao.salvar_comprovante(upload, "despesa-1")
            self.assertTrue(prestacao.salvar_despesas_seguro(pd.DataFrame()))

        self.assertIn("despesa-1", caminho)
        salvar_arquivo.assert_called_once()
        salvar_csv.assert_called_once()
        self.assertEqual(autorizar.call_count, 2)
        for chamada in autorizar.call_args_list:
            self.assertEqual(
                chamada.kwargs,
                {"modulo": "prestacao_contas", "recurso": "despesa", "acao": "criar"},
            )


class TestUniformesEpisRBAC003(unittest.TestCase):
    def setUp(self):
        uniformes.st.error.reset_mock()
        uniformes.st.success.reset_mock()
        uniformes.st.rerun.reset_mock()
        self.resultado = ResultadoEscritaCSV(
            StatusEscrita.SUCESSO_ATUALIZADO, "data/arquivo.csv"
        )

    def test_operacoes_consultam_permissao_especifica(self):
        recursos = ("item", "compra", "movimentacao", "entrega", "devolucao", "baixa")
        for recurso in recursos:
            with self.subTest(recurso=recurso), patch.object(
                uniformes, "pode", side_effect=(True,)
            ) as autorizar:
                self.assertTrue(uniformes._pode_operacao(recurso, "criar"))
                autorizar.assert_called_once_with(
                    modulo="uniformes_epis", recurso=recurso, acao="criar"
                )

    def test_guarda_legada_preserva_admin_operacional(self):
        with patch.object(uniformes, "pode", side_effect=(False, True)) as autorizar:
            self.assertTrue(uniformes._pode_operacao("compra", "criar"))
        self.assertEqual(autorizar.call_args_list[1].kwargs, {
            "modulo": "uniformes_epis", "recurso": "cadastros", "acao": "editar"
        })

    def test_usuario_comum_sem_permissao_nao_persiste(self):
        with patch.object(uniformes, "_pode_operacao", return_value=False), patch.object(
            uniformes, "salvar_base"
        ) as salvar:
            resultado = uniformes._salvar(
                pd.DataFrame(), "data/arquivo.csv", [], None, "ok", recurso="item"
            )
        self.assertFalse(resultado)
        salvar.assert_not_called()

    def test_autoridades_validas_persistem_sem_bypass_local(self):
        for autoridade in ("admin_operacional", "superadmin", "proprietario_recuperado"):
            with self.subTest(autoridade=autoridade), patch.object(
                uniformes, "_pode_operacao", return_value=True
            ), patch.object(uniformes, "salvar_base", return_value=self.resultado) as salvar:
                self.assertTrue(
                    uniformes._salvar(
                        pd.DataFrame(),
                        "data/arquivo.csv",
                        [],
                        None,
                        "ok",
                        recurso="entrega",
                    )
                )
                salvar.assert_called_once()


class TestCatalogoERegressoesRBAC003(unittest.TestCase):
    def test_catalogo_elimina_estado_inexistente_sem_conceder_rbac(self):
        catalogo = pd.read_csv(ROOT / "data/permissoes_catalogo.csv", dtype=str).fillna("")
        estados = catalogo["estado_protecao"].value_counts().to_dict()
        self.assertEqual(
            estados,
            {"completa": 33, "parcial": 23, "específica de Medições": 6},
        )
        local = catalogo[
            (catalogo["modulo"] == "dados")
            & (catalogo["recurso"] == "local_trabalho")
            & (catalogo["acao"] == "criar")
        ].iloc[0]
        self.assertEqual(local["estado_protecao"], "completa")
        matriz_roles = pd.read_csv(ROOT / "data/roles_permissoes.csv", dtype=str)
        self.assertEqual(
            matriz_roles.columns.tolist(),
            ["role_id", "modulo", "recurso", "acao", "efeito"],
        )
        self.assertNotIn("usuario", matriz_roles.columns)

    def test_ferias_mantem_revalidacao_central_e_recurso_legado(self):
        fonte = (ROOT / "pages/ferias.py").read_text(encoding="utf-8")
        self.assertIn('pode(modulo="ferias", recurso=recurso, acao=acao)', fonte)
        self.assertIn('recurso="registros"', fonte)

    def test_medicoes_e_autenticacao_ficam_fora_do_diff_documentado(self):
        fonte = (ROOT / "docs/RBAC003_ENDURECIMENTO_FRONTEIRAS.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Autenticação", fonte)
        self.assertIn("Medições não foram alterados", fonte)


if __name__ == "__main__":
    unittest.main()
