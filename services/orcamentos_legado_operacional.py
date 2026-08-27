"""Roteamento seguro do estado mutável do fluxo legado de Orçamentos."""

import pandas as pd

from services.dados_operacionais import ler_csv_operacional, salvar_csv_operacional
from services.github import StatusLeitura, carregar_github as carregar_github_main


ARQUIVOS_OPERACIONAIS = frozenset({
    "data/orcamentos.csv",
    "data/clientes.csv",
    "data/insumos.csv",
})


def arquivo_operacional(caminho):
    return caminho in ARQUIVOS_OPERACIONAIS


def carregar_github(caminho, token, repo):
    if not arquivo_operacional(caminho):
        return carregar_github_main(caminho, token, repo)

    resultado = ler_csv_operacional(caminho, token, repo)
    if resultado.pode_sobrescrever:
        return resultado.dados
    if resultado.status == StatusLeitura.ARQUIVO_INEXISTENTE:
        return pd.DataFrame()
    raise RuntimeError(
        f"Leitura operacional de {caminho} não confirmada; operação bloqueada."
    )


def salvar_github(df, caminho, token, repo):
    if not arquivo_operacional(caminho):
        raise RuntimeError(
            f"Escrita de catálogo estrutural recusada pelo backend operacional: {caminho}."
        )

    leitura = ler_csv_operacional(caminho, token, repo)
    if leitura.pode_sobrescrever:
        resultado = salvar_csv_operacional(
            df,
            caminho,
            token,
            repo,
            sha_esperado=leitura.sha,
        )
    elif leitura.status == StatusLeitura.ARQUIVO_INEXISTENTE:
        resultado = salvar_csv_operacional(
            df,
            caminho,
            token,
            repo,
            criar=True,
        )
    else:
        raise RuntimeError(
            f"Leitura operacional de {caminho} não autorizou a escrita."
        )

    if not resultado.sucesso:
        raise RuntimeError(resultado.erro or f"Erro ao salvar {caminho}.")
    return resultado
