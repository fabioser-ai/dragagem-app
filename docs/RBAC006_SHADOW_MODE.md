# RBAC-006 — Cálculo em modo sombra

## Objetivo e isolamento

O Shadow Mode recebe snapshots confirmados de usuários operacionais,
associações, Roles, permissões das Roles, catálogo canônico e permissões
individuais vigentes. O fluxo é exclusivamente de leitura:

`Usuário → Roles ativas → permissões allow existentes no catálogo → conjunto deduplicado → comparação`

> O Shadow Mode calcula permissões, mas não participa da autorização do APP.

O serviço não consulta nem altera `session_state`, claims, login, rotas ou
persistência. `data/permissoes_usuarios.csv` e AC-001 a AC-003 continuam sendo
as fontes da autorização efetiva.

## Autorização efetiva e RBAC Shadow

- **Autorização efetiva:** decisões atuais do APP, inclusive curingas e escopo
  de obra, baseadas na autoridade central e em `permissoes_usuarios.csv`.
- **RBAC Shadow:** projeção diagnóstica das permissões específicas vinculadas às
  Roles do usuário. Seu resultado nunca é consumido por uma guarda.

A seção **DIAGNÓSTICO RBAC** fica dentro da Administração, já restrita a
superadmin ou proprietário com custódia administrativa, e não possui ações de
alteração.

## Status e ocorrências

- `IGUAL`: os conjuntos específicos comparados são idênticos;
- `DIVERGENTE`: existe diferença ou referência inválida;
- `SEM ROLE`: não existe associação ativa;
- `ROLE VAZIA`: todas as Roles ativas válidas do usuário não concedem permissões;
- `RBAC possui permissões a mais`: permissões calculadas ausentes no conjunto atual;
- `RBAC possui permissões a menos`: permissões atuais ausentes no conjunto calculado;
- `Permissão inexistente`: concessão da Role não pertence ao catálogo canônico ativo;
- `Role inexistente`: associação aponta para Role ausente ou inativa.

Permissões repetidas em várias Roles são deduplicadas.

## Limitações e próximos passos

A comparação preserva curingas atuais (`todos`) como chaves literais e não tenta
expandir seu significado. O RBAC documental também não modela escopo de obra.
Por isso, divergência é evidência para análise humana, não recomendação automática
de migração. Não há precedência `allow/deny`; somente concessões `allow` são
calculadas neste modo.

No estado inicial da `main`, `usuarios_operacionais.csv` não possui registros;
portanto, a quantidade real comparada é zero. Quando houver usuários e vínculos,
o diagnóstico será calculado em tempo de leitura. Qualquer ativação futura exige
missão própria, homologação das divergências e definição explícita de curingas,
escopo de obra e migração.
