# AUDIT_048 — Atestados e Serviços Vinculados

Data: 2026-07-12

## Status e escopo

- Auditoria concluída.
- Nenhum comportamento funcional foi alterado.
- Escopo: entrada pela área Dados, schemas, leitura e normalização, busca, seleção, criação, edição e exclusão de atestados, inclusão e exclusão de serviços vinculados, relação entre os dois CSVs, persistência, feedback, integridade referencial e consumidores observados.

## Componentes observados

- `pages/dados.py`;
- `services/github.py`;
- `services/dados_persistencia.py`;
- `data/atestados.csv`;
- `data/atestados_servicos.csv`;
- `docs/audit/AUDIT_043_DADOS.md`;
- `docs/architecture/16_DADOS.md`.

## Entrada e autorização

A subárea Atestados é acionada por `pages/dados.py` quando `st.session_state.subdados == "atestados"`. O fluxo chama `render_atestados()`.

A tela não revalida autorização nem aplica permissão granular por operação. O acesso depende da autorização geral do módulo Dados. Quem alcança a subárea pode visualizar, criar, editar e excluir atestados, além de criar e excluir serviços vinculados.

## Persistência e schemas

O subsistema usa dois CSVs relacionados:

### `data/atestados.csv`

- `id_atestado`;
- `cliente`;
- `contrato`;
- `obra`;
- `local`;
- `ano`;
- `data_inicio`;
- `data_fim`;
- `descricao`;
- `observacoes`.

### `data/atestados_servicos.csv`

- `id_servico`;
- `id_atestado`;
- `servico`;
- `unidade`;
- `quantidade`;
- `observacoes`.

`garantir_estrutura_atestados()` lê os dois arquivos com `carregar_github()`. Quando um retorno está vazio, cria um DataFrame vazio com o schema esperado. Colunas ausentes são criadas com string vazia, os DataFrames são preenchidos com `fillna("")` e o retorno é reduzido às colunas declaradas.

Consequências observadas:

- falha de leitura, arquivo inexistente e arquivo realmente vazio continuam indistinguíveis para a tela;
- colunas extras são descartadas pelo recorte de schema e podem desaparecer em uma gravação posterior;
- as duas leituras não formam um snapshot atômico: cada arquivo pode representar um instante diferente.

## Dados reais observados

Os dois CSVs já estão populados. O arquivo de atestados contém registros históricos com preenchimento heterogêneo, incluindo:

- campos `ano`, `data_inicio` ou `data_fim` vazios;
- períodos completos armazenados em um único campo textual;
- datas em formatos diferentes, incluindo texto brasileiro e timestamp;
- identificadores existentes em formato abreviado, enquanto novas inclusões usam UUID completo.

O arquivo de serviços vinculados possui volume significativamente maior que o arquivo de atestados e contém quantidades decimais, unidades com grafias variadas e múltiplos serviços por atestado.

A migração de persistência não deve normalizar retroativamente esses dados no mesmo Kid Step.

## Busca e seleção

`filtrar_atestados_por_busca()` pesquisa o termo em todos os valores do atestado e em todos os valores dos serviços. Serviços encontrados produzem uma lista de `id_atestado`, usada para incluir os atestados correspondentes no resultado.

A seleção visual usa um dicionário cuja chave é:

`cliente | obra | contrato`

O valor é `id_atestado`.

Se dois registros produzirem o mesmo rótulo, a entrada posterior substitui a anterior no dicionário. Os UUIDs continuam distintos no CSV, mas um dos registros pode ficar inacessível pelo seletor.

## Criação de atestado

A aba Novo Atestado:

- exige apenas `cliente` e `obra`;
- gera `id_atestado` com `uuid.uuid4()`;
- recebe datas por `date_input` e persiste sua representação textual;
- concatena o novo registro ao DataFrame completo;
- regrava integralmente `data/atestados.csv` com `salvar_github()`;
- apresenta sucesso e executa `st.rerun()` sem verificar resultado estruturado nem reler o arquivo.

Não existe regra de unicidade por cliente, contrato, obra, período ou descrição.

## Edição de atestado

A edição é ativada por `st.session_state.atestado_em_edicao` e localiza o registro pelo `id_atestado` selecionado.

Todos os campos são editáveis. Entretanto, `data_inicio` e `data_fim` usam `text_input`, enquanto a criação usa `date_input`. Assim, o mesmo campo possui contratos de entrada diferentes entre criação e edição.

A edição:

- altera o DataFrame em memória;
- regrava integralmente apenas `data/atestados.csv` com `salvar_github()`;
- remove o marcador de edição da sessão;
- apresenta sucesso e executa `st.rerun()` sem confirmar a gravação.

Serviços vinculados não são alterados quando os dados principais do atestado são editados, pois a relação usa o `id_atestado`, que permanece estável.

## Exclusão de atestado

A exclusão remove:

1. o atestado de `df_atestados`;
2. todos os serviços com o mesmo `id_atestado` de `df_servicos`.

Depois executa duas gravações sequenciais:

1. salva `data/atestados.csv`;
2. salva `data/atestados_servicos.csv`.

Não existe confirmação adicional, transação, rollback ou compensação.

Falhas parciais possíveis:

- primeira gravação conclui e a segunda falha: serviços órfãos permanecem;
- primeira gravação falha e a segunda conclui: o atestado permanece sem seus serviços;
- uma das bases foi lida incorretamente como vazia e é regravada de forma destrutiva.

O uso de SHA esperado em cada arquivo evita sobrescrita concorrente silenciosa, mas não cria atomicidade entre dois arquivos.

## Inclusão de serviço vinculado

A aba Serviços Vinculados seleciona um atestado pelo mesmo rótulo potencialmente ambíguo.

A criação de serviço:

- exige apenas `servico`;
- gera `id_servico` com `uuid.uuid4()`;
- usa o `id_atestado` selecionado;
- recebe quantidade por `number_input` com mínimo zero;
- concatena ao DataFrame completo de serviços;
- regrava integralmente `data/atestados_servicos.csv` com `salvar_github()`;
- apresenta sucesso e executa `st.rerun()` sem confirmação estruturada.

A integridade referencial depende apenas do estado em memória da tela. Não existe validação na persistência de que o `id_atestado` ainda existe no arquivo de atestados no momento da escrita.

## Exclusão de serviço

A interface lista serviços do atestado escolhido, usa o índice do DataFrame filtrado para obter `id_servico`, remove pelo identificador estável e regrava integralmente o CSV de serviços.

Não existe confirmação adicional. Serviços não podem ser editados pela interface observada.

## Concorrência e leitura ambígua

Todos os caminhos ainda usam `carregar_github()` e `salvar_github()`:

- criação de atestado;
- edição de atestado;
- exclusão composta de atestado e serviços;
- criação de serviço;
- exclusão de serviço.

Nenhuma operação usa o SHA obtido pela leitura da tela. Uma sessão pode sobrescrever alterações realizadas por outra sessão após a leitura inicial.

Como falhas de leitura são convertidas em DataFrames vazios, ações posteriores podem substituir um arquivo existente por uma versão incompleta.

## Feedback e tratamento de erros

Os retornos de `salvar_github()` não são verificados. As mensagens de sucesso ou remoção são emitidas após a chamada, sem contrato explícito de resultado e sem releitura de confirmação.

Não existe política uniforme de conflito, retry, indisponibilidade ou bloqueio de botões após leitura não confirmada.

## Consumidores externos

Não foi localizado consumidor funcional externo dos dois CSVs nesta sessão. A busca do conector não retornou referências adicionais, e os componentes observados apontam o uso para `pages/dados.py`.

Essa ausência deve ser tratada como limite da evidência, não como prova definitiva de inexistência de consumidores externos.

## O que foi aprendido

- Atestados e serviços formam um agregado lógico distribuído em dois CSVs.
- Cada registro possui identidade estável, mas os seletores visuais podem ser ambíguos.
- Operações simples regravam um arquivo inteiro; a exclusão do agregado regrava dois arquivos sequencialmente.
- O contrato explícito de leitura e escrita pode proteger cada CSV individualmente contra leitura ambígua e conflito concorrente.
- O contrato atual não fornece transação multi-arquivo nem rollback.
- Os dados históricos reais possuem formatos heterogêneos e não devem ser normalizados incidentalmente durante a migração de persistência.

## O que ainda não foi compreendido

- Existe consumidor externo não indexado ou não localizado para atestados ou serviços?
- Qual é a política oficial de unicidade para atestados?
- Datas devem permanecer texto histórico ou adotar formato canônico para novos registros e edições?
- A exclusão física deve continuar permitida?
- Qual estado deve prevalecer após falha parcial na exclusão composta?
- Deve existir edição de serviços vinculados?
- Quais perfis podem criar, editar e excluir atestados e serviços?

## Observações Técnicas

### OT-099 — Atestados formam agregado lógico em dois CSVs

O atestado é armazenado em um arquivo e seus serviços em outro, ligados por `id_atestado`.

### OT-100 — Exclusão composta não é atômica

A exclusão grava primeiro atestados e depois serviços. Falha parcial pode produzir órfãos ou perda dos vínculos.

### OT-101 — Persistência segura por arquivo não equivale a transação

SHA esperado protege cada atualização individual contra concorrência, mas não garante que duas gravações sejam concluídas juntas.

### OT-102 — Dados históricos possuem formatos heterogêneos

Datas, períodos, identificadores e campos opcionais existentes não seguem um único padrão observável.

### OT-103 — Seletores podem ocultar registros distintos

O rótulo `cliente | obra | contrato` não é garantidamente único e é usado como chave de dicionário.

### OT-104 — Integridade referencial é mantida somente pela tela

A inclusão de serviços usa o atestado selecionado em memória; não há validação referencial na camada de persistência.

### OT-105 — Leitura conjunta não constitui snapshot atômico

Atestados e serviços são carregados em chamadas independentes e podem refletir instantes diferentes.

## Perguntas em Aberto

### PA-032 — Qual política de exclusão deve proteger o agregado?

Deve ser definido se a exclusão física continuará, se haverá desativação lógica ou se será necessário mecanismo de compensação para falha parcial.

### PA-033 — Qual formato oficial de datas e períodos?

A criação usa datas estruturadas, a edição aceita texto e os dados históricos possuem múltiplos formatos.

### PA-034 — Como garantir unicidade e seleção inequívoca?

Deve ser definido um rótulo visual que não esconda registros distintos e, se necessário, uma regra de unicidade de negócio.

### PA-035 — A persistência precisa validar a referência do serviço?

Deve ser decidido se a escrita de serviços deve confirmar que o `id_atestado` existe na versão atual do arquivo principal.

## Baby step seguro

Migrar primeiro os caminhos que alteram apenas um arquivo, preservando comportamento e schemas:

1. criar leitura estruturada separada para atestados e serviços, preservando status e SHA de cada arquivo;
2. bloquear todas as ações de escrita quando a leitura do arquivo correspondente não autorizar escrita;
3. migrar criação e edição de atestado para escrita segura de `atestados.csv`;
4. migrar criação e exclusão de serviço para escrita segura de `atestados_servicos.csv`;
5. verificar resultado antes de sucesso e `st.rerun()`;
6. preservar dados históricos, schemas, geração de UUIDs, busca, filtros e regras atuais;
7. não alterar datas, rótulos, permissões, unicidade ou UI no mesmo Kid Step.

A exclusão composta de atestado e serviços deve ficar fora desse primeiro Kid Step. Ela exige uma decisão explícita de consistência multi-arquivo e não deve ser convertida mecanicamente em duas escritas seguras sem política para falha parcial.
