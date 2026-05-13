# ============================================================
# ARQUIVOS
# ============================================================

ARQ_OBRAS = "data/obras.csv"
ARQ_MEDICOES = "data/medicoes.csv"
ARQ_FRENTES = "data/medicoes_frentes.csv"
ARQ_MC = "data/medicoes_mc.csv"
ARQ_ITENS = "data/medicoes_itens.csv"
ARQ_SERVICOS = "data/medicoes_servicos.csv"


# ============================================================
# MODELOS DE MEDIÇÃO
# ============================================================

MODELOS_MEDICAO = {
    "ast_bags": "AST / Bags / Comprimento x AST",
    "padrao_fos": "Padrão FOS",
    "diario_equipamento": "Diária / Equipamento",
    "batimetria": "Batimetria",
}

# ============================================================
# CONFIG MODELOS MEDIÇÃO
# ============================================================

CONFIG_MODELOS_MEDICAO = {
    "padrao_fos": {
        "usa_aditivo": False,
        "usa_periodo_fim": False,
        "usa_apostilamento": False,
    },
    "ast_bags": {
        "usa_aditivo": True,
        "usa_periodo_fim": True,
        "usa_apostilamento": True,
    },
    "diario_equipamento": {
        "usa_aditivo": False,
        "usa_periodo_fim": True,
        "usa_apostilamento": False,
    },
    "batimetria": {
        "usa_aditivo": False,
        "usa_periodo_fim": True,
        "usa_apostilamento": False,
    },
}

# ============================================================
# COLUNAS
# ============================================================

COL_OBRAS = [
    "obra_id",
    "nome_obra",
    "contratante",
    "contrato",
    "objeto",
    "cidade",
    "status",
    "modelo_medicao",
    "observacoes",
    "criado_em",
    "atualizado_em",
]

COL_MEDICOES = [
    "medicao_id",
    "obra_id",
    "numero_bm",
    "aditivo",
    "periodo_inicio",
    "periodo_fim",
    "data_bm",
    "dias_uteis_mes",
    "apostilamento_percentual",
    "status",
    "observacoes",
    "criado_em",
    "atualizado_em",
]

COL_FRENTES = [
    "frente_id",
    "medicao_id",
    "nome_frente",
    "dias_trabalhados",
    "observacoes",
    "criado_em",
    "atualizado_em",
]

COL_MC = [
    "mc_id",
    "medicao_id",
    "frente_id",
    "tipo",
    "descricao",
    "comprimento",
    "ast",
    "resultado",
]

COL_ITENS = [
    "item_id",
    "medicao_id",
    "frente_id",
    "codigo",
    "descricao",
    "unidade",
    "origem_mc",
    "quantidade",
    "valor_unitario",
    "total",
]

COL_SERVICOS = [
    "codigo",
    "descricao",
    "unidade",
]
