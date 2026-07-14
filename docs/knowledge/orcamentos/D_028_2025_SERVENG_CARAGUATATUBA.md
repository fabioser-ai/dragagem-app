# D_028_2025- SERVENG - CARAGUATATUBA.xlsx — Dragagem no Rio Juqueriquerê

## Status da análise

- **Arquivo original:** `D_028_2025- SERVENG - CARAGUATATUBA.xlsx`
- **Data da análise:** 14/07/2026
- **Versão do arquivo:** não identificada no nome ou no conteúdo visível do arquivo.
- **Quantidade de abas:** 8.
- **Status:** engenharia reversa vertical concluída para o arquivo analisado.
- Todas as abas, tabelas, células relevantes e fórmulas identificáveis foram examinadas.
- Nenhuma funcionalidade, arquitetura, banco de dados, tela, modelo consolidado ou decisão de implementação foi definido.
- Este documento é exclusivo deste orçamento e não altera registros de outros arquivos.

## Regra de classificação usada neste registro

| Categoria operacional solicitada | Categoria documental equivalente |
| --- | --- |
| **EVIDÊNCIA CONFIRMADA** | Fato observado diretamente no Excel ou anomalia cuja existência é observável. |
| **EVIDÊNCIA PARCIAL** | Interpretação provisória ou possível regra observada somente neste orçamento. |
| **DÚVIDA** | Informação insuficiente, referência não explicada ou comportamento que exige validação. |

Todas as descobertas reutilizáveis deste arquivo possuem **confiança Nível C**, pois foram observadas em uma única fonte.

## Classificação aparente do orçamento

### EVIDÊNCIA CONFIRMADA

**Origem:** abas `Dados Obra`, `Produção`, `3. Dragagem`, `5. Mediçao` e `6. Plan. Preços`.

O arquivo representa um orçamento para:

- cliente `SERVENG`;
- proposta `Proposta D_028_2025`;
- objeto `Rio Juqueriquere`;
- local `Caraguatatuba - SP`;
- dragagem de 31.000 m³;
- uso indicado de draga de 10 polegadas;
- distância total de recalque de 300 m;
- linha flutuante de 200 m;
- linha de terra de 100 m;
- disposição em `Bacia de Decantaçao`;
- medição por `preços unitários de serviços`;
- responsabilidade da FOS pelo canteiro e pela mobilização;
- composição comercial por mobilização, dragagem, medição e desmobilização.

### EVIDÊNCIA PARCIAL

O orçamento aparenta pertencer a uma família de **dragagem direta com disposição em bacia de decantação e medição fortemente baseada em topografia**.

A estrutura não contém fornecimento de bags, preparo de células ou sistema de polímero. A topografia, porém, possui peso econômico muito maior que em uma medição simples, sendo registrada como cinco ações de topografia.

Essa classificação é provisória e não deve ser promovida a padrão geral sem crosscheck.

## Características distintivas observadas

### EVIDÊNCIA CONFIRMADA

- O volume é 31.000 m³ e o prazo matemático calculado é aproximadamente 3,994 meses, depois arredondado para 4 meses nas composições.
- A aba de medição usa quantidade `110.710` para topografia, obtida por `22.142 × 5`, com preço unitário de R$ 0,85.
- O custo de topografia é R$ 94.103,50, representando a maior parcela da medição.
- O seguro de responsabilidade civil parte de R$ 8.269,69 e recebe multiplicador de 1,3.
- A composição de dragagem usa valor patrimonial de equipamento de R$ 1.000.000,00.
- A planilha comercial aplica BDI de 100% aos quatro itens de venda.
- O custo total consolidado é R$ 976.422,52 e o preço total de venda é R$ 1.952.845,04.
- O preço de venda unitário total implícito é aproximadamente R$ 63,00/m³ quando o total comercial é dividido pelo volume.
- A célula `L6` da planilha de preços exibe R$ 57,333251/m³ para a soma de dragagem e medição, sem mobilização e desmobilização.

### EVIDÊNCIA PARCIAL

- A quantidade de topografia pode representar área, extensão, volume de levantamento ou uma unidade operacional própria multiplicada por cinco campanhas. O arquivo não esclarece a unidade física real.
- A aplicação uniforme de BDI de 100% pode representar margem comercial específica desta proposta, e não regra geral.
- A composição de dragagem parece derivada de modelo histórico anterior e adaptada parcialmente para este orçamento.

---

# Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identidade da proposta e premissas técnicas, contratuais e de calendário. |
| 2 | `Produção` | Produção horária, produção mensal e prazo matemático. |
| 3 | `1. Mob. Draga` | Mobilização da draga de 10 polegadas e equipe de carga e montagem. |
| 4 | `2. Canteiro de obras` | Implantação do canteiro e rateio mensal pelo prazo arredondado. |
| 5 | `3. Dragagem` | Composição mensal principal de operação, pessoal, manutenção, apoio, administrativas, BDI e financeiras. |
| 6 | `4. Desmob. Draga` | Desmobilização da draga e equipe correspondente. |
| 7 | `5. Mediçao` | Topografia, seguro de responsabilidade civil e acompanhamento FOS. |
| 8 | `6. Plan. Preços` | Consolidação de custo, quantidade, custo unitário, BDI e preço de venda. |

## Fluxo completo observado

```text
Dados da obra
    ↓
Produção mensal e prazo
    ↓
Mobilização da draga
    ↓
Canteiro de obras e rateio mensal
    ↓
Composição mensal da dragagem
    ↓
Custo total da dragagem por 4 meses
    ↓
Medição e desmobilização
    ↓
Planilha detalhada de custo e venda
```

A sequência visual é linear, mas as dependências são cruzadas. `Dados Obra` e `Produção` alimentam várias abas; o canteiro mensal alimenta `3. Dragagem`; e mobilização, dragagem, medição e desmobilização alimentam `6. Plan. Preços`.

---

# Análise por aba

## 1. Aba `Dados Obra`

### Objetivo

Registrar a identidade comercial e as premissas físicas e operacionais básicas.

### Entradas — EVIDÊNCIA CONFIRMADA

- proposta: `Proposta D_028_2025`;
- data registrada: 03/01/2025;
- cliente: `SERVENG`;
- contato e e-mail: não preenchidos;
- objeto: `Rio Juqueriquere`;
- local: `Caraguatatuba - SP`;
- volume: 31.000 m³;
- tipo de material: não preenchido;
- distância de recalque: 300 m;
- seio da linha de recalque: 0 m;
- linha flutuante: 200 m;
- seio da linha flutuante: 0 m;
- linha de terra: 100 m;
- profundidade, espessura média e área: não preenchidas;
- bota-fora: `Bacia de Decantaçao`;
- sistema de medição: `preços unitários de serviços`;
- canteiro: responsabilidade FOS;
- mobilização: responsabilidade FOS;
- jornada: 9 h/dia;
- calendário: 22 dias/mês.

### Fórmulas — EVIDÊNCIA CONFIRMADA

- `H16 = B16 + E16`: distância total de recalque = 300 m.
- `H17 = B17 + E17`: linha flutuante total = 200 m.
- `G21 = B21 × D21 × B20`: volume geométrico, atualmente igual a zero por ausência de dimensões.

### Entidades conceituais

- proposta;
- cliente;
- contato;
- obra;
- volume contratual;
- material;
- recalque;
- linha flutuante;
- linha de terra;
- bota-fora;
- sistema de medição;
- responsabilidade por canteiro;
- responsabilidade por mobilização;
- jornada e calendário.

### Regras implícitas — EVIDÊNCIA PARCIAL

- O volume informado pode coexistir com um volume geométrico calculável.
- O seio da linha é tratado como parcela adicional da extensão.
- Responsabilidades de canteiro e mobilização são premissas explícitas capazes de alterar custos.

### Dúvidas

- Qual material será dragado no Rio Juqueriquerê?
- Por que profundidade, espessura e área não foram preenchidas?
- O volume de 31.000 m³ vem de levantamento externo, contrato ou estimativa?
- O campo data representa criação, emissão ou data-base de preços?

---

## 2. Aba `Produção`

### Objetivo

Converter parâmetros de bombeamento e calendário em produção útil e prazo.

### Entradas — EVIDÊNCIA CONFIRMADA

- vazão: 350 m³/h;
- eficiência: 70%;
- concentração: 16%;
- jornada: 9 h/dia;
- calendário: 22 dias/mês;
- volume: 31.000 m³.

### Fórmulas — EVIDÊNCIA CONFIRMADA

- `H4 = Dados Obra!B27`: dias por mês.
- `H6 = H3 × H4`: 198 h/mês.
- `D8 = D3 × (D4/100) × (D5/100)`: produção útil = 39,2 m³/h.
- `D11 = H6`: horas trabalhadas por mês.
- `D13 = D8 × D11`: produção mensal = 7.761,6 m³/mês.
- `D18 = D13`: repetição da produção mensal no bloco de prazo.
- `D21 = Dados Obra!B14`: volume = 31.000 m³.
- `D24 = D21 ÷ D18`: prazo = 3,994021851 mês.

### Dependências

- recebe volume, jornada e dias de `Dados Obra`;
- fornece horas mensais para combustível e cálculo de preço por hora;
- fornece prazo para canteiro e custo total da dragagem.

### Regra observada — EVIDÊNCIA PARCIAL

A produção útil é calculada pela multiplicação direta de vazão, eficiência e concentração. O prazo matemático é posteriormente arredondado para cima nas composições dependentes de duração.

### Dúvidas

- Eficiência de 70% e concentração de 16% são específicas desta obra?
- A vazão de 350 m³/h representa capacidade nominal, recomendada ou histórica?
- Há margem operacional adicional além do arredondamento para quatro meses?

---

## 3. Aba `1. Mob. Draga`

### Objetivo

Compor o evento único de mobilização da draga de 10 polegadas.

### Mão de obra — EVIDÊNCIA CONFIRMADA

Equipe diária:

- 1 Operador Líder a R$ 30,00/h;
- 1 Operador de Draga a R$ 26,71/h;
- 4 Ajudantes Gerais a R$ 10,75/h;
- 6 refeições a R$ 40,00;
- 6 transportes a R$ 15,00;
- jornada de 9 h;
- leis sociais de 120%.

Regra:

```text
quantidade × valor-hora × horas/dia × (1 + leis sociais)
```

Custo diário da equipe: **R$ 2.304,258**.

### Serviços e recursos — EVIDÊNCIA CONFIRMADA

- guindaste para carregamento: 1 dia × R$ 2.000,00;
- carreta prancha rebaixada: quantidade vazia, preço de referência R$ 12.800,00;
- carreta extensível: quantidade vazia, preço de referência R$ 4.900,00;
- carreta carga seca para draga: 4 × R$ 8.000,00 = R$ 32.000,00;
- anotação: `Fabiano (7200 - 23/04/2025)`;
- guindaste para descarregamento e montagem: quantidade vazia, anotação `Serveng`;
- trator D4: quantidade vazia;
- mão de obra para carga e montagem: 5 dias × custo diário = R$ 11.521,29.

### Resultados — EVIDÊNCIA CONFIRMADA

- total: R$ 45.521,29;
- BDI interno: 0%;
- preço final de custo: R$ 45.521,29.

### Regras implícitas — EVIDÊNCIA PARCIAL

- Itens sob responsabilidade do cliente podem permanecer na composição com quantidade vazia e custo zero.
- Uma cotação anotada pode diferir do preço efetivamente adotado.
- Mobilização é custo único, não mensal.

### Dúvidas

- Por que a carreta usa R$ 8.000,00 quando a anotação registra R$ 7.200,00?
- A data 23/04/2025 é posterior à data da proposta; houve revisão de cotação?
- O guindaste de descarregamento é fornecido pela SERVENG?

---

## 4. Aba `2. Canteiro de obras`

### Objetivo

Compor a implantação do canteiro e converter o total em custo mensal rateado pelo prazo.

### Mão de obra — EVIDÊNCIA CONFIRMADA

- 1 Operador Líder;
- 1 Operador de Draga;
- 2 Ajudantes Gerais;
- 4 refeições;
- 4 transportes;
- jornada de 9 h;
- leis sociais de 100%;
- transporte de R$ 14,00.

Custo diário: **R$ 1.623,78**.

### Recursos — EVIDÊNCIA CONFIRMADA

Com custo efetivo:

- PPRA + PCMSO + LTCAT: R$ 3.000,00;
- ART principal e corresponsáveis: R$ 500,00;
- EPI: 4 × R$ 400,00 = R$ 1.600,00;
- placa de obra: R$ 4.000,00;
- água potável: 32 galões × R$ 25,00 = R$ 800,00;
- material de escritório: preço unitário R$ 200,00 e total exibido R$ 1.000,00;
- exames médicos: 5 × R$ 400,00 = R$ 2.000,00;
- integração: 2 dias × R$ 1.623,78 = R$ 3.247,56.

Sem custo por quantidade vazia:

- containers;
- frete de containers;
- vigilância;
- banheiro químico.

Anotações `Serveng` aparecem em container almoxarifado, vigilância e banheiro químico.

### Fórmulas e resultados — EVIDÊNCIA CONFIRMADA

- `D25 = ROUNDUP(Produção!D24,0)+1`: quantidade de meses de material de escritório, conceitualmente 5.
- `F29 = SUM(F15:F28)`: total do canteiro = R$ 16.147,56.
- `F30 = ROUNDUP(Produção!D24,0)`: prazo de operação = 4 meses.
- `F31 = F29 × BDI`: BDI interno zero.
- `F32 = F29 ÷ F30`: custo mensal = R$ 4.036,89.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- Na leitura automatizada do arquivo, `D25` e `F30` foram exibidas como `#NAME?`, embora células dependentes apresentem valores compatíveis com prazo de 4 meses e quantidade de 5 meses.
- A fórmula `D24 = 8 × F30` resulta em 32 galões de água.
- A quantidade do material de escritório depende do prazo arredondado mais um mês.

A existência da inconsistência de avaliação é confirmada; não se conclui se o Excel original aberto no Microsoft Excel também exibe erro ou se o problema decorre do mecanismo de cálculo usado na inspeção.

### Dúvidas

- Por que material de escritório usa prazo + 1 mês?
- O canteiro é integralmente de implantação ou inclui consumo durante operação?
- Quais itens anotados como SERVENG são responsabilidades contratuais do cliente?

---

## 5. Aba `3. Dragagem`

### Objetivo

Compor o custo mensal principal de dragagem e custos associados.

### Identificação interna — EVIDÊNCIA CONFIRMADA

A própria aba contém referências que não coincidem integralmente com a proposta atual:

- título: `CUSTO DE DRAGAGEM, Canteiro e Operação do Sistema de Desidratação de lodo`;
- referência: `SERVENG`;
- data interna: `12/04/2021`;
- cliente interno: `DAAE`;
- equipamento: draga de 10 polegadas;
- valor do equipamento: R$ 1.000.000,00.

### Anomalia observada

A identificação `CLIENTE: DAAE`, a data de 2021 e a menção a sistema de desidratação de lodo são resíduos de outro contexto dentro de um orçamento identificado como SERVENG, Caraguatatuba, 2025.

Não se conclui que os cálculos estejam errados; registra-se apenas que a aba foi adaptada sem atualização completa dos textos.

### I — Operação — EVIDÊNCIA CONFIRMADA

Parâmetros:

- horas mensais: 198;
- eficiência de operação do motor: 90%;
- consumo: 40 l/h;
- combustível: R$ 7,00/l.

Fórmula do combustível:

```text
198 × 0,90 × 40 × 7 = R$ 49.896,00/mês
```

Demais custos:

- filtros e lubrificantes: R$ 4.000,00;
- fretes e carretos: R$ 1.500,00;
- segurança e uniformes: R$ 500,00.

Total de operação: **R$ 55.896,00/mês**.

A descrição indica filtros como 10% do combustível, mas R$ 4.000,00 não corresponde a 10% de R$ 49.896,00.

### II — Pessoal — EVIDÊNCIA CONFIRMADA

A aba calcula 257,3999 horas remuneradas por mês a partir de:

- 22 horas extras a 70%;
- 0 horas extras a 100%;
- 219,9999 horas normais;
- fórmula: `(A × 1,70) + (B × 2) + C`.

Equipe efetivamente quantificada:

- 1 Operador Líder a R$ 30,00/h;
- 1 Operador de Draga a R$ 26,71/h;
- 3 Ajudantes a R$ 10,00/h.

Salários: R$ 22.319,145329.

Encargos sociais: 120% = R$ 26.782,974395.

Cantina:

- 2 funcionários alojados;
- 3 funcionários da cidade;
- café R$ 15, almoço R$ 30, jantar R$ 30;
- total mensal: R$ 7.470,00.

Alojamento:

- aluguel: R$ 2.500,00;
- água e luz: R$ 250,00;
- multa de rescisão: R$ 1.000,00;
- limpeza: R$ 200,00;
- total: R$ 3.950,00.

Viagens nas folgas e prêmios de produção estão estruturados, mas sem custo efetivo.

Total de pessoal: **R$ 60.522,119724/mês**.

### III — Manutenção — EVIDÊNCIA CONFIRMADA

Base: equipamento de R$ 1.000.000,00.

- peças e acessórios: 0,6% = R$ 6.000,00/mês;
- docagem anual rateada: 1,0% = R$ 10.000,00/mês;
- limpeza e pintura: R$ 1.000,00;
- mão de obra de terceiros: R$ 1.000,00.

Total: **R$ 18.000,00/mês**.

### IV — Equipamentos de apoio — EVIDÊNCIA CONFIRMADA

Custos diretos do bloco:

- linha de recalque: R$ 5.416,40/mês;
- automóvel, carros e combustível: R$ 5.000,00/mês;
- ferramentas: R$ 350,00/mês;
- canteiro: R$ 4.036,89/mês.

Total: **R$ 14.803,29/mês**.

#### Dimensionamento econômico da linha de recalque

Tubulação:

- 300 m × R$ 120,00 = R$ 36.000,00;
- depreciação em 10 meses = R$ 3.600,00;
- juros de 1% = R$ 360,00;
- custo mensal = R$ 3.960,00.

Flutuantes:

- quantidade: `200/12×3 = 50 peças`;
- 50 × R$ 200,00 = R$ 10.000,00;
- depreciação em 10 meses = R$ 1.000,00;
- juros de 1% = R$ 100,00;
- custo mensal = R$ 1.100,00.

Acoplamentos:

- quantidade: `(300/12)+2 = 27 peças`;
- 27 × R$ 120,00 = R$ 3.240,00;
- depreciação em 10 meses = R$ 324,00;
- juros de 1% = R$ 32,40;
- custo mensal = R$ 356,40.

Total da linha: R$ 5.416,40/mês.

### V — Administrativas — EVIDÊNCIA CONFIRMADA

- comissões: R$ 0,00;
- viagens de inspeção: R$ 2.500,00;
- viagens administrativas: R$ 0,00;
- comunicações: R$ 300,00;
- seguro e licenciamento: vazio.

Total: **R$ 2.800,00/mês**.

### Despesas diretas

```text
Operação + Pessoal + Manutenção + Equipamentos de apoio + Administrativas
= R$ 152.021,409724/mês
```

### VI — BDI interno — EVIDÊNCIA CONFIRMADA

- oficina: 5% das despesas diretas = R$ 7.601,070486;
- administração: 5% das despesas diretas = R$ 7.601,070486;
- outros: vazio.

Total BDI interno: **R$ 15.202,140972/mês**.

### VII — Financeiras — EVIDÊNCIA CONFIRMADA

- depreciação do equipamento em 60 meses: R$ 16.666,666667;
- juros de capital de 1%: R$ 10.000,00;
- atrasos de 0,5% sobre despesas diretas: R$ 760,107049.

Total financeiro: **R$ 27.426,773715/mês**.

### Resultado mensal — EVIDÊNCIA CONFIRMADA

- despesas diretas: R$ 152.021,409724;
- BDI interno: R$ 15.202,140972;
- financeiras: R$ 27.426,773715;
- custo mensal total: **R$ 194.650,324411**.

### Custo total da dragagem

- prazo usado: `ROUNDUP(3,994...,0) = 4 meses`;
- custo total: `R$ 194.650,324411 × 4`;
- resultado: **R$ 778.601,297646**.

### Bloco de preço por hora — EVIDÊNCIA CONFIRMADA

A aba também calcula:

- custo mensal: R$ 194.650,324411;
- BDI multiplicador: 1,6;
- preço de venda mensal: R$ 311.440,519058;
- horas trabalhadas: 198;
- eficiência de operação: 60%;
- horas produtivas: 118,8;
- preço por hora produtiva: R$ 2.621,553191.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- Existem células exibidas como `#NAME?` em horas mensais, produção prevista, prazo e referências do bloco de hora à disposição.
- Apesar disso, células dependentes contêm resultados numéricos consistentes com 198 h/mês, produção de 7.761,6 m³/mês e prazo arredondado de 4 meses.
- O texto `operação Bags` permanece no rótulo do custo total, embora este orçamento indique bacia de decantação e não apresente bags.
- O título menciona sistema de desidratação de lodo, mas não há composição específica de desidratação nesta aba.
- A descrição de filtros como 10% do combustível não coincide com o valor utilizado.
- O resumo não preenche visualmente cada subtotal individual, embora as fórmulas de despesas diretas usem os blocos correspondentes.

### Regras implícitas — EVIDÊNCIA PARCIAL

- O custo da draga é tratado mensalmente e multiplicado pelo prazo inteiro arredondado.
- O valor patrimonial do equipamento alimenta manutenção, depreciação e juros.
- A linha de recalque é tratada como investimento depreciado em 10 meses, acrescido de juros de 1%.
- O canteiro entra como custo mensal dentro da dragagem.
- Existe simultaneamente uma visão de custo por m³ e uma visão de preço por hora produtiva.

### Dúvidas

- A composição de 2021 foi formalmente validada para 2025?
- O valor do equipamento de R$ 1.000.000,00 é valor de reposição, contábil ou comercial?
- Por que a docagem usa 1% ao mês e é descrita como anual?
- Por que a eficiência da produção é 70%, a eficiência de combustível é 90% e a eficiência de preço por hora é 60%?
- Qual é a função operacional do fator adicional 0,62 na fórmula `D234 = J251 × 0,6 × 0,62`?
- O bloco de preço por hora é usado comercialmente ou apenas como referência?

---

## 6. Aba `4. Desmob. Draga`

### Objetivo

Compor o evento único de desmobilização.

### EVIDÊNCIA CONFIRMADA

O título registra `Desmobilização da Draga 6"`, enquanto a mobilização e a composição principal indicam draga de 10 polegadas.

Equipe:

- 1 Operador Líder;
- 1 Operador de Draga;
- 4 Ajudantes Gerais;
- 6 refeições;
- 6 transportes;
- jornada de 9 h;
- leis sociais de 132%.

Custo diário: **R$ 2.411,9448**.

Serviços:

- guindaste: 1 × R$ 3.000,00;
- carreta carga seca: 4 × R$ 8.000,00 = R$ 32.000,00;
- mão de obra: 3 dias × R$ 2.411,9448 = R$ 7.235,8344;
- demais itens com quantidade vazia.

Resultados:

- total: R$ 42.235,8344;
- BDI interno: 0%;
- preço final de custo: R$ 42.235,8344.

### Anomalias observadas

- Divergência de capacidade: título de 6 polegadas versus draga de 10 polegadas no restante do orçamento.
- Leis sociais de 132% diferem dos 120% da mobilização e dos 100% do canteiro.
- O guindaste custa R$ 3.000,00 na desmobilização e R$ 2.000,00 na mobilização.

### Dúvidas

- O título de 6 polegadas é mero resíduo de modelo?
- A diferença de leis sociais é intencional?
- Por que a desmobilização usa somente três dias de equipe, contra cinco na mobilização?

---

## 7. Aba `5. Mediçao`

### Objetivo

Compor os custos de levantamento, seguro e acompanhamento necessários à medição.

### Equipe diária — EVIDÊNCIA CONFIRMADA

- 1 Operador Líder a R$ 17,00/h;
- 1 Operador de Draga a R$ 16,00/h;
- 2 Ajudantes Gerais a R$ 8,00/h;
- 4 refeições a R$ 30,00;
- 4 transportes a R$ 10,00;
- jornada de 9 h;
- leis sociais de 100%.

Custo diário: **R$ 1.042,00**.

### Serviços — EVIDÊNCIA CONFIRMADA

- topografia: `22.142 × 5 = 110.710` unidades;
- preço unitário: R$ 0,85;
- total topografia: R$ 94.103,50;
- observação: `5 Ações de Topografia`;
- seguro de RC: `R$ 8.269,69 × 1,3 = R$ 10.750,597`;
- acompanhamento FOS: 5 dias × R$ 1.042,00 = R$ 5.210,00.

### Resultados — EVIDÊNCIA CONFIRMADA

- total: R$ 110.064,097;
- BDI interno: 0%;
- preço final de custo: R$ 110.064,097.

Existe um segundo bloco de BDI e preço final nas linhas 22 e 23 com resultado zero e sem base preenchida.

### Regras implícitas — EVIDÊNCIA PARCIAL

- A medição pode ser composta por diversas campanhas topográficas.
- O seguro de RC recebe margem ou fator de atualização de 30%.
- A equipe FOS acompanha cada ação de topografia por um dia.

### Dúvidas

- O que representa exatamente a base 22.142?
- A unidade `un` da topografia é adequada ou apenas genérica?
- O multiplicador 1,3 do seguro representa impostos, reajuste, margem ou cobertura adicional?
- O segundo bloco de BDI é resíduo sem uso?

---

## 8. Aba `6. Plan. Preços`

### Objetivo

Consolidar custo total, quantidade, unidade, custo unitário, BDI comercial e preço de venda.

### Itens comerciais — EVIDÊNCIA CONFIRMADA

| Item | Serviço | Custo total | Quantidade | Unidade | Custo unitário | BDI | Preço unitário | Preço total |
| --- | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | Mobilização e montagem de equipamento de dragagem | R$ 45.521,29 | 1 | un | R$ 45.521,29 | 100% | R$ 91.042,58 | R$ 91.042,58 |
| 5 | Dragagem | R$ 778.601,30 | 31.000 | m3 | R$ 25,116171/m³ | 100% | R$ 50,232342/m³ | R$ 1.557.202,60 |
| 7 | Medição | R$ 110.064,10 | 1 | un | R$ 110.064,10 | 100% | R$ 220.128,19 | R$ 220.128,19 |
| 8 | Desmobilização | R$ 42.235,83 | 1 | un | R$ 42.235,83 | 100% | R$ 84.471,67 | R$ 84.471,67 |

### Totais — EVIDÊNCIA CONFIRMADA

- custo total: **R$ 976.422,519046**;
- preço de venda total: **R$ 1.952.845,038092**;
- BDI comercial uniforme: 100%;
- `L6 = (J5 + J6) ÷ volume`: R$ 57,333251/m³ para dragagem + medição.

### Fórmulas principais

- mobilização recebe `1. Mob. Draga!F24`;
- dragagem recebe `3. Dragagem!D247`;
- quantidade da dragagem recebe `Dados Obra!B14`;
- custo unitário da dragagem = custo total ÷ volume;
- medição recebe `5. Mediçao!F20`;
- desmobilização recebe `4. Desmob. Draga!F24`;
- preço unitário = custo unitário × `(1 + BDI/100)`;
- preço total = quantidade × preço unitário;
- custo e preço finais são somados verticalmente.

### Regras implícitas — EVIDÊNCIA PARCIAL

- Dragagem é vendida por m³.
- Mobilização, medição e desmobilização são vendidas como eventos únicos.
- O BDI comercial é aplicado depois da consolidação dos custos internos.
- A planilha distingue BDI interno da composição e BDI comercial da venda.

### Dúvidas

- Por que os números dos itens saltam de 1 para 5, 7 e 8?
- Quais itens 2, 3, 4 e 6 existiam no modelo de origem?
- O preço unitário contratual relevante é R$ 50,232342/m³, R$ 57,333251/m³ ou o total geral dividido por 31.000 m³?
- Mobilização, medição e desmobilização serão faturadas separadamente ou rateadas no preço por m³?

---

# Dependências entre abas

| Origem | Destino | Informação transmitida |
| --- | --- | --- |
| `Dados Obra` | `Produção` | volume, horas/dia e dias/mês. |
| `Dados Obra` | `1. Mob. Draga` | horas/dia. |
| `Dados Obra` | `2. Canteiro de obras` | horas/dia. |
| `Dados Obra` | `3. Dragagem` | dias/mês, distância total e linha flutuante. |
| `Dados Obra` | `4. Desmob. Draga` | horas/dia. |
| `Produção` | `2. Canteiro de obras` | prazo arredondado. |
| `Produção` | `3. Dragagem` | horas mensais, produção mensal e prazo. |
| `2. Canteiro de obras` | `3. Dragagem` | custo mensal do canteiro. |
| `1. Mob. Draga` | `6. Plan. Preços` | custo da mobilização. |
| `3. Dragagem` | `6. Plan. Preços` | custo total da dragagem. |
| `5. Mediçao` | `6. Plan. Preços` | custo da medição. |
| `4. Desmob. Draga` | `6. Plan. Preços` | custo da desmobilização. |

# Entidades conceituais encontradas

### EVIDÊNCIA CONFIRMADA

- proposta;
- cliente;
- obra;
- objeto;
- local;
- volume;
- material;
- equipamento de dragagem;
- parâmetros de produção;
- prazo;
- jornada;
- calendário;
- equipe;
- função;
- salário-hora;
- leis sociais;
- refeição;
- transporte;
- mobilização;
- canteiro;
- dragagem;
- manutenção;
- equipamentos de apoio;
- linha de recalque;
- tubulação;
- flutuante;
- acoplamento;
- despesas administrativas;
- custos financeiros;
- medição;
- topografia;
- seguro de responsabilidade civil;
- desmobilização;
- item comercial;
- custo total;
- custo unitário;
- BDI interno;
- BDI comercial;
- preço de venda.

# Regras de negócio observadas

### EVIDÊNCIA CONFIRMADA

1. Produção útil = vazão × eficiência × concentração.
2. Produção mensal = produção útil × horas/dia × dias/mês.
3. Prazo matemático = volume ÷ produção mensal.
4. Custos mensais dependentes de duração usam prazo arredondado para cima.
5. Mão de obra diária = quantidade × valor-hora × jornada × encargos.
6. Mobilização e desmobilização são eventos únicos.
7. Canteiro é somado e depois rateado pelo prazo arredondado.
8. O custo mensal de dragagem reúne operação, pessoal, manutenção, apoio, administrativas, BDI interno e financeiras.
9. O custo total da dragagem é o custo mensal multiplicado por quatro meses.
10. Linha de recalque, flutuantes e acoplamentos são depreciados em 10 meses e acrescidos de juros de 1%.
11. O valor do equipamento alimenta manutenção, depreciação e juros.
12. A medição reúne topografia, seguro e acompanhamento FOS.
13. O BDI comercial de 100% dobra o custo unitário de cada item.
14. Dragagem é vendida por m³; os demais itens são unidades únicas.

### EVIDÊNCIA PARCIAL

1. Itens de responsabilidade do cliente podem permanecer visíveis com quantidade vazia.
2. O orçamento preserva referências de cotação e fornecedor junto aos preços adotados.
3. Há distinção entre custo interno, BDI interno e margem comercial final.
4. A medição pode acompanhar múltiplas campanhas topográficas.
5. A composição principal é uma adaptação de modelo histórico anterior.

# Coeficientes e valores relevantes deste arquivo

Todos os valores abaixo são específicos desta fonte até validação posterior.

| Parâmetro | Valor observado |
| --- | ---: |
| Vazão | 350 m³/h |
| Eficiência de produção | 70% |
| Concentração | 16% |
| Eficiência do consumo | 90% |
| Eficiência do preço por hora | 60% |
| Horas por dia | 9 |
| Dias por mês | 22 |
| Produção mensal | 7.761,6 m³ |
| Prazo matemático | 3,9940 meses |
| Prazo custeado | 4 meses |
| Leis sociais mobilização | 120% |
| Leis sociais canteiro | 100% |
| Leis sociais dragagem | 120% |
| Leis sociais desmobilização | 132% |
| Valor da draga | R$ 1.000.000,00 |
| Combustível | R$ 7,00/l |
| Consumo | 40 l/h |
| BDI interno da dragagem | 10% total, dividido em 5% oficina e 5% administração |
| BDI comercial | 100% |
| Depreciação linha | 10 meses |
| Depreciação draga | 60 meses |
| Juros de capital | 1% |
| Atrasos | 0,5% das despesas diretas |
| Topografia | 5 ações |
| Seguro RC | base × 1,3 |

# Terminologia observada

- `Seio da linha`: parcela adicional da extensão de recalque ou linha flutuante.
- `Bota Fora`: destino do material dragado.
- `Linha de terra`: trecho terrestre da tubulação.
- `Linha flutuante`: trecho sustentado por flutuadores.
- `Hora à disposição`: preço horário calculado a partir do custo mensal.
- `Horas produtivas`: horas mensais multiplicadas por eficiência operacional.
- `BDI interno`: acréscimos de oficina e administração dentro da composição.
- `BDI comercial`: margem aplicada na planilha de venda.
- `Ações de Topografia`: campanhas ou eventos de levantamento, sem definição física suficiente no arquivo.

# Anomalias e inconsistências consolidadas

### EVIDÊNCIA CONFIRMADA

1. Referências de planilha usam nomes com espaço final, como `'Dados Obra '` e `'1. Mob. Draga '`, enquanto os nomes apresentados não exibem esse espaço.
2. O avaliador da inspeção exibiu `#NAME?` em algumas fórmulas, embora resultados dependentes permaneçam numéricos.
3. A aba de dragagem contém data de 2021 e cliente DAAE em proposta SERVENG de 2025.
4. A aba de dragagem menciona desidratação de lodo e operação de bags sem composição correspondente.
5. A desmobilização indica draga de 6 polegadas, divergindo da draga de 10 polegadas.
6. Filtros descritos como 10% do combustível usam R$ 4.000,00, inferior a 10% do combustível calculado.
7. Leis sociais variam entre 100%, 120% e 132% sem explicação textual.
8. O item material de escritório exibe quantidade `#NAME?` na leitura, mas total de R$ 1.000,00.
9. O bloco de medição possui segundo BDI e preço final zerados e sem base.
10. A numeração comercial salta itens, indicando herança de estrutura mais ampla.
11. Campos relevantes permanecem vazios: material, profundidade, espessura, área, contato e e-mail.
12. A cotação anotada da carreta é R$ 7.200,00, mas o preço adotado é R$ 8.000,00.

# Perguntas para validação futura

1. Qual material será dragado no Rio Juqueriquerê?
2. O volume de 31.000 m³ é contratual ou calculado por topografia?
3. O que representa a base 22.142 multiplicada por cinco ações de topografia?
4. O preço da dragagem será faturado por m³ e os demais itens separadamente?
5. O BDI de 100% é específico desta oportunidade?
6. A composição de custos de 2021 foi validada para preços de 2025?
7. Qual a justificativa das diferentes taxas de leis sociais?
8. A draga correta é de 10 ou 6 polegadas?
9. Quais recursos serão fornecidos pela SERVENG?
10. Qual é o significado do fator 0,62 na fórmula de preço?
11. O seguro de RC multiplicado por 1,3 representa qual acréscimo?
12. Os erros `#NAME?` aparecem quando o arquivo é aberto no Excel ou somente no mecanismo de inspeção?

# Conhecimentos específicos deste orçamento

### EVIDÊNCIA CONFIRMADA

- Dragagem de 31.000 m³ no Rio Juqueriquerê, em Caraguatatuba.
- Recalque total de 300 m, dividido em 200 m flutuantes e 100 m terrestres.
- Produção adotada de 7.761,6 m³/mês.
- Prazo de custo de quatro meses.
- Cinco ações de topografia com custo total de R$ 94.103,50.
- Custo total de R$ 976.422,52.
- Preço de venda de R$ 1.952.845,04.

# Possíveis conhecimentos reutilizáveis

### EVIDÊNCIA PARCIAL

- Estrutura de orçamento por mobilização, operação, medição e desmobilização.
- Uso de produção para transformar volume em prazo e prazo em custo total.
- Canteiro rateado mensalmente e incorporado à operação.
- Separação entre BDI interno e BDI comercial.
- Linha de recalque tratada por depreciação e juros.
- Medição baseada em múltiplas campanhas topográficas.

Nenhum desses itens é consolidado como método geral nesta etapa.

# Limitações da análise

- O arquivo não contém explicações externas, memorial descritivo, contrato, proposta em PDF ou cotações anexas.
- A inspeção preservou fórmulas e valores disponíveis, mas algumas funções foram exibidas como `#NAME?`; não foi possível comprovar se o Microsoft Excel reproduz o mesmo erro.
- Campos vazios impedem concluir material, geometria de dragagem, contato e responsabilidades completas.
- Textos residuais de modelos anteriores tornam algumas interpretações dependentes de validação do especialista.
- Não foi realizada comparação decisória com outros orçamentos.

# Validação final

- [x] Todas as 8 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Entidades, regras, fórmulas, dependências, padrões, exceções, anomalias e dúvidas preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhum documento de outro orçamento alterado.
- [x] Nenhum índice geral ou documento de consolidação alterado.
