# RBAC-005 — Associação de usuários operacionais às Roles

## Modelo

Usuário é a identidade operacional registrada em `usuarios_operacionais.csv`.
Role é uma função institucional de `roles.csv`. Permissão é uma decisão de
negócio documentada em `roles_permissoes.csv`. Associação é o vínculo explícito
entre `usuario_id` e `role_id`, registrado em `usuarios_roles.csv`.

“A associação Usuário → Role criada no RBAC-005 é administrativa e documental. Ela ainda não participa do login nem do cálculo de autorização.”

“Um usuário sem Role ou com Role vazia permanece sem acesso concedido pelo RBAC.”

## Persistência e histórico

A base possui `usuario_role_id` UUID imutável, `usuario_id`, `role_id`, estado,
datas e autoria. A identidade funcional é o par usuário + Role. Retirada ocorre
por inativação, nunca exclusão. Reativação preserva o UUID e a criação original,
atualizando somente estado, data e responsável. Um usuário pode manter várias
Roles independentes.

Todas as alterações exigem leitura confirmada de usuários, Roles e associações,
controle de concorrência por SHA e nova autorização imediatamente antes da
persistência. Falhas são fechadas e não viram bases vazias.

## Regras

- somente `usuario_id` operacional existente e ativo recebe nova Role;
- usuário inativo conserva histórico e pode perder associação existente;
- somente `role_id` existente e ativo pode ser atribuído;
- Role vazia é válida;
- APP_USERS, proprietário e superadmin não podem ser associados;
- duplicidade ativa é negada;
- login, nome, matrícula e perfil não inferem associação.

## Autoridade e interface

Somente superadmin ou proprietário com custódia recuperada administra vínculos,
por `pode_gerenciar_usuarios_roles()`. A seção **ROLES DOS USUÁRIOS** apresenta
identidade operacional, estado, histórico, autoria, Roles ativas e retiradas e
as permissões documentais da Role, sem exibir credenciais ou Secrets.

## Ausência de efeito operacional

O arquivo não é importado por login, `services/permissoes.py` ou decisão de
rotas. Não cria claims, não altera `session_state`, não substitui
`permissoes_usuarios.csv` e não integra Medições.

## Riscos residuais e próximos passos

As associações podem divergir da autorização efetiva enquanto as duas fontes
coexistirem. A futura ativação exigirá missão própria para cálculo, precedência,
escopo e migração, com homologação antes de qualquer efeito operacional.
