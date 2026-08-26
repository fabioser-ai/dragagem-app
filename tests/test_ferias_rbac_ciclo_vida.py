from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
CATALOGO = ROOT / "data" / "permissoes_catalogo.csv"
ROLES = ROOT / "data" / "roles.csv"
MATRIZ = ROOT / "data" / "roles_permissoes.csv"
FERIAS = ROOT / "pages" / "ferias.py"


def test_ciclo_vida_ferias_existe_no_catalogo_canonico():
    catalogo = pd.read_csv(CATALOGO)
    linha = catalogo[
        (catalogo["modulo"] == "ferias")
        & (catalogo["recurso"] == "ciclo_vida")
        & (catalogo["acao"] == "alterar")
        & (catalogo["ativo"] == "sim")
    ]
    assert len(linha) == 1


def test_role_rh_concede_ciclo_vida_ferias():
    roles = pd.read_csv(ROLES)
    matriz = pd.read_csv(MATRIZ)
    rh = roles.loc[roles["codigo"] == "RH", "role_id"]
    assert len(rh) == 1

    concessao = matriz[
        (matriz["role_id"] == rh.iloc[0])
        & (matriz["modulo"] == "ferias")
        & (matriz["recurso"] == "ciclo_vida")
        & (matriz["acao"] == "alterar")
        & (matriz["efeito"] == "allow")
    ]
    assert len(concessao) == 1


def test_tela_revalida_mesma_capacidade_no_ponto_sensivel():
    codigo = FERIAS.read_text(encoding="utf-8")
    assert 'pode(modulo="ferias", recurso="ciclo_vida", acao="alterar")' in codigo
