"""Consultas puras do painel de Orçamentos."""

from collections.abc import Iterable

from modulos.orcamentos.persistencia.indice import ResumoIndice


def filtrar_resumos(
    resumos: Iterable[ResumoIndice],
    *,
    busca: str = "",
    estado: str = "",
) -> list[ResumoIndice]:
    """Filtra o índice já carregado, sem qualquer acesso remoto."""

    termo = busca.strip().casefold()
    estado_normalizado = estado.strip().casefold()

    filtrados = []
    for resumo in resumos:
        campos = (
            resumo.objeto,
            resumo.finalidade,
            resumo.responsavel,
            resumo.orcamento_id,
            resumo.versao_id,
        )
        if termo and not any(termo in str(valor).casefold() for valor in campos):
            continue
        if estado_normalizado and resumo.estado.casefold() != estado_normalizado:
            continue
        filtrados.append(resumo)

    return sorted(
        filtrados,
        key=lambda item: (item.objeto.casefold(), item.numero, item.versao_id),
    )
