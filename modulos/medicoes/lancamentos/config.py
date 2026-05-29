ARQUIVO_LANCAMENTOS_TRABALHO = "data/medicoes/lancamentos_trabalho.csv"
ARQUIVO_LOCAIS_TRABALHO = "data/medicoes/locais_trabalho.csv"


COLUNAS_LANCAMENTOS_TRABALHO = [
    "lancamento_id",
    "obra_id",
    "local_id",
    "local_nome",
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


COLUNAS_LOCAIS_TRABALHO = [
    "local_id",
    "obra_id",
    "nome_local",
    "descricao",
    "ativo",
    "criado_em",
    "atualizado_em",
]


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
