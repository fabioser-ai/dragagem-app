"""Autoridade RBAC efetiva para usuários operacionais.

Não consulta o modelo legado e nega quando qualquer fonte necessária não pode
ser confirmada. O escopo de obra pertence à associação Pessoa → Role.
"""

from dataclasses import dataclass

import pandas as pd
import streamlit as st

from services.github import ler_csv_github


ARQUIVOS = {
    "usuarios": "data/usuarios_operacionais.csv",
    "associacoes": "data/usuarios_roles.csv",
    "roles": "data/roles.csv",
    "matriz": "data/roles_permissoes.csv",
    "catalogo": "data/permissoes_catalogo.csv",
}
COLUNAS_OBRIGATORIAS = {
    "usuarios": {"usuario_id", "login", "ativo"},
    "associacoes": {"usuario_id", "role_id", "ativo"},
    "roles": {"role_id", "codigo", "ativo"},
    "matriz": {"role_id", "modulo", "recurso", "acao", "efeito"},
    "catalogo": {"modulo", "recurso", "acao", "escopo_obra", "ativo"},
}


@dataclass(frozen=True)
class DecisaoRBAC:
    permitido: bool
    codigo: str
    roles: tuple = ()
    origens: tuple = ()
    escopos: tuple = ()


def _texto(valor):
    return str(valor or "").strip().casefold()


def _ativo(valor):
    return _texto(valor) in {"sim", "s", "true", "1", "ativo"}


def _carregar_fontes():
    fontes = {}
    try:
        token = st.secrets["GITHUB_TOKEN"]
        repo = st.secrets["REPO"]
        for nome, arquivo in ARQUIVOS.items():
            resultado = ler_csv_github(arquivo, token, repo)
            if not resultado.leitura_confirmada:
                return None
            fontes[nome] = resultado.dados.fillna("").copy()
    except Exception:
        return None
    return fontes


def _fontes_validas(fontes):
    return isinstance(fontes, dict) and all(
        nome in fontes
        and isinstance(fontes[nome], pd.DataFrame)
        and colunas.issubset(fontes[nome].columns)
        for nome, colunas in COLUNAS_OBRIGATORIAS.items()
    )


def _contexto_usuario(fontes, usuario):
    login = _texto(usuario)
    identidades = fontes["usuarios"]
    encontrados = identidades[
        (identidades["login"].map(_texto) == login)
        & identidades["ativo"].map(_ativo).astype(bool)
    ]
    if len(encontrados) != 1:
        return None, DecisaoRBAC(False, "identidade_inexistente_ou_inativa")
    identidade = encontrados.iloc[0]
    associacoes = fontes["associacoes"]
    vinculos = associacoes[
        (associacoes["usuario_id"].astype(str) == str(identidade["usuario_id"]))
        & associacoes["ativo"].map(_ativo).astype(bool)
    ].copy()
    if vinculos.empty:
        return None, DecisaoRBAC(False, "sem_role_ativa")
    return (identidade, vinculos), None


def _concessoes_validas(fontes, vinculos):
    roles = fontes["roles"]
    matriz = fontes["matriz"]
    catalogo = fontes["catalogo"]
    catalogo_ativo = {
        (_texto(row["modulo"]), _texto(row["recurso"]), _texto(row["acao"])):
        _texto(row.get("escopo_obra", "nao")) == "sim"
        for _, row in catalogo[catalogo["ativo"].map(_ativo).astype(bool)].iterrows()
    }
    concessoes = []
    for _, vinculo in vinculos.iterrows():
        role_id = str(vinculo["role_id"])
        encontradas = roles[
            (roles["role_id"].astype(str) == role_id)
            & roles["ativo"].map(_ativo).astype(bool)
        ]
        if len(encontradas) != 1:
            continue
        role = encontradas.iloc[0]
        escopo = _texto(vinculo.get("obra_id", "")) or "todas"
        for _, permissao in matriz[
            matriz["role_id"].astype(str) == role_id
        ].iterrows():
            chave = tuple(_texto(permissao[item]) for item in ("modulo", "recurso", "acao"))
            if chave not in catalogo_ativo:
                continue
            concessoes.append({
                "chave": chave,
                "efeito": _texto(permissao["efeito"]),
                "role": str(role["codigo"]),
                "escopo": escopo,
                "exige_obra": catalogo_ativo[chave],
            })
    return concessoes


def _deny_aplicavel(deny, *, chave, escopo, exige_obra):
    if deny["chave"] != chave or deny["efeito"] != "deny":
        return False
    if not exige_obra:
        return True
    return deny["escopo"] in {"todas", escopo}


def _allow_efetivo(allow, concessoes):
    """Um deny vence somente a mesma permissão no escopo aplicável."""
    if allow["efeito"] != "allow":
        return False
    if allow["exige_obra"] and allow["escopo"] == "todas":
        # Um deny específico deixa outras obras acessíveis; somente deny global
        # elimina uma concessão global para fins de acesso ao módulo.
        return not any(
            item["chave"] == allow["chave"]
            and item["efeito"] == "deny"
            and item["escopo"] == "todas"
            for item in concessoes
        )
    return not any(
        _deny_aplicavel(
            item, chave=allow["chave"], escopo=allow["escopo"],
            exige_obra=allow["exige_obra"],
        )
        for item in concessoes
    )


def avaliar(*, usuario, modulo, recurso, acao, obra_id=None, fontes=None):
    fontes = _carregar_fontes() if fontes is None else fontes
    if not _fontes_validas(fontes):
        return DecisaoRBAC(False, "leitura_nao_confirmada")
    contexto, erro = _contexto_usuario(fontes, usuario)
    if erro:
        return erro
    _, vinculos = contexto
    chave = (_texto(modulo), _texto(recurso), _texto(acao))
    catalogo = fontes["catalogo"]
    reconhecidas = catalogo[
        catalogo["ativo"].map(_ativo).astype(bool)
        & (catalogo["modulo"].map(_texto) == chave[0])
        & (catalogo["recurso"].map(_texto) == chave[1])
        & (catalogo["acao"].map(_texto) == chave[2])
    ]
    if len(reconhecidas) != 1:
        return DecisaoRBAC(False, "permissao_desconhecida")
    exige_obra = _texto(reconhecidas.iloc[0].get("escopo_obra", "nao")) == "sim"
    solicitada = _texto(obra_id) or "todas"
    candidatas = []
    for item in _concessoes_validas(fontes, vinculos):
        if item["chave"] != chave:
            continue
        if exige_obra and item["escopo"] not in {"todas", solicitada}:
            continue
        candidatas.append(item)
    if not candidatas:
        codigo = "escopo_incompativel" if exige_obra else "nao_concedida"
        return DecisaoRBAC(False, codigo)
    if any(item["efeito"] == "deny" for item in candidatas):
        return DecisaoRBAC(False, "negada_explicitamente")
    permitidas = [item for item in candidatas if item["efeito"] == "allow"]
    if not permitidas:
        return DecisaoRBAC(False, "nao_concedida")
    roles = tuple(sorted({item["role"] for item in permitidas}))
    escopos = tuple(sorted({item["escopo"] for item in permitidas}))
    origens = tuple(f"{item['role']}@{item['escopo']}" for item in permitidas)
    return DecisaoRBAC(True, "concedida", roles, tuple(sorted(set(origens))), escopos)


def avaliar_modulo(*, usuario, modulo, fontes=None):
    fontes = _carregar_fontes() if fontes is None else fontes
    if not _fontes_validas(fontes):
        return DecisaoRBAC(False, "leitura_nao_confirmada")
    contexto, erro = _contexto_usuario(fontes, usuario)
    if erro:
        return erro
    _, vinculos = contexto
    candidatas = [
        item for item in _concessoes_validas(fontes, vinculos)
        if item["chave"][0] == _texto(modulo)
    ]
    permitidas = [item for item in candidatas if _allow_efetivo(item, candidatas)]
    if not permitidas:
        return DecisaoRBAC(False, "modulo_nao_concedido")
    roles = tuple(sorted({item["role"] for item in permitidas}))
    return DecisaoRBAC(True, "concedida", roles)


def listar_obras(*, usuario, modulo, recurso, acao, fontes=None):
    fontes = _carregar_fontes() if fontes is None else fontes
    if not _fontes_validas(fontes):
        return []
    contexto, erro = _contexto_usuario(fontes, usuario)
    if erro:
        return []
    _, vinculos = contexto
    chave = (_texto(modulo), _texto(recurso), _texto(acao))
    itens = [item for item in _concessoes_validas(fontes, vinculos) if item["chave"] == chave]
    allows = [item for item in itens if item["efeito"] == "allow"]
    denies = [item for item in itens if item["efeito"] == "deny"]
    if any(item["escopo"] == "todas" for item in denies):
        return []
    negados = sorted({item["escopo"] for item in denies})
    if any(item["escopo"] == "todas" for item in allows):
        # Representa de modo explícito o conjunto "todas, exceto ...".
        return ["todas", *(f"!{escopo}" for escopo in negados)]
    permitidos = sorted({
        item["escopo"] for item in allows
        if item["escopo"] not in set(negados)
    })
    return permitidos


def listar_permissoes(*, usuario, fontes=None):
    fontes = _carregar_fontes() if fontes is None else fontes
    if not _fontes_validas(fontes):
        return []
    contexto, erro = _contexto_usuario(fontes, usuario)
    if erro:
        return []
    _, vinculos = contexto
    return [item for item in _concessoes_validas(fontes, vinculos) if item["efeito"] == "allow"]
