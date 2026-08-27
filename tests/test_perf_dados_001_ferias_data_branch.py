from pathlib import Path


def test_ferias_folgas_usam_branch_operacional():
    fonte = Path("pages/ferias.py").read_text()
    assert "ler_csv_operacional(arquivo, TOKEN, REPO)" in fonte
    assert "salvar_csv_operacional(" in fonte
    assert "from services.dados_operacionais import" in fonte


def test_ferias_folgas_nao_persistem_diretamente_na_main():
    fonte = Path("pages/ferias.py").read_text()
    assert "salvar_csv_github(" not in fonte
