# Composição - Xisto - 3 turnos.xlsx — Registro de Descoberta

## Status da análise

- **Status:** análise integral concluída.
- **Data da análise:** 14/07/2026.
- **Arquivo original:** `Composição - Xisto - 3 turnos.xlsx`.
- **Versão explícita no arquivo:** não identificada.
- **Quantidade de abas:** 15.
- **Escopo:** documentação exclusiva deste Excel.
- **Alterações funcionais ou arquiteturais:** nenhuma.
- **Consolidação com outros orçamentos:** não realizada.
- **Confiança das descobertas reutilizáveis:** Nível C, por derivarem de uma única fonte.

## Regra de classificação das evidências

| Classificação solicitada | Correspondência documental |
| --- | --- |
| EVIDÊNCIA CONFIRMADA | Conteúdo, fórmula, valor, texto ou anomalia diretamente observável no Excel. |
| EVIDÊNCIA PARCIAL | Interpretação ou possível regra observada somente neste orçamento. |
| DÚVIDA | Informação sem comprovação suficiente ou que exige validação do especialista. |

## Classificação aparente do orçamento

### EVIDÊNCIA CONFIRMADA

O arquivo representa orçamento de **dragagem e desidratação de lodo de ETE por centrífuga**, com:

- cliente SANEPAR;
- referência textual a `XISTO`;
- local preenchido como Suzano - SP;
- volume estimado de dragagem de 44.717,75 m³;
- base seca estimada de 3.577,42 t;
- produção mínima desejada de 1.414 t de material desaguado por mês;
- operação planejada por 11,5 meses;
- jornada global de 16 h/dia e 26 dias/mês;
- mobilização separada para draga e centrífuga;
- custos mensais separados de dragagem e operação da centrífuga;
- fornecimento de polímero;
- transporte e destinação final;
- desmobilização separada para draga e centrífuga;
- consolidação comercial com BDI por item.

### EVIDÊNCIA PARCIAL

O nome do arquivo e os quadros de turno indicam intenção de modelar operação em **três turnos**, mas a premissa global registra 16 h/dia e a aba de produção mantém simultaneamente cenários de 24 h/3 turnos e 16 h/2 turnos. Portanto, o regime efetivamente contratado não pode ser afirmado sem validação.

### DÚVIDA

Há inconsistência aparente entre:
- título `SANEPAR / XISTO`;
- objeto de lodo de ETE;
- local `Suzano - SP`;
- histórico de Palotina.

Não é possível concluir, somente pelo arquivo, se todos esses elementos pertencem à mesma proposta ou se existem resíduos de modelos anteriores.

## Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identidade, escopo, balanço de massa e parâmetros globais. |
| 2 | `Fornecedores` | Contatos e cotações de guindaste e containers. |
| 3 | `Historico - PALOTINA` | Histórico de teor de sólidos desaguado. |
| 4 | `Produção (NOVO CALCULO)` | Capacidade da centrífuga em diferentes regimes e concentrações. |
| 5 | `1. Canteiro` | Implantação/custeio do canteiro e integração. |
| 6 | `2.1 Mob Draga` | Mobilização da draga. |
| 7 | `2.2 Mob Centr` | Mobilização da centrífuga. |
| 8 | `4.1 Draga Dec` | Custo mensal e total da dragagem. |
| 9 | `4.2 Centrífuga` | Custo mensal e total do decanter. |
| 10 | `Op. Centrifuga` | Dosagem e custo de polímero. |
| 11 | `Transp e Destinacao` | Custo de transporte e destinação final. |
| 12 | `5. Desmob Canteiro` | Estrutura de desmobilização do canteiro, atualmente quebrada. |
| 13 | `Desmob Draga` | Desmobilização da draga. |
| 14 | `Desmob Centr` | Desmobilização da centrífuga. |
| 15 | `Plan. Final` | Consolidação de custo e venda. |

## Fluxo completo observado

```text
Dados da obra e balanço de massa
    ├── histórico de sólidos desaguados
    ├── cálculo de produção da centrífuga
    ├── canteiro e integração
    ├── mobilização da draga
    ├── mobilização da centrífuga
    ├── custo mensal da dragagem
    ├── custo mensal da centrífuga
    ├── consumo e custo de polímero
    ├── transporte e destinação final
    ├── desmobilização da draga
    └── desmobilização da centrífuga
             ↓
        Planilha final
             ↓
       preço de venda total
```

## Dependências entre abas — EVIDÊNCIA CONFIRMADA

| Aba consumidora | Abas referenciadas por fórmula |
| --- | --- |
| `1. Canteiro` | `Dados Obra ` (2 refs.) |
| `2.1 Mob Draga` | `1. Canteiro` (12 refs.) |
| `2.2 Mob Centr` | `1. Canteiro` (12 refs.) |
| `4.1 Draga Dec` | `Produção (NOVO CALCULO)` (2 refs.), `Dados Obra ` (4 refs.), `2.1 Mob Draga` (1 refs.), `1. Canteiro` (5 refs.) |
| `4.2 Centrífuga` | `4.1 Draga Dec` (3 refs.), `Dados Obra ` (4 refs.), `1. Canteiro` (2 refs.), `Produção (NOVO CALCULO)` (1 refs.) |
| `Op. Centrifuga` | `Dados Obra ` (1 refs.) |
| `Desmob Draga` | `1. Canteiro` (16 refs.) |
| `Desmob Centr` | `1. Canteiro` (12 refs.) |
| `Plan. Final` | `2.1 Mob Draga` (1 refs.), `2.2 Mob Centr` (1 refs.), `Dados Obra ` (2 refs.), `4.1 Draga Dec` (1 refs.), `4.2 Centrífuga` (1 refs.), `Op. Centrifuga` (2 refs.), `Desmob Draga` (1 refs.), `Desmob Centr` (1 refs.), `Transp e Destinacao` (1 refs.) |

Observação: diversas fórmulas registram o nome `'Dados Obra '` com espaço final. O nome exibido pelo arquivo é `Dados Obra`. A existência dessa divergência é confirmada; seu efeito real no Excel precisa ser validado porque alguns resultados permanecem em cache.

---

# Análise por aba

## 1. Aba `Dados Obra`

### Objetivo e papel no fluxo
Centralizar a identidade comercial, o escopo técnico e os parâmetros globais usados nas composições posteriores.

### Entradas e resultados — EVIDÊNCIA CONFIRMADA
- Proposta `D_026_2024`, cliente SANEPAR, objeto `Dragagem e desidratação de lodo`, local `Suzano - SP`.
- Material: `Lodo de ETE`; bota-fora/processamento: `CENTRÍFUGA`.
- Produção mínima desejada: 1.414 t de material desaguado por mês.
- Teor de sólidos in situ: 8%; teor de sólidos desaguado: 22%.
- Prazo de operação: 11,5 meses.
- Volume total estimado: 44.717,75 m³.
- Base seca total: 3.577,42 t.
- Volume desaguado total calculado: 16.261,00 m³.
- Recalque: 350 m; linha flutuante: 150 m; linha de terra: 200 m.
- Jornada: 16 h/dia e 26 dias/mês.

### Regras observadas
- O volume mensal a dragar deriva da produção desaguada mínima e da razão entre sólidos desaguados e sólidos in situ.
- O volume total deriva do volume mensal multiplicado pelo prazo.
- A massa seca deriva do volume total multiplicado pelo teor de sólidos in situ.
- O volume desaguado deriva da massa seca dividida pelo teor de sólidos desaguado.
- Distância e linha flutuante aceitam uma parcela adicional denominada `seio da linha`.

### Entidades conceituais
Proposta, cliente, obra, material, volume dragado, massa seca, volume desaguado, teor de sólidos, prazo, produção mínima, linha de recalque, linha flutuante, linha de terra, bota-fora, sistema de medição, responsabilidade por canteiro e mobilização, jornada.

### Dúvidas
- O título `SANEPAR / XISTO` e o local `Suzano - SP` representam a mesma oportunidade, uma adaptação ou um reaproveitamento de planilha?
- A produção de 1.414 t/mês é obrigação contratual, capacidade mínima ou meta interna?
- O prazo de 11,5 meses inclui mobilização e desmobilização?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `O5` = `=(M10*M6)/M7`
- `M8` = `=(M5*M7)/M6`
- `P9` = `=M10*M6`
- `M10` = `=M8*M9`
- `L13` = `=M10`
- `O13` = `=M13+N13`
- `Q13` = `=L13*P13`
- `S13` = `=Q13/R13`
- `B15` = `=L13`
- `Q16` = `=SUM(Q13:Q15)`
- `S16` = `=SUM(S13:S15)`
- `H17` = `=B17+E17`
- `H18` = `=B18+E18`
- `G22` = `=B22*D22*B21`

## 2. Aba `Fornecedores`

### Objetivo e papel no fluxo
Preservar cotações e contatos de fornecedores, principalmente para guindaste de 100 t e, de forma ainda não preenchida, containers.

### Evidências confirmadas
- Empresas registradas: TRUCKAP, ENGEGUIND e SÃO JOSÉ.
- Para ENGEGUIND: diária de R$ 6.500, plano de rigger de R$ 1.500, mobilização de R$ 6.000, desmobilização de R$ 6.000 e integração antecipada como cortesia.
- Para SÃO JOSÉ: diária, mobilização e desmobilização de R$ 6.500 cada.
- Há cabeçalho para `CONTAINER`, mas sem fornecedores preenchidos.

### Regra implícita — EVIDÊNCIA PARCIAL
A planilha funciona como memória de cotação datada e fonte manual para valores utilizados nas abas de mobilização e desmobilização.

### Dúvidas
- Qual a data-base exata das cotações desta aba?
- Os preços incluem impostos, operador, combustível e plano de içamento?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- Nenhuma fórmula identificada.

## 3. Aba `Historico - PALOTINA`

### Objetivo e papel no fluxo
Registrar histórico operacional de percentual de sólidos após desaguamento usado como referência para a premissa de 22%.

### Evidências confirmadas
- Cinco observações históricas: 22,00%; 23,27%; 22,96%; 20,76%; 21,20%.
- Média calculada: 22,038%, apresentada como 22,04%.
- O título identifica `PALOTINA`.

### Regra implícita — EVIDÊNCIA PARCIAL
O percentual de sólidos desaguado adotado no orçamento é sustentado por média histórica de resultados informados pela SANEPAR.

### Dúvidas
- As datas numéricas representam medições mensais em 2020?
- As condições de Palotina são comparáveis ao lodo da obra em Suzano?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `B10` = `=AVERAGE(B5:B9)`

## 4. Aba `Produção (NOVO CALCULO)`

### Objetivo e papel no fluxo
Estimar capacidade de desaguamento para uma centrífuga de 40 m³/h em regimes de 24 h e 16 h, considerando concentração de alimentação e teor final de sólidos.

### Evidências confirmadas
- Capacidade nominal usada: 40 m³/h.
- Dias de trabalho: 26.
- Teor de sólidos desaguado: 22%.
- São analisadas concentrações de alimentação de 1,6%, 2,0% e 2,44%.
- Para 24 h/3 turnos, resultados mensais de material desaguado: 1.270,69; 1.588,36; 1.937,80 t/mês.
- Para 16 h/2 turnos, resultados mensais: 968,15; 1.210,18; 1.476,42 t/mês.
- O orçamento usa 436,8 h/mês como horas trabalhadas na operação principal.
- Há indicação de higienização e tempos úteis derivados de horários de turnos.

### Regras observadas
- Massa seca por hora = vazão volumétrica × concentração de sólidos.
- Massa desaguada por hora = massa seca por hora ÷ teor de sólidos desaguado.
- Produção diária = produção horária × tempo útil diário.
- Produção mensal = produção diária × dias de trabalho.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA
- `S10` contém fórmula quebrada `#REF!-S9` e resultado `#REF!`.
- Há textos e cálculos residuais, incluindo referência a `20 metros de skid - centrifuga de 60M3/h`, embora o cálculo principal use centrífuga de 40 m³/h.
- O título do arquivo indica três turnos, mas o arquivo mantém também cenário de dois turnos.

### Dúvidas
- Qual concentração de alimentação foi efetivamente escolhida para o orçamento final?
- O fator de tempo útil de 16,8 h/dia para o cenário de 24 h decorre de higienização, troca de turnos ou disponibilidade?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `L1` = `='Dados Obra '!M6`
- `M1` = `=L1/40`
- `E2` = `=C2`
- `J5` = `=L1*M1`
- `D6` = `='Dados Obra '!B28`
- `D7` = `='Dados Obra '!M7`
- `H9` = `=D10+E10-F10-G10`
- `I9` = `=H10*0.75`
- `J9` = `=I10*D6`
- `L9` = `='Dados Obra '!B27`
- `S9` = `=NOW()-S8`
- `D10` = `=TIME(7,0,0)`
- `E10` = `=TIME(19,0,0)`
- `F10` = `=TIME(12,0,0)`
- `G10` = `=TIME(1,0,0)`
- `H10` = `=(E10-D10-F10-G10)*24`
- `I10` = `=H10*0.75`
- `J10` = `=H10*D6`
- `L10` = `=H10/L9`
- `S10` = `=#REF!-S9`
- `D11` = `=TIME(7,0,0)`
- `E11` = `=TIME(15,0,0)`
- `F11` = `=TIME(8,0,0)`
- `L11` = `=L9*L10`
- `D12` = `=TIME(15,0,0)`
- `E12` = `=TIME(23,0,0)`
- `F12` = `=TIME(8,0,0)`
- `H13` = `=(E12-D11)*24`
- `I13` = `=H13*0.8`
- `E14` = `=TIME(16,0,0)`
- `F14` = `=TIME(17,0,0)`
- `E15` = `=TIME(7,0,0)`
- `F15` = `=TIME(7,0,0)`
- `E16` = `=TIME(9,0,0)`
- `F16` = `=TIME(10,0,0)`
- `B18` = `=D7`
- `C26` = `=C2*C24`
- `D26` = `=D2*D24`
- `E26` = `=E2*E24`
- `C27` = `=C26/$B$18`
- `D27` = `=D26/$B$18`
- `E27` = `=E26/$B$18`
- `C28` = `=C27*$H$10`
- `D28` = `=D27*$H$10`
- `E28` = `=E27*$H$10`
- `C29` = `=C28*$D$6`
- `D29` = `=D28*$D$6`
- `E29` = `=E28*$D$6`
- `C40` = `=C2*C38`
- `D40` = `=D2*D38`
- `E40` = `=E2*E38`
- `C41` = `=C40/$B$18`
- `D41` = `=D40/$B$18`
- `E41` = `=E40/$B$18`
- `C42` = `=C41*$I$13`
- `D42` = `=D41*$I$13`
- `E42` = `=E41*$I$13`
- `C43` = `=C42*$D$6`
- `D43` = `=D42*$D$6`
- `E43` = `=E42*$D$6`

## 5. Aba `1. Canteiro`

### Objetivo e papel no fluxo
Compor implantação e manutenção do canteiro, incluindo mão de obra de integração, containers, consumíveis e referências de mobiliário.

### Evidências confirmadas
- Equipe de integração: 1 encarregado, 3 operadores de draga, 3 operadores de centrífuga e 12 ajudantes.
- Custo diário calculado: R$ 6.261,845.
- Leis sociais: 110%.
- Prazo: 11,5 meses.
- Itens com custo: container almoxarifado, container sanitário/vestiário, material de limpeza, material de escritório e oito dias de integração.
- Total: R$ 88.044,76.
- Conversão para custo mensal: R$ 7.656,0661.
- BDI interno da aba: 0%.
- Há quadro de turnos que totaliza 19 pessoas e referências de preços de mobiliário e tendas.

### Regras observadas
- Mão de obra diária = quantidade × valor-hora × 9 h × (1 + 110%).
- Itens mensais = quantidade de meses × preço unitário.
- Custo mensal do canteiro = total de implantação/custeio ÷ prazo de operação.
- O custo mensal é reutilizado nas abas operacionais.

### Dúvidas
- Por que a jornada usada na integração é 9 h, enquanto a operação global está definida como 16 h/dia?
- Os custos de mobiliário à direita são somente memória de preço ou compõem algum total?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `A4` = `=L7`
- `F4` = `=(A4*C4*D4)*(E4/100+1)`
- `F5` = `=(A5*C5*D5)*(E5/100+1)`
- `A6` = `=L9`
- `F6` = `=(A6*C6*D6)*(E6/100+1)`
- `A7` = `=L11`
- `F7` = `=(A7*C7*D7)*(E7/100+1)`
- `A8` = `=L12`
- `F8` = `=(A8*C8*D8)*(E8/100+1)`
- `A9` = `=L13`
- `F9` = `=A9*C9`
- `A10` = `=A9`
- `F10` = `=A10*C10`
- `F11` = `=SUM(F4:F10)`
- `L6` = `=SUM(I6:K6)`
- `L7` = `=SUM(I7:K7)`
- `N7` = `=M7*1.25`
- `L8` = `=SUM(I8:K8)`
- `L9` = `=SUM(I9:K9)`
- `N9` = `=M9*1.25`
- `L10` = `=SUM(I10:K10)`
- `L11` = `=SUM(I11:K11)`
- `N11` = `=M11*1.25`
- `L12` = `=SUM(I12:K12)`
- `L13` = `=SUM(I13:K13)`
- `D14` = `='Dados Obra '!M9`
- `F14` = `=D14*E14`
- `D15` = `='Dados Obra '!M9`
- `F15` = `=D15*E15`
- `D16` = `=$F$30`
- `F16` = `=D16*E16`
- `D17` = `=$F$30`
- `F17` = `=D17*E17`
- `F18` = `=D18*E18`
- `F19` = `=D19*E19`
- `K19` = `=I19*J19`
- `F20` = `=D20*E20`
- `K20` = `=I20*J20`
- `F21` = `=D21*E21`
- `K21` = `=I21*J21`
- `F22` = `=D22*E22`
- `K22` = `=I22*J22`
- `F23` = `=D23*E23`
- `K23` = `=I23*J23`
- `F24` = `=D24*E24`
- `K24` = `=I24*J24`
- `D25` = `=$F$30`
- `F25` = `=D25*E25`
- `K25` = `=I25*J25`
- `D26` = `=$F$30`
- `F26` = `=D26*E26`
- `K26` = `=SUM(K19:K25)`
- `F27` = `=D27*E27`
- `F28` = `=D28*E28`
- `F29` = `=SUM(F14:F28)`
- `F30` = `='Dados Obra '!M9`
- `F31` = `=F29/F30`
- `F32` = `=F31*(E32/100)`
- `F33` = `=F31+F32`

## 6. Aba `2.1 Mob Draga`

### Objetivo e papel no fluxo
Compor a mobilização da draga e elementos associados ao canteiro.

### Evidências confirmadas
- Equipe de mobilização: operador líder, 2 operadores de draga, 2 ajudantes, refeições e transporte.
- Custo diário: R$ 2.115,43.
- Recursos principais: 3 carretas carga seca, guindaste de descarga/montagem, plano de rigger, mobilização do guindaste, munck, frete de containers, mobiliário, segurança, programas legais, ART, tenda, bebedouro e exames.
- Cinco dias de mão de obra.
- Total e preço final: R$ 157.289,46; BDI interno 0%.
- Observações registram cotações e datas por WhatsApp.

### Regras observadas
- Mão de obra diária segue quantidade × valor-hora × 9 h × (1 + 110%).
- Cada serviço é quantidade × preço unitário.
- A quantidade de pessoas deriva do quadro de turnos.
- O total é soma das linhas de serviço e da mão de obra de mobilização.

### Dúvidas
- Alguns itens têm quantidade vazia e preço informado; representam opções não selecionadas?
- O título menciona draga de 10", elétrica ou miúda; qual equipamento é efetivamente mobilizado?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `A5` = `=M5`
- `F5` = `=(A5*C5*D5)*(E5/100+1)`
- `F6` = `=(A6*C6*D6)*(E6/100+1)`
- `A7` = `=M9-M10`
- `F7` = `=(A7*C7*D7)*(E7/100+1)`
- `F8` = `=(A8*C8*D8)*(E8/100+1)`
- `A9` = `=M10-M9`
- `F9` = `=(A9*C9*D9)*(E9/100+1)`
- `A10` = `=M10+M9-M5`
- `F10` = `=A10*C10`
- `A11` = `=A10`
- `F11` = `=A11*C11`
- `F12` = `=SUM(F5:F11)`
- `I12` = `='1. Canteiro'!I11`
- `J12` = `='1. Canteiro'!J11`
- `K12` = `='1. Canteiro'!K11`
- `M12` = `=SUM(I12:K12)`
- `I13` = `='1. Canteiro'!I12`
- `J13` = `='1. Canteiro'!J12`
- `K13` = `='1. Canteiro'!K12`
- `M13` = `=SUM(I13:K13)`
- `I5` = `='1. Canteiro'!I7`
- `J5` = `='1. Canteiro'!J7`
- `K5` = `='1. Canteiro'!K7`
- `M5` = `=SUM(I5:K5)`
- `I6` = `='1. Canteiro'!I8`
- `J6` = `='1. Canteiro'!J8`
- `K6` = `='1. Canteiro'!K8`
- `M6` = `=SUM(I6:K6)`
- `I9` = `='1. Canteiro'!I9`
- `J9` = `='1. Canteiro'!J9`
- `K9` = `='1. Canteiro'!K9`
- `M9` = `=SUM(I9:K9)`
- `I10` = `='1. Canteiro'!I10`
- `J10` = `='1. Canteiro'!J10`
- `K10` = `='1. Canteiro'!K10`
- `M10` = `=SUM(I10:K10)`
- `F15` = `=D15*E15`
- `F16` = `=D16*E16`
- `F17` = `=D17*E17`
- `F18` = `=D18*E18`
- `F19` = `=D19*E19`
- `F20` = `=D20*E20`
- `F21` = `=D21*E21`
- `F22` = `=D22*E22`
- `F23` = `=D23*E23`
- `F24` = `=D24*E24`
- `F25` = `=D25*E25`
- `F26` = `=D26*E26`
- `F27` = `=D27*E27`
- `F28` = `=D28*E28`
- `F29` = `=D29*E29`
- `F30` = `=D30*E30`
- `F31` = `=D31*E31`
- `F32` = `=D32*E32`
- `F33` = `=D33*E33`
- `F34` = `=D34*E34`
- `F35` = `=D35*E35`
- `F36` = `=D36*E36`
- `F37` = `=SUM(F15:F36)`
- `F38` = `=F37*(E38/100)`
- `F39` = `=F37+F38`
- `C42` = `=SUM(C38:C41)`

## 7. Aba `2.2 Mob Centr`

### Objetivo e papel no fluxo
Compor a mobilização da centrífuga e seus skids, tanques e periféricos.

### Evidências confirmadas
- Equipe: operador líder, 3 operadores de centrífuga, 9 ajudantes, refeições e transporte.
- Custo diário: R$ 3.957,50.
- Recursos com custo: instalações elétricas, exames, carreta de equipamentos complementares e cinco dias de mão de obra.
- Total e preço final: R$ 220.864,30; BDI interno 0%.
- Quadro logístico indica cinco carretas para skids, tanques de equalização e periféricos.

### Regras observadas
- Estrutura semelhante à mobilização da draga, mas com composição de pessoal e logística específica da centrífuga.
- Valores não selecionados permanecem estruturados com quantidade vazia ou zero.

### Dúvidas
- O total elevado em relação às linhas visíveis depende de fórmulas e células não rotuladas; a composição necessita validação operacional.
- Quais itens pertencem à centrífuga comprada, à locada ou ao skid GRATT?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `A5` = `=M5`
- `F5` = `=(A5*C5*D5)*(E5/100+1)`
- `F6` = `=(A6*C6*D6)*(E6/100+1)`
- `F7` = `=(A7*C7*D7)*(E7/100+1)`
- `A8` = `=M12`
- `F8` = `=(A8*C8*D8)*(E8/100+1)`
- `A9` = `=M13`
- `F9` = `=(A9*C9*D9)*(E9/100+1)`
- `A10` = `=M12+M13+M5`
- `F10` = `=A10*C10`
- `A11` = `=A10`
- `F11` = `=A11*C11`
- `F12` = `=SUM(F5:F11)`
- `I12` = `='1. Canteiro'!I11`
- `J12` = `='1. Canteiro'!J11`
- `K12` = `='1. Canteiro'!K11`
- `M12` = `=SUM(I12:K12)`
- `I13` = `='1. Canteiro'!I12`
- `J13` = `='1. Canteiro'!J12`
- `K13` = `='1. Canteiro'!K12`
- `M13` = `=SUM(I13:K13)`
- `I5` = `='1. Canteiro'!I7`
- `J5` = `='1. Canteiro'!J7`
- `K5` = `='1. Canteiro'!K7`
- `M5` = `=SUM(I5:K5)`
- `I6` = `='1. Canteiro'!I8`
- `J6` = `='1. Canteiro'!J8`
- `K6` = `='1. Canteiro'!K8`
- `M6` = `=SUM(I6:K6)`
- `I9` = `='1. Canteiro'!I9`
- `J9` = `='1. Canteiro'!J9`
- `K9` = `='1. Canteiro'!K9`
- `M9` = `=SUM(I9:K9)`
- `I10` = `='1. Canteiro'!I10`
- `J10` = `='1. Canteiro'!J10`
- `K10` = `='1. Canteiro'!K10`
- `M10` = `=SUM(I10:K10)`
- `F15` = `=D15*E15`
- `F16` = `=D16*E16`
- `F17` = `=D17*E17`
- `F18` = `=D18*E18`
- `F19` = `=D19*E19`
- `F20` = `=D20*E20`
- `F21` = `=D21*E21`
- `F22` = `=D22*E22`
- `F23` = `=D23*E23`
- `F24` = `=D24*E24`
- `F25` = `=D25*E25`
- `F26` = `=D26*E26`
- `F27` = `=D27*E27`
- `F28` = `=D28*E28`
- `F29` = `=D29*E29`
- `F30` = `=D30*E30`
- `F31` = `=D31*E31`
- `F32` = `=D32*E32`
- `F33` = `=D33*E33`
- `F34` = `=D34*E34`
- `F35` = `=SUM(F15:F34)`
- `F36` = `=F35*(E36/100)`
- `F37` = `=F35+F36`
- `C42` = `=SUM(C38:C41)`

## 8. Aba `4.1 Draga Dec`

### Objetivo e papel no fluxo
Calcular o custo mensal e total da dragagem que alimenta o sistema de desidratação.

### Estrutura observada — EVIDÊNCIA CONFIRMADA
A aba é dividida em: operação; pessoal; encargos; alimentação; alojamento; viagens; prêmios; manutenção; equipamentos de apoio; administrativas; BDI interno; financeiras; resumo; custo mensal, custo total e preço por hora.

### Valores principais
- Valor do equipamento: R$ 350.000.
- Horas mensais: 436,8; eficiência operacional: 90%.
- Custo de operação: R$ 4.810,808/mês.
- Pessoal direto: encarregado, 3 operadores de draga e 3 ajudantes.
- Salários calculados: R$ 36.488,3966; encargos de 110%: R$ 40.137,2363.
- Alimentação: R$ 9.930; alojamento: R$ 3.600; viagens de folga: R$ 3.200.
- Total de pessoal: R$ 93.355,6328.
- Manutenção: R$ 6.600.
- Equipamentos de apoio: linha de recalque, automóvel, ferramentas e custo mensal do canteiro.
- Despesas administrativas: R$ 1.750.
- Despesas diretas: R$ 122.041,0347.
- BDI interno de oficina e administração: R$ 12.204,1035.
- Financeiras: R$ 9.333,3333.
- Custo mensal total: R$ 143.578,4715.
- Prazo: 11,5 meses.
- Custo total da dragagem: R$ 1.651.152,4225.
- Preço de venda mensal auxiliar: custo × 1,6.
- Preço por hora auxiliar: R$ 368,1499, usando fator 0,7.

### Regras observadas
- Horas remuneradas mensais combinam horas extras a 70%, horas a 100% e horas normais.
- Encargos = 110% dos salários.
- Manutenção usa percentuais sobre o valor do equipamento mais valores fixos.
- Depreciação = valor do equipamento ÷ 60 meses.
- Juros = 1% do valor do equipamento.
- Custo total = custo mensal × prazo.
- Linha de recalque é custeada por depreciação e juros de tubulação, flutuantes e acoplamentos.

### Anomalias observadas
- `D178`, `H188` e `I188` contêm `#REF!`; `J188` propaga o erro.
- Algumas fórmulas referenciam `'Dados Obra '` com espaço final, enquanto o nome exibido da aba é `Dados Obra`.
- `D184`, preço de venda por m³, resulta zero porque depende de produção quebrada.
- A descrição menciona `Operação do Sistema de Desidratação de lodo`, mas a aba calcula principalmente dragagem.

### Dúvidas
- O custo de energia/combustível da draga elétrica é responsabilidade da SANEPAR ou da FOS? Há textos contraditórios.
- O fator 0,7 aplicado ao preço por hora representa produtividade, disponibilidade ou margem comercial?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `C9` = `='Produção (NOVO CALCULO)'!J10`
- `F10` = `=C9*D9*E9*F9`
- `F11` = `=(C9*D9*E9*L12)*0.1`
- `E15` = `=F10+F11+F12+F13`
- `A20` = `=L24`
- `E20` = `=D20*B20*A20`
- `K20` = `='Dados Obra '!B28`
- `L20` = `=J20*K20`
- `A21` = `=L24`
- `B21` = `='2.1 Mob Draga'!M5`
- `D21` = `='1. Canteiro'!C4`
- `L21` = `=J21*K21`
- `A22` = `=L24`
- `D22` = `='1. Canteiro'!C6`
- `A23` = `=L24`
- `D23` = `='1. Canteiro'!C8`
- `L23` = `=J23*K23`
- `A24` = `=L24`
- `D24` = `='1. Canteiro'!C5`
- `L24` = `=(L20*1.7)+(L21*2)+L23`
- `A25` = `=L24`
- `A26` = `=L24`
- `A27` = `=L24`
- `E27` = `=D27*B27*A27`
- `K28` = `=I28*J28`
- `K29` = `=J29*I29`
- `E31` = `=E20+E21+E22+E23+E24+E25+E26+E27+E28`
- `K31` = `=(K28+K29)*K30`
- `K33` = `=K32+K31`
- `C37` = `=E31`
- `E37` = `=(C37*A37)/100`
- `E46` = `=G52+G53`
- `B52` = `=B21+B22`
- `G52` = `=B52*(C52+D52+E52)*F52`
- `B53` = `=B23+B24`
- `G53` = `=B53*(C53+D53+E53)*F53`
- `E62` = `=C59+C60+C61+C62`
- `B69` = `=B52`
- `E69` = `=D69*B69`
- `E71` = `=SUM(E67:E69)`
- `G87` = `=E71+E62+E46+E37+E31`
- `E92` = `=(0.6/100)*F7`
- `E93` = `=(1/100)*F7`
- `E97` = `=E92+E93+E94+E95`
- `H99` = `=E97`
- `E103` = `=K120`
- `I104` = `='Dados Obra '!H17`
- `K104` = `=I104*J104`
- `J105` = `=K104/I105`
- `J106` = `=K104*(1/100)`
- `J107` = `=J105+J106`
- `I109` = `='Dados Obra '!H18/4`
- `K109` = `=I109*J109`
- `J110` = `=K109/I110`
- `J111` = `=K109*(1/100)`
- `J112` = `=J110+J111`
- `I114` = `='Dados Obra '!H17/12`
- `K114` = `=I114*J114`
- `J115` = `=K114/I115`
- `J116` = `=K114*(1/100)`
- `J117` = `=J115+J116`
- `H120` = `=J107`
- `I120` = `=J112`
- `J120` = `=J117`
- `K120` = `=SUM(H120:J120)`
- `D114` = `=SUM(E103:E112)`
- `E131` = `=SUM(E126:E130)`
- `G134` = `=E15+G87+E97+D114+E131`
- `E138` = `=G134*5%`
- `E139` = `=G134*5%`
- `E142` = `=SUM(E138:E140)`
- `E145` = `=F7/60`
- `E146` = `=F7*1%`
- `E149` = `=SUM(E145:E147)`
- `D163` = `=E15`
- `D164` = `=G87`
- `D165` = `=E97`
- `D166` = `=D114`
- `D167` = `=E131`
- `D168` = `=SUM(D163:D167)`
- `D171` = `=E142`
- `D173` = `=E149`
- `D175` = `=SUM(D168,D171,D173)`
- `D178` = `=#REF!`
- `D180` = `=D175/D178`
- `D184` = `=D180*(1+A182/100)`
- `D187` = `=D175/24/60*1.374`
- `H188` = `=#REF!`
- `I188` = `=#REF!`
- `J188` = `=H188*I188`
- `D197` = `=D175`
- `D199` = `=D197+D198`
- `D200` = `='Dados Obra '!M9`
- `D201` = `=D199*D200`
- `J200` = `=D199`
- `J201` = `=1.6`
- `J202` = `=J200*J201`
- `J203` = `='Produção (NOVO CALCULO)'!J10`
- `J204` = `=70%`
- `J206` = `=J202/(J203*J204)`

## 9. Aba `4.2 Centrífuga`

### Objetivo e papel no fluxo
Calcular custo mensal e total da operação do decanter/centrífuga.

### Estrutura observada — EVIDÊNCIA CONFIRMADA
Repete a estrutura de operação, pessoal, encargos, alimentação, alojamento, viagens, manutenção, apoio, administrativas, BDI interno, financeiras, resumo e consolidação.

### Valores principais
- Valor do equipamento: R$ 1.200.000.
- Três skids GRATT de 40" são registrados a R$ 1.500.000 cada, totalizando R$ 4.500.000 em quadro auxiliar; o cálculo financeiro principal usa R$ 1.200.000.
- Horas mensais: 436,8.
- Custo operacional: R$ 3.100,0393.
- Equipe principal: 9 ajudantes e 3 operadores de decanter.
- Salários: R$ 40.013,3853; encargos 110%: R$ 44.014,7238.
- Alimentação: R$ 13.590; alojamento: R$ 2.300; viagens: R$ 1.500.
- Total de pessoal: R$ 101.418,1091.
- Manutenção: R$ 7.000.
- Despesas diretas: R$ 116.818,1484.
- BDI interno: R$ 11.681,8148.
- Financeiras: R$ 26.000.
- Custo mensal total: R$ 154.499,9633.
- Produção prevista: 3.825,36 m³/mês.
- Prazo: 11,5 meses.
- Total da operação: R$ 1.776.749,5778.
- Preço de venda mensal auxiliar: custo × 1,6.
- Preço por hora auxiliar: R$ 396,1538.

### Regras observadas
- Manutenção de peças usa 0,5% do valor do equipamento, embora o rótulo mencione 0,1%.
- Depreciação = valor do equipamento ÷ 60.
- Juros de capital = 0,5% do valor do equipamento.
- A produção prevista referencia a aba de produção.
- Total da operação = custo mensal × prazo.

### Anomalias observadas
- `D187` contém referência quebrada multiplicada por 0,6 e 0,62.
- O rótulo da manutenção (0,1%) diverge do cálculo observado (0,5%).
- Existem quadros auxiliares com valores de aquisição distintos e sem ligação clara ao total principal.
- Fórmulas também referenciam `'Dados Obra '` com espaço final.

### Dúvidas
- Qual valor de ativo deve fundamentar depreciação, juros e manutenção: R$ 1,2 milhão, R$ 1,5 milhão por skid ou o conjunto de R$ 4,5 milhões?
- A produção de 3.825,36 m³/mês representa lodo de alimentação, lodo desaguado ou capacidade hidráulica?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `R7` = `=P7*Q7`
- `C9` = `='4.1 Draga Dec'!C9`
- `F10` = `=C9*D9*E9*F9`
- `F11` = `=1100`
- `E15` = `=F10+F11+F12+F13`
- `A20` = `=L24`
- `E20` = `=D20*B20*A20`
- `K20` = `='Dados Obra '!B28`
- `L20` = `=J20*K20`
- `A21` = `=L24`
- `L21` = `=J21*K21`
- `A22` = `=L24`
- `A23` = `=L24`
- `D23` = `='1. Canteiro'!C8`
- `L23` = `=J23*K23`
- `A24` = `=L24`
- `D24` = `='1. Canteiro'!C7`
- `L24` = `=(L20*1.7)+(L21*2)+L23`
- `A25` = `=L24`
- `A26` = `=L24`
- `A27` = `=L24`
- `E27` = `=D27*B27*A27`
- `K27` = `=I27*J27`
- `K28` = `=J28*I28`
- `E31` = `=E20+E21+E22+E23+E24+E25+E26+E27+E28`
- `K30` = `=K27+K28`
- `K31` = `=220`
- `K32` = `=K31+K30`
- `C37` = `=E31`
- `E37` = `=(C37*A37)/100`
- `E46` = `=G52+G53`
- `B52` = `=B23/B24`
- `G52` = `=B52*(C52+D52+E52)*F52`
- `B53` = `=B23`
- `G53` = `=B53*(C53+D53+E53)*F53`
- `E62` = `=C59+C60+C61+C62`
- `B69` = `=B52`
- `E69` = `=D69*B69`
- `E71` = `=SUM(E67:E69)`
- `G87` = `=E71+E62+E46+E37+E31`
- `E92` = `=(0.5/100)*F7`
- `E93` = `=0`
- `E97` = `=E92+E93+E94+E95`
- `H99` = `=E97`
- `K9` = `=SUM(K5:K8)`
- `E103` = `=K120`
- `I104` = `='Dados Obra '!H17`
- `K104` = `=I104*J104`
- `J105` = `=K104/I105`
- `J106` = `=K104*(1/100)`
- `J107` = `=J105+J106`
- `I109` = `='Dados Obra '!H18/4`
- `K109` = `=I109*J109`
- `J110` = `=K109/I110`
- `J111` = `=K109*(1/100)`
- `J112` = `=J110+J111`
- `I114` = `='Dados Obra '!H17/12`
- `K114` = `=I114*J114`
- `J115` = `=K114/I115`
- `J116` = `=K114*(1/100)`
- `J117` = `=J115+J116`
- `H120` = `=J107`
- `I120` = `=J112`
- `J120` = `=J117`
- `K120` = `=SUM(H120:J120)`
- `D114` = `=SUM(E103:E112)`
- `E131` = `=SUM(E126:E130)`
- `G134` = `=E15+G87+E97+D114+E131`
- `E138` = `=G134*5%`
- `E139` = `=G134*5%`
- `E142` = `=SUM(E138:E140)`
- `E145` = `=F7/60`
- `E146` = `=F7*0.5%`
- `E149` = `=SUM(E145:E147)`
- `D163` = `=E15`
- `D164` = `=G87`
- `D165` = `=E97`
- `D166` = `=D114`
- `D167` = `=E131`
- `D168` = `=SUM(D163:D167)`
- `D171` = `=E142`
- `D173` = `=E149`
- `D175` = `=SUM(D168,D171,D173)`
- `D178` = `='Produção (NOVO CALCULO)'!D42*D188`
- `D180` = `=D175/D178`
- `D184` = `=D180*(1+B182/100)`
- `D187` = `=#REF!*0.6*0.62`
- `H188` = `=22`
- `I188` = `=9`
- `J188` = `=H188*I188`
- `D197` = `=D175`
- `D198` = `='Dados Obra '!M9`
- `D199` = `=D197*D198`
- `D201` = `=D199+D200`
- `J199` = `=D197`
- `J200` = `=1.6`
- `J201` = `=J199*J200`
- `J202` = `='4.1 Draga Dec'!J203`
- `J203` = `='4.1 Draga Dec'!J204`
- `J205` = `=J201/(J202*J203)`
- `Q109` = `=12`

## 10. Aba `Op. Centrifuga`

### Objetivo e papel no fluxo
Calcular o fornecimento de polímero para o período operacional.

### Evidências confirmadas
- Dosagem: 13 kg de polímero por tonelada de base seca.
- Base seca total referenciada: 3.577,42 t.
- Quantidade total: 46.506,46 kg.
- Preço unitário: R$ 18,5161/kg.
- Custo total: R$ 861.116,28.

### Regra observada
Quantidade de polímero = toneladas de base seca × dosagem em kg/t; custo = quantidade × preço unitário.

### Dúvidas
- A dosagem de 13 kg/t é específica do lodo de xisto, histórica ou garantida por fornecedor?
- O preço do polímero possui data-base e fornecedor?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `E16` = `='Dados Obra '!P9`
- `E17` = `=C17*E16`
- `E18` = `=C18*E17`
- `E19` = `=C19*E18`

## 11. Aba `Transp e Destinacao`

### Objetivo e papel no fluxo
Registrar estimativa de transporte e destinação final do material desaguado.

### Evidências confirmadas
- Quantidade estimada: 18.000 t.
- Preço unitário: R$ 388,8889/t.
- Custo total: R$ 7.000.000.
- BDI comercial na planilha final: 30%, gerando preço de venda de R$ 9.100.000.

### Regra observada
Custo total = quantidade × preço unitário.

### Dúvidas
- A quantidade de 18.000 t diverge do volume desaguado total de 16.261 m³ e da base seca de 3.577 t; é massa úmida projetada, limite contratual ou arredondamento?
- O preço inclui transporte, taxa de aterro, impostos e documentação ambiental?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `E18` = `=C18*D18`
- `E19` = `=SUM(E18:E18)`

## 12. Aba `5. Desmob Canteiro`

### Objetivo e papel no fluxo
Estruturar desmobilização do canteiro e equipe de retirada.

### Evidências confirmadas
- A aba mantém quadro de mão de obra e itens de canteiro, mas quantidades dos serviços estão zeradas ou vazias.
- O total calculado é zero.

### Anomalias observadas
- Prazo (`F30`) está quebrado com `#REF!`.
- Preço unitário, BDI e preço final (`F31:F33`) propagam o erro.
- O documento final não referencia esta aba diretamente.

### Dúvidas
- A desmobilização do canteiro está incorporada às abas `Desmob Draga` e `Desmob Centr`?
- A aba é resíduo de modelo anterior ou custo ainda pendente?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `A4` = `=L7`
- `F4` = `=(A4*C4*D4)*(E4/100+1)`
- `A5` = `=L8`
- `F5` = `=(A5*C5*D5)*(E5/100+1)`
- `A6` = `=L9`
- `F6` = `=(A6*C6*D6)*(E6/100+1)`
- `A7` = `=L11`
- `F7` = `=(A7*C7*D7)*(E7/100+1)`
- `A8` = `=L12`
- `F8` = `=(A8*C8*D8)*(E8/100+1)`
- `A9` = `=L13`
- `F9` = `=A9*C9`
- `A10` = `=A9`
- `F10` = `=A10*C10`
- `F11` = `=SUM(F4:F10)`
- `L6` = `=SUM(I6:K6)`
- `L7` = `=SUM(I7:K7)`
- `N7` = `=M7*1.25`
- `L8` = `=SUM(I8:K8)`
- `L9` = `=SUM(I9:K9)`
- `N9` = `=M9*1.25`
- `L10` = `=SUM(I10:K10)`
- `L11` = `=SUM(I11:K11)`
- `N11` = `=M11*1.25`
- `L12` = `=SUM(I12:K12)`
- `L13` = `=SUM(I13:K13)`
- `F14` = `=D14*E14`
- `F15` = `=D15*E15`
- `F16` = `=D16*E16`
- `F17` = `=D17*E17`
- `F18` = `=D18*E18`
- `F19` = `=D19*E19`
- `K19` = `=I19*J19`
- `F20` = `=D20*E20`
- `K20` = `=I20*J20`
- `F21` = `=D21*E21`
- `K21` = `=I21*J21`
- `F22` = `=D22*E22`
- `K22` = `=I22*J22`
- `F23` = `=D23*E23`
- `K23` = `=I23*J23`
- `F24` = `=D24*E24`
- `K24` = `=I24*J24`
- `F25` = `=D25*E25`
- `K25` = `=I25*J25`
- `F26` = `=D26*E26`
- `K26` = `=SUM(K19:K25)`
- `F27` = `=D27*E27`
- `F28` = `=D28*E28`
- `F29` = `=SUM(F14:F28)`
- `F30` = `=#REF!`
- `F31` = `=F29/F30`
- `F32` = `=F31*(E32/100)`
- `F33` = `=F31+F32`

## 13. Aba `Desmob Draga`

### Objetivo e papel no fluxo
Compor a desmobilização da draga.

### Evidências confirmadas
- Equipe: líder, 3 operadores de draga, 3 ajudantes, refeições e transporte.
- Custo diário: R$ 2.883,545.
- Itens com custo: 3 carretas, guindaste, plano de rigger, mobilização do guindaste, munck, fretes, exames e cinco dias de mão de obra.
- Total e preço final: R$ 55.967,725; BDI interno 0%.
- Logística final indica três carretas.

### Regras observadas
Estrutura espelha a mobilização, mas com quantidades e custos próprios de retirada.

### Dúvidas
- Por que mobiliário, segurança, tenda e outros itens permanecem estruturados com quantidade zero?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `A5` = `=M5`
- `F5` = `=(A5*C5*D5)*(E5/100+1)`
- `F6` = `=(A6*C6*D6)*(E6/100+1)`
- `A7` = `=M9-M10`
- `F7` = `=(A7*C7*D7)*(E7/100+1)`
- `F8` = `=(A8*C8*D8)*(E8/100+1)`
- `A9` = `=M10-M9`
- `F9` = `=(A9*C9*D9)*(E9/100+1)`
- `A10` = `=M10+M9-M5`
- `F10` = `=A10*C10`
- `A11` = `=A10`
- `F11` = `=A11*C11`
- `F12` = `=SUM(F5:F11)`
- `I12` = `='1. Canteiro'!I11`
- `J12` = `='1. Canteiro'!J11`
- `K12` = `='1. Canteiro'!K11`
- `M12` = `=SUM(I12:K12)`
- `I13` = `='1. Canteiro'!I12`
- `J13` = `='1. Canteiro'!J12`
- `K13` = `='1. Canteiro'!K12`
- `M13` = `=SUM(I13:K13)`
- `I5` = `='1. Canteiro'!I7`
- `J5` = `='1. Canteiro'!J7`
- `K5` = `='1. Canteiro'!K7`
- `M5` = `=SUM(I5:K5)`
- `I6` = `='1. Canteiro'!I8`
- `J6` = `='1. Canteiro'!J8`
- `K6` = `='1. Canteiro'!K8`
- `M6` = `=SUM(I6:K6)`
- `I9` = `='1. Canteiro'!I9`
- `J9` = `='1. Canteiro'!J9`
- `K9` = `='1. Canteiro'!K9`
- `M9` = `=SUM(I9:K9)`
- `I10` = `='1. Canteiro'!I10`
- `J10` = `='1. Canteiro'!J10`
- `K10` = `='1. Canteiro'!K10`
- `M10` = `=SUM(I10:K10)`
- `F15` = `=D15*E15`
- `F16` = `=D16*E16`
- `F17` = `=D17*E17`
- `F18` = `=D18*E18`
- `F19` = `=D19*E19`
- `F20` = `=D20*E20`
- `F21` = `=D21*E21`
- `F22` = `=D22*E22`
- `F23` = `=D23*E23`
- `F24` = `=D24*E24`
- `F25` = `=D25*E25`
- `F26` = `=D26*E26`
- `F27` = `=D27*E27`
- `F28` = `=D28*E28`
- `F29` = `=D29*E29`
- `F30` = `=D30*E30`
- `F31` = `=D31*E31`
- `F32` = `=D32*E32`
- `F33` = `=D33*E33`
- `F34` = `=D34*E34`
- `F35` = `=SUM(F15:F34)`
- `F36` = `=F35*(E36/100)`
- `F37` = `=F35+F36`
- `C43` = `=SUM(C39:C42)`

## 14. Aba `Desmob Centr`

### Objetivo e papel no fluxo
Compor a desmobilização da centrífuga e seus periféricos.

### Evidências confirmadas
- Equipe: 3 operadores de centrífuga, 9 ajudantes, refeições e transporte.
- Custo diário: R$ 3.957,50.
- Custos selecionados: instalações elétricas, exames, carreta de complementos e cinco dias de mão de obra.
- Total e preço final: R$ 33.487,50; BDI interno 0%.
- Logística registra cinco carretas para skids e tanques.

### Dúvidas
- A descrição de algumas linhas está vazia apesar de preço ou item preenchido.
- A instalação elétrica na desmobilização representa desmontagem elétrica?

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `A5` = `=M5`
- `F5` = `=(A5*C5*D5)*(E5/100+1)`
- `F6` = `=(A6*C6*D6)*(E6/100+1)`
- `F7` = `=(A7*C7*D7)*(E7/100+1)`
- `A8` = `=M12`
- `F8` = `=(A8*C8*D8)*(E8/100+1)`
- `A9` = `=M13`
- `F9` = `=(A9*C9*D9)*(E9/100+1)`
- `A10` = `=M12+M13+M5`
- `F10` = `=A10*C10`
- `A11` = `=A10`
- `F11` = `=A11*C11`
- `F12` = `=SUM(F5:F11)`
- `I12` = `='1. Canteiro'!I11`
- `J12` = `='1. Canteiro'!J11`
- `K12` = `='1. Canteiro'!K11`
- `M12` = `=SUM(I12:K12)`
- `I13` = `='1. Canteiro'!I12`
- `J13` = `='1. Canteiro'!J12`
- `K13` = `='1. Canteiro'!K12`
- `M13` = `=SUM(I13:K13)`
- `I5` = `='1. Canteiro'!I7`
- `J5` = `='1. Canteiro'!J7`
- `K5` = `='1. Canteiro'!K7`
- `M5` = `=SUM(I5:K5)`
- `I6` = `='1. Canteiro'!I8`
- `J6` = `='1. Canteiro'!J8`
- `K6` = `='1. Canteiro'!K8`
- `M6` = `=SUM(I6:K6)`
- `I9` = `='1. Canteiro'!I9`
- `J9` = `='1. Canteiro'!J9`
- `K9` = `='1. Canteiro'!K9`
- `M9` = `=SUM(I9:K9)`
- `I10` = `='1. Canteiro'!I10`
- `J10` = `='1. Canteiro'!J10`
- `K10` = `='1. Canteiro'!K10`
- `M10` = `=SUM(I10:K10)`
- `F15` = `=D15*E15`
- `F16` = `=D16*E16`
- `F17` = `=D17*E17`
- `F18` = `=D18*E18`
- `F19` = `=D19*E19`
- `F20` = `=D20*E20`
- `F21` = `=D21*E21`
- `F22` = `=D22*E22`
- `F23` = `=D23*E23`
- `F24` = `=D24*E24`
- `F25` = `=D25*E25`
- `F26` = `=D26*E26`
- `F27` = `=D27*E27`
- `F28` = `=D28*E28`
- `F29` = `=D29*E29`
- `F30` = `=D30*E30`
- `F31` = `=D31*E31`
- `F32` = `=D32*E32`
- `F33` = `=D33*E33`
- `F34` = `=SUM(F15:F33)`
- `F35` = `=F34*(E35/100)`
- `F36` = `=F34+F35`
- `C42` = `=SUM(C38:C41)`

## 15. Aba `Plan. Final`

### Objetivo e papel no fluxo
Consolidar custos e aplicar BDI comercial para formar preços de venda.

### Evidências confirmadas
Bloco principal:
- Mobilização da draga: custo R$ 157.289,46; BDI 45%; venda R$ 228.069,717.
- Mobilização da centrífuga: custo R$ 220.864,30; BDI 45%; venda R$ 320.253,235.
- Dragagem: custo R$ 1.651.152,4225; quantidade 3.577,42 t; custo unitário R$ 461,5484/t; BDI 50%; venda R$ 2.476.728,6337.
- Operação da centrífuga: custo R$ 1.776.749,5778; quantidade 3.577,42 t; custo unitário R$ 496,6567/t; BDI 50%; venda R$ 2.665.124,3667.
- Polímero: custo R$ 861.116,28; quantidade 46.506,46 kg; custo unitário R$ 18,5161/kg; BDI 40%; venda R$ 1.205.562,792.
- Desmobilização da draga: custo R$ 55.967,725; BDI 45%; venda R$ 81.153,2013.
- Desmobilização da centrífuga: custo R$ 33.487,50; BDI 45%; venda R$ 48.556,875.
- Custo total do bloco: R$ 4.756.627,2653.
- Preço de venda do bloco: R$ 7.025.448,8206.

Bloco separado:
- Transporte e destinação final: custo R$ 7.000.000; BDI 30%; venda R$ 9.100.000.

Total geral:
- Preço de venda total: R$ 16.125.448,8206.

### Regras observadas
- Custo unitário = custo total ÷ quantidade.
- Preço unitário = custo unitário × (1 + BDI).
- Preço total = preço unitário × quantidade.
- Mobilizações e desmobilizações são vendidas por verba (`vb`).
- Dragagem e operação da centrífuga são vendidas por tonelada de base seca.
- Polímero é vendido por quilograma.
- Transporte/destinação é tratado em bloco comercial separado.

### Anomalias e dúvidas
- A linha `Dragagem e desaguamento Centrífuga` funciona como cabeçalho sem valores.
- Células auxiliares com volumes e índices (`L`, `N`, `O`) não possuem rótulos completos.
- O total geral soma os dois blocos, mas não apresenta impostos, condições de pagamento ou validade.
- A planilha não mostra uma linha específica para desmobilização do canteiro.

### Inventário completo de fórmulas — EVIDÊNCIA CONFIRMADA

- `C4` = `='2.1 Mob Draga'!F39`
- `G4` = `=C4/E4`
- `I4` = `=G4*(H4/100+1)`
- `J4` = `=I4*E4`
- `L4` = `=SUM(J4:J5)`
- `C5` = `='2.2 Mob Centr'!F37`
- `G5` = `=C5/E5`
- `I5` = `=G5*(H5/100+1)`
- `J5` = `=I5*E5`
- `O7` = `='Dados Obra '!O5`
- `C8` = `='4.1 Draga Dec'!D201`
- `E8` = `='Dados Obra '!P9`
- `G8` = `=C8/E8`
- `I8` = `=G8*(H8/100+1)`
- `J8` = `=I8*E8`
- `L8` = `=SUM(I8:I10)`
- `N8` = `=L8/N7`
- `O8` = `=L8/O7`
- `C9` = `='4.2 Centrífuga'!D199`
- `E9` = `=E8`
- `G9` = `=C9/E9`
- `I9` = `=G9*(H9/100+1)`
- `J9` = `=I9*E9`
- `C10` = `='Op. Centrifuga'!E19`
- `E10` = `='Op. Centrifuga'!E18`
- `G10` = `=C10/E10`
- `I10` = `=G10*(H10/100+1)`
- `J10` = `=I10*E10`
- `C11` = `='Desmob Draga'!F37`
- `G11` = `=C11/E11`
- `I11` = `=G11*(H11/100+1)`
- `J11` = `=I11*E11`
- `L11` = `=SUM(I11:I12)`
- `C12` = `='Desmob Centr'!F36`
- `G12` = `=C12/E12`
- `I12` = `=G12*(H12/100+1)`
- `J12` = `=I12*E12`
- `C14` = `=SUM(C4:C12)`
- `J14` = `=SUM(J4:J12)`
- `J16` = `=J14/E8`
- `C21` = `='Transp e Destinacao'!E19`
- `G21` = `=C21/E21`
- `I21` = `=G21*(H21/100+1)`
- `J21` = `=I21*E21`
- `C23` = `=SUM(C21:C22)`
- `J23` = `=SUM(J21:J22)`
- `J31` = `=J23+J14`

---

# Conhecimento extraído do arquivo

## Entidades encontradas — EVIDÊNCIA CONFIRMADA

Proposta, cliente, contato, obra, material, lagoa, volume dragado, massa seca, volume desaguado, teor de sólidos, meta de produção, prazo, jornada, turno, equipamento, draga, centrífuga/decanter, skid, tanque de equalização, tanque de preparo de polímero, bomba, linha de recalque, flutuante, acoplamento, canteiro, mobilização, desmobilização, equipe, função, salário, encargos sociais, alimentação, alojamento, viagem, manutenção, depreciação, juros, BDI, polímero, transporte, destinação final, fornecedor, cotação, item comercial, unidade, custo e preço de venda.

## Regras de negócio observadas — EVIDÊNCIA PARCIAL

1. O orçamento parte de um balanço de massa entre lodo in situ, base seca e lodo desaguado.
2. A produção da centrífuga depende da capacidade hidráulica, concentração de alimentação, teor final de sólidos, tempo útil e dias de operação.
3. Mobilização, operação e desmobilização da draga e da centrífuga são composições separadas.
4. O canteiro é composto em valor total e convertido para custo mensal pelo prazo.
5. A mão de obra operacional usa horas remuneradas que combinam horas normais e extras.
6. Encargos sociais de 110% são aplicados sobre salários nas composições observadas.
7. Custos de ativos incluem manutenção, depreciação e juros de capital.
8. Polímero é dimensionado por kg por tonelada de base seca.
9. A formação comercial usa BDI diferente por família de item.
10. Transporte e destinação final são tratados como bloco comercial separado.

Todas permanecem provisórias e específicas desta fonte.

## Coeficientes e parâmetros observados — EVIDÊNCIA CONFIRMADA

- 8% de sólidos in situ.
- 22% de sólidos após desaguamento.
- 13 kg de polímero por tonelada de base seca.
- 110% de encargos sociais.
- 16 h/dia e 26 dias/mês na premissa global.
- 436,8 h/mês nas composições operacionais.
- 90% de eficiência nas abas de custo de equipamentos.
- 60 meses de depreciação.
- BDI comercial: 45% mobilizações/desmobilizações, 50% dragagem e centrífuga, 40% polímero, 30% transporte/destinação.
- Multiplicador auxiliar de 1,6 nas abas de custo mensal.
- Fator auxiliar de 0,7 para preço por hora.

Esses números não são classificados como constantes gerais da FOS.

## Terminologia observada

- `SS`, `ST` e `%ST`: teor de sólidos.
- `Base seca`: massa de sólidos secos.
- `Lodo des`: material após desaguamento.
- `Decanter`: centrífuga.
- `vb`: verba.
- `MDO`: mão de obra.
- `Mob` / `Desmob`: mobilização / desmobilização.
- `Plano de Rigger`: planejamento de içamento.
- `Linha de recalque`, `flutuante`, `acoplamento`: componentes da tubulação de dragagem.

## Anomalias consolidadas — EVIDÊNCIA CONFIRMADA

1. Fórmulas `#REF!` em `Produção (NOVO CALCULO)`, `4.1 Draga Dec`, `4.2 Centrífuga` e `5. Desmob Canteiro`.
2. Referências a `'Dados Obra '` com espaço final.
3. Regime de três turnos coexistindo com premissa de 16 h/dia e cenário de dois turnos.
4. Valores diferentes para ativo da centrífuga em quadros da mesma aba.
5. Rótulo de manutenção de 0,1% divergente da fórmula de 0,5%.
6. Aba de desmobilização do canteiro não alimenta a planilha final.
7. Conteúdo residual de locais/equipamentos diferentes: Xisto, Suzano, Palotina, centrífuga 40 m³/h e anotação de 60 m³/h.
8. Algumas linhas possuem item/preço sem descrição ou quantidade.
9. Preços e contatos aparecem sem data-base formal, embora algumas observações tenham datas de WhatsApp.
10. O preço final não apresenta impostos, condição de pagamento, validade ou contingências.

## Dúvidas para validação do especialista

1. Qual é a obra real representada: Xisto, Suzano ou outra?
2. O regime final é 24 h/3 turnos ou 16 h/2 turnos?
3. Qual concentração de sólidos alimenta a centrífuga?
4. Qual capacidade e quantidade de centrífugas foram efetivamente previstas?
5. Qual valor patrimonial deve basear depreciação e juros da centrífuga?
6. A energia é fornecida pela SANEPAR?
7. O transporte/destinação de R$ 7 milhões foi cotado por qual fornecedor e data?
8. A quantidade de 18.000 t representa massa úmida?
9. A dosagem de 13 kg/t de polímero foi testada neste lodo?
10. A desmobilização do canteiro está incorporada em outros itens?
11. O multiplicador 1,6 e o fator 0,7 têm significado comercial formal?
12. As fórmulas quebradas já existiam no arquivo utilizado para proposta ou surgiram após remoção de abas?

## Limitações registradas

- A análise foi realizada sobre o arquivo Excel fornecido, sem acesso a proposta comercial em PDF, cotações originais, memória de reunião ou explicação do especialista.
- Valores calculados em células com fórmulas quebradas podem conter resultados em cache de uma versão anterior.
- Não foi possível atribuir data-base a todos os preços.
- Nenhuma conclusão foi promovida a regra geral da FOS.
- Nenhum documento de outro orçamento foi alterado.
- Nenhum índice geral ou documento de consolidação foi alterado.
- Nenhuma decisão arquitetural foi tomada.

## Validação final

- [x] Todas as 15 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Fórmulas inventariadas.
- [x] Dependências entre abas registradas.
- [x] Entidades, regras, padrões, exceções, anomalias e dúvidas preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma consolidação realizada.
- [x] Nenhuma decisão arquitetural tomada.
