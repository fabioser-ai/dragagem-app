import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from services import autorizacao, rbac_authority as rbac
from tests.test_authz001_rbac_authority import fontes


ROOT = Path(__file__).resolve().parents[1]


class TestSnapshotRBACPorExecucao(unittest.TestCase):
    def setUp(self):
        self.estado = patch.object(rbac.st, "session_state", {}, create=True)
        self.estado.start()
        rbac.st.secrets = {"GITHUB_TOKEN": "token", "REPO": "org/repo"}

    def tearDown(self):
        self.estado.stop()

    def _leituras(self, snapshots):
        chamadas = []

        def ler(arquivo, _token, _repo):
            indice_execucao = len(chamadas) // len(rbac.ARQUIVOS)
            chamadas.append(arquivo)
            nome = next(nome for nome, caminho in rbac.ARQUIVOS.items() if caminho == arquivo)
            return Mock(leitura_confirmada=True, dados=snapshots[indice_execucao][nome])

        return chamadas, ler

    def test_multiplas_avaliacoes_reutilizam_um_snapshot(self):
        chamadas, ler = self._leituras([fontes()])
        with patch.object(rbac, "ler_csv_github", side_effect=ler):
            rbac.iniciar_execucao()
            for modulo in ("medicoes", "crm", "dados", "ferias"):
                rbac.avaliar_modulo(usuario="teste", modulo=modulo)

        self.assertEqual(chamadas, list(rbac.ARQUIVOS.values()))

    def test_role_removida_e_adicionada_valem_na_execucao_seguinte(self):
        sem_role = fontes(associacoes=[])
        sem_role["associacoes"] = sem_role["associacoes"].reindex(
            columns=["usuario_id", "role_id", "obra_id", "ativo"]
        )
        chamadas, ler = self._leituras([fontes(), sem_role, fontes()])
        with patch.object(rbac, "ler_csv_github", side_effect=ler):
            rbac.iniciar_execucao()
            self.assertTrue(rbac.avaliar_modulo(usuario="teste", modulo="medicoes").permitido)

            rbac.iniciar_execucao()
            self.assertFalse(rbac.avaliar_modulo(usuario="teste", modulo="medicoes").permitido)

            rbac.iniciar_execucao()
            self.assertTrue(rbac.avaliar_modulo(usuario="teste", modulo="medicoes").permitido)

        self.assertEqual(len(chamadas), 3 * len(rbac.ARQUIVOS))

    def test_alteracao_de_escopo_e_deny_nao_ficam_obsoletos(self):
        obra_a = fontes(associacoes=[
            {"usuario_id": "u1", "role_id": "r1", "obra_id": "obra-a", "ativo": "sim"}
        ])
        negado = fontes(matriz=[
            {"role_id": "r1", "modulo": "medicoes", "recurso": "lancamento", "acao": "criar", "efeito": "deny"}
        ])
        chamadas, ler = self._leituras([fontes(), obra_a, negado])
        with patch.object(rbac, "ler_csv_github", side_effect=ler):
            rbac.iniciar_execucao()
            self.assertTrue(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", obra_id="obra-b").permitido)

            rbac.iniciar_execucao()
            self.assertFalse(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", obra_id="obra-b").permitido)

            rbac.iniciar_execucao()
            self.assertFalse(rbac.avaliar(usuario="teste", modulo="medicoes", recurso="lancamento", acao="criar", obra_id="obra-a").permitido)

        self.assertEqual(len(chamadas), 3 * len(rbac.ARQUIVOS))

    def test_falha_e_memorizada_na_execucao_e_retentada_na_proxima(self):
        falha = Mock(leitura_confirmada=False)
        sucesso = [Mock(leitura_confirmada=True, dados=df) for df in fontes().values()]
        with patch.object(rbac, "ler_csv_github", side_effect=[falha, *sucesso]) as ler:
            rbac.iniciar_execucao()
            self.assertFalse(rbac.avaliar_modulo(usuario="teste", modulo="medicoes").permitido)
            self.assertFalse(rbac.avaliar_modulo(usuario="teste", modulo="medicoes").permitido)
            self.assertEqual(ler.call_count, 1)

            rbac.iniciar_execucao()
            self.assertTrue(rbac.avaliar_modulo(usuario="teste", modulo="medicoes").permitido)
            self.assertEqual(ler.call_count, 1 + len(rbac.ARQUIVOS))

    def test_owner_bypass_e_modos_permanecem_inalterados(self):
        autorizacao.st.session_state.clear()
        autorizacao.st.session_state.update(autenticado=True, usuario="fabio", perfil="superadmin")
        autorizacao.st.secrets = {"SYSTEM_OWNER_ID": "fabio", "AUTHORIZATION_MODE": "RBAC"}
        with patch.object(rbac, "avaliar_modulo") as avaliar:
            self.assertTrue(autorizacao.pode_acessar("crm"))
            avaliar.assert_not_called()

        autorizacao.st.session_state["usuario"] = "teste"
        autorizacao.st.secrets = {"AUTHORIZATION_MODE": "LEGACY"}
        with patch.object(autorizacao, "pode_acessar_modulo", return_value=True), patch.object(rbac, "avaliar_modulo") as avaliar:
            self.assertTrue(autorizacao.pode_acessar("crm"))
            avaliar.assert_not_called()

    def test_app_inicia_snapshot_antes_da_primeira_decisao(self):
        fonte = (ROOT / "app.py").read_text(encoding="utf-8")
        self.assertLess(
            fonte.index("iniciar_execucao_autorizacao()"),
            fonte.index("if not pode_acessar_rota(tela):"),
        )


if __name__ == "__main__":
    unittest.main()
