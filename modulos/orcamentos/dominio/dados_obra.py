"""Valores da aba ``Dados Obra`` do modelo oficial SABESP."""

from dataclasses import dataclass, fields
from datetime import date


@dataclass(frozen=True, slots=True)
class DadosObra:
    proposta: str = "Proposta D_055_2021"
    data: date = date(2021, 5, 28)
    cliente: str = "SABESP - CUBATAO ETA 3"
    contato: str = ""
    email: str = ""
    objeto: str = "Dragagem ETEL ETA3"
    local: str = "CUBATAO"
    volume_dragagem: float | None = 5000.0
    tipo_material: str = "Areia + Lodo + Antracito"
    distancia_recalque: float | None = 200.0
    seio_recalque: float | None = 0.0
    linha_flutuante: float | None = 100.0
    seio_linha_flutuante: float | None = 0.0
    linha_terra: float | None = 100.0
    profundidade_dragagem: float | None = None
    espessura_media: float | None = None
    area_comprimento: float | None = None
    area_largura: float | None = None
    tipo_bota_fora: str = "Bag"
    sistema_medicao: str = "preços unitários de serviços"
    canteiro_obras: str = "FOS"
    mobilizacao: str = "FOS"
    horario_trabalho: float | None = 9.0
    dias_trabalho: float | None = 22.0

    def __post_init__(self):
        for campo in fields(self):
            valor = getattr(self, campo.name)
            if campo.name == "data":
                if not isinstance(valor, date):
                    raise ValueError("data deve ser uma data válida.")
            elif campo.name in CAMPOS_NUMERICOS:
                if valor is not None and (
                    isinstance(valor, bool) or not isinstance(valor, (int, float))
                ):
                    raise ValueError(f"{campo.name} deve ser numérico ou vazio.")
            elif not isinstance(valor, str):
                raise ValueError(f"{campo.name} deve ser texto.")

    @staticmethod
    def _somar(primeiro: float | None, segundo: float | None) -> float:
        return (primeiro or 0.0) + (segundo or 0.0)

    @property
    def total_recalque(self) -> float:
        """Equivale a ``H16 = B16 + E16``."""
        return self._somar(self.distancia_recalque, self.seio_recalque)

    @property
    def total_linha_flutuante(self) -> float:
        """Equivale a ``H17 = B17 + E17``."""
        return self._somar(self.linha_flutuante, self.seio_linha_flutuante)

    @property
    def volume_geometrico(self) -> float:
        """Equivale a ``G21 = B21 * D21 * B20``."""
        return (
            (self.area_comprimento or 0.0)
            * (self.area_largura or 0.0)
            * (self.espessura_media or 0.0)
        )


CAMPOS_NUMERICOS = frozenset(
    {
        "volume_dragagem",
        "distancia_recalque",
        "seio_recalque",
        "linha_flutuante",
        "seio_linha_flutuante",
        "linha_terra",
        "profundidade_dragagem",
        "espessura_media",
        "area_comprimento",
        "area_largura",
        "horario_trabalho",
        "dias_trabalho",
    }
)
