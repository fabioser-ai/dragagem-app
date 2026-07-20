"""Fotografia funcional mínima da aba 5. Operação Sistema."""

from dataclasses import dataclass
import math


def _numero(valor, campo):
    if valor is not None and (
        isinstance(valor, bool) or not isinstance(valor, (int, float))
        or not math.isfinite(valor) or valor < 0
    ):
        raise ValueError(f"{campo} deve ser numérico não negativo ou vazio.")
    return float(valor) if valor is not None else None


def _texto(valor, campo, *, vazio=False):
    if not isinstance(valor, str) or (not vazio and not valor.strip()):
        raise ValueError(f"{campo} deve ser texto{' ou vazio' if vazio else ' não vazio'}.")
    return valor.strip()


@dataclass(frozen=True, slots=True)
class LinhaMaoObraOperacaoSistema:
    id: str
    descricao: str
    quantidade: float | None
    custo_hora_manual: float | None
    custo_hora_operador_calculado: bool
    encargos_sociais: float | None

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição"))
        for campo in ("quantidade", "custo_hora_manual", "encargos_sociais"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if not isinstance(self.custo_hora_operador_calculado, bool):
            raise ValueError("Origem do custo-hora inválida.")
        if self.custo_hora_manual is not None and self.custo_hora_operador_calculado:
            raise ValueError("Custo-hora deve possuir uma única origem.")


@dataclass(frozen=True, slots=True)
class ItemOperacaoSistema:
    id: str
    numero: int
    descricao: str
    unidade: str
    quantidade_manual: float | None
    quantidade_polimero: bool
    quantidade_dias_operacao: bool
    preco_unitario_manual: float | None
    preco_unitario_custo_diario: bool
    preco_total_calculado: bool
    preco_total_manual: float | None
    observacao: str = ""

    def __post_init__(self):
        object.__setattr__(self, "id", _texto(self.id, "id"))
        object.__setattr__(self, "descricao", _texto(self.descricao, "descrição"))
        object.__setattr__(self, "unidade", _texto(self.unidade, "unidade"))
        object.__setattr__(self, "observacao", _texto(self.observacao, "observação", vazio=True))
        if isinstance(self.numero, bool) or not isinstance(self.numero, int) or self.numero < 1:
            raise ValueError("número do item deve ser inteiro positivo.")
        for campo in ("quantidade_manual", "preco_unitario_manual", "preco_total_manual"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        flags = (
            self.quantidade_polimero, self.quantidade_dias_operacao,
            self.preco_unitario_custo_diario, self.preco_total_calculado,
        )
        if not all(isinstance(x, bool) for x in flags):
            raise ValueError("Origens do item inválidas.")
        if sum((self.quantidade_manual is not None, self.quantidade_polimero, self.quantidade_dias_operacao)) > 1:
            raise ValueError("Quantidade deve possuir uma única origem.")
        if self.preco_unitario_manual is not None and self.preco_unitario_custo_diario:
            raise ValueError("Preço unitário deve possuir uma única origem.")
        if self.preco_total_calculado and self.preco_total_manual is not None:
            raise ValueError("Preço total deve ser manual ou calculado.")


def _equipe_inicial():
    return (
        LinhaMaoObraOperacaoSistema(
            "operador-sistema", "Operador do Sistema de preparo e injeção",
            1, None, True, 110,
        ),
        LinhaMaoObraOperacaoSistema(
            "ajudante-geral", "Ajudante Geral", 1, 11.13, False, 110,
        ),
    )


def _itens_iniciais():
    def item(numero, id_, descricao, unidade, quantidade, polimero, dias, unitario, custo_dia, calculado, total, observacao=""):
        return ItemOperacaoSistema(
            id_, numero, descricao, unidade, quantidade, polimero, dias,
            unitario, custo_dia, calculado, total, observacao,
        )
    return (
        item(1, "equipamento-polimero", "Equipamento de preparo e injeção polímero", "vb", 1, False, False, 25000, False, True, None, "Novo 85k"),
        item(2, "polimero", "Polimero (calculado sobre base seca)", "kg", None, True, False, 22, False, True, None, "Total  ton secas (3 kg por ton seca) - Matryx - Xenifloc 3080X - 20,70 (20/01/21)"),
        item(3, "frete-polimero", "Frete Polimero", "un", 2, False, False, 1500, False, True, None),
        item(4, "agua-operacao", "(Caminhao Pipa) fornecimento de água para operação", "mes", None, False, False, None, False, False, 0, "Fornecido pela Contratante"),
        item(5, "energia-diesel", "(Gerador) fornecimento de energia para operação + diesel", "mes", None, False, False, None, False, False, 0, "Fornecido pela Contratante"),
        item(6, "instalacoes-hidraulicas", "Instalações hidráulicas", "vb", 1, False, False, 2000, False, False, 2000),
        item(7, "maquina-wap", "Máquina Wap", "vb", None, False, False, None, False, False, 0),
        item(8, "mao-obra-operacao", "Mão de obra para operação do sistema", "dia", None, False, True, None, True, False, 58344.8175),
    )


@dataclass(frozen=True, slots=True)
class OperacaoSistema:
    equipe: tuple[LinhaMaoObraOperacaoSistema, ...] = _equipe_inicial()
    custo_refeicao: float | None = 30.0
    custo_transporte: float | None = 10.0
    itens: tuple[ItemOperacaoSistema, ...] = _itens_iniciais()

    def __post_init__(self):
        for campo in ("custo_refeicao", "custo_transporte"):
            object.__setattr__(self, campo, _numero(getattr(self, campo), campo))
        if not isinstance(self.equipe, tuple) or not all(isinstance(x, LinhaMaoObraOperacaoSistema) for x in self.equipe):
            raise ValueError("Equipe da operação do sistema inválida.")
        if not isinstance(self.itens, tuple) or not all(isinstance(x, ItemOperacaoSistema) for x in self.itens):
            raise ValueError("Itens da operação do sistema inválidos.")
        ids = [x.id for x in self.equipe] + [x.id for x in self.itens]
        if len(ids) != len(set(ids)):
            raise ValueError("Identificadores da operação do sistema devem ser únicos.")


@dataclass(frozen=True, slots=True)
class ResultadoLinhaOperacaoSistema:
    id: str
    custo_hora: float | None
    horas_dia: float | None
    total: float


@dataclass(frozen=True, slots=True)
class MemorialPolimero:
    tonelada_seca: float | None
    dosagem_kg_por_tonelada: float
    acrescimo: float
    quantidade_polimero: float


@dataclass(frozen=True, slots=True)
class ResultadoItemOperacaoSistema:
    id: str
    quantidade: float | None
    preco_unitario: float | None
    preco_total: float | None


@dataclass(frozen=True, slots=True)
class ResultadosOperacaoSistema:
    mao_obra: tuple[ResultadoLinhaOperacaoSistema, ...]
    quantidade_pessoas: float
    total_refeicoes: float
    total_transportes: float
    custo_por_dia: float
    memorial_polimero: MemorialPolimero
    prazo_execucao_meses: int | None
    dias_operacao: float
    itens: tuple[ResultadoItemOperacaoSistema, ...]
    total: float
    custo_mensal: float | None


def calcular_operacao_sistema(
    operacao: OperacaoSistema,
    horas_dados_obra: float | None,
    tonelada_seca_fornecimento_bag: float | None,
    prazo_producao_meses: float | None,
) -> ResultadosOperacaoSistema:
    """Reproduz somente as 19 fórmulas efetivamente presentes na aba oficial."""
    zero = lambda valor: 0.0 if valor is None else valor
    mao_obra = []
    for linha in operacao.equipe:
        custo = 15.15 * 1.25 if linha.custo_hora_operador_calculado else linha.custo_hora_manual
        total = zero(linha.quantidade) * zero(custo) * zero(horas_dados_obra)
        total *= 1 + zero(linha.encargos_sociais) / 100
        mao_obra.append(ResultadoLinhaOperacaoSistema(linha.id, custo, horas_dados_obra, total))
    pessoas = sum(zero(x.quantidade) for x in operacao.equipe)
    refeicoes = pessoas * zero(operacao.custo_refeicao)
    transportes = pessoas * zero(operacao.custo_transporte)
    custo_dia = sum(x.total for x in mao_obra) + refeicoes + transportes

    quantidade_polimero = zero(tonelada_seca_fornecimento_bag) * 3 * 1.05
    memorial = MemorialPolimero(tonelada_seca_fornecimento_bag, 3.0, 1.05, quantidade_polimero)
    prazo = math.ceil(prazo_producao_meses) if prazo_producao_meses is not None else None
    dias = zero(prazo) * 30

    itens = []
    for item in operacao.itens:
        quantidade = item.quantidade_manual
        if item.quantidade_polimero:
            quantidade = quantidade_polimero
        elif item.quantidade_dias_operacao:
            quantidade = dias
        unitario = custo_dia if item.preco_unitario_custo_diario else item.preco_unitario_manual
        total_item = item.preco_total_manual
        if item.preco_total_calculado:
            total_item = zero(quantidade) * zero(unitario)
        itens.append(ResultadoItemOperacaoSistema(item.id, quantidade, unitario, total_item))
    total = sum(zero(x.preco_total) for x in itens)
    custo_mensal = None if prazo in (None, 0) else total / prazo
    return ResultadosOperacaoSistema(
        tuple(mao_obra), pessoas, refeicoes, transportes, custo_dia, memorial,
        prazo, dias, tuple(itens), total, custo_mensal,
    )
