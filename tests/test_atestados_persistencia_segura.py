import unittest

from services.github import ResultadoLeituraCSV, StatusLeitura


class TestAtestadosPersistenciaSegura(unittest.TestCase):
    def resultado(self, status, sha=None):
        return ResultadoLeituraCSV(status=status, dados=None, arquivo="teste.csv", sha=sha)

    def test_leitura_confirmada_libera_escrita(self):
        resultado = self.resultado(StatusLeitura.SUCESSO_VAZIO, "sha")
        self.assertTrue(resultado.pode_sobrescrever)

    def test_arquivo_inexistente_permite_criacao(self):
        resultado = self.resultado(StatusLeitura.ARQUIVO_INEXISTENTE)
        self.assertTrue(resultado.leitura_confirmada)


if __name__ == "__main__":
    unittest.main()
