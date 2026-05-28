# ============================================================
# ARQUIVOS
# ============================================================

ARQ_OBRAS = "data/obras.csv"
ARQ_MEDICOES = "data/medicoes.csv"
ARQ_FRENTES = "data/medicoes_frentes.csv"
ARQ_MC = "data/medicoes_mc.csv"
ARQ_ITENS = "data/medicoes_itens.csv"
ARQ_SERVICOS = "data/medicoes_servicos.csv"
ARQ_TABELAS_SERVICOS_DIR = "data/medicoes_tabelas"

# Lançar Trabalho Executado
ARQ_LOCAIS_TRABALHO = "data/medicoes_locais_trabalho.csv"
ARQ_LANCAMENTOS_PRODUCAO = "data/medicoes_lancamentos_producao.csv"

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
# ETAPAS MODELO
# ============================================================

ETAPAS_MODELO = {
    "padrao_fos": [
        "obra",
        "bm",
        "mc",
        "medicao",
        "resumo",
    ],
    "ast_bags": [
        "obra",
        "bm",
        "frentes",
        "mc",
        "medicao",
        "resumo",
    ],
    "diario_equipamento": [
        "obra",
        "bm",
        "frentes",
        "medicao",
        "resumo",
    ],
    "batimetria": [
        "obra",
        "bm",
        "mc",
        "resumo",
    ],
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
    "arquivo_tabela_servicos",
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

COL_TABELA_SERVICOS_CONTRATO = [
    "fonte",
    "codigo",
    "item",
    "descricao",
    "unidade",
    "quantidade_base",
    "custo_unitario_sem_bdi",
    "bdi",
    "preco_unitario_com_bdi",
    "preco_total",
    "ativo",
]

# ============================================================
# COLUNAS — LANÇAR TRABALHO EXECUTADO
# ============================================================

COL_LOCAIS_TRABALHO = [
    "local_id",
    "obra_id",
    "nome_local",
    "ativo",
    "observacoes",
    "criado_em",
    "atualizado_em",
]

COL_LANCAMENTOS_PRODUCAO = [
    "id_lancamento",
    "obra_id",
    "nome_obra",
    "local_id",
    "nome_local",
    "codigo_item",
    "descricao_item",
    "unidade",
    "quantidade",
    "data_servico",
    "observacao",
    "foto_arquivo",
    "usuario",
    "data_hora_lancamento",
    "status",
]
