# D_042_2025 - CMPC - Dragagem - Bombeamento.xlsx — Registro de Descoberta

## Status da análise

- **Arquivo original:** `D_042_2025 - CMPC - Dragagem - Bombeamento.xlsx`
- **Data da análise:** 14/07/2026
- **Versão/revisão identificável:** campo `REVISÃO ATUAL` presente, sem valor preenchido.
- **Quantidade de abas:** 8.
- **Status:** engenharia reversa vertical concluída para o arquivo disponibilizado.
- **Escopo:** documentação exclusiva deste Excel.
- **Restrições respeitadas:** nenhuma funcionalidade, arquitetura, banco de dados, tela, consolidação ou alteração em documentos de outros orçamentos foi produzida.

## Regra de classificação adotada

| Categoria solicitada | Uso neste documento |
| --- | --- |
| **EVIDÊNCIA CONFIRMADA** | Informação comprovada diretamente nas células, fórmulas, nomes de abas ou resultados do Excel. |
| **EVIDÊNCIA PARCIAL** | Interpretação operacional observada exclusivamente neste orçamento; confiança Nível C. |
| **DÚVIDA** | Informação sem comprovação suficiente, referência ambígua ou finalidade não demonstrada. |
| **ANOMALIA OBSERVADA** | Existência de erro, inconsistência, fórmula quebrada ou resíduo confirmada no arquivo, sem concluir automaticamente qual seria a correção. |

Todas as interpretações reutilizáveis permanecem **Nível C**, pois derivam de uma única fonte.

# 1. Classificação aparente do orçamento

## EVIDÊNCIA CONFIRMADA

O arquivo representa um orçamento para:

- cliente `CMPC IGUAÇU`;
- objeto `DRAGAGEM DA LAGOA 01`;
- local `PIRAÍ DO SUL PR`;
- dragagem de 10.000 m³ de `Efluente industríal`;
- equipamento principal identificado como `Draga elétrica`;
- bombeamento direto para a lagoa 2;
- linha de recalque registrada em 300 m na entrada principal;
- linha flutuante de 100 m;
- linha de terra de 200 m;
- medição por `preços unitários de serviços`;
- canteiro e mobilização sob responsabilidade da FOS;
- composição comercial separada em canteiro, mobilização da draga, dragagem, desmobilização da draga/equipamento e desmobilização final.

## EVIDÊNCIA PARCIAL

A estrutura aparenta corresponder a uma família de **dragagem por bombeamento direto entre lagoas**, com operação de draga elétrica e sem comprovação de fornecimento ou operação efetiva de bags no escopo final.

A planilha principal da draga conserva textos herdados de um modelo com `Sistema de Desidratação de lodo`, `bags` e `polímero`, porém:

- o bota-fora declarado é bombeamento direto para lagoa 2;
- a produção é chamada de `PRODUÇÃO DRAGAGEM LODO`;
- o item comercial é `DRAGAGEM E DESAGUAMENTO`, mas a linha vendida é somente `Dragagem`;
- o custo `Operação dos bags + polímero` está vazio;
- a planta de polímero aparece em títulos de mobilização/desmobilização, porém sua carreta tem quantidade zero ou vazia.

Esses elementos indicam possível reaproveitamento de modelo anterior. Não é possível concluir, apenas pelo arquivo, se polímero/desaguamento foi retirado do escopo ou se ficou pendente de preenchimento.

# 2. Identidade e inventário da fonte

## Identificação comercial — EVIDÊNCIA CONFIRMADA

- código exibido: `042_2025`;
- proposta: `Proposta D_042_2025`;
- data em `Dados Obra`: 17/04/2025;
- data em `7.2 Draga`: 22/04/2025;
- cliente: `CMPC IGUAÇU`;
- contato: `Marcio Domingues`;
- e-mail: vazio;
- revisão atual: vazia.

## Inventário das abas

| Ordem | Aba | Dimensão observada | Papel identificado |
| --- | --- | --- | --- |
| 1 | `Dados Obra` | A1:O27 | Identidade, premissas técnicas, linhas e calendário operacional. |
| 2 | `Produção` | A1:I38 | Produção horária/mensal, prazo e cronograma agregado. |
| 3 | `3. Canteiro` | A1:N38 | Equipe, implantação e custo mensal do canteiro. |
| 4 | `4. Mob Draga` | A1:N36 | Mobilização da draga e recursos de montagem. |
| 5 | `7.2 Draga` | A1:L207 | Composição mensal completa da operação da draga. |
| 6 | `9. DesMob Draga` | A1:G36 | Desmobilização da draga e equipamento associado. |
| 7 | `15. Desmob Final` | A1:N38 | Desmobilização final/limpeza e retirada do canteiro. |
| 8 | `Plan. Final` | A1:L17 | Consolidação de custo, BDI comercial e preço de venda. |

# 3. Fluxo completo observado

```text
Dados Obra
  ├─ volume, jornada, dias, linhas e responsabilidade
  ↓
Produção
  ├─ produção útil = vazão × eficiência × concentração
  ├─ produção mensal
  ├─ prazo matemático e prazo arredondado
  └─ cronograma agregado
  ↓
3. Canteiro
  ├─ custo diário da equipe
  ├─ custos de implantação/apoio
  └─ custo mensal do canteiro
  ↓
4. Mob Draga
  ├─ equipe importada do canteiro
  ├─ fretes, guindastes, instalações e montagem
  └─ custo único de mobilização
  ↓
7.2 Draga
  ├─ operação
  ├─ pessoal
  ├─ encargos, refeições, alojamento e viagens
  ├─ manutenção
  ├─ equipamentos de apoio e linha de recalque
  ├─ administrativas, BDI interno e financeiras
  ├─ custo mensal
  └─ custo total pelo prazo
  ↓
9. DesMob Draga + 15. Desmob Final
  ↓
Plan. Final
  ├─ custo por item
  ├─ BDI comercial específico por item
  └─ preço total de venda
```

# 4. Análise por aba

## 4.1. Aba `Dados Obra`

### Objetivo e papel

Registrar dados comerciais, técnicos e operacionais que alimentam produção, linha de recalque, composições de equipe e custos.

### Entradas — EVIDÊNCIA CONFIRMADA

- volume contratual: 10.000 m³;
- anotação: `4400 x 2 metros = 8800 + 10% = 9680 (arredondado para 10k)`;
- material: `Efluente industríal`;
- distância de recalque informada: 300 m;
- seio adicional do recalque: 0 m;
- linha flutuante informada: 100 m;
- seio adicional da linha flutuante: 0 m;
- linha de terra: 200 m;
- profundidade: vazia;
- espessura média: vazia;
- área: vazia;
- bota-fora: `Bombeamento Direto lagoa 2`;
- sistema de medição: preços unitários;
- canteiro: FOS;
- mobilização: FOS;
- jornada: 9 h/dia;
- calendário: 22 dias/mês.

### Quadro lateral de lagoas e linhas — EVIDÊNCIA CONFIRMADA

| Registro | Volume | Linha flutuante | Linha terra | Recalque |
| --- | ---: | ---: | ---: | ---: |
| Lagoa 1 - Lodo | 10.000 | 100 | 800 | 900 |
| Lagoa 1 - Água | 15.600 | vazio | vazio | vazio |
| Totais/médias calculados | 25.600 | 100 | 800 | 900 |

Também existe:

- `Linha de recalque`: 300 m;
- `Linha de retorno do percolado para lagoa 2`: 600 m, calculado como `2 × 300`.

### Fórmulas — EVIDÊNCIA CONFIRMADA

- `O13 = M13 + N13`: recalque lateral de 900 m.
- `B14 = L13`: volume principal recebe 10.000 m³.
- `L15 = SOMA(L13:L14)`: 25.600 m³.
- `M15`, `N15`, `O15`: médias das duas linhas; células vazias não alteram a média observada.
- `H16 = B16 + E16`: total de recalque principal = 300 m.
- `B17 = M15`: linha flutuante principal = 100 m.
- `H17 = B17 + E17`: total da linha flutuante = 100 m.
- `O18 = 2 × 300`: retorno do percolado = 600 m.
- `G21 = B21 × D21 × B20`: volume geométrico; resultado zero por falta de dimensões.

### Dependências

Fornece:

- jornada e dias para `Produção`, `3. Canteiro` e `15. Desmob Final`;
- volume para `Produção` e `Plan. Final`;
- distâncias de recalque para `7.2 Draga`.

### Entidades conceituais

Proposta, cliente, contato, obra, lagoa, material, volume, linha flutuante, linha terrestre, recalque, retorno de percolado, bota-fora, sistema de medição, responsabilidade e jornada.

### ANOMALIAS OBSERVADAS

- Há divergência entre a entrada principal `Linha de terra = 200 m` e o quadro lateral `Linha Terra = 800 m`.
- A distância principal de recalque é 300 m, enquanto o quadro lateral totaliza 900 m.
- A linha de retorno é 600 m, mas não está incorporada à célula principal de distância de recalque.
- Profundidade, espessura e área estão vazias, deixando o volume geométrico em zero.
- O texto menciona `percolado`, conceito normalmente associado a desaguamento, embora o bota-fora seja bombeamento direto.

### DÚVIDAS

- Qual conjunto de linhas representa o dimensionamento efetivamente usado: 300/100/200 ou 900/100/800?
- Os 600 m de retorno do percolado fazem parte do escopo?
- O volume de água de 15.600 m³ é bombeado, drenado, deslocado ou apenas inventariado?
- O acréscimo de 10% sobre 8.800 m³ é contingência padrão ou decisão específica?

---

## 4.2. Aba `Produção`

### Objetivo e papel

Transformar vazão, eficiência, concentração e jornada em produção útil e prazo.

### Entradas — EVIDÊNCIA CONFIRMADA

- vazão: 150 m³/h;
- eficiência: 80%;
- concentração: 20%;
- jornada: 9 h/dia;
- calendário: 22 dias/mês;
- volume: 10.000 m³.

### Fórmulas e resultados

- horas/mês = `9 × 22 = 198 h`;
- produção horária = `150 × 80% × 20% = 24 m³/h`;
- produção mensal = `24 × 198 = 4.752 m³/mês`;
- prazo matemático = `10.000 ÷ 4.752 = 2,104377 mês`;
- prazo arredondado = `ARREDONDAR.PARA.CIMA(...;0) = 3 meses`;
- `Mobilizações = 2`;
- `Operação = 3`.

Cronograma lateral:

- canteiro: 0,5 mês;
- mobilização da draga: 0,5 mês;
- dragagem bags: 3 meses;
- desmobilização da draga: 0;
- desmobilização final: 0;
- total: 4 meses.

### Regras observadas — EVIDÊNCIA PARCIAL

- A concentração é aplicada como fração do volume bombeado para representar produção de material.
- O prazo econômico da operação usa arredondamento inteiro para cima.
- O prazo total adiciona 0,5 mês de canteiro e 0,5 mês de mobilização, mas não adiciona tempo para as desmobilizações.

### Dependências

Recebe volume, jornada e dias de `Dados Obra`; fornece prazo de operação e prazo total para canteiro, draga e planilha final.

### ANOMALIAS OBSERVADAS

- O texto `Dragagem Bags` permanece, apesar do bota-fora declarado como bombeamento direto.
- Fórmulas que referenciam esta aba em outras abas aparecem como `#NAME?` no arquivo carregado, embora a aba exista. A fórmula é armazenada sem o sinal `=` em algumas referências externas (`Produção!H38` / `Produção!H34`), indicando possível incompatibilidade ou fórmula malformada.
- O cronograma atribui zero às duas desmobilizações, embora existam custos relevantes para ambas.

### DÚVIDAS

- Eficiência de 80% e concentração de 20% são premissas técnicas específicas deste efluente?
- Os 3 meses são usados por segurança comercial ou somente pelo arredondamento matemático?
- O prazo total de 4 meses deve ser a quantidade do canteiro, apesar das referências quebradas?

---

## 4.3. Aba `3. Canteiro`

### Objetivo e papel

Compor equipe e itens de implantação/manutenção do canteiro, convertendo o total em preço mensal.

### Equipe e salários — EVIDÊNCIA CONFIRMADA

| Função | Quant. | Salário mensal | Hora-base | Dissídio | Transferência | R$/h usado |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Engenheiro | 1 | 9.500,00 | 43,1818 | 3,2386 | não aplicado | 46,4205 |
| Aux. Técnico | 1 | 5.000,00 | 22,7273 | 1,7045 | 6,1080 | 30,5398 |
| Encarregado | 1 | 11.132,00 | 28,0000 | 2,1000 | 7,5250 | 37,6250 |
| Operador de Draga | 1 | 5.500,00 | 25,0000 | 1,8750 | 6,7188 | 33,5938 |
| Operador de Polímero | 1 | 3.900,60 | 17,7300 | 1,3298 | 4,7649 | 23,8247 |
| Ajudante | 4 | 2.310,00 | 10,5000 | 0,7875 | não aplicado | 11,2875 |

Parâmetros:

- divisor salarial: 220 h/mês;
- dissídio: 7,5%;
- transferência: 25% em posições selecionadas;
- leis sociais: 110%;
- engenheiro atua 50% da jornada;
- demais posições listadas atuam 100%;
- 9 refeições a R$ 35;
- 9 transportes a R$ 15.

Custo diário calculado: **R$ 4.115,53096875**.

### Fórmula de mão de obra

```text
quantidade × R$/h × horas/dia
+ (quantidade × R$/h × horas/dia × leis sociais)
```

As leis sociais de 110% são adicionadas sobre o custo-base, produzindo fator total de 2,10.

### Itens do canteiro — EVIDÊNCIA CONFIRMADA

- container almoxarifado: quantidade vinculada ao prazo total, mas com erro `#NAME?`;
- container sanitário/vestiário: 4 meses × R$ 1.000;
- container escritório: 4 meses × R$ 1.000;
- fretes de containers: 3 × R$ 2.000;
- PGR + PCMSO + LTCAT + PR: R$ 5.000;
- ART principal e corresponsáveis: R$ 500;
- placa de obra: R$ 2.500;
- linha vazia: quantidade 0 × R$ 150;
- duas tendas: 2 × R$ 14.320 = R$ 28.640;
- água potável: 32 galões × R$ 30 = R$ 960;
- material de escritório: 4 meses × R$ 200;
- banheiro químico: 4 meses × R$ 1.650;
- viagem da equipe: 9 × R$ 500;
- exames médicos: 9 × R$ 500;
- máscara de fuga: 9 × R$ 250;
- mão de obra de viagem/registro/integração: 5 dias × custo diário.

Total: **R$ 94.827,65484375**.

Prazo de operação exibido: 4 meses.

Preço unitário mensal: **R$ 23.706,9137109375**.

BDI interno: 0%.

### Cotações/anotações

- tenda: `Locup Tendas 8 x 8m com logo e 3 fechamentos laterais`;
- valor auxiliar de R$ 13.120 e anotação `zap em 28/11/24`;
- água/frete: R$ 1.200 com anotação `chute`.

### Dependências

- recebe jornada de `Dados Obra`;
- deveria receber prazo total de `Produção!H38`;
- fornece salários/hora e equipe para mobilizações/desmobilizações e para `7.2 Draga`;
- fornece custo total para `Plan. Final`.

### ANOMALIAS OBSERVADAS

- `D18 = Produção!H38` resulta em `#NAME?`; por consequência, o primeiro container e a quantidade de venda do canteiro ficam quebrados.
- Apesar disso, diversas linhas foram preenchidas manualmente com 4 meses, e o total calculado exclui o container almoxarifado quebrado.
- Há fórmula para quantidade de água `prazo × 8`, indicando 8 galões por mês.
- O preço unitário divide o total por 4, mas o item comercial do canteiro depende da célula quebrada.
- Título diz `subitem da Dragagem`, enquanto na planilha final o canteiro é item comercial separado.
- Operador de polímero permanece na equipe, embora não haja comprovação de operação de polímero.
- Alguns salários/hora não têm fórmulas visíveis em todas as linhas, sugerindo valores colados ou fórmulas substituídas.

### DÚVIDAS

- O container almoxarifado deveria ser cobrado por 4 meses?
- A tenda usada foi R$ 14.320 ou a cotação auxiliar de R$ 13.120?
- O operador de polímero integra realmente esta obra?
- Máscara de fuga é requisito da CMPC ou padrão FOS?

---

## 4.4. Aba `4. Mob Draga`

### Objetivo e papel

Compor o evento único de mobilização da draga e de uma possível planta de polímero.

### Equipe — EVIDÊNCIA CONFIRMADA

Importa a equipe do canteiro:

- 1 engenheiro;
- 1 auxiliar técnico;
- 1 encarregado;
- 1 operador de draga;
- 1 operador de polímero;
- 4 ajudantes;
- 9 refeições;
- 9 transportes.

Custo diário: **R$ 4.115,53096875**.

### Serviços e recursos

- máquina de solda PEAD: R$ 5.000;
- guindaste de carregamento: R$ 2.500;
- treinamentos: 9 × R$ 300 = R$ 2.700;
- mobiliário do canteiro: R$ 17.000;
- mobiliário do alojamento: R$ 17.000;
- 3 carretas de carga seca para draga/tubos: R$ 30.000;
- carreta do equipamento de polímero: quantidade zero;
- guindaste de descarregamento/montagem: 2 × R$ 10.000;
- instalações hidráulicas: R$ 2.000;
- instalações elétricas: R$ 2.000;
- máquina WAP: R$ 5.000;
- barrilete: R$ 0;
- viagem de ida: 1 dia de equipe = R$ 4.115,53;
- carga e montagem: 7 dias de equipe = R$ 28.808,72.

Total: **R$ 136.124,24775**.

BDI interno: 0%.

### Subcomposição de mobiliário

A área lateral totaliza R$ 17.000:

- 3 mesas de escritório × R$ 1.000;
- 4 cadeiras × R$ 500;
- 2 armários de escritório × R$ 1.500;
- 1 cesto de lixo × R$ 500;
- 4 armários de vestiário × R$ 1.500;
- 1 bebedouro × R$ 2.500.

### Logística adicional

Linhas inferiores registram:

- carreta da draga: 3;
- carreta da tubulação: 2;
- carreta de periféricos: 1.

Essas quantidades somam 6, mas a composição principal cobra somente 3 carretas.

### Cotações/anotações

- treinamentos: `Preços VALE Vitória`;
- carreta: `Fabiano R$ 8.800,00 + 0,2%`;
- anotação `Zap de 11/07/25`, posterior à data da proposta.

### ANOMALIAS OBSERVADAS

- O título inclui `PLANTA DE POLÍMERO`, porém a carreta correspondente está zerada.
- A data de cotação de 11/07/2025 é posterior às datas de abril/2025 da proposta, sugerindo revisão posterior não identificada.
- A lista de carretas inferior não coincide com a quantidade cobrada.
- `E19 = N31` faz o mobiliário principal depender da subcomposição lateral.
- `E20 = E19` replica exatamente R$ 17.000 para mobiliário de alojamento, mas a subcomposição lateral parece descrever somente um conjunto de mobiliário.
- Barrilete permanece zerado.
- O custo usado na planilha final é `F30` (total antes do BDI), equivalente ao final apenas porque BDI interno é zero.

### DÚVIDAS

- Foram necessárias 3 ou 6 carretas?
- O mobiliário do alojamento deveria duplicar o mobiliário do canteiro?
- A planta de polímero estava excluída ou apenas não cotada?
- A cotação posterior pertence a uma revisão não registrada?

---

## 4.5. Aba `7.2 Draga`

### Objetivo e papel

Compor o custo mensal da operação da draga, aplicar custos indiretos e financeiros e multiplicar pelo prazo de operação.

### Identificação — EVIDÊNCIA CONFIRMADA

- referência: `CMPC - Dragagem lagoa 1`;
- data: 22/04/2025;
- cliente: CMPC;
- equipamento: draga elétrica;
- valor do equipamento “no estado”: R$ 200.000.

### I — Operação

Parâmetros:

- 198 h/mês;
- eficiência: 90%;
- consumo: 9 por hora;
- valor de combustível: R$ 1;
- célula auxiliar: 7.

Composição:

- combustível: `198 × 0,9 × 9 × 1 = R$ 1.603,80`;
- filtros/lubrificantes: `(198 × 0,9 × 9 × 7) × 10% = R$ 1.122,66`;
- fretes/carretos: R$ 1.000;
- segurança/uniformes: R$ 500.

Total operação: **R$ 4.226,46/mês**.

### ANOMALIA OBSERVADA

A descrição da fórmula de combustível diz `0,15 x HP x hora`, mas a fórmula real usa horas, eficiência, consumo e preço. A linha de filtros usa o valor 7, não o custo de combustível calculado, e resulta em 70% do combustível, apesar do texto `10% combustível`.

### II — Pessoal

#### Horas remuneradas

A planilha calcula:

- 44 horas extras a 70%: `2 h × 22 dias`;
- 0 hora extra a 100%;
- 219,9999 horas normais: `7,33333 × 30`;
- total remunerado: `(44 × 1,70) + (0 × 2) + 219,9999 = 294,7999 h`.

Engenheiro usa 50% desse total: 147,39995 h.

#### Equipe efetivamente quantificada

- encarregado: 1 × 294,7999 h × R$ 37,625 = R$ 11.091,8462375;
- operador de draga: 1 × 294,7999 h × R$ 33,59375 = R$ 9.903,434140625;
- ajudante: 1 × 294,7999 h × R$ 11,2875 = R$ 3.327,55387125.

Engenheiro, auxiliar técnico e operador de polímero têm quantidade vazia e custo zero.

Total salários: **R$ 24.322,834249375**.

Encargos sociais: 110% = **R$ 26.755,1176743125**.

#### Refeições

- 2 alojados × (R$ 15 café + R$ 30 almoço + R$ 30 jantar) × 30 dias = R$ 4.500;
- 1 funcionário da cidade × (R$ 15 café + R$ 30 almoço) × 22 dias = R$ 990.

Total: **R$ 5.490**.

#### Alojamento

- aluguel: R$ 1.500;
- água e luz: R$ 400;
- limpeza: R$ 400;
- multa de rescisão: vazia.

Total: **R$ 2.300**.

#### Viagens nas folgas

- 1 funcionário × R$ 1.500 = R$ 1.500.

#### Prêmios de produção

Estrutura presente para engenheiro, encarregado, draguistas e ajudantes, sem quantidades ou valores; total zero.

Total do bloco pessoal: **R$ 60.367,9519236875**.

### EVIDÊNCIA PARCIAL

A operação mensal parece usar escala contínua de 30 dias para horas normais e refeições de alojados, embora a produção utilize 22 dias úteis e 198 h/mês.

### III — Manutenção

- peças/acessórios: 0,6% do equipamento = R$ 1.200;
- docagem anual apropriada: 1% ao mês = R$ 2.000;
- limpeza/pintura: R$ 500;
- terceiros: R$ 500.

Total: **R$ 4.200/mês**.

### IV — Equipamentos de apoio

Composição principal:

- linha de recalque: R$ 4.078,6666667;
- batimetria final: sem valor;
- bomba de percolado: R$ 500;
- automóvel: R$ 5.000;
- cabo elétrico: R$ 3.000;
- demais itens vazios.

Total: **R$ 12.578,6666667**.

#### Linha de recalque

Tubulação terrestre:

- 300 m × R$ 120 = R$ 36.000;
- depreciação em 12 meses = R$ 3.000/mês;
- juros de 1% = R$ 360/mês;
- subtotal = R$ 3.360/mês.

Flutuantes:

- 25 peças × R$ 200 = R$ 5.000;
- depreciação em 12 meses = R$ 416,6667;
- juros de 1% = R$ 50;
- subtotal = R$ 466,6667.

Acoplamentos:

- 27 peças × R$ 100 = R$ 2.700;
- depreciação em 12 meses = R$ 225;
- juros de 1% = R$ 27;
- subtotal = R$ 252.

Total mensal da linha: **R$ 4.078,6666667**.

### ANOMALIAS OBSERVADAS

- A tubulação usa 300 m, não os 800/900 m do quadro lateral de `Dados Obra`.
- Flutuantes e acoplamentos são calculados em peças sem fórmula que relacione quantidade ao comprimento de 100 m.
- Bomba de percolado permanece no custo, apesar de bota-fora por bombeamento direto.
- Batimetria final aparece sem preço.

### V — Administrativas

- comissões: R$ 0;
- viagens de inspeção: R$ 1.000;
- viagens administrativas: R$ 0;
- comunicações: R$ 300;
- seguro/licenciamento: vazio.

Total: **R$ 1.300/mês**.

### Total de despesas diretas

```text
Operação                  4.226,46
Pessoal                  60.367,9519236875
Manutenção                4.200,00
Equipamentos de apoio    12.578,6666666667
Administrativas           1.300,00
TOTAL                    82.673,0785903542
```

### VI — BDI interno

- oficina: 5% das despesas diretas = R$ 4.133,6539295;
- administração: 5% = R$ 4.133,6539295;
- outros: vazio.

Total BDI interno: **R$ 8.267,3078590**, equivalente a 10%.

### VII — Financeiras

- depreciação do equipamento em 60 meses: R$ 3.333,3333333;
- juros de capital: 1% do equipamento = R$ 2.000;
- atrasos: vazio.

Total: **R$ 5.333,3333333**.

### Resumo mensal

- despesas diretas: R$ 82.673,0785904;
- BDI interno: R$ 8.267,3078590;
- financeiras: R$ 5.333,3333333;
- custo total mensal: **R$ 96.273,7197827**.

### Produção e custo unitário

- produção prevista exibida: **5.702,4 m³/mês**;
- essa produção não vem diretamente da aba `Produção`, que calcula 4.752 m³/mês;
- fórmula armazenada para `D188`: `J207 × 0,6 × 0,62`;
- preço de venda em `D185`: zero, porque células de custo unitário/BDI naquela seção estão vazias.

### Hora à disposição

- custo horário exibido: **R$ 452,194744434**;
- quantidade auxiliar: 26 dias × 9 h = 234 h.

Em bloco lateral:

- custo mensal: R$ 96.273,7197827;
- BDI: fator 1,5;
- preço de venda mensal: R$ 144.410,579674;
- horas trabalhadas: 198;
- eficiência: 0,6;
- horas produtivas: 118,8;
- preço/hora: R$ 1.215,57726998;
- cálculo adicional: R$ 729,34636199 e R$ 437,60781719.

### Custo total da dragagem

- custo mensal dragagem: R$ 96.273,7197827;
- custo de bags/polímero: vazio;
- custo mensal total: R$ 96.273,7197827;
- tempo de operação: referência `Produção!H34`, exibida como `#NAME?`;
- valor cacheado/resultado exibido do custo total: **R$ 288.821,159348**, correspondente a 3 meses.

### Dependências

Recebe:

- salários e leis sociais de `3. Canteiro`;
- distâncias de `Dados Obra`;
- prazo de `Produção`.

Fornece custo total de dragagem para `Plan. Final`.

### ANOMALIAS OBSERVADAS

- Título menciona canteiro e sistema de desidratação, embora canteiro seja cobrado separadamente e bags/polímero estejam vazios.
- Há três eficiências diferentes: 80% na produção; 90% no combustível; 60% na hora produtiva.
- Produção mensal de 5.702,4 m³ diverge dos 4.752 m³ da aba `Produção`.
- A fórmula de prazo está quebrada (`#NAME?`), mas o resultado total preservado corresponde a 3 meses.
- O bloco de preço de venda por m³ está incompleto e retorna zero.
- O bloco comercial lateral usa BDI como fator 1,5, enquanto a planilha final aplica 100% ao item dragagem.
- O custo de combustível de draga elétrica merece esclarecimento: pode representar gerador, apoio ou resíduo de modelo.
- A quantidade de ajudantes na operação é 1, enquanto canteiro/mobilização usam 4.
- Operador de polímero existe na tabela salarial, mas não é quantificado na operação.
- O custo total mensal inclui simultaneamente BDI interno e custos financeiros; depois recebe novo BDI comercial na planilha final.

### DÚVIDAS

- A draga elétrica é alimentada por rede ou gerador?
- Qual é a lógica correta para a produção de 5.702,4 m³/mês?
- O fator 0,62 representa concentração, disponibilidade ou outro coeficiente?
- Qual das eficiências deve governar cada cálculo?
- A linha de recalque deveria considerar 300, 800 ou 900 m?
- O BDI interno de 10% e o BDI comercial de 100% têm naturezas distintas?
- O preço por hora de R$ 1.215,58 é alternativa comercial ou apenas referência?

---

## 4.6. Aba `9. DesMob Draga`

### Objetivo e papel

Compor a retirada da draga e de possível planta de polímero.

### Equipe

Replica a equipe e custos-hora do canteiro. Custo diário: **R$ 4.115,53096875**.

### Serviços e recursos

Itens com quantidade:

- 3 carretas de carga seca × R$ 10.000 = R$ 30.000;
- 2 guindastes × R$ 10.000 = R$ 20.000;
- viagem de volta: 9 × R$ 700 = R$ 6.300;
- mão de obra: 5 dias × R$ 4.115,53096875 = R$ 20.577,65484375.

Demais itens têm quantidade vazia e total zero.

Total: **R$ 76.877,65484375**.

BDI interno: 0%.

### ANOMALIAS OBSERVADAS

- Título inclui planta de polímero, mas a carreta correspondente não é quantificada.
- A descrição do guindaste diz `descarregamento e montagem`, embora esta seja uma desmobilização.
- Máquina de solda, guindaste de carregamento e treinamentos permanecem estruturados, mas vazios.
- Linhas inferiores repetem 3 carretas da draga, 2 da tubulação e 1 de periféricos; o custo principal cobra 3 carretas.
- A planilha final usa `F30`, subtotal antes do BDI, equivalente ao preço final somente porque BDI é zero.

### DÚVIDAS

- O retorno requer 3 ou 6 carretas?
- O valor de viagem de volta por pessoa é R$ 700, diferente da viagem inicial calculada como um dia de equipe.

---

## 4.7. Aba `15. Desmob Final`

### Objetivo e papel

Compor retirada final do canteiro, viagens, exames e mão de obra de limpeza.

### Equipe e diferença salarial

A estrutura replica `3. Canteiro`, porém o encarregado apresenta:

- salário mensal: R$ 11.132;
- hora-base: R$ 50,60;
- dissídio: R$ 3,795;
- transferência: R$ 13,59875;
- R$/h: R$ 67,99375.

Isso difere do encarregado do canteiro, que usa R$ 37,625/h.

Custo diário total: **R$ 4.689,50034375**.

### Itens

- frete de containers: 3 × R$ 2.000 = R$ 6.000;
- viagem da equipe: 9 × R$ 500 = R$ 4.500;
- exames médicos: 9 × R$ 500 = R$ 4.500;
- mão de obra de viagem + limpeza final: 5 dias × R$ 4.689,50034375 = R$ 23.447,50171875.

Total: **R$ 38.447,50171875**.

Demais itens têm quantidade vazia e total zero.

### ANOMALIAS OBSERVADAS

- `Prazo de Operação` é zero.
- `Preço unitário = total ÷ prazo` resulta em `#DIV/0!`.
- BDI e preço final também resultam em `#DIV/0!`.
- A planilha final ignora o preço final quebrado e importa diretamente o total `F34`.
- Exames médicos são cobrados novamente na desmobilização final, além do canteiro.
- O encarregado tem custo-hora muito superior ao usado nas demais abas; a hora-base de R$ 50,60 não corresponde ao salário dividido por 220.
- O título ainda diz `CANTEIRO DE OBRAS : subitem da Dragagem`, apesar de representar desmobilização final.
- A fórmula de preço unitário pressupõe duração, mas a planilha final trata o item como verba única.

### DÚVIDAS

- O custo-hora do encarregado foi alterado intencionalmente?
- Exames médicos na saída representam demissionais?
- A desmobilização final deve ser evento único ou custo mensal?

---

## 4.8. Aba `Plan. Final`

### Objetivo e papel

Consolidar custos e aplicar BDI comercial individual por item.

### Composição de venda — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Custo total | Quant. | Unidade | Custo unit. | BDI | Preço unit. | Preço total |
| --- | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 3 | Canteiro de Obras | 94.827,65 | `#NAME?` | mês | 23.706,91 | 50% | 35.560,37 | 142.241,48* |
| 4 | Mobilização Draga | 136.124,25 | 1 | vb | 136.124,25 | 50% | 204.186,37 | 204.186,37 |
| 7.2 | Dragagem | 288.821,16 | 10.000 | m³ | 28,8821 | 100% | 57,7642 | 577.642,32 |
| 9 | Desmobilização Draga/Eqto Pol. | 76.877,65 | 1 | vb | 76.877,65 | 50% | 115.316,48 | 115.316,48 |
| 15 | Desmobilização Final | 38.447,50 | 1 | vb | 38.447,50 | 50% | 57.671,25 | 57.671,25 |

\* O valor de R$ 142.241,48 corresponde a 4 meses × R$ 35.560,37, apesar da quantidade exibida como `#NAME?`, indicando valor cacheado anterior.

Preço total de venda: **R$ 1.097.057,90743071**.

### Fórmula comercial

```text
custo unitário = custo total ÷ quantidade
preço unitário = custo unitário × (1 + BDI%)
preço total = quantidade × preço unitário
```

### Outros resultados presentes

- `Custo Total` em C12: R$ 38.447,50, pois a fórmula soma somente `C10:C11`;
- `C14 = J12 - C12`: R$ 1.058.610,40571196;
- `C17 = J12 × 1%`: R$ 10.970,5790743.

### ANOMALIAS OBSERVADAS

- O rótulo `Custo Total` não soma todos os custos; soma apenas a desmobilização final e a linha vazia seguinte.
- O valor em C14 aparenta margem/diferença, mas não tem rótulo.
- O valor em C17 é 1% da venda, mas não tem rótulo.
- O total de venda inclui valor cacheado do canteiro apesar da quantidade quebrada.
- BDI comercial varia: 50% em eventos e canteiro, 100% na dragagem.
- Dragagem recebe BDI interno de 10% na composição, custos financeiros e depois BDI comercial de 100%.
- Mobilização e desmobilizações importam subtotal antes de BDI interno, mas estes BDIs são zero.
- A coluna `UNITÁRIO` repete preços unitários para alguns itens e fica vazia para dragagem.
- O grupo `DRAGAGEM E DESAGUAMENTO` não tem custo próprio; funciona como cabeçalho.
- Não há impostos, lucro, contingência ou comissão explicitamente rotulados na planilha final, além do BDI.
- O item de desmobilização menciona equipamento de polímero, embora não haja custo comprovado da planta.

### DÚVIDAS

- Qual é o significado dos valores sem rótulo em C14 e C17?
- O BDI de 100% na dragagem é margem comercial específica desta proposta?
- O preço de venda total homologado é o cache de R$ 1.097.057,91?
- O canteiro deveria ter quantidade 4 meses, restaurando a fórmula quebrada?

# 5. Dependências entre abas

| Origem | Destino | Conhecimento transferido |
| --- | --- | --- |
| `Dados Obra` | `Produção` | horas/dia, dias/mês, volume. |
| `Dados Obra` | `3. Canteiro` | jornada diária. |
| `Dados Obra` | `15. Desmob Final` | jornada diária. |
| `Dados Obra` | `7.2 Draga` | distâncias de recalque e linha flutuante. |
| `Produção` | `3. Canteiro` | prazo total de 4 meses; referência quebrada. |
| `Produção` | `7.2 Draga` | prazo de operação de 3 meses; referência quebrada. |
| `Produção` | `Plan. Final` | quantidade do canteiro; referência quebrada. |
| `3. Canteiro` | `4. Mob Draga` | equipe, horas, leis sociais e custos-hora. |
| `3. Canteiro` | `9. DesMob Draga` | equipe, horas, leis sociais e custos-hora. |
| `3. Canteiro` | `7.2 Draga` | custos-hora, quantidades selecionadas e encargos. |
| `3. Canteiro` | `Plan. Final` | custo total do canteiro. |
| `4. Mob Draga` | `Plan. Final` | custo da mobilização. |
| `7.2 Draga` | `Plan. Final` | custo total da dragagem. |
| `9. DesMob Draga` | `Plan. Final` | custo da desmobilização da draga. |
| `15. Desmob Final` | `Plan. Final` | custo da desmobilização final. |

# 6. Entidades encontradas

## EVIDÊNCIA CONFIRMADA

- proposta e revisão;
- cliente e contato;
- obra, objeto e local;
- lagoa de origem e lagoa de destino;
- material/efluente;
- volume de lodo e volume de água;
- linha de recalque, flutuante, terrestre e retorno de percolado;
- draga elétrica;
- planta/equipamento de polímero;
- canteiro, alojamento, containers e banheiro;
- equipe, função, salário, dissídio, transferência, encargos e jornada;
- refeição, transporte, viagem e exame;
- equipamento de apoio;
- mobilização e desmobilização;
- produção, eficiência, concentração e prazo;
- combustível, manutenção, depreciação e juros;
- custo direto, BDI interno, financeiro, custo unitário, BDI comercial e preço de venda;
- cotação, fornecedor/anotação e data de referência.

# 7. Regras de negócio e fórmulas importantes

## EVIDÊNCIA CONFIRMADA

1. Produção útil horária:
   `vazão × eficiência × concentração`.

2. Produção mensal:
   `produção horária × horas/dia × dias/mês`.

3. Prazo:
   `volume ÷ produção mensal`, arredondado para cima para meses inteiros.

4. Custo diário de função:
   `quantidade × R$/h × horas/dia × (1 + leis sociais)`.

5. Hora-base salarial:
   `salário mensal ÷ 220`.

6. Dissídio:
   `hora-base × 7,5%`.

7. Transferência:
   `(hora-base + dissídio) × 25%`, apenas em funções selecionadas.

8. Linha de recalque mensal:
   investimento dividido por 12 meses mais juros de 1%.

9. Manutenção:
   percentuais sobre o valor do equipamento mais verbas fixas.

10. Depreciação do equipamento:
    `valor do equipamento ÷ 60 meses`.

11. BDI interno da draga:
    5% oficina + 5% administração sobre despesas diretas.

12. Custo total da dragagem:
    custo mensal × prazo inteiro.

13. Preço comercial:
    custo unitário × `(1 + BDI comercial)`.

## EVIDÊNCIA PARCIAL

- O orçamento separa custos de implantação, operação e retirada em itens comerciais.
- O custo mensal da draga combina custo operacional, indireto interno e financeiro antes da margem comercial.
- Prazos podem ser arredondados para cima e usados como quantidades comerciais.
- Custos de linha são apropriados mensalmente por depreciação curta e juros.

# 8. Terminologia observada

- `seio da linha`;
- `linha flut`;
- `linha terra`;
- `recalque`;
- `retorno do percolado`;
- `bota fora`;
- `bombeamento direto`;
- `leis sociais`;
- `dissídio`;
- `transf 25%`;
- `hora à disposição`;
- `valor no estado`;
- `docagem anual`;
- `despesas diretas`;
- `BDI`;
- `vb` — verba;
- `bags`;
- `planta de polímero`;
- `barrilete`.

# 9. Padrões e características específicas deste arquivo

## EVIDÊNCIA PARCIAL

- Há forte reutilização estrutural de um modelo de dragagem com bags/polímero em uma proposta cujo destino declarado é outra lagoa.
- O arquivo opera simultaneamente com jornada produtiva de 22 dias e custos de pessoal/alojamento em 30 dias.
- A composição da draga é mensal; mobilizações e desmobilizações são eventos.
- O BDI é aplicado em duas camadas: uma interna na composição da draga e outra comercial por item.
- Cotações e valores auxiliares são mantidos nas próprias abas, às vezes com datas posteriores à proposta.
- Valores cacheados preservam resultados comerciais mesmo quando fórmulas atuais estão quebradas.

# 10. Catálogo consolidado de anomalias observadas

## EVIDÊNCIA CONFIRMADA quanto à existência

1. `#NAME?` em:
   - `3. Canteiro!D18`;
   - `7.2 Draga!D201`;
   - `Plan. Final!E5`.

2. `#DIV/0!` em:
   - `15. Desmob Final!F36:F38`.

3. Divergência de comprimentos de linha: 300/100/200 versus 900/100/800.

4. Produção mensal divergente: 4.752 versus 5.702,4 m³/mês.

5. Eficiências diferentes: 80%, 90% e 60%.

6. Custo de combustível em equipamento descrito como draga elétrica.

7. Filtro descrito como 10% do combustível, mas fórmula não usa o custo de combustível calculado.

8. Operador de polímero presente em estruturas, sem custo operacional quantificado.

9. Planta de polímero citada, mas carreta zerada/vazia.

10. Custo de bags/polímero vazio.

11. Prazo zero para desmobilizações no cronograma.

12. Quantidades logísticas inferiores indicam 6 carretas, composição cobra 3.

13. Encarregado com R$/h divergente na desmobilização final.

14. Exames médicos cobrados no canteiro e novamente na desmobilização final.

15. `Custo Total` da planilha final soma apenas a desmobilização final.

16. Valores sem rótulo na planilha final.

17. Data de cotação posterior à proposta sem revisão identificada.

18. Resultado comercial do canteiro depende de valor cacheado quando a quantidade está quebrada.

# 11. Dúvidas para validação futura do especialista

1. O escopo inclui somente bombeamento direto ou também polímero/desaguamento?
2. Qual é o comprimento efetivo de cada trecho da linha?
3. O volume de 15.600 m³ de água faz parte da produção?
4. Qual produção mensal deve prevalecer?
5. Qual é a origem do fator 0,62?
6. Por que há três eficiências?
7. Como uma draga elétrica consome combustível?
8. Quantas carretas foram consideradas?
9. O operador de polímero integra a equipe?
10. O encarregado da desmobilização final tem custo-hora diferente por qual motivo?
11. Os exames finais são demissionais?
12. O canteiro é 4 meses?
13. O BDI de 100% da dragagem é margem específica?
14. O valor final de R$ 1.097.057,91 foi o valor efetivamente proposto?
15. O 1% sem rótulo em C17 representa comissão, imposto ou reserva?
16. O valor em C14 representa lucro bruto ou diferença venda/custo parcial?
17. A cotação de julho de 2025 representa revisão posterior?

# 12. Limitações registradas

- A análise foi realizada sobre o arquivo Excel disponibilizado, preservando fórmulas e valores cacheados.
- Não houve acesso a proposta em PDF, memorial descritivo, cotações externas, histórico de revisões ou explicação do especialista.
- Fórmulas quebradas foram documentadas, não corrigidas.
- A intenção de negócio por trás de textos herdados não pode ser confirmada apenas pelo Excel.
- Não foi realizado crosscheck para consolidar regras gerais da FOS.
- Nenhum índice geral ou documento de consolidação foi alterado.

# 13. Validação final

- [x] Todas as 8 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Identidade completa do arquivo preservada.
- [x] Entradas, resultados, fórmulas, dependências, entidades, regras, exceções, padrões e dúvidas registrados.
- [x] Evidências classificadas.
- [x] Fórmulas quebradas e inconsistências registradas.
- [x] Limitações registradas.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhum documento de outro orçamento alterado.
- [x] Nenhuma consolidação realizada.
