# APP FOS — Crosscheck preliminar de 49 orçamentos

## Status e limite desta leitura

- Conjunto recebido: **49 arquivos**.
- Arquivos `.xlsx` analisados estruturalmente: **48**.
- Arquivo `.xls` legado identificado: **1**; preservado no inventário, ainda sem leitura estrutural completa.
- Fórmulas inventariadas nos `.xlsx`: **19.651**.
- Este documento é um primeiro crosscheck automatizado da estrutura. A consolidação funcional final ainda exige leitura detalhada de fórmulas, valores, vínculos e exceções por família.

## Conclusão principal

> O método atual da FOS já revela um núcleo recorrente e famílias claras de orçamento. O novo sistema deve preservar a lógica de trabalho, mas separar núcleo comum, modelos de engenharia e pacotes opcionais.

Não recomendo copiar um workbook específico para o APP. Recomendo um construtor de orçamento guiado por etapas, com modelos selecionáveis e pacotes ativáveis conforme a obra.

## Evidências quantitativas

| Elemento estrutural | Arquivos em que foi identificado |
|---|---:|
| Dados da obra | 47/48 |
| Produção e prazo | 46/48 |
| Desmobilização | 45/48 |
| Dragagem principal | 41/48 |
| Canteiro / mobilização de equipe | 39/48 |
| Mobilização de draga | 37/48 |
| BDI / formação de preço | 31/48 |
| Resumo / proposta final | 31/48 |
| Medição / batimetria | 30/48 |
| Operação de desaguamento/planta | 26/48 |
| Mobilização sistema/polímero/centrífuga | 25/48 |
| Barrilete / linha de recalque | 22/48 |
| Preparo de célula / bacia / paliçada | 22/48 |
| Bags / geotêxteis | 20/48 |
| Cotações | 5/48 |
| Carga / transporte / destinação | 4/48 |

## Famílias provisórias identificadas

| Família | Quantidade | Observação |
|---|---:|---|
| Dragagem com bags/geotêxteis | 20 | Maior família; normalmente agrega célula/bacia, bags, polímero ou operação de planta. |
| Dragagem com centrífuga | 7 | Fluxo semelhante à dragagem, mas com mobilização/operação próprias do sistema de desaguamento. |
| Dragagem/bombeamento | 7 | Orçamentos mais enxutos, sem todos os pacotes de desaguamento. |
| Composição padrão de draga | 4 | Modelos de referência ou formação de preço do equipamento/equipe. |
| Batimetria / levantamento | 4 | Família distinta, com equipe, mobilização, levantamento e relatório. |
| Dragagem com paliçada/bacia | 2 | Implantação física específica acoplada à dragagem. |
| Composição de mão de obra | 1 | Modelo focado em equipe e encargos. |
| Equalização técnica | 1 | Documento comparativo, não necessariamente orçamento operacional completo. |
| Outros / composição específica | 1 | Modelo não classificado automaticamente. |
| Equipamento / motobomba | 1 | Composição específica de equipamento. |

## Duplicidades confirmadas no conjunto

- `D_036_2025_A - SAEC - Catanduva- SP.xlsx` e `D_036_2025_B - SAEC - Catanduva- SP.xlsx` são binariamente idênticos.
- `D_042_2025 - CMPC - Dragagem - Bombeamento.xlsx` e `D_050_2025 - CMPC - Dragagem - Bombeamento.xlsx` são binariamente idênticos.

Esses casos devem permanecer rastreáveis no acervo, mas contam como dois documentos administrativos e apenas uma evidência estrutural cada.

## Núcleo comum candidato

Os elementos abaixo aparecem com recorrência suficiente para formar a espinha dorsal do novo sistema:

1. Identificação e premissas da obra.
2. Modelo de produção e prazo.
3. Calendário operacional e regime de trabalho.
4. Composição de mão de obra.
5. Mobilização e desmobilização.
6. Operação principal.
7. Formação de custo e preço.
8. Consolidação técnica/comercial.

Nem todos devem ser uma tela única e fixa. Alguns são seções obrigatórias; outros podem ser etapas configuráveis.

## Componentes opcionais e condicionais

A recorrência mostra que estes componentes devem ser ativáveis conforme o orçamento:

- canteiro;
- barrilete e linha de recalque;
- sistema de polímero;
- centrífuga;
- preparo de célula, bacia ou paliçada;
- fornecimento de bags;
- operação da planta de desaguamento;
- medição e batimetria;
- carga, transporte e destinação;
- mobilizações e desmobilizações específicas.

A regra de **Não aplicável** faz sentido para esses blocos, desde que desative cálculos sem apagar o histórico.

## Arquitetura funcional recomendada

```text
Orçamento
├── Identificação e premissas
├── Seleção da família/modelo
├── Produção e prazo
├── Pacotes aplicáveis
│   ├── mobilização
│   ├── canteiro
│   ├── dragagem/operação principal
│   ├── desaguamento
│   ├── estruturas auxiliares
│   ├── medição/controle
│   └── desmobilização
├── Composições e recursos
├── Cotações e parâmetros adotados
├── Formação de preço
└── Resumo técnico e comercial
```

## Princípios que o sistema precisa preservar

- O engenheiro trabalha por premissas, produção, dimensionamentos e composições.
- Valores de referência devem poder ser alterados no orçamento.
- O sistema deve guardar valor sugerido, valor adotado e origem.
- Alterações em catálogos não podem mudar orçamentos antigos.
- Fórmulas devem ser rastreáveis e testáveis fora das telas.
- Um pacote pode consumir resultados de outro; o cálculo é uma rede, não apenas uma sequência.
- A apresentação comercial pode resumir uma composição técnica muito mais detalhada.
- Exceções reais devem ser suportadas, não eliminadas para simplificar o software.

## Processo recomendado antes do Work implementar

1. Fechar o inventário estrutural dos 48 `.xlsx` e converter controladamente o único `.xls`.
2. Agrupar os modelos por família e escolher representantes de cada uma.
3. Fazer leitura profunda de fórmulas e dependências de cada representante.
4. Produzir matrizes de campos, fórmulas, pacotes, direcionadores e resultados.
5. Validar com Fabio as diferenças que representam decisão de engenharia.
6. Consolidar o **Método FOS de Orçamento Provisório V1**.
7. Só então entregar ao Work a arquitetura física e os Kid Steps.

## Direção para o produto

O novo módulo deve ser moderno e simples de operar, mas não deve alterar a lógica mental da FOS. A modernização deve ocorrer em:

- navegação;
- reutilização de catálogos;
- preenchimento assistido;
- rastreabilidade;
- versões;
- validações;
- recalculo automático;
- comparação histórica;
- consolidação e emissão.

A lógica de engenharia continua sendo a da FOS; o APP organiza, explica e preserva essa lógica.

## Próximo artefato recomendado

Produzir um documento consolidado com:

- matriz arquivo × etapa;
- matriz arquivo × família;
- catálogo de nomes equivalentes de abas;
- fórmulas recorrentes por conceito;
- parâmetros embutidos e respectivas frequências;
- dependências entre etapas;
- lista de divergências que exigem decisão do especialista;
- proposta de telas do MVP.

Inventário tabular correspondente: `INVENTARIO_49_ORCAMENTOS.csv`.