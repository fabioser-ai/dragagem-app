# Modelo 003 — Draga 14 — Torres/RS

## Status

- Engenharia reversa vertical concluída para o arquivo analisado.
- Nenhuma implementação funcional foi realizada.
- As interpretações permanecem provisórias até o crosscheck com os demais modelos.

## Fonte analisada

- Arquivo: `Composição preços - Draga 14.xlsx`
- Proposta registrada: `D_010_2026`.
- Local registrado: Torres — RS.
- Objeto registrado: execução de dragagem de 500.000 m³.
- Equipamento central: draga de 14 polegadas.
- Sistema de medição indicado: preço mensal.

## Regra de evidência

Este documento separa:

- **Fato observado:** conteúdo, valor, fórmula ou dependência presente no Excel.
- **Interpretação:** leitura conceitual provisória.
- **Hipótese para crosscheck:** possibilidade que depende de comparação com outros modelos.
- **Anomalia observada:** erro, referência quebrada, texto residual ou comportamento inconsistente presente no arquivo.

## Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identificação comercial, premissas técnicas, linha de recalque e calendário operacional. |
| 2 | `Produção` | Cálculo de produção horária, produção mensal e prazo da obra. |
| 3 | `1. Mobilização` | Mobilização da equipe e equipamentos, logística da linha de recalque e preço final do evento. |
| 4 | `2. Dragagem` | Composição mensal completa da operação da Draga 14, incluindo operação, pessoal, manutenção, apoio, administrativas, BDI, financeiras e preço de venda. |
| 5 | `3. Desmobilização` | Desmobilização da equipe e equipamentos, com estrutura semelhante à mobilização, mas quantidades e valores próprios. |

## Fluxo observado

```text
Dados e premissas da obra
        ↓
Produção e prazo
        ↓
Mobilização
        ↓
Operação mensal da Draga 14
        ↓
Desmobilização
```

Diferentemente dos modelos 001 e 002, o arquivo não possui uma aba final separada de consolidação comercial. A própria aba `2. Dragagem` contém resumo de despesas, custo total, preço unitário, BDI, preço de venda e cálculo de hora à disposição.

## 1. Dados da obra

### Fatos observados

A aba contém:

- proposta e data;
- cliente e contato;
- objeto e local;
- volume de dragagem;
- tipo de material;
- distância total de recalque;
- linha flutuante e linha de terra;
- profundidade, espessura e área, ainda sem preenchimento neste arquivo;
- tipo de bota-fora;
- sistema de medição;
- responsabilidades por canteiro e mobilização;
- horas por dia e dias por mês.

Valores usados:

- volume: 500.000 m³;
- material: areia fina;
- distância total de recalque: 1.200 m;
- linha flutuante: 700 m;
- linha de terra: 500 m;
- jornada: 21 h/dia;
- calendário: 26 dias/mês.

### Interpretação

A aba funciona como contrato de premissas do orçamento. Ela combina identidade comercial, parâmetros técnicos e calendário operacional.

## 2. Produção

### Fatos observados

Entradas:

- vazão: 850 m³/h;
- eficiência: 75%;
- concentração: 18%;
- horas por dia: 21;
- dias por mês: 26.

Resultados:

- produção horária: 114,75 m³/h;
- horas por mês: 546;
- produção mensal: 62.653,5 m³/mês;
- prazo bruto: aproximadamente 7,98 meses.

A lógica observada é:

```text
produção horária = vazão × eficiência × concentração
produção mensal = produção horária × horas mensais
prazo = volume total ÷ produção mensal
```

### Interpretação

A aba representa o dimensionamento produtivo que alimenta custos mensais, preço por metro cúbico e prazo da obra.

## 3. Mobilização

### Fatos observados

A aba possui dois blocos principais.

### Equipe

Composição observada:

- encarregado;
- operadores de draga;
- maquinistas;
- barqueiro;
- mecânico;
- ajudantes gerais;
- refeições;
- transporte.

O custo diário calculado é de aproximadamente R$ 7.582,17.

### Itens de mobilização

Incluem:

- treinamentos;
- exames médicos;
- comunicação;
- viagens;
- laudo de flutuabilidade;
- guindastes;
- carretas prancha e extensíveis;
- seguro de transporte;
- carretas carga seca;
- plano de rigging;
- veículo;
- mão de obra de integração e mobilização.

Resultados observados:

- subtotal: R$ 405.121,70;
- BDI: 50%;
- preço final: R$ 607.682,55.

### Linha de recalque e logística

A aba calcula:

- quantidade estimada de tubos de 14 polegadas;
- comprimento total da linha;
- quantidade de carretas necessárias para transporte dos tubos.

Para 1.200 m de linha, o arquivo estima 5 carretas de carga seca.

### Interpretação

A mobilização combina um evento único, equipe temporária, serviços terceiros e logística específica da linha de recalque.

## 4. Dragagem

### Papel observado

A aba é o centro econômico do modelo. Ela concentra praticamente todo o custo mensal da operação e contém os seguintes grupos:

1. operação;
2. pessoal;
3. manutenção;
4. equipamentos de apoio;
5. administrativas;
6. BDI;
7. financeiras;
8. resumo e preço de venda.

### 4.1 Operação

Itens observados:

- combustível;
- filtros e lubrificantes;
- fretes e carretos;
- materiais de segurança e uniformes.

A composição contém campos para horas mensais, eficiência, consumo por hora e valor do combustível.

Há observações indicando responsabilidades contratuais, como combustível fornecido pela contratante e alguns itens fornecidos por terceiro.

### 4.2 Pessoal

A aba calcula salários a partir de:

- quantidade de funcionários;
- função;
- valor unitário;
- horas normais;
- horas extras de 70%;
- horas extras de 100%;
- encargos sociais.

Equipe observada:

- encarregado;
- operadores de draga;
- maquinistas;
- barqueiro;
- ajudantes;
- mecânico;
- motorista previsto, mas zerado.

Também existem blocos de:

- cantina;
- alojamento;
- viagens nas folgas;
- prêmios de produção.

### 4.3 Manutenção

Itens observados:

- peças e acessórios, calculados como percentual mensal do preço do equipamento;
- docagem anual convertida para percentual mensal;
- limpeza e pintura;
- mão de obra de terceiros.

Custo mensal de manutenção observado: R$ 27.500,00.

### 4.4 Equipamentos de apoio

Itens observados:

- linha de recalque;
- rebocador;
- veículos;
- voadora;
- medidor/batimetria;
- máquina de solda;
- maçarico;
- ferramentas;
- canteiro;
- barrilete.

A linha de recalque é decomposta em:

- tubulação;
- flutuantes;
- acoplamentos;
- depreciação mensal;
- juros sobre o capital.

O custo mensal total da linha de recalque observado é R$ 67.017,50.

### 4.5 Administrativas

Itens observados:

- comissões;
- viagens de inspeção;
- viagens administrativas;
- comunicação;
- seguro e licenciamento.

Custo administrativo mensal observado: R$ 8.300,00.

### 4.6 BDI e financeiras

O BDI interno da composição inclui:

- oficina: 5%;
- administração: 5%;
- campo adicional para outros percentuais.

Custos financeiros observados:

- depreciação do equipamento em 60 meses;
- juros de capital de 1%;
- atraso como percentual das despesas diretas, zerado neste modelo.

### 4.7 Resultado econômico

Valores observados:

- despesas diretas: aproximadamente R$ 481.541,03/mês;
- BDI interno: aproximadamente R$ 48.154,10;
- custos financeiros: R$ 40.000,00;
- custo total: aproximadamente R$ 569.695,13/mês;
- produção prevista: 62.653,5 m³/mês;
- custo unitário: aproximadamente R$ 9,09/m³;
- BDI comercial aplicado no resumo: 100%;
- preço mensal de venda: aproximadamente R$ 1.139.390,27;
- preço equivalente: aproximadamente R$ 18,23/m³.

A aba também contém cálculo de hora à disposição e um valor sugerido para colocar o equipamento em funcionamento.

### Interpretação

Este modelo demonstra que o custo mensal da draga pode ser tratado como um centro de custo completo e autônomo. O preço mensal é posteriormente convertido em custo e preço por metro cúbico usando a produção prevista.

## 5. Desmobilização

### Fatos observados

A estrutura é semelhante à mobilização, mas as quantidades e a equipe são menores.

A aba inclui:

- equipe de desmobilização;
- exames e viagens;
- laudo;
- guindastes;
- carretas;
- seguro;
- planos de rigging;
- veículo;
- mão de obra de desmobilização;
- logística da linha de recalque.

Resultados observados:

- subtotal: R$ 349.450,60;
- BDI: 50%;
- preço final: aproximadamente R$ 524.175,90.

### Interpretação

A desmobilização não é simples inversão da mobilização. Ela reutiliza a mesma estrutura de composição, mas com equipe, serviços e valores próprios.

## Anomalias observadas

### Referências à aba Produção com resultado `#NAME?`

Foram observadas as seguintes células na aba `2. Dragagem`:

- `C9`, referenciando `Produção!H6`;
- `E232`, referenciando `Produção!D13`;
- `H242`, referenciando `Produção!H4`;
- `I242`, referenciando `Produção!H3`;
- `C246`, com `ROUNDUP(Produção!D24,0)`.

As referências pretendem consumir valores da aba Produção, mas o arquivo armazena ou apresenta resultado `#NAME?` nesses pontos.

A anomalia não impediu identificar os valores-alvo, pois os mesmos resultados estão visíveis na aba Produção e em outros campos da própria composição.

### Texto residual

O título da aba `2. Dragagem` menciona `operação do Sistema de Desidratação de lodo`, embora este arquivo não contenha sistema específico de desaguamento como bags ou centrífuga.

Isso pode ser herança de outro modelo de planilha e não deve ser tratado como evidência de que desaguamento faz parte deste orçamento.

### Valores estimados sem fonte formal

Alguns itens possuem observações como `chute`. Esses valores devem ser tratados como estimativas específicas da proposta, não como parâmetros consolidados da FOS.

## Padrões confirmados pelo Modelo 003

### Núcleo comum já repetido

O terceiro modelo repete:

- dados da obra;
- produção e prazo;
- mobilização;
- operação;
- desmobilização;
- custos de equipe;
- manutenção;
- equipamentos de apoio;
- despesas administrativas;
- BDI;
- custos financeiros.

### Eventos e recorrências

O arquivo reforça a distinção entre:

- eventos únicos: mobilização e desmobilização;
- custos recorrentes mensais: operação, pessoal, manutenção e apoio;
- custos dependentes de produção: preço equivalente por metro cúbico.

### Responsabilidades contratuais

Itens podem estar presentes na estrutura, mas serem zerados ou anotados como fornecidos pela contratante ou por terceiros.

O futuro sistema deverá representar a responsabilidade pelo recurso separadamente de sua existência técnica.

### Preço mensal e preço por produção

O mesmo centro de custo pode produzir:

- preço mensal de venda;
- custo unitário por metro cúbico;
- preço de venda por metro cúbico;
- hora à disposição.

Isso indica que a unidade comercial não precisa ser única para todo o modelo.

## Comparação preliminar com os modelos anteriores

| Elemento | Modelo 001 — Bags | Modelo 002 — Centrífuga | Modelo 003 — Draga 14 |
| --- | --- | --- | --- |
| Dados da obra | Sim | Sim | Sim |
| Produção e prazo | Sim | Sim | Sim |
| Mobilização | Vários sistemas | Draga e centrífuga | Draga e linha de recalque |
| Desaguamento | Bags/polímero | Centrífuga | Não observado como sistema próprio |
| Operação da draga | Integrada ao conjunto | Centro separado | Centro principal e autônomo |
| Manutenção | Dentro de pacotes | Genérica + especializada | Pacote mensal dentro da draga |
| Consolidação final separada | Sim | Sim | Não; embutida na aba Dragagem |
| Unidade comercial | Varia por pacote | TSS e mês | Mês, m³ e hora à disposição |
| Revisões comerciais | Limitadas | Explícitas | Não estruturadas em aba própria |

## Hipóteses para crosscheck

1. Dados da obra, produção, mobilização, operação e desmobilização formam um núcleo recorrente do Método de Orçamento FOS.
2. Sistemas de desaguamento são componentes opcionais, não parte obrigatória de todo orçamento de dragagem.
3. A operação da draga pode existir como centro de custo autônomo e ser reutilizada dentro de modelos maiores.
4. O sistema deverá suportar várias unidades comerciais para um mesmo orçamento ou pacote: mês, m³, TSS, hora e evento.
5. Responsabilidade contratual deve ser um atributo explícito de cada recurso ou item.
6. A consolidação comercial pode existir em aba própria ou dentro da composição principal; a arquitetura futura não deve depender da estrutura física do Excel.

## Conhecimento ainda não consolidado

Ainda não devem ser tratados como regras universais:

- percentuais de BDI;
- percentuais de manutenção;
- equipe padrão da Draga 14;
- consumo de combustível;
- valores de salário;
- quantidade de carretas;
- preço de linha de recalque;
- fórmula e valor de hora à disposição;
- margem comercial de 100% usada neste arquivo.

## Próximo passo

Analisar os próximos modelos integralmente e ampliar o crosscheck antes de definir a arquitetura do sistema orçamentário.
