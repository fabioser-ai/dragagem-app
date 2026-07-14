# Análise de Conhecimento — Composição - Klabin Ortigueira.xlsx

## Identificação

- **Nome integral do arquivo:** `Composição - Klabin Ortigueira.xlsx`
- **Data da análise:** 2026-07-14
- **Versão explícita:** não identificada no nome
- **Criação registrada no workbook:** 2010-07-15T18:27:10Z
- **Última modificação registrada:** 2025-01-20T13:55:57Z
- **Último autor registrado:** Fabio Pereira Serafini
- **Quantidade de abas:** 21
- **Células não vazias ou com fórmula:** 3.940
- **Fórmulas encontradas:** 1.104
- **SHA-256 da fonte:** `c8554a40b0c25089f08dd3eacd88f91d1258838f472ba020100a32e4ffa173ff`
- **Status:** ANÁLISE COMPLETA — todas as abas inspecionadas; nenhuma consolidação realizada

## Classificação

**EVIDÊNCIA CONFIRMADA:** orçamento técnico-comercial de dragagem de lodo de ETE com desidratação/desaguamento por centrífugas (decanters), incluindo canteiro, mobilizações, operação, serviços complementares, desmobilizações e consolidação comercial.

**EVIDÊNCIA CONFIRMADA:** processo representado: dragagem hidráulica de lagoa, recalque, alimentação das centrífugas, separação sólido-líquido, movimentação do lodo desaguado e retirada dos sistemas.

**EVIDÊNCIA CONFIRMADA:** local da obra: Ortigueira-PR. O cabeçalho identifica KLABIN.

**EVIDÊNCIA PARCIAL:** o arquivo estuda configurações com duas ou três centrífugas, um ou dois turnos e produção mínima faturável. A aba `RESUMO` usa horizonte econômico de 58 meses, enquanto as composições principais usam seis meses de operação. A coexistência não é explicada.

## Escopo e premissas observadas

- Objeto: dragagem e desidratação de lodo.
- Volume: 15.000 m³.
- Material: lodo de ETE.
- Destinação/processamento: centrífuga.
- Recalque total: 200 m, sendo 100 m flutuante e 100 m terrestre.
- Jornada-base: 12 h/dia e 22 dias/mês.
- Produção mínima informada nos parâmetros: 833 t de lodo desaguado/mês.
- Sólidos in situ: 10%.
- Sólidos após desaguamento: 30%.
- Prazo operacional usado: 6 meses.
- Proposta indicada: D_026_2024.

## Fluxo completo observado

1. `Dados Obra ` reúne identificação, escopo, volumes, linhas, jornada e parâmetros.
2. `Produção (NOVO CALCULO)`, `Produção (cliente)` e `Produção` executam cálculos paralelos de capacidade, produção e prazo.
3. `1. Canteiro` dimensiona equipe, salários, leis sociais e estrutura de apoio.
4. `2.1 Mob Draga` e `2.2 Mob Centr` compõem mobilizações.
5. As abas `3.x` compõem aluguel, manutenção, base de concreto, remoção de ensecadeira e movimentação de lodo desaguado.
6. `4.1 Draga Dec` compõe a operação mensal da dragagem.
7. `4.2 Centrífuga` compõe a operação mensal do desaguamento.
8. `5. Desmob Canteiro`, `Desmob Draga` e `Desmob Centr` compõem a retirada.
9. `Plan. Final` consolida as composições.
10. `Final` apresenta a saída comercial resumida.
11. `RESUMO` simula cenários comerciais e econômicos independentes.

## Entidades encontradas

**EVIDÊNCIA CONFIRMADA:** proposta, cliente, contato, obra, local, objeto, material, volume, lagoa, recalque, linha flutuante, linha terrestre, teor de sólidos, lodo seco, lodo desaguado, jornada, prazo, produção mínima, draga, centrífuga/decanter, tanque, bomba, polímero, canteiro, equipe, função, turno, salário-hora, leis sociais, refeições, alojamento, mobilização, desmobilização, equipamento de apoio, manutenção, custo direto, BDI, despesa financeira, preço de venda, faturamento mínimo, cenário comercial e fornecedor.

## Regras de negócio e fórmulas relevantes

- **EVIDÊNCIA CONFIRMADA:** volume mensal estimado a dragar = `(produção desaguada × % sólidos desaguado) ÷ % sólidos in situ`.
- **EVIDÊNCIA CONFIRMADA:** volume total = `volume mensal × prazo`.
- **EVIDÊNCIA CONFIRMADA:** lodo seco = `volume × % sólidos in situ`.
- **EVIDÊNCIA CONFIRMADA:** lodo desaguado = `lodo seco ÷ % sólidos desaguado`.
- **EVIDÊNCIA CONFIRMADA:** custo diário de mão de obra = `quantidade × salário-hora × horas/dia × (1 + leis sociais)`; as composições usam 110% de leis sociais.
- **EVIDÊNCIA CONFIRMADA:** determinadas funções recebem adicional de 25%, calculado por multiplicador 1,25.
- **EVIDÊNCIA CONFIRMADA:** horas mensais remuneradas = `(HE 70% × 1,70) + (HE 100% × 2) + horas normais`.
- **EVIDÊNCIA CONFIRMADA:** despesas diretas agregam operação, pessoal, manutenção, equipamentos de apoio e administrativas.
- **EVIDÊNCIA CONFIRMADA:** o BDI interno das operações contém parcelas de oficina e administração, ambas em 5% quando utilizadas.
- **EVIDÊNCIA CONFIRMADA:** células laterais das operações aplicam fator 1,6 ao custo mensal para formar preço mensal de venda.
- **EVIDÊNCIA CONFIRMADA:** preço horário = `preço mensal ÷ horas trabalhadas × 0,7`.
- **EVIDÊNCIA CONFIRMADA:** no `RESUMO`, faturamento mínimo = `preço proposto × quantidade mínima`.
- **EVIDÊNCIA CONFIRMADA:** resultados do `RESUMO` usam 85% do faturamento, custos mínimos e períodos de 15 e 43 meses, totalizando 58 meses.
- **DÚVIDA:** o arquivo não explica o significado econômico do fator 0,85.

## Dependências entre abas

- `Produção (cliente)` e `Produção` dependem de `Dados Obra `.
- `1. Canteiro` depende de `Produção`.
- Mobilizações, serviços 3.x e desmobilizações dependem principalmente de `1. Canteiro`.
- `4.1 Draga Dec` depende de `1. Canteiro`, `2.1 Mob Draga`, `Dados Obra ` e `Produção`.
- `4.2 Centrífuga` depende de `1. Canteiro`, `4.1 Draga Dec`, `Dados Obra ` e `Produção`.
- `Plan. Final` reúne mobilizações, serviços complementares, operações, desmobilizações e cálculos de produção.
- `Final` depende de `Dados Obra ` e `Plan. Final`.

## Análise por aba

### `RESUMO`
Simula quantidades mínimas de 1.500, 1.780, 2.400 e 3.000 t/mês, configurações com duas ou três centrífugas, um ou dois turnos, base e estrutura metálica. Calcula faturamento mínimo, resultado nos primeiros 15 meses, resultado nos últimos 43 meses, resultado total e média mensal. Custos mínimos: R$ 220 mil; adicional de R$ 300 mil para três centrífugas e R$ 200 mil para duas. Há resultados hardcoded ao lado de fórmulas.

### `Dados Obra `
Contém proposta, contatos, objeto, local, volume, material, linhas e jornada. Parâmetros: 833 t desaguadas/mês, 10% ST in situ, 30% ST desaguado, 6 meses e volume total estimado de aproximadamente 14.994 m³. **Anomalia:** cabeçalho KLABIN, mas campo Cliente = SUZANO. Profundidade, espessura e área estão vazias.

### `Fornecedores`
Estrutura de cadastro para guindaste de 100 t, com empresa, contato, telefone, e-mail, preço e observação. Nenhum fornecedor foi preenchido.

### `Produção (NOVO CALCULO)`
Matriz teórica para duas ou três centrífugas de 40 m³/h, 12 ou 16 horas, 22 ou 26 dias e concentrações de entrada de 2%, 3% e 4%, com sólidos desaguados de 20%, 30% e 40%. **Anomalia:** `D39` usa 22 dias em bloco de 16 horas cujas células vizinhas usam 26 dias.

### `Produção (cliente)`
Usa vazão 80 m³/h, eficiência 65%, concentração 25%, entrada com 2% de sólidos, 12 h/dia e 22 dias/mês. Resultados armazenados: 274,56 t secas/mês, 915,2 t desaguadas/mês e prazo aproximado de 4,37 meses.

### `Produção`
É o cálculo operacional de produção e prazo utilizado por diversas composições. Mantém blocos paralelos e resíduos de identificação Suzano. **DÚVIDA:** não está explícito qual das três abas de produção é a referência oficial.

### `1. Canteiro`
Dimensiona encarregado, técnico de segurança, operador de draga, operadores de centrífuga e ajudantes. Usa 110% de leis sociais, refeição e transporte. Inclui containers, limpeza, material de escritório e integração. Total armazenado: R$ 46.829,424; rateio mensal: R$ 7.804,904.

### `2.1 Mob Draga`
Inclui equipe por 22 dias, quatro carretas, guindaste, plano de rigger, munck, containers, mobiliário, segurança, tenda, exames e documentação. Total armazenado: R$ 219.554,416. Contém item repetido e referências históricas de cotação.

### `2.2 Mob Centr`
Compõe a mobilização das centrífugas, reaproveitando salários e equipe do canteiro. **Anomalia:** o título interno ainda menciona mobilização de draga 10 polegadas e draga elétrica/miúda.

### `3.1 - Aluguel 3 meses Centrif`
Composição específica para aluguel inicial de centrífugas. Soma itens, permite BDI e gera preço final. O título interno menciona manutenção de equipamentos SUZANO.

### `3.3 - Manutenção`
Composição de manutenção com mão de obra, peças, materiais e serviços. Depende de `1. Canteiro` e `Dados Obra `. Mantém referências SUZANO e itens zerados.

### `3.4. BASE DE CONCRETO`
Composição específica da base de concreto. Lista recursos, quantidades, preços e mão de obra. Mantém título interno reaproveitado de manutenção SUZANO.

### `3.5. Remoção Ensecadeira`
Composição específica de remoção de ensecadeira. **Anomalia:** numeração 3.5 duplicada.

### `3.5. Mov. Lodo desag`
Composição específica da movimentação do lodo desaguado. **Anomalia:** numeração 3.5 duplicada e título interno reaproveitado.

### `4.1 Draga Dec`
Organiza custos de operação, pessoal, manutenção, equipamentos de apoio, administrativas, BDI e financeiras. Custo mensal armazenado: R$ 129.795,469. Custo de seis meses: R$ 778.772,815. Preço mensal com fator 1,6: R$ 207.672,751. Preço/hora com fator 0,7: R$ 550,647. **Erros:** `D205 = D201/D203` resulta em `#DIV/0!`; `D206 = D205*4000` também resulta em `#DIV/0!`.

### `4.2 Centrífuga`
Valor do equipamento: R$ 3.000.000. Custo mensal armazenado: R$ 351.876,687. Total de seis meses: R$ 2.111.260,120. Preço mensal com fator 1,6: R$ 563.002,699. Preço/hora: R$ 1.492,810. **Anomalias:** depreciação rotulada como 60 meses usa `F7/12`; manutenção rotulada como 0,1% usa `F7*0,005` (0,5%); `D187` contém `=#REF!*0.6*0.62`.

### `5. Desmob Canteiro`
Compõe a retirada do canteiro com estrutura semelhante à implantação. Contém itens zerados e reaproveitados.

### `Desmob Draga`
Espelha a mobilização da draga para carga, guindaste, carretas, equipe e retorno. O título interno ainda menciona mobilização.

### `Desmob Centr`
Espelha a mobilização das centrífugas. O título interno ainda menciona mobilização de draga.

### `Plan. Final`
Consolida mobilizações, serviços pontuais, operações e desmobilizações, aplicando quantidades, preços de custo e venda. É o principal elo com a apresentação comercial. Possui referências a múltiplas abas de produção, valores fixos, fórmulas e auto-referências.

### `Final`
Síntese comercial com identificação, itens, unidades, quantidades, preços unitários e totais importados de `Plan. Final`. O arquivo não identifica claramente qual cenário foi efetivamente enviado ou aprovado.

## Anomalias confirmadas

1. Dois `#DIV/0!` em `4.1 Draga Dec`.
2. Um `#REF!` em `4.2 Centrífuga`.
3. Divergência KLABIN/SUZANO.
4. Rótulo de depreciação de 60 meses com fórmula de 12 meses.
5. Rótulo de manutenção de 0,1% com fórmula de 0,5%.
6. Assimetria de dias na matriz de produção.
7. Duas abas numeradas como 3.5.
8. Títulos e observações residuais de Suzano, Aracruz e outros modelos.
9. Mistura de fórmulas e valores hardcoded em cenários equivalentes.
10. Itens repetidos, sem descrição, zerados ou com fórmulas em linhas aparentemente inativas.

## Dúvidas

- O cliente correto desta versão é Klabin ou Suzano?
- O horizonte de 58 meses pertence a esta proposta ou é cenário reaproveitado?
- O fator 0,85 representa impostos, retenção, margem ou outro conceito?
- Qual aba de produção é a fonte oficial?
- A produção mínima válida é 833, 1.500, 1.780, 2.400 ou 3.000 t/mês?
- A capacidade unitária da centrífuga é 40 ou 60 m³/h?
- A depreciação correta é 12 ou 60 meses?
- A manutenção correta é 0,1% ou 0,5%?
- Quais valores zerados são exclusões deliberadas e quais são pendências?
- Qual cenário da planilha final foi efetivamente enviado/aprovado?

## Classificação final das evidências

- **EVIDÊNCIA CONFIRMADA:** conteúdo literal, fórmulas, valores armazenados, referências e erros presentes diretamente no Excel.
- **EVIDÊNCIA PARCIAL:** interpretação do papel operacional das abas e identificação de reaproveitamento histórico; observada somente neste arquivo.
- **DÚVIDA:** significados não rotulados, parâmetros conflitantes e escolha do cenário vigente.

## Limitações

- O Excel não foi alterado nem recalculado.
- Os valores armazenados foram preservados como encontrados.
- Não houve comparação com outros orçamentos.
- Não houve consolidação, arquitetura, banco de dados, telas ou implementação.

## Validação

- [x] Todas as 21 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Entidades, regras, fórmulas, dependências, anomalias, terminologias e dúvidas registradas.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma consolidação realizada.
- [x] Nenhuma decisão arquitetural tomada.
