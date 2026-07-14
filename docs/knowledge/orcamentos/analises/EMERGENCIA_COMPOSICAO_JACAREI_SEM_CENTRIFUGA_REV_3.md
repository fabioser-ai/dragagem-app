# Registro de descoberta — `EMERGENCIA - Composição - Jacarei - Sem Centrifuga  - Rev.3.xlsx`

## 1. Identificação da análise

- **Nome integral da fonte:** `EMERGENCIA - Composição - Jacarei - Sem Centrifuga  - Rev.3.xlsx`
- **Data da análise:** 2026-07-14
- **Versão aparente:** Rev.3
- **Quantidade de abas:** 12
- **Quantidade de células não vazias identificadas:** 2.046
- **Quantidade de fórmulas identificadas:** 524
- **Status:** análise integral concluída, com dúvidas e anomalias preservadas
- **Escopo:** somente o arquivo acima; nenhuma consolidação com outros orçamentos foi realizada

## 2. Classificação aparente

### EVIDÊNCIA CONFIRMADA

O arquivo contém uma composição de custos e preços para dragagem e desidratação de lodo de ETE, operação com draga elétrica, mobilização e desmobilização, tanque de equalização, mão de obra, fabricação/venda de draga e consolidação comercial.

As células internas registram cliente **SUZANO**, local **Suzano - SP**, objeto **Dragagem e desidratação de lodo**, material **Lodo de ETE**, medição por **preços unitários de serviços**, centrífuga de propriedade da Suzano e prazo de seis meses.

### EVIDÊNCIA PARCIAL

A estrutura comercial separa o primeiro mês, com fornecimento da draga e mão de obra, dos cinco meses seguintes, tratados como operação somente com mão de obra. Essa separação é observada apenas neste arquivo e não constitui regra geral da FOS.

O título `EMERGENCIA` sugere atendimento emergencial, mas não há célula interna detalhando a natureza da emergência.

### DÚVIDA

O nome do arquivo contém `Jacarei` e `Sem Centrifuga`, enquanto o conteúdo interno informa `SUZANO`, `Suzano - SP` e operação com centrífuga de propriedade da Suzano. Não foi possível determinar se o arquivo foi renomeado, se “Sem Centrífuga” significa sem fornecimento do equipamento, ou se existem resíduos de uma versão anterior.

## 3. Visão geral do fluxo

### EVIDÊNCIA CONFIRMADA

1. `Dados Obra` registra premissas físicas, comerciais e de escopo.
2. `Fornecedores` preserva cotações de guindaste e inicia cadastro de container.
3. `Produção (NOVO CALCULO)` simula capacidade de desaguamento por centrífuga e horas mensais.
4. `1. Canteiro` calcula custo do canteiro e uma matriz-base de salários/turnos.
5. `2.1 Mob Draga` calcula mobilização da draga e recursos auxiliares.
6. `4.1 Draga Dec` calcula o primeiro mês de dragagem, incluindo custos financeiros do equipamento.
7. `Tq Equal.` calcula implantação/locação do tanque de equalização e adaptações.
8. `Venda Draga` compõe fabricação e referência de mercado da draga.
9. `Draga MDO` calcula os cinco meses restantes, excluindo depreciação, juros e parte da manutenção.
10. `Desmob Draga` calcula a desmobilização.
11. `Plan. Final` consolida custos e aplica percentuais de BDI por grupo.
12. `Final` apresenta preços comerciais Rev.3, comparação Rev.2 e cenário sem venda da draga.

## 4. Dependências entre abas

### EVIDÊNCIA CONFIRMADA

- `Dados Obra` alimenta prazo, dias de trabalho, distâncias e volumes.
- `Produção (NOVO CALCULO)` alimenta as horas mensais de `4.1 Draga Dec` e `Draga MDO`.
- `1. Canteiro` alimenta salários, refeições, transporte e custo mensal de canteiro.
- `2.1 Mob Draga` reutiliza dados de `1. Canteiro` e alimenta `Plan. Final`.
- `4.1 Draga Dec`, `Draga MDO`, `Tq Equal.`, `Venda Draga` e `Desmob Draga` alimentam `Plan. Final`.
- `Plan. Final` alimenta a coluna de referência de custos com BDI em `Final`.

### Anomalia observada

`Final!D3` e `Final!D8` contêm referências externas no formato `'[1]Plan. Final'!...`, embora a aba `Plan. Final` exista no próprio arquivo. Os valores em cache são 1, mas a fórmula preserva um vínculo externo/residual.

## 5. Análise por aba

### 5.1 `Dados Obra`

**Objetivo:** centralizar identificação, produção, dados físicos, prazo e escopo.

**Entradas:** proposta `D_026_2025`; cliente SUZANO; contato Thais; local Suzano-SP; volume informado 37.910 m³; lodo de ETE; recalque 150 m; linha flutuante 150 m; linha de terra 0 m; 9 h/dia; 26 dias/mês; prazo 6 meses; sólidos in situ 2%; sólidos desaguados 22%; produção mínima 408 t desaguadas/mês.

**Fórmulas:**

- volume mensal = `(produção desejada × %SS desaguado) / %SS in situ` = 4.488 m³/mês;
- volume total = volume mensal × prazo = 26.928 m³;
- base seca = volume total × 2% = 538,56 t;
- lodo desaguado = base seca ÷ 22% = 2.448 t;
- recalque consolidado = linha flutuante + linha terrestre;
- volume geométrico opcional = largura × comprimento × espessura.

**Observações e dúvidas:** o volume informado de 37.910 m³ diverge do calculado de 26.928 m³; profundidade, espessura e área estão vazias; o quadro lateral registra 150 m de linha flutuante, 200 m de linha terrestre e 350 m total; existe cálculo 24 × 26 = 624 sem rótulo suficiente.

### 5.2 `Fornecedores`

**Objetivo:** registrar cotações, principalmente guindaste de 100 t.

- Engeguind: diária R$ 6.500; rigger R$ 1.500; mobilização R$ 6.000; desmobilização R$ 6.000; integração antecipada como cortesia.
- São José: diária, mobilização e desmobilização de R$ 6.500 cada.
- Truckap possui telefone, sem preço.
- o bloco `CONTAINER` está sem fornecedores.

As cotações não estão ligadas por fórmula às composições.

### 5.3 `Produção (NOVO CALCULO)`

**Objetivo:** simular produção da centrífuga por vazão, concentração, teor final e tempo útil.

**Premissas:** centrífuga de 40 m³/h, valor operacional 25 m³/h; cenário de três centrífugas 120 m³/h; concentração de 3,5%; bombeamento de 20%, resultando 0,7%; sólidos finais 22%; 26 dias/mês; tempo útil 70% de 24 h = 16,8 h/dia; eficiência adicional de 75% = 12,6 h/dia; bloco alternativo de 16 h × 85% = 13,6 h/dia.

**Fórmulas:** base seca/hora = vazão × concentração; toneladas úmidas/hora = base seca/hora ÷ 22%; toneladas/dia = toneladas/hora × horas úteis; toneladas/mês = toneladas/dia × 26.

**Resultados:** 347,45 t/mês a 0,7%; 421,91 t/mês a 0,85%; 496,36 t/mês a 1,0%.

**Anomalias:** `S10` contém `#REF!`; existem dois métodos de tempo útil; 408 t/mês em `Dados Obra` não é resultado direto visível da tabela.

### 5.4 `1. Canteiro`

**Objetivo:** calcular custo mensal do canteiro e manter matriz de salários/turnos.

Equipe ativa: 1 operador de draga e 2 ajudantes; encargos de 110%; adicional de 25% para determinadas funções; três refeições e transportes. Custo diário: **R$ 1.106,529**.

Itens ativos: container almoxarifado R$ 7.200; eletricista R$ 27.000; material de escritório R$ 1.800; integração R$ 5.532,645. Total: **R$ 41.532,645**. Custo mensal: **R$ 6.922,1075**.

Vários itens permanecem com quantidade zero. Existe memória de mobiliário de R$ 10.000 não incluída automaticamente.

### 5.5 `2.1 Mob Draga`

**Objetivo:** calcular mobilização da draga, equipe, transporte e documentos.

Recursos ativos: líder, 2 operadores, 2 ajudantes, treinamentos R$ 3.000, duas carretas R$ 12.000, frete de containers R$ 1.200, mobiliário de alojamento R$ 10.000, segurança R$ 5.000, PGR/PCMSO/LTCAT R$ 2.500, ARTs R$ 500, tenda R$ 5.000, bebedouro R$ 1.000, exames R$ 1.750, carreta do tanque R$ 6.000 e mão de obra R$ 11.601,0575.

Total: **R$ 59.551,0575**.

A quantidade de carretas vem de bloco auxiliar. Há cotação datada de 21/08/2024 e observação de tenda já pertencente à FOS. Itens de guindaste ficam zerados apesar das cotações.

### 5.6 `4.1 Draga Dec`

**Objetivo:** calcular o primeiro mês de operação com draga e mão de obra, incluindo custos financeiros.

Estrutura: operação; pessoal; manutenção; equipamentos de apoio; administrativas; BDI interno; financeiras; resumo/preço por hora.

**Operação:** 436,8 h/mês; eficiência 90%; consumo 30/h; combustível R$ 11.793,60; filtros/lubrificantes R$ 8.255,52; fretes R$ 1.000; segurança R$ 1.000; total R$ 22.049,12.

**Pessoal:** 1 operador e 2 ajudantes; encargos 110%; pessoal, alimentação, alojamento e viagens totalizam R$ 34.752,6632.

**Manutenção:** peças 0,6% ao mês do equipamento; docagem 1% ao mês; limpeza R$ 500; terceiros R$ 500; total R$ 9.800.

**Apoio:** tubulação 150 m × R$ 120; flutuantes 37,5 × R$ 200; acoplamentos 14,5 × R$ 100; automóvel R$ 5.000; plano de saúde R$ 600; ferramentas R$ 150; canteiro R$ 6.922,1075; total R$ 14.064,5242.

**Administrativas/financeiras:** inspeção R$ 1.500; comunicação R$ 250; oficina 5%; administração 5%; depreciação em 60 meses; juros 1% do equipamento.

**Resultados:** despesas diretas R$ 82.416,3074; BDI interno R$ 8.241,6307; financeiras R$ 14.666,6667; custo mensal **R$ 105.324,6048**; período 1 mês; preço auxiliar com fator 1,6 R$ 168.519,3676; preço/hora R$ 270,0631.

**Anomalias:** produção prevista e horas à disposição estão em `#REF!`; custo por m³ não é calculado; textos mencionam combustível FOS, eletricidade Suzano e bags sem alinhamento completo.

### 5.7 `Tq Equal.`

**Objetivo:** compor tanque de equalização, painel, mangotes, adaptações e mão de obra.

Itens: tanque 6 × R$ 2.500 = R$ 15.000; painel 6 × R$ 2.500 = R$ 15.000; mangote 40 m × R$ 200 = R$ 8.000; abraçadeiras R$ 500; adaptação de peneira/sensor R$ 10.000; mão de obra R$ 1.562,142.

Total: **R$ 50.062,142**. Custo mensal: **R$ 8.343,6903**.

Tanque e painel usam base de R$ 60.000 apropriada em 24 meses. A aba reutiliza estrutura visual do canteiro.

### 5.8 `Venda Draga`

**Objetivo:** compor custo de fabricação e referência de mercado.

Fabricação: flutuante R$ 200.000; inversor R$ 50.000; painel R$ 15.000; bomba R$ 42.700; guincho R$ 30.000; sarrilhos/outros R$ 12.300; total **R$ 350.000**. Referência ARVEN 6": **R$ 750.000**.

Total da aba: **R$ 1.100.000**, somando fabricação e referência ARVEN.

**Anomalias:** não está explicado se são duas unidades ou alternativas; prazo vazio; preço unitário, BDI e preço final apresentam `#DIV/0!`; `Plan. Final` usa R$ 1,1 milhão diretamente.

### 5.9 `Draga MDO`

**Objetivo:** calcular os cinco meses restantes apresentados como “só mão de obra”.

Diferenças frente ao primeiro mês: docagem zerada; depreciação zerada; juros zerados; manutenção cai a R$ 4.300; despesas diretas R$ 76.916,3074; BDI interno R$ 7.691,6307; custo mensal **R$ 84.607,9381**; prazo 5 meses; custo total **R$ 423.039,6905**.

Repete os `#REF!` de produção e horas à disposição. Apesar do título “só mão de obra”, a composição mantém combustível, manutenção parcial, apoio, canteiro e automóvel.

### 5.10 `Desmob Draga`

**Objetivo:** calcular desmontagem e retorno dos equipamentos.

Itens ativos: duas carretas R$ 12.000; frete de containers R$ 1.200; exames R$ 1.750; carreta do tanque R$ 6.000; mão de obra R$ 11.601,0575. Total: **R$ 32.551,0575**.

O bloco auxiliar registra nove carretas, mas a composição usa somente duas mais uma do tanque. O título ainda diz mobilização. Guindaste/rigger ficam zerados.

### 5.11 `Plan. Final`

**Objetivo:** consolidar custo, quantidade, BDI e preço de venda.

| Componente | Custo | Quantidade | BDI | Preço total |
|---|---:|---:|---:|---:|
| Mobilização | R$ 59.551,06 | 1 vb | 70% | R$ 101.236,80 |
| Draga + MDO | R$ 105.324,60 | 1 mês | 70% | R$ 179.051,83 |
| Só MDO | R$ 423.039,69 | 5 meses | 70% | R$ 719.167,47 |
| Tanque | R$ 50.062,14 | 6 meses | 70% | R$ 85.105,64 |
| Venda da draga | R$ 1.100.000,00 | 1 | 15% | R$ 1.265.000,00 |
| Desmobilização | R$ 32.551,06 | 1 vb | 70% | R$ 55.336,80 |

Custo total: **R$ 1.770.528,55**. Preço calculado: **R$ 2.404.898,54**.

Serviços recebem 70%; venda do equipamento recebe 15%. Esse BDI comercial é adicional ao BDI interno incorporado nas abas de operação.

### 5.12 `Final`

**Objetivo:** apresentar proposta comercial Rev.3, comparar Rev.2 e cenário sem venda.

| Item | Quantidade | Preço unitário | Total |
|---|---:|---:|---:|
| Mobilização | 1 | R$ 130.000 | R$ 130.000 |
| Operação com draga + MDO | 1 mês | R$ 233.500 | R$ 233.500 |
| MDO para operação | 5 meses | R$ 173.600 | R$ 868.000 |
| Tanque | 6 meses | R$ 14.500 | R$ 87.000 |
| Venda da draga | 1 | R$ 1.060.000 | R$ 1.060.000 |
| Desmobilização | 1 | R$ 65.600 | R$ 65.600 |

Total Rev.3: **R$ 2.444.100**. Coluna de valores possíveis: R$ 2.445.819,30. Rev.2: R$ 2.704.302,71. Desconto: 9,6218%. Cenário sem venda: R$ 1.683.600. Diferença associada à venda: R$ 760.500. Diferença de preço mensal entre primeiro mês e MDO: R$ 59.900.

**Anomalias:** referências externas residuais; draga descrita com vazão nominal de 300 m³/h sem cálculo correspondente; total adotado supera `Plan. Final` em R$ 39.201,46 sem fórmula explicativa; cenário sem venda agrega seis meses à operação com draga e zera a linha separada de MDO.

## 6. Entidades conceituais encontradas

Proposta; cliente; contato; obra/local; material; volume; sólidos in situ/desaguados; produção; prazo; draga; centrífuga; tanque; linha de recalque; flutuantes; acoplamentos; equipe; função; turno; salário; adicional; encargos; mobilização; desmobilização; fornecedor; cotação; item de custo; custo direto; BDI interno; custo financeiro; BDI comercial; preço negociado; revisão; cenário sem venda.

## 7. Regras de negócio observadas

### EVIDÊNCIA PARCIAL — Nível C

1. Conversão de volume em massa usa teores de sólidos in situ e final.
2. O prazo é dividido em primeiro mês com custo completo e cinco meses reduzidos.
3. Encargos sociais de 110% sobre horas × valor-hora.
4. Algumas funções recebem 25% de adicional.
5. Oficina e administração adicionam 5% cada sobre despesas diretas.
6. Depreciação da draga em 60 meses.
7. Juros de 1% ao mês sobre equipamento.
8. Linha/flutuantes/acoplamentos em 24 meses e juros de 1%.
9. BDI comercial de 70% para serviços e 15% para venda.
10. Preços finais podem ser substituídos por valores comerciais manuais.

Nenhuma regra foi promovida a padrão geral da FOS.

## 8. Valores embutidos e referências

Diesel R$ 7; melosa/energia R$ 1; carreta R$ 6.000; guindaste R$ 6.500/dia; rigger R$ 1.500; tanque/painel base R$ 60.000 em 24 meses; fabricação da draga R$ 350.000; ARVEN R$ 750.000; valor do equipamento R$ 550.000; automóvel R$ 5.000/mês; plano de saúde R$ 200/pessoa; refeição R$ 35.

As datas-base e validade de vários preços não estão registradas.

## 9. Anomalias consolidadas

1. Jacareí/Sem Centrífuga no nome versus Suzano/com centrífuga no conteúdo.
2. Um `#REF!` em `Produção`.
3. Quatro `#REF!` em cada aba de operação.
4. Três `#DIV/0!` em `Venda Draga`.
5. Duas fórmulas com vínculo externo residual em `Final`.
6. Divergência de volumes.
7. Divergência de distâncias.
8. Títulos copiados em abas de objetivos diferentes.
9. Resíduos de textos de bags/centrífuga.
10. Valores finais manuais sem derivação integral.
11. Soma de fabricação e ARVEN sem finalidade explícita.
12. Presença de `externalLink1.xml`.

## 10. Dúvidas para validação do especialista

1. O orçamento é da Suzano em Suzano-SP ou de Jacareí?
2. O que significa “Sem Centrífuga”?
3. A centrífuga é fornecida e operada pela Suzano?
4. Qual volume é contratual: 37.910 ou 26.928 m³?
5. Qual distância deve ser usada: 150 ou 350 m?
6. Como foi definida a produção de 408 t/mês?
7. Por que a venda soma fabricação e referência ARVEN?
8. O primeiro mês inclui venda/fornecimento ou apenas custo financeiro?
9. Por que “só mão de obra” inclui outros custos?
10. Qual a justificativa dos preços manuais Rev.3?
11. O cenário sem venda representa locação por seis meses?
12. As fórmulas quebradas deveriam alimentar preços por produção/hora?
13. O combustível é FOS ou a energia é Suzano?

## 11. Limitações

- Arquivo analisado sem alteração.
- Resultados de fórmulas lidos do cache do Excel; erros preservados.
- Sem acesso a cotações originais ou esclarecimentos externos.
- Divergências não foram corrigidas nem escolhidas.
- Nenhuma comparação transversal ou arquitetura foi realizada.

## 12. Validação final

- [x] Todas as 12 abas analisadas.
- [x] Documento exclusivo produzido.
- [x] Fórmulas, dependências, entidades, regras, valores e anomalias preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma funcionalidade criada.
- [x] Nenhuma arquitetura definida.
- [x] Nenhuma consolidação realizada.
