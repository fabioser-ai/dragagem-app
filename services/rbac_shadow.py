"""Cálculo diagnóstico do RBAC, isolado da autorização efetiva do APP."""

from dataclasses import dataclass

import pandas as pd


CHAVE = ("modulo", "recurso", "acao")


def _texto(valor):
    return str(valor or "").strip().casefold()


def _ativo(valor):
    return _texto(valor) in {"sim", "s", "true", "1", "ativo"}


def _df(dados, colunas):
    if dados is None:
        base = pd.DataFrame()
    elif isinstance(dados, pd.DataFrame):
        base = dados.copy()
    else:
        base = pd.DataFrame(dados)
    for coluna in colunas:
        if coluna not in base.columns:
            base[coluna] = ""
    return base.fillna("")


def _chave(linha, *, campo_acao="acao"):
    return (
        _texto(linha["modulo"]),
        _texto(linha["recurso"]),
        _texto(linha[campo_acao]),
    )


def _formatar(permissoes):
    return [" / ".join(item) for item in sorted(permissoes)]


@dataclass(frozen=True)
class DiagnosticoUsuario:
    usuario_id: str
    login: str
    nome: str
    roles: tuple
    permissoes_atuais: tuple
    permissoes_rbac: tuple
    rbac_a_mais: tuple
    rbac_a_menos: tuple
    ocorrencias: tuple
    status: str


def calcular_usuario(
    *, usuario, associacoes, roles, roles_permissoes,
    catalogo_permissoes, permissoes_atuais,
):
    """Calcula e compara snapshots sem consultar sessão ou conceder acesso."""
    usuario_id = str(usuario.get("usuario_id", ""))
    login = str(usuario.get("login", ""))
    associacoes = _df(associacoes, ("usuario_id", "role_id", "ativo"))
    roles = _df(roles, ("role_id", "codigo", "ativo"))
    matriz = _df(roles_permissoes, ("role_id", "modulo", "recurso", "acao", "efeito"))
    catalogo = _df(catalogo_permissoes, (*CHAVE, "ativo"))
    atuais = _df(
        permissoes_atuais,
        ("usuario", "modulo", "recurso", "permissao", "obra_id", "ativo"),
    )

    vinculos = associacoes[
        (associacoes["usuario_id"].astype(str) == usuario_id)
        & associacoes["ativo"].map(_ativo).astype(bool)
    ]
    atuais_usuario = atuais[
        (atuais["usuario"].map(_texto) == _texto(login))
        & atuais["ativo"].map(_ativo).astype(bool)
    ]
    chaves_atuais = {
        _chave(linha, campo_acao="permissao")
        for _, linha in atuais_usuario.iterrows()
    }
    catalogo_ativo = {
        _chave(linha)
        for _, linha in catalogo[catalogo["ativo"].map(_ativo).astype(bool)].iterrows()
    }

    codigos_roles = []
    chaves_rbac = set()
    ocorrencias = []
    roles_validas = 0
    roles_vazias = 0

    if vinculos.empty:
        ocorrencias.append("Usuário sem Role")

    for _, vinculo in vinculos.iterrows():
        role_id = str(vinculo["role_id"])
        encontrada = roles[
            (roles["role_id"].astype(str) == role_id)
            & roles["ativo"].map(_ativo).astype(bool)
        ]
        if len(encontrada) != 1:
            ocorrencias.append(f"Role inexistente: {role_id}")
            continue
        roles_validas += 1
        codigo = str(encontrada.iloc[0]["codigo"])
        codigos_roles.append(codigo)
        concessoes = matriz[
            (matriz["role_id"].astype(str) == role_id)
            & (matriz["efeito"].map(_texto) == "allow")
        ]
        if concessoes.empty:
            roles_vazias += 1
            ocorrencias.append(f"Role vazia: {codigo}")
            continue
        for _, permissao in concessoes.iterrows():
            chave = _chave(permissao)
            if chave not in catalogo_ativo:
                ocorrencias.append(f"Permissão inexistente: {' / '.join(chave)}")
                continue
            chaves_rbac.add(chave)

    a_mais = chaves_rbac - chaves_atuais
    a_menos = chaves_atuais - chaves_rbac
    if a_mais:
        ocorrencias.append("RBAC possui permissões a mais")
    if a_menos:
        ocorrencias.append("RBAC possui permissões a menos")

    if vinculos.empty:
        status = "SEM ROLE"
    elif roles_validas == len(vinculos) and roles_validas == roles_vazias:
        status = "ROLE VAZIA"
    elif not ocorrencias and chaves_rbac == chaves_atuais:
        status = "IGUAL"
    else:
        status = "DIVERGENTE"

    return DiagnosticoUsuario(
        usuario_id=usuario_id,
        login=login,
        nome=str(usuario.get("nome", "")),
        roles=tuple(sorted(set(codigos_roles))),
        permissoes_atuais=tuple(_formatar(chaves_atuais)),
        permissoes_rbac=tuple(_formatar(chaves_rbac)),
        rbac_a_mais=tuple(_formatar(a_mais)),
        rbac_a_menos=tuple(_formatar(a_menos)),
        ocorrencias=tuple(dict.fromkeys(ocorrencias)),
        status=status,
    )


def diagnosticar_usuarios(
    *, usuarios, associacoes, roles, roles_permissoes,
    catalogo_permissoes, permissoes_atuais,
):
    """Compara todos os usuários operacionais; não escreve nem altera estado."""
    usuarios = _df(usuarios, ("usuario_id", "login", "nome"))
    return [
        calcular_usuario(
            usuario=linha,
            associacoes=associacoes,
            roles=roles,
            roles_permissoes=roles_permissoes,
            catalogo_permissoes=catalogo_permissoes,
            permissoes_atuais=permissoes_atuais,
        )
        for _, linha in usuarios.iterrows()
    ]
