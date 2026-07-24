"""Modelos mínimos, em memória, do domínio de Orçamentos."""

from dataclasses import dataclass, field

from modulos.orcamentos.dominio.barrilete import Barrilete
from modulos.orcamentos.dominio.canteiro import Canteiro
from modulos.orcamentos.dominio.carga_transporte import CargaTransporte
from modulos.orcamentos.dominio.cotacoes import Cotacoes
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.desmobilizacao_draga import DesmobilizacaoDraga
from modulos.orcamentos.dominio.desmobilizacao_equipamento_polimero import (
    DesmobilizacaoEquipamentoPolimero,
)
from modulos.orcamentos.dominio.dragagem import Dragagem
from modulos.orcamentos.dominio.estados import EstadoCenario, EstadoVersao
from modulos.orcamentos.dominio.fornecimento_bag import FornecimentoBag
from modulos.orcamentos.dominio.identidades import CenarioId, OrcamentoId, VersaoId
from modulos.orcamentos.dominio.mobilizacao_draga import MobilizacaoDraga
from modulos.orcamentos.dominio.mobilizacao_equipamento_polimero import (
    MobilizacaoEquipamentoPolimero,
)
from modulos.orcamentos.dominio.medicao_orcamento import MedicaoOrcamento
from modulos.orcamentos.dominio.operacao_sistema import OperacaoSistema
from modulos.orcamentos.dominio.planilha_precos import PlanilhaPrecos
from modulos.orcamentos.dominio.premissas import Premissa
from modulos.orcamentos.dominio.preparacao_celula import PreparacaoCelula
from modulos.orcamentos.dominio.producao import Producao
from modulos.orcamentos.dominio.resultados import ResultadoOperacao


def _texto_obrigatorio(valor: str, campo: str) -> str:
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} deve ser informado.")
    return valor.strip()


@dataclass(frozen=True, slots=True)
class Cenario:
    id: CenarioId
    versao_id: VersaoId
    nome: str
    estado: EstadoCenario = EstadoCenario.ATIVO

    def __post_init__(self):
        object.__setattr__(self, "nome", _texto_obrigatorio(self.nome, "nome"))

    def como_descartado(self) -> "Cenario":
        if self.estado is EstadoCenario.DESCARTADO:
            return self
        return Cenario(self.id, self.versao_id, self.nome, EstadoCenario.DESCARTADO)


@dataclass(slots=True)
class VersaoOrcamento:
    id: VersaoId
    orcamento_id: OrcamentoId
    numero: int
    autor: str
    estado: EstadoVersao = EstadoVersao.ELABORACAO
    versao_anterior_id: VersaoId | None = None
    _cenarios: dict[CenarioId, Cenario] = field(default_factory=dict, repr=False)
    cenario_adotado_id: CenarioId | None = None
    _premissas: dict[tuple[CenarioId, str], tuple[Premissa, ...]] = field(
        default_factory=dict, repr=False
    )
    _dados_obra: DadosObra | None = field(default=None, repr=False)
    _cotacoes: Cotacoes = field(default_factory=Cotacoes.iniciais, repr=False)
    _producao: Producao = field(default_factory=Producao, repr=False)
    _barrilete: Barrilete = field(default_factory=Barrilete, repr=False)
    _mobilizacao_draga: MobilizacaoDraga = field(default_factory=MobilizacaoDraga, repr=False)
    _mobilizacao_equipamento_polimero: MobilizacaoEquipamentoPolimero = field(
        default_factory=MobilizacaoEquipamentoPolimero, repr=False
    )
    _canteiro: Canteiro = field(default_factory=Canteiro, repr=False)
    _preparacao_celula: PreparacaoCelula = field(default_factory=PreparacaoCelula, repr=False)
    _fornecimento_bag: FornecimentoBag = field(default_factory=FornecimentoBag, repr=False)
    _operacao_sistema: OperacaoSistema = field(default_factory=OperacaoSistema, repr=False)
    _dragagem: Dragagem = field(default_factory=Dragagem, repr=False)
    _desmobilizacao_draga: DesmobilizacaoDraga = field(
        default_factory=DesmobilizacaoDraga, repr=False
    )
    _desmobilizacao_equipamento_polimero: DesmobilizacaoEquipamentoPolimero = field(
        default_factory=DesmobilizacaoEquipamentoPolimero, repr=False
    )
    _medicao_orcamento: MedicaoOrcamento = field(
        default_factory=MedicaoOrcamento, repr=False
    )
    _carga_transporte: CargaTransporte = field(
        default_factory=CargaTransporte, repr=False
    )
    _planilha_precos: PlanilhaPrecos = field(
        default_factory=PlanilhaPrecos, repr=False
    )
    _inicializada: bool = field(default=False, init=False, repr=False)

    _CAMPOS_PROTEGIDOS = {
        "id",
        "orcamento_id",
        "numero",
        "autor",
        "estado",
        "versao_anterior_id",
        "cenario_adotado_id",
        "_cenarios",
        "_premissas",
        "_dados_obra",
        "_cotacoes",
        "_producao",
        "_barrilete",
        "_mobilizacao_draga",
        "_mobilizacao_equipamento_polimero",
        "_canteiro",
        "_preparacao_celula",
        "_fornecimento_bag",
        "_operacao_sistema",
        "_dragagem",
        "_desmobilizacao_draga",
        "_desmobilizacao_equipamento_polimero",
        "_medicao_orcamento",
        "_carga_transporte",
        "_planilha_precos",
        "_inicializada",
    }

    def __setattr__(self, nome, valor):
        if getattr(self, "_inicializada", False) and nome in self._CAMPOS_PROTEGIDOS:
            raise AttributeError(
                f"{nome} não pode ser alterado diretamente; use as operações do domínio."
            )
        object.__setattr__(self, nome, valor)

    def __post_init__(self):
        if not isinstance(self.numero, int) or self.numero < 1:
            raise ValueError("O número da versão deve ser inteiro positivo.")
        object.__setattr__(self, "autor", _texto_obrigatorio(self.autor, "autor"))
        if self.versao_anterior_id == self.id:
            raise ValueError("Uma versão não pode derivar de si mesma.")
        object.__setattr__(self, "_inicializada", True)

    @property
    def cenarios(self) -> tuple[Cenario, ...]:
        return tuple(self._cenarios.values())

    @property
    def premissas(self) -> tuple[tuple[CenarioId, Premissa], ...]:
        return tuple(
            (cenario_id, historico[-1])
            for (cenario_id, _), historico in self._premissas.items()
            if historico
        )

    @property
    def editavel(self) -> bool:
        return self.estado is EstadoVersao.ELABORACAO

    @property
    def dados_obra(self) -> DadosObra | None:
        return self._dados_obra

    @property
    def cotacoes(self) -> Cotacoes:
        return self._cotacoes

    @property
    def producao(self) -> Producao:
        return self._producao

    @property
    def barrilete(self) -> Barrilete:
        return self._barrilete

    @property
    def mobilizacao_draga(self) -> MobilizacaoDraga:
        return self._mobilizacao_draga

    @property
    def mobilizacao_equipamento_polimero(self) -> MobilizacaoEquipamentoPolimero:
        return self._mobilizacao_equipamento_polimero

    @property
    def canteiro(self) -> Canteiro:
        return self._canteiro

    @property
    def preparacao_celula(self) -> PreparacaoCelula:
        return self._preparacao_celula

    @property
    def fornecimento_bag(self) -> FornecimentoBag:
        return self._fornecimento_bag

    @property
    def operacao_sistema(self) -> OperacaoSistema:
        return self._operacao_sistema

    @property
    def dragagem(self) -> Dragagem:
        return self._dragagem

    @property
    def desmobilizacao_draga(self) -> DesmobilizacaoDraga:
        return self._desmobilizacao_draga

    @property
    def desmobilizacao_equipamento_polimero(
        self,
    ) -> DesmobilizacaoEquipamentoPolimero:
        return self._desmobilizacao_equipamento_polimero

    @property
    def medicao_orcamento(self) -> MedicaoOrcamento:
        return self._medicao_orcamento

    @property
    def carga_transporte(self) -> CargaTransporte:
        return self._carga_transporte

    @property
    def planilha_precos(self) -> PlanilhaPrecos:
        return self._planilha_precos

    def registrar_dados_obra(self, dados: DadosObra) -> ResultadoOperacao[DadosObra]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Dados Obra."
            )
        if not isinstance(dados, DadosObra):
            return ResultadoOperacao.falha("Dados Obra inválidos.")
        object.__setattr__(self, "_dados_obra", dados)
        return ResultadoOperacao.ok(dados)

    def registrar_cotacoes(self, cotacoes: Cotacoes) -> ResultadoOperacao[Cotacoes]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Cotações."
            )
        if not isinstance(cotacoes, Cotacoes):
            return ResultadoOperacao.falha("Cotações inválidas.")
        object.__setattr__(self, "_cotacoes", cotacoes)
        return ResultadoOperacao.ok(cotacoes)

    def registrar_producao(self, producao: Producao) -> ResultadoOperacao[Producao]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Produção."
            )
        if not isinstance(producao, Producao):
            return ResultadoOperacao.falha("Produção inválida.")
        object.__setattr__(self, "_producao", producao)
        return ResultadoOperacao.ok(producao)

    def registrar_barrilete(self, barrilete: Barrilete) -> ResultadoOperacao[Barrilete]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Barrilete."
            )
        if not isinstance(barrilete, Barrilete):
            return ResultadoOperacao.falha("Barrilete inválido.")
        object.__setattr__(self, "_barrilete", barrilete)
        return ResultadoOperacao.ok(barrilete)

    def registrar_mobilizacao_draga(
        self, mobilizacao: MobilizacaoDraga
    ) -> ResultadoOperacao[MobilizacaoDraga]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Mobilização da Draga."
            )
        if not isinstance(mobilizacao, MobilizacaoDraga):
            return ResultadoOperacao.falha("Mobilização da Draga inválida.")
        object.__setattr__(self, "_mobilizacao_draga", mobilizacao)
        return ResultadoOperacao.ok(mobilizacao)

    def registrar_mobilizacao_equipamento_polimero(
        self, mobilizacao: MobilizacaoEquipamentoPolimero
    ) -> ResultadoOperacao[MobilizacaoEquipamentoPolimero]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Mobilização do Equipamento de Polímero."
            )
        if not isinstance(mobilizacao, MobilizacaoEquipamentoPolimero):
            return ResultadoOperacao.falha("Mobilização do Equipamento de Polímero inválida.")
        object.__setattr__(self, "_mobilizacao_equipamento_polimero", mobilizacao)
        return ResultadoOperacao.ok(mobilizacao)

    def registrar_canteiro(self, canteiro: Canteiro) -> ResultadoOperacao[Canteiro]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Canteiro."
            )
        if not isinstance(canteiro, Canteiro):
            return ResultadoOperacao.falha("Canteiro inválido.")
        object.__setattr__(self, "_canteiro", canteiro)
        return ResultadoOperacao.ok(canteiro)

    def registrar_preparacao_celula(
        self, preparacao: PreparacaoCelula
    ) -> ResultadoOperacao[PreparacaoCelula]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Preparação da Célula."
            )
        if not isinstance(preparacao, PreparacaoCelula):
            return ResultadoOperacao.falha("Preparação da Célula inválida.")
        object.__setattr__(self, "_preparacao_celula", preparacao)
        return ResultadoOperacao.ok(preparacao)

    def registrar_fornecimento_bag(
        self, fornecimento: FornecimentoBag
    ) -> ResultadoOperacao[FornecimentoBag]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Fornecimento de Bag."
            )
        if not isinstance(fornecimento, FornecimentoBag):
            return ResultadoOperacao.falha("Fornecimento de Bag inválido.")
        object.__setattr__(self, "_fornecimento_bag", fornecimento)
        return ResultadoOperacao.ok(fornecimento)

    def registrar_operacao_sistema(
        self, operacao: OperacaoSistema
    ) -> ResultadoOperacao[OperacaoSistema]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Operação do Sistema."
            )
        if not isinstance(operacao, OperacaoSistema):
            return ResultadoOperacao.falha("Operação do Sistema inválida.")
        object.__setattr__(self, "_operacao_sistema", operacao)
        return ResultadoOperacao.ok(operacao)

    def registrar_dragagem(self, dragagem: Dragagem) -> ResultadoOperacao[Dragagem]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Dragagem."
            )
        if not isinstance(dragagem, Dragagem):
            return ResultadoOperacao.falha("Dragagem inválida.")
        object.__setattr__(self, "_dragagem", dragagem)
        return ResultadoOperacao.ok(dragagem)

    def registrar_desmobilizacao_draga(
        self, desmobilizacao: DesmobilizacaoDraga
    ) -> ResultadoOperacao[DesmobilizacaoDraga]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Desmobilização da Draga."
            )
        if not isinstance(desmobilizacao, DesmobilizacaoDraga):
            return ResultadoOperacao.falha("Desmobilização da Draga inválida.")
        object.__setattr__(self, "_desmobilizacao_draga", desmobilizacao)
        return ResultadoOperacao.ok(desmobilizacao)

    def registrar_desmobilizacao_equipamento_polimero(
        self, desmobilizacao: DesmobilizacaoEquipamentoPolimero
    ) -> ResultadoOperacao[DesmobilizacaoEquipamentoPolimero]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar "
                "Desmobilização do Equipamento de Polímero."
            )
        if not isinstance(desmobilizacao, DesmobilizacaoEquipamentoPolimero):
            return ResultadoOperacao.falha(
                "Desmobilização do Equipamento de Polímero inválida."
            )
        object.__setattr__(
            self, "_desmobilizacao_equipamento_polimero", desmobilizacao
        )
        return ResultadoOperacao.ok(desmobilizacao)

    def registrar_medicao_orcamento(
        self, medicao: MedicaoOrcamento
    ) -> ResultadoOperacao[MedicaoOrcamento]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Medição."
            )
        if not isinstance(medicao, MedicaoOrcamento):
            return ResultadoOperacao.falha("Medição inválida.")
        object.__setattr__(self, "_medicao_orcamento", medicao)
        return ResultadoOperacao.ok(medicao)

    def registrar_carga_transporte(
        self, carga_transporte: CargaTransporte
    ) -> ResultadoOperacao[CargaTransporte]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar Carga e Transporte."
            )
        if not isinstance(carga_transporte, CargaTransporte):
            return ResultadoOperacao.falha("Carga e Transporte inválida.")
        object.__setattr__(self, "_carga_transporte", carga_transporte)
        return ResultadoOperacao.ok(carga_transporte)

    def registrar_planilha_precos(
        self, planilha_precos: PlanilhaPrecos
    ) -> ResultadoOperacao[PlanilhaPrecos]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode alterar a Planilha de Preços."
            )
        if not isinstance(planilha_precos, PlanilhaPrecos):
            return ResultadoOperacao.falha("Planilha de Preços inválida.")
        object.__setattr__(self, "_planilha_precos", planilha_precos)
        return ResultadoOperacao.ok(planilha_precos)

    def historico_premissa(
        self, cenario_id: CenarioId, conceito: str
    ) -> tuple[Premissa, ...]:
        chave = (cenario_id, _texto_obrigatorio(conceito, "conceito"))
        return self._premissas.get(chave, ())

    def registrar_premissa(
        self, cenario_id: CenarioId, premissa: Premissa
    ) -> ResultadoOperacao[Premissa]:
        if not self.editavel:
            return ResultadoOperacao.falha(
                "Versão congelada ou aprovada não pode receber premissas."
            )
        cenario = self._cenarios.get(cenario_id)
        if cenario is None:
            return ResultadoOperacao.falha("O cenário não pertence a esta versão.")
        if cenario.estado is EstadoCenario.DESCARTADO:
            return ResultadoOperacao.falha("Cenário descartado não pode receber premissas.")
        chave = (cenario_id, premissa.conceito)
        historico = self._premissas.get(chave, ())
        if premissa.sequencia != len(historico) + 1:
            return ResultadoOperacao.falha(
                "A sequência da premissa deve continuar o histórico existente."
            )
        self._premissas[chave] = historico + (premissa,)
        return ResultadoOperacao.ok(premissa)

    def adicionar_cenario(self, cenario: Cenario) -> ResultadoOperacao[Cenario]:
        if not self.editavel:
            return ResultadoOperacao.falha("Versão congelada ou aprovada não pode ser alterada.")
        if cenario.versao_id != self.id:
            return ResultadoOperacao.falha("O cenário pertence a outra versão.")
        if cenario.id in self._cenarios:
            return ResultadoOperacao.falha("Já existe cenário com esta identidade na versão.")
        self._cenarios[cenario.id] = cenario
        return ResultadoOperacao.ok(cenario)

    def descartar_cenario(self, cenario_id: CenarioId) -> ResultadoOperacao[Cenario]:
        if not self.editavel:
            return ResultadoOperacao.falha("Versão congelada ou aprovada não pode ser alterada.")
        cenario = self._cenarios.get(cenario_id)
        if cenario is None:
            return ResultadoOperacao.falha("O cenário não pertence a esta versão.")
        if cenario.estado is EstadoCenario.DESCARTADO:
            return ResultadoOperacao.falha("O cenário já está descartado.")
        if self.cenario_adotado_id == cenario_id:
            return ResultadoOperacao.falha("O cenário adotado não pode ser descartado.")
        descartado = cenario.como_descartado()
        self._cenarios[cenario_id] = descartado
        return ResultadoOperacao.ok(descartado)

    def adotar_cenario(self, cenario_id: CenarioId) -> ResultadoOperacao[Cenario]:
        if not self.editavel:
            return ResultadoOperacao.falha("A adoção só pode mudar durante a elaboração.")
        cenario = self._cenarios.get(cenario_id)
        if cenario is None:
            return ResultadoOperacao.falha("O cenário não pertence a esta versão.")
        if cenario.estado is EstadoCenario.DESCARTADO:
            return ResultadoOperacao.falha("Cenário descartado não pode ser adotado.")
        object.__setattr__(self, "cenario_adotado_id", cenario_id)
        return ResultadoOperacao.ok(cenario)

    def congelar(self) -> ResultadoOperacao["VersaoOrcamento"]:
        if self.estado is not EstadoVersao.ELABORACAO:
            return ResultadoOperacao.falha("Somente versão em elaboração pode ser congelada.")
        if not any(c.estado is EstadoCenario.ATIVO for c in self._cenarios.values()):
            return ResultadoOperacao.falha("A versão precisa possuir ao menos um cenário ativo.")
        object.__setattr__(self, "estado", EstadoVersao.CONGELADA)
        return ResultadoOperacao.ok(self)

    def aprovar(self) -> ResultadoOperacao["VersaoOrcamento"]:
        if self.estado is not EstadoVersao.CONGELADA:
            return ResultadoOperacao.falha("Somente versão congelada pode ser aprovada.")
        if self.cenario_adotado_id is None:
            return ResultadoOperacao.falha("A aprovação exige um cenário adotado.")
        cenario = self._cenarios.get(self.cenario_adotado_id)
        if cenario is None or cenario.estado is not EstadoCenario.ATIVO:
            return ResultadoOperacao.falha("O cenário adotado precisa existir e estar ativo.")
        object.__setattr__(self, "estado", EstadoVersao.APROVADA)
        return ResultadoOperacao.ok(self)


@dataclass(slots=True)
class Orcamento:
    id: OrcamentoId
    objeto: str
    finalidade: str
    responsavel: str
    _versoes: dict[VersaoId, VersaoOrcamento] = field(default_factory=dict, repr=False)

    def __post_init__(self):
        self.objeto = _texto_obrigatorio(self.objeto, "objeto")
        self.finalidade = _texto_obrigatorio(self.finalidade, "finalidade")
        self.responsavel = _texto_obrigatorio(self.responsavel, "responsável")

    @property
    def versoes(self) -> tuple[VersaoOrcamento, ...]:
        return tuple(self._versoes.values())

    def adicionar_versao(self, versao: VersaoOrcamento) -> ResultadoOperacao[VersaoOrcamento]:
        if versao.orcamento_id != self.id:
            return ResultadoOperacao.falha("A versão pertence a outro orçamento.")
        if versao.id in self._versoes:
            return ResultadoOperacao.falha("Já existe versão com esta identidade.")
        if any(existente.numero == versao.numero for existente in self._versoes.values()):
            return ResultadoOperacao.falha("Já existe versão com este número.")
        if versao.versao_anterior_id is not None and versao.versao_anterior_id not in self._versoes:
            return ResultadoOperacao.falha("A versão anterior não pertence ao orçamento.")
        self._versoes[versao.id] = versao
        return ResultadoOperacao.ok(versao)
