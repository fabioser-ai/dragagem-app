import hashlib
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from services import autorizacao, permissoes_catalogo as catalogo, roles
from services.github import ResultadoEscritaCSV, ResultadoLeituraCSV, StatusEscrita, StatusLeitura


ROOT = Path(__file__).resolve().parents[1]


def matriz():
    return pd.read_csv(ROOT / catalogo.ARQUIVO, dtype=str).fillna("")


def leitura(dados=None, status=StatusLeitura.SUCESSO_COM_DADOS, sha="sha-catalogo"):
    return ResultadoLeituraCSV(
        status, catalogo._df(matriz() if dados is None else dados), catalogo.ARQUIVO,
        sha=sha, erro=None if status == StatusLeitura.SUCESSO_COM_DADOS else "falha",
    )


class TestCatalogoPermissoesRBAC002(unittest.TestCase):
    def setUp(self):
        catalogo.st.secrets = {"GITHUB_TOKEN": "token", "REPO": "org/repo"}
        catalogo.st.session_state = {"autenticado": True, "usuario": "fabio"}
        self.escrita_ok = ResultadoEscritaCSV(
            StatusEscrita.SUCESSO_ATUALIZADO, catalogo.ARQUIVO, sha="novo-sha"
        )

    def test_matriz_institucional_e_valida_unica_e_rastreavel(self):
        df = matriz()
        self.assertEqual(df.columns.tolist(), catalogo.COLUNAS)
        self.assertEqual(len(df), 66)
        self.assertEqual(df["permissao_id"].nunique(), 66)
        self.assertFalse(df.duplicated(["modulo", "recurso", "acao"]).any())
        self.assertEqual(catalogo.validar_catalogo(df), [])
        self.assertTrue((df["evidencia"].str.strip() != "").all())

    def test_acao_fora_do_catalogo_e_negada(self):
        df = matriz()
        df.loc[0, "acao"] = "enviar"
        self.assertTrue(any(e.startswith("acao_invalida") for e in catalogo.validar_catalogo(df)))

    def test_modulo_desconhecido_e_negado(self):
        df = matriz()
        df.loc[0, "modulo"] = "desconhecido"
        self.assertTrue(any(e.startswith("modulo_invalido") for e in catalogo.validar_catalogo(df)))

    def test_recurso_vazio_e_negado(self):
        df = matriz()
        df.loc[0, "recurso"] = ""
        self.assertTrue(any(e.startswith("recurso_invalido") for e in catalogo.validar_catalogo(df)))

    def test_sensibilidade_e_estado_aceitam_apenas_valores_homologados(self):
        df = matriz()
        df.loc[0, "sensibilidade"] = "extrema"
        df.loc[1, "estado_protecao"] = "quase completa"
        erros = catalogo.validar_catalogo(df)
        self.assertTrue(any(e.startswith("sensibilidade_invalida") for e in erros))
        self.assertTrue(any(e.startswith("estado_protecao_invalido") for e in erros))

    def test_permissao_id_e_identidade_sao_imutaveis(self):
        atual = matriz()
        alterado = atual.copy()
        alterado.loc[0, "modulo"] = "dados"
        with patch.object(catalogo, "pode_gerenciar_catalogo_permissoes", return_value=True), patch.object(
            catalogo, "salvar_csv_github"
        ) as salvar:
            resultado = catalogo.salvar_catalogo_seguro(alterado, leitura=leitura(atual))
        self.assertEqual(resultado.codigo, "catalogo_invalido")
        self.assertIn("identidade_imutavel", resultado.mensagem)
        salvar.assert_not_called()

    def test_exclusao_fisica_nao_existe(self):
        atual = matriz()
        reduzido = atual.iloc[1:].reset_index(drop=True)
        with patch.object(catalogo, "pode_gerenciar_catalogo_permissoes", return_value=True), patch.object(
            catalogo, "salvar_csv_github"
        ) as salvar:
            resultado = catalogo.salvar_catalogo_seguro(reduzido, leitura=leitura(atual))
        self.assertIn("exclusao_fisica_negada", resultado.mensagem)
        self.assertFalse(hasattr(catalogo, "excluir_permissao"))
        salvar.assert_not_called()

    def test_nova_permissao_deve_nascer_inativa(self):
        atual = matriz()
        nova = atual.iloc[0].copy()
        nova["permissao_id"] = "00000000-0000-4000-8000-999999999999"
        nova["modulo"] = "obras"
        nova["recurso"] = "documento_obra"
        nova["acao"] = "visualizar"
        nova["ativo"] = "sim"
        proposto = pd.concat([atual, pd.DataFrame([nova])], ignore_index=True)
        with patch.object(catalogo, "pode_gerenciar_catalogo_permissoes", return_value=True):
            resultado = catalogo.salvar_catalogo_seguro(proposto, leitura=leitura(atual))
        self.assertIn("permissao_nova_deve_nascer_inativa", resultado.mensagem)

    def test_usuario_comum_e_admin_nao_administram_catalogo(self):
        for perfil in ("user", "admin"):
            with self.subTest(perfil=perfil), patch.object(
                catalogo, "pode_gerenciar_catalogo_permissoes", return_value=False
            ), patch.object(catalogo, "salvar_csv_github") as salvar:
                resultado = catalogo.salvar_catalogo_seguro(matriz(), leitura=leitura())
                self.assertEqual(resultado.codigo, "nao_autorizado")
                salvar.assert_not_called()

    def test_superadmin_e_proprietario_recuperado_administram(self):
        for autoridade in ("superadmin", "proprietario_recuperado"):
            with self.subTest(autoridade=autoridade), patch.object(
                catalogo, "pode_gerenciar_catalogo_permissoes", return_value=True
            ), patch.object(catalogo, "salvar_csv_github", return_value=self.escrita_ok):
                self.assertTrue(catalogo.salvar_catalogo_seguro(matriz(), leitura=leitura()).sucesso)

    def test_revalidacao_imediata_impede_persistencia(self):
        with patch.object(
            catalogo, "pode_gerenciar_catalogo_permissoes", side_effect=(True, False)
        ), patch.object(catalogo, "salvar_csv_github") as salvar:
            resultado = catalogo.salvar_catalogo_seguro(matriz(), leitura=leitura())
        self.assertEqual(resultado.codigo, "nao_autorizado")
        salvar.assert_not_called()

    def test_falha_de_leitura_bloqueia_persistencia(self):
        falha = leitura(status=StatusLeitura.FALHA_TEMPORARIA, sha=None)
        with patch.object(catalogo, "pode_gerenciar_catalogo_permissoes", return_value=True), patch.object(
            catalogo, "salvar_csv_github"
        ) as salvar:
            resultado = catalogo.salvar_catalogo_seguro(matriz(), leitura=falha)
        self.assertEqual(resultado.codigo, "leitura_nao_confirmada")
        salvar.assert_not_called()

    def test_concorrencia_respeita_sha_observado(self):
        conflito = ResultadoEscritaCSV(
            StatusEscrita.CONFLITO, catalogo.ARQUIVO, erro="conflito"
        )
        with patch.object(catalogo, "pode_gerenciar_catalogo_permissoes", return_value=True), patch.object(
            catalogo, "salvar_csv_github", return_value=conflito
        ) as salvar:
            resultado = catalogo.salvar_catalogo_seguro(matriz(), leitura=leitura())
        self.assertEqual(resultado.codigo, "falha_persistencia")
        self.assertEqual(salvar.call_args.kwargs["sha_esperado"], "sha-catalogo")

    def test_catalogo_nao_altera_acesso_roles_usuarios_auth_ou_medicoes(self):
        caminho_usuarios = ROOT / "data/usuarios_operacionais.csv"
        usuarios_antes = caminho_usuarios.read_bytes()
        usuarios = pd.read_csv(caminho_usuarios, dtype=str).fillna("")
        self.assertEqual(
            usuarios.columns.tolist(),
            [
                "usuario_id", "login", "nome", "matricula", "email",
                "perfil_base", "ativo", "criado_em", "criado_por",
                "atualizado_em", "atualizado_por", "exige_troca_senha",
                "credencial_configurada",
            ],
        )
        self.assertEqual(catalogo.validar_catalogo(matriz()), [])
        self.assertEqual(caminho_usuarios.read_bytes(), usuarios_antes)

        esperados = {
            "data/permissoes_usuarios.csv": "23b33a97d78c41f217e7bcdae397e5fcb555f72c344974adb3b1550cad2dca5e",
            "services/auth.py": "f1d69b8e69d24c829b31558ebbdfa0fe21ebe909aca7aee2fbcabeab22c843bf",
            "pages/medicoes.py": "f23a8cf9d1c7e01f94a93447c1f924dbc2dfd80b1bb904a1a9ff3e64e496257f",
        }
        for caminho, esperado in esperados.items():
            atual = hashlib.sha256((ROOT / caminho).read_bytes()).hexdigest()
            self.assertEqual(atual, esperado, caminho)
        matriz_roles = pd.read_csv(ROOT / "data/roles_permissoes.csv", dtype=str)
        self.assertEqual(matriz_roles.columns.tolist(), roles.COLUNAS_PERMISSOES)
        self.assertNotIn("usuario", matriz_roles.columns)

    def test_interface_e_somente_consulta_e_possui_filtros(self):
        fonte = (ROOT / "pages/administracao.py").read_text(encoding="utf-8")
        self.assertIn("Este catálogo não concede acesso", fonte)
        for rotulo in ("Módulo", "Ação", "Sensibilidade", "Estado da proteção"):
            self.assertIn(rotulo, fonte)
        self.assertNotIn("salvar_catalogo_seguro", fonte)
        self.assertNotIn("conceder_role", fonte)


class TestAutorizacaoCatalogoRBAC002(unittest.TestCase):
    def test_guarda_central_distingue_admin_superadmin_e_custodia(self):
        if not isinstance(autorizacao.st.session_state, dict):
            autorizacao.st.session_state = {}
        autorizacao.st.secrets = {"AUTHORIZATION_MODE": "LEGACY"}
        casos = (("user", False, False), ("admin", False, False), ("superadmin", False, True), ("user", True, True))
        for perfil, recuperado, esperado in casos:
            autorizacao.st.session_state.clear()
            autorizacao.st.session_state.update(autenticado=True, usuario="u", perfil=perfil)
            with patch.object(autorizacao, "recuperacao_administrativa_ativa", return_value=recuperado):
                self.assertEqual(autorizacao.pode_gerenciar_catalogo_permissoes(), esperado)


if __name__ == "__main__":
    unittest.main()
