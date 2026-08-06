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
3. **PERMISSÕES RBAC** — catálogo canônico consultivo do modelo em preparação;
4. **DIAGNÓSTICO** — comparação global do Shadow Mode;
5. **ACESSO ATUAL** — modelo efetivo em uso hoje, protegido contra edição acidental.

## Ajuda e separação dos modelos

O cabeçalho apresenta **Mais informações** como documentação interna do módulo.
Ela explica finalidade, limites, fluxo recomendado, diferenças entre cadastro,
credencial, Role e permissão, convivência dos dois modelos, próximos passos e um
glossário curto. A interface também apresenta dois contextos visuais distintos:

- **ACESSO EM USO HOJE:** APP_USERS autentica as contas protegidas e as
  permissões efetivas atuais controlam a autorização;
- **NOVO MODELO POR ROLES — EM PREPARAÇÃO:** usuários operacionais, Roles,
  permissões calculadas e Shadow Mode ainda não alteram o acesso real.

> Hoje, o acesso real ainda é definido pelo modelo atual. O novo modelo de
> usuários operacionais, Roles e permissões está em preparação e ainda não
> substitui a autorização existente.

APP_USERS permanece visível conceitualmente porque ainda contém as contas
protegidas e credenciais existentes. Ele não é administrado pelos usuários
operacionais. O modelo atual não é escondido nem apresentado como já substituído.

## Jornada principal

`Voltar ao menu ou selecionar pessoa → visão geral → funções → acesso → histórico → detalhes técnicos`

A seleção do usuário é única. Busca, filtro e lista resumida precedem a ficha.
As ações de edição, ativação, inativação, atribuição e retirada permanecem no
contexto da pessoa selecionada. O cabeçalho usa o mesmo mecanismo de navegação
do APP (`session_state.tela = "menu"`) para retornar ao menu inicial, sem criar rota.

## Padrão visual administrativo

A página utiliza conceitualmente um padrão Object Page, sem dependência externa:

- cabeçalho do módulo com retorno, título, descrição e documentação interna;
- cabeçalho do usuário selecionado com nome, login e matrícula;
- cards/métricas para estados principais;
- navegação interna horizontal com uma seção visível por vez;
- consulta separada da edição;
- detalhes técnicos recolhidos;
- tabelas reservadas para listas, históricos, catálogos e comparações.

Não foi adicionado framework visual, tema global ou CSS. Os componentes nativos
do Streamlit preservam o empilhamento em telas estreitas, mas a experiência mobile
continua pendente de teste físico.

## Ficha consolidada

O topo da ficha resume cadastro, entrada no APP, credencial, quantidade de Roles,
fonte do acesso real e estado comparativo do novo RBAC. As ajudas deixam explícito
que cadastro ativo não significa entrada disponível e Role atribuída não significa
acesso liberado.

Além do significado conceitual, a ficha deriva explicações do estado concreto:

- cadastro ativo/inativo é explicado a partir do registro selecionado;
- ausência de entrada e credencial é vinculada à inexistência de autenticação operacional;
- quantidade de Roles é calculada pelas associações ativas;
- divergência descreve se o RBAC concederia a mais, a menos ou ambos;
- funções atribuídas são nomeadas sem sugerir efeito real.

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
- “O novo modelo concederia” substitui “RBAC a mais”.
- “O acesso atual possui, mas as Roles não concedem” substitui “RBAC a menos”.
- O e-mail é identificado como apenas cadastral.
- A criação informa que nenhum convite, senha ou credencial será produzido.
- A ativação informa que não habilita login.
- A inativação informa que não revoga sessões de `APP_USERS`.
- A retirada de Role exige confirmação e informa que o histórico é preservado.
- `usuario_id`, login, perfil-base, estado ativo, credencial configurada e troca
  de senha possuem explicações contextuais.
- A consulta das permissões atuais começa com edição desabilitada; qualquer
  alteração exige habilitação explícita.
- Tabelas administrativas usam `column_config` e `help` nos cabeçalhos não
  autoexplicativos, com legenda próxima quando necessário.

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

1. Confirmar que existe botão claro para voltar ao menu e que o retorno funciona.
2. Confirmar que **Mais informações** está visível no cabeçalho.
3. Entender a finalidade do módulo sem documentação externa.
4. Compreender cada coluna pelo tooltip ou ajuda próxima.
5. Entender por que cada estado da pessoa selecionada está como está.
6. Confirmar que os estados principais aparecem em cards, fora das tabelas.
7. Avaliar se a interface parece uma aplicação administrativa, não uma planilha.
8. Confirmar que consulta e edição estão claramente separadas.
9. Confirmar que a tela não promete credencial, e-mail ou acesso inexistente.
10. Avaliar a responsividade no desktop e registrar que aparelho real ainda será testado.

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
