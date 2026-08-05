import csv
import hashlib
import unittest
import uuid
from collections import Counter
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
ATESTADO_ID = "d1877f47-9c3b-47e0-8f3a-e5cc5395e683"
PREFIXO_ATESTADOS_SHA256 = "60c49dc1c2775b3da8046a8a2c0eb6ae3624a4e7232e595f0486cc44e3e8f7b0"
PREFIXO_SERVICOS_SHA256 = "ad33b80f3c4fae2ce038180f0f5945181e8dc8aa3c166ec5b1e005dfe53bdec4"

ITENS_ESPERADOS = [
    "1.1", "1.2", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7",
    "2.8", "2.9", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7",
    "3.8", "4.1", "4.2",
]


def carregar_csv(nome):
    with (RAIZ / "data" / nome).open(encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def item_documental(servico):
    prefixo = "Item documental: "
    observacoes = servico["observacoes"]
    if not observacoes.startswith(prefixo):
        return None
    return observacoes[len(prefixo):].split(" | ", 1)[0]


class TestImportacaoAtestado028(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atestados = carregar_csv("atestados.csv")
        cls.servicos = carregar_csv("atestados_servicos.csv")
        cls.atestados_028 = [
            atestado for atestado in cls.atestados
            if atestado["cliente"] == "ULTRAFERTIL S/A"
            and atestado["contrato"] == "CPG 3233/06"
        ]
        cls.servicos_028 = [
            servico for servico in cls.servicos
            if servico["id_atestado"] == ATESTADO_ID
        ]

    def test_um_atestado_e_21_servicos(self):
        self.assertEqual(len(self.atestados_028), 1)
        self.assertEqual(self.atestados_028[0]["id_atestado"], ATESTADO_ID)
        self.assertEqual(len(self.servicos_028), 21)

    def test_itens_documentais_sao_unicos_e_preservam_ordem(self):
        itens = [item_documental(servico) for servico in self.servicos_028]
        self.assertEqual(itens, ITENS_ESPERADOS)
        self.assertEqual(Counter(itens), Counter(ITENS_ESPERADOS))

    def test_titulos_dos_grupos_nao_sao_servicos(self):
        titulos = {
            "SERVIÇOS PRELIMINARES",
            "Construção de Bases civis",
            "Construção de canaleta para escoamento pluvial (8,65m)",
            "Descarte de entulho",
        }
        self.assertTrue(titulos.isdisjoint({s["servico"] for s in self.servicos_028}))

    def test_descricoes_repetidas_permanecem_independentes(self):
        esperadas = {
            "Demolição de piso em concreto armado com utilização de martelete pneumático": 2,
            "Escavação manual de vala até 2,00m profundidade": 2,
            "Lastro de brita": 2,
            "Fôrma de madeira em tábuas e compensado plastificado": 2,
            "Armadura de aço CA-50": 2,
            "Fornecimento e aplicação de grout": 2,
            "Reaterro apiloado": 2,
            "Piso em concreto fck 18 Mpa": 2,
        }
        contagem = Counter(s["servico"] for s in self.servicos_028)
        for descricao, quantidade in esperadas.items():
            with self.subTest(descricao=descricao):
                self.assertEqual(contagem[descricao], quantidade)

    def test_quantitativos_criticos_e_unidades(self):
        por_item = {item_documental(s): s for s in self.servicos_028}
        esperados = {
            "2.1": ("4,50", "m³"),
            "2.5": ("210,00", "kg"),
            "2.7": ("136,00", "un"),
            "3.1": ("1,30", "m³"),
            "3.3": ("0,32", "m³"),
            "3.4": ("12,00", "m²"),
            "3.5": ("93,00", "kg"),
            "3.8": ("0,52", "m³"),
            "4.1": ("25,00", "m³"),
            "4.2": ("25,00", "m³"),
        }
        for item, (quantidade, unidade) in esperados.items():
            with self.subTest(item=item):
                self.assertEqual(por_item[item]["quantidade"], quantidade)
                self.assertEqual(por_item[item]["unidade"], unidade)

    def test_capitalizacao_documental_das_unidades(self):
        por_item = {item_documental(s): s for s in self.servicos_028}
        self.assertEqual(por_item["1.1"]["unidade"], "vb")
        self.assertEqual(por_item["1.2"]["unidade"], "Vb")

    def test_metadados_criticos_do_atestado(self):
        atestado = self.atestados_028[0]
        self.assertEqual(atestado["data_inicio"], "2006-09-26")
        self.assertEqual(atestado["data_fim"], "2006-10-11")
        self.assertIn("Valor do contrato: R$ 51.000,00", atestado["observacoes"])

    def test_importacoes_001_a_027_permanecem_inalteradas(self):
        verificacoes = [
            ("atestados.csv", PREFIXO_ATESTADOS_SHA256, ATESTADO_ID),
            ("atestados_servicos.csv", PREFIXO_SERVICOS_SHA256, ATESTADO_ID),
        ]
        for nome, digest_esperado, marcador in verificacoes:
            with self.subTest(arquivo=nome):
                linhas = (RAIZ / "data" / nome).read_bytes().splitlines(keepends=True)
                indice_028 = next(
                    indice for indice, linha in enumerate(linhas)
                    if marcador.encode() in linha
                )
                digest = hashlib.sha256(b"".join(linhas[:indice_028])).hexdigest()
                self.assertEqual(digest, digest_esperado)

    def test_uuids_unicos_e_relacionamentos_integros(self):
        ids_atestados = [a["id_atestado"] for a in self.atestados]
        ids_servicos = [s["id_servico"] for s in self.servicos]
        self.assertEqual(len(ids_atestados), len(set(ids_atestados)))
        self.assertEqual(len(ids_servicos), len(set(ids_servicos)))
        self.assertTrue({s["id_atestado"] for s in self.servicos}.issubset(set(ids_atestados)))
        for identificador in [ATESTADO_ID, *(s["id_servico"] for s in self.servicos_028)]:
            with self.subTest(identificador=identificador):
                self.assertEqual(str(uuid.UUID(identificador)), identificador)


if __name__ == "__main__":
    unittest.main()
