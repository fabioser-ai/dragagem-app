import importlib
import json
import math
import sys
import types
import unittest
from contextlib import nullcontext
from dataclasses import asdict, replace
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.carga_transporte import salvar_carga_transporte
from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.dominio.carga_transporte import (
    FORMULAS_CARGA_TRANSPORTE,
    INDICE_WORKSHEET_CARGA_TRANSPORTE,
    WORKSHEET_ORIGEM_CARGA_TRANSPORTE,
    CargaTransporte,
    ItemCargaTransporte,
    LinhaMaoObraCargaTransporte,
    calcular_carga_transporte,
)
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.persistencia.contratos import (
    ResultadoPersistencia,
    StatusPersistencia,
)
from modulos.orcamentos.persistencia.serializacao import (
    desserializar_versao,
    serializar_versao,
)


WORKSHEETS_NA_ORDEM_REAL = (
    "Dados Obra ",
    "Cotaçoes",
    "Produção",
    "Barrilete",
    "1. Mob. Draga",
    "2. Mob. Eq. Polimero",
    "Canteiro",
    "3. Prep. Célula",
    "4. Forn. Bag",
    "5. Operação Sistema",
    "6. Dragagem",
    "7. Medição",
    "8. Carga e Transporte",
    "8. Desmob. Draga",
    "9. Desmob. Eq. Polimero ",
    "10. Plan. Preços",
    "Planilha1",
)


class ColunaFalsa:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class StreamlitCargaTransporteFalso:
    def __init__(self, *, salvar=False, valores=None, session_state=None):
        self.salvar = salvar
        self.valores = valores or {}
        self.session_state = session_state if session_state is not None else {}
        self.formularios = []
        self.campos = []
        self.metricas = []
        self.erros = []
        self.reruns = 0

    def form(self, chave):
        self.formularios.append(chave)
        return nullcontext()

    def form_submit_button(self, texto):
        return self.salvar and texto == "Salvar Carga e Transporte"

    def subheader(self, texto):
        pass

    def markdown(self, texto):
        pass

    def success(self, texto):
        pass

    def error(self, texto):
        self.erros.append(texto)

    def columns(self, n):
        return tuple(ColunaFalsa() for _ in range(n))

    def number_input(self, rotulo, **kwargs):
        chave = kwargs["key"]
        self.campos.append((rotulo, chave, kwargs.get("value")))
        return self.valores.get(chave, kwargs.get("value"))

    def metric(self, rotulo, valor, **kwargs):
        self.metricas.append((rotulo, valor))

    def rerun(self):
        self.reruns += 1


class TestDescobertaCargaTransporte(unittest.TestCase):
    def test_primeira_worksheet_funcional_pendente_foi_identificada(self):
        implementadas = set(WORKSHEETS_NA_ORDEM_REAL[:12]) | {
            "8. Desmob. Draga",
            "9. Desmob. Eq. Polimero ",
        }
        primeira_pendente = next(
            (indice, nome)
            for indice, nome in enumerate(WORKSHEETS_NA_ORDEM_REAL)
            if nome not in implementadas
        )
        self.assertEqual(
            primeira_pendente,
            (
                INDICE_WORKSHEET_CARGA_TRANSPORTE,
                WORKSHEET_ORIGEM_CARGA_TRANSPORTE,
            ),
        )
        self.assertEqual(primeira_pendente, (12, "8. Carga e Transporte"))


class TestCalculosCargaTransporte(unittest.TestCase):
    def calcular(self, carga_transporte=None):
        return calcular_carga_transporte(carga_transporte or CargaTransporte())

    def test_fotografia_inicial_preserva_estrutura_e_numeracao(self):
        carga = CargaTransporte()
        self.assertEqual(len(carga.equipe), 3)
        self.assertEqual(len(carga.itens), 3)
        self.assertEqual([item.numero for item in carga.itens], [1, 3, 4])
        self.assertIsNone(carga.equipe[0].quantidade)
        self.assertEqual(carga.equipe[1].custo_hora, 15.1)
        self.assertEqual(carga.equipe[2].quantidade, 5)
        self.assertEqual(carga.itens[0].descricao, "Carga e Transporte (6KM)")
        self.assertEqual(carga.itens[2].descricao, "Acompanhamento  FOS")
        self.assertIsNone(carga.bdi_principal)
        self.assertEqual(carga.bdi_secundario, 0)

    def test_lista_completa_das_dezoito_formulas(self):
        self.assertEqual(
            FORMULAS_CARGA_TRANSPORTE,
            (
                ("F5", "=(A5*C5*D5)+(A5*C5*D5)*(E5/100)"),
                ("D6", "=D5"),
                ("F6", "=(A6*C6*D6)+(A6*C6*D6)*(E6/100)"),
                ("F7", "=(A7*C7*D7)+(A7*C7*D7)*(E7/100)"),
                ("A8", "=A5+A7+A6"),
                ("F8", "=A8*C8"),
                ("A9", "=A8"),
                ("F9", "=A9*C9"),
                ("F10", "=SUM(F5:F9)"),
                ("F15", "=D15*E15"),
                ("F16", "=D16*E16"),
                ("E17", "=F10"),
                ("F17", "=D17*E17"),
                ("F18", "=SUM(F15:F17)"),
                ("F19", "=F18*(E19/100)"),
                ("F20", "=SUM(F18:F19)"),
                ("F22", "=F21*(E22/100)"),
                ("F23", "=SUM(F21:F22)"),
            ),
        )

    def test_mao_de_obra_referencia_interna_e_custo_diario(self):
        resultado = self.calcular()
        self.assertEqual([item.horas_dia for item in resultado.mao_obra], [9, 9, 9])
        self.assertEqual(resultado.mao_obra[0].total, 0)
        self.assertAlmostEqual(resultado.mao_obra[1].total, 570.78)
        self.assertAlmostEqual(resultado.mao_obra[2].total, 756)
        self.assertEqual(resultado.quantidade_pessoas, 7)
        self.assertEqual(resultado.total_refeicoes, 210)
        self.assertEqual(resultado.total_transportes, 70)
        self.assertAlmostEqual(resultado.custo_por_dia, 1606.78)

    def test_itens_vazios_resultam_zero_sem_criar_integracoes(self):
        resultado = self.calcular()
        self.assertEqual(resultado.itens[0].preco_unitario, 32)
        self.assertIsNone(resultado.itens[1].preco_unitario)
        self.assertAlmostEqual(resultado.itens[2].preco_unitario, 1606.78)
        self.assertEqual([item.preco_total for item in resultado.itens], [0, 0, 0])
        self.assertEqual(resultado.total, 0)

    def test_quantidades_manuais_acionam_somente_formulas_existentes(self):
        base = CargaTransporte()
        alterada = replace(
            base,
            itens=(
                replace(base.itens[0], quantidade=10),
                replace(base.itens[1], quantidade=2, preco_unitario_manual=100),
                replace(base.itens[2], quantidade=3),
            ),
        )
        resultado = self.calcular(alterada)
        self.assertEqual(resultado.itens[0].preco_total, 320)
        self.assertEqual(resultado.itens[1].preco_total, 200)
        self.assertAlmostEqual(resultado.itens[2].preco_total, 4820.34)
        self.assertAlmostEqual(resultado.total, 5340.34)

    def test_bdi_principal_vazio_e_bloco_secundario_zero(self):
        resultado = self.calcular()
        self.assertEqual(resultado.valor_bdi_principal, 0)
        self.assertEqual(resultado.preco_final, 0)
        self.assertEqual(resultado.valor_bdi_secundario, 0)
        self.assertEqual(resultado.preco_final_secundario, 0)
        com_bdi = self.calcular(
            replace(
                CargaTransporte(),
                itens=tuple(
                    replace(item, quantidade=1)
                    if item.id == "carga-transporte-6km"
                    else item
                    for item in CargaTransporte().itens
                ),
                bdi_principal=10,
                bdi_secundario=10,
            )
        )
        self.assertEqual(com_bdi.valor_bdi_principal, 3.2)
        self.assertEqual(com_bdi.preco_final, 35.2)
        self.assertEqual(com_bdi.preco_final_secundario, 0)

    def test_nao_existem_referencias_externas(self):
        self.assertFalse(
            any("!" in formula for _, formula in FORMULAS_CARGA_TRANSPORTE)
        )

    def test_decimais_e_vazios_permanecem_seguros(self):
        base = CargaTransporte()
        vazio = CargaTransporte(
            tuple(
                replace(
                    item,
                    quantidade=None,
                    custo_hora=None,
                    encargos_sociais=None,
                )
                for item in base.equipe
            ),
            None,
            None,
            tuple(
                replace(
                    item,
                    quantidade=None,
                    preco_unitario_manual=None,
                    preco_unitario_custo_diario=False,
                )
                for item in base.itens
            ),
            None,
            None,
        )
        resultado = self.calcular(vazio)
        self.assertEqual(
            (
                resultado.custo_por_dia,
                resultado.total,
                resultado.preco_final,
                resultado.preco_final_secundario,
            ),
            (0, 0, 0, 0),
        )
        self.assertTrue(
            all(math.isfinite(item.preco_total) for item in resultado.itens)
        )

    def test_invalidos_e_origens_duplicadas_sao_rejeitados(self):
        for valor in (-1, math.nan, math.inf):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                CargaTransporte(custo_refeicao=valor)
        with self.assertRaises(ValueError):
            replace(
                CargaTransporte().itens[2],
                preco_unitario_manual=1,
            )
        with self.assertRaises(ValueError):
            LinhaMaoObraCargaTransporte("x", "X", 1, 1, 8, "outra", 1)

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(
            salvar_carga_transporte(versao, CargaTransporte()).sucesso
        )


class TestPersistenciaCargaTransporte(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_preserva_medicao(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        medicao = asdict(versao.medicao_orcamento)
        alterada = replace(
            CargaTransporte(),
            custo_refeicao=35.75,
            bdi_principal=2.5,
        )
        versao.registrar_carga_transporte(alterada)
        carregada = desserializar_versao(
            serializar_versao(orcamento, versao)
        ).valor[1]
        self.assertEqual(asdict(carregada.carga_transporte), asdict(alterada))
        self.assertEqual(asdict(carregada.medicao_orcamento), medicao)

    def test_serializacao_persiste_somente_entradas(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = json.loads(serializar_versao(orcamento, versao))["versao"][
            "carga_transporte"
        ]
        for nome in (
            "custo_por_dia",
            "total",
            "valor_bdi_principal",
            "preco_final",
            "valor_bdi_secundario",
            "preco_final_secundario",
        ):
            self.assertNotIn(nome, dados)

    def test_schema_18_sem_nova_aba_continua_legivel(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 18
        documento["versao"].pop("carga_transporte")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(
            asdict(resultado.valor[1].carga_transporte),
            asdict(CargaTransporte()),
        )

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["carga_transporte"]["equipe"][0]["custo_hora"] = -1
        self.assertEqual(
            desserializar_versao(json.dumps(documento)).status,
            StatusPersistencia.DADO_CORROMPIDO,
        )


class TestTelaCargaTransporte(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module(
            "modulos.orcamentos.apresentacao.carga_transporte"
        )

    def _dominio(self):
        return criar_orcamento_vazio("Fabio").valor

    def test_formulario_unico_sem_leitura_persistencia_ou_rerun_na_edicao(self):
        orcamento, versao = self._dominio()
        falso, repositorio = StreamlitCargaTransporteFalso(), Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="s",
            )
        self.assertEqual(falso.formularios, ["carga_transporte_formulario"])
        repositorio.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_uma_vez_preserva_medicao_e_faz_rerun(self):
        orcamento, versao = self._dominio()
        medicao = asdict(versao.medicao_orcamento)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="c"
        )
        falso = StreamlitCargaTransporteFalso(
            salvar=True, valores={"carga_transporte_custo_refeicao": 37.5}
        )
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="original",
            )
        repositorio.persistir_documento_versao.assert_called_once()
        _, salva, snapshot = repositorio.persistir_documento_versao.call_args.args
        self.assertEqual(snapshot, "original")
        self.assertEqual(salva.carga_transporte.custo_refeicao, 37.5)
        self.assertEqual(asdict(salva.medicao_orcamento), medicao)
        self.assertEqual(falso.reruns, 1)

    def test_conflito_nao_atualiza_estado_nem_executa_rerun(self):
        orcamento, versao = self._dominio()
        estado = {}
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.BRANCH_AVANCADA
        )
        falso = StreamlitCargaTransporteFalso(
            salvar=True, session_state=estado
        )
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="original",
            )
        self.assertEqual(falso.reruns, 0)
        self.assertNotIn("novo_orcamento_detalhe", estado)
        self.assertEqual(len(falso.erros), 1)


if __name__ == "__main__":
    unittest.main()
