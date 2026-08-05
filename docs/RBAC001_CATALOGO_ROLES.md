# RBAC-001 — Catálogo de Roles

## Filosofia

O RBAC do APP FOS adota Roles reutilizáveis para agrupar permissões explícitas
por módulo, recurso e ação. Ele não busca reproduzir a complexidade do SAP.
Prioriza simplicidade, rastreabilidade, negação por padrão e poucos conceitos.

> O objetivo deste RBAC é manter o sistema simples.
>
> Sempre que uma decisão puder ser tomada entre maior flexibilidade ou menor complexidade, optar pela menor complexidade.

## Modelo

Uma Role descreve uma função institucional reutilizável. Um usuário representa
uma identidade individual. Não existe vínculo usuário → Role no RBAC-001.

Uma permissão responde explicitamente: quem (a Role) pode fazer o quê (ação),
em qual módulo e sobre qual recurso. O efeito é textual: `allow` ou `deny`.
Não há regra implícita, herança, composição, precedência ou escopo por obra.

Os catálogos são:

- `data/roles.csv`: identidade, descrição, estado, versão e autoria da Role;
- `data/roles_permissoes.csv`: `role_id`, módulo, recurso, ação e efeito.

As ações válidas nesta fase são apenas: `visualizar`, `criar`, `editar`,
`excluir`, `aprovar`, `cancelar` e `administrar`.

## Roles institucionais iniciais

O catálogo nasce com seis Roles: `FUNCIONARIO`, `ENCARREGADO`, `APROVADOR`,
`ENGENHARIA`, `FINANCEIRO` e `RH`. O catálogo de permissões nasce vazio; assim,
nenhuma Role concede acesso por sua simples existência.

Roles novas são criadas inativas. O UUID e o código são imutáveis. Edições
incrementam a versão. Não há exclusão física, somente ativação e inativação.

## Autoridade administrativa

Somente superadmin ou proprietário com custódia administrativa recuperada pode
gerenciar Roles, por `pode_gerenciar_roles()`. A autorização é revalidada
imediatamente antes da persistência, que exige o SHA da leitura confirmada.

`SUPERADMIN`, `OWNER`, `PROPRIETARIO`, `ROOT`, `SYSTEM` e equivalentes são
reservados. Superadmin é autoridade técnica global, não uma função reutilizável.
O proprietário representa custódia canônica e permanente; portanto também
permanece fora do catálogo de Roles.

## Limites e riscos residuais

- Nenhum usuário utiliza Roles neste passo.
- O catálogo ainda não participa do login ou do cálculo de permissões.
- As permissões das Roles são apenas visualizadas e permanecem vazias.
- As permissões atuais em `data/permissoes_usuarios.csv` continuam sendo a fonte vigente.
- Conflitos, precedência, herança e escopo por obra não existem nesta fase.
- RBAC-002 deverá criar o vínculo usuário → Role sem promover migração implícita.
