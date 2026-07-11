# Arquitetura Atual — Matriz de Cobertura Documental

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_042_MATRIZ_COBERTURA_DOCUMENTAL.md`

## Objetivo

Esta matriz relaciona os módulos e fluxos explícitos do roteador principal do APP FOS às fontes arquiteturais vigentes, indicando cobertura, atualização e lacunas conhecidas.

## Cobertura por rota ou domínio

| Domínio ou fluxo | Rotas principais | Fonte vigente | Cobertura | Lacunas principais |
| --- | --- | --- | --- | --- |
| Serviços compartilhados e bootstrap | pré-roteamento | `12_SERVICOS_COMPARTILHADOS.md` | Alta para autenticação, sessão, persistência, logs e UI | `app.py` e o roteador não possuem documento modular próprio. |
| Menu | `menu` | `11_ADMINISTRACAO.md`, `12_SERVICOS_COMPARTILHADOS.md`, `13_AUDITORIA_TRANSVERSAL.md` | Parcial | Falta auditoria dedicada da exposição de módulos, cards e coerência com o roteador. |
| Medições — fundação | `carregando_medicoes`, `medicoes` | `01_MEDICOES_FUNDACAO.md` | Alta para o recorte migrado | Legado ainda preservado para reconciliação. |
| Medições — lançamentos | interno a `medicoes` | `02_MEDICOES_LANCAMENTOS.md` | Alta para o fluxo auditado | Identidade de obra, vínculos, foto e confirmação de persistência. |
| Medições — aprovação | interno a `medicoes` | `03_MEDICOES_APROVACAO.md` | Alta para o fluxo auditado | Cruzamento entre aprovador, obra e vínculo. |
| Medições — gestão | interno a `medicoes` | `04_MEDICOES_GESTAO.md` | Alta para o fluxo auditado | Estado e persistência da vinculação lançamento/BM. |
| Orçamentos | `orcamento`, `orcamento_lista`, `orcamento_etapa0`, `orcamento1`, `orcamento2`, `orcamento3` | `08_ORCAMENTOS.md` | Alta | Finalização, barrilete, código e autorização interna. |
| Prestação de Contas | `prestacao_contas` | `09_PRESTACAO_CONTAS.md` | Alta | Máquina de estados, consistência comprovante/despesa e acesso administrativo. |
| CRM | `crm` | `10_CRM.md` | Alta | Homônimos, integridade referencial e gravação composta. |
| Administração | `administracao` | `11_ADMINISTRACAO.md` | Alta para permissões | Contas em `APP_USERS`, validações e trilha de alterações permanecem fora do módulo. |
| Dados | `dados` | legado, quando aplicável | Baixa / não demonstrada | Sem auditoria modular dedicada. |
| Férias | `ferias` | legado, quando aplicável | Baixa / não demonstrada | Sem auditoria modular dedicada; fornece dados organizacionais à Prestação de Contas. |
| Obras | `obras` | evidência direta em `app.py` e referências parciais | Baixa | Sem auditoria própria; lê diretamente `data/orcamentos.csv`. |
| Fallback de rota | estado não reconhecido | evidência direta em `app.py` | Parcial | Sem inventário central nem registro do estado inválido. |

## Situação global

A cobertura arquitetural é forte para o ciclo priorizado já auditado:

- Medições;
- Orçamentos;
- Prestação de Contas;
- CRM;
- Administração;
- Serviços Compartilhados.

A cobertura integral do aplicativo ainda não está demonstrada porque `Dados`, `Férias` e `Obras` permanecem sem auditoria modular dedicada.

## Interpretação do estado oficial

A expressão “Arquitetura auditada” em `PROJECT_STATE.md` deve ser entendida como referência ao ciclo priorizado e documentado, não como afirmação de que todas as rotas e todos os domínios do aplicativo possuem cobertura equivalente.

## Próxima decisão

Antes de implementar o contrato de leitura em `services/github.py`, escolher explicitamente entre:

1. completar as auditorias de `Dados`, `Férias` e `Obras`; ou
2. tratar primeiro o risco sistêmico da persistência, mantendo essas três lacunas funcionais registradas.

A segunda sequência é compatível com as evidências já produzidas, desde que não seja confundida com cobertura arquitetural integral.
