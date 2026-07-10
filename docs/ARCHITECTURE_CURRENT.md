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

Os detalhes internos de `tela_lancar_producao()` ainda não foram auditados nesta etapa.

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

Os detalhes internos de `tela_aprovar_lancamentos()` ainda não foram auditados nesta etapa.

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
