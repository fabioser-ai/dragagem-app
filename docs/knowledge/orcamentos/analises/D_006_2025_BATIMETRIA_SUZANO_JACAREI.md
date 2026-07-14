# Análise do orçamento — `D_006_2025 - Batimetria Suzano Jacarei.xlsx`

## 1. Identificação da análise

- **Nome completo do arquivo:** `D_006_2025 - Batimetria Suzano Jacarei.xlsx`
- **Data da análise:** 2026-07-14
- **Versão declarada no nome:** D_006_2025
- **Versão interna adicional:** não identificada
- **Data registrada na aba de dados:** 2024-12-17
- **Última modificação registrada nas propriedades do arquivo:** 2025-01-31 15:26:51 UTC
- **Último autor registrado:** Fabio Pereira Serafini
- **Aplicativo de gravação registrado:** Microsoft Macintosh Excel
- **Quantidade de abas:** 7
- **Status da análise:** CONCLUÍDA
- **Escopo:** exclusivamente o arquivo acima

## 2. Regra de evidência adotada

Este documento utiliza as classificações exigidas para esta análise:

- **EVIDÊNCIA CONFIRMADA:** informação comprovada diretamente no Excel, incluindo valor, texto, fórmula, comentário, formatação, metadado ou dependência.
- **EVIDÊNCIA PARCIAL:** informação observada somente neste orçamento e que não pode ser generalizada como método da FOS.
- **DÚVIDA:** interpretação sem comprovação suficiente, divergência não resolvida ou significado operacional que exige esclarecimento.

Quando aplicável, uma evidência também é identificada como **ANOMALIA OBSERVADA**, sem que isso represente correção ou decisão arquitetural.

## 3. Classificação do orçamento

### 3.1 Tipo aparente

**EVIDÊNCIA CONFIRMADA**

O arquivo representa uma proposta de serviços de batimetria. Essa classificação é sustentada pelo nome do arquivo, pela proposta `D_006_2025`, pelo cliente `Suzano - Jacarei`, pelo objeto `Batimetria Lagoa Polimento`, pelo pacote principal `Batimetria (JASAO)` e pela consolidação comercial.

### 3.2 Processo operacional representado

**EVIDÊNCIA CONFIRMADA**

O processo representado é composto por:

1. registro de dados gerais da oportunidade e da obra;
2. cálculo de produção e prazo baseado em parâmetros típicos de dragagem;
3. mobilização de barco/equipe;
4. execução de batimetria por fornecedor ou referência denominada JASAO;
5. elaboração de relatório final;
6. desmobilização de barco/equipe;
7. aplicação de BDI por item e consolidação do preço de venda.

### 3.3 Área de atuação

**EVIDÊNCIA CONFIRMADA**

- Área principal: levantamento batimétrico.
- Contexto técnico registrado: lagoa de polimento.
- Cliente registrado: Suzano — Jacareí.

### 3.4 Características diferenciadoras aparentes

**EVIDÊNCIA PARCIAL**

Neste arquivo, a batimetria é tratada como serviço principal contratado em verba única, acompanhado por mobilização, relatório e desmobilização também em quantidades unitárias.

**EVIDÊNCIA PARCIAL**

Embora seja um orçamento de batimetria, a planilha preserva estruturas, textos e fórmulas de um modelo de dragagem, incluindo vazão, eficiência, concentração, produção da draga, volume de dragagem, linha de recalque e operador de draga.

**DÚVIDA**

Não é possível concluir somente pelo arquivo se a estrutura de dragagem foi mantida deliberadamente para estimar suporte operacional ou se é apenas herança de um modelo anterior.

## 4. Inventário das abas

| Ordem | Nome exato da aba | Dimensão usada observada | Papel no fluxo |
| --- | --- | --- | --- |
| 1 | `Dados Obra ` | A1:K27 | Identificação, premissas técnicas e calendário. O nome contém espaço final. |
| 2 | `Produção` | A1:O33 | Cálculo de produção horária, produção mensal e prazo. |
| 3 | `1. Mob. Equipe` | A1:J30 | Mobilização do barco/equipe e serviços associados. |
| 4 | `2. Batimetria Jasao` | A1:H19 | Composição do serviço principal de batimetria. |
| 5 | `3. Relatorio final` | A1:H27 | Composição do relatório final e coleta/análise de amostra. |
| 6 | `4. Desmob. Equipe` | A1:J28 | Desmobilização do barco/equipe e serviços associados. |
| 7 | `5. Plan. Preços` | A1:L16 | Consolidação de custos, BDI e preços de venda. |

**EVIDÊNCIA CONFIRMADA**

Não foram identificadas abas ocultas, filtros automáticos ou tabelas estruturadas do Excel. A aba ativa no último salvamento era `5. Plan. Preços`.

## 5. Fluxo completo observado

```text
Dados Obra
    ├── calendário operacional ──> Produção
    ├── volume de dragagem ─────> Produção
    └── horas/dia ──────────────> Batimetria Jasao

1. Mob. Equipe ────────────────> 5. Plan. Preços
2. Batimetria Jasao ───────────> 5. Plan. Preços
3. Relatorio final ────────────> 5. Plan. Preços
4. Desmob. Equipe ─────────────> 5. Plan. Preços
```

**EVIDÊNCIA CONFIRMADA**

A aba `Produção` não alimenta nenhuma das composições de custo nem a planilha final. Os quatro pacotes de serviço alimentam diretamente a consolidação comercial.

**EVIDÊNCIA PARCIAL**

O fluxo econômico deste orçamento é essencialmente orientado a eventos ou verbas unitárias, e não a produção, volume ou prazo calculado.

## 6. Convenção visual declarada no arquivo

A aba `Dados Obra ` contém uma legenda explícita:

- azul: dados a serem preenchidos;
- vermelho: informações pendentes;
- preto: resultados automáticos.

**EVIDÊNCIA CONFIRMADA**

O arquivo utiliza cores de fonte azul, vermelha e preta em diferentes células.

**DÚVIDA**

A aplicação da convenção não é totalmente consistente em todas as abas. Existem valores fixos e fórmulas em estilos herdados, e a cor isoladamente não é suficiente para classificar com segurança toda célula.

## 7. Análise por aba

### 7.1 Aba `Dados Obra `

#### Objetivo e papel

**EVIDÊNCIA CONFIRMADA**

Registrar identificação da proposta, dados do cliente, objeto, local, premissas físicas, critérios de medição, responsabilidades e calendário operacional. É a origem de parâmetros consumidos pela aba `Produção` e, pontualmente, pela aba `2. Batimetria Jasao`.

#### Entradas e valores registrados

| Campo | Valor observado |
| --- | --- |
| Proposta | Proposta D_006_2025 |
| Data | 2024-12-17 |
| Cliente | Suzano - Jacarei |
| Contato / e-mail | vazios |
| Objeto | Batimetria Lagoa Polimento |
| Local | Santos - SP |
| Volume dragagem | 0 m³ |
| Tipo de material | Lodo + Areia |
| Distância de recalque | 300 m |
| Seio da linha de recalque | 0 m |
| Linha flutuante | 200 m |
| Seio da linha flutuante | 0 m |
| Linha de terra | 100 m |
| Profundidade / espessura / área | vazias |
| Volume geométrico calculado | 0 m³ |
| Tipo de bota-fora | Batimetria |
| Sistema de medição | preços unitários de serviços |
| Canteiro de obras | FOS |
| Mobilização | FOS |
| Horas de trabalho | 9 h/dia |
| Dias de trabalho | 22 dias/mês |

#### Fórmulas e finalidade

- `H16 = B16 + E16`: soma distância de recalque e seio da linha, resultando em 300 m.
- `H17 = B17 + E17`: soma linha flutuante e seio, resultando em 200 m.
- `G21 = B21 × D21 × B20`: calcula volume geométrico a partir de duas dimensões e espessura; como as entradas estão vazias, o resultado é 0.

#### Entidades conceituais

Proposta, cliente, contato, obra, local, material, geometria/volume, linha de recalque, sistema de medição, responsabilidades e calendário operacional.

#### Anomalias e dúvidas

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

O cliente e o nome do arquivo indicam Jacareí, enquanto o campo `Local` registra `Santos - SP`.

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

O objeto é batimetria, mas a aba mantém campos de dragagem e recalque, com volume igual a zero.

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

O campo `Tipo de Bota Fora` contém `Batimetria`, embora batimetria não descreva disposição de material.

**DÚVIDA**

O valor `Santos - SP` pode ser resíduo de outra proposta, local da base operacional ou local efetivo. O arquivo não permite determinar qual alternativa é correta.

### 7.2 Aba `Produção`

#### Objetivo

**EVIDÊNCIA CONFIRMADA**

Calcular produção horária, horas trabalhadas por mês, produção mensal e prazo a partir de parâmetros de uma draga.

#### Entradas e saídas

| Variável | Valor |
| --- | ---: |
| Vazão | 0 m³/h |
| Eficiência | 65% |
| Concentração | 21% |
| Horas/dia | 9 |
| Dias/mês | 22 |
| Horas/mês | 198 |
| Produção horária | 0 m³/h |
| Produção mensal | 0 m³/mês |
| Volume | 0 m³ |
| Prazo | `#DIV/0!` |

#### Fórmulas

- `H3 = 'Dados Obra '!B26`;
- `H6 = H3 × H4`;
- `D8 = D3 × (D4/100) × (D5/100)`;
- `D11 = H6`;
- `D13 = D8 × D11`;
- `D18 = D13`;
- `D21 = 'Dados Obra '!B14`;
- `D24 = D21 ÷ D18`.

#### Anomalias

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

O prazo apresenta `#DIV/0!` porque a produção mensal é zero.

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

A aba não alimenta qualquer custo ou preço deste orçamento.

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

Parâmetros de produção de draga coexistem com um objeto de batimetria, sem evidência de uso econômico.

### 7.3 Aba `1. Mob. Equipe`

#### Objetivo

**EVIDÊNCIA CONFIRMADA**

Compor o custo da mobilização do barco/equipe, incluindo mão de obra diária, alimentação, transporte, documentação, combustível e serviços potenciais.

#### Bloco de mão de obra

| Recurso | Nº func. | R$/h | Hrs/dia | Leis sociais | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Operador Líder | vazio | 34,00 | 9 | 110% | 0,00 |
| Operador de Draga | vazio | 20,00 | 9 | 110% | 0,00 |
| Operador de preparo de polímero | vazio | 20,00 | 9 | 110% | 0,00 |
| Ajudante Geral | 1 | 10,50 | 9 | 110% | 198,45 |
| Refeições | 1 | 30,00 | — | — | 30,00 |
| Transporte | 1 | 10,00 | — | — | 10,00 |
| **Custo por dia** |  |  |  |  | **238,45** |

A fórmula das funções é `quantidade × valor-hora × horas/dia × (1 + leis sociais/100)`. Refeições e transporte usam a soma do efetivo. O custo diário é a soma do bloco.

#### Composição de serviços

| Item | Descrição | Unid. | Qtd. | Preço unit. | Total |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | Guindaste para carregamento | dia | vazio | 2.500,00 | 0,00 |
| 2 | Treinamentos | dia | 0 | 1.500,00 | 0,00 |
| 3 | Mobiliário Canteiro | vb | vazio | 3.500,00 | 0,00 |
| 4 | Carreta Carga Seca para DRAGA | un | 0 | 2.500,00 | 0,00 |
| 5 | Guindaste p/descarregamento e montagem DRAGA | dia | vazio | 2.500,00 | 0,00 |
| 6 | Documentação | vb | 1 | 1.000,00 | 1.000,00 |
| 7 | Combustível + Frete | vb | 1 | 400,00 | 400,00 |
| 8 | Frete | vb | vazio | 5.000,00 | 0,00 |
| 9 | Trator D4 para lançar draga na água | dia | vazio | 2.000,00 | 0,00 |
| 10 | Mão de obra p/carga e montagem | dia | 1 | 238,45 | 238,45 |
|  | **TOTAL / preço final** |  |  |  | **1.638,45** |

#### Comentário e anomalias

**EVIDÊNCIA CONFIRMADA**

A célula `D25` contém comentário de Aguinaldo: `5 dias de mob`.

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

Apesar do comentário indicar 5 dias, a quantidade utilizada é 1 dia.

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

O título é `Mobilização Barco`, mas itens ainda mencionam `DRAGA`. A nota `chute` aparece ao lado do guindaste. `Peba` e `Leonardo` aparecem em células auxiliares e não participam das fórmulas.

**DÚVIDA**

Não está comprovado se `Peba` e `Leonardo` identificam pessoas previstas, referências salariais ou notas internas.

### 7.4 Aba `2. Batimetria Jasao`

#### Objetivo

**EVIDÊNCIA CONFIRMADA**

Compor o custo do serviço principal de batimetria e eventual acompanhamento da FOS.

#### Composição

| Item | Descrição | Unid. | Qtd. | Preço unit. | Total |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | Batimetria (JASAO) | vb | 1 | 14.200,00 | 14.200,00 |
| 2 | Mão de obra acompanhamento (FOS) | dia | 1 | 0,00 | 0,00 |
|  | TOTAL |  |  |  | 14.200,00 |
|  | Quantidade de Repetições |  |  | 1 | 14.200,00 |
|  | **Preço final** |  |  |  | **14.200,00** |

O bloco de equipe contém Operador Líder, Operador de Draga, Ajudante Geral, Refeições e Transporte, mas todas as quantidades resultam em zero.

#### Fórmulas

- horas/dia referenciam `Dados Obra `;
- custos de funções usam quantidade × R$/h × horas × 2,10;
- `F15 = D15 × E15`;
- `E16 = F10`, usando o custo diário da equipe como preço do acompanhamento;
- `F17 = SOMA(F15:F16)`;
- `F18 = F17 × E18`;
- `F19 = F18`.

#### Anomalias e dúvidas

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

O título interno é `3. PREPARO DE CÉLULA - Manta PEAD`, incompatível com a batimetria e com a numeração da aba.

**DÚVIDA**

`JASAO` aparenta ser fornecedor, prestador ou referência, mas não há cadastro, contato, data de cotação ou documento de origem do preço.

### 7.5 Aba `3. Relatorio final`

#### Objetivo e composição

**EVIDÊNCIA CONFIRMADA**

Compor os custos de elaboração do relatório final e coleta/análise de amostra.

| Recurso/item | Quantidade | Parâmetro | Total |
| --- | ---: | ---: | ---: |
| Engenheiro | 1 | R$ 50/h × 9 h × 2,10 | 945,00 |
| Demais funções/refeição/transporte | vazio/0 | — | 0,00 |
| Relatório Final (DWG, Adaptação, ETC) | 1 vb | preço unitário 0 | 0,00 |
| Coleta + Análise amostra | 1 dia | 250,00 | 250,00 |
| **Preço final** |  |  | **250,00** |

#### Anomalias e dúvidas

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

O custo diário do engenheiro, R$ 945,00, não é referenciado por qualquer item. O item `Relatório Final` tem preço unitário zero, e o preço final corresponde somente à coleta/análise.

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

O bloco mantém cargos de operação de draga e preparo de polímero, sem utilização.

**DÚVIDA**

Não está comprovado se o custo do engenheiro deveria compor o relatório, se está absorvido em outro item ou se foi deliberadamente excluído.

### 7.6 Aba `4. Desmob. Equipe`

#### Objetivo e composição

**EVIDÊNCIA CONFIRMADA**

Compor a desmobilização do barco/equipe. O bloco de mão de obra repete um Ajudante Geral, refeição e transporte, totalizando R$ 238,45/dia.

| Item | Descrição | Qtd. | Preço unit. | Total |
| ---: | --- | ---: | ---: | ---: |
| 1 | Guindaste para carregamento | vazio | 2.500,00 | 0,00 |
| 2 | Treinamentos | vazio | 3.000,00 | 0,00 |
| 3 | Mobiliário Canteiro | vazio | 3.500,00 | 0,00 |
| 4 | Carreta Carga Seca para DRAGA | vazio | 2.500,00 | 0,00 |
| 5 | Guindaste p/descarregamento e montagem DRAGA | vazio | 2.500,00 | 0,00 |
| 6 | Frete | vazio | 5.000,00 | 0,00 |
| 7 | Trator D4 para lançar draga na água | vazio | 2.000,00 | 0,00 |
| 8 | Mão de obra p/carga e montagem | 1 | 238,45 | 238,45 |
|  | **Preço final** |  |  | **238,45** |

#### Comentário e anomalias

**EVIDÊNCIA CONFIRMADA**

A célula `D23` contém comentário de Aguinaldo: `5 dias de mob`.

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

A quantidade usada é 1 dia. O título interno é `Mobilização da Draga 6"`, embora a aba seja de desmobilização. As descrições são majoritariamente de mobilização/montagem, e a nota `chute` permanece.

**DÚVIDA**

Não está comprovado se o custo correto seria apenas um dia de ajudante ou se faltam frete, içamento, transporte e demais recursos.

### 7.7 Aba `5. Plan. Preços`

#### Objetivo

**EVIDÊNCIA CONFIRMADA**

Consolidar custos dos quatro pacotes, transformar custos totais em custos unitários, aplicar BDI individual e calcular preço total de venda.

| Item | Descrição | Custo total | Qtd. | Unid. | BDI | Preço total |
| ---: | --- | ---: | ---: | --- | ---: | ---: |
| 1 | Mobilização Barco | 1.638,45 | 1 | un | 23,5% | 2.023,48575 |
| 3 | Batimetria Jasao | 14.200,00 | 1 | m² | 22,0% | 17.324,00 |
| 4 | Relatorio final | 250,00 | 1 | m³ | 23,5% | 308,75 |
| 8 | Desmobilização Barco | 238,45 | 1 | un | 23,5% | 294,48575 |

Fórmulas por item:

```text
custo unitário = custo total ÷ quantidade
preço unitário = custo unitário × (1 + BDI/100)
preço total = quantidade × preço unitário
```

Resultados:

- custo total exibido: **R$ 14.688,45**;
- soma matemática dos quatro custos: **R$ 16.326,90**;
- preço de venda: **R$ 19.950,7215**.

#### Anomalias e dúvidas

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

`C8 = SOMA(C5:C7)` exclui a mobilização em C4. O custo total exibido é R$ 1.638,45 menor que a soma integral. `J8 = SOMA(J4:J7)` inclui os quatro itens.

**ANOMALIA OBSERVADA — EVIDÊNCIA CONFIRMADA**

A numeração é 1, 3, 4 e 8. A batimetria usa `m²` e o relatório `m³`, ambos com quantidade 1 e sem base física preenchida que determine essas quantidades.

**EVIDÊNCIA PARCIAL**

O BDI não é uniforme: 22% para batimetria e 23,5% para os demais itens.

**DÚVIDA**

Não está comprovado o motivo da diferença de BDI nem se `m²` e `m³` são unidades contratuais reais ou resíduos.

## 8. Dependências entre abas

| Origem | Destino | Finalidade |
| --- | --- | --- |
| `Dados Obra ` B26 | `Produção` H3 | Horas por dia |
| `Dados Obra ` B14 | `Produção` D21 | Volume total |
| `Dados Obra ` B26 | `2. Batimetria Jasao` D5/D7 | Horas diárias de equipe |
| `1. Mob. Equipe` F30 | `5. Plan. Preços` C4 | Custo de mobilização |
| `2. Batimetria Jasao` F19 | `5. Plan. Preços` C5 | Custo da batimetria |
| `3. Relatorio final` F20 | `5. Plan. Preços` C6 | Custo do relatório/análise |
| `4. Desmob. Equipe` F28 | `5. Plan. Preços` C7 | Custo de desmobilização |

## 9. Entidades encontradas

### Comerciais

Proposta, cliente, contato, objeto, item de venda, custo, BDI, preço unitário e preço total.

### Técnicas e operacionais

Obra, lagoa de polimento, batimetria, material, volume, linha de recalque, linha flutuante, linha de terra, profundidade, espessura, área, calendário, produção, prazo, mobilização, desmobilização, relatório, coleta e análise.

### Recursos

Função/cargo, quantidade de funcionários, valor-hora, jornada, leis sociais, refeição, transporte, guindaste, carreta, trator, frete, documentação, combustível, treinamento, mobiliário e JASAO.

## 10. Regras de negócio observadas

1. **EVIDÊNCIA CONFIRMADA:** custo de função = quantidade × valor-hora × horas/dia × (1 + leis sociais).
2. **EVIDÊNCIA CONFIRMADA:** leis sociais de 110% nos blocos de equipe.
3. **EVIDÊNCIA CONFIRMADA:** refeições e transporte podem ser dimensionados pela soma do efetivo.
4. **EVIDÊNCIA CONFIRMADA:** serviço = quantidade × preço unitário.
5. **EVIDÊNCIA CONFIRMADA:** a batimetria admite quantidade de repetições.
6. **EVIDÊNCIA CONFIRMADA:** BDI comercial é aplicado por item.
7. **EVIDÊNCIA CONFIRMADA:** cada pacote possui subtotal, BDI interno e preço final; o BDI interno está zerado.
8. **EVIDÊNCIA PARCIAL:** os itens são vendidos em quantidade 1, funcionando como verbas unitárias neste arquivo.
9. **EVIDÊNCIA PARCIAL:** a execução principal é tratada como compra externa de R$ 14.200,00, sem custo de acompanhamento FOS.

## 11. Fórmulas importantes consolidadas

```text
horas/mês = horas/dia × dias/mês
produção horária = vazão × eficiência × concentração
produção mensal = produção horária × horas/mês
prazo = volume ÷ produção mensal
custo da função = quantidade × R$/h × horas/dia × (1 + leis sociais/100)
custo diário = soma das funções + refeições + transporte
preço total do serviço = quantidade × preço unitário
custo unitário = custo total ÷ quantidade
preço unitário = custo unitário × (1 + BDI/100)
preço total = quantidade × preço unitário
```

## 12. Terminologias

Batimetria; Lagoa de Polimento; JASAO; Mobilização Barco; Desmobilização Barco; Relatório Final; DWG; coleta/análise de amostra; verba (`vb`); leis sociais; BDI; seio da linha; linha flutuante; linha de terra; bota-fora; preços unitários; quantidade de repetições; `chute`.

## 13. Padrões observados exclusivamente neste arquivo

**EVIDÊNCIA PARCIAL**

- quatro pacotes comercializáveis: mobilização, serviço principal, relatório e desmobilização;
- pacotes com bloco de mão de obra seguido de composição de serviços;
- BDI interno zerado e BDI aplicado na consolidação;
- quantidade comercial igual a 1;
- comentários de célula registrando duração sem alterar a fórmula;
- reutilização de modelo de dragagem para orçamento de batimetria.

Nenhum desses padrões deve ser tratado como regra geral sem crosscheck futuro.

## 14. Exceções e anomalias consolidadas

1. Local `Santos - SP` diverge de Suzano/Jacareí.
2. `Tipo de Bota Fora` contém `Batimetria`.
3. Volume, vazão e produção estão zerados.
4. Prazo apresenta `#DIV/0!`.
5. Produção não participa da formação do preço.
6. Títulos internos são resíduos de preparo de célula, mobilização de draga e outros modelos.
7. Termos `draga`, `polímero`, `manta PEAD` e `trator D4` permanecem.
8. Comentários indicam 5 dias, mas quantidades usadas são 1 dia.
9. Custo do engenheiro do relatório não é apropriado ao item final.
10. `Custo Total` exclui mobilização.
11. Unidades `m²` e `m³` não correspondem a quantidades físicas preenchidas.
12. Numeração dos itens finais contém lacunas.
13. Notas `chute`, `Peba` e `Leonardo` não participam dos cálculos.
14. Não há data-base nem origem formal da cotação JASAO.
15. O BDI varia sem justificativa registrada.

## 15. Dúvidas para validação futura

1. O local correto é Jacareí ou Santos?
2. `JASAO` é empresa, profissional, equipamento, método ou nome interno?
3. Qual é a fonte e data-base dos R$ 14.200,00?
4. A batimetria é verba única ou deveria ser medida por área?
5. Qual é a unidade contratual correta da batimetria?
6. Qual é a unidade contratual correta do relatório?
7. A coleta/análise faz parte obrigatória do relatório?
8. O engenheiro deveria ser apropriado ao relatório?
9. Mobilização e desmobilização deveriam considerar 5 dias?
10. Quais recursos compõem efetivamente mobilização e desmobilização?
11. Os preços auxiliares são referências reais, estimativas ou resíduos?
12. Por que a batimetria recebe BDI de 22% e os demais 23,5%?
13. A aba de produção possui função real neste tipo de orçamento?
14. A FOS forneceria barco e equipe para acompanhamento, posicionamento ou acesso?
15. O custo total deveria incluir mobilização, resultando em R$ 16.326,90?
16. O valor de venda deveria ser arredondado?
17. `Lodo + Areia`, linhas de recalque e dados de dragagem são reais ou resíduos?
18. Qual o significado de `preços unitários de serviços` quando todas as quantidades comerciais são 1?

## 16. Limitações

- A análise foi realizada sobre o Excel recebido, incluindo células, fórmulas, comentários, nomes exatos das abas e propriedades internas.
- Não foram fornecidos proposta em PDF, escopo do cliente, cotação JASAO, e-mails, memorial técnico ou confirmação do especialista.
- Valores de mercado não foram validados externamente.
- Não foi executada comparação com outros orçamentos.
- Não foi tomada decisão arquitetural.
- Não foi proposta correção das fórmulas.
- Não foi alterado o Excel original.

## 17. Checklist de validação

- [x] Todas as 7 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Valores, fórmulas, dependências, comentários, resíduos e anomalias preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma consolidação entre orçamentos realizada.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma funcionalidade criada.
- [x] Nenhum índice geral alterado.
- [x] Nenhum documento de outro orçamento alterado.

## 18. Conclusão restrita a este arquivo

**EVIDÊNCIA CONFIRMADA**

O orçamento registra quatro entregas: mobilização do barco, batimetria JASAO, relatório final e desmobilização, com preço de venda calculado de R$ 19.950,7215.

**EVIDÊNCIA CONFIRMADA**

A maior parcela é a batimetria JASAO, com custo de R$ 14.200,00 e venda de R$ 17.324,00.

**EVIDÊNCIA CONFIRMADA**

A planilha contém uma estrutura de dragagem que não participa da formação econômica e apresenta prazo inválido por divisão por zero.

**EVIDÊNCIA CONFIRMADA**

O total de custo exibido é inconsistente porque exclui a mobilização, enquanto o total de venda inclui todos os itens.

**EVIDÊNCIA PARCIAL**

Este arquivo evidencia um orçamento simplificado de batimetria construído a partir de um modelo mais amplo de dragagem, preservando componentes não utilizados ou não revisados.

Nenhuma afirmação deste documento deve ser promovida a regra geral do Método de Orçamento FOS sem curadoria e crosscheck futuros.
