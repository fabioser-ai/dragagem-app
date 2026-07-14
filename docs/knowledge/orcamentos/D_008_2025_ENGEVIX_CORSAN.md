# D_008_2025 - ENGEVIX - Corsan.xlsx — Registro de Descoberta Independente

## Status da análise

- **Status:** engenharia reversa vertical concluída.
- **Data da análise:** 14/07/2026.
- **Arquivo analisado:** `D_008_2025 - ENGEVIX - Corsan.xlsx`.
- **Versão identificável:** código interno `Proposta D_008_2025`; nenhuma revisão ou versão adicional foi declarada no nome ou nas células examinadas.
- **Data registrada no orçamento:** 19/02/2025.
- **Quantidade de abas:** 15.
- **Escopo:** todas as abas, células preenchidas, fórmulas, dependências, tabelas auxiliares, observações e anomalias foram examinadas.
- **Limitação:** os resultados calculados foram lidos do próprio arquivo. O mecanismo de inspeção utilizado não recalculou algumas funções do Excel, exibindo `#NAME?` para `ROUNDUP`; a fórmula armazenada é válida e os valores dependentes existentes no arquivo indicam prazo arredondado de 3 meses.
- **Proibição respeitada:** nenhuma funcionalidade, arquitetura, banco de dados, tela, consolidação ou alteração de outro documento foi realizada.

## Identidade permanente da fonte

- **Nome integral:** `D_008_2025 - ENGEVIX - Corsan.xlsx`.
- **Proposta:** `Proposta D_008_2025`.
- **Cliente:** `Engevix - Corsan`.
- **Objeto:** `Dragagem ETE ANA TERRA`.
- **Local:** `CRUZ ALTA (RS)`.
- **Volume de dragagem:** 7.505 m³.
- **Material:** `ESGOTO`.
- **Bota-fora:** `Bag`.
- **Responsabilidade por canteiro:** FOS.
- **Responsabilidade por mobilização:** FOS.
- **Jornada:** 9 h/dia, 22 dias/mês.
- **Sistema de medição registrado:** `M3 ( Batimetria) NAO IREMOS ACEITAR - PROPOR preço por M3 base seca`.

## Regra de classificação das evidências

| Classificação solicitada | Aplicação neste documento |
| --- | --- |
| **EVIDÊNCIA CONFIRMADA** | Informação diretamente observada no Excel, incluindo fórmulas, textos, valores, vínculos e anomalias existentes. |
| **EVIDÊNCIA PARCIAL** | Interpretação operacional baseada exclusivamente neste orçamento; confiança Nível C. |
| **DÚVIDA** | Informação sem comprovação suficiente, ambiguidade ou possível resíduo não explicado. |

As afirmações reutilizáveis permanecem com **confiança Nível C**, pois foram observadas em uma única fonte e não foram consolidadas.

## Classificação aparente do orçamento

### EVIDÊNCIA CONFIRMADA

O arquivo representa uma proposta de **dragagem de lodo/esgoto em ETE, com desaguamento e acondicionamento em geobags, sistema de preparo e injeção de polímero e preparo de célula com manta PEAD, geotêxtil e brita**.

O processo orçado inclui:

1. mobilização da draga;
2. mobilização e montagem do equipamento de polímero e barrilete;
3. implantação e custeio do canteiro;
4. preparo de célula;
5. fornecimento e instalação de bags;
6. operação do sistema de desidratação;
7. dragagem;
8. medição e acompanhamento;
9. desmobilização da draga;
10. desmobilização do equipamento de polímero;
11. consolidação de custos e preços de venda.

### EVIDÊNCIA PARCIAL

Este orçamento aparenta ser estruturado para venda com dois grandes blocos comerciais:

- mobilizações, medição e desmobilizações cobradas como itens globais;
- núcleo técnico de preparo de célula, bags e dragagem/operação, precificado com referência à tonelada ou ao metro cúbico de base seca.

A planilha usa a tonelada seca calculada como quantidade comercial da dragagem e operação (`450,3`), embora algumas legendas usem `m3`. A unidade comercial efetiva precisa de validação.

## Características distintivas observadas

### EVIDÊNCIA CONFIRMADA

- A medição inicialmente descrita por batimetria é rejeitada no próprio campo de premissa, com orientação para propor preço por base seca.
- A quantidade seca é calculada como `volume in situ × 6% de sólidos`.
- O volume a acomodar em bags é calculado dividindo a tonelada seca por `22%` de sólidos após desaguamento.
- A seleção usada prevê cinco bags de 8 × 30 m, embora a necessidade matemática seja de aproximadamente 4,45 bags.
- O preparo da célula possui uma composição física explícita por m² de célula.
- A operação de polímero usa dosagem de 4 kg por tonelada seca, acrescida de 10%.
- A planilha comercial aplica BDI de 85% item a item.
- Existem subtotais comerciais paralelos para mobilizações/medição, núcleo técnico e desmobilizações.

---

# Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identificação, premissas técnicas, responsabilidades e jornada. |
| 2 | `Cotaçoes` | Registro auxiliar de fornecedores, contatos e referências de preço. |
| 3 | `Produção` | Produção útil da draga, produção mensal e prazo matemático. |
| 4 | `Barrilete` | Composição física e custo depreciado do barrilete. |
| 5 | `1. Mob. Draga` | Mobilização, transporte, descarga e montagem da draga. |
| 6 | `2. Mob. Eq. Polimero` | Mobilização, cobertura, instalações, barrilete e montagem do sistema de polímero. |
| 7 | `Canteiro` | Implantação e custeio mensal do canteiro. |
| 8 | `3. Prep. Célula` | Dimensionamento físico e custo de preparação da célula. |
| 9 | `4. Forn. Bag` | Dimensionamento, seleção, fornecimento e instalação dos bags. |
| 10 | `5. Operação Sistema` | Equipamento, polímero, utilidades e mão de obra do sistema de desidratação. |
| 11 | `7. Dragagem` | Centro principal de custo mensal e custo total da dragagem + operação dos bags. |
| 12 | `8. Medição` | Amostras, batimetria e acompanhamento de coleta dos bags. |
| 13 | `10. Desmob. Draga` | Desmontagem, carregamento e transporte da draga. |
| 14 | `11. Desmob. Eq. Polimero` | Desmontagem e transporte do equipamento de polímero. |
| 15 | `10. Plan. Preços` | Consolidação de custos, BDI e preços comerciais. |

## Fluxo completo observado

```text
Dados Obra
    ├── Produção ──> prazo matemático
    ├── jornada ──> equipes e custos diários
    └── volume ──> base seca e bags

Cotações ──> referências manuais de preço

Barrilete ──> Mobilização do equipamento de polímero
Mobilização da draga ──> fretes e guindastes reutilizados nas desmobilizações
Produção ──> Canteiro, Operação do Sistema e Dragagem
Preparo de Célula ──> custo e área comercial
Fornecimento de Bag ──> tonelada seca, bags e custo
Operação do Sistema ──> custo mensal
Canteiro ──> custo mensal da dragagem

Dragagem + Operação do Sistema
    ──> custo total pelo prazo arredondado

Mobilizações + Preparo + Bags + Dragagem + Medição + Desmobilizações
    ──> Planilha de Preços
    ──> custo total e preço de venda
```

---

# Análise por aba

## 1. Aba `Dados Obra`

### Objetivo e papel

Registrar a identidade da proposta e as premissas que alimentam produção, equipes, dimensionamento e composições.

### Entradas — EVIDÊNCIA CONFIRMADA

- proposta: `Proposta D_008_2025`;
- data: 19/02/2025;
- cliente: `Engevix - Corsan`;
- contato e e-mail: vazios;
- objeto: `Dragagem ETE ANA TERRA`;
- local: `CRUZ ALTA (RS)`;
- volume: 7.505 m³;
- material: `ESGOTO`;
- distância de recalque: 500 m;
- seio adicional do recalque: 0 m;
- linha flutuante: 300 m;
- seio adicional da linha flutuante: 0 m;
- linha de terra: 200 m;
- profundidade, espessura média e dimensões da área: vazias;
- bota-fora: Bag;
- canteiro: FOS;
- mobilização: FOS;
- jornada: 9 h/dia;
- calendário: 22 dias/mês.

### Fórmulas e saídas — EVIDÊNCIA CONFIRMADA

- `H16 = B16 + E16`: recalque total = 500 m.
- `H17 = B17 + E17`: linha flutuante total = 300 m.
- `G21 = B21 × D21 × B20`: volume geométrico = 0, porque as dimensões e espessura não foram preenchidas.

### Regra explícita relevante

O campo de medição contém: `M3 ( Batimetria) NAO IREMOS ACEITAR - PROPOR preço por M3 base seca`.

### Entidades conceituais

Proposta, cliente, obra, local, material, volume in situ, recalque, linha flutuante, linha terrestre, bota-fora, sistema de medição, responsabilidade, jornada e calendário.

### Dúvidas

- O preço solicitado deve ser por m³ de base seca ou por tonelada seca?
- O volume contratual de 7.505 m³ foi medido por levantamento, estimativa ou dado do cliente?
- A rejeição da batimetria é decisão comercial desta proposta ou condição técnica permanente?
- O contato e e-mail foram intencionalmente omitidos?

## 2. Aba `Cotaçoes`

### Objetivo e papel

Preservar referências auxiliares de mercado usadas ou consideradas nas composições.

### Registros — EVIDÊNCIA CONFIRMADA

**Guindaste**

- Ideal Guindastes;
- contato Gil(a);
- telefone `(13) 3209-9100`;
- guindaste de 50 t;
- R$ 400/h;
- R$ 4.000/dia;
- observação `Sem frete`;
- e-mail registrado.

**Movimentação de material**

- Fox, contato Guilherme;
- escavadeira hidráulica: R$ 2.500/dia;
- caminhão 17 m³: R$ 1.000/dia;
- frete ida e volta: R$ 1.500.

**Brita**

- Engebrita: contatos, sem preço preenchido;
- Rubão/Mercia: brita nº 2 posta em obra a R$ 158/m³;
- contatos adicionais registrados.

**Carreta**

- Lince/Fabiano, sem preço preenchido nesta aba.

**Container**

- seção criada, sem fornecedores ou valores preenchidos.

**Referência web**

- link para reservatório de fibra de 20.000 litros.

### Dependências

Não há fórmulas ligando esta aba às composições. Os preços são transportados manualmente e por observações textuais.

### Anomalias e dúvidas

- Diversas cotações estão incompletas e sem data-base individual.
- Alguns valores usados nas composições diferem dos registros desta aba.
- Não há indicação explícita de proposta formal, validade, impostos, frete ou localização para todos os fornecedores.
- A referência de telefone com DDD 13 e fornecedores de São Paulo pode não refletir a logística de Cruz Alta/RS.

## 3. Aba `Produção`

### Objetivo

Calcular produção útil, produção mensal e prazo matemático.

### Entradas — EVIDÊNCIA CONFIRMADA

- vazão: 130 m³/h;
- eficiência: 65%;
- concentração: 15%;
- jornada: 9 h/dia;
- calendário: 22 dias/mês;
- volume: 7.505 m³.

### Fórmulas — EVIDÊNCIA CONFIRMADA

- horas/mês = `9 × 22 = 198`;
- produção horária = `130 × 65% × 15% = 12,675 m³/h`;
- produção mensal = `12,675 × 198 = 2.509,65 m³/mês`;
- prazo = `7.505 ÷ 2.509,65 = 2,990456837 meses`.

### Dependências

Recebe jornada, calendário e volume de `Dados Obra`. Fornece prazo para `Canteiro`, `5. Operação Sistema` e `7. Dragagem`.

### EVIDÊNCIA PARCIAL

Eficiência e concentração são tratadas como fatores multiplicativos independentes da vazão nominal.

### Dúvidas

- A concentração de 15% representa sólidos volumétricos, concentração de bombeamento ou outro critério?
- A produção resultante é volume in situ, volume de polpa ou volume equivalente seco?
- Existe margem operacional além do arredondamento para 3 meses?

## 4. Aba `Barrilete`

### Objetivo

Compor o conjunto de distribuição hidráulica do sistema de polímero e apropriar apenas uma parcela depreciada ao orçamento.

### Mão de obra diária — EVIDÊNCIA CONFIRMADA

- 2 operadores de draga/técnicos de polímero a R$ 23/h;
- 4 ajudantes a R$ 10/h;
- 110% de leis sociais;
- 6 refeições a R$ 30;
- 6 transportes a R$ 10;
- custo diário: R$ 1.865,40.

### Materiais e serviços

Inclui tubos de ferro de 8", tocos, joelhos, tees, ponteiras, caps, válvulas, mangueira, braçadeiras, curva PVC, bomba lameira e montagem.

### Fórmulas e regras

- vários preços são custo-base × `1,4`;
- total físico: R$ 30.074,80;
- depreciação apropriada: `20% × total = R$ 6.014,96`;
- BDI da aba: 0%;
- preço final transferido: R$ 6.014,96.

### EVIDÊNCIA PARCIAL

A planilha não vende ou apropria o barrilete integralmente; apropria 20% do investimento, sugerindo reutilização em outras obras.

### Dúvidas

- O multiplicador 1,4 é margem de compra, impostos, frete ou atualização?
- A depreciação fixa de 20% corresponde a cinco usos, vida útil estimada ou decisão comercial?
- A mangueira de 200 m está ligada à linha de terra, à água de processo ou ao polímero?

## 5. Aba `1. Mob. Draga`

### Objetivo

Compor carga, transporte, descarga, montagem e apoio inicial da draga de 6".

### Equipe diária

- 1 operador líder;
- 2 operadores de draga;
- 4 ajudantes;
- técnico de segurança com quantidade vazia e custo zero;
- 7 refeições e 7 transportes;
- custo diário: R$ 2.739,338.

### Itens de custo

- guindaste para carregamento: R$ 2.000;
- treinamentos: quantidade vazia, custo zero;
- mobiliário: quantidade vazia, custo zero;
- 3 carretas de carga seca a R$ 18.000: R$ 54.000;
- 2 dias de guindaste na descarga/montagem a R$ 5.500: R$ 11.000;
- frete adicional: zero;
- trator D4: zero;
- 5 dias de mão de obra: R$ 13.696,69.

### Resultado

- total e preço final: R$ 80.696,69;
- BDI interno: 0%;
- observação: `Dois retornos`.

### Dependências

O preço da carreta e do guindaste é reutilizado nas abas de desmobilização; a quantidade de dias usa o custo diário calculado.

### Anomalias e dúvidas

- O guindaste da cotação registra R$ 4.000/dia, mas a composição usa R$ 5.500/dia para descarga e R$ 2.000 para carga.
- A carreta não possui preço na aba `Cotaçoes`, mas usa R$ 18.000.
- `Dois retornos` não está incorporado por fórmula identificável.
- Treinamentos, mobiliário e trator permanecem como itens com custo zero.

## 6. Aba `2. Mob. Eq. Polimero`

### Objetivo

Compor implantação do sistema de preparo/injeção de polímero, cobertura, infraestrutura, barrilete e mão de obra.

### Equipe diária

- 1 operador de polímero;
- 2 operadores líderes;
- 4 ajudantes;
- refeições e transporte para 7 pessoas;
- 110% de leis sociais;
- custo diário: R$ 2.731,519.

### Itens e resultados

- cobertura do equipamento: R$ 7.000;
- munck: R$ 2.000;
- brita para lastro: R$ 240;
- concreto: R$ 2.000;
- frete: R$ 18.000, herdado da carreta da draga;
- instalações hidráulicas: R$ 1.500;
- instalações elétricas: R$ 1.500;
- máquina WAP: 50% de R$ 4.000 = R$ 2.000;
- barrilete: R$ 6.014,96;
- cinco dias de apoio: R$ 13.657,595;
- preço final: R$ 53.912,555;
- observação: `2 mobilizaçoes`.

### Dúvidas

- A observação de duas mobilizações já está refletida nas quantidades ou deveria multiplicar o total?
- Por que são usados dois operadores líderes?
- O frete é realmente igual ao da carreta da draga?
- O barrilete apropriado em 20% é incorporado integralmente nesta mobilização.

## 7. Aba `Canteiro`

### Objetivo

Compor implantação, documentação, utilidades e integração do canteiro e converter o total em custo mensal.

### Prazo

A quantidade dos containers é `ROUNDUP(prazo, 0) + 1`, resultando em 4 meses para uma operação de 3 meses.

### Itens

- três containers: almoxarifado, refeitório e escritório;
- dois fretes;
- PPRA, PCMSO e LTCAT;
- ART principal e corresponsáveis;
- placa de obra;
- vigilância com custo zero;
- água potável: 8 galões por mês de canteiro;
- material de escritório;
- banheiro químico;
- exames médicos para 7 pessoas;
- três dias de integração.

### Resultado

- total de implantação e permanência: R$ 43.728,014;
- prazo de operação: 3 meses;
- custo unitário mensal: R$ 14.576,0047;
- BDI interno: 1%;
- preço mensal final: R$ 14.721,7647.

### Regra implícita — EVIDÊNCIA PARCIAL

O mês adicional dos containers aparenta cobrir mobilização/implantação ou desmobilização além do prazo produtivo.

### Anomalias e dúvidas

- Itens marcados `Orçar` já possuem valores.
- Vigilância permanece sem quantidade e custo.
- O BDI de 1% é específico desta aba e será novamente sucedido por BDI comercial de 85%.
- Não está explicitado por que apenas o custo mensal, e não o total, é incorporado à dragagem.

## 8. Aba `3. Prep. Célula`

### Objetivo

Dimensionar materiais e recursos por área de célula e compor o custo de implantação.

### Dimensionamento físico — EVIDÊNCIA CONFIRMADA

Área-base da célula: 1.116 m².

Coeficientes:

- manta PEAD: 1,196 m² por m² de célula → 1.334,736 m²;
- Bidim: 1,48 m² por m² → 1.651,68 m²;
- brita: 0,10 m³ por m² → 111,6 m³;
- retroescavadeira: 0,023 h por m² → 25,668 h;
- mão de obra: 0,023 h por m² → 25,668 h;
- conversão da mão de obra: 25,668 h ÷ 10 pessoas = 2,5668 dias.

### Composição econômica

- preparo de terreno: R$ 12.000;
- mobilização de patrola: R$ 1.000;
- aluguel de retro: R$ 10.000;
- mobilização/desmobilização da retro: R$ 2.000;
- regularização manual: R$ 13.346,69;
- PEAD: R$ 30.698,928;
- material de empréstimo: quantidade vazia e custo zero;
- instalação do PEAD: R$ 8.008,416;
- mobilização de mão de obra PEAD: R$ 8.500;
- Bidim: R$ 14.865,12;
- brita: quantidade física acrescida em 20%, totalizando 133,92 m³ e R$ 21.159,36;
- retro para espalhamento: R$ 9.000;
- instalação de Bidim e brita: R$ 13.346,69.

### Resultado

- total: R$ 143.925,204;
- quantidade de repetições: 1;
- preço final: R$ 143.925,204.

### Regras e anomalias

- A brita recebe fator de segurança de 20%; PEAD e Bidim usam coeficientes próprios já superiores a 1.
- O cálculo físico de mão de obra produz 2,5668 dias, mas a composição econômica usa 5 dias em duas linhas.
- A área da célula é entrada manual e não é derivada da quantidade de bags.
- O material de empréstimo possui observação histórica, mas não compõe custo.

### Dúvidas

- Como foi definida a área de 1.116 m²?
- Os coeficientes incluem sobreposição, ancoragem, perdas e taludes?
- Por que o cálculo de mão de obra por coeficiente não determina os cinco dias usados?
- As duas linhas de mão de obra representam equipes ou atividades distintas?

## 9. Aba `4. Forn. Bag`

### Objetivo

Converter volume in situ em massa/volume seco, dimensionar bags e compor fornecimento, frete, descarga e instalação.

### Conversão de material — EVIDÊNCIA CONFIRMADA

- volume in situ: 7.505 m³;
- sólidos in situ: 6%;
- tonelada seca: `7.505 × 6% = 450,3`;
- sólidos após desaguamento: 22%;
- volume a acomodar: `450,3 ÷ 22% = 2.046,818 m³`.

### Capacidades de bags registradas

- 6 × 50: 550 m³;
- 8 × 30: 460 m³;
- 8 × 25: 375 m³;
- 6 × 30: 340 m³;
- 8 × 10: 150 m³;
- 8 × 13: 190 m³;
- 8 × 14: 200 m³;
- 8 × 15: 225 m³;
- 8 × 20: 300 m³;
- 6 × 15: 160 m³.

### Seleção

- necessidade matemática para bag 8 × 30: 4,4496 unidades;
- quantidade comercial usada: 5 unidades;
- preço unitário: R$ 35.100;
- fornecimento: R$ 175.500;
- munck: R$ 4.000;
- instalação: 11 dias × R$ 2.669,338 = R$ 29.362,718;
- frete para bags: quantidade vazia e custo zero;
- preço final: R$ 208.862,718.

### Formação de preço dos bags

Há dois métodos coexistentes:

1. preço por capacidade volumétrica (`R$/m³`) em várias dimensões;
2. preço por área de tecido (`R$/m²`) para um bag denominado `P18 x 30`, com 540 m² × R$ 65/m² = R$ 35.100.

O preço de 8 × 30 usado na composição é igual ao resultado do cálculo por área.

### Anomalias

- A nota `Será fornecido pela propria SABESP` é incompatível com cliente Engevix/Corsan e aparenta resíduo de outro orçamento.
- Os quadros laterais citam `ELIAS FAUSTO` e `CABREUVA`, locais não pertencentes à proposta atual.
- Algumas dimensões têm preço calculado, mas quantidade zero.
- O item `Bag 6,00 x 30,00m` usa fórmula dependente de `H15`, célula vazia, resultando em zero.
- O frete dos bags está precificado unitariamente, mas sem quantidade.
- O preço médio exibido em `F30` divide o total por cinco bags.

### Dúvidas

- A unidade `Tonelada Seca` é realmente tonelada, apesar de derivar de m³ × percentual sem densidade explícita?
- O percentual de 6% é massa/massa, volume/volume ou empiricamente tratado como t/m³?
- Os 22% representam teor de sólidos final em massa?
- O bag efetivamente escolhido é 8 × 30 ou 18 × 30, já que o cálculo de área usa `18 × 30`?
- A capacidade de 460 m³ e o preço de R$ 75/m³ são referências técnicas ou comerciais?
- A célula de 1.116 m² suporta os cinco bags e suas áreas de operação?

## 10. Aba `5. Operação Sistema`

### Objetivo

Compor equipamento, polímero, utilidades, instalações e mão de obra da desidratação.

### Dosagem de polímero — EVIDÊNCIA CONFIRMADA

- base seca: 450,3;
- dosagem nominal: 4 kg por tonelada seca;
- acréscimo: 10%;
- quantidade: `450,3 × 4 × 1,1 = 1.981,32 kg`;
- preço-base: R$ 23,40/kg;
- preço com acréscimo de 10%: R$ 25,74/kg;
- custo: R$ 50.999,1768.

### Outros itens

- equipamento de preparo/injeção: R$ 50.000, com nota de estrutura reutilizada da SABESP;
- dois fretes de polímero: R$ 2.000;
- água, energia, tanque, frete de tanque e diesel permanecem com custo zero, acompanhados por notas de fornecimento da Corsan em alguns casos;
- instalações hidráulicas: R$ 2.000;
- máquina WAP: 60% de R$ 6.000 = R$ 3.600;
- mão de obra: 90 dias × R$ 1.185,325 = R$ 106.679,25.

### Resultado

- custo total: R$ 215.278,4268;
- prazo arredondado: 3 meses;
- custo mensal: R$ 71.759,4756.

### Equipe diária

- 1 operador do sistema;
- 3 ajudantes;
- refeições e transporte para 4;
- 110% de leis sociais;
- custo diário: R$ 1.185,325.

### Anomalias e dúvidas

- O equipamento de R$ 50.000 é cobrado mesmo com nota de reutilização de estrutura da SABESP.
- Água, energia e tanques estão zerados, mas não há fórmula de exclusão; dependem de quantidades vazias.
- Diesel permanece como item zerado.
- O acréscimo de 10% é aplicado tanto à quantidade quanto ao preço do polímero, ampliando o custo em 21% sobre quantidade × preço-base.
- A dosagem de 4 kg/t seca precisa ser confirmada para este lodo e polímero.
- A mão de obra usa 30 dias por mês, embora a produção use 22 dias úteis.

## 11. Aba `7. Dragagem`

### Objetivo

Compor o custo mensal da draga, equipe, manutenção, apoio, despesas administrativas, BDI financeiro e somar o custo mensal da operação dos bags/polímero.

### Identificação interna — ANOMALIA CONFIRMADA

A aba contém resíduos históricos:

- `DATA: 28/05/2021`;
- `CLIENTE: REFAP`;
- equipamento `Draga 6" Elétrica`;
- título numérico `5.` apesar do nome da aba ser `7. Dragagem`.

Esses textos não correspondem ao cliente e à data da proposta atual. Os vínculos econômicos, contudo, alimentam a consolidação atual.

### I — Operação

- valor do equipamento: R$ 450.000;
- horas mensais: 198;
- eficiência usada no combustível: 90%;
- consumo/h: 1;
- combustível: R$ 7;
- combustível mensal: R$ 1.247,40;
- filtros/lubrificantes: 10% do combustível;
- fretes e carretos: R$ 2.000;
- segurança/uniformes: R$ 500;
- subtotal: R$ 3.872,14.

### II — Pessoal

Horas remuneradas:

- 11 h extras a 70%;
- 0 h extras a 100%;
- 219,9999 h normais;
- total remunerado: 238,6999 h/mês.

Equipe ativa:

- 1 operador líder a R$ 30/h;
- 1 operador de draga a R$ 26,71/h;
- 1 ajudante a R$ 10,75/h.

Funções cadastradas, porém sem quantidade:

- engenheiro;
- técnico de segurança;
- motorista;
- operador de booster;
- administrativo.

Resultados:

- salários: R$ 16.102,695254;
- encargos: 110% = R$ 17.712,964779;
- refeições: R$ 5.960;
- alojamento: R$ 3.150;
- viagens nas folgas: zero;
- prêmio de produção: sem valores;
- subtotal pessoal agregado: R$ 42.925,660033.

### III — Manutenção

- peças e acessórios: 0,6% ao mês do valor do equipamento = R$ 2.700;
- docagem anual apropriada mensalmente: 1% do valor = R$ 4.500;
- limpeza/pintura: R$ 250;
- terceiros: R$ 250;
- subtotal: R$ 7.700.

### IV — Equipamentos de apoio

Linha de recalque:

- tubulação considerada: 250 m × R$ 150 = R$ 37.500;
- depreciação em 12 meses: R$ 3.125/mês;
- juros: 1% = R$ 375/mês;
- flutuantes: 37,5 peças × R$ 200 = R$ 7.500;
- depreciação: R$ 625/mês;
- juros: R$ 75/mês;
- acoplamentos: `(250/12)+2 = 22,8333` peças × R$ 150 = R$ 3.425;
- depreciação: R$ 285,4167/mês;
- juros: R$ 34,25/mês;
- custo mensal da linha: R$ 4.519,6667.

Outros apoios:

- automóvel: R$ 5.000;
- canteiro: R$ 14.721,7647;
- linhas para batimetria, medidor de vazão/densidade, pick-up, solda, maçarico e ferramentas estão vazias ou zeradas.

Subtotal de apoio usado nas despesas diretas: R$ 24.241,43138.

### V — Administrativas

- viagens de inspeção: R$ 5.000;
- comunicações: R$ 300;
- comissões, viagens administrativas, seguro/licenciamento: zero;
- subtotal: R$ 5.300.

### Despesas diretas e adicionais

- despesas diretas: R$ 84.039,231413;
- oficina: 5% = R$ 4.201,961571;
- administração: 5% = R$ 4.201,961571;
- BDI interno: R$ 8.403,923141;
- depreciação da draga em 60 meses: R$ 7.500;
- juros de capital: 1% = R$ 4.500;
- atrasos: 0,5% das despesas diretas = R$ 420,196157;
- financeiras: R$ 12.420,196157;
- custo mensal da dragagem: R$ 104.863,350712.

### Integração com operação dos bags

- custo mensal da operação dos bags/polímero: R$ 71.759,4756;
- custo mensal conjunto: R$ 176.622,826312;
- prazo arredondado: 3 meses;
- custo total: R$ 529.868,478935.

### Quadro paralelo de preço por hora

- custo mensal: R$ 176.622,826312;
- fator comercial/BDI: 1,6;
- preço de venda mensal: R$ 282.596,522099;
- 198 h/mês;
- eficiência: 60%;
- horas produtivas: 118,8;
- preço por hora produtiva: R$ 2.378,7586;
- valor auxiliar por hora: R$ 1.427,2552;
- valor após fator 0,6: R$ 856,3531;
- hora à disposição: R$ 884,8982, calculada por fórmula diferente.

### Anomalias e dúvidas

- A produção prevista do resumo está fixada em 1.930,5 m³/mês, diferente de 2.509,65 m³/mês da aba `Produção`.
- As células de custo unitário e preço de venda por m³ estão vazias/zeradas.
- A linha de recalque usa 250 m, enquanto `Dados Obra` registra 500 m de recalque total e 300 m flutuante.
- O preço da draga e percentuais de manutenção, docagem, depreciação, juros e atrasos não possuem fonte nesta planilha.
- O automóvel é custo fixo de R$ 5.000, sem composição.
- O custo do canteiro já inclui BDI de 1%.
- O bloco de BDI interno de 10% e o bloco financeiro são incorporados antes do BDI comercial de 85%.
- Eficiência de 90% no combustível, 60% no preço por hora e 65% na produção coexistem com finalidades diferentes.
- A apropriação de horas remuneradas usa 30 dias para horas normais, apesar de 22 dias produtivos.
- A fórmula de hora à disposição não é explicada operacionalmente.

## 12. Aba `8. Medição`

### Objetivo

Compor amostragem, batimetria e acompanhamento FOS.

### Equipe

- 1 operador líder a R$ 14,50/h;
- operador de draga com quantidade vazia;
- 2 ajudantes;
- refeições/transporte para 3;
- 110% de leis sociais;
- custo diário: R$ 800,40.

### Itens

- 40 amostras a R$ 60: R$ 2.400;
- batimetria FOS: preço R$ 12.000, quantidade vazia, custo zero;
- 11 dias de acompanhamento/coleta: R$ 8.804,40.

### Resultado

- preço final: R$ 11.204,40;
- BDI interno: 0%.

### Anomalias

- Existe um segundo bloco de BDI/preço final referindo linha 21 vazia, resultando em zero.
- Batimetria aparece como item zerado apesar de ser citada no sistema de medição rejeitado.
- A quantidade de 11 dias de coleta não deriva de fórmula identificada.

## 13. Aba `10. Desmob. Draga`

### Objetivo

Compor desmontagem, carregamento e transporte da draga.

### Composição

- equipe diária: 2 operadores/técnicos + 4 ajudantes;
- custo diário: R$ 1.398,192;
- 3 carretas a R$ 18.000: R$ 54.000;
- 3 dias de mão de obra: R$ 4.194,576;
- 2 dias de guindaste a R$ 5.500: R$ 11.000;
- frete adicional: zero;
- preço final: R$ 69.194,576.

### Dependências

Reutiliza os preços de carreta e guindaste da mobilização da draga.

### Dúvidas

- Os salários horários são menores que os usados na mobilização e operação.
- O título diz `DESMOBILIZAÇÃO E MONTAGEM`, apesar de a atividade ser desmontagem.
- A verba de cobertura permanece como item zerado.

## 14. Aba `11. Desmob. Eq. Polimero`

### Objetivo

Compor desmontagem e transporte do equipamento de polímero.

### Composição

- mesma equipe diária da desmobilização da draga;
- 1 carreta a R$ 18.000;
- 2 dias de apoio: R$ 2.796,384;
- demais itens de implantação são preservados, mas zerados;
- preço final: R$ 20.796,384.

### Anomalias e dúvidas

- O nome e título mantêm numeração incoerente com o fluxo.
- O barrilete aparece com preço unitário, mas quantidade vazia e custo zero, sugerindo que não é descartado na desmobilização.
- Instalações e WAP permanecem como linhas de custo zero.
- Não há custo de guindaste/munck para desmontagem.

## 15. Aba `10. Plan. Preços`

### Objetivo

Consolidar os custos dos pacotes e aplicar BDI comercial.

### Itens e preços — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Custo | Quantidade | Unidade | BDI | Preço total |
| --- | --- | ---: | ---: | --- | ---: | ---: |
| 1 | Mobilização e montagem da draga | R$ 80.696,69 | 1 | un | 85% | R$ 149.288,8765 |
| 2 | Mobilização do equipamento de polímero e barrilete | R$ 53.912,555 | 1 | un | 85% | R$ 99.738,22675 |
| 3 | Preparo de célula | R$ 143.925,204 | 1.116 | m² | 85% | R$ 266.261,6274 |
| 4 | Fornecimento de bags | R$ 208.862,718 | 1 | un | 85% | R$ 386.396,0283 |
| 6 | Dragagem e operação do sistema de polímero | R$ 529.868,478935 | 450,3 | `m3` | 85% | R$ 980.256,686031 |
| 8 | Medição | R$ 11.204,40 | 1 | un | 85% | R$ 20.728,14 |
| 9 | Desmobilização da draga | R$ 69.194,576 | 1 | un | 85% | R$ 128.009,9656 |
| 10 | Desmobilização do equipamento de polímero | R$ 20.796,384 | 1 | un | 85% | R$ 38.473,3104 |

### Totais

- custo total: R$ 1.118.461,005935;
- preço de venda total: R$ 2.069.152,860981;
- relação preço/custo: 1,85 em todos os itens, coerente com BDI de 85%.

### Subtotais paralelos

- mobilizações + medição: R$ 269.755,24325;
- preparo + bags + dragagem/operação: R$ 1.632.914,341731;
- preço desse núcleo dividido por 450,3: R$ 3.626,2810 por unidade seca;
- desmobilizações: R$ 166.483,276.

### Cálculos auxiliares sem rótulo suficiente

- `J12 ÷ 12.600 = 164,21848`;
- `J12 ÷ 1.625 = 1.273,32484`;
- constante 1.625;
- constante 1.273,3248;
- `J12 ÷ 450,3 = 4.595,0541`.

### Anomalias e dúvidas

- A sequência de itens pula 5 e 7.
- A unidade da dragagem está como `m3`, mas a quantidade de 450,3 vem da célula `Tonelada Seca`.
- Algumas células de custo unitário e preço total foram digitadas como valores, embora correspondam matematicamente às fórmulas padrão.
- Os cálculos auxiliares em M/O não possuem títulos suficientes para interpretação.
- O BDI de 85% incide sobre custos que já incluem BDI interno, encargos, custos financeiros e outros percentuais.
- Não há impostos, retenções, comissão, contingência comercial ou margem explicitamente separados na planilha final.

---

# Dependências entre abas

## EVIDÊNCIA CONFIRMADA

- `Dados Obra` → `Produção`: volume, horas/dia e dias/mês.
- `Dados Obra` → `Barrilete`, mobilizações, preparo de célula, bags, operação e desmobilizações: horas/dia.
- `Dados Obra` → `4. Forn. Bag`: volume in situ.
- `Produção` → `Canteiro`: prazo arredondado + 1 mês.
- `Produção` → `5. Operação Sistema`: prazo arredondado.
- `Produção` → `7. Dragagem`: prazo arredondado.
- `Barrilete` → `2. Mob. Eq. Polimero`: valor depreciado do barrilete.
- `1. Mob. Draga` → `2. Mob. Eq. Polimero`, `10. Desmob. Draga` e `11. Desmob. Eq. Polimero`: preços de carreta e guindaste.
- `Canteiro` → `7. Dragagem`: custo mensal do canteiro.
- `4. Forn. Bag` → `5. Operação Sistema`: tonelada seca.
- `5. Operação Sistema` → `7. Dragagem`: custo mensal de desidratação.
- todas as composições principais → `10. Plan. Preços`: custos e quantidades.

## Dependências manuais

- `Cotaçoes` não possui fórmulas de saída.
- Vários comentários citam fornecedores e locais, mas os valores são transferidos manualmente.
- Coeficientes e preços-base permanecem embutidos em fórmulas ou células das próprias composições.

---

# Entidades conceituais encontradas

### EVIDÊNCIA CONFIRMADA

- proposta e cliente;
- obra e local;
- volume in situ;
- material/lodo/esgoto;
- base seca;
- teor de sólidos inicial e final;
- produção da draga;
- prazo;
- equipamento principal;
- linha de recalque e componentes;
- equipe, função, salário-hora e leis sociais;
- mobilização e desmobilização;
- canteiro;
- célula de desaguamento;
- manta PEAD;
- geotêxtil/Bidim;
- brita;
- geobag;
- capacidade de bag;
- polímero, dosagem e preço;
- equipamento de preparo/injeção;
- utilidades;
- medição, amostra e batimetria;
- custo diário, mensal, global e unitário;
- depreciação;
- juros de capital;
- manutenção;
- BDI interno e BDI comercial;
- fornecedor, cotação e referência;
- preço de custo e preço de venda.

---

# Regras de negócio observadas

## EVIDÊNCIA CONFIRMADA

1. Produção útil = vazão × eficiência × concentração.
2. Prazo matemático = volume ÷ produção mensal.
3. Prazos de custos mensais são arredondados para cima.
4. Containers permanecem um mês além do prazo produtivo.
5. Custo de mão de obra = quantidade × salário-hora × horas/dia × (1 + leis sociais).
6. Refeição e transporte são calculados pela quantidade total de pessoas.
7. Barrilete é apropriado em 20% do custo total.
8. Tonelada seca = volume in situ × 6%.
9. Volume pós-desaguamento = tonelada seca ÷ 22%.
10. Bags são dimensionados pela capacidade volumétrica e arredondados comercialmente.
11. Quantidade de polímero = tonelada seca × 4 kg/t × 1,1.
12. O preço do polímero também recebe fator 1,1.
13. A operação do sistema usa 30 dias por mês.
14. Manutenção e custos financeiros são percentuais do valor da draga ou das despesas diretas.
15. A planilha comercial aplica 85% sobre cada custo unitário.

## EVIDÊNCIA PARCIAL

- A proposta privilegia medição por base seca para reduzir a incerteza da concentração do material bombeado.
- O orçamento apropria investimentos reutilizáveis por depreciação ou fração, mas os critérios não são uniformes.
- O núcleo comercial pode estar sendo apresentado em unidade seca, enquanto mobilizações e apoios ficam separados como verbas globais.
- O sistema de desidratação e a dragagem são tratados como operações acopladas no custo total.

---

# Coeficientes e valores embutidos

## EVIDÊNCIA CONFIRMADA — confiança Nível C

- leis sociais: 110%;
- vazão: 130 m³/h;
- eficiência produtiva: 65%;
- concentração: 15%;
- sólidos in situ: 6%;
- sólidos após desaguamento: 22%;
- polímero: 4 kg/t seca;
- segurança de polímero: 10%;
- preço-base do polímero: R$ 23,40/kg;
- fator de preço do polímero: 1,1;
- PEAD: 1,196 m²/m²;
- Bidim: 1,48 m²/m²;
- brita: 0,1 m³/m² + 20%;
- retro e mão de obra: 0,023 h/m²;
- barrilete: preços-base × 1,4 e apropriação de 20%;
- peças/manutenção: 0,6% ao mês do valor da draga;
- docagem: 1% ao mês;
- oficina: 5%;
- administração: 5%;
- depreciação da draga: 60 meses;
- juros: 1%;
- atrasos: 0,5% das despesas diretas;
- BDI comercial: 85%.

Nenhum desses valores deve ser tratado como padrão geral da FOS sem crosscheck e validação.

---

# Exceções, resíduos e inconsistências preservadas

## EVIDÊNCIA CONFIRMADA

1. `7. Dragagem` contém cliente REFAP e data de 2021.
2. `4. Forn. Bag` menciona SABESP, Elias Fausto e Cabreúva.
3. `5. Operação Sistema` menciona reutilização de estrutura da SABESP.
4. A numeração das abas e dos títulos não é sequencial.
5. A medição por batimetria é rejeitada nas premissas, mas permanece como item de custo.
6. A unidade comercial `m3` é associada à quantidade calculada como tonelada seca.
7. A produção mensal fixa em `7. Dragagem` diverge da aba `Produção`.
8. O comprimento de recalque usado no custo da linha diverge da premissa da obra.
9. Há itens com preço unitário e quantidade vazia, produzindo custo zero.
10. Há itens marcados `Orçar` com valores já preenchidos.
11. Existem subtotais e cálculos auxiliares sem rótulo suficiente.
12. O custo do polímero recebe 10% na quantidade e no preço.
13. Diferentes eficiências são usadas para produção, combustível e preço/hora.
14. Diferentes calendários são usados: 22 dias produtivos e 30 dias para operação/folha.
15. O BDI final incide sobre custos que já contêm percentuais internos.

Nenhuma dessas ocorrências é declarada erro de negócio sem validação do especialista.

---

# Terminologia observada

- **Base seca / tonelada seca:** quantidade derivada do volume in situ e teor de sólidos.
- **Bag / geobag:** unidade de acondicionamento e desaguamento.
- **Célula:** área preparada para instalação e operação dos bags.
- **Barrilete:** conjunto de tubulações, válvulas e derivações do sistema.
- **Seio da linha:** parcela adicional somada à extensão nominal.
- **Linha flutuante / linha de terra:** segmentos do recalque.
- **Operação do sistema:** preparo/injeção de polímero e apoio ao desaguamento.
- **Hora à disposição:** valor horário auxiliar calculado por lógica diferente do preço por hora produtiva.
- **BDI interno:** percentuais incorporados nas composições.
- **BDI comercial:** acréscimo de 85% na planilha final.

---

# Dúvidas consolidadas para validação futura

1. Qual é a unidade contratual correta: m³ in situ, m³ seco ou tonelada seca?
2. Como o teor de sólidos deve ser medido e validado?
3. Os 6% e 22% são valores específicos desta obra?
4. O percentual de sólidos pode ser usado diretamente para converter m³ em toneladas sem densidade?
5. Qual bag foi efetivamente proposto: 8 × 30 ou 18 × 30?
6. A área de célula foi dimensionada para cinco bags?
7. O cliente forneceria água, energia, estrutura do equipamento ou bags?
8. As notas de SABESP/REFAP/Elias Fausto/Cabreúva são apenas resíduos?
9. O equipamento de polímero de R$ 50.000 é aquisição, depreciação, aluguel ou adaptação?
10. Por que o polímero recebe 10% na quantidade e no preço?
11. Por que a operação usa 30 dias e a produção usa 22?
12. Qual comprimento da linha deve ser custeado: 250 m, 500 m ou 500 + 300 m?
13. A produção correta é 2.509,65 ou 1.930,5 m³/mês?
14. O BDI de 85% já contempla todos os impostos, riscos e lucro?
15. Os percentuais internos devem ser acumulados com o BDI comercial?
16. O mês adicional do canteiro é regra de mobilização/desmobilização?
17. A quantidade de 11 dias para instalação/coleta dos bags tem origem técnica?
18. O preço por base seca exclui mobilizações e desmobilizações ou deve incorporar tudo?
19. O subtotal por unidade seca de R$ 3.626,28 e o total por unidade de R$ 4.595,05 têm papéis comerciais distintos?
20. O valor de R$ 1.273,32 vinculado à constante 1.625 representa qual grandeza?

---

# Validação final

- [x] Todas as 15 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Nome integral do arquivo preservado.
- [x] Data, versão identificável, quantidade de abas e status registrados.
- [x] Fórmulas e finalidades operacionais documentadas.
- [x] Dependências entre abas registradas.
- [x] Entidades, regras, terminologia, exceções e dúvidas preservadas.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma consolidação realizada.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhum documento de outro orçamento ou índice geral alterado.
