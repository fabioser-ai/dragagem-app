from unittest.mock import Mock, patch

import pandas as pd

from services.github import ler_csv_github, salvar_csv_github


ARQUIVOS_FERIAS = ("data/ferias.csv", "data/folgas.csv")
DATA_BRANCH = "data-operacional"


def test_leitura_de_ferias_e_folgas_usa_branch_operacional():
    resposta = Mock(status_code=404, headers={})
    with patch("services.github.requests.get", return_value=resposta) as get:
        for arquivo in ARQUIVOS_FERIAS:
            ler_csv_github(arquivo, "token", "repo")
            assert get.call_args.kwargs["params"] == {"ref": DATA_BRANCH}


def test_escrita_de_ferias_e_folgas_usa_branch_operacional():
    resposta = Mock(status_code=200)
    resposta.json.return_value = {"content": {"sha": "novo"}}
    with patch("services.github.requests.put", return_value=resposta) as put:
        for arquivo in ARQUIVOS_FERIAS:
            salvar_csv_github(
                pd.DataFrame([{"a": 1}]),
                arquivo,
                "token",
                "repo",
                sha_esperado="sha-lido",
            )
            assert put.call_args.kwargs["json"]["branch"] == DATA_BRANCH


def test_demais_arquivos_mantem_comportamento_padrao():
    resposta_get = Mock(status_code=404, headers={})
    with patch("services.github.requests.get", return_value=resposta_get) as get:
        ler_csv_github("data/outro.csv", "token", "repo")
        assert "params" not in get.call_args.kwargs

    resposta_put = Mock(status_code=200)
    resposta_put.json.return_value = {"content": {"sha": "novo"}}
    with patch("services.github.requests.put", return_value=resposta_put) as put:
        salvar_csv_github(
            pd.DataFrame([{"a": 1}]),
            "data/outro.csv",
            "token",
            "repo",
            sha_esperado="sha-lido",
        )
        assert "branch" not in put.call_args.kwargs["json"]
