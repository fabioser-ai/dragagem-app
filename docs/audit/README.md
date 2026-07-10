# Auditorias Arquiteturais

Esta pasta preserva o histórico incremental das auditorias arquiteturais do APP FOS.

## Regra de uso

Cada auditoria concluída deve gerar um arquivo no formato:

```text
AUDIT_XXX_<SUBSISTEMA>.md
```

Exemplo:

```text
AUDIT_034_ORCAMENTOS.md
```

## Workflow obrigatório

1. Auditar um subsistema por vez.
2. Basear conclusões somente em código observado e documentação oficial.
3. Marcar hipóteses explicitamente como hipóteses.
4. Criar o relatório incremental nesta pasta assim que a auditoria for concluída.
5. Consolidar os fatos observados em `docs/ARCHITECTURE_CURRENT.md` na mesma sessão, quando operacionalmente possível.
6. Confirmar toda escrita por leitura posterior.
7. Caso a consolidação não possa ser realizada, manter o relatório como pendente de consolidação e não perder a análise produzida.

## Papel dos documentos

- `docs/PROJECT_STATE.md`: estado oficial e regras do processo.
- `docs/ARCHITECTURE_CURRENT.md`: arquitetura consolidada atual.
- `docs/audit/`: histórico detalhado das auditorias.

## Integridade

Os relatórios desta pasta não substituem `ARCHITECTURE_CURRENT.md`. Eles preservam o conhecimento produzido até sua consolidação no documento oficial.
