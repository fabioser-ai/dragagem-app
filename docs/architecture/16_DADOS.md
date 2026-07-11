# Arquitetura Atual — Dados

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_043_DADOS.md`

## Visão geral

O módulo Dados mantém catálogos técnicos compartilhados e cadastros auxiliares usados por outros módulos do APP FOS.

Arquivos principais:

- `pages/dados.py`;
- `pages/dados_detalhados/locais_trabalho.py`;
- `services/github.py`;
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
2. quando o retorno está vazio, cria um DataFrame com as colunas esperadas;
3. seleciona registros pelo índice atual;
4. permite editar, excluir ou adicionar;
5. regrava o arquivo inteiro.

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

Quando `carregar_github()` retorna DataFrame vazio após falha HTTP, o CRUD assume uma base vazia válida.

Uma inclusão posterior pode substituir o CSV original por um DataFrame novo e incompleto.

As gravações substituem o arquivo inteiro e não possuem locking, transação, retry central ou releitura de confirmação.

## Locais de trabalho

Locais são armazenados em `data/medicoes/locais_trabalho.csv` com:

- `local_id` estável;
- `obra_id`;
- nome;
- estado ativo;
- observações;
- timestamps.

A tela impede nome duplicado dentro da mesma obra e permite apenas inclusão.

Limitações:

- não existe edição, desativação ou exclusão;
- não existe filtragem das obras conforme vínculo ou permissão do usuário;
- um usuário com acesso ao módulo Dados pode cadastrar local em qualquer obra carregada;
- a tela carrega todas as bases gerais de Medições, embora use apenas obras.

## Atestados

Atestados usam dois CSVs:

- `atestados.csv`, identificado por `id_atestado` UUID;
- `atestados_servicos.csv`, identificado por `id_servico` UUID e ligado por `id_atestado`.

A criação exige cliente e obra. Datas são estruturadas na criação e texto livre na edição.

Os seletores usam `cliente | obra | contrato` como chave visual. Rótulos iguais podem sobrescrever entradas no dicionário, embora os registros tenham UUIDs diferentes.

Excluir um atestado grava primeiro o arquivo de atestados e depois o arquivo de serviços. Não existe transação; uma falha parcial pode produzir inconsistência.

Serviços vinculados podem ser adicionados e excluídos, mas não editados pela interface observada.

## Schemas

A estrutura de atestados cria colunas ausentes e reduz o DataFrame às colunas declaradas. Colunas extras podem desaparecer em gravações posteriores.

O CRUD genérico depende de os arquivos manterem as colunas esperadas. Divergências de schema podem causar falhas de acesso ou de inclusão.

## Efeitos sistêmicos

- vazão e sólidos alteram bases de cálculo de produção;
- salários alteram composições iniciais de equipe;
- horários e dias alteram opções de orçamento, mas a interpretação posterior depende de textos específicos;
- locais alteram opções operacionais de lançamento em Medições;
- exclusões de catálogos não possuem reconciliação automática com agregados históricos que já copiaram valores textuais.

## Observações técnicas consolidadas

- Dados é catálogo mestre compartilhado por Orçamentos e Medições.
- O CRUD genérico usa índice de DataFrame como identidade.
- Leitura ambígua como vazio pode preceder sobrescrita destrutiva.
- O parser monetário é aplicado a vazão e percentuais.
- Os catálogos não possuem vigência, histórico ou autor de alteração.
- A tela não revalida autorização internamente.
- Locais não filtram obras permitidas.
- Atestados mantêm relação entre dois CSVs sem transação.
- Rótulos de atestado podem ser ambíguos.
- Datas de atestado usam tipos de entrada diferentes entre criação e edição.
- A estrutura de atestados descarta colunas desconhecidas.
- Mensagens de sucesso não são seguidas por releitura de confirmação.

## Perguntas em aberto

- Quais perfis podem administrar cada base e operação?
- Deve existir autorização granular por cadastro?
- Os catálogos precisam de IDs estáveis, vigência e histórico?
- Qual é o formato numérico oficial para moeda, vazão e percentuais?
- Orçamentos devem preservar versões dos parâmetros mestres?
- Horários e dias devem formar um catálogo fechado compatível com os cálculos?
- Locais devem ser limitados às obras permitidas ao usuário?
- Atestados precisam de regra de unicidade e política de exclusão?
- Como tratar falhas parciais entre atestados e serviços?
- Existe consumidor de atestados fora do módulo Dados ainda não identificado?

## Baby step seguro futuro

Separar conversão monetária de conversão numérica geral, depois de definir formalmente os formatos de entrada e persistência para moeda, vazão e percentuais.

A correção deve ser isolada, testada com os valores já existentes e não combinada com mudanças simultâneas em permissões, schemas ou persistência.
