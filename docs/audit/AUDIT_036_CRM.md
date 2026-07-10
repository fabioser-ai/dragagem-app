# Auditoria Arquitetural — CRM

Data: 2026-07-10

## Status

- Auditoria concluída.
- Consolidação em `docs/ARCHITECTURE_CURRENT.md` pendente.
- Nenhum comportamento funcional foi alterado.

## Escopo auditado

- entrada pelo menu e roteamento em `app.py`;
- permissão geral de acesso ao módulo;
- navegação interna;
- cadastro e edição de clientes;
- cadastro e edição de contatos;
- registro e consulta de interações;
- consulta geral;
- schemas e relacionamentos entre entidades;
- persistência em CSV no GitHub;
- tratamento de erros e efeitos colaterais.

## Componentes diretamente envolvidos

- `app.py`
- `pages/menu.py`
- `pages/crm/crm.py`
- `pages/crm/navegacao.py`
- `pages/crm/config.py`
- `pages/crm/repositorio.py`
- `pages/crm/etapa1_clientes.py`
- `pages/crm/etapa2_contatos.py`
- `pages/crm/etapa3_interacoes.py`
- `pages/crm/utils.py`
- `services/permissoes.py`
- `services/github.py`

## Arquivos de dados

- `data/crm/clientes.csv`
- `data/crm/contatos.csv`
- `data/crm/interacoes.csv`

## 1. Entrada, autorização e navegação

O cartão do CRM é exibido no menu somente quando `pode_acessar_modulo("crm")` retorna verdadeiro. O botão define `st.session_state.tela = "crm"`, e o roteador de `app.py` chama `crm()`.

O perfil global `funcionario` é bloqueado pelo roteador antes de entrar no CRM, pois `crm` não pertence à lista de telas permitidas desse perfil.

Dentro do CRM não existe nova verificação de `pode_acessar_modulo("crm")`. A defesa observada depende do menu e do bloqueio global do roteador.

A navegação interna usa um `radio` na barra lateral e retorna uma das páginas:

- `clientes`;
- `contatos`;
- `interacoes`;
- `consulta`.

A página selecionada não é gravada explicitamente em uma chave de domínio do CRM; o estado visual fica associado ao widget Streamlit.

## 2. Modelo de dados

### Clientes

A entidade cliente possui identidade própria por `id_cliente` UUID e inclui dados cadastrais, status comercial, responsável, necessidade, último contato, próxima ação e timestamps de criação e atualização.

### Contatos

A entidade contato possui `id_contato` UUID e referência textual a `id_cliente`. Não existe validação de integridade referencial na camada de repositório.

### Interações

A entidade interação possui `id_interacao` UUID, referência obrigatória na tela a `id_cliente` e referência opcional a `id_contato`.

Não existe banco relacional, chave estrangeira ou mecanismo central que impeça referências órfãs caso os CSVs sejam editados externamente ou gravados de maneira inconsistente.

## 3. Persistência

`pages/crm/repositorio.py` implementa wrappers específicos do CRM sobre `services/github.py`.

O wrapper de leitura:

1. lê o CSV completo;
2. cria DataFrame vazio quando necessário;
3. acrescenta colunas ausentes;
4. restringe o resultado ao schema configurado;
5. converte todos os valores para texto.

Consequência observada: colunas extras existentes no arquivo são descartadas da visão carregada e também podem desaparecer na próxima gravação.

O wrapper de escrita:

1. acrescenta colunas ausentes;
2. restringe ao schema configurado;
3. converte tudo para texto;
4. substitui integralmente o CSV no GitHub.

Existe tentativa de chamar `salvar_github()` com `mensagem_commit`. Se a assinatura não aceitar esse parâmetro, um `TypeError` provoca nova chamada sem mensagem personalizada.

## 4. Fluxo de clientes

A criação exige somente `nome_empresa` preenchido. O sistema gera UUID, `created_at` e `updated_at`.

Não foi observada validação de duplicidade por:

- nome da empresa;
- documento ou CNPJ;
- combinação de cidade e endereço.

A listagem oferece busca textual e filtros por status, estado e responsável.

A edição seleciona o cliente pelo `nome_empresa` e, quando existem nomes duplicados, usa a primeira linha correspondente no DataFrame filtrado. A identidade persistente usada na atualização é o `id_cliente` dessa linha.

Na criação, `data_proxima_acao` usa `date_input`; na edição, o mesmo campo é texto livre. Portanto, criação e edição não aplicam o mesmo tipo de entrada.

A edição não valida novamente se o nome da empresa ficou vazio.

## 5. Fluxo de contatos

O cadastro exige pelo menos um cliente e somente o nome do contato é obrigatório.

O seletor de clientes constrói um dicionário `nome_empresa -> id_cliente`. Empresas homônimas sobrescrevem entradas anteriores e não podem ser distinguidas na interface.

O campo `contato_principal` aceita `Sim` ou `Não`, mas não existe regra que:

- limite a um contato principal por cliente;
- remova automaticamente o principal anterior;
- garanta que cada cliente tenha um contato principal.

A listagem combina contatos e clientes por `id_cliente` com `left join`.

A edição identifica visualmente o contato pelo rótulo `nome_contato - nome_empresa`. Rótulos duplicados selecionam a primeira linha correspondente.

A tela permite mover um contato para outro cliente alterando `id_cliente`. Interações históricas que referenciem esse contato não são atualizadas. Assim, uma interação pode continuar apontando para o cliente original e para um contato posteriormente movido para outra empresa.

A edição não valida novamente se o nome do contato ficou vazio.

## 6. Fluxo de interações

O registro exige cliente e descrição. O contato é opcional.

O seletor de clientes também usa `nome_empresa -> id_cliente` e sofre a mesma colisão para empresas homônimas.

As opções de contato usam `nome_contato -> id_contato`. Contatos homônimos do mesmo cliente sobrescrevem entradas anteriores.

Ao cadastrar uma interação, o sistema executa duas gravações independentes:

1. acrescenta a interação em `interacoes.csv`;
2. recarrega e atualiza o cliente em `clientes.csv`.

A atualização do cliente copia:

- `ultimo_contato`;
- `proxima_acao`;
- `data_proxima_acao`;
- `responsavel`, quando informado;
- `updated_at`.

Não existe transação. Se a interação for salva e a atualização do cliente falhar, os dois arquivos ficam temporariamente divergentes.

A função `cadastrar_interacao()` não retorna um resultado estruturado para informar se ambas as gravações foram concluídas.

As interações não possuem edição ou exclusão pela interface auditada.

A listagem ordena `data_interacao` como texto. O formato produzido pela tela é ISO `YYYY-MM-DD`, portanto a ordenação cronológica funciona enquanto esse padrão for preservado.

## 7. Consulta geral

A consulta carrega os três CSVs e apresenta métricas de quantidade.

A busca rápida opera somente sobre campos do cadastro de clientes. Embora o placeholder mencione contexto amplo, ela não pesquisa conteúdo de contatos nem descrições ou resultados das interações.

A consulta apresenta somente dados resumidos do cliente e não constrói uma visão agregada com contatos e histórico comercial.

## 8. Tratamento de erros e efeitos colaterais

A leitura captura exceções, exibe detalhes no Streamlit e retorna DataFrame vazio. Como `services.github.carregar_github()` também pode retornar vazio em falhas HTTP, parte dos erros pode ser interpretada como ausência de dados.

As telas exibem sucesso depois das funções de cadastro ou atualização. Erros de gravação propagados impedem normalmente essa mensagem, mas atualizações cujo ID não seja encontrado retornam silenciosamente sem indicar falha; a tela ainda pode informar sucesso.

Todas as gravações substituem o arquivo completo. Não existe locking ou controle transacional entre usuários.

Não existem operações de exclusão para clientes, contatos ou interações na interface auditada.

## 9. Fatos observados nos dados atuais

- `clientes.csv` contém um cliente cadastrado.
- `contatos.csv` possui apenas o cabeçalho.
- `interacoes.csv` possui apenas o cabeçalho.

## 10. O que foi aprendido

O CRM é um módulo separado por domínio, com configuração, repositório, telas e utilitários próprios. O modelo possui três entidades ligadas por UUIDs, mas a interface usa nomes como chaves em seletores e rótulos, criando ambiguidades para homônimos.

O registro de interação também mantém um resumo comercial no cadastro do cliente, o que cria duplicação intencional de informação entre `interacoes.csv` e `clientes.csv` sem transação entre as gravações.

## 11. O que ainda não foi compreendido

- Se nomes de empresas devem ser únicos.
- Se documento ou CNPJ deve ser único e obrigatório para determinados tipos de cliente.
- Se deve existir exatamente um contato principal por cliente.
- Se contatos podem ser transferidos entre clientes depois de existirem interações.
- Se o responsável deve ser um usuário cadastrado ou texto livre.
- Se interações precisam de edição, cancelamento ou correção auditável.
- Se a consulta geral deveria pesquisar e consolidar contatos e interações.
- Se o resumo armazenado no cliente deve ser derivado sempre da interação cronologicamente mais recente.

## 12. O que deve ser documentado

### Observações Técnicas propostas

- OT-045 — CRM possui repositório próprio sobre `services/github.py`.
- OT-046 — Schemas do CRM descartam colunas não declaradas.
- OT-047 — Seletores de clientes usam nome da empresa como chave visual.
- OT-048 — Seletores de contatos usam nome do contato como chave visual.
- OT-049 — Não existe integridade referencial entre os CSVs do CRM.
- OT-050 — Interação e atualização do cliente são gravações independentes.
- OT-051 — Contato pode mudar de cliente sem atualização das interações históricas.
- OT-052 — Não existe unicidade de contato principal.
- OT-053 — Criação e edição usam tipos diferentes para data da próxima ação.
- OT-054 — Atualizações com ID inexistente falham silenciosamente.
- OT-055 — Consulta geral pesquisa somente o cadastro de clientes.
- OT-056 — Entidades do CRM não possuem exclusão pela interface auditada.

### Perguntas em Aberto propostas

- PA-036 — Regra de unicidade de clientes.
- PA-037 — Regra de documento ou CNPJ.
- PA-038 — Regra de contato principal.
- PA-039 — Transferência de contato entre clientes.
- PA-040 — Identidade e origem do responsável comercial.
- PA-041 — Política de correção de interações.
- PA-042 — Escopo desejado da consulta geral.
- PA-043 — Regra para atualização do último contato e próxima ação.
- PA-044 — Estratégia de integridade referencial e transação entre CSVs.

## 13. Baby step seguro

O primeiro baby step futuro deve ser eliminar a ambiguidade dos seletores sem alterar o modelo persistente: exibir rótulos descritivos, mas manter `id_cliente` e `id_contato` como valores reais de seleção.

Exemplo conceitual:

- cliente: `Nome da empresa | Cidade | ID abreviado`;
- contato: `Nome do contato | Cargo | ID abreviado`.

Esse passo deve ser implementado somente após decisão funcional sobre empresas e contatos homônimos.

## Próximo subsistema

Administração.
