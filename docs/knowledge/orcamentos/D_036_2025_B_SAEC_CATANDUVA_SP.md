# D_036_2025_B - SAEC - Catanduva- SP.xlsx — Registro independente de descoberta

## Status da análise

- **Arquivo original:** `D_036_2025_B - SAEC - Catanduva- SP.xlsx`
- **Data da análise:** 14/07/2026
- **Versão identificável:** revisão `B`, indicada no nome do arquivo; a proposta interna está registrada como `Proposta D_036_2025`.
- **Quantidade de abas:** 16.
- **Fórmulas identificadas:** 381.
- **Status:** engenharia reversa vertical concluída para o conteúdo acessível do arquivo.
- Todas as abas foram examinadas.
- Nenhum documento de outro orçamento, índice geral, documento de consolidação, arquitetura, banco de dados, tela ou funcionalidade foi alterado ou definido.
- Toda descoberta reutilizável permanece provisória e restrita a esta fonte.

## Limitações da análise

### EVIDÊNCIA CONFIRMADA

- A leitura foi realizada diretamente sobre o arquivo XLSX enviado.
- O analisador conseguiu identificar valores, fórmulas e referências entre abas.
- Três fórmulas com `ROUNDUP(...)` foram apresentadas pelo motor de recálculo da ferramenta como `#NAME?`: `Canteiro!D15`, `5. Operação Sistema!F26` e `7. Dragagem!D247`.
- As fórmulas são legíveis e os valores dependentes preservados no arquivo indicam intenção de arredondar o prazo para cima, mas a ferramenta utilizada não permitiu confirmar se o Excel original as recalcula normalmente.

### DÚVIDA

- Não foi possível distinguir, apenas pela leitura estrutural, se o `#NAME?` é defeito real persistido no arquivo ou limitação do motor de cálculo da ferramenta.
- Não foi possível confirmar a data-base de todos os preços sem documentos externos de cotação.
- O arquivo contém referências textuais e cabeçalhos herdados de outros projetos; não se assume que representem o cliente ou a obra atual.

## Regra de classificação aplicada

| Categoria solicitada | Uso neste documento |
| --- | --- |
| **EVIDÊNCIA CONFIRMADA** | Informação diretamente observada em células, fórmulas, títulos, valores ou relações do Excel. |
| **EVIDÊNCIA PARCIAL** | Interpretação operacional baseada exclusivamente neste orçamento. |
| **DÚVIDA** | Informação incompleta, ambígua, residual ou não comprovável somente pelo arquivo. |

Todas as interpretações e possíveis padrões deste documento possuem confiança equivalente a **Nível C**, pois decorrem de uma única fonte.

# 1. Classificação do orçamento

## EVIDÊNCIA CONFIRMADA

O arquivo representa orçamento para:

- cliente `SAEC`;
- objeto `DRAGAGEM ETE CATANDUVA`;
- local `Catanduva - SP`;
- volume nominal de dragagem de `25.000 m³`;
- material descrito como `ESGOTO`;
- disposição/desaguamento em `Bag`;
- medição em `Base seca`;
- draga elétrica de 6 polegadas indicada na composição principal;
- linha total de recalque de 500 m, sendo 300 m flutuantes e 200 m terrestres;
- preparo de célula com manta PEAD, geotêxtil e brita;
- fornecimento e instalação de geobags;
- preparo e injeção de polímero;
- mobilização, transferência, medição e desmobilização;
- consolidação de custo e preço de venda por pacotes.

## EVIDÊNCIA PARCIAL

A classificação aparente é:

**dragagem de lodo de ETE com desaguamento em geobags, preparo de célula impermeabilizada e tratamento com polímero, medida em base seca.**

Características distintivas observadas neste arquivo:

- separação do preparo da célula e do fornecimento dos bags em pacotes comerciais próprios;
- dimensionamento dos bags pela conversão do volume úmido em tonelada seca e posterior reconversão pela concentração após desaguamento;
- dosagem de polímero sobre tonelada seca;
- custo principal da dragagem calculado mensalmente e multiplicado pelo prazo arredondado;
- BDI comercial uniforme de 85% aplicado na planilha final;
- existência de uma aba de cotações e observações de fornecedores, embora vários preços sejam inseridos diretamente nas composições.

# 2. Identidade e premissas principais

## EVIDÊNCIA CONFIRMADA

| Campo | Valor observado |
| --- | --- |
| Proposta | Proposta D_036_2025 |
| Data interna | 28/05/2025 |
| Cliente | SAEC |
| Objeto | DRAGAGEM ETE CATANDUVA |
| Local | Catanduva - SP |
| Volume | 25.000 m³ |
| Material | ESGOTO |
| Distância total de recalque | 500 m |
| Linha flutuante total | 300 m |
| Linha terrestre | 200 m |
| Bota-fora | Bag |
| Medição | Base seca |
| Canteiro | FOS |
| Mobilização | FOS |
| Jornada | 9 h/dia |
| Calendário | 22 dias/mês |

Campos não preenchidos: contato, e-mail, profundidade, espessura média e área de dragagem.

# 3. Inventário e fluxo das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identidade, premissas técnicas e calendário. |
| 2 | `Cotaçoes` | Registro de fornecedores, contatos e referências de preço. |
| 3 | `Produção` | Produção horária, mensal e prazo matemático. |
| 4 | `Barrilete` | Composição física e depreciação do barrilete. |
| 5 | `1. Mob. Draga` | Mobilização e montagem da draga. |
| 6 | `2. Mob. Eq. Polimero` | Mobilização e montagem do equipamento de polímero. |
| 7 | `Canteiro` | Implantação e custo mensal do canteiro. |
| 8 | `3. Prep. Célula` | Dimensionamento e custo da célula impermeabilizada. |
| 9 | `4. Forn. Bag` | Dimensionamento, fornecimento e instalação dos bags. |
| 10 | `5. Operação Sistema` | Equipamento, polímero e equipe do sistema de desidratação. |
| 11 | `7. Dragagem` | Centro principal de custos mensais da dragagem e operação. |
| 12 | `8. Medição` | Amostras, batimetria e acompanhamento dos bags. |
| 13 | `9. Transferencia` | Transferência da draga. |
| 14 | `10. Desmob. Draga` | Desmobilização da draga. |
| 15 | `11. Desmob. Eq. Polimero` | Desmobilização do equipamento de polímero. |
| 16 | `10. Plan. Preços` | Consolidação de custos, BDI e preço de venda. |

Fluxo observado:

```text
Dados Obra
    ├── Produção ─────────────────────────────┐
    ├── jornadas das equipes                 │
    └── volume ──> dimensionamento dos bags  │
                                                   ↓
Barrilete ──> Mobilização/Desmobilização do equipamento de polímero
Produção ──> prazo arredondado ──> Canteiro / Operação / Dragagem
Bags ──> área da célula / amostras / polímero / quantidade de bags
Canteiro ──> Dragagem
Operação do sistema ──> Dragagem
Composições individuais ──> Planilha de Preços
```

# 4. Análise por aba

## 4.1. Aba `Dados Obra`

### Objetivo e papel

Registrar a identidade da proposta e as premissas usadas pelas demais abas.

### Entradas e saídas — EVIDÊNCIA CONFIRMADA

- `H16 = B16 + E16`: recalque total, resultando em 500 m.
- `H17 = B17 + E17`: linha flutuante total, resultando em 300 m.
- `G21 = B21 × D21 × B20`: volume geométrico; resulta em zero porque dimensões e espessura estão vazias.
- Horas/dia e dias/mês alimentam `Produção` e diversas equipes.
- Volume de 25.000 m³ alimenta `Produção` e `4. Forn. Bag`.

### Entidades

Proposta, cliente, obra, material, volume, recalque, linha flutuante, linha terrestre, área, espessura, bota-fora, medição, responsabilidade e jornada.

### DÚVIDAS

- Qual a diferença operacional entre o volume informado e o volume geométrico calculável?
- O termo `ESGOTO` representa lodo bruto, lodo digerido ou outra condição?
- Profundidade, espessura e área não foram necessárias ou ficaram pendentes?

## 4.2. Aba `Cotaçoes`

### Objetivo e papel

Preservar referências de fornecedores e preços para guindaste, contêiner, movimentação de material, brita e carreta.

### Conteúdo — EVIDÊNCIA CONFIRMADA

- Guindaste Ideal, 50 t: R$ 400/h ou R$ 4.000/dia; anotação `Sem frete`.
- Observação explícita: `NAO COTEI PREÇOS LOCALMENTE`.
- FOX: escavadeira hidráulica R$ 2.500/dia; caminhão 17 m³ R$ 1.000/dia; frete ida e volta R$ 1.500.
- RUBAO: brita nº 2 posto em obra a R$ 158/m³.
- Registro de fornecedores e contatos para carreta, brita e guindaste.
- Link para reservatório de fibra de 20.000 litros.

### EVIDÊNCIA PARCIAL

A aba funciona como memória auxiliar e não alimenta fórmulas diretamente. Os preços efetivamente usados nas composições podem divergir dessas referências.

### Anomalias e dúvidas

- Há seções sem preços preenchidos.
- O aviso de ausência de cotação local reduz a confiança das referências de logística.
- Não há data explícita para todas as cotações.

## 4.3. Aba `Produção`

### Objetivo

Converter vazão, eficiência, concentração, jornada e calendário em produção e prazo.

### Fórmulas e resultados — EVIDÊNCIA CONFIRMADA

- vazão: 130 m³/h;
- eficiência: 65%;
- concentração: 15%;
- produção útil: `130 × 65% × 15% = 12,675 m³/h`;
- horas mensais: `9 × 22 = 198 h/mês`;
- produção mensal: `12,675 × 198 = 2.509,65 m³/mês`;
- prazo matemático: `25.000 ÷ 2.509,65 = 9,961548423 meses`.

### EVIDÊNCIA PARCIAL

Eficiência e concentração são aplicadas como fatores multiplicativos da vazão para obter volume útil produzido.

### DÚVIDAS

- Vazão de 130 m³/h é nominal, testada ou escolhida para esta obra?
- Eficiência de 65% e concentração de 15% são específicas deste lodo?
- O prazo comercial usa 10 meses por arredondamento para cima.

## 4.4. Aba `Barrilete`

### Objetivo

Compor o investimento físico do barrilete e apropriar 20% como custo do orçamento.

### Composição — EVIDÊNCIA CONFIRMADA

Inclui tubos de ferro, tocos, joelhos, tees, ponteiras, caps, válvulas, mangueira, braçadeiras, curvas, bomba lameira e mão de obra.

- Diversos preços são formados por `preço-base × 1,4`.
- custo físico total: R$ 30.074,80;
- depreciação apropriada: 20%, equivalente a R$ 6.014,96;
- BDI interno: 0%;
- preço final usado: R$ 6.014,96.

### EVIDÊNCIA PARCIAL

A planilha não vende o barrilete integralmente; apropria uma parcela de 20% do investimento.

### DÚVIDAS

- O fator 1,4 representa margem de compra, impostos, frete ou atualização?
- A taxa de 20% é depreciação por obra, vida útil esperada ou critério comercial?

## 4.5. Aba `1. Mob. Draga`

### Objetivo

Compor mobilização e montagem da draga de 6".

### Equipe — EVIDÊNCIA CONFIRMADA

1 operador líder, 2 operadores de draga e 4 ajudantes; leis sociais de 110%; refeição e transporte.

Fórmula de mão de obra:

```text
quantidade × R$/h × horas/dia × (1 + leis sociais)
```

Custo diário da equipe: R$ 2.739,338.

### Serviços e resultado

- guindaste para carregamento;
- carreta carga seca para a draga: 3 unidades × R$ 18.000;
- guindaste de descarga e montagem: 2 dias × R$ 5.500;
- mão de obra: 5 dias;
- itens estruturados, porém zerados: treinamento, mobiliário, frete e trator D4;
- custo final: R$ 80.696,69;
- BDI interno: 0%;
- observação: `Dois retornos`.

### DÚVIDAS

- O texto `Dois retornos` representa duas mobilizações, duas viagens ou contingência?
- O preço de carreta é muito superior à referência parcial anotada; exige confirmação de escopo/distância.

## 4.6. Aba `2. Mob. Eq. Polimero`

### Objetivo

Compor mobilização, implantação e montagem do equipamento de preparo/injeção de polímero.

### Equipe e serviços — EVIDÊNCIA CONFIRMADA

- 1 operador de polímero, 2 operadores líderes e 4 ajudantes;
- custo diário: R$ 2.731,519;
- cobertura do equipamento;
- munck;
- brita e concreto para piso;
- frete do equipamento;
- instalações hidráulicas e elétricas;
- parcela de máquina WAP;
- barrilete a R$ 6.014,96;
- 5 dias de mão de obra;
- preço final: R$ 53.912,555;
- observação: `2 mobilizaçoes`.

### EVIDÊNCIA PARCIAL

A implantação do sistema de polímero exige base física, cobertura, utilidades e barrilete próprios.

## 4.7. Aba `Canteiro`

### Objetivo

Compor implantação e permanência do canteiro, convertendo o total em custo mensal.

### Estrutura — EVIDÊNCIA CONFIRMADA

- equipe de integração com custo diário de R$ 2.669,338;
- três contêineres;
- dois fretes;
- PPRA, PCMSO e LTCAT;
- ARTs;
- placa;
- água potável;
- material de escritório;
- banheiro químico;
- exames médicos;
- três dias de integração;
- vigilância estruturada, mas sem custo.

Prazo pretendido:

```text
meses de canteiro = arredondar para cima o prazo de Produção + 1
prazo de operação = meses de canteiro - 1
```

Valores preservados indicam 11 meses de canteiro e 10 meses de operação.

- total: R$ 88.948,014;
- custo unitário mensal: R$ 8.894,8014;
- acréscimo interno de 1%: R$ 88,948014;
- preço mensal final: R$ 8.983,749414.

### DÚVIDA

O acréscimo de 1% está rotulado como `BDI`, mas não há explicação de por que somente esta composição usa 1% enquanto outras usam 0%.

## 4.8. Aba `3. Prep. Célula`

### Objetivo

Dimensionar e custear a preparação de uma célula impermeabilizada para acomodação dos bags.

### Dimensionamento físico — EVIDÊNCIA CONFIRMADA

Área da célula recebida da aba de bags: 4.148 m².

Coeficientes:

- PEAD: 1,196 m² por m² de célula → 4.961,008 m²;
- Bidim: 1,48 m² por m² → 6.139,04 m²;
- brita: 0,10 m³ por m² → 414,8 m³;
- retroescavadeira: 0,023 h por m² → 95,404 h;
- mão de obra: 0,023 h por m² → 95,404 h;
- divisão por equipe de 10 pessoas → 9,5404 dias.

### Composição de custos

- preparo do terreno;
- mobilização de patrola;
- aluguel e mobilização de retro;
- regularização manual;
- PEAD e instalação;
- Bidim;
- brita com fator adicional de 1,2, resultando em 497,76 m³;
- retro para espalhamento;
- mão de obra de instalação.

Custo final: R$ 342.436,662, com uma repetição.

### EVIDÊNCIA PARCIAL

Os fatores 1,196, 1,48, 0,10, 0,023 e 1,2 parecem representar perdas, sobreposições, espessuras ou produtividade específicas da solução.

### DÚVIDAS

- Origem técnica dos coeficientes.
- A linha `Material de emprestimo` possui preço, mas quantidade e custo zero.
- Observações citam referências de outros locais e datas, podendo ser resíduos históricos.

## 4.9. Aba `4. Forn. Bag`

### Objetivo

Converter volume e teor de sólidos em quantidade de bags, selecionar dimensão e compor fornecimento e instalação.

### Cálculo de massa e volume — EVIDÊNCIA CONFIRMADA

```text
volume de dragagem = 25.000 m³
sólidos in situ = 10%
tonelada seca = 25.000 × 10% = 2.500
sólidos após desaguamento = 22%
volume a acomodar = 2.500 ÷ 22% = 11.363,636 m³
```

### Seleção observada

- bag selecionado: 8 × 30 m;
- capacidade usada: 460 m³ por bag;
- quantidade calculada: 24,703557;
- quantidade de compra: 25 bags, por arredondamento para cima;
- preço unitário utilizado: R$ 35.100;
- fornecimento: R$ 877.500;
- munck: 2 dias;
- instalação: 11 dias;
- preço final: R$ 910.862,718.

### Área da célula

- arranjo `4 × 4`;
- dimensões `34 m × 122 m`;
- área: 4.148 m²;
- essa área alimenta `3. Prep. Célula`.

### Tabela comparativa de bags

O arquivo registra capacidades e preços por m³ para diversas dimensões, incluindo 6×50, 8×30, 8×25, 6×30, 8×10, 8×13, 8×14, 8×15, 8×20 e 6×15. Apenas o bag 8×30 participa do cenário final.

### EVIDÊNCIA PARCIAL

- O cálculo trata o percentual in situ como conversão direta do volume para tonelada seca, implicitamente assumindo uma relação unitária entre m³ e tonelada para a fração seca ou uma simplificação equivalente.
- O preço do bag é calculado por área na linha final: 18 × 30 = 540 m²; R$ 65/m²; total de R$ 35.100.

### DÚVIDAS

- Unidade física da `Tonelada Seca`, pois a fórmula parte diretamente de volume × percentual.
- Origem das capacidades de cada bag.
- Por que o título de preço usa `P18 x 30` enquanto o item selecionado é 8 × 30.
- O arranjo e a área consideram corredores, taludes, folgas e segunda camada?

## 4.10. Aba `5. Operação Sistema`

### Objetivo

Compor equipamento, insumos e equipe para preparo e injeção de polímero.

### Equipe

- 1 operador do sistema;
- 3 ajudantes;
- custo diário: R$ 1.185,325.

### Polímero — EVIDÊNCIA CONFIRMADA

```text
quantidade = tonelada seca × 4 kg/t × 1,1
           = 2.500 × 4 × 1,1
           = 11.000 kg

preço = R$ 23,40 × 1,1 = R$ 25,74/kg
custo = R$ 283.140
```

Observação: SNF Flonex 4350 SH, floculante catiônico em pó; referência de 02/08/2024.

### Outros componentes

- equipamento de preparo/injeção: R$ 50.000;
- dois fretes de polímero;
- instalações hidráulicas;
- parcela de máquina WAP;
- itens estruturados e zerados: caminhão-pipa, gerador/diesel, tanques, frete de tanque e diesel;
- 300 dias de equipe, derivados de 10 meses × 30 dias;
- total: R$ 696.337,50;
- custo mensal preservado: R$ 69.633,75.

### EVIDÊNCIA PARCIAL

- Dosagem nominal: 4 kg de polímero por tonelada seca.
- Fator 1,1 é aplicado tanto à quantidade quanto ao preço, gerando margem dupla de 10%.

### DÚVIDAS

- O fator duplo de 1,1 é deliberado?
- A equipe opera todos os 30 dias do mês, embora a produção da draga use 22 dias/mês?
- A observação `Iremos usar a estrutura da SABESP` é premissa real desta obra ou resíduo de outro orçamento?

## 4.11. Aba `7. Dragagem`

### Objetivo

Concentrar custos mensais de operação, pessoal, manutenção, apoio, administrativas, BDI e financeiras, somando depois a operação dos bags.

### Resíduos documentais — EVIDÊNCIA CONFIRMADA

O cabeçalho registra:

- `CLIENTE: REFAP`;
- data `28/05/2021`;
- draga 6" elétrica;
- valor do equipamento R$ 450.000.

Esses dados conflitam com `SAEC`, `Catanduva` e a data da proposta atual.

### DÚVIDA

Não se assume que REFAP ou 2021 pertençam à obra atual. O conteúdo aparenta ter sido reutilizado como modelo.

### I. Operação

- 198 h/mês;
- eficiência: 0,9;
- consumo: 1 unidade/h;
- combustível: R$ 7;
- combustível: R$ 1.247,40;
- filtros/lubrificantes: 10% do combustível;
- fretes e carretos: R$ 2.000;
- segurança e uniformes: R$ 500;
- total: R$ 3.872,14.

### II. Pessoal

Horas mensais remuneradas:

```text
horas extras 70%: 0,5 × 22 = 11 h
horas extras 100%: 0 × 1 = 0 h
horas normais: 7,33333 × 30 = 219,9999 h
total remunerado = 11 × 1,7 + 0 × 2 + 219,9999 = 238,6999 h
```

Equipe efetivamente quantificada:

- 1 operador líder;
- 1 operador de draga;
- 1 ajudante.

Engenheiro, técnico de segurança, motorista, booster e administrativo estão estruturados, mas com quantidade vazia.

- salários: R$ 16.102,695254;
- encargos sociais: 110% = R$ 17.712,9647794;
- refeições: R$ 5.960;
- alojamento: R$ 3.150;
- viagens nas folgas: R$ 0;
- total de pessoal: R$ 42.925,6600334.

### III. Manutenção

- peças e acessórios: 0,6% ao mês do equipamento = R$ 2.700;
- docagem anual apropriada: 1% ao mês = R$ 4.500;
- limpeza/pintura: R$ 250;
- terceiros: R$ 250;
- total: R$ 7.700.

### IV. Equipamentos de apoio

- linha de recalque: R$ 4.519,666667/mês;
- canteiro: R$ 8.983,749414/mês;
- automóveis e combustível: R$ 5.000;
- total do bloco: R$ 18.503,416081.

A linha de recalque é decomposta em:

- tubulação: aquisição R$ 37.500; depreciação em 12 meses + 1% de juros → R$ 3.500/mês;
- flutuantes: aquisição R$ 7.500; depreciação + juros → R$ 700/mês;
- acoplamentos: aquisição R$ 3.425; depreciação + juros → R$ 319,666667/mês.

### V. Administrativas

- viagens de inspeção: R$ 5.000;
- comunicações: R$ 300;
- demais itens zerados;
- total: R$ 5.300.

### Despesas diretas, BDI e financeiras

- despesas diretas: R$ 78.301,216114;
- oficina: 5% das despesas diretas;
- administração: 5%;
- BDI interno total: 10% = R$ 7.830,121611;
- depreciação do equipamento em 60 meses: R$ 7.500;
- juros de capital: 1% do equipamento = R$ 4.500;
- atrasos: 0,5% das despesas diretas = R$ 391,506081;
- financeiras: R$ 12.391,506081;
- custo mensal da dragagem: R$ 98.522,843806.

### Integração com o sistema de bags

- custo mensal da operação dos bags/polímero: R$ 69.633,75;
- custo mensal combinado: R$ 168.156,593806;
- prazo pretendido: 10 meses, por arredondamento para cima;
- custo total: R$ 1.681.565,93806.

### Bloco de preço horário

- multiplicador mensal: 1,6;
- preço de venda mensal: R$ 269.050,55009;
- horas trabalhadas: 198;
- eficiência: 60%;
- horas produtivas: 118,8;
- preço por hora produtiva: R$ 2.264,73527;
- hora à disposição: 60% × 62% do preço/h = R$ 842,48152.

### Anomalias e dúvidas

- produção prevista de 1.930,5 m³/mês não está vinculada à aba `Produção`, que calcula 2.509,65 m³/mês;
- campos `CUSTO UNITÁRIO`, `BDI` e `PREÇO DE VENDA R$/m³` estão vazios ou zerados no resumo antigo;
- o modelo combina lógica antiga de preço horário com a consolidação atual por m³ e pacotes;
- confirmar se a eficiência 0,9 do combustível, 0,6 das horas produtivas e 0,62 da hora à disposição são conceitos distintos e intencionais;
- confirmar se a draga elétrica deveria consumir combustível na forma descrita.

## 4.12. Aba `8. Medição`

### Objetivo

Compor amostragem e acompanhamento do processo de medição.

### EVIDÊNCIA CONFIRMADA

- equipe diária: 1 operador líder e 2 ajudantes;
- custo diário: R$ 800,40;
- amostras: 3 por bag × 25 bags = 75;
- preço por amostra: R$ 65;
- acompanhamento: 25 dias × R$ 800,40;
- batimetria está estruturada a R$ 12.000, mas com quantidade vazia;
- preço final: R$ 24.885;
- BDI interno: 0%.

### EVIDÊNCIA PARCIAL

A quantidade de amostras é diretamente proporcional ao número de bags, usando três amostras por unidade.

## 4.13. Aba `9. Transferencia`

### Objetivo

Compor um evento de transferência da draga.

### EVIDÊNCIA CONFIRMADA

- guindaste: R$ 7.500;
- um dia de acompanhamento/equipe: R$ 800,40;
- preço final: R$ 8.300,40;
- BDI interno: 0%.

### DÚVIDA

A descrição da mão de obra menciona `Coleta BagsFOS`, embora a aba seja de transferência, sugerindo reaproveitamento de linha.

## 4.14. Aba `10. Desmob. Draga`

### Objetivo

Compor desmontagem e desmobilização da draga.

### EVIDÊNCIA CONFIRMADA

- equipe diária: 2 operadores/técnicos e 4 ajudantes;
- custo diário: R$ 1.398,192;
- três carretas × R$ 18.000;
- três dias de equipe;
- dois dias de guindaste × R$ 5.500;
- preço final: R$ 69.194,576;
- BDI interno: 0%.

### DÚVIDAS

- Título interno diz `7 - DESMOBILIZAÇÃO`, embora a aba seja `10`.
- Frete do guindaste está estruturado com quantidade 2 e preço zero.

## 4.15. Aba `11. Desmob. Eq. Polimero`

### Objetivo

Compor a retirada do equipamento de polímero.

### EVIDÊNCIA CONFIRMADA

- mesma equipe diária da desmobilização da draga;
- uma carreta: R$ 18.000;
- dois dias de mão de obra: R$ 2.796,384;
- demais itens estruturados e zerados: cobertura, brita, concreto, instalações, WAP e barrilete;
- preço final: R$ 20.796,384;
- BDI interno: 0%.

### DÚVIDA

O título interno ainda diz `2 - DESMOBILIZAÇÃO E MONTAGEM`, sinalizando nomenclatura reaproveitada.

## 4.16. Aba `10. Plan. Preços`

### Objetivo

Consolidar os pacotes de custo e aplicar BDI comercial.

### Estrutura — EVIDÊNCIA CONFIRMADA

| Item | Serviço | Custo total | Quantidade | Unidade | BDI | Preço total |
| ---: | --- | ---: | ---: | --- | ---: | ---: |
| 1 | Mobilização e montagem da draga | R$ 80.696,69 | 1 | un | 85% | R$ 149.288,8765 |
| 2 | Mobilização do equipamento de polímero e barrilete | R$ 53.912,555 | 1 | un | 85% | R$ 99.738,22675 |
| 3 | Preparo de célula | R$ 342.436,662 | 4.148 | m² | 85% | R$ 633.507,8247 |
| 4 | Fornecimento de bags | R$ 910.862,718 | 1 | un | 85% | R$ 1.685.096,0283 |
| 5 | Transferência | R$ 8.300,40 | 1 | un | 85% | R$ 15.355,74 |
| 6 | Dragagem e operação do sistema | R$ 1.681.565,93806 | 2.500 | m³ | 85% | R$ 3.110.896,98541 |
| 7 | Medição | R$ 24.885,00 | 1 | un | 85% | R$ 46.037,25 |
| 8 | Desmobilização da draga | R$ 69.194,576 | 1 | un | 85% | R$ 128.009,9656 |
| 9 | Desmobilização do equipamento de polímero | R$ 20.796,384 | 1 | un | 85% | R$ 38.473,3104 |

Totais:

- custo total: R$ 3.192.650,92306;
- preço de venda: R$ 5.906.404,20766;
- preço da dragagem/operação: R$ 2.362,561683 por m³ de base seca;
- agregações auxiliares registradas: R$ 295.064,35325; R$ 5.444.856,57841; R$ 166.483,276;
- valor auxiliar de R$ 2.177,942631 por unidade, calculado pelo subtotal de itens 3 a 6 dividido por 2.500;
- células auxiliares usam divisores 12.600, 1.625 e 3.634,710281 sem rótulos suficientes.

### Regra comercial observada

```text
custo unitário = custo total ÷ quantidade
preço unitário = custo unitário × (1 + 85%)
preço total = quantidade × preço unitário
```

### DÚVIDAS

- Por que a quantidade comercial do item de dragagem é 2.500 m³, correspondente à tonelada seca, embora a unidade esteja escrita como `m3`?
- Qual o significado dos divisores 12.600, 1.625 e do resultado 3.634,710281?
- O BDI uniforme de 85% é específico desta proposta?
- O preparo de célula é vendido por área; bags e mobilizações são globais; dragagem é vendida por base seca. Confirmar se essa combinação é a estrutura contratual pretendida.

# 5. Entidades conceituais encontradas

## EVIDÊNCIA CONFIRMADA

- proposta;
- cliente;
- obra;
- local;
- material;
- volume dragado;
- massa/tonelada seca;
- concentração in situ;
- concentração após desaguamento;
- produção da draga;
- prazo;
- draga;
- linha de recalque;
- linha flutuante;
- barrilete;
- equipamento de polímero;
- polímero;
- geobag;
- célula;
- PEAD;
- geotêxtil/Bidim;
- brita;
- canteiro;
- equipe;
- cargo/função;
- leis sociais;
- refeição;
- transporte;
- equipamento de apoio;
- mobilização;
- transferência;
- medição;
- amostra;
- desmobilização;
- custo direto;
- BDI interno;
- despesas financeiras;
- custo mensal;
- custo unitário;
- BDI comercial;
- preço de venda;
- fornecedor;
- cotação.

# 6. Regras e fórmulas importantes

## EVIDÊNCIA CONFIRMADA

1. **Produção útil**
   ```text
   vazão × eficiência × concentração
   ```

2. **Produção mensal**
   ```text
   produção útil × horas/dia × dias/mês
   ```

3. **Prazo**
   ```text
   volume total ÷ produção mensal
   ```

4. **Mão de obra diária**
   ```text
   quantidade × valor-hora × horas/dia × (1 + leis sociais)
   ```

5. **Massa seca**
   ```text
   volume in situ × percentual de sólidos in situ
   ```

6. **Volume após desaguamento**
   ```text
   massa seca ÷ percentual de sólidos após desaguamento
   ```

7. **Quantidade de bags**
   ```text
   volume após desaguamento ÷ capacidade do bag
   ```
   com compra arredondada para cima.

8. **Polímero**
   ```text
   massa seca × 4 kg/t × 1,1
   ```

9. **Canteiro e operação**
   ```text
   prazo arredondado para cima
   ```

10. **Dragagem total**
    ```text
    (custo mensal da dragagem + custo mensal do sistema de bags) × prazo arredondado
    ```

11. **Preço comercial**
    ```text
    custo unitário × 1,85
    ```

12. **Barrilete**
    ```text
    20% do custo físico total
    ```

# 7. Padrões observados exclusivamente neste arquivo

## EVIDÊNCIA PARCIAL

- Composições auxiliares possuem bloco de equipe seguido de bloco de materiais/serviços.
- Leis sociais são majoritariamente 110%.
- BDI dentro das composições é geralmente 0%, exceto 1% no canteiro.
- O BDI comercial é aplicado somente na planilha final e é uniforme em 85%.
- Itens não aplicáveis frequentemente permanecem estruturados com quantidade vazia e custo zero.
- Custos mensais são formados pela apropriação de aquisição, depreciação, juros e despesas operacionais.
- A planilha preserva notas de fornecedores, datas e projetos anteriores dentro das composições.
- A medição em base seca altera a quantidade comercial de 25.000 m³ in situ para 2.500 unidades secas.

Nenhum desses padrões é promovido a regra geral da FOS neste documento.

# 8. Exceções, inconsistências e anomalias observadas

## EVIDÊNCIA CONFIRMADA quanto à existência

- Cabeçalho `REFAP` e data de 2021 na aba principal de dragagem, incompatíveis com SAEC/2025.
- Observação `estrutura da SABESP` em operação do sistema.
- Referências a Curitiba, Corsan, Elias Fausto e cotações de 2024.
- Numeração das abas e títulos internos não é sequencial.
- Duas abas iniciam com `10`.
- A aba `7. Dragagem` é o quinto pacote na planilha comercial.
- Produção prevista antiga de 1.930,5 m³/mês diverge da produção calculada de 2.509,65 m³/mês.
- Fórmulas de `ROUNDUP` não foram recalculadas pela ferramenta.
- Várias linhas possuem descrição e preço, mas quantidade vazia e custo zero.
- Algumas linhas repetem números de item.
- Há fórmulas auxiliares sem rótulo suficiente na planilha final.
- O custo do polímero recebe fator 1,1 na quantidade e novamente no preço.
- A equipe do sistema é calculada por 30 dias/mês, enquanto a draga opera 22 dias/mês.
- A draga é descrita como elétrica, mas existe custo de combustível no bloco de operação.
- O item comercial de dragagem usa quantidade 2.500 e unidade `m3`, embora 2.500 derive da tonelada seca.

Essas ocorrências não são classificadas automaticamente como erros de negócio.

# 9. Dúvidas para validação futura

1. A unidade comercial da base seca é tonelada seca, m³ equivalente seco ou outra unidade contratual?
2. O fator de densidade foi omitido deliberadamente na conversão de volume para tonelada seca?
3. Os percentuais de sólidos de 10% e 22% são resultados de ensaio, premissas conservadoras ou valores históricos?
4. A capacidade de 460 m³ do bag 8×30 é nominal ou efetiva?
5. O arranjo 4×4 e a área de 4.148 m² incluem folgas e segunda camada?
6. Os coeficientes de PEAD, Bidim, brita e produtividade são específicos deste projeto?
7. A dosagem de 4 kg/t seca foi definida por ensaio?
8. O acréscimo duplo de 10% do polímero é intencional?
9. Por que a operação do sistema usa 30 dias/mês?
10. O BDI comercial de 85% inclui impostos, risco, lucro e custos indiretos?
11. Qual é o significado dos cálculos auxiliares sem rótulo na planilha final?
12. O cabeçalho REFAP e outras referências históricas devem ser ignorados integralmente?
13. O custo de combustível é aplicável a uma draga elétrica?
14. A produção prevista de 1.930,5 m³/mês ainda possui algum uso?
15. O preço por hora e a hora à disposição são alternativas contratuais ou apenas memória de cálculo?
16. A transferência da draga ocorre uma única vez?
17. O texto `Dois retornos` e `2 mobilizaçoes` representa repetição real dos eventos?
18. O sistema de medição exige três amostras por bag em todos os casos ou somente nesta proposta?

# 10. Validação final

- [x] Todas as 16 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Fórmulas, dependências, entidades, regras, exceções, padrões e dúvidas preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma consolidação entre orçamentos realizada.
- [x] Nenhum índice geral ou documento de outro orçamento alterado.
