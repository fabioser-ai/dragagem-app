# UX-ACESSO-001 — Ficha consolidada do usuário

## Objetivo

Reorganizar a Administração de identidade e acesso em torno da pessoa
administrada, preservando integralmente autorização, persistência, dados e o
caráter diagnóstico do RBAC.

> A reorganização do UX-ACESSO-001 não cria credenciais nem altera acesso efetivo.

> O usuário operacional ativo e com Role continua sem capacidade de login até a
> implementação e homologação da autenticação operacional.

## Estrutura anterior

A página apresentava, em uma única sequência vertical, catálogo de permissões,
Roles, usuários operacionais, associações Usuário → Role, diagnóstico RBAC e
permissões legadas. A mesma pessoa precisava ser selecionada novamente em
seções distantes, e conceitos técnicos apareciam antes da tarefa administrativa.

## Estrutura nova

A Administração passa a possuir cinco áreas:

1. **USUÁRIOS** — jornada principal e ficha consolidada;
2. **ROLES** — catálogo institucional, vínculos e permissões;
3. **PERMISSÕES** — catálogo canônico consultivo;
4. **DIAGNÓSTICO** — comparação global do Shadow Mode;
5. **AVANÇADO** — permissões efetivas legadas e operações técnicas.

## Jornada principal

`Selecionar pessoa → identidade → estado → funções → acesso → auditoria`

A seleção do usuário é única. Busca, filtro e lista resumida precedem a ficha.
As ações de edição, ativação, inativação, atribuição e retirada permanecem no
contexto da pessoa selecionada.

## Ficha consolidada

- **Identidade:** nome, login, matrícula, e-mail cadastral, perfil-base e UUID
  recolhido em detalhe técnico.
- **Estado:** cadastro ativo/inativo, impossibilidade atual de login, ausência de
  credencial e estado informativo de troca de senha.
- **Funções:** ativas e retiradas, objetivo, quantidade/resumo de permissões e
  indicação explícita de Role vazia.
- **Acesso:** permissões efetivas, calculadas pelas Roles, diferenças e status do
  Shadow Mode em linguagem administrativa.
- **Auditoria:** autoria, datas e histórico técnico das associações.

## Linguagem e mensagens

- “Funções atribuídas ao usuário” substitui “Associação Usuário → Role”.
- “O acesso por Roles concederia” substitui “RBAC a mais”.
- “O acesso atual possui, mas as Roles não concedem” substitui “RBAC a menos”.
- O e-mail é identificado como apenas cadastral.
- A criação informa que nenhum convite, senha ou credencial será produzido.
- A ativação informa que não habilita login.
- A inativação informa que não revoga sessões de `APP_USERS`.
- A retirada de Role exige confirmação e informa que o histórico é preservado.

## Segurança preservada

Não foram alterados serviços, contratos de persistência, fontes de dados ou
regras de autorização. Todas as gravações continuam usando as guardas centrais,
leitura confirmada, SHA observado, negação por padrão, autoria e timestamps.
Falha de leitura bloqueia a ficha e suas ações.

## Limites deste PR

Não foram implementados autenticação operacional, senha, hash, convite, e-mail,
primeiro acesso, reset, troca obrigatória, revogação de sessão, MFA, ativação do
RBAC, precedência, escopo por obra, migração de permissões ou integração de
Medições.

## Roteiro de homologação visual

1. Abrir Administração e confirmar as cinco abas.
2. Na aba USUÁRIOS, localizar o usuário TESTE por busca ou seleção.
3. Identificar rapidamente se o cadastro está ativo.
4. Confirmar a mensagem de que o usuário ainda não pode entrar no APP.
5. Conferir identidade e e-mail apenas cadastral.
6. Conferir a função FUNCIONARIO, seu objetivo e permissões.
7. Conferir o acesso atual e o calculado pelas Roles.
8. Verificar se a divergência é compreensível sem interpretar chaves técnicas.
9. Se autorizado para o teste, retirar e reatribuir FUNCIONARIO usando as
   confirmações apresentadas.
10. Confirmar que o histórico da associação foi preservado.

A homologação visual depende do proprietário após a publicação do Draft PR.

## Pendências para AUTH-002

- modelo seguro de credenciais com hash;
- primeiro acesso sem transmissão de senha em claro;
- reset e troca obrigatória;
- revogação e inativação efetiva;
- integração homologada do usuário operacional ao login;
- auditoria dos eventos de credencial.

## Riscos residuais

- usuários operacionais continuam sem capacidade de autenticação;
- Roles continuam sem efeito real;
- permissões legadas e RBAC coexistem;
- a responsividade deve ser homologada em celular real;
- o escopo dos dados do primeiro piloto ainda exige decisão humana.
