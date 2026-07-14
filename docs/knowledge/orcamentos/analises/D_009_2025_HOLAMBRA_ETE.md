# Análise individual — `D_009_2025- HOLAMBRA - ETE.xlsx`

## 1. Identificação

- **Arquivo-fonte:** `D_009_2025- HOLAMBRA - ETE.xlsx`
- **Data da análise:** 2026-07-14
- **Versão declarada no arquivo:** não identificada
- **Proposta registrada:** `Proposta D_009_2025`
- **Data registrada na aba Dados Obra:** 2025-02-24
- **Quantidade de abas:** 16
- **Status:** ANÁLISE INDIVIDUAL CONCLUÍDA, COM ANOMALIAS E DÚVIDAS REGISTRADAS
- **Escopo:** conhecimento extraído exclusivamente deste arquivo
- **Grau de confiança geral:** Nível C — fonte única, ainda não submetida a crosscheck

## 2. Classificação aparente

### EVIDÊNCIA CONFIRMADA

O arquivo representa um orçamento de **dragagem de lodo de estação de tratamento de esgoto**, para duas lagoas da ETE Cachoeira, em Holambra/SP, com:

- volume nominal de dragagem de 8.000 m³;
- material identificado como `Lodo - ETE`;
- recalque total de 500 m, composto por 200 m de linha flutuante e 300 m de linha de terra;
- desaguamento e acondicionamento em bags;
- preparação de célula com manta PEAD, Bidim e brita;
- preparo e injeção de polímero;
- draga elétrica de 6";
- medição por preços unitários de serviços;
- composição comercial final por itens.

### EVIDÊNCIA PARCIAL

Este orçamento aparenta pertencer à família operacional **dragagem com desaguamento em bags e célula impermeabilizada**, com separação entre mobilização, implantação, fornecimentos, operação, dragagem, medição, transferência e desmobilização.

Essa classificação é válida apenas para este arquivo até futuro crosscheck.

## 3. Estrutura e sequência das abas

1. `Dados Obra`
2. `Orçamentos`
3. `Produção`
4. `1. Mob. Draga`
5. `Barrilete`
6. `2. Mob. Eq. Polimero`
7. `3. Prep. Célula`
8. `4. Forn. Bag`
9. `5. Canteiro de obras`
10. `6. Operação Sistema`
11. `7. Dragagem`
12. `8. Desmob. Draga`
13. `9. Desmob. Eq. Polimero`
14. `10. Mediçao`
15. `11. Transferencia`
16. `12. Plan. Preços`

### EVIDÊNCIA CONFIRMADA

A numeração indica uma sequência comercial/operacional de serviços. `Barrilete`, `Dados Obra`, `Orçamentos` e `Produção` funcionam como abas auxiliares, enquanto as abas numeradas alimentam a composição final.

## 4. Fluxo global observado

1. Dados gerais da obra são registrados em `Dados Obra`.
2. `Produção` transforma vazão, eficiência, concentração, jornada e dias mensais em produção mensal e prazo.
3. Abas de mobilização, implantação e apoio calculam mão de obra e custos diretos.
4. `Barrilete` calcula componentes físicos e aplica depreciação de 25%.
5. `4. Forn. Bag` dimensiona a quantidade de bags com base em volume e teor de sólidos.
6. `6. Operação Sistema` calcula equipamento, polímero, energia, instalações e mão de obra do desaguamento.
7. `7. Dragagem` calcula custo mensal da dragagem, despesas diretas, BDI interno, financeiras e custo total por período.
8. `12. Plan. Preços` reúne custos, quantidades, unidades e percentuais comerciais de BDI para formar preço de venda.

## 5. Análise por aba

---

## 5.1. Dados Obra

### Objetivo

Concentrar identificação da proposta, dados do cliente, características físicas, método de disposição, responsabilidades e calendário de trabalho.

### Entradas confirmadas

- Proposta: `Proposta D_009_2025`
- Data: 2025-02-24
- Cliente: `AEGEA`
- Objeto: `Dragagem duas Lagoas ETE Cachoeira`
- Local: `HOLAMBRA - SP`
- Volume: 8.000 m³
- Material: `Lodo - ETE`
- Distância de recalque: 500 m
- Linha flutuante: 200 m
- Linha de terra: 300 m
- Tipo de bota-fora: `Bag`
- Sistema de medição: `preços unitários de serviços`
- Canteiro de obras: `FOS`
- Mobilização: `FOS`
- Jornada: 9 h/dia
- Dias de trabalho: 22 dias/mês

### Fórmulas

- Recalque total: linha informada + seio da linha.
- Linha flutuante total: linha informada + seio da linha.
- Volume geométrico: área × espessura, embora os campos geométricos estejam vazios e o resultado seja zero.

### Regras e observações

- A própria aba declara convenção visual: azul para dados a preencher, vermelho para pendências e preto para resultados automáticos.
- Profundidade, espessura média e área de dragagem não foram preenchidas.
- Contato e e-mail não foram preenchidos.
- O volume de 8.000 m³ foi informado diretamente, não derivado da geometria nesta planilha.

### DÚVIDA

Não está comprovado se os campos geométricos são opcionais por método de medição, se ficaram pendentes ou se o volume veio de levantamento externo.

---

## 5.2. Orçamentos

### Objetivo aparente

Aba mínima com cabeçalho `Empresa`.

### EVIDÊNCIA CONFIRMADA

Não há conteúdo operacional suficiente além do cabeçalho.

### DÚVIDA

Pode ser resíduo, aba incompleta, ponto de integração ou estrutura não utilizada neste arquivo.

---

## 5.3. Produção

### Objetivo

Calcular produção horária, produção mensal e prazo estimado.

### Entradas

- Vazão: 120 m³/h
- Eficiência: 65%
- Concentração: 15%
- Horas/dia: 9
- Dias/mês: 22
- Volume total: 8.000 m³

### Fórmulas e resultados

- Horas/mês = 9 × 22 = 198 h/mês.
- Produção = 120 × 65% × 15% = 11,7 m³/h.
- Produção mensal = 11,7 × 198 = 2.316,6 m³/mês.
- Prazo = 8.000 ÷ 2.316,6 = 3,4533 meses.

### Regra implícita

A concentração funciona como fator multiplicador da vazão, reduzindo o volume efetivo considerado como produção.

### DÚVIDA

A unidade `m³/h` do resultado pode representar volume de sólidos, volume de lodo equivalente ou produção contratual. O arquivo não define explicitamente.

---

## 5.4. 1. Mob. Draga

### Objetivo

Compor mobilização da draga elétrica de 6".

### Mão de obra diária

- 1 operador líder;
- 2 operadores de draga;
- 4 ajudantes gerais;
- refeições e transporte para 7 pessoas;
- 9 h/dia;
- leis sociais de 100%;
- custo diário: R$ 2.643,56.

### Composição

- guindaste para carregamento;
- carretas;
- guindaste para descarregamento/montagem;
- trator D4;
- mão de obra de carga e montagem.

### Resultado

- Total/Preço final: R$ 33.174,24.
- BDI interno da aba: 0%.

### Observações

- Três carretas de carga seca a R$ 4.700.
- Comentário textual: `Fabiano - 25/02/25 - 4500 + 0,2%`.
- Diversos itens estão zerados por quantidade vazia.

---

## 5.5. Barrilete

### Objetivo

Compor um barrilete global para o sistema de desaguamento.

### Componentes

Tubos, tocos, joelhos, tees, ponteiras, caps, válvulas, mangueira, braçadeiras, curva, bomba lameira e mão de obra.

### Regra de preço

Diversos preços unitários são calculados como preço-base × 1,4.

### Resultados

- Custo integral: R$ 27.964,96.
- Valor apropriado: 25% do custo = R$ 6.991,24.
- BDI: 0%.
- Preço final da aba: R$ 6.991,24.

### Regra implícita

O orçamento não apropria o custo integral do barrilete; apropria 25% como depreciação/consumo da obra.

### DÚVIDA

Não está comprovado se 25% representa depreciação física, reutilização estimada em quatro obras, desgaste, locação interna ou critério comercial.

---

## 5.6. 2. Mob. Eq. Polimero

### Objetivo

Compor mobilização e montagem do equipamento de polímero.

### Componentes

Cobertura, brita, concreto, frete, instalações hidráulicas/elétricas, máquina WAP, barrilete e mão de obra.

### Dependência

O item Barrilete recebe o preço final da aba `Barrilete`.

### Resultado

- Total: R$ 27.047,92.
- BDI: 0%.
- Preço final: R$ 27.047,92.

### Observações

Brita e concreto estão sem quantidades e resultam em zero.

---

## 5.7. 3. Prep. Célula

### Objetivo

Dimensionar e precificar a preparação da célula com manta PEAD, Bidim e brita.

### Dimensionamento físico

Para área de célula de 1.800 m²:

- Manta PEAD: 1,196 m²/m² → 2.152,8 m².
- Bidim: 1,48 m²/m² → 2.664 m².
- Brita: 0,17 m³/m² → 306 m³.
- Retroescavadeira: 0,023 h/m² → 41,4 h.
- Mão de obra: 0,023 h/m² → 41,4 h.
- Conversão de mão de obra: 41,4 ÷ 10 = 4,14 dias.

### Composição de custos

Inclui preparo de terreno, mobilização de máquinas, regularização, manta, instalação, mobilização de equipe especializada, Bidim, brita, retroescavadeira e mão de obra.

### Resultados

- Manta PEAD: R$ 49.514,40.
- Instalação PEAD: R$ 10.764,00.
- Bidim: R$ 21.312,00.
- Brita: quantidade de custo acrescida em 15%, chegando a 351,9 m³; custo R$ 35.190,00.
- Total/Preço final: R$ 143.498,20.
- BDI: 0%.

### Regras e observações

- O acréscimo de 15% é aplicado apenas à quantidade de brita na composição.
- Há indicação `Repassar AEGEA` em itens de preparo/mobilização de máquinas.
- Há observação de que 10.500 m² cobrem a base das duas lagoas.
- A área utilizada no orçamento da célula é 1.800 m².

### DÚVIDA

A relação entre 10.500 m² de base das lagoas e a célula de 1.800 m² não está explicada.

---

## 5.8. 4. Forn. Bag

### Objetivo

Dimensionar e precificar bags para acomodação do lodo desaguado.

### Cálculo físico

- Volume dragado: 8.000 m³.
- Sólidos in situ: 10%.
- Tonelada seca: 800.
- Sólidos após desaguamento: 25%.
- Volume a acomodar = 800 ÷ 25% = 3.200 m³.
- Capacidade informada do bag 8 × 30 m: 430 m³.
- Quantidade usada: 8 bags.
- Capacidade total: 3.440 m³.

### Composição

- 8 bags 8 × 30 m a R$ 35.000;
- frete;
- Munck;
- mão de obra de instalação.

### Resultado

- Total/Preço final: R$ 286.443,56.
- BDI interno: 0%.

### Regras implícitas

- A tonelada seca é calculada numericamente como volume × fração de sólidos, sem densidade explícita.
- O número de bags é informado como 8, suficiente para capacidade superior aos 3.200 m³ calculados.
- A fórmula não arredonda automaticamente a quantidade de bags; o valor 8 está preenchido manualmente.

### DÚVIDA

A equivalência direta de 1 m³ de sólidos para 1 tonelada seca é implícita e não documentada.

---

## 5.9. 5. Canteiro de obras

### Objetivo

Calcular custos de canteiro tratados como subitem da dragagem.

### Componentes

Containers, fretes, programas de segurança, ART, placa, vigilância, água, escritório, banheiro químico, exames e integração.

### Resultado observado

- Total direto: R$ 43.437,12.
- Preço final mostrado: R$ 10.859,28.

### Regra pretendida

O preço final é calculado como total ÷ prazo de operação.

### ANOMALIA OBSERVADA

As células de prazo e quantidades mensais exibem `#NAME?`, embora as fórmulas pretendam usar o prazo arredondado da aba `Produção`.

Consequentemente:

- quantidade de containers;
- material de escritório;
- banheiro químico;
- prazo de operação;
- custo mensal do canteiro

ficam logicamente dependentes de uma referência com erro visível.

### Observação

O valor final de R$ 10.859,28 corresponde a R$ 43.437,12 ÷ 4, indicando que o arquivo conserva valor calculado/cached para quatro meses, apesar do erro exibido nas células de prazo.

---

## 5.10. 6. Operação Sistema

### Objetivo

Calcular operação do sistema de preparo e injeção de polímero.

### Equipe

- 1 operador do sistema;
- 2 ajudantes;
- refeições e transporte para 3 pessoas;
- custo diário: R$ 1.017,78.

### Componentes principais

- equipamento de preparo/injeção: R$ 40.000;
- polímero: 4.400 kg × R$ 25 = R$ 110.000;
- fretes de polímero: R$ 6.000;
- gerador + diesel: R$ 27.132;
- instalações hidráulicas;
- WAP;
- mão de obra: 120 dias × R$ 1.017,78 = R$ 122.133,60.

### Fórmula de polímero

Quantidade = tonelada seca calculada em `4. Forn. Bag` × 5 kg/t × 1,1.

Com 800 t secas:

- base: 4.000 kg;
- acréscimo de 10%: 4.400 kg.

### Resultados

- Total: R$ 308.265,60.
- Prazo usado: 4 meses.
- Custo mensal: R$ 77.066,40.

### Observações textuais

- Polímero: `5 kg por ton seca`.
- Preço registrado de compra em Curitiba: R$ 17/kg.
- Preço utilizado no orçamento: R$ 25/kg.
- Água por caminhão-pipa aparece como responsabilidade da AEGEA e custo zero.
- Gerador contém observação `AEGEA (Margem)`.

### EVIDÊNCIA PARCIAL

O preço de R$ 25/kg aparenta incorporar margem ou contingência sobre uma referência de R$ 17/kg, mas isso não está formalmente declarado.

---

## 5.11. 7. Dragagem

### Objetivo

Calcular o custo mensal da dragagem e integrar operação, pessoal, manutenção, equipamentos de apoio, administrativas, BDI, financeiras e custo total do período.

### Identificação interna

A aba contém dados históricos/residuais:

- referência: `ETE HOLAMBRA`;
- data: 24/05/2018;
- cliente: `DAAE`;
- equipamento: draga elétrica de 6";
- valor do equipamento no estado: R$ 500.000.

### I — Operação

Entradas:

- horas mensais referenciadas da produção;
- eficiência 90%;
- consumo 7;
- valor combustível 7.

Custos exibidos:

- combustível: R$ 8.731,80;
- filtros/lubrificantes: R$ 600;
- fretes/carretos: R$ 1.000;
- segurança/uniformes: R$ 400;
- total: R$ 10.731,80.

### II — Pessoal

Equipe efetivamente quantificada:

- 1 operador líder;
- 1 operador de draga;
- 1 ajudante.

Horas mensais usadas: 219,9999.

Salários: R$ 15.061,19.

Encargos sociais: 100% dos salários = R$ 15.061,19.

Outros custos:

- cantina: R$ 2.160;
- alojamento: R$ 2.250;
- viagens nas folgas: R$ 500.

Total do bloco de pessoal consolidado na aba: R$ 35.032,39.

### III — Manutenção

- peças e acessórios: 0,6% ao mês sobre R$ 500.000 = R$ 3.000;
- docagem anual: 1% ao mês sobre R$ 500.000 = R$ 5.000;
- limpeza/pintura: R$ 250;
- terceiros: R$ 250;
- total: R$ 8.500.

### IV — Equipamentos de apoio

Componentes visíveis:

- linha de recalque;
- automóvel;
- cabo elétrico;
- ferramentas;
- canteiro.

Total do bloco: R$ 27.053,95.

#### Linha de recalque

A linha é decomposta em:

- tubulação: 500 m × R$ 150 = R$ 75.000; depreciação em 12 meses + juros de 1% → R$ 7.000/mês;
- flutuante: 50 peças × R$ 200 = R$ 10.000; depreciação em 12 meses + juros de 1% → R$ 933,33/mês;
- acoplamentos: 43,6667 peças × R$ 150 = R$ 6.550; depreciação em 12 meses + juros de 1% → R$ 611,33/mês;
- total mensal da linha: R$ 8.544,67.

### V — Administrativas

- viagens de inspeção: R$ 2.500;
- comunicações: R$ 300;
- demais itens zerados;
- total: R$ 2.800.

### Despesas diretas

Soma dos blocos I a V: R$ 84.118,13.

### VI — BDI interno

- oficina: 5% das despesas diretas;
- administração: 5% das despesas diretas;
- total: R$ 8.411,81.

### VII — Financeiras

- depreciação do equipamento em 60 meses: R$ 8.333,33;
- juros de capital de 1%: R$ 5.000;
- atrasos de 0,5% sobre despesas diretas: R$ 420,59;
- total: R$ 13.753,92.

### Custo mensal

- custo total mensal da dragagem: R$ 106.283,87;
- operação do sistema de polímero: R$ 77.066,40;
- custo mensal combinado: R$ 183.350,27.

### Custo do período

- tempo de operação usado: 4 meses;
- custo total de dragagem + operação dos bags: R$ 733.401,08.

### Indicadores auxiliares

- BDI comercial auxiliar: 1,6;
- preço de venda mensal: R$ 293.360,43;
- horas produtivas: 118,8;
- preço/hora: R$ 2.469,36.

### ANOMALIAS OBSERVADAS

- Várias células de referência à aba `Produção` exibem `#NAME?`.
- O cabeçalho traz cliente `DAAE`, enquanto `Dados Obra` informa `AEGEA`.
- A data interna de 2018 é incompatível com a proposta de 2025.
- A produção prevista e o tempo de operação aparecem com erro, embora valores dependentes estejam preenchidos/cached.
- O custo de combustível é calculado com fórmula dependente da célula de horas que apresenta erro.
- Existem amplas áreas vazias e blocos históricos aparentemente reutilizados.
- O custo mensal do canteiro é importado de uma aba com erro de prazo, mas apresenta valor numérico.

### EVIDÊNCIA PARCIAL

A aba parece derivada de modelo histórico de custo de draga, reutilizado e adaptado para este orçamento.

---

## 5.12. 8. Desmob. Draga

### Objetivo

Compor desmobilização da draga.

### Diferenças observadas em relação à mobilização

- leis sociais: 132%, contra 100% na mobilização;
- refeição: R$ 35, contra R$ 40;
- mão de obra: 3 dias;
- custo diário: R$ 2.975,53.

### Resultado

- Total/Preço final: R$ 30.526,59.

### ANOMALIA OBSERVADA

Na planilha comercial final, a desmobilização da draga usa o custo da mobilização, R$ 33.174,24, em vez do preço final desta aba.

---

## 5.13. 9. Desmob. Eq. Polimero

### Objetivo

Compor desmontagem e desmobilização do equipamento de polímero.

### Premissas

- leis sociais: 132%;
- custo diário da equipe: R$ 2.253,25;
- frete: R$ 4.700;
- mão de obra de desmontagem: 3 dias.

### Resultado

- Total/Preço final: R$ 11.459,75.

### ANOMALIA OBSERVADA

Na planilha comercial final, o custo usado para este item é R$ 18.933,544, calculado como 70% do custo de mobilização do equipamento de polímero, e não o resultado desta aba.

---

## 5.14. 10. Mediçao

### Objetivo

Compor custos de medição/controle.

### Componentes

- batimetria: quantidade e preço vazios;
- laboratório: 50 × R$ 60 = R$ 3.000;
- acompanhamento FOS: 4 dias × R$ 2.573,56 = R$ 10.294,24.

### Resultado principal

- Total/Preço final: R$ 13.294,24.

### ANOMALIA OBSERVADA

Há um segundo bloco duplicado de BDI e preço final nas linhas finais, resultando em zero.

### Observação

O título interno diz `8 - Medição`, embora a aba seja numerada como item 10.

---

## 5.15. 11. Transferencia

### Objetivo

Compor uma transferência da draga de 6".

### Componentes

- Munck/guindaste: R$ 5.000;
- dois fretes: R$ 3.000;
- mão de obra: 3 dias × R$ 2.573,56 = R$ 7.720,68.

### Resultado

- Total: R$ 15.720,68.
- Prazo: 1.
- Preço final: R$ 15.720,68.

### Regra de cálculo

O preço final é total ÷ prazo de operação.

---

## 5.16. 12. Plan. Preços

### Objetivo

Consolidar custos e aplicar percentuais comerciais de BDI por item.

### Estrutura comercial

| Item | Serviço | Custo | Quantidade | Unidade | BDI | Preço total |
|---|---|---:|---:|---|---:|---:|
| 1 | Mobilização draga | R$ 33.174,24 | 1 | un | 75% | R$ 58.054,92 |
| 2 | Mobilização equipamento polímero e barrilete | R$ 27.047,92 | 1 | un | 75% | R$ 47.333,86 |
| 3 | Preparo de célula | R$ 143.498,20 | 1.800 | m² | 75% | R$ 251.121,85 |
| 4 | Bags 8 × 30 m | R$ 286.443,56 | 8 | un | 60% | R$ 458.309,70 |
| 5 | Dragagem e desaguamento | R$ 733.401,08 | 800 | t base seca | 80% | R$ 1.320.121,95 |
| 6 | Transferência | R$ 15.720,68 | 1 | un | 75% | R$ 27.511,19 |
| 7 | Medição | R$ 13.294,24 | 1 | un | 60% | R$ 21.270,78 |
| 8 | Desmobilização da draga | R$ 33.174,24 | 1 | un | 75% | R$ 58.054,92 |
| 9 | Desmobilização equipamento polímero | R$ 18.933,54 | 1 | un | 75% | R$ 33.133,70 |

### Totais

- Custo total: R$ 1.304.687,71.
- Preço de venda total: R$ 2.274.912,87.

### Fórmula comercial

Preço unitário = custo unitário × (1 + BDI%).

Preço total = quantidade × preço unitário.

### Unidades comerciais observadas

- global/unidade;
- m²;
- peça;
- tonelada de base seca.

### ANOMALIAS OBSERVADAS

1. O custo da desmobilização da draga replica a mobilização e ignora a aba `8. Desmob. Draga`.
2. O custo da desmobilização do equipamento de polímero é 70% da mobilização e ignora a aba `9. Desmob. Eq. Polimero`.
3. Parte dos preços unitários e totais das linhas 2, 3, 5, 6, 8 e 9 não aparece como fórmula identificada, embora contenha valores coerentes com a aplicação do BDI.
4. A célula lateral R$ 2.078.335,47 soma apenas itens 3 a 7, não o orçamento inteiro.
5. O indicador 259,7919 corresponde a R$ 2.078.335,47 ÷ 8.000 m³, mas o total comercial final por m³ seria diferente.
6. O item dragagem é vendido por tonelada de base seca, enquanto vários cálculos de produção e prazo usam m³.

## 6. Entidades conceituais encontradas

### EVIDÊNCIA CONFIRMADA

- Proposta
- Cliente
- Contato
- Obra
- Local
- Material dragado
- Volume dragado
- Linha de recalque
- Draga
- Equipe
- Função
- Jornada
- Leis sociais
- Mobilização
- Desmobilização
- Barrilete
- Equipamento de polímero
- Célula de desaguamento
- Manta PEAD
- Geotêxtil/Bidim
- Brita
- Bag
- Polímero
- Canteiro
- Medição
- Transferência
- Item comercial
- Custo direto
- Custo mensal
- BDI
- Despesa financeira
- Preço de venda
- Unidade de medição

## 7. Regras de negócio extraídas

### EVIDÊNCIA CONFIRMADA

1. Produção mensal deriva de vazão × eficiência × concentração × horas/dia × dias/mês.
2. Prazo deriva de volume total ÷ produção mensal.
3. Custo de mão de obra diária considera quantidade × salário/hora × horas/dia × (1 + leis sociais).
4. Refeição e transporte são multiplicados pelo total de pessoas.
5. Barrilete apropria 25% do custo integral.
6. Manta, Bidim, brita, retroescavadeira e mão de obra são dimensionados por coeficientes por m² de célula.
7. Brita recebe acréscimo de 15% na quantidade de custo.
8. Tonelada seca é calculada como volume × teor de sólidos in situ.
9. Volume após desaguamento é tonelada seca ÷ teor de sólidos final.
10. Polímero é dimensionado em 5 kg/t seca com acréscimo de 10%.
11. Canteiro é transformado em custo mensal pela divisão do total pelo prazo arredondado.
12. Custos mensais de dragagem e operação do sistema são somados e multiplicados pelo prazo arredondado.
13. BDI comercial varia por item entre 60%, 75% e 80%.
14. A composição comercial usa diferentes unidades conforme o serviço.
15. Certos itens podem ser repassados ao cliente e permanecer com custo zero no orçamento.

## 8. Coeficientes e parâmetros específicos deste arquivo

### EVIDÊNCIA PARCIAL — Nível C

- Vazão: 120 m³/h
- Eficiência de produção: 65%
- Concentração: 15%
- Jornada: 9 h/dia
- Dias úteis: 22/mês
- Sólidos in situ: 10%
- Sólidos após desaguamento: 25%
- Polímero: 5 kg/t seca
- Acréscimo de polímero: 10%
- Manta PEAD: 1,196 m²/m² de célula
- Bidim: 1,48 m²/m²
- Brita: 0,17 m³/m²
- Perda/acréscimo de brita: 15%
- Retroescavadeira: 0,023 h/m²
- Mão de obra: 0,023 h/m²
- Barrilete: apropriação de 25%
- Leis sociais: 100% em várias abas; 132% nas desmobilizações
- BDI interno da dragagem: 5% oficina + 5% administração
- Juros: 1% do equipamento
- Atrasos: 0,5% das despesas diretas
- Depreciação da draga: 60 meses
- Depreciação da linha: 12 meses
- BDI comercial: 60%, 75% ou 80%

Nenhum desses valores deve ser promovido a regra geral da FOS sem crosscheck e validação.

## 9. Dependências entre abas

### EVIDÊNCIA CONFIRMADA

- `Dados Obra` → `Produção`
- `Dados Obra` → abas de mão de obra pela jornada
- `Produção` → `5. Canteiro de obras`
- `Produção` → `7. Dragagem`
- `Barrilete` → `2. Mob. Eq. Polimero`
- `Dados Obra` → `4. Forn. Bag`
- `4. Forn. Bag` → `6. Operação Sistema`
- `5. Canteiro de obras` → `7. Dragagem`
- `6. Operação Sistema` → `7. Dragagem`
- abas numeradas → `12. Plan. Preços`

## 10. Terminologia observada

- Bag
- Bota-fora
- Base seca
- Tonelada seca
- Célula
- Manta PEAD
- Bidim RT 14
- Barrilete
- Linha flutuante
- Linha de terra
- Seio da linha
- Equipamento de preparo e injeção de polímero
- Draguista/operador de draga
- Hora à disposição
- Despesas diretas
- Leis sociais
- BDI
- Preço unitário de serviço

## 11. Anomalias consolidadas

### EVIDÊNCIA CONFIRMADA

1. Células `#NAME?` em `5. Canteiro de obras` e `7. Dragagem`.
2. Dados históricos conflitantes na aba Dragagem: DAAE/2018 versus AEGEA/2025.
3. Aba `Orçamentos` praticamente vazia.
4. Desmobilização da draga na planilha comercial não usa a aba de desmobilização.
5. Desmobilização do polímero na planilha comercial não usa a aba de desmobilização.
6. Segundo bloco duplicado e zerado em `10. Mediçao`.
7. Numeração interna de Medição inconsistente.
8. Campos geométricos da dragagem vazios.
9. Quantidade de bags preenchida manualmente, sem arredondamento automático.
10. Responsabilidades AEGEA/FOS aparecem como textos livres e, em alguns casos, custos zerados.
11. Há valores de mercado e comentários datados misturados às fórmulas.
12. Existem resultados numéricos preservados apesar de referências exibirem erro.

## 12. Dúvidas para validação futura

1. A produção de 11,7 m³/h representa sólidos, lodo in situ ou volume contratual?
2. A conversão de 8.000 m³ × 10% = 800 t secas assume densidade de 1 t/m³?
3. Por que a área de célula é 1.800 m² quando há nota de 10.500 m² para as lagoas?
4. O coeficiente de 430 m³ por bag 8 × 30 m é capacidade nominal, útil ou empírica?
5. A apropriação de 25% do barrilete representa qual conceito econômico?
6. O consumo de polímero de 5 kg/t seca é ensaio, experiência ou premissa comercial?
7. O acréscimo de 10% no polímero é perda, segurança ou margem?
8. O prazo comercial deve ser 3,453 meses ou 4 meses?
9. Qual é a origem das leis sociais de 100% e 132%?
10. A desmobilização da draga deve ser igual à mobilização ou usar sua aba própria?
11. A desmobilização do polímero deve ser 70% da mobilização ou usar sua aba própria?
12. O cliente correto é AEGEA ou DAAE?
13. O custo de energia/gerador é da FOS, da AEGEA ou uma margem?
14. Quais itens `Repassar AEGEA` entram ou não entram na proposta?
15. O preço comercial principal deve ser analisado por m³, t seca ou composição de itens?

## 13. Limitações da análise

- A análise foi realizada sobre os valores, fórmulas e textos disponíveis no arquivo.
- Não foram alteradas fórmulas, dados ou formatação.
- Não foi executada consolidação com outros orçamentos.
- Não foi tomada decisão arquitetural.
- Comentários embutidos e elementos gráficos não foram considerados fonte principal; observações textuais visíveis nas células foram preservadas.
- Erros exibidos foram registrados como anomalias, sem inferir correção definitiva.
- Valores numéricos podem ser resultados armazenados pelo Excel mesmo quando células antecedentes apresentam erro.

## 14. Validação final

- [x] Todas as 16 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Fórmulas e dependências principais registradas.
- [x] Regras explícitas e implícitas preservadas.
- [x] Evidências classificadas.
- [x] Anomalias e dúvidas registradas.
- [x] Limitações registradas.
- [x] Nenhuma consolidação realizada.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhum documento de outro orçamento alterado.
