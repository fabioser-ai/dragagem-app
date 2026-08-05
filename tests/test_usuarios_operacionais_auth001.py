import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import pandas as pd

from services.github import ResultadoEscritaCSV, ResultadoLeituraCSV, StatusEscrita, StatusLeitura
from services import usuarios_operacionais as usuarios


ROOT = Path(__file__).resolve().parents[1]


def leitura(dados=None, status=StatusLeitura.SUCESSO_COM_DADOS, sha="sha-base"):
    return ResultadoLeituraCSV(
        status, usuarios._df(dados), usuarios.ARQUIVO, sha=sha,
        erro=None if status == StatusLeitura.SUCESSO_COM_DADOS else "falha",
    )


class TestUsuariosOperacionaisAUTH001(unittest.TestCase):
    def setUp(self):
        usuarios.st.secrets = {
            "APP_USERS": '{"Fabio":{"role":"superadmin"}}',
            "GITHUB_TOKEN": "token",
            "REPO": "org/repo",
        }
        usuarios.st.session_state = {"autenticado": True, "usuario": "fabio"}
        self.salvo = ResultadoEscritaCSV(
            StatusEscrita.SUCESSO_ATUALIZADO, usuarios.ARQUIVO, sha="novo-sha"
        )

    def criar(self, **alteracoes):
        argumentos = dict(
            leitura=leitura(), login="operador.1", nome="Operador Um",
            matricula="M-1", email="operador@example.com", perfil_base="user",
        )
        argumentos.update(alteracoes)
        return usuarios.criar_usuario(**argumentos)

    def test_criacao_autorizada_superadmin_ou_proprietario_recuperado(self):
        for autoridade in ("superadmin", "proprietario_recuperado"):
            with self.subTest(autoridade=autoridade), patch.object(
                usuarios, "pode_gerenciar_usuarios_operacionais", return_value=True
            ), patch.object(usuarios, "salvar_csv_github", return_value=self.salvo) as salvar:
                resultado = self.criar()
                self.assertTrue(resultado.sucesso)
                registro = salvar.call_args.args[0].iloc[0]
                self.assertEqual(registro["ativo"], "nao")
                self.assertEqual(registro["perfil_base"], "user")
                self.assertEqual(registro["credencial_configurada"], "nao")
                self.assertEqual(registro["exige_troca_senha"], "nao")

    def test_usuario_comum_e_admin_nao_autorizado_nao_gravam(self):
        for perfil in ("user", "admin"):
            with self.subTest(perfil=perfil), patch.object(
                usuarios, "pode_gerenciar_usuarios_operacionais", return_value=False
            ), patch.object(usuarios, "salvar_csv_github") as salvar:
                self.assertEqual(self.criar().codigo, "nao_autorizado")
                salvar.assert_not_called()

    def test_revalidacao_imediata_impede_persistencia(self):
        with patch.object(
            usuarios, "pode_gerenciar_usuarios_operacionais", side_effect=(True, False)
        ), patch.object(usuarios, "salvar_csv_github") as salvar:
            self.assertEqual(self.criar().codigo, "nao_autorizado")
            salvar.assert_not_called()

    def test_login_interno_duplicado_e_conflito_protegido_sao_negados(self):
        existente = usuarios._df(pd.DataFrame([{
            "usuario_id": "id-1", "login": "operador.1", "nome": "Um",
            "matricula": "", "perfil_base": "user", "ativo": "nao",
        }]))
        with patch.object(usuarios, "pode_gerenciar_usuarios_operacionais", return_value=True):
            self.assertEqual(self.criar(leitura=leitura(existente), login=" OPERADOR.1 ").codigo, "login_duplicado")
            self.assertEqual(self.criar(login=" fAbIo ").codigo, "login_protegido")

    def test_espacos_sao_normalizados_e_uuid_e_novo(self):
        with patch.object(usuarios, "pode_gerenciar_usuarios_operacionais", return_value=True), patch.object(
            usuarios, "salvar_csv_github", return_value=self.salvo
        ) as salvar:
            self.assertTrue(self.criar(login=" Operador.1 ").sucesso)
        registro = salvar.call_args.args[0].iloc[0]
        self.assertEqual(registro["login"], "operador.1")
        self.assertTrue(registro["usuario_id"])

    def test_perfis_elevados_e_desconhecidos_sao_negados(self):
        for perfil in ("superadmin", "proprietario", "owner", "admin", "desconhecido"):
            with self.subTest(perfil=perfil), patch.object(
                usuarios, "pode_gerenciar_usuarios_operacionais", return_value=True
            ), patch.object(usuarios, "salvar_csv_github") as salvar:
                self.assertEqual(self.criar(perfil_base=perfil).codigo, "perfil_negado")
                salvar.assert_not_called()

    def test_matricula_duplicada_e_negada(self):
        existente = usuarios._df(pd.DataFrame([{
            "usuario_id": "id-1", "login": "outro", "nome": "Outro",
            "matricula": " M-1 ", "perfil_base": "user", "ativo": "nao",
        }]))
        with patch.object(usuarios, "pode_gerenciar_usuarios_operacionais", return_value=True):
            self.assertEqual(self.criar(leitura=leitura(existente)).codigo, "matricula_duplicada")

    def test_edicao_preserva_id_login_registro_e_permite_inativacao(self):
        existente = usuarios._df(pd.DataFrame([{
            "usuario_id": "id-imutavel", "login": "operador.1", "nome": "Antigo",
            "matricula": "M-1", "email": "", "perfil_base": "user", "ativo": "sim",
            "criado_em": "antes", "criado_por": "autor", "atualizado_em": "antes",
            "atualizado_por": "autor", "exige_troca_senha": "nao",
            "credencial_configurada": "nao",
        }]))
        with patch.object(usuarios, "pode_gerenciar_usuarios_operacionais", return_value=True), patch.object(
            usuarios, "salvar_csv_github", return_value=self.salvo
        ) as salvar:
            resultado = usuarios.editar_usuario(
                leitura=leitura(existente), usuario_id="id-imutavel", nome="Novo",
                matricula="M-1", email="novo@example.com", perfil_base="funcionario", ativo="nao",
            )
        self.assertTrue(resultado.sucesso)
        registro = salvar.call_args.args[0].iloc[0]
        self.assertEqual(registro["usuario_id"], "id-imutavel")
        self.assertEqual(registro["login"], "operador.1")
        self.assertEqual(registro["ativo"], "nao")
        self.assertEqual(len(salvar.call_args.args[0]), 1)

    def test_falhas_de_leitura_negam_sem_tratar_base_como_vazia(self):
        falha = leitura(status=StatusLeitura.FALHA_TEMPORARIA, sha=None)
        with patch.object(usuarios, "pode_gerenciar_usuarios_operacionais", return_value=True), patch.object(
            usuarios, "salvar_csv_github"
        ) as salvar:
            self.assertEqual(self.criar(leitura=falha).codigo, "leitura_nao_confirmada")
            salvar.assert_not_called()

    def test_falha_app_users_bloqueia_sem_expor_conteudo(self):
        usuarios.st.secrets.pop("APP_USERS")
        with patch.object(usuarios, "pode_gerenciar_usuarios_operacionais", return_value=True), patch.object(
            usuarios, "salvar_csv_github"
        ) as salvar:
            resultado = self.criar()
        self.assertEqual(resultado.codigo, "app_users_indisponivel")
        self.assertNotIn("APP_USERS", resultado.mensagem)
        salvar.assert_not_called()

    def test_nenhuma_credencial_secret_ou_permissao_e_persistida(self):
        with patch.object(usuarios, "pode_gerenciar_usuarios_operacionais", return_value=True), patch.object(
            usuarios, "salvar_csv_github", return_value=self.salvo
        ) as salvar:
            self.assertTrue(self.criar().sucesso)
        colunas = set(salvar.call_args.args[0].columns)
        for proibida in ("password", "senha", "hash", "secret", "token", "permissao"):
            self.assertNotIn(proibida, colunas)

    def test_base_e_interface_nao_oferecem_exclusao_ou_edicao_protegida(self):
        fonte = (ROOT / "pages" / "administracao.py").read_text(encoding="utf-8")
        self.assertNotIn("SYSTEM_OWNER_ID", fonte)
        self.assertNotIn("st.secrets", fonte)
        self.assertNotIn("excluir_usuario", fonte)
        self.assertIn("não são ", fonte)
        self.assertIn("editáveis nesta interface", fonte)


if __name__ == "__main__":
    unittest.main()
