"""Índice CSV mínimo, sem detalhes de domínio."""

import csv
import io
from dataclasses import dataclass

from modulos.orcamentos.dominio.estados import EstadoVersao
from modulos.orcamentos.dominio.modelos import Orcamento, VersaoOrcamento
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia

CAMPOS_INDICE = (
    "orcamento_id", "versao_id", "numero", "objeto",
    "finalidade", "responsavel", "estado",
)


@dataclass(frozen=True, slots=True)
class ResumoIndice:
    orcamento_id: str
    versao_id: str
    numero: int
    objeto: str
    finalidade: str
    responsavel: str
    estado: str


def resumo_de(orcamento: Orcamento, versao: VersaoOrcamento) -> ResumoIndice:
    return ResumoIndice(
        str(orcamento.id), str(versao.id), versao.numero, orcamento.objeto,
        orcamento.finalidade, orcamento.responsavel, versao.estado.value,
    )


def serializar_indice(resumos: list[ResumoIndice]) -> str:
    saida = io.StringIO(newline="")
    escritor = csv.DictWriter(saida, fieldnames=CAMPOS_INDICE, lineterminator="\n")
    escritor.writeheader()
    for resumo in resumos:
        escritor.writerow({campo: getattr(resumo, campo) for campo in CAMPOS_INDICE})
    return saida.getvalue()


def desserializar_indice(conteudo: str) -> ResultadoPersistencia[list[ResumoIndice]]:
    try:
        leitor = csv.DictReader(io.StringIO(conteudo))
        if tuple(leitor.fieldnames or ()) != CAMPOS_INDICE:
            return ResultadoPersistencia(
                StatusPersistencia.DADO_CORROMPIDO, erro="Cabeçalho do índice inválido."
            )
        resumos = []
        vistos = set()
        for linha in leitor:
            if None in linha or any(valor is None or not str(valor).strip() for valor in linha.values()):
                raise ValueError
            numero = int(linha["numero"])
            EstadoVersao(linha["estado"])
            if numero < 1 or linha["orcamento_id"] in vistos:
                raise ValueError
            vistos.add(linha["orcamento_id"])
            resumos.append(ResumoIndice(
                linha["orcamento_id"], linha["versao_id"], numero,
                linha["objeto"], linha["finalidade"], linha["responsavel"], linha["estado"],
            ))
        return ResultadoPersistencia(StatusPersistencia.SUCESSO, resumos)
    except (TypeError, ValueError, csv.Error):
        return ResultadoPersistencia(
            StatusPersistencia.DADO_CORROMPIDO, erro="Conteúdo do índice inválido."
        )


def atualizar_resumo(resumos: list[ResumoIndice], novo: ResumoIndice) -> list[ResumoIndice]:
    atualizados = [item for item in resumos if item.orcamento_id != novo.orcamento_id]
    atualizados.append(novo)
    return atualizados
