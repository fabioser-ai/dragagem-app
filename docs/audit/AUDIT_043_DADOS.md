# AUDIT_043 — Auditoria Arquitetural do Módulo Dados

Data: 2026-07-11

## Status e escopo

- Auditoria concluída.
- Nenhum comportamento funcional foi alterado.
- Escopo: entrada e autorização, navegação interna, CRUD genérico, equipamentos, materiais, desaguamento, horários, dias, salários, locais de trabalho, atestados, serviços vinculados, persistência, consumidores e riscos de integridade.

## Componentes diretamente envolvidos

- `app.py`;
- `pages/menu.py`;
- `pages/dados.py`;
- `pages/dados_detalhados/locais_trabalho.py`;
- `services/permissoes.py`;
- `services/github.py`;
- `modulos/medicoes/repositorio.py`;
- `pages/orcamento/etapa0.py`;
- `pages/orcamento/etapa1.py`;
- `pages/orcamento/etapa2.py`.

## Arquivos de dados administrados

- `data/equipamentos.csv`;
- `data/materiais.csv`;
- `data/desaguamento.csv`;
- `data/horarios.csv`;
- `data/dias.csv`;
- `data/salarios.csv`;
- `data/atestados.csv`;
- `data/atestados_servicos.csv`;
- `data/medicoes/locais_trabalho.csv`.

## 1. Entrada, autorização e navegação

O cartão Dados é exibido no menu quando `pode_acessar_modulo("dados")` retorna verdadeiro. O roteador principal chama `dados.render()` quando `st.session_state.tela == "dados"`.

O perfil global `funcionario` é bloqueado pelo roteador principal porque `dados` não pertence à lista de telas permitidas para esse perfil.

Dentro de `pages/dados.py` não existe nova validação de `pode_acessar_modulo("dados")` nem autorização granular por base, operação ou obra. Quem alcança a tela pode visualizar, incluir, editar e excluir registros das bases expostas.

A navegação interna usa `st.session_state.subdados` e um rádio com oito opções:

- Equipamentos;
- Materiais;
- Desaguamento;
- Horários;
- Dias;
- Salários;
- Locais de Trabalho;
- Atestados.

## 2. Papel arquitetural do módulo

Dados funciona como catálogo técnico compartilhado, não apenas como cadastro isolado.

Consumidores observados:

- Orçamentos usa `materiais.csv`, `desaguamento.csv`, `horarios.csv` e `dias.csv` na Etapa 0;
- Orçamentos usa `equipamentos.csv` e `materiais.csv` nos cálculos da Etapa 1;
- Orçamentos usa `salarios.csv` no dimensionamento de equipe da Etapa 2;
- Medições usa `data/medicoes/locais_trabalho.csv` no fluxo operacional de lançamentos.

Assim, alterações administrativas nessas bases podem modificar seletores e cálculos de outros módulos imediatamente, sem versionamento de vigência ou cópia histórica dos parâmetros mestres.

## 3. CRUD genérico

A função `crud()` é reutilizada para equipamentos, materiais, desaguamento, horários, dias e salários.

Fluxo observado:

1. lê o CSV pelo serviço central do GitHub;
2. quando o DataFrame vem vazio, cria um DataFrame com as colunas esperadas;
3. exibe a tabela;
4. permite selecionar uma linha pelo índice do DataFrame;
5. permite editar, excluir ou adicionar;
6. regrava o CSV inteiro.

### 3.1 Leitura ambígua e sobrescrita

Como `carregar_github()` retorna DataFrame vazio para respostas HTTP diferentes de 200, uma falha de autenticação, rede, API ou arquivo inexistente pode ser interpretada como base validamente vazia.

Nesse estado, uma inclusão pode criar um DataFrame novo e substituir o arquivo original por apenas o registro recém-adicionado.

### 3.2 Identidade por índice

Edição e exclusão selecionam a linha pelo índice atual do DataFrame. As bases do CRUD genérico não possuem IDs estáveis próprios.

Não existe confirmação adicional antes da exclusão, histórico, autor, data ou justificativa de alteração.

### 3.3 Validações

O CRUD não exige preenchimento de campos textuais, não verifica duplicidade e não valida regras de domínio como:

- nome único de equipamento;
- vazão ou consumo não negativos;
- percentuais de sólidos dentro de intervalo esperado;
- horário inicial anterior ao final;
- descrição única de jornada;
- posição salarial única;
- valor-hora não negativo.

## 4. Conversão numérica

A função `converter_valores()` envia `Vazao`, `Consumo`, `Valor`, `Valor_Hora`, `Solidos_InSitu` e `Solidos_Desaguado` para `parse_moeda()`.

`parse_moeda()` remove todos os pontos e troca vírgula por ponto, assumindo formato monetário brasileiro.

Consequência observável:

- `120.0` pode ser reinterpretado como `1200`;
- `40.0` pode ser reinterpretado como `400`;
- `0.2` pode ser reinterpretado como `2`.

Esse risco ocorre porque vazão e percentuais usam o mesmo parser destinado a moeda. Os dados atuais de equipamentos e materiais usam ponto decimal nos CSVs, e o formulário de edição apresenta alguns desses valores como texto com ponto.

O problema afeta parâmetros consumidos diretamente nos cálculos de Orçamentos.

## 5. Equipamentos, materiais, desaguamento, horários, dias e salários

Schemas definidos pela tela:

- Equipamentos: `Equipamento`, `Vazao`, `Consumo`, `Valor`;
- Materiais: `Material`, `Solidos_InSitu`, `Solidos_Desaguado`;
- Desaguamento: `Tipo`;
- Horários: `Inicio`, `Fim`;
- Dias: `Descricao`;
- Salários: `Posicao`, `Valor_Hora`.

A tela não registra vigência, versão, status ativo, data de atualização ou responsável.

Registros excluídos deixam de aparecer para novos usos, mas valores já copiados para orçamentos podem permanecer nos agregados existentes. Não existe mecanismo explícito de reconciliação entre cadastro mestre alterado e orçamentos já criados.

## 6. Locais de trabalho

`pages/dados_detalhados/locais_trabalho.py` administra `data/medicoes/locais_trabalho.csv`.

A tela:

- carrega as bases gerais de Medições para obter obras;
- permite selecionar qualquer obra disponível;
- lista locais da obra;
- cria `local_id` estável no formato `LOC_<8 caracteres>`;
- impede nome duplicado na mesma obra por comparação normalizada;
- grava `ativo = sim` e timestamps de criação e atualização.

Limitações observadas:

- não existe edição, desativação ou exclusão pela interface;
- não existe filtragem das obras conforme vínculo ou permissão do usuário;
- o usuário com acesso geral ao módulo Dados pode cadastrar local em qualquer obra carregada;
- a leitura vazia continua sujeita ao risco de substituição integral;
- `carregar_bases()` carrega seis DataFrames, embora a tela use apenas a base de obras.

## 7. Atestados e serviços vinculados

Atestados são mantidos em dois CSVs relacionados:

- `atestados.csv`, identificado por `id_atestado` UUID;
- `atestados_servicos.csv`, identificado por `id_servico` UUID e ligado por `id_atestado`.

### 7.1 Estrutura

A leitura cria colunas ausentes e reduz os DataFrames aos schemas declarados. Colunas extras podem desaparecer em gravações futuras.

A criação de atestado exige somente cliente e obra. Datas usam `date_input` na criação, mas texto livre na edição.

### 7.2 Seletores

Os seletores usam como rótulo a combinação `cliente | obra | contrato`, mapeada para `id_atestado`.

Rótulos idênticos sobrescrevem entradas no dicionário e tornam atestados homônimos inacessíveis pelo seletor, embora possuam UUIDs distintos.

### 7.3 Exclusão composta

Excluir um atestado executa duas gravações sequenciais:

1. remove e salva o atestado;
2. remove e salva os serviços vinculados.

Não existe transação. Se apenas uma gravação concluir, pode haver serviço órfão ou perda parcial de consistência.

A exclusão ocorre sem confirmação adicional.

### 7.4 Serviços

A interface permite adicionar e excluir serviços vinculados, mas não editar um serviço existente.

Quantidade possui mínimo zero. Serviço é o único campo obrigatório na inclusão.

Não existe validação referencial na camada de persistência além do filtro realizado pela tela.

## 8. Tratamento de erros e feedback

As operações principais de CRUD não envolvem gravações em `try/except`. Exceções do serviço central podem interromper a execução e impedir a mensagem de sucesso.

Quando a chamada não lança exceção, a interface exibe sucesso sem reler o arquivo gravado para confirmar o conteúdo persistido.

Não existe política uniforme de confirmação, retry, conflito concorrente ou bloqueio de escrita após leitura ambígua.

## 9. Efeitos sistêmicos

- Alterar vazão ou concentração muda parâmetros-base de novos cálculos de Orçamentos.
- Alterar salários muda a base inicial de novas composições de equipe.
- Alterar horários e dias muda opções da Etapa 0, embora a Etapa 1 ainda use regras textuais fixas para interpretar esses valores.
- Alterar locais afeta opções do fluxo de lançamento de Medições.
- Excluir cadastros mestres pode deixar valores históricos textuais em agregados já existentes, sem vínculo versionado com a origem.

## 10. Observações Técnicas

### OT-083 — Dados é catálogo mestre compartilhado

O módulo fornece parâmetros consumidos por Orçamentos e Medições.

### OT-084 — CRUD genérico usa índice como identidade

Equipamentos, materiais, jornadas e salários não possuem ID estável na interface.

### OT-085 — Leitura ambígua permite sobrescrita destrutiva

Uma falha de leitura pode ser tratada como base vazia e preceder gravação integral.

### OT-086 — Parser monetário é aplicado a grandezas não monetárias

Vazão e percentuais de sólidos usam uma conversão que remove pontos.

### OT-087 — Cadastros mestres não possuem vigência ou histórico

A tela não registra versão, validade, autor ou justificativa das alterações.

### OT-088 — Dados não revalida autorização internamente

Quem alcança a tela possui acesso às operações de todas as bases expostas.

### OT-089 — Locais de trabalho não filtram obras permitidas

A seleção usa todas as obras retornadas por `carregar_bases()`.

### OT-090 — Atestados usam relação entre dois CSVs sem transação

Exclusão de atestado e serviços ocorre em duas gravações independentes.

### OT-091 — Rótulos de atestado podem ser ambíguos

A combinação cliente, obra e contrato é usada como chave visual em dicionário.

### OT-092 — Datas de atestado possuem tipos de entrada diferentes

Criação usa data estruturada; edição usa texto livre.

### OT-093 — Schemas de atestados descartam colunas desconhecidas

Os DataFrames são reduzidos às colunas declaradas.

### OT-094 — Feedback de sucesso não confirma releitura

A interface não valida por leitura posterior o conteúdo efetivamente persistido.

## 11. Perguntas em aberto

- Quais bases devem ser administráveis por cada perfil ou permissão?
- Deve existir autorização granular por cadastro e operação?
- Equipamentos, materiais, jornadas e salários precisam de IDs estáveis?
- Alterações de parâmetros mestres precisam de vigência e histórico?
- Orçamentos devem preservar uma fotografia dos parâmetros ou referenciar versões do cadastro?
- Qual formato numérico oficial deve ser usado na interface e nos CSVs?
- Percentuais de sólidos devem aceitar qual intervalo e unidade?
- Horários e dias devem ser dados livres ou catálogo fechado compatível com as regras da Etapa 1?
- Usuários do módulo Dados podem administrar locais de todas as obras?
- Locais devem oferecer edição, desativação e exclusão?
- Atestados precisam de unicidade por cliente, obra e contrato?
- A exclusão física de atestados e serviços deve continuar permitida?
- Como tratar falha parcial entre gravação do atestado e dos serviços?
- Atestados são consumidos por algum fluxo não identificado nesta auditoria?

## 12. Baby step seguro

O primeiro baby step futuro deve ser separar conversão monetária de conversão numérica geral no CRUD, com testes explícitos para os valores já usados nos CSVs.

Antes de implementar essa correção, deve ser definido o formato oficial de entrada e persistência para moeda, vazão e percentuais. A alteração deve ser isolada e validada sem modificar simultaneamente permissões, schemas ou fluxo de persistência.
