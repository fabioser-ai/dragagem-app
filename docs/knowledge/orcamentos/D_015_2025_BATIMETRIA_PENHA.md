# D_015_2025 - Batimetria Penha.xlsx — Batimetria de Lagoa Anaeróbica

## Status

- Engenharia reversa vertical concluída para o arquivo analisado.
- Todas as 7 abas foram examinadas.
- Fórmulas, valores, dependências, comentários, nomenclaturas e anomalias foram inventariados.
- Nenhuma funcionalidade, arquitetura, banco de dados, tela ou consolidação foi definida.
- As descobertas reutilizáveis permanecem provisórias e possuem confiança Nível C, pois derivam de uma única fonte.

## Identidade permanente da fonte

- **Arquivo original:** `D_015_2025 - Batimetria Penha.xlsx`
- **Data da análise:** 14/07/2026
- **Versão explícita do arquivo:** não identificada.
- **Última modificação registrada nos metadados do arquivo:** 17/03/2025 às 18:57:32 UTC.
- **Último autor registrado:** `Fabio Pereira Serafini`.
- **Proposta registrada:** `Proposta D_015_2025`
- **Data registrada na planilha:** 17/03/2025
- **Cliente registrado:** `Penha`
- **Objeto registrado:** `Batimetria Lagoa Anaeróbica`
- **Local registrado:** `Coronel Vivida - PR`
- **Quantidade de abas:** 7
- **Status da análise:** concluída com limitações registradas.

## Regra de classificação usada neste registro

| Categoria operacional | Correspondência documental |
| --- | --- |
| **EVIDÊNCIA CONFIRMADA** | Conteúdo, valor, fórmula, comentário, dependência ou anomalia presente diretamente no Excel. |
| **EVIDÊNCIA PARCIAL** | Interpretação ou possível regra observada somente neste orçamento. |
| **DÚVIDA** | Informação sem comprovação suficiente ou cujo significado operacional não pode ser concluído pelo arquivo. |

Uma anomalia é **EVIDÊNCIA CONFIRMADA quanto à sua existência**, sem concluir automaticamente que representa erro de negócio.

## Classificação aparente do orçamento

### EVIDÊNCIA CONFIRMADA

O arquivo registra um orçamento com os seguintes elementos:

- objeto: batimetria de lagoa anaeróbica;
- cliente: Penha;
- local: Coronel Vivida - PR;
- material informado: `Lodo + Areia`;
- tipo de bota-fora informado: `Batimetria`;
- sistema de medição: `preços unitários de serviços`;
- mobilização e canteiro atribuídos à FOS;
- contratação principal de batimetria indicada como `Batimetria (JASAO)`;
- entrega de relatório final;
- mobilização e desmobilização de equipe/barco;
- consolidação comercial por preços unitários.

### EVIDÊNCIA PARCIAL

O orçamento aparenta representar uma **prestação de serviço de levantamento batimétrico**, com execução técnica principal terceirizada à referência `JASAO` e participação da FOS na mobilização, acompanhamento, relatório e desmobilização.

Embora a planilha contenha uma aba de produção de draga e campos típicos de dragagem, os parâmetros de produção estão zerados e não alimentam nenhuma composição financeira. Portanto, neste arquivo, a estrutura de dragagem aparenta ser um resíduo de modelo reutilizado, e não o processo econômico principal.

### DÚVIDA

- `Penha` é o cliente final, um contato, uma unidade operacional ou abreviação de empresa?
- `JASAO` identifica pessoa física, empresa, fornecedor ou equipe interna?
- O levantamento inclui efetivamente uso de barco/draga da FOS ou apenas equipe e logística?
- A unidade comercial `m²` atribuída à batimetria é intencional, apesar da quantidade ser 1 e o custo representar verba global?
- O tipo de bota-fora `Batimetria` é preenchimento incorreto de um campo não aplicável ou classificação deliberada?

## Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra ` | Identificação da proposta e premissas técnicas, operacionais e comerciais. O nome possui espaço final. |
| 2 | `Produção` | Estrutura de cálculo de produção e prazo de dragagem, atualmente zerada e sem impacto financeiro. |
| 3 | `1. Mob. Equipe` | Composição da mobilização da equipe/barco e custos de apoio. |
| 4 | `2. Batimetria Jasao` | Contratação da batimetria e estrutura de mão de obra de acompanhamento. |
| 5 | `3. Relatorio final` | Composição do relatório final, coleta e análise de amostra. |
| 6 | `4. Desmob. Equipe` | Composição da desmobilização da equipe/barco. |
| 7 | `5. Plan. Preços` | Consolidação dos custos, BDI comercial e preço de venda. |

## Fluxo completo observado

```text
Dados da obra
    ├── horas/dia e dias/mês ──> Produção
    └── volume de dragagem ────> Produção

Mobilização da equipe/barco ───────────────┐
Batimetria contratada + acompanhamento ───┤
Relatório final + coleta/análise ──────────┼──> Planilha de preços
Desmobilização da equipe/barco ────────────┘
```

A aba `Produção` recebe entradas de `Dados Obra`, mas não fornece resultados a nenhuma composição financeira neste arquivo.

---

# Análise por aba

## 1. Aba `Dados Obra `

### Objetivo

Registrar a identidade comercial da proposta e as premissas gerais da obra.

### Papel no fluxo

É a fonte de horas por dia, dias por mês e volume usados na aba `Produção`. Os demais campos não possuem dependências externas observadas neste arquivo.

### Convenção visual — EVIDÊNCIA CONFIRMADA

A legenda da própria aba declara:

- azul: dados a serem preenchidos;
- vermelho: informações pendentes;
- preto: resultados automáticos.

As células de entrada efetivamente usam predominantemente fonte azul. Existem observações em vermelho em outras abas.

### Entradas observadas — EVIDÊNCIA CONFIRMADA

- proposta: `Proposta D_015_2025`;
- data: 17/03/2025;
- cliente: `Penha`;
- contato: não preenchido;
- e-mail: não preenchido;
- objeto: `Batimetria Lagoa Anaeróbica`;
- local: `Coronel Vivida - PR`;
- volume de dragagem: `0 m³`;
- tipo de material: `Lodo + Areia`;
- distância de recalque: `300 m`;
- seio da linha de recalque: `0 m`;
- linha flutuante: `200 m`;
- seio da linha flutuante: `0 m`;
- linha de terra: `100 m`;
- profundidade de dragagem: não preenchida;
- espessura média de dragagem: não preenchida;
- área de dragagem: não preenchida;
- dimensão complementar da área: não preenchida;
- tipo de bota-fora: `Batimetria`;
- sistema de medição: `preços unitários de serviços`;
- canteiro de obras: `FOS`;
- mobilização: `FOS`;
- horário de trabalho: `9 h/dia`;
- dias de trabalho: `22 dias/mês`.

### Fórmulas e resultados — EVIDÊNCIA CONFIRMADA

- `H16 = B16 + E16`: distância total de recalque.
  - resultado: `300 m`.
- `H17 = B17 + E17`: linha flutuante total.
  - resultado: `200 m`.
- `G21 = B21 × D21 × B20`: volume geométrico.
  - resultado: `0 m³`, pois as dimensões não estão preenchidas.

### Entidades conceituais

- proposta;
- cliente;
- contato;
- obra;
- local;
- material;
- volume;
- linha de recalque;
- linha flutuante;
- linha de terra;
- profundidade;
- espessura;
- área;
- bota-fora;
- sistema de medição;
- responsabilidade por canteiro;
- responsabilidade por mobilização;
- jornada;
- calendário mensal.

### Regras implícitas — EVIDÊNCIA PARCIAL

- O arquivo preserva um formulário genérico de dragagem mesmo quando o objeto é batimetria.
- A distância total pode incluir uma parcela adicional denominada `seio da linha`.
- O volume informado e o volume geométrico calculável podem coexistir.
- Responsabilidades por canteiro e mobilização são tratadas como premissas explícitas.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- O nome real da aba possui espaço final: `Dados Obra `.
- O volume de dragagem está zerado, embora o arquivo mantenha cálculo de produção e prazo.
- `Tipo de Bota Fora` contém `Batimetria`, que não descreve um destino de material.
- O cabeçalho `Área de Dragagem (m² ou L x C)` combina duas formas de entrada, mas não esclarece a unidade das células.
- Contato, e-mail, profundidade, espessura e área permanecem vazios.

### Dúvidas

- Os campos de dragagem são deliberadamente mantidos como formulário padrão mesmo em levantamentos sem dragagem?
- O volume zero confirma que não existe dragagem ou apenas que o volume ainda não foi levantado?
- A batimetria tem como finalidade determinar posteriormente o volume?
- Qual é o significado operacional de `seio da linha` neste tipo de serviço?

---

## 2. Aba `Produção`

### Objetivo

Converter parâmetros de vazão, eficiência, concentração e jornada em produção horária, produção mensal e prazo.

### Papel no fluxo

Recebe dados da aba `Dados Obra `. Nenhuma fórmula de outra aba referencia os resultados de `Produção` neste arquivo.

### Entradas — EVIDÊNCIA CONFIRMADA

- vazão: `0 m³/h`;
- eficiência: `65%`;
- concentração: `21%`;
- horas por dia: `9`;
- dias por mês: `22`;
- volume total: `0 m³`.

### Fórmulas — EVIDÊNCIA CONFIRMADA

- `H3 = 'Dados Obra '!B26`: horas por dia.
- `H6 = H3 × H4`: horas mensais.
- `D8 = D3 × (D4/100) × (D5/100)`: produção horária útil.
- `D11 = H6`: horas trabalhadas no mês.
- `D13 = D8 × D11`: produção mensal.
- `D18 = D13`: repetição da produção mensal na seção de prazo.
- `D21 = 'Dados Obra '!B14`: quantidade total a dragar.
- `D24 = D21 ÷ D18`: prazo de execução.

### Resultados — EVIDÊNCIA CONFIRMADA

- horas mensais: `198 h/mês`;
- produção horária: `0 m³/h`;
- produção mensal: `0 m³/mês`;
- quantidade total a dragar: `0 m³`;
- prazo: `#DIV/0!`.

### Dependências

- depende de `Dados Obra ` para horas/dia e volume;
- dias/mês está digitado diretamente como `22`, embora exista o mesmo valor em `Dados Obra `;
- não alimenta as demais abas.

### Regras implícitas — EVIDÊNCIA PARCIAL

A fórmula preserva o método:

```text
produção útil = vazão nominal × eficiência × concentração
produção mensal = produção útil × horas mensais
prazo = volume ÷ produção mensal
```

Neste orçamento, o método não é operacionalmente utilizado devido à vazão e ao volume zerados.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- A fórmula de horas/dia referencia `B26`, corretamente correspondente a 9 h/dia.
- Dias/mês não é referenciado de `Dados Obra `; foi digitado novamente em `H4`.
- O prazo apresenta erro `#DIV/0!`.
- A aba permanece estruturalmente completa, mas isolada do preço final.
- O título `Cálculo de Produção da Draga` não corresponde diretamente ao objeto comercial de batimetria.

### Dúvidas

- A aba deveria ter sido removida, ignorada ou preenchida quando o serviço é somente batimetria?
- Eficiência de 65% e concentração de 21% são resíduos de outro orçamento?
- A produção deveria representar produtividade da equipe de batimetria, em vez de produção de draga?

---

## 3. Aba `1. Mob. Equipe`

### Objetivo

Compor o custo de mobilização da equipe e dos recursos logísticos necessários ao início do serviço.

### Papel no fluxo

Gera preço final consumido diretamente pela aba `5. Plan. Preços`.

### Composição de mão de obra — EVIDÊNCIA CONFIRMADA

Equipe ativa:

- 1 operador de draga;
- 1 ajudante geral;
- 2 refeições;
- 2 transportes.

Posições estruturadas, mas sem quantidade:

- operador líder;
- operador de preparo de polímero.

Parâmetros:

- operador líder: R$ 34/h;
- operador de draga: R$ 20/h;
- operador de preparo de polímero: R$ 20/h;
- ajudante geral: R$ 10,50/h;
- 9 h/dia;
- leis sociais: 110%;
- refeição: R$ 30 por pessoa;
- transporte: R$ 10 por pessoa.

Fórmula de pessoal:

```text
quantidade × valor-hora × horas/dia × (1 + leis sociais)
```

Resultados:

- operador de draga: R$ 378,00/dia;
- ajudante geral: R$ 198,45/dia;
- refeições: R$ 60,00/dia;
- transporte: R$ 20,00/dia;
- custo diário da equipe: R$ 656,45.

A célula `G5` registra `Peba` e a célula `G8` registra `Leonardo`, associadas visualmente às linhas de operador líder e ajudante geral.

### Serviços e recursos — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Quantidade | Preço unitário | Total |
| --- | --- | ---: | ---: | ---: |
| 1 | Guindaste para carregamento | vazia | R$ 2.500,00 | R$ 0,00 |
| 2 | Treinamentos — trabalho em altura e espaço confinado | 0 | R$ 1.500,00 | R$ 0,00 |
| 3 | Mobiliário canteiro | vazia | R$ 3.500,00 | R$ 0,00 |
| 4 | Carreta carga seca para draga | 0 | R$ 2.500,00 | R$ 0,00 |
| 5 | Guindaste para descarregamento e montagem da draga | vazia | R$ 2.500,00 | R$ 0,00 |
| 6 | Documentação | 1 | R$ 1.000,00 | R$ 1.000,00 |
| 7 | Combustível + frete | 1 | R$ 4.000,00 | R$ 4.000,00 |
| 8 | Frete | vazia | R$ 5.000,00 | R$ 0,00 |
| 9 | Trator D4 para lançar draga na água | vazia | R$ 2.000,00 | R$ 0,00 |
| 10 | Mão de obra para carga e montagem | 1 dia | R$ 656,45 | R$ 656,45 |

Observação `chute` na linha do guindaste de descarregamento/montagem.

### Fórmulas e resultados — EVIDÊNCIA CONFIRMADA

- custos de pessoal em `F5:F8`;
- quantidade de refeições `A9 = A5 + A8 + A6 + A7`;
- quantidade de transporte `A10 = A9`;
- custo diário `F11 = SOMA(F5:F10)`;
- itens com total calculado por quantidade × preço unitário;
- `E25 = F11`: custo diário transferido para a linha de mão de obra;
- `F26 = SOMA(F16:F25)`: subtotal;
- `F27 = F26 × (E27/100)`: BDI interno;
- `F28 = SOMA(F26:F27)`: preço final;
- `F30 = SOMA(F28:F29)`: repetição final.

Resultados:

- subtotal: R$ 5.656,45;
- BDI interno: célula vazia, com resultado R$ 0,00;
- preço final: R$ 5.656,45.

### Comentário da célula — EVIDÊNCIA CONFIRMADA

A célula `D25`, quantidade da mão de obra, possui comentário de `Aguinaldo`:

> 5 dias de mob

Apesar do comentário, a quantidade efetivamente usada é `1`.

### Regras implícitas — EVIDÊNCIA PARCIAL

- Mobilização é tratada como pacote de evento único.
- Recursos não aplicáveis podem permanecer na estrutura com quantidade vazia ou zero.
- Mão de obra pode ser apropriada pelo custo diário calculado no bloco superior.
- Nomes em coluna auxiliar podem indicar pessoas previstas para a equipe.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- Título interno: `1 - Mobilização Barco`, enquanto as descrições citam draga.
- A aba se chama `Mob. Equipe`, mas inclui recursos de mobilização de equipamento.
- O comentário indica 5 dias, porém a fórmula utiliza 1 dia.
- O BDI interno está vazio, embora a planilha de preços aplique 30% de BDI comercial.
- `Combustivel + Frete` e `Frete` coexistem como itens separados.
- A observação `chute` explicita caráter estimado do preço de um recurso que não foi ativado.

### Dúvidas

- A mobilização é de barco, draga, equipe ou combinação dos três?
- O custo deveria usar 5 dias conforme comentário?
- `Peba` e `Leonardo` são nomes de funcionários confirmados para a execução?
- Por que operador líder está sem quantidade, embora exista um nome associado?
- Documentação e combustível/frete são custos comprovados, cotados ou estimados?

---

## 4. Aba `2. Batimetria Jasao`

### Objetivo

Compor o custo da batimetria contratada e de eventual acompanhamento da FOS.

### Papel no fluxo

Gera o maior custo do orçamento e alimenta diretamente a planilha de preços.

### Composição de mão de obra — EVIDÊNCIA CONFIRMADA

A estrutura contém:

- operador líder;
- operador de draga;
- ajudante geral;
- refeições;
- transporte.

Todas as quantidades estão vazias ou zeradas. O custo diário calculado é R$ 0,00.

Os valores-hora preservados são:

- operador líder: R$ 34/h;
- operador de draga: R$ 20/h;
- ajudante geral: R$ 10/h;
- leis sociais: 110%.

As horas/dia são referenciadas de `Dados Obra `, mas não geram custo por ausência de quantidade.

### Serviços — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Unidade | Quantidade | Preço unitário | Total |
| --- | --- | --- | ---: | ---: | ---: |
| 1 | Batimetria (JASAO) | vb | 1 | R$ 35.000,00 | R$ 35.000,00 |
| 2 | Mão de obra acompanhamento (FOS) | dia | 1 | R$ 0,00 | R$ 0,00 |

Observação em vermelho:

`Preço passado 26/02/2025 - Zap Jasao`

### Fórmulas e resultados — EVIDÊNCIA CONFIRMADA

- horas/dia da equipe referenciadas de `Dados Obra `;
- custo diário da equipe: soma dos custos de pessoal;
- total da batimetria: quantidade × preço unitário;
- preço unitário da mão de obra de acompanhamento: custo diário calculado;
- subtotal: R$ 35.000,00;
- quantidade de repetições: `1`;
- preço final: subtotal × quantidade de repetições;
- preço final: R$ 35.000,00.

### Entidades conceituais

- fornecedor ou executor de batimetria;
- cotação;
- data da cotação;
- canal de comunicação;
- verba;
- acompanhamento FOS;
- repetição do serviço.

### Regras implícitas — EVIDÊNCIA PARCIAL

- A batimetria principal é precificada como verba global.
- O arquivo preserva data e canal da referência de preço.
- A quantidade de repetições permite multiplicar o pacote completo.
- Acompanhamento FOS pode ser ativado por custo diário, mas está zerado neste orçamento.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- O título interno da aba é `3. PREPARO DE CÉLULA - Manta PEAD`, incompatível com o conteúdo.
- O bloco de mão de obra mantém descrição `montagem canteiro`, incompatível com batimetria.
- O nome da aba usa `Jasao`; a descrição e observação usam `JASAO` e `Jasao`.
- O preço foi registrado em 26/02/2025, antes da data da proposta de 17/03/2025.
- A mão de obra de acompanhamento possui quantidade 1 e preço unitário zero.
- A unidade `vb` da composição é convertida para `m²` na consolidação comercial.

### Dúvidas

- `JASAO` é fornecedor formal?
- Existe documento de cotação além da mensagem de WhatsApp?
- O preço de R$ 35.000 inclui deslocamento, equipamento, processamento e relatório?
- A quantidade de repetições representa campanhas, lagoas, visitas ou medições?
- Por que o relatório final é cobrado separadamente se a batimetria pode incluir processamento?

---

## 5. Aba `3. Relatorio final`

### Objetivo

Compor o custo de elaboração do relatório final e da coleta/análise de amostra.

### Papel no fluxo

Gera custo próprio consumido pela planilha de preços.

### Composição de mão de obra — EVIDÊNCIA CONFIRMADA

Equipe ativa:

- 1 engenheiro;
- 9 h/dia;
- R$ 50/h;
- leis sociais de 110%;
- custo: R$ 945,00/dia.

Demais posições estruturadas, mas sem quantidade:

- operador de draga;
- operador de preparo de polímero;
- ajudante geral;
- refeições;
- transporte.

Custo diário total: R$ 945,00.

### Serviços — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Unidade | Quantidade | Preço unitário | Total |
| --- | --- | --- | ---: | ---: | ---: |
| 1 | Relatório final — DWG, adaptação, etc. | vb | 1 | R$ 3.500,00 | R$ 3.500,00 |
| 2 | Coleta + análise de amostra | dia | 1 | R$ 250,00 | R$ 250,00 |

### Fórmulas e resultados — EVIDÊNCIA CONFIRMADA

- engenheiro: quantidade × R$/h × horas/dia × (1 + leis sociais);
- custo diário: soma da equipe;
- serviços: quantidade × preço unitário;
- subtotal: R$ 3.750,00;
- BDI interno: 0%;
- preço final: R$ 3.750,00.

### Regras implícitas — EVIDÊNCIA PARCIAL

- O relatório é tratado como entrega de verba global.
- Coleta e análise de amostra são cobradas como componente separado.
- O bloco de mão de obra de engenharia não é transferido para a composição inferior; o preço de R$ 3.500 é digitado diretamente.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- O título interno é `4. Relatorio Final`, apesar de a aba ser a terceira composição.
- O bloco superior usa a descrição `Mão de obra montagem canteiro`.
- O custo diário do engenheiro de R$ 945 não é referenciado por nenhuma linha de serviço.
- A planilha comercial atribui unidade `m³` ao relatório final.
- Existe célula vermelha vazia fora do intervalo principal, indicando possível resíduo de modelo.

### Dúvidas

- O preço de R$ 3.500 foi calculado a partir do engenheiro ou apenas estimado?
- Quantos dias de engenharia estão embutidos no relatório?
- A coleta/análise é laboratorial, de sedimento, de água ou outro material?
- O DWG é a entrega principal ou um dos formatos do relatório?

---

## 6. Aba `4. Desmob. Equipe`

### Objetivo

Compor o custo de desmobilização da equipe e dos recursos após o serviço.

### Papel no fluxo

Gera preço final consumido diretamente pela planilha de preços.

### Composição de mão de obra — EVIDÊNCIA CONFIRMADA

Equipe ativa:

- 1 ajudante geral;
- 1 refeição;
- 1 transporte.

Posições sem quantidade:

- operador líder;
- operador de draga;
- operador de preparo de polímero.

Parâmetros:

- ajudante geral: R$ 10,50/h;
- 9 h/dia;
- leis sociais: 110%;
- refeição: R$ 30;
- transporte: R$ 10.

Resultados:

- ajudante geral: R$ 198,45;
- refeição: R$ 30,00;
- transporte: R$ 10,00;
- custo diário: R$ 238,45.

### Serviços e recursos — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Quantidade | Preço unitário | Total |
| --- | --- | ---: | ---: | ---: |
| 1 | Guindaste para carregamento | vazia | R$ 2.500,00 | R$ 0,00 |
| 2 | Treinamentos — trabalho em altura e espaço confinado | vazia | R$ 3.000,00 | R$ 0,00 |
| 3 | Mobiliário canteiro | vazia | R$ 3.500,00 | R$ 0,00 |
| 4 | Carreta carga seca para draga | vazia | R$ 2.500,00 | R$ 0,00 |
| 5 | Guindaste para descarregamento e montagem da draga | vazia | R$ 2.500,00 | R$ 0,00 |
| 6 | Frete | 1 | R$ 4.500,00 | R$ 4.500,00 |
| 7 | Trator D4 para lançar draga na água | vazia | R$ 2.000,00 | R$ 0,00 |
| 8 | Mão de obra para carga e montagem | 1 dia | R$ 238,45 | R$ 238,45 |

Observação `chute` na linha do guindaste.

### Fórmulas e resultados — EVIDÊNCIA CONFIRMADA

- custo diário da equipe: R$ 238,45;
- custo diário transferido para `E23`;
- subtotal: R$ 4.738,45;
- BDI interno: célula vazia, resultado R$ 0,00;
- preço final: R$ 4.738,45;
- repetição final em `F28`: R$ 4.738,45.

### Comentário da célula — EVIDÊNCIA CONFIRMADA

A célula `D23`, quantidade da mão de obra, possui comentário de `Aguinaldo`:

> 5 dias de mob

Apesar do comentário, a quantidade efetivamente usada é `1`.

### Regras implícitas — EVIDÊNCIA PARCIAL

- Desmobilização é pacote de evento único.
- Pode reutilizar a mesma estrutura de recursos da mobilização, ativando apenas itens aplicáveis.
- Mão de obra é apropriada pelo custo diário do bloco superior.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- Título interno: `1 - Mobilização da Draga 6"`, incompatível com desmobilização e com a numeração da aba.
- Descrições ainda mencionam `montagem`.
- `Trator D4 para lançar draga na água` é item típico de mobilização, não de retirada.
- O comentário indica 5 dias, mas a quantidade usada é 1.
- O preço de treinamento é R$ 3.000, diferente dos R$ 1.500 da mobilização, embora o item esteja inativo.
- O BDI interno está vazio, enquanto a consolidação aplica 30%.

### Dúvidas

- O frete de desmobilização de R$ 4.500 possui cotação?
- Deveriam ser considerados 5 dias de equipe?
- A mesma composição foi copiada da mobilização sem revisão integral?
- O barco ou a draga de 6" foi efetivamente mobilizado para o levantamento?

---

## 7. Aba `5. Plan. Preços`

### Objetivo

Consolidar os custos dos quatro pacotes e aplicar BDI comercial por item.

### Papel no fluxo

É a saída financeira final do arquivo.

### Estrutura e valores — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Custo total | Quantidade | Unidade | Custo unitário | BDI | Preço unitário | Preço total |
| ---: | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | Mobilização Barco | R$ 5.656,45 | 1 | un | R$ 5.656,45 | 30% | R$ 7.353,385 | R$ 7.353,385 |
| 3 | Batimetria Jasao | R$ 35.000,00 | 1 | m² | R$ 35.000,00 | 50% | R$ 52.500,00 | R$ 52.500,00 |
| 4 | Relatorio final | R$ 3.750,00 | 1 | m³ | R$ 3.750,00 | 30% | R$ 4.875,00 | R$ 4.875,00 |
| 8 | Desmobilização Barco | R$ 4.738,45 | 1 | un | R$ 4.738,45 | 30% | R$ 6.159,985 | R$ 6.159,985 |

### Fórmulas — EVIDÊNCIA CONFIRMADA

Para cada item:

```text
custo total = preço final da aba de composição
custo unitário = custo total ÷ quantidade
preço unitário = custo unitário × (1 + BDI)
preço total = quantidade × preço unitário
```

Referências:

- `C4 = '1. Mob. Equipe'!F30`
- `C5 = '2. Batimetria Jasao'!F19`
- `C6 = '3. Relatorio final'!F20`
- `C7 = '4. Desmob. Equipe'!F28`
- `C8 = SOMA(C5:C7)`
- `J8 = SOMA(J4:J7)`

### Resultados — EVIDÊNCIA CONFIRMADA

- soma exibida como `Custo Total`: **R$ 43.488,45**;
- preço total de venda: **R$ 70.888,37**;
- soma aritmética de todos os quatro custos: **R$ 49.144,90**;
- margem bruta nominal entre todos os custos e venda: **R$ 21.743,47**;
- multiplicador global de venda sobre todos os custos: aproximadamente **1,4424**;
- acréscimo global nominal sobre todos os custos: aproximadamente **44,24%**.

Os três últimos cálculos são derivações matemáticas da própria planilha e não representam regra consolidada da FOS.

### Regras explícitas — EVIDÊNCIA CONFIRMADA

- BDI de 30% para mobilização;
- BDI de 50% para batimetria;
- BDI de 30% para relatório final;
- BDI de 30% para desmobilização;
- preço final de venda é a soma dos quatro preços totais.

### Regras implícitas — EVIDÊNCIA PARCIAL

- O serviço principal de terceiro recebe BDI superior aos pacotes auxiliares.
- Cada pacote pode possuir BDI comercial independente.
- A planilha separa custo total, custo unitário, preço unitário e preço total mesmo quando quantidade é 1.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- `C8 = SOMA(C5:C7)` exclui o custo da mobilização em `C4`.
- Portanto, o valor rotulado `Custo Total` de R$ 43.488,45 não representa a soma dos quatro custos.
- `J8` inclui corretamente os quatro preços de venda.
- A numeração dos itens é descontínua: 1, 3, 4 e 8.
- Batimetria usa unidade `m²`, embora a composição de origem use `vb`.
- Relatório final usa unidade `m³`, embora a composição de origem use `vb`.
- Descrições de mobilização/desmobilização usam `Barco`, enquanto as abas internas alternam entre equipe, barco e draga.
- Os valores unitários de mobilização e desmobilização possuem três casas decimais.
- A coluna D está mesclada e vazia entre os dados, possivelmente como separador visual.

### Dúvidas

- O custo total deveria incluir a mobilização?
- As unidades `m²` e `m³` foram escolhidas para uma futura medição variável ou são resíduos?
- O item da batimetria deveria ser vendido como verba, campanha, lagoa, hectare ou metro quadrado?
- Os números 2, 5, 6 e 7 representam itens removidos ou estrutura herdada?
- O BDI de 50% da batimetria foi definido por risco, impostos, gestão do terceiro ou margem comercial?

---

# Dependências entre abas

## EVIDÊNCIA CONFIRMADA

| Origem | Destino | Informação |
| --- | --- | --- |
| `Dados Obra ` | `Produção` | horas por dia (`B26`) |
| `Dados Obra ` | `Produção` | volume total (`B14`) |
| `1. Mob. Equipe` | `5. Plan. Preços` | preço final de mobilização |
| `2. Batimetria Jasao` | `5. Plan. Preços` | preço final de batimetria |
| `3. Relatorio final` | `5. Plan. Preços` | preço final do relatório |
| `4. Desmob. Equipe` | `5. Plan. Preços` | preço final de desmobilização |

Não foram observadas dependências da aba `Produção` para qualquer composição financeira.

# Entidades encontradas

## EVIDÊNCIA CONFIRMADA

- proposta;
- cliente;
- contato;
- obra;
- localização;
- objeto;
- material;
- volume;
- levantamento batimétrico;
- fornecedor/executor;
- cotação;
- data da cotação;
- canal de comunicação da cotação;
- equipe;
- função de mão de obra;
- pessoa indicada;
- jornada;
- leis sociais;
- refeição;
- transporte;
- recurso de mobilização;
- documentação;
- frete;
- combustível;
- relatório final;
- arquivo DWG;
- coleta;
- análise de amostra;
- pacote de serviço;
- quantidade;
- unidade;
- custo;
- BDI;
- preço de venda;
- comentário de célula;
- observação de estimativa.

# Terminologias preservadas

## EVIDÊNCIA CONFIRMADA

- `Batimetria Lagoa Anaeróbica`
- `Lodo + Areia`
- `Seio da linha`
- `preços unitários de serviços`
- `Batimetria (JASAO)`
- `Preço passado`
- `Zap Jasao`
- `vb`
- `Mão de obra acompanhamento`
- `Relatorio Final (DWG, Adaptaçao , ETC)`
- `Coleta + Analise amostra`
- `chute`
- `BDI`
- `Preço Final`
- `Quantidade de Repetiçoes`

# Padrões observados somente neste orçamento

## EVIDÊNCIA PARCIAL — confiança Nível C

- Uso de uma composição superior de mão de obra e uma composição inferior de serviços em cada pacote.
- Cálculo de mão de obra com encargos sociais de 110%.
- Refeições e transporte dimensionados a partir da quantidade total de equipe.
- Pacotes de mobilização e desmobilização com estrutura quase espelhada.
- Serviço principal terceirizado precificado por cotação datada.
- BDI comercial individual por pacote.
- Preservação de linhas inativas com quantidade zero ou vazia.
- Reutilização de um modelo de dragagem para um orçamento cujo objeto principal é batimetria.
- Entrega de relatório e coleta/análise separadas da execução batimétrica.

Nenhum desses padrões deve ser promovido a regra geral da FOS sem crosscheck.

# Exceções e particularidades

## EVIDÊNCIA CONFIRMADA

- O volume e a vazão estão zerados.
- A aba de produção retorna `#DIV/0!`.
- A aba de produção não interfere no preço.
- A mobilização tem comentário de 5 dias, mas usa 1 dia.
- A desmobilização tem comentário de 5 dias, mas usa 1 dia.
- O custo total consolidado exclui mobilização.
- A venda total inclui mobilização.
- A batimetria tem BDI de 50%, superior aos demais pacotes.
- Diversos títulos internos pertencem aparentemente a outros tipos de serviço.
- Unidades comerciais não correspondem às unidades das composições de origem.

# Anomalias consolidadas

## EVIDÊNCIA CONFIRMADA

1. **Erro calculado visível:** prazo `#DIV/0!`.
2. **Total incompleto:** `C8` exclui a mobilização.
3. **Títulos incompatíveis:** preparo de célula, mobilização de draga e montagem de canteiro aparecem em abas de batimetria, relatório ou desmobilização.
4. **Comentários divergentes:** `5 dias de mob` versus quantidade 1.
5. **Unidades divergentes:** `vb` na origem versus `m²` ou `m³` na consolidação.
6. **Nomenclatura inconsistente:** equipe, barco e draga são usados para os mesmos pacotes.
7. **Numeração descontínua:** itens comerciais 1, 3, 4 e 8.
8. **Aba sem efeito financeiro:** `Produção`.
9. **Campo semanticamente incompatível:** `Tipo de Bota Fora = Batimetria`.
10. **Valores de entrada preservados sem uso:** custos de equipe do relatório, parâmetros de produção e vários recursos inativos.

# Conhecimentos específicos do arquivo

## EVIDÊNCIA CONFIRMADA

- Cotação de batimetria: R$ 35.000,00.
- Referência da cotação: 26/02/2025, via WhatsApp de `Jasao`.
- Custo do relatório final: R$ 3.500,00.
- Coleta + análise: R$ 250,00.
- Mobilização calculada: R$ 5.656,45.
- Desmobilização calculada: R$ 4.738,45.
- Venda total calculada: R$ 70.888,37.
- Material informado: lodo + areia.
- Local: Coronel Vivida - PR.

Esses valores pertencem a esta proposta e não devem ser considerados tabela vigente ou preço geral.

# Possíveis conhecimentos reutilizáveis

## EVIDÊNCIA PARCIAL — confiança Nível C

- Uma cotação deve preservar fornecedor, data e canal de origem.
- Serviços de batimetria podem exigir pacotes separados de mobilização, execução, relatório e desmobilização.
- Acompanhamento FOS pode existir como componente opcional.
- Quantidade de repetições pode representar múltiplas campanhas ou unidades de levantamento.
- Diferentes pacotes podem usar BDI distintos.
- Comentários de células podem conter premissas operacionais relevantes não refletidas nas fórmulas.

# Dúvidas para validação do especialista

1. Este orçamento foi efetivamente enviado ao cliente com valor de R$ 70.888,37?
2. O custo total deveria ser R$ 49.144,90, incluindo mobilização?
3. A mobilização e a desmobilização deveriam usar 5 dias de equipe?
4. O orçamento envolvia barco, draga de 6" ou apenas equipe de apoio?
5. Quem ou o que é `JASAO`?
6. A cotação de R$ 35.000 incluía relatório, deslocamentos e processamento?
7. Por que o relatório foi precificado separadamente?
8. Qual análise de amostra seria realizada?
9. A unidade correta da batimetria é verba, m², lagoa, campanha ou outra?
10. A unidade correta do relatório é verba?
11. O BDI de 50% da batimetria foi deliberado?
12. A aba `Produção` deveria ser ignorada neste tipo de orçamento?
13. `Penha` é a razão social completa do cliente?
14. O tipo de bota-fora `Batimetria` é apenas não aplicável?
15. `Peba` e `Leonardo` eram pessoas designadas para a obra?
16. Os preços marcados ou associados a `chute` foram substituídos antes da proposta?
17. O orçamento teve revisão posterior não indicada no nome do arquivo?

# Limitações da análise

## EVIDÊNCIA CONFIRMADA

- O arquivo não declara número formal de versão ou revisão.
- Não foram fornecidos anexos de cotação, proposta comercial emitida, mensagens de WhatsApp ou contrato.
- Não foi possível validar se os valores exibidos foram aceitos, revisados ou realizados.
- A análise identifica fórmulas e resultados armazenados no arquivo, mas não executa correção do Excel.
- A ferramenta `gh` não está instalada no ambiente e o `git clone` não pôde acessar a rede; a leitura e escrita do repositório foram realizadas exclusivamente pelo conector GitHub.
- A busca textual do conector não retornou listagem completa da pasta; os documentos relacionados foram localizados por caminhos declarados na documentação oficial.
- O `artifact_tool` normalizou visualmente o nome `Dados Obra ` sem o espaço final em algumas inspeções; a estrutura XML do próprio Excel confirmou o espaço final.

# Validação final

- [x] Todas as 7 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Fórmulas relevantes inventariadas.
- [x] Dependências entre abas registradas.
- [x] Comentários de células registrados.
- [x] Entidades, regras, padrões, exceções e dúvidas preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma consolidação entre orçamentos realizada.
- [x] Nenhum documento de outro orçamento alterado.
- [x] Nenhum índice geral alterado.
