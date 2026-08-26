import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from services import roles
from services.github import ResultadoEscritaCSV, ResultadoLeituraCSV, StatusEscrita, StatusLeitura


ROOT = Path(__file__).resolve().parents[1]


def leitura_roles(ativo="sim"):
    dados = pd.DataFrame([{
        "role_id": "r1", "codigo": "ENGENHARIA", "nome": "Engenharia",
        "descricao": "Engenharia", "ativo": ativo, "versao": 1,
        "criado_em": "", "criado_por": "", "atualizado_em": "", "atualizado_por": "",
    }])
    return ResultadoLeituraCSV(
        StatusLeitura.SUCESSO_COM_DADOS,
        roles._df(dados, roles.COLUNAS_ROLES),
        roles.ARQUIVO_ROLES,
        sha="sha-roles",
    )


def leitura_matriz(dados=None, status=StatusLeitura.SUCESSO_COM_DADOS):
    base = pd.DataFrame(dados or [], columns=roles.COLUNAS_PERMISSOES)
    return ResultadoLeituraCSV(
        status,
        roles._df(base, roles.COLUNAS_PERMISSOES),
        roles.ARQUIVO_PERMISSOES,
        sha="sha-matriz" if status == StatusLeitura.SUCESSO_COM_DADOS else None,
        erro=None if status == StatusLeitura.SUCESSO_COM_DADOS else "falha",
    )


def catalogo():
    return pd.DataFrame([
        {
            "modulo": "dados", "recurso": "cadastro", "acao": "visualizar",
            "nome": "Consultar cadastros", "descricao": "Consulta", "sensibilidade": "baixa", "ativo": "sim",
        },
        {
            "modulo": "obras", "recurso": "obra", "acao": "visualizar",
            "nome": "Consultar obras", "descricao": "Consulta", "sensibilidade": "baixa", "ativo": "sim",
        },
        {
            "modulo": "administracao", "recurso": "role", "acao": "editar",
            "nome": "Editar Role", "descricao": "Crítica", "sensibilidade": "crítica", "ativo": "sim",
        },
    ])


class TestRBACUX001RolePermissionsEditor(unittest.TestCase):
    def setUp(self):
        roles.st.secrets = {"GITHUB_TOKEN": "token", "REPO": "org/repo"}
        roles.st.session_state = {"usuario": "fabio"}
        self.escrita_ok = ResultadoEscritaCSV(
            StatusEscrita.SUCESSO_ATUALIZADO, roles.ARQUIVO_PERMISSOES, sha="novo-sha"
        )

    def salvar(self, **trocas):
        args = dict(
            leitura=leitura_matriz(),
            leitura_roles=leitura_roles(),
            catalogo_permissoes=catalogo(),
            role_id="r1",
            chaves_allow={("dados", "cadastro", "visualizar")},
        )
        args.update(trocas)
        return roles.salvar_roles_permissoes(**args)

    def test_adiciona_allow_valido_e_usa_sha_observado(self):
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github", return_value=self.escrita_ok
        ) as salvar:
            resultado = self.salvar()
        self.assertTrue(resultado.sucesso)
        gravado = salvar.call_args.args[0]
        self.assertEqual(
            gravado[["role_id", "modulo", "recurso", "acao", "efeito"]].values.tolist(),
            [["r1", "dados", "cadastro", "visualizar", "allow"]],
        )
        self.assertEqual(salvar.call_args.kwargs["sha_esperado"], "sha-matriz")
        self.assertIn("ENGENHARIA", salvar.call_args.kwargs["mensagem"])

    def test_substitui_allows_sem_duplicar(self):
        atual = [["r1", "dados", "cadastro", "visualizar", "allow"]]
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github", return_value=self.escrita_ok
        ) as salvar:
            resultado = self.salvar(
                leitura=leitura_matriz(atual),
                chaves_allow={
                    ("dados", "cadastro", "visualizar"),
                    ("obras", "obra", "visualizar"),
                },
            )
        self.assertTrue(resultado.sucesso)
        gravado = salvar.call_args.args[0]
        self.assertEqual(len(gravado), 2)
        self.assertFalse(gravado.duplicated(["role_id", "modulo", "recurso", "acao"]).any())

    def test_preserva_denies_existentes(self):
        atual = [["r1", "obras", "obra", "visualizar", "deny"]]
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github", return_value=self.escrita_ok
        ) as salvar:
            resultado = self.salvar(leitura=leitura_matriz(atual))
        self.assertTrue(resultado.sucesso)
        gravado = salvar.call_args.args[0]
        self.assertIn(
            ["r1", "obras", "obra", "visualizar", "deny"],
            gravado[roles.COLUNAS_PERMISSOES].values.tolist(),
        )

    def test_permissao_critica_ou_administracao_e_negada(self):
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github"
        ) as salvar:
            resultado = self.salvar(chaves_allow={("administracao", "role", "editar")})
        self.assertFalse(resultado.sucesso)
        self.assertEqual(resultado.codigo, "permissao_proibida")
        salvar.assert_not_called()

    def test_permissao_fora_do_catalogo_e_negada(self):
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github"
        ) as salvar:
            resultado = self.salvar(chaves_allow={("dados", "fantasma", "visualizar")})
        self.assertFalse(resultado.sucesso)
        self.assertEqual(resultado.codigo, "permissao_proibida")
        salvar.assert_not_called()

    def test_role_inativa_nao_e_editada(self):
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github"
        ) as salvar:
            resultado = self.salvar(leitura_roles=leitura_roles("nao"))
        self.assertFalse(resultado.sucesso)
        self.assertEqual(resultado.codigo, "role_inativa")
        salvar.assert_not_called()

    def test_leitura_ambigua_nao_grava(self):
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github"
        ) as salvar:
            resultado = self.salvar(
                leitura=leitura_matriz(status=StatusLeitura.FALHA_TEMPORARIA)
            )
        self.assertFalse(resultado.sucesso)
        self.assertEqual(resultado.codigo, "leitura_nao_confirmada")
        salvar.assert_not_called()

    def test_revalidacao_imediata_bloqueia_gravacao(self):
        with patch.object(
            roles, "pode_gerenciar_roles", side_effect=(True, False)
        ), patch.object(roles, "salvar_csv_github") as salvar:
            resultado = self.salvar()
        self.assertFalse(resultado.sucesso)
        self.assertEqual(resultado.codigo, "nao_autorizado")
        salvar.assert_not_called()

    def test_conflito_de_sha_e_propagado_sem_sucesso(self):
        conflito = ResultadoEscritaCSV(
            StatusEscrita.CONFLITO, roles.ARQUIVO_PERMISSOES, erro="conflito"
        )
        with patch.object(roles, "pode_gerenciar_roles", return_value=True), patch.object(
            roles, "salvar_csv_github", return_value=conflito
        ):
            resultado = self.salvar()
        self.assertFalse(resultado.sucesso)
        self.assertEqual(resultado.codigo, "falha_persistencia")

    def test_ux_expoe_editor_humano_confirmacao_e_nao_expoe_admin(self):
        fonte = (ROOT / "pages" / "administracao.py").read_text(encoding="utf-8")
        self.assertIn("_render_editor_permissoes_role", fonte)
        self.assertIn("st.multiselect", fonte)
        self.assertIn("Salvar permissões", fonte)
        self.assertIn("modifica o acesso real", fonte)
        self.assertIn("sensibilidade", fonte)
        self.assertIn('!= "administracao"', fonte)
        self.assertIn("deny", fonte)


if __name__ == "__main__":
    unittest.main()
