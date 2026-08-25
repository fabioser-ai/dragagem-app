# UX-ACESSO-002 — Administração One Stop Shop

## Objetivo

Transformar Administração em uma entrada orientada a tarefas. A página inicial
pergunta o que o administrador deseja fazer e encaminha para uma única área, sem
exibir simultaneamente identidade, acesso efetivo, Roles, Shadow Mode e auditoria.

## Navegação

O fluxo possui no máximo três níveis:

1. Administração;
2. área escolhida;
3. tarefa ou pessoa selecionada.

Todas as áreas oferecem `← Voltar para Administração`. Ao sair para o menu inicial,
a área selecionada é limpa para que a próxima entrada comece novamente pelo one
stop shop.

## Inventário de preservação

| Função anterior | Nova localização |
|---|---|
| Listagem, busca e seleção de usuário | Pessoas |
| Cadastro e edição de identidade | Pessoas |
| Ativação e inativação | Pessoas |
| Estado observável da credencial e da entrada | Pessoas |
| Configuração ou redefinição de credencial | Pessoas |
| Consulta das permissões efetivas | Acessos |
| Inclusão, desativação e exclusão de regra efetiva | Acessos |
| Catálogo, criação e edição de Roles | Roles → Catálogo de Roles |
| Associação e retirada Pessoa → Role | Roles → Função de uma pessoa |
| Permissões documentais da Role | Roles → Catálogo de Roles |
| Comparação atual × Roles e ocorrências | Diagnóstico |
| Detalhes técnicos de identidade e associação | Diagnóstico → análise individual |
| Catálogo canônico de permissões | Diagnóstico → Catálogo técnico |
| Metadados de criação/alteração e histórico de funções | Auditoria |

Nenhuma capacidade existente foi removida. O histórico disponível continua sendo
o histórico já persistido nas identidades e associações de Roles; não foi criado
um novo sistema de logs.

## Invariantes

- `APP_USERS` e sua precedência não foram alterados.
- AUTH-002, bcrypt, sessão e fail-closed não foram alterados.
- `permissoes_usuarios.csv` continua sendo a autoridade efetiva.
- Roles continuam documentais e não concedem acesso real.
- O Shadow Mode continua somente diagnóstico.
- Serviços de persistência e regras de negócio não foram modificados.

## Homologação visual

1. Entre em Administração e confirme as cinco áreas, sem tabelas técnicas abertas.
2. Abra Pessoas, localize um usuário e confirme cadastro, credencial e entrada no APP.
3. Edite um dado não crítico e confirme que ativação/inativação e credencial permanecem disponíveis.
4. Volte à Administração, abra Acessos e selecione `TESTE`; confira módulos permitidos,
   módulos sem acesso e as regras efetivas detalhadas.
5. Habilite a edição apenas para confirmar que os controles existentes aparecem;
   não salve uma alteração sem necessidade.
6. Abra Roles, associe ou retire uma função de teste e confirme o aviso discreto de
   que a Role não altera o acesso real.
7. Abra Diagnóstico e confira o Shadow Mode, a análise individual e o catálogo técnico.
8. Abra Auditoria e confira os metadados e o histórico de funções da pessoa.
9. Use `← Voltar para Administração` em cada área e confirme o retorno à entrada.
10. Saia para o menu inicial, entre novamente em Administração e confirme que a tela
    volta a perguntar o que deseja fazer.
