# Arquitetura Atual — Medições: Aprovação

Última atualização: 2026-07-11

Fonte: `docs/ARCHITECTURE_CURRENT.md` e `docs/audit/AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md`.

## Entrada e escopo

O fluxo `aprovacao` exige `pode_aprovar_lancamentos()` e é destinado a `aprovador` e `admin`. A tela carrega `lancamentos_trabalho.csv` e mostra lançamentos com `status_aprovacao = pendente`.

Não foi observado filtro por obra vinculada, autor, data do serviço ou status de medição. O filtro visual usa `nome_obra`, não `obra_id`.

## Decisões

Ao aprovar, grava `status_aprovacao = aprovado`, responsável, data e atualização. Ao reprovar, grava o mesmo conjunto de campos, mudando apenas o status.

`status_medicao` não muda em nenhuma decisão. Portanto, aprovado permanece elegível para gestão; reprovado deixa de ser elegível.

## Persistência e limites

- a tela atualiza o DataFrame diretamente e regrava o CSV inteiro;
- o serviço existente de atualização não é usado;
- o retorno do salvamento não é verificado antes da mensagem de sucesso;
- reprovação não tem responsável, data ou justificativa em campos próprios;
- não há saída explícita para o início de Medições; o rerun preserva o fluxo de aprovação.
