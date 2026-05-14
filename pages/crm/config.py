from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "crm"

ARQUIVO_CLIENTES = DATA_DIR / "clientes.csv"
ARQUIVO_CONTATOS = DATA_DIR / "contatos.csv"
ARQUIVO_INTERACOES = DATA_DIR / "interacoes.csv"


COLUNAS_CLIENTES = [
    "id_cliente",
    "nome_empresa",
    "tipo_cliente",
    "documento",
    "cidade",
    "estado",
    "endereco_local",
    "setor_atividade",
    "origem_cliente",
    "status_relacionamento",
    "responsavel",
    "necessidade_cliente",
    "ultimo_contato",
    "proxima_acao",
    "data_proxima_acao",
    "observacoes_gerais",
    "created_at",
    "updated_at",
]

COLUNAS_CONTATOS = [
    "id_contato",
    "id_cliente",
    "nome_contato",
    "cargo",
    "telefone",
    "whatsapp",
    "email",
    "contato_principal",
    "observacoes",
    "created_at",
    "updated_at",
]

COLUNAS_INTERACOES = [
    "id_interacao",
    "id_cliente",
    "id_contato",
    "data_interacao",
    "tipo_contato",
    "descricao",
    "responsavel",
    "resultado",
    "proxima_acao",
    "data_proxima_acao",
    "created_at",
]


TIPOS_CLIENTE = [
    "Empresa privada",
    "Órgão público",
    "Prefeitura",
    "Construtora",
    "Indústria",
    "Porto/Terminal",
    "Consultoria/Engenharia",
    "Pessoa física",
    "Outro",
]

STATUS_RELACIONAMENTO = [
    "Novo lead",
    "Contato iniciado",
    "Em relacionamento",
    "Oportunidade identificada",
    "Proposta futura",
    "Cliente ativo",
    "Cliente inativo",
    "Sem interesse no momento",
]

ORIGENS_CLIENTE = [
    "Indicação",
    "Cliente antigo",
    "Prospecção ativa",
    "Licitação",
    "Site",
    "Evento",
    "Contato comercial",
    "Outro",
]

TIPOS_CONTATO = [
    "Telefone",
    "WhatsApp",
    "Email",
    "Reunião presencial",
    "Reunião online",
    "Visita técnica",
    "Indicação",
    "Outro",
]

RESULTADOS_INTERACAO = [
    "Sem retorno",
    "Contato realizado",
    "Interesse identificado",
    "Necessita orçamento",
    "Aguardando informações",
    "Agendar reunião",
    "Sem interesse no momento",
    "Outro",
]
