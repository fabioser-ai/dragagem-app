# Análise individual — `Aguas de Joinville- Dragagem ETA PIRAI.xlsx`

## 1. Identificação da análise

- **Nome completo do arquivo:** `Aguas de Joinville- Dragagem ETA PIRAI.xlsx`
- **Data da análise:** 2026-07-14
- **Versão declarada no arquivo:** não identificada.
- **Última modificação registrada nos metadados do arquivo:** 2025-06-25 12:52:11 UTC.
- **Último autor registrado nos metadados:** Fabio Pereira Serafini.
- **Quantidade de abas:** 15.
- **Status da análise:** análise integral concluída.
- **Documento exclusivo:** este registro trata somente do arquivo acima.
- **Escopo:** descoberta e preservação de conhecimento; nenhuma consolidação, arquitetura ou implementação foi realizada.

## 2. Regra de classificação utilizada

Neste documento:

- **EVIDÊNCIA CONFIRMADA:** informação comprovada diretamente por célula, fórmula, metadado, nome de aba ou relacionamento interno do Excel.
- **EVIDÊNCIA PARCIAL:** interpretação ou padrão observado somente neste orçamento, sem confirmação como regra geral da FOS.
- **DÚVIDA:** ponto sem comprovação suficiente, conflito interno, célula sem explicação ou decisão que exige validação do especialista.

O grau de confiança reutilizável deste registro é **Nível C**, pois deriva de uma única fonte.

## 3. Classificação do orçamento

### EVIDÊNCIA CONFIRMADA

O arquivo representa um orçamento de:

- dragagem de uma lagoa de decantação;
- material classificado como `Lodo - ETA`;
- utilização de draga de 6";
- recalque por tubulação;
- desaguamento por bags;
- preparo de célula com manta PEAD, geotêxtil e camada drenante;
- sistema de preparo e injeção de polímero;
- mobilização, operação, desmobilização, batimetria, projeto e análises;
- medição comercial por preços unitários de serviços.

Cliente indicado na aba `Dados Obra `: `Agua de Joinville`.

Local indicado: `Joinville`.

Volume nominal de dragagem: `3.917 m³`.

### EVIDÊNCIA PARCIAL

Tipo aparente do orçamento: **dragagem de lodo de estação de tratamento de água, com desaguamento em bags e medição principal por tonelada de sólidos secos**.

O processo operacional representado parece ser:

1. mobilizar a draga;
2. mobilizar e montar o sistema de polímero;
3. preparar a célula de recebimento dos bags;
4. fornecer e instalar bags;
5. implantar canteiro;
6. operar a dragagem, o sistema de desidratação e a dosagem de polímero;
7. executar acompanhamento por batimetria, projeto e análises;
8. desmobilizar os equipamentos;
9. consolidar custos e preço de venda;
10. arredondar/reformular a apresentação comercial.

Características que diferenciam este orçamento:

- base econômica de dragagem convertida para toneladas de sólidos secos;
- concentração de sólidos in situ e concentração após desaguamento usadas no dimensionamento;
- custo de polímero derivado da massa seca;
- célula dimensionada em área;
- bags dimensionados por volume útil;
- custo de canteiro mensalizado;
- operação conjunta de dragagem e desaguamento;
- apresentação comercial final com valores manualmente arredondados.

## 4. Inventário das abas

| Ordem | Aba | Papel observado | Situação |
| --- | --- | --- | --- |
| 1 | `Dados Obra ` | Identificação, premissas técnicas, responsabilidades e calendário. | Analisada |
| 2 | `Produção` | Produção horária, produção mensal e prazo. | Analisada |
| 3 | `1. Mob. Draga ` | Mobilização da draga e equipe de apoio. | Analisada |
| 4 | `Barrilete` | Composição do barrilete e apropriação por depreciação. | Analisada |
| 5 | `2. Mob. Eq. Polimero` | Mobilização e montagem do equipamento de polímero. | Analisada |
| 6 | `3. Prep. Célula` | Dimensionamento e custo da célula de bags. | Analisada |
| 7 | `4. Forn. Bag` | Fornecimento, instalação e dimensionamento dos bags. | Analisada |
| 8 | `5. Canteiro de obras` | Custo de implantação e manutenção mensal do canteiro. | Analisada |
| 9 | `6. Operação Sistema` | Operação do sistema de desidratação e consumo de polímero. | Analisada |
| 10 | `7. Dragagem` | Composição central dos custos mensais e totais de dragagem. | Analisada |
| 11 | `8. Desmob. Draga` | Desmobilização física da draga. | Analisada |
| 12 | `9. Desmob. Eq. Polimero ` | Desmontagem e desmobilização do sistema de polímero. | Analisada |
| 13 | `Batimetria` | Projeto, batimetria e análises laboratoriais. | Analisada |
| 14 | `10. Plan. Preços` | Consolidação detalhada de custos e preços com BDI. | Analisada |
| 15 | `11. Arredondamento` | Apresentação comercial simplificada e arredondada. | Analisada |

## 5. Fluxo geral e dependências

### EVIDÊNCIA CONFIRMADA

```text
Dados Obra
   ├── Produção
   │     ├── Canteiro
   │     └── Dragagem
   ├── Mobilizações e desmobilizações
   └── Premissas de jornada

Barrilete
   └── Mobilização do equipamento de polímero

Preparo de Célula
   └── Planilha de Preços

Fornecimento de Bags
   ├── massa seca
   ├── volume desaguado
   ├── quantidade equivalente de bags
   ├── Operação do Sistema
   └── Planilha de Preços

Canteiro
   └── Dragagem

Operação do Sistema
   └── Dragagem

Dragagem
   └── Planilha de Preços

Mobilizações, desmobilizações e Batimetria
   └── Planilha de Preços

Planilha de Preços
   └── referência comercial detalhada

Arredondamento
   └── proposta comercial simplificada, parcialmente manual
```

O arquivo possui dependências em rede, não apenas sequência linear.

## 6. Análise por aba

## 6.1. Aba `Dados Obra `

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** registrar identificação comercial, características físicas da obra, responsabilidades contratuais e calendário operacional.

### Entradas observadas

- proposta: `D_0XX_2025`;
- data armazenada como serial Excel `42671`;
- cliente: `Agua de Joinville`;
- objeto: `Lagoa de Decantaçao`;
- local: `Joinville`;
- volume: `3.917 m³`;
- material: `Lodo - ETA`;
- distância de recalque: `300 m`;
- linha flutuante: `150 m`;
- linha de terra: `150 m`;
- tipo de bota-fora: `Bag`;
- sistema de medição: `preços unitários de serviços`;
- responsabilidade pelo canteiro: `FOS`;
- responsabilidade pela mobilização: `FOS`;
- jornada: `9 h/dia`;
- calendário: `22 dias/mês`.

### Fórmulas e saídas

- distância total de recalque: `B16 + E16 = 300 m`;
- linha flutuante total: `B17 + E17 = 150 m`;
- volume geométrico: `B21 × D21 × B20`, atualmente igual a zero por falta de entradas.

### Regras observadas

**EVIDÊNCIA CONFIRMADA:**

- cores são usadas como semântica: azul para dados a preencher, vermelho para pendências, preto para resultados automáticos;
- o “seio da linha” é somado à distância nominal;
- horário e dias alimentam diversas composições de mão de obra e produção.

### Anomalias e dúvidas

- **DÚVIDA:** a data serial `42671` corresponde a data histórica incompatível com referências de 2025, podendo ser resíduo de modelo.
- **DÚVIDA:** proposta permanece genérica (`D_0XX_2025`).
- **DÚVIDA:** contato e e-mail estão vazios.
- **DÚVIDA:** profundidade, espessura e área estão vazias.
- **EVIDÊNCIA PARCIAL:** o título do arquivo cita ETA Piraí, mas essa identificação não aparece explicitamente nas células desta aba.

## 6.2. Aba `Produção`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** converter vazão, eficiência, concentração e jornada em produção mensal e prazo de execução.

### Entradas

- vazão: `120 m³/h`;
- eficiência: `65%`;
- concentração: `18%`;
- horas/dia: `9`, referenciada de `Dados Obra !B26`;
- dias/mês: `22`, referenciada de `Dados Obra !B27`;
- volume: `3.917 m³`, referenciado de `Dados Obra !B14`.

### Fórmulas

- horas/mês = `9 × 22 = 198 h`;
- produção horária = `120 × 65% × 18% = 14,04 m³/h`;
- produção mensal = `14,04 × 198 = 2.779,92 m³/mês`;
- prazo = `3.917 ÷ 2.779,92 = 1,409033 mês`.

### Regras

**EVIDÊNCIA PARCIAL:** a concentração é tratada como fração volumétrica de sólidos aplicada diretamente à vazão hidráulica para estimar produção de material in situ.

### Dúvidas

- **DÚVIDA:** por que o prazo calculado de 1,409 mês é substituído por `2 meses` em várias abas?
- **DÚVIDA:** confirmar se eficiência de 65% e concentração de 18% são premissas específicas desta obra ou estimativas históricas.
- **DÚVIDA:** confirmar se a unidade da produção calculada representa efetivamente volume in situ dragado.

## 6.3. Aba `1. Mob. Draga `

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** calcular custo de evento único para mobilização da draga de 6".

### Equipe diária

- 2 operadores de draga;
- 2 ajudantes gerais;
- 4 refeições;
- 4 transportes;
- encargos sociais: `120%`;
- custo diário: `R$ 1.643,416`.

Fórmula da mão de obra: `quantidade × valor-hora × horas + encargos`.

### Serviços

- guindaste para carregamento;
- carretas possíveis;
- 2 carretas de carga seca para a draga;
- guindaste para descarregamento e montagem;
- trator D4 opcional;
- 5 dias de mão de obra.

Custo final: `R$ 34.217,08`.

### Observações e anomalias

- existem comentários de cotação em células de apoio;
- carreta prancha e carreta extensível possuem preço, mas quantidade vazia e custo zero;
- trator D4 possui quantidade zero;
- alguns preços totais são fórmulas e outros são números fixos;
- **DÚVIDA:** confirmar se os 5 dias de equipe incluem carga, transporte, lançamento e montagem completos.

## 6.4. Aba `Barrilete`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** compor fisicamente um barrilete de distribuição e apropriar parte de seu valor no orçamento.

### Composição

- tubos de ferro de 6";
- tocos;
- joelhos;
- tees;
- ponteiras;
- caps;
- válvulas;
- mangueiras;
- braçadeiras;
- curvas;
- bomba lameira;
- mão de obra.

Valor integral da composição: `R$ 19.595,558`.

Apropriação: `40% de depreciação = R$ 7.838,2232`.

Preço final: `R$ 7.838,2232`.

### Dependência

O preço final alimenta `2. Mob. Eq. Polimero!E20`.

### Regras e dúvidas

- **EVIDÊNCIA PARCIAL:** o equipamento é apropriado por percentual de depreciação, e não integralmente.
- **DÚVIDA:** por que a taxa é 40% neste orçamento?
- **DÚVIDA:** a nomenclatura “depreciação” representa desgaste, reutilização prevista, locação interna ou recuperação de investimento?
- **DÚVIDA:** confirmar vida útil e quantidade esperada de reutilizações.

## 6.5. Aba `2. Mob. Eq. Polimero`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** calcular a mobilização e montagem do sistema de preparo/injeção de polímero.

### Componentes

- cobertura do equipamento;
- brita para lastro;
- concreto;
- frete;
- instalações hidráulicas;
- instalações elétricas;
- barrilete;
- 5 dias de mão de obra de apoio.

Equipe diária: 2 operadores/técnicos, 2 ajudantes, refeições e transporte.

Custo final: `R$ 42.855,3032`.

### Dependências

- jornada de `Dados Obra`;
- barrilete de `Barrilete!F31`;
- custo diário interno da própria aba.

### Evidência parcial

A mobilização do polímero inclui preparação civil mínima do local, instalações e componente mecânico de distribuição.

## 6.6. Aba `3. Prep. Célula`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** dimensionar materiais e recursos físicos da célula onde os bags serão instalados e calcular seu custo.

### Dimensionamento

Área de célula: `822,25 m²`.

Coeficientes:

- manta PEAD: `1,196 m²/m²`;
- Bidim: `1,48 m²/m²`;
- brita: `0,17 m³/m²`;
- retroescavadeira: `0,023 h/m²`;
- mão de obra: `0,023 h/m²`.

Resultados:

- PEAD: `983,411 m²`;
- Bidim: `1.216,93 m²`;
- brita geométrica: `139,7825 m³`;
- retroescavadeira: `18,91175 h`;
- mão de obra: `18,91175 h`;
- tempo teórico com 10 pessoas: `1,891175 dias`.

### Composição financeira

Inclui:

- patrol e mobilização;
- retroescavadeira e mobilização/desmobilização;
- regularização manual;
- manta PEAD;
- instalação de PEAD;
- taxa de mobilização da equipe de PEAD;
- Bidim;
- brita;
- retroescavadeira para espalhamento;
- mão de obra.

Custo final: `R$ 87.890,653`.

### Valores embutidos e referências

- PEAD: `R$ 15,90/m²`, com observação `Danlo 10/06/25 - 15,90 - DIPROTEC`;
- Bidim: `R$ 6,00/m²`, embora a observação cite `3,39`;
- brita: `R$ 100/m³`, observação `Vogelsanger - Brita 2 - ??? Era 60`;
- quantidade financeira de brita = quantidade geométrica × `1,3`.

### Anomalias e dúvidas

- **EVIDÊNCIA CONFIRMADA:** a quantidade de manta comprada é `900 m²`, inferior ao dimensionamento calculado de `983,411 m²`.
- **EVIDÊNCIA CONFIRMADA:** a quantidade de Bidim usa exatamente o dimensionamento.
- **EVIDÊNCIA CONFIRMADA:** brita inclui multiplicador de 30%.
- **DÚVIDA:** o 1,3 representa empolamento, perdas, compactação ou margem de segurança?
- **DÚVIDA:** por que a área de célula é `822,25 m²` e como foi definida?
- **DÚVIDA:** por que a manta financeira não acompanha o cálculo?
- **DÚVIDA:** validar preços e data-base das cotações.

## 6.7. Aba `4. Forn. Bag`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** precificar fornecimento/instalação e dimensionar a capacidade necessária dos bags.

### Composição financeira

- 4 bags de 8 × 30 m;
- preço unitário: `R$ 35.000`;
- frete e munck com preço cadastrado, mas quantidade vazia;
- 2 dias de equipe de instalação.

Preço final: `R$ 143.792,532`.

### Dimensionamento físico

Premissas:

- volume dragado: `3.917 m³`;
- sólidos totais in situ: `0,1989`, aparentemente 19,89%;
- sólidos após desaguamento: `0,48`, aparentemente 48%;
- capacidade de referência: `75 × 440 = 33.000`;
- capacidades calculadas:
  - bag 8 × 52: `848,64`;
  - bag 6 × 30: `336,60`;
  - bag 8 × 24: `359,04`;
  - soma: `1.544,28`.

Resultados:

- massa seca/base seca: `3.917 × 0,1989 = 779,0913`;
- volume após desaguamento: `779,0913 ÷ 0,48 = 1.623,106875`;
- quantidade equivalente: `1.623,106875 ÷ 440 = 3,688879`.

### Regras e interpretações

- **EVIDÊNCIA PARCIAL:** a planilha converte volume in situ em massa seca por teor de sólidos e depois em volume desaguado.
- **EVIDÊNCIA PARCIAL:** a quantidade comercial de 4 bags arredonda a necessidade equivalente de 3,688879.
- **EVIDÊNCIA PARCIAL:** as fórmulas de capacidade usam dimensões geométricas multiplicadas por fatores `2,4 × 0,85` ou `2,2 × 0,85`.

### Dúvidas

- qual é a unidade exata de `779,0913`: tonelada seca, m³ de sólidos ou outra?
- por que a capacidade de referência usada na divisão é `440`, enquanto as capacidades listadas variam?
- qual a origem dos fatores 2,4, 2,2 e 0,85?
- a solução real usaria 4 bags 8 × 30 ou três bags de dimensões específicas, como afirma a planilha de preços?
- frete e munck são responsabilidade da FOS ou foram intencionalmente zerados?

## 6.8. Aba `5. Canteiro de obras`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** calcular custo total do canteiro e convertê-lo em custo mensal para consumo pela dragagem.

### Componentes

- containers;
- fretes;
- PPRA, PCMSO e LTCAT;
- ART;
- placa;
- vigilância;
- água;
- material de escritório;
- gerador e diesel;
- exames médicos;
- integração.

Custo total: `R$ 57.899,416`.

Prazo adotado: `2 meses`.

Preço final mensal: `R$ 28.949,708`.

### Fórmulas relevantes

- container almoxarifado = `ROUNDUP(prazo calculado, 0) + 1 = 3 meses`;
- água = `6 × meses do container = 18 galões`;
- gerador mensal = `5.500 + (9 × 7 × 22 × 7) = R$ 15.202`;
- preço final = total ÷ 2 meses.

### Anomalias e dúvidas

- **EVIDÊNCIA CONFIRMADA:** o arquivo importado exibe `#NAME?` na quantidade do container em uma leitura de cálculo, embora a fórmula XML seja `ROUNDUP(Produção!D24,0)+1`.
- **EVIDÊNCIA CONFIRMADA:** containers sanitário e escritório, vigilância, possuem preços, mas quantidades vazias e custo zero.
- **DÚVIDA:** o fator `7` no custo de combustível do gerador representa litros por hora e o segundo `7` representa preço por litro?
- **DÚVIDA:** por que o custo mensal é dividido por 2, mas alguns itens foram dimensionados para 3 meses?
- **DÚVIDA:** confirmar se o canteiro deve durar um mês adicional para mobilização/desmobilização.

## 6.9. Aba `6. Operação Sistema`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** calcular custo mensal e total do sistema de desidratação, incluindo polímero e equipe.

### Componentes

- equipamento de preparo e injeção;
- polímero;
- frete;
- água e energia opcionais;
- instalações hidráulicas;
- máquina WAP;
- mão de obra operacional.

### Fórmulas

- valor do equipamento apropriado = `R$ 90.000 × 70% = R$ 63.000`;
- base seca = `779,0913`, referenciada de `4. Forn. Bag`;
- consumo de polímero = `779,0913 × 3 = 2.337,2739 kg`;
- custo do polímero = `2.337,2739 × R$ 23 = R$ 53.757,2997`;
- mão de obra = `60 dias × R$ 821,708 = R$ 49.302,48`;
- custo total = `R$ 175.059,7797`;
- prazo = `2 meses`;
- custo mensal = `R$ 87.529,88985`.

### Regras e dúvidas

- **EVIDÊNCIA PARCIAL:** consumo adotado de polímero: `3 kg por unidade de base seca`.
- **EVIDÊNCIA PARCIAL:** operação é dimensionada em dias corridos (`60 dias` para 2 meses).
- **DÚVIDA:** unidade da base seca e, portanto, do consumo `3`.
- **DÚVIDA:** motivo da apropriação de 70% do equipamento.
- **DÚVIDA:** água e energia estão zeradas por responsabilidade do cliente ou omissão?
- **DÚVIDA:** por que o prazo é fixado em 2 meses, e não ligado diretamente à produção calculada?

## 6.10. Aba `7. Dragagem`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** concentrar custos mensais de operação da draga, pessoal, manutenção, apoio, administração, BDI e finanças; incorporar canteiro e operação do sistema; calcular custo total da dragagem e preço por hora.

### Identificações internas

A aba contém:

- `REF.: Limpeza bacia de acumulaçao`;
- `CLIENTE: ENFIL`;
- `EQUIPAMENTO: Draga 6"`;
- `DATA: 24/06/2025`;
- valor do equipamento “no estado”: `R$ 250.000`.

### I — Operação

- horas/mês: `198`;
- eficiência: `0,9`;
- consumo: `9`;
- combustível: `R$ 7`;
- combustível: `R$ 11.226,60`;
- filtros/lubrificantes: `10%` do combustível;
- fretes: `R$ 1.000`;
- segurança/uniformes: `R$ 500`;
- total: `R$ 13.849,26`.

### II — Pessoal

Horas remuneradas por mês: `219,9999`, calculadas por:

- horas extras 70%;
- horas extras 100%;
- horas normais;
- fórmula final `(A × 1,70) + (B × 2) + C`.

Equipe efetivamente quantificada:

- 1 operador de draga;
- 1 ajudante.

Salários: `R$ 8.241,196254`.

Encargos sociais: `120% = R$ 9.889,435505`.

Cantina: `R$ 2.310`.

Alojamento: `R$ 5.500`.

Viagens de folga: zero.

Prêmios de produção: sem valores.

Total pessoal e benefícios: `R$ 25.940,631759`.

### III — Manutenção

- peças e acessórios: `0,6% ao mês` sobre o equipamento;
- docagem anual apropriada: `1,0% ao mês`;
- limpeza e pintura;
- terceiros.

Total: `R$ 5.000`.

### IV — Equipamentos de apoio e linha de recalque

Custos de apoio informados:

- automóvel: `R$ 4.500`;
- máquina de solda: `R$ 250`;
- maçarico: `R$ 150`;
- ferramentas: `R$ 150`;
- canteiro: `R$ 28.949,708`;
- linha de recalque: `R$ 5.278`.

Linha de recalque:

- tubulação: `300 m × R$ 150 = R$ 45.000`;
- depreciação em 12 meses: `R$ 3.750`;
- juros: `1% = R$ 450`;
- custo mensal tubulação: `R$ 4.200`;
- flutuantes: 37,5 peças, calculadas por `150/12×3`;
- custo: `R$ 7.500`;
- depreciação: `R$ 625`;
- juros: `R$ 75`;
- custo mensal flutuantes: `R$ 700`;
- acoplamentos: `(300/12)+2 = 27 peças`;
- custo: `R$ 4.050`;
- depreciação: `R$ 337,50`;
- juros: `R$ 40,50`;
- custo mensal: `R$ 378`.

Total da seção de apoio: `R$ 39.277,708`.

### V — Administrativas

- viagens de inspeção: `R$ 3.000`;
- comunicações: `R$ 300`;
- demais linhas zeradas/vazias.

Total: `R$ 3.300`.

### Despesas diretas

Total: `R$ 87.367,599759`.

### VI — BDI interno da dragagem

- oficina: `5%`;
- administração: `5%`;
- outros: vazio.

Total: `R$ 8.736,759976`.

### VII — Financeiras

- depreciação do equipamento em 60 meses: `R$ 4.166,666667`;
- juros de capital: `1% = R$ 2.500`;
- atrasos: sem valor.

Total: `R$ 6.666,666667`.

### Resumo

- custo mensal da dragagem: `R$ 102.771,026401`;
- custo mensal da operação de bags + polímero: `R$ 87.529,88985`;
- custo mensal total: `R$ 190.300,916251`;
- prazo adotado: `2 meses`;
- custo total dragagem + operação de bags: `R$ 380.601,832503`.

### Preço por hora

- BDI multiplicador: `1,6`;
- preço de venda mensal: `R$ 304.481,466002`;
- horas trabalhadas/mês: `198`;
- eficiência de operação: `0,6`;
- horas produtivas: `118,8`;
- preço/hora produtiva: `R$ 2.562,975303`;
- hora à disposição: `60%` do preço/hora = `R$ 1.537,785182`.

### Anomalias e dúvidas

- **EVIDÊNCIA CONFIRMADA:** cliente interno `ENFIL` diverge de `Agua de Joinville`.
- **EVIDÊNCIA CONFIRMADA:** a fórmula de combustível multiplica horas por eficiência de 90%, consumo e preço.
- **EVIDÊNCIA CONFIRMADA:** a eficiência usada para preço/hora é 60%, diferente dos 65% da produção e dos 90% do combustível.
- **EVIDÊNCIA CONFIRMADA:** o campo `PREÇO DE VENDA (R$/m³)` está zerado, sem custo unitário preenchido.
- **EVIDÊNCIA CONFIRMADA:** muitas funções estão disponíveis, porém com quantidade zero ou vazia.
- **DÚVIDA:** qual eficiência é operacionalmente correta para cada finalidade?
- **DÚVIDA:** por que as horas remuneradas são 220 enquanto as trabalhadas são 198?
- **DÚVIDA:** o BDI de 10% nesta aba é custo indireto interno, enquanto o BDI comercial de 60% é margem/preço?
- **DÚVIDA:** o item “docagem anual 1,0% a.m.” está conceitualmente correto?
- **DÚVIDA:** confirmar se preço por hora é apenas referência para hora à disposição ou forma alternativa de cobrança.
- **DÚVIDA:** por que prazo e quantidade de dias são fixados em 2 meses/60 dias.

## 6.11. Aba `8. Desmob. Draga`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** calcular desmobilização da draga.

Inclui:

- guindaste;
- carreta;
- mão de obra;
- opções zeradas de outras carretas e trator.

Preço final: `R$ 20.223,674`.

### Anomalia relevante

**EVIDÊNCIA CONFIRMADA:** a planilha de preços não usa este resultado. Ela usa o custo da mobilização (`R$ 34.217,08`) também para desmobilização.

### Dúvida

Confirmar se isso é decisão comercial deliberada ou resíduo de fórmula.

## 6.12. Aba `9. Desmob. Eq. Polimero `

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** calcular desmontagem e desmobilização do sistema de polímero.

Componentes:

- desmontagem de tenda;
- frete;
- itens hidráulicos/elétricos opcionais;
- máquina WAP opcional;
- 3 dias de equipe.

Preço final: `R$ 12.723,674`.

### Anomalia relevante

**EVIDÊNCIA CONFIRMADA:** a planilha de preços não usa este resultado. Ela calcula desmobilização do equipamento de polímero como `70%` do custo de mobilização, resultando em `R$ 29.998,71224`.

### Dúvida

Confirmar qual método representa a proposta efetivamente enviada.

## 6.13. Aba `Batimetria`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** estimar projeto, batimetria e análises.

Composição comercial:

- 2 batimetrias a `R$ 10.000`;
- 30 análises a `R$ 25`;
- 1 projeto a `R$ 20.000`.

Preço final: `R$ 40.750`.

Bloco auxiliar:

- 148 análises de sólidos totais a `R$ 50`;
- 8 análises de densidade a `R$ 200`;
- custo de `R$ 1.500` ao dividir por 6 meses.

### Dúvidas

- o bloco auxiliar não alimenta a composição principal;
- a composição principal usa 30 análises a R$ 25, divergindo do bloco auxiliar;
- quantidade de meses `6` diverge do prazo de 2 meses;
- confirmar frequência de coleta, escopo laboratorial e vínculo entre os dois blocos.

## 6.14. Aba `10. Plan. Preços`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** consolidar custos de pacotes, aplicar BDI de 60% e calcular preços unitários e totais.

### Itens e preços com BDI

1. mobilização da draga: `R$ 54.747,328`;
2. mobilização do polímero/barrilete: `R$ 68.568,48512`;
3. preparo de célula: `R$ 171,024682/m²`, total `R$ 140.625,0448`;
4. fornecimento de bags: `R$ 57.517,0128/un`, total `R$ 230.068,0512`;
5. dragagem e desaguamento: `R$ 781,632309/ton base seca`, total `R$ 608.962,932004`;
7. desmobilização da draga: `R$ 54.747,328`;
8. desmobilização do polímero: `R$ 47.997,939584`;
9. análises + batimetria + projeto: `R$ 65.200`.

Custo total indicado: `R$ 753.573,192943`.

Preço de venda: `R$ 1.270.917,108708`.

### Fórmula complementar

`(preço total da dragagem + preço total dos bags) ÷ base seca = R$ 1.076,935377`.

### Anomalias

- item 6 não existe;
- custo total soma `C4:C10`, portanto exclui Batimetria da soma de custos, apesar de o preço de venda incluir `J11`;
- desmobilização da draga usa custo da mobilização, não a aba própria;
- desmobilização do polímero usa 70% da mobilização, não a aba própria;
- célula usa área de `822,25 m²`;
- bags usam 4 unidades equivalentes;
- há valor isolado de `R$ 497.000` em `J16`, sem rótulo ou dependência;
- descrição dos bags informa que “real será 3 bags com dimensões específicas”, mas a composição usa 4 equivalentes.

### Dúvidas

- o BDI de 60% representa markup comercial total?
- por que o custo de Batimetria é excluído do custo total?
- qual valor foi efetivamente ofertado: R$ 1.270.917,11, R$ 874.392,50 ou R$ 497.000?
- confirmar a lógica deliberada de desmobilização.

## 6.15. Aba `11. Arredondamento`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA:** apresentar uma versão comercial simplificada, com preços arredondados e agrupamento diferente da planilha detalhada.

Título interno: `PLANILHA DE PREÇOS – ETE CANDIDO MOTA`.

Itens:

- mobilização da draga: `R$ 45.000`;
- mobilização do polímero: `R$ 72.000`;
- preparo de célula: `822,25 m² × R$ 130 = R$ 106.892,50`;
- dragagem e desaguamento: `300 toneladas secas × R$ 1.935 = R$ 580.500`;
- desmobilização da draga: `R$ 45.000`;
- desmobilização do polímero: `R$ 25.000`.

Total global: `R$ 874.392,50`.

### Anomalias

- cliente/local do título (`ETE CANDIDO MOTA`) diverge do arquivo e dos dados da obra;
- quantidade comercial da dragagem é `300 t secas`, enquanto a massa calculada é `779,0913`;
- fornecimento dos bags, canteiro, operação do sistema, batimetria e projeto são incorporados/omitidos na descrição agregada;
- apenas a área da célula é referenciada automaticamente; os demais preços e quantidades são manuais;
- total é substancialmente inferior ao preço detalhado de `R$ 1.270.917,11`.

### Dúvidas

- esta aba pertence à proposta de Joinville ou é resíduo de outro orçamento?
- o total de R$ 874.392,50 foi o valor final ofertado?
- por que a quantidade de 300 toneladas secas foi usada?
- quais pacotes estão incluídos no preço unitário de R$ 1.935/t?
- a aba foi usada apenas como referência de arredondamento ou como documento comercial definitivo?

## 7. Entidades conceituais encontradas

### EVIDÊNCIA CONFIRMADA

- orçamento;
- proposta;
- cliente;
- contato;
- obra;
- local;
- objeto;
- material;
- volume in situ;
- sólidos totais in situ;
- sólidos após desaguamento;
- massa/base seca;
- distância de recalque;
- linha flutuante;
- linha de terra;
- jornada;
- calendário;
- produção;
- prazo;
- equipamento de dragagem;
- equipamento de polímero;
- barrilete;
- célula;
- manta PEAD;
- geotêxtil/Bidim;
- brita/camada drenante;
- bag;
- canteiro;
- equipe;
- função;
- salário/valor-hora;
- encargos;
- refeição;
- transporte;
- combustível;
- manutenção;
- equipamento de apoio;
- mobilização;
- desmobilização;
- análise laboratorial;
- batimetria;
- projeto;
- custo;
- custo mensal;
- custo unitário;
- BDI;
- preço de venda;
- hora produtiva;
- hora à disposição;
- cotação/referência de preço.

## 8. Regras de negócio extraídas

### EVIDÊNCIA CONFIRMADA

1. Produção horária = vazão × eficiência × concentração.
2. Produção mensal = produção horária × horas/dia × dias/mês.
3. Prazo calculado = volume ÷ produção mensal.
4. Mão de obra diária = quantidade × valor-hora × horas/dia × (1 + encargos).
5. Refeição e transporte são calculados pelo número total de pessoas.
6. Barrilete é apropriado por 40% do valor integral neste arquivo.
7. Equipamento de polímero é apropriado por 70% do valor de referência neste arquivo.
8. Área da célula gera quantidades físicas por coeficientes unitários.
9. Brita financeira recebe acréscimo de 30% sobre quantidade geométrica.
10. Massa seca = volume in situ × teor de sólidos in situ.
11. Volume desaguado = massa seca ÷ teor de sólidos desaguado.
12. Necessidade equivalente de bags = volume desaguado ÷ capacidade de referência.
13. Consumo de polímero = base seca × 3.
14. Canteiro é convertido de custo total para custo mensal.
15. Dragagem combina custos mensais da draga, canteiro e sistema de desaguamento.
16. BDI comercial detalhado = 60%.
17. Hora produtiva = horas trabalhadas × eficiência.
18. Preço/hora = preço mensal ÷ horas produtivas.
19. Hora à disposição = 60% do preço/hora neste arquivo.
20. A apresentação final pode agrupar e arredondar itens manualmente.

## 9. Valores e coeficientes observados

Todos os valores abaixo são **EVIDÊNCIA PARCIAL**, pois pertencem somente a este orçamento:

- vazão: `120 m³/h`;
- eficiência de produção: `65%`;
- concentração de produção: `18%`;
- sólidos in situ: `19,89%`;
- sólidos desaguados: `48%`;
- jornada: `9 h/dia`;
- calendário: `22 dias/mês`;
- encargos: `120%`;
- consumo de polímero: `3` por unidade de base seca;
- BDI comercial: `60%`;
- eficiência de operação para combustível: `90%`;
- eficiência para preço por hora: `60%`;
- depreciação do barrilete: `40%`;
- apropriação do equipamento de polímero: `70%`;
- depreciação da tubulação/flutuantes/acoplamentos: `12 meses`;
- depreciação da draga: `60 meses`;
- juros de capital: `1%`;
- manutenção: `0,6% + 1,0%` do valor da draga;
- PEAD: `1,196 m²/m²`;
- Bidim: `1,48 m²/m²`;
- brita: `0,17 m³/m²`, acrescida de 30%;
- retroescavadeira e mão de obra: `0,023 h/m²`.

## 10. Terminologia encontrada

- `Bag`: unidade geotêxtil de desaguamento.
- `Base seca` / `ton base seca` / `tonelada 100% seca`: unidade econômica associada ao teor de sólidos.
- `ST in situ`: sólidos totais no material antes do desaguamento.
- `ST Desaguado`: concentração de sólidos após desaguamento.
- `Barrilete`: conjunto de distribuição hidráulica.
- `Seio da linha`: comprimento adicional aplicado à linha de recalque.
- `Célula`: área preparada para instalação e drenagem dos bags.
- `Hora à disposição`: preço reduzido aplicado ao período não produtivo/disponível.
- `VB`: verba/global.
- `No estado`: valor atribuído ao equipamento no estado atual.

## 11. Exceções, inconsistências e resíduos

### EVIDÊNCIA CONFIRMADA

1. Três identidades de cliente/local coexistem:
   - Águas de Joinville;
   - ENFIL;
   - ETE Cândido Mota.
2. O nome do arquivo cita ETA Piraí, mas o texto não aparece explicitamente nas células principais.
3. Prazo calculado: 1,409 mês; prazo usado: 2 meses; alguns itens: 3 meses; Batimetria: 6 meses.
4. Massa seca calculada: 779,0913; apresentação arredondada: 300 toneladas.
5. Desmobilizações próprias não são utilizadas na planilha detalhada.
6. Custo de Batimetria não entra no custo total, mas entra no preço de venda.
7. Aba final arredondada é majoritariamente manual.
8. Existe valor isolado de R$ 497.000 sem contexto.
9. Existe fórmula que pode aparecer como `#NAME?` em ambiente de importação.
10. Existem preços com quantidades vazias, resultando em custo zero.
11. Existem coeficientes e percentuais diferentes para conceitos chamados genericamente de eficiência.
12. O custo unitário em R$/m³ da aba Dragagem não está preenchido.
13. Há comentário vazio em `F7` de uma planilha, sem conteúdo útil.
14. Não foram identificados links externos ou nomes definidos.
15. As fórmulas dependem apenas de células internas do arquivo.

## 12. Conhecimentos específicos deste orçamento

### EVIDÊNCIA PARCIAL

- A obra é tratada como dragagem com desaguamento em bags para lodo de ETA.
- A cobrança detalhada é estruturada principalmente por tonelada de base seca.
- O preparo de célula é medido por m².
- Mobilizações e desmobilizações são itens globais.
- O fornecimento de bags é tratado como item unitário.
- Projeto, batimetria e análises são agrupados.
- O sistema de polímero e o canteiro são incorporados ao custo da dragagem.
- A apresentação comercial pode reduzir o número de itens e adotar valores arredondados manualmente.

## 13. Dúvidas para validação do especialista

1. O cliente correto é Águas de Joinville? ENFIL atuava como cliente, integradora ou apenas era resíduo?
2. A obra é efetivamente ETA Piraí?
3. O título ETE Cândido Mota é resíduo de outro orçamento?
4. Qual foi o valor efetivamente apresentado ao cliente?
5. Qual quantidade comercial correta: 779,0913 ou 300 toneladas secas?
6. Como foi definida a área de célula de 822,25 m²?
7. Quais dimensões reais de bags seriam usadas?
8. Qual capacidade efetiva por bag deve ser adotada?
9. Qual a origem dos fatores geométricos 2,4, 2,2 e 0,85?
10. O teor de 19,89% veio de análise laboratorial?
11. O teor de 48% é meta, experiência ou dado do fornecedor?
12. O consumo de polímero de 3 kg/t seca foi ensaiado?
13. Por que o prazo operacional foi arredondado para 2 meses?
14. Canteiro deve durar 3 meses?
15. Por que a batimetria menciona 6 meses?
16. Qual desmobilização deve ser usada: aba própria ou percentual/repetição da mobilização?
17. O BDI de 60% já engloba os 10% internos da aba Dragagem?
18. O valor de R$ 497.000 tem função comercial?
19. Água e energia são fornecidas pelo cliente?
20. Frete e munck dos bags estão incluídos em outro item?
21. Qual o significado econômico da apropriação de 40% do barrilete e 70% do sistema de polímero?
22. A fórmula de combustível deve usar 90% de eficiência?
23. Qual eficiência deve ser usada para produção, custo e hora produtiva?
24. A unidade de `base seca` é tonelada?
25. Qual proposta/código definitivo deveria constar no arquivo?

## 14. Limitações registradas

- O arquivo foi analisado estruturalmente por leitura do workbook, células, fórmulas, valores armazenados e metadados.
- A análise não validou as premissas com o especialista.
- Valores de mercado e cotações não foram verificados externamente.
- Não foi executada comparação com outros orçamentos para promover padrões gerais.
- O cálculo exibido pelo Excel pode depender da versão do aplicativo; a fórmula `ROUNDUP` apareceu como `#NAME?` em uma leitura importada, embora sua expressão esteja presente no XML.
- Não foram alteradas fórmulas, valores ou estrutura do Excel.
- Nenhum documento de outro orçamento foi modificado.
- Nenhum índice geral ou documento de consolidação foi atualizado.

## 15. Validação final

- [x] Todas as 15 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Fórmulas e dependências relevantes registradas.
- [x] Entidades, regras, padrões, exceções e terminologias preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Dúvidas explicitadas.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma consolidação realizada.
- [x] Nenhuma funcionalidade criada.
