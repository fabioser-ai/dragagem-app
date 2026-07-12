# Arquitetura Atual — Dados

Última atualização: 2026-07-12

Fontes de auditoria:

- `docs/audit/AUDIT_043_DADOS.md`;
- `docs/audit/AUDIT_047_LOCAIS_TRABALHO.md`;
- `docs/audit/AUDIT_048_ATESTADOS_SERVICOS.md`.

## Visão geral

O módulo Dados mantém catálogos técnicos compartilhados e cadastros auxiliares usados por outros módulos do APP FOS.

Arquivos principais:

- `pages/dados.py`;
- `pages/dados_detalhados/locais_trabalho.py`;
- `services/github.py`;
- `services/dados_persistencia.py`;
- `services/permissoes.py`.

## Entrada e autorização

O menu exibe Dados quando `pode_acessar_modulo("dados")` retorna verdadeiro. O roteador principal chama `dados.render()` para a rota `dados`.

O perfil global `funcionario` é bloqueado pelo roteador. Dentro do módulo não existe revalidação da permissão geral nem autorização granular por cadastro, operação ou obra.

Quem alcança a tela pode visualizar, incluir, editar e excluir registros das bases expostas, conforme os controles disponíveis em cada subárea.

## Navegação interna

A opção corrente é mantida em `st.session_state.subdados`.

Subáreas observadas:

- Equipamentos;
- Materiais;
- Desaguamento;
- Horários;
- Dias;
- Salários;
- Locais de Trabalho;
- Atestados.

## Bases administradas

- `data/equipamentos.csv`;
- `data/materiais.csv`;
- `data/desaguamento.csv`;
- `data/horarios.csv`;
- `data/dias.csv`;
- `data/salarios.csv`;
- `data/atestados.csv`;
- `data/atestados_servicos.csv`;
- `data/medicoes/locais_trabalho.csv`.

## Consumidores observados

### Orçamentos

- Etapa 0 usa materiais, desaguamento, horários e dias;
- Etapa 1 usa equipamentos e materiais;
- Etapa 2 usa salários.

### Medições

- o fluxo de lançamentos usa locais de trabalho vinculados à obra.

Alterações nessas bases podem modificar seletores e parâmetros-base de cálculos em outros módulos.

## CRUD genérico

Equipamentos, materiais, desaguamento, horários, dias e salários usam a mesma função `crud()`.

O fluxo:

1. lê o CSV;
2. normaliza o DataFrame para as colunas esperadas;
3. seleciona registros pelo índice atual;
4. permite editar, excluir ou adicionar;
5. regrava o arquivo inteiro.

A persistência segura foi introduzida para esses seis cadastros por meio de `services/dados_persistencia.py`. A tela usa resultado explícito de leitura, bloqueia escrita após leitura não confirmada e encaminha o SHA observado para atualização.

Não existem IDs estáveis nessas bases pela interface, nem trilha de alteração, confirmação de exclusão, vigência ou validações de domínio além da conversão de alguns campos numéricos.

## Conversão numérica

`converter_valores()` usa `parse_moeda()` para:

- vazão;
- consumo;
- valor;
- valor-hora;
- sólidos in situ;
- sólidos desaguados.

O parser remove pontos e troca vírgula por ponto. Esse comportamento é apropriado apenas para uma convenção monetária brasileira específica e pode reinterpretar incorretamente grandezas não monetárias já persistidas com ponto decimal.

Exemplos possíveis:

- `120.0` → `1200`;
- `40.0` → `400`;
- `0.2` → `2`.

Equipamentos e materiais alimentam diretamente cálculos de Orçamentos.

## Risco de leitura e gravação

O contrato legado de `carregar_github()` transforma diferentes falhas em DataFrame vazio. Consumidores ainda não migrados podem assumir uma base vazia válida e sobrescrever o CSV original.

O contrato explícito reduz esse risco nos consumidores já migrados, mas não fornece transação entre múltiplos arquivos.

## Locais de trabalho

Locais são armazenados em `data/medicoes/locais_trabalho.csv` com:

- `local_id` estável;
- `obra_id`;
- nome;
- estado ativo;
- observações;
- timestamps.

A tela impede nome duplicado dentro da mesma obra e permite apenas inclusão.

A administração de Locais foi migrada para o contrato explícito por meio do adaptador de Dados. A inclusão usa o SHA da leitura, permite criação explícita após arquivo inexistente, bloqueia o botão após leitura não confirmada e só apresenta sucesso após escrita confirmada.

Limitações preservadas:

- não existe edição, desativação ou exclusão;
- não existe filtragem das obras conforme vínculo ou permissão do usuário;
- um usuário com acesso ao módulo Dados pode cadastrar local em qualquer obra carregada;
- a tela carrega todas as bases gerais de Medições, embora use apenas obras;
- o consumidor interno de Medições permanece em camada legada distinta.

## Atestados e serviços vinculados

Atestados formam um agregado lógico distribuído em dois CSVs:

- `atestados.csv`, identificado por `id_atestado`;
- `atestados_servicos.csv`, identificado por `id_servico` e ligado por `id_atestado`.

### Leitura e schema

`garantir_estrutura_atestados()` lê os dois arquivos separadamente pelo contrato legado, cria colunas ausentes, preenche valores nulos e reduz cada DataFrame ao schema declarado.

Consequências:

- arquivo vazio, arquivo inexistente e falha de leitura são indistinguíveis para a tela;
- colunas extras podem ser descartadas em gravação posterior;
- as duas leituras não constituem snapshot atômico.

Os dados reais possuem formatos históricos heterogêneos, incluindo identificadores abreviados, campos vazios e datas ou períodos em diferentes representações. A migração de persistência não deve normalizar esses dados incidentalmente.

### Busca e seleção

A busca percorre os campos do atestado e dos serviços vinculados.

Os seletores usam `cliente | obra | contrato` como chave visual de dicionário. Rótulos iguais podem ocultar registros distintos, embora os IDs permaneçam diferentes.

### Criação e edição de atestado

A criação exige cliente e obra, gera UUID e usa entradas de data estruturadas. A edição localiza o registro por `id_atestado`, mas recebe datas como texto livre.

Ambas as operações regravam integralmente `atestados.csv` pelo contrato legado e apresentam sucesso sem verificar resultado estruturado.

### Serviços vinculados

Serviços possuem `id_servico` estável e referência textual por `id_atestado`. A interface permite inclusão e exclusão, mas não edição.

A criação exige apenas o nome do serviço e aceita quantidade não negativa. A integridade referencial é mantida pela seleção em memória da tela; a camada de persistência não confirma a existência atual do atestado referenciado.

### Exclusão composta

Excluir um atestado remove o registro principal e seus serviços em memória, depois executa duas gravações sequenciais:

1. `atestados.csv`;
2. `atestados_servicos.csv`.

Não existe transação, rollback ou compensação. Falha parcial pode deixar serviços órfãos ou manter o atestado sem seus serviços.

Usar SHA esperado em cada arquivo evita conflito concorrente silencioso, mas não transforma as duas gravações em operação atômica.

## Schemas

A estrutura de atestados cria colunas ausentes e reduz os DataFrames às colunas declaradas. Colunas extras podem desaparecer em gravações posteriores.

O CRUD genérico depende de os arquivos manterem as colunas esperadas. Divergências de schema podem causar falhas de acesso ou de inclusão.

## Efeitos sistêmicos

- vazão e sólidos alteram bases de cálculo de produção;
- salários alteram composições iniciais de equipe;
- horários e dias alteram opções de orçamento, mas a interpretação posterior depende de textos específicos;
- locais alteram opções operacionais de lançamento em Medições;
- exclusões de catálogos não possuem reconciliação automática com agregados históricos que já copiaram valores textuais;
- exclusões parciais de atestados podem romper a relação com serviços.

## Observações técnicas consolidadas

- Dados é catálogo mestre compartilhado por Orçamentos e Medições.
- O CRUD genérico usa índice de DataFrame como identidade.
- O parser monetário é aplicado a vazão e percentuais.
- Os catálogos não possuem vigência, histórico ou autor de alteração.
- A tela não revalida autorização internamente.
- Locais possuem identidade estável e são copiados para lançamentos.
- Administração e consumo de Locais usam camadas de persistência diferentes.
- Locais não filtram obras permitidas.
- Atestados formam agregado lógico em dois CSVs.
- A exclusão composta de atestado e serviços não é atômica.
- Persistência segura por arquivo não equivale a transação multi-arquivo.
- Dados históricos de atestados possuem formatos heterogêneos.
- Rótulos de atestado podem ser ambíguos.
- Datas de atestado usam tipos de entrada diferentes entre criação e edição.
- A estrutura de atestados descarta colunas desconhecidas.
- Integridade referencial de serviços é mantida apenas pela tela.
- A leitura conjunta de atestados e serviços não constitui snapshot atômico.

## Perguntas em aberto

- Quais perfis podem administrar cada base e operação?
- Deve existir autorização granular por cadastro?
- Os catálogos precisam de IDs estáveis, vigência e histórico?
- Qual é o formato numérico oficial para moeda, vazão e percentuais?
- Orçamentos devem preservar versões dos parâmetros mestres?
- Horários e dias devem formar um catálogo fechado compatível com os cálculos?
- Locais devem ser limitados às obras permitidas ao usuário?
- Qual camada deve ser canônica para Locais de Trabalho?
- Atestados precisam de regra de unicidade?
- Qual formato oficial deve ser usado para datas e períodos?
- A exclusão física de atestados deve continuar permitida?
- Como tratar falha parcial entre gravação do atestado e dos serviços?
- A escrita de serviços deve validar a existência atual do atestado?
- Existe consumidor de atestados fora do módulo Dados ainda não identificado?

## Próximo Kid Step seguro

Migrar primeiro somente as operações de Atestados que alteram um único arquivo:

1. leitura estruturada separada para `atestados.csv` e `atestados_servicos.csv`, preservando status e SHA próprios;
2. criação e edição de atestado com escrita segura no arquivo principal;
3. criação e exclusão de serviço com escrita segura no arquivo de serviços;
4. bloqueio de cada ação quando a leitura do arquivo correspondente não autorizar escrita;
5. sucesso e `st.rerun()` somente após resultado confirmado;
6. preservação integral de schemas, dados históricos, UUIDs, busca, filtros e regras atuais.

Não incluir no mesmo Kid Step:

- exclusão composta de atestado e serviços;
- mudança de datas;
- mudança de rótulos;
- nova regra de unicidade;
- permissões granulares;
- edição de serviços;
- normalização retroativa de dados.

A exclusão composta exige decisão específica de consistência multi-arquivo antes da implementação.
