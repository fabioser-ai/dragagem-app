from datetime import datetime
from math import isfinite
from uuid import uuid4

import pandas as pd


ARQ_ITENS = "data/uniformes_epis_itens.csv"
ARQ_COMPRAS = "data/uniformes_epis_compras.csv"
ARQ_MOVIMENTACOES = "data/uniformes_epis_movimentacoes.csv"
ARQ_ENTREGAS = "data/uniformes_epis_entregas.csv"

COLUNAS_ITENS = [
    "item_id",
    "categoria",
    "nome",
    "descricao",
    "tamanho",
    "ca",
    "unidade",
    "ativo",
    "observacoes",
    "criado_em",
    "atualizado_em",
]

COLUNAS_COMPRAS = [
    "compra_id",
    "item_id",
    "data_compra",
    "fornecedor",
    "quantidade",
    "valor_unitario",
    "local_inicial",
    "obra_id",
    "nota_fiscal",
    "observacoes",
    "criado_por",
    "criado_em",
]

COLUNAS_MOVIMENTACOES = [
    "movimentacao_id",
    "item_id",
    "data_movimentacao",
    "quantidade",
    "local_origem",
    "obra_origem_id",
    "local_destino",
    "obra_destino_id",
    "responsavel",
    "observacoes",
    "criado_por",
    "criado_em",
]

COLUNAS_ENTREGAS = [
    "evento_id",
    "tipo_evento",
    "matricula",
    "funcionario",
    "item_id",
    "tamanho",
    "data_evento",
    "quantidade",
    "local_estoque",
    "obra_id",
    "responsavel",
    "motivo",
    "observacoes",
    "criado_por",
    "criado_em",
]

COLUNAS_ESTOQUE = [
    "item_id",
    "categoria",
    "nome",
    "tamanho",
    "ca",
    "unidade",
    "localizacao",
    "obra_id",
    "quantidade",
]


def agora():
    return datetime.now().isoformat(timespec="seconds")


def gerar_id(prefixo):
    return f"{prefixo}_{uuid4().hex[:12]}"


def _texto(valor):
    if pd.isna(valor):
        return ""
    return str(valor).strip()


def _numero_positivo(valor, campo):
    try:
        numero = float(valor)
    except (TypeError, ValueError):
        raise ValueError(f"{campo} deve ser um número.") from None
    if not isfinite(numero) or numero <= 0:
        raise ValueError(f"{campo} deve ser maior que zero.")
    return numero


def _adicionar_linha(df, linha):
    nova_linha = pd.DataFrame([linha], columns=df.columns)
    if df.empty:
        return nova_linha
    return pd.concat([df, nova_linha], ignore_index=True)


def carregar_bases(token, repo):
    from services.dados_persistencia import carregar_cadastro_resultado

    return {
        "itens": carregar_cadastro_resultado(
            ARQ_ITENS, COLUNAS_ITENS, token, repo
        ),
        "compras": carregar_cadastro_resultado(
            ARQ_COMPRAS, COLUNAS_COMPRAS, token, repo
        ),
        "movimentacoes": carregar_cadastro_resultado(
            ARQ_MOVIMENTACOES, COLUNAS_MOVIMENTACOES, token, repo
        ),
        "entregas": carregar_cadastro_resultado(
            ARQ_ENTREGAS, COLUNAS_ENTREGAS, token, repo
        ),
    }


def salvar_base(df, arquivo, colunas, token, repo, resultado_leitura):
    from services.dados_persistencia import salvar_cadastro_seguro

    return salvar_cadastro_seguro(
        df,
        arquivo,
        colunas,
        token,
        repo,
        resultado_leitura=resultado_leitura,
    )


def cadastrar_item(
    itens,
    *,
    categoria,
    nome,
    descricao="",
    tamanho="",
    ca="",
    unidade="un",
    observacoes="",
    item_id=None,
    instante=None,
):
    categoria = _texto(categoria)
    nome = _texto(nome)
    unidade = _texto(unidade)
    if categoria not in {"Uniforme", "EPI"}:
        raise ValueError("A categoria deve ser Uniforme ou EPI.")
    if not nome:
        raise ValueError("Informe o nome do item.")
    if not unidade:
        raise ValueError("Informe a unidade.")

    ativos = itens[
        itens["ativo"].astype(str).str.lower().isin(["sim", "s", "1", "true"])
    ]
    duplicado = ativos[
        (ativos["categoria"].astype(str).str.casefold() == categoria.casefold())
        & (ativos["nome"].astype(str).str.strip().str.casefold() == nome.casefold())
        & (
            ativos["tamanho"].astype(str).str.strip().str.casefold()
            == _texto(tamanho).casefold()
        )
        & (
            ativos["ca"].astype(str).str.strip().str.casefold()
            == _texto(ca).casefold()
        )
    ]
    if not duplicado.empty:
        raise ValueError(
            "Já existe um item ativo com categoria, nome, tamanho e CA iguais."
        )

    momento = instante or agora()
    novo = {
        "item_id": item_id or gerar_id("ITEM"),
        "categoria": categoria,
        "nome": nome,
        "descricao": _texto(descricao),
        "tamanho": _texto(tamanho),
        "ca": _texto(ca),
        "unidade": unidade,
        "ativo": "sim",
        "observacoes": _texto(observacoes),
        "criado_em": momento,
        "atualizado_em": momento,
    }
    return _adicionar_linha(itens, novo)


def registrar_compra(
    compras,
    itens,
    *,
    item_id,
    data_compra,
    fornecedor,
    quantidade,
    valor_unitario,
    local_inicial,
    obra_id="",
    nota_fiscal="",
    observacoes="",
    criado_por="",
    compra_id=None,
    instante=None,
):
    item_id = _texto(item_id)
    if item_id not in set(itens["item_id"].astype(str)):
        raise ValueError("Selecione um item cadastrado.")
    if not _texto(data_compra):
        raise ValueError("Informe a data da compra.")
    if not _texto(local_inicial):
        raise ValueError("Informe a localização inicial.")

    novo = {
        "compra_id": compra_id or gerar_id("COMPRA"),
        "item_id": item_id,
        "data_compra": _texto(data_compra),
        "fornecedor": _texto(fornecedor),
        "quantidade": _numero_positivo(quantidade, "Quantidade"),
        "valor_unitario": _numero_positivo(valor_unitario, "Valor unitário"),
        "local_inicial": _texto(local_inicial),
        "obra_id": _texto(obra_id),
        "nota_fiscal": _texto(nota_fiscal),
        "observacoes": _texto(observacoes),
        "criado_por": _texto(criado_por),
        "criado_em": instante or agora(),
    }
    return _adicionar_linha(compras, novo)


def calcular_estoque(itens, compras, movimentacoes, entregas=None):
    saldos = {}

    def acumular(item_id, local, obra_id, quantidade):
        chave = (_texto(item_id), _texto(local), _texto(obra_id))
        saldos[chave] = saldos.get(chave, 0.0) + float(quantidade)

    for _, compra in compras.iterrows():
        quantidade = pd.to_numeric(compra.get("quantidade"), errors="coerce")
        if pd.notna(quantidade):
            acumular(
                compra.get("item_id"),
                compra.get("local_inicial"),
                compra.get("obra_id"),
                quantidade,
            )

    for _, movimento in movimentacoes.iterrows():
        quantidade = pd.to_numeric(movimento.get("quantidade"), errors="coerce")
        if pd.isna(quantidade):
            continue
        acumular(
            movimento.get("item_id"),
            movimento.get("local_origem"),
            movimento.get("obra_origem_id"),
            -quantidade,
        )
        acumular(
            movimento.get("item_id"),
            movimento.get("local_destino"),
            movimento.get("obra_destino_id"),
            quantidade,
        )

    if entregas is not None:
        for _, evento in entregas.iterrows():
            quantidade = pd.to_numeric(
                evento.get("quantidade"), errors="coerce"
            )
            if pd.isna(quantidade):
                continue
            tipo = _texto(evento.get("tipo_evento")).upper()
            if tipo == "ENTREGA":
                quantidade = -quantidade
            elif tipo == "DEVOLUCAO":
                quantidade = quantidade
            else:
                continue
            acumular(
                evento.get("item_id"),
                evento.get("local_estoque"),
                evento.get("obra_id"),
                quantidade,
            )

    itens_por_id = {
        str(linha["item_id"]): linha for _, linha in itens.iterrows()
    }
    linhas = []
    for (item_id, local, obra_id), quantidade in saldos.items():
        if abs(quantidade) < 1e-9:
            continue
        item = itens_por_id.get(item_id, {})
        linhas.append(
            {
                "item_id": item_id,
                "categoria": _texto(item.get("categoria", "")),
                "nome": _texto(item.get("nome", "")),
                "tamanho": _texto(item.get("tamanho", "")),
                "ca": _texto(item.get("ca", "")),
                "unidade": _texto(item.get("unidade", "")),
                "localizacao": local,
                "obra_id": obra_id,
                "quantidade": quantidade,
            }
        )

    if not linhas:
        return pd.DataFrame(columns=COLUNAS_ESTOQUE)
    return (
        pd.DataFrame(linhas, columns=COLUNAS_ESTOQUE)
        .sort_values(["categoria", "nome", "localizacao", "obra_id"])
        .reset_index(drop=True)
    )


def saldo_disponivel(estoque, item_id, local, obra_id=""):
    filtro = (
        (estoque["item_id"].astype(str) == _texto(item_id))
        & (estoque["localizacao"].astype(str) == _texto(local))
        & (estoque["obra_id"].astype(str) == _texto(obra_id))
    )
    return float(
        pd.to_numeric(
            estoque.loc[filtro, "quantidade"], errors="coerce"
        ).sum()
    )


def registrar_movimentacao(
    movimentacoes,
    estoque,
    *,
    item_id,
    data_movimentacao,
    quantidade,
    local_origem,
    local_destino,
    obra_origem_id="",
    obra_destino_id="",
    responsavel="",
    observacoes="",
    criado_por="",
    movimentacao_id=None,
    instante=None,
):
    quantidade = _numero_positivo(quantidade, "Quantidade")
    item_id = _texto(item_id)
    local_origem = _texto(local_origem)
    local_destino = _texto(local_destino)
    obra_origem_id = _texto(obra_origem_id)
    obra_destino_id = _texto(obra_destino_id)

    if not _texto(data_movimentacao):
        raise ValueError("Informe a data da movimentação.")
    if not local_origem or not local_destino:
        raise ValueError("Informe a origem e o destino.")
    if (local_origem, obra_origem_id) == (local_destino, obra_destino_id):
        raise ValueError("Origem e destino devem ser diferentes.")
    disponivel = saldo_disponivel(
        estoque, item_id, local_origem, obra_origem_id
    )
    if quantidade > disponivel + 1e-9:
        raise ValueError(
            f"Saldo insuficiente na origem. Disponível: {disponivel:g}."
        )

    novo = {
        "movimentacao_id": movimentacao_id or gerar_id("MOV"),
        "item_id": item_id,
        "data_movimentacao": _texto(data_movimentacao),
        "quantidade": quantidade,
        "local_origem": local_origem,
        "obra_origem_id": obra_origem_id,
        "local_destino": local_destino,
        "obra_destino_id": obra_destino_id,
        "responsavel": _texto(responsavel),
        "observacoes": _texto(observacoes),
        "criado_por": _texto(criado_por),
        "criado_em": instante or agora(),
    }
    return _adicionar_linha(movimentacoes, novo)


def calcular_posse_funcionarios(itens, entregas):
    saldos = {}
    nomes = {}
    tamanhos = {
        str(linha["item_id"]): _texto(linha.get("tamanho", ""))
        for _, linha in itens.iterrows()
    }
    itens_por_id = {
        str(linha["item_id"]): linha for _, linha in itens.iterrows()
    }

    for _, evento in entregas.iterrows():
        matricula = _texto(evento.get("matricula"))
        item_id = _texto(evento.get("item_id"))
        quantidade = pd.to_numeric(
            evento.get("quantidade"), errors="coerce"
        )
        if not matricula or not item_id or pd.isna(quantidade):
            continue
        tipo = _texto(evento.get("tipo_evento")).upper()
        if tipo == "ENTREGA":
            sinal = 1
        elif tipo in {"DEVOLUCAO", "BAIXA"}:
            sinal = -1
        else:
            continue
        chave = (matricula, item_id)
        saldos[chave] = saldos.get(chave, 0.0) + sinal * float(quantidade)
        nomes[matricula] = _texto(evento.get("funcionario"))

    linhas = []
    for (matricula, item_id), quantidade in saldos.items():
        if abs(quantidade) < 1e-9:
            continue
        item = itens_por_id.get(item_id, {})
        linhas.append(
            {
                "matricula": matricula,
                "funcionario": nomes.get(matricula, ""),
                "item_id": item_id,
                "categoria": _texto(item.get("categoria", "")),
                "item": _texto(item.get("nome", "")),
                "tamanho": tamanhos.get(item_id, ""),
                "quantidade": quantidade,
                "unidade": _texto(item.get("unidade", "")),
            }
        )

    colunas = [
        "matricula",
        "funcionario",
        "item_id",
        "categoria",
        "item",
        "tamanho",
        "quantidade",
        "unidade",
    ]
    if not linhas:
        return pd.DataFrame(columns=colunas)
    return (
        pd.DataFrame(linhas, columns=colunas)
        .sort_values(["funcionario", "item", "tamanho"])
        .reset_index(drop=True)
    )


def saldo_em_posse(posses, matricula, item_id):
    filtro = (
        (posses["matricula"].astype(str) == _texto(matricula))
        & (posses["item_id"].astype(str) == _texto(item_id))
    )
    return float(
        pd.to_numeric(
            posses.loc[filtro, "quantidade"], errors="coerce"
        ).sum()
    )


def _item_por_id(itens, item_id):
    encontrados = itens[itens["item_id"].astype(str) == _texto(item_id)]
    if encontrados.empty:
        raise ValueError("Selecione um item cadastrado.")
    return encontrados.iloc[0]


def registrar_entrega(
    entregas,
    itens,
    estoque,
    *,
    matricula,
    funcionario,
    item_id,
    quantidade,
    data_entrega,
    local_estoque,
    obra_id="",
    responsavel="",
    observacoes="",
    criado_por="",
    evento_id=None,
    instante=None,
):
    matricula = _texto(matricula)
    funcionario = _texto(funcionario)
    item_id = _texto(item_id)
    local_estoque = _texto(local_estoque)
    obra_id = _texto(obra_id)
    quantidade = _numero_positivo(quantidade, "Quantidade")
    item = _item_por_id(itens, item_id)

    if not matricula:
        raise ValueError("Informe a matrícula do funcionário.")
    if not funcionario:
        raise ValueError("Informe o nome do funcionário.")
    if not _texto(data_entrega):
        raise ValueError("Informe a data da entrega.")
    if not local_estoque:
        raise ValueError("Informe o local de saída do estoque.")
    if not _texto(responsavel):
        raise ValueError("Informe o responsável pela entrega.")

    disponivel = saldo_disponivel(
        estoque, item_id, local_estoque, obra_id
    )
    if quantidade > disponivel + 1e-9:
        raise ValueError(
            f"Saldo insuficiente no estoque. Disponível: {disponivel:g}."
        )

    evento = {
        "evento_id": evento_id or gerar_id("ENT"),
        "tipo_evento": "ENTREGA",
        "matricula": matricula,
        "funcionario": funcionario,
        "item_id": item_id,
        "tamanho": _texto(item.get("tamanho", "")),
        "data_evento": _texto(data_entrega),
        "quantidade": quantidade,
        "local_estoque": local_estoque,
        "obra_id": obra_id,
        "responsavel": _texto(responsavel),
        "motivo": "",
        "observacoes": _texto(observacoes),
        "criado_por": _texto(criado_por),
        "criado_em": instante or agora(),
    }
    return _adicionar_linha(entregas, evento)


def registrar_devolucao(
    entregas,
    itens,
    posses,
    *,
    matricula,
    funcionario,
    item_id,
    quantidade,
    data_devolucao,
    local_estoque,
    obra_id="",
    responsavel="",
    observacoes="",
    criado_por="",
    evento_id=None,
    instante=None,
):
    matricula = _texto(matricula)
    funcionario = _texto(funcionario)
    item_id = _texto(item_id)
    quantidade = _numero_positivo(quantidade, "Quantidade")
    item = _item_por_id(itens, item_id)

    if not matricula or not funcionario:
        raise ValueError("Funcionário e matrícula são obrigatórios.")
    if not _texto(data_devolucao):
        raise ValueError("Informe a data da devolução.")
    if not _texto(local_estoque):
        raise ValueError("Informe o local de retorno ao estoque.")
    if not _texto(responsavel):
        raise ValueError("Informe o responsável pela devolução.")
    disponivel = saldo_em_posse(posses, matricula, item_id)
    if quantidade > disponivel + 1e-9:
        raise ValueError(
            f"Quantidade superior à posse do funcionário. Disponível: {disponivel:g}."
        )

    evento = {
        "evento_id": evento_id or gerar_id("DEV"),
        "tipo_evento": "DEVOLUCAO",
        "matricula": matricula,
        "funcionario": funcionario,
        "item_id": item_id,
        "tamanho": _texto(item.get("tamanho", "")),
        "data_evento": _texto(data_devolucao),
        "quantidade": quantidade,
        "local_estoque": _texto(local_estoque),
        "obra_id": _texto(obra_id),
        "responsavel": _texto(responsavel),
        "motivo": "",
        "observacoes": _texto(observacoes),
        "criado_por": _texto(criado_por),
        "criado_em": instante or agora(),
    }
    return _adicionar_linha(entregas, evento)


def registrar_baixa(
    entregas,
    itens,
    posses,
    *,
    matricula,
    funcionario,
    item_id,
    quantidade,
    data_baixa,
    motivo,
    responsavel="",
    observacoes="",
    criado_por="",
    evento_id=None,
    instante=None,
):
    matricula = _texto(matricula)
    funcionario = _texto(funcionario)
    item_id = _texto(item_id)
    motivo = _texto(motivo)
    quantidade = _numero_positivo(quantidade, "Quantidade")
    item = _item_por_id(itens, item_id)

    if not matricula or not funcionario:
        raise ValueError("Funcionário e matrícula são obrigatórios.")
    if not _texto(data_baixa):
        raise ValueError("Informe a data da baixa.")
    if not motivo:
        raise ValueError("Informe o motivo da baixa.")
    if not _texto(responsavel):
        raise ValueError("Informe o responsável pela baixa.")
    disponivel = saldo_em_posse(posses, matricula, item_id)
    if quantidade > disponivel + 1e-9:
        raise ValueError(
            f"Quantidade superior à posse do funcionário. Disponível: {disponivel:g}."
        )

    evento = {
        "evento_id": evento_id or gerar_id("BAIXA"),
        "tipo_evento": "BAIXA",
        "matricula": matricula,
        "funcionario": funcionario,
        "item_id": item_id,
        "tamanho": _texto(item.get("tamanho", "")),
        "data_evento": _texto(data_baixa),
        "quantidade": quantidade,
        "local_estoque": "",
        "obra_id": "",
        "responsavel": _texto(responsavel),
        "motivo": motivo,
        "observacoes": _texto(observacoes),
        "criado_por": _texto(criado_por),
        "criado_em": instante or agora(),
    }
    return _adicionar_linha(entregas, evento)


def historico_funcionario(entregas, itens, matricula):
    eventos = entregas[
        entregas["matricula"].astype(str) == _texto(matricula)
    ].copy()
    colunas = [
        "data",
        "item",
        "tamanho",
        "quantidade_entregue",
        "quantidade_devolvida",
        "quantidade_baixada",
        "situacao_apos_evento",
        "responsavel",
        "motivo",
        "observacoes",
    ]
    if eventos.empty:
        return pd.DataFrame(columns=colunas)

    nomes = {
        str(linha["item_id"]): _texto(linha.get("nome", ""))
        for _, linha in itens.iterrows()
    }
    eventos = eventos.sort_values(
        ["data_evento", "criado_em", "evento_id"]
    )
    saldos = {}
    linhas = []
    for _, evento in eventos.iterrows():
        item_id = _texto(evento["item_id"])
        tipo = _texto(evento["tipo_evento"]).upper()
        quantidade = float(evento["quantidade"])
        saldos[item_id] = saldos.get(item_id, 0.0)
        if tipo == "ENTREGA":
            saldos[item_id] += quantidade
        else:
            saldos[item_id] -= quantidade
        linhas.append(
            {
                "data": evento["data_evento"],
                "item": nomes.get(item_id, item_id),
                "tamanho": evento["tamanho"],
                "quantidade_entregue": quantidade if tipo == "ENTREGA" else 0,
                "quantidade_devolvida": quantidade if tipo == "DEVOLUCAO" else 0,
                "quantidade_baixada": quantidade if tipo == "BAIXA" else 0,
                "situacao_apos_evento": saldos[item_id],
                "responsavel": evento["responsavel"],
                "motivo": evento["motivo"],
                "observacoes": evento["observacoes"],
            }
        )
    return pd.DataFrame(linhas, columns=colunas)
