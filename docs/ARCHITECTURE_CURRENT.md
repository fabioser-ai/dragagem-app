# APP FOS — ARCHITECTURE CURRENT

Status:
Em construção.

Última atualização:
2026-07-08

---

# Objetivo

Este documento descreve como o APP FOS funciona atualmente.

Ele documenta apenas fatos observados no código.

Ele NÃO tenta explicar os motivos históricos das decisões.

Quando um motivo histórico for confirmado pelo Fabio, ele será registrado posteriormente em um ADR (Architecture Decision Record).

---

# Organização deste documento

1. Visão Geral
2. Inicialização
3. Autenticação
4. Interface
5. Persistência
6. Permissões
7. Módulos
8. Fluxos
9. Observações Técnicas
10. Perguntas em Aberto


# 1. Visão Geral

O APP FOS é uma aplicação desenvolvida em Streamlit.

A navegação é controlada através de `st.session_state.tela`.

O ponto de entrada principal é `app.py`.

Fluxo simplificado:

Usuário
↓

Login

↓

Aplicação do estilo visual

↓

Menu Principal

↓

Módulo selecionado

↓

Leitura e gravação de dados em arquivos CSV armazenados no GitHub.


# 2. Inicialização

Responsável:

app.py

Responsabilidades observadas:

- Configurar a página Streamlit.
- Executar autenticação.
- Aplicar estilo visual global.
- Inicializar a tela principal.
- Controlar o roteamento entre módulos.
- Aplicar restrições por perfil.

Observação:

O aplicativo utiliza `st.session_state.tela` como mecanismo central de navegação.

# 3. Autenticação

Arquivo principal:

services/auth.py

Funcionamento observado:

- Usuários são carregados através de APP_USERS em st.secrets.
- A sessão armazena:
    - usuário
    - nome
    - perfil
    - matrícula
    - último acesso
- Existe timeout de sessão.
- Eventos importantes geram registro em log.

Observação:

As senhas atualmente são comparadas diretamente com os valores armazenados em APP_USERS.

Motivo histórico:

DESCONHECIDO.


# 4. Interface

Arquivo principal:

services/ui.py

Responsabilidade:

Aplicar CSS global ao Streamlit.

Características observadas:

- Tema claro.
- Correção de contraste.
- Ajustes de botões.
- Ajustes de tabelas.
- Ajustes para melhor legibilidade.

Motivo histórico provável:

Melhorar a experiência de uso em dispositivos móveis.

Status:

A confirmar.



# 5. Persistência

## Visão Geral

O APP FOS utiliza arquivos CSV armazenados diretamente no repositório GitHub como mecanismo principal de persistência.

O GitHub atua como repositório de dados da aplicação.

Não existe atualmente um banco de dados relacional.

---

## Serviço responsável

Arquivo:

services/github.py

Este serviço centraliza a comunicação direta com a GitHub Contents API.

Toda leitura e gravação de dados deve passar por esse serviço ou por wrappers internos de módulos que chamam esse serviço.

---

## Operações principais

Foram identificadas as seguintes responsabilidades:

- carregar arquivos CSV
- salvar arquivos CSV
- carregar arquivos binários
- salvar arquivos binários

Funções observadas:

- salvar_github(df, arquivo, token, repo)
- carregar_github(arquivo, token, repo)
- salvar_arquivo_github(conteudo_bytes, arquivo, token, repo, mensagem=None)
- carregar_arquivo_github(arquivo, token, repo)

---

## Funcionamento de CSV

### Leitura

Fluxo observado em `carregar_github()`:

1. Monta URL da GitHub Contents API usando repo e caminho do arquivo.
2. Faz GET autenticado com token.
3. Se a resposta não for 200, retorna DataFrame vazio.
4. Obtém o campo `content` retornado pela API.
5. Decodifica o conteúdo base64.
6. Lê o CSV com pandas.
7. Retorna um DataFrame.

Observação:

A função não diferencia, no retorno, arquivo inexistente, erro de autenticação, erro de rede ou CSV vazio. Nesses casos, o comportamento observado é retornar DataFrame vazio quando o status não é 200.

### Gravação

Fluxo observado em `salvar_github()`:

1. Monta URL da GitHub Contents API usando repo e caminho do arquivo.
2. Faz GET para descobrir o SHA atual do arquivo.
3. Converte o DataFrame para CSV sem índice.
4. Codifica o CSV em base64.
5. Faz PUT na GitHub Contents API.
6. Se o arquivo já existir, envia o SHA obtido.
7. Se a resposta não for 200 ou 201, lança exceção.

Observação:

A gravação substitui o arquivo inteiro.

---

## Funcionamento de arquivos binários

### Gravação

Fluxo observado em `salvar_arquivo_github()`:

1. Monta URL da GitHub Contents API usando repo e caminho do arquivo.
2. Faz GET para descobrir o SHA atual do arquivo, se existir.
3. Codifica os bytes em base64.
4. Faz PUT na GitHub Contents API.
5. Se a resposta não for 200 ou 201, lança exceção.
6. Retorna o caminho do arquivo.

Uso observado:

- Prestação de Contas salva comprovantes em `data/comprovantes`.
- Medições salva fotos de lançamentos em `data/medicoes/fotos_lancamentos`.

### Leitura

Fluxo observado em `carregar_arquivo_github()`:

1. Monta URL da GitHub Contents API usando repo e caminho do arquivo.
2. Faz GET autenticado.
3. Se a resposta não for 200, retorna None.
4. Se houver `download_url`, baixa o conteúdo bruto.
5. Se não houver `download_url`, usa fallback para decodificar o campo `content` em base64.
6. Retorna bytes ou None.

---

## Estrutura dos dados

Os módulos armazenam seus dados em arquivos CSV.

Exemplos:

data/orcamentos.csv

data/permissoes_usuarios.csv

data/log_acessos.csv

data/crm/

data/medicoes/

Cada módulo é responsável apenas pelo conteúdo de seus próprios arquivos.

---

## Wrappers por módulo

Além do serviço central, alguns módulos possuem wrappers próprios para padronizar colunas e tratamento de erro.

Exemplos observados:

- `services/permissoes.py` usa `carregar_github()` e `salvar_github()` para `data/permissoes_usuarios.csv`.
- `services/log.py` usa `carregar_github()` e `salvar_github()` para `data/log_acessos.csv`.
- `modulos/medicoes/repositorio.py` define `carregar_csv()` e `salvar_csv()` sobre o serviço central.
- `modulos/medicoes/lancamentos/repositorio.py` também define wrappers próprios de CSV sobre o serviço central.
- `pages/prestacao_contas.py` chama diretamente as funções do serviço central para CSV e arquivos binários.

Observação:

Existe mais de um wrapper de CSV no sistema. Eles têm a mesma intenção geral, mas não são uma única abstração compartilhada.

---

## Funcionamento

Fluxo simplificado:

Tela

↓

DataFrame (pandas)

↓

Wrapper do módulo, quando existe

↓

services/github.py

↓

GitHub Contents API

↓

Arquivo CSV ou arquivo binário no repositório

---

## Vantagens observadas

Arquitetura simples.

Baixo custo operacional.

Deploy simples utilizando Streamlit Cloud.

Versionamento automático através do GitHub.

Facilidade para backup.

Estrutura facilmente compreendida.

---

## Limitações observadas

Não existe controle transacional.

Gravações simultâneas podem gerar conflitos.

Arquivos CSV tendem a crescer continuamente.

Não existe mecanismo de locking.

A gravação de CSV substitui o arquivo inteiro.

A leitura de CSV retorna DataFrame vazio quando a resposta HTTP não é 200, sem expor a causa para o chamador.

Não foi observado mecanismo central de retry para falhas temporárias de rede ou API.

Existem wrappers de CSV duplicados em módulos diferentes.

---

## Motivo histórico

DESCONHECIDO.

Hipótese:

A arquitetura foi escolhida para manter simplicidade operacional durante o desenvolvimento inicial.

Status:

A confirmar.


# 6. Permissões

## Visão geral

O APP FOS possui mais de uma camada de autorização observada no código.

Até esta auditoria, foram identificadas duas camadas principais:

1. Permissão geral do aplicativo.
2. Permissão específica do módulo Medições.

Essas camadas não são equivalentes.

---

## 6.1 Permissão geral do aplicativo

Arquivo principal:

services/permissoes.py

Arquivo de dados:

data/permissoes_usuarios.csv

Colunas esperadas:

- usuario
- modulo
- recurso
- permissao
- obra_id
- ativo

Responsabilidades observadas:

- Carregar permissões gerais do usuário.
- Normalizar textos para comparação.
- Identificar se o perfil global do usuário é superadmin.
- Verificar se o usuário pode acessar um módulo.
- Verificar permissões por módulo, recurso, permissão e obra.
- Listar obras permitidas conforme filtros.

Funções observadas:

- eh_superadmin()
- pode_acessar_modulo(modulo)
- pode_executar(modulo, recurso, permissao, obra_id)
- obras_permitidas(modulo, recurso, permissao)

Funcionamento observado:

- O perfil global `superadmin` retorna acesso verdadeiro nas verificações gerais.
- `pode_acessar_modulo()` verifica apenas se existe permissão ativa para o módulo informado ou para `todos`.
- `pode_executar()` possui lógica mais granular, cruzando módulo, recurso, permissão e obra.
- `obras_permitidas()` retorna `['todas']` para superadmin.

Uso efetivo observado:

- O menu principal utiliza `pode_acessar_modulo()` para decidir quais módulos aparecem para o usuário.
- O menu principal utiliza `eh_superadmin()` para exibir o módulo Administração.
- A tela de Administração usa `eh_superadmin()` para restringir acesso à gestão de permissões.

Status de `pode_executar()`:

- A função existe e implementa regra granular.
- Nesta auditoria, seu uso efetivo ainda não foi confirmado nos arquivos centrais analisados.
- A autorização atualmente observada depende principalmente de `pode_acessar_modulo()` no menu, combinada com regras específicas dentro de cada módulo.

---

## 6.2 Administração de permissões

Arquivo principal:

pages/administracao.py

Responsabilidades observadas:

- Exibir permissões cadastradas.
- Criar novas permissões.
- Desativar permissões existentes.
- Excluir linhas de permissão.

Restrição de acesso observada:

- Apenas usuários com perfil global `superadmin` acessam a tela de Administração.

Observação:

O perfil `superadmin` pertence à camada global do aplicativo.
Ele não deve ser confundido com o perfil `admin` do módulo Medições.

---

## 6.3 Permissões específicas do módulo Medições

Arquivo principal:

modulos/medicoes/permissoes.py

Arquivo de dados:

data/medicoes/usuarios_obras.csv

Colunas esperadas:

- usuario_id
- email
- nome
- obra_id
- perfil_medicao
- ativo

Responsabilidades observadas:

- Identificar o usuário logado a partir de chaves existentes em `st.session_state`.
- Carregar vínculos ativos entre usuário e obra.
- Aceitar correspondência por usuario_id, email ou nome.
- Determinar o maior perfil de medição do usuário.
- Autorizar fluxos internos do módulo Medições conforme perfil.

Perfis observados em Medições:

- funcionario
- encarregado
- aprovador
- admin

Hierarquia observada:

admin > aprovador > encarregado > funcionario

Permissões internas observadas:

- `funcionario`, `encarregado`, `aprovador` e `admin` podem lançar trabalho.
- `encarregado`, `aprovador` e `admin` podem visualizar lançamentos.
- `aprovador` e `admin` podem aprovar lançamentos.
- Apenas `admin` pode criar ou gerenciar medição.

Observação:

O perfil `admin` de Medições é específico do módulo Medições.
Ele não equivale automaticamente ao perfil global `superadmin`.

---

## 6.4 Relação entre permissão global e Medições

Fluxo observado:

1. O menu principal usa a permissão geral para decidir se o módulo Medições aparece.
2. Ao entrar em Medições, o próprio módulo valida se o usuário possui vínculo ativo em `usuarios_obras.csv`.
3. O perfil interno de Medições decide quais fluxos aparecem ou são executáveis.

Consequência observada:

Ter acesso geral ao módulo Medições não significa, sozinho, ter acesso operacional interno às funções de Medições.

Da mesma forma, o funcionamento interno de Medições depende dos vínculos definidos em `data/medicoes/usuarios_obras.csv`.

---

# 7. Módulos

## 7.1 Módulo Medições — Repositórios

### Visão geral

O módulo Medições possui repositórios próprios acima de `services/github.py`.

Esses repositórios não substituem o serviço central de GitHub. Eles funcionam como camadas intermediárias para:

- definir quais arquivos CSV pertencem ao módulo;
- aplicar schemas de colunas esperadas;
- retornar DataFrames com colunas normalizadas;
- encapsular operações específicas do domínio de Medições.

Arquivos principais observados:

- `modulos/medicoes/repositorio.py`
- `modulos/medicoes/lancamentos/repositorio.py`
- `modulos/medicoes/config.py`
- `modulos/medicoes/lancamentos/config.py`

---

### 7.1.1 Configuração central de Medições

Arquivo:

`modulos/medicoes/config.py`

Responsabilidades observadas:

- Declarar caminhos dos arquivos usados pelo módulo Medições.
- Declarar modelos de medição.
- Declarar etapas por modelo.
- Declarar colunas esperadas dos CSVs.
- Declarar status usados em lançamentos.
- Declarar perfis de Medições.

Arquivos de dados observados:

- `data/obras.csv`
- `data/medicoes/medicoes.csv`
- `data/medicoes/medicao.csv`
- `data/medicoes/frentes.csv`
- `data/medicoes/mc.csv`
- `data/medicoes/itens.csv`
- `data/medicoes/servicos.csv`
- `data/medicoes_tabelas/`
- `data/medicoes/locais_trabalho.csv`
- `data/medicoes/lancamentos_trabalho.csv`
- `data/medicoes/usuarios_obras.csv`

Observação:

`data/obras.csv` é tratado como cadastro geral de obras, mas é consumido diretamente pelo módulo Medições.

---

### 7.1.2 Repositório geral de Medições

Arquivo:

`modulos/medicoes/repositorio.py`

Responsabilidades observadas:

- Definir wrappers genéricos `carregar_csv()` e `salvar_csv()` sobre `services/github.py`.
- Carregar bases principais do fluxo de gestão de Medições.
- Carregar vínculos de usuários com obras.
- Carregar tabela contratual por obra.
- Carregar e salvar locais de trabalho.
- Carregar lançamentos de produção.
- Salvar fotos de lançamentos.
- Manter temporariamente função legada de salvamento de lançamento de produção.

Funções observadas:

- `carregar_csv(caminho, colunas)`
- `salvar_csv(caminho, df)`
- `carregar_bases()`
- `carregar_usuarios_obras()`
- `carregar_tabela_contrato(nome_arquivo)`
- `carregar_locais_trabalho()`
- `salvar_locais_trabalho(df)`
- `carregar_lancamentos_producao()`
- `salvar_foto_lancamento(id_lancamento, foto)`
- `salvar_lancamento_producao(dados, foto=None)`

Uso observado:

- `pages/medicoes.py` importa `carregar_bases()` para carregar obras, medições, frentes, MC, itens e serviços antes de renderizar o fluxo de gestão.
- `modulos/medicoes/permissoes.py` usa `carregar_usuarios_obras()` para validar acesso interno ao módulo Medições.

Observação importante:

O próprio arquivo marca `salvar_lancamento_producao()` como legado e orienta que o fluxo oficial atual deve usar `modulos.medicoes.lancamentos.servicos.criar_lancamento_trabalho`.

---

### 7.1.3 Repositório de lançamentos de Medições

Arquivo:

`modulos/medicoes/lancamentos/repositorio.py`

Responsabilidades observadas:

- Definir wrappers próprios `carregar_csv()` e `salvar_csv()` sobre `services/github.py`.
- Carregar e salvar lançamentos de trabalho.
- Carregar e salvar locais de trabalho.
- Listar locais ativos por obra.
- Buscar local por ID.
- Criar local de trabalho.
- Carregar e salvar vínculos de usuários com obras.

Funções observadas:

- `carregar_csv(caminho, colunas)`
- `salvar_csv(caminho, df)`
- `carregar_lancamentos_trabalho()`
- `salvar_lancamentos_trabalho(df)`
- `carregar_locais_trabalho()`
- `salvar_locais_trabalho(df)`
- `listar_locais_por_obra(obra_id)`
- `buscar_local_por_id(local_id)`
- `criar_local_trabalho(obra_id, nome_local, observacoes='')`
- `carregar_usuarios_obras()`
- `salvar_usuarios_obras(df)`

Uso observado:

- `modulos/medicoes/lancamentos/servicos.py` usa `carregar_lancamentos_trabalho()` e `salvar_lancamentos_trabalho()` para criar, listar, aprovar e vincular lançamentos.

Observação:

Este repositório pertence ao subdomínio de lançamentos de trabalho executado, mas também acessa `locais_trabalho.csv` e `usuarios_obras.csv`.

---

### 7.1.4 Configuração de lançamentos

Arquivo:

`modulos/medicoes/lancamentos/config.py`

Funcionamento observado:

Este arquivo reexporta constantes definidas em `modulos/medicoes/config.py` para o subpacote de lançamentos.

Não foi observada configuração independente neste arquivo.

---

### 7.1.5 Sobreposição observada

Foi observada sobreposição entre o repositório geral de Medições e o repositório específico de lançamentos.

Arquivos acessados por ambos:

- `data/medicoes/locais_trabalho.csv`
- `data/medicoes/usuarios_obras.csv`
- `data/medicoes/lancamentos_trabalho.csv`

Interpretação operacional:

- O repositório geral atende o fluxo de gestão e mantém compatibilidade com partes legadas.
- O repositório de lançamentos atende o fluxo operacional atual de lançamento de trabalho executado.

Status:

A sobreposição está documentada.
Não refatorar sem necessidade comprovada.

---

# 8. Fluxos

A documentar conforme próximas auditorias.

---

# 9. Observações Técnicas

## OT-001 — Fluxo legado de lançamentos

Existe histórico de fluxo legado de lançamentos dentro do módulo Medições.

Status:

Documentado parcialmente.

Ação futura:

Eliminar gradualmente código legado somente quando não houver mais referências ao fluxo antigo.

## OT-002 — Duas camadas de autorização

O sistema possui uma camada geral de permissões do aplicativo e uma camada específica de permissões de Medições.

A camada geral usa `data/permissoes_usuarios.csv`.

A camada de Medições usa `data/medicoes/usuarios_obras.csv`.

Essas camadas devem ser tratadas como distintas até que o código prove o contrário.

## OT-003 — `pode_executar()` ainda sem uso efetivo confirmado

A função `pode_executar()` existe em `services/permissoes.py` e implementa verificação granular por módulo, recurso, permissão e obra.

Nesta auditoria, não foi confirmado uso efetivo dessa função nos arquivos centrais analisados.

A autorização observada no fluxo principal depende de `pode_acessar_modulo()` para exibição de módulos e de permissões internas específicas no módulo Medições.

## OT-004 — Persistência por substituição integral de arquivo

As gravações CSV realizadas pelo serviço central convertem o DataFrame inteiro para CSV e substituem o conteúdo completo do arquivo no GitHub.

Esse funcionamento é simples e coerente com a arquitetura atual, mas deve ser considerado em qualquer evolução futura que envolva muitos usuários, arquivos grandes ou edições simultâneas.

## OT-005 — Wrappers duplicados de CSV

Foram observados wrappers de CSV em mais de um módulo.

Exemplos:

- modulos/medicoes/repositorio.py
- modulos/medicoes/lancamentos/repositorio.py

Eles centralizam colunas e tratamento de erro dentro de seus respectivos contextos, mas ainda não existe uma única camada compartilhada de repositório CSV para todo o app.

Não refatorar sem necessidade comprovada.

## OT-006 — Sobreposição entre repositórios de Medições

O módulo Medições possui um repositório geral e um repositório específico de lançamentos.

Ambos acessam parte dos mesmos arquivos de dados, especialmente locais de trabalho, vínculos de usuários com obras e lançamentos de trabalho.

Essa sobreposição parece refletir a coexistência entre fluxo de gestão, fluxo operacional atual e compatibilidade temporária com código legado.

Não consolidar esses repositórios sem auditoria completa dos fluxos que ainda dependem de cada um.

# 10. Perguntas em Aberto

## PA-001 — Uso real de `pode_executar()`

Confirmar por busca ampla no repositório se `pode_executar()` é chamada em algum módulo ainda não auditado.

## PA-002 — Relação desejada entre `superadmin` e `admin` de Medições

Confirmar se um `superadmin` global deve ou não possuir automaticamente perfil `admin` dentro do módulo Medições.

Hoje, pela lógica observada, essas permissões pertencem a camadas diferentes.

## PA-003 — Tratamento desejado para falhas de leitura no GitHub

Definir se `carregar_github()` deve continuar retornando DataFrame vazio para qualquer status HTTP diferente de 200 ou se, futuramente, deve diferenciar arquivo inexistente, erro de autenticação, erro de rede e CSV realmente vazio.

## PA-004 — Estratégia futura para concorrência

Definir se o app continuará aceitando o risco de conflito em gravações simultâneas ou se, em etapa futura, precisará de controle de concorrência, fila, locking, banco de dados ou outro mecanismo.

## PA-005 — Fronteira futura entre repositório geral e repositório de lançamentos

Confirmar se a sobreposição entre `modulos/medicoes/repositorio.py` e `modulos/medicoes/lancamentos/repositorio.py` deve permanecer como separação de contexto ou se, futuramente, deverá ser consolidada.

Nenhuma consolidação deve ser feita antes da auditoria completa dos fluxos de Medições.
