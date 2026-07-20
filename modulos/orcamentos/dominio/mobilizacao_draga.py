"""Fotografia mínima da aba 1. Mob. Draga do Excel oficial."""

from dataclasses import dataclass
import math


def _texto(valor, campo, *, vazio=False):
    if not isinstance(valor, str) or (not vazio and not valor.strip()):
        raise ValueError(f"{campo} deve ser texto{' ou vazio' if vazio else ' não vazio'}.")
    return valor.strip()


def _numero(valor, campo):
    if valor is not None and (
        isinstance(valor, bool)
        or not isinstance(valor, (int, float))
        or not math.isfinite(valor)
        or valor < 0
    ):
        raise ValueError(f"{campo} deve ser numérico não negativo ou vazio.")
    return float(valor) if valor is not None else None


@dataclass(frozen=True, slots=True)
class LinhaMaoObraMobilizacao:
    id: str
    descricao: str
    quantidade: float | None
    custo_hora_manual: float | None
    custo_hora_base: float | None
    multiplicador_custo: float | None
    horas_dia_manual: float | None
    horas_referencia_id: str | None
    encargos_sociais: float | None

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição"))
        for campo in (
            "quantidade",
            "custo_hora_manual",
            "custo_hora_base",
            "multiplicador_custo",
            "horas_dia_manual",
            "encargos_sociais",
        ):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if self.horas_referencia_id is not None:
            object.__setattr__(
                self, "horas_referencia_id", _texto(self.horas_referencia_id, "referência")
            )
        formula_custo = self.custo_hora_base is not None or self.multiplicador_custo is not None
        if formula_custo and (
            self.custo_hora_base is None
            or self.multiplicador_custo is None
            or self.custo_hora_manual is not None
        ):
            raise ValueError("Custo/h deve ser manual ou base multiplicada, nunca ambos.")
        if self.horas_dia_manual is not None and self.horas_referencia_id is not None:
            raise ValueError("Horas/dia devem ser manuais ou referenciadas, nunca ambas.")

    @property
    def custo_hora(self):
        if self.custo_hora_base is None:
            return self.custo_hora_manual
        return self.custo_hora_base * self.multiplicador_custo


@dataclass(frozen=True, slots=True)
class ItemMobilizacaoDraga:
    id: str
    descricao: str
    unidade: str
    quantidade: float | None
    preco_unitario_manual: float | None
    preco_unitario_custo_diario: bool
    preco_total_calculado: bool
    preco_total_manual: float | None
    observacao: str = ""

    def __post_init__(self):
        for campo in ("id", "descricao", "unidade"):
            object.__setattr__(self, campo, _texto(getattr(self, campo), campo))
        object.__setattr__(self, "observacao", _texto(self.observacao, "observação", vazio=True))
        object.__setattr__(self, "quantidade", _numero(self.quantidade, "quantidade"))
        object.__setattr__(
            self,
            "preco_unitario_manual",
            _numero(self.preco_unitario_manual, "preço unitário"),
        )
        object.__setattr__(
            self, "preco_total_manual", _numero(self.preco_total_manual, "preço total")
        )
        if not isinstance(self.preco_unitario_custo_diario, bool) or not isinstance(
            self.preco_total_calculado, bool
        ):
            raise ValueError("Origens de preço inválidas.")
        if self.preco_unitario_custo_diario and self.preco_unitario_manual is not None:
            raise ValueError("Preço unitário deve ser manual ou vir do custo diário.")
        if self.preco_total_calculado and self.preco_total_manual is not None:
            raise ValueError("Preço total deve ser manual ou calculado.")


def _equipe_inicial():
    return (
        LinhaMaoObraMobilizacao(
            "operador-lider", "Operador Líder", None, 18, None, None, 9, None, 110
        ),
        LinhaMaoObraMobilizacao(
            "operador-draga", "Operador de Draga", 2, None, 22.68, 1.25,
            None, "operador-lider", 110,
        ),
        LinhaMaoObraMobilizacao(
            "ajudante-geral", "Ajudante Geral", 2, 11.13, None, None, 9, None, 110
        ),
    )


def _itens_iniciais():
    def calculado(id_, descricao, unidade, quantidade, unitario, observacao=""):
        return ItemMobilizacaoDraga(
            id_, descricao, unidade, quantidade, unitario, False, True, None, observacao
        )

    def informado(id_, descricao, unidade, quantidade, unitario, total, observacao=""):
        return ItemMobilizacaoDraga(
            id_, descricao, unidade, quantidade, unitario, False, False, total, observacao
        )

    return (
        calculado("guindaste-carregamento", "Guindaste para carregamento", "dia", 1, 1200),
        informado(
            "treinamentos",
            "Treinamentos (Trabalho em Altura e espaço confinado)",
            "dia", None, 3000, 0,
        ),
        informado("mobiliario-canteiro", "Mobiliário Canteiro", "vb", None, 3500, 0),
        informado(
            "carreta-carga-seca", "Carreta Carga Seca para DRAGA", "un", 1, 1300,
            1300, "Fabiano 23/03/2026",
        ),
        calculado(
            "guindaste-descarregamento",
            "Guindaste p/descarregamento e montagem DRAGA",
            "dia", 1, 5000, "Ideal",
        ),
        calculado("frete", "Frete", "vb", 1, 1000),
        informado(
            "trator-d4", "Trator D4 para lançar draga na água", "dia", None, 2000, 0
        ),
        ItemMobilizacaoDraga(
            "mao-obra-carga-montagem",
            "Mão de obra p/carga e montagem (r$/dia)",
            "dia", 5, None, True, False, 8461.72, "",
        ),
    )


@dataclass(frozen=True, slots=True)
class MobilizacaoDraga:
    equipe: tuple[LinhaMaoObraMobilizacao, ...] = _equipe_inicial()
    custo_refeicao: float | None = 40.0
    custo_transporte: float | None = 10.0
    itens: tuple[ItemMobilizacaoDraga, ...] = _itens_iniciais()
    bdi: float | None = None

    def __post_init__(self):
        object.__setattr__(self, "custo_refeicao", _numero(self.custo_refeicao, "refeição"))
        object.__setattr__(
            self, "custo_transporte", _numero(self.custo_transporte, "transporte")
        )
        object.__setattr__(self, "bdi", _numero(self.bdi, "BDI"))
        if not isinstance(self.equipe, tuple) or not all(
            isinstance(item, LinhaMaoObraMobilizacao) for item in self.equipe
        ):
            raise ValueError("Equipe da mobilização inválida.")
        if not isinstance(self.itens, tuple) or not all(
            isinstance(item, ItemMobilizacaoDraga) for item in self.itens
        ):
            raise ValueError("Itens da mobilização inválidos.")
        ids_equipe = [item.id for item in self.equipe]
        ids_itens = [item.id for item in self.itens]
        if len(ids_equipe) != len(set(ids_equipe)) or len(ids_itens) != len(set(ids_itens)):
            raise ValueError("Identificadores da mobilização devem ser únicos.")
        if any(
            item.horas_referencia_id is not None
            and item.horas_referencia_id not in ids_equipe
            for item in self.equipe
        ):
            raise ValueError("Referência de horas não pertence à equipe.")


@dataclass(frozen=True, slots=True)
class ResultadoLinhaMaoObra:
    id: str
    horas_dia: float | None
    total: float


@dataclass(frozen=True, slots=True)
class ResultadoItemMobilizacao:
    id: str
    preco_unitario: float | None
    preco_total: float | None


@dataclass(frozen=True, slots=True)
class ResultadosMobilizacaoDraga:
    mao_obra: tuple[ResultadoLinhaMaoObra, ...]
    quantidade_refeicoes: float
    total_refeicoes: float
    quantidade_transportes: float
    total_transportes: float
    custo_por_dia: float
    itens: tuple[ResultadoItemMobilizacao, ...]
    total_composicao: float
    valor_bdi: float
    preco_final: float
    preco_final_repetido: float


def calcular_mobilizacao_draga(mobilizacao: MobilizacaoDraga) -> ResultadosMobilizacaoDraga:
    """Reproduz somente as fórmulas realmente presentes em 1. Mob. Draga."""

    def zero(valor):
        return 0.0 if valor is None else valor

    por_id = {linha.id: linha for linha in mobilizacao.equipe}
    resultados_mao_obra = []
    for linha in mobilizacao.equipe:
        horas = linha.horas_dia_manual
        if linha.horas_referencia_id is not None:
            horas = por_id[linha.horas_referencia_id].horas_dia_manual
        total = zero(linha.quantidade) * zero(linha.custo_hora) * zero(horas)
        total *= 1 + zero(linha.encargos_sociais) / 100
        resultados_mao_obra.append(ResultadoLinhaMaoObra(linha.id, horas, total))

    quantidade_equipe = sum(zero(linha.quantidade) for linha in mobilizacao.equipe)
    total_refeicoes = quantidade_equipe * zero(mobilizacao.custo_refeicao)
    total_transportes = quantidade_equipe * zero(mobilizacao.custo_transporte)
    custo_por_dia = (
        sum(item.total for item in resultados_mao_obra)
        + total_refeicoes
        + total_transportes
    )

    resultados_itens = []
    for item in mobilizacao.itens:
        unitario = custo_por_dia if item.preco_unitario_custo_diario else item.preco_unitario_manual
        total = item.preco_total_manual
        if item.preco_total_calculado:
            total = zero(item.quantidade) * zero(unitario)
        resultados_itens.append(ResultadoItemMobilizacao(item.id, unitario, total))

    total_composicao = sum(zero(item.preco_total) for item in resultados_itens)
    valor_bdi = total_composicao * zero(mobilizacao.bdi) / 100
    preco_final = total_composicao + valor_bdi
    return ResultadosMobilizacaoDraga(
        tuple(resultados_mao_obra),
        quantidade_equipe,
        total_refeicoes,
        quantidade_equipe,
        total_transportes,
        custo_por_dia,
        tuple(resultados_itens),
        total_composicao,
        valor_bdi,
        preco_final,
        preco_final,
    )
