# Modelo 002 — Dragagem e Desaguamento por Centrífugas — Suzano/Jacareí

## Status

- **Status da análise:** engenharia reversa vertical concluída para o arquivo analisado.
- **Data da análise:** 2026-07-14.
- **Arquivo:** `FINAL Composição - Jacarei .xlsx`.
- **Versão declarada no arquivo:** não identificada. O nome contém `FINAL`; a proposta interna é `D_026_2024`.
- **Quantidade de abas:** 13.
- **Implementação funcional:** nenhuma.
- **Consolidação com outros orçamentos:** nenhuma.
- **Documento exclusivo:** este registro contém somente evidências deste Excel.

## Classificação

### EVIDÊNCIA CONFIRMADA

- **Tipo aparente:** orçamento de dragagem e desidratação/desaguamento de lodo de ETE por centrifugação.
- **Processo operacional:** dragagem hidráulica, recalque, alimentação de planta de desaguamento com três centrífugas, operação da draga e da planta, mobilização, canteiro e desmobilização.
- **Área de atuação:** saneamento/indústria de papel e celulose, em instalação da Suzano.
- **Material:** lodo de ETE.
- **Forma comercial:** mobilização e desmobilização por verba; operação apresentada em tonelada desaguada e também calculada por volume dragado.
- **Cliente indicado:** Suzano.
- **Local indicado dentro da aba `Dados Obra`:** Suzano - SP.
- **Nome do arquivo:** contém `Jacarei`.

### EVIDÊNCIA PARCIAL

- O arquivo aparenta ter sido adaptado de outros orçamentos: existem títulos e observações herdados, como `Preço Aracruz REVISÃO FINAL`, referências a `VALE Vitória`, `GRATT (COMPRA ARACRUZ)` e títulos de mobilização da draga usados também nas abas de centrífuga.
- A classificação geográfica como Jacareí decorre do nome do arquivo e da coluna `Preço Suzano Jacareí`, mas a aba de dados registra apenas `Suzano - SP`.

### DÚVIDA

- Não há confirmação textual inequívoca de que a unidade industrial seja Suzano Jacareí.
- Não há confirmação da data-base de todos os preços.
- Não há identificação explícita do autor, revisor ou número de revisão.

## Regra de evidência usada neste documento

- **EVIDÊNCIA CONFIRMADA:** conteúdo, valor, fórmula, dependência ou erro diretamente observado no Excel.
- **EVIDÊNCIA PARCIAL:** padrão ou interpretação observada somente neste arquivo.
- **DÚVIDA:** significado não demonstrado com segurança pelo arquivo.

## Inventário das abas

| Ordem | Aba | Dimensão observada | Papel no orçamento |
| --- | --- | --- | --- |
| 1 | `Dados Obra` | A1:S28 | Identificação, premissas de produção, volumes, sólidos, prazo, recalque e regime de trabalho. |
| 2 | `Fornecedores` | A1:F15 | Cotações de guindaste de 100 t e estrutura iniciada para containers. |
| 3 | `Produção (NOVO CALCULO)` | A1:S29 | Cenários de capacidade das centrífugas, turnos, horas úteis e produção em base seca. |
| 4 | `1. Canteiro` | A1:N33 | Custo de implantação/canteiro apropriado mensalmente ao prazo. |
| 5 | `2.1 Mob Draga` | A1:M42 | Mobilização da draga e infraestrutura geral. |
| 6 | `2.2 Mob Centr` | A1:M42 | Mobilização da planta/centrífugas e instalações elétricas. |
| 7 | `4.1 Draga Dec` | A1:L206 | Composição mensal e total da operação de dragagem. |
| 8 | `4.2 Centrífuga` | A1:R205 | Composição mensal e total da operação do sistema de desaguamento/decanter. |
| 9 | `5. Desmob Canteiro` | A1:N33 | Estrutura de desmobilização do canteiro; cálculo final quebrado. |
| 10 | `Desmob Draga` | A1:M43 | Desmobilização da draga e equipamentos associados. |
| 11 | `Desmob Centr` | A1:M42 | Desmobilização da planta de centrífugas. |
| 12 | `Plan. Final` | A1:O16 | Consolidação de custos, BDI, preços unitários e totais. |
| 13 | `Final` | A1:N20 | Apresentação comercial e comparações com referências de Aracruz/Jacareí. |

## Fluxo e dependências observados

```text
Dados Obra
   ├── Produção (NOVO CALCULO)
   ├── 1. Canteiro
   ├── 4.1 Draga Dec
   ├── 4.2 Centrífuga
   └── Plan. Final / Final

1. Canteiro
   ├── 2.1 Mob Draga
   ├── 2.2 Mob Centr
   ├── Desmob Draga
   └── Desmob Centr

2.1 Mob Draga ─┐
2.2 Mob Centr ─┤
4.1 Draga Dec ─┤
4.2 Centrífuga ┤── Plan. Final ── Final
Desmob Draga ──┤
Desmob Centr ──┘
```

### EVIDÊNCIA CONFIRMADA

- O arquivo é uma rede de composições, não apenas uma sequência linear.
- Salários e quantidades de turnos do canteiro são reutilizados nas mobilizações e desmobilizações.
- Os custos totais de cada pacote alimentam `Plan. Final`.
- `Final` consome preços agrupados de `Plan. Final`, aplica quantidades comerciais e calcula comparações adicionais.
- Algumas fórmulas usam referências com o nome textual `'Dados Obra '` contendo espaço final, embora a aba exibida seja `Dados Obra`; o arquivo importado preservou essas fórmulas e os valores calculados.

## 1. Aba `Dados Obra`

### Identificação

- Título: `SUZANO - SUZANO`.
- Proposta: `Proposta D_026_2024`.
- Data serial do Excel: `45454`.
- Cliente: `SUZANO`.
- Contatos: `Jorge / Camila`.
- Objeto: `Dragagem e desidratação de lodo`.
- Local: `Suzano - SP`.
- Material: `Lodo de ETE`.
- Tipo de bota-fora/processo: `CENTRÍFUGA`.
- Medição: `preços unitários de serviços`.
- Canteiro: responsabilidade FOS.
- Mobilização: responsabilidade FOS.
- Regime: 16 h/dia e 26 dias/mês.

### Premissas e resultados

- Produção mínima desejada: 611 t desaguadas/mês.
- Total desejado: 3.055 t desaguadas.
- Sólidos in situ: 2%.
- Sólidos desaguados no bloco principal: 20%.
- Volume mensal estimado: 6.110 m³.
- Prazo: 5 meses.
- Volume total: 30.550 m³.
- Base seca: 611 t.
- Distância de recalque informada: 350 m.
- Linha flutuante: 150 m.
- Linha de terra: 200 m.
- No memorial lateral, aparecem 100 m de linha flutuante, 150 m de linha de terra e 250 m de recalque.
- No memorial lateral, a conversão usa 15% de sólidos desaguados, produzindo 4.073,333 m³ de lodo desaguado.

### Fórmulas principais

- `M8 = (M5 × M7) ÷ M6`.
- `M10 = M8 × M9`.
- `O5 = (M10 × M6) ÷ M7`.
- `P9 = M10 × M6`.
- `O13 = M13 + N13`.
- `Q13 = L13 × P13`.
- `S13 = Q13 ÷ R13`.
- Totais: `Q16 = SOMA(Q13:Q15)` e `S16 = SOMA(S13:S15)`.
- Recalque e linha flutuante totais: valor informado + seio.
- Volume geométrico: multiplicação das dimensões e espessura quando preenchidas.

### Inconsistências

- A observação ao lado de 2% diz `não informado (chutamos 10%)`, mas a célula usada é 2%.
- O bloco superior usa 20% de sólidos desaguados; o memorial de volume usa 15%.
- O volume desaguado correspondente a 611 t é 3.055 m³ a 20%, mas 4.073,333 m³ a 15%.
- O recalque aparece como 350 m nos dados gerais e como 250 m no memorial lateral.
- Profundidade, espessura e área de dragagem estão vazias.
- A data está armazenada como serial, sem texto de versão ou data-base de preços.

## 2. Aba `Fornecedores`

### EVIDÊNCIA CONFIRMADA

Bloco `GUINDASTE - 100 TON`:

- TRUCKAP — telefone `(11) 99847-2900`.
- ENGEGUIND — contato Daniel — telefones `(11) 2033-0015 / (11) 99329-7766`.
  - diária: R$ 6.500;
  - plano de rigger: R$ 1.500;
  - mobilização: R$ 6.000;
  - desmobilização: R$ 6.000;
  - integração antecipada: cortesia.
- SAO JOSE — contato Nairê — telefones `(11) 2238-4444 / (11) 2238-4441`.
  - diária: R$ 6.500;
  - mobilização: R$ 6.500;
  - desmobilização: R$ 6.500.

O bloco `CONTAINER` possui apenas cabeçalho, sem fornecedores preenchidos.

### EVIDÊNCIA PARCIAL

- A aba funciona como registro de cotação de mercado, mas não possui data explícita por linha.
- Os valores de guindaste são coerentes com preços usados nas composições de mobilização.

## 3. Aba `Produção (NOVO CALCULO)`

### Estrutura observada

- Capacidade nominal por centrífuga: 40 m³/h.
- Cenário com 3 centrífugas: 120 m³/h.
- Comentário técnico: `20 metros de skid - centrifuga de 60M3/h`.
- Dias de operação: 26.
- Sólidos desaguados: 20%.
- Horário-base: 16 h.
- Fator de disponibilidade/eficiência: 85%.
- Tempo útil calculado: 13,6 h/dia.
- Horas mensais trabalhadas: 436,8 h/mês.

### Cenários de produção em base seca

A tabela final combina concentrações de 0,7%, 3%, 4% e uma coluna adicional:

- 0,7% e 40 m³/h: 0,28 t base seca/h; 1,4 t/h de material a 20%; 23,52 t/dia; 611,52 t/mês.
- 3% e 40 m³/h: 1,2 t base seca/h; 6 t/h; 100,8 t/dia; 2.620,8 t/mês.
- 4% e 40 m³/h: 1,6 t base seca/h; 8 t/h; 134,4 t/dia; 3.494,4 t/mês.
- Coluna adicional: 3,528 t/dia e 91,728 t/mês.

### Fórmulas e lógica

- Capacidade total = capacidade unitária × quantidade de centrífugas.
- Tempo útil é derivado das janelas de turno e higienização.
- Horas mensais = tempo útil diário × 26 dias.
- Tonelada seca/h = vazão × concentração.
- Tonelada de material desaguado/h = tonelada seca/h ÷ 20%.
- Produção diária = produção horária × tempo útil.
- Produção mensal = produção diária × 26 dias.

### Erro confirmado

- `S10` contém `#REF!` com fórmula `#REF! - S9`.

### DÚVIDAS

- O arquivo menciona simultaneamente uma centrífuga de 40 m³/h, três centrífugas de 40 m³/h e centrífuga de 60 m³/h.
- Não está explicitado qual cenário foi adotado comercialmente.
- A relação entre 611 t/mês da aba `Dados Obra` e 611,52 t/mês desta aba indica aproximação, mas não há regra de arredondamento documentada.

## 4. Aba `1. Canteiro`

### Equipe diária

- 1 encarregado.
- 1 técnico de segurança.
- 2 operadores de draga.
- 6 operadores de centrífuga.
- 10 ajudantes gerais.
- Total de 20 pessoas para refeição e transporte.
- Encargos sociais: 110%.
- Jornada usada na composição: 9 h/dia.
- Custo diário total: R$ 6.762,043.

### Infraestrutura e serviços

- Container almoxarifado: 5 meses × R$ 1.200.
- Container sanitário/vestiário: 5 × R$ 1.700.
- Container escritório: 5 × R$ 1.700.
- Material de limpeza: 5 × R$ 1.000.
- Material de escritório: 5 × R$ 300.
- Banheiro químico: 5 × R$ 2.000.
- Integração/mão de obra: 8 dias × R$ 6.762,043.

### Resultados

- Total: R$ 93.596,344.
- Prazo apropriado: 5 meses.
- Custo unitário mensal: R$ 18.719,2688.
- BDI interno: 0%.
- Preço final mensal: R$ 18.719,2688.

### Tabelas auxiliares

- Mobiliário com referência `Preços VALE Vitória`.
- Mesa, mesa redonda, cadeiras, armários, cestos e bebedouro somam R$ 10.000.
- Referências de tendas: fornecedor `Tendas Paraná`, contato por WhatsApp em 16/01/24, dimensões 6×6 e 4×4, com preços por altura.

### Regras

- Custo de mão de obra = quantidade × salário/hora × 9 h × (1 + 110%).
- Refeição e transporte = número de pessoas × preço unitário.
- Custo mensal do canteiro = total de implantação ÷ prazo.

## 5. Aba `2.1 Mob Draga`

### Equipe e turnos

- 1 líder, 1 técnico, 3 operadores de draga, 3 operadores de centrífuga e 12 ajudantes.
- Três turnos para operadores e ajudantes.
- 20 refeições e transportes.
- Custo diário: R$ 6.636,358.

### Itens com valores ativos

- Treinamentos: R$ 3.000.
- 3 carretas para draga: R$ 15.000.
- Munck: R$ 2.000.
- Frete de 3 containers: R$ 3.600.
- Mobiliário do canteiro: R$ 13.500.
- Mobiliário do alojamento: R$ 13.500.
- Materiais de segurança: R$ 5.000.
- PGR + PCMSO + LTCAT: R$ 5.000.
- ART principal e corresponsáveis: R$ 500.
- 10 tendas: R$ 56.000.
- Bebedouro: R$ 5.000.
- 20 exames médicos: R$ 7.000.
- Mão de obra de mobilização: 22 dias × R$ 6.636,358 = R$ 145.999,876.

### Resultado

- Total e preço final: R$ 275.099,876.
- BDI interno: 0%.
- Quantidade logística: 3 carretas, detalhadas como 2 para draga e 1 para tubulação.

### Observações

- Alguns itens possuem preços preenchidos, mas quantidade vazia e, portanto, total zero.
- A descrição do título inclui `DRAGA ELETRICA OU MIUDA`, sinal de reaproveitamento de modelo.

## 6. Aba `2.2 Mob Centr`

### Equipe

- 1 líder, 1 técnico, 4 operadores de centrífuga e 2 ajudantes.
- Custo diário: R$ 2.973,613.

### Valores ativos

- 1 carreta: R$ 5.000.
- Instalações elétricas: 10 dias × R$ 1.500 = R$ 15.000.
- Materiais elétricos: R$ 8.000.
- 6 exames: R$ 2.100.
- 2 carretas de complemento: R$ 10.000.
- Mão de obra: 22 dias × R$ 2.973,613 = R$ 65.419,486.

### Resultado

- Total e preço final: R$ 105.519,486.
- BDI interno: 0%.
- Quadro logístico indica 2 carretas, embora uma linha de carreta principal e duas diárias de carreta complementar coexistam.

## 7. Aba `4.1 Draga Dec`

### Papel

Centro de custo mensal da dragagem. A aba combina operações, pessoal, manutenção, equipamentos de apoio, linha de recalque, despesas administrativas, BDI, despesas financeiras, resumo e apropriação por prazo.

### Categorias confirmadas

1. Operação:
   - combustível;
   - filtros/lubrificantes;
   - fretes e carretos;
   - materiais de segurança;
   - outros insumos operacionais.
2. Pessoal:
   - salários por função;
   - horas extras;
   - encargos sociais de 110%;
   - cantina;
   - alojamento;
   - viagens em folgas;
   - prêmios de produção.
3. Manutenção:
   - peças e acessórios;
   - docagem;
   - limpeza e pintura;
   - terceiros.
4. Apoio:
   - automóveis;
   - ferramentas;
   - plano de saúde;
   - equipamentos;
   - linha de recalque.
5. Administrativas.
6. BDI interno.
7. Financeiras:
   - depreciação;
   - juros de capital;
   - atrasos.

### Resultados confirmados

- Despesas diretas: R$ 205.600,402863412.
- BDI interno: R$ 20.560,0402863412.
- Financeiras: R$ 14.666,6666666667.
- Custo mensal total: R$ 262.767,069529702.
- Prazo: 5 meses.
- Custo total da dragagem: R$ 1.313.835,347648511.
- Multiplicador comercial lateral: 1,6.
- Preço de venda mensal lateral: R$ 420.427,311247524.
- Horas trabalhadas/mês: 436,8.
- Fator: 0,7.
- Preço/hora: R$ 673,761716742826.

### Erros confirmados

- Produção prevista em `D178`: `#REF!`.
- Bloco de hora à disposição usa referências quebradas em `H188`, `I188` e `J188`.
- Apesar do erro em produção prevista, o custo total de 5 meses permanece calculado a partir do custo mensal.

### EVIDÊNCIA PARCIAL

- O título abreviado `Draga Dec` e a presença de custos de decanter em algumas áreas sugerem que a planilha foi adaptada e que limites entre dragagem e desaguamento não estão totalmente limpos.

## 8. Aba `4.2 Centrífuga`

### Identificação e ativos

- Título: `CUSTO DE DESAGUAMENTO - DECANTER`.
- Referência: dragagem de lagoa com desaguamento em centrífugas.
- Cliente: Suzano.
- Equipamento: centrífuga.
- Valor do equipamento `no estado`: R$ 1.500.000.
- Ativos auxiliares listados:
  - tanque de equalização FOS: R$ 100.000;
  - tanque de preparo de polímero: R$ 80.000;
  - bomba de transferência: R$ 50.000;
  - bomba de polímero: R$ 20.000;
  - GRATT skid: 3 unidades e total de R$ 4.500.000;
  - referência `GRATT (COMPRA ARACRUZ)` de R$ 1.200.000.

### Operação mensal

- Horas: 436,8.
- Eficiência: 90%.
- Custos operacionais exibidos: R$ 3.100,039312.

### Pessoal

- 9 ajudantes a R$ 10,50/h.
- 5 operadores de decanter a R$ 17,50/h.
- Salários: R$ 50.996,3818.
- Encargos de 110%: R$ 56.096,01998.
- Cantina: R$ 17.190.
- Alojamento: R$ 4.100.
- Viagens de folga: R$ 2.500.
- Total de pessoal mostrado em área auxiliar: R$ 130.882,40178.

### Manutenção e apoio

- Manutenção: R$ 8.500/mês.
- Apoio inclui 2 automóveis, mangote canaflex, ferramentas e plano de saúde.
- Linha de recalque:
  - tubulação;
  - flutuantes;
  - acoplamentos;
  - apropriação de depreciação e juros.
- Total mensal da linha de recalque: R$ 2.692,27777778.

### BDI e financeiras

- Despesas diretas: R$ 159.082,441092.
- Oficina 5%: R$ 7.954,1220546.
- Administração 5%: R$ 7.954,1220546.
- BDI interno total: R$ 15.908,2441092.
- Depreciação em 60 meses: R$ 25.000.
- Juros de capital de 0,5%: R$ 7.500.
- Financeiras: R$ 32.500.

### Resultados

- Custo mensal: R$ 207.490,6852012.
- Produção prevista: 3.825,36 m³/mês.
- Prazo: 5 meses.
- Total da operação: R$ 1.037.453,426006.
- Multiplicador lateral: 1,6.
- Preço de venda mensal lateral: R$ 331.985,09632192.
- Horas/mês: 436,8.
- Fator: 0,7.
- Preço/hora: R$ 532,027397951795.

### Erro confirmado

- `D187`, hora à disposição, contém `#REF! × 0,6 × 0,62`.

### Inconsistências

- O custo de manutenção de 0,1% sobre R$ 1,5 milhão deveria ser R$ 1.500, mas a linha mostra R$ 7.500, equivalente a 0,5%.
- O ativo GRATT aparece com valores de R$ 1,2 milhão, R$ 1,5 milhão unitário e R$ 4,5 milhões total, sem indicação inequívoca de qual base alimenta depreciação e juros.
- O custo unitário e preço de venda por m³ no bloco principal permanecem vazios/zero, enquanto o preço/hora lateral é calculado.

## 9. Aba `5. Desmob Canteiro`

### Estrutura

- Replica equipe, salários, encargos, refeições e transporte do canteiro.
- Possui estrutura de itens mensais e mão de obra de integração.
- Total dos itens ativos é zero porque as quantidades foram deixadas vazias.

### Erros confirmados

- `F30`, prazo, é `#REF!`.
- `F31 = F29 ÷ F30` resulta `#REF!`.
- `F32` e `F33` propagam o erro.
- Preço final da aba é `#REF!`.

### Consequência

- Esta aba não alimenta a consolidação final.
- A desmobilização comercial usada no preço vem das abas `Desmob Draga` e `Desmob Centr`.

## 10. Aba `Desmob Draga`

### Equipe e logística

- Equipe diária: 1 líder, 1 técnico, 2 operadores de draga, 2 operadores de centrífuga e 8 ajudantes.
- 14 pessoas para refeição e transporte.
- Custo diário: R$ 4.742,143.
- Logística: 9 carretas:
  - 3 para draga;
  - 2 para 1.500 m de tubulação;
  - 1 para flutuantes/periféricos;
  - 3 para draga elétrica.

### Itens ativos

- 9 carretas: R$ 45.000.
- Munck: R$ 2.000.
- Frete de 3 containers: R$ 3.600.
- 14 exames: R$ 4.900.
- Mão de obra de 22 dias: R$ 104.327,146.

### Resultado

- Total e preço final: R$ 159.827,146.
- BDI interno: 0%.

## 11. Aba `Desmob Centr`

### Equipe e logística

- 4 operadores de centrífuga e 2 ajudantes.
- Custo diário: R$ 2.019,90.
- 5 carretas no quadro logístico:
  - skid 1;
  - skid 2;
  - skid 3;
  - 2 para tanques de equalização/periféricos.

### Itens ativos

- Instalações elétricas: 2 dias × R$ 1.500 = R$ 3.000.
- 6 exames: R$ 2.100.
- 5 carretas: R$ 25.000.
- Mão de obra: 22 dias × R$ 2.019,90 = R$ 44.437,80.

### Resultado

- Total e preço final: R$ 74.537,80.
- BDI interno: 0%.

## 12. Aba `Plan. Final`

### Composição consolidada

| Componente | Custo | BDI | Preço |
| --- | ---: | ---: | ---: |
| Mobilização draga | R$ 275.099,876 | 70% | R$ 467.669,7892 |
| Mobilização centrífuga | R$ 105.519,486 | 70% | R$ 179.383,1262 |
| Dragagem | R$ 1.313.835,347648511 | 75% | R$ 2.299.211,858384895 |
| Operação centrífuga | R$ 1.037.453,426006 | 75% | R$ 1.815.543,4955105 |
| Desmobilização draga | R$ 159.827,146 | 70% | R$ 271.706,1482 |
| Desmobilização centrífuga | R$ 74.537,80 | 70% | R$ 126.714,26 |

### Totais

- Custo total: R$ 2.966.273,081654511.
- Preço de venda total: R$ 5.160.228,677495394.
- Mobilização agrupada: R$ 647.052,9154.
- Desmobilização agrupada: R$ 398.420,4082.
- Preço unitário agrupado de dragagem + centrífuga: R$ 6.734,460481007192 por tonelada.
- Custo agrupado de dragagem + centrífuga: R$ 3.055. uma referência lateral também mostra 17.000 m³ e `volume desaguado (15%)`.
- Preço por volume lateral: R$ 1.346,89209620144 por m³ em uma célula e R$ 242,044432582082 em outra, conforme divisores diferentes.
- Preço total dividido por 611 t: R$ 8.445,546117013739.

### Fórmulas principais

- Custo unitário = custo total ÷ quantidade.
- Preço unitário = custo unitário × (1 + BDI).
- Preço total = quantidade × preço unitário.
- Mobilização e desmobilização são somadas em células agrupadoras.
- Dragagem e centrífuga são somadas para formar preço unitário combinado.
- Custo e preço total são somas das linhas componentes.

### Inconsistências

- A quantidade operacional usada é 611 t, mas `Final` usa 139.200 t.
- A linha lateral contém 17.000 m³, valor não rastreado diretamente às premissas de 30.550 m³, 3.055 m³ ou 4.073,333 m³.
- O preço unitário agrupado de R$ 6.734,46 é composto por duas parcelas: dragagem e centrífuga.

## 13. Aba `Final`

### Estrutura comercial

1. Mobilização e montagem dos equipamentos de dragagem e complemento da planta:
   - quantidade: 1 verba;
   - preço: R$ 647.052,9154.
2. Dragagem e desaguamento por centrifugação + manutenção de estrutura:
   - unidade: tonelada desaguada;
   - quantidade: `2400 × 58 = 139.200`;
   - preço unitário: R$ 6.734,460481;
   - preço total calculado: R$ 937.436.898,956201.
3. Desmobilização:
   - quantidade: 1 verba;
   - preço: R$ 398.420,4082.

### Totais e indicadores

- Valor total calculado: R$ 938.482.372,279801.
- Soma dos preços unitários/agrupados: R$ 1.045.473,3236.
- Custo total importado: R$ 2.966.273,081654511.
- Relação preço/custo: 316,384347%.
- Preço total por tonelada: R$ 6.741,971065.
- Preço por volume dragado e centrifugado: R$ 30.685,332208 para divisor de 30.550 m³.
- Cenário de 40%:
  - quantidade: 55.680;
  - preço resultante: R$ 16.836,151203.

### Referências comparativas

- Coluna `Preço Aracruz REVISÃO FINAL`.
- Coluna `Preço Suzano Jacareí`.
- Mobilização de referência Jacareí: R$ 259.001,28.
- Operação de referência: 1.947 t e 97,35 m³.
- Desmobilização de referência Jacareí: R$ 197.185,01.
- Observação:
  - na condição considerada errônea de medição de uma obra, foi praticado R$ 980/t SS, descrito como 50% do preço, com resultado de 15%.

### Inconsistência crítica

A quantidade `139.200` toneladas desaguadas não corresponde às premissas centrais:

- produção desejada: 611 t/mês;
- prazo: 5 meses;
- total: 3.055 t;
- cálculo comercial: 2.400 × 58.

O preço total de aproximadamente R$ 938 milhões decorre diretamente dessa quantidade. O arquivo não explica o significado de 2.400 e 58. Portanto:

- o valor total comercial não pode ser tratado como validado;
- a fórmula deve ser preservada como evidência do arquivo;
- não há base para corrigir ou substituir o valor nesta análise.

## Fórmulas e regras transversais

### Mão de obra

```text
custo da função =
quantidade de pessoas
× salário-hora
× horas/dia
× (1 + encargos sociais)
```

- Encargos usados nas composições de campo: 110%.
- Adicional de 25% aparece em tabelas auxiliares de salário.
- Jornada diária predominante na mão de obra: 9 h.
- Regime operacional global: 16 h/dia.
- Horas úteis do processo: 13,6 h/dia.
- Horas mensais: 436,8 h.

### Eventos únicos

```text
preço total do item = quantidade × preço unitário
```

Aplicado a carretas, guindastes, materiais, exames, instalações, tendas e outros itens.

### Custos mensais e prazo

```text
custo total da operação = custo mensal × prazo
```

Prazo central: 5 meses.

### BDI comercial

- Mobilização/desmobilização: 70%.
- Operação: 75%.
- Blocos internos de composição geralmente usam BDI 0%, 10% ou multiplicador lateral de 1,6.
- O arquivo usa tanto percentual explícito quanto fator multiplicativo, sem uma única camada homogênea.

### Produção

```text
tonelada seca/h = vazão × concentração de sólidos
tonelada desaguada/h = tonelada seca/h ÷ concentração final
produção mensal = produção horária × horas úteis/dia × dias/mês
```

### Depreciação e capital

- Centrífuga: depreciação em 60 meses.
- Juros de capital: 0,5% ao mês.
- Linha de recalque: depreciação e juros por componente.
- Não há data de aquisição nem valor residual.

## Entidades encontradas

### Comerciais

- Proposta.
- Cliente.
- Contato.
- Objeto.
- Local.
- Item comercial.
- Unidade de medição.
- Quantidade.
- Custo.
- BDI.
- Preço unitário.
- Preço total.
- Referência comparativa de obra.

### Técnicas

- Obra.
- Lagoa de polimento.
- Lodo de ETE.
- Volume dragado.
- Percentual de sólidos in situ.
- Percentual de sólidos desaguados.
- Tonelada seca.
- Tonelada desaguada.
- Distância de recalque.
- Linha flutuante.
- Linha terrestre.
- Draga.
- Centrífuga/decanter.
- Skid.
- Tanque de equalização.
- Sistema de polímero.
- Linha de recalque.
- Canteiro.

### Recursos e custos

- Função de mão de obra.
- Turno.
- Salário-hora.
- Encargos.
- Refeição.
- Transporte.
- Alojamento.
- Exames.
- Treinamentos.
- Carreta.
- Guindaste.
- Munck.
- Container.
- Tenda.
- Mobiliário.
- Materiais.
- Manutenção.
- Depreciação.
- Juros.
- Fornecedor.
- Cotação.

## Terminologia observada

- `SS`: sólidos secos/base seca, conforme contexto.
- `% ST is`: percentual de sólidos totais in situ.
- `% ST des`: percentual de sólidos após desaguamento.
- `Ton des`: tonelada desaguada.
- `vb`: verba.
- `MDO`: mão de obra.
- `L. Sociais`: leis/encargos sociais.
- `Decanter`: centrífuga de desaguamento.
- `Mob` e `Desmob`: mobilização e desmobilização.
- `Hora à disposição`: preço associado à disponibilidade do equipamento/equipe.
- `Fator 0,7`: fator usado na apropriação do preço por hora, sem definição textual.

## Padrões observados neste orçamento

### EVIDÊNCIA PARCIAL

- Separação de mobilização/desmobilização entre draga e planta.
- Canteiro tratado como subitem mensal da dragagem.
- Custos de operação organizados pelo modelo clássico: operação, pessoal, manutenção, apoio, administrativas, BDI e financeiras.
- Preço comercial final reduzido a três macroitens.
- Uso de tabelas auxiliares laterais nas próprias abas para salários, turnos, logística, mobiliário e ativos.
- Células vazias são usadas para desativar itens, mantendo preços de referência no modelo.
- BDI interno das mobilizações é zero; BDI comercial é aplicado na consolidação.
- A planilha preserva valores e comentários de outras obras como referência.

## Exceções e anomalias

### EVIDÊNCIA CONFIRMADA

1. Referências `#REF!` em quatro abas.
2. Concentração final de sólidos divergente: 15% e 20%.
3. Concentração in situ de 2% acompanhada de observação sobre 10%.
4. Recalque divergente: 250 m e 350 m.
5. Cenários de centrífuga divergentes: 40 m³/h, 3×40 m³/h e menção a 60 m³/h.
6. Quantidade comercial de 139.200 t divergente do total de 3.055 t.
7. Referências misturadas a Aracruz, VALE Vitória, Suzano e Jacareí.
8. Títulos copiados entre abas de draga e centrífuga.
9. Bloco de desmobilização do canteiro quebrado e não usado na consolidação.
10. Células de preço por m³ vazias/zeradas em composições que possuem preço/hora lateral.
11. Datas de cotações aparecem apenas em observações pontuais.
12. Alguns itens possuem preço mas quantidade vazia, resultando em custo zero.
13. BDI é usado em diferentes níveis e formatos.
14. O preço total comercial final é matematicamente válido em relação à fórmula, mas não coerente com as premissas de quantidade.

## Dúvidas para validação futura com o especialista

1. O arquivo é efetivamente da unidade Suzano Jacareí?
2. Qual é o percentual de sólidos in situ adotado: 2%, 3,5%, 10% ou outro?
3. Qual é o percentual final de sólidos desaguados: 15% ou 20%?
4. Qual volume deve reger o orçamento: 30.550 m³, 17.000 m³, 6.110 m³/mês ou outro?
5. O total comercial correto é 3.055 t desaguadas?
6. O que representam `2400 × 58 = 139.200` na aba `Final`?
7. Quantas centrífugas e qual capacidade nominal foram efetivamente consideradas?
8. A linha de recalque é 250 m ou 350 m?
9. O canteiro deve ser cobrado mensalmente dentro da dragagem ou como item separado?
10. A desmobilização do canteiro foi intencionalmente excluída?
11. O fator 0,7 no preço/hora representa disponibilidade, produtividade ou margem de segurança?
12. O multiplicador 1,6 é BDI de 60% ou outra composição?
13. O valor de manutenção da centrífuga deveria usar 0,1% ou 0,5%?
14. Quais preços de Aracruz/VALE são apenas referência histórica e quais foram usados na proposta?
15. A medição contratual é por tonelada seca, tonelada desaguada ou volume dragado?

## Limitações da análise

- O arquivo foi lido sem alteração.
- Foram analisadas as 13 abas, valores e fórmulas disponíveis.
- Formatação, cores e formas auxiliares foram consideradas apenas quando afetavam o significado; não foram reproduzidas.
- Não foram encontradas tabelas estruturadas nem nomes definidos.
- Foram observadas duas formas gráficas de chave nas abas de operação, sem conteúdo lógico adicional.
- A análise não corrige fórmulas quebradas.
- A análise não valida preços com fontes externas.
- A análise não compara este orçamento com outros modelos.
- Não foi possível inferir, com segurança, significados não escritos no arquivo.

## Validação do Kid Step

- [x] Todas as abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Conhecimento técnico, comercial, fórmulas, dependências, exceções e erros preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma funcionalidade criada.
- [x] Nenhum índice geral ou documento de consolidação alterado.
