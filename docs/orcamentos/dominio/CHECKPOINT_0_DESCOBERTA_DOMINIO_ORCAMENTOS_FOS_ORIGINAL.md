# CHECKPOINT 0 — DESCOBERTA DO DOMÍNIO DE ORÇAMENTOS FOS

**Data da verificação:** 28/08/2026  
**Escopo:** mineração histórica 2015–2026  
**Modo:** somente leitura  
**Resultado:** checkpoint concluído; mineração pesada não iniciada

## 1. Resumo executivo

A estrutura histórica descrita na missão foi confirmada. As pastas `Obras 2015` a `Obras 2026` estão diretamente dentro da pasta correta `Obras`, que por sua vez está dentro de `FOS OBRAS _ BACCKUP`.

O achado central é que a campanha anterior produziu **158 fichas de auditoria individual**, mas elas foram salvas fora da árvore formal `MERLIN — Base de Conhecimento das Obras`, em um diretório alternativo. A árvore formal contém apenas a metodologia e o inventário inicial de 2026; as áreas de análises, padrões, decisões e evidências estão vazias.

As 158 fichas não representam 158 obras independentes nem 158 análises profundas. Existem cenários e revisões repetidos, 51 fichas declaram ausência de planilha e várias outras apenas inventariam arquivos `.xls` sem ler abas ou fórmulas. A campanha anterior realizou grande volume de triagem, sobretudo em 2015 e 2016, mas não chegou à consolidação transversal, à matriz Obras × Blocos, ao catálogo normalizado nem ao mapa final do domínio.

O inventário atual observou **573 pastas de primeiro nível** e **pelo menos 1.069 arquivos Excel**. Esses números são universo bruto, não contagem de obras ou orçamentos: incluem agregadores, planilhas auxiliares, temporários, cópias e revisões.

## 2. A — Árvore encontrada

Estrutura confirmada:

```text
FOS OBRAS _ BACCKUP
└── Obras
    ├── Obras 2015
    ├── Obras 2016
    ├── Obras 2017
    ├── Obras 2018
    ├── Obras 2019
    ├── Obras 2020
    ├── Obras 2021
    ├── Obras 2022
    ├── Obras 2023
    ├── Obras 2024
    ├── Obras 2025
    ├── Obras 2026
    ├── MERLIN — Base de Conhecimento das Obras
    ├── Obras Concluídas
    ├── LABORATORIO
    ├── ATIVA - OBRAS ATUAIS
    └── arquivos avulsos
```

Os IDs anuais coincidem com os fornecidos na missão. Existe outra pasta homônima `Obras` em outro local do Drive; por isso os IDs devem continuar sendo usados como referência canônica.

Diferenças e anomalias internas relevantes:

- nomenclatura predominantemente livre em 2015–2020;
- adoção parcial de códigos `D_` e `OP_` a partir de 2021;
- 2022 contém item `D_0XX` e é materialmente menor que os anos vizinhos;
- 2024 contém `D_034_2024 ERRADO D_031_2024` e item com referência a 2023;
- 2025 contém `D_030_2030`, `D_040_2024` e duplicidade nominal de `D_017_2025`;
- 2026 contém duas pastas `D_007_2026`, uma CMPC e outra SABESP Cubatão.

## 3. B — Base Merlin recuperada

A pasta formal `MERLIN — Base de Conhecimento das Obras` possui seis áreas:

1. `00 — Método e Governança` — contém a metodologia;
2. `01 — Inventário do Acervo` — contém o inventário inicial de 2026;
3. `02 — Análises por Obra` — vazia;
4. `03 — Padrões e Famílias` — vazia;
5. `04 — Decisões e Backlog` — vazia;
6. `05 — Evidências e Referências` — vazia.

Foram localizadas **158 auditorias individuais fora dessa árvore**, no diretório alternativo de ID `1mWvgZdexBSQoYMepgrYY42WhehDKKhho`.

A metodologia existente estabelece corretamente:

- cobertura do domínio, não simples volume de planilhas;
- preservação integral das fontes;
- separação entre fatos, interpretações, recorrências, regras de família e exceções;
- interface guiada separada da base configurável e do motor de cálculo;
- versionamento por vigência e snapshot dos parâmetros usados;
- sugestões históricas rastreáveis, sem substituir a decisão do engenheiro;
- BDI, margem e decisões comerciais sob responsabilidade humana.

## 4. C — Cobertura existente

### 4.1 Auditorias localizadas

| Ano | Fichas de auditoria |
|---|---:|
| 2015 | 17 |
| 2016 | 81 |
| 2017 | 0 |
| 2018 | 1 |
| 2019 | 0 |
| 2020 | 2 |
| 2021 | 5 |
| 2022 | 1 |
| 2023 | 5 |
| 2024 | 1 |
| 2025 | 36 |
| 2026 | 3 |
| Sem ano explícito | 6 |
| **Total** | **158** |

O total inclui revisões, cenários e variações da mesma obra. Não deve ser convertido diretamente em quantidade de obras lógicas.

### 4.2 Onde a campanha anterior parou

A cronologia indica:

- amostragem transversal de 2018–2026 em 28–29/07/2026;
- varredura de 2015 entre 29–31/07/2026;
- varredura massiva de 2016 entre 31/07 e 12/08/2026;
- últimos registros: `SANEPAR - PARANAVAÍ` e `AMBEV`, em 12/08/2026.

Conclusão: a campanha parou durante ou ao final da triagem de 2016. Não avançou sistematicamente por 2017–2026 e não consolidou os resultados.

### 4.3 Profundidade real das fichas

- 51 de 158 fichas declaram explicitamente ausência de planilha;
- muitas fichas registram a existência de `.xls`, mas não leem fórmulas ou abas;
- 116 mencionam Excel, incluindo menções negativas ou limitações;
- parte substancial representa triagem documental, não auditoria profunda da memória de cálculo.

### 4.4 Blocos/componentes já evidenciados

As menções existentes evidenciam, sem homologar taxonomia:

- dragagem;
- bags/geobags/células;
- centrífuga/decanter;
- batimetria;
- bombeamento direto e motobomba;
- mobilização e desmobilização;
- barrilete e tubulação;
- polímero;
- destinação;
- paliçada;
- impermeabilização;
- mão de obra, combustível e gerador;
- cronograma, EAP, histogramas e QQP;
- BDI, leis sociais, propostas técnica e comercial;
- locação versus execução;
- venda de equipamentos;
- draga com ou sem equipe e diferentes portes de draga.

Contagens indicativas por menção nas fichas, não por obra normalizada: dragagem 70; mobilização 57; BDI 52; polímero 43; desmobilização 41; bags 37; barrilete 24; mão de obra 20; batimetria 18; cronograma 15; destinação 14; paliçada 12; centrífuga 11; bombeamento 8; impermeabilização 8; combustível 8; laboratório 7; gerador 5; motobomba 1; tubulação 1.

### 4.5 Consolidações existentes

Não foram localizados:

- matriz Obras × Blocos;
- catálogo normalizado de blocos;
- catálogo de dados mestres;
- consolidação transversal;
- mapa final do domínio;
- backlog preenchido de implementação.

As normalizações presentes são implícitas e ainda não homologadas.

## 5. D — Universo bruto 2015–2026

| Ano | Pastas de 1º nível | Excel observados | Possíveis artefatos orçamentários* | Sinais de revisão/cópia* |
|---|---:|---:|---:|---:|
| 2015 | 19 | 10 | 8 | 6 |
| 2016 | 82 | 81 | 66 | 40 |
| 2017 | 29 | 43 | 43 | 21 |
| 2018 | 76 | 64 | 30 | 40 |
| 2019 | 58 | 138 | 168 | 26 |
| 2020 | 80 | 178 | 191 | 125 |
| 2021 | 85 | 185 | 224 | 122 |
| 2022 | 19 | 44 | 37 | 9 |
| 2023 | 14 | 144 | 50 | 31 |
| 2024 | 26 | 54 | 91 | 21 |
| 2025 | 68 | 109 | 220 | 135 |
| 2026 | 17 | 19 | 39 | 4 |
| **Total bruto** | **573** | **1.069** | **1.167** | **580** |

\* Heurística lexical por nomes e caminhos. Um mesmo arquivo pode produzir mais de um sinal, e candidatos incluem propostas, editais e documentos não Excel. Não interpretar como quantidade de obras ou orçamentos.

Limitações de comparabilidade:

- 2015–2018 foram varridos até profundidade 2; os números de Excel são piso;
- 2019–2022 foram varridos recursivamente até quatro níveis;
- 2023–2026 tiveram varredura recursiva completa da fila observada;
- pastas de primeiro nível incluem obras, clientes, agregadores, cadastros e concorrências;
- arquivos `~$`, auxiliares e formulários entram no universo Excel;
- duplicidade foi inferida por nomes, não por hash ou comparação de conteúdo;
- 2022 pode ser acervo incompleto ou migrado, não necessariamente queda real de atividade.

## 6. Famílias aparentes no universo bruto

Estas são evidências para orientar amostragem, não taxonomia oficial:

- dragagem com dragas de diferentes portes;
- dragagem elétrica e dragagem combinada com bomba;
- bags/geobags, inclusive cenários com e sem polímero e em múltiplos níveis;
- centrífuga/decanter em diferentes quantidades e turnos;
- batimetria;
- bombeamento sem dragagem;
- locação de draga, bomba ou motobomba, com e sem equipe;
- venda de draga/equipamento;
- mobilização/desmobilização;
- operação, mão de obra e startup;
- destinação/transporte;
- impermeabilização/cortina;
- limpeza e remoção de vegetação;
- extração de areia;
- serviços em ETA/ETE;
- composições comerciais com BDI, impostos, leis sociais e margem.

## 7. E — Gap

### Isto já foi analisado

- metodologia e princípios arquiteturais iniciais;
- inventário preliminar de 2026;
- 158 fichas de triagem/auditoria, concentradas em 2015, 2016 e 2025;
- diversidade inicial de famílias, cenários e componentes;
- necessidade de base configurável, versionamento, snapshot e sugestões rastreáveis;
- inventário bruto atual das pastas anuais 2015–2026.

### Isto ainda não foi analisado de forma suficiente

- 2017 e 2019: nenhuma ficha anterior;
- 2018, 2020, 2022, 2024 e 2026: cobertura anterior muito pequena;
- 2021 e 2023: cobertura anterior limitada diante do universo;
- deduplicação por obra lógica e linhagem de versões;
- identificação da versão oficial/vencedora de cada proposta;
- leitura sistemática de abas, fórmulas, referências, entradas e saídas;
- classificação Mestre/Contextual/Derivado/Histórico;
- proveniência por campo;
- requisitos de snapshot;
- matriz Obras × Blocos;
- normalização semântica dos blocos;
- catálogos candidatos de blocos e dados mestres;
- campos destinados à inteligência histórica;
- cobertura quantitativa do domínio por família.

### Famílias aparentemente faltantes ou sub-representadas na análise profunda

- venda de equipamento;
- locação com/sem equipe;
- bombeamento isolado e motobomba;
- impermeabilização/cortina;
- limpeza/remoção de vegetação;
- extração de areia;
- operação/startup e mão de obra isolada;
- destinação/transporte como núcleo relevante;
- comparações sistemáticas entre bags com/sem polímero;
- combinações multi-equipamento e múltiplos turnos;
- propostas abertas com BDI, impostos, leis sociais, margem e desconto;
- batimetria como orçamento autônomo;
- obras em que proposta final e memória de cálculo divergem.

## 8. F — Proposta de próximo lote

Recomenda-se um lote inicial de **12 unidades lógicas**, selecionado por diversidade e capacidade de preencher gaps, não por volume:

1. **2017 — International Paper:** alternativas GEOBAGS e Decanter/Draga 6, com revisões.
2. **2017 — CAESB Venda Draga:** venda de equipamento, família rara.
3. **2019 — Vale Maravilhas:** Planilha de Custo Rev2–Rev4 e composição final; excelente para linhagem de versões.
4. **2020 — caso “só bombeamento”:** separa bombeamento de dragagem.
5. **2021 — Bosch:** opções A–D, bags e proposta final; bom para cenários e oficialidade.
6. **2021 — Matinhos/CFF:** planilha orçamentária, Curva ABC, encargos/impostos e revisões.
7. **2022 — Petrobras DFP/PPU:** estrutura contratual/comercial distinta, com BDI e leis sociais.
8. **2023 — Suzano Aracruz:** combinação Dragagem + Centrífuga.
9. **2024 — Venda Draga FC001:** atualizar e comparar o domínio de venda com 2017.
10. **2024 — SABESP/Modelo 02:** planilha aberta de custos `.xlsm`, duas dragas e três decanters.
11. **2025 — Bracell:** bags em dois níveis, com e sem polímero.
12. **2026 — SK ETE Aeroporto:** centrífuga recente; ou SABESP Cubatão se a prioridade for comparar revisões REV1/REV2.

Antes da auditoria profunda, cada unidade deve passar por uma etapa curta de resolução de linhagem:

1. agrupar arquivos por obra/orçamento lógico;
2. identificar cenários, revisões, temporários e cópias;
3. apontar provável versão oficial e preservar alternativas;
4. escolher a planilha representativa sem apagar a história;
5. registrar a justificativa da escolha.

## 9. Decisão solicitada a Fabio

Validar se o próximo lote deve:

- manter as 12 unidades propostas; ou
- priorizar primeiro 2017 e 2019, anos sem auditoria anterior; ou
- trocar algum caso por uma obra que Fabio considere tecnicamente mais representativa.

Após essa validação, a próxima fase deve executar apenas o lote aprovado, construir a primeira matriz Obras × Blocos e trazer um novo checkpoint antes de ampliar a mineração.

## 10. Estado de parada

Conforme a missão, o trabalho para neste Checkpoint 0.

Não foram modificados arquivos no Drive, Excels, APP, módulo legado ou repositório. Nenhum desenvolvimento ou merge foi realizado.
