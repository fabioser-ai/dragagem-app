# AUDIT_042 — Matriz de Cobertura Documental

Data: 2026-07-11

## Objetivo

Relacionar cada módulo ou fluxo roteado por `app.py` à fonte arquitetural vigente, à auditoria de origem, ao nível de atualização e às lacunas conhecidas.

Esta auditoria é exclusivamente documental. Nenhum comportamento funcional foi alterado.

## Fontes examinadas

- `app.py`;
- `docs/PROJECT_STATE.md`;
- `docs/DEVELOPMENT_PHILOSOPHY.md`;
- `docs/architecture/README.md`;
- `docs/architecture/01_MEDICOES_FUNDACAO.md` a `04_MEDICOES_GESTAO.md`;
- `docs/architecture/08_ORCAMENTOS.md` a `14_CONHECIMENTO_REGISTRADO.md`;
- `docs/audit/AUDIT_034_ORCAMENTOS.md` a `AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md`;
- `docs/ARCHITECTURE_CURRENT.md`, somente como legado de transição.

## Inventário do roteador

O roteador principal observado em `app.py` possui os seguintes destinos explícitos:

- `menu`;
- `dados`;
- `administracao`;
- `ferias`;
- `prestacao_contas`;
- `carregando_medicoes`;
- `medicoes`;
- `crm`;
- `obras`;
- `orcamento`;
- `orcamento_lista`;
- `orcamento_etapa0`;
- `orcamento1`;
- `orcamento2`;
- `orcamento3`;
- fallback para `menu`.

Autenticação e estilo global são executados antes do roteamento.

## Matriz de cobertura

| Módulo ou fluxo | Rotas observadas | Fonte arquitetural vigente | Auditoria de origem | Cobertura | Atualização | Lacunas conhecidas |
| --- | --- | --- | --- | --- | --- | --- |
| Bootstrap, autenticação, sessão, persistência, logs e UI global | pré-roteamento | `docs/architecture/12_SERVICOS_COMPARTILHADOS.md` | `AUDIT_038_SERVICOS_COMPARTILHADOS.md` | Alta para os serviços centrais | 2026-07-11 | O roteador `app.py` não possui documento modular próprio; o acoplamento entre bootstrap e módulos é tratado transversalmente. |
| Menu principal e exposição de módulos | `menu` | `docs/architecture/11_ADMINISTRACAO.md`, `12_SERVICOS_COMPARTILHADOS.md` e `13_AUDITORIA_TRANSVERSAL.md` | AUDIT_037, AUDIT_038 e AUDIT_039 | Parcial | 2026-07-11 | Não existe auditoria dedicada ao menu, aos cards, ao fallback de navegação e à coerência entre módulos exibidos e rotas disponíveis. |
| Medições — fundação e entrada | `carregando_medicoes`, `medicoes` | `docs/architecture/01_MEDICOES_FUNDACAO.md` | `AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md` e auditorias anteriores de Medições | Alta para o recorte migrado | 2026-07-11 | O documento legado permanece para reconciliação completa. |
| Medições — lançamentos | interno ao módulo `medicoes` | `docs/architecture/02_MEDICOES_LANCAMENTOS.md` | `AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md` e auditoria específica anterior | Alta para o fluxo auditado | 2026-07-11 | Permanecem perguntas sobre identidade de obra, autorização por vínculo, foto e confirmação de persistência. |
| Medições — aprovação | interno ao módulo `medicoes` | `docs/architecture/03_MEDICOES_APROVACAO.md` | `AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md` e auditoria específica anterior | Alta para o fluxo auditado | 2026-07-11 | Permanecem lacunas de cruzamento entre aprovador, obra e vínculo. |
| Medições — gestão | interno ao módulo `medicoes` | `docs/architecture/04_MEDICOES_GESTAO.md` | `AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md` e auditoria específica anterior | Alta para o fluxo auditado | 2026-07-11 | Máquina de estados e persistência da vinculação lançamento/BM ainda precisam de definição. |
| Orçamentos | `orcamento`, `orcamento_lista`, `orcamento_etapa0`, `orcamento1`, `orcamento2`, `orcamento3` | `docs/architecture/08_ORCAMENTOS.md` | `AUDIT_034_ORCAMENTOS.md` | Alta para as rotas observadas | 2026-07-11 | Finalização não persistida; cálculo e unidade do barrilete; geração de código; autorização interna. |
| Prestação de Contas | `prestacao_contas` | `docs/architecture/09_PRESTACAO_CONTAS.md` | `AUDIT_035_PRESTACAO_CONTAS.md` | Alta para o arquivo principal e fluxos observados | 2026-07-11 | Máquina de estados, acesso de `superadmin`, consistência comprovante/despesa e identidade do proprietário. |
| CRM | `crm` | `docs/architecture/10_CRM.md` | `AUDIT_036_CRM.md` | Alta para clientes, contatos, interações e consulta geral | 2026-07-11 | Homônimos, integridade referencial, atualização composta e autorização interna. |
| Administração | `administracao` | `docs/architecture/11_ADMINISTRACAO.md` | `AUDIT_037_ADMINISTRACAO.md` | Alta para permissões granulares | 2026-07-11 | Não administra contas em `APP_USERS`; não valida usuário, obra, duplicidade ou conflitos; sem trilha própria. |
| Dados | `dados` | `docs/ARCHITECTURE_CURRENT.md` como legado, quando houver conteúdo aplicável | Nenhuma auditoria modular identificada | Baixa / não demonstrada | Legado anterior a 2026-07-11 | Não existe documento modular nem auditoria dedicada. Escopo, cadastros, permissões, persistência e consumidores precisam ser auditados. |
| Férias | `ferias` | `docs/ARCHITECTURE_CURRENT.md` como legado, quando houver conteúdo aplicável | Nenhuma auditoria modular identificada | Baixa / não demonstrada | Legado anterior a 2026-07-11 | Não existe documento modular nem auditoria dedicada. O módulo também fornece dados organizacionais para Prestação de Contas. |
| Obras | `obras` | Evidência direta em `app.py`; referências parciais em Orçamentos e transversal | Nenhuma auditoria modular identificada | Baixa | Código atual observado em 2026-07-11 | A rota lê diretamente `data/orcamentos.csv`, trata falha como DataFrame vazio e exibe a tabela completa. Não existe auditoria própria do significado de “obra” nesse fluxo. |
| Fallback de rota | qualquer estado não reconhecido | Evidência direta em `app.py` | Nenhuma auditoria dedicada | Parcial | Código atual observado em 2026-07-11 | O fallback redefine `tela = menu`; não existe inventário central de rotas nem registro de estado inválido. |

## Conclusões

1. A documentação modular cobre com boa profundidade Medições, Orçamentos, Prestação de Contas, CRM, Administração e Serviços Compartilhados.
2. A cobertura do aplicativo inteiro ainda não pode ser declarada completa.
3. `Dados`, `Férias` e `Obras` são destinos explícitos do roteador sem auditoria modular dedicada.
4. `Menu`, bootstrap e fallback possuem cobertura transversal, mas não uma auditoria de fluxo própria.
5. O documento legado continua necessário enquanto os domínios sem consolidação modular não forem auditados ou reconciliados.
6. A frase “Arquitetura auditada” deve ser interpretada como o ciclo priorizado já auditado, não como cobertura integral de todas as rotas do aplicativo.

## Classificação de lacunas

### Lacunas prioritárias de cobertura

1. `Dados`, por concentrar cadastros técnicos consumidos por outros módulos.
2. `Férias`, por ser módulo funcional e também fonte de dados organizacionais para Prestação de Contas.
3. `Obras`, por expor diretamente o conteúdo de `data/orcamentos.csv` como cadastro operacional.

### Lacunas secundárias

- menu principal e catálogo de módulos;
- roteador e fallback;
- reconciliação final do documento legado.

## Próximo baby step seguro

Antes de implementar o contrato de leitura em `services/github.py`, decidir formalmente entre duas sequências:

1. concluir primeiro as auditorias modulares de `Dados`, `Férias` e `Obras`; ou
2. iniciar o contrato de leitura como correção de infraestrutura prioritária, registrando explicitamente que a cobertura funcional desses três módulos permanece pendente.

A matriz demonstra que a segunda opção é tecnicamente possível para a infraestrutura já auditada, mas não autoriza declarar a arquitetura funcional integralmente coberta.
