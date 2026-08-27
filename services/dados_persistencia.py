import pandas as pd

from services.github import (
    ResultadoEscritaCSV,
    ResultadoLeituraCSV,
    StatusEscrita,
    StatusLeitura,
)
from services.dados_operacionais import ler_csv_operacional, salvar_csv_operacional


# Compatibilidade de testabilidade: preserva os nomes históricos usados pelos
# testes/mocks, mas a implementação real continua apontando para a branch
# operacional separada da main.
def ler_csv_github(arquivo, token, repo):
    return ler_csv_operacional(arquivo, token, repo)


def salvar_csv_github(
    df,
    arquivo,
    token,
    repo,
    *,
    sha_esperado=None,
    criar=False,
    mensagem=None,
):
    return salvar_csv_operacional(
        df,
        arquivo,
        token,
        repo,
        sha_esperado=sha_esperado,
        criar=criar,
        mensagem=mensagem,
    )


def normalizar_dataframe(df, colunas):
    if df is None:
        df = pd.DataFrame(columns=colunas)

    df = df.copy()

    for coluna in colunas:
        if coluna not in df.columns:
            df[coluna] = ""

    return df[colunas]


def carregar_cadastro_resultado(arquivo, colunas, token, repo):
    resultado = ler_csv_github(arquivo, token, repo)

    dados = (
        normalizar_dataframe(resultado.dados, colunas)
        if resultado.leitura_confirmada
        else pd.DataFrame(columns=colunas)
    )

    return ResultadoLeituraCSV(
        status=resultado.status,
        dados=dados,
        arquivo=resultado.arquivo,
        http_status=resultado.http_status,
        sha=resultado.sha,
        erro=resultado.erro,
        rate_limit_limit=resultado.rate_limit_limit,
        rate_limit_remaining=resultado.rate_limit_remaining,
        rate_limit_reset=resultado.rate_limit_reset,
        retry_after=resultado.retry_after,
    )


def salvar_cadastro_seguro(
    df,
    arquivo,
    colunas,
    token,
    repo,
    *,
    resultado_leitura,
    mensagem=None,
):
    dados = normalizar_dataframe(df, colunas)

    if resultado_leitura.status in {
        StatusLeitura.SUCESSO_COM_DADOS,
        StatusLeitura.SUCESSO_VAZIO,
    }:
        return salvar_csv_github(
            dados,
            arquivo,
            token,
            repo,
            sha_esperado=resultado_leitura.sha,
            mensagem=mensagem,
        )

    if resultado_leitura.status == StatusLeitura.ARQUIVO_INEXISTENTE:
        return salvar_csv_github(
            dados,
            arquivo,
            token,
            repo,
            criar=True,
            mensagem=mensagem,
        )

    return ResultadoEscritaCSV(
        status=StatusEscrita.REQUISICAO_INVALIDA,
        arquivo=arquivo,
        erro="A leitura não autorizou a escrita do cadastro.",
    )
