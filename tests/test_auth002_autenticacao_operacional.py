import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import pandas as pd

from services import auth
from services import credenciais_operacionais as cred
from services.github import ResultadoLeituraCSV, StatusLeitura
from services.persistencia_multi_arquivo import SnapshotBranch


ROOT = Path(__file__).resolve().parents[1]


def leitura(arquivo, dados, status=StatusLeitura.SUCESSO_COM_DADOS, sha="sha"):
    return ResultadoLeituraCSV(status, dados, arquivo, sha=sha)


USUARIO = {
    "usuario_id": "u-1", "login": "operador", "nome": "Operador",
    "matricula": "M-1", "email": "o@example.com", "perfil_base": "funcionario",
    "ativo": "sim", "criado_em": "", "criado_por": "", "atualizado_em": "",
    "atualizado_por": "", "exige_troca_senha": "nao",
    "credencial_configurada": "sim",
}


class TestCredenciaisAUTH002(unittest.TestCase):
    def setUp(self):
        self._secrets_original = cred.st.secrets
        self._session_original = cred.st.session_state
        cred.st.secrets = {
            "APP_USERS": '{"fabio":{"password":"legada"}}',
            "GITHUB_TOKEN": "token", "REPO": "org/repo", "GITHUB_BRANCH": "main",
        }
        cred.st.session_state = {"autenticado": True, "usuario": "fabio"}
        self.hash = cred.gerar_hash("segredo")
        self.usuarios = cred._df_usuarios(pd.DataFrame([USUARIO]))
        self.credenciais = cred._df(pd.DataFrame([{
            "usuario_id": "u-1", "password_hash": self.hash,
            "algoritmo": "bcrypt", "configurada_em": "antes",
            "configurada_por": "fabio", "atualizada_em": "antes",
            "atualizada_por": "fabio",
        }]))

    def tearDown(self):
        cred.st.secrets = self._secrets_original
        cred.st.session_state = self._session_original

    def autenticar(self, **mudancas):
        usuario = dict(USUARIO)
        usuario.update(mudancas.pop("usuario", {}))
        usuarios = leitura(cred.ARQUIVO_USUARIOS, cred._df_usuarios(pd.DataFrame([usuario])))
        creds = leitura(cred.ARQUIVO, mudancas.pop("credenciais", self.credenciais))
        with patch.object(cred, "ler_csv_github", return_value=usuarios), patch.object(
            cred, "carregar_credenciais_resultado", return_value=creds
        ):
            return cred.autenticar_usuario_operacional(
                login=mudancas.pop("login", "operador"),
                senha=mudancas.pop("senha", "segredo"),
                usuarios_protegidos=mudancas.pop("protegidos", {"fabio": {}}),
            )

    def test_bcrypt_hash_e_verificacao_sem_senha_recuperavel(self):
        self.assertTrue(self.hash.startswith("$2"))
        self.assertNotIn("segredo", self.hash)
        self.assertTrue(cred.verificar_hash("segredo", self.hash))
        self.assertFalse(cred.verificar_hash("errada", self.hash))

    def diagnosticar(self, *, usuario=None, dados=None, status=StatusLeitura.SUCESSO_COM_DADOS):
        identidade = dict(USUARIO)
        identidade.update(usuario or {})
        base = self.credenciais if dados is None else dados
        resultado = leitura(cred.ARQUIVO, base, status)
        return cred.diagnosticar_credencial(identidade, resultado)

    def test_diagnostico_marcador_sim_e_credencial_valida_disponivel(self):
        resultado = self.diagnosticar()
        self.assertTrue(resultado.disponivel)
        self.assertEqual(resultado.codigo, "disponivel")

    def test_diagnostico_marcador_sim_e_credencial_ausente_inconsistente(self):
        resultado = self.diagnosticar(dados=cred._df())
        self.assertFalse(resultado.disponivel)
        self.assertEqual(resultado.codigo, "registro_inconsistente")

    def test_diagnostico_falha_de_leitura_nao_afirma_disponibilidade(self):
        resultado = self.diagnosticar(status=StatusLeitura.FALHA_TEMPORARIA)
        self.assertFalse(resultado.disponivel)
        self.assertEqual(resultado.codigo, "leitura_nao_confirmada")

    def test_diagnostico_credencial_duplicada_inconsistente(self):
        duplicada = pd.concat([self.credenciais, self.credenciais], ignore_index=True)
        resultado = self.diagnosticar(dados=duplicada)
        self.assertFalse(resultado.disponivel)
        self.assertEqual(resultado.codigo, "registro_inconsistente")

    def test_diagnostico_hash_corrompido_inconsistente(self):
        corrompida = self.credenciais.copy()
        corrompida.at[0, "password_hash"] = "hash-corrompido"
        resultado = self.diagnosticar(dados=corrompida)
        self.assertFalse(resultado.disponivel)
        self.assertEqual(resultado.codigo, "hash_invalido")

    def test_diagnostico_marcador_nao_ignora_registro_residual(self):
        resultado = self.diagnosticar(usuario={"credencial_configurada": "nao"})
        self.assertFalse(resultado.disponivel)
        self.assertEqual(resultado.codigo, "nao_configurada")

    def test_login_operacional_constroi_dados_da_sessao(self):
        self.assertEqual(self.autenticar(), {
            "usuario": "operador", "perfil": "funcionario",
            "matricula": "M-1", "nome": "Operador",
        })

    def test_senha_incorreta_usuario_inexistente_inativo_e_sem_marcador_negam(self):
        self.assertIsNone(self.autenticar(senha="errada"))
        self.assertIsNone(self.autenticar(login="ausente"))
        self.assertIsNone(self.autenticar(usuario={"ativo": "nao"}))
        self.assertIsNone(self.autenticar(usuario={"credencial_configurada": "nao"}))

    def test_credencial_ausente_duplicada_corrompida_ou_algoritmo_invalido_nega(self):
        self.assertIsNone(self.autenticar(credenciais=cred._df()))
        duplicada = pd.concat([self.credenciais, self.credenciais], ignore_index=True)
        self.assertIsNone(self.autenticar(credenciais=duplicada))
        corrompida = self.credenciais.copy()
        corrompida.at[0, "password_hash"] = "sha256:inseguro"
        self.assertIsNone(self.autenticar(credenciais=corrompida))
        corrompida.at[0, "algoritmo"] = "sha256"
        self.assertIsNone(self.autenticar(credenciais=corrompida))

    def test_falhas_de_leitura_negam(self):
        falha = leitura(cred.ARQUIVO_USUARIOS, pd.DataFrame(), StatusLeitura.FALHA_TEMPORARIA)
        with patch.object(cred, "ler_csv_github", return_value=falha):
            self.assertIsNone(cred.autenticar_usuario_operacional(
                login="operador", senha="segredo", usuarios_protegidos={}
            ))

    def test_colisao_protegida_e_perfil_administrativo_negam(self):
        self.assertIsNone(self.autenticar(protegidos={" OPERADOR ": {}}))
        self.assertIsNone(self.autenticar(usuario={"perfil_base": "superadmin"}))

    def test_configuracao_nao_autorizada_nao_publica(self):
        with patch.object(cred, "pode_gerenciar_usuarios_operacionais", return_value=False), patch.object(
            cred, "publicar_arquivos_em_commit"
        ) as publicar:
            resultado = cred.configurar_credencial(usuario_id="u-1", senha="nova")
        self.assertEqual(resultado.codigo, "nao_autorizado")
        publicar.assert_not_called()

    def test_configuracao_publica_identidade_e_credencial_atomicamente_com_snapshot(self):
        vazio = leitura(cred.ARQUIVO, cred._df(), StatusLeitura.ARQUIVO_INEXISTENTE, sha=None)
        usuarios = leitura(cred.ARQUIVO_USUARIOS, self.usuarios)
        escrita = Mock(sucesso=True)
        with patch.object(cred, "pode_gerenciar_usuarios_operacionais", return_value=True), patch.object(
            cred, "resolver_snapshot_branch", return_value=SnapshotBranch("main", "commit-1", "tree-1")
        ), patch.object(cred, "ler_csv_github", return_value=usuarios) as ler, patch.object(
            cred, "carregar_credenciais_resultado", return_value=vazio
        ), patch.object(cred, "publicar_arquivos_em_commit", return_value=escrita) as publicar:
            resultado = cred.configurar_credencial(usuario_id="u-1", senha="nova")
        self.assertTrue(resultado.sucesso)
        self.assertEqual(ler.call_args.kwargs["ref"], "commit-1")
        self.assertEqual(publicar.call_args.kwargs["snapshot_esperado"], "commit-1")
        alteracoes = publicar.call_args.args[0]
        self.assertEqual({a.arquivo for a in alteracoes}, {cred.ARQUIVO, cred.ARQUIVO_USUARIOS})
        identidade_csv = next(a.conteudo for a in alteracoes if a.arquivo == cred.ARQUIVO_USUARIOS).decode()
        credencial_csv = next(a.conteudo for a in alteracoes if a.arquivo == cred.ARQUIVO).decode()
        self.assertIn(",sim\n", identidade_csv)
        self.assertNotIn("nova", credencial_csv)
        self.assertIn("$2", credencial_csv)

    def test_falha_ou_conflito_nao_declara_sucesso(self):
        usuarios = leitura(cred.ARQUIVO_USUARIOS, self.usuarios)
        escrita = Mock(sucesso=False)
        with patch.object(cred, "pode_gerenciar_usuarios_operacionais", return_value=True), patch.object(
            cred, "resolver_snapshot_branch", return_value=SnapshotBranch("main", "commit-1", "tree-1")
        ), patch.object(cred, "ler_csv_github", return_value=usuarios), patch.object(
            cred, "carregar_credenciais_resultado", return_value=leitura(cred.ARQUIVO, self.credenciais)
        ), patch.object(cred, "publicar_arquivos_em_commit", return_value=escrita):
            resultado = cred.configurar_credencial(usuario_id="u-1", senha="nova")
        self.assertFalse(resultado.sucesso)
        self.assertEqual(resultado.codigo, "falha_persistencia")


class TestIntegracaoAuthAUTH002(unittest.TestCase):
    def test_conta_protegida_preserva_caminho_legado_e_precedencia(self):
        fonte = (ROOT / "services/auth.py").read_text(encoding="utf-8")
        self.assertIn('senha == usuarios[usuario].get("password")', fonte)
        self.assertLess(fonte.index('usuario in usuarios'), fonte.index('_autenticar_operacional(usuario, senha, usuarios)'))

    def test_sessao_operacional_preserva_contrato(self):
        estado = {}
        with patch.object(auth.st, "session_state", estado), patch.object(auth.time, "time", return_value=123):
            auth._abrir_sessao(usuario="operador", perfil="user", matricula="M", nome="Nome")
        for chave in ("autenticado", "usuario", "perfil", "matricula", "nome", "ultimo_acesso", "tela"):
            self.assertIn(chave, estado)
        self.assertEqual(estado["tela"], "menu")

    def test_logout_timeout_e_shadow_permanecem_isolados(self):
        fonte_auth = (ROOT / "services/auth.py").read_text(encoding="utf-8")
        fonte_autorizacao = (ROOT / "services/autorizacao.py").read_text(encoding="utf-8")
        self.assertIn("def logout", fonte_auth)
        self.assertIn("SESSION_TIMEOUT_SECONDS", fonte_auth)
        self.assertNotIn("rbac_shadow", fonte_auth)
        self.assertNotIn("rbac_shadow", fonte_autorizacao)


if __name__ == "__main__":
    unittest.main()
