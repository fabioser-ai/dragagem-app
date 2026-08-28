# CHECKPOINT 0 — DESCOBERTA DO DOMÍNIO DE ORÇAMENTOS FOS

**Data da verificação:** 28/08/2026  
**Escopo:** mineração histórica 2015–2026  
**Modo:** somente leitura  
**Resultado:** checkpoint concluído; mineração pesada não iniciada

> Documento preservado no repositório do APP FOS a partir do relatório original do Checkpoint 0. O arquivo original completo desta sessão contém o inventário, cobertura, gaps, famílias aparentes e proposta de próximo lote. Este registro existe para preservar o marco de descoberta do domínio antes da implementação do novo sistema de Orçamentos.

## Resumo executivo

A estrutura histórica foi confirmada. As pastas `Obras 2015` a `Obras 2026` estão dentro da pasta correta `Obras`, que por sua vez está dentro de `FOS OBRAS _ BACCKUP`.

A campanha anterior produziu **158 fichas de auditoria individual**, porém elas foram salvas fora da árvore formal `MERLIN — Base de Conhecimento das Obras`. As 158 fichas não representam 158 obras independentes nem 158 análises profundas: existem cenários e revisões repetidos, 51 fichas declaram ausência de planilha e várias outras apenas inventariam arquivos `.xls` sem leitura funcional de abas ou fórmulas.

O inventário atual observou **573 pastas de primeiro nível** e **pelo menos 1.069 arquivos Excel**. Esses números representam universo bruto e incluem agregadores, auxiliares, temporários, cópias e revisões.

## Árvore histórica confirmada

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
    └── ATIVA - OBRAS ATUAIS
```

## Princípios recuperados

A metodologia histórica estabelece:

- cobertura do domínio, não simples volume de planilhas;
- preservação integral das fontes;
- separação entre fatos, interpretações, recorrências, regras de família e exceções;
- interface guiada separada da base configurável e do motor de cálculo;
- versionamento por vigência e snapshot dos parâmetros usados;
- sugestões históricas rastreáveis sem substituir a decisão do engenheiro;
- BDI, margem e decisões comerciais sob responsabilidade humana.

## Cobertura anterior

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

A campanha anterior parou durante ou ao final da triagem de 2016 e não chegou à consolidação transversal.

## Blocos/componentes já evidenciados

Sem homologar taxonomia:

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

## Universo bruto 2015–2026

| Ano | Pastas 1º nível | Excel observados |
|---|---:|---:|
| 2015 | 19 | 10 |
| 2016 | 82 | 81 |
| 2017 | 29 | 43 |
| 2018 | 76 | 64 |
| 2019 | 58 | 138 |
| 2020 | 80 | 178 |
| 2021 | 85 | 185 |
| 2022 | 19 | 44 |
| 2023 | 14 | 144 |
| 2024 | 26 | 54 |
| 2025 | 68 | 109 |
| 2026 | 17 | 19 |
| **Total bruto** | **573** | **1.069** |

Os números não representam quantidade de obras ou orçamentos lógicos.

## Gaps principais

Ainda faltam, entre outros:

- deduplicação por obra lógica e linhagem de versões;
- leitura sistemática de abas, fórmulas, referências, entradas e saídas;
- classificação Mestre / Contextual / Derivado / Histórico;
- proveniência por campo;
- requisitos de snapshot;
- matriz Obras × Blocos;
- normalização semântica dos blocos;
- catálogos candidatos de blocos e dados mestres;
- campos destinados à inteligência histórica;
- cobertura quantitativa do domínio por família.

## Próximo lote proposto no Checkpoint 0

1. 2017 — International Paper — alternativas GEOBAGS e Decanter/Draga 6.
2. 2017 — CAESB Venda Draga — venda de equipamento.
3. 2019 — Vale Maravilhas — linhagem Rev2–Rev4 e composição final.
4. 2020 — caso “só bombeamento”.
5. 2021 — Bosch — opções A–D, bags e proposta final.
6. 2021 — Matinhos/CFF — Curva ABC, encargos/impostos e revisões.
7. 2022 — Petrobras DFP/PPU — estrutura contratual/comercial distinta.
8. 2023 — Suzano Aracruz — Dragagem + Centrífuga.
9. 2024 — Venda Draga FC001.
10. 2024 — SABESP/Modelo 02 — duas dragas e três decanters.
11. 2025 — Bracell — bags em dois níveis, com e sem polímero.
12. 2026 — SK ETE Aeroporto — centrífuga recente; alternativa SABESP Cubatão.

Antes da auditoria profunda, cada unidade deve resolver sua linhagem de arquivos, cenários, revisões, temporários e cópias, preservando a história.

## Estado deste marco

Checkpoint 0 concluído em modo read-only. Nenhum Excel, arquivo do Drive, módulo do APP, dado operacional ou código foi alterado durante a descoberta. Nenhum desenvolvimento ou merge fazia parte deste checkpoint.

---

**Nota de preservação:** este documento é um marco histórico da descoberta do domínio do novo sistema de Orçamentos FOS. Não deve ser confundido com `docs/AUDIT_ORCAMENTOS.md`, que trata de auditorias do módulo/código de Orçamentos. Este documento registra a mineração do domínio de negócio a partir do acervo histórico de orçamentos da FOS.
