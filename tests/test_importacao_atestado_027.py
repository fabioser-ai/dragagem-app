import csv
import hashlib
import unittest
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
ATESTADO_ID = "b4a3eef1-968c-46bb-83ac-e023f98da188"
PREFIXO_ATESTADOS_SHA256 = "e19176e6c59ae913a52bcf6763b40b1d03635eb9ddec04e16d2d94b268e611d4"
PREFIXO_SERVICOS_SHA256 = "862067e08d37030271187c1ed9707564607d5651868e1e866e0b80573bb481d3"

CODIGOS_ESPERADOS = [
    "02.01.01", "02.01.10", "02.01.15", "02.01.25", "02.02.52",
    "02.02.95", "02.03.01", "02.04.02", "02.05.14", "02.05.18",
    "03.03.98", "03.50.01", "04.01.31", "04.01.45", "04.50.01",
    "05.80.01", "05.80.21", "05.80.71", "05.80.81", "06.60.01",
    "07.03.90", "07.04.07", "07.70.55", "09.05.02", "09.05.03",
    "09.05.70", "09.05.73", "09.06.37", "09.07.04", "09.08.77",
    "09.11.73", "09.13.15", "09.13.18", "09.13.27", "09.13.34",
    "09.64.21", "12.01.01", "12.01.05", "12.02.07", "12.50.02",
    "13.50.01", "13.50.02", "15.04.01", "16.01.16", "16.02.07",
    "16.02.71", "16.06.60", "16.18.01", "16.50.01", "16.50.02",
    "16.80.98",
]

UUIDS_INCORRETOS = set("""
f8c8a73c-7785-44c8-9529-107feb57d007
99d0349a-70df-4aec-afb4-7aa0feb3c65b
d370ef0f-569e-4b93-b13e-5465b8daf2a6
43973d03-3415-4bee-a92d-c0889adf1408
fdfea25b-c40c-46f6-9f3f-be3280fdb24f
ff3282be-d038-4989-8317-473ca966fe51
2daa0c4a-16de-455b-99ce-4ec150d79519
77e9d532-4d51-4a9a-9f7b-84f8c8d0be91
7fea8c09-9c91-4fb8-8d98-b377810412fe
1749629b-381e-4b76-9b00-d8b8420b2c92
bc91fa75-ab30-4fca-a1e3-af4ec26c348b
dbc43c04-72ef-448b-ae11-9dc4888832c6
ecc4b65c-f78d-4efa-8137-a5af9b6238d9
05984f6d-7a91-4cbe-a00c-5f0e9efcd86f
0abbda95-e10f-43c2-bf0c-d8e870667ca6
92a65d34-251a-4437-b7dd-76b3a05425ac
d9574125-b624-40c1-831b-6861763185c9
8c872317-f591-4181-9889-298b3b989a1e
07157b69-75d9-4002-9904-ae66430f000e
ee727ca0-e28b-441d-ad43-10169327de55
6b07cbd6-1a58-47bc-a347-30e198968592
b6dcb3e7-ee31-4969-aef8-97f679d6edea
1f99eb92-3ef5-402e-b280-6cef978c8dc0
e3168271-0bbd-483d-ac8e-8dece0ae009c
7fd2f583-fd76-4ffa-8df3-e53d02ed44fe
b8924b0f-63c4-43f5-995c-1fe2bcd4d1e9
9238482c-f98d-410b-818f-75e20342e9d0
abd47520-9a45-4cb2-a666-e856d916f847
fc564198-07eb-439c-9ec2-b59d8dfb3127
fe872faa-9215-4a7a-9701-090305ed146c
f7bded43-98f3-475e-b374-8e86ee4a3ca0
70b5af78-3682-4236-96d7-acfaf23edcd6
30175e92-1ef7-47df-b713-dd45398091df
09989b3c-9a6f-4e48-ba6e-80429b6850fb
63b9174c-805e-43ef-b959-bfe355edf52d
ed32951e-01b8-42eb-8d40-1df64d7a7b7d
a6bf7b12-7693-45cd-bfc5-f40726cf40b8
fa891bd9-4530-4e6f-827b-323b2306047c
b4318e63-a741-4ed5-8c17-dc1af782cd36
61ba078a-1e8a-45ed-b963-24bc7424c112
149d08c0-805c-47ea-b27a-3d6b6ba546dc
f5757a35-cc3e-4597-9c74-a4f6c61359db
d95b5135-01bb-474f-b25d-a5563bc1d309
03382492-5a48-4555-9d28-5181fca30de4
5f885185-9cf8-4a92-afa2-430b1120fd50
f388c085-0b48-4ca5-a1c8-b512611caa54
e03722e3-8700-4102-bbae-fb8e5b80d7f0
e310f17d-4ad0-49d5-bbf4-92882154d1a9
""".split())


def carregar_csv(nome):
    with (RAIZ / "data" / nome).open(encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def codigo_documental(servico):
    prefixo = "Código documental: "
    observacoes = servico["observacoes"]
    if not observacoes.startswith(prefixo):
        return None
    return observacoes[len(prefixo):]


class TestImportacaoAtestado027(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atestados = carregar_csv("atestados.csv")
        cls.servicos = carregar_csv("atestados_servicos.csv")
        cls.servicos_027 = [
            servico for servico in cls.servicos
            if servico["id_atestado"] == ATESTADO_ID
        ]

    def test_atestado_e_51_servicos_existem_uma_unica_vez(self):
        registros = [
            atestado for atestado in self.atestados
            if atestado["id_atestado"] == ATESTADO_ID
        ]
        self.assertEqual(len(registros), 1)
        self.assertEqual(len(self.servicos_027), 51)

    def test_codigos_documentais_sao_unicos_e_preservam_ordem(self):
        codigos = [codigo_documental(servico) for servico in self.servicos_027]
        self.assertEqual(codigos, CODIGOS_ESPERADOS)
        self.assertEqual(len(set(codigos)), 51)

    def test_tres_quantidades_zeradas_permanecem_textuais(self):
        por_codigo = {
            codigo_documental(servico): servico
            for servico in self.servicos_027
        }
        zerados = {"02.05.14", "16.01.16", "16.18.01"}
        self.assertEqual(
            {codigo for codigo, servico in por_codigo.items() if servico["quantidade"] == "0,00"},
            zerados,
        )

    def test_amostras_criticas_preservam_quantidade_e_unidade(self):
        por_codigo = {
            codigo_documental(servico): servico
            for servico in self.servicos_027
        }
        esperados = {
            "02.01.01": ("98,93", "M3"),
            "02.03.01": ("117,10", "M2"),
            "02.04.02": ("1.478,40", "KG"),
            "02.05.18": ("14,77", "M3"),
            "04.01.31": ("63,96", "M2"),
            "07.03.90": ("545,29", "M2"),
            "12.01.01": ("133,15", "M2"),
            "13.50.01": ("28,72", "M3"),
            "15.04.01": ("213,36", "M2"),
            "16.80.98": ("145,11", "M3"),
        }
        for codigo, (quantidade, unidade) in esperados.items():
            with self.subTest(codigo=codigo):
                self.assertEqual(por_codigo[codigo]["quantidade"], quantidade)
                self.assertEqual(por_codigo[codigo]["unidade"], unidade)

    def test_importacoes_001_a_026_permanecem_inalteradas(self):
        verificacoes = [
            ("atestados.csv", PREFIXO_ATESTADOS_SHA256),
            ("atestados_servicos.csv", PREFIXO_SERVICOS_SHA256),
        ]
        for nome, digest_esperado in verificacoes:
            with self.subTest(arquivo=nome):
                linhas = (RAIZ / "data" / nome).read_bytes().splitlines(keepends=True)
                indice_027 = next(
                    indice for indice, linha in enumerate(linhas)
                    if ATESTADO_ID.encode() in linha
                )
                digest = hashlib.sha256(b"".join(linhas[:indice_027])).hexdigest()
                self.assertEqual(digest, digest_esperado)

    def test_uuid_incorreto_nao_permanece_vinculado(self):
        ids_atuais = {servico["id_servico"] for servico in self.servicos_027}
        self.assertTrue(ids_atuais.isdisjoint(UUIDS_INCORRETOS))


if __name__ == "__main__":
    unittest.main()
