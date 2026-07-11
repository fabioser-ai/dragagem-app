# Arquitetura Atual — Medições: Lançamentos

Última atualização: 2026-07-11

Fonte: `docs/ARCHITECTURE_CURRENT.md` e `docs/audit/AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md`.

## Fluxo observado

O fluxo `lancamento` exige `pode_lancar_trabalho()`. A tela identifica o usuário, carrega obras e vínculos, seleciona local ativo e item contratual, recebe quantidade, data, observação e fotografia opcional e chama `criar_lancamento_trabalho()`.

O registro entra em `data/medicoes/lancamentos_trabalho.csv` com aprovação pendente e status de medição ainda não medido.

## Evidências e limites

- A fotografia pode ser recebida pelo uploader, mas o fluxo registrado guarda apenas o nome em `foto_url`; a função de salvar bytes não é chamada nesse fluxo.
- O sucesso visual não confirma persistência quando o wrapper retorna falha e esse retorno não é verificado.
- A filtragem de obras usa vínculos e perfil interno; há fatos registrados de que aprovador/admin podem receber todas as obras e de que obras não são filtradas por status.
- O lançamento depende de identidade de obra, local e item contratual. A definição canônica do identificador contratual permanece em aberto.

## Relação com aprovação e gestão

Lançamento pendente segue para aprovação. Aprovado permanece `nao_medido` e torna-se elegível para a seleção no fluxo de gestão. A vinculação efetiva ao BM não é persistida pelo fluxo de gestão auditado.
