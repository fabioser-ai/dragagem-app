# Modelo 001 — Dragagem com Desaguamento em Bags — SABESP

## Status

- Engenharia reversa vertical concluída para o arquivo analisado.
- Nenhuma implementação funcional foi realizada.
- As interpretações deste documento ainda dependem do crosscheck com outros modelos.

## Fonte analisada

- Arquivo: `D_004_2026 - SABESP.xlsx`
- Tipo de obra: dragagem com desaguamento e acondicionamento em bags.
- Cliente registrado no arquivo: SABESP — Cubatão — ETA 3.
- Volume usado no modelo: 5.000 m³.

## Regra de evidência

Este documento separa:

- **Fato observado:** conteúdo, valor, fórmula ou dependência presente no Excel.
- **Informação do especialista:** explicação fornecida por Fabio.
- **Interpretação:** leitura conceitual provisória.
- **Hipótese para crosscheck:** possibilidade que somente poderá ser consolidada após comparação com outros modelos.

## Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identificação, premissas técnicas e calendário operacional. |
| 2 | `Cotaçoes` | Estrutura para pesquisas de mercado de guindaste, container, banheiro químico e destinação. |
| 3 | `Produção` | Cálculo de produção horária, produção mensal e prazo. |
| 4 | `Barrilete` | Composição física do barrilete, mão de obra, depreciação e preço utilizado por outros pacotes. |
| 5 | `1. Mob. Draga` | Mobilização da draga: equipe, fretes, guindastes e apoio. |
| 6 | `2. Mob. Eq. Polimero` | Mobilização do sistema de polímero e consumo do preço do barrilete. |
| 7 | `Canteiro` | Infraestrutura temporária, obrigações de apoio e preço mensal. |
| 8 | `3. Prep. Célula` | Dimensionamento físico e composição do preparo da célula. |
| 9 | `4. Forn. Bag` | Dimensionamento da necessidade de bags e composição de fornecimento/instalação. |
| 10 | `5. Operação Sistema` | Operação do sistema de desidratação e consumo de polímero. |
| 11 | `6. Dragagem` | Centro principal de custos operacionais, pessoais, manutenção, apoio, administrativas, BDI e financeiras. |
| 12 | `7. Medição` | Amostras, batimetria e acompanhamento da coleta dos bags. |
| 13 | `8. Carga e Transporte` | Estrutura opcional de carga, transporte e acompanhamento; valores zerados neste modelo. |
| 14 | `8. Desmob. Draga` | Desmobilização da draga. |
| 15 | `9. Desmob. Eq. Polimero` | Desmobilização do sistema de polímero. |
| 16 | `10. Plan. Preços` | Consolidação detalhada de custo, BDI, preço unitário e preço total. |
| 17 | `Planilha1` | Consolidação comercial simplificada em quatro macroitens e total geral. |

## Fluxo observado

```text
Dados e premissas da obra
        ↓
Produção e prazo
        ↓
Dimensionamentos específicos
        ↓
Composições de mobilização, implantação, operação, apoio e desmobilização
        ↓
Consolidação detalhada de preços
        ↓
Apresentação comercial simplificada
```

O arquivo possui ordem sequencial de trabalho, mas também contém dependências em rede entre abas. Não deve ser interpretado apenas como uma sequência linear.

## 1. Dados da obra

### Fatos observados

A aba contém:

- proposta, data, cliente e contato;
- objeto e local;
- volume de dragagem;
- tipo de material;
- distância de recalque;
- linha flutuante e linha de terra;
- profundidade, espessura média e área;
- tipo de bota-fora;
- sistema de medição;
- responsabilidade por canteiro e mobilização;
- horas por dia e dias por mês.

Fórmulas observadas:

- distância total de recalque = distância informada + seio;
- linha flutuante total = linha informada + seio;
- volume geométrico = área × dimensão × espessura, quando preenchido.

### Interpretação

A aba funciona como conjunto de premissas do orçamento. Ela mistura identificação comercial, caracterização técnica, decisões executivas e calendário operacional.

## 2. Cotações

### Fatos observados

A aba possui blocos para:

- guindaste;
- container;
- banheiro químico;
- destinação.

Cada bloco admite fornecedor, contato, telefone, detalhe e preço. Nenhuma fórmula foi observada.

### Interpretação

A aba registra pesquisa de mercado utilizada na elaboração do orçamento. Fornecedor e contato têm potencial de reutilização; preço cotado é temporal e deve preservar o contexto do orçamento.

### Hipótese para crosscheck

Comparar se outros modelos possuem as mesmas famílias de cotação e se existe padrão reutilizável de fornecedor, serviço, data-base e preço cotado.

## 3. Produção

### Fatos observados

Entradas principais:

- vazão: 120 m³/h;
- eficiência: 60%;
- concentração: 15%;
- 9 horas/dia;
- 22 dias/mês.

Fórmulas:

- horas mensais = horas/dia × dias/mês;
- produção horária = vazão × eficiência × concentração;
- produção mensal = produção horária × horas mensais;
- prazo = volume total ÷ produção mensal.

Resultado do arquivo:

- produção horária: 10,8 m³/h;
- produção mensal: 2.138,4 m³/mês;
- prazo: aproximadamente 2,338 meses.

### Interpretação

A produção transforma premissas de operação em prazo e alimenta custos dependentes de tempo.

## 4. Barrilete

### Fatos observados

A aba combina:

- custo diário de equipe;
- composição de tubos, conexões, válvulas, mangueiras, bomba e montagem;
- preços de diversos componentes formados por valor-base × 1,4;
- total da composição;
- apropriação de 20% como depreciação;
- BDI interno zerado neste modelo.

O valor final de R$ 5.923,36 é consumido pelas abas de mobilização e desmobilização do sistema de polímero.

### Interpretação

O barrilete é um componente técnico reutilizado por outros pacotes. O arquivo precifica seu uso por depreciação, não pelo valor integral da composição.

## 5. Mobilização da draga

### Fatos observados

Estrutura:

- equipe de carga e montagem;
- encargos sociais de 110%;
- refeições e transporte;
- guindaste, carreta, frete, trator, treinamentos, mobiliário e mão de obra;
- subtotal e BDI zerado.

Preço final no modelo: R$ 16.961,72.

### Interpretação

É um pacote de evento único. Recursos humanos são calculados por dia; contratações e serviços são somados à composição.

## 6. Mobilização do sistema de polímero

### Fatos observados

Inclui:

- equipe;
- cobertura e munck;
- brita e concreto;
- frete;
- instalações hidráulicas e elétricas;
- máquina WAP;
- barrilete referenciado de outra aba;
- mão de obra de apoio.

Preço final no modelo: R$ 39.925,08.

### Interpretação

Confirma que um pacote pode consumir o resultado de outro pacote. O orçamento é uma rede de dependências.

## 7. Canteiro

### Fatos observados

O próprio título identifica o canteiro como subitem da dragagem.

Inclui:

- equipe;
- containers;
- fretes;
- PPRA, PCMSO, LTCAT e ART;
- placa, vigilância, água, escritório e banheiro químico;
- exames médicos e integração.

A quantidade do container de almoxarifado contém erro `#NAME?` no arquivo importado. O preço mensal é calculado dividindo o total pelo prazo arredondado.

### Interpretação

É um custo de suporte dependente da duração da obra e consumido pela composição de Dragagem.

## 8. Preparo da célula

### Fatos observados

A aba possui memorial de quantidades por área de célula:

- PEAD: 1,196 m² por m² de célula;
- Bidim: 1,48 m² por m² de célula;
- brita: 0,15 m³ por m² de célula;
- retroescavadeira: 0,023 h por m²;
- mão de obra: 0,023 h por m².

Também contém composição de custos para terreno, mobilização de equipamentos, PEAD, instalação, Bidim, brita, retroescavadeira e mão de obra.

Preço final no modelo: R$ 177.323,61.

### Interpretação

Primeiro ocorre dimensionamento físico; depois as quantidades são precificadas. Os coeficientes são candidatos a conhecimento técnico, mas não podem ser generalizados antes do crosscheck.

## 9. Fornecimento de bags

### Fatos observados

A aba contém duas áreas relacionadas:

1. composição de fornecimento e instalação;
2. dimensionamento do volume e combinação de modelos de bags.

Dimensionamento observado:

- volume: 5.000 m³;
- sólidos in situ: 10%;
- tonelada seca: 500;
- sólidos após desaguamento: 20%;
- volume a acomodar: 2.500 m³.

O modelo seleciona 5 bags 8 × 30 e 10 bags 8 × 15. A tabela contém capacidades, quantidades, volumes, reinício de célula e referências de preço por m³.

Preço final de fornecimento/instalação: R$ 355.460,245.

### Interpretação

O número de bags é resultado de um modelo de engenharia e alimenta a composição financeira.

### Hipótese para crosscheck

Capacidades efetivas, reinício de célula e preço por m³ precisam ser comparados com outros arquivos e validados como específicos de modelo, material, fornecedor ou experiência histórica.

## 10. Operação do sistema de desidratação

### Fatos observados

Inclui:

- equipe diária;
- equipamento de preparo e injeção;
- polímero;
- frete;
- água e energia atribuídas à contratante neste modelo;
- instalações hidráulicas;
- mão de obra operacional.

A quantidade de polímero é calculada por:

```text
tonelada seca × 3 kg/t × 1,05
```

A mão de obra é calculada com base no prazo arredondado × 30 dias.

O custo mensal é o total dividido pelo prazo arredondado.

### Informação do especialista

O consumo de polímero não é constante da FOS. Ele varia conforme:

- tipo de material;
- tipo de equipamento ou processo de desaguamento;
- características da obra;
- experiência histórica.

O valor de 3 kg/t pertence a este orçamento. No sistema futuro, o histórico deverá apoiar uma sugestão, preservando o valor efetivamente adotado pelo engenheiro.

## 11. Dragagem

### Fatos observados

É a maior aba do modelo e concentra múltiplas categorias:

- operações e insumos;
- pessoal;
- encargos e provisões;
- cantina;
- alojamento;
- viagens de folga;
- prêmios de produção;
- manutenção;
- equipamentos de apoio;
- linha de recalque;
- despesas administrativas;
- BDI;
- despesas financeiras;
- resumo, custo mensal, custo unitário e hora à disposição.

Dependências observadas:

- consome o preço mensal do canteiro;
- consome o custo mensal da operação do sistema de bags/polímero;
- utiliza produção e prazo;
- consolida custo mensal da dragagem e custo mensal de desaguamento;
- gera o custo total usado na planilha de preços.

Valores relevantes no arquivo:

- despesas diretas: R$ 57.823,3591;
- BDI interno: R$ 5.782,3359;
- financeiras: R$ 4.289,1168;
- custo mensal da dragagem: R$ 67.894,8118;
- operação mensal de bags/polímero: R$ 40.998,2725;
- custo mensal total: R$ 108.893,0843;
- custo total da dragagem + operação dos bags: R$ 326.679,2530.

O arquivo contém referências e cálculos auxiliares para linha de recalque, depreciação, juros, atrasos, custo por hora e preço de venda.

### Interpretação

A aba representa uma estrutura analítica de custos da operação principal, com subgrupos e diferentes direcionadores de custo.

### Limite da evidência

Algumas fórmulas e rótulos exigem explicação do especialista antes de qualquer consolidação. Percentuais como 0,6%, 1%, 5%, 60 meses, 1% de juros e fatores internos não devem ser generalizados.

## 12. Medição

### Fatos observados

Inclui:

- equipe diária;
- amostras;
- batimetria FOS;
- acompanhamento da coleta dos bags;
- subtotal e BDI zerado.

Preço final: R$ 14.204,144.

### Interpretação

Neste modelo, a aba representa custo de serviços de controle, acompanhamento e evidência técnica, não o módulo operacional de boletim de medição do APP.

## 13. Carga e transporte

### Fatos observados

Possui estrutura para:

- carga e transporte a 6 km;
- batimetria;
- acompanhamento FOS.

As quantidades estão vazias e o preço final é zero neste orçamento.

### Interpretação

É um pacote disponível, mas não utilizado no modelo atual. A distância de 6 km aparenta ser premissa específica da obra.

## 14. Desmobilização da draga

### Fatos observados

Inclui equipe, fretes, guindaste, desmontagem e carregamento.

Preço final: R$ 17.310,245.

### Interpretação

Não é simples espelho matemático da mobilização. Possui composição própria.

## 15. Desmobilização do sistema de polímero

### Fatos observados

Inclui equipe, frete, desmontagem e referências a componentes do sistema. O barrilete é novamente referenciado, embora sua quantidade esteja vazia e o custo resultante seja zero nessa linha.

Preço final: R$ 6.808,91.

### Interpretação

Mobilização, operação e desmobilização formam um ciclo de vida operacional, mas cada evento possui composição própria.

## 16. Planilha detalhada de preços

### Fatos observados

A aba recebe custos finais das demais composições e aplica BDI comercial por item.

Itens utilizados:

- mobilização da draga;
- mobilização do equipamento de polímero e barrilete;
- preparo de célula;
- fornecimento de bags;
- dragagem e operação do sistema de polímero;
- medição;
- desmobilização da draga;
- desmobilização do sistema de polímero.

BDIs observados:

- 60% para a maioria dos itens;
- 45% para fornecimento de bags.

Resultados:

- custo total: R$ 937.711,4870;
- preço de venda: R$ 1.474.158,0945.

### Interpretação

A aba é a consolidação detalhada para formação do preço de venda. Não executa os modelos de engenharia; consome os resultados deles.

## 17. Consolidação comercial simplificada

### Correção de interpretação

A `Planilha1` não é aba residual.

### Fatos observados

Ela consolida a proposta em quatro macroitens:

1. mobilização e montagem dos equipamentos;
2. preparo da célula de desaguamento;
3. dragagem e desaguamento com fornecimento e operação dos geobags;
4. desmobilização dos equipamentos.

Total geral: R$ 1.474.158,0945, igual ao preço de venda da planilha detalhada.

### Interpretação

Existe separação entre composição técnica detalhada e apresentação comercial resumida.

## Padrões observados neste modelo

### Padrão de mão de obra

Várias abas calculam:

```text
quantidade × valor-hora × horas/dia × (1 + encargos)
```

Depois somam refeições e transporte para obter custo diário da equipe.

### Padrão de pacote

Muitos pacotes seguem:

```text
equipe
+ materiais
+ serviços e terceiros
= subtotal
+ BDI
= preço final
```

### Direcionadores de custo observados

- tempo: equipe, canteiro e operação;
- volume: dragagem e transporte;
- massa seca: polímero;
- área: preparo da célula;
- quantidade: fornecimento de bags;
- evento único: mobilização e desmobilização;
- valor de equipamento: manutenção, depreciação e juros.

### Dependências relevantes

- `Dados Obra` alimenta Produção e diversos custos diários;
- Produção alimenta prazo e custos por duração;
- Barrilete alimenta mobilização/desmobilização do sistema de polímero;
- Bags alimentam tonelada seca e quantidade de polímero;
- Canteiro alimenta Dragagem;
- Operação do sistema alimenta Dragagem;
- Dragagem e demais pacotes alimentam a planilha detalhada;
- a planilha detalhada alimenta a consolidação comercial.

## Inconsistências e alertas observados

- Existem fórmulas `#NAME?` no canteiro e em cálculos de prazo importados.
- Alguns títulos e numerações de abas não coincidem com o conteúdo ou repetem números.
- Há BDI em níveis diferentes: dentro de algumas composições, na Dragagem e na planilha comercial.
- Diversos valores e percentuais estão diretamente embutidos nas fórmulas.
- Algumas linhas existem, mas estão zeradas ou sem quantidade.
- Há preços com observações de fornecedor e datas, sem estrutura formal de data-base.
- Não existe separação explícita entre valor sugerido, valor adotado e valor realizado.
- O arquivo contém referências a preços e práticas de anos diferentes.

Esses pontos não são classificados como erros de negócio sem validação. Devem ser tratados como evidência a investigar.

## Modelo conceitual provisório

A evidência deste primeiro arquivo sugere, sem ainda consolidar:

```text
Empreendimento e premissas
        ↓
Modelos de engenharia
        ↓
Sistemas operacionais
        ↓
Pacotes e subpacotes
        ↓
Recursos e direcionadores de custo
        ↓
Consolidação detalhada
        ↓
Apresentação comercial
```

### Hipótese para crosscheck

O sistema orçamentário poderá ser composto por elementos reutilizáveis, mas esta hipótese só poderá ser confirmada comparando outros tipos de obra.

## Conhecimento candidato à base histórica

Não consolidado, mas candidato a registro histórico:

- produção sugerida e produção efetivamente adotada;
- eficiência e concentração;
- consumo de polímero por material e equipamento de desaguamento;
- capacidade efetiva dos modelos de bags;
- coeficientes de preparo de célula;
- composição e desempenho de equipes;
- consumo e manutenção de equipamentos;
- preços cotados, fornecedor e data-base;
- orçamento, realizado e desvio após execução.

## Próximo passo

Analisar integralmente os próximos modelos de orçamento usando a mesma classificação de evidências.

Após quantidade suficiente de modelos:

1. executar crosscheck horizontal;
2. identificar núcleo comum e variações;
3. classificar exceções;
4. consolidar o Método de Orçamento FOS;
5. somente então definir a arquitetura do sistema orçamentário.