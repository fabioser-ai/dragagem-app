import importlib
import json
import math
import sys
import types
import unittest
from contextlib import nullcontext
from dataclasses import asdict, replace
from unittest.mock import Mock, patch

from modulos.orcamentos.aplicacao.criacao import criar_orcamento_vazio
from modulos.orcamentos.aplicacao.medicao_orcamento import (
    salvar_medicao_orcamento,
)
from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.medicao_orcamento import (
    FORMULAS_MEDICAO_ORCAMENTO,
    REFERENCIAS_SALARIAIS_MEDICAO,
    ItemMedicaoOrcamento,
    LinhaMaoObraMedicao,
    MedicaoOrcamento,
    calcular_medicao_orcamento,
)
from modulos.orcamentos.persistencia.contratos import (
    ResultadoPersistencia,
    StatusPersistencia,
)
from modulos.orcamentos.persistencia.serializacao import (
    desserializar_versao,
    serializar_versao,
)


class ColunaFalsa:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class StreamlitMedicaoFalso:
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
        return self.salvar and texto == "Salvar Medição do orçamento"

    def subheader(self, texto):
        pass

    def markdown(self, texto):
        pass

    def caption(self, texto):
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


class TestCalculosMedicaoOrcamento(unittest.TestCase):
    def calcular(self, medicao=None):
        return calcular_medicao_orcamento(medicao or MedicaoOrcamento())

    def test_fotografia_inicial_preserva_estrutura_e_numeracao(self):
        medicao = MedicaoOrcamento()
        self.assertEqual(len(medicao.equipe), 3)
        self.assertEqual(len(medicao.itens), 3)
        self.assertEqual([item.numero for item in medicao.itens], [1, 3, 4])
        self.assertIsNone(medicao.equipe[0].quantidade)
        self.assertEqual(medicao.equipe[0].custo_hora, 14.5)
        self.assertEqual(
            medicao.itens[2].descricao, "Acompanhamento  Coleta BagsFOS"
        )
        self.assertIsNone(medicao.bdi_principal)
        self.assertEqual(medicao.bdi_secundario, 0)

    def test_lista_completa_das_dezenove_formulas_sem_compartilhadas(self):
        self.assertEqual(
            FORMULAS_MEDICAO_ORCAMENTO,
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
                ("E16", "=F10"),
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
        self.assertAlmostEqual(resultado.mao_obra[1].total, 857.304)
        self.assertAlmostEqual(resultado.mao_obra[2].total, 420.714)
        self.assertEqual(resultado.quantidade_pessoas, 4)
        self.assertEqual(resultado.total_refeicoes, 120)
        self.assertEqual(resultado.total_transportes, 40)
        self.assertAlmostEqual(resultado.custo_por_dia, 1438.018)

    def test_itens_repetem_custo_diario_sem_referencia_externa(self):
        resultado = self.calcular()
        self.assertEqual(resultado.itens[0].preco_unitario, 60)
        self.assertEqual(resultado.itens[0].preco_total, 2700)
        self.assertAlmostEqual(resultado.itens[1].preco_unitario, 1438.018)
        self.assertAlmostEqual(resultado.itens[1].preco_total, 4314.054)
        self.assertAlmostEqual(resultado.itens[2].preco_total, 7190.09)

    def test_total_bdi_principal_vazio_e_preco_final(self):
        resultado = self.calcular()
        self.assertAlmostEqual(resultado.total, 14204.144)
        self.assertEqual(resultado.valor_bdi_principal, 0)
        self.assertAlmostEqual(resultado.preco_final, 14204.144)
        com_bdi = self.calcular(
            replace(MedicaoOrcamento(), bdi_principal=7.5)
        )
        self.assertAlmostEqual(com_bdi.valor_bdi_principal, com_bdi.total * 0.075)
        self.assertAlmostEqual(com_bdi.preco_final, com_bdi.total * 1.075)

    def test_bloco_secundario_preserva_f21_vazia_e_bdi_zero(self):
        resultado = self.calcular()
        self.assertEqual(resultado.valor_bdi_secundario, 0)
        self.assertEqual(resultado.preco_final_secundario, 0)
        alterado = self.calcular(
            replace(MedicaoOrcamento(), bdi_secundario=10)
        )
        self.assertEqual(alterado.valor_bdi_secundario, 0)
        self.assertEqual(alterado.preco_final_secundario, 0)

    def test_referencias_salariais_sao_informativas_e_nao_formulas(self):
        self.assertEqual(
            REFERENCIAS_SALARIAIS_MEDICAO,
            (
                (22.68, "Operador"),
                (11.13, "ajudante"),
                (15.15, "Operador sistema de desidrataçao"),
            ),
        )
        self.assertFalse(
            any(celula.startswith(("K", "L")) for celula, _ in FORMULAS_MEDICAO_ORCAMENTO)
        )

    def test_decimais_e_vazios_permanecem_seguros(self):
        base = MedicaoOrcamento()
        vazio = MedicaoOrcamento(
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
                MedicaoOrcamento(custo_refeicao=valor)
        with self.assertRaises(ValueError):
            replace(
                MedicaoOrcamento().itens[1],
                preco_unitario_manual=1,
            )
        with self.assertRaises(ValueError):
            LinhaMaoObraMedicao("x", "X", 1, 1, 8, "outra", 1)

    def test_versao_congelada_recusa_salvamento(self):
        _, versao = criar_orcamento_vazio("Fabio").valor
        object.__setattr__(versao, "estado", EstadoVersao.CONGELADA)
        self.assertFalse(
            salvar_medicao_orcamento(versao, MedicaoOrcamento()).sucesso
        )


class TestPersistenciaMedicaoOrcamento(unittest.TestCase):
    def test_round_trip_persiste_entradas_e_preserva_telas_anteriores(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        desmob_polimero = asdict(versao.desmobilizacao_equipamento_polimero)
        alterada = replace(
            MedicaoOrcamento(),
            custo_refeicao=35.75,
            bdi_principal=2.5,
        )
        versao.registrar_medicao_orcamento(alterada)
        carregada = desserializar_versao(
            serializar_versao(orcamento, versao)
        ).valor[1]
        self.assertEqual(asdict(carregada.medicao_orcamento), asdict(alterada))
        self.assertEqual(
            asdict(carregada.desmobilizacao_equipamento_polimero),
            desmob_polimero,
        )

    def test_serializacao_persiste_somente_entradas(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        dados = json.loads(serializar_versao(orcamento, versao))["versao"][
            "medicao_orcamento"
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

    def test_schema_17_sem_nova_aba_continua_legivel(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["schema_version"] = 17
        documento["versao"].pop("medicao_orcamento")
        documento["versao"].pop("carga_transporte")
        documento["versao"].pop("planilha_precos")
        resultado = desserializar_versao(json.dumps(documento))
        self.assertTrue(resultado.sucesso)
        self.assertEqual(
            asdict(resultado.valor[1].medicao_orcamento),
            asdict(MedicaoOrcamento()),
        )

    def test_documento_invalido_e_rejeitado(self):
        orcamento, versao = criar_orcamento_vazio("Fabio").valor
        documento = json.loads(serializar_versao(orcamento, versao))
        documento["versao"]["medicao_orcamento"]["equipe"][0]["custo_hora"] = -1
        self.assertEqual(
            desserializar_versao(json.dumps(documento)).status,
            StatusPersistencia.DADO_CORROMPIDO,
        )


class TestTelaMedicaoOrcamento(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.modules.setdefault("streamlit", types.ModuleType("streamlit"))
        cls.tela = importlib.import_module(
            "modulos.orcamentos.apresentacao.medicao_orcamento"
        )

    def _dominio(self):
        return criar_orcamento_vazio("Fabio").valor

    def test_formulario_unico_sem_leitura_persistencia_ou_rerun_na_edicao(self):
        orcamento, versao = self._dominio()
        falso, repositorio = StreamlitMedicaoFalso(), Mock()
        with patch.object(self.tela, "st", falso):
            self.tela.render(
                repositorio=repositorio,
                orcamento=orcamento,
                versao=versao,
                snapshot_esperado="s",
            )
        self.assertEqual(falso.formularios, ["medicao_orcamento_formulario"])
        repositorio.assert_not_called()
        self.assertEqual(falso.reruns, 0)

    def test_salvar_persiste_uma_vez_e_faz_rerun(self):
        orcamento, versao = self._dominio()
        desmob = asdict(versao.desmobilizacao_equipamento_polimero)
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.SUCESSO, commit_sha="c"
        )
        falso = StreamlitMedicaoFalso(
            salvar=True, valores={"medicao_custo_refeicao": 37.5}
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
        self.assertEqual(salva.medicao_orcamento.custo_refeicao, 37.5)
        self.assertEqual(
            asdict(salva.desmobilizacao_equipamento_polimero), desmob
        )
        self.assertEqual(falso.reruns, 1)

    def test_conflito_nao_atualiza_estado_nem_executa_rerun(self):
        orcamento, versao = self._dominio()
        estado = {}
        repositorio = Mock()
        repositorio.persistir_documento_versao.return_value = ResultadoPersistencia(
            StatusPersistencia.BRANCH_AVANCADA
        )
        falso = StreamlitMedicaoFalso(salvar=True, session_state=estado)
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


class TestIsolamentoModuloOperacionalMedicoes(unittest.TestCase):
    def test_novo_dominio_nao_importa_modulo_operacional(self):
        modulo = importlib.import_module(
            "modulos.orcamentos.dominio.medicao_orcamento"
        )
        nomes = set(modulo.__dict__)
        self.assertFalse(any(nome.startswith("modulos.medicoes") for nome in nomes))
        with open(modulo.__file__, encoding="utf-8") as arquivo:
            self.assertNotIn("modulos.medicoes", arquivo.read())

    def test_arquivos_operacionais_nao_sao_necessarios_para_calcular(self):
        resultado = calcular_medicao_orcamento(MedicaoOrcamento())
        self.assertAlmostEqual(resultado.preco_final, 14204.144)


if __name__ == "__main__":
    unittest.main()
