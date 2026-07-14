# D_011_2025 - SAMAE IBIPORA.xlsx — Registro Independente de Descoberta

## 1. Status da análise

- **Arquivo original:** `D_011_2025 - SAMAE IBIPORA.xlsx`
- **Data da análise:** 14/07/2026
- **Versão do arquivo:** não identificada no nome, nas abas ou nas células inspecionadas
- **Quantidade de abas:** 11
- **Status:** engenharia reversa vertical concluída para o arquivo recebido
- **Escopo:** exclusivamente este Excel
- **Alterações no Excel:** nenhuma
- **Consolidação com outros orçamentos:** não realizada
- **Decisões arquiteturais:** nenhuma
- **Grau de confiança das descobertas reutilizáveis:** Nível C, pois foram observadas em uma única fonte

Todas as abas foram examinadas, incluindo valores, fórmulas, dependências, composições, resultados, observações textuais e anomalias calculadas presentes no arquivo.

## 2. Regra de classificação usada neste registro

| Classificação solicitada | Correspondência documental | Uso neste documento |
| --- | --- | --- |
| **EVIDÊNCIA CONFIRMADA** | Fato observado ou anomalia observada | Informação presente diretamente no Excel ou resultado verificável de suas fórmulas |
| **EVIDÊNCIA PARCIAL** | Interpretação ou hipótese para crosscheck | Leitura conceitual provisória observada somente neste orçamento |
| **DÚVIDA** | Informação insuficiente | Ponto que não pode ser concluído apenas pelo arquivo |

Uma anomalia é classificada como **EVIDÊNCIA CONFIRMADA quanto à sua existência**, sem concluir automaticamente que representa erro de negócio.

## 3. Identidade permanente da fonte

### EVIDÊNCIA CONFIRMADA

- Proposta registrada: `D_011_225`
- Data registrada: 16/02/2025
- Cliente: `SAMAE`
- Contato: `Eloise Vitoria Verlingue da Silva`
- E-mail: não preenchido
- Objeto: `Desassoreamento do Leito de Captação do Ribeirãso Jacutinga`
- Local: `Ibiporã`
- Volume de dragagem informado: 13.100 m³
- Tipo de material: `Areia + Argila`
- Equipamento indicado nas composições: draga de 6"
- Distância total de recalque: 500 m
- Linha flutuante total: 100 m
- Linha de terra: 400 m
- Tipo de bota-fora: `Ensecadeira`
- Sistema de medição: `preços unitários de serviços`
- Responsável pelo canteiro: FOS
- Responsável pela mobilização: FOS
- Jornada: 9 h/dia
- Calendário: 22 dias/mês

### DÚVIDAS

- O código `D_011_225` aparenta omitir um dígito do ano, mas o arquivo não permite afirmar se é erro de digitação ou convenção deliberada.
- O objeto contém a grafia `Ribeirãso Jacutinga`; não é possível concluir pelo Excel se deveria ser `Ribeirão Jacutinga`.
- O arquivo não registra revisão, autor, data-base geral de preços ou histórico de alterações.

## 4. Classificação aparente do orçamento

### EVIDÊNCIA CONFIRMADA

O orçamento representa um serviço de desassoreamento do leito de captação com:

- dragagem hidráulica por draga de 6";
- recalque de 500 m;
- material classificado como areia e argila;
- preparação de área por ensecadeira;
- remoção prévia de vegetação;
- movimentação/transporte da vegetação;
- medição topográfica por área;
- mobilização e desmobilização da draga;
- canteiro de obras;
- composição mensal detalhada da operação de dragagem;
- consolidação comercial por preços unitários de serviços.

### EVIDÊNCIA PARCIAL

O arquivo aparenta representar uma família de orçamento de **dragagem com intervenção terrestre e preparação de área para recebimento do material em ensecadeira**, incluindo atividades preliminares que não pertencem apenas à operação da draga.

Esta classificação permanece específica desta fonte e não constitui padrão geral da FOS.

## 5. Inventário completo das abas

| Ordem | Aba | Dimensão observada | Papel no orçamento |
| --- | --- | --- | --- |
| 1 | `Dados Obra` | A1:H27 | Identidade, premissas técnicas, responsabilidades e jornada |
| 2 | `Produção` | A1:H24 | Produção horária, mensal e prazo matemático |
| 3 | `1. Mob. Draga` | A1:G25 | Mobilização da draga, projetos e montagem |
| 4 | `2. Canteiro` | A1:F28 | Implantação e custo mensal do canteiro |
| 5 | `3. Remoção de Veg` | A1:F20 | Remoção de vegetação com hidrotrator |
| 6 | `4. Prep. Área - Ensecadeira` | A1:G43 | Preparação física da área e formação da ensecadeira |
| 7 | `5. Mov. De Vegetação` | A1:F38 | Escavação, estimativa de volume e transporte da vegetação |
| 8 | `6. Medição` | A1:G38 | Medição topográfica da área da ensecadeira |
| 9 | `7. Dragagem` | A1:L250 | Composição mensal e total do custo de dragagem |
| 10 | `8. Desmob. Draga` | A1:G21 | Desmobilização da draga |
| 11 | `Plan. Preços` | A1:J12 | Consolidação do custo e preço de venda por serviço |

## 6. Fluxo completo observado

```text
Dados Obra
    ├── Produção
    │     ├── prazo da obra
    │     ├── produção mensal
    │     └── horas mensais
    ├── Mobilização
    ├── Canteiro
    ├── Dragagem
    └── Desmobilização

Remoção de vegetação
Preparação da área / ensecadeira
Movimentação de vegetação
Medição
Dragagem
Mobilização
Desmobilização
    └── Plan. Preços
```

### EVIDÊNCIA CONFIRMADA

A apresentação é sequencial, mas a dependência é uma rede:

- `Dados Obra` alimenta `Produção`, mobilização, canteiro, dragagem e desmobilização.
- `Produção` alimenta duração do canteiro, quantidade de horas e duração total da dragagem.
- `2. Canteiro` alimenta a composição mensal da aba `7. Dragagem`.
- As abas de custo alimentam `Plan. Preços`.
- `Plan. Preços` aplica BDI comercial próprio sobre os custos unitários.

---

# 7. Análise por aba

## 7.1 Aba `Dados Obra`

### Objetivo

Registrar a identificação da proposta e as premissas físicas e operacionais da obra.

### Entradas — EVIDÊNCIA CONFIRMADA

- proposta: `D_011_225`;
- data: 16/02/2025;
- cliente: SAMAE;
- contato: Eloise Vitoria Verlingue da Silva;
- e-mail: vazio;
- objeto: desassoreamento do leito de captação do Ribeirãso Jacutinga;
- local: Ibiporã;
- volume: 13.100 m³;
- material: areia + argila;
- distância de recalque: 500 m;
- seio da linha de recalque: 0 m;
- linha flutuante: 100 m;
- seio da linha flutuante: 0 m;
- linha de terra: 400 m;
- profundidade: vazia;
- espessura média: vazia;
- dimensões/área de dragagem: vazias;
- bota-fora: ensecadeira;
- medição: preços unitários de serviços;
- canteiro: FOS;
- mobilização: FOS;
- 9 h/dia;
- 22 dias/mês.

### Fórmulas e resultados — EVIDÊNCIA CONFIRMADA

- `H16 = B16 + E16`: totaliza a distância de recalque; resultado 500 m.
- `H17 = B17 + E17`: totaliza a linha flutuante; resultado 100 m.
- `G21 = B21 × D21 × B20`: calcula volume geométrico pela área/dimensões e espessura; resultado 0 porque as entradas estão vazias.

### Entidades conceituais

- proposta;
- cliente;
- contato;
- obra;
- local;
- volume;
- material;
- linha de recalque;
- linha flutuante;
- linha terrestre;
- profundidade;
- espessura;
- área;
- bota-fora;
- sistema de medição;
- responsabilidade;
- jornada;
- calendário.

### Regras implícitas — EVIDÊNCIA PARCIAL

- O volume informado e o volume geométrico calculável coexistem como conceitos distintos.
- A linha total pode incluir uma parcela denominada `seio da linha`.
- Canteiro e mobilização possuem responsáveis explícitos.
- Jornada e dias úteis funcionam como premissas globais.

### Dúvidas

- Quando o volume geométrico deve substituir ou validar o volume informado?
- Qual é a finalidade operacional do `seio da linha`?
- Como as composições mudam quando canteiro ou mobilização não são responsabilidade da FOS?
- Profundidade e espessura não são necessárias neste caso ou apenas ficaram pendentes?

---

## 7.2 Aba `Produção`

### Objetivo

Converter parâmetros de bombeamento e calendário em produção útil e prazo de execução.

### Entradas — EVIDÊNCIA CONFIRMADA

- vazão: 120 m³/h;
- eficiência: 80%;
- concentração: 15%;
- horas/dia: 9;
- dias/mês: 22;
- volume: 13.100 m³.

### Fórmulas — EVIDÊNCIA CONFIRMADA

- `H3 = 'Dados Obra '!B26`
- `H4 = 'Dados Obra '!B27`
- `H6 = H3 × H4`
- `D8 = D3 × (D4/100) × (D5/100)`
- `D11 = H6`
- `D13 = D8 × D11`
- `D18 = D13`
- `D21 = 'Dados Obra '!B14`
- `D24 = D21 ÷ D18`

### Finalidade operacional

- horas mensais = horas/dia × dias/mês;
- produção útil por hora = vazão × eficiência × concentração;
- produção mensal = produção útil por hora × horas mensais;
- prazo = volume total ÷ produção mensal.

### Resultados — EVIDÊNCIA CONFIRMADA

- 198 h/mês;
- 14,4 m³/h;
- 2.851,2 m³/mês;
- prazo matemático: 4,5945566779 meses.

### Regra implícita — EVIDÊNCIA PARCIAL

Eficiência e concentração são aplicadas como fatores multiplicativos independentes sobre a vazão nominal.

### Anomalia observada — EVIDÊNCIA CONFIRMADA

As fórmulas referenciam `'Dados Obra '` com espaço final, enquanto o nome inspecionado da aba é `Dados Obra`. O arquivo preserva valores calculados em algumas células, mas a divergência nominal é relevante e reaparece em outras abas.

### Dúvidas

- A vazão de 120 m³/h é nominal, histórica ou ajustada às condições desta obra?
- A eficiência de 80% e a concentração de 15% foram escolhidas para areia + argila?
- O prazo comercial deve usar 4,5946 meses, 5 meses ou incluir margem adicional?

---

## 7.3 Aba `1. Mob. Draga`

### Objetivo

Compor o custo único de mobilização da draga de 6", incluindo transporte, projetos e montagem.

### Mão de obra — EVIDÊNCIA CONFIRMADA

Equipe diária:

- 2 operadores de draga a R$ 28/h;
- 2 ajudantes gerais a R$ 10,75/h;
- 4 refeições a R$ 50;
- 4 transportes a R$ 10;
- 9 h/dia;
- leis sociais de 120%.

Fórmula do pessoal:

```text
quantidade × valor-hora × horas/dia × (1 + leis sociais/100)
```

Custo diário calculado: **R$ 1.774,50**.

### Serviços e recursos — EVIDÊNCIA CONFIRMADA

- guindaste para carregamento: quantidade vazia, R$ 1.000/dia;
- carreta prancha rebaixada: quantidade e preço vazios;
- carreta extensível: quantidade e preço vazios;
- carreta carga seca para draga: 3 × R$ 10.000 = R$ 30.000; observação `Fabiano`;
- guindaste para descarregamento e montagem: 1 × R$ 7.500; observação `Chute`;
- projeto básico: 1 × R$ 15.000;
- projeto executivo: 1 × R$ 30.000;
- trator D4: quantidade e preço vazios;
- mão de obra: 5 dias × R$ 1.774,50 = R$ 8.872,50.

### Fórmulas relevantes

- custos de mão de obra por função;
- total de refeições e transportes pela quantidade de pessoas;
- `F9 = SOMA(F5:F8)`;
- cada serviço: quantidade × preço unitário;
- `E22 = F9`, levando o custo diário à linha da mão de obra;
- `F23 = SOMA(F14:F22)`;
- BDI interno = subtotal × percentual;
- preço final = subtotal + BDI.

### Resultado — EVIDÊNCIA CONFIRMADA

- subtotal: R$ 91.372,50;
- BDI interno: 0%;
- preço final: R$ 91.372,50.

### Dúvidas

- Projetos básico e executivo pertencem sempre à mobilização ou apenas a este contrato?
- Os preços de R$ 10.000 por carreta e R$ 7.500 por guindaste são cotações datadas ou estimativas?
- A observação `Chute` indica ausência de cotação?
- Por que o guindaste de carregamento e o trator D4 permanecem sem quantidade?

---

## 7.4 Aba `2. Canteiro`

### Objetivo

Compor implantação e operação do canteiro e converter o custo total em custo mensal para a dragagem.

### Mão de obra — EVIDÊNCIA CONFIRMADA

Repete a equipe e o custo diário da mobilização:

- 2 operadores;
- 2 ajudantes;
- 4 refeições;
- 4 transportes;
- custo diário: R$ 1.774,50.

### Itens — EVIDÊNCIA CONFIRMADA

- container almoxarifado: R$ 1.000/mês;
- banheiro químico: R$ 950/mês;
- transferência com Munck: quantidade vazia × R$ 1.000;
- frete para containers: 2 × R$ 500;
- PPRA + PCMSO + LTCAT: 1 × R$ 2.000;
- ART principal + ARTs de corresponsabilidade: 1 × R$ 500;
- placa de obra: 1 × R$ 3.000;
- gerador, locação + diesel: quantidade vazia × R$ 7.000;
- água potável: 48 × R$ 20;
- material de escritório: R$ 200/mês;
- montagem/desmontagem: 5 dias × R$ 1.774,50.

### Regras e fórmulas — EVIDÊNCIA CONFIRMADA

- duração dos itens mensais = `ARREDONDAR.PARA.CIMA(prazo, 0) + 1`;
- água = `2 × 4 × duração do container`;
- custo total = soma dos itens;
- `Meses` repete a duração arredondada + 1;
- preço final mensal = custo total ÷ meses.

### Valores preservados no arquivo

- custo total: R$ 29.232,50;
- preço final mensal: R$ 4.872,083333.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- `D14`, `D15`, `D23` e `F26` aparecem como `#NAME?`.
- As fórmulas usam `ROUNDUP`, mas os valores calculados indicam duração de 6 meses.
- O total de R$ 29.232,50 e o custo mensal de R$ 4.872,083333 permanecem armazenados apesar dos erros exibidos nas células de duração.
- O título da aba diz `CANTEIRO DE OBRAS : subitem da Dragagem`, confirmando que o custo mensal é incorporado à dragagem.

### Dúvidas

- O mês adicional representa mobilização/desmobilização, margem de prazo ou período administrativo?
- O custo total deve incluir todos os seis meses dos itens mensais quando as fórmulas são recalculadas?
- Por que o preço final é custo mensal e não subtotal + BDI, como nas demais abas?

---

## 7.5 Aba `3. Remoção de Veg`

### Objetivo

Compor a remoção de vegetação por hidrotrator, incluindo mobilização/desmobilização e mão de obra.

### Itens — EVIDÊNCIA CONFIRMADA

- hidrotrator: 1 mês × R$ 92.000;
- mobilização/desmobilização: 1 verba × R$ 50.000;
- mão de obra: 5 dias × R$ 1.774,50 = R$ 8.872,50.

### Resultado — EVIDÊNCIA CONFIRMADA

- subtotal: R$ 150.872,50;
- divisor `Unitario`: 1;
- BDI interno: 0%;
- preço final: R$ 150.872,50.

### Regras e fórmulas

- o custo diário de equipe é calculado, embora a linha usada na composição apenas importe esse custo;
- total = soma dos itens;
- preço final = total ÷ `Unitario`.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- O título principal ainda diz `CANTEIRO DE OBRAS : subitem da Dragagem`, apesar de a composição tratar de remoção de vegetação.
- A numeração do item de mão de obra é `11`, embora existam apenas três linhas de serviço.
- `Unitario = 1` não altera o valor e sua finalidade não é explicitada.

### Dúvidas

- O hidrotrator executa exclusivamente a remoção ou também movimenta o material?
- A mobilização/desmobilização de R$ 50.000 pertence ao hidrotrator?
- Qual é a unidade comercial pretendida para este serviço?

---

## 7.6 Aba `4. Prep. Área - Ensecadeira`

### Objetivo

Compor a preparação da área de disposição e registrar cálculos auxiliares de volume e produtividade.

### Equipe — EVIDÊNCIA CONFIRMADA

- 2 operadores de draga;
- 6 ajudantes gerais;
- 8 refeições;
- 8 transportes;
- custo diário: R$ 2.865,90.

### Itens da composição — EVIDÊNCIA CONFIRMADA

- regularização manual: 10 dias × R$ 2.865,90 = R$ 28.659,00;
- escavadeira hidráulica sem frete: 16 dias × R$ 3.000 = R$ 48.000; observação `Danilo 2500 curitiba`;
- trator para limpeza do terreno + acesso: 3 dias × R$ 2.500 = R$ 7.500;
- tubulação para drenagem: 100 m × R$ 15 = R$ 1.500;
- mão de obra: 15 dias × R$ 2.865,90 = R$ 42.988,50.

### Resultado

- subtotal: R$ 128.647,50;
- BDI interno: 0%;
- preço final: R$ 128.647,50.

### Cálculos auxiliares — EVIDÊNCIA CONFIRMADA

Bloco TCPO:

- 1 m³ corresponde a 0,0484 h;
- 1.248 m³ corresponde a 60,4032 h;
- a 8 h/dia, corresponde a 7,5504 dias.

Bloco geométrico textual:

- área: 10.848,98 m²;
- perímetro: 400 m;
- volume: 10.848,98 × 1,25 = 13.561 m³;
- seção de leira: 1,25 × 1,25 = 1,56; duplicada = 3,12 m²;
- volume da leira: 3,12 × 400 = 1.248 m³.

Bloco de limpeza do terreno:

- coeficiente: 0,001 h/m²;
- área: 18.000 m²;
- resultado: 18 h.

### Regras implícitas — EVIDÊNCIA PARCIAL

- A ensecadeira é dimensionada por perímetro e seção da leira.
- O volume de preparação considera uma camada de 1,25 m sobre a área.
- A produtividade pode ser referenciada a composição TCPO.
- A escavadeira e o trator são estimados por dias inteiros.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- O título usa `Caixa`, enquanto a aba e a consolidação comercial usam `Ensecadeira`.
- A observação indica cotação de Danilo por R$ 2.500 em Curitiba, mas o preço unitário usado é R$ 3.000.
- O volume textual de 13.561 m³ é próximo, mas não igual, ao volume de dragagem de 13.100 m³.
- A quantidade comercial de ensecadeira em `Plan. Preços` é 1.800 m³, diferente dos volumes auxiliares de 1.248 m³ e 13.561 m³.

### Dúvidas

- A quantidade comercial de 1.800 m³ representa volume de leira, volume movimentado ou margem?
- O coeficiente TCPO de 0,0484 h/m³ é aplicado apenas à regularização manual?
- A camada de 1,25 m é altura da ensecadeira, espessura de preparo ou profundidade da caixa?
- O preço de escavadeira foi majorado deliberadamente sobre a referência de R$ 2.500?

---

## 7.7 Aba `5. Mov. De Vegetação`

### Objetivo

Estimar o volume de vegetação, sua redução por secagem, a quantidade de viagens e o custo de transporte.

### Composição principal — EVIDÊNCIA CONFIRMADA

- escavadeira: 15 diárias × R$ 2.500 = R$ 37.500;
- movimentação do volume da ensecadeira: 76 viagens × R$ 585 = R$ 44.460;
- total e preço final: R$ 81.960;
- BDI interno: 0%.

### Cálculo auxiliar — EVIDÊNCIA CONFIRMADA

Áreas:

- lagoa: 2.270 m²;
- bacia: 8.000 m².

Volume inicial:

```text
2.270 × 0,3 + 8.000 × 0,2 = 2.281 m³
```

Volume após perda por secagem:

```text
2.281 × 0,499 = 1.138,219 m³
```

Viagens de caminhão de 15 m³:

```text
1.138,219 ÷ 15 = 75,8812667 viagens
```

Preço de referência:

- R$ 450 por viagem, atribuído a `Danilo em Curitina`.

Preço com margem:

```text
R$ 450 × 1,3 = R$ 585 por viagem
```

Custo calculado sem arredondamento:

```text
R$ 585 × 75,8812667 = R$ 44.390,541
```

A composição usa 76 viagens e totaliza R$ 44.460.

### Regras implícitas — EVIDÊNCIA PARCIAL

- A vegetação é convertida em volume usando espessuras distintas: 0,30 m na lagoa e 0,20 m na bacia.
- A perda de volume por exposição ao sol é representada pelo fator 0,499.
- O caminhão é considerado com capacidade de 15 m³.
- A cotação de transporte recebe margem de 30%.
- A quantidade de viagens é arredondada para cima.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- A equipe diária possui vários campos zerados ou vazios e não influencia o preço final.
- A linha de ajudante geral tem quantidade vazia, não zero.
- Há grafias `Curitina` e `Portnto`.
- A célula de observação identifica o custo como `Chutado`.
- O título diz `Transporte Vegetaçao até 10KM`, estabelecendo um limite de distância que não aparece como parâmetro variável.
- A linha do item chama `Movimentação volume ensecadeira`, embora o bloco auxiliar calcule volume de vegetação.

### Dúvidas

- O fator 0,499 deriva de experiência, medição ou estimativa?
- As espessuras de 0,30 m e 0,20 m representam altura média real da vegetação?
- O custo de 76 viagens inclui carga, descarga, disposição e distância máxima de 10 km?
- A escavadeira de 15 dias executa carga, escavação ou ambas?

---

## 7.8 Aba `6. Medição`

### Objetivo

Compor o custo de topografia para medição volumétrica da ensecadeira.

### Item principal — EVIDÊNCIA CONFIRMADA

- topografia: 11.000 m² × R$ 3,65 = R$ 40.150;
- observação: `Chute - para retornar 6 vezes e fazer o levantamento`;
- texto adicional: serão 6 visitas, preço aparentemente negociável;
- texto adicional: `nao fiz cotaçao`.

### Resultado — EVIDÊNCIA CONFIRMADA

- total: R$ 40.150;
- BDI interno: 0%;
- a célula `Preço Final` mostra R$ 86.100.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- O preço final de R$ 86.100 não possui fórmula identificada e diverge do total de R$ 40.150.
- A planilha comercial usa o custo de R$ 40.150, não o `Preço Final` de R$ 86.100.
- O bloco auxiliar das linhas 27 a 38 é cópia do cálculo de vegetação e transporte da aba anterior, sem vínculo com a medição.
- A equipe diária está zerada/vazia e não participa da composição.
- O texto confirma ausência de cotação.
- A quantidade usada comercialmente em `Plan. Preços` é 10.848,98 m², enquanto esta aba calcula custo para 11.000 m².

### Dúvidas

- O valor de R$ 86.100 é resíduo, proposta comercial anterior ou valor digitado deliberadamente?
- As seis visitas são obrigatórias para o método de medição?
- A unidade correta é área levantada, visita, campanha ou verba?
- A quantidade de 11.000 m² é arredondamento da área de 10.848,98 m²?

---

## 7.9 Aba `7. Dragagem`

### Objetivo

Compor o custo mensal da operação de dragagem, somar despesas diretas, BDI interno e financeiras, calcular custo unitário, preço de venda e custo total pelo prazo.

### Observações de identidade preservadas — EVIDÊNCIA CONFIRMADA

A aba contém cabeçalho legado:

- referência: `Rio Jaguari`;
- data: 26/06/2018;
- cliente: `Santher`;
- equipamento: draga 6";
- observação: inicialmente pensada draga de 10", mas o local não permitiria por dimensões;
- valor do equipamento `no estado`: R$ 150.000.

Essas informações divergem da obra SAMAE e indicam reutilização de um modelo anterior.

### I — Operação

Entradas:

- horas mensais: referência a `Produção!H6`;
- eficiência: 0,9;
- consumo/hora: 9;
- combustível: R$ 7 por unidade.

Fórmulas:

- combustível = horas × eficiência × consumo/h × valor combustível;
- filtros/lubrificantes = 10% do combustível;
- fretes e carretos: R$ 1.000;
- segurança e uniformes: R$ 500.

Resultados preservados:

- combustível: R$ 11.226,60;
- filtros: R$ 1.122,66;
- operação total: R$ 13.849,26.

### II — Pessoal

#### Salários

Horas mensais calculadas no bloco lateral:

- horas extras 70%: 0;
- horas extras 100%: 0;
- horas normais: 7,33333 × 30 = 219,9999;
- total a receber: 219,9999 h.

Equipe efetivamente valorizada:

- 2 operadores de draga × R$ 28/h;
- 2 ajudantes × R$ 10,75/h.

Salários totais: R$ 17.049,99225.

#### Encargos sociais

- taxa: 120%;
- base: salários;
- resultado: R$ 20.459,99070.

#### Cantina

Tabela efetiva:

- 2 funcionários alojados: café R$ 3,50 + almoço R$ 25 + jantar R$ 25, por 30 dias = R$ 3.210;
- 2 funcionários da cidade: café R$ 3,50 + almoço R$ 25, por 22 dias = R$ 1.254;
- total: R$ 4.464.

O bloco textual anterior ainda lista valores antigos: almoço 10, café 2,50, lanche 2,50 e jantar 10.

#### Alojamento

- aluguel: R$ 2.500;
- água e luz: R$ 100;
- limpeza: R$ 100;
- total: R$ 2.700.

#### Viagens nas folgas

- 1 funcionário × R$ 500;
- total: R$ 500.

#### Prêmios de produção

- estrutura existente, sem quantidades ou valores;
- total zero.

#### Total de pessoal

- R$ 45.173,98295.

### III — Manutenção

- peças e acessórios: 0,6% a.m. sobre R$ 150.000 = R$ 900;
- docagem anual: 1,0% a.m. sobre R$ 150.000 = R$ 1.500;
- limpeza e pintura: R$ 500;
- mão de obra de terceiros: R$ 500;
- total: R$ 3.400.

### IV — Equipamentos de apoio

Itens do bloco mensal:

- linha de recalque: R$ 6.678;
- rebocador e cábrea: zero;
- pick-up: zero;
- caminhão: vazio;
- automóvel: R$ 4.000, descrito como locação + combustível;
- máquina de solda: zero;
- outros: zero;
- ferramentas: R$ 300;
- canteiro: R$ 4.872,083333, importado de `2. Canteiro`.

Total: R$ 15.850,083333.

#### Subcomposição da linha de recalque

Tubulação:

- 500 m × R$ 120 = R$ 60.000;
- depreciação em 12 meses = R$ 5.000/mês;
- juros de 1% = R$ 600;
- custo mensal: R$ 5.600.

Flutuantes:

- 25 peças × R$ 200 = R$ 5.000;
- depreciação em 12 meses = R$ 416,666667;
- juros de 1% = R$ 50;
- custo mensal: R$ 466,666667.

Acoplamentos:

- 43,6666667 peças × R$ 150 = R$ 6.550;
- depreciação em 12 meses = R$ 545,833333;
- juros de 1% = R$ 65,50;
- custo mensal: R$ 611,333333.

Total mensal da linha: R$ 6.678.

### V — Administrativas

- comissões: zero;
- viagens de inspeção: R$ 4.000;
- viagens administrativas: zero;
- comunicações: R$ 300;
- seguro e licenciamento: vazio;
- total: R$ 4.300.

### Total de despesas diretas

```text
Operação + Pessoal + Manutenção + Equipamentos de apoio + Administrativas
```

Resultado: **R$ 82.573,326283/mês**.

### VI — BDI interno

- oficina: 5% das despesas diretas = R$ 4.128,666314;
- administração: 5% = R$ 4.128,666314;
- outros: vazio;
- total: R$ 8.257,332628.

### VII — Financeiras

- depreciação em 60 meses sobre R$ 150.000 = R$ 2.500;
- juros de capital de 1% = R$ 1.500;
- atrasos: vazio;
- total: R$ 4.000.

### Resumo mensal

- despesas diretas: R$ 82.573,326283;
- BDI interno: R$ 8.257,332628;
- financeiras: R$ 4.000;
- custo mensal total: R$ 94.830,658912.

### Produção, custo unitário e venda

- produção prevista: referência a `Produção!D13`;
- custo unitário = custo mensal ÷ produção mensal;
- valor preservado: R$ 33,259911/m³;
- BDI de venda da aba: 35%;
- preço de venda: R$ 44,900880/m³.

### Hora à disposição

- valor: R$ 356,333385;
- bloco lateral usa 22 dias × 9 h = 198 h;
- outro bloco calcula preço de operação/hora com:
  - custo mensal R$ 94.830,658912;
  - multiplicador BDI 1,5;
  - preço mensal R$ 142.245,988368;
  - horas trabalhadas/mês;
  - eficiência de operação 0,75;
  - horas produtivas 148,5;
  - preço/hora R$ 957,885444.

### Total da dragagem

- custo mensal: R$ 94.830,658912;
- tempo: `ARREDONDAR.PARA.CIMA(Produção!D24,0)`;
- duração preservada: 5 meses;
- custo total: R$ 474.153,294558.

### Fórmulas estruturantes — EVIDÊNCIA CONFIRMADA

- `G181 = E178 + D161 + H146 + G87 + E15`: soma grandes grupos;
- `E185 = G181 × 5%`;
- `E186 = G181 × 5%`;
- `E189 = E185 + E186`;
- `E192 = F7 ÷ 60`: depreciação;
- `E193 = F7 × 1%`: juros;
- `D215 = G181`;
- `D218 = E189`;
- `D220 = E196`;
- `D222 = D215 + D218 + D220`;
- `D225 = Produção!D13`;
- `D227 = D222 ÷ D225`;
- `D231 = D227 × B229 + D227`;
- `D246 = ARREDONDAR.PARA.CIMA(Produção!D24,0)`;
- `D247 = D245 × D246`.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- Cabeçalho e observações pertencem a Rio Jaguari/Santher, não à obra SAMAE.
- `C9`, `D225`, `H235`, `I235`, `D246` e `J247` aparecem como `#NAME?`.
- As fórmulas dependentes de `Produção` preservam valores calculados em células posteriores, indicando cache anterior ou recálculo parcial.
- O cálculo de horas salariais usa 7,33333 h/dia × 30 dias = 219,9999 h, diferente da jornada global de 9 h/dia × 22 dias = 198 h.
- A eficiência de combustível é 90%, a eficiência de produção é 80% e a eficiência operacional horária é 75%; são três conceitos distintos sem explicação.
- O bloco de refeições contém uma tabela antiga e outra efetivamente utilizada com valores diferentes.
- A linha de recalque usa 500 m, coerente com a distância total, mas a observação menciona tubulação de 8" FGS enquanto a draga é de 6".
- O custo mensal do canteiro é importado apesar das células de duração com erro.
- Existem dois BDI internos de 5% e um BDI de venda de 35%; a planilha comercial aplica ainda outro BDI de 100%.
- `D245 = SOMA(D244:D244)` e `D248 = SOMA(D247:D247)` são somas de uma única célula.
- O custo total de dragagem usa prazo inteiro de 5 meses, não o prazo matemático de 4,5946.
- O volume usado na `Plan. Preços` para dragagem é 13.000 m³, não 13.100 m³.

### Dúvidas

- Quais informações legadas do cabeçalho ainda têm função?
- Qual das três eficiências deve ser interpretada como disponibilidade, utilização ou rendimento?
- A equipe opera todos os dias do mês ou somente 22 dias?
- O valor do equipamento de R$ 150.000 é histórico, contábil ou valor de reposição?
- Por que o BDI de venda interno é 35%, enquanto a consolidação comercial usa 100%?
- A tubulação deve ser dimensionada pelo diâmetro da draga ou por outra condição hidráulica?
- Qual é a definição contratual da hora à disposição?

---

## 7.10 Aba `8. Desmob. Draga`

### Objetivo

Compor o custo único de retirada, carga, transporte e desmontagem da draga.

### Equipe — EVIDÊNCIA CONFIRMADA

- 2 operadores de draga a R$ 15/h;
- 2 ajudantes a R$ 8/h;
- 4 refeições a R$ 30;
- 4 transportes a R$ 10;
- 9 h/dia;
- leis sociais de 120%;
- custo diário: R$ 1.070,80.

### Itens

- guindaste para carregamento: 1 × R$ 1.000;
- carreta carga seca: 3 × R$ 10.000; observação `Genival (25/06/18)`;
- guindaste para descarregamento/montagem: 1 × R$ 7.500;
- trator D4: quantidade e preço vazios; observação `Terraplenagem Lavoro`;
- mão de obra: 3 dias × R$ 1.070,80 = R$ 3.212,40.

### Resultado

- subtotal: R$ 41.712,40;
- BDI interno: 0%;
- preço final: R$ 41.712,40.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- O texto do guindaste diz `descarregamento e montagem` dentro da desmobilização.
- Salários, refeição e transporte são inferiores aos da mobilização.
- A cotação `Genival (25/06/18)` é explicitamente antiga em relação à proposta de 2025.
- A mobilização inclui projetos; a desmobilização não.
- O custo de transporte por carreta é idêntico ao da mobilização.

### Dúvidas

- A assimetria salarial entre mobilização e desmobilização é deliberada?
- O guindaste deveria ser descrito como carregamento/desmontagem?
- Os valores de 2018 foram atualizados ou apenas reutilizados?

---

## 7.11 Aba `Plan. Preços`

### Objetivo

Consolidar custos, quantidades, custos unitários, BDI comercial, preços unitários e preços totais.

### Estrutura — EVIDÊNCIA CONFIRMADA

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

Fórmulas gerais:

```text
custo unitário = custo total ÷ quantidade
preço unitário = custo unitário × (1 + BDI/100)
preço total = quantidade × preço unitário
```

### Itens comerciais

| Serviço | Custo total | Quantidade | Unidade | Custo unitário | BDI | Preço total |
| --- | ---: | ---: | --- | ---: | ---: | ---: |
| Mobilização | R$ 91.372,50 | 1 | vb | R$ 91.372,50 | 100% | R$ 182.745,00 |
| Remoção de vegetação | R$ 150.872,50 | 1 | vb | R$ 150.872,50 | 100% | R$ 301.745,00 |
| Movimentação de vegetação | R$ 81.960,00 | 1.138,219 | m³ | R$ 72,007232 | 100% | R$ 163.920,00 |
| Ensecadeira | R$ 128.647,50 | 1.800 | m³ | R$ 71,470833 | 100% | R$ 257.295,00 |
| Dragagem | R$ 474.153,294558 | 13.000 | m³ | R$ 36,473330 | 100% | R$ 948.306,589117 |
| Medição | R$ 40.150,00 | 10.848,98 | m² | R$ 3,700809 | 100% | R$ 80.300,00 |
| Desmobilização | R$ 41.712,40 | 1 | vb | R$ 41.712,40 | 100% | R$ 83.424,80 |

### Totais — EVIDÊNCIA CONFIRMADA

- custo total mostrado: R$ 927.005,794558;
- preço de venda: R$ 2.017.736,389117.

### Fórmulas e dependências

- mobilização recebe `1. Mob. Draga!F25`;
- remoção recebe `3. Remoção de Veg!F20`;
- movimentação recebe `5. Mov. De Vegetação!F24`;
- quantidade de movimentação recebe o volume pós-secagem;
- ensecadeira recebe `4. Prep. Área - Ensecadeira!F22`;
- dragagem recebe `7. Dragagem!D247`;
- medição recebe `6. Medição!F22`;
- desmobilização recebe `8. Desmob. Draga!F21`;
- preço de venda total soma todos os itens.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- `C12 = SOMA(C5:C9)`: o custo total exclui medição e desmobilização.
- O preço de venda `J12 = SOMA(J5:J11)` inclui todos os itens.
- Portanto, o total de custo exibido não é comparável diretamente ao total de venda.
- A referência de mobilização usa nome de aba com espaço final: `'1. Mob. Draga '!F25`.
- A dragagem usa 13.000 m³, enquanto `Dados Obra` informa 13.100 m³.
- A ensecadeira usa 1.800 m³, sem fórmula de origem.
- A medição usa 10.848,98 m², enquanto sua composição foi calculada para 11.000 m².
- Todos os itens recebem BDI de 100%, inclusive a dragagem que já contém BDI interno de 10%, financeiras e uma referência de venda de 35%.
- A numeração comercial apresenta apenas `1.2` para mobilização e `2.1` para dragagem; os demais itens ficam sem código.
- Não existe item comercial separado para canteiro; ele está incorporado na dragagem.

### Reconstituição do custo total completo — EVIDÊNCIA CONFIRMADA

Somando também medição e desmobilização:

```text
R$ 927.005,794558
+ R$ 40.150,00
+ R$ 41.712,40
= R$ 1.008.868,194558
```

Com BDI uniforme de 100%, esse total produziria R$ 2.017.736,389117, exatamente o preço de venda mostrado.

Isso confirma que o preço de venda inclui todos os itens e corresponde a duas vezes o custo completo, enquanto a célula `Custo Total` omite os dois últimos itens.

---

# 8. Dependências entre abas

## EVIDÊNCIA CONFIRMADA

| Origem | Destino | Informação |
| --- | --- | --- |
| `Dados Obra` | `Produção` | horas/dia, dias/mês, volume |
| `Dados Obra` | `1. Mob. Draga` | horas/dia |
| `Dados Obra` | `2. Canteiro` | horas/dia |
| `Dados Obra` | `4. Prep. Área - Ensecadeira` | horas/dia |
| `Dados Obra` | `7. Dragagem` | dias/mês, linha total, linha flutuante |
| `Dados Obra` | `8. Desmob. Draga` | horas/dia |
| `Produção` | `2. Canteiro` | prazo arredondado |
| `Produção` | `7. Dragagem` | horas mensais, produção mensal, prazo |
| `2. Canteiro` | `7. Dragagem` | custo mensal do canteiro |
| abas de composição | `Plan. Preços` | custos totais e quantidades |

## EVIDÊNCIA PARCIAL

As abas `3. Remoção de Veg`, `4. Prep. Área - Ensecadeira`, `5. Mov. De Vegetação` e `6. Medição` são pacotes de serviço relativamente independentes, unidos comercialmente na consolidação final.

---

# 9. Entidades conceituais encontradas

### EVIDÊNCIA CONFIRMADA

- proposta;
- cliente;
- contato;
- obra;
- local;
- objeto;
- material dragado;
- volume contratual;
- volume geométrico;
- equipamento de dragagem;
- linha de recalque;
- linha flutuante;
- linha terrestre;
- bota-fora;
- ensecadeira;
- vegetação;
- canteiro;
- mobilização;
- desmobilização;
- produção;
- prazo;
- jornada;
- equipe;
- função;
- salário/hora;
- leis sociais;
- refeição;
- transporte;
- recurso/equipamento de apoio;
- serviço;
- fornecedor/referência de preço;
- cotação;
- quantidade;
- unidade;
- custo unitário;
- custo total;
- BDI;
- preço unitário;
- preço total;
- medição;
- topografia;
- visita de levantamento;
- despesa direta;
- despesa financeira;
- depreciação;
- juros;
- manutenção;
- produtividade;
- hora à disposição.

---

# 10. Regras de negócio observadas

## EVIDÊNCIA CONFIRMADA

1. Produção útil = vazão × eficiência × concentração.
2. Produção mensal = produção útil horária × horas/dia × dias/mês.
3. Prazo matemático = volume ÷ produção mensal.
4. Durações mensais dependentes usam arredondamento para cima.
5. O canteiro adiciona um mês ao prazo arredondado.
6. Mão de obra diária inclui quantidade, salário/hora, horas/dia e leis sociais.
7. Refeição e transporte são tratados por número de pessoas.
8. Mobilização e desmobilização são eventos de verba/quantidade única.
9. O volume de vegetação é estimado por área × espessura.
10. A secagem da vegetação reduz o volume pelo fator 0,499.
11. Viagens = volume pós-secagem ÷ 15 m³, arredondadas para cima.
12. O frete de referência recebe margem de 30%.
13. A ensecadeira utiliza cálculo por seção × perímetro e referências TCPO.
14. A dragagem é composta mensalmente por operação, pessoal, manutenção, apoio, administrativas, BDI interno e financeiras.
15. O custo total da dragagem = custo mensal × prazo inteiro.
16. O preço comercial de cada item = custo unitário × (1 + BDI).
17. O BDI comercial final é 100% para todos os itens.
18. O canteiro não aparece como item comercial separado; compõe o custo mensal da dragagem.
19. Medição é comercializada por m².
20. Movimentação de vegetação e ensecadeira são comercializadas por m³.
21. Mobilização, remoção de vegetação e desmobilização são comercializadas por verba.

## EVIDÊNCIA PARCIAL

- O mês adicional do canteiro pode representar implantação e retirada.
- O BDI de 100% pode funcionar como markup comercial global, e não apenas BDI técnico.
- Valores anotados como `chute` ou sem cotação podem ser usados como provisórios para fechar o orçamento.
- A planilha preserva blocos legados como memória de cálculo, mesmo quando não participam diretamente do resultado atual.

---

# 11. Coeficientes, margens e parâmetros observados

Todos os itens abaixo são **EVIDÊNCIA CONFIRMADA quanto à presença neste arquivo** e **Nível C quanto à reutilização**.

| Parâmetro | Valor | Contexto |
| --- | ---: | --- |
| Eficiência de produção | 80% | Produção da draga |
| Concentração | 15% | Produção da draga |
| Eficiência de combustível | 90% | Custo operacional |
| Eficiência operacional horária | 75% | Preço/hora |
| Leis sociais | 120% | Mobilização, canteiro, ensecadeira, desmobilização |
| Leis sociais em blocos não usados | 110% | Movimentação e medição |
| Filtros/lubrificantes | 10% | Sobre combustível |
| Manutenção de peças | 0,6% a.m. | Sobre valor do equipamento |
| Docagem | 1,0% a.m. | Sobre valor do equipamento |
| Depreciação | 60 meses | Draga |
| Juros de capital | 1% a.m. | Draga e linha |
| BDI oficina | 5% | Despesas diretas |
| BDI administração | 5% | Despesas diretas |
| BDI de venda interno da dragagem | 35% | Preço/m³ dentro da aba |
| BDI comercial final | 100% | Todos os itens |
| Redução de volume da vegetação | fator 0,499 | Secagem |
| Margem sobre frete | 30% | Transporte de vegetação |
| Capacidade do caminhão | 15 m³ | Viagens |
| Espessura lagoa | 0,30 m | Volume de vegetação |
| Espessura bacia | 0,20 m | Volume de vegetação |
| Seção de leira | 3,12 m² | Ensecadeira |
| TCPO | 0,0484 h/m³ | Preparação da área |
| Limpeza com trator | 0,001 h/m² | Preparação da área |
| Distância máxima citada | 10 km | Transporte de vegetação |

---

# 12. Cotações, referências e observações de preço

## EVIDÊNCIA CONFIRMADA

- `Fabiano`: carreta carga seca da mobilização.
- `Chute`: guindaste de descarregamento/montagem da mobilização.
- `Danilo 2500 curitiba`: escavadeira usada a R$ 3.000/dia.
- `Danilo em Curitina`: R$ 450 por viagem da vegetação.
- `Chutado`: custo final de viagens.
- `não fiz cotação`: topografia.
- `Genival (25/06/18)`: carreta da desmobilização.
- `Terraplenagem Lavoro`: trator D4.
- `Tubulação 8" FGS - R$ 51,06`: anotação lateral, enquanto o preço usado é R$ 120/m.
- Cabeçalho legado de 26/06/2018.

## EVIDÊNCIA PARCIAL

O arquivo combina cotações identificáveis, preços históricos, estimativas sem cotação e margens empíricas no mesmo fluxo de custo.

---

# 13. Anomalias consolidadas deste arquivo

## EVIDÊNCIA CONFIRMADA

1. Referências a nomes de abas com espaço final diferente do nome inspecionado.
2. Dez células exibidas como `#NAME?`:
   - `2. Canteiro!D14`
   - `2. Canteiro!D15`
   - `2. Canteiro!D23`
   - `2. Canteiro!F26`
   - `7. Dragagem!C9`
   - `7. Dragagem!D225`
   - `7. Dragagem!H235`
   - `7. Dragagem!I235`
   - `7. Dragagem!D246`
   - `7. Dragagem!J247`
3. Cabeçalho da dragagem pertence a Rio Jaguari/Santher/2018.
4. Título da remoção de vegetação ainda diz canteiro de obras.
5. Bloco de vegetação foi copiado para a aba de medição.
6. Preço final da medição, R$ 86.100, diverge do total de R$ 40.150 e não alimenta a consolidação.
7. O custo total da planilha comercial exclui medição e desmobilização.
8. Volume de dragagem varia entre 13.100 m³ e 13.000 m³.
9. Área de medição varia entre 11.000 m² e 10.848,98 m².
10. Volume de ensecadeira aparece como 1.248 m³, 1.800 m³ e 13.561 m³ em contextos distintos.
11. Três eficiências diferentes aparecem sem definição conjunta.
12. Há múltiplas camadas de BDI/markup.
13. Valores e cotações de 2018 coexistem com proposta de 2025.
14. Alguns resultados permanecem calculados mesmo quando células predecessoras mostram erro.
15. Diversas linhas vazias ou zeradas permanecem nas composições.
16. Há erros de grafia e textos residuais.
17. A quantidade de meses do canteiro adiciona 1 ao prazo arredondado; a dragagem usa apenas o prazo arredondado.
18. O preço final de algumas abas significa subtotal, enquanto no canteiro significa custo mensal e na medição é um valor divergente digitado.

---

# 14. Terminologia encontrada

- desassoreamento;
- leito de captação;
- recalque;
- seio da linha;
- linha flutuante;
- linha de terra;
- bota-fora;
- ensecadeira;
- caixa;
- leira;
- hidrotrator;
- batimetria/topografia;
- hora à disposição;
- draguista;
- operador booster;
- cábrea;
- docagem;
- cantina;
- leis sociais;
- TCPO;
- PPRA;
- PCMSO;
- LTCAT;
- ART;
- verba (`vb`);
- preço unitário de serviço;
- custo no estado;
- despesas diretas;
- financeiras;
- BDI;
- margem.

---

# 15. Conhecimentos específicos deste orçamento

## EVIDÊNCIA CONFIRMADA

- Material: areia + argila.
- Dragagem: draga de 6".
- Recalque: 500 m.
- Linha flutuante: 100 m.
- Disposição: ensecadeira.
- Intervenção inclui vegetação da lagoa e bacia.
- Vegetação calculada em 2.281 m³ antes da secagem.
- Volume transportável após secagem: 1.138,219 m³.
- Transporte previsto: 76 viagens até 10 km.
- Área de referência da ensecadeira: 10.848,98 m².
- Medição prevista com seis retornos topográficos.
- Prazo matemático: 4,5946 meses.
- Prazo de custo da dragagem: 5 meses.
- Duração usada no canteiro: 6 meses.
- Custo completo reconstruído: R$ 1.008.868,194558.
- Preço de venda: R$ 2.017.736,389117.

---

# 16. Possíveis padrões — EVIDÊNCIA PARCIAL

Estes pontos não são consolidados:

- separação do orçamento em mobilização, preliminares, operação, medição e desmobilização;
- cálculo de produção antes da composição de custos;
- transformação do prazo fracionário em meses inteiros;
- canteiro tratado como custo mensal da dragagem;
- composição de dragagem baseada em custo mensal;
- apresentação comercial com custo, quantidade, custo unitário, BDI e preço;
- preservação de linhas vazias como catálogo de opções;
- coexistência de memória de cálculo auxiliar e composição principal;
- uso de observações textuais para registrar fornecedor, origem, chute ou ausência de cotação.

---

# 17. Exceções e variações internas

## EVIDÊNCIA CONFIRMADA

- Mobilização e desmobilização usam salários diferentes.
- Leis sociais variam entre 120% e 110%.
- Horas mensais variam entre 198 e 219,9999.
- A duração do canteiro é um mês maior que a duração da dragagem.
- O BDI varia conforme o nível do cálculo.
- O preço final não possui significado uniforme entre abas.
- Quantidades comerciais podem divergir das premissas físicas.
- Algumas composições usam custos arredondados; outras preservam muitas casas decimais.
- A cotação anotada pode ser diferente do preço efetivamente utilizado.

---

# 18. Dúvidas para validação futura do especialista

1. O código correto é `D_011_225` ou `D_011_2025`?
2. O nome correto do curso d'água é Ribeirão Jacutinga?
3. Qual é a origem da vazão, eficiência e concentração?
4. O prazo operacional é 5 meses e o canteiro 6 meses?
5. Por que a dragagem comercializa 13.000 m³ em vez de 13.100 m³?
6. O que representam os volumes 1.248, 1.800 e 13.561 m³ da ensecadeira?
7. O fator 0,499 de secagem da vegetação é histórico?
8. As seis visitas topográficas são uma exigência?
9. O preço final de medição de R$ 86.100 deve ser ignorado?
10. Por que o custo total comercial exclui medição e desmobilização?
11. O BDI comercial de 100% é markup, margem de risco ou BDI formal?
12. O BDI interno de 10% e o BDI de venda de 35% da dragagem devem coexistir com o BDI de 100%?
13. Qual jornada deve orientar salários: 198 ou 219,9999 h/mês?
14. As referências de 2018 ainda são válidas?
15. A linha de recalque é de 6" ou 8"?
16. Qual é a regra oficial da hora à disposição?
17. O mês adicional do canteiro cobre implantação e desmobilização?
18. Os projetos básico e executivo pertencem à mobilização?
19. A remoção de vegetação deve ser verba ou volume?
20. A movimentação inclui apenas transporte ou também carga e descarga?

---

# 19. Limitações da análise

## EVIDÊNCIA CONFIRMADA

- A análise foi realizada sobre o arquivo recebido, sem acesso a histórico de versões.
- Não houve entrevista com o especialista durante esta sessão.
- Não foram consultadas propostas comerciais, contratos, cotações ou medições externas.
- O arquivo contém valores calculados armazenados e células com erro; o registro preserva ambos.
- Não foi realizada correção ou recálculo do workbook.
- Não foi realizada comparação decisória com outros orçamentos.
- Não foi inferida arquitetura de software.
- Não foram atualizados índices gerais, documentos de consolidação ou análises de outros arquivos.

---

# 20. Checklist de validação

- [x] Todas as 11 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Nome integral do arquivo preservado.
- [x] Data, versão disponível, quantidade de abas e status registrados.
- [x] Valores, fórmulas e dependências principais documentados.
- [x] Entidades, regras, terminologia, padrões provisórios e exceções registrados.
- [x] Evidências classificadas.
- [x] Anomalias e células com erro registradas.
- [x] Limitações registradas.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma consolidação realizada.
- [x] Nenhum documento de outro orçamento alterado.
