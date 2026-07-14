# D_013_2025- Sanepar - Stingler.xlsx — Dragagem e Desaguamento em Bags

## Status da análise

- **Arquivo original:** `D_013_2025- Sanepar - Stingler.xlsx`
- **Data da análise:** 14/07/2026
- **Versão do arquivo:** não identificada no nome nem em metadado visível.
- **Quantidade de abas:** 15.
- **Status:** engenharia reversa vertical concluída para o arquivo disponibilizado.
- **Escopo:** documentação exclusiva deste Excel.
- **Restrições respeitadas:** nenhuma funcionalidade, arquitetura, banco de dados, tela, índice geral ou consolidação foi criada ou alterada.

## Regra de classificação utilizada

| Categoria solicitada | Correspondência documental |
| --- | --- |
| EVIDÊNCIA CONFIRMADA | Informação observada diretamente no Excel, inclusive a existência de anomalias. |
| EVIDÊNCIA PARCIAL | Interpretação ou possível regra observada apenas neste orçamento. |
| DÚVIDA | Informação sem comprovação suficiente ou significado operacional não explicitado. |

Todas as descobertas reutilizáveis permanecem com confiança **Nível C**, porque foram observadas em uma única fonte.

## Classificação aparente do orçamento

### EVIDÊNCIA CONFIRMADA

O arquivo representa orçamento de **dragagem e desaguamento de lodo da Lagoa Stingler, em Lapa/PR, para a SANEPAR**, com:

- draga hidráulica de 6";
- recalque total de 400 m;
- linha flutuante de 200 m;
- linha terrestre de 200 m;
- preparo de célula com manta PEAD, bidim e brita;
- fornecimento de bags 8×30 m;
- sistema de preparo e injeção de polímero;
- volume de dragagem de 8.670,4 m³;
- conversão para 700,481616 toneladas de base seca;
- medição comercial por preços unitários;
- dragagem/desaguamento comercializada em tonelada de base seca;
- aplicação de BDI comercial de 70%.

### EVIDÊNCIA PARCIAL

O orçamento aparenta pertencer à família de obras de **dragagem com desaguamento em bags e condicionamento químico por polímero**, incluindo infraestrutura de célula e operação integrada de dragagem/desidratação.

Essa classificação permanece restrita a este arquivo e não constitui consolidação do Método FOS.

## Inventário e fluxo das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identidade e premissas da obra. |
| 2 | `Orçamentos` | Memória de cotações de fornecedores. |
| 3 | `Produção` | Produção mensal e prazo. |
| 4 | `1. Mob. Draga` | Mobilização da draga. |
| 5 | `Barrilete` | Composição e apropriação do barrilete. |
| 6 | `2. Mob. Eq. Polimero` | Mobilização do sistema de polímero. |
| 7 | `3. Prep. Célula` | Dimensionamento e custo da célula. |
| 8 | `4. Forn. Bag` | Dimensionamento e fornecimento de bags. |
| 9 | `5. Canteiro de obras` | Implantação e custo mensal do canteiro. |
| 10 | `6. Operação Sistema` | Operação mensal do polímero/desidratação. |
| 11 | `7. Dragagem` | Centro de custos mensal da dragagem e consolidação operacional. |
| 12 | `8. Desmob. Draga` | Desmobilização da draga. |
| 13 | `9. Desmob. Eq. Polimero` | Desmobilização do sistema de polímero. |
| 14 | `10. Mediçao` | Medição, laboratório e acompanhamento. |
| 15 | `11. Plan. Preços` | Consolidação comercial e cenários de venda. |

```text
Dados da obra
    ↓
Produção e prazo
    ↓
Dimensionamentos físicos da célula e dos bags
    ↓
Mobilizações + canteiro + operação do polímero + dragagem
    ↓
Desmobilizações + medição
    ↓
Planilha detalhada de custo e venda
```

---

# Análise completa por aba


## 1. Aba `Dados Obra`


### Objetivo
Registrar identidade comercial, premissas técnicas, responsabilidades e calendário operacional.

### Papel no fluxo
É a fonte primária para volume, recalque, linha flutuante, jornada, dias mensais e classificações gerais usadas por diversas abas.

### Entradas e resultados — EVIDÊNCIA CONFIRMADA
- Proposta: `Proposta D_013_2025`.
- Data registrada: 06/03/2025.
- Cliente: SANEPAR.
- Objeto: `Dragagem e Desaguamento Lagoa Stingler`.
- Local: Lapa - PR.
- Volume de dragagem: 8.670,4 m³.
- Material: lodo de lagoa.
- Distância de recalque: 400 m; seio adicional: 0 m; total: 400 m.
- Linha flutuante: 200 m; seio adicional: 0 m; total: 200 m.
- Linha de terra: 200 m.
- Profundidade, espessura média e área de dragagem: não preenchidas.
- Bota-fora: bag.
- Sistema de medição: preços unitários de serviços.
- Canteiro e mobilização: responsabilidade FOS.
- Jornada: 9 h/dia.
- Calendário: 22 dias/mês.
- Volume geométrico calculado: 0 m³, porque as dimensões não foram preenchidas.

### Entidades
Proposta; cliente; obra; local; material; volume; linha de recalque; linha flutuante; linha terrestre; bota-fora; sistema de medição; responsabilidade; jornada.

### Regras e interpretações — EVIDÊNCIA PARCIAL
- O volume contratual informado pode coexistir com um volume geométrico calculável.
- A distância total soma distância nominal e “seio da linha”.
- Responsabilidade por canteiro e mobilização é uma premissa explícita.

### Dúvidas
- Em quais situações o volume geométrico deve substituir o volume informado?
- O “seio da linha” representa folga, catenária, margem operacional ou extensão física?
- Como as composições mudam quando canteiro ou mobilização são responsabilidade do cliente?


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `H16` | `=B16+E16` |
| `H17` | `=B17+E17` |
| `G21` | `=B21*D21*B20` |

---


## 2. Aba `Orçamentos`


### Objetivo
Preservar referências pontuais de fornecedores e preços.

### Conteúdo — EVIDÊNCIA CONFIRMADA
- BR Guindastes: guindaste de 75 toneladas, R$ 4.000; contato Tomas; telefone registrado; data 07/03/2025.
- Linha subordinada: mobilização e desmobilização, R$ 1.500.
- ROTATIVO Locações: almoxarifado; contato Leonardo; telefone registrado; data 07/03/2025.
- Linha subordinada: banheiro, sem preço preenchido.

### Papel no fluxo
Não foram identificadas fórmulas nem referências diretas a esta aba nas demais fórmulas do arquivo. A aba funciona como memória de cotação, não como fonte automática de cálculo.

### Entidades
Fornecedor; equipamento/serviço; preço; contato; telefone; data de cotação.

### Anomalias e dúvidas
- Os preços da cotação não alimentam automaticamente as composições.
- Não está explícito se os preços usados nas abas de custo foram copiados desta aba ou obtidos de outras fontes.


---


## 3. Aba `Produção`


### Objetivo
Converter vazão, eficiência, concentração e calendário em produção útil mensal e prazo matemático.

### Entradas — EVIDÊNCIA CONFIRMADA
- Vazão: 120 m³/h.
- Eficiência: 65%.
- Concentração: 15%.
- Jornada: 9 h/dia, recebida de `Dados Obra`.
- Dias: 22 dias/mês, recebidos de `Dados Obra`.
- Volume: 8.670,4 m³, recebido de `Dados Obra`.

### Resultados — EVIDÊNCIA CONFIRMADA
- Horas mensais: 198 h/mês.
- Produção útil: 11,7 m³/h.
- Produção mensal: 2.316,6 m³/mês.
- Prazo matemático: 3,742726409 meses.

### Regras — EVIDÊNCIA PARCIAL
- Produção útil = vazão × eficiência × concentração.
- Produção mensal = produção útil × horas mensais.
- Prazo = volume ÷ produção mensal.
- Abas posteriores arredondam o prazo para cima, resultando em 4 meses.

### Dúvidas
- Vazão, eficiência e concentração são parâmetros específicos desta lagoa, da draga de 6" ou estimativas gerais?
- A concentração de 15% representa sólidos em volume, sólidos em massa ou outro conceito operacional?


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `H3` | `='Dados Obra '!B26` |
| `H4` | `='Dados Obra '!B27` |
| `H6` | `=H3*H4` |
| `D8` | `=D3*(D4/100)*(D5/100)` |
| `D11` | `=H6` |
| `D13` | `=D8*D11` |
| `D18` | `=D13` |
| `D21` | `='Dados Obra '!B14` |
| `D24` | `=D21/D18` |

---


## 4. Aba `1. Mob. Draga`


### Objetivo
Compor o evento de mobilização e montagem da draga de 6".

### Composição — EVIDÊNCIA CONFIRMADA
Equipe diária: 1 operador líder, 2 operadores de draga e 4 ajudantes; 7 refeições e 7 transportes. Jornada de 9 h/dia, leis sociais de 100%. Custo diário: R$ 2.643,56.

Serviços:
- guindaste para carregamento: 1 dia × R$ 1.000;
- carreta prancha e carreta extensível estruturadas, mas sem quantidade;
- 2 carretas carga seca × R$ 9.000;
- guindaste para descarregamento/montagem: 1 dia × R$ 5.500;
- trator D4 estruturado, sem quantidade;
- mão de obra: 4 dias × custo diário.

Resultado: R$ 35.074,24, com BDI interno 0%.

### Observações
- Nota na carreta: `Fabiano - 8500 + 0,2 adv`, enquanto a composição usa R$ 9.000.
- Mobilização é tratada como item global e evento único.


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `='Dados Obra '!B26` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F19` | `=D19*E19` |
| `E21` | `=F10` |
| `F22` | `=SUM(F15:F21)` |
| `F23` | `=F22*(E23/100)` |
| `F24` | `=SUM(F22:F23)` |

---


## 5. Aba `Barrilete`


### Objetivo
Compor um barrilete de distribuição, incorporado à mobilização do equipamento de polímero.

### Composição — EVIDÊNCIA CONFIRMADA
Inclui tubos de ferro de 8", tocos, joelhos, tees 8"×6", ponteiras, caps, válvulas, mangueira, braçadeiras, curvas, válvulas esfera, bomba lameira e um dia de montagem.

Os preços unitários de materiais são calculados por preço-base × 1,4. O total bruto é R$ 27.964,96. A planilha apropria somente 25% desse total como “depreciação”, resultando em R$ 6.991,24. BDI interno: 0%.

### Regras — EVIDÊNCIA PARCIAL
- O fator 1,4 representa acréscimo embutido sobre preços-base, mas sua natureza não é explicitada.
- Apenas 25% do investimento do barrilete é imputado ao orçamento.

### Dúvidas
- O fator 1,4 cobre impostos, frete, perda, margem de compra ou atualização?
- Os 25% representam depreciação por obra, reaproveitamento previsto ou vida útil de quatro obras?


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A5+A6` |
| `F7` | `=A7*C7` |
| `A8` | `=A5+A6` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `E14` | `=400*1.4` |
| `F14` | `=D14*E14` |
| `E15` | `=165*1.4` |
| `E16` | `=165*1.4` |
| `E17` | `=220*1.4` |
| `E18` | `=55*1.4` |
| `E19` | `=35*1.4` |
| `E20` | `=2000*1.4` |
| `E21` | `=1100*1.4` |
| `E22` | `=18*1.4` |
| `E23` | `=14*1.4` |
| `E24` | `=35*1.4` |
| `E25` | `=60*1.4` |
| `E26` | `=1200*1.4` |
| `E27` | `=F9` |
| `F28` | `=SUM(F14:F27)` |
| `F29` | `=F28*0.25` |
| `F30` | `=F29*(E30/100)` |
| `F31` | `=F29+F30` |

---


## 6. Aba `2. Mob. Eq. Polimero`


### Objetivo
Compor mobilização, cobertura e montagem do sistema de preparo e injeção de polímero.

### Composição — EVIDÊNCIA CONFIRMADA
- verba para cobertura: R$ 5.000;
- brita e concreto estruturados, sem quantidade/preço;
- frete: R$ 9.000;
- hidráulica: R$ 1.000;
- elétrica: R$ 1.000;
- meia máquina WAP: 0,5 × R$ 4.500;
- barrilete: R$ 6.991,24;
- mão de obra: 3 dias × R$ 2.035,56.

Resultado: R$ 31.347,92. BDI interno 0%.

### Dependências
Recebe o preço final do `Barrilete` e o custo diário de sua própria equipe.


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A5+A6` |
| `F7` | `=A7*C7` |
| `A8` | `=A5+A6` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `F14` | `=D14*E14` |
| `E21` | `=Barrilete!F31` |
| `E22` | `=F9` |
| `F24` | `=SUM(F14:F22)` |
| `F25` | `=F24*(E25/100)` |
| `F26` | `=F24` |

---


## 7. Aba `3. Prep. Célula`


### Objetivo
Dimensionar e precificar o preparo de célula revestida com manta PEAD, bidim e brita.

### Dimensionamento físico — EVIDÊNCIA CONFIRMADA
Área da célula: 1.656 m².

Coeficientes:
- manta PEAD: 1,196 m² por m² de célula → 1.980,576 m²;
- bidim: 1,48 m² por m² → 2.450,88 m²;
- brita: 0,17 m³ por m² → 281,52 m³;
- retroescavadeira: 0,023 h por m² → 38,088 h;
- mão de obra: 0,023 h por m² → 38,088 h; conversão registrada: 3,8088 dias para equipe indicada.

Na composição de custo, a brita recebe 15% adicional: 323,748 m³.

### Composição — EVIDÊNCIA CONFIRMADA
Inclui preparo com patrola/trator, mobilizações, retroescavadeira, regularização manual, manta PEAD 1,0 mm, instalação da manta, taxa de mobilização da equipe PEAD, bidim RT 14, brita 2, espalhamento e mão de obra.

Resultado: R$ 170.704,968. BDI interno 0%.

### Regras — EVIDÊNCIA PARCIAL
- Coeficientes por área transformam a geometria da célula em materiais e horas.
- A brita recebe margem de 15%; os demais materiais não recebem margem explícita equivalente.
- Dias de mão de obra e retro são arredondados manualmente na composição, não por fórmula uniforme.

### Dúvidas
- Origem técnica dos coeficientes 1,196; 1,48; 0,17 e 0,023.
- Motivo da margem exclusiva de 15% sobre brita.
- Relação entre área da célula e volume de bags.


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `O6` | `=K6*N6` |
| `D7` | `='Dados Obra '!B26` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `N7` | `=N6` |
| `O7` | `=K7*N7` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `N8` | `=N6` |
| `O8` | `=K8*N8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `N9` | `=N6` |
| `O9` | `=K9*N9` |
| `F10` | `=SUM(F5:F9)` |
| `N10` | `=N6` |
| `O10` | `=K10*N10` |
| `O11` | `=O10/10` |
| `F15` | `=D15*E15` |
| `E19` | `=F10` |
| `D20` | `=O6` |
| `D21` | `=O6` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `D23` | `=O7` |
| `D24` | `=O8*1.15` |
| `E26` | `=F10` |
| `F27` | `=SUM(F15:F26)` |
| `F28` | `=F27*(E28/100)` |
| `F29` | `=SUM(F27:F28)` |

---


## 8. Aba `4. Forn. Bag`


### Objetivo
Dimensionar a quantidade de bags e compor fornecimento, frete, descarga e instalação.

### Conversão de volume — EVIDÊNCIA CONFIRMADA
- volume dragado: 8.670,4 m³;
- fração de sólidos in situ: 0,08079;
- tonelada seca calculada: 700,481616 t;
- fração de sólidos após desaguamento: 0,23;
- volume a acomodar: 3.045,572243 m³;
- capacidade adotada: bag 8×60 = 880 m³; bag 8×30 = 440 m³;
- seleção: 7 bags 8×30, capacidade total 3.080 m³.

### Composição — EVIDÊNCIA CONFIRMADA
- 7 bags 8×30 × R$ 35.000 = R$ 245.000;
- frete = R$ 2.500;
- munck = R$ 1.300;
- instalação = 1 dia de equipe, R$ 2.643,56.

Resultado: R$ 251.443,56. BDI interno 0%.

### Regras — EVIDÊNCIA PARCIAL
- Tonelada seca = volume dragado × fração de sólidos in situ.
- Volume após desaguamento = tonelada seca ÷ fração de sólidos desaguados.
- A quantidade de bags é escolhida para capacidade ligeiramente superior ao volume calculado.

### Dúvidas
- As frações 0,08079 e 0,23 são massa/massa, massa/volume ou aproximações operacionais?
- A capacidade de 440 m³ por bag 8×30 considera enchimento seguro, geometria real ou experiência de campo?


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `='Dados Obra '!B26` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `D15` | `=C33` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `F18` | `=D18*E18` |
| `E19` | `=F10` |
| `F19` | `=D19*E19` |
| `F20` | `=SUM(F15:F19)` |
| `F21` | `=F20*(E21/100)` |
| `F22` | `=SUM(F20:F21)` |
| `B26` | `='Dados Obra '!B14` |
| `B28` | `=B26*B27` |
| `B30` | `=B28/B29` |
| `D32` | `=B32*C32` |
| `D33` | `=B33*C33` |
| `D34` | `=SUM(D32:D33)` |

---


## 9. Aba `5. Canteiro de obras`


### Objetivo
Compor custos de implantação e permanência do canteiro como subitem mensal da dragagem.

### Composição — EVIDÊNCIA CONFIRMADA
Inclui almoxarifado, sanitário/vestiário, escritório, fretes, programas legais, ARTs, placa, vigilância, água potável, material de escritório, banheiro químico, exames e integração.

Total bruto armazenado: R$ 38.437,12. Preço final armazenado: R$ 9.609,28, equivalente ao total dividido por 4 meses.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA
As células `D15`, `D24`, `D25` e `F29` estão salvas com `#NAME?`, embora contenham fórmulas relacionadas ao arredondamento do prazo. O resultado final de R$ 9.609,28 indica apropriação mensal em quatro meses.

### Regras — EVIDÊNCIA PARCIAL
- Alguns itens são multiplicados por prazo arredondado + 1 mês.
- O total do canteiro é convertido em custo mensal pelo prazo arredondado.
- Há coexistência de implantação única e custos mensais na mesma composição.


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `='Dados Obra '!B26` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `A9` | `=A5+A6+A7` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `D15` | `=ROUNDUP(Produção!D24,0)+1` |
| `F15` | `=D15*E15` |
| `D16` | `=ROUNDUP(Produção!D24,0)+1` |
| `F16` | `=D16*E16` |
| `D17` | `=ROUNDUP(Produção!D24,0)+1` |
| `F17` | `=D17*E17` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `D24` | `=ROUNDUP(Produção!D24,0)+1` |
| `D25` | `=ROUNDUP(Produção!D24,0)+1` |
| `F27` | `=SUM(F15:F26)` |
| `F29` | `=ROUNDUP(Produção!D24,0)` |
| `F31` | `=F27/F29` |

---


## 10. Aba `6. Operação Sistema`


### Objetivo
Compor o custo mensal de operação do sistema de desidratação e injeção de polímero.

### Composição — EVIDÊNCIA CONFIRMADA
- equipamento de preparo/injeção: R$ 40.000;
- polímero: 3.082,1191104 kg × R$ 20 = R$ 61.642,38;
- frete: 3 × R$ 1.000;
- água para operação por reuso: R$ 10.000;
- gerador/energia/diesel: 4 meses × R$ 14.009 = R$ 56.036;
- hidráulica: R$ 2.000;
- WAP: R$ 2.000;
- mão de obra: 120 dias × R$ 1.017,78 = R$ 122.133,60.

Total: R$ 296.811,982208. Prazo: 4 meses. Custo mensal: R$ 74.202,995552.

### Regras — EVIDÊNCIA PARCIAL
- Polímero é calculado sobre tonelada seca.
- Comentário operacional menciona 4 kg por tonelada seca, mas a quantidade calculada corresponde a aproximadamente 4,4 kg/t.
- A mão de obra usa 30 dias por mês durante 4 meses, não 22 dias úteis.
- O gerador é tratado como custo mensal pelo prazo arredondado.

### Anomalia
`D18` está salva com `#NAME?`, associada ao prazo arredondado.


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A5+A6` |
| `F7` | `=A7*C7` |
| `A8` | `=A5+A6` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `F14` | `=D14*E14` |
| `D15` | `='4. Forn. Bag'!B28*4.4` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `D18` | `=ROUNDUP(Produção!D24,0)` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `D21` | `=D18*30` |
| `E21` | `=F9` |
| `F21` | `=D21*E21` |
| `F22` | `=SUM(F14:F21)` |
| `F23` | `=D18` |
| `F24` | `=F22/F23` |

---


## 11. Aba `7. Dragagem`


### Objetivo
Concentrar o custo mensal de dragagem, canteiro e apoio, e depois combinar esse custo com a operação do sistema de polímero.

### Estrutura observada — EVIDÊNCIA CONFIRMADA
A aba contém sete blocos:
1. Operação.
2. Pessoal.
3. Manutenção.
4. Equipamentos de apoio.
5. Administrativas.
6. BDI interno.
7. Financeiras.

### Premissas e resíduos de modelo
O cabeçalho registra `ETE HOLAMBRA`, cliente `DAAE`, data 24/05/2018 e draga hidráulica de 6", enquanto a obra vigente é SANEPAR — Lagoa Stingler, 2025. Isso é uma anomalia documental confirmada e indica reaproveitamento de modelo.

Valor do equipamento “no estado”: R$ 500.000.

### Operação — EVIDÊNCIA CONFIRMADA
- combustível: horas mensais × eficiência × 10 l/h × R$ 7/l = R$ 12.474;
- filtros/lubrificantes: R$ 600;
- fretes/carretos: R$ 1.000;
- segurança/uniformes: R$ 400;
- subtotal: R$ 14.474.

### Pessoal — EVIDÊNCIA CONFIRMADA
Equipe ativa: 1 operador líder, 1 operador de draga e 1 ajudante. Base mensal de 219,9999 h. Salários: R$ 15.061,193154. Encargos sociais: 100%, R$ 15.061,193154. Alimentação: R$ 4.780. Alojamento: R$ 2.750. Viagens nas folgas: R$ 500. Subtotal de pessoal: R$ 38.152,386308.

### Manutenção — EVIDÊNCIA CONFIRMADA
- peças/acessórios: 0,6% ao mês do valor do equipamento = R$ 3.000;
- docagem anual apropriada: 1% ao mês = R$ 5.000;
- limpeza/pintura: R$ 250;
- terceiros: R$ 250;
- subtotal: R$ 8.500.

### Apoio — EVIDÊNCIA CONFIRMADA
- linha de recalque apropriada: R$ 7.028/mês;
- automóvel: R$ 4.500;
- ferramentas: R$ 150;
- canteiro: R$ 9.609,28;
- subtotal: R$ 21.287,28.

A linha de recalque é decomposta em tubulação, flutuantes e acoplamentos, com depreciação em 12 meses e juros de 1%.

### Administrativas, BDI e financeiras
- administrativas: R$ 3.300;
- despesas diretas: R$ 85.713,666308;
- oficina 5% + administração 5%: R$ 8.571,3666308;
- depreciação da draga em 60 meses: R$ 8.333,333333;
- juros de capital 1%: R$ 5.000;
- atrasos 0,5% das despesas diretas: R$ 428,568332;
- financeiras: R$ 13.761,901665;
- custo mensal da dragagem: R$ 108.046,934604.

### Consolidação com polímero — EVIDÊNCIA CONFIRMADA
- custo mensal dragagem: R$ 108.046,934604;
- custo mensal operação polímero: R$ 74.202,995552;
- custo mensal total: R$ 182.249,930156;
- prazo arredondado: 4 meses;
- custo total: R$ 728.999,720623.

Há ainda bloco de preço por hora com BDI 1,6, eficiência operacional de 60% e fator adicional 0,62.

### Anomalias observadas
- Cabeçalho de obra antiga.
- Diversas células ligadas a produção e prazo estão salvas como `#NAME?`.
- O bloco de “Preço de venda (R$/m³)” permanece em zero.
- O bloco horário utiliza fatores 0,6 e 0,62 sem explicação.
- A aba combina custo mensal, custo total, preço horário e referências históricas em um único local.

### Dúvidas
- O fator 0,62 representa disponibilidade, rendimento adicional ou margem?
- Por que o combustível usa eficiência de 90%, enquanto produção usa 65%?
- O valor de filtros indicado como “10% combustível” não corresponde a 10% de R$ 12.474.
- A base de 219,9999 h/mês usa 30 dias × 7,33333 h, diferente das 198 h operacionais.


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `C9` | `=Produção!H6` |
| `F10` | `=C9*D9*E9*F9` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `K20` | `='Dados Obra '!B27` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `A23` | `=L24` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `L24` | `=(L20*1.7)+(L21*2)+L23` |
| `A25` | `=L24` |
| `A26` | `=L24` |
| `A27` | `=L24` |
| `E27` | `=D27*B27*A27` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `E69` | `=D69*B69` |
| `E71` | `=SUM(E67:E69)` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E139` | `=(0.6/100)*F7` |
| `E140` | `=(1/100)*F7` |
| `E144` | `=E139+E140+E141+E142` |
| `H146` | `=E144` |
| `E150` | `=K167` |
| `I151` | `='Dados Obra '!H16` |
| `K151` | `=I151*J151` |
| `J152` | `=K151/I152` |
| `J153` | `=K151*(1/100)` |
| `J154` | `=SUM(J152:J153)` |
| `I156` | `='Dados Obra '!H17/12*3` |
| `K156` | `=I156*J156` |
| `J157` | `=K156/I157` |
| `E158` | `='5. Canteiro de obras'!F31` |
| `J158` | `=K156*(1/100)` |
| `J159` | `=SUM(J157:J158)` |
| `D161` | `=E150+E151+E152+E155+E156+E157+E158+E159+E153+E154` |
| `I161` | `=(I151/12)+2` |
| `K161` | `=I161*J161` |
| `J162` | `=K161/I162` |
| `J163` | `=K161*(1/100)` |
| `J164` | `=SUM(J162:J163)` |
| `H167` | `=J154` |
| `I167` | `=J159` |
| `J167` | `=J164` |
| `K167` | `=SUM(H167:J167)` |
| `E178` | `=E173+E174+E175+E176+E177` |
| `G181` | `=E178+D161+H146+G87+E15` |
| `E185` | `=G181*(5/100)` |
| `E186` | `=G181*(5/100)` |
| `E189` | `=E185+E186` |
| `E192` | `=F7/60` |
| `E193` | `=F7*0.01` |
| `E194` | `=G181*0.005` |
| `E196` | `=E192+E193+E194` |
| `D215` | `=G181` |
| `D218` | `=E189` |
| `D220` | `=E196` |
| `D222` | `=D215+D218+D220` |
| `D225` | `=Produção!D13` |
| `D231` | `=D227+D229` |
| `D234` | `=J253*0.6*0.62` |
| `H235` | `=Produção!H4` |
| `I235` | `=Produção!H3` |
| `J235` | `=H235*I235` |
| `D244` | `=D222` |
| `D245` | `='6. Operação Sistema'!F24` |
| `D246` | `=SUM(D244:D245)` |
| `D247` | `=ROUNDUP(Produção!D24,0)` |
| `J247` | `=D246` |
| `D248` | `=D246*D247` |
| `J249` | `=J247*J248` |
| `L249` | `=J249/J250` |
| `J250` | `=Produção!H6` |
| `L251` | `=L249*L250` |
| `J252` | `=J250*J251` |
| `J253` | `=J249/J252` |

---


## 12. Aba `8. Desmob. Draga`


### Objetivo
Compor desmobilização da draga de 6".

### Conteúdo — EVIDÊNCIA CONFIRMADA
Usa equipe semelhante à mobilização, porém leis sociais de 132%, refeição de R$ 35 e custo diário de R$ 2.975,5296. Inclui 2 carretas a R$ 9.000, guindaste R$ 5.500 e 3 dias de mão de obra.

Resultado: R$ 32.426,5888. BDI interno 0%.

### Anomalia
Na planilha comercial, o custo usado para desmobilização da draga é R$ 35.074,24, igual à mobilização, não o preço final desta aba.


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `='Dados Obra '!B26` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F19` | `=D19*E19` |
| `E21` | `=F10` |
| `F22` | `=SUM(F15:F21)` |
| `F23` | `=F22*(E23/100)` |
| `F24` | `=SUM(F22:F23)` |

---


## 13. Aba `9. Desmob. Eq. Polimero`


### Objetivo
Compor desmontagem e transporte do sistema de polímero.

### Conteúdo — EVIDÊNCIA CONFIRMADA
Equipe com leis sociais de 132%, custo diário R$ 2.253,2496. Apenas frete de R$ 9.000 e três dias de desmontagem estão ativos; demais itens têm quantidade vazia.

Resultado da aba: R$ 15.759,7488. BDI interno 0%.

### Anomalia
A planilha comercial usa R$ 21.943,544, valor diferente do resultado desta aba. A diferença não foi explicada por fórmula direta.


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A5+A6` |
| `F7` | `=A7*C7` |
| `A8` | `=A5+A6` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `F16` | `=D16*E16` |
| `E20` | `=F9` |
| `F21` | `=SUM(F14:F20)` |
| `F22` | `=F21*(E22/100)` |
| `F23` | `=F21` |

---


## 14. Aba `10. Mediçao`


### Objetivo
Compor custos de medição, laboratório e acompanhamento.

### Conteúdo — EVIDÊNCIA CONFIRMADA
- batimetria estruturada, sem quantidade/preço;
- laboratório: 50 × R$ 60 = R$ 3.000;
- acompanhamento FOS: 4 dias × R$ 2.573,56 = R$ 10.294,24;
- total: R$ 13.294,24;
- BDI interno 0%.

Há um segundo bloco final de BDI/preço final zerado, sem itens associados.

### Dúvidas
- O laboratório mede sólidos, qualidade de água, teor de umidade ou outro parâmetro?
- A batimetria será responsabilidade do cliente ou custo pendente?


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `='Dados Obra '!B26` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `E17` | `=F10` |
| `F18` | `=SUM(F15:F17)` |
| `F19` | `=F18*(E19/100)` |
| `F20` | `=SUM(F18:F19)` |

---


## 15. Aba `11. Plan. Preços`


### Objetivo
Consolidar custos por item, definir unidades comerciais e aplicar BDI de venda.

### Itens comerciais — EVIDÊNCIA CONFIRMADA
1. Mobilização da dragagem: 1 un.
2. Mobilização do polímero e barrilete: 1 un.
3. Preparo de célula: 1.656 m².
4. Fornecimento de bags 8×30: 7 un.
5. Dragagem e desaguamento: 700,481616 t base seca.
7. Medição: 1 un.
8. Desmobilização da dragagem: 1 un.
9. Desmobilização do polímero: 1 un.

### Resultados — EVIDÊNCIA CONFIRMADA
- custo total consolidado: R$ 1.287.882,432623;
- BDI comercial por item: 70%;
- preço de venda: R$ 2.189.400,135459;
- preço indicado retirando mobilização: R$ 228,31/m³;
- cenário “mínimo do mínimo”: R$ 1.803.035,41, com BDI 40% e R$ 194,74/m³;
- retorno mostrado para BDI 70%: 41,17647% sobre venda;
- retorno mostrado para BDI 40%: 28,57143% sobre venda.

### Regras — EVIDÊNCIA PARCIAL
- Preço unitário = custo unitário × (1 + BDI).
- Percentual de retorno é calculado como margem sobre preço de venda, não markup sobre custo.
- A unidade principal da dragagem é tonelada de base seca, embora também seja mostrado preço equivalente por m³.

### Anomalias
- Numeração salta do item 5 para o 7.
- Desmobilização da draga usa custo da mobilização.
- Desmobilização do polímero usa valor que não coincide com sua aba.
- A quantidade de toneladas secas é a base de cobrança principal da dragagem/desaguamento.


### Fórmulas preservadas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula preservada |
| --- | --- |
| `C4` | `='1. Mob. Draga'!F24` |
| `G4` | `=C4/E4` |
| `I4` | `=G4*(1+H4/100)` |
| `J4` | `=I4*E4` |
| `C5` | `='2. Mob. Eq. Polimero'!F26` |
| `G5` | `=C5/E5` |
| `I5` | `=G5*(1+H5/100)` |
| `J5` | `=I5*E5` |
| `C6` | `='3. Prep. Célula'!F29` |
| `G6` | `=C6/E6` |
| `I6` | `=G6*(1+H6/100)` |
| `J6` | `=I6*E6` |
| `C7` | `='4. Forn. Bag'!F22` |
| `G7` | `=C7/E7` |
| `I7` | `=G7*(1+H7/100)` |
| `J7` | `=I7*E7` |
| `C8` | `='7. Dragagem'!D248` |
| `E8` | `='4. Forn. Bag'!B28` |
| `G8` | `=C8/E8` |
| `I8` | `=G8*(1+H8/100)` |
| `J8` | `=I8*E8` |
| `C9` | `='10. Mediçao'!F20` |
| `G9` | `=C9/E9` |
| `I9` | `=G9*(1+H9/100)` |
| `J9` | `=I9*E9` |
| `L9` | `=SUM(J4:J9)` |
| `C10` | `='1. Mob. Draga'!F24` |
| `G10` | `=C10/E10` |
| `I10` | `=G10*(1+H10/100)` |
| `J10` | `=I10*E10` |
| `C11` | `='9. Desmob. Eq. Polimero'!F23+'2. Mob. Eq. Polimero'!F22` |
| `G11` | `=C11/E11` |
| `I11` | `=G11*(1+H11/100)` |
| `J11` | `=I11*E11` |
| `L11` | `=(J8+J9+J11)/(Dados Obra!B14)` |
| `C12` | `=SUM(C4:C11)` |
| `J12` | `=SUM(J4:J11)` |
| `I16` | `=J12` |
| `J16` | `=H4/100` |
| `K16` | `=L11` |
| `M16` | `=(I16-C12)/I16` |
| `I17` | `=C12*1.4` |
| `J17` | `=0.4` |
| `K17` | `=(I17-J4-J5-J6-J7-J10)/(Dados Obra!B14)` |
| `M17` | `=(I17-C12)/I17` |

---

# Extração transversal exclusiva deste arquivo

## Entidades encontradas — EVIDÊNCIA CONFIRMADA

Proposta; cliente; contato; obra; local; material; volume dragado; tonelada seca; produção; prazo; draga; barrilete; sistema de polímero; célula de desaguamento; manta PEAD; bidim; brita; bag; equipe; função; salário-hora; leis sociais; refeição; transporte; equipamento de apoio; fornecedor; cotação; mobilização; implantação; operação; manutenção; administrativo; BDI; custo financeiro; desmobilização; medição; laboratório; item comercial; unidade de venda.

## Regras de negócio observadas — EVIDÊNCIA PARCIAL

1. O prazo matemático é arredondado para cima para apropriações mensais.
2. O custo de mão de obra diária usa quantidade × valor-hora × horas × (1 + leis sociais).
3. Mobilizações e desmobilizações são eventos globais.
4. O canteiro combina itens únicos e mensais e é convertido em custo mensal.
5. A produção útil aplica vazão, eficiência e concentração.
6. O dimensionamento dos bags converte volume dragado em tonelada seca e depois em volume desaguado.
7. O polímero é dosado sobre tonelada seca.
8. O preparo da célula usa coeficientes por metro quadrado.
9. Equipamentos reutilizáveis podem ser apropriados por depreciação parcial.
10. O custo mensal da dragagem recebe manutenção, apoio, administrativas, BDI interno e financeiras.
11. O preço comercial aplica BDI por item.
12. A margem mostrada é retorno sobre venda, diferente do BDI/markup sobre custo.
13. O orçamento combina unidades comerciais globais, unidade, m², tonelada seca e preço equivalente por m³.

## Coeficientes e valores embutidos que exigem validação futura

| Valor | Uso observado | Classificação |
| --- | --- | --- |
| 65% | eficiência de produção | EVIDÊNCIA PARCIAL |
| 15% | concentração da produção | EVIDÊNCIA PARCIAL |
| 0,08079 | fração de sólidos in situ | EVIDÊNCIA PARCIAL |
| 0,23 | fração de sólidos após desaguamento | EVIDÊNCIA PARCIAL |
| 1,196 | manta PEAD por área da célula | EVIDÊNCIA PARCIAL |
| 1,48 | bidim por área da célula | EVIDÊNCIA PARCIAL |
| 0,17 | brita por área da célula | EVIDÊNCIA PARCIAL |
| 0,023 | horas de retro e mão de obra por área | EVIDÊNCIA PARCIAL |
| 15% | margem adicional de brita | EVIDÊNCIA PARCIAL |
| 1,4 | multiplicador dos preços-base do barrilete | DÚVIDA |
| 25% | depreciação/apropriação do barrilete | DÚVIDA |
| 4 kg/t | dosagem comentada de polímero | EVIDÊNCIA PARCIAL |
| ~4,4 kg/t | dosagem efetiva resultante | EVIDÊNCIA CONFIRMADA |
| 0,6%/mês | peças e acessórios sobre draga | EVIDÊNCIA PARCIAL |
| 1%/mês | docagem sobre draga | EVIDÊNCIA PARCIAL |
| 5% + 5% | oficina e administração | EVIDÊNCIA PARCIAL |
| 60 meses | depreciação da draga | EVIDÊNCIA PARCIAL |
| 1% | juros de capital | EVIDÊNCIA PARCIAL |
| 0,5% | atrasos sobre despesas diretas | EVIDÊNCIA PARCIAL |
| 70% | BDI comercial principal | EVIDÊNCIA CONFIRMADA |
| 40% | cenário mínimo | EVIDÊNCIA CONFIRMADA |
| 0,6 e 0,62 | fatores do preço horário | DÚVIDA |

## Dependências principais entre abas — EVIDÊNCIA CONFIRMADA

- `Dados Obra` → `Produção`, mobilizações, célula, bags, dragagem.
- `Produção` → canteiro, operação de polímero, dragagem.
- `Barrilete` → `2. Mob. Eq. Polimero`.
- `4. Forn. Bag` → quantidade de toneladas secas usada em `11. Plan. Preços`.
- `5. Canteiro de obras` → `7. Dragagem`.
- `6. Operação Sistema` → `7. Dragagem`.
- Composições individuais → `11. Plan. Preços`.
- Algumas ligações comerciais não usam o resultado das abas correspondentes, configurando divergências rastreáveis.

## Anomalias observadas — EVIDÊNCIA CONFIRMADA

1. Células salvas com `#NAME?` em canteiro, operação e dragagem.
2. Cabeçalho da aba `7. Dragagem` refere-se a ETE Holambra/DAAE em 2018.
3. Desmobilização da draga na planilha comercial usa o valor da mobilização.
4. Desmobilização do polímero na planilha comercial não coincide com sua composição.
5. Polímero comentado como 4 kg/t, mas quantidade equivale a aproximadamente 4,4 kg/t.
6. Filtros descritos como 10% do combustível, mas valor não corresponde a 10%.
7. Bases de horas mensais divergentes: 198 h operacionais e 219,9999 h salariais.
8. Leis sociais variam de 100% nas etapas iniciais para 132% nas desmobilizações.
9. A aba de cotações não alimenta automaticamente as composições.
10. Numeração comercial salta o item 6.
11. Há blocos duplicados/zerados na medição.
12. O preço de venda por m³ na aba de dragagem permanece zerado, enquanto a planilha comercial calcula equivalentes por m³.

## Dúvidas para validação do especialista

1. Qual é a definição exata de concentração usada na produção?
2. Como foi obtida a fração de sólidos in situ `0,08079`?
3. Como foi definida a fração desaguada `0,23`?
4. Por que a dosagem efetiva de polímero difere dos 4 kg/t comentados?
5. Qual é o significado do multiplicador `1,4` no barrilete?
6. Qual é a justificativa da apropriação de 25% do barrilete?
7. Qual é a origem dos coeficientes de preparo de célula?
8. Por que a brita recebe 15% adicional?
9. Qual é a regra oficial para dias úteis versus dias corridos na mão de obra?
10. Qual valor correto deve ser usado nas duas desmobilizações?
11. Qual é a unidade comercial prioritária: tonelada seca, m³ dragado ou ambas?
12. O cenário “mínimo do mínimo” é limite comercial, referência de negociação ou simulação?
13. Os fatores 0,6 e 0,62 do preço horário representam quais perdas ou margens?
14. Os `#NAME?` existiam operacionalmente no Excel original ou são resíduos de compatibilidade/recalculo?
15. A informação de ETE Holambra deve ser removida em revisão futura do arquivo ou preservada como histórico do modelo?

# Validação final

- [x] Todas as 15 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Fórmulas e dependências relevantes preservadas.
- [x] Evidências classificadas.
- [x] Limitações e dúvidas registradas.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma consolidação de múltiplos orçamentos realizada.
- [x] Nenhum índice geral modificado.

## Limitações registradas

- O arquivo não contém explicação textual para todos os coeficientes.
- Valores salvos como `#NAME?` foram preservados como anomalias; não foi possível afirmar, somente pelo arquivo, se decorrem de fórmula inválida, compatibilidade de aplicativo ou ausência de recálculo.
- Não houve validação oral do especialista nesta sessão.
- Nenhuma informação deste registro foi promovida a regra geral da FOS.
