"""Fotografia e quatro relações da aba Produção do Excel oficial."""

from dataclasses import dataclass


def _numero_nao_negativo(valor, campo):
    if valor is not None and (
        isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor < 0
    ):
        raise ValueError(f"{campo} deve ser numérico não negativo ou vazio.")
    return float(valor) if valor is not None else None


@dataclass(frozen=True, slots=True)
class Producao:
    vazao: float | None = 120.0
    eficiencia: float | None = 60.0
    concentracao: float | None = 15.0

    def __post_init__(self):
        for campo in ("vazao", "eficiencia", "concentracao"):
            object.__setattr__(
                self,
                campo,
                _numero_nao_negativo(getattr(self, campo), campo),
            )


@dataclass(frozen=True, slots=True)
class ResultadosProducao:
    producao_horaria: float | None
    horas_mensais: float | None
    producao_mensal: float | None
    prazo_meses: float | None


def calcular_producao(
    producao: Producao,
    horas_por_dia: float | None,
    dias_por_mes: float | None,
    volume_total: float | None,
) -> ResultadosProducao:
    """Reproduz D8, H6, D13 e D24 sem persistir resultados derivados."""
    entradas = (producao.vazao, producao.eficiencia, producao.concentracao)
    producao_horaria = None
    if all(valor is not None for valor in entradas):
        producao_horaria = (
            producao.vazao
            * (producao.eficiencia / 100)
            * (producao.concentracao / 100)
        )

    horas_mensais = None
    if horas_por_dia is not None and dias_por_mes is not None:
        horas_mensais = horas_por_dia * dias_por_mes

    producao_mensal = None
    if producao_horaria is not None and horas_mensais is not None:
        producao_mensal = producao_horaria * horas_mensais

    prazo_meses = None
    if (
        volume_total is not None
        and volume_total > 0
        and producao_mensal is not None
        and producao_mensal > 0
    ):
        prazo_meses = volume_total / producao_mensal

    return ResultadosProducao(
        producao_horaria,
        horas_mensais,
        producao_mensal,
        prazo_meses,
    )
