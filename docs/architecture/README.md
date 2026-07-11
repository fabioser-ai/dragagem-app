# Arquitetura Atual — Estrutura Modular

Esta pasta contém a documentação oficial e consolidada da arquitetura atual do APP FOS.

## Regra de autoridade

- `docs/PROJECT_STATE.md` registra o estado oficial e o workflow do projeto.
- `docs/architecture/` é a fonte consolidada da arquitetura atual por domínio.
- `docs/audit/` preserva o histórico detalhado de cada auditoria.
- `docs/ARCHITECTURE_CURRENT.md` permanece como documento legado durante a transição para a estrutura modular.

## Workflow oficial

1. Auditar um subsistema por vez.
2. Criar `docs/audit/AUDIT_XXX_<SUBSISTEMA>.md`.
3. Consolidar os fatos observados no arquivo modular correspondente desta pasta.
4. Confirmar toda escrita por leitura posterior.
5. Atualizar `docs/PROJECT_STATE.md`.
6. Não registrar hipóteses como fatos.

## Índice atual

- `08_ORCAMENTOS.md`
- `09_PRESTACAO_CONTAS.md`
- `10_CRM.md`

## Migração

Os demais domínios serão migrados gradualmente a partir do documento legado e de novas auditorias. Nenhum conteúdo do arquivo legado deve ser removido até a migração correspondente ser confirmada.