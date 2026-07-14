# D_014_2025 - CLUBE DE CAMPO.xlsx — Desassoreamento de Lago com Bombeamento Direto

## Status

- **Data da análise:** 14/07/2026.
- **Status da análise:** engenharia reversa vertical concluída para o arquivo disponibilizado.
- **Arquivo analisado:** `D_014_2025 - CLUBE DE CAMPO.xlsx`.
- **Versão do arquivo:** não identificada no nome nem em campo específico do workbook.
- **Quantidade de abas:** 9.
- **Todas as abas foram examinadas:** sim.
- **Escopo:** documentação exclusiva deste Excel.
- Nenhuma funcionalidade, arquitetura, banco de dados, tela, índice geral ou documento de consolidação foi criado ou alterado.
- Todas as descobertas reutilizáveis permanecem provisórias, com confiança **Nível C**, pois derivam de uma única fonte.

## Identidade permanente da fonte

- **Nome completo do arquivo:** `D_014_2025 - CLUBE DE CAMPO.xlsx`.
- **Proposta registrada dentro da planilha:** `D_015_225`.
- **Data registrada:** 14/03/2025.
- **Cliente:** `CLUBE DE CAMPO SÃO PAULO`.
- **Contato:** `Marcos`.
- **Objeto:** `Desassoreamento lago com bombeamento direto`.
- **Local:** `CLUBE DE CAMPO SAO PAULO`.
- **Volume informado:** 10.000 m³.
- **Material:** `Areia + Argila`.
- **Equipamento principal indicado:** draga de 6".
- **Destino/bota-fora:** `Área definida pelo Clube`.
- **Sistema de medição:** `preços unitários de serviços`.
- **Responsabilidade pelo canteiro:** FOS.
- **Responsabilidade pela mobilização:** FOS.

## Regra de classificação usada neste registro

| Categoria neste documento | Correspondência documental |
| --- | --- |
| **EVIDÊNCIA CONFIRMADA** | Informação diretamente observada no Excel, inclusive a existência de anomalias. |
| **EVIDÊNCIA PARCIAL** | Interpretação ou possível padrão observado somente neste orçamento. |
| **DÚVIDA** | Informação insuficiente, ambígua, contraditória ou dependente de esclarecimento. |

Uma anomalia é classificada como **EVIDÊNCIA CONFIRMADA quanto à sua existência**, sem concluir automaticamente que o comportamento de negócio está errado.

# 1. Classificação aparente do orçamento

## EVIDÊNCIA CONFIRMADA

O arquivo representa um orçamento de:

- desassoreamento de lago;
- dragagem de areia e argila;
- bombeamento direto;
- volume contratual de 10.000 m³;
- recalque total informado de 300 m;
- linha flutuante total de 100 m;
- linha de terra de 200 m;
- uso de draga de 6";
- preparo de uma área de disposição com referência a ensecadeira/leira;
- medição volumétrica por batimetria;
- composição de mobilização, preparo de área, dragagem, medição e desmobilização;
- formação de preço por itens de serviço.

## EVIDÊNCIA PARCIAL

O orçamento aparenta pertencer à família de **dragagem direta para área de disposição previamente definida**, com necessidade de preparar ou regularizar a área receptora e formar uma contenção/leira.

A planilha também contém uma composição detalhada denominada “Operação do Sistema de Desidratação de lodo”, mas não há no arquivo um pacote explícito de bags, polímero, prensa, centrífuga ou outro equipamento de desaguamento. O título pode ser resíduo de modelo anterior ou pode usar “desidratação” em sentido amplo para a área de disposição. A classificação específica desse componente permanece indeterminada.

## Características diferenciadoras observadas

- restrição física do local teria impedido o uso inicialmente cogitado de draga de 10";
- emprego de draga de 6";
- disposição em área definida pelo clube;
- preparo da área tratado como item comercial próprio;
- nota afirmando que a responsabilidade pelo preparo da área seria definida na proposta como sendo da contratante;
- preço comercial do preparo da área expresso em m²;
- medição por batimetria com cinco unidades comerciais, embora a observação mencione seis visitas;
- grande presença de referências, comentários e fórmulas herdados de modelos anteriores.

# 2. Inventário das abas

| Ordem | Aba | Dimensão observada | Papel no orçamento |
| --- | --- | --- | --- |
| 1 | `Dados Obra` | A1:H27 | Identificação, premissas técnicas, responsabilidades e jornada. |
| 2 | `Produção` | A1:H24 | Produção horária, produção mensal e prazo matemático. |
| 3 | `1. Mob. Draga` | A1:G25 | Mobilização da draga de 6". |
| 4 | `2. Canteiro` | A1:F28 | Canteiro e custo mensal apropriado à dragagem. |
| 5 | `3. Prep. Área - Ensecadeira` | A1:L22 | Preparo da área receptora e dimensionamento simplificado de volume. |
| 6 | `6. Medição` | A1:G24 | Medição volumétrica/batimetria. |
| 7 | `7. Dragagem` | A1:L250 | Composição principal de custo operacional e total da dragagem. |
| 8 | `8. Desmob. Draga` | A1:G21 | Desmobilização da draga. |
| 9 | `Plan. Preços` | A1:M10 | Consolidação comercial dos itens e aplicação de BDI. |

A numeração das abas salta de `3` para `6`, depois `7` e `8`. Não existem no arquivo abas numeradas `4` ou `5`.

# 3. Fluxo completo observado

```text
Dados Obra
    ↓
Produção horária, mensal e prazo
    ↓
Mobilização da draga
    ↓
Canteiro mensal
    ↓
Preparo da área / ensecadeira
    ↓
Composição mensal da dragagem
    ↓
Custo total da dragagem pelo prazo arredondado
    ↓
Medição e desmobilização
    ↓
Planilha de preços de custo e venda
```

As dependências não são estritamente lineares:

- `Dados Obra` alimenta `Produção`, mobilização, canteiro, preparo da área, dragagem e planilha de preços;
- `Produção` alimenta duração, horas mensais, custo unitário e apropriações temporais;
- `2. Canteiro` alimenta `7. Dragagem`;
- `1. Mob. Draga`, `3. Prep. Área - Ensecadeira`, `7. Dragagem`, `6. Medição` e `8. Desmob. Draga` alimentam `Plan. Preços`.

---

# 4. Análise por aba

## 4.1 Aba `Dados Obra`

### Objetivo

Registrar a identidade comercial e as premissas físicas e operacionais da obra.

### Papel no fluxo

É a principal fonte de parâmetros compartilhados.

### Entradas — EVIDÊNCIA CONFIRMADA

- proposta: `D_015_225`;
- data: 14/03/2025;
- cliente: `CLUBE DE CAMPO SÃO PAULO`;
- contato: `Marcos`;
- e-mail: vazio;
- objeto: `Desassoreamento lago com bombeamento direto`;
- local: `CLUBE DE CAMPO SAO PAULO`;
- volume: 10.000 m³;
- material: `Areia + Argila`;
- distância de recalque: 300 m;
- seio adicional do recalque: 0 m;
- linha flutuante: 100 m;
- seio adicional da linha flutuante: 0 m;
- linha de terra: 200 m;
- profundidade: vazia;
- espessura média: vazia;
- área de dragagem: vazia;
- bota-fora: `Área definida pelo Clube`;
- sistema de medição: `preços unitários de serviços`;
- canteiro: FOS;
- mobilização: FOS;
- jornada: 9 h/dia;
- calendário: 22 dias/mês.

### Fórmulas e resultados — EVIDÊNCIA CONFIRMADA

- `B16 = SOMA(B17:B18)`: a distância de recalque é reconstruída pela soma da linha flutuante e da linha de terra, resultando em 300 m.
- `H16 = B16 + E16`: distância total com eventual seio, resultando em 300 m.
- `H17 = B17 + E17`: linha flutuante total com eventual seio, resultando em 100 m.
- `G21 = B21 × D21 × B20`: volume geométrico por área/dimensões e espessura; resulta em zero porque os campos estão vazios.

### Entidades conceituais

- proposta;
- cliente;
- contato;
- obra;
- material;
- volume;
- linha de recalque;
- linha flutuante;
- linha de terra;
- profundidade;
- espessura;
- área;
- bota-fora;
- sistema de medição;
- responsabilidade por canteiro;
- responsabilidade por mobilização;
- jornada e calendário.

### Regras implícitas — EVIDÊNCIA PARCIAL

- O recalque total deve ser coerente com a soma das parcelas flutuante e terrestre.
- Pode haver uma folga física chamada `seio da linha`.
- O volume informado pode coexistir com um volume geométrico calculável.
- Responsabilidades de cliente e FOS são premissas que podem alterar o escopo de custo.

### Anomalias — EVIDÊNCIA CONFIRMADA

- O nome do arquivo indica `D_014_2025`, mas a célula de proposta registra `D_015_225`.
- O ano na proposta interna aparece como `225`, aparentemente incompleto.
- E-mail não preenchido.
- Profundidade, espessura e área não preenchidas.
- O volume geométrico permanece em zero e não valida o volume contratual de 10.000 m³.

### Dúvidas

- Qual é o código correto: `D_014_2025`, `D_015_2025` ou `D_015_225`?
- O volume de 10.000 m³ veio de levantamento anterior, estimativa ou limite contratual?
- O seio representa folga operacional, geometria da tubulação ou reserva de comprimento?
- A área definida pelo clube já existe ou depende integralmente do item de preparo?

---

## 4.2 Aba `Produção`

### Objetivo

Converter capacidade hidráulica e fatores operacionais em produção útil e prazo.

### Entradas — EVIDÊNCIA CONFIRMADA

- vazão: 120 m³/h;
- eficiência: 80%;
- concentração: 15%;
- horas/dia: 9, recebidas de `Dados Obra`;
- dias/mês: 22, recebidos de `Dados Obra`;
- volume: 10.000 m³, recebido de `Dados Obra`.

### Fórmulas — EVIDÊNCIA CONFIRMADA

- horas mensais = 9 × 22 = 198 h/mês;
- produção horária = 120 × 80% × 15% = 14,4 m³/h;
- produção mensal = 14,4 × 198 = 2.851,2 m³/mês;
- prazo matemático = 10.000 ÷ 2.851,2 = 3,507295173961841 meses.

Fórmulas identificadas:

- `H3 = Dados Obra!B26`;
- `H4 = Dados Obra!B27`;
- `H6 = H3 × H4`;
- `D8 = D3 × (D4/100) × (D5/100)`;
- `D11 = H6`;
- `D13 = D8 × D11`;
- `D18 = D13`;
- `D21 = Dados Obra!B14`;
- `D24 = D21 ÷ D18`.

### Saídas

- produção útil: 14,4 m³/h;
- horas mensais: 198 h/mês;
- produção mensal: 2.851,2 m³/mês;
- prazo matemático: 3,5073 meses.

### Regra implícita — EVIDÊNCIA PARCIAL

A concentração é aplicada como fração volumétrica direta da vazão, e a eficiência também é aplicada multiplicativamente.

### Observação explícita

O volume/prazo “pode oscilar dependendo do resultado da batimetria”.

### Dependências

Fornece dados para `2. Canteiro`, `7. Dragagem` e demais cálculos baseados em duração ou produção.

### Dúvidas

- A vazão de 120 m³/h é nominal, histórica ou deliberadamente reduzida?
- Eficiência de 80% e concentração de 15% são específicas desta obra?
- O prazo comercial correto é 3,507 meses, 4 meses, ou 5 meses em componentes com margem adicional?
- A concentração representa sólidos em volume, densidade convertida ou estimativa empírica?

---

## 4.3 Aba `1. Mob. Draga`

### Objetivo

Compor o custo único de mobilização da draga de 6".

### Equipe — EVIDÊNCIA CONFIRMADA

- 2 operadores de draga;
- 2 ajudantes gerais;
- 4 refeições;
- 4 transportes;
- jornada de 9 h/dia;
- leis sociais de 120%.

Cálculo da mão de obra:

```text
quantidade × valor-hora × horas/dia × (1 + leis sociais)
```

Custos:

- operadores: R$ 1.108,80/dia;
- ajudantes: R$ 425,70/dia;
- refeições: R$ 200,00/dia;
- transportes: R$ 40,00/dia;
- custo diário total: R$ 1.774,50.

### Serviços e recursos

- guindaste para carregamento: quantidade vazia, R$ 1.000/dia;
- carreta prancha rebaixada: quantidade e preço vazios;
- carreta extensível: quantidade e preço vazios;
- carreta carga seca para draga: 2 × R$ 7.000 = R$ 14.000;
- guindaste para descarregamento e montagem: 1 × R$ 7.500;
- projeto básico: quantidade vazia, preço de referência R$ 15.000;
- projeto executivo: quantidade vazia, preço de referência R$ 30.000;
- trator D4: quantidade e preço vazios;
- mão de obra de carga e montagem: 5 dias × R$ 1.774,50 = R$ 8.872,50.

### Resultados

- subtotal: R$ 30.372,50;
- BDI interno: 0%;
- preço final: R$ 30.372,50.

### Referências e observações

- carreta carga seca: `Fabiano (estimado)`;
- guindaste de descarregamento: `Chute`.

### Regras implícitas — EVIDÊNCIA PARCIAL

- Mobilização é evento único.
- Itens sem quantidade permanecem como alternativas estruturadas, mas não oneram o total.
- Projetos podem fazer parte do escopo, porém foram zerados neste orçamento.

### Dúvidas

- O preço de R$ 7.000 por carreta é cotação, estimativa ou custo total por viagem?
- Por que o guindaste de carregamento está zerado e o de descarregamento foi incluído?
- Projeto básico e executivo foram excluídos por responsabilidade do cliente ou por não serem necessários?

---

## 4.4 Aba `2. Canteiro`

### Objetivo

Compor custos de implantação/manutenção do canteiro e produzir um valor mensal apropriável à dragagem.

### Equipe

Repete a equipe diária da mobilização:

- 2 operadores;
- 2 ajudantes;
- refeições e transporte para 4 pessoas;
- custo diário: R$ 1.774,50.

### Itens

- container almoxarifado: R$ 1.000/mês, quantidade dependente do prazo;
- banheiro químico: quantidade vazia, R$ 950/mês;
- transferência/Munck: quantidade vazia, R$ 1.000;
- frete para containers: 2 × R$ 500 = R$ 1.000;
- PPRA + PCMSO + LTCAT: R$ 2.000;
- ART principal e corresponsáveis: R$ 500;
- placa de obra: quantidade vazia, R$ 3.000;
- gerador: quantidade vazia, referência de R$ 7.000/mês;
- água potável: 40 galões × R$ 20 = R$ 800;
- material de escritório: R$ 200/mês, quantidade dependente do prazo;
- mão de obra de montagem/desmontagem: 5 dias × R$ 1.774,50 = R$ 8.872,50.

### Fórmulas de duração

- meses/quantidade de container = `ARREDONDAR.PARA.CIMA(prazo, 0) + 1`;
- água potável = `2 × 4 × meses`;
- material de escritório = `ARREDONDAR.PARA.CIMA(prazo, 0) + 1`;
- divisor mensal = `ARREDONDAR.PARA.CIMA(prazo, 0) + 1`.

Com prazo de 3,507 meses, a intenção aparente é usar 5 meses.

### Resultados armazenados

- total nominal: R$ 19.172,50;
- preço final mensal exibido: R$ 3.834,50;
- BDI interno: 0%.

### Regra implícita — EVIDÊNCIA PARCIAL

O custo total do canteiro é distribuído por uma duração inteira acrescida de um mês, aparentemente para cobrir implantação e desmobilização ou margem temporal.

### Anomalias — EVIDÊNCIA CONFIRMADA

As células de duração exibem `#NAME?` no ambiente de leitura, embora a fórmula registrada seja de arredondamento para cima. O valor final de R$ 3.834,50 corresponde a R$ 19.172,50 ÷ 5, indicando que a planilha armazenou resultado calculado anteriormente.

### Dúvidas

- O `+1` significa mês adicional de mobilização/desmobilização?
- O custo mensal deve ser apropriado por 5 meses mesmo que a dragagem seja multiplicada por 4 meses?
- Por que o gerador, banheiro e placa estão zerados?
- A água foi calculada com oito unidades por mês; qual é a unidade operacional exata?

---

## 4.5 Aba `3. Prep. Área - Ensecadeira`

### Objetivo

Compor custos de preparo da área receptora e estimar sua capacidade geométrica.

### Equipe

- 2 operadores de draga;
- 6 ajudantes;
- 8 refeições;
- 8 transportes;
- jornada de 9 h/dia;
- leis sociais de 120%;
- custo diário: R$ 2.865,90.

### Dimensionamento físico

- altura da leira: 1,5 m;
- área indicada: 100 × 50 = 5.000 m²;
- volume possível: 5.000 × 1,5 = 7.500 m³.

### Composição

- regularização manual: 3 dias × R$ 2.865,90 = R$ 8.597,70;
- escavadeira hidráulica sem frete: 8 dias × R$ 3.000 = R$ 24.000;
- trator para limpeza do terreno e acesso: 1 dia × R$ 2.500;
- tubulação para drenagem: quantidade vazia, R$ 15/m;
- mão de obra: 5 dias × R$ 2.865,90 = R$ 14.329,50.

### Resultado

- subtotal: R$ 49.427,20;
- BDI interno: 0%;
- preço final: R$ 49.427,20.

### Observações explícitas

- `SERÁ DEFINIDO EM PROPOSTA QUE A RESPONSABILIDADE DE PREPARO DA ÁREA É DA CONTRATANTE (GORDURA)`.
- Referência da escavadeira: `Danilo 2500 curitiba`, enquanto o preço usado é R$ 3.000.

### Regras e interpretações — EVIDÊNCIA PARCIAL

- O preparo da área é mantido no orçamento mesmo com intenção de atribuir a responsabilidade à contratante.
- A leira é dimensionada de forma simplificada como área plana × altura.
- A capacidade calculada de 7.500 m³ é inferior ao volume de dragagem de 10.000 m³.

### Anomalias — EVIDÊNCIA CONFIRMADA

- O título da aba menciona ensecadeira, mas a composição fala em regularização, limpeza, acesso, drenagem e leira.
- A capacidade geométrica de 7.500 m³ não comporta os 10.000 m³ informados, sem considerar empolamento, água, taludes ou fator de segurança.
- O termo `(GORDURA)` aparece na nota de responsabilidade, possivelmente como comentário interno.
- A referência de preço da escavadeira diverge do preço aplicado.

### Dúvidas

- A área de 100 × 50 é limite real disponível ou premissa de cálculo?
- Haveria necessidade de segunda célula, alteamento ou retirada intermediária?
- A altura útil de 1,5 m considera borda livre?
- O custo deve permanecer na venda se a responsabilidade é da contratante?
- “Ensecadeira” é o termo operacional correto para essa estrutura?

---

## 4.6 Aba `6. Medição`

### Objetivo

Compor a medição volumétrica por batimetria.

### Composição de pessoal

A estrutura contém funções e custos horários, mas quantidades estão zeradas ou vazias:

- operador líder;
- técnico;
- operador de draga;
- ajudante geral;
- refeições;
- transporte.

O custo diário resulta em zero.

### Serviço principal

- batimetria: 5 × R$ 12.000 = R$ 60.000;
- observação: `Baseado em preço Jasao`;
- texto: `serao 6 visitas - acredito que é negociavel por esse preço`;
- texto: `nao fiz cotaçao`.

### Resultado

- total: R$ 60.000;
- BDI interno: 0%;
- preço final: R$ 60.000.

### Anomalias — EVIDÊNCIA CONFIRMADA

- Quantidade comercial: 5.
- Observação operacional: 6 visitas.
- O autor declara não ter realizado cotação.
- A linha usa preço baseado em referência informal.

### Dúvidas

- São cinco medições, seis visitas ou cinco medições além da inicial?
- A unidade `vb` representa visita, campanha ou pacote?
- O preço de R$ 12.000 inclui mobilização e relatório?
- A batimetria será executada por terceiro ou pela FOS?

---

## 4.7 Aba `7. Dragagem`

### Objetivo

Compor o custo mensal e total da dragagem, incluindo operação, pessoal, manutenção, equipamentos de apoio, despesas administrativas, BDI interno e custos financeiros.

### Identificação interna — EVIDÊNCIA CONFIRMADA

- título: `CUSTO DE DRAGAGEM, Canteiro e Operação do Sistema de Desidratação de lodo`;
- referência: `Billings`;
- data interna: `26/06/2018`;
- cliente: `CLUBE DE CAMPO`;
- equipamento: `Draga 6"`;
- observação: inicialmente foi cogitada draga de 10", mas o local não permitiria por causa das dimensões;
- valor do equipamento “no estado”: R$ 300.000.

### I — Operação

Entradas:

- horas mensais: referência a `Produção`;
- eficiência: 0,9;
- consumo por hora: 9;
- valor do combustível: R$ 7.

Custos armazenados:

- combustível: R$ 11.226,60;
- filtros e lubrificantes: 10% do combustível = R$ 1.122,66;
- fretes e carretos: R$ 1.000;
- segurança e uniformes: R$ 500;
- total: R$ 13.849,26.

A fórmula do combustível multiplica horas × eficiência × consumo × preço.

### II — Pessoal

#### Salários

Estrutura de horas:

- total mensal padrão armazenado: 219,9999 h;
- fórmula de total: horas extras 70% × 1,7 + horas extras 100% × 2 + horas normais;
- horas normais: 7,33333 × 30 = 219,9999 h.

Equipe efetivamente onerada:

- 2 operadores de draga a R$ 28/h: R$ 12.319,9944;
- 2 ajudantes a R$ 10,75/h: R$ 4.729,99785.

Funções estruturadas, porém zeradas:

- engenheiro;
- operador líder;
- vigilante;
- motorista;
- operador de booster;
- administrativo.

Subtotal salarial: R$ 17.049,99225.

#### Encargos sociais

- 120% sobre salários;
- valor: R$ 20.459,9907.

#### Alimentação

Tabela-base textual:

- almoço: R$ 10;
- café: R$ 2,50;
- lanche: R$ 2,50;
- jantar: R$ 10.

Tabela efetivamente calculada:

- 2 funcionários alojados: café R$ 3,50, almoço R$ 25, jantar R$ 25, 30 dias = R$ 3.210;
- 2 funcionários da cidade: café R$ 3,50, almoço R$ 25, sem jantar, 22 dias = R$ 1.254;
- total: R$ 4.464.

#### Alojamento

- aluguel: R$ 3.000;
- água e luz: R$ 100;
- multa de rescisão: vazia;
- limpeza: R$ 100;
- total: R$ 3.200.

#### Viagens nas folgas

- 1 unidade de `Funcionários` × R$ 500 = R$ 500.

#### Prêmios de produção

Há estrutura para engenheiro, encarregado, draguistas e ajudantes, sem valores.

#### Total de pessoal

- R$ 45.673,98295.

### III — Manutenção

Base: equipamento de R$ 300.000.

- peças e acessórios: 0,6% ao mês = R$ 1.800;
- docagem anual apropriada: 1,0% ao mês = R$ 3.000;
- limpeza e pintura: R$ 500;
- mão de obra de terceiros: R$ 500;
- total: R$ 5.800.

### IV — Equipamentos de apoio

Custos mensais listados:

- linha de recalque: R$ 4.204,666666666666;
- rebocador e cábrea: R$ 0;
- pick-up: R$ 0;
- caminhão: vazio;
- automóvel: R$ 4.000, anotado como locação + combustível;
- máquina de solda: R$ 0;
- outros: vazio;
- ferramentas: R$ 300;
- canteiro: R$ 3.834,50, recebido de `2. Canteiro`.

Total armazenado: R$ 12.339,166666666666.

#### Subcomposição da linha de recalque

Tubulação:

- 300 m × R$ 120/m = R$ 36.000;
- depreciação em 12 meses = R$ 3.000/mês;
- juros de 1% = R$ 360/mês;
- custo mensal: R$ 3.360.

Flutuantes:

- 25 peças × R$ 200 = R$ 5.000;
- depreciação em 12 meses = R$ 416,6667;
- juros de 1% = R$ 50;
- custo mensal: R$ 466,6667.

Acoplamentos:

- 27 peças × R$ 150 = R$ 4.050;
- depreciação em 12 meses = R$ 337,50;
- juros de 1% = R$ 40,50;
- custo mensal: R$ 378.

Total mensal da linha: R$ 4.204,6667.

Observação textual: `Tubulaçao 8"FGS - R$ 51,06`, divergente do preço de R$ 120/m usado.

### V — Administrativas

- comissões: R$ 0;
- viagens de inspeção: R$ 2.000;
- viagens administrativas: R$ 0;
- comunicações: R$ 300;
- seguro e licenciamento: vazio;
- total: R$ 2.300.

### Despesas diretas

```text
operação
+ pessoal
+ manutenção
+ equipamentos de apoio
+ administrativas
= R$ 79.962,40961666667
```

### VI — BDI interno

- oficina: 5% das despesas diretas = R$ 3.998,1204808333337;
- administração: 5% = R$ 3.998,1204808333337;
- outros: vazio;
- total: R$ 7.996,240961666667.

Este BDI interno de 10% compõe o custo mensal antes do BDI comercial da planilha final.

### VII — Financeiras

- depreciação: valor do equipamento ÷ 60 meses = R$ 5.000;
- juros de capital: 1% do equipamento = R$ 3.000;
- atrasos: vazio;
- total: R$ 8.000.

### Resumo mensal

- despesas diretas: R$ 79.962,40961666667;
- BDI interno: R$ 7.996,240961666667;
- financeiras: R$ 8.000;
- custo total mensal: R$ 95.958,65057833334.

### Produção e preço unitário

- produção prevista: referência à produção mensal de 2.851,2 m³/mês;
- custo unitário: R$ 33,65553120732791/m³;
- margem/BDI adicional na seção: 35%;
- preço de venda calculado: R$ 45,434967129892684/m³;
- hora à disposição: R$ 360,5718991428283.

### Totalização da dragagem

- custo mensal: R$ 95.958,65057833334;
- prazo arredondado: 4 meses;
- custo total: R$ 383.834,60231333337;
- total do item: R$ 383.834,60231333337.

### Quadro de preço por hora

O quadro lateral usa:

- custo mensal;
- fator de venda 1,5;
- horas mensais;
- eficiência de operação 0,75;
- horas produtivas: 148,5;
- preço/hora: R$ 969,2792987710438.

Também existem valores intermediários em L246:L250 associados a custo/produção horária.

### Regras implícitas — EVIDÊNCIA PARCIAL

- O prazo usado no custo total é arredondado para cima, sem mês adicional.
- Equipamentos e linha de recalque são apropriados mensalmente por depreciação e juros.
- O canteiro entra no custo mensal da dragagem.
- Há duas camadas de acréscimo: BDI interno no custo e BDI comercial no preço final.
- O custo horário à disposição e o preço produtivo são métricas distintas.

### Anomalias — EVIDÊNCIA CONFIRMADA

- A aba conserva referência `Billings` e data `26/06/2018`.
- O título menciona sistema de desidratação de lodo sem composição inequívoca desse sistema.
- A aba usa draga 6", mas a linha de recalque é descrita como tubulação 8".
- A observação de preço da tubulação (R$ 51,06) diverge do preço usado (R$ 120).
- As tabelas de refeições apresentam preços-base diferentes dos valores usados.
- Há funções de pessoal zeradas e uma estrutura extensa de itens não utilizados.
- O valor `Turno 8h = 260h/H.mês` não corresponde ao total usado de 219,9999 h.
- Existem fórmulas exibindo `#NAME?` nas referências à aba `Produção`.
- O custo total mensal inclui BDI interno, e a venda final ainda recebe BDI comercial de 81%.
- A seção de preço de venda por m³ usa 35%, enquanto a planilha comercial usa 81%.
- O quadro horário usa fator 1,5, diferente de 35% e 81%.
- A fórmula de hora à disposição usa fatores fixos `0,6` e `0,62`, sem explicação textual.
- A fórmula de combustível usa eficiência 0,9, diferente da eficiência de produção de 80% e da eficiência do quadro horário de 75%.

### Dúvidas

- Qual das três eficiências representa disponibilidade, desempenho hidráulico e produtividade?
- Qual é o preço oficial de combustível e sua data-base?
- Por que a hora mensal usa 220 h, enquanto a produção usa 198 h?
- O valor “no estado” de R$ 300.000 é custo de reposição, contábil ou de aquisição?
- A docagem de 1% ao mês é reserva anual, provisão histórica ou regra específica?
- O automóvel de R$ 4.000 é obrigatório?
- A linha de 8" é compatível e usual com a draga de 6"?
- Qual BDI/margem deve ser considerado para cada finalidade: 10%, 35%, 50% ou 81%?
- O preço à disposição é contratual ou apenas referência interna?
- A referência Billings deve ser removida em revisão futura ou preserva origem legítima do modelo?

---

## 4.8 Aba `8. Desmob. Draga`

### Objetivo

Compor o custo único de retirada da draga.

### Equipe

- 2 operadores a R$ 15/h;
- 2 ajudantes a R$ 8/h;
- 4 refeições a R$ 30;
- 4 transportes a R$ 10;
- jornada de 9 h;
- leis sociais de 120%;
- custo diário: R$ 1.070,80.

### Serviços

- guindaste para carregamento: 1 × R$ 1.000;
- 2 carretas carga seca × R$ 7.000 = R$ 14.000;
- guindaste para descarregamento/montagem: 1 × R$ 7.500;
- trator D4: zerado, observação `Terraplenagem Lavoro`;
- mão de obra: 3 dias × R$ 1.070,80 = R$ 3.212,40.

### Resultado

- total: R$ 25.712,40;
- BDI interno: 0%;
- preço final: R$ 25.712,40.

### Anomalias — EVIDÊNCIA CONFIRMADA

- Os valores-hora e de refeição são menores que os da mobilização.
- A descrição do guindaste permanece “descarregamento e montagem DRAGA”, embora a aba seja de desmobilização.
- O item de trator menciona “lançar draga na água”, também incompatível com retirada.
- A composição aparenta ter sido copiada e parcialmente adaptada.

### Dúvidas

- A diferença salarial entre mobilização e desmobilização é intencional?
- O segundo guindaste seria para descarregamento na base da FOS?
- São realmente necessárias duas carretas de carga seca nas duas pontas?

---

## 4.9 Aba `Plan. Preços`

### Objetivo

Consolidar custos e formar preços de venda por item.

### Estrutura

Colunas:

- item;
- descrição;
- custo total;
- quantidade;
- unidade;
- custo unitário;
- BDI;
- preço unitário;
- preço total.

### Itens — EVIDÊNCIA CONFIRMADA

#### Mobilização

- custo: R$ 30.372,50;
- quantidade: 1 vb;
- BDI: 80%;
- preço: R$ 54.670,50.

#### Preparo de área

- custo: R$ 49.427,20;
- quantidade: 5.000 m²;
- custo unitário: R$ 9,88544/m²;
- BDI: 80%;
- preço unitário: R$ 17,793792/m²;
- total: R$ 88.968,96.

#### Dragagem

- custo: R$ 383.834,60231333337;
- quantidade: 10.000 m³;
- custo unitário: R$ 38,38346023133334/m³;
- BDI: 81%;
- preço unitário: R$ 69,47406301871334/m³;
- total: R$ 694.740,6301871333.

#### Medição

- custo: R$ 60.000;
- quantidade: 5 vb;
- custo unitário: R$ 12.000;
- BDI: 65%;
- preço unitário: R$ 19.800;
- total: R$ 99.000.

#### Desmobilização

- custo: R$ 25.712,40;
- quantidade: 1 vb;
- BDI: 80%;
- preço: R$ 46.282,32.

### Totais armazenados

- custo total exibido: R$ 463.634,3023133334;
- preço de venda: R$ 983.662,4101871334;
- subtotal lateral de preparo + dragagem + medição: R$ 882.709,5901871333;
- preço médio lateral: R$ 88,27095901871333 por m³.

### Fórmulas importantes

- custo unitário = custo total ÷ quantidade;
- preço unitário = custo unitário × (1 + BDI);
- preço total = quantidade × preço unitário;
- preço de venda geral = soma dos preços dos cinco itens.

### Anomalias — EVIDÊNCIA CONFIRMADA

- O custo total `C10 = SOMA(C5:C7)` soma apenas mobilização, preparo e dragagem, excluindo medição e desmobilização.
- Apesar disso, o preço de venda `J10 = SOMA(J5:J9)` inclui os cinco itens.
- O subtotal lateral `L7 = SOMA(J6:J8)` exclui mobilização e desmobilização.
- O preço médio lateral divide esse subtotal por 10.000 m³.
- A dragagem recebe 81%, mobilização/preparo/desmobilização 80% e medição 65%, sem justificativa textual.
- O item de preparo é vendido por m², embora sua finalidade seja conter/dispor volume.
- O item de medição usa quantidade 5, contradizendo a observação de seis visitas.
- O item de desmobilização não possui fórmulas visíveis de custo unitário, BDI e preço unitário, mas o total armazenado corresponde a 80%.

### Dúvidas

- O custo total comercial deveria incluir medição e desmobilização?
- O preço médio lateral de R$ 88,27/m³ representa o núcleo variável da proposta?
- Os BDIs são margens comerciais negociadas por item, impostos embutidos ou composição formal?
- Por que o preparo é vendido por área e não por volume ou verba?
- O total comercial de R$ 983.662,41 foi efetivamente proposto?

---

# 5. Dependências entre abas

| Origem | Destino | Informação |
| --- | --- | --- |
| `Dados Obra` | `Produção` | Horas/dia, dias/mês e volume. |
| `Dados Obra` | `1. Mob. Draga` | Horas/dia. |
| `Dados Obra` | `2. Canteiro` | Horas/dia. |
| `Dados Obra` | `3. Prep. Área - Ensecadeira` | Horas/dia. |
| `Dados Obra` | `7. Dragagem` | Dias/mês, recalque total e linha flutuante. |
| `Dados Obra` | `8. Desmob. Draga` | Horas/dia. |
| `Dados Obra` | `Plan. Preços` | Volume de dragagem. |
| `Produção` | `2. Canteiro` | Prazo arredondado + 1. |
| `Produção` | `7. Dragagem` | Horas mensais, produção mensal e prazo arredondado. |
| `2. Canteiro` | `7. Dragagem` | Custo mensal de canteiro. |
| `1. Mob. Draga` | `Plan. Preços` | Custo de mobilização. |
| `3. Prep. Área - Ensecadeira` | `Plan. Preços` | Custo e área de preparo. |
| `7. Dragagem` | `Plan. Preços` | Custo total da dragagem. |
| `6. Medição` | `Plan. Preços` | Custo da medição. |
| `8. Desmob. Draga` | `Plan. Preços` | Custo da desmobilização. |

# 6. Entidades encontradas

## Comerciais

- proposta;
- cliente;
- contato;
- item de venda;
- unidade comercial;
- custo total;
- custo unitário;
- BDI/margem;
- preço unitário;
- preço total.

## Técnicas e operacionais

- obra;
- lago;
- material dragado;
- volume;
- área;
- profundidade;
- espessura;
- vazão;
- eficiência;
- concentração;
- produção horária;
- produção mensal;
- prazo;
- draga;
- linha de recalque;
- linha flutuante;
- linha terrestre;
- tubulação;
- flutuante;
- acoplamento;
- área de disposição;
- leira/ensecadeira;
- batimetria.

## Recursos

- função profissional;
- salário-hora;
- encargos sociais;
- refeição;
- transporte;
- alojamento;
- equipamento de apoio;
- veículo;
- canteiro;
- fornecedor/referência informal;
- combustível;
- manutenção;
- depreciação;
- juros.

# 7. Regras de negócio extraídas

## EVIDÊNCIA CONFIRMADA

1. Produção útil = vazão × eficiência × concentração.
2. Produção mensal = produção útil por hora × horas/dia × dias/mês.
3. Prazo matemático = volume ÷ produção mensal.
4. Custo total da dragagem usa o prazo arredondado para cima.
5. Canteiro distribui seu total por prazo arredondado para cima + 1.
6. Mão de obra de mobilização, canteiro e preparo usa quantidade × valor-hora × horas/dia × (1 + encargos).
7. Encargos de várias composições são 120%.
8. Manutenção usa percentuais do valor do equipamento.
9. Linha de recalque usa depreciação em 12 meses e juros de 1%.
10. Despesas diretas somam operação, pessoal, manutenção, apoio e administrativas.
11. BDI interno da dragagem soma 5% de oficina e 5% de administração.
12. Financeiras incluem depreciação em 60 meses e juros de 1% do equipamento.
13. A planilha comercial pode aplicar BDI diferente por item.
14. Itens com quantidade vazia permanecem na estrutura e totalizam zero.
15. O preparo da área é comercializado por m².
16. A dragagem é comercializada por m³.
17. Mobilização e desmobilização são comercializadas por verba.
18. Medição é comercializada por múltiplas verbas/unidades.

## EVIDÊNCIA PARCIAL

- O orçamento parece manter um catálogo-modelo amplo, ativando ou desativando itens pela quantidade.
- Custo, preço mensal, preço por m³ e preço por hora coexistem para diferentes usos comerciais.
- A apropriação de custos fixos pelo prazo inteiro é elemento central da composição.
- A área de disposição é tratada como responsabilidade contratual independente da dragagem.
- Referências de fornecedores e “chutes” são preservadas diretamente na planilha para orientar revisão.

# 8. Terminologia observada

- bota-fora;
- linha flutuante;
- linha de terra;
- seio da linha;
- recalque;
- ensecadeira;
- leira;
- gordura;
- batimetria;
- hora à disposição;
- draguista;
- operador líder;
- booster;
- leis sociais;
- valor no estado;
- despesas diretas;
- BDI;
- verba (`vb`);
- preço unitário de serviços;
- docagem;
- cábrea.

# 9. Valores e coeficientes embutidos

Todos os itens abaixo são **EVIDÊNCIA CONFIRMADA quanto à presença no arquivo**, mas **EVIDÊNCIA PARCIAL quanto à reutilização**:

- eficiência de produção: 80%;
- concentração: 15%;
- eficiência de combustível: 90%;
- eficiência do quadro horário: 75%;
- encargos sociais: 120%;
- filtros/lubrificantes: 10% do combustível;
- peças e acessórios: 0,6% ao mês;
- docagem: 1,0% ao mês;
- oficina: 5%;
- administração: 5%;
- depreciação do equipamento: 60 meses;
- juros do equipamento: 1%;
- depreciação da linha: 12 meses;
- BDI comercial: 65%, 80% e 81%;
- margem de preço por m³ na aba de dragagem: 35%;
- fator mensal do quadro horário: 1,5;
- fatores sem explicação na hora à disposição: 0,6 e 0,62;
- mês adicional no canteiro: `+1`.

Nenhum desses valores deve ser promovido a padrão geral da FOS com base apenas neste arquivo.

# 10. Anomalias consolidadas

## Identidade e rastreabilidade

- nome do arquivo e código interno divergentes;
- referência interna a Billings;
- data interna de 2018 em composição de 2025;
- numeração de abas incompleta;
- título de desidratação sem sistema claramente composto.

## Fórmulas e compatibilidade

Foram observadas células exibindo `#NAME?`:

- `2. Canteiro`: D14, D23 e F26;
- `7. Dragagem`: C9, D225, H235, I235, D246 e J247.

As fórmulas correspondem principalmente a referências à aba `Produção` e uso de `ROUNDUP`. Como resultados numéricos armazenados ainda aparecem em células dependentes, a falha pode ser de compatibilidade do mecanismo de cálculo/leitura ou de nomes/funções no arquivo, não necessariamente uma falha original no Excel utilizado pela FOS.

## Coerência física

- área de 5.000 m² × 1,5 m = 7.500 m³, inferior ao volume de 10.000 m³;
- linha de recalque principal: 300 m;
- linha de tubulação apropriada: 300 m;
- linha flutuante informada: 100 m, mas composição usa 25 flutuantes sem comprimento individual explícito;
- draga 6" com tubulação descrita como 8".

## Coerência temporal

- produção usa 198 h/mês;
- salários usam aproximadamente 220 h/mês;
- texto menciona turno de 260 h/mês;
- quadro horário usa 198 h × 75% = 148,5 h produtivas;
- canteiro usa prazo arredondado + 1;
- dragagem usa prazo arredondado sem +1.

## Coerência comercial

- custo total comercial exclui medição e desmobilização;
- preço de venda inclui todos os itens;
- subtotal lateral exclui mobilização e desmobilização;
- múltiplas margens/BDIs sem explicação;
- cinco medições na composição versus seis visitas na observação;
- preparo possivelmente de responsabilidade do cliente, mas incluído na venda.

## Preços e referências

- diversas referências são estimativas, “chute” ou indicação informal;
- batimetria sem cotação;
- preço da escavadeira citado como R$ 2.500 e usado como R$ 3.000;
- preço da tubulação citado como R$ 51,06 e usado como R$ 120;
- preços de refeição divergem entre tabela-base e tabela efetiva.

# 11. Conhecimentos específicos deste orçamento

## EVIDÊNCIA CONFIRMADA

- Clube de Campo São Paulo;
- desassoreamento de lago;
- areia + argila;
- 10.000 m³;
- 300 m de recalque;
- 100 m de linha flutuante;
- draga de 6";
- área de disposição definida pelo cliente;
- preparo de área de 5.000 m²;
- leira de 1,5 m;
- batimetria;
- prazo matemático de 3,507 meses;
- custo total da dragagem de R$ 383.834,60;
- preço de venda geral armazenado de R$ 983.662,41.

## EVIDÊNCIA PARCIAL

- Restrição dimensional do lago determinou equipamento menor.
- A área receptora pode ser gargalo físico do escopo.
- A responsabilidade contratual pelo preparo da área estava aberta durante a elaboração.
- O orçamento utiliza partes de um modelo histórico anterior adaptado.

# 12. Possíveis padrões observados

Todos são **EVIDÊNCIA PARCIAL**, confiança Nível C:

- separação entre dados, produção, eventos fixos, operação e preço;
- cálculo do prazo antes da composição temporal;
- estrutura de composições com itens opcionais zerados;
- formação de custo mensal da dragagem;
- apropriação de equipamentos por depreciação e juros;
- BDI específico por item comercial;
- manutenção de comentários informais dentro do arquivo;
- presença simultânea de preço por m³ e preço por hora.

# 13. Exceções e particularidades

- preparo da área pode ser da contratante;
- equipamento originalmente cogitado foi alterado pela restrição local;
- capacidade geométrica da área não cobre o volume;
- canteiro usa duração diferente da dragagem;
- medição possui quantidade e número de visitas conflitantes;
- desmobilização usa valores de mão de obra diferentes da mobilização;
- composição principal contém resíduos históricos explícitos.

# 14. Dúvidas prioritárias para validação do especialista

1. Qual é o código correto da proposta?
2. A área de 5.000 m² e leira de 1,5 m foi realmente adotada?
3. Como seriam dispostos 10.000 m³ em capacidade geométrica de 7.500 m³?
4. O preparo da área entrou ou não na proposta final?
5. Foram previstas cinco medições ou seis visitas?
6. O valor comercial final de R$ 983.662,41 foi efetivamente enviado?
7. Qual era o preço final por m³ considerado na proposta?
8. Por que a dragagem possui BDI de 81%?
9. O custo mensal de canteiro por cinco meses é deliberado?
10. O custo total comercial deveria incluir medição e desmobilização?
11. As referências Billings/2018 são somente resíduos de template?
12. Havia algum sistema real de desidratação além da área de disposição?
13. A linha era de 8" para uma draga de 6"?
14. Qual preço de tubulação deveria prevalecer?
15. As diferenças de horas mensais são intencionais?
16. As diferenças de valores salariais entre mobilização e desmobilização são intencionais?
17. Qual eficiência corresponde a cada dimensão operacional?
18. O preço à disposição era parte contratual?
19. O valor de R$ 300.000 do equipamento corresponde a qual base econômica?
20. Os custos e preços têm data-base verificável?

# 15. Limitações da análise

- A análise foi realizada exclusivamente sobre o arquivo disponibilizado.
- Não foram fornecidas proposta em PDF, contrato, cotações, e-mails ou medições posteriores.
- Não houve validação oral do especialista durante esta sessão.
- Não é possível concluir quais valores foram efetivamente enviados ao cliente.
- Não é possível distinguir com segurança todos os resíduos de template das decisões conscientes.
- Algumas fórmulas exibem `#NAME?` no mecanismo de leitura, embora existam resultados armazenados.
- Não foi encontrada informação explícita de versão do arquivo.
- Não houve comparação horizontal nem consolidação com outros orçamentos.

# 16. Validação final

- [x] Todas as 9 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Nome completo do arquivo preservado.
- [x] Data da análise registrada.
- [x] Versão registrada como não identificada.
- [x] Quantidade de abas registrada.
- [x] Status da análise registrado.
- [x] Entidades documentadas.
- [x] Regras de negócio documentadas.
- [x] Fórmulas importantes e finalidades documentadas.
- [x] Dependências entre abas documentadas.
- [x] Terminologias documentadas.
- [x] Exceções e anomalias preservadas.
- [x] Evidências classificadas.
- [x] Dúvidas registradas.
- [x] Limitações registradas.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma consolidação realizada.
- [x] Nenhum documento de outro orçamento alterado.
- [x] Nenhum índice geral alterado.
