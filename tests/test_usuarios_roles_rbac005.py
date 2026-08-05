import hashlib
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from services import autorizacao, usuarios_roles as ur
from services.github import ResultadoEscritaCSV, ResultadoLeituraCSV, StatusEscrita, StatusLeitura


ROOT = Path(__file__).resolve().parents[1]
COL_USUARIOS = [
    "usuario_id", "login", "nome", "matricula", "email", "perfil_base",
    "ativo", "criado_em", "criado_por", "atualizado_em", "atualizado_por",
    "exige_troca_senha", "credencial_configurada",
]
COL_ROLES = [
    "role_id", "codigo", "nome", "descricao", "ativo", "versao",
    "criado_em", "criado_por", "atualizado_em", "atualizado_por",
]


def leitura(dados, arquivo="data/teste.csv", sha="sha", status=StatusLeitura.SUCESSO_COM_DADOS):
    return ResultadoLeituraCSV(status, dados, arquivo, sha=sha, erro=None if sha else "falha")


def usuario(usuario_id="u1", login="joao", ativo="sim"):
    linha = {coluna: "" for coluna in COL_USUARIOS}
    linha.update(usuario_id=usuario_id, login=login, nome="João", ativo=ativo)
    return pd.DataFrame([linha])


def roles(*linhas):
    registros = []
    for role_id, codigo, ativo in linhas or (("r1", "FUNCIONARIO", "sim"),):
        linha = {coluna: "" for coluna in COL_ROLES}
        linha.update(role_id=role_id, codigo=codigo, nome=codigo, ativo=ativo, versao="1")
        registros.append(linha)
    return pd.DataFrame(registros)


class TestUsuariosRolesRBAC005(unittest.TestCase):
    def setUp(self):
        ur.st.secrets = {"GITHUB_TOKEN": "token", "REPO": "org/repo", "APP_USERS": {"fabio": {}}}
        ur.st.session_state = {"autenticado": True, "usuario": "fabio"}
        self.vazia = leitura(pd.DataFrame(columns=ur.COLUNAS), ur.ARQUIVO, "sha-assoc")
        self.usuarios = leitura(usuario(), "data/usuarios_operacionais.csv", "sha-u")
        self.roles = leitura(roles(), "data/roles.csv", "sha-r")
        self.escrita = ResultadoEscritaCSV(StatusEscrita.SUCESSO_ATUALIZADO, ur.ARQUIVO)

    def atribuir(self, **mudancas):
        argumentos = dict(
            leitura=self.vazia, leitura_usuarios=self.usuarios,
            leitura_roles=self.roles, usuario_id="u1", role_id="r1",
        )
        argumentos.update(mudancas)
        return ur.atribuir_role(**argumentos)

    def test_atribuicao_autorizada_usa_ids_uuid_e_sha(self):
        with patch.object(ur, "pode_gerenciar_usuarios_roles", return_value=True), patch.object(
            ur, "identificador_proprietario", return_value="owner"
        ), patch.object(ur, "salvar_csv_github", return_value=self.escrita) as salvar:
            resultado = self.atribuir()
        self.assertTrue(resultado.sucesso)
        registro = salvar.call_args.args[0].iloc[0]
        self.assertEqual((registro["usuario_id"], registro["role_id"]), ("u1", "r1"))
        self.assertEqual(registro["ativo"], "sim")
        self.assertTrue(registro["usuario_role_id"])
        self.assertEqual(salvar.call_args.kwargs["sha_esperado"], "sha-assoc")

    def test_retirada_inativa_sem_excluir_e_reativacao_preserva_uuid(self):
        base = pd.DataFrame([{
            "usuario_role_id": "uuid-imutavel", "usuario_id": "u1", "role_id": "r1",
            "ativo": "sim", "criado_em": "antes", "criado_por": "autor",
            "atualizado_em": "antes", "atualizado_por": "autor",
        }])
        leitura_base = leitura(base, ur.ARQUIVO, "sha-base")
        with patch.object(ur, "pode_gerenciar_usuarios_roles", return_value=True), patch.object(
            ur, "salvar_csv_github", return_value=self.escrita
        ) as salvar:
            self.assertTrue(ur.retirar_role(
                leitura=leitura_base, leitura_usuarios=self.usuarios,
                leitura_roles=self.roles, usuario_id="u1", role_id="r1",
            ).sucesso)
            inativada = salvar.call_args.args[0]
            self.assertEqual(len(inativada), 1)
            self.assertEqual(inativada.iloc[0]["ativo"], "nao")
            self.assertEqual(inativada.iloc[0]["usuario_role_id"], "uuid-imutavel")

        leitura_inativa = leitura(inativada, ur.ARQUIVO, "sha-inativa")
        with patch.object(ur, "pode_gerenciar_usuarios_roles", return_value=True), patch.object(
            ur, "identificador_proprietario", return_value="owner"
        ), patch.object(ur, "salvar_csv_github", return_value=self.escrita) as salvar:
            self.assertTrue(self.atribuir(leitura=leitura_inativa).sucesso)
            reativada = salvar.call_args.args[0]
        self.assertEqual(len(reativada), 1)
        self.assertEqual(reativada.iloc[0]["usuario_role_id"], "uuid-imutavel")
        self.assertEqual(reativada.iloc[0]["ativo"], "sim")

    def test_duplicada_ativa_e_negada_sem_escrita(self):
        base = pd.DataFrame([{
            "usuario_role_id": "id", "usuario_id": "u1", "role_id": "r1", "ativo": "sim"
        }])
        with patch.object(ur, "pode_gerenciar_usuarios_roles", return_value=True), patch.object(
            ur, "identificador_proprietario", return_value="owner"
        ), patch.object(ur, "salvar_csv_github") as salvar:
            resultado = self.atribuir(leitura=leitura(base, ur.ARQUIVO))
        self.assertEqual(resultado.codigo, "associacao_duplicada")
        salvar.assert_not_called()

    def test_usuario_inexistente_inativo_e_identificador_textual_sao_negados(self):
        casos = (
            ("inexistente", self.usuarios, "usuario_inexistente"),
            ("u1", leitura(usuario(ativo="nao")), "usuario_inativo"),
            ("joao", self.usuarios, "usuario_inexistente"),
        )
        with patch.object(ur, "pode_gerenciar_usuarios_roles", return_value=True), patch.object(
            ur, "identificador_proprietario", return_value="owner"
        ):
            for usuario_id, leitura_usuarios, codigo in casos:
                with self.subTest(codigo=codigo):
                    self.assertEqual(
                        self.atribuir(usuario_id=usuario_id, leitura_usuarios=leitura_usuarios).codigo,
                        codigo,
                    )

    def test_role_inexistente_inativa_e_codigo_textual_sao_negados(self):
        casos = (
            ("inexistente", self.roles, "role_inexistente"),
            ("r1", leitura(roles(("r1", "FUNCIONARIO", "nao"))), "role_inativa"),
            ("FUNCIONARIO", self.roles, "role_inexistente"),
        )
        with patch.object(ur, "pode_gerenciar_usuarios_roles", return_value=True), patch.object(
            ur, "identificador_proprietario", return_value="owner"
        ):
            for role_id, leitura_roles, codigo in casos:
                with self.subTest(codigo=codigo):
                    self.assertEqual(self.atribuir(role_id=role_id, leitura_roles=leitura_roles).codigo, codigo)

    def test_role_vazia_e_multiplas_roles_sao_validas(self):
        catalogo = leitura(roles(("r1", "ENCARREGADO", "sim"), ("r2", "RH", "sim")))
        with patch.object(ur, "pode_gerenciar_usuarios_roles", return_value=True), patch.object(
            ur, "identificador_proprietario", return_value="owner"
        ), patch.object(ur, "salvar_csv_github", return_value=self.escrita) as salvar:
            self.assertTrue(self.atribuir(leitura_roles=catalogo, role_id="r1").sucesso)
            primeira = salvar.call_args.args[0]
            self.assertTrue(self.atribuir(
                leitura=leitura(primeira, ur.ARQUIVO), leitura_roles=catalogo, role_id="r2"
            ).sucesso)
            segunda = salvar.call_args.args[0]
        self.assertEqual(len(segunda), 2)

    def test_contas_app_users_proprietario_e_superadmin_sao_negadas(self):
        protegidos = leitura(pd.concat([
            usuario("u1", "fabio"), usuario("u2", "owner"), usuario("u3", "superadmin")
        ], ignore_index=True))
        ur.st.secrets["APP_USERS"] = {"fabio": {}, "superadmin": {}}
        with patch.object(ur, "pode_gerenciar_usuarios_roles", return_value=True), patch.object(
            ur, "identificador_proprietario", return_value="owner"
        ):
            for uid in ("u1", "u2", "u3"):
                with self.subTest(uid=uid):
                    self.assertEqual(self.atribuir(usuario_id=uid, leitura_usuarios=protegidos).codigo, "conta_protegida")

    def test_usuario_comum_admin_operacional_superadmin_e_proprietario(self):
        casos = (("user", False, False), ("admin", False, False), ("superadmin", False, True), ("user", True, True))
        for perfil, recuperado, esperado in casos:
            autorizacao.st.session_state.clear()
            autorizacao.st.session_state.update(autenticado=True, usuario="u", perfil=perfil)
            with self.subTest(perfil=perfil), patch.object(
                autorizacao, "recuperacao_administrativa_ativa", return_value=recuperado
            ):
                self.assertEqual(autorizacao.pode_gerenciar_usuarios_roles(), esperado)

    def test_revalidacao_imediata_falha_leitura_e_acao_negada_nao_escrevem(self):
        falha = leitura(pd.DataFrame(columns=ur.COLUNAS), ur.ARQUIVO, None, StatusLeitura.FALHA_TEMPORARIA)
        with patch.object(ur, "pode_gerenciar_usuarios_roles", return_value=False), patch.object(
            ur, "salvar_csv_github"
        ) as salvar:
            self.assertEqual(self.atribuir().codigo, "nao_autorizado")
            salvar.assert_not_called()
        with patch.object(ur, "pode_gerenciar_usuarios_roles", return_value=True), patch.object(
            ur, "salvar_csv_github"
        ) as salvar:
            self.assertEqual(self.atribuir(leitura=falha).codigo, "leitura_nao_confirmada")
            salvar.assert_not_called()
        with patch.object(ur, "pode_gerenciar_usuarios_roles", side_effect=(True, False)), patch.object(
            ur, "identificador_proprietario", return_value="owner"
        ), patch.object(ur, "salvar_csv_github") as salvar:
            self.assertEqual(self.atribuir().codigo, "nao_autorizado")
            salvar.assert_not_called()

    def test_associacao_nao_altera_acesso_auth_matrizes_ou_medicoes(self):
        esperados = {
            "services/auth.py": "b8f864ed3c9a892f53280e28ee56b78f5c979cee62d253923f88b55b477caec0",
            "services/permissoes.py": "f586e6897dcec87e65479bd6a13fd25da42cb4eb44f3dca7d3240c5865244746",
            "data/permissoes_usuarios.csv": "23b33a97d78c41f217e7bcdae397e5fcb555f72c344974adb3b1550cad2dca5e",
            "data/roles_permissoes.csv": "8ad445f518c3c72900aa32b7385c0d8350630af408dcded9218e8ad8813cdc7a",
            "pages/medicoes.py": "f23a8cf9d1c7e01f94a93447c1f924dbc2dfd80b1bb904a1a9ff3e64e496257f",
        }
        for caminho, esperado in esperados.items():
            self.assertEqual(hashlib.sha256((ROOT / caminho).read_bytes()).hexdigest(), esperado, caminho)
        for caminho in ("services/auth.py", "services/permissoes.py"):
            self.assertNotIn("usuarios_roles", (ROOT / caminho).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
