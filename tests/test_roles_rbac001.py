import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from services import autorizacao, roles
from services.github import ResultadoEscritaCSV, ResultadoLeituraCSV, StatusEscrita, StatusLeitura


ROOT = Path(__file__).resolve().parents[1]


def leitura(dados=None, status=StatusLeitura.SUCESSO_COM_DADOS, sha="sha-roles"):
    return ResultadoLeituraCSV(
        status, roles._df(dados, roles.COLUNAS_ROLES), roles.ARQUIVO_ROLES,
        sha=sha, erro=None if status == StatusLeitura.SUCESSO_COM_DADOS else "falha",
    )


class TestCatalogoRolesRBAC001(unittest.TestCase):
    def setUp(self):
        roles.st.secrets = {"GITHUB_TOKEN": "token", "REPO": "org/repo"}
        roles.st.session_state = {"autenticado": True, "usuario": "fabio"}
        self.escrita_ok = ResultadoEscritaCSV(
            StatusEscrita.SUCESSO_ATUALIZADO, roles.ARQUIVO_ROLES, sha="novo-sha"
        )

    def criar(self, **mudancas):
        argumentos = dict(
            leitura=leitura(), codigo="OPERACAO", nome="Operação",
            descricao="Atividades operacionais",
        )
        argumentos.update(mudancas)
        return roles.criar_role(**argumentos)

    def test_catalogos_possuem_schema_exato_e_roles_institucionais(self):
        df_roles = pd.read_csv(ROOT / roles.ARQUIVO_ROLES)
        df_permissoes = pd.read_csv(ROOT / roles.ARQUIVO_PERMISSOES)
        self.assertEqual(df_roles.columns.tolist(), roles.COLUNAS_ROLES)
        self.assertEqual(df_permissoes.columns.tolist(), roles.COLUNAS_PERMISSOES)
        self.assertEqual(
            df_roles["codigo"].tolist(),
            ["FUNCIONARIO", "ENCARREGADO", "APROVADOR", "ENGENHARIA", "FINANCEIRO", "RH"],
        )
        self.assertTrue(df_permissoes.empty)

    def test_criacao_normaliza_codigo_e_inicia_inativa(self):
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github", return_value=self.escrita_ok
        ) as salvar:
            resultado = self.criar(codigo="  apoio-tecnico ")
        self.assertTrue(resultado.sucesso)
        registro = salvar.call_args.args[0].iloc[0]
        self.assertEqual(registro["codigo"], "APOIO_TECNICO")
        self.assertEqual(registro["ativo"], "nao")
        self.assertEqual(int(registro["versao"]), 1)
        self.assertTrue(registro["role_id"])

    def test_usuario_comum_e_admin_operacional_nao_gravam(self):
        for perfil in ("user", "admin"):
            with self.subTest(perfil=perfil), patch.object(
                roles, "pode_gerenciar_roles", return_value=False
            ), patch.object(roles, "salvar_csv_github") as salvar:
                self.assertEqual(self.criar().codigo, "nao_autorizado")
                salvar.assert_not_called()

    def test_superadmin_e_proprietario_recuperado_podem_criar(self):
        for autoridade in ("superadmin", "proprietario_recuperado"):
            with self.subTest(autoridade=autoridade), patch.object(
                roles, "pode_gerenciar_roles", return_value=True
            ), patch.object(roles, "salvar_csv_github", return_value=self.escrita_ok):
                self.assertTrue(self.criar().sucesso)

    def test_revalidacao_imediata_bloqueia_persistencia(self):
        with patch.object(
            roles, "pode_gerenciar_roles", side_effect=(True, False)
        ), patch.object(roles, "salvar_csv_github") as salvar:
            self.assertEqual(self.criar().codigo, "nao_autorizado")
            salvar.assert_not_called()

    def test_codigo_duplicado_e_invalido_sao_negados(self):
        existente = pd.DataFrame([{
            "role_id": "id-1", "codigo": "OPERACAO", "nome": "Operação",
            "descricao": "", "ativo": "sim", "versao": 1,
        }])
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github"
        ) as salvar:
            self.assertEqual(self.criar(leitura=leitura(existente), codigo=" operacao ").codigo, "codigo_duplicado")
            self.assertEqual(self.criar(codigo="1CODIGO").codigo, "codigo_invalido")
            salvar.assert_not_called()

    def test_roles_protegidas_e_equivalentes_sao_negadas(self):
        proibidas = ("SUPERADMIN", "super_admin", "OWNER", "PROPRIETÁRIO", "ROOT", "SYSTEM")
        with patch.object(roles, "pode_gerenciar_roles", return_value=True):
            for codigo in proibidas:
                with self.subTest(codigo=codigo), patch.object(roles, "salvar_csv_github") as salvar:
                    self.assertEqual(self.criar(codigo=codigo).codigo, "role_protegida")
                    salvar.assert_not_called()

    def test_edicao_preserva_uuid_codigo_e_incrementa_versao(self):
        existente = pd.DataFrame([{
            "role_id": "id-imutavel", "codigo": "OPERACAO", "nome": "Antiga",
            "descricao": "Antes", "ativo": "sim", "versao": 4,
            "criado_em": "antes", "criado_por": "autor", "atualizado_em": "antes",
            "atualizado_por": "autor",
        }])
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github", return_value=self.escrita_ok
        ) as salvar:
            resultado = roles.editar_role(
                leitura=leitura(existente), role_id="id-imutavel", nome="Nova",
                descricao="Depois", ativo="nao",
            )
        self.assertTrue(resultado.sucesso)
        registro = salvar.call_args.args[0].iloc[0]
        self.assertEqual(registro["role_id"], "id-imutavel")
        self.assertEqual(registro["codigo"], "OPERACAO")
        self.assertEqual(registro["ativo"], "nao")
        self.assertEqual(int(registro["versao"]), 5)
        self.assertEqual(len(salvar.call_args.args[0]), 1)

    def test_ativacao_e_inativacao_preservam_registro(self):
        for estado in ("sim", "nao"):
            existente = pd.DataFrame([{
                "role_id": "id-1", "codigo": "OPERACAO", "nome": "Operação",
                "descricao": "", "ativo": "nao", "versao": 1,
            }])
            with self.subTest(estado=estado), patch.object(
                roles, "pode_gerenciar_roles", return_value=True
            ), patch.object(roles, "salvar_csv_github", return_value=self.escrita_ok) as salvar:
                resultado = roles.editar_role(
                    leitura=leitura(existente), role_id="id-1", nome="Operação",
                    ativo=estado,
                )
                self.assertTrue(resultado.sucesso)
                self.assertEqual(len(salvar.call_args.args[0]), 1)
                self.assertEqual(salvar.call_args.args[0].iloc[0]["ativo"], estado)

    def test_concorrencia_usa_sha_observado_e_conflito_e_propagado(self):
        conflito = ResultadoEscritaCSV(
            StatusEscrita.CONFLITO, roles.ARQUIVO_ROLES, erro="conflito"
        )
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github", return_value=conflito
        ) as salvar:
            resultado = self.criar()
        self.assertFalse(resultado.sucesso)
        self.assertEqual(resultado.codigo, "falha_persistencia")
        self.assertEqual(salvar.call_args.kwargs["sha_esperado"], "sha-roles")

    def test_falha_de_leitura_nao_e_base_vazia(self):
        falha = leitura(status=StatusLeitura.FALHA_TEMPORARIA, sha=None)
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github"
        ) as salvar:
            self.assertEqual(self.criar(leitura=falha).codigo, "leitura_nao_confirmada")
            salvar.assert_not_called()

    def test_exclusao_nao_existe_e_interface_nao_a_oferece(self):
        self.assertFalse(hasattr(roles, "excluir_role"))
        fonte = (ROOT / "pages" / "administracao.py").read_text(encoding="utf-8")
        self.assertNotIn("excluir_role", fonte)
        self.assertIn("Roles não podem ser excluídas", fonte)

    def test_catalogo_nao_vincula_usuario_nem_calcula_permissoes(self):
        colunas = set(roles.COLUNAS_ROLES + roles.COLUNAS_PERMISSOES)
        self.assertNotIn("usuario", colunas)
        self.assertNotIn("obra_id", colunas)
        self.assertFalse(hasattr(roles, "calcular_permissoes"))
        self.assertEqual(
            roles.ACOES_PADRONIZADAS,
            ("visualizar", "criar", "editar", "excluir", "aprovar", "cancelar", "administrar"),
        )
        self.assertEqual(roles.EFEITOS, ("allow", "deny"))


class TestAutorizacaoRolesRBAC001(unittest.TestCase):
    def setUp(self):
        autorizacao.st.session_state.clear()

    def test_guarda_central_preserva_superadmin_admin_e_proprietario(self):
        casos = (
            ("user", False, False),
            ("admin", False, False),
            ("superadmin", False, True),
            ("user", True, True),
        )
        for perfil, recuperado, esperado in casos:
            with self.subTest(perfil=perfil, recuperado=recuperado):
                autorizacao.st.session_state.update(
                    autenticado=True, usuario="usuario", perfil=perfil,
                )
                with patch.object(
                    autorizacao, "recuperacao_administrativa_ativa", return_value=recuperado
                ):
                    self.assertEqual(autorizacao.pode_gerenciar_roles(), esperado)


if __name__ == "__main__":
    unittest.main()
