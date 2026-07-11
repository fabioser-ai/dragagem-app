# PROJECT_STATE

## Objetivo
Centralizar o estado oficial do desenvolvimento do APP FOS.

## Filosofia
- Baby steps.
- Uma mudança por vez.
- Evitar refatorações grandes.
- Auditoria antes de implementação.

## Estado atual
- Arquitetura auditada.
- Fluxo legado de lançamento identificado e documentado.
- Dependências básicas declaradas em requirements.txt.
- Auditorias incrementais preservadas em `docs/audit/`.
- Estrutura modular oficial criada em `docs/architecture/`.
- Auditoria de Orçamentos concluída em `docs/audit/AUDIT_034_ORCAMENTOS.md` e consolidada em `docs/architecture/08_ORCAMENTOS.md`.
- Auditoria de Prestação de Contas concluída em `docs/audit/AUDIT_035_PRESTACAO_CONTAS.md` e consolidada em `docs/architecture/09_PRESTACAO_CONTAS.md`.
- Auditoria do CRM concluída em `docs/audit/AUDIT_036_CRM.md` e consolidada em `docs/architecture/10_CRM.md`.
- Auditoria de Administração concluída em `docs/audit/AUDIT_037_ADMINISTRACAO.md` e consolidada em `docs/architecture/11_ADMINISTRACAO.md`.
- Auditoria de Serviços Compartilhados concluída em `docs/audit/AUDIT_038_SERVICOS_COMPARTILHADOS.md` e consolidada em `docs/architecture/12_SERVICOS_COMPARTILHADOS.md`.
- `docs/ARCHITECTURE_CURRENT.md` permanece como documento legado durante a migração gradual.

## Workflow oficial de auditoria
1. Auditar um subsistema por vez.
2. Registrar a auditoria concluída em `docs/audit/AUDIT_XXX_<SUBSISTEMA>.md`.
3. Consolidar os fatos observados no arquivo correspondente em `docs/architecture/`.
4. Registrar apenas fatos observados; hipóteses devem ser explicitamente marcadas.
5. Confirmar toda escrita por leitura posterior do trecho alterado.
6. Atualizar este `PROJECT_STATE.md`.
7. Somente depois considerar a auditoria encerrada e avançar para o próximo subsistema.

## Hierarquia documental
- `docs/PROJECT_STATE.md`: estado oficial e workflow do projeto.
- `docs/architecture/`: fonte modular e consolidada da arquitetura atual.
- `docs/audit/`: histórico incremental e detalhado das auditorias realizadas.
- `docs/ARCHITECTURE_CURRENT.md`: documento legado de transição; não remover conteúdo até a migração correspondente ser confirmada.

## Próximo passo
Executar a auditoria transversal final de consistência, cruzando os módulos e serviços já auditados para identificar padrões, duplicações, riscos sistêmicos e uma sequência segura de evolução arquitetural.
