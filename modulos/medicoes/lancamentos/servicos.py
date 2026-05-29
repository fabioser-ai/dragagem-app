import pandas as pd

from modulos.medicoes.lancamentos.config import (
    STATUS_APROVACAO_PADRAO,
    STATUS_MEDICAO_PADRAO,
)
from modulos.medicoes.lancamentos.repositorio import (
    carregar_lancamentos_trabalho,
    salvar_lancamentos_trabalho,
)
from modulos.medicoes.utils import agora_iso, novo_id


def criar_lancamento_trabalho(
    obra_id,
    nome_obra,
    local_id,
    nome_local,
    item_id,
    codigo_item,
    descricao_item,
    unidade,
    quantidade_executada,
    data_servico,
    observacao="",
    foto_url="",
    criado_por="",
):
    df = carregar_lancamentos_trabalho()

    novo = {
        "lancamento_id": novo_id("LAN"),
        "obra_id": obra_id,
        "nome_obra": nome_obra,
        "local_id": local_id or "",
        "nome_local": nome_local or "",
        "item_id": item_id,
        "codigo_item": codigo_item,
        "descricao_item": descricao_item,
        "unidade": unidade,
        "quantidade_executada": str(quantidade_executada),
        "data_servico": str(data_servico),
        "observacao": observacao or "",
        "foto_url": foto_url or "",
        "status_aprovacao": STATUS_APROVACAO_PADRAO,
        "aprovado_por": "",
        "aprovado_em": "",
        "status_medicao": STATUS_MEDICAO_PADRAO,
        "medicao_id_vinculada": "",
        "criado_por": criado_por or "",
        "criado_em": agora_iso(),
        "atualizado_em": agora_iso(),
    }

    df = pd.concat(
        [df, pd.DataFrame([novo])],
        ignore_index=True,
    )

    salvar_lancamentos_trabalho(df)

    return novo


def listar_lancamentos_trabalho():
    return carregar_lancamentos_trabalho()


def listar_lancamentos_por_obra(obra_id):
    df = carregar_lancamentos_trabalho()

    if df.empty:
        return df

    return df[df["obra_id"] == obra_id].copy()


def listar_lancamentos_pendentes():
    df = carregar_lancamentos_trabalho()

    if df.empty:
        return df

    return df[df["status_aprovacao"] == STATUS_APROVACAO_PADRAO].copy()


def atualizar_status_aprovacao(
    lancamento_id,
    novo_status,
    aprovado_por="",
):
    df = carregar_lancamentos_trabalho()

    if df.empty:
        return False

    mask = df["lancamento_id"] == lancamento_id

    if not mask.any():
        return False

    df.loc[mask, "status_aprovacao"] = novo_status
    df.loc[mask, "aprovado_por"] = aprovado_por or ""
    df.loc[mask, "aprovado_em"] = agora_iso()
    df.loc[mask, "atualizado_em"] = agora_iso()

    salvar_lancamentos_trabalho(df)

    return True


def vincular_lancamento_a_medicao(
    lancamento_id,
    medicao_id,
    status_medicao="medido",
):
    df = carregar_lancamentos_trabalho()

    if df.empty:
        return False

    mask = df["lancamento_id"] == lancamento_id

    if not mask.any():
        return False

    df.loc[mask, "status_medicao"] = status_medicao
    df.loc[mask, "medicao_id_vinculada"] = medicao_id
    df.loc[mask, "atualizado_em"] = agora_iso()

    salvar_lancamentos_trabalho(df)

    return True
