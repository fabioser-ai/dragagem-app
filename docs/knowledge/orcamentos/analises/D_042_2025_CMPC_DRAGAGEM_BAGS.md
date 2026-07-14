# D_042_2025 - CMPC - Dragagem - Bags.xlsx — Registro independente de descoberta

## Status

- **Data da análise:** 14/07/2026.
- **Status:** engenharia reversa vertical concluída no escopo documental.
- **Arquivo original:** `D_042_2025 - CMPC - Dragagem - Bags.xlsx`.
- **Identificador visível na pasta de trabalho:** `042_2025`.
- **Proposta registrada internamente:** `Proposta D_023_2025`.
- **Data registrada no arquivo:** 17/04/2025.
- **Revisão:** o campo `REVISÃO ATUAL` existe, sem número ou descrição visível.
- **Quantidade de abas:** 12.
- **Todas as abas foram analisadas.**
- Nenhuma funcionalidade, arquitetura, banco de dados, tela, consolidação entre orçamentos ou decisão de implementação foi criada.
- Este documento descreve exclusivamente este Excel.

## Limitações registradas

### EVIDÊNCIA CONFIRMADA

- O arquivo foi lido por ferramenta de análise de planilhas com acesso a valores e fórmulas.
- A ferramenta avaliou algumas referências válidas entre abas como `#NAME?`, embora outras células dependentes contenham valores numéricos coerentes com o resultado esperado. Essas ocorrências foram registradas como **anomalia observada ou limitação de avaliação**, sem concluir automaticamente que o Excel original apresenta o mesmo erro ao ser aberto no Microsoft Excel.
- Não foi feita alteração nem recálculo persistente no arquivo original.
- Não foi realizada comparação decisória com outros orçamentos.

## Classificação das evidências

| Categoria deste documento | Significado |
|---|---|
| **EVIDÊNCIA CONFIRMADA** | Informação diretamente observada no arquivo. |
| **EVIDÊNCIA PARCIAL** | Interpretação ou possível regra observada somente neste orçamento. |
| **DÚVIDA** | Informação sem comprovação suficiente. |

Todas as descobertas reutilizáveis possuem confiança **Nível C**, por terem sido observadas nesta única fonte.

# 1. Classificação aparente do orçamento

## EVIDÊNCIA CONFIRMADA

O arquivo representa orçamento para:

- cliente `CMPC IGUAÇU - A1 ENGENHARIA`;
- contato `Marcio Domingues`;
- objeto `DRAGAGEM DA LAGOA 01`;
- local `PIRAÍ DO SUL PR`;
- material descrito como `Efluente industríal`;
- volume de dragagem de 10.000 m³;
- bota-fora por `Bags`;
- sistema de medição por `preços unitários de serviços`;
- linha de recalque total de 900 m, composta por 100 m de linha flutuante e 800 m de linha de terra;
- mobilização, canteiro, preparo de células, fornecimento/operação de bags, dragagem elétrica, operação de sistema de polímero e desmobilizações;
- formação de preço final por itens, com BDI comercial distinto por item.

## EVIDÊNCIA PARCIAL

A classificação aparente é:

**dragagem de efluente industrial/lodo de lagoa, com desaguamento e acondicionamento em geobags, operação de planta de polímero e retorno de percolado.**

Características que diferenciam este orçamento, observadas somente nesta fonte:

- draga elétrica;
- linha de recalque extensa, de 900 m;
- duas células de desaguamento;
- conjunto heterogêneo de bags, com dimensões e níveis diferentes;
- polímero indicado como repassado ao cliente CMPC;
- sistema de preparo de polímero orçado com base em cotações e estimativas históricas;
- prazo físico total de 6 meses, embora a operação calculada seja 4 meses;
- BDI comercial de 45% para bags e 50% para os demais itens consolidados.

# 2. Identidade e inconsistências de identificação

## EVIDÊNCIA CONFIRMADA

- Nome do arquivo: `D_042_2025 - CMPC - Dragagem - Bags.xlsx`.
- Código na célula `Dados Obra!A1`: `042_2025`.
- Proposta na célula `Dados Obra!B5`: `Proposta D_023_2025`.
- Data da proposta: 17/04/2025.
- Data na composição de dragagem: 22/04/2025.
- Cliente: `CMPC IGUAÇU - A1 ENGENHARIA`.
- Referência na aba de dragagem: `CMPC - Dragagem lagoa 1`.

## DÚVIDA

- O código correto da proposta é `D_042_2025` ou `D_023_2025`?
- A diferença decorre de reutilização de modelo, revisão comercial ou renumeração?
- A data de 22/04/2025 na aba de dragagem representa data-base da composição ou revisão posterior?

# 3. Inventário das abas

| Ordem | Aba | Papel observado |
|---:|---|---|
| 1 | `Dados Obra` | Identificação, premissas físicas, responsabilidades e jornada. |
| 2 | `Produção` | Produção horária/mensal e prazos de execução. |
| 3 | `3. Canteiro` | Custo do canteiro durante o prazo total. |
| 4 | `4. Mob Draga + Pol.` | Mobilização conjunta da draga e planta de polímero. |
| 5 | `Barrilete` | Composição física e depreciação do barrilete. |
| 6 | `6. Prep Célula` | Dimensionamento e custo de preparo das células. |
| 7 | `7.1. Bags` | Seleção, capacidade, fornecimento e espalhamento dos bags. |
| 8 | `7.2 Draga` | Composição mensal detalhada da dragagem elétrica. |
| 9 | `7.3 Op.Planta` | Custo de operação do sistema de polímero. |
| 10 | `9. DesMob Draga + Pol.` | Desmobilização da draga e planta de polímero. |
| 11 | `15. Desmob Final` | Desmobilização final do canteiro/equipe. |
| 12 | `Plan. Final` | Consolidação dos custos e preços de venda. |

# 4. Fluxo completo observado

```text
Dados da obra
    ↓
Produção horária e mensal
    ↓
Prazo de operação arredondado + cronograma físico total
    ↓
Canteiro pelo prazo total
    ↓
Mobilização da draga e planta de polímero
    ↘ Barrilete depreciado
    ↓
Preparo das células
    ↓
Fornecimento e operação dos bags
    ↓
Dragagem elétrica
    ↓
Operação do sistema de polímero
    ↓
Desmobilização da draga/planta
    ↓
Desmobilização final
    ↓
Planilha detalhada de custos e venda
```

## EVIDÊNCIA PARCIAL

O fluxo mistura quatro naturezas de cálculo:

1. premissas físicas e operacionais;
2. dimensionamentos de produção, prazo, célula e bags;
3. composições de custo por evento, mês, dia, área ou volume;
4. consolidação comercial com BDI.

# 5. Análise por aba

## 5.1 Aba `Dados Obra`

### Objetivo e papel

Registrar identidade comercial, premissas físicas, forma de disposição, responsabilidades e calendário.

### Entradas — EVIDÊNCIA CONFIRMADA

- proposta: `Proposta D_023_2025`;
- data: 17/04/2025;
- cliente: `CMPC IGUAÇU - A1 ENGENHARIA`;
- contato: `Marcio Domingues`;
- e-mail: não preenchido;
- objeto: `DRAGAGEM DA LAGOA 01`;
- local: `PIRAÍ DO SUL PR`;
- volume contratual: 10.000 m³;
- justificativa textual: `4400 x 2 metros = 8800 + 10% = 9680 (arredondado para 10k)`;
- material: `Efluente industríal`;
- recalque: 900 m;
- linha flutuante: 100 m;
- linha de terra: 800 m;
- profundidade, espessura média e área: não preenchidas;
- bota-fora: `Bags`;
- medição: `preços unitários de serviços`;
- canteiro: responsabilidade FOS;
- mobilização: responsabilidade FOS;
- jornada: 9 h/dia;
- calendário: 22 dias/mês.

### Quadro lateral — EVIDÊNCIA CONFIRMADA

- Lagoa 1 — lodo: 10.000 m³;
- Lagoa 1 — água: 15.600 m³;
- total: 25.600 m³;
- linha de recalque indicada: 300 m;
- retorno do percolado para lagoa 2: 600 m;
- soma lateral: 900 m.

### Regras e fórmulas

- recalque total = linha flutuante + linha de terra;
- distância total de recalque = distância base + seio;
- linha flutuante total = linha base + seio;
- volume geométrico potencial = dimensões × espessura.

### Saídas

- volume adotado: 10.000 m³;
- recalque total: 900 m;
- linha flutuante total: 100 m;
- volume geométrico calculado: 0 m³ por ausência de dimensões.

### Entidades

Proposta, cliente, contato, obra, lagoa, material, volume de lodo, volume de água, linha de recalque, linha de retorno de percolado, linha flutuante, linha de terra, bota-fora, medição, responsabilidade e jornada.

### EVIDÊNCIA PARCIAL

- O volume comercial foi arredondado para cima depois de adicionar 10% ao valor geométrico informado em texto.
- O recalque de 900 m parece combinar 300 m de linha de processo e 600 m de retorno de percolado.
- O volume de água é registrado para contexto operacional, mas não alimenta diretamente o preço final observado.

### Dúvidas

- O retorno do percolado deve ser considerado parte da linha de recalque da dragagem?
- A margem de 10% é contingência, incerteza de levantamento ou regra comercial?
- Por que profundidade, espessura e área estruturadas estão vazias enquanto o cálculo textual usa `4400 x 2`?

## 5.2 Aba `Produção`

### Objetivo

Calcular produção útil e prazo.

### Entradas — EVIDÊNCIA CONFIRMADA

- vazão: 150 m³/h;
- eficiência: 50%;
- concentração: 20%;
- 9 h/dia;
- 22 dias/mês;
- volume: 10.000 m³.

### Fórmulas operacionais

```text
horas mensais = 9 × 22 = 198 h/mês
produção útil = 150 × 50% × 20% = 15 m³/h
produção mensal = 15 × 198 = 2.970 m³/mês
prazo matemático = 10.000 ÷ 2.970 = 3,3670 meses
prazo operacional = arredondamento para cima = 4 meses
```

### Cronograma físico

- canteiro: 0,5 mês;
- mobilização: 0,5 mês;
- preparo de célula: 0,5 mês;
- dragagem/bags: 4 meses;
- desmobilização da draga: 0,25 mês;
- desmobilização final: 0,25 mês;
- total: 6 meses.

### EVIDÊNCIA PARCIAL

- O cronograma soma etapas sequencialmente, sem sobreposição.
- O prazo comercial do canteiro usa 6 meses; a operação principal usa 4 meses.
- “Mobilizações = 2” aparece sem ligação clara com o cronograma detalhado.

### Dúvidas

- As fases realmente não se sobrepõem?
- O preparo da célula ocorre integralmente antes da dragagem?
- A eficiência de 50% já considera paradas, troca de bags e operação da planta?

## 5.3 Aba `3. Canteiro`

### Objetivo

Compor o custo do canteiro por todo o prazo físico e convertê-lo em custo mensal.

### Equipe diária

- 1 engenheiro a 50% de atuação;
- 1 auxiliar técnico;
- 1 encarregado;
- 1 operador de draga;
- 1 operador de polímero;
- 4 ajudantes;
- 9 refeições;
- 9 transportes;
- leis sociais: 110%;
- custo diário: R$ 4.115,53096875.

### Formação dos valores-hora

A planilha contém quadro auxiliar de salários mensais, divisor de 220 h, dissídio de 7,5% e adicional de transferência de 25% em algumas funções.

Exemplos:

- engenheiro: R$ 9.500/mês → R$ 43,1818/h + 7,5% = R$ 46,42045/h, sem transferência; atuação 50%;
- auxiliar técnico: R$ 5.000/mês → dissídio + transferência = R$ 30,53977/h;
- encarregado: salário de R$ 11.132/mês, mas valor-hora base usado no quadro é R$ 28/h, resultando R$ 37,625/h;
- operador de draga: R$ 33,59375/h;
- operador de polímero: R$ 23,8246875/h;
- ajudante: R$ 11,2875/h.

### Itens de custo

- 3 containers por 6 meses;
- frete de containers;
- PGR, PCMSO, LTCAT e PR;
- ART principal e corresponsabilidades;
- placa de obra;
- tendas de canteiro;
- água potável;
- material de escritório;
- banheiro químico;
- viagem da equipe;
- exames médicos;
- máscaras de fuga;
- mão de obra de viagem, registro e integração.

### Resultados

- total: R$ 105.007,65484375;
- prazo: 6 meses;
- custo unitário mensal: R$ 17.501,275807291666;
- BDI interno: 0%.

### Referências e observações

- tenda 8 × 8 m com logo e três fechamentos: `Locup Tendas`, registro `zap em 28/11/24`;
- frete da tenda: R$ 1.200, marcado como `chute`.

### Anomalias / DÚVIDAS

- A ferramenta avaliou `D18 = Produção!H39` como `#NAME?`, embora o valor utilizado na linha e nas células seguintes seja 6 meses.
- O item 8 está vazio, mas preserva preço unitário R$ 150 e quantidade zero.
- O preço de encarregado no quadro lateral não deriva do salário mensal mostrado por divisão simples por 220.

## 5.4 Aba `4. Mob Draga + Pol.`

### Objetivo

Compor a mobilização conjunta da draga e da planta de polímero.

### Equipe

Mesma equipe-base do canteiro, com custo diário de R$ 4.115,53096875.

### Itens

- locação de máquina de solda PEAD;
- guindaste para carregamento;
- treinamentos de altura e espaço confinado;
- mobiliário de canteiro;
- mobiliário do alojamento;
- 3 carretas carga seca para draga e tubos;
- 1 carreta para equipamento de polímero;
- 2 dias de guindaste para descarregamento/montagem;
- instalações hidráulicas;
- instalações elétricas;
- máquina WAP;
- barrilete depreciado;
- viagem de ida;
- 7 dias de mão de obra.

### Resultado

- total: R$ 155.266,487978125;
- BDI interno: 0%;
- preço final: R$ 155.266,487978125.

### Quadro de mobiliário

Total de R$ 17.000, composto por:

- 3 mesas: R$ 3.000;
- 4 cadeiras: R$ 2.000;
- 2 armários de escritório: R$ 3.000;
- 1 cesto de lixo: R$ 500;
- 4 armários de vestiário: R$ 6.000;
- 1 bebedouro: R$ 2.500.

### Cotações e referências

- carretas: observação `Fabiano R$ 8.800,00 + 0,2%`, enquanto preço usado é R$ 10.000;
- carreta do polímero: `Zap de 22/04/25`;
- treinamentos: `Preços VALE Vitória`.

### EVIDÊNCIA PARCIAL

- O barrilete entra na mobilização por apenas 30% do custo de aquisição, tratado como depreciação.
- A mão de obra de viagem usa o mesmo custo diário da equipe completa.

## 5.5 Aba `Barrilete`

### Objetivo

Compor o conjunto de tubulações, válvulas e acessórios do barrilete e apropriar 30% do custo.

### Equipe de montagem

- 1 encarregado;
- 1 operador de draga + técnico de operação de polímero;
- 4 ajudantes;
- 5 refeições;
- 5 transportes;
- custo por dia: R$ 2.264,73409375.

### Materiais e serviços

- 6 tubos de ferro de 6 m, diâmetro 8";
- 8 tocos de 0,50 m;
- 8 joelhos de 90°;
- 6 tees flangeados;
- 6 ponteiras flange/escama;
- cap;
- válvulas gaveta de 4" e 3";
- 200 m de mangueira;
- braçadeiras;
- curvas longas PVC;
- válvulas esfera;
- bomba lameira;
- mão de obra de montagem.

### Resultados

- custo total de aquisição/montagem: R$ 30.474,13409375;
- apropriação de 30%: R$ 9.142,240228125;
- este valor alimenta a mobilização.

### EVIDÊNCIA PARCIAL

A planilha chama o fator de 30% de “depreciação”, mas não registra vida útil, número de obras ou critério temporal.

### DÚVIDA

- Os 30% representam desgaste esperado nesta obra, rateio por reutilização ou contingência?

## 5.6 Aba `6. Prep Célula`

### Objetivo

Dimensionar e precificar a preparação de duas células de desaguamento.

### Células

- Célula 1: 35 × 60 m = 2.100 m²;
- Célula 2: 30 × 50 m = 1.500 m²;
- área total: 3.600 m².

### Coeficientes físicos

- manta PEAD: 1,196 m² por m² de célula → 4.305,6 m²;
- Bidim: 1,48 m² por m² → 5.328 m²;
- brita: 0,15 m³ por m² → 540 m³ no quadro auxiliar;
- retroescavadeira: 0,023 h por m² → 82,8 h;
- mão de obra: 0,023 h por m² → 82,8 h;
- prazo auxiliar: 10,35 dias.

### Itens de custo

- preparo de terreno;
- mobilização de patrol;
- aluguel e mobilização/desmobilização de retro;
- regularização manual;
- fornecimento e instalação de PEAD;
- mobilização da equipe de PEAD;
- Bidim;
- brita;
- retroescavadeira para espalhamento;
- mão de obra de instalação de Bidim e brita.

### Resultado

- custo total: R$ 288.085,571625;
- preço unitário interno não calculado porque `Prazo de Operação` está vazio;
- na planilha final, o custo é dividido diretamente pelos 3.600 m², resultando R$ 80,0237698958/m².

### Anomalias e exceções

- o quadro auxiliar calcula 540 m³ de brita, mas a composição usa 594 m³, exatamente 10% a mais;
- a observação do PEAD diz `chute pra cima`;
- linhas 11 a 14 da composição permanecem vazias com preços zero;
- `F36:F38` apresentam divisão por zero porque `F35` está vazio.

### EVIDÊNCIA PARCIAL

- A brita parece receber margem de 10%, mas essa margem não é explicitada por fórmula.
- Os coeficientes são usados para dimensionamento preliminar, mas alguns valores da composição podem ser ajustados manualmente.

## 5.7 Aba `7.1. Bags`

### Objetivo

Selecionar bags, verificar capacidade das células e compor o custo de fornecimento/espalhamento.

### Base física

- volume a dragar: 10.000 m³;
- sólidos totais in situ: 10%;
- volume seco: 1.000 m³;
- sólidos totais desaguados: 20%;
- volume desaguado: 5.000 m³;
- observação: média obtida na obra foi 25%.

### Relação física

```text
volume seco = volume a dragar × % ST in situ
volume desaguado = volume seco ÷ % ST desaguado
```

### Bags selecionados

Composição de compra:

- 2 P13 × 20;
- 2 P13 × 25;
- 1 P18 × 20;
- 1 P18 × 25;
- 2 P20 × 20;
- 3 P20 × 25;
- mais 1 P13 × 25;
- 1 P18 × 40;
- 1 P18 × 45.

### Capacidade

- Célula 1: 3.585,5 m³;
- Célula 2: 1.579 m³;
- total: 5.164,5 m³;
- necessidade estimada: 5.000 m³;
- folga aparente: 164,5 m³, aproximadamente 3,29%.

### Formação de preço dos bags

A tabela lateral usa:

```text
preço do bag = perímetro × comprimento × R$ 60/m²
```

Há nota: `Preços praticados em 2025 nas obras Chapecó e Curitiba R$ 55,00/m²`, mas a composição usa R$ 60/m².

### Resultados

- custo de bags: R$ 375.960;
- mão de obra de espalhamento: 5 dias × R$ 4.115,53096875;
- total: R$ 396.537,65484375;
- prazo preenchido: 1;
- preço interno: R$ 396.537,65484375;
- BDI interno: 0%.

### EVIDÊNCIA PARCIAL

- A capacidade nominal dos bags é calculada por área de seção a 2,30 m × comprimento.
- As células combinam bags em primeiro e segundo nível.
- A seleção mantém pequena margem sobre o volume desaguado.
- O preço por m² foi elevado de uma referência de R$ 55 para R$ 60 sem fórmula explicativa.

### Dúvidas

- A capacidade geométrica considera redução por enchimento real, recalque ou sobreposição?
- A observação de 25% de ST deveria reduzir a quantidade de bags?
- Por que há duas linhas P13 × 25 na composição principal?

## 5.8 Aba `7.2 Draga`

### Objetivo

Compor o custo mensal da dragagem elétrica por operação, pessoal, manutenção, apoio, administração, BDI e financeiras.

### Identificação

- referência: `CMPC - Dragagem lagoa 1`;
- data: 22/04/2025;
- cliente: CMPC;
- equipamento: draga elétrica;
- valor do equipamento “no estado”: R$ 200.000.

### I — Operação

Entradas:

- 198 h/mês;
- eficiência: 90%;
- consumo: 9 por hora;
- valor energético/combustível: R$ 1;
- fator adicional visível: 7.

Custos:

- consumo: R$ 1.603,80;
- filtros/lubrificantes: R$ 1.122,66;
- fretes/carretos: R$ 1.000;
- segurança/uniformes: R$ 500;
- total: R$ 4.226,46.

### II — Pessoal

Cálculo de horas remuneradas:

- 2 h extras/dia a 70% × 22 dias = 44 h;
- 0 h extras a 100%;
- horas normais: 7,33333 × 30 = 219,9999 h;
- horas equivalentes remuneradas: 294,7999 h/mês.

Equipe efetivamente quantificada:

- 1 encarregado;
- 1 operador de draga;
- 1 ajudante.

Engenheiro, auxiliar técnico e operador de polímero aparecem com quantidade vazia e custo zero.

Resultados:

- salários: R$ 24.322,834249375;
- encargos sociais de 110%: R$ 26.755,117674312492;
- cantina: R$ 5.490;
- alojamento: R$ 2.300;
- viagens nas folgas: R$ 1.500;
- total de pessoal: R$ 60.367,95192368749.

### III — Manutenção

- peças e acessórios: 0,6% ao mês sobre R$ 200.000 = R$ 1.200;
- docagem: 1,0% ao mês = R$ 2.000;
- limpeza e pintura: R$ 500;
- terceiros: R$ 500;
- total: R$ 4.200.

### IV — Equipamentos de apoio

Itens visíveis:

- linha de recalque: R$ 11.265,333333333332;
- bomba de percolado: R$ 500;
- automóvel: R$ 5.000;
- cabo elétrico: R$ 3.000;
- subtotal: R$ 19.765,333333333332.

Composição da linha de recalque:

- tubulação: 900 m × R$ 120 = R$ 108.000, depreciados em 12 meses, mais 1% de juros → R$ 10.080/mês;
- flutuantes: 25 × R$ 200 = R$ 5.000, depreciados em 12 meses + juros → R$ 466,6667/mês;
- acoplamentos: 77 × R$ 100 = R$ 7.700, depreciados em 12 meses + juros → R$ 718,6667/mês;
- total mensal: R$ 11.265,3333.

### V — Administrativas

- viagens de inspeção: R$ 1.000;
- comunicações: R$ 300;
- total: R$ 1.300.

### Despesas diretas e BDI interno

- despesas diretas: R$ 89.859,74525702083;
- oficina 5%: R$ 4.492,987262851041;
- administração 5%: R$ 4.492,987262851041;
- outros: 0%;
- total BDI interno: R$ 8.985,974525702082.

### VII — Financeiras

- depreciação em 60 meses: R$ 3.333,3333333333335;
- juros de capital de 1%: R$ 2.000;
- atrasos 0,5%: estruturado, sem valor;
- total: R$ 5.333,333333333334.

### Resultado mensal e total

- custo mensal total: R$ 104.179,05311605624;
- produção prevista: 5.702,4 m³/mês;
- hora à disposição: R$ 489,32585554511263;
- custo total para 4 meses: R$ 416.716,21246422495.

Quadro alternativo de preço horário:

- BDI/fator: 1,5;
- preço de venda mensal: R$ 156.268,57967408435;
- 198 h/mês;
- eficiência de operação: 60%;
- horas produtivas: 118,8;
- preço por hora produtiva: R$ 1.315,39208479869;
- valor auxiliar com fator 0,6: R$ 473,5411505275283.

### Anomalias e divergências internas

- A aba `Produção` calcula 2.970 m³/mês com eficiência de 50% e concentração de 20%; esta aba calcula produção prevista de 5.702,4 m³/mês com lógica própria.
- O custo unitário e preço de venda por m³ no resumo principal estão vazios/zero.
- `D201` foi avaliada como `#NAME?` pela ferramenta ao referenciar `Produção!H35`, mas `D202` contém o custo total de quatro meses.
- O texto “combustível” permanece em composição de draga elétrica.
- O custo de filtros é descrito como 10% do combustível, porém R$ 1.122,66 corresponde a 70% de R$ 1.603,80, não 10%.
- O quadro de linha de recalque usa 900 m integralmente como tubulação a R$ 120/m, além de 25 peças flutuantes, sem explicar a relação com os 100 m flutuantes.

### Dúvidas

- Qual produção deve governar o prazo e o custo unitário: 2.970 ou 5.702,4 m³/mês?
- O item energético deveria ser eletricidade, diesel do gerador ou custo equivalente?
- O fator 7 na operação representa dias, potência, tarifa ou outro parâmetro?
- Por que somente três funções têm quantidade na equipe mensal?
- A hora à disposição de R$ 489,33 e a hora produtiva de R$ 1.315,39 são modalidades comerciais alternativas?

## 5.9 Aba `7.3 Op.Planta`

### Objetivo

Compor o custo da operação do sistema de preparo/dosagem de polímero.

### Equipe diária efetiva

- 1 operador de polímero;
- 3 ajudantes;
- 4 refeições;
- 4 transportes;
- custo diário: R$ 1.290,28784375.

As demais funções permanecem listadas com quantidade vazia e custo zero.

### Equipamento de polímero

Referências:

- UAP 10 m³ + bombas 10 m³/h: R$ 257.000, Gratt, 07/01/2022;
- UAP 20 m³ + bombas 20 m³/h: R$ 323.000, Gratt, 07/01/2022;
- tanques 5 m³ + bombas 10 m³/h: valor zero, `chute`;
- tanques 10 m³ + bombas 20 m³/h: R$ 334.100, valor orçado com 30% adicional, estimativa 2023.

### Itens

- depreciação do equipamento;
- manutenção de 10% da depreciação;
- polímero calculado sobre base seca;
- fretes de polímero;
- água por caminhão-pipa;
- energia/gerador e diesel;
- instalações hidráulicas;
- máquina WAP;
- mão de obra de operação.

### Polímero

- sólidos secos: 1.000 t secas;
- consumo: 5 kg/t seca;
- quantidade: 5.000 kg;
- preço do polímero: vazio/zero;
- observação: `Repassado para CMPC`.

### Resultado

- depreciação: R$ 55.683,333333333336 para 4 meses;
- manutenção: R$ 5.568,333333333334;
- fretes: R$ 4.500;
- instalações: R$ 2.000;
- mão de obra: 88 dias × R$ 1.290,28784375 = R$ 113.545,33025;
- total: R$ 181.296,99691666669.

### Anomalias

- `D18` foi avaliada como `#NAME?` ao referenciar o prazo de operação.
- `Prazo de Operação` em `F28` está vazio; por isso `F29:F31` apresentam divisão por zero.
- Água, energia e WAP têm preço unitário informado, mas quantidade vazia e custo zero.
- O título da aba/cabeçalho aparece como `PREPARO DE CÉLULA`, embora o conteúdo seja operação da planta.

### EVIDÊNCIA PARCIAL

O cliente assume o custo do polímero, mas a FOS assume operação, depreciação, manutenção e logística associada.

## 5.10 Aba `9. DesMob Draga + Pol.`

### Objetivo

Compor a desmobilização da draga e da planta de polímero.

### Equipe e itens

- equipe-base de 9 pessoas;
- custo diário: R$ 4.115,53096875;
- 3 carretas para draga/tubos;
- 1 carreta para equipamento de polímero;
- 2 dias de guindaste;
- 9 viagens de volta a R$ 700;
- 5 dias de mão de obra.

Itens de mobilização permanecem listados, mas vários têm quantidade vazia e custo zero.

### Resultado

- total: R$ 86.877,65484375;
- BDI interno: 0%;
- preço final: R$ 86.877,65484375.

### Referências

- carretas: `Fabiano R$ 8.800,00 + 0,2%`;
- equipamento de polímero: `Zap de 11/07/25`.

### EVIDÊNCIA PARCIAL

A desmobilização reutiliza a estrutura da mobilização, zerando itens que não se repetem.

## 5.11 Aba `15. Desmob Final`

### Objetivo

Compor retirada de containers, viagem, exames e mão de obra de limpeza final.

### Particularidade da equipe

O encarregado usa R$ 67,99375/h, diferente de R$ 37,625/h nas demais abas. O quadro lateral mostra:

- salário mensal R$ 11.132;
- R$ 50,60/h;
- dissídio 7,5%;
- transferência 25%;
- total R$ 67,99375/h.

Custo diário da equipe: R$ 4.689,50034375.

### Itens efetivos

- frete de 3 containers: R$ 6.000;
- viagem da equipe: R$ 4.500;
- exames médicos: R$ 4.500;
- 5 dias de mão de obra de viagem e limpeza final: R$ 23.447,50171875.

### Resultado

- total: R$ 38.447,50171875;
- prazo de operação: 0;
- preço unitário e preço final: divisão por zero.

### Anomalias

- diversos itens herdados do canteiro permanecem com preço unitário, mas quantidade vazia e custo zero;
- o prazo é explicitamente zero, gerando `#DIV/0!`;
- o encarregado recebe adicional de transferência nesta aba, mas não no canteiro/mobilização.

### Dúvida

- A diferença salarial do encarregado é deliberada para a equipe de desmobilização ou resíduo de outra composição?

## 5.12 Aba `Plan. Final`

### Objetivo

Consolidar custos e aplicar BDI comercial.

### Itens e preços

| Item | Descrição | Custo | Quantidade | Unidade | BDI | Preço total |
|---|---|---:|---:|---|---:|---:|
| 3 | Canteiro | R$ 105.007,65 | 6 | mês | 50% | R$ 157.511,48 |
| 4 | Mobilização | R$ 155.266,49 | 1 | vb | 50% | R$ 232.899,73 |
| 6 | Preparo de célula | R$ 288.085,57 | 3.600 | m² | 50% | R$ 432.128,36 |
| 7.1 | Bags | R$ 396.537,65 | 10.000 | m³ | 45% | R$ 574.979,60 |
| 7.2 | Dragagem | R$ 416.716,21 | 10.000 | m³ | 50% | R$ 625.074,32 |
| 7.3 | Operação da planta | R$ 181.297,00 | 10.000 | m³ | 50% | R$ 271.945,50 |
| 9 | Desmobilização draga/planta | R$ 86.877,65 | 1 | vb | 50% | R$ 130.316,48 |
| 15 | Desmobilização final | R$ 38.447,50 | 1 | vb | 50% | R$ 57.671,25 |

### Consolidação observada

- soma dos preços de venda: R$ 2.482.526,7201088374;
- valor auxiliar em `C17`: R$ 2.444.079,218390087;
- valor auxiliar em `C20`: R$ 24.825,267201088373.

### Anomalias críticas

- a linha `Custo Total` em `C15` referencia somente o custo da desmobilização final, R$ 38.447,50, e não a soma dos custos;
- `E5` foi avaliada como `#NAME?`, embora o cálculo de custo unitário use 6 meses;
- `C17` é igual ao preço total de venda menos o custo da desmobilização final, sugerindo fórmula de soma incompleta ou faixa deslocada;
- `C20` corresponde exatamente a 1% do preço de venda total;
- a coluna `L — UNITÁRIO` contém valores apenas para itens globais e um valor de R$ 147,1999413594775 na linha de bags, que não corresponde ao preço unitário de bags de R$ 57,49796/m³ isoladamente.

### DÚVIDAS

- Qual é o significado de `C17` e `C20`?
- O valor em `L9` soma mais de um componente por m³?
- O “Custo Total” deveria ser a soma dos custos C5:C13?
- Há impostos, comissão ou margem adicionais não rotulados na área inferior?

# 6. Entidades conceituais encontradas

## EVIDÊNCIA CONFIRMADA

- proposta e revisão;
- cliente, contato e local;
- obra, lagoa e objeto;
- material/efluente;
- volume in situ, volume de água, volume seco e volume desaguado;
- linha de recalque, linha flutuante, linha terrestre e retorno de percolado;
- draga elétrica;
- planta/UAP de polímero;
- polímero;
- barrilete;
- célula de desaguamento;
- PEAD, Bidim e brita;
- geobag por modelo/dimensão;
- capacidade por bag, nível e célula;
- equipe, função, salário, hora, encargos, dissídio e transferência;
- mobilização, canteiro, operação e desmobilização;
- custo diário, mensal, global, por área e por volume;
- depreciação, manutenção, juros, BDI interno e BDI comercial;
- cotação, fornecedor, data-base e estimativa.

# 7. Regras de negócio observadas

## EVIDÊNCIA CONFIRMADA

1. Produção útil é calculada multiplicando vazão, eficiência e concentração.
2. Prazo operacional é arredondado para cima.
3. O cronograma físico inclui períodos adicionais antes e depois da operação.
4. Mão de obra diária usa quantidade × valor-hora × horas × (1 + encargos).
5. Salários podem receber dissídio de 7,5% e transferência de 25%.
6. Engenheiro pode ser apropriado parcialmente.
7. Canteiro é rateado pelo prazo total.
8. Barrilete é apropriado por 30% do custo total.
9. Células são dimensionadas por área e coeficientes de materiais.
10. Volume desaguado deriva de sólidos secos e teor final.
11. Bags são precificados por perímetro × comprimento × preço por m².
12. Capacidade total de bags deve cobrir o volume desaguado.
13. Draga é composta mensalmente por centros de custo.
14. Linha de recalque é depreciada e recebe juros.
15. Equipamento de polímero é depreciado em 24 meses.
16. Polímero pode ser repassado ao cliente.
17. BDI interno das composições é diferente do BDI comercial final.
18. O preço final usa BDI por item, não um único BDI geral.

## EVIDÊNCIA PARCIAL

- Margens físicas e comerciais são aplicadas em pontos distintos: arredondamento do volume, 10% aparente de brita, folga de bags, majoração de R$ 55 para R$ 60/m² e BDI.
- O orçamento preserva valores de mercado e cotações dentro das próprias abas, ao lado do valor efetivamente adotado.
- Algumas composições são modelos reutilizados com itens zerados em vez de removidos.

# 8. Dependências entre abas

## EVIDÊNCIA CONFIRMADA

- `Dados Obra` → `Produção`: jornada, calendário e volume.
- `Produção` → `3. Canteiro`: prazo total de 6 meses.
- `Produção` → `6. Prep Célula`, `7.2 Draga`, `7.3 Op.Planta`: prazo de operação de 4 meses, ainda que algumas referências tenham sido avaliadas como erro.
- `3. Canteiro` → várias abas: valores-hora e composição de equipe.
- `Barrilete` → `4. Mob Draga + Pol.`: apropriação de 30%.
- `6. Prep Célula` → `Plan. Final`: custo total dividido por área.
- `7.1. Bags` → `Plan. Final`: custo dividido pelo volume in situ.
- `7.2 Draga` → `Plan. Final`: custo total de quatro meses.
- `7.3 Op.Planta` → `Plan. Final`: custo total da planta.
- desmobilizações → `Plan. Final`: valores globais.
- `Plan. Final` aplica BDI comercial e consolida preço.

# 9. Terminologia observada

- `vb`: verba/global;
- `ST`: sólidos totais;
- `TS`: tonelada seca;
- `UAP`: unidade/equipamento de preparo de polímero, sem expansão textual no arquivo;
- `seio da linha`: parcela adicional da linha, zerada neste orçamento;
- `hora à disposição`: custo/hora baseado em horas totais disponíveis;
- `hora produtiva`: preço/hora após eficiência;
- `barrilete`: conjunto de tubos, válvulas, conexões e bomba;
- `primeiro nível` / `segundo nível`: disposição vertical/estratificada dos bags;
- `chute`: estimativa não baseada em cotação formal registrada.

# 10. Anomalias consolidadas

## EVIDÊNCIA CONFIRMADA quanto à existência

- divergência entre nome/código do arquivo e proposta interna;
- títulos copiados incorretamente em algumas abas;
- fórmulas avaliadas como `#NAME?` em referências interabas;
- divisões por zero por prazos vazios ou iguais a zero;
- duas produções mensais diferentes;
- descrição de filtro a 10% com cálculo aparente de 70%;
- “Custo Total” final apontando apenas para uma linha;
- totais auxiliares sem rótulo;
- diferença de valor-hora do encarregado;
- preços de referência diferentes dos preços adotados;
- itens estruturados com quantidade vazia e preço unitário preenchido;
- BDI interno zero em várias abas e BDI comercial aplicado depois;
- produção/custo unitário principal da draga não concluído na própria aba;
- valor de polímero zerado por repasse ao cliente.

# 11. Perguntas para validação futura do especialista

1. Qual é o código correto desta proposta?
2. O volume de 10.000 m³ contém margem fixa de 10%?
3. O retorno de percolado faz parte dos 900 m de recalque?
4. Qual produção é operacionalmente correta?
5. O prazo de 6 meses pressupõe ausência de sobreposição?
6. Por que a brita usa 594 m³ em vez de 540 m³?
7. A seleção de bags usa capacidade geométrica integral?
8. O teor final de 20% é conservador frente à média de 25%?
9. O preço de R$ 60/m² é atualização deliberada da referência de R$ 55/m²?
10. Qual é a fonte do fator 7 da operação da draga?
11. A draga elétrica realmente possui custo chamado combustível?
12. Filtros/lubrificantes são 10% ou 70%?
13. Por que a produção da composição da draga diverge da aba Produção?
14. Quais funções efetivamente compõem a equipe mensal?
15. O custo de polímero é sempre repassado ao cliente neste tipo de obra?
16. Qual sistema de polímero foi efetivamente escolhido?
17. Por que o encarregado tem valor-hora maior na desmobilização final?
18. O que representam `C17`, `C20` e a coluna `L` da planilha final?
19. Qual deveria ser o custo total consolidado?
20. Os erros de referência aparecem no Excel original ou somente no avaliador usado nesta análise?

# 12. Checklist de validação

- [x] Todas as 12 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Entidades, regras, fórmulas, dependências, exceções e dúvidas preservadas.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhum outro documento de orçamento alterado.
- [x] Nenhum índice geral alterado.
- [x] Nenhuma consolidação entre planilhas realizada.

# Apêndice A — Inventário integral de fórmulas

As fórmulas abaixo são transcritas para rastreabilidade. A finalidade operacional das principais fórmulas foi explicada nas seções anteriores.

## `Dados Obra`

| Célula | Fórmula |
|---|---|
| `O13` | `=M13+N13` |
| `B14` | `=L13` |
| `L15` | `=SUM(L13:L14)` |
| `M15` | `=AVERAGE(M13:M14)` |
| `N15` | `=AVERAGE(N13:N14)` |
| `O15` | `=AVERAGE(O13:O14)` |
| `B16` | `=B17+B18` |
| `H16` | `=B16+E16` |
| `B17` | `=M15` |
| `H17` | `=B17+E17` |
| `B18` | `=N13` |
| `O18` | `=2*300` |
| `G21` | `=B21*D21*B20` |

## `Produção`

| Célula | Fórmula |
|---|---|
| `I3` | `='Dados Obra '!B26` |
| `I4` | `='Dados Obra '!B27` |
| `I6` | `=I3*I4` |
| `D8` | `=D3*(D4/100)*(D5/100)` |
| `D11` | `=I6` |
| `D13` | `=D8*D11` |
| `D17` | `=D13` |
| `D20` | `='Dados Obra '!B14` |
| `D23` | `=ROUNDUP(D20/D17,0)` |
| `E23` | `=D20/D17` |
| `D27` | `=D23` |
| `H35` | `=D27` |
| `H39` | `=SUM(H32:H38)` |

## `3. Canteiro`

| Célula | Fórmula |
|---|---|
| `A5` | `=N13` |
| `C5` | `=M5` |
| `D5` | `='Dados Obra '!B26*'3. Canteiro'!N5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `J5` | `=I5/220` |
| `K5` | `=J5*0.075` |
| `M5` | `=J5+K5+L5` |
| `D6` | `='Dados Obra '!B26` |
| `J6` | `=I6/220` |
| `K6` | `=J6*0.075` |
| `L6` | `=(J6+K6)*0.25` |
| `M6` | `=J6+K6+L6` |
| `D7` | `=D6` |
| `D8` | `=D7` |
| `J8` | `=I8/220` |
| `K8` | `=J8*0.075` |
| `M8` | `=J8+K8+L8` |
| `D9` | `=D8` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `L11` | `=(J11+K11)*0.25` |
| `A12` | `=SUM(A5:A11)` |
| `F12` | `=A12*C12` |
| `L12` | `=(J12+K12)*0.25` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `K13` | `=J13*0.075` |
| `L13` | `=(J13+K13)*0.25` |
| `M13` | `=J13+K13+L13` |
| `F14` | `=SUM(F5:F13)` |
| `D18` | `=Produção!H39` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `D20` | `=D18` |
| `E22` | `=1500+750+2000+750` |
| `F25` | `=D25*E25` |
| `E26` | `=L26+L27` |
| `D27` | `=D18*8` |
| `D28` | `=D18` |
| `D29` | `=D28` |
| `D30` | `=A12` |
| `F30` | `=D30*E30` |
| `D31` | `=A12` |
| `D32` | `=D31` |
| `F32` | `=D32*E32` |
| `E33` | `=F14` |
| `F34` | `=SUM(F18:F33)` |
| `F35` | `='3. Canteiro'!D18` |
| `F36` | `=F34/F35` |
| `F37` | `=F36*(E37/100)` |
| `F38` | `=F36+F37` |

## `4. Mob Draga + Pol.`

| Célula | Fórmula |
|---|---|
| `A5` | `='3. Canteiro'!A5` |
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='3. Canteiro'!A6` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `=E5` |
| `A7` | `='3. Canteiro'!A7` |
| `C7` | `='3. Canteiro'!C7` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `A8` | `='3. Canteiro'!A8` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `=D7` |
| `E8` | `=E7` |
| `A9` | `='3. Canteiro'!A9` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `=D6` |
| `E9` | `=E8` |
| `A10` | `='3. Canteiro'!A10` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `=D6` |
| `E10` | `=E9` |
| `A11` | `=SUM(A5:A10)` |
| `C11` | `='3. Canteiro'!C12` |
| `F11` | `=A11*C11` |
| `A12` | `=A11` |
| `C12` | `='3. Canteiro'!C13` |
| `F12` | `=A12*C12` |
| `F13` | `=SUM(F5:F12)` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `D18` | `=A11` |
| `F18` | `=D18*E18` |
| `E19` | `=N31` |
| `N19` | `=L19*M19` |
| `E20` | `=E19` |
| `N20` | `=L20*M20` |
| `F21` | `=D21*E21` |
| `N21` | `=L21*M21` |
| `E22` | `=E21` |
| `F22` | `=D22*E22` |
| `F23` | `=D23*E23` |
| `N23` | `=L23*M23` |
| `F24` | `=D24*E24` |
| `F25` | `=D25*E25` |
| `F26` | `=D26*E26` |
| `E27` | `=Barrilete!F29` |
| `F27` | `=D27*E27` |
| `E28` | `=F13` |
| `F28` | `=D28*E28` |
| `E29` | `=F13` |
| `F30` | `=SUM(F16:F29)` |
| `F31` | `=F30*(E31/100)` |
| `N31` | `=SUM(N19:N30)` |
| `F32` | `=SUM(F30:F31)` |

## `Barrilete`

| Célula | Fórmula |
|---|---|
| `A4` | `='4. Mob Draga + Pol.'!A7` |
| `C4` | `='3. Canteiro'!C7` |
| `D4` | `='3. Canteiro'!D6` |
| `E4` | `='3. Canteiro'!E5` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `A5` | `='4. Mob Draga + Pol.'!A9` |
| `C5` | `='3. Canteiro'!C9` |
| `D5` | `='3. Canteiro'!D6` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='4. Mob Draga + Pol.'!A10` |
| `C6` | `='3. Canteiro'!C10` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `='3. Canteiro'!E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=SUM(A4:A6)` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F4:F8)` |
| `E14` | `=560` |
| `F14` | `=D14*E14` |
| `E15` | `=210*1.1` |
| `F15` | `=D15*E15` |
| `E16` | `=210*1.1` |
| `F16` | `=D16*E16` |
| `E17` | `=280*1.1` |
| `F17` | `=D17*E17` |
| `E18` | `=70*1.1` |
| `F18` | `=D18*E18` |
| `E19` | `=49` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `E23` | `=17.8181818181818*1.1` |
| `F23` | `=D23*E23` |
| `F24` | `=D24*E24` |
| `F25` | `=D25*E25` |
| `F26` | `=D26*E26` |
| `E27` | `=F9` |
| `F27` | `=D27*E27` |
| `F28` | `=SUM(F14:F27)` |
| `F29` | `=F28*0.3` |
| `F30` | `=F29*(E30/100)` |
| `F31` | `=F29+F30` |

## `6. Prep Célula`

| Célula | Fórmula |
|---|---|
| `A5` | `='3. Canteiro'!A5` |
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='3. Canteiro'!A6` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `='3. Canteiro'!E6` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `='3. Canteiro'!A7` |
| `C7` | `='3. Canteiro'!C7` |
| `D7` | `='3. Canteiro'!D7` |
| `E7` | `='3. Canteiro'!E7` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `='3. Canteiro'!A8` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `='3. Canteiro'!D8` |
| `E8` | `='3. Canteiro'!E8` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `='3. Canteiro'!A9` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `='3. Canteiro'!D9` |
| `E9` | `='3. Canteiro'!E9` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `A10` | `='3. Canteiro'!A10` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `='3. Canteiro'!D10` |
| `E10` | `='3. Canteiro'!E10` |
| `F10` | `=(A10*C10*D10)+(A10*C10*D10)*(E10/100)` |
| `A12` | `=SUM(A5:A11)` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `K15` | `=I15*J15` |
| `M15` | `=K15*L15` |
| `K16` | `=I16*J16` |
| `M16` | `=K16*L16` |
| `M17` | `=SUM(M15:M16)` |
| `N7` | `=J7*M7` |
| `N8` | `=J8*M8` |
| `N9` | `=J9*M9` |
| `N10` | `=J10*M10` |
| `N11` | `=J11*M11` |
| `N12` | `=N10/8` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `E22` | `=F14` |
| `F22` | `=D22*E22` |
| `F23` | `=D23*E23` |
| `F24` | `=D24*E24` |
| `F25` | `=D25*E25` |
| `F26` | `=D26*E26` |
| `D27` | `=N9*1.1` |
| `F27` | `=D27*E27` |
| `F28` | `=D28*E28` |
| `F29` | `=D29*E29` |
| `F30` | `=D30*E30` |
| `F31` | `=D31*E31` |
| `D32` | `=ROUNDUP(N10/8,0)` |
| `F32` | `=D32*E32` |
| `D33` | `=D32` |
| `E33` | `=F14` |
| `F33` | `=D33*E33` |
| `F34` | `=SUM(F18:F33)` |
| `F36` | `=F34/F35` |
| `F37` | `=F36*(E37/100)` |
| `F38` | `=F36+F37` |

## `7.1. Bags`

| Célula | Fórmula |
|---|---|
| `A5` | `='3. Canteiro'!A5` |
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='3. Canteiro'!A6` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `='3. Canteiro'!E6` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `='3. Canteiro'!A7` |
| `C7` | `='3. Canteiro'!C7` |
| `D7` | `='3. Canteiro'!D7` |
| `E7` | `='3. Canteiro'!E7` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `='3. Canteiro'!A8` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `='3. Canteiro'!D8` |
| `E8` | `='3. Canteiro'!E8` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `='3. Canteiro'!A9` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `='3. Canteiro'!D9` |
| `E9` | `='3. Canteiro'!E9` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `A10` | `='3. Canteiro'!A10` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `='3. Canteiro'!D10` |
| `E10` | `='3. Canteiro'!E10` |
| `F10` | `=(A10*C10*D10)+(A10*C10*D10)*(E10/100)` |
| `A12` | `=SUM(A5:A11)` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `I18` | `='Dados Obra '!B14` |
| `I20` | `=I18*I19` |
| `I23` | `=I20/I22` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `F23` | `=D23*E23` |
| `F24` | `=D24*E24` |
| `F25` | `=D25*E25` |
| `F26` | `=D26*E26` |
| `F27` | `=D27*E27` |
| `E28` | `=F14` |
| `F28` | `=D28*E28` |
| `F29` | `=SUM(F18:F28)` |
| `F31` | `=F29/F30` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |
| `D38` | `=B38*C38` |
| `F38` | `=D38*E38` |
| `M38` | `=I38*J38*K38` |
| `D39` | `=B39*C39` |
| `F39` | `=D39*E39` |
| `M39` | `=I39*J39*K39` |
| `D40` | `=B40*C40` |
| `F40` | `=D40*E40` |
| `M40` | `=I40*J40*K40` |
| `D41` | `=B41*C41` |
| `F41` | `=D41*E41` |
| `M41` | `=I41*J41*K41` |
| `D42` | `=B42*C42` |
| `F42` | `=D42*E42` |
| `M42` | `=I42*J42*K42` |
| `D43` | `=B43*C43` |
| `F43` | `=D43*E43` |
| `M43` | `=I43*J43*K43` |
| `F44` | `=SUM(F38:F43)` |
| `D47` | `=B47*C47` |
| `F47` | `=D47*E47` |
| `D48` | `=B48*C48` |
| `F48` | `=D48*E48` |
| `M48` | `=I48*J48*K48` |
| `D49` | `=B49*C49` |
| `F49` | `=D49*E49` |
| `M49` | `=I49*J49*K49` |
| `D50` | `=B50*C50` |
| `F50` | `=D50*E50` |
| `M50` | `=I50*J50*K50` |
| `D51` | `=B51*C51` |
| `F51` | `=D51*E51` |
| `D52` | `=B52*C52` |
| `F52` | `=D52*E52` |
| `F53` | `=SUM(F47:F52)` |
| `F54` | `=F44+F53` |

## `7.2 Draga`

| Célula | Fórmula |
|---|---|
| `C9` | `=Produção!I6` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=F10*0.7` |
| `E15` | `=SUM(F10:F13)` |
| `L20` | `=J20*K20` |
| `L21` | `=J21*K21` |
| `L23` | `=J23*K23` |
| `L24` | `=L20*1.7+L21*2+L23` |
| `A20` | `=L24*0.5` |
| `A21` | `=L24` |
| `A22` | `=L24` |
| `A23` | `=L24` |
| `A24` | `=L24` |
| `A25` | `=L24` |
| `A26` | `=L24` |
| `A27` | `=L24` |
| `D20` | `='3. Canteiro'!C5` |
| `D21` | `='3. Canteiro'!C6` |
| `D22` | `='3. Canteiro'!C7` |
| `D23` | `='3. Canteiro'!C8` |
| `D24` | `='3. Canteiro'!C9` |
| `D25` | `='3. Canteiro'!C10` |
| `E20` | `=A20*B20*D20` |
| `E21` | `=A21*B21*D21` |
| `E22` | `=A22*B22*D22` |
| `E23` | `=A23*B23*D23` |
| `E24` | `=A24*B24*D24` |
| `E25` | `=A25*B25*D25` |
| `E26` | `=A26*B26*D26` |
| `E27` | `=A27*B27*D27` |
| `E31` | `=SUM(E20:E27)` |
| `C37` | `=E31` |
| `E37` | `=A37/100*C37` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E46` | `=SUM(G52:G53)` |
| `E69` | `=B69*D69` |
| `E71` | `=SUM(E67:E70)` |
| `G87` | `=SUM(E15+E31+E37+E46+E62+E71+E86)` |
| `E94` | `=F7*0.006` |
| `E95` | `=F7*0.01` |
| `E99` | `=SUM(E94:E97)` |
| `K105` | `=I105*J105` |
| `J106` | `=K105/I106` |
| `J107` | `=J106*I107` |
| `J108` | `=SUM(J106:J107)` |
| `K110` | `=I110*J110` |
| `J111` | `=K110/I111` |
| `J112` | `=J111*I112` |
| `J113` | `=SUM(J111:J112)` |
| `K115` | `=I115*J115` |
| `J116` | `=K115/I116` |
| `J117` | `=J116*I117` |
| `J118` | `=SUM(J116:J117)` |
| `H121` | `=J108` |
| `I121` | `=J113` |
| `J121` | `=J118` |
| `K121` | `=SUM(H121:J121)` |
| `E104` | `=K121` |
| `E108` | `=SUM(E104:E107)` |
| `E128` | `=SUM(E127:E127)` |
| `G132` | `=SUM(E15+E87+E99+E108+E128)` |
| `E136` | `=G132*0.05` |
| `E137` | `=G132*0.05` |
| `E138` | `=G132*0` |
| `E141` | `=SUM(E136:E138)` |
| `E146` | `=F7/60` |
| `E147` | `=F7*0.01` |
| `E150` | `=SUM(E146:E148)` |
| `D169` | `=G132` |
| `D172` | `=E141` |
| `D174` | `=E150` |
| `D176` | `=SUM(D169,D172,D174)` |
| `D179` | `=Produção!D13*D199` |
| `D183` | `=D176/Produção!I6` |
| `J199` | `=H199*I199` |
| `D198` | `=D176` |
| `D200` | `=SUM(D198:D199)` |
| `D201` | `=Produção!H35` |
| `D202` | `=D200*D201` |
| `J201` | `=D176` |
| `J202` | `=1.5` |
| `J203` | `=J201*J202` |
| `J204` | `=Produção!I6` |
| `J205` | `=0.6` |
| `J206` | `=J204*J205` |
| `J207` | `=J203/J206` |
| `L203` | `=J203/J204` |
| `L204` | `=J204/330` |
| `L205` | `=L203*L204` |

## `7.3 Op.Planta`

| Célula | Fórmula |
|---|---|
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `='3. Canteiro'!E6` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='3. Canteiro'!C7` |
| `D7` | `='3. Canteiro'!D7` |
| `E7` | `='3. Canteiro'!E7` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `='3. Canteiro'!D8` |
| `E8` | `='3. Canteiro'!E8` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `='3. Canteiro'!D9` |
| `E9` | `='3. Canteiro'!E9` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `='3. Canteiro'!D10` |
| `E10` | `='3. Canteiro'!E10` |
| `F10` | `=(A10*C10*D10)+(A10*C10*D10)*(E10/100)` |
| `A12` | `=SUM(A5:A11)` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `D18` | `=Produção!H35` |
| `E18` | `=L15/24` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `E19` | `=E18*0.1` |
| `F19` | `=D19*E19` |
| `D20` | `=D35` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `D26` | `=Produção!H35*22` |
| `E26` | `=F14` |
| `F26` | `=D26*E26` |
| `F27` | `=SUM(F18:F26)` |
| `F29` | `=F27/F28` |
| `F30` | `=F29*(E30/100)` |
| `F31` | `=F29+F30` |
| `D33` | `='7.1. Bags'!I20` |
| `D35` | `=D33*D34` |

## `9. DesMob Draga + Pol.`

| Célula | Fórmula |
|---|---|
| `A5` | `='3. Canteiro'!A5` |
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='3. Canteiro'!A6` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `='3. Canteiro'!E6` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `='3. Canteiro'!A7` |
| `C7` | `='3. Canteiro'!C7` |
| `D7` | `='3. Canteiro'!D7` |
| `E7` | `='3. Canteiro'!E7` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `='3. Canteiro'!A8` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `='3. Canteiro'!D8` |
| `E8` | `='3. Canteiro'!E8` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `='3. Canteiro'!A9` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `='3. Canteiro'!D9` |
| `E9` | `='3. Canteiro'!E9` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `A10` | `='3. Canteiro'!A10` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `='3. Canteiro'!D10` |
| `E10` | `='3. Canteiro'!E10` |
| `F10` | `=(A10*C10*D10)+(A10*C10*D10)*(E10/100)` |
| `A11` | `=SUM(A5:A10)` |
| `F11` | `=A11*C11` |
| `A12` | `=A11` |
| `F12` | `=A12*C12` |
| `F13` | `=SUM(F5:F12)` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `E22` | `=E21` |
| `F22` | `=D22*E22` |
| `F23` | `=D23*E23` |
| `F24` | `=D24*E24` |
| `F25` | `=D25*E25` |
| `F26` | `=D26*E26` |
| `E27` | `=Barrilete!F29` |
| `F27` | `=D27*E27` |
| `F28` | `=D28*E28` |
| `E29` | `=F13` |
| `F29` | `=D29*E29` |
| `F30` | `=SUM(F16:F29)` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=F30+F31` |

## `15. Desmob Final`

| Célula | Fórmula |
|---|---|
| `A5` | `='3. Canteiro'!A5` |
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='3. Canteiro'!A6` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `='3. Canteiro'!E6` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `='3. Canteiro'!A7` |
| `C7` | `=M7` |
| `D7` | `='3. Canteiro'!D7` |
| `E7` | `='3. Canteiro'!E7` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `='3. Canteiro'!A8` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `='3. Canteiro'!D8` |
| `E8` | `='3. Canteiro'!E8` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `='3. Canteiro'!A9` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `='3. Canteiro'!D9` |
| `E9` | `='3. Canteiro'!E9` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `A10` | `='3. Canteiro'!A10` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `='3. Canteiro'!D10` |
| `E10` | `='3. Canteiro'!E10` |
| `F10` | `=(A10*C10*D10)+(A10*C10*D10)*(E10/100)` |
| `A12` | `=SUM(A5:A11)` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `J5` | `=I5/220` |
| `K5` | `=J5*0.075` |
| `M5` | `=J5+K5+L5` |
| `J6` | `=I6/220` |
| `K6` | `=J6*0.075` |
| `L6` | `=(J6+K6)*0.25` |
| `M6` | `=J6+K6+L6` |
| `K7` | `=J7*0.075` |
| `L7` | `=(J7+K7)*0.25` |
| `M7` | `=J7+K7+L7` |
| `J8` | `=I8/220` |
| `K8` | `=J8*0.075` |
| `L8` | `=(J8+K8)*0.25` |
| `M8` | `=J8+K8+L8` |
| `J9` | `=I9/220` |
| `K9` | `=J9*0.075` |
| `L9` | `=(J9+K9)*0.25` |
| `M9` | `=J9+K9+L9` |
| `J10` | `=I10/220` |
| `K10` | `=J10*0.075` |
| `M10` | `=J10+K10+L10` |
| `F21` | `=D21*E21` |
| `F30` | `=D30*E30` |
| `F31` | `=D31*E31` |
| `E33` | `=F14` |
| `F33` | `=D33*E33` |
| `F34` | `=SUM(F18:F33)` |
| `F36` | `=F34/F35` |
| `F37` | `=F36*(E37/100)` |
| `F38` | `=F36+F37` |

## `Plan. Final`

| Célula | Fórmula |
|---|---|
| `C5` | `='3. Canteiro'!F34` |
| `E5` | `=Produção!H39` |
| `G5` | `=C5/E5` |
| `I5` | `=G5+(G5*H5/100)` |
| `J5` | `=I5*E5` |
| `L5` | `=I5` |
| `C6` | `='4. Mob Draga + Pol.'!F32` |
| `G6` | `=C6/E6` |
| `I6` | `=G6+(G6*H6/100)` |
| `J6` | `=I6*E6` |
| `L6` | `=I6` |
| `C7` | `='6. Prep Célula'!F34` |
| `E7` | `='6. Prep Célula'!M17` |
| `G7` | `=C7/E7` |
| `I7` | `=G7+(G7*H7/100)` |
| `J7` | `=I7*E7` |
| `L7` | `=I7` |
| `C9` | `='7.1. Bags'!F29` |
| `E9` | `='Dados Obra '!B14` |
| `G9` | `=C9/E9` |
| `I9` | `=G9+(G9*H9/100)` |
| `J9` | `=I9*E9` |
| `L9` | `=SUM(I9:I11)` |
| `C10` | `='7.2 Draga'!D202` |
| `E10` | `='Dados Obra '!B14` |
| `G10` | `=C10/E10` |
| `I10` | `=G10+(G10*H10/100)` |
| `J10` | `=I10*E10` |
| `C11` | `='7.3 Op.Planta'!F27` |
| `E11` | `='Dados Obra '!B14` |
| `G11` | `=C11/E11` |
| `I11` | `=G11+(G11*H11/100)` |
| `J11` | `=I11*E11` |
| `C12` | `='9. DesMob Draga + Pol.'!F30` |
| `G12` | `=C12/E12` |
| `I12` | `=G12+(G12*H12/100)` |
| `J12` | `=I12*E12` |
| `L12` | `=I12` |
| `C13` | `='15. Desmob Final'!F34` |
| `G13` | `=C13/E13` |
| `I13` | `=G13+(G13*H13/100)` |
| `J13` | `=I13*E13` |
| `L13` | `=I13` |
| `C15` | `=SUM(C13)` |
| `J15` | `=SUM(J5:J13)` |
| `C17` | `=SUM(J5:J12)` |
| `C20` | `=J15*0.01` |
