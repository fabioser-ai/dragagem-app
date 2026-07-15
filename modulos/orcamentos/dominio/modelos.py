"""Modelos mínimos, em memória, do domínio de Orçamentos."""

from dataclasses import dataclass, field

from modulos.orcamentos.aplicacao.resultados import ResultadoOperacao
from modulos.orcamentos.dominio.estados import EstadoCenario, EstadoVersao
from modulos.orcamentos.dominio.identidades import CenarioId, OrcamentoId, VersaoId


def _texto_obrigatorio(valor: str, campo: str) -> str:
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} deve ser informado.")
    return valor.strip()


@dataclass(slots=True)
class Cenario:
    id: CenarioId
    versao_id: VersaoId
    nome: str
    estado: EstadoCenario = EstadoCenario.ATIVO

    def __post_init__(self):
        self.nome = _texto_obrigatorio(self.nome, "nome")

    def descartar(self) -> ResultadoOperacao["Cenario"]:
        if self.estado is EstadoCenario.DESCARTADO:
            return ResultadoOperacao.falha("O cenário já está descartado.")
        self.estado = EstadoCenario.DESCARTADO
        return ResultadoOperacao.ok(self)


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

    def __post_init__(self):
        if not isinstance(self.numero, int) or self.numero < 1:
            raise ValueError("O número da versão deve ser inteiro positivo.")
        self.autor = _texto_obrigatorio(self.autor, "autor")
        if self.versao_anterior_id == self.id:
            raise ValueError("Uma versão não pode derivar de si mesma.")

    @property
    def cenarios(self) -> tuple[Cenario, ...]:
        return tuple(self._cenarios.values())

    @property
    def editavel(self) -> bool:
        return self.estado is EstadoVersao.ELABORACAO

    def adicionar_cenario(self, cenario: Cenario) -> ResultadoOperacao[Cenario]:
        if not self.editavel:
            return ResultadoOperacao.falha("Versão congelada ou aprovada não pode ser alterada.")
        if cenario.versao_id != self.id:
            return ResultadoOperacao.falha("O cenário pertence a outra versão.")
        if cenario.id in self._cenarios:
            return ResultadoOperacao.falha("Já existe cenário com esta identidade na versão.")
        self._cenarios[cenario.id] = cenario
        return ResultadoOperacao.ok(cenario)

    def adotar_cenario(self, cenario_id: CenarioId) -> ResultadoOperacao[Cenario]:
        if not self.editavel:
            return ResultadoOperacao.falha("A adoção só pode mudar durante a elaboração.")
        cenario = self._cenarios.get(cenario_id)
        if cenario is None:
            return ResultadoOperacao.falha("O cenário não pertence a esta versão.")
        if cenario.estado is EstadoCenario.DESCARTADO:
            return ResultadoOperacao.falha("Cenário descartado não pode ser adotado.")
        self.cenario_adotado_id = cenario_id
        return ResultadoOperacao.ok(cenario)

    def congelar(self) -> ResultadoOperacao["VersaoOrcamento"]:
        if self.estado is not EstadoVersao.ELABORACAO:
            return ResultadoOperacao.falha("Somente versão em elaboração pode ser congelada.")
        if not self._cenarios:
            return ResultadoOperacao.falha("A versão precisa possuir ao menos um cenário.")
        self.estado = EstadoVersao.CONGELADA
        return ResultadoOperacao.ok(self)

    def aprovar(self) -> ResultadoOperacao["VersaoOrcamento"]:
        if self.estado is not EstadoVersao.CONGELADA:
            return ResultadoOperacao.falha("Somente versão congelada pode ser aprovada.")
        if self.cenario_adotado_id is None:
            return ResultadoOperacao.falha("A aprovação exige um cenário adotado.")
        self.estado = EstadoVersao.APROVADA
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
