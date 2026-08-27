import importlib
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import pandas as pd

from services.github import StatusEscrita, StatusLeitura
from services import prestacao_contas_operacional as operacional


ROOT = Path(__file__).resolve().parents[1]


def carregar_pagina():
    st = types.ModuleType("streamlit")
    st.secrets = {"GITHUB_TOKEN": "token-teste", "REPO": "repo-teste"}
    st.session_state = {"autenticado": True, "usuario": "usuario-teste"}
    with patch.dict(sys.modules, {"streamlit": st}):
        sys.modules.pop("pages.prestacao_contas", None)
        return importlib.import_module("pages.prestacao_contas")


def test_csvs_da_prestacao_usam_leitura_operacional():
    pagina = carregar_pagina()
    vazio_tipos = pd.DataFrame(columns=pagina.COLUNAS_TIPOS)
    vazio_despesas = pd.DataFrame(columns=pagina.COLUNAS_DESPESAS)

    with patch.object(
        pagina,
        "carregar_csv_operacional",
        side_effect=(vazio_tipos, vazio_despesas),
    ) as carregar:
        pagina.carregar_tipos()
        pagina.carregar_despesas()

    assert [chamada.args[0] for chamada in carregar.call_args_list] == [
        pagina.ARQ_TIPOS,
        pagina.ARQ_DESPESAS,
    ]


def test_aliases_legados_de_escrita_e_binarios_apontam_para_backend_operacional():
    pagina = carregar_pagina()

    assert pagina.salvar_github is operacional.salvar_csv
    assert pagina.salvar_arquivo_github is operacional.salvar_arquivo
    assert pagina.carregar_arquivo_github is operacional.carregar_arquivo


def test_csv_da_prestacao_e_salvo_na_branch_operacional():
    leitura = Mock(
        pode_sobrescrever=True,
        sha="sha-atual",
        status=StatusLeitura.SUCESSO_COM_DADOS,
    )
    escrita = Mock(sucesso=True, status=StatusEscrita.SUCESSO_ATUALIZADO)

    with patch.object(operacional, "ler_csv_operacional", return_value=leitura), patch.object(
        operacional, "salvar_csv_operacional", return_value=escrita
    ) as salvar:
        assert operacional.salvar_csv(
            pd.DataFrame([{"ID": "1"}]),
            "data/prestacao_contas.csv",
            "token",
            "owner/repo",
        )

    salvar.assert_called_once()
    assert salvar.call_args.args[1] == "data/prestacao_contas.csv"
    assert salvar.call_args.kwargs["sha_esperado"] == "sha-atual"


def test_tipos_de_despesa_sao_salvos_na_branch_operacional():
    leitura = Mock(
        pode_sobrescrever=True,
        sha="sha-atual",
        status=StatusLeitura.SUCESSO_COM_DADOS,
    )
    escrita = Mock(sucesso=True, status=StatusEscrita.SUCESSO_ATUALIZADO)

    with patch.object(operacional, "ler_csv_operacional", return_value=leitura), patch.object(
        operacional, "salvar_csv_operacional", return_value=escrita
    ) as salvar:
        assert operacional.salvar_csv(
            pd.DataFrame([{"Tipo_Despesa": "Táxi"}]),
            "data/tipos_despesa.csv",
            "token",
            "owner/repo",
        )

    assert salvar.call_args.args[1] == "data/tipos_despesa.csv"
    assert salvar.call_args.kwargs["sha_esperado"] == "sha-atual"


def test_upload_de_comprovante_informa_branch_operacional():
    inexistente = Mock(status_code=404)
    salvo = Mock(status_code=201)

    with patch.object(operacional.requests, "get", return_value=inexistente) as get, patch.object(
        operacional.requests, "put", return_value=salvo
    ) as put:
        caminho = operacional.salvar_arquivo(
            b"pdf", "data/comprovantes/nota.pdf", "token", "owner/repo"
        )

    assert caminho == "data/comprovantes/nota.pdf"
    assert get.call_args.kwargs["params"] == {"ref": operacional.DATA_BRANCH}
    assert put.call_args.kwargs["json"]["branch"] == operacional.DATA_BRANCH
    assert operacional.DATA_BRANCH != "main"


def test_leitura_de_comprovante_informa_branch_operacional():
    resposta = Mock(
        status_code=200,
    )
    resposta.json.return_value = {"content": "cGRm"}

    with patch.object(operacional.requests, "get", return_value=resposta) as get:
        assert operacional.carregar_arquivo(
            "data/comprovantes/nota.pdf", "token", "owner/repo"
        ) == b"pdf"

    assert get.call_args.kwargs["params"] == {"ref": operacional.DATA_BRANCH}


def test_pagina_nao_importa_escritas_genericas_do_github():
    fonte = (ROOT / "pages" / "prestacao_contas.py").read_text(encoding="utf-8")

    assert "from services.github import (" not in fonte
    assert fonte.count("salvar_github(") == 5


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for teste in (
        test_csvs_da_prestacao_usam_leitura_operacional,
        test_aliases_legados_de_escrita_e_binarios_apontam_para_backend_operacional,
        test_csv_da_prestacao_e_salvo_na_branch_operacional,
        test_tipos_de_despesa_sao_salvos_na_branch_operacional,
        test_upload_de_comprovante_informa_branch_operacional,
        test_leitura_de_comprovante_informa_branch_operacional,
        test_pagina_nao_importa_escritas_genericas_do_github,
    ):
        suite.addTest(unittest.FunctionTestCase(teste))
    return suite
