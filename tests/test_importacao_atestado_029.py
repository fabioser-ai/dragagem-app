import csv
import hashlib
import unittest
import uuid
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
ATESTADO_ID = "0d44afef-d290-44d4-8580-7ac262c8a58e"
PREFIXO_ATESTADOS_SHA256 = "efd552d9189e87acec29513ce9a4ac8d0c96c37dcbf5604e4682f1410aa55ae1"
PREFIXO_SERVICOS_SHA256 = "81e9c85b3abebb472ae2bdb5fec88a18a107ec76b3700d317a5f58f643007a33"

CODIGOS_ESPERADOS = [
    "020117", "020119", "020150U", "020406U", "030159", "040101",
    "040250", "050101", "050201", "050207", "050213", "050301",
    "050403", "050513", "050515", "065017", "065023U", "070169",
    "090107", "184213U", "200204", "200604", "210170U", "210231",
    "210235", "210404", "210405U", "210406U", "210407U", "210408U",
    "210410", "210411",
]

SEM_CODIGO_ESPERADOS = [
    ("ATERRO C/AREIA DE SAMARITA INCL. FORN. ESPALH. E COMPACT.", "M3", "120,00"),
    ("FORN. E COLOC. DE TAB. DE MADEIRA C/ARO DE METAL E REDE", "UN", "2,00"),
    ("FORN. E COLOC. DE REDE DE NYLON DE PROTECAO NAS QUADRAS", "M2", "264,00"),
    ("RECOMPOSICAO DOS PILARES DE APOIO DAS TAB. DAS QUADRAS", "UN", "2,00"),
    ("AGUAS PLUVIAIS MEDINDO 0,50X0,60X0,80 INCL. TAMPAS DE CONCR.", "UN", "3,00"),
]


def carregar_csv(nome):
    with (RAIZ / "data" / nome).open(encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def codigo_documental(servico):
    prefixo = "Código documental: "
    observacoes = servico["observacoes"]
    return observacoes[len(prefixo):] if observacoes.startswith(prefixo) else ""


class TestImportacaoAtestado029(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atestados = carregar_csv("atestados.csv")
        cls.servicos = carregar_csv("atestados_servicos.csv")
        cls.atestados_029 = [
            atestado for atestado in cls.atestados
            if atestado["id_atestado"] == ATESTADO_ID
        ]
        cls.servicos_029 = [
            servico for servico in cls.servicos
            if servico["id_atestado"] == ATESTADO_ID
        ]

    def test_um_atestado_da_prefeitura_e_metadados(self):
        self.assertEqual(len(self.atestados_029), 1)
        atestado = self.atestados_029[0]
        self.assertEqual(atestado["cliente"], "Prefeitura Municipal de Cubatão")
        self.assertEqual(atestado["contrato"], "027/2003")
        self.assertIn("Processo: 8981/02", atestado["observacoes"])
        self.assertEqual(
            atestado["obra"],
            "REFORMA DA QUADRA E PÁTIO DA EMEF BERNARDO J. M. LORENA",
        )

    def test_exatamente_37_servicos(self):
        self.assertEqual(len(self.servicos_029), 37)

    def test_32_codigos_unicos_e_5_servicos_sem_codigo(self):
        codigos = [codigo_documental(s) for s in self.servicos_029]
        com_codigo = [codigo for codigo in codigos if codigo]
        self.assertEqual(com_codigo, CODIGOS_ESPERADOS)
        self.assertEqual(len(com_codigo), 32)
        self.assertEqual(len(set(com_codigo)), 32)
        self.assertEqual(codigos[-5:], [""] * 5)

    def test_servicos_sem_codigo_permanecem_na_ordem_final(self):
        encontrados = [
            (s["servico"], s["unidade"], s["quantidade"])
            for s in self.servicos_029[-5:]
        ]
        self.assertEqual(encontrados, SEM_CODIGO_ESPERADOS)

    def test_quantidades_criticas(self):
        por_codigo = {codigo_documental(s): s for s in self.servicos_029 if codigo_documental(s)}
        esperados = {
            "020117": ("1,00", "M3"),
            "020119": ("179,15", "M3"),
            "020150U": ("2.208,71", "M2"),
            "040101": ("262,89", "M3"),
            "065017": ("2.834,96", "M2"),
            "065023U": ("625,25", "M2"),
            "210231": ("2.353,71", "M2"),
            "210410": ("1.200,00", "M2"),
            "210411": ("847,40", "M"),
        }
        for codigo, (quantidade, unidade) in esperados.items():
            with self.subTest(codigo=codigo):
                self.assertEqual(por_codigo[codigo]["quantidade"], quantidade)
                self.assertEqual(por_codigo[codigo]["unidade"], unidade)
        self.assertEqual(
            (self.servicos_029[-1]["quantidade"], self.servicos_029[-1]["unidade"]),
            ("3,00", "UN"),
        )

    def test_datas_ano_e_valor_permanecem_vazios(self):
        atestado = self.atestados_029[0]
        self.assertEqual(atestado["ano"], "")
        self.assertEqual(atestado["data_inicio"], "")
        self.assertEqual(atestado["data_fim"], "")
        self.assertNotIn("Valor", atestado["observacoes"])
        self.assertNotIn("Data de emissão", atestado["observacoes"])

    def test_importacoes_001_a_028_permanecem_inalteradas(self):
        verificacoes = [
            ("atestados.csv", PREFIXO_ATESTADOS_SHA256),
            ("atestados_servicos.csv", PREFIXO_SERVICOS_SHA256),
        ]
        for nome, digest_esperado in verificacoes:
            with self.subTest(arquivo=nome):
                linhas = (RAIZ / "data" / nome).read_bytes().splitlines(keepends=True)
                indice_029 = next(
                    indice for indice, linha in enumerate(linhas)
                    if ATESTADO_ID.encode() in linha
                )
                digest = hashlib.sha256(b"".join(linhas[:indice_029])).hexdigest()
                self.assertEqual(digest, digest_esperado)

    def test_uuids_unicos_e_relacionamentos_integros(self):
        ids_atestados = [a["id_atestado"] for a in self.atestados]
        ids_servicos = [s["id_servico"] for s in self.servicos]
        self.assertEqual(len(ids_atestados), len(set(ids_atestados)))
        self.assertEqual(len(ids_servicos), len(set(ids_servicos)))
        self.assertTrue({s["id_atestado"] for s in self.servicos}.issubset(set(ids_atestados)))
        for identificador in [ATESTADO_ID, *(s["id_servico"] for s in self.servicos_029)]:
            with self.subTest(identificador=identificador):
                self.assertEqual(str(uuid.UUID(identificador)), identificador)


if __name__ == "__main__":
    unittest.main()
