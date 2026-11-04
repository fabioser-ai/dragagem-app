"""Adaptadores somente leitura para a futura composição de orçamento.

Nenhuma leitura é feita na importação. Falhas e arquivos ausentes NÃO são
interpretados como cadastros vazios. Não consulta o cadastro legado de clientes.
A autorização da tela chamadora deve ser verificada antes da leitura.
"""
from dataclasses import dataclass
from typing import Optional

import pandas as pd

from pages.crm.config import COLUNAS_CLIENTES, COLUNAS_CONTATOS
from services.dados_operacionais import ler_csv_operacional
from services.github import StatusLeitura


FONTES = {
    "clientes": ("data/crm/clientes.csv", tuple(COLUNAS_CLIENTES)),
    "contatos": ("data/crm/contatos.csv", tuple(COLUNAS_CONTATOS)),
    "materiais": ("data/materiais.csv", ("Material", "Solidos_InSitu", "Solidos_Desaguado")),
    "horarios": ("data/horarios.csv", ("Inicio", "Fim")),
    "regimes": ("data/dias.csv", ("Descricao",)),
}


@dataclass(frozen=True)
class LeituraCatalogo:
    fonte: str
    arquivo: str
    disponivel: bool
    dados: pd.DataFrame
    status: str
    erro: Optional[str] = None
    sha: Optional[str] = None


def consultar_catalogo(fonte: str, token: str, repo: str) -> LeituraCatalogo:
    """Consulta catálogo operacional, preservando erro, vazio real e SHA."""
    if fonte not in FONTES:
        raise ValueError("Fonte de catálogo não reconhecida.")
    arquivo, colunas = FONTES[fonte]
    resultado = ler_csv_operacional(arquivo, token, repo)
    status = resultado.status.value
    vazio = pd.DataFrame(columns=list(colunas))
    if resultado.status not in {StatusLeitura.SUCESSO_COM_DADOS, StatusLeitura.SUCESSO_VAZIO}:
        return LeituraCatalogo(fonte, arquivo, False, vazio, status,
                              resultado.erro or "Leitura não confirmada.", resultado.sha)
    dados = resultado.dados
    if dados is None:
        return LeituraCatalogo(fonte, arquivo, False, vazio, status,
                              "Resposta sem DataFrame.", resultado.sha)
    faltantes = [col for col in colunas if col not in dados.columns]
    if faltantes:
        return LeituraCatalogo(fonte, arquivo, False, vazio, status,
                              "Colunas obrigatórias ausentes: " + ", ".join(faltantes),
                              resultado.sha)
    dados = dados.loc[:, list(colunas)].copy().fillna("").astype(str)
    return LeituraCatalogo(fonte, arquivo, True, dados, status, sha=resultado.sha)


def contatos_do_cliente(clientes: LeituraCatalogo, contatos: LeituraCatalogo,
                        id_cliente: str) -> pd.DataFrame:
    """Filtra por ID estável; falha fechada se as fontes não estiverem válidas."""
    if not clientes.disponivel or not contatos.disponivel:
        raise ValueError("Cadastros CRM indisponíveis; não é seguro selecionar contato.")
    if not id_cliente or id_cliente not in set(clientes.dados["id_cliente"]):
        raise ValueError("Cliente não encontrado no CRM.")
    return contatos.dados.loc[
        contatos.dados["id_cliente"] == id_cliente
    ].copy().reset_index(drop=True)


def listar_opcoes(catalogo: LeituraCatalogo, coluna: str) -> list[str]:
    """Extrai opções de uma coluna já validada, sem fabricar alternativas."""
    if not catalogo.disponivel:
        raise ValueError("Cadastro indisponível.")
    if coluna not in catalogo.dados.columns:
        raise ValueError("Coluna não disponível no catálogo.")
    return sorted(set(v.strip() for v in catalogo.dados[coluna] if v.strip()),
                  key=str.casefold)
