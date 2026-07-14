# Orçamentos — Base Oficial de Conhecimento

## Missão

Preservar, organizar, homologar e consolidar o conhecimento da FOS Engenharia relacionado à elaboração de orçamentos antes de qualquer decisão arquitetural ou implementação.

## Escopo

Esta pasta registra a governança documental do domínio de orçamentos. Ela não contém implementação de software e não autoriza a criação antecipada de banco de dados, APIs, classes, interfaces, componentes ou tabelas.

## Estrutura

- `metodologia/`: regras permanentes para extração, documentação, homologação e vocabulário.
- `analises/`: índice das análises individuais, sempre identificadas pelo nome completo do arquivo Excel.
- `consolidacao/`: resultados transversais homologados após quantidade significativa de análises.

Os documentos históricos existentes em `docs/knowledge/orcamentos/` permanecem válidos como registros de conhecimento já produzidos. Novas análises devem seguir esta metodologia e preservar referência bidirecional com registros anteriores quando aplicável.

## Fluxo oficial

```text
Descoberta
    ↓
Documentação
    ↓
Homologação
    ↓
Consolidação
    ↓
Arquitetura
    ↓
Implementação
    ↓
Testes
    ↓
Homologação Final
```

Arquitetura nunca pode preceder documentação homologada.

## Responsabilidades

### Curador da Base de Conhecimento

- preservar rastreabilidade;
- organizar e revisar a documentação;
- impedir que hipóteses sejam tratadas como fatos;
- evitar duplicidades e contradições;
- manter coerência entre análises, consolidações e arquitetura.

### Especialista da FOS

- esclarecer práticas, exceções e decisões implícitas;
- homologar interpretações relevantes;
- decidir quando uma quantidade significativa de análises foi atingida.

### Arquitetura e implementação

Somente podem utilizar conhecimento documentado, homologado e consolidado.

## Regra de identificação

O identificador permanente de cada análise é o nome completo do arquivo Excel, incluindo extensão.

Exemplo válido:

`D_004_2026 - SABESP.xlsx`

Identificadores genéricos como `ANALYSIS_001`, `PLANILHA_A` ou `ORCAMENTO_01` são proibidos.

## Regra de ouro

Em caso de conflito entre memória, conversa e documentação, prevalece a documentação oficial do repositório.