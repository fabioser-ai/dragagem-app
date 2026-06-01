# ============================================================
# ARQUIVOS
# ============================================================

# Cadastros gerais
ARQ_OBRAS = "data/obras.csv"

# Medições — nova organização
ARQ_MEDICOES = "data/medicoes/medicoes.csv"
ARQ_MEDICAO = "data/medicoes/medicao.csv"
ARQ_FRENTES = "data/medicoes/frentes.csv"
ARQ_MC = "data/medicoes/mc.csv"
ARQ_ITENS = "data/medicoes/itens.csv"
ARQ_SERVICOS = "data/medicoes/servicos.csv"

# Tabelas contratuais específicas por obra
ARQ_TABELAS_SERVICOS_DIR = "data/medicoes_tabelas"

# Lançar Trabalho Executado
ARQ_LOCAIS_TRABALHO = "data/medicoes/locais_trabalho.csv"
ARQ_LANCAMENTOS_PRODUCAO = "data/medicoes/lancamentos_trabalho.csv"
ARQ_USUARIOS_OBRAS = "data/medicoes/usuarios_obras.csv"


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
        "lancamentos",
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
    "lancamento_id",
    "obra_id",
    "nome_obra",
    "local_id",
    "nome_local",
    "item_id",
    "codigo_item",
    "descricao_item",
    "unidade",
    "quantidade_executada",
    "data_servico",
    "observacao",
    "foto_url",
    "status_aprovacao",
    "aprovado_por",
    "aprovado_em",
    "status_medicao",
    "medicao_id_vinculada",
    "criado_por",
    "criado_em",
    "atualizado_em",
]

COL_USUARIOS_OBRAS = [
    "usuario_id",
    "email",
    "nome",
    "obra_id",
    "perfil_medicao",
    "ativo",
]


# ============================================================
# STATUS — LANÇAMENTOS
# ============================================================

STATUS_APROVACAO = [
    "pendente",
    "aprovado",
    "reprovado",
    "corrigir",
]

STATUS_MEDICAO = [
    "nao_medido",
    "selecionado_para_medicao",
    "medido",
    "glosado",
    "postergado",
]

STATUS_APROVACAO_PADRAO = "pendente"
STATUS_MEDICAO_PADRAO = "nao_medido"


# ============================================================
# PERFIS — MEDIÇÕES
# ============================================================

PERFIS_MEDICAO = [
    "funcionario",
    "encarregado",
    "aprovador",
    "admin",
]
