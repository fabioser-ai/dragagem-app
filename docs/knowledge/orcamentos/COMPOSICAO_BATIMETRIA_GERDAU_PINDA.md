# Análise de Orçamento — `Composição - Batimetria - Gerdau Pinda.xlsx`

## 1. Identificação da análise

- **Nome completo do arquivo:** `Composição - Batimetria - Gerdau Pinda.xlsx`
- **Data da análise:** 2026-07-14
- **Versão declarada no arquivo:** não identificada.
- **Proposta registrada:** `Proposta D_034/2025`.
- **Data registrada na planilha:** 2025-05-21.
- **Cliente registrado:** GERDAU.
- **Contato registrado:** Inácio.
- **Quantidade de abas:** 7.
- **Status da análise:** análise integral concluída.
- **Escopo documental:** exclusivamente este arquivo.
- **Implementação, arquitetura e consolidação:** não realizadas.

## 2. Regra de classificação das evidências

Neste documento:

- **EVIDÊNCIA CONFIRMADA:** informação comprovada diretamente em célula, fórmula, rótulo, valor ou dependência do Excel.
- **EVIDÊNCIA PARCIAL:** informação observada somente neste orçamento e que não pode ser promovida a regra geral da FOS.
- **DÚVIDA:** interpretação sem comprovação suficiente, campo não preenchido, fórmula inativa ou significado operacional não declarado.

Todas as regras e valores deste documento permanecem restritos ao arquivo analisado.

## 3. Classificação do orçamento

### 3.1 Tipo aparente

**EVIDÊNCIA CONFIRMADA**

Orçamento para execução de um conjunto de serviços técnicos relacionados às lagoas de estabilização da GERDAU, composto por:

1. mobilização e preparação de equipe;
2. coleta de amostras e análises laboratoriais;
3. levantamento batimétrico;
4. elaboração de projeto e escopo de dragagem;
5. consolidação comercial dos quatro pacotes.

### 3.2 Processo operacional representado

**EVIDÊNCIA CONFIRMADA**

O fluxo observado é:

```text
Cadastro da obra e geometria das lagoas
        ↓
Quantificação de áreas e amostras
        ↓
Composição de mobilização
        ↓
Composição de coleta e análises
        ↓
Composição da batimetria subcontratada
        ↓
Composição da elaboração de projeto
        ↓
Resumo de custos e preço de venda
```

### 3.3 Área de atuação

**EVIDÊNCIA CONFIRMADA**

- batimetria;
- amostragem ambiental;
- caracterização laboratorial;
- levantamento geométrico de lagoas;
- projeto e definição de escopo para futura dragagem;
- mobilização de equipe técnica.

### 3.4 Características diferenciadoras

**EVIDÊNCIA PARCIAL**

Este orçamento se diferencia por:

- não precificar diretamente a execução da dragagem;
- preparar informações para uma futura intervenção de dragagem;
- usar área em metros quadrados como principal base econômica da batimetria;
- subcontratar o serviço batimétrico à empresa SUBGEO;
- incluir análises laboratoriais e caracterização conforme NBR 10004;
- calcular a quantidade de amostras a partir de regras distintas por tipo de lagoa;
- aplicar BDI comercial de 70% no resumo, embora as abas operacionais exibam BDI de 50% em fórmulas inativas;
- manter uma aba de produção de draga sem entradas suficientes e sem participação no resumo final.

## 4. Inventário das abas

| Ordem | Aba | Dimensão observada | Papel no arquivo |
| --- | --- | --- | --- |
| 1 | `Dados Obra` | A1:P27 | Identificação, objeto, geometria das lagoas, área total, quantidade de amostras e preço unitário da SUBGEO. |
| 2 | `Produção` | A1:H24 | Estrutura de cálculo de produção e prazo de dragagem, não preenchida para este orçamento. |
| 3 | `1. Mobilização` | A1:M40 | Mão de obra, viagem, integração, documentação e itens de mobilização. |
| 4 | `2.Amostras` | A1:G24 | Coleta, análises laboratoriais, caracterização NBR 10004 e deslocamento. |
| 5 | `3. Batimetria` | A1:F24 | Subcontratação da batimetria por área, mobilização e acompanhamento. |
| 6 | `4. Projeto` | A1:F24 | Mão de obra de engenheiro para elaboração de projeto e escopo de dragagem. |
| 7 | `RESUMO` | A1:J15 | Consolidação dos custos, aplicação de BDI de venda, preço por m² e preço final apresentado. |

## 5. Visão geral das dependências

**EVIDÊNCIA CONFIRMADA**

```text
Dados Obra
 ├── Produção
 ├── 1. Mobilização
 ├── 2.Amostras
 ├── 3. Batimetria
 └── RESUMO

1. Mobilização
 ├── 2.Amostras
 ├── 3. Batimetria
 └── 4. Projeto

1. Mobilização ─┐
2.Amostras      ├── RESUMO
3. Batimetria   │
4. Projeto      ┘
```

As abas de composição reutilizam salários e custos diários da aba `1. Mobilização`. O `RESUMO` consome os totais de custo das quatro composições.

---

# 6. Análise por aba

## 6.1 Aba `Dados Obra`

### Objetivo observado

**EVIDÊNCIA CONFIRMADA**

Registrar a identificação comercial da proposta e as premissas geométricas das lagoas utilizadas para quantificar área de levantamento, quantidade de amostras e preço unitário da subcontratação batimétrica.

### Papel no fluxo

A aba é a principal fonte de entradas do arquivo. Ela alimenta:

- horas e dias de trabalho;
- área total das lagoas;
- quantidade total de amostras;
- preço unitário por m² da SUBGEO;
- campos da aba de produção;
- composições de amostragem e batimetria;
- quantidade de m² apresentada no resumo.

### Identificação comercial

**EVIDÊNCIA CONFIRMADA**

- título: `Batimetria Gerdau`;
- proposta: `Proposta D_034/2025`;
- data: 2025-05-21;
- cliente: GERDAU;
- contato: Inácio;
- objeto: `Batimetria das Lagoas de Estabilização`.

### Convenção visual declarada

**EVIDÊNCIA CONFIRMADA**

A própria aba declara:

- azul: dados a serem preenchidos;
- vermelho: informações pendentes;
- preto: resultados automáticos.

**DÚVIDA**

A análise estrutural confirmou os rótulos, mas não foi usada como fundamento para inferir responsabilidade ou obrigatoriedade de cada célula somente pela cor.

### Cadastro das lagoas

#### Lagoas anaeróbias

**EVIDÊNCIA CONFIRMADA**

- largura: 33 m;
- comprimento: 65 m;
- profundidade: 3 m;
- quantidade de lagoas: 2;
- área total calculada: 4.290 m²;
- amostras calculadas: 10.

Fórmulas:

```text
Área = largura × comprimento × quantidade
K13 = M13 × N13 × P13
4.290 = 33 × 65 × 2
```

```text
Amostras = 5 × quantidade de lagoas
L13 = 5 × P13
10 = 5 × 2
```

#### Lagoa facultativa

**EVIDÊNCIA CONFIRMADA**

- largura: 61 m;
- comprimento: 150 m;
- profundidade: 2,4 m;
- quantidade de lagoas: 1;
- área total calculada: 9.150 m²;
- amostras calculadas: 8.

Fórmulas:

```text
Área = largura × comprimento × quantidade
K14 = M14 × N14 × P14
9.150 = 61 × 150 × 1
```

```text
Amostras = 8 × quantidade de lagoas
L14 = 8 × P14
8 = 8 × 1
```

#### Totais

**EVIDÊNCIA CONFIRMADA**

```text
Área total = soma das áreas cadastradas
K19 = SOMA(K13:K18)
Área total = 13.440 m²
```

```text
Amostras totais = soma das amostras calculadas
L19 = SOMA(L13:L18)
Amostras totais = 18
```

### Preço da SUBGEO

**EVIDÊNCIA CONFIRMADA**

A planilha registra:

- valor global: R$ 18.000,00;
- referência textual: `SubGeo ZAP em 15/05/25`;
- área total: 13.440 m²;
- preço calculado: R$ 1,339285714 por m².

Fórmula:

```text
Preço por m² = valor global da cotação ÷ área total
K21 = J22 ÷ K19
R$ 1,339285714/m² = R$ 18.000,00 ÷ 13.440 m²
```

**EVIDÊNCIA PARCIAL**

O preço é uma cotação datada e específica deste orçamento. Não deve ser tratado como preço padrão da FOS.

### Campos gerais não preenchidos

**EVIDÊNCIA CONFIRMADA**

Permanecem vazios ou zerados:

- local;
- volume de dragagem;
- tipo de material;
- distância de recalque;
- linha flutuante;
- linha de terra;
- profundidade de dragagem;
- espessura média de dragagem;
- área de dragagem no bloco genérico;
- tipo de bota-fora;
- sistema de medição;
- canteiro de obras;
- mobilização.

### Fórmulas genéricas de dragagem

**EVIDÊNCIA CONFIRMADA**

A aba contém fórmulas herdadas de um modelo de dragagem:

```text
Distância total de recalque = distância informada + seio da linha
H16 = B16 + E16
```

```text
Linha flutuante total = linha informada + seio da linha
H17 = B17 + E17
```

```text
Volume geométrico = dimensão 1 × dimensão 2 × espessura média
G21 = B21 × D21 × B20
```

Como as entradas estão vazias, os resultados são zero.

### Calendário

**EVIDÊNCIA CONFIRMADA**

- horário de trabalho: 9 h/dia;
- dias de trabalho: 22 dias/mês.

### Regras de negócio observadas

**EVIDÊNCIA PARCIAL**

1. A quantidade de amostras das lagoas anaeróbias foi calculada como 5 por lagoa.
2. A quantidade de amostras da lagoa facultativa foi calculada como 8 por lagoa.
3. A batimetria foi cotada por preço global e convertida para preço unitário por m².
4. A área de cada família de lagoa considera largura, comprimento e número de lagoas, mas não utiliza profundidade.
5. A profundidade aparece como informação técnica, sem participação nos cálculos de custo deste arquivo.

### Dúvidas

- Qual critério técnico sustenta 5 amostras por lagoa anaeróbia?
- Qual critério técnico sustenta 8 amostras por lagoa facultativa?
- A profundidade é apenas descritiva ou será usada para estimar volume em etapa posterior?
- O preço da SUBGEO inclui todos os serviços batimétricos ou somente levantamento de campo?
- O campo de volume de dragagem foi deliberadamente deixado vazio porque a batimetria precede sua determinação?

---

## 6.2 Aba `Produção`

### Objetivo observado

**EVIDÊNCIA CONFIRMADA**

Calcular produção horária, produção mensal e prazo de uma operação de dragagem com base em:

- vazão;
- eficiência;
- concentração;
- horas por dia;
- dias por mês;
- quantidade total a dragar.

### Papel no fluxo

**EVIDÊNCIA CONFIRMADA**

A aba recebe:

```text
Horas por dia = Dados Obra!B26 = 9
Dias por mês = Dados Obra!B27 = 22
```

e calcula:

```text
Horas mensais = 9 × 22 = 198 h/mês
```

### Fórmulas

**EVIDÊNCIA CONFIRMADA**

```text
Produção horária = vazão × eficiência × concentração
D8 = D3 × (D4/100) × (D5/100)
```

```text
Produção mensal = produção horária × horas mensais
D13 = D8 × D11
```

```text
Quantidade total a dragar = Dados Obra!B14
D21 = Dados Obra!B14
```

```text
Horas necessárias = quantidade total ÷ produção horária
F22 = D21 ÷ D8
D24 = D21 ÷ D8
```

```text
Dias necessários = horas necessárias ÷ 9
G24 = D24 ÷ 9
```

### Estado neste orçamento

**EVIDÊNCIA CONFIRMADA**

- vazão: vazia;
- eficiência: vazia;
- concentração: vazia;
- produção horária: 0;
- produção mensal: 0;
- quantidade total a dragar: 0;
- prazo: `#DIV/0!`;
- número de horas: `#DIV/0!`;
- dias: `#DIV/0!`.

### Anomalias observadas

**EVIDÊNCIA CONFIRMADA**

1. A aba está funcionalmente inativa neste orçamento.
2. Há divisão por zero por ausência de vazão, eficiência e concentração.
3. A quantidade total a dragar referencia `Dados Obra!B14`, que está vazia.
4. O cálculo de dias divide por 9 fixamente, em vez de referenciar a célula de horas por dia.
5. A aba não alimenta o `RESUMO`.

### Interpretação restrita

**EVIDÊNCIA PARCIAL**

A aba aparenta ser um resíduo de um modelo mais amplo de orçamento de dragagem. Neste arquivo, o preço final independe de produção, volume e prazo.

### Dúvidas

- A aba deveria ter sido removida ou preenchida?
- O serviço de projeto depende do prazo de dragagem futuro ou apenas de cinco dias de engenharia?
- O cálculo de dias deveria referenciar `H3`, e não usar o número fixo 9?
- O orçamento foi apresentado mesmo com erros visíveis nesta aba?

---

## 6.3 Aba `1. Mobilização`

### Objetivo observado

**EVIDÊNCIA CONFIRMADA**

Compor o custo de mobilização de equipe, deslocamento, integração e recursos necessários para iniciar os serviços na GERDAU.

### Estrutura

A aba possui três blocos:

1. custo diário da equipe;
2. tabela auxiliar de salários e adicional de 25%;
3. itens de mobilização.

### Composição diária de mão de obra

**EVIDÊNCIA CONFIRMADA**

| Recurso | Quantidade | R$/h utilizado | Horas/dia | Leis sociais | Custo |
| --- | ---: | ---: | ---: | ---: | ---: |
| Encarregado | 1 | 30,375 | 9 | 110% | R$ 574,0875 |
| Operador Líder | 1 | 28,4875 | 9 | 110% | R$ 538,41375 |
| Ajudante Geral — pré-parada | 1 | 14,125 | 9 | 110% | R$ 266,9625 |
| Terceirizados (SubGeo) | 2 | vazio | 9 | 110% | R$ 0,00 |
| Refeições | 5 | R$ 35,00 | — | — | R$ 175,00 |
| Transporte | 5 | R$ 15,00 | — | — | R$ 75,00 |

Custo diário total:

```text
F11 = SOMA(F5:F10)
Custo por dia = R$ 1.629,46375
```

### Regra de encargos

**EVIDÊNCIA CONFIRMADA**

Para pessoal próprio:

```text
Custo = quantidade × salário-hora × horas/dia
      + (quantidade × salário-hora × horas/dia × leis sociais)
```

Exemplo do encarregado:

```text
1 × 30,375 × 9 × (1 + 110%) = R$ 574,0875
```

### Salários com adicional de 25%

**EVIDÊNCIA CONFIRMADA**

A tabela auxiliar registra:

| Função | Base | Com 25% |
| --- | ---: | ---: |
| Encarregado | R$ 24,30/h | R$ 30,375/h |
| Operador de draga | R$ 22,79/h | R$ 28,4875/h |
| Ajudante de draga | R$ 11,30/h | R$ 14,125/h |

Fórmula:

```text
Valor com adicional = valor-base × 1,25
```

**EVIDÊNCIA PARCIAL**

O adicional de 25% é aplicado neste orçamento, mas o arquivo não explica sua natureza.

### Itens com custo efetivo

**EVIDÊNCIA CONFIRMADA**

| Item | Descrição | Quantidade | Preço unitário | Total |
| ---: | --- | ---: | ---: | ---: |
| 5 | PPRA + PCMSO + LTCAT | 1 vb | R$ 2.500,00 | R$ 2.500,00 |
| 6 | ART Principal + ARTs de corresponsabilidade | 1 vb | R$ 750,00 | R$ 750,00 |
| 13 | Documentação e custo Bancodoc | 1 un | R$ 1.000,00 | R$ 1.000,00 |
| 14 | Treinamentos e acesso ao portal GERDAU | 5 dias | R$ 500,00 | R$ 2.500,00 |
| 15 | Carro Peba + gasolina para viagem | 2 dias | R$ 1.000,00 | R$ 2.000,00 |
| 16 | Carro Aguinaldo + gasolina para viagem | 1 dia | R$ 1.000,00 | R$ 1.000,00 |
| 17 | Hospedagem + refeição | 5 vb | R$ 1.100,00 | R$ 5.500,00 |
| 18 | Equipamentos de apoio | 1 vb | R$ 500,00 | R$ 500,00 |
| 19 | Integração prévia | 1 dia | R$ 1.629,46375 | R$ 1.629,46375 |
| 20 | Mão de obra — viagem e integração | 2 dias | R$ 1.629,46375 | R$ 3.258,9275 |

Total:

```text
F36 = SOMA(F16:F35)
Total de custo = R$ 20.638,39125
```

### Itens estruturados, mas zerados

**EVIDÊNCIA CONFIRMADA**

- container almoxarifado;
- container sanitário/vestiário;
- container escritório com sanitário;
- frete para containers;
- placa de obra;
- vigilância;
- água potável;
- material de escritório;
- mobiliário;
- exames de COVID.

Alguns itens contêm referência textual `Westrock`, mas não possuem quantidade.

### Hospedagem e alimentação auxiliar

**EVIDÊNCIA CONFIRMADA**

A tabela lateral considera:

| Pessoa | Hospedagem | Alimentação |
| --- | ---: | ---: |
| Eu | R$ 250,00 | R$ 100,00 |
| Líder | R$ 150,00 | R$ 100,00 |
| Ajudantes | R$ 150,00 | R$ 100,00 |
| Operador | R$ 150,00 | R$ 100,00 |
| Total diário auxiliar | R$ 700,00 | R$ 400,00 |

```text
Total auxiliar = R$ 1.100,00/dia
```

Esse valor alimenta o preço unitário do item `Hospedagem + refeição`.

### Fórmulas de preço unitário e BDI inativas

**EVIDÊNCIA CONFIRMADA**

A parte inferior contém:

```text
Preço unitário = total ÷ prazo de operação
F38 = F36 ÷ F37
```

```text
BDI = preço unitário × 50%
F39 = F38 × 50%
```

```text
Preço final = preço unitário + BDI
F40 = F38 + F39
```

Como o prazo de operação está vazio, as três células retornam `#DIV/0!`.

### Anomalias observadas

**EVIDÊNCIA CONFIRMADA**

1. O título da aba diz `CANTEIRO DE OBRAS : subitem da Dragagem`, embora a aba se chame `1. Mobilização`.
2. A quantidade de terceirizados é 2, porém o salário-hora está vazio e o custo é zero.
3. O BDI da aba é 50%, mas o `RESUMO` aplica 70%.
4. O preço final interno da aba está quebrado e não é utilizado pelo resumo.
5. O `RESUMO` consome diretamente `F36`, o custo total sem BDI.
6. Existem fornecedores ou referências textuais sem data-base completa.
7. `Documentação e Custo Bancodoc` possui observação `chute`.

### Dúvidas

- O adicional de 25% é periculosidade, mobilização, adicional temporário ou margem de segurança salarial?
- Os dois terceirizados da SUBGEO têm custo incluído no preço de R$ 18.000,00?
- O BDI correto é 50% ou 70%?
- O título herdado de canteiro de obras tem algum significado operacional neste serviço?
- Os valores da tabela de hospedagem representam custo por dia e por pessoa?
- Os itens zerados foram descartados para esta proposta ou apenas não preenchidos?

---

## 6.4 Aba `2.Amostras`

### Objetivo observado

**EVIDÊNCIA CONFIRMADA**

Compor custos de:

- análises laboratoriais;
- caracterização conforme NBR 10004;
- viagem para entrega das amostras;
- mão de obra para coleta.

### Mão de obra diária

**EVIDÊNCIA CONFIRMADA**

A aba reutiliza os salários da mobilização e reproduz custo diário de:

```text
R$ 1.629,46375/dia
```

A quantidade de terceirizados é herdada da mobilização, mas permanece sem custo.

### Quantificação de análises

**EVIDÊNCIA CONFIRMADA**

#### Análise laboratorial

- descrição: `Análise laboratorial (12 amostras)`;
- unidade: un;
- quantidade usada: 18;
- preço unitário: R$ 60,00;
- total: R$ 1.080,00.

A quantidade é referenciada de:

```text
Dados Obra!L19 = 18 amostras
```

**Anomalia observada:** o texto diz 12 amostras, mas a quantidade calculada e precificada é 18.

#### Caracterização NBR 10004

- quantidade: 3;
- preço unitário: R$ 4.095,00;
- total: R$ 12.285,00;
- referência: `BioAgri em 21/05/25`.

**EVIDÊNCIA PARCIAL**

O arquivo não explica por que 18 amostras comuns correspondem a 3 caracterizações NBR 10004.

#### Viagem

- descrição: viagem para levar as amostras;
- quantidade: 1;
- preço: R$ 1.000,00;
- total: R$ 1.000,00.

#### Mão de obra de coleta

- quantidade: 1 dia;
- custo diário: R$ 1.629,46375;
- total: R$ 1.629,46375.

### Total

**EVIDÊNCIA CONFIRMADA**

```text
F20 = SOMA(F16:F19)
Total = R$ 15.994,46375
```

### Fórmulas de prazo e BDI inativas

**EVIDÊNCIA CONFIRMADA**

- preço unitário = total ÷ prazo;
- BDI interno = 50%;
- preço final = preço unitário + BDI.

Como o prazo está vazio, as fórmulas retornam `#DIV/0!`.

O `RESUMO` usa diretamente o custo total de R$ 15.994,46375 e aplica BDI de 70%.

### Regras e relações

**EVIDÊNCIA PARCIAL**

1. O número de análises laboratoriais acompanha a quantidade total de amostras calculada nas lagoas.
2. A caracterização NBR 10004 é tratada separadamente das análises unitárias.
3. A coleta foi estimada em apenas um dia.
4. A entrega das amostras foi estimada como uma viagem global.

### Dúvidas

- Por que a descrição menciona 12 amostras quando a quantidade é 18?
- Quais análises estão incluídas nos R$ 60,00 por amostra?
- Qual agrupamento produz três caracterizações NBR 10004?
- As 18 amostras são simples, compostas ou representam pontos de coleta?
- Um dia é suficiente para a coleta nas três lagoas?
- O preço da BioAgri inclui coleta, frascos, preservação e transporte?

---

## 6.5 Aba `3. Batimetria`

### Objetivo observado

**EVIDÊNCIA CONFIRMADA**

Compor o custo da execução da batimetria subcontratada, mobilização da subcontratada e acompanhamento pela equipe FOS.

### Mão de obra diária

A aba reutiliza os salários e o custo diário da aba de mobilização:

```text
Custo diário = R$ 1.629,46375
```

### Subcontratação da SUBGEO

**EVIDÊNCIA CONFIRMADA**

- unidade: m²;
- quantidade: 13.440 m²;
- preço unitário: R$ 1,339285714/m²;
- total: R$ 18.000,00.

Dependências:

```text
Quantidade = Dados Obra!K19
Preço unitário = Dados Obra!K21
Preço total = quantidade × preço unitário
```

### Outros itens

**EVIDÊNCIA CONFIRMADA**

- mobilização: 1 verba × R$ 2.500,00 = R$ 2.500,00;
- item 3: sem descrição, preço unitário zero e total zero;
- mão de obra de acompanhamento: 2 dias × R$ 1.629,46375 = R$ 3.258,9275.

### Total

```text
Total = R$ 18.000,00
      + R$ 2.500,00
      + R$ 0,00
      + R$ 3.258,9275
      = R$ 23.758,9275
```

### Fórmulas de prazo e BDI inativas

Como nas abas anteriores:

- prazo vazio;
- preço unitário interno com `#DIV/0!`;
- BDI interno de 50% com `#DIV/0!`;
- preço final interno com `#DIV/0!`.

O resumo utiliza diretamente o custo total e aplica 70%.

### Regras e relações

**EVIDÊNCIA PARCIAL**

1. O levantamento foi contratado por preço global e representado economicamente como preço por m².
2. A FOS adiciona dois dias de acompanhamento próprio.
3. A mobilização da SUBGEO é cobrada separadamente do valor de R$ 18.000,00.
4. A quantidade de m² corresponde à soma das projeções em planta das lagoas.

### Anomalias observadas

**EVIDÊNCIA CONFIRMADA**

- há uma linha de item sem descrição;
- o título continua identificando `CANTEIRO DE OBRAS`;
- o BDI interno não participa do preço;
- a quantidade de terceirizados da composição diária não gera custo;
- o preço da SUBGEO tem referência de WhatsApp, não uma cotação formal anexada ao arquivo.

### Dúvidas

- O valor de R$ 18.000,00 já inclui equipamentos, embarcação, processamento e relatório?
- A mobilização adicional de R$ 2.500,00 pertence à SUBGEO ou à FOS?
- Os dois dias de acompanhamento incluem viagem?
- A área de 13.440 m² é área líquida ou área total sem acréscimos de borda?
- A batimetria entrega somente superfícies ou também cálculo de volume de sedimentos?

---

## 6.6 Aba `4. Projeto`

### Objetivo observado

**EVIDÊNCIA CONFIRMADA**

Compor o custo de elaboração do projeto e do escopo de dragagem após a batimetria e a caracterização das lagoas.

### Composição diária

| Recurso | Quantidade | R$/h | Horas/dia | Leis sociais | Custo |
| --- | ---: | ---: | ---: | ---: | ---: |
| Engenheiro | 1 | R$ 90,00 | 9 | 110% | R$ 1.701,00 |
| Refeição | 1 | R$ 35,00 | — | — | R$ 35,00 |
| Transporte | 1 | R$ 15,00 | — | — | R$ 15,00 |

```text
Custo por dia = R$ 1.751,00
```

### Regra de custo do engenheiro

**EVIDÊNCIA CONFIRMADA**

```text
1 × R$ 90,00/h × 9 h × (1 + 110%) = R$ 1.701,00/dia
```

### Composição do serviço

- mão de obra;
- quantidade: 5 dias;
- preço unitário: R$ 1.751,00/dia;
- total: R$ 8.755,00.

Os três primeiros itens da tabela estão vazios ou zerados.

### Total

```text
F20 = SOMA(F16:F19)
Total = R$ 8.755,00
```

### Fórmulas de prazo e BDI inativas

A aba contém o mesmo bloco de:

- preço unitário por prazo;
- BDI de 50%;
- preço final.

As fórmulas retornam `#DIV/0!` por ausência de prazo.

O resumo usa o custo total e aplica 70%.

### Regras e relações

**EVIDÊNCIA PARCIAL**

1. A elaboração de projeto foi estimada em cinco dias de engenheiro.
2. O custo horário do engenheiro é R$ 90,00 neste arquivo.
3. Refeição e transporte são adicionados por dia de trabalho.
4. Leis sociais de 110% também são aplicadas ao engenheiro.

### Dúvidas

- Quais entregáveis compõem `Elaboração do projeto e Escopo Dragagem`?
- Os cinco dias incluem reuniões, relatório, desenhos, memorial e orçamento da futura dragagem?
- O valor de R$ 90,00/h é salário, custo interno ou preço de referência?
- O engenheiro trabalha integralmente nove horas por dia neste pacote?
- Há necessidade de ART específica do projeto, além das ARTs previstas na mobilização?

---

## 6.7 Aba `RESUMO`

### Objetivo observado

**EVIDÊNCIA CONFIRMADA**

Consolidar o custo direto dos quatro pacotes, aplicar BDI comercial, calcular preço de venda e preço unitário por m² e registrar o preço final apresentado.

### Composição consolidada

| Item | Descrição | Custo direto | Quantidade | Unidade | BDI | Preço de venda |
| ---: | --- | ---: | ---: | --- | ---: | ---: |
| 1 | Mobilização | R$ 20.638,39125 | 1 | un | 70% | R$ 35.085,265125 |
| 2 | Coleta de amostras e análise geral | R$ 15.994,46375 | 1 | un | 70% | R$ 27.190,588375 |
| 3 | Batimetria | R$ 23.758,9275 | 1 | un | 70% | R$ 40.390,17675 |
| 4 | Elaboração do projeto e Escopo Dragagem | R$ 8.755,00 | 1 | un | 70% | R$ 14.883,50 |

### Custo total

```text
C8 = SOMA(C4:C7)
Custo total = R$ 69.146,7825
```

### Preço de venda

Para os itens com fórmulas visíveis:

```text
Preço unitário de venda = custo unitário × (1 + BDI)
```

Exemplo da mobilização:

```text
R$ 20.638,39125 × 1,70 = R$ 35.085,265125
```

Preço total:

```text
J8 = SOMA(J4:J7)
Preço de venda = R$ 117.549,53025
```

### Diferença entre venda e custo

```text
J9 = J8 - C8
Diferença = R$ 48.402,74775
```

**EVIDÊNCIA CONFIRMADA**

Essa diferença equivale exatamente a 70% do custo direto total, porque o mesmo BDI foi aplicado a todos os itens.

### Preço por m²

```text
Quantidade de m² = Dados Obra!K19 = 13.440 m²
Preço unitário = preço de venda ÷ área
R$ 117.549,53025 ÷ 13.440 = R$ 8,74624481/m²
```

### Preço final apresentado

**EVIDÊNCIA CONFIRMADA**

- preço matemático: R$ 117.549,53025;
- preço final apresentado: R$ 117.549,00.

**EVIDÊNCIA PARCIAL**

O valor apresentado foi reduzido em aproximadamente R$ 0,53 em relação ao cálculo. O arquivo não contém fórmula ou justificativa para o arredondamento.

### Anomalias observadas

**EVIDÊNCIA CONFIRMADA**

1. O resumo usa BDI de 70%, diferente dos 50% existentes nas abas de composição.
2. Algumas células de custo unitário e preço de venda não exibiram fórmula estrutural equivalente para todos os itens na inspeção, embora os valores calculados sigam a mesma relação econômica.
3. O preço final apresentado é digitado, e não ligado por fórmula ao preço total.
4. O preço é dividido pela área total das lagoas, apesar de o escopo incluir mobilização, análises e projeto, não apenas batimetria.
5. O custo total das abas é usado antes do BDI; os blocos de BDI internos das abas são ignorados.

### Dúvidas

- O BDI comercial aprovado é 70%?
- Os 50% nas abas são resíduos de outro orçamento?
- O preço por m² é apenas uma referência comercial ou a unidade contratual?
- O preço final apresentado foi arredondado deliberadamente para número inteiro?
- O contrato seria medido por item global, por m² ou por entrega?

---

# 7. Entidades conceituais encontradas

## 7.1 Entidades comerciais

**EVIDÊNCIA CONFIRMADA**

- proposta;
- cliente;
- contato;
- data;
- objeto;
- preço apresentado;
- BDI;
- preço de venda.

## 7.2 Entidades físicas e operacionais

**EVIDÊNCIA CONFIRMADA**

- lagoa;
- tipo de lagoa;
- largura;
- comprimento;
- profundidade;
- quantidade de lagoas;
- área;
- ponto ou amostra;
- mobilização;
- viagem;
- integração;
- levantamento batimétrico;
- projeto de dragagem.

## 7.3 Entidades de recursos

**EVIDÊNCIA CONFIRMADA**

- engenheiro;
- encarregado;
- operador líder;
- ajudante;
- terceirizado;
- refeição;
- transporte;
- hospedagem;
- veículo;
- equipamentos de apoio.

## 7.4 Entidades de fornecedores e referências

**EVIDÊNCIA CONFIRMADA**

- SUBGEO;
- BioAgri;
- Westrock;
- Bancodoc;
- portal GERDAU;
- cotação por WhatsApp;
- cotação com data-base.

## 7.5 Entidades regulatórias e documentais

**EVIDÊNCIA CONFIRMADA**

- PPRA;
- PCMSO;
- LTCAT;
- ART;
- NBR 10004;
- documentação de acesso;
- treinamentos;
- integração.

## 7.6 Entidades econômicas

**EVIDÊNCIA CONFIRMADA**

- salário-hora;
- adicional de 25%;
- leis sociais;
- custo diário;
- quantidade;
- unidade;
- preço unitário;
- preço total;
- custo direto;
- BDI;
- preço de venda;
- preço por m².

---

# 8. Regras de negócio extraídas

## 8.1 Regras confirmadas no arquivo

1. **Área por família de lagoas**

```text
Área = largura × comprimento × quantidade de lagoas
```

2. **Quantidade de amostras das lagoas anaeróbias**

```text
Amostras = 5 × quantidade de lagoas anaeróbias
```

3. **Quantidade de amostras das lagoas facultativas**

```text
Amostras = 8 × quantidade de lagoas facultativas
```

4. **Preço unitário da SUBGEO**

```text
Preço por m² = cotação global ÷ área total
```

5. **Custo diário de pessoal**

```text
Custo = quantidade × salário-hora × horas/dia × (1 + leis sociais)
```

6. **Salário com adicional**

```text
Salário utilizado = salário-base × 1,25
```

7. **Refeições e transporte**

```text
Custo = número total de pessoas × valor unitário
```

8. **Custo de cada item**

```text
Preço total = quantidade × preço unitário
```

9. **Preço de venda por item no resumo**

```text
Preço de venda = custo direto × 1,70
```

10. **Preço unitário global por área**

```text
Preço por m² = preço total de venda ÷ área total das lagoas
```

## 8.2 Regras observadas somente neste orçamento

**EVIDÊNCIA PARCIAL**

- 5 amostras por lagoa anaeróbia;
- 8 amostras por lagoa facultativa;
- três caracterizações NBR 10004;
- dois dias de acompanhamento da batimetria;
- cinco dias de elaboração de projeto;
- custo do engenheiro de R$ 90,00/h;
- leis sociais de 110%;
- adicional salarial de 25%;
- BDI comercial de 70%;
- R$ 60,00 por análise laboratorial;
- cotação SUBGEO de R$ 18.000,00;
- mobilização SUBGEO de R$ 2.500,00;
- documentação/Bancodoc de R$ 1.000,00;
- treinamentos GERDAU por cinco dias;
- cálculo comercial de R$ 8,74624481/m².

Nenhuma dessas regras deve ser promovida a padrão geral sem crosscheck e validação.

---

# 9. Fórmulas importantes

| Finalidade | Fórmula |
| --- | --- |
| Área das lagoas | `largura × comprimento × quantidade` |
| Amostras anaeróbias | `5 × quantidade de lagoas` |
| Amostras facultativas | `8 × quantidade de lagoas` |
| Área total | `SOMA(áreas)` |
| Amostras totais | `SOMA(amostras)` |
| Preço SUBGEO por m² | `R$ 18.000 ÷ 13.440` |
| Horas mensais | `horas/dia × dias/mês` |
| Produção horária | `vazão × eficiência × concentração` |
| Produção mensal | `produção horária × horas mensais` |
| Prazo em horas | `volume ÷ produção horária` |
| Custo de funcionário | `quantidade × R$/h × horas × (1 + 110%)` |
| Adicional salarial | `salário-base × 1,25` |
| Total de item | `quantidade × preço unitário` |
| Custo total por pacote | `SOMA(itens)` |
| Venda por pacote | `custo × 1,70` |
| Venda total | `SOMA(vendas dos pacotes)` |
| Diferença venda-custo | `venda total - custo total` |
| Preço comercial por m² | `venda total ÷ 13.440` |

---

# 10. Terminologia observada

| Termo | Uso no arquivo |
| --- | --- |
| Batimetria | Levantamento das lagoas, subcontratado à SUBGEO. |
| Lagoas anaeróbias | Duas lagoas de 33 × 65 m e 3 m de profundidade. |
| Lagoa facultativa | Uma lagoa de 61 × 150 m e 2,4 m de profundidade. |
| Amostra | Unidade de coleta/análise; total de 18. |
| Caracterização NBR 10004 | Serviço laboratorial precificado em três unidades. |
| Mobilização | Preparação, documentação, viagem, integração e recursos iniciais. |
| Integração | Processo prévio de acesso à GERDAU. |
| Bancodoc | Custo documental registrado como estimativa. |
| Leis sociais | Acréscimo de 110% sobre mão de obra. |
| Com 25% | Valor salarial base multiplicado por 1,25. |
| vb | Verba/global. |
| un | Unidade. |
| m² | Unidade da batimetria e referência comercial final. |
| BDI | Acréscimo comercial; 50% nas abas inativas e 70% no resumo. |
| Peba | Identificação informal de veículo ou responsável, sem definição no arquivo. |

---

# 11. Padrões estruturais observados

## 11.1 Composição repetida

**EVIDÊNCIA CONFIRMADA**

As abas `1. Mobilização`, `2.Amostras`, `3. Batimetria` e `4. Projeto` repetem o mesmo formato:

1. bloco de mão de obra;
2. custo por dia;
3. tabela de itens;
4. total;
5. prazo de operação;
6. preço unitário;
7. BDI;
8. preço final.

## 11.2 Reutilização de custos

**EVIDÊNCIA CONFIRMADA**

- salários de encarregado, operador e ajudante são centralizados na mobilização;
- outras abas referenciam esses valores;
- custo diário é repetido ou reconstruído;
- custo diário da mobilização é usado como preço da mão de obra de coleta e acompanhamento.

## 11.3 Separação entre custo e venda

**EVIDÊNCIA CONFIRMADA**

- as abas calculam custos diretos;
- o resumo aplica o BDI de venda;
- o preço final apresentado é separado do cálculo detalhado.

## 11.4 Precificação por pacote global

**EVIDÊNCIA CONFIRMADA**

Embora existam unidades técnicas internas, cada um dos quatro macroserviços aparece no resumo como uma unidade global.

---

# 12. Exceções e anomalias consolidadas

## 12.1 Fórmulas com erro

**EVIDÊNCIA CONFIRMADA**

Foram identificadas 15 células com `#DIV/0!`:

- `Produção!F22`;
- `Produção!D24`;
- `Produção!G24`;
- `1. Mobilização!F38:F40`;
- `2.Amostras!F22:F24`;
- `3. Batimetria!F22:F24`;
- `4. Projeto!F22:F24`.

Causa observada:

- produção zero;
- volume vazio;
- prazo de operação vazio.

## 12.2 Divergência de BDI

**EVIDÊNCIA CONFIRMADA**

- abas operacionais: 50%;
- resumo comercial: 70%;
- somente o BDI de 70% participa do preço final.

## 12.3 Divergência na descrição das amostras

**EVIDÊNCIA CONFIRMADA**

- descrição: 12 amostras;
- quantidade efetiva: 18 amostras.

## 12.4 Aba de produção sem função no resultado

**EVIDÊNCIA CONFIRMADA**

A aba de produção não alimenta o resumo e permanece com entradas vazias.

## 12.5 Títulos herdados

**EVIDÊNCIA CONFIRMADA**

As quatro abas de composição exibem o título `CANTEIRO DE OBRAS : subitem da Dragagem`, independentemente de seu conteúdo.

## 12.6 Preço final digitado

**EVIDÊNCIA CONFIRMADA**

O valor de R$ 117.549,00 é digitado e não possui fórmula ligando-o ao total de R$ 117.549,53025.

## 12.7 Campos e linhas residuais

**EVIDÊNCIA CONFIRMADA**

- campos genéricos de dragagem vazios;
- itens sem descrição;
- fornecedores sem quantidade;
- linha de terceirizados sem custo;
- tabelas auxiliares parcialmente preenchidas.

---

# 13. Conhecimento operacional preservado

## 13.1 Conhecimento específico deste orçamento

**EVIDÊNCIA PARCIAL**

- três lagoas somando 13.440 m²;
- 18 amostras;
- batimetria SUBGEO de R$ 18.000,00;
- mobilização da batimetria de R$ 2.500,00;
- coleta e análises de R$ 15.994,46375;
- mobilização FOS de R$ 20.638,39125;
- batimetria total de R$ 23.758,9275;
- projeto de R$ 8.755,00;
- custo direto total de R$ 69.146,7825;
- preço calculado de R$ 117.549,53025;
- preço apresentado de R$ 117.549,00;
- referência de R$ 8,74624481/m².

## 13.2 Conhecimento potencialmente reutilizável, ainda não consolidado

**EVIDÊNCIA PARCIAL**

- modelagem geométrica de lagoas;
- regras de amostragem por família de lagoa;
- decomposição do serviço em mobilização, amostras, batimetria e projeto;
- uso de subcontratação batimétrica por área;
- acompanhamento da subcontratada por equipe FOS;
- composição diária com leis sociais;
- registros de fornecedores e data-base;
- aplicação de BDI no resumo e não nas composições.

## 13.3 Dúvidas operacionais prioritárias

1. Qual é o critério de amostragem?
2. Qual é o escopo exato das análises de R$ 60,00?
3. Por que existem três caracterizações NBR 10004?
4. O BDI correto é 50% ou 70%?
5. Qual é a natureza do adicional de 25%?
6. Qual o escopo completo da SUBGEO?
7. Qual a finalidade futura da aba de produção?
8. O preço por m² é unidade comercial ou mera referência?
9. Quais entregáveis compõem o projeto?
10. Por que o preço final foi arredondado para baixo?

---

# 14. Limitações da análise

- A análise foi realizada sobre o conteúdo estrutural, valores e fórmulas presentes no arquivo Excel fornecido.
- Não foram disponibilizados anexos, propostas comerciais, cotações formais, e-mails, mensagens de WhatsApp ou relatórios relacionados.
- As referências `SubGeo ZAP em 15/05/25` e `BioAgri em 21/05/25` foram preservadas como texto do arquivo, sem validação externa.
- Não houve explicação do especialista durante esta análise.
- Campos vazios não foram preenchidos por inferência.
- Valores observados em apenas este arquivo não foram consolidados como regras gerais.
- A presença de fórmulas quebradas foi registrada, mas nenhuma fórmula foi corrigida.
- O arquivo original não foi modificado.

---

# 15. Validação final

- [x] Todas as 7 abas analisadas.
- [x] Tabelas e células relevantes documentadas.
- [x] Fórmulas e dependências registradas.
- [x] Entidades e terminologias preservadas.
- [x] Regras explícitas e implícitas registradas.
- [x] Exceções e anomalias registradas.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Nenhuma documentação de outro orçamento alterada.
- [x] Nenhum índice geral atualizado.
- [x] Nenhuma consolidação realizada.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma funcionalidade criada.
- [x] Arquivo Excel original preservado sem alterações.

## Status final

**ANÁLISE INTEGRAL CONCLUÍDA**

Este documento registra exclusivamente o conhecimento observado no arquivo `Composição - Batimetria - Gerdau Pinda.xlsx` e permanece como evidência independente para futura curadoria.
