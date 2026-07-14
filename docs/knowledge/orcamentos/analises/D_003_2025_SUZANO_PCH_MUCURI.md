# Análise do orçamento — D_003_2025- Suzano PCH Mucuri.xlsx

## 1. Identificação da análise

- **Nome completo do arquivo:** `D_003_2025- Suzano PCH Mucuri.xlsx`
- **Data da análise:** 2026-07-14
- **Versão identificável:** não existe número ou etiqueta explícita de versão no nome do arquivo ou nas células observadas.
- **Proposta registrada no Excel:** `Proposta D_003_2025`.
- **Data registrada no Excel:** 2025-01-24.
- **Cliente:** Suzano.
- **Local:** PCH MUCURI.
- **Quantidade de abas:** 13.
- **Quantidade de fórmulas identificadas:** 217.
- **Tamanho do arquivo analisado:** 42.930 bytes.
- **SHA-256 do arquivo analisado:** `2970faaded3a4c24033f4095adc8f9805800c30ffa421ca15f861df5965537b9`.
- **Status da análise:** CONCLUÍDA.

## 2. Escopo e regra de evidência

Este documento preserva exclusivamente o conhecimento encontrado no arquivo `D_003_2025- Suzano PCH Mucuri.xlsx`.

As informações são classificadas conforme solicitado:

- **EVIDÊNCIA CONFIRMADA:** informação comprovada diretamente no Excel.
- **EVIDÊNCIA PARCIAL:** interpretação ou possível regra observada somente neste orçamento.
- **DÚVIDA:** informação sem comprovação suficiente no arquivo.

Nenhuma conclusão deste documento representa consolidação do Método de Orçamento FOS.

## 3. Classificação do orçamento

### 3.1 Tipo aparente

**EVIDÊNCIA CONFIRMADA**

O objeto registrado é `Remoçao de vegetaçao sobrenadante - 7km2`, no local `PCH MUCURI`, para o cliente Suzano.

O orçamento contém composições para mobilização e desmobilização de hidrotractor e escavadeira, canteiro de obras, operação de hidrotractor, escavadeira long reach, caminhão, comboio, triturador, medição e consolidação de custos e preço de venda.

### 3.2 Processo operacional representado

**EVIDÊNCIA PARCIAL**

O arquivo aparenta representar remoção mecânica de vegetação sobrenadante em reservatório de PCH, combinando hidrotractor, escavadeira long reach, caminhão, comboio e triturador.

### 3.3 Área de atuação

**EVIDÊNCIA PARCIAL**

A área aparente é limpeza ou manejo de vegetação em ambiente de reservatório hidrelétrico, com apoio terrestre e logística de movimentação e trituração.

### 3.4 Características distintivas

**EVIDÊNCIA CONFIRMADA**

- O volume de dragagem da aba `Dados Obra` está vazio.
- O objeto não descreve dragagem de sedimentos, apesar de a planilha conservar terminologia de dragagem.
- A quantidade comercial principal é calculada por `45.000 m²/mês × 0,03 m × 24 meses = 32.400`.
- A consolidação comercial separa os valores em `MOB`, `LIMPEZA` e `DESMOB`.
- O BDI aplicado na planilha final é 50% para todos os itens.
- Os BDIs internos das composições individuais estão zerados.

## 4. Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identificação da proposta, objeto, local e premissas gerais herdadas de um modelo de dragagem. |
| 2 | `Produção` | Cálculo genérico de produção e prazo, atualmente sem volume de entrada. |
| 3 | `1. Mob. Hidrotractor` | Mobilização do hidrotractor. |
| 4 | `2. Mob. Escavadeira` | Mobilização da escavadeira. |
| 5 | `3. Canteiro de obras` | Estrutura temporária, apoio, equipe e custos de canteiro. |
| 6 | `4. Hidrotractor` | Locação e diesel do hidrotractor. |
| 7 | `5. Escadeira` | Locação e diesel da escavadeira; o nome contém a grafia `Escadeira`. |
| 8 | `6. Caminhao&Comboio` | Caminhão, comboio, refeição do motorista e cálculo auxiliar de viagens. |
| 9 | `7. Triturador` | Locação, diesel, mobilização e desmobilização do triturador. |
| 10 | `8. Mediçao` | Estrutura física para medição/apontamento. |
| 11 | `9. DesMob. Hidrotractor` | Desmobilização do hidrotractor. |
| 12 | `10. DesMob. Escavadeira` | Desmobilização da escavadeira. |
| 13 | `11. Plan. Preços` | Consolidação dos custos, BDI, preços e macrogrupos comerciais. |

## 5. Fluxo geral observado

**EVIDÊNCIA PARCIAL**

```text
Dados gerais da proposta
        ↓
Cálculo genérico de produção e prazo
        ↓
Mobilizações
        ↓
Canteiro e recursos operacionais
        ↓
Medição
        ↓
Desmobilizações
        ↓
Planilha detalhada de custos e venda
        ↓
Macrogrupos MOB / LIMPEZA / DESMOB
```

**EVIDÊNCIA CONFIRMADA**

O fluxo não é integralmente conectado. A aba `Produção` calcula prazo zero, enquanto as composições operacionais adotam 24 meses diretamente. A planilha de preços também calcula a quantidade 32.400 por fórmula própria, sem consumir o prazo calculado na aba `Produção`.

# 6. Análise detalhada por aba

## 6.1 Aba `Dados Obra`

### Objetivo e papel

**EVIDÊNCIA CONFIRMADA**

Registrar identificação da proposta, cliente, objeto, local e premissas técnicas e operacionais. A aba aparenta ser uma ficha de premissas reaproveitada de um modelo de dragagem.

### Entradas observadas

**EVIDÊNCIA CONFIRMADA**

- Proposta: `Proposta D_003_2025`.
- Data: 2025-01-24.
- Cliente: Suzano.
- Contato e e-mail: vazios.
- Objeto: `Remoçao de vegetaçao sobrenadante - 7km2`.
- Local: `PCH MUCURI`.
- Volume de dragagem, tipo de material, distância de recalque, linha flutuante, linha de terra, profundidade, espessura e área: vazios.
- Seio da linha: 0.
- Tipo de bota-fora: `Bacia de Decantaçao`.
- Sistema de medição: `preços unitários de serviços`.
- Canteiro e mobilização: responsabilidade da FOS.
- Horário: 9 h/dia.
- Dias de trabalho: 22 dias/mês.

### Fórmulas e finalidade

**EVIDÊNCIA CONFIRMADA**

- `H16 = B16 + E16`: soma distância principal e seio da linha.
- `H17 = B17 + E17`: soma linha flutuante e seio da linha.
- `G21 = B21 × D21 × B20`: calcula volume geométrico.

As fórmulas resultam em zero ou vazio por falta de entradas.

### Dependências

**EVIDÊNCIA CONFIRMADA**

- `B26` fornece horas/dia para as composições de pessoal.
- `B27` fornece dias/mês para `Produção`.
- `B14` fornece quantidade total para `Produção`.

### Entidades conceituais

**EVIDÊNCIA PARCIAL**

Proposta, cliente, contato, obra, local, objeto, material, volume, sistema de medição, responsabilidade operacional e calendário.

### Anomalias e dúvidas

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- O objeto é remoção de vegetação, mas os campos permanecem nomeados como dragagem, recalque, linha flutuante, profundidade e bota-fora.
- O texto `7km2` não é reproduzido em célula numérica de área.
- `Bacia de Decantaçao` permanece preenchida, embora o processo aparente ser de vegetação sobrenadante.

**DÚVIDA**

- O texto `7km2` representa sete quilômetros quadrados, sete mil metros quadrados, extensão linear ou descrição comercial?
- A bacia de decantação participa realmente deste método?
- Qual é a unidade contratual final: m³, m², mês ou serviço composto?

## 6.2 Aba `Produção`

### Objetivo

**EVIDÊNCIA CONFIRMADA**

Calcular produção horária, horas mensais, produção mensal e prazo.

### Entradas, fórmulas e resultados

**EVIDÊNCIA CONFIRMADA**

- Vazão: 350 m³/h.
- Eficiência: 30%.
- Concentração: 15%.
- Horas/dia: 9.
- Dias/mês: 22.
- `H6 = H3 × H4`: 198 h/mês.
- `D8 = D3 × (D4/100) × (D5/100)`: 15,75 m³/h.
- `D13 = D8 × D11`: 3.118,5 m³/mês.
- `D21 = 'Dados Obra '!B14`: 0.
- `D24 = D21 ÷ D18`: 0 mês.

### Dependências e anomalias

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- Nenhuma composição de custo depende do prazo calculado.
- O prazo zero não controla os 24 meses usados nas demais abas.
- O cálculo é denominado `Produção da Draga`, embora os recursos centrais sejam mecânicos.
- A produção mensal não é usada na planilha final.

**DÚVIDA**

A aba foi abandonada durante a elaboração? Vazão, eficiência e concentração possuem significado operacional neste método ou são resíduos do template?

## 6.3 Aba `1. Mob. Hidrotractor`

### Objetivo

**EVIDÊNCIA CONFIRMADA**

Compor o custo de mobilização do hidrotractor.

### Equipe e custo diário

**EVIDÊNCIA CONFIRMADA**

- 1 Operador Líder: R$ 30/h, 9 h/dia, 120% de leis sociais = R$ 594,00.
- Operador de Draga: quantidade vazia, custo zero.
- 2 Ajudantes Gerais: R$ 10,75/h, 9 h/dia, 120% = R$ 425,70.
- 3 refeições a R$ 40,00 = R$ 120,00.
- 3 transportes a R$ 15,00 = R$ 45,00.
- Custo diário: R$ 1.184,70.

### Itens

**EVIDÊNCIA CONFIRMADA**

- Munck: 2 dias × R$ 4.000,00 = R$ 8.000,00.
- Mobilização do hidrotractor: R$ 30.312,50.
- Mão de obra: 2 dias × R$ 1.184,70 = R$ 2.369,40.
- Total e preço final: R$ 40.681,90.
- BDI interno: 0%.

### Regra de cálculo

**EVIDÊNCIA CONFIRMADA**

Custo da função = quantidade × valor hora × horas/dia × (1 + leis sociais/100). Refeições e transportes usam a soma das quantidades de funções. Preço total do item = quantidade × preço unitário.

**DÚVIDA**

A verba de R$ 30.312,50 corresponde a frete, fornecedor, locação de transporte ou preço histórico?

## 6.4 Aba `2. Mob. Escavadeira`

### Objetivo e valores

**EVIDÊNCIA CONFIRMADA**

Compor a mobilização da escavadeira. A equipe gera o mesmo custo diário de R$ 1.184,70.

- Munck: quantidade vazia; total zero.
- Item descrito como `Mobilizaçao (HIDROTRACTOR)`: R$ 30.312,50.
- Mão de obra: 1 dia × R$ 1.184,70.
- Total e preço final: R$ 31.497,20.
- BDI interno: 0%.

### Anomalias

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- O item principal está nomeado como hidrotractor.
- A verba de R$ 30.312,50 é igual à do hidrotractor.
- O munck possui preço unitário, mas quantidade vazia.

## 6.5 Aba `3. Canteiro de obras`

### Objetivo

**EVIDÊNCIA CONFIRMADA**

Compor infraestrutura temporária, alojamento, apoio, segurança, inspeção, barreira de contenção e mão de obra de integração durante 24 meses.

### Equipe diária

**EVIDÊNCIA CONFIRMADA**

- Operador líder: R$ 540,00.
- Operador de draga: quantidade vazia.
- 2 ajudantes: R$ 387,00.
- Refeições: R$ 120,00.
- Transporte: R$ 42,00.
- Custo diário: R$ 1.089,00.
- Leis sociais: 100%.

### Itens e valores

**EVIDÊNCIA CONFIRMADA**

- Container almoxarifado: R$ 21.600,00; observação `Nutrilog`.
- Containers sanitário e escritório: zerados.
- Frete para containers: R$ 5.000,00.
- PPRA + PCMSO + LTCAT: R$ 3.000,00.
- ART principal + corresponsabilidade: R$ 500,00.
- EPI: R$ 76.800,00.
- Alojamento: R$ 60.000,00.
- Móveis: R$ 15.000,00.
- Veículo: R$ 72.000,00.
- Combustível do veículo: R$ 23.040,00.
- Barreira de contenção: R$ 111.000,00.
- Viagens de inspeção: R$ 108.000,00.
- Barco de apoio: R$ 24.000,00.
- Placa e vigilância: zeradas; vigilância marcada `Nao será necessario`.
- Água potável: R$ 4.800,00.
- Material de escritório: R$ 4.800,00.
- Banheiro químico: R$ 28.800,00; observação `vestiário`.
- Exames médicos: R$ 900,00.
- Mão de obra de integração: R$ 574.992,00.
- Total: R$ 1.134.232,00.
- Prazo: 24 meses.
- Preço final mensal calculado: R$ 47.259,67.

### Fórmulas embutidas

**EVIDÊNCIA CONFIRMADA**

- EPI por funcionário: `400 × 3 × 8 = 9.600`.
- Combustível: `4 × 40 × 6 = 960` por mês.
- Barreira: `370 × 300 = 111.000`.
- Água: `24 × 8 = 192` unidades.
- Integração: `22 × 24 = 528` dias.
- Preço mensal = total ÷ 24.

### Anomalias e dúvidas

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- O título afirma `subitem da Dragagem`.
- Os fatores de EPI, barreira, água e combustível não possuem unidades ou explicação completa.
- O preço mensal calculado não é usado na planilha final; ela usa o total integral.

**DÚVIDA**

O fator 3 do EPI representa anos, kits ou trocas? Os 370 e 300 da barreira representam metros e preço por metro? As oito unidades de água são galões mensais?

## 6.6 Aba `4. Hidrotractor`

### Objetivo e valores

**EVIDÊNCIA CONFIRMADA**

Compor locação e combustível do hidrotractor durante 24 meses.

- Locação: 24 × R$ 92.400,00 = R$ 2.217.600,00.
- Diesel: 62.832 l × R$ 6,00 = R$ 376.992,00.
- Consumo indicado: 17 l/h.
- Total: R$ 2.594.592,00.
- Preço final mensal: R$ 108.108,00.
- BDI interno: 0%.

### Fórmula de diesel

**EVIDÊNCIA CONFIRMADA**

`22 dias/mês × 17 l/h × 7 h/dia × 24 meses = 62.832 l`.

### Anomalias

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- O calendário geral é 9 h/dia, mas o diesel usa 7 h/dia.
- O custo diário da equipe é calculado em R$ 1.089,00, porém não incluído.
- Existe linha de container zerada.

**DÚVIDA**

As duas horas de diferença correspondem a improdutividade, manutenção, intervalo ou limitação operacional?

## 6.7 Aba `5. Escadeira`

### Objetivo e valores

**EVIDÊNCIA CONFIRMADA**

Compor locação e combustível da escavadeira long reach durante 24 meses.

- Locação: 24 × R$ 92.400,00 = R$ 2.217.600,00.
- Diesel: 85.008 l × R$ 6,00 = R$ 510.048,00.
- Consumo indicado: 23 l/h.
- Total: R$ 2.727.648,00.
- Preço final mensal: R$ 113.652,00.
- BDI interno: 0%.

### Fórmula de diesel

**EVIDÊNCIA CONFIRMADA**

`22 × 23 × 7 × 24 = 85.008 l`.

### Anomalias

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- O nome é `Escadeira`, enquanto a planilha final usa `Escavadeira Long Reach`.
- O título interno é `CANTEIRO DE OBRAS : subitem da Dragagem`.
- A equipe diária não integra o total.
- A locação mensal é igual à do hidrotractor.
- O diesel usa 7 h/dia, não 9 h/dia.

## 6.8 Aba `6. Caminhao&Comboio`

### Objetivo

**EVIDÊNCIA CONFIRMADA**

Compor locação de caminhão, comboio e refeição do motorista, além de calcular viagens diárias.

### Equipe e itens

**EVIDÊNCIA CONFIRMADA**

- Motorista, refeição e transporte: custo diário de R$ 594,00.
- Locação: R$ 432.000,00.
- Diesel: zero.
- Comboio: R$ 187.200,00.
- Refeição do motorista: 2.112 × R$ 30,00 = R$ 63.360,00.
- Total: R$ 682.560,00.
- Prazo: 24 meses.
- Preço final mensal: R$ 28.440,00.
- Observação: `Empresa R3 - Local`.

### Cálculo auxiliar

**EVIDÊNCIA CONFIRMADA**

- Capacidade: 14 m³.
- Consumo indicado: 20 l/h, não apropriado.
- Área: 45.000 m²/mês.
- Espessura: 0,03 m.
- Volume: 1.350 m³/mês.
- Período: 22 dias.
- Volume diário: 61,3636 m³/dia.
- Viagens: 4,3831 por dia.
- Refeições: `2 × 2 × 22 × 24 = 2.112`.

### Anomalias e dúvidas

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- Diesel zerado apesar do consumo indicado.
- Viagens calculadas não alimentam custo ou quantidade.
- Os dois fatores 2 das refeições não são identificados.
- Refeição custa R$ 30 na composição e R$ 40 na equipe.
- A área de 45.000 m²/mês não vem de `Dados Obra`.

**DÚVIDA**

Os fatores 2 representam refeições e motoristas/turnos? O caminhão é contratado independentemente das viagens? O combustível está incluso?

## 6.9 Aba `7. Triturador`

### Objetivo e valores

**EVIDÊNCIA CONFIRMADA**

Compor locação, combustível, mobilização e desmobilização do triturador.

- Locação: R$ 288.000,00.
- Diesel: 18.480 l × R$ 6,00 = R$ 110.880,00.
- Mobilização: R$ 10.000,00.
- Desmobilização: R$ 10.000,00.
- Total: R$ 418.880,00.
- Prazo: 24 meses.
- Preço final mensal: R$ 17.453,33.

### Fórmula

**EVIDÊNCIA CONFIRMADA**

`22 × 7 × 5 × 24 = 18.480 l`.

### Anomalias

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- O consumo de 5 l/h está apenas embutido na fórmula.
- A equipe diária de R$ 594,00 não é apropriada.
- Mobilização e desmobilização estão dentro da operação, diferentemente dos outros equipamentos.

## 6.10 Aba `8. Mediçao`

### Objetivo e valores

**EVIDÊNCIA CONFIRMADA**

Compor estrutura de medição/apontamento.

- Equipe diária calculada: R$ 1.042,00.
- Escada 1,70 m para apontador: R$ 15.000,00.
- Cobertura: R$ 4.000,00.
- Total e preço final: R$ 19.000,00.
- BDI interno: 0%.

### Anomalias e dúvidas

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- O custo diário da equipe não é incluído.
- Existe item 3 vazio.
- Existe segundo bloco de BDI e preço final zerado.
- O bloco usa cargos de dragagem.

**DÚVIDA**

A `Escada 1,70m (apontador)` representa torre, plataforma, régua ou posto de observação? A mão de obra está incluída em outro custo?

## 6.11 Aba `9. DesMob. Hidrotractor`

**EVIDÊNCIA CONFIRMADA**

A composição é numericamente idêntica à mobilização do hidrotractor:

- munck: R$ 8.000,00;
- verba descrita como mobilização: R$ 30.312,50;
- mão de obra: R$ 2.369,40;
- total e preço final: R$ 40.681,90.

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

A aba é de desmobilização, mas o item principal permanece descrito como mobilização.

## 6.12 Aba `10. DesMob. Escavadeira`

**EVIDÊNCIA CONFIRMADA**

A composição é numericamente idêntica à mobilização da escavadeira:

- munck: zero;
- verba descrita como mobilização do hidrotractor: R$ 30.312,50;
- mão de obra: R$ 1.184,70;
- total e preço final: R$ 31.497,20.

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- O título interno afirma mobilização, não desmobilização.
- O item principal afirma hidrotractor.
- A planilha final referencia `F18`, não `F20`; os valores coincidem porque o BDI interno é zero.

## 6.13 Aba `11. Plan. Preços`

### Objetivo

**EVIDÊNCIA CONFIRMADA**

Consolidar custos, calcular custo unitário, aplicar BDI de 50%, calcular preço total e apresentar macrogrupos comerciais.

### Valores

| Serviço | Custo total | Quantidade | Custo unitário | BDI | Preço unitário | Preço total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Mobilização Hidrotractor | R$ 40.681,90 | 1 | R$ 40.681,90 | 50% | R$ 61.022,85 | R$ 61.022,85 |
| Mobilização Escavadeira | R$ 31.497,20 | 1 | R$ 31.497,20 | 50% | R$ 47.245,80 | R$ 47.245,80 |
| Canteiro | R$ 1.134.232,00 | 32.400 | R$ 35,007160 | 50% | R$ 52,510741 | R$ 1.701.348,00 |
| Hidrotractor | R$ 2.594.592,00 | 32.400 | R$ 80,08 | 50% | R$ 120,12 | R$ 3.891.888,00 |
| Escavadeira Long Reach | R$ 2.727.648,00 | 32.400 | R$ 84,186667 | 50% | R$ 126,28 | R$ 4.091.472,00 |
| Caminhão + Comboio | R$ 682.560,00 | 32.400 | R$ 21,066667 | 50% | R$ 31,60 | R$ 1.023.840,00 |
| Triturador | R$ 418.880,00 | 32.400 | R$ 12,928395 | 50% | R$ 19,392593 | R$ 628.320,00 |
| Medição | R$ 19.000,00 | 1 | R$ 19.000,00 | 50% | R$ 28.500,00 | R$ 28.500,00 |
| Desmobilização Hidrotractor | R$ 40.681,90 | 1 | R$ 40.681,90 | 50% | R$ 61.022,85 | R$ 61.022,85 |
| Desmobilização Escavadeira | R$ 31.497,20 | 1 | R$ 31.497,20 | 50% | R$ 47.245,80 | R$ 47.245,80 |

### Totais

**EVIDÊNCIA CONFIRMADA**

- Custo total: R$ 7.721.270,20.
- Preço de venda: R$ 11.581.905,30.
- Acréscimo: R$ 3.860.635,10.
- BDI uniforme: 50%.

### Quantidade comercial

**EVIDÊNCIA CONFIRMADA**

`45.000 × 0,03 × 24 = 32.400`.

Pelas células auxiliares de `6. Caminhao&Comboio`, os fatores aparentam representar 45.000 m²/mês, 0,03 m de espessura e 24 meses. A unidade final permanece `un`.

### Macrogrupos

**EVIDÊNCIA CONFIRMADA**

- `MOB = J4 + J5 + 10% de J6 + J11 = R$ 306.903,45`.
- `LIMPEZA = 90% de J6 + J7 + J8 + J9 + J10 = R$ 11.166.733,20`.
- `DESMOB = I12 + I13 = R$ 108.268,65`.
- Total = R$ 11.581.905,30.

### Anomalias e dúvidas

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- A unidade 32.400 é `un`, embora o cálculo aparente resultar em m³.
- A quantidade não depende de `Produção` nem de `Dados Obra`.
- `DESMOB` soma preços unitários, não totais; coincide porque quantidade = 1.
- A desmobilização da escavadeira referencia `F18`, não `F20`.
- A numeração dos itens é inconsistente.
- Custos mensais das abas não são usados; os totais integrais são diluídos por 32.400.

**DÚVIDA**

A divisão 10%/90% do canteiro é específica? Por que medição integra MOB? A unidade correta é m³ de vegetação removida?

# 7. Dependências entre abas

## 7.1 Confirmadas

**EVIDÊNCIA CONFIRMADA**

- `Dados Obra!B26` alimenta horas/dia nas composições.
- `Dados Obra!B27` alimenta dias/mês de `Produção`.
- `Dados Obra!B14` alimenta o volume de `Produção`.
- Cada composição alimenta `11. Plan. Preços` por total ou preço final.
- A planilha final calcula BDI e macrogrupos.

## 7.2 Ausentes ou interrompidas

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

- O prazo de `Produção` não alimenta custos.
- O volume de `Dados Obra` não alimenta a quantidade comercial.
- O cálculo de viagens não alimenta o custo do caminhão.
- Equipes calculadas não são incluídas em hidrotractor, escavadeira, caminhão, triturador ou medição.
- Diesel do caminhão não é apropriado.
- Preços finais mensais não são usados na consolidação.

# 8. Entidades encontradas

## 8.1 Comerciais

**EVIDÊNCIA PARCIAL**

Proposta, cliente, contato, objeto, local, serviço, item comercial, macrogrupo, custo, preço, BDI e preço de venda.

## 8.2 Operacionais

**EVIDÊNCIA PARCIAL**

Obra, canteiro, hidrotractor, escavadeira long reach, caminhão, comboio, triturador, barco de apoio, barreira de contenção, medição, mobilização, desmobilização, locação, combustível, equipe, inspeção e alojamento.

## 8.3 Pessoal

**EVIDÊNCIA PARCIAL**

Operador líder, operador de draga, ajudante geral, motorista, apontador, refeição, transporte e leis sociais.

## 8.4 Grandezas

**EVIDÊNCIA PARCIAL**

Horas/dia, dias/mês, prazo, área mensal, espessura, volume, capacidade do caminhão, viagens/dia, consumo horário, preço de diesel e quantidade comercial.

# 9. Regras de negócio observadas

## 9.1 Mão de obra

**EVIDÊNCIA CONFIRMADA**

`custo = quantidade × salário-hora × horas/dia × (1 + leis sociais)`.

Refeições e transporte são calculados separadamente por quantidade de pessoas.

**EVIDÊNCIA PARCIAL**

Mobilizações usam 120% de leis sociais; canteiro e operações usam 100%. O arquivo não explica a diferença.

## 9.2 Equipamentos

**EVIDÊNCIA CONFIRMADA**

- Locação mensal × 24 meses.
- Diesel = dias/mês × horas efetivas/dia × consumo horário × prazo × preço/litro.
- Hidrotractor e escavadeira usam 7 horas produtivas.
- Triturador usa 7 horas e consumo implícito de 5 l/h.

## 9.3 Custos de evento

**EVIDÊNCIA CONFIRMADA**

Mobilização, desmobilização, fretes, ARTs, documentos, móveis, barreira, escada e cobertura são verbas únicas.

## 9.4 BDI

**EVIDÊNCIA CONFIRMADA**

BDI interno = 0%; BDI final = 50%; preço unitário de venda = custo unitário × 1,5.

## 9.5 Diluição comercial

**EVIDÊNCIA CONFIRMADA**

Canteiro e equipamentos são divididos por 32.400 para obter custo unitário, recebem BDI e são multiplicados novamente pela quantidade.

## 9.6 Segmentação comercial

**EVIDÊNCIA CONFIRMADA**

O preço é reapresentado em mobilização, limpeza e desmobilização. O canteiro é repartido 10%/90%.

# 10. Terminologias

**EVIDÊNCIA CONFIRMADA**

Proposta, dados da obra, dragagem, remoção de vegetação sobrenadante, hidrotractor, escavadeira long reach, caminhão de movimentação, comboio, triturador, medição, mobilização, desmobilização, canteiro, leis sociais, verba, prazo, preço final, custo total, custo unitário, BDI, preço unitário, preço total, MOB, LIMPEZA e DESMOB.

# 11. Padrões observados exclusivamente neste arquivo

**EVIDÊNCIA PARCIAL**

- Estrutura-padrão de equipe no topo das composições.
- Prazo operacional fixo de 24 meses.
- Diesel a R$ 6,00/litro.
- 22 dias/mês.
- 7 horas produtivas para equipamentos, com jornada geral de 9 horas.
- BDI de 50% apenas na consolidação.
- Diluição por área × espessura × prazo.
- Separação final em mobilização, limpeza e desmobilização.

Esses padrões não devem ser tratados como universais sem crosscheck.

# 12. Exceções e anomalias consolidadas

## 12.1 Resíduos de template

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

Campos de vazão, eficiência, concentração, draga, recalque, linha flutuante, profundidade, bota-fora, operador de draga, títulos de dragagem e containers zerados permanecem no arquivo.

## 12.2 Nomenclatura

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

`Escadeira` versus `Escavadeira Long Reach`; desmobilizações com títulos de mobilização; mobilização da escavadeira descrita como hidrotractor; `Motorisa`; grafias sem padronização.

## 12.3 Lógicas desconectadas

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

Prazo zero versus 24 meses; produção e volume não usados; viagens não usadas; equipes calculadas e não apropriadas; diesel do caminhão ausente.

## 12.4 Referências frágeis

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

Algumas fórmulas usam nomes de abas com espaço final, como `'Dados Obra '` e `'1. Mob. Hidrotractor '`. A planilha final usa células diferentes (`F18` ou `F20`) para resultados equivalentes.

## 12.5 Valores sem unidade ou justificativa

**EVIDÊNCIA CONFIRMADA — ANOMALIA**

45.000 m²/mês, 0,03 m e 24 meses não estão nas premissas gerais; fatores de EPI, barreira, água e refeições não são nomeados; a quantidade 32.400 aparece como `un`.

# 13. Dúvidas para validação futura

1. O objeto `7km2` está correto e qual sua interpretação dimensional?
2. A quantidade contratual é 32.400 m³, 32.400 unidades ou outra grandeza?
3. A área mensal correta é 45.000 m²?
4. A espessura correta é 0,03 m?
5. O prazo de 24 meses foi definido comercialmente ou por produtividade?
6. A aba `Produção` deve ser ignorada?
7. Qual é a produtividade real do conjunto operacional?
8. Por que equipamentos usam 7 horas em jornada de 9 horas?
9. As equipes operacionais estão apropriadas em outro custo ou foram omitidas?
10. O diesel do caminhão está incluso na locação?
11. Qual o significado dos fatores de 2.112 refeições?
12. As locações iguais de hidrotractor e escavadeira são deliberadas?
13. A verba de R$ 30.312,50 é igual para todos os movimentos?
14. Por que o canteiro é repartido 10%/90%?
15. Por que medição integra MOB?
16. A barreira corresponde a 370 m × R$ 300/m?
17. O EPI de R$ 9.600 por funcionário cobre qual período?
18. A bacia de decantação participa do processo?
19. O que é a `Escada 1,70m (apontador)`?
20. O BDI de 50% é específico desta proposta?

# 14. Conhecimento específico deste orçamento

**EVIDÊNCIA PARCIAL**

Este orçamento representa composição de longo prazo para limpeza de vegetação sobrenadante em PCH, estruturada sobre área mensal de 45.000 m², espessura aparente de 0,03 m, prazo fixo de 24 meses, quantidade comercial de 32.400, conjunto de hidrotractor, escavadeira, caminhão, comboio e triturador, infraestrutura de apoio, mobilização e desmobilização separadas, BDI de 50% e preço de venda de R$ 11.581.905,30.

Nada nesta seção deve ser generalizado sem curadoria e crosscheck.

# 15. Limitações

- Análise realizada apenas sobre o arquivo fornecido, sem entrevista adicional.
- O arquivo não contém histórico ou versão explícita.
- Não foram encontrados erros computados `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?` ou `#N/A` no estado importado.
- A ausência de erro computado não elimina inconsistências lógicas ou resíduos de template.
- Não houve comparação com outros orçamentos.
- Não foi tomada decisão arquitetural.

# 16. Validação final

- [x] Todas as 13 abas analisadas.
- [x] Documento exclusivo produzido.
- [x] Entidades, fórmulas, relações, regras, exceções, padrões, anomalias e dúvidas preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma consolidação realizada.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhum documento de outro orçamento alterado.
- [x] Nenhum índice geral alterado.