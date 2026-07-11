# AUDIT_041 — Migração Documental de Medições

Data: 2026-07-11

## Objetivo

Extrair do documento legado `docs/ARCHITECTURE_CURRENT.md` o conhecimento específico do módulo Medições e organizá-lo na mesma estrutura modular usada pelos subsistemas auditados posteriormente.

## Método

- Preservar `docs/ARCHITECTURE_CURRENT.md` sem remoções.
- Registrar somente fatos já presentes no legado e nas auditorias de Medições referenciadas por ele.
- Não reauditar código nem modificar comportamento.
- Separar a consolidação por responsabilidade operacional.

## Documentos de destino

| Documento | Conteúdo migrado |
| --- | --- |
| `docs/architecture/01_MEDICOES_FUNDACAO.md` | Entrada, autorização interna, dados, repositórios e fronteiras de contexto. |
| `docs/architecture/02_MEDICOES_LANCAMENTOS.md` | Fluxo operacional de lançamento de trabalho executado. |
| `docs/architecture/03_MEDICOES_APROVACAO.md` | Fluxo de decisão sobre lançamentos pendentes. |
| `docs/architecture/04_MEDICOES_GESTAO.md` | Fluxo de obra, BM, frentes, MC, seleção de lançamentos e resumo. |

## Limite da migração

A migração torna o conhecimento navegável e rastreável. Ela não resolve lacunas funcionais, não reconcilia o documento legado e não transforma perguntas em decisões.

## Resultado esperado

Após a migração, a pasta modular terá fonte específica para Medições, e o legado continuará apenas como documento de transição até que sua reconciliação completa seja realizada em auditoria própria.
