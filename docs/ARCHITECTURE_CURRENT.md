# APP FOS — ARCHITECTURE CURRENT

Status:
Em construção.

Última atualização:
2026-07-10

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
- Medições possui função para salvar fotos em `data/medicoes/fotos_lancamentos`, mas o fluxo operacional atual não chama essa função.

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

## 7.2 Módulo Medições — Fluxo principal

### Visão geral

O fluxo principal do módulo Medições é iniciado por `pages/medicoes.py` e delegado para `modulos/medicoes/navegacao.py`.

Arquivos principais observados:

- `pages/medicoes.py`
- `modulos/medicoes/navegacao.py`
- `modulos/medicoes/permissoes.py`
- `modulos/medicoes/config.py`
- `modulos/medicoes/utils.py`

---

### 7.2.1 Entrada do módulo

Arquivo:

`pages/medicoes.py`

Responsabilidades observadas:

- Exibir título e descrição do módulo.
- Validar acesso interno ao módulo com `tem_acesso_medicoes()`.
- Obter perfil interno com `obter_perfil_medicao()`.
- Inicializar `st.session_state["fluxo_medicoes"]`.
- Inicializar `st.session_state["etapa_medicoes"]`.
- Redirecionar funcionário diretamente para o fluxo de lançamento.
- Impedir acesso ao fluxo de gestão quando o perfil não pode criar medição.
- Chamar `navegacao()`.
- Carregar bases e renderizar etapas apenas quando o fluxo atual é `gestao`.

Estados de sessão observados:

- `fluxo_medicoes`
- `etapa_medicoes`

Fluxo simplificado:

Entrada em Medições

↓

Validação por `tem_acesso_medicoes()`

↓

Inicialização de estado

↓

Ajuste automático para funcionário, se aplicável

↓

Proteção contra acesso indevido à gestão

↓

Delegação para `navegacao()`

↓

Se fluxo for `gestao`, carrega bases e renderiza etapa atual.

---

### 7.2.2 Navegação interna

Arquivo:

`modulos/medicoes/navegacao.py`

Responsabilidades observadas:

- Definir labels visuais das etapas de medição.
- Resolver etapas disponíveis conforme modelo de medição.
- Renderizar tela inicial do módulo Medições.
- Definir opções disponíveis conforme permissões internas.
- Direcionar para fluxo de gestão.
- Direcionar para fluxo de lançamento.
- Direcionar para fluxo de aprovação.
- Proteger cada fluxo contra acesso indevido.
- Controlar avanço e retorno entre etapas da gestão.

Fluxos internos observados:

- `inicio`
- `gestao`
- `lancamento`
- `aprovacao`

---

### 7.2.3 Tela inicial de Medições

Função:

`tela_inicial_medicoes()`

Funcionamento observado:

- Obtém o perfil interno de medição.
- Monta lista de opções disponíveis.
- Inclui `gestao` quando `pode_criar_medicao()` é verdadeiro.
- Inclui `lancamento` quando `pode_lancar_trabalho()` é verdadeiro.
- Inclui `aprovacao` quando `pode_aprovar_lancamentos()` é verdadeiro.
- Se não houver opções, exibe aviso.
- Se o perfil for `funcionario`, define `fluxo_medicoes = "lancamento"` e retorna sem renderizar escolha manual.
- Para demais perfis, renderiza botões de acesso aos fluxos disponíveis.

Observação:

O funcionário não escolhe fluxo manualmente. Ele é direcionado para lançamento.

---

### 7.2.4 Fluxo de gestão

Função:

`navegacao_gestao()`

Proteção observada:

- Se `pode_criar_medicao()` for falso, o fluxo volta para `inicio` e exibe aviso.

Funcionamento observado:

- Lê `etapa_medicoes` da sessão.
- Obtém a ordem de etapas através de `obter_etapas()`.
- Se a etapa atual não existir na ordem do modelo, ajusta para a primeira etapa.
- Renderiza barra visual das etapas.
- Renderiza botões Voltar, Início Medições e Próximo.
- Usa `ir_para(etapa)` para mudar etapa e executar `st.rerun()`.

Etapas possíveis por modelo:

- `padrao_fos`: obra, bm, lancamentos, resumo.
- `ast_bags`: obra, bm, frentes, mc, lancamentos, resumo.
- `diario_equipamento`: obra, bm, frentes, lancamentos, resumo.
- `batimetria`: obra, bm, mc, resumo.

Renderização das etapas:

A renderização concreta das telas de etapa ocorre em `pages/medicoes.py`, após a navegação, quando `fluxo_medicoes == "gestao"`.

---

### 7.2.5 Fluxo de lançamento

Função:

`navegacao_lancamento()`

Proteção observada:

- Se `pode_lancar_trabalho()` for falso, o fluxo volta para `inicio` e exibe aviso.

Destino observado:

- Chama `tela_lancar_producao()`.

Observação:

Os detalhes internos de `tela_lancar_producao()` estão documentados na seção 7.3.

---

### 7.2.6 Fluxo de aprovação

Função:

`tela_aprovacao_placeholder()`

Proteção observada:

- Se `pode_aprovar_lancamentos()` for falso, o fluxo volta para `inicio` e exibe aviso.

Destino observado:

- Chama `tela_aprovar_lancamentos()`.

Observação:

Apesar do nome `placeholder`, a função chama uma tela real de aprovação.

Os detalhes internos de `tela_aprovar_lancamentos()` estão documentados na seção 7.4.

---

## 7.3 Módulo Medições — Fluxo operacional de lançamentos

### Visão geral

A tela operacional de lançamento é implementada por `tela_lancar_producao()`, em `modulos/medicoes/lancamentos/tela_lancar.py`.

Componentes diretamente envolvidos:

- `pages/medicoes.py`
- `modulos/medicoes/navegacao.py`
- `modulos/medicoes/permissoes.py`
- `modulos/medicoes/lancamentos/tela_lancar.py`
- `modulos/medicoes/lancamentos/servicos.py`
- `modulos/medicoes/lancamentos/repositorio.py`
- `modulos/medicoes/repositorio.py`
- `modulos/medicoes/config.py`
- `modulos/medicoes/utils.py`
- `services/github.py`

Arquivos de dados diretamente consumidos:

- `data/obras.csv`
- `data/medicoes/usuarios_obras.csv`
- `data/medicoes/locais_trabalho.csv`
- tabela contratual indicada por `arquivo_tabela_servicos` em `data/obras.csv`
- `data/medicoes/lancamentos_trabalho.csv`

### Entrada, navegação e permissão

O acesso começa em `pages/medicoes.py`, após `tem_acesso_medicoes()`.

O fluxo `lancamento` é protegido novamente em `navegacao_lancamento()` por `pode_lancar_trabalho()`.

Os perfis `funcionario`, `encarregado`, `aprovador` e `admin` podem entrar no fluxo.

O perfil `funcionario` é redirecionado automaticamente para esse fluxo.

### Identificação do usuário e obras disponíveis

A tela possui a função local `_obter_usuario_logado()`, que procura, nesta ordem:

- `email`
- `usuario_email`
- `user_email`
- `usuario_logado`
- `usuario`
- `login`

Ela aceita valor textual e, especificamente nessa tela, também aceita dicionário.

A função `_filtrar_obras_por_usuario()` cruza o identificador encontrado com `usuario_id`, `email` ou `nome` em `usuarios_obras.csv`, considerando apenas vínculos ativos.

Funcionamento observado:

- sem identificação do usuário, nenhuma obra é liberada;
- sem vínculos ativos, nenhuma obra é liberada;
- para o perfil obtido da primeira linha de vínculo, `admin` ou `aprovador` recebe a lista completa de obras;
- demais perfis recebem apenas as obras cujos `obra_id` aparecem nos vínculos;
- o campo `status` de `data/obras.csv` não é usado para filtrar obras nessa tela.

Observação:

`obter_perfil_medicao()` escolhe o maior perfil do conjunto de vínculos, mas `_filtrar_obras_por_usuario()` usa o perfil da primeira linha encontrada. Os dois pontos não aplicam exatamente a mesma regra quando um usuário possui múltiplos vínculos com perfis diferentes.

### Local e item contratual

Os locais são obtidos por `listar_locais_por_obra(obra_id)`.

Somente locais da obra cujo campo `ativo` corresponda a valor aceito são exibidos. A lista é ordenada por `nome_local`.

A tela exige um local válido antes de criar o lançamento.

A tabela contratual é definida pelo campo `arquivo_tabela_servicos` da obra e carregada a partir de `data/medicoes_tabelas/`.

Itens inativos são filtrados quando a coluna `ativo` existe.

O rótulo do serviço combina `codigo`, `descricao` e `unidade`.

O campo `item_id` gravado recebe o mesmo valor de `codigo_item`. A coluna contratual `item` não é usada como identificador nessa tela.

### Quantidade, data, observação e fotografia

A quantidade é recebida por `st.number_input()`, com mínimo zero e passo 0,01.

No salvamento, a tela rejeita quantidade menor ou igual a zero.

A data é recebida por `st.date_input()`.

A observação é opcional.

O uploader aceita PNG, JPG e JPEG.

Funcionamento observado da fotografia:

- o objeto enviado não é repassado para `salvar_foto_lancamento()`;
- a tela grava apenas `foto.name` no campo `foto_url`;
- portanto, o fluxo atual não persiste os bytes da fotografia selecionada.

### Criação, persistência e estados

A tela chama `criar_lancamento_trabalho()`.

O serviço:

1. carrega todo o CSV de lançamentos;
2. cria um ID com prefixo `LAN`;
3. monta o registro;
4. adiciona a linha ao DataFrame;
5. solicita a substituição integral de `lancamentos_trabalho.csv`;
6. retorna o dicionário montado.

Estados iniciais observados:

- `status_aprovacao = pendente`
- `status_medicao = nao_medido`
- `aprovado_por`, `aprovado_em` e `medicao_id_vinculada` vazios

O lançamento nasce independente de uma medição.

O fluxo de aprovação altera `status_aprovacao`.

A etapa de gestão da medição considera elegíveis lançamentos da obra com `status_aprovacao = aprovado` e `status_medicao = nao_medido`.

### Tratamento de erros e efeitos colaterais

Os wrappers de leitura convertem exceções em DataFrames vazios.

O wrapper de gravação captura exceções, exibe erro no Streamlit e retorna `False`.

`criar_lancamento_trabalho()` não verifica o valor retornado por `salvar_lancamentos_trabalho()`.

A tela exibe mensagem de sucesso após o retorno do serviço. Consequentemente, o código observado permite mensagem de sucesso mesmo quando o wrapper informou falha de persistência.

A gravação substitui integralmente o CSV e cria um commit no repositório de dados.


## 7.4 Módulo Medições — Fluxo de aprovação

### Visão geral

A tela de aprovação é implementada por `tela_aprovar_lancamentos()`, em `modulos/medicoes/lancamentos/tela_aprovar.py`.

Componentes diretamente envolvidos:

- `pages/medicoes.py`
- `modulos/medicoes/navegacao.py`
- `modulos/medicoes/permissoes.py`
- `modulos/medicoes/lancamentos/tela_aprovar.py`
- `modulos/medicoes/lancamentos/repositorio.py`
- `modulos/medicoes/lancamentos/servicos.py`
- `modulos/medicoes/config.py`
- `services/auth.py`
- `services/github.py`
- `modulos/medicoes/fluxo_medicao/etapa5_lancamentos.py`

Arquivo de dados alterado:

- `data/medicoes/lancamentos_trabalho.csv`

### Entrada e permissão

O acesso começa na opção de aprovação da tela inicial de Medições.

A opção é exibida quando `pode_aprovar_lancamentos()` retorna verdadeiro.

Ao entrar, `fluxo_medicoes` recebe `aprovacao`.

`tela_aprovacao_placeholder()` executa novamente `pode_aprovar_lancamentos()` antes de chamar a tela real.

Os perfis internos autorizados são:

- `aprovador`
- `admin`

A permissão é determinada pelo maior perfil encontrado entre todos os vínculos ativos do usuário em `usuarios_obras.csv`.

### Escopo dos lançamentos apresentados

A tela carrega todo o conteúdo de `lancamentos_trabalho.csv`.

Em seguida, apresenta somente linhas cujo `status_aprovacao`, após normalização de texto, seja `pendente`.

Não foi observado filtro por:

- `obra_id` vinculada ao usuário;
- vínculos ativos do aprovador em `usuarios_obras.csv`;
- autor do lançamento;
- data do serviço;
- `status_medicao`.

Consequência observada:

Um usuário que possua perfil interno `aprovador` ou `admin` em qualquer vínculo ativo pode visualizar e decidir sobre todos os lançamentos pendentes existentes no arquivo.

### Filtro visual por obra

A tela monta o filtro a partir dos valores únicos de `nome_obra` presentes nos lançamentos pendentes.

A opção `Todas` preserva a lista completa.

Quando uma obra é escolhida, a comparação usa `nome_obra`, não `obra_id`.

Obras diferentes que compartilhem o mesmo nome são agrupadas pelo filtro visual.

### Informações apresentadas

Cada lançamento pendente é exibido em um `expander`.

Campos apresentados:

- ID do lançamento;
- nome da obra;
- nome do local;
- código e descrição do item;
- quantidade e unidade;
- data do serviço;
- observação;
- valor textual de `foto_url`;
- usuário criador.

A tela não carrega nem renderiza os bytes de uma fotografia.

### Aprovação

Ao aprovar, a tela atualiza todas as linhas cujo `lancamento_id` corresponda ao ID selecionado:

- `status_aprovacao = aprovado`;
- `aprovado_por = usuário logado`;
- `aprovado_em = data e hora atuais`;
- `atualizado_em = data e hora atuais`.

O fluxo oficial de autenticação grava o login em `st.session_state.usuario`, que é a primeira chave consultada por `_usuario_logado()`.

O campo `status_medicao` não é alterado pela aprovação.

Assim, um lançamento criado como `nao_medido` permanece nesse estado e passa a ser elegível na etapa de seleção da gestão da medição.

### Reprovação

Ao reprovar, a tela atualiza:

- `status_aprovacao = reprovado`;
- `aprovado_por = usuário logado`;
- `aprovado_em = data e hora atuais`;
- `atualizado_em = data e hora atuais`.

Não existe campo específico para responsável ou data da reprovação no schema atual.

Não existe campo nem entrada de justificativa da reprovação.

O campo `status_medicao` também permanece inalterado.

Lançamentos reprovados não aparecem na etapa de seleção da medição, pois essa etapa exige `status_aprovacao = aprovado`.

### Persistência

A própria tela modifica o DataFrame e chama `salvar_lancamentos_trabalho(df)`.

A função `atualizar_status_aprovacao()` existente na camada de serviços não é usada pela tela auditada.

A gravação substitui integralmente `lancamentos_trabalho.csv`.

Após solicitar a gravação, a tela exibe mensagem de aprovação ou reprovação e executa `st.rerun()`.

O retorno booleano de `salvar_lancamentos_trabalho()` não é verificado. Portanto, a interface pode informar aprovação ou reprovação mesmo quando o wrapper retornou `False`.

### Navegação de saída

Não existe, na tela auditada, botão para retornar ao início de Medições ou ao menu principal.

A tela também não altera `fluxo_medicoes` após uma decisão ou quando não existem pendências.

O `st.rerun()` mantém o usuário no fluxo `aprovacao`.


## 7.5 Módulo Medições — Gestão completa da medição

### Visão geral

O fluxo de gestão é acessível somente ao perfil interno `admin` de Medições.

Ele é coordenado por:

- `pages/medicoes.py`
- `modulos/medicoes/navegacao.py`
- `modulos/medicoes/config.py`
- `modulos/medicoes/repositorio.py`
- arquivos de etapa em `modulos/medicoes/fluxo_medicao/`
- repositório e serviços de lançamentos

O fluxo usa estado de sessão para conectar as etapas e arquivos CSV para persistir parte dos dados.

### Estados de sessão diretamente envolvidos

Foram observadas as seguintes chaves:

- `fluxo_medicoes`
- `etapa_medicoes`
- `obra_id`
- `modelo_medicao`
- `arquivo_tabela_servicos`
- `medicao_id`
- `frente_id`
- `lancamentos_selecionados`
- `df_lancamentos_selecionados`, lida como alternativa no resumo

A última chave não é preenchida pelas etapas auditadas.

A troca de obra não limpa explicitamente o BM, a frente ou os lançamentos anteriormente mantidos na sessão.

A troca de BM também não limpa explicitamente a frente ou os lançamentos selecionados.

### Sequência por modelo

A ordem é definida por `ETAPAS_MODELO`:

- `padrao_fos`: obra, BM, lançamentos, resumo;
- `ast_bags`: obra, BM, frentes, MC, lançamentos, resumo;
- `diario_equipamento`: obra, BM, frentes, lançamentos, resumo;
- `batimetria`: obra, BM, MC, resumo.

A barra de etapas renderiza componentes `st.button()`, mas o retorno desses botões não é usado. A mudança de etapa ocorre pelos controles Voltar e Próximo.

O botão Próximo altera a etapa sem validar se a etapa atual possui os dados necessários. As próprias telas posteriores exibem avisos quando faltam chaves de sessão.

### Etapa 1 — Obra

Arquivo:

`modulos/medicoes/fluxo_medicao/etapa1_obra.py`

Funcionamento observado:

- lista toda obra com `obra_id` preenchido;
- não filtra pelo campo `status`;
- monta o seletor usando `nome_obra | contrato`;
- grava `obra_id`, `modelo_medicao` e `arquivo_tabela_servicos` na sessão;
- permite cadastrar uma nova obra;
- exige somente o nome no cadastro;
- grava a nova obra em `data/obras.csv`.

O arquivo da tabela contratual é informado como texto livre. A etapa não confirma a existência desse arquivo ao cadastrar a obra.

Rótulos iguais de nome e contrato resultam na mesma chave do mapa usado pelo seletor.

### Etapa 2 — BM

Arquivo:

`modulos/medicoes/fluxo_medicao/etapa2_bm.py`

Funcionamento observado:

- exige `obra_id` na sessão;
- lista BMs filtrados pela obra selecionada;
- grava o `medicao_id` escolhido na sessão;
- permite criar novo BM;
- configura campos conforme o modelo da obra;
- rejeita período final anterior ao inicial;
- cria o BM com `status = rascunho`;
- grava em `data/medicoes/medicoes.csv`.

Não foi observada validação de duplicidade de número ou período.

Se a obra selecionada não possui BM, a etapa não remove um `medicao_id` anterior que ainda esteja na sessão.

Não foi observado, nas etapas auditadas, mecanismo que altere o status do BM após sua criação.

### Etapa 3 — Frentes

Arquivo:

`modulos/medicoes/fluxo_medicao/etapa3_frentes.py`

Funcionamento observado:

- exige `medicao_id` na sessão;
- lista frentes filtradas pelo BM;
- grava `frente_id` na sessão;
- permite criar frente com nome, dias trabalhados e observações;
- exige somente o nome;
- grava em `data/medicoes/frentes.csv`.

Se o BM não possui frente, a etapa não remove um `frente_id` anterior mantido na sessão.

Rótulos iguais de nome e dias trabalhados resultam na mesma chave do mapa usado pelo seletor.

### Etapa 4 — Memória de cálculo

Arquivo:

`modulos/medicoes/fluxo_medicao/etapa4_mc.py`

Existem dois comportamentos.

#### Comportamento `padrao_fos`

A função `tela_mc_padrao_fos()`:

- cria ou reutiliza uma frente chamada `MEDIÇÃO GERAL`;
- carrega a tabela contratual da obra;
- permite informar quantidade executada por item;
- calcula quantidade multiplicada pelo preço unitário com BDI;
- grava os dados no schema legado de `COL_MC`;
- substitui todos os registros de MC da frente.

Mapeamento de compatibilidade observado:

- `comprimento` recebe quantidade executada;
- `ast` recebe preço unitário;
- `resultado` recebe total;
- `descricao` concatena item, código e descrição contratual.

O schema `COL_MC` não preserva em colunas próprias fonte, código, item e unidade.

Ao reabrir uma MC persistida, esses campos estruturados não existem no DataFrame carregado. A tela os recria vazios e não reconcilia o registro com a tabela contratual.

A gravação inclui todas as linhas da tabela contratual, inclusive aquelas com quantidade zero.

Observação de alcance:

Embora esse comportamento exista no arquivo, `padrao_fos` não contém a etapa `mc` em `ETAPAS_MODELO`. Portanto, a tela não é alcançada pela sequência normal configurada atualmente para esse modelo.

#### Comportamento dos demais modelos

`tela_mc()` direciona todo modelo diferente de `padrao_fos` para `tela_mc_ast()`.

Essa tela:

- exige uma frente na sessão;
- usa editor com linhas dinâmicas;
- calcula `resultado = comprimento × ast`;
- substitui todos os registros de MC da frente.

Novas linhas adicionadas dinamicamente não recebem explicitamente novos `mc_id`, `medicao_id` ou `frente_id` antes da gravação.

O modelo `batimetria`, quando chega à etapa MC, usa esse mesmo cálculo genérico de comprimento por AST.

### Etapa 5 — Seleção de lançamentos

Arquivo:

`modulos/medicoes/fluxo_medicao/etapa5_lancamentos.py`

Funcionamento observado:

- exige somente `obra_id`;
- carrega lançamentos de trabalho;
- filtra pela obra;
- exige `status_aprovacao = aprovado`;
- exige `status_medicao = nao_medido`;
- renderiza um checkbox por lançamento;
- grava apenas a lista de IDs em `st.session_state.lancamentos_selecionados`.

Não foi observado filtro pela data do serviço em relação ao período do BM.

A etapa não exige `medicao_id` para permitir a seleção.

A etapa não grava a seleção em CSV.

A etapa não altera `status_medicao` e não preenche `medicao_id_vinculada`.

### Etapa 6 — Resumo

Arquivo:

`modulos/medicoes/fluxo_medicao/etapa6_resumo.py`

Funcionamento observado:

- exige `medicao_id` na sessão;
- tenta usar primeiro `df_lancamentos_selecionados`;
- na ausência desse DataFrame, recarrega lançamentos pelos IDs de `lancamentos_selecionados`;
- não revalida obra, aprovação, status de medição ou período;
- apresenta os lançamentos;
- agrupa quantidades por código, descrição e unidade;
- não calcula valor financeiro;
- não usa efetivamente os argumentos `frentes`, `itens` e `medicoes`.

O indicador `Quantidade total` soma as quantidades dos grupos mesmo quando existirem unidades diferentes.

Não existe ação de confirmar, salvar, finalizar ou vincular a medição nessa tela.

### Persistência efetiva da gestão

Persistências observadas:

- obras em `data/obras.csv`;
- BMs em `data/medicoes/medicoes.csv`;
- frentes em `data/medicoes/frentes.csv`;
- MC em `data/medicoes/mc.csv`.

Não persistidos no fluxo auditado:

- seleção de lançamentos para o BM;
- mudança do lançamento para `medido`;
- preenchimento de `medicao_id_vinculada`;
- mudança do status do BM;
- consolidação financeira do resumo.

A função `vincular_lancamento_a_medicao()` existe em `modulos/medicoes/lancamentos/servicos.py`, mas não é chamada pelas etapas de gestão auditadas.

### Etapa de itens desconectada

O arquivo `modulos/medicoes/fluxo_medicao/etapa5_itens.py` implementa `tela_medicao()` para transformar resultado de MC em itens financeiros.

Essa função não é importada nem chamada por `pages/medicoes.py` no fluxo atual.

O arquivo permanece fora da sequência configurada de gestão.


# 8. Fluxos

## 8.1 Fluxo principal de Medições

Fluxo observado:

Menu Principal

↓

Módulo Medições

↓

`pages/medicoes.py`

↓

Validação de acesso interno por `tem_acesso_medicoes()`

↓

Inicialização de `fluxo_medicoes` e `etapa_medicoes`

↓

`modulos/medicoes/navegacao.py`

↓

Escolha ou redirecionamento de fluxo interno

↓

Fluxo `gestao`, `lancamento` ou `aprovacao`.

---

## 8.2 Fluxo gestão de Medições

Fluxo observado:

`fluxo_medicoes = gestao`

↓

Validação por `pode_criar_medicao()`

↓

Determinação das etapas pelo modelo em `ETAPAS_MODELO`

↓

Navegação entre etapas por `etapa_medicoes`

↓

Renderização da etapa em `pages/medicoes.py`.

---

## 8.3 Fluxo operacional de lançamento

Fluxo observado:

`fluxo_medicoes = lancamento`

↓

Validação por `pode_lancar_trabalho()`

↓

`tela_lancar_producao()`.

Detalhes internos ainda não auditados.

---

## 8.4 Fluxo de aprovação de lançamentos

Fluxo observado:

`fluxo_medicoes = aprovacao`

↓

Validação por `pode_aprovar_lancamentos()`

↓

`tela_aprovar_lancamentos()`.

Detalhes internos ainda não auditados.

---

## 8.5 Fluxo detalhado de criação de lançamento

Fluxo observado:

Entrada no módulo Medições

↓

Validação interna por `tem_acesso_medicoes()`

↓

Seleção ou redirecionamento para `fluxo_medicoes = lancamento`

↓

Validação por `pode_lancar_trabalho()`

↓

Identificação do usuário na sessão

↓

Carregamento de obras e vínculos ativos

↓

Filtragem de obras conforme vínculo e perfil obtido na tela

↓

Seleção de local ativo da obra

↓

Carregamento da tabela contratual vinculada à obra

↓

Seleção de item contratual ativo

↓

Preenchimento de quantidade, data, observação e fotografia opcional

↓

Validação de local e quantidade

↓

`criar_lancamento_trabalho()`

↓

Inclusão em `data/medicoes/lancamentos_trabalho.csv` com aprovação pendente e ainda não medido.


## 8.6 Fluxo detalhado de aprovação

Fluxo observado:

Entrada no módulo Medições

↓

Validação interna por `tem_acesso_medicoes()`

↓

Opção de aprovação disponível para perfil `aprovador` ou `admin`

↓

`fluxo_medicoes = aprovacao`

↓

Nova validação por `pode_aprovar_lancamentos()`

↓

Carregamento integral de `lancamentos_trabalho.csv`

↓

Seleção de linhas com `status_aprovacao = pendente`

↓

Filtro visual opcional por `nome_obra`

↓

Exibição dos dados do lançamento

↓

Decisão de aprovar ou reprovar

↓

Atualização direta do DataFrame na tela

↓

Substituição integral de `lancamentos_trabalho.csv`

↓

`st.rerun()` mantendo o fluxo de aprovação.

Relação com a gestão da medição:

Lançamento pendente

↓

Aprovação altera `status_aprovacao` para `aprovado`

↓

`status_medicao` permanece `nao_medido`

↓

A etapa de lançamentos da gestão pode apresentá-lo como elegível para seleção.


## 8.7 Fluxo detalhado de gestão da medição

Fluxo persistido observado:

Perfil `admin` de Medições

↓

Seleção ou cadastro da obra

↓

Seleção ou cadastro do BM em estado `rascunho`

↓

Criação ou seleção de frente, quando prevista pelo modelo

↓

Criação de MC, quando prevista pelo modelo

↓

Gravação dos respectivos CSVs.

Fluxo de lançamentos observado:

Seleção da obra

↓

Carregamento de lançamentos aprovados e `nao_medido`

↓

Marcação por checkbox

↓

IDs armazenados somente na sessão

↓

Resumo por item e quantidade

↓

Fim da interface atual.

Não foi observada, após o resumo:

- persistência da associação entre lançamento e BM;
- alteração para `status_medicao = medido`;
- preenchimento de `medicao_id_vinculada`;
- finalização do BM;
- consolidação financeira.


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

## OT-007 — `tela_aprovacao_placeholder()` chama tela real de aprovação

A função `tela_aprovacao_placeholder()` em `modulos/medicoes/navegacao.py` possui nome de placeholder, mas chama `tela_aprovar_lancamentos()` após validar permissão.

O nome pode não refletir mais o papel atual da função.

Não renomear sem auditoria completa do fluxo de aprovação e dos imports relacionados.

## OT-008 — Fotografia não persistida no fluxo operacional atual

`tela_lancar_producao()` recebe uma fotografia pelo uploader, mas grava somente o nome original do arquivo em `foto_url`.

A função existente `salvar_foto_lancamento()` não é chamada por esse fluxo.

Assim, o CSV pode indicar um nome de fotografia sem que os bytes tenham sido salvos pelo fluxo atual.

## OT-009 — Sucesso visual não confirma persistência

`salvar_lancamentos_trabalho()` retorna `False` quando a gravação falha.

`criar_lancamento_trabalho()` não verifica esse retorno e devolve o registro montado.

A tela então exibe mensagem de sucesso.

O sucesso visual do fluxo atual não confirma, por si só, que o CSV foi persistido.

## OT-010 — Regras diferentes para perfil em múltiplos vínculos

`obter_perfil_medicao()` escolhe o maior perfil encontrado em todos os vínculos ativos.

`_filtrar_obras_por_usuario()` usa o perfil da primeira linha de vínculo.

Um usuário com múltiplos vínculos e perfis diferentes pode, portanto, ser autorizado a entrar por uma regra e ter suas obras filtradas por outra.

## OT-011 — Aprovador e admin recebem todas as obras na tela de lançamento

Quando o perfil obtido da primeira linha é `admin` ou `aprovador`, `_filtrar_obras_por_usuario()` retorna todas as obras carregadas, não apenas as obras presentes nos vínculos do usuário.

## OT-012 — Obras não são filtradas por status no lançamento

`tela_lancar_producao()` carrega `data/obras.csv`, mas não filtra o campo `status` antes de apresentar ou liberar obras.


## OT-013 — Aprovação sem restrição por obra vinculada

A permissão de entrada depende do perfil interno do usuário, mas a tela de aprovação não cruza os lançamentos com os vínculos de obra do aprovador.

Um perfil `aprovador` ou `admin` pode atuar sobre todos os lançamentos pendentes do arquivo.

## OT-014 — Tela de aprovação não usa o serviço de atualização existente

Existe `atualizar_status_aprovacao()` em `modulos/medicoes/lancamentos/servicos.py`.

A tela auditada modifica o DataFrame diretamente e chama o repositório, duplicando a lógica de alteração dos campos de auditoria.

## OT-015 — Campos de aprovação também registram reprovação

A reprovação grava o responsável em `aprovado_por` e o momento em `aprovado_em`.

O schema atual não possui campos específicos para reprovação.

## OT-016 — Resultado da gravação não é verificado na aprovação

`salvar_lancamentos_trabalho()` retorna um booleano.

A tela ignora esse retorno, exibe mensagem de decisão concluída e executa `st.rerun()`.

## OT-017 — Ausência de saída na tela de aprovação

A tela de aprovação não oferece controle para alterar `fluxo_medicoes` e retornar ao início do módulo.

Após as decisões, o rerun preserva o fluxo de aprovação.

## OT-018 — Filtro de aprovação usa nome da obra

O filtro visual agrupa pendências por `nome_obra`, e não por `obra_id`.

Nomes iguais em obras distintas não são diferenciados pelo filtro.

## OT-019 — Reprovação sem justificativa estruturada

A decisão de reprovar não solicita nem grava um motivo.

O lançamento conserva apenas sua observação original e o novo status.


## OT-020 — Gestão não conclui a vinculação dos lançamentos

A seleção feita na etapa de lançamentos permanece em `st.session_state`.

O fluxo auditado não chama `vincular_lancamento_a_medicao()` e não modifica os campos persistidos dos lançamentos.

## OT-021 — BM permanece em rascunho

Novos BMs são criados com status `rascunho`.

Não foi observada transição de status no fluxo completo de gestão auditado.

## OT-022 — Estado descendente não é limpo ao mudar contexto

A seleção de uma nova obra não limpa explicitamente BM, frente e lançamentos selecionados.

A seleção de um novo BM não limpa explicitamente frente e lançamentos selecionados.

Isso permite que chaves de um contexto anterior permaneçam na sessão até serem sobrescritas.

## OT-023 — Avanço não valida conclusão da etapa

O botão Próximo altera `etapa_medicoes` sem consultar a etapa renderizada ou validar seus pré-requisitos.

As validações ocorrem apenas quando a etapa seguinte tenta usar o estado.

## OT-024 — Botões da barra de etapas não alteram a etapa

A barra visual cria botões para todas as etapas, mas não utiliza o retorno de clique desses componentes.

A navegação efetiva ocorre apenas pelos controles Voltar e Próximo.

## OT-025 — MC de `padrao_fos` fora da sequência atual

Existe implementação específica de MC contratual para `padrao_fos`, mas a configuração atual desse modelo não inclui a etapa `mc`.

## OT-026 — Schema de MC não preserva identidade contratual estruturada

No comportamento contratual de MC, fonte, código, item e unidade são reduzidos a texto dentro de `descricao` porque `COL_MC` não possui essas colunas.

Ao reabrir registros, a tela não reconstrói esses campos pela tabela contratual.

## OT-027 — MC contratual grava itens com quantidade zero

A persistência de `tela_mc_padrao_fos()` inclui a tabela contratual inteira, mesmo quando apenas poucos itens possuem quantidade executada.

## OT-028 — Linhas dinâmicas da MC genérica sem IDs explícitos

A MC genérica permite novas linhas, mas não atribui explicitamente IDs e vínculos às linhas adicionadas antes de salvar.

## OT-029 — Seleção não considera período do BM

A elegibilidade de lançamentos usa obra, aprovação e status de medição.

A data do serviço não é comparada ao início ou fim do período selecionado.

## OT-030 — Resumo não revalida elegibilidade

Ao recuperar lançamentos por IDs da sessão, o resumo não confirma novamente obra, status de aprovação, status de medição ou período.

## OT-031 — Quantidade total pode combinar unidades diferentes

O resumo agrupa corretamente por unidade, mas o indicador final soma as quantidades de todos os grupos em um único número.

## OT-032 — Etapa de itens fora do fluxo atual

`etapa5_itens.py` contém uma tela de itens financeiros baseada em MC, mas não é chamada pelo roteamento atual.

## OT-033 — Modelo batimetria usa cálculo genérico da MC AST

Todo modelo diferente de `padrao_fos` é enviado a `tela_mc_ast()`.

Assim, a etapa MC de `batimetria` usa `comprimento × ast` no código atual.


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

## PA-006 — Auditoria interna dos fluxos de lançamento e aprovação

Auditar separadamente `tela_lancar_producao()` e `tela_aprovar_lancamentos()`.

Essas telas são chamadas pelo fluxo principal de Medições, mas seus detalhes internos ainda não foram documentados.

## PA-007 — Regra desejada para obras de aprovador e admin

Confirmar se `aprovador` e `admin` devem lançar em todas as obras cadastradas ou somente nas obras às quais possuem vínculo ativo.

## PA-008 — Persistência desejada para fotografias

Definir se a fotografia é obrigatória ou opcional e se deve ser salva em `data/medicoes/fotos_lancamentos` por meio da função já existente.

## PA-009 — Identificador contratual do lançamento

Confirmar se `item_id` deve continuar recebendo o código contratual ou se deveria usar a coluna `item` da tabela contratual.

## PA-010 — Confirmação de gravação na camada de serviço

Definir como o fluxo deve comunicar falha de persistência antes de exibir sucesso ao usuário.

## PA-011 — Obras inativas no fluxo operacional

Confirmar se obras com status diferente de ativo devem permanecer selecionáveis na tela de lançamento.

## PA-012 — Escopo de atuação do aprovador

Confirmar se o aprovador deve atuar globalmente sobre todas as obras ou somente sobre obras às quais possui vínculo ativo.

## PA-013 — Dados próprios de reprovação

Definir se reprovações precisam de responsável, data e justificativa em campos próprios.

## PA-014 — Camada responsável pela mudança de status

Confirmar se a regra de aprovação deve ser centralizada em `atualizar_status_aprovacao()` ou se a atualização direta na tela é intencional.

## PA-015 — Navegação de saída da aprovação

Definir se a tela deve possuir retorno explícito ao início de Medições e ao menu principal.

## PA-016 — Identidade da obra no filtro de aprovação

Confirmar se o filtro deve distinguir obras por `obra_id` além de exibir `nome_obra`.

## PA-017 — Momento de consolidação da medição

Definir qual ação deve confirmar a seleção, vincular os lançamentos ao BM e alterar seu status de medição.

## PA-018 — Elegibilidade por período

Confirmar se a data do serviço deve obrigatoriamente estar dentro do período do BM.

## PA-019 — Limpeza de estado ao mudar obra ou BM

Definir quais chaves descendentes devem ser apagadas quando o usuário troca a obra ou o BM.

## PA-020 — Ciclo de vida do BM

Definir os estados do BM e o evento que encerra o estado `rascunho`.

## PA-021 — Papel da MC no modelo `padrao_fos`

Confirmar se a etapa contratual de MC deve voltar à sequência desse modelo ou se sua implementação é compatibilidade histórica.

## PA-022 — Regra de cálculo para batimetria

Confirmar se `comprimento × ast` representa corretamente a memória de cálculo do modelo `batimetria`.

## PA-023 — Modelo persistente da MC contratual

Definir se fonte, código, item e unidade precisam ser preservados em colunas próprias.

## PA-024 — Indicador de quantidade com múltiplas unidades

Definir se o resumo deve apresentar totais separados por unidade e eliminar o somatório geral heterogêneo.

## PA-025 — Destino de `etapa5_itens.py`

Confirmar se a etapa desconectada deve ser reintegrada, preservada como legado ou removida futuramente após busca completa de referências.
