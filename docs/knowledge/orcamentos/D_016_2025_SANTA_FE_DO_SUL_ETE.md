# Análise — `D_016_2025- Santa Fé do Sul - ETE.xlsx`

## 1. Identificação da análise

- **Nome completo do arquivo:** `D_016_2025- Santa Fé do Sul - ETE.xlsx`
- **Data da análise:** 2026-07-14
- **Versão identificável no arquivo:** não há número de revisão explícito; a proposta interna é `D_016_2025`.
- **Data registrada na planilha:** 2025-03-18.
- **Quantidade de abas:** 15.
- **Status da análise:** engenharia reversa vertical concluída para o conteúdo acessível do arquivo.
- **Escopo:** documentação exclusiva deste Excel.
- **Implementação, arquitetura ou consolidação:** não realizadas.

## 2. Regra de evidência usada neste documento

Para atender ao Kid Step V2, as afirmações são marcadas como:

- **EVIDÊNCIA CONFIRMADA:** conteúdo, valor, fórmula, vínculo ou anomalia diretamente observado no Excel.
- **EVIDÊNCIA PARCIAL:** interpretação ou padrão observado somente neste orçamento, sem validade geral para a FOS.
- **DÚVIDA:** ponto sem comprovação suficiente na fonte.

As marcações não transformam valores desta planilha em regras gerais da FOS.

## 3. Classificação do orçamento

### 3.1 Tipo aparente

**EVIDÊNCIA CONFIRMADA —** orçamento para **dragagem de lodo de estação de tratamento de esgoto, com desaguamento por bags/geobags e dosagem de polímero**.

A classificação é sustentada pelos registros:

- objeto: `Dragagem e Desaguamento em Geobags`;
- local: Santa Fé do Sul — SP;
- material: `Lodo - ETE`;
- bota-fora: `Bag`;
- equipamento: draga elétrica de 6";
- presença de sistema de preparo e injeção de polímero;
- fornecimento de bags 8 × 30 m;
- cliente indicado em `Dados Obra`: SAAE — Santa Fé do Sul;
- referência indicada em `7. Dragagem`: ETE Santa Fé do Sul e cliente DAAE.

### 3.2 Processo operacional representado

**EVIDÊNCIA CONFIRMADA —** o arquivo representa o seguinte processo:

```text
dados e premissas da obra
        ↓
produção da draga e prazo teórico
        ↓
mobilização da draga
        ↓
composição/depreciação do barrilete
        ↓
mobilização do sistema de polímero
        ↓
preparo da célula de recebimento
        ↓
dimensionamento e fornecimento de bags
        ↓
canteiro de obras
        ↓
operação do sistema de desidratação
        ↓
dragagem e custos mensais
        ↓
desmobilizações
        ↓
medição
        ↓
planilha consolidada de custos e preços de venda
```

### 3.3 Área de atuação

**EVIDÊNCIA CONFIRMADA —** saneamento, especificamente dragagem e manejo de lodo de ETE.

### 3.4 Características particulares deste orçamento

- **EVIDÊNCIA CONFIRMADA —** volume orçado de 5.000 m³.
- **EVIDÊNCIA CONFIRMADA —** distância total de recalque de 500 m, composta por 200 m de linha flutuante e 300 m de linha terrestre.
- **EVIDÊNCIA CONFIRMADA —** operação prevista em 9 h/dia e 22 dias/mês.
- **EVIDÊNCIA CONFIRMADA —** sistema de medição descrito como `preços unitários de serviços`.
- **EVIDÊNCIA CONFIRMADA —** canteiro e mobilização atribuídos à FOS.
- **EVIDÊNCIA CONFIRMADA —** preparo da célula foi estruturado tecnicamente, mas todos os seus custos foram excluídos do preço por indicação `Responsabilidade SAAE`.
- **EVIDÊNCIA CONFIRMADA —** água para operação do polímero foi atribuída ao SAAE; a linha de gerador também contém anotação `SAAE`, embora mantenha custo.
- **EVIDÊNCIA PARCIAL —** o arquivo parece ter sido preparado como cotação para concorrência, pois a aba `Orçamentos` registra que não houve orçamento específico por se tratar somente de cotação para concorrência.
- **DÚVIDA —** divergência de identificação do cliente entre `SAAE` e `DAAE`; o Excel não explica se é erro de digitação, mudança de denominação ou entidades distintas.

## 4. Inventário das abas

| Ordem | Aba | Papel observado |
| ---: | --- | --- |
| 1 | `Dados Obra` | Identificação, premissas técnicas, responsabilidades e calendário. |
| 2 | `Orçamentos` | Registro pontual de cotação de guindaste. |
| 3 | `Produção` | Produção horária, produção mensal e prazo teórico. |
| 4 | `1. Mob. Draga` | Mobilização da draga, fretes, guindaste e equipe. |
| 5 | `Barrilete` | Composição física do barrilete e apropriação por depreciação. |
| 6 | `2. Mob. Eq. Polimero` | Mobilização e montagem do sistema de polímero. |
| 7 | `3. Prep. Célula` | Memorial físico e composição de preparo da célula. |
| 8 | `4. Forn. Bag` | Dimensionamento e fornecimento dos bags. |
| 9 | `5. Canteiro de obras` | Custos temporários do canteiro, apropriados mensalmente. |
| 10 | `6. Operação Sistema` | Equipamento, polímero, energia e equipe do desaguamento. |
| 11 | `7. Dragagem` | Centro principal de custos mensais da dragagem. |
| 12 | `8. Desmob. Draga` | Desmobilização da draga. |
| 13 | `9. Desmob. Eq. Polimero` | Desmobilização do sistema de polímero. |
| 14 | `10. Mediçao` | Laboratório, batimetria e acompanhamento FOS. |
| 15 | `12. Plan. Preços` | Consolidação de custo, BDI, preço unitário e preço total. |

**EVIDÊNCIA CONFIRMADA —** não existe aba numerada como `11`, e a consolidação final inicia em `12. Plan. Preços`.

---

## 5. Análise integral por aba

## 5.1 `Dados Obra`

### Objetivo e papel no fluxo

**EVIDÊNCIA CONFIRMADA —** concentra identificação comercial, caracterização da obra, premissas geométricas, responsabilidades operacionais e calendário usado por outras abas.

### Entradas observadas

- proposta: `Proposta D_016_2025`;
- data: 18/03/2025;
- cliente: `SAAE - Santa Fé do Sul`;
- contato e e-mail: não preenchidos;
- objeto: `Dragagem e Desaguamento em Geobags`;
- local: Santa Fé do Sul — SP;
- volume de dragagem: 5.000 m³;
- material: lodo de ETE;
- distância de recalque: 500 m;
- linha flutuante: 200 m;
- linha de terra: 300 m;
- profundidade: não preenchida;
- espessura média: não preenchida;
- área/dimensões: não preenchidas;
- tipo de bota-fora: Bag;
- sistema de medição: preços unitários de serviços;
- canteiro: FOS;
- mobilização: FOS;
- jornada: 9 h/dia;
- calendário: 22 dias/mês.

### Fórmulas e finalidade

- `H16 = B16 + E16`: soma a distância informada e eventual “seio da linha”.
- `H17 = B17 + E17`: soma linha flutuante e eventual “seio da linha”.
- `G21 = B21 * D21 * B20`: calcula volume geométrico com dimensões/espessura, quando preenchidas.

### Dependências de saída

Jornada e dias/mês alimentam `Produção` e várias composições de mão de obra. Volume alimenta `Produção` e `4. Forn. Bag`. Distâncias alimentam a composição da linha de recalque em `7. Dragagem`.

### Regras e observações

- **EVIDÊNCIA CONFIRMADA —** cores possuem semântica declarada: azul para entrada, vermelho para pendência e preto para resultado automático.
- **EVIDÊNCIA CONFIRMADA —** o volume é informado diretamente, embora exista fórmula alternativa de volume geométrico.
- **DÚVIDA —** profundidade, espessura e área permanecem vazias; não é possível saber se foram desnecessárias ou apenas não levantadas.
- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** diversas fórmulas em outras abas aparecem referenciando `'Dados Obra '` com espaço final, enquanto o nome visível da aba é `Dados Obra`. O arquivo mantém resultados em várias dessas células, mas a diferença nominal deve ser preservada como risco de referência.

## 5.2 `Orçamentos`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** registra uma única cotação de mercado.

### Conteúdo

- empresa/descrição: `GRUPO SAO JOAO Munck Guindaste`;
- equipamento: guindaste de 50 toneladas;
- preço: R$ 7.500,00;
- contato: Flora;
- telefone: registrado no arquivo;
- data: 26/02/2025;
- observação: não foi feito orçamento específico porque seria somente cotação para concorrência.

### Regras e dependências

- **EVIDÊNCIA CONFIRMADA —** não foram observadas fórmulas.
- **EVIDÊNCIA PARCIAL —** o preço de R$ 7.500,00 coincide com o guindaste usado na mobilização e desmobilização, mas não há referência de célula ligando diretamente esta aba às composições.
- **DÚVIDA —** não é possível comprovar se a cotação foi formalmente aceita ou apenas usada como referência manual.

## 5.3 `Produção`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** converte vazão, eficiência, concentração e calendário em produção mensal e prazo teórico.

### Entradas

- vazão: 120 m³/h;
- eficiência: 65%;
- concentração: 15%;
- horas/dia: 9;
- dias/mês: 22;
- volume: 5.000 m³.

### Fórmulas

- `H3 = Dados Obra!B26`: horas por dia.
- `H4 = Dados Obra!B27`: dias por mês.
- `H6 = H3 * H4`: 198 h/mês.
- `D8 = D3 * (D4/100) * (D5/100)`: 11,7 m³/h de sólidos/material considerado.
- `D11 = H6`: horas trabalhadas por mês.
- `D13 = D8 * D11`: 2.316,6 m³/mês.
- `D18 = D13`: replica produção mensal para o cálculo do prazo.
- `D21 = Dados Obra!B14`: volume a dragar.
- `D24 = D21 / D18`: prazo de 2,158335 meses.

### Regras e dependências

- **EVIDÊNCIA CONFIRMADA —** eficiência e concentração são multiplicadores percentuais simultâneos da vazão.
- **EVIDÊNCIA CONFIRMADA —** o prazo não é arredondado nesta aba; outras abas aplicam `ROUNDUP`.
- **EVIDÊNCIA CONFIRMADA —** produção mensal alimenta `7. Dragagem`; prazo alimenta canteiro, operação do sistema e total de dragagem.
- **EVIDÊNCIA PARCIAL —** a produção calculada parece tratar o produto vazão × eficiência × concentração como volume efetivo de material, mas a natureza física exata da unidade não é explicitada.
- **DÚVIDA —** não há margem adicional de contingência no prazo desta aba.

## 5.4 `1. Mob. Draga`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** compõe o evento único de mobilização da draga elétrica de 6".

### Equipe diária

- 1 operador líder;
- 2 operadores de draga;
- 4 ajudantes gerais;
- 7 refeições;
- 7 transportes;
- jornada de 9 h;
- leis sociais de 100%;
- custo diário: R$ 2.643,56.

### Serviços e recursos

- guindaste para carregamento;
- carreta prancha rebaixada;
- carreta extensível;
- três carretas de carga seca para a draga;
- guindaste de descarregamento/montagem;
- trator D4;
- quatro dias de mão de obra.

### Fórmulas e resultado

A mão de obra segue a família:

```text
quantidade × R$/h × horas/dia
+ o mesmo valor × leis sociais %
```

Refeição e transporte seguem quantidade × preço unitário.

- total dos recursos: R$ 56.574,24;
- BDI interno: 0%;
- preço final: R$ 56.574,24.

### Observações e anomalias

- **EVIDÊNCIA CONFIRMADA —** várias linhas existem com quantidade vazia e total zero, preservando opções de transporte/equipamento.
- **EVIDÊNCIA CONFIRMADA —** anotação da carreta de carga seca menciona Fabiano, data 25/02/25 e `11500 + 0,2%`, enquanto o preço usado é R$ 12.500,00.
- **EVIDÊNCIA CONFIRMADA —** guindaste de montagem usa R$ 7.500,00, compatível com a cotação da aba `Orçamentos`, sem vínculo por fórmula.
- **DÚVIDA —** a anotação `0,2%` não possui base explicitada.

## 5.5 `Barrilete`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** calcula o valor apropriado do barrilete usado na instalação do sistema.

### Composição

Inclui tubos de ferro de 8", tocos, joelhos, tees, ponteiras, caps, válvulas, mangueira, braçadeiras, curva PVC, válvula esfera, bomba lameira e mão de obra.

### Formação de preços

**EVIDÊNCIA CONFIRMADA —** diversos preços unitários são formados por um valor-base multiplicado por 1,4, por exemplo:

- tubo: `400 × 1,4`;
- toco/joelho: `165 × 1,4`;
- tee: `220 × 1,4`;
- válvula gaveta 8": `2.000 × 1,4`;
- válvula gaveta 6": `1.100 × 1,4`;
- bomba lameira: `1.200 × 1,4`.

### Resultado e apropriação

- composição integral: R$ 27.964,96;
- depreciação apropriada: 25%, equivalente a R$ 6.991,24;
- BDI interno: 0%;
- preço final consumido por `2. Mob. Eq. Polimero`: R$ 6.991,24.

### Evidências e dúvidas

- **EVIDÊNCIA CONFIRMADA —** somente 25% do valor integral é levado ao orçamento.
- **EVIDÊNCIA PARCIAL —** o multiplicador 1,4 aparenta ser margem, atualização ou fator de preço interno, mas sua finalidade não está nomeada.
- **DÚVIDA —** não há vida útil, número de utilizações ou justificativa explícita para os 25%.

## 5.6 `2. Mob. Eq. Polimero`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** compõe mobilização e montagem do equipamento de preparo/injeção de polímero.

### Conteúdo

- verba para cobertura do equipamento;
- brita e concreto, sem quantidade/preço;
- frete de mobilização;
- instalações hidráulicas e elétricas;
- meia apropriação de máquina WAP;
- barrilete;
- três dias de mão de obra de apoio.

### Dependências

- `E21 = Barrilete!F31`: incorpora R$ 6.991,24 do barrilete.
- `E22 = custo diário da equipe`: incorpora R$ 2.035,56 por dia.
- total: R$ 34.847,92.
- BDI interno: 0%.
- preço final: R$ 34.847,92.

### Observações

- **EVIDÊNCIA CONFIRMADA —** brita e concreto permanecem como itens opcionais zerados.
- **EVIDÊNCIA CONFIRMADA —** máquina WAP é apropriada em quantidade 0,5.
- **EVIDÊNCIA CONFIRMADA —** a fórmula de `Preço Final` retorna diretamente o subtotal, apesar de existir linha de BDI.

## 5.7 `3. Prep. Célula`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** dimensiona fisicamente e precifica o preparo de uma célula com manta PEAD, Bidim e brita.

### Memorial de quantidades

Para área de célula de 1.800 m²:

- manta PEAD: 1,196 m²/m² → 2.152,8 m²;
- Bidim: 1,48 m²/m² → 2.664 m²;
- brita: 0,17 m³/m² → 306 m³ no memorial;
- retroescavadeira: 0,023 h/m² → 41,4 h;
- mão de obra: 0,023 h/m² → 41,4 h;
- conversão de mão de obra: 4,14 dias, usando divisão por 10;
- observação de equipe: 4 oficiais + 6 ajudantes.

### Composição financeira

Itens previstos:

- preparo de terreno;
- mobilização de patrola;
- aluguel e mobilização de retroescavadeira;
- regularização manual;
- manta PEAD;
- instalação de PEAD;
- taxa de mobilização da mão de obra PEAD;
- Bidim;
- brita;
- retroescavadeira;
- mão de obra de instalação.

### Responsabilidade e resultado

- **EVIDÊNCIA CONFIRMADA —** as linhas relevantes estão marcadas `Responsabilidade SAAE`.
- **EVIDÊNCIA CONFIRMADA —** subtotal, BDI e preço final são zero.
- **EVIDÊNCIA CONFIRMADA —** os valores brutos calculados permanecem visíveis, mas não entram no total.

### Anomalias

- **EVIDÊNCIA CONFIRMADA —** o memorial calcula 306 m³ de brita (`0,17 × 1.800`), mas a composição utiliza 351,9 m³, resultante de `O8 × 1,15`.
- **EVIDÊNCIA CONFIRMADA —** existe anotação `10.500 m2 cobre a base das duas lagoas`, sem vínculo de fórmula com a área de 1.800 m².
- **DÚVIDA —** não está explícito se os 15% adicionais de brita representam empolamento, perda, contingência ou critério executivo.
- **DÚVIDA —** não está claro se a célula de 1.800 m² é uma das duas lagoas ou apenas área de orçamento.

## 5.8 `4. Forn. Bag`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** dimensiona capacidade de acondicionamento e compõe fornecimento/instalação dos bags.

### Modelo físico

- volume de dragagem: 5.000 m³;
- sólidos in situ: 8%;
- tonelada seca: 400;
- sólidos após desaguamento: 25%;
- volume a acomodar: 1.600 m³;
- capacidade bag 8 × 60: 880 m³, quantidade zero;
- capacidade bag 8 × 30: 440 m³, quantidade quatro;
- capacidade total selecionada: 1.760 m³.

Fórmulas:

```text
tonelada seca = volume × % sólidos in situ
volume após desaguamento = tonelada seca ÷ % sólidos desaguados
capacidade selecionada = capacidade unitária × quantidade
```

### Composição financeira

- quatro bags 8 × 30 m a R$ 35.000,00;
- frete: R$ 2.500,00;
- munck: R$ 1.300,00;
- um dia de mão de obra: R$ 2.643,56;
- total/preço final: R$ 146.443,56;
- BDI interno: 0%.

### Dependências

- quantidade de bags da célula `C33` alimenta a composição.
- tonelada seca alimenta o consumo de polímero em `6. Operação Sistema`.
- custo e quantidade alimentam `12. Plan. Preços`.

### Evidências e dúvidas

- **EVIDÊNCIA CONFIRMADA —** capacidade total excede em 160 m³ a necessidade calculada.
- **EVIDÊNCIA CONFIRMADA —** anotação do munck menciona `desmob - 1300 x 2`, mas a composição usa quantidade 1.
- **EVIDÊNCIA PARCIAL —** a seleção de quatro bags parece ser arredondamento operacional para cima.
- **DÚVIDA —** capacidades de 440 e 880 m³ não possuem fonte ou condição de enchimento declarada.
- **DÚVIDA —** o significado físico de `% Solidos Desagua = 0,25` não é detalhado.

## 5.9 `5. Canteiro de obras`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** calcula infraestrutura temporária e converte o total em custo mensal a ser consumido pela dragagem.

### Itens

- containers;
- fretes;
- PPRA, PCMSO e LTCAT;
- ARTs;
- placa de obra;
- vigilância;
- água potável;
- material de escritório;
- banheiro químico;
- exames médicos;
- integração.

### Regras

- prazo-base: `ROUNDUP(Produção!D24,0) + 1` para alguns itens;
- vigilância: quantidade igual ao prazo-base;
- água potável: `4 × 4 × 6 = 96` galões;
- equipe de integração: dois dias;
- total da composição: R$ 37.587,12;
- prazo de operação usado no divisor: `ROUNDUP(Produção!D24,0)` = 3 meses;
- preço mensal: R$ 12.529,04.

### Anomalias

- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** `D15` e `D24` exibem `#NAME?` no valor armazenado/importado, embora contenham fórmula de arredondamento do prazo.
- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** `F29`, denominado `Prazo de Operação`, também exibe `#NAME?` no arquivo importado, apesar de a fórmula apontar para o prazo arredondado.
- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** o preço final R$ 12.529,04 corresponde ao total dividido por três, indicando que o arquivo preserva resultado numérico em `F31` mesmo com erro exibido em célula intermediária.
- **EVIDÊNCIA CONFIRMADA —** container sanitário/vestiário e banheiro químico estão zerados.
- **DÚVIDA —** alguns itens usam prazo + 1 e o rateio mensal usa apenas prazo arredondado; a motivação não é explicitada.

## 5.10 `6. Operação Sistema`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** calcula custo total e mensal do sistema de preparo/injeção de polímero.

### Equipe

- 1 operador do sistema;
- 2 ajudantes;
- 3 refeições;
- 3 transportes;
- custo diário: R$ 1.017,78.

### Itens e regras

- equipamento de preparo/injeção: R$ 45.000,00;
- polímero: 2.200 kg a R$ 25/kg;
- fretes de polímero: três unidades a R$ 4.000,00;
- água por caminhão-pipa: zerada, anotação SAAE;
- gerador e diesel: três meses a R$ 9.044,00;
- instalações hidráulicas;
- máquina WAP;
- mão de obra de operação: 90 dias.

Consumo de polímero:

```text
tonelada seca dos bags × 5 kg/t × 1,10
400 × 5 × 1,10 = 2.200 kg
```

Mão de obra:

```text
prazo arredondado × 30 dias × custo diário
3 × 30 × R$ 1.017,78
```

Resultado:

- total: R$ 233.732,20;
- prazo: 3 meses;
- custo mensal: R$ 77.910,7333.

### Observações e anomalias

- **EVIDÊNCIA CONFIRMADA —** comentário do polímero informa pagamento de R$ 17/kg em Curitiba, enquanto o preço utilizado é R$ 25/kg.
- **EVIDÊNCIA CONFIRMADA —** comentário de frete registra `1500 em cada`, enquanto o preço usado é R$ 4.000 por unidade.
- **EVIDÊNCIA CONFIRMADA —** linha de gerador contém observações `SAAE` e `Gordura`, sem explicação adicional.
- **EVIDÊNCIA PARCIAL —** o fator 1,10 aparenta margem de consumo/perda.
- **DÚVIDA —** não está claro se o equipamento de R$ 45.000 é compra, locação, depreciação ou verba global.
- **DÚVIDA —** a divergência entre preços anotados e adotados não é explicada.

## 5.11 `7. Dragagem`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** é a maior composição do arquivo e calcula o custo mensal da dragagem, reunindo operação, pessoal, manutenção, apoio, administrativas, BDI e financeiras.

### Bloco I — Operação

Entradas principais:

- quantidade de horas/mês ligada a `Produção!H6`, mas exibida como `#NAME?` no valor importado;
- eficiência: 90%;
- consumo: 2;
- valor de combustível: R$ 7,00.

Custos:

- combustível: R$ 2.494,80;
- filtros/lubrificantes: R$ 600,00;
- fretes/carretos: R$ 1.000,00;
- segurança/uniformes: R$ 400,00;
- total: R$ 4.494,80.

**ANOMALIA / EVIDÊNCIA CONFIRMADA —** o texto `Combustível 0,15 x HP x hora` não corresponde diretamente à fórmula visível `C9 × D9 × E9 × F9`.

### Bloco II — Pessoal

Quadro de salários:

- operador líder: 1 × R$ 31/h;
- operador de draga: 1 × R$ 26,71/h;
- ajudante: 1 × R$ 10,75/h;
- funções opcionais zeradas: engenheiro, ajudante booster, motorista, operador booster e administrativo.

Horas mensais calculadas: 219,9999 h por função ativa.

A aba possui memorial de horas:

- horas extras 70%;
- horas extras 100%;
- horas normais;
- total a receber = A × 1,70 + B × 2 + C.

No cenário preenchido, extras são zero e horas normais são 7,33333 × 30 = 219,9999.

Resultados:

- salários: R$ 15.061,193154;
- encargos sociais: 100% dos salários, R$ 15.061,193154;
- cantina: R$ 6.730,00;
- alojamento: R$ 2.750,00;
- viagens nas folgas: R$ 500,00;
- prêmios de produção: zerados;
- total do grupo de pessoal consolidado em `G87`: R$ 40.102,386308.

### Cantina

Memorial:

- três funcionários alojados;
- um funcionário da cidade;
- preços unitários efetivos usados no memorial: café R$ 15, almoço R$ 25, jantar R$ 25;
- 30 dias para alojados e 22 dias para funcionário da cidade.

**ANOMALIA / EVIDÊNCIA CONFIRMADA —** as linhas descritivas acima exibem valores R$ 10/R$ 2,50/R$ 2,50/R$ 10, que não são os mesmos valores usados no memorial de refeições.

### Alojamento

- aluguel: R$ 2.500;
- água e luz: R$ 150;
- limpeza: R$ 100;
- total: R$ 2.750.

### Bloco III — Manutenção

- peças e acessórios: 0,6% ao mês sobre equipamento de R$ 500.000 → R$ 3.000;
- docagem anual apropriada: 1% ao mês sobre R$ 500.000 → R$ 5.000;
- limpeza e pintura: R$ 250;
- mão de obra de terceiros: R$ 250;
- total: R$ 8.500.

### Bloco IV — Equipamentos de apoio

Custos mensais visíveis:

- linha de recalque: R$ 8.544,6667;
- rebocador/cábrea: zero;
- pick-up: zero;
- automóvel + combustível: R$ 4.000;
- ferramentas: R$ 150;
- canteiro: R$ 12.529,04;
- total: R$ 25.223,7067.

#### Memorial da linha de recalque

Tubulação:

- 500 m × R$ 150/m = R$ 75.000;
- depreciação em 12 meses = R$ 6.250/mês;
- juros de 1% = R$ 750;
- subtotal = R$ 7.000/mês.

Flutuantes:

- 50 peças × R$ 200 = R$ 10.000;
- depreciação em 12 meses = R$ 833,3333;
- juros de 1% = R$ 100;
- subtotal = R$ 933,3333.

Acoplamentos:

- 43,6667 peças × R$ 150 = R$ 6.550;
- depreciação em 12 meses = R$ 545,8333;
- juros de 1% = R$ 65,50;
- subtotal = R$ 611,3333.

Total mensal da linha: R$ 8.544,6667.

**EVIDÊNCIA CONFIRMADA —** quantidade de acoplamentos é fracionária.

### Bloco V — Administrativas

- comissões: zero;
- viagens de inspeção: R$ 2.500;
- viagens administrativas: zero;
- comunicações: R$ 300;
- seguro/licenciamento: vazio;
- total: R$ 2.800.

### Despesas diretas

```text
operação + pessoal + manutenção + equipamentos de apoio + administrativas
= R$ 81.120,8929746667/mês
```

### Bloco VI — BDI interno mensal

- oficina: 5% das despesas diretas;
- administração: 5% das despesas diretas;
- outros: vazio;
- total: R$ 8.112,0892974667.

### Bloco VII — Financeiras

- depreciação: equipamento ÷ 60 meses = R$ 8.333,3333;
- juros de capital: 1% do equipamento = R$ 5.000;
- atrasos: 0,5% das despesas diretas = R$ 405,6045;
- total: R$ 13.738,9377982067.

### Resumo mensal

- despesas diretas: R$ 81.120,8929746667;
- BDI interno: R$ 8.112,0892974667;
- financeiras: R$ 13.738,9377982067;
- custo mensal da dragagem: R$ 102.971,92007034.

### Hora à disposição

- custo/hora à disposição: R$ 906,2403645;
- memorial de dias e horas apresenta `#NAME?` em células de entrada, mantendo total 198 h.

### Consolidação dragagem + operação dos bags

- custo mensal dragagem: R$ 102.971,92007034;
- custo mensal operação polímero: R$ 77.910,7333333333;
- custo mensal total: R$ 180.882,6534036733;
- tempo de operação: célula exibe `#NAME?`, mas o custo total corresponde a três meses;
- custo total: R$ 542.647,96021102.

### Formação auxiliar de preço/hora

- custo mensal: R$ 180.882,6534;
- multiplicador/BDI: 1,6;
- preço de venda mensal: R$ 289.412,2454;
- horas trabalhadas/mês: célula exibe `#NAME?`;
- eficiência: 0,6;
- horas produtivas: 118,8;
- preço/hora: R$ 2.436,1300.

### Anomalias e dúvidas da aba

- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** múltiplas células exibem `#NAME?`: horas mensais, produção prevista, prazo e horas trabalhadas.
- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** o resumo contém campos de custo unitário e preço de venda por m³ incompletos/zerados.
- **EVIDÊNCIA CONFIRMADA —** o custo total de três meses está numericamente formado apesar do erro exibido na célula de prazo.
- **EVIDÊNCIA CONFIRMADA —** BDI aparece em dois contextos: 10% interno no custo mensal e multiplicador 1,6 na formação auxiliar de preço.
- **DÚVIDA —** não está explícito se o multiplicador 1,6 equivale a BDI de 60% ou a outro fator comercial.
- **DÚVIDA —** a origem do fator `0,62` usado em `D234 = J253 × 0,6 × 0,62` não está identificada.
- **DÚVIDA —** não é possível confirmar o papel final das células auxiliares `D225`, `D231` e `D234`, pois não alimentam claramente a planilha final.
- **EVIDÊNCIA PARCIAL —** a aba mistura modelo histórico detalhado de custo mensal com um bloco mais novo de consolidação do sistema de bags.

## 5.12 `8. Desmob. Draga`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** compõe desmobilização da draga.

### Diferenças em relação à mobilização

- leis sociais: 132%, contra 100% na mobilização;
- refeições: R$ 35, contra R$ 40;
- mão de obra: três dias;
- duas carretas de carga seca;
- custo diário: R$ 2.975,5296.

### Resultado

- total/preço final: R$ 41.426,5888;
- BDI interno: 0%.

### Anomalia de consolidação

**ANOMALIA / EVIDÊNCIA CONFIRMADA —** `12. Plan. Preços` não usa este resultado. A consolidação define o custo da desmobilização da draga como `C10 = C4`, repetindo a mobilização de R$ 56.574,24. Portanto, o valor detalhado desta aba não chega ao preço final.

## 5.13 `9. Desmob. Eq. Polimero`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** compõe desmontagem e transporte do sistema de polímero.

### Conteúdo

- equipe com leis sociais de 132%;
- refeições a R$ 30;
- transporte;
- piso, tenda, instalações e WAP como opções zeradas;
- frete: R$ 12.500;
- três dias de mão de obra.

### Resultado

- custo diário: R$ 2.253,2496;
- total/preço final: R$ 19.259,7488;
- BDI interno: 0%.

### Anomalia de consolidação

**ANOMALIA / EVIDÊNCIA CONFIRMADA —** `12. Plan. Preços` define `C11 = C5 × 0,7`, resultando em R$ 24.393,544, e não referencia esta aba. Assim, o valor detalhado de R$ 19.259,7488 não é utilizado no total final.

## 5.14 `10. Mediçao`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** compõe serviços de medição e acompanhamento.

### Conteúdo

- batimetria: quantidade/preço vazios e total zero, anotação `Estimativa`;
- laboratório: 20 unidades × R$ 60 = R$ 1.200;
- acompanhamento FOS: quatro dias × R$ 2.573,56 = R$ 10.294,24.

### Resultado

- total/preço final principal: R$ 11.494,24;
- BDI interno: 0%.

### Anomalias

- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** o título interno diz `8 - Medição`, apesar do nome da aba ser `10. Mediçao`.
- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** há um segundo bloco de BDI/preço final nas linhas 22–23, zerado e sem subtotal correspondente.
- **EVIDÊNCIA CONFIRMADA —** a jornada da primeira função não é vinculada por fórmula a `Dados Obra`, enquanto as demais fórmulas replicam valores locais.

## 5.15 `12. Plan. Preços`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA —** consolida custo total, quantidade, unidade, custo unitário, BDI, preço unitário e preço total.

### Itens consolidados

| Item | Descrição | Custo | Quantidade | BDI | Preço total |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | Mobilização e montagem da draga | R$ 56.574,24 | 1 un | 75% | R$ 99.004,92 |
| 2 | Mobilização sistema polímero e barrilete | R$ 34.847,92 | 1 un | 75% | R$ 60.983,86 |
| 3 | Preparo de célula | R$ 0,00 | 1.800 m² | 75% | R$ 0,00 |
| 4 | Fornecimento de quatro bags 8 × 30 | R$ 146.443,56 | 4 un | 60% | R$ 234.309,696 |
| 5 | Dragagem e desaguamento | R$ 542.647,96021102 | 400 t base seca | 80% | R$ 976.766,3283798359 |
| 7 | Medição | R$ 11.494,24 | 1 un | 60% | R$ 18.390,784 |
| 8 | Desmobilização da draga | R$ 56.574,24 | 1 un | 75% | R$ 99.004,92 |
| 9 | Desmobilização do sistema de polímero | R$ 24.393,544 | 1 un | 75% | R$ 42.688,702 |

### Totais

- custo total consolidado: R$ 872.975,7042110199;
- preço de venda total: R$ 1.531.149,210379836;
- preço médio sobre volume dragado: R$ 245,89336167596718/m³;
- subtotal mobilizações: R$ 159.988,78;
- subtotal execução/medição: R$ 1.229.466,808379836;
- subtotal desmobilizações: R$ 141.693,622.

### Fórmulas e regras

- custo unitário = custo total ÷ quantidade;
- preço unitário = custo unitário × (1 + BDI%);
- preço total = quantidade × preço unitário;
- custo total geral = soma dos custos;
- preço de venda = soma dos preços totais;
- preço por m³ = subtotal de execução/medição ÷ volume de dragagem.

### Lacunas e anomalias

- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** item 6 não existe.
- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** fórmulas de custo unitário e preço de venda não estão presentes em todas as linhas. Algumas células possuem valores armazenados sem fórmula observável.
- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** desmobilização da draga repete o custo da mobilização e ignora `8. Desmob. Draga`.
- **ANOMALIA / EVIDÊNCIA CONFIRMADA —** desmobilização do polímero é calculada como 70% da mobilização e ignora `9. Desmob. Eq. Polimero`.
- **EVIDÊNCIA CONFIRMADA —** o preço médio de R$ 245,893/m³ é calculado somente sobre itens de execução/medição (`J6:J9`), excluindo mobilização e desmobilização.
- **DÚVIDA —** não está explícito por que o preço médio por m³ exclui os eventos de mobilização/desmobilização.
- **DÚVIDA —** não existe aba comercial simplificada final; esta parece ser a única consolidação de apresentação.

---

## 6. Dependências entre abas

```text
Dados Obra
├── Produção
│   ├── 5. Canteiro de obras
│   ├── 7. Dragagem
│   └── prazo usado por 6. Operação Sistema
├── 1. Mob. Draga
├── Barrilete
│   └── 2. Mob. Eq. Polimero
├── 3. Prep. Célula
│   └── 12. Plan. Preços
└── 4. Forn. Bag
    ├── 6. Operação Sistema
    └── 12. Plan. Preços

5. Canteiro de obras
└── 7. Dragagem

6. Operação Sistema
└── 7. Dragagem

7. Dragagem
└── 12. Plan. Preços

1. Mob. Draga
└── 12. Plan. Preços

2. Mob. Eq. Polimero
└── 12. Plan. Preços

10. Mediçao
└── 12. Plan. Preços
```

### Dependências não consumidas pela consolidação

- **EVIDÊNCIA CONFIRMADA —** `8. Desmob. Draga` calcula preço próprio, mas a planilha final repete a mobilização.
- **EVIDÊNCIA CONFIRMADA —** `9. Desmob. Eq. Polimero` calcula preço próprio, mas a planilha final usa 70% da mobilização.
- **EVIDÊNCIA CONFIRMADA —** a aba `Orçamentos` não é referenciada por fórmula.
- **EVIDÊNCIA CONFIRMADA —** vários memoriais auxiliares da aba `7. Dragagem` não possuem saída claramente consumida na consolidação.

## 7. Entidades conceituais encontradas

Todas abaixo são **EVIDÊNCIAS PARCIAIS**, pois foram identificadas neste único orçamento:

- proposta;
- cliente;
- contato;
- obra/local;
- objeto;
- material dragado;
- volume;
- linha de recalque;
- jornada/calendário;
- equipamento principal;
- equipe/função;
- salário horário;
- leis sociais;
- refeição;
- transporte;
- recurso/insumo;
- fornecedor/cotação;
- mobilização;
- desmobilização;
- barrilete;
- sistema de polímero;
- célula de recebimento;
- manta PEAD;
- Bidim;
- brita;
- bag/modelo/capacidade;
- concentração de sólidos;
- tonelada seca;
- consumo de polímero;
- canteiro;
- custo mensal;
- custo de evento único;
- depreciação;
- juros;
- despesas diretas;
- BDI;
- preço de venda;
- medição;
- responsabilidade da contratante/contratada.

## 8. Regras de negócio observadas

### Produção e prazo

- **EVIDÊNCIA CONFIRMADA —** produção horária = vazão × eficiência × concentração.
- **EVIDÊNCIA CONFIRMADA —** produção mensal = produção horária × horas/dia × dias/mês.
- **EVIDÊNCIA CONFIRMADA —** prazo teórico = volume ÷ produção mensal.
- **EVIDÊNCIA CONFIRMADA —** vários custos usam prazo arredondado para cima.

### Mão de obra

- **EVIDÊNCIA CONFIRMADA —** custo de salário diário/mensal usa quantidade × valor horário × horas × (1 + leis sociais).
- **EVIDÊNCIA CONFIRMADA —** refeições e transporte usam quantidade de pessoas × valor unitário.
- **EVIDÊNCIA CONFIRMADA —** mobilização usa leis sociais de 100%; desmobilização usa 132%.
- **DÚVIDA —** não está documentada a razão da diferença de 100% para 132%.

### Bags e polímero

- **EVIDÊNCIA CONFIRMADA —** tonelada seca = volume dragado × percentual de sólidos in situ.
- **EVIDÊNCIA CONFIRMADA —** volume desaguado = tonelada seca ÷ percentual de sólidos após desaguamento.
- **EVIDÊNCIA CONFIRMADA —** seleção de bags deve oferecer capacidade total igual ou superior ao volume desaguado.
- **EVIDÊNCIA CONFIRMADA —** polímero = tonelada seca × 5 kg/t × 1,10.
- **EVIDÊNCIA PARCIAL —** os coeficientes pertencem a este orçamento até crosscheck.

### Apropriação de ativos e infraestrutura

- **EVIDÊNCIA CONFIRMADA —** barrilete é apropriado por 25% do valor integral.
- **EVIDÊNCIA CONFIRMADA —** linha de recalque é apropriada por depreciação em 12 meses mais juros de 1%.
- **EVIDÊNCIA CONFIRMADA —** equipamento principal é depreciado em 60 meses e recebe juros de capital de 1%.
- **EVIDÊNCIA CONFIRMADA —** canteiro é totalizado e depois rateado pelo prazo arredondado.

### Preço de venda

- **EVIDÊNCIA CONFIRMADA —** BDI varia por item: 60%, 75% ou 80%.
- **EVIDÊNCIA CONFIRMADA —** preço unitário = custo unitário × (1 + BDI).
- **EVIDÊNCIA CONFIRMADA —** preço médio por m³ apresentado exclui mobilizações e desmobilizações.
- **EVIDÊNCIA PARCIAL —** os percentuais de BDI parecem escolhidos por família de serviço, mas a regra não está explicitada.

## 9. Terminologia observada

- bag / geobag;
- bota-fora;
- linha flutuante;
- linha de terra;
- seio da linha;
- barrilete;
- célula;
- PEAD;
- Bidim;
- base seca / tonelada seca;
- sólidos in situ;
- sólidos desaguados;
- polímero;
- draguista / operador de draga;
- booster;
- hora à disposição;
- leis sociais;
- cantina;
- custos diretos;
- BDI;
- financeiras;
- mobilização/desmobilização;
- preço unitário de serviço;
- acompanhamento FOS.

## 10. Padrões internos observados neste arquivo

- **EVIDÊNCIA PARCIAL —** composições de eventos usam bloco de equipe no topo e tabela de recursos abaixo.
- **EVIDÊNCIA PARCIAL —** custos intermediários possuem linha de BDI interno, frequentemente zerada, antes da aplicação do BDI comercial na planilha final.
- **EVIDÊNCIA PARCIAL —** itens opcionais são preservados com quantidade vazia e total zero.
- **EVIDÊNCIA PARCIAL —** responsabilidades de terceiros podem manter o memorial técnico e zerar somente a apropriação financeira.
- **EVIDÊNCIA PARCIAL —** o arquivo combina valores cotados, preços anotados, preços efetivamente usados e fatores de apropriação sem separar formalmente suas naturezas.
- **EVIDÊNCIA PARCIAL —** resultados de um pacote podem alimentar outro pacote, formando rede e não somente sequência de abas.

## 11. Exceções e anomalias consolidadas

1. **EVIDÊNCIA CONFIRMADA —** divergência `SAAE` × `DAAE` na identificação do cliente.
2. **EVIDÊNCIA CONFIRMADA —** referências exibidas como `'Dados Obra '` com espaço final.
3. **EVIDÊNCIA CONFIRMADA —** múltiplas células com `#NAME?`.
4. **EVIDÊNCIA CONFIRMADA —** preparo da célula possui custos calculados, mas total zero por responsabilidade SAAE.
5. **EVIDÊNCIA CONFIRMADA —** memorial de brita 306 m³ versus composição 351,9 m³.
6. **EVIDÊNCIA CONFIRMADA —** textos de refeição em `7. Dragagem` divergem dos valores usados no memorial.
7. **EVIDÊNCIA CONFIRMADA —** texto da fórmula de combustível diverge da fórmula visível.
8. **EVIDÊNCIA CONFIRMADA —** acoplamentos calculados em quantidade fracionária.
9. **EVIDÊNCIA CONFIRMADA —** desmobilizações detalhadas são ignoradas pela consolidação.
10. **EVIDÊNCIA CONFIRMADA —** numeração de itens/abas possui lacunas e duplicidade de título.
11. **EVIDÊNCIA CONFIRMADA —** segundo bloco de BDI/preço em `10. Mediçao` está zerado.
12. **EVIDÊNCIA CONFIRMADA —** cotações/anotações mostram preços diferentes dos preços adotados.
13. **EVIDÊNCIA CONFIRMADA —** alguns resultados numéricos permanecem coerentes mesmo quando células intermediárias exibem erro.
14. **DÚVIDA —** não é possível distinguir quais erros são originários da planilha e quais podem depender do mecanismo de cálculo/importação sem abertura no Excel com recálculo controlado.

## 12. Dúvidas para validação futura pelo especialista

1. O cliente correto é SAAE ou DAAE?
2. O orçamento foi uma proposta efetiva ou somente base de concorrência?
3. O multiplicador 1,4 do barrilete representa qual regra?
4. Por que 25% de depreciação do barrilete?
5. Por que a brita recebe 15% adicional?
6. As capacidades de 440/880 m³ dos bags são nominais ou efetivas?
7. O consumo de polímero de 5 kg/t e a margem de 10% vieram de teste, histórico ou fornecedor?
8. Por que o preço do polímero usado é R$ 25/kg quando a anotação registra R$ 17/kg?
9. Por que o frete usado é R$ 4.000 quando a anotação registra R$ 1.500?
10. Água e gerador são responsabilidade do SAAE ou apenas a água?
11. Por que mobilização usa 100% de leis sociais e desmobilização usa 132%?
12. Por que itens do canteiro usam prazo + 1, mas o rateio usa prazo sem o mês adicional?
13. O BDI interno de 10% da dragagem é custo indireto, margem ou ambos?
14. O multiplicador 1,6 da aba Dragagem é equivalente a BDI de 60%?
15. Qual a origem do fator 0,62?
16. Por que a consolidação ignora os valores detalhados das duas desmobilizações?
17. O preço médio por m³ deve excluir mobilização e desmobilização?
18. Qual o papel pretendido dos campos de custo unitário e preço por m³ que estão incompletos?
19. Os `#NAME?` já existiam no arquivo original ou aparecem após recálculo em determinado software?
20. A célula de 1.800 m² corresponde a uma lagoa, às duas ou a uma área parcial?

## 13. Conhecimentos específicos, reutilizáveis e inéditos

### Conhecimentos específicos deste orçamento

- **EVIDÊNCIA CONFIRMADA —** 5.000 m³ de lodo de ETE.
- **EVIDÊNCIA CONFIRMADA —** 8% de sólidos in situ e 25% após desaguamento.
- **EVIDÊNCIA CONFIRMADA —** quatro bags 8 × 30.
- **EVIDÊNCIA CONFIRMADA —** 500 m de recalque.
- **EVIDÊNCIA CONFIRMADA —** área de célula de 1.800 m².
- **EVIDÊNCIA CONFIRMADA —** operação em 9 h/dia, 22 dias/mês.
- **EVIDÊNCIA CONFIRMADA —** consumo de polímero de 5 kg/t com adicional de 10%.

### Candidatos a conhecimento reutilizável

Todos são **EVIDÊNCIAS PARCIAIS**:

- estrutura de cálculo produção → prazo → custos mensais;
- separação entre mobilização, operação e desmobilização;
- memorial de capacidade dos bags;
- operação de polímero baseada em tonelada seca;
- apropriação mensal de ativos e linha de recalque;
- preservação de itens opcionais zerados;
- responsabilidade de terceiros zerando preço sem apagar memorial;
- BDI comercial por família de item.

### Conceitos possivelmente inéditos em relação à documentação já existente, sem consolidação

- **EVIDÊNCIA PARCIAL —** preparo da célula integralmente de responsabilidade do cliente, mantendo memorial técnico.
- **EVIDÊNCIA PARCIAL —** consolidação deliberada ou residual que substitui desmobilização detalhada por proporção da mobilização.
- **EVIDÊNCIA PARCIAL —** preço médio de execução por m³ calculado sem mobilização/desmobilização.
- **EVIDÊNCIA PARCIAL —** uso conjunto de 8% in situ e 25% desaguado para dimensionar bags.

Nenhum destes pontos é promovido a padrão FOS neste documento.

## 14. Limitações da análise

- **EVIDÊNCIA CONFIRMADA —** o arquivo foi analisado por leitura estrutural do `.xlsx`, incluindo valores armazenados, fórmulas e relações entre células.
- **LIMITAÇÃO —** não foi executado recálculo no Microsoft Excel; portanto, células `#NAME?` foram registradas como aparecem na leitura do arquivo.
- **LIMITAÇÃO —** elementos puramente visuais, comentários de célula não expostos pela leitura e histórico de edições podem não estar disponíveis.
- **LIMITAÇÃO —** não foi realizada comparação com outros orçamentos para consolidar padrões.
- **LIMITAÇÃO —** nenhuma informação externa foi usada para corrigir ou completar o Excel.
- **LIMITAÇÃO —** nenhuma decisão arquitetural foi tomada.

## 15. Validação final

- [x] Todas as 15 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Identificação, fluxo, entidades, regras, fórmulas, dependências, exceções, terminologia e dúvidas preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma consolidação entre orçamentos realizada.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma funcionalidade criada.
- [x] Nenhum documento de outro orçamento alterado.
- [x] Nenhum índice geral alterado.
