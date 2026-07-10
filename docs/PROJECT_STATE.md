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
- Auditoria de Orçamentos concluída em `docs/audit/AUDIT_034_ORCAMENTOS.md` e pendente de consolidação em `docs/ARCHITECTURE_CURRENT.md`.
- Auditoria de Prestação de Contas concluída em `docs/audit/AUDIT_035_PRESTACAO_CONTAS.md` e pendente de consolidação em `docs/ARCHITECTURE_CURRENT.md`.

## Workflow oficial de auditoria
1. Auditar um subsistema por vez.
2. Registrar a auditoria concluída em `docs/audit/AUDIT_XXX_<SUBSISTEMA>.md`.
3. Atualizar `docs/ARCHITECTURE_CURRENT.md` na mesma sessão, quando operacionalmente possível.
4. Registrar apenas fatos observados; hipóteses devem ser explicitamente marcadas.
5. Confirmar toda escrita por leitura posterior do trecho alterado.
6. Se a consolidação no documento principal não puder ser concluída, preservar primeiro o relatório em `docs/audit/` e registrar que ele ainda está pendente de consolidação.
7. Somente depois considerar a auditoria encerrada e avançar para o próximo subsistema.

## Hierarquia documental
- `docs/PROJECT_STATE.md`: estado oficial e workflow do projeto.
- `docs/ARCHITECTURE_CURRENT.md`: visão consolidada e oficial da arquitetura atual.
- `docs/audit/`: histórico incremental e detalhado das auditorias realizadas.

## Próximo passo
Consolidar as auditorias de Orçamentos e Prestação de Contas em `docs/ARCHITECTURE_CURRENT.md`. Depois, auditar o módulo CRM.
