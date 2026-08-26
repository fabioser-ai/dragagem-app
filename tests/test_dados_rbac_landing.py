from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
CATALOGO = ROOT / "data" / "permissoes_catalogo.csv"
ROLES = ROOT / "data" / "roles.csv"
MATRIZ = ROOT / "data" / "roles_permissoes.csv"
HUB = ROOT / "pages" / "dados_hub.py"
APP = ROOT / "app.py"


def test_app_usa_landing_autorizada_de_dados():
    codigo = APP.read_text(encoding="utf-8")
    assert "from pages import dados_hub" in codigo
    assert "dados_hub.render()" in codigo


def test_landing_so_exibe_recurso_com_visualizar():
    codigo = HUB.read_text(encoding="utf-8")
    assert '_permitido(cfg["recurso"], "visualizar")' in codigo
    assert 'if not _permitido(recurso, "visualizar")' in codigo


def test_crud_segrega_criar_editar_excluir():
    codigo = HUB.read_text(encoding="utf-8")
    for acao in ("criar", "editar", "excluir"):
        assert f'_permitido(recurso, "{acao}")' in codigo
        assert f'_salvar(candidato, cfg, leitura, "{acao}")' in codigo


def test_salario_tem_quatro_capacidades_canonicas():
    catalogo = pd.read_csv(CATALOGO, dtype=str).fillna("")
    salario = catalogo[
        (catalogo["modulo"] == "dados") & (catalogo["recurso"] == "salario")
    ]
    assert set(salario["acao"]) == {"visualizar", "criar", "editar", "excluir"}
    assert (salario["ativo"] == "sim").all()


def test_rh_ve_atestado_e_salario_sem_escrita_em_salario():
    roles = pd.read_csv(ROLES, dtype=str).fillna("")
    matriz = pd.read_csv(MATRIZ, dtype=str).fillna("")
    rh = roles.loc[roles["codigo"] == "RH", "role_id"]
    assert len(rh) == 1
    permissoes = matriz[matriz["role_id"] == rh.iloc[0]]

    assert ((permissoes["modulo"] == "dados") &
            (permissoes["recurso"] == "atestado") &
            (permissoes["acao"] == "visualizar") &
            (permissoes["efeito"] == "allow")).any()
    assert ((permissoes["modulo"] == "dados") &
            (permissoes["recurso"] == "salario") &
            (permissoes["acao"] == "visualizar") &
            (permissoes["efeito"] == "allow")).any()

    salario = permissoes[
        (permissoes["modulo"] == "dados") & (permissoes["recurso"] == "salario")
    ]
    assert set(salario["acao"]) == {"visualizar"}


def test_rh_nao_recebe_cadastro_generico():
    roles = pd.read_csv(ROLES, dtype=str).fillna("")
    matriz = pd.read_csv(MATRIZ, dtype=str).fillna("")
    rh_id = roles.loc[roles["codigo"] == "RH", "role_id"].iloc[0]
    permissoes = matriz[matriz["role_id"] == rh_id]
    assert not ((permissoes["modulo"] == "dados") &
                (permissoes["recurso"] == "cadastro")).any()
