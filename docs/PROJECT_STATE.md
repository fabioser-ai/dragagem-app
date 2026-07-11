# PROJECT_STATE

## Objetivo

Centralizar o estado oficial do desenvolvimento do APP FOS.

## Filosofia

A filosofia oficial de desenvolvimento está registrada em `docs/DEVELOPMENT_PHILOSOPHY.md`.

Princípios centrais:

- Baby steps.
- Uma alteração por vez.
- Arquitetura antes de implementação.
- Auditoria antes de implementação.
- Código observado acima de hipóteses.
- Documentação oficial acima da memória.
- Não refatorar por preferência pessoal.
- Confirmar toda escrita por leitura posterior.
- O conhecimento oficial do projeto pertence ao repositório.

## Estado atual

- Arquitetura auditada.
- Fluxo legado de lançamento identificado e documentado.
- Dependências básicas declaradas em `requirements.txt`.
- Auditorias incrementais preservadas em `docs/audit/`.
- Estrutura modular oficial criada em `docs/architecture/`.
- Auditoria de Orçamentos concluída em `docs/audit/AUDIT_034_ORCAMENTOS.md` e consolidada em `docs/architecture/08_ORCAMENTOS.md`.
- Auditoria de Prestação de Contas concluída em `docs/audit/AUDIT_035_PRESTACAO_CONTAS.md` e consolidada em `docs/architecture/09_PRESTACAO_CONTAS.md`.
- Auditoria do CRM concluída em `docs/audit/AUDIT_036_CRM.md` e consolidada em `docs/architecture/10_CRM.md`.
- Auditoria de Administração concluída em `docs/audit/AUDIT_037_ADMINISTRACAO.md` e consolidada em `docs/architecture/11_ADMINISTRACAO.md`.
- Auditoria de Serviços Compartilhados concluída em `docs/audit/AUDIT_038_SERVICOS_COMPARTILHADOS.md` e consolidada em `docs/architecture/12_SERVICOS_COMPARTILHADOS.md`.
- `docs/ARCHITECTURE_CURRENT.md` permanece como documento legado durante a migração gradual.
- A filosofia de desenvolvimento foi formalizada em `docs/DEVELOPMENT_PHILOSOPHY.md`.
- AUDIT_039 — Auditoria Transversal de Consistência concluída em `docs/audit/AUDIT_039_AUDITORIA_TRANSVERSAL.md` e consolidada em `docs/architecture/13_AUDITORIA_TRANSVERSAL.md`.
- AUDIT_040 — Auditoria do Conhecimento Registrado concluída em `docs/audit/AUDIT_040_CONHECIMENTO_REGISTRADO.md` e consolidada em `docs/architecture/14_CONHECIMENTO_REGISTRADO.md`.
- AUDIT_041 — Migração documental de Medições concluída em `docs/audit/AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md` e consolidada em `docs/architecture/01_MEDICOES_FUNDACAO.md` a `04_MEDICOES_GESTAO.md`.
- O conhecimento específico de Medições possui agora fontes modulares; `docs/ARCHITECTURE_CURRENT.md` permanece legado até reconciliação completa.

## Workflow oficial de auditoria

1. Ler `docs/PROJECT_STATE.md`, `docs/DEVELOPMENT_PHILOSOPHY.md` e a documentação aplicável de `docs/architecture/`.
2. Auditar um subsistema por vez ou um recorte transversal explicitamente definido.
3. Registrar a auditoria concluída em `docs/audit/AUDIT_XXX_<SUBSISTEMA>.md`.
4. Consolidar os fatos observados no arquivo correspondente em `docs/architecture/`.
5. Registrar apenas fatos observados; hipóteses, lacunas e limites devem ser explicitamente marcados.
6. Confirmar toda escrita por leitura posterior do trecho alterado.
7. Atualizar este `PROJECT_STATE.md`.
8. Somente depois considerar a auditoria encerrada e avançar para o próximo subsistema.

## Hierarquia documental

- `docs/PROJECT_STATE.md`: estado oficial e workflow do projeto.
- `docs/DEVELOPMENT_PHILOSOPHY.md`: princípios e regras permanentes de desenvolvimento e auditoria.
- `docs/architecture/`: fonte modular e consolidada da arquitetura atual por domínio.
- `docs/audit/`: histórico incremental e detalhado das auditorias realizadas.
- `docs/ARCHITECTURE_CURRENT.md`: documento legado de transição; não remover conteúdo até a migração correspondente ser confirmada.

## Próximo passo

Executar o baby step documental identificado na AUDIT_040: criar uma matriz de cobertura por módulo ou fluxo roteado, com fonte arquitetural vigente, auditoria de origem, nível de atualização e lacunas conhecidas. A matriz deve apontar as novas fontes modulares de Medições. Só depois reavaliar o início da implementação do contrato de leitura em `services/github.py`.
