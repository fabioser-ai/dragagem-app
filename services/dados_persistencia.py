import pandas as pd

from services.github import (
    ResultadoEscritaCSV,
    ResultadoLeituraCSV,
    StatusEscrita,
    StatusLeitura,
    ler_csv_github,
    salvar_csv_github,
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
