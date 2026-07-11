# Arquitetura Atual — Administração

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_037_ADMINISTRACAO.md`

## Visão geral

O módulo Administração gerencia autorizações armazenadas em `data/permissoes_usuarios.csv`. Ele não gerencia contas autenticáveis, senhas, nomes, matrículas ou perfis globais, que permanecem em `APP_USERS` dentro de `st.secrets`.

Arquivos principais:

- `pages/administracao.py`
- `services/permissoes.py`
- `services/auth.py`
- `services/github.py`
- `pages/menu.py`
- `app.py`

Arquivo de dados:

- `data/permissoes_usuarios.csv`

## Entrada e autorização

O menu principal exibe Administração somente quando `eh_superadmin()` retorna verdadeiro.

A própria tela repete a verificação e interrompe a execução para qualquer perfil diferente de `superadmin`.

`eh_superadmin()` depende exclusivamente do perfil global armazenado em `st.session_state.perfil`, preenchido no login a partir de `APP_USERS`.

Uma permissão ampla no CSV não concede acesso ao módulo Administração.

## Duas fontes de controle de acesso

O sistema mantém duas fontes distintas:

### Identidade e perfil global

Fonte:

- `APP_USERS` em `st.secrets`.

Dados observados:

- usuário;
- senha;
- nome;
- matrícula;
- perfil global.

### Permissões granulares

Fonte:

- `data/permissoes_usuarios.csv`.

Schema:

- `usuario`;
- `modulo`;
- `recurso`;
- `permissao`;
- `obra_id`;
- `ativo`.

A tela Administração atua somente sobre a segunda fonte.

## Modelo de autorização

`services/permissoes.py` oferece:

- `eh_superadmin()`;
- `permissoes_usuario()`;
- `pode_acessar_modulo()`;
- `pode_executar()`;
- `obras_permitidas()`.

O perfil `superadmin` recebe retorno verdadeiro diretamente nas verificações gerais.

`pode_acessar_modulo()` considera apenas módulo e estado ativo. Recurso, ação e obra não participam da decisão de exibir o módulo.

`pode_executar()` combina módulo, recurso, permissão e obra, aceitando os curingas `todos` e `todas`.

`obras_permitidas()` lista os valores de `obra_id` das linhas compatíveis.

O uso efetivo de `pode_executar()` fora da própria definição não foi confirmado nos arquivos observados.

## Interface administrativa

A tela apresenta:

- tabela integral de permissões;
- formulário de inclusão;
- controle de desativação;
- controle de exclusão física de linha.

Módulos disponíveis no formulário:

- medições;
- férias;
- prestação de contas;
- orçamento;
- CRM;
- obras;
- dados;
- todos.

Somente Medições apresenta recursos específicos na interface. Os demais módulos usam `todos`.

Permissões oferecidas:

- visualizar;
- lançar;
- criar;
- editar;
- aprovar;
- excluir;
- todos.

`obra_id` é informado como texto livre e assume `todas` quando vazio.

## Inclusão

A inclusão valida somente que o campo usuário não esteja vazio.

Não existe validação observada para:

- existência do usuário em `APP_USERS`;
- duplicidade;
- conflito entre linhas amplas e específicas;
- validade de `obra_id`;
- coerência entre recurso, permissão e módulo.

A tela permite criar uma permissão já inativa.

## Desativação e exclusão

A linha é selecionada pelo índice atual do DataFrame.

Desativar altera `ativo` para `nao`.

Excluir remove fisicamente a linha e redefine os índices.

Não existem campos próprios para:

- autor da alteração;
- data da alteração;
- justificativa;
- histórico de transições.

Não há confirmação antes da exclusão nem controle específico para reativação ou edição direta.

## Persistência

`carregar_permissoes()` captura exceções de leitura e retorna DataFrame vazio. Também cria colunas ausentes e restringe o resultado ao schema oficial.

`salvar_permissoes()` substitui integralmente `data/permissoes_usuarios.csv` usando o serviço central do GitHub.

Consequências observadas:

- uma falha de leitura pode ser confundida com arquivo realmente vazio;
- uma gravação posterior pode substituir o arquivo por um conjunto incompleto de linhas;
- alterações simultâneas podem sobrescrever umas às outras;
- não existe locking ou transação.

## Dados atuais

O arquivo atual contém:

- Fabio com permissão ampla;
- Ana com permissão ampla;
- Gedeon com lançamento em uma obra específica de Medições;
- Karina com acesso a Férias;
- Peba com acesso a Prestação de Contas.

A linha de Fabio no CSV não é a origem do acesso à Administração. Esse acesso vem do perfil global `superadmin`.

## Observações Técnicas

### OT-061 — Administração gerencia autorizações, não contas

A interface altera somente `data/permissoes_usuarios.csv`. Contas, senhas e perfis globais permanecem em `APP_USERS`.

### OT-062 — Duas fontes distintas de acesso

Perfil global e permissões granulares são armazenados e administrados separadamente.

### OT-063 — Administração depende exclusivamente de `superadmin`

Acesso ao módulo não pode ser concedido por uma linha no CSV de permissões.

### OT-064 — Usuário informado não é validado

A tela aceita texto que não corresponda a uma conta existente.

### OT-065 — Duplicidades e conflitos são permitidos

Não existe prevenção de linhas idênticas ou combinações sobrepostas.

### OT-066 — `obra_id` é texto livre

A interface não cruza o valor informado com cadastro oficial de obras.

### OT-067 — Alterações sem metadados próprios

O domínio não registra autor, data ou motivo de inclusão, desativação ou exclusão.

### OT-068 — Exclusão imediata

A remoção física ocorre sem confirmação adicional.

### OT-069 — Erro de leitura pode parecer arquivo vazio

`carregar_permissoes()` converte exceções em DataFrame vazio.

### OT-070 — Substituição integral do CSV

Toda alteração regrava o arquivo completo.

### OT-071 — Granularidade disponível sem adoção confirmada

`pode_executar()` implementa autorização granular, mas seu uso efetivo permanece não confirmado nos demais módulos observados.

## Perguntas em Aberto

### PA-046 — Administração de contas

Definir se a interface deverá futuramente administrar também `APP_USERS`.

### PA-047 — Duplicidades e conflitos

Definir precedência e validação para permissões amplas, específicas e repetidas.

### PA-048 — Validação de obra

Definir qual cadastro deve ser a fonte oficial para `obra_id`.

### PA-049 — Trilha de auditoria

Definir se alterações de permissão precisam de autor, data, justificativa e histórico.

### PA-050 — Exclusão ou desativação

Definir se exclusão física deve permanecer permitida.

### PA-051 — Papel do perfil `admin`

Definir se um `admin` global deve possuir algum acesso administrativo sem ser `superadmin`.

### PA-052 — Falhas de leitura

Definir como impedir gravações quando a leitura atual do arquivo não puder ser confirmada.

### PA-053 — Uso de `pode_executar()`

Definir quais módulos devem adotar a autorização granular.

## Baby step seguro

O primeiro passo futuro deve impedir qualquer escrita administrativa após leitura ambígua ou malsucedida.

A camada deve diferenciar arquivo vazio válido de arquivo inexistente, erro de autenticação, erro de rede/API e CSV inválido. Enquanto a leitura não estiver confirmada, a tela não deve permitir inclusão, desativação ou exclusão.