# Auditoria Arquitetural — Administração

Data: 2026-07-11

## Status

- Auditoria concluída.
- Nenhum comportamento funcional foi alterado.
- Consolidação prevista em `docs/architecture/11_ADMINISTRACAO.md`.

## Escopo auditado

- entrada pelo menu e roteamento;
- restrição por `superadmin`;
- relação entre login, perfil global e permissões granulares;
- leitura e gravação de `data/permissoes_usuarios.csv`;
- inclusão, desativação e exclusão de permissões;
- vocabulário de módulos, recursos e permissões;
- efeitos sobre os demais módulos;
- tratamento de erros, concorrência e rastreabilidade.

## Componentes diretamente envolvidos

- `pages/menu.py`
- `app.py`
- `pages/administracao.py`
- `services/auth.py`
- `services/permissoes.py`
- `services/github.py`
- `data/permissoes_usuarios.csv`
- `APP_USERS` em `st.secrets`

## 1. O que foi aprendido

### 1.1 Entrada e autorização

O cartão Administração é exibido no menu somente quando `eh_superadmin()` retorna verdadeiro. A própria tela repete essa validação e interrompe a execução para qualquer outro perfil.

`eh_superadmin()` depende exclusivamente de `st.session_state.perfil`, preenchido no login a partir do campo `role` de `APP_USERS` em `st.secrets`.

Assim, possuir uma linha ampla em `data/permissoes_usuarios.csv` não concede acesso à Administração. O acesso depende do perfil global `superadmin`.

### 1.2 Escopo real do módulo

A tela não cria, remove, altera senha ou modifica perfil global de usuários. Ela administra somente linhas do arquivo `data/permissoes_usuarios.csv`.

As contas autenticáveis e seus atributos continuam em `APP_USERS`, fora desta interface. Portanto, existem duas fontes distintas:

- `APP_USERS`: identidade, senha, nome, matrícula e perfil global;
- `data/permissoes_usuarios.csv`: autorizações por módulo, recurso, permissão e obra.

A Administração não valida se o texto informado em `usuario` corresponde a uma conta existente em `APP_USERS`.

### 1.3 Modelo de permissão

O schema observado é:

- `usuario`;
- `modulo`;
- `recurso`;
- `permissao`;
- `obra_id`;
- `ativo`.

A tela oferece módulos predefinidos e recursos específicos apenas para Medições. Para os demais módulos, o recurso disponível é `todos`.

O campo `obra_id` é texto livre, com valor inicial `todas`.

A tela permite criar uma linha já inativa com `ativo = nao`.

### 1.4 Interpretação das permissões

`services/permissoes.py` normaliza textos para minúsculas e aceita como ativos os valores `sim`, `s`, `true`, `1` e `ativo`.

`pode_acessar_modulo()` considera apenas módulo e estado ativo. Recurso, permissão e obra não participam da decisão de exibir o módulo.

`pode_executar()` implementa a combinação granular de módulo, recurso, permissão e obra, com suporte ao curinga `todos` e ao curinga de obra `todas`.

`obras_permitidas()` retorna os valores de `obra_id` das linhas compatíveis.

Na busca executada durante esta auditoria, não foi localizado uso efetivo de `pode_executar()` fora de sua definição. Essa ausência já havia sido registrada na documentação legada e permanece válida para os arquivos observados.

### 1.5 Inclusão de permissões

Ao salvar uma nova permissão, a tela valida apenas que `usuario` não esteja vazio.

Não foi observada validação para:

- existência do usuário em `APP_USERS`;
- duplicidade exata da permissão;
- conflito entre linhas amplas e específicas;
- validade real do `obra_id`;
- coerência entre recurso e permissão;
- utilidade da permissão para o módulo selecionado.

Linhas duplicadas são aceitas.

### 1.6 Desativação e exclusão

A seleção da linha usa o índice atual do DataFrame incorporado a uma descrição textual.

Desativar altera `ativo` para `nao` e substitui o CSV inteiro.

Excluir remove a linha pelo índice, redefine os índices e substitui o CSV inteiro.

Não existe:

- confirmação antes de excluir;
- edição direta de uma linha;
- botão específico para reativar;
- registro de quem alterou;
- data da alteração;
- justificativa;
- histórico de versões dentro do domínio do aplicativo.

O histórico disponível é apenas o versionamento geral do arquivo no GitHub.

### 1.7 Persistência e falhas de leitura

`carregar_permissoes()` captura qualquer exceção e retorna um DataFrame vazio. Também completa colunas ausentes e restringe o retorno ao schema oficial.

Esse comportamento cria um risco relevante: se uma falha de leitura for interpretada como arquivo vazio e o superadmin salvar uma nova linha, a gravação poderá substituir o arquivo original por um DataFrame contendo somente os dados disponíveis naquela sessão.

`salvar_permissoes()` substitui integralmente o CSV, sem locking ou controle transacional. Alterações simultâneas podem sobrescrever umas às outras.

### 1.8 Dados atuais

O arquivo atual contém permissões amplas para Fabio e Ana, uma permissão de lançamento em uma obra específica para Gedeon, acesso a Férias para Karina e acesso a Prestação de Contas para Peba.

A linha ampla de Fabio no CSV não é a origem do acesso à Administração; esse acesso vem do perfil global `superadmin`.

## 2. O que ainda não foi compreendido

- Como as contas em `APP_USERS` são administradas operacionalmente hoje.
- Se Administração deve futuramente gerenciar também identidade, senha, matrícula, nome e perfil global.
- Se linhas duplicadas são toleradas intencionalmente.
- Se permissões granulares serão efetivamente aplicadas pelos módulos além de Medições.
- Qual deve ser a fonte oficial para validar `obra_id`.
- Se exclusões devem ser permitidas ou se apenas desativação deveria preservar histórico.
- Se um `admin` global deveria possuir algum acesso administrativo sem ser `superadmin`.
- Se a tela deve impedir que um superadmin remova permissões essenciais de outros usuários.

## 3. O que deve ser documentado

### Observações Técnicas propostas

- OT-061 — Administração gerencia autorizações, não contas de login.
- OT-062 — Perfil global e permissões granulares possuem fontes distintas.
- OT-063 — Acesso à Administração depende exclusivamente de `superadmin`.
- OT-064 — Inclusão de permissão não valida existência do usuário.
- OT-065 — Linhas duplicadas e conflitos de permissão são aceitos.
- OT-066 — `obra_id` é texto livre na Administração.
- OT-067 — Alterações não possuem metadados de auditoria próprios.
- OT-068 — Exclusão é imediata e sem confirmação.
- OT-069 — Falha de leitura pode ser confundida com arquivo vazio.
- OT-070 — Persistência substitui integralmente o arquivo de permissões.
- OT-071 — Vocabulário granular existe, mas uso efetivo permanece limitado.

### Perguntas em Aberto propostas

- PA-046 — Administração futura de contas em `APP_USERS`.
- PA-047 — Regra para duplicidades e conflitos de autorização.
- PA-048 — Fonte oficial e validação de `obra_id`.
- PA-049 — Necessidade de trilha de auditoria para permissões.
- PA-050 — Exclusão física versus desativação.
- PA-051 — Escopo administrativo do perfil global `admin`.
- PA-052 — Estratégia para falhas de leitura antes de gravações.
- PA-053 — Adoção efetiva de `pode_executar()` pelos módulos.

## 4. Baby step seguro

Antes de qualquer ampliação funcional, o menor passo seguro é impedir gravação após uma leitura ambígua ou malsucedida.

A camada de permissões deve distinguir claramente:

- arquivo válido e vazio;
- arquivo inexistente;
- erro de autenticação;
- erro de rede/API;
- CSV inválido.

A tela de Administração não deve permitir salvar, desativar ou excluir enquanto a leitura atual não tiver sido confirmada como válida.

Esse passo reduz o risco de perda integral das permissões sem alterar o modelo de autorização.