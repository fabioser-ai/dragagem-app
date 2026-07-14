# D_001_2025- Nutrilog(1).xlsx — Dragagem de Gesso com Bacia de Decantação

## Status

- Engenharia reversa vertical concluída para o arquivo analisado.
- Todas as 8 abas foram examinadas.
- Nenhuma funcionalidade, arquitetura, banco de dados, tela ou fluxo de implementação foi definido.
- As descobertas reutilizáveis deste documento permanecem provisórias até comparação com outros orçamentos e validação do especialista.

## Identidade permanente da fonte

- **Arquivo original:** `D_001_2025- Nutrilog(1).xlsx`
- **Proposta registrada:** `Proposta D_001_2025`
- **Data registrada:** 02/01/2025
- **Cliente registrado:** NUTRILOG
- **Objeto registrado:** Dragagem Gesso
- **Local registrado:** Cubatão - SP
- **Volume registrado:** 6.000 m³
- **Equipamento indicado na composição principal:** draga de 10"
- **Bota-fora indicado:** bacia de decantação
- **Sistema de medição indicado:** preços unitários de serviços

## Regra de classificação usada neste registro

Este documento preserva simultaneamente a taxonomia oficial da Base de Conhecimento e o grau operacional solicitado para a descoberta:

| Categoria documental | Grau operacional |
| --- | --- |
| Fato observado | EVIDÊNCIA CONFIRMADA |
| Interpretação baseada em uma única fonte | EVIDÊNCIA PARCIAL |
| Hipótese para crosscheck | EVIDÊNCIA PARCIAL |
| Informação insuficiente ou fórmula não explicada | DÚVIDA |
| Anomalia observada | EVIDÊNCIA CONFIRMADA quanto à existência da anomalia, sem concluir erro de negócio |

Todas as descobertas reutilizáveis deste arquivo possuem **confiança Nível C**, pois foram observadas em uma única fonte.

## Classificação aparente do orçamento

### EVIDÊNCIA CONFIRMADA

**Origem:** arquivo `D_001_2025- Nutrilog(1).xlsx`; abas `Dados Obra`, `3. Dragagem` e `6. Plan. Preços`.

O orçamento representa:

- dragagem de gesso;
- volume de 6.000 m³;
- recalque total de 250 m;
- linha flutuante de 200 m;
- linha de terra de 50 m;
- disposição em bacia de decantação;
- formação de preço por mobilização, dragagem, medição e desmobilização;
- venda da dragagem em unidade volumétrica `m3`.

### EVIDÊNCIA PARCIAL

**Contexto:** comparação exclusiva com o modelo anteriormente documentado `D_004_2026 - SABESP.xlsx`.

Este arquivo aparenta pertencer a uma família de **dragagem direta com disposição em bacia de decantação**, sem os pacotes de preparo de célula, fornecimento de bags, sistema de polímero e operação de desaguamento observados no modelo SABESP.

A diferença deve ser preservada como **possível novo modelo de orçamento**, não como erro ou simplificação do modelo anterior.

## Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identificação da proposta, premissas técnicas, responsabilidades e calendário operacional. |
| 2 | `Produção` | Cálculo de produção horária, produção mensal e prazo estimado. |
| 3 | `1. Mob. Draga` | Composição da mobilização da draga e equipe de carga/montagem. |
| 4 | `2. Canteiro de obras` | Composição do canteiro e conversão do total para custo mensal. |
| 5 | `3. Dragagem` | Centro principal de custos operacionais, pessoal, manutenção, apoio, administrativas, BDI e financeiras. |
| 6 | `4. Desmob. Draga` | Composição própria da desmobilização da draga. |
| 7 | `5. Mediçao` | Custos de batimetria, seguro de responsabilidade civil e acompanhamento FOS. |
| 8 | `6. Plan. Preços` | Consolidação dos custos e aplicação de BDI comercial por item. |

## Fluxo completo observado

```text
Dados da obra
    ↓
Produção mensal e prazo
    ↓
Mobilização da draga
    ↓
Canteiro mensal
    ↓
Composição mensal da dragagem
    ↓
Custo total da dragagem pelo prazo arredondado
    ↓
Medição e desmobilização
    ↓
Planilha detalhada de custo e venda
```

O fluxo é sequencial na apresentação, porém as dependências formam uma rede: `Dados Obra` e `Produção` alimentam várias composições; o preço mensal do canteiro alimenta `3. Dragagem`; e os resultados finais alimentam `6. Plan. Preços`.

---

# Análise por aba

## 1. Aba `Dados Obra`

### Objetivo

Registrar a identidade comercial e as premissas técnicas e operacionais usadas pelo orçamento.

### Papel no fluxo

É a principal fonte de entradas para `Produção`, mobilização, desmobilização e dragagem.

### Entradas observadas — EVIDÊNCIA CONFIRMADA

**Origem:** `Dados Obra`.

- proposta: `Proposta D_001_2025`;
- data: 02/01/2025;
- cliente: NUTRILOG;
- contato e e-mail: não preenchidos;
- objeto: `Dragagem Gesso`;
- local: `Cubatao - Sp`;
- volume: 6.000 m³;
- tipo de material: não preenchido, embora o objeto identifique gesso;
- distância de recalque informada: 250 m;
- seio da linha de recalque: 0 m;
- linha flutuante informada: 200 m;
- seio da linha flutuante: 0 m;
- linha de terra: 50 m;
- profundidade, espessura média e área: não preenchidas;
- bota-fora: `Bacia de Decantaçao`;
- sistema de medição: `preços unitários de serviços`;
- responsabilidade pelo canteiro: FOS;
- responsabilidade pela mobilização: FOS;
- horário: 9 h/dia;
- calendário: 22 dias/mês.

### Fórmulas e saídas — EVIDÊNCIA CONFIRMADA

- `H16 = B16 + E16`: distância total de recalque.
- `H17 = B17 + E17`: linha flutuante total.
- `G21 = B21 × D21 × B20`: volume geométrico por dimensões e espessura, atualmente zero por entradas vazias.

Resultados:

- distância total de recalque: 250 m;
- linha flutuante total: 200 m;
- volume geométrico: 0 m³.

### Entidades conceituais observadas

- proposta;
- cliente;
- contato;
- obra;
- material;
- volume;
- linha de recalque;
- linha flutuante;
- linha de terra;
- bota-fora;
- sistema de medição;
- responsabilidade operacional;
- jornada de trabalho.

### Regras implícitas — EVIDÊNCIA PARCIAL

- O volume contratual informado pode coexistir com um volume geométrico calculável.
- A linha total pode incluir uma parcela adicional chamada `seio da linha`.
- Responsabilidade por canteiro e mobilização é uma premissa explícita da obra.

### Dúvidas

- Por que `Tipo de material` está vazio se o objeto registra gesso?
- Quando o volume geométrico calculado deve prevalecer sobre o volume informado?
- O seio da linha é margem técnica, folga operacional ou extensão física prevista?
- Como a responsabilidade do cliente alteraria as composições quando não fosse FOS?

---

## 2. Aba `Produção`

### Objetivo

Transformar parâmetros operacionais da draga em produção horária, produção mensal e prazo.

### Entradas — EVIDÊNCIA CONFIRMADA

**Origem:** `Produção`.

- vazão: 350 m³/h;
- eficiência: 30%;
- concentração: 15%;
- horas por dia: 9;
- dias por mês: 22;
- volume total: 6.000 m³, referenciado de `Dados Obra`.

### Fórmulas — EVIDÊNCIA CONFIRMADA

- horas mensais = horas/dia × dias/mês;
- produção horária = vazão × eficiência × concentração;
- produção mensal = produção horária × horas mensais;
- prazo = volume total ÷ produção mensal.

Fórmulas identificadas:

- `H4 = 'Dados Obra'!B27`;
- `H6 = H3 × H4`;
- `D8 = D3 × (D4/100) × (D5/100)`;
- `D11 = H6`;
- `D13 = D8 × D11`;
- `D18 = D13`;
- `D21 = 'Dados Obra'!B14`;
- `D24 = D21 ÷ D18`.

### Resultados — EVIDÊNCIA CONFIRMADA

- horas mensais: 198 h/mês;
- produção horária: 15,75 m³/h;
- produção mensal: 3.118,5 m³/mês;
- prazo matemático: 1,924001924 mês.

### Regra operacional observada — EVIDÊNCIA PARCIAL

A concentração é aplicada diretamente como fator percentual da vazão, juntamente com a eficiência, para obter volume de produção útil.

### Dependências

- recebe horas/dia, dias/mês e volume de `Dados Obra`;
- fornece horas mensais e prazo para outras abas;
- o prazo é arredondado para cima em composições dependentes de duração.

### Dúvidas

- O valor de vazão de 350 m³/h corresponde à capacidade nominal, histórica ou escolhida para a obra?
- Eficiência de 30% e concentração de 15% são estimativas específicas do gesso e desta condição?
- O prazo comercial deve usar 1,924 mês, 2 meses ou outra margem operacional?

---

## 3. Aba `1. Mob. Draga`

### Objetivo

Compor o custo do evento de mobilização da draga de 10".

### Papel no fluxo

Gera um custo único usado diretamente pela planilha detalhada de preços.

### Composição de mão de obra — EVIDÊNCIA CONFIRMADA

**Origem:** `1. Mob. Draga`, linhas 4 a 10.

Equipe:

- 1 Operador Líder;
- 1 Operador de Draga;
- 4 Ajudantes Gerais;
- 6 refeições;
- 6 transportes.

Os custos de pessoal seguem:

```text
quantidade × valor-hora × horas/dia × (1 + leis sociais)
```

Parâmetros:

- 9 h/dia, recebido de `Dados Obra`;
- leis sociais: 120%;
- refeição: R$ 40 por pessoa;
- transporte: R$ 15 por pessoa.

Custo diário da equipe: **R$ 2.304,258**.

### Serviços e recursos — EVIDÊNCIA CONFIRMADA

- guindaste para carregamento: 1 dia × R$ 2.000;
- carreta prancha rebaixada: quantidade vazia;
- carreta extensível: quantidade vazia;
- carreta carga seca para draga: 4 × R$ 2.000;
- guindaste para descarregamento e montagem: quantidade vazia, observação `Nutrilog`;
- trator D4 para lançar a draga na água: quantidade vazia;
- mão de obra para carga e montagem: 5 dias × custo diário.

Observação de fornecedor/preço na carreta carga seca: `Fabiano (1100)`, enquanto o preço unitário utilizado na linha é R$ 2.000.

### Resultados — EVIDÊNCIA CONFIRMADA

- subtotal: R$ 21.521,29;
- BDI interno: 0%;
- preço final: R$ 21.521,29.

### Regras e interpretações — EVIDÊNCIA PARCIAL

- Mobilização é tratada como evento único.
- Contratações sob responsabilidade do cliente podem permanecer estruturadas na composição com quantidade vazia e custo zero.
- Observações laterais registram contexto de fornecedor ou responsabilidade, mas não possuem estrutura formal.

### Dúvidas

- O texto `Fabiano (1100)` indica cotação de R$ 1.100 não utilizada?
- A responsabilidade `Nutrilog` explica a quantidade vazia do guindaste de descarregamento?
- Por que o título indica draga de 10", enquanto a desmobilização indica 6"?

---

## 4. Aba `2. Canteiro de obras`

### Objetivo

Compor o custo de implantação do canteiro e convertê-lo em valor mensal consumido pela operação de dragagem.

### Papel no fluxo

É identificado no próprio arquivo como `subitem da Dragagem`.

### Composição de mão de obra — EVIDÊNCIA CONFIRMADA

Equipe de montagem:

- 1 Operador Líder;
- 1 Operador de Draga;
- 2 Ajudantes Gerais;
- 4 refeições;
- 4 transportes.

Parâmetros:

- 9 h/dia;
- leis sociais: 100%;
- refeição: R$ 40;
- transporte: R$ 14.

Custo diário: **R$ 1.623,78**.

### Itens de canteiro — EVIDÊNCIA CONFIRMADA

- container almoxarifado: quantidade vazia; observação `Nutrilog`;
- container sanitário/vestiário: quantidade vazia;
- container escritório com sanitário: quantidade vazia;
- frete para containers: quantidade vazia;
- PPRA + PCMSO + LTCAT: 1 × R$ 3.000;
- ART principal + ARTs de corresponsabilidade: 1 × R$ 500;
- EPI: 4 × R$ 400;
- placa de obra: quantidade vazia;
- vigilância: quantidade vazia; observação `Nao será necessario`;
- água potável: quantidade vazia;
- material de escritório: fórmula de quantidade quebrada no valor importado, preço unitário R$ 200 e preço total preservado em R$ 600;
- banheiro químico: quantidade vazia; observação `vestiário`;
- exames médicos: 5 × R$ 300;
- mão de obra de integração: 2 dias × R$ 1.623,78.

### Fórmulas e resultados — EVIDÊNCIA CONFIRMADA

- quantidade de EPI = número total de pessoas da equipe;
- quantidade de material de escritório = prazo arredondado + 1;
- subtotal = soma dos itens;
- prazo de operação = prazo arredondado para cima;
- preço mensal = subtotal ÷ prazo arredondado.

Valores preservados no arquivo:

- subtotal: R$ 10.447,56;
- prazo operacional esperado pela fórmula: 2 meses;
- BDI: 0%;
- preço final mensal: R$ 5.223,78.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- `D25` apresenta `#NAME?` no valor calculado, embora a fórmula seja `ROUNDUP(Produção!D24,0)+1`.
- `F30` apresenta `#NAME?`, embora a fórmula seja `ROUNDUP(Produção!D24,0)`.
- O total de R$ 600 em material de escritório está preservado mesmo com a quantidade exibida como `#NAME?`.
- O preço final mensal de R$ 5.223,78 corresponde a R$ 10.447,56 ÷ 2.

Não se conclui, apenas pela anomalia, que a regra operacional esteja errada.

### Interpretações — EVIDÊNCIA PARCIAL

- Custos de implantação são apropriados mensalmente durante o prazo arredondado da obra.
- Alguns itens podem ser removidos quando fornecidos pelo cliente ou declarados desnecessários.
- A fórmula `prazo + 1` para material de escritório pode representar um mês adicional de preparação/encerramento.

### Dúvidas

- Por que apenas material de escritório usa `prazo + 1`?
- Containers sob responsabilidade da Nutrilog foram excluídos por fornecimento direto?
- O total deve ser apropriado pelo prazo matemático ou pelo prazo inteiro arredondado?

---

## 5. Aba `3. Dragagem`

### Objetivo

Consolidar o custo mensal da operação principal e transformá-lo em custo total para o prazo previsto.

### Papel no fluxo

É o maior centro de custos do arquivo e alimenta o item `Dragagem` da planilha detalhada.

### Identificação e resíduos históricos — EVIDÊNCIA CONFIRMADA

O cabeçalho contém:

- `REF.: COPEBRAS - NUTRILOG`;
- data `12/04/2021`;
- cliente `DAAE`;
- equipamento `Draga de 10"`;
- valor do equipamento `NO ESTADO`: R$ 1.000.000.

Existe divergência entre o cliente da aba (`DAAE`) e o cliente do orçamento (`NUTRILOG`).

### I — Operação

#### Entradas e itens — EVIDÊNCIA CONFIRMADA

- quantidade de horas mensais referenciada de `Produção`;
- eficiência: 0,9;
- consumo por hora: 40;
- valor combustível: 0,15;
- combustível: R$ 1.069,20;
- filtros/lubrificantes: R$ 4.000;
- fretes e carretos: R$ 1.500;
- materiais de segurança e uniformes: R$ 500.

Total de operação: **R$ 7.069,20**.

#### Fórmula observada

`F10 = C9 × D9 × E9 × F9`.

O rótulo da linha informa `Combustível 0,15 x HP x hora`, mas os fatores efetivamente usados exigem esclarecimento sobre as unidades.

#### Anomalia

`C9` apresenta `#NAME?` no valor importado, embora a fórmula referencie `Produção!H6`.

### II — Pessoal

#### Salários — EVIDÊNCIA CONFIRMADA

Funções ativas:

- 1 Operador Líder, valor-hora R$ 30;
- 1 Operador de Draga, valor-hora R$ 26,71;
- 2 Ajudantes, valor-hora R$ 10.

Funções estruturadas, porém zeradas ou sem quantidade:

- Engenheiro;
- ajudante booster;
- Motorista;
- operador booster;
- Administrativo.

A quantidade de horas remuneradas é calculada por:

```text
(A × 1,70) + (B × 2) + C
```

onde:

- A = horas extras mensais a 70%;
- B = horas extras mensais a 100%;
- C = horas normais mensais.

Neste arquivo:

- A = 1 h/dia × 22 dias = 22 h;
- B = 0;
- C = 7,33333 h/dia × 30 dias = 219,9999 h;
- total remunerado = 257,3999 h/mês.

Total de salários: **R$ 19.745,146329**.

#### Encargos sociais — EVIDÊNCIA CONFIRMADA

- taxa: 120% sobre salários;
- valor: R$ 23.694,1755948.

#### Cantina — EVIDÊNCIA CONFIRMADA

Tabela distingue:

- funcionários alojados: 2, com café, almoço e jantar, 30 dias;
- funcionários da cidade: 2, com café e almoço, 22 dias.

Total: **R$ 4.320**.

#### Alojamento — EVIDÊNCIA CONFIRMADA

A estrutura contém aluguel, água/luz, multa por rescisão e limpeza, mas o total utilizado é zero.

#### Viagens nas folgas — EVIDÊNCIA CONFIRMADA

Há estrutura para engenheiro, encarregado e funcionários, mas o total utilizado é zero.

#### Prêmios de produção — EVIDÊNCIA CONFIRMADA

Há estrutura para engenheiro, encarregado, draguistas e ajudantes, sem valores utilizados.

#### Total de pessoal

A soma de salários, encargos, cantina, alojamento e viagens resulta em **R$ 47.759,3219238**.

### III — Manutenção — EVIDÊNCIA CONFIRMADA

Itens:

- peças e acessórios: 0,6% ao mês sobre valor do equipamento = R$ 6.000;
- docagem anual: 1,0% ao mês sobre valor do equipamento = R$ 10.000;
- limpeza e pintura: R$ 1.000;
- mão de obra de terceiros: R$ 1.000.

Total: **R$ 18.000**.

### IV — Equipamentos de apoio — EVIDÊNCIA CONFIRMADA

Itens ativos:

- linha de recalque: R$ 4.701,40;
- automóvel: R$ 3.500, com anotação `carros + combustivel`;
- ferramentas: R$ 150;
- canteiro: R$ 5.223,78, referenciado da aba `2. Canteiro de obras`.

Itens estruturados e zerados:

- rebocador e cábrea;
- pick-up;
- cabo elétrico;
- maçarico.

Total do grupo: **R$ 13.575,18**.

#### Memória da linha de recalque

**Tubulação:**

- 250 m × R$ 120/m = R$ 30.000;
- depreciação em 10 meses = R$ 3.000/mês;
- juros de 1% = R$ 300/mês;
- subtotal mensal = R$ 3.300.

**Flutuante:**

- 50 peças × R$ 200 = R$ 10.000;
- depreciação em 10 meses = R$ 1.000/mês;
- juros de 1% = R$ 100/mês;
- subtotal mensal = R$ 1.100.

**Acoplamento:**

- 22,833333 peças × R$ 120 = R$ 2.740;
- depreciação em 10 meses = R$ 274/mês;
- juros de 1% = R$ 27,40/mês;
- subtotal mensal = R$ 301,40.

Total mensal da linha: **R$ 4.701,40**.

#### Dependências confirmadas

- tubulação usa a distância total de recalque de `Dados Obra`;
- flutuante usa a linha flutuante dividida por 12 e multiplicada por 3;
- canteiro usa o preço mensal de `2. Canteiro de obras`;
- os subtotais alimentam o custo mensal de equipamentos de apoio.

### V — Administrativas — EVIDÊNCIA CONFIRMADA

- comissões: R$ 0;
- viagens de inspeção: R$ 1.000;
- viagens administrativas: R$ 0;
- comunicações: R$ 300;
- seguro e licenciamento: sem valor.

Total: **R$ 1.300**.

### Despesas diretas — EVIDÊNCIA CONFIRMADA

A soma de operação, pessoal, manutenção, equipamentos de apoio e administrativas resulta em:

**R$ 87.703,7019238 por mês.**

### VI — BDI interno — EVIDÊNCIA CONFIRMADA

- oficina: 5% das despesas diretas;
- administração: 5% das despesas diretas;
- outros: sem percentual.

Total: **R$ 8.770,37019238**.

### VII — Financeiras — EVIDÊNCIA CONFIRMADA

- depreciação do equipamento em 60 meses: R$ 16.666,6666667;
- juros de capital de 1% sobre o equipamento: R$ 10.000;
- atrasos de 0,5% sobre despesas diretas: R$ 438,5185096.

Total: **R$ 27.105,1851763**.

### Resumo da dragagem — EVIDÊNCIA CONFIRMADA

- despesas diretas: R$ 87.703,7019238;
- BDI interno: R$ 8.770,37019238;
- financeiras: R$ 27.105,1851763;
- custo mensal: R$ 123.579,257292;
- prazo usado no total: 2 meses, por arredondamento para cima;
- custo total da dragagem: R$ 247.158,514585.

### Cálculos auxiliares de hora à disposição e preço por hora — EVIDÊNCIA CONFIRMADA

O arquivo contém duas áreas auxiliares:

1. `Hora à Disposição`, com custo de R$ 619,1445618.
2. `Preço de Operação por Hora`, com:
   - custo mensal: R$ 123.579,257292;
   - fator de venda: 1,6;
   - preço de venda mensal: R$ 197.726,811668;
   - eficiência operacional: 60%;
   - horas produtivas: 118,8;
   - preço por hora: R$ 1.664,36710158.

A fórmula final de referência também calcula:

```text
custo total ÷ (horas mensais × eficiência)
```

com fatores adicionais de 0,6 e 0,62 em outra célula auxiliar.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- referências simples a `Produção` apresentam `#NAME?` no valor importado em várias células;
- o cabeçalho registra cliente DAAE, divergente de NUTRILOG;
- o cabeçalho registra data de 2021 dentro de proposta de 2025;
- o texto da aba mistura `Canteiro e Operação do Sistema de Desidratação de lodo`, embora não exista pacote de bags/polímero neste arquivo;
- existem estruturas não utilizadas para booster, alojamento, viagens e prêmios;
- percentuais e prazos estão embutidos diretamente em fórmulas;
- o preço de venda por m³ dentro do resumo da aba permanece zero e não é o preço final comercial usado;
- há duas lógicas auxiliares de hora/preço por hora sem explicação suficiente;
- a numeração do título é `7.` apesar de a aba ser a terceira composição no arquivo.

### Dúvidas

- Qual o significado operacional de eficiência 0,9 no combustível versus eficiência 30% na produção?
- O valor de combustível R$ 0,15 é custo por HP-hora, fator histórico ou preço antigo?
- Por que filtros e lubrificantes são rotulados como 10% do combustível, mas usam R$ 4.000 enquanto combustível resulta em R$ 1.069,20?
- A docagem de 1% ao mês é uma provisão anual distribuída ou uma taxa histórica?
- Por que a linha flutuante usa `metros ÷ 12 × 3` para obter peças?
- Por que os acoplamentos usam `(metros ÷ 12) + 2`?
- Qual a finalidade de aplicar 60% e 62% em `D234`?
- Qual das duas áreas de cálculo por hora é efetivamente usada comercialmente?
- Os resíduos DAAE/COPEBRAS/2021 são apenas herança de template?

---

## 6. Aba `4. Desmob. Draga`

### Objetivo

Compor o custo do evento de desmobilização.

### Composição — EVIDÊNCIA CONFIRMADA

Equipe:

- 1 Operador Líder;
- 1 Operador de Draga;
- 4 Ajudantes Gerais;
- refeições e transportes para 6 pessoas.

Parâmetros:

- 9 h/dia;
- leis sociais: 132%;
- custo diário da equipe: R$ 2.411,9448.

Recursos:

- guindaste para carregamento: 1 × R$ 3.000;
- carretas prancha e extensível: quantidades vazias;
- 4 carretas carga seca × R$ 2.000;
- guindaste para descarregamento: quantidade vazia;
- trator D4: quantidade vazia;
- mão de obra: 3 dias × custo diário.

### Resultados — EVIDÊNCIA CONFIRMADA

- subtotal: R$ 18.235,8344;
- BDI interno: 0%;
- preço final: R$ 18.235,8344.

### Evidência de variação em relação à mobilização

A desmobilização não é um espelho da mobilização:

- leis sociais: 132% contra 120%;
- guindaste: R$ 3.000 contra R$ 2.000;
- mão de obra: 3 dias contra 5 dias;
- resultado final distinto.

### Anomalia observada

O título informa `Desmobilização da Draga 6"`, enquanto a mobilização e a aba de dragagem informam draga de 10".

### Dúvida

A indicação de 6" é residual de outro orçamento ou representa equipamento diferente usado na retirada?

---

## 7. Aba `5. Mediçao`

### Objetivo

Compor custos associados à medição técnica e cobertura de risco.

### Itens — EVIDÊNCIA CONFIRMADA

- batimetria: 3 unidades × R$ 22.000 = R$ 66.000;
- seguro de RC: 1 verba × R$ 10.750,597;
- acompanhamento FOS: 1 dia × R$ 1.042.

A equipe diária estruturada inclui:

- 1 Operador Líder;
- 1 Operador de Draga;
- 2 Ajudantes;
- refeições e transporte de 4 pessoas.

Parâmetros de equipe:

- salários menores que os usados nas demais composições;
- 9 h/dia;
- leis sociais: 100%;
- refeição: R$ 30;
- transporte: R$ 10;
- custo diário: R$ 1.042.

### Fórmulas — EVIDÊNCIA CONFIRMADA

- seguro de RC = `8.269,69 × 1,3`;
- acompanhamento FOS usa o custo diário da equipe;
- subtotal = soma dos três itens;
- BDI interno = 0%;
- preço final = subtotal.

### Resultado — EVIDÊNCIA CONFIRMADA

Preço final utilizado: **R$ 77.792,597**.

### Anomalias observadas

- o título numera a composição como `8 - Medição`, embora a aba seja `5. Mediçao`;
- existe um segundo bloco de BDI e preço final nas linhas finais, com valor zero e sem subtotal correspondente;
- os valores-hora de pessoal são diferentes dos usados em mobilização, canteiro, desmobilização e dragagem;
- não há explicação no arquivo para o fator 1,3 aplicado ao seguro.

### Interpretação — EVIDÊNCIA PARCIAL

`Medição` representa um pacote de serviços técnicos da proposta, não o fluxo de boletim de medição do APP.

### Dúvidas

- As 3 batimetrias correspondem a levantamento inicial, intermediário e final?
- O fator 1,3 do seguro é margem, imposto, BDI ou atualização?
- Por que o acompanhamento usa apenas um dia, independentemente das três batimetrias?
- Os salários desta aba são resíduos históricos ou equipe específica contratada para medição?

---

## 8. Aba `6. Plan. Preços`

### Objetivo

Consolidar os custos finais e aplicar BDI comercial por item para formar o preço de venda.

### Itens comercializados — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Custo | Quantidade | Unidade | BDI | Preço total |
| --- | --- | ---: | ---: | --- | ---: | ---: |
| 1 | Mobilização e montagem de Equipamento de Dragagem | R$ 21.521,29 | 1 | un | 50% | R$ 32.281,935 |
| 5 | Dragagem | R$ 247.158,514585 | 6.000 | m3 | 70% | R$ 420.169,474794 |
| 7 | Medição | R$ 77.792,597 | 1 | un | 50% | R$ 116.688,8955 |
| 8 | Desmobilização Equipamento de Dragagem | R$ 18.235,8344 | 1 | un | 50% | R$ 27.353,7516 |

### Fórmulas — EVIDÊNCIA CONFIRMADA

- custo do item = referência à composição de origem;
- custo unitário = custo total ÷ quantidade, quando volumétrico;
- preço unitário = custo unitário × (1 + BDI);
- preço total = quantidade × preço unitário;
- custo total = soma dos custos;
- preço de venda = soma dos preços totais.

### Resultados — EVIDÊNCIA CONFIRMADA

- custo total: **R$ 364.708,235985**;
- preço de venda: **R$ 596.494,056894**;
- custo unitário da dragagem: **R$ 41,19308576/m³**;
- preço unitário de venda da dragagem: **R$ 70,02824580/m³**;
- célula auxiliar `L6`: **R$ 89,47639505/m³**, calculada como `(preço da dragagem + medição) ÷ volume`.

### Interpretações — EVIDÊNCIA PARCIAL

- Mobilização, medição e desmobilização são vendidas como verbas/eventos.
- Dragagem é vendida por metro cúbico.
- O preço auxiliar de R$ 89,4764/m³ parece distribuir dragagem e medição sobre o volume, mas não inclui mobilização e desmobilização.

### Anomalias e dúvidas

- A numeração dos itens salta de 1 para 5, 7 e 8, preservando possível estrutura de template mais amplo.
- Não existe aba de consolidação comercial simplificada neste arquivo.
- Não está explicado por que a dragagem recebe BDI de 70% e os demais itens 50%.
- Não está explicado se o preço auxiliar em `L6` é usado em proposta, negociação ou comparação interna.

---

# Dependências entre abas

## EVIDÊNCIA CONFIRMADA

```text
Dados Obra
├── Produção: dias/mês e volume
├── Mobilização: horas/dia
├── Canteiro: horas/dia
├── Dragagem: dias/mês, recalque total e linha flutuante
└── Desmobilização: horas/dia

Produção
├── Canteiro: prazo arredondado
└── Dragagem:
    ├── horas mensais
    ├── produção mensal
    └── prazo arredondado

Canteiro
└── Dragagem: custo mensal do canteiro

Mobilização
└── Planilha de Preços: custo do item 1

Dragagem
└── Planilha de Preços: custo total do item 5

Medição
└── Planilha de Preços: custo do item 7

Desmobilização
└── Planilha de Preços: custo do item 8
```

# Padrões observados neste arquivo

## 1. Padrão de equipe diária — EVIDÊNCIA PARCIAL

**Fontes:** `1. Mob. Draga`, `2. Canteiro de obras`, `4. Desmob. Draga`, `5. Mediçao`.

```text
quantidade × valor-hora × horas/dia × (1 + leis sociais)
+ refeições
+ transporte
= custo diário
```

O padrão também foi observado no modelo SABESP, mas os percentuais, salários, refeições e composição variam.

## 2. Pacotes de evento único — EVIDÊNCIA PARCIAL

**Fontes:** mobilização, medição e desmobilização.

Esses pacotes geram valor total e são comercializados como `un`.

## 3. Pacote dependente de prazo — EVIDÊNCIA PARCIAL

**Fontes:** `2. Canteiro de obras` e `3. Dragagem`.

O canteiro é apropriado mensalmente e a dragagem multiplica custo mensal pelo prazo arredondado.

## 4. Custo por volume — EVIDÊNCIA PARCIAL

**Fonte:** `6. Plan. Preços`.

O custo total da dragagem é convertido em custo unitário por m³ usando o volume contratado.

## 5. Valor de equipamento como direcionador — EVIDÊNCIA PARCIAL

**Fonte:** `3. Dragagem`.

O valor do equipamento direciona:

- manutenção;
- docagem;
- depreciação;
- juros de capital.

## 6. Linhas opcionais preservadas com quantidade vazia — EVIDÊNCIA PARCIAL

**Fontes:** mobilização, canteiro, dragagem e desmobilização.

A planilha mantém recursos possíveis no template, mas quantidade vazia produz custo zero.

## 7. BDI em múltiplos níveis — EVIDÊNCIA CONFIRMADA

**Fontes:** composições, `3. Dragagem` e `6. Plan. Preços`.

- BDI interno das composições de mobilização, canteiro, medição e desmobilização: 0%;
- BDI interno de oficina e administração em `3. Dragagem`: 10% combinado;
- BDI comercial na planilha final: 50% ou 70%, conforme item.

# Comparação com a base existente

## Evidências já conhecidas e reforçadas

### Produção como ponte entre premissas e prazo

**Fonte nova:** `Produção`.
**Fonte anterior:** `D_004_2026 - SABESP.xlsx`.

Ambos os modelos usam:

```text
vazão × eficiência × concentração = produção horária
produção horária × horas mensais = produção mensal
volume ÷ produção mensal = prazo
```

**Classificação:** EVIDÊNCIA PARCIAL, confiança Nível B candidata após validação, pois agora foi observada em duas fontes, mas os parâmetros variam.

### Mobilização e desmobilização como composições próprias

Os dois arquivos preservam composições separadas, com valores, dias e recursos distintos.

**Classificação:** EVIDÊNCIA PARCIAL, observada em duas fontes.

### Canteiro como custo de suporte dependente da duração

O canteiro é apropriado pelo prazo e consumido pela dragagem nos dois modelos.

**Classificação:** EVIDÊNCIA PARCIAL, observada em duas fontes.

### Centro analítico de custo da dragagem

Ambos possuem grupos de:

- operação;
- pessoal;
- manutenção;
- equipamentos de apoio;
- administrativas;
- BDI;
- financeiras.

**Classificação:** EVIDÊNCIA PARCIAL, observada em duas fontes.

### Consolidação final com BDI comercial por item

Os dois modelos recebem custos das composições e formam preço de venda por item.

**Classificação:** EVIDÊNCIA PARCIAL, observada em duas fontes.

## Novas evidências

### Família sem desaguamento em bags

Este arquivo forma preço apenas com:

- mobilização;
- dragagem;
- medição;
- desmobilização.

Não contém:

- preparo de célula;
- fornecimento de bags;
- sistema de polímero;
- operação de desaguamento;
- desmobilização do sistema de polímero.

**Classificação:** EVIDÊNCIA PARCIAL — possível novo modelo de orçamento.

### Bacia de decantação como destino operacional

A disposição é registrada como `Bacia de Decantaçao`.

**Classificação:** EVIDÊNCIA CONFIRMADA para este orçamento; EVIDÊNCIA PARCIAL como conceito reutilizável.

### Gesso como material/objeto de dragagem

O objeto registra `Dragagem Gesso`.

**Classificação:** EVIDÊNCIA CONFIRMADA para esta fonte.

### Medição com batimetria e seguro de RC de alto peso econômico

Medição corresponde a aproximadamente R$ 77,8 mil de custo e inclui três batimetrias e seguro.

**Classificação:** EVIDÊNCIA CONFIRMADA para esta fonte.

### BDI comercial diferenciado por item

A dragagem recebe 70%, enquanto mobilização, medição e desmobilização recebem 50%.

**Classificação:** EVIDÊNCIA CONFIRMADA para esta fonte; DÚVIDA quanto à regra.

### Linha de recalque apropriada por depreciação e juros

A composição transforma o investimento em tubulação, flutuantes e acoplamentos em custo mensal.

**Classificação:** EVIDÊNCIA CONFIRMADA para esta fonte; EVIDÊNCIA PARCIAL como método reutilizável.

## Evidências distintas, não contraditórias

- O modelo SABESP usa desaguamento em bags; o modelo Nutrilog usa bacia de decantação.
- O modelo SABESP possui consolidação comercial simplificada adicional; o Nutrilog termina na planilha detalhada.
- O modelo SABESP possui várias composições técnicas específicas; o Nutrilog possui quatro itens comerciais.
- Os BDIs e percentuais internos diferem entre modelos.
- As taxas de leis sociais variam entre abas e arquivos.

Essas diferenças são preservadas como modelos e contextos distintos.

# Anomalias globais observadas

## EVIDÊNCIA CONFIRMADA

1. Referências a `Produção` resultam em `#NAME?` em células calculadas do arquivo importado:
   - `2. Canteiro de obras!D25`;
   - `2. Canteiro de obras!F30`;
   - `3. Dragagem!C9`;
   - `3. Dragagem!D225`;
   - `3. Dragagem!H235`;
   - `3. Dragagem!I235`;
   - `3. Dragagem!D246`;
   - `3. Dragagem!J248`.

2. Apesar dos erros exibidos, várias células dependentes preservam valores calculados anteriormente.

3. Existem referências históricas incompatíveis com a identidade atual:
   - COPEBRAS;
   - DAAE;
   - data de 2021;
   - proposta e cliente de 2025.

4. Títulos e numerações não coincidem:
   - `3. Dragagem` tem título `7.`;
   - `4. Desmob. Draga` tem título `8`;
   - `5. Mediçao` tem título `8`;
   - planilha final usa itens 1, 5, 7 e 8.

5. Equipamento divergente:
   - mobilização e dragagem: 10";
   - desmobilização: 6".

6. Há fórmulas com constantes embutidas:
   - 0,6%;
   - 1%;
   - 5%;
   - 0,5%;
   - 60 meses;
   - 10 meses;
   - 1,3;
   - 1,6;
   - 0,6;
   - 0,62;
   - fatores de horas extras 1,7 e 2.

7. Existem linhas de template não utilizadas e células com valores residuais.

Nenhuma dessas anomalias é promovida automaticamente a erro do processo de negócio.

# Conhecimento reutilizável candidato

Todos os itens abaixo permanecem **EVIDÊNCIA PARCIAL, confiança Nível C ou candidata a Nível B**, conforme indicado:

- volume contratual e volume geométrico podem ser conceitos distintos;
- produção depende de vazão, eficiência, concentração e calendário;
- prazo matemático pode ser arredondado para custeio;
- mobilização e desmobilização são eventos com composições próprias;
- canteiro pode ser apropriado mensalmente;
- linhas opcionais podem representar responsabilidade do cliente;
- custo de dragagem combina despesas diretas, BDI interno e financeiras;
- valor do equipamento pode direcionar manutenção, depreciação e juros;
- linha de recalque pode ser custeada por depreciação e juros;
- medição técnica pode constituir item comercial independente;
- itens podem receber BDIs comerciais diferentes;
- proposta pode vender simultaneamente verbas e serviços por volume;
- template histórico pode conter resíduos de obras anteriores e exige rastreabilidade de origem.

# Perguntas para validação futura com o especialista

1. Este modelo representa corretamente uma família chamada `dragagem com bacia de decantação`?
2. A bacia de decantação pertence à Nutrilog ou à FOS?
3. A concentração de 15% refere-se a sólidos em volume, massa ou estimativa operacional?
4. Eficiência de 30% é específica do gesso?
5. O prazo deve sempre ser arredondado para cima nos custos mensais?
6. O canteiro sempre é dividido pelo prazo inteiro?
7. Qual a origem dos percentuais de leis sociais de 100%, 120%, 132%?
8. Por que os salários variam entre as composições?
9. A batimetria ocorre três vezes por regra ou por necessidade desta obra?
10. O seguro de RC usa fator 1,3 por qual motivo?
11. O BDI de 70% da dragagem e 50% dos eventos é uma decisão específica?
12. Qual é o preço unitário usado comercialmente: R$ 70,03/m³, R$ 89,48/m³ ou outro valor com todos os itens distribuídos?
13. A draga correta é 10" ou 6"?
14. As referências DAAE/COPEBRAS/2021 são resíduos de template?
15. Qual a finalidade das duas áreas de cálculo de preço por hora?
16. A taxa de filtros/lubrificantes está correta ou o rótulo `10% combustível` é residual?
17. A linha flutuante realmente utiliza três peças por trecho de 12 m?
18. Os valores de manutenção e docagem devem ser históricos por equipamento?
19. Os itens sem quantidade devem ser preservados como alternativas do orçamento?
20. O arquivo foi efetivamente vendido/executado e existe valor realizado para comparação?

# Resultado da descoberta

## EVIDÊNCIA CONFIRMADA

O arquivo demonstra um orçamento completo de dragagem de gesso com quatro macroitens comerciais e custo final de venda de **R$ 596.494,056894**.

## EVIDÊNCIA PARCIAL

A comparação com o primeiro modelo indica que o Método de Orçamento FOS pode possuir:

- um núcleo comum de premissas, produção, mobilização, canteiro, dragagem, medição, desmobilização e consolidação;
- famílias de processo diferentes conforme o destino e o método de tratamento do material;
- pacotes opcionais específicos de desaguamento;
- composição comercial adaptada a cada obra.

## DÚVIDA

Ainda não há evidência suficiente para definir:

- nomenclatura oficial das famílias;
- quais percentuais são padrões;
- quais itens são obrigatórios;
- quais fórmulas são vigentes;
- quais resíduos históricos devem ser descartados;
- qualquer arquitetura do futuro módulo.

## Próximo passo documental

Analisar os próximos arquivos individualmente, preservando o nome original e comparando cada nova evidência com este documento e com `001_DESAGUAMENTO_BAGS_SABESP.md`.

Nenhuma consolidação definitiva deve ocorrer nesta etapa.
