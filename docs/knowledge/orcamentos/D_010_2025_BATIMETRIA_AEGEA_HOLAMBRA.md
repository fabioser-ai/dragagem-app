# D_010_2025 - Batimetria Aegea Holambra.xlsx — Batimetria de Lagoas de Aeração e Decantação

## Status

- **Status da análise:** CONCLUÍDA.
- **Data da análise:** 14/07/2026.
- **Arquivo analisado:** `D_010_2025 - Batimetria Aegea Holambra.xlsx`.
- **Versão do arquivo:** não identificada no nome, nas abas ou nas células examinadas.
- **Quantidade de abas:** 7.
- Todas as abas, tabelas, células preenchidas, fórmulas e dependências observáveis foram examinadas.
- Nenhuma funcionalidade, arquitetura, banco de dados, tela, consolidação ou decisão de implementação foi criada.
- Este documento preserva exclusivamente o conhecimento deste arquivo.

## Identidade permanente da fonte

- **Nome completo:** `D_010_2025 - Batimetria Aegea Holambra.xlsx`
- **Proposta registrada:** `Proposta D_010_2025`
- **Data registrada na planilha:** 26/02/2025
- **Cliente:** Aegea
- **Contato:** não preenchido
- **E-mail:** não preenchido
- **Objeto:** `Batimetria Lagoa Aeraçao e Decantaçao`
- **Local:** `Holambra - SP`
- **Material registrado:** `Lodo + Areia`
- **Volume de dragagem registrado:** 0 m³
- **Tipo de bota-fora:** `Batimetria`
- **Sistema de medição:** `preços unitários de serviços`
- **Responsabilidade pelo canteiro:** FOS
- **Responsabilidade pela mobilização:** FOS
- **Jornada:** 9 h/dia
- **Calendário:** 22 dias/mês
- **Preço de venda calculado:** R$ 19.985,543

## Regra de classificação usada neste registro

| Categoria solicitada | Uso neste documento |
| --- | --- |
| **EVIDÊNCIA CONFIRMADA** | Informação comprovada diretamente no Excel, inclusive a existência objetiva de anomalias. |
| **EVIDÊNCIA PARCIAL** | Interpretação ou regra implícita observada somente neste arquivo. |
| **DÚVIDA** | Informação sem comprovação suficiente ou cujo significado operacional não pode ser concluído apenas pelo Excel. |

Todas as possíveis regras reutilizáveis deste arquivo possuem confiança equivalente a **Nível C**, porque foram observadas em uma única fonte e não foram consolidadas.

# 1. Classificação do orçamento

## EVIDÊNCIA CONFIRMADA

O orçamento representa a prestação dos seguintes serviços em Holambra/SP:

1. mobilização de equipe/barco;
2. batimetria executada por fornecedor identificado como JASAO;
3. elaboração de relatório final;
4. desmobilização de equipe/barco.

A planilha comercial consolida esses quatro pacotes e aplica BDI individual por item.

O objeto registrado menciona batimetria de lagoa de aeração e lagoa de decantação.

## EVIDÊNCIA PARCIAL

A planilha aparenta ser um orçamento de **serviço técnico de levantamento batimétrico**, e não um orçamento de execução de dragagem, apesar de manter abas e premissas herdadas de modelos de dragagem.

Características que diferenciam este arquivo:

- volume de dragagem igual a zero;
- cálculo de produção da draga permanece no arquivo, mas não participa da formação do preço;
- não existe composição de operação mensal de dragagem;
- o principal serviço é uma contratação externa por verba;
- o relatório final é um pacote separado;
- a mobilização e a desmobilização são composições pequenas, baseadas em um ajudante geral e despesas individuais;
- o preço final é predominantemente determinado pela batimetria terceirizada.

## DÚVIDA

- O serviço envolve exclusivamente levantamento batimétrico ou também coleta de amostra, adaptação de desenho e outras entregas técnicas?
- A palavra `Barco` representa efetivamente uma embarcação própria da FOS, o equipamento do fornecedor ou apenas resíduo de nomenclatura?
- Por que a planilha preserva dados de recalque, linha flutuante, linha de terra e produção de draga em um orçamento de batimetria?
- O título do objeto deveria mencionar duas lagoas distintas ou uma única estrutura combinada?

# 2. Inventário das abas

| Ordem | Aba | Dimensão observada | Papel observado |
| --- | --- | --- | --- |
| 1 | `Dados Obra` | A1:H27 | Identificação da proposta e premissas gerais da obra. |
| 2 | `Produção` | A1:H24 | Cálculo de produção e prazo de dragagem, atualmente sem resultado útil. |
| 3 | `1. Mob. Equipe` | A1:G30 | Composição da mobilização de equipe/barco. |
| 4 | `2. Batimetria Jasao` | A1:G19 | Composição da batimetria terceirizada e eventual acompanhamento FOS. |
| 5 | `3. Relatorio final` | A1:F20 | Composição do relatório final e coleta/análise de amostra. |
| 6 | `4. Desmob. Equipe` | A1:G28 | Composição da desmobilização de equipe/barco. |
| 7 | `5. Plan. Preços` | A1:J8 | Consolidação de custo, BDI, preço unitário e preço total de venda. |

# 3. Fluxo completo observado

```text
Dados da obra
    ├── horas por dia e dias por mês → Produção
    └── volume de dragagem → Produção

Produção
    └── calcula produção e prazo, mas não alimenta a planilha comercial

Mobilização de equipe
    └── preço final → Planilha de Preços

Batimetria JASAO
    └── preço final → Planilha de Preços

Relatório final
    └── preço final → Planilha de Preços

Desmobilização de equipe
    └── preço final → Planilha de Preços

Planilha de Preços
    └── aplica BDI individual e calcula preço de venda
```

## EVIDÊNCIA CONFIRMADA

A única dependência comercial entre abas ocorre quando `5. Plan. Preços` importa os preços finais das quatro abas de composição.

A aba `Produção` recebe dados de `Dados Obra`, mas seu resultado não é referenciado por nenhuma aba de composição ou pela planilha comercial.

## EVIDÊNCIA PARCIAL

O fluxo de cálculo de produção parece ter sido preservado como estrutura padrão de outro tipo de orçamento, sem função econômica neste arquivo.

# 4. Convenção visual

## EVIDÊNCIA CONFIRMADA

A aba `Dados Obra` contém uma legenda:

- azul: dados a serem preenchidos;
- vermelho: informações pendentes;
- preto: resultados automáticos.

A legenda demonstra distinção visual entre entrada, pendência e cálculo automático.

## DÚVIDA

A inspeção confirmou a existência da legenda e das cores, mas este documento não classifica individualmente cada célula pela cor, pois o significado operacional é suficientemente preservado pelas fórmulas e pelos valores preenchidos.

---

# 5. Análise por aba

## 5.1. Aba `Dados Obra`

### Objetivo

Registrar a identidade comercial e as premissas gerais da obra.

### Papel no fluxo

É a origem das horas diárias, dias mensais e volume utilizados pela aba `Produção`. Também preserva diversas premissas que não alimentam nenhuma composição comercial deste arquivo.

### Entradas — EVIDÊNCIA CONFIRMADA

| Campo | Valor |
| --- | --- |
| Proposta | `Proposta D_010_2025` |
| Data | 26/02/2025 |
| Cliente | Aegea |
| Contato | vazio |
| E-mail | vazio |
| Objeto | `Batimetria Lagoa Aeraçao e Decantaçao` |
| Local | `Holambra - SP` |
| Volume dragagem | 0 m³ |
| Tipo de material | `Lodo + Areia` |
| Distância de recalque | 300 m |
| Seio da linha de recalque | 0 m |
| Total de recalque | 300 m |
| Linha flutuante | 200 m |
| Seio da linha flutuante | 0 m |
| Total de linha flutuante | 200 m |
| Linha de terra | 100 m |
| Profundidade de dragagem | vazio |
| Espessura média de dragagem | vazio |
| Dimensões/área de dragagem | vazias |
| Volume geométrico | 0 m³ |
| Tipo de bota-fora | `Batimetria` |
| Sistema de medição | `preços unitários de serviços` |
| Canteiro de obras | FOS |
| Mobilização | FOS |
| Horário de trabalho | 9 h/dia |
| Dias de trabalho | 22 dias/mês |

### Fórmulas — EVIDÊNCIA CONFIRMADA

- `H16 = B16 + E16`  
  Finalidade: calcular a distância total de recalque, incluindo o campo denominado `Seio da linha`.

- `H17 = B17 + E17`  
  Finalidade: calcular o total de linha flutuante, incluindo o campo denominado `Seio da linha`.

- `G21 = B21 × D21 × B20`  
  Finalidade: calcular volume geométrico a partir de duas dimensões e espessura média.

### Saídas

- recalque total: 300 m;
- linha flutuante total: 200 m;
- volume geométrico: 0 m³;
- horas diárias e dias mensais disponíveis para `Produção`.

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
- sistema de medição;
- responsabilidade operacional;
- jornada e calendário.

### Regras implícitas — EVIDÊNCIA PARCIAL

- Uma extensão total pode ser composta por comprimento principal mais `seio da linha`.
- A planilha admite duas fontes de volume: volume informado e volume geométrico.
- Responsabilidades por canteiro e mobilização são registradas como premissas, mesmo quando não alteram automaticamente as composições.
- O modelo conserva parâmetros típicos de dragagem mesmo quando o objeto é batimetria.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

1. `Tipo de Bota Fora` recebe o valor `Batimetria`, que não descreve claramente um local ou método de disposição.
2. O volume de dragagem é zero, embora vários campos de dragagem e recalque estejam preenchidos.
3. Profundidade, espessura e área estão vazias; portanto o volume geométrico permanece zero.
4. Contato e e-mail estão vazios.
5. O objeto apresenta grafia sem acentuação em `Aeraçao` e `Decantaçao`.

### Dúvidas

- `Batimetria` em `Tipo de Bota Fora` é valor intencional, marcador de “não aplicável” ou resíduo de edição?
- As distâncias de recalque são necessárias para o levantamento batimétrico?
- O material `Lodo + Areia` afeta preço, método ou apenas caracteriza o fundo?
- O volume zero é correto porque não haverá dragagem ou deveria haver volume estimado da lagoa?
- O cálculo geométrico deveria usar comprimento × largura × espessura, área × espessura, ou aceitar ambas as formas?

---

## 5.2. Aba `Produção`

### Objetivo

Calcular produção horária, horas mensais, produção mensal e prazo de execução de dragagem.

### Papel no fluxo

Recebe horas/dia, dias/mês e volume de `Dados Obra`. Não alimenta nenhuma composição de custo ou preço deste arquivo.

### Entradas — EVIDÊNCIA CONFIRMADA

| Variável | Valor |
| --- | ---: |
| Vazão | 0 m³/h |
| Eficiência | 65% |
| Concentração | 21% |
| Horas/dia | 9 |
| Dias/mês | 22 |
| Volume total | 0 m³ |

### Fórmulas — EVIDÊNCIA CONFIRMADA

- `H3 = 'Dados Obra '!B26`  
  Finalidade: importar horas trabalhadas por dia.

- `H6 = H3 × H4`  
  Finalidade: calcular horas trabalhadas por mês.

- `D8 = D3 × (D4/100) × (D5/100)`  
  Finalidade: transformar vazão, eficiência e concentração em produção horária útil.

- `D11 = H6`  
  Finalidade: repetir as horas mensais no bloco de produção.

- `D13 = D8 × D11`  
  Finalidade: calcular produção mensal.

- `D18 = D13`  
  Finalidade: repetir produção mensal no bloco de prazo.

- `D21 = 'Dados Obra '!B14`  
  Finalidade: importar o volume total a dragar.

- `D24 = D21 ÷ D18`  
  Finalidade: calcular prazo em meses.

### Resultados — EVIDÊNCIA CONFIRMADA

- horas mensais: 198 h/mês;
- produção horária: 0 m³/h;
- produção mensal: 0 m³/mês;
- volume total: 0 m³;
- prazo: `#DIV/0!`.

### Dependências

- recebe `Dados Obra!B26`;
- recebe `Dados Obra!B14`;
- usa o valor local de 22 dias/mês em `H4`;
- não fornece resultado a nenhuma outra aba.

### Entidades conceituais

- draga;
- vazão;
- eficiência;
- concentração;
- produção horária;
- jornada mensal;
- produção mensal;
- volume;
- prazo.

### Regras implícitas — EVIDÊNCIA PARCIAL

- A produção útil é calculada pela multiplicação direta de vazão, eficiência e concentração.
- O prazo é calculado por divisão simples entre volume e produção mensal.
- Não existe tratamento para produção zero ou volume zero.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

1. `D24` apresenta `#DIV/0!`.
2. A vazão é zero.
3. A aba não participa da formação do preço.
4. A fórmula de `H3` e a de `D21` referenciam literalmente uma aba escrita como `'Dados Obra '`, com espaço final no nome interno da referência.
5. O título menciona produção da draga em um orçamento classificado pelo objeto como batimetria.
6. O prazo não possui proteção por condição, valor padrão ou indicação de “não aplicável”.

### Dúvidas

- A aba deveria ter sido removida deste modelo ou deve continuar como referência para possível dragagem futura?
- Eficiência de 65% e concentração de 21% possuem alguma relação com a batimetria?
- Um prazo de serviço deveria ser informado diretamente para este tipo de orçamento?
- O erro `#DIV/0!` é aceito como consequência de bloco não utilizado ou foi deixado sem revisão?

---

## 5.3. Aba `1. Mob. Equipe`

### Objetivo

Compor o custo da mobilização de equipe/barco.

### Papel no fluxo

Calcula um preço final único, importado por `5. Plan. Preços`.

### Composição de mão de obra — EVIDÊNCIA CONFIRMADA

| Recurso | Quantidade | R$/h ou R$/un | Horas/dia | Leis sociais | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Operador Líder | vazio | 34,00 | 9 | 110% | 0,00 |
| Operador de Draga | vazio | 20,00 | 9 | 110% | 0,00 |
| Operador de preparo de polímero | vazio | 20,00 | 9 | 110% | 0,00 |
| Ajudante Geral | 1 | 10,50 | 9 | 110% | 198,45 |
| Refeições | 1 | 30,00 | — | — | 30,00 |
| Transporte | 1 | 10,00 | — | — | 10,00 |

Observação textual ao lado do ajudante: `Leonardo`.

O valor `Peba` aparece ao lado da linha de Operador Líder.

### Fórmulas da mão de obra — EVIDÊNCIA CONFIRMADA

Para os profissionais:

```text
quantidade × valor-hora × horas/dia
+ quantidade × valor-hora × horas/dia × leis sociais
```

Equivalente a:

```text
quantidade × valor-hora × horas/dia × (1 + leis sociais)
```

Fórmulas:

- `F5 = (A5×C5×D5) + (A5×C5×D5)×(E5/100)`
- `D6 = D5`
- `F6 = (A6×C6×D6) + (A6×C6×D6)×(E6/100)`
- `D7 = D6`
- `F7 = (A7×C7×D7) + (A7×C7×D7)×(E7/100)`
- `F8 = (A8×C8×D8) + (A8×C8×D8)×(E8/100)`
- `A9 = A5 + A8 + A6 + A7`
- `F9 = A9 × C9`
- `A10 = A9`
- `F10 = A10 × C10`
- `F11 = SOMA(F5:F10)`

### Resultado da mão de obra

- custo por dia: R$ 238,45.

### Serviços e recursos — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Unidade | Quantidade | Preço unitário | Total |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | Guindaste para carregamento | dia | vazio | 2.500,00 | 0,00 |
| 2 | Treinamentos — Trabalho em Altura e espaço confinado | dia | 0 | 1.500,00 | 0,00 |
| 3 | Mobiliário Canteiro | vb | vazio | 3.500,00 | 0,00 |
| 4 | Carreta Carga Seca para DRAGA | un | 0 | 2.500,00 | 0,00 |
| 5 | Guindaste para descarregamento e montagem DRAGA | dia | vazio | 2.500,00 | 0,00 |
| 6 | Documentação | vb | 1 | 1.000,00 | 1.000,00 |
| 7 | Combustivel + Frete | vb | 1 | 400,00 | 400,00 |
| 8 | Frete | vb | vazio | 5.000,00 | 0,00 |
| 9 | Trator D4 para lançar draga na água | dia | vazio | 2.000,00 | 0,00 |
| 10 | Mão de obra p/carga e montagem | dia | 1 | 238,45 | 238,45 |

Observação na linha do guindaste de descarregamento: `chute`.

### Fórmulas dos serviços — EVIDÊNCIA CONFIRMADA

- `F16 = D16 × E16`
- `F17 = D17 × E17`
- `F20 = D20 × E20`
- `F21 = D21 × E21`
- `F22 = D22 × E22`
- `F23 = D23 × E23`
- `E25 = F11`
- `F26 = SOMA(F16:F25)`
- `F27 = F26 × (E27/100)`
- `F28 = SOMA(F26:F27)`
- `F30 = SOMA(F28:F29)`

### Resultados — EVIDÊNCIA CONFIRMADA

- subtotal: R$ 1.638,45;
- BDI interno: 0%;
- preço final: R$ 1.638,45;
- preço final repetido em `F30`: R$ 1.638,45.

### Entidades conceituais

- evento de mobilização;
- equipe;
- função;
- salário-hora;
- jornada;
- leis sociais;
- refeição;
- transporte;
- documentação;
- combustível;
- frete;
- equipamento de içamento;
- carreta;
- trator;
- BDI.

### Regras implícitas — EVIDÊNCIA PARCIAL

- A quantidade total de refeições e transportes é derivada da soma das quantidades de profissionais.
- O custo diário da equipe pode ser utilizado como preço unitário de um item de serviço.
- Itens não utilizados permanecem na composição com quantidade vazia ou zero.
- O BDI da aba é separado do BDI comercial aplicado depois na planilha de preços.
- A mobilização é tratada como evento único na consolidação comercial.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

1. O título da aba é `Mob. Equipe`, mas o título interno é `Mobilização Barco`.
2. A composição conserva vários recursos específicos de mobilização de draga, embora apenas documentação, combustível/frete e mão de obra estejam ativos.
3. `Peba`, `Leonardo` e `chute` são textos sem classificação formal.
4. Há dois campos denominados `Preço Final`, em `F28` e `F30`.
5. A linha 29 está vazia, mas integra a soma `F30 = SOMA(F28:F29)`.
6. Algumas quantidades não utilizadas estão vazias e outras estão explicitamente em zero.
7. O preço de `Combustivel + Frete` é R$ 400, enquanto existe também uma linha separada de `Frete` por R$ 5.000.

### Dúvidas

- `Peba` é fornecedor, equipamento, pessoa, local ou observação?
- `Leonardo` identifica o ajudante designado ou a fonte do preço?
- `chute` significa estimativa sem cotação?
- O barco realmente requer guindaste, carreta e trator, ou essas linhas são resíduos do modelo de draga?
- Qual a diferença operacional entre `Combustivel + Frete` e `Frete`?
- A documentação de R$ 1.000 corresponde a qual entrega?

---

## 5.4. Aba `2. Batimetria Jasao`

### Objetivo

Compor o preço do serviço de batimetria contratado do fornecedor identificado como JASAO e permitir eventual custo de acompanhamento FOS.

### Papel no fluxo

Gera o maior custo individual do orçamento e alimenta `5. Plan. Preços`.

### Composição de mão de obra — EVIDÊNCIA CONFIRMADA

| Recurso | Quantidade | R$/h ou R$/un | Horas/dia | Leis sociais | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Operador Líder | vazio | 34,00 | 9 | 110% | 0,00 |
| Operador de Draga | vazio | 20,00 | 9 | 110% | 0,00 |
| Ajudante Geral | vazio | 10,00 | 9 | 110% | 0,00 |
| Refeições | 0 | 30,00 | — | — | 0,00 |
| Transporte | 0 | 10,00 | — | — | 0,00 |

- custo por dia: R$ 0,00.

### Fórmulas da mão de obra — EVIDÊNCIA CONFIRMADA

- `D5 = 'Dados Obra '!B26`
- `F5 = (A5×C5×D5) + (A5×C5×D5)×(E5/100)`
- `D6 = D5`
- `F6 = (A6×C6×D6) + (A6×C6×D6)×(E6/100)`
- `D7 = 'Dados Obra '!B26`
- `F7 = (A7×C7×D7) + (A7×C7×D7)×(E7/100)`
- `A8 = A5 + A7 + A6`
- `F8 = A8 × C8`
- `A9 = A8`
- `F9 = A9 × C9`
- `F10 = SOMA(F5:F9)`

### Serviços — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Unidade | Quantidade | Preço unitário | Total |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | Batimetria (JASAO) | vb | 1 | 11.500,00 | 11.500,00 |
| 2 | Mão de obra acompanhameto (FOS) | dia | 1 | 0,00 | 0,00 |

Observação da batimetria:

`Preço passado 26/02/2025 - Zap Jasao`

### Fórmulas dos serviços — EVIDÊNCIA CONFIRMADA

- `F15 = D15 × E15`
- `E16 = F10`
- `F17 = SOMA(F15:F16)`
- `F18 = F17 × E18`
- `F19 = F18`

### Resultados — EVIDÊNCIA CONFIRMADA

- total: R$ 11.500,00;
- quantidade de repetições: 1;
- preço após repetições: R$ 11.500,00;
- preço final: R$ 11.500,00.

### Entidades conceituais

- fornecedor de batimetria;
- cotação;
- data-base;
- canal de cotação;
- verba;
- acompanhamento FOS;
- repetição do serviço.

### Regras implícitas — EVIDÊNCIA PARCIAL

- A batimetria é precificada por verba no fornecedor.
- O custo pode ser multiplicado por uma quantidade de repetições.
- O acompanhamento FOS pode ser inserido como número de dias multiplicado pelo custo diário da equipe.
- A cotação possui rastreabilidade mínima de data e canal.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

1. O título interno da aba é `3. PREPARO DE CÉLULA - Manta PEAD`, incompatível com o conteúdo de batimetria.
2. O número `3` no título interno não corresponde ao número `2` da aba.
3. O cabeçalho da equipe menciona `montagem canteiro`, sem relação direta explícita com batimetria.
4. O fornecedor está grafado `Jasao`/`JASAO`, sem identificação empresarial completa.
5. `acompanhameto` está grafado sem `n`.
6. A quantidade do acompanhamento FOS é 1 dia, mas o preço unitário é zero.
7. A fórmula `F18 = F17 × E18` usa a célula de preço unitário da linha `Quantidade de Repetiçoes` para armazenar o multiplicador.
8. Não existe BDI interno nesta aba; a multiplicação por repetição ocupa a linha equivalente.
9. A unidade comercial posterior é `m²`, embora a composição de origem use `vb`.

### Dúvidas

- O preço de R$ 11.500 cobre uma lagoa, duas lagoas ou todo o escopo?
- O nome correto do fornecedor é JASAO, Jasão ou outra razão social?
- O serviço possui área mensurável, mas foi cotado por verba?
- Em quais situações a quantidade de repetições seria maior que 1?
- Por que o acompanhamento FOS tem um dia e custo zero?
- A cotação enviada por WhatsApp foi formalizada em proposta, e-mail ou documento?

---

## 5.5. Aba `3. Relatorio final`

### Objetivo

Compor custos ligados à elaboração do relatório final e à coleta/análise de amostra.

### Papel no fluxo

Gera um preço final único importado por `5. Plan. Preços`.

### Composição de mão de obra — EVIDÊNCIA CONFIRMADA

| Recurso | Quantidade | R$/h ou R$/un | Horas/dia | Leis sociais | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Engenheiro | 1 | 50,00 | 9 | 110% | 945,00 |
| Operador de Draga | vazio | 20,00 | 9 | 110% | 0,00 |
| Operador de preparo de polímero | vazio | 20,00 | 9 | 110% | 0,00 |
| Ajudante Geral | vazio | 10,00 | 9 | 110% | 0,00 |
| Refeições | vazio | 30,00 | — | — | 0,00 |
| Transporte | 0 | 10,00 | — | — | 0,00 |

- custo por dia: R$ 945,00.

### Fórmulas da mão de obra — EVIDÊNCIA CONFIRMADA

- `F5 = (A5×C5×D5) + (A5×C5×D5)×(E5/100)`
- `D6 = D5`
- `F6 = (A6×C6×D6) + (A6×C6×D6)×(E6/100)`
- `D7 = D6`
- `F7 = (A7×C7×D7) + (A7×C7×D7)×(E7/100)`
- `F8 = (A8×C8×D8) + (A8×C8×D8)×(E8/100)`
- `F9 = A9 × C9`
- `A10 = A9`
- `F10 = A10 × C10`
- `F11 = SOMA(F5:F10)`

### Serviços — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Unidade | Quantidade | Preço unitário | Total |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | Relatorio Final (DWG, Adaptaçao , ETC) | vb | 1 | 0,00 | 0,00 |
| 2 | Coleta + Analise amostra | dia | 1 | 250,00 | 250,00 |

### Fórmulas dos serviços — EVIDÊNCIA CONFIRMADA

- `F16 = D16 × E16`
- `F18 = SOMA(F16:F17)`
- `F19 = F18 × (E19/100)`
- `F20 = SOMA(F18:F19)`

### Resultados — EVIDÊNCIA CONFIRMADA

- total: R$ 250,00;
- BDI interno: 0%;
- preço final: R$ 250,00.

### Entidades conceituais

- relatório final;
- engenheiro;
- desenho DWG;
- adaptação;
- coleta;
- amostra;
- análise;
- BDI.

### Regras implícitas — EVIDÊNCIA PARCIAL

- O custo de engenharia pode ser calculado na parte de mão de obra, mas não é transferido automaticamente para o item `Relatorio Final`.
- O relatório é tratado como verba.
- Coleta e análise de amostra são agregadas em uma única linha e precificadas por dia.
- O BDI interno é separado do BDI comercial da consolidação.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

1. A mão de obra do engenheiro custa R$ 945,00 por dia, mas não é incorporada ao preço final.
2. O item `Relatorio Final` possui quantidade 1 e preço unitário zero.
3. O preço final de R$ 250,00 decorre exclusivamente de `Coleta + Analise amostra`.
4. O cabeçalho da equipe menciona `montagem canteiro`.
5. Permanecem linhas de Operador de Draga e Operador de preparo de polímero sem função aparente no escopo.
6. A unidade comercial posterior do relatório é `m³`, embora a composição de origem use `vb`.
7. Grafias: `Relatorio`, `Adaptaçao`, `Analise`.

### Dúvidas

- O custo do engenheiro deveria compor o relatório final?
- O valor de R$ 250 inclui laboratório, deslocamento, coleta e emissão de laudo?
- O relatório em DWG é entregue pelo fornecedor de batimetria ou elaborado pela FOS?
- A unidade `m³` na planilha comercial é intencional?
- O relatório final foi considerado sem custo por estar incluído na cotação da batimetria?

---

## 5.6. Aba `4. Desmob. Equipe`

### Objetivo

Compor o custo da desmobilização de equipe/barco.

### Papel no fluxo

Calcula preço final único importado por `5. Plan. Preços`.

### Composição de mão de obra — EVIDÊNCIA CONFIRMADA

| Recurso | Quantidade | R$/h ou R$/un | Horas/dia | Leis sociais | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Operador Líder | vazio | 34,00 | 9 | 110% | 0,00 |
| Operador de Draga | vazio | 20,00 | 9 | 110% | 0,00 |
| Operador de preparo de polímero | vazio | 20,00 | 9 | 110% | 0,00 |
| Ajudante Geral | 1 | 10,50 | 9 | 110% | 198,45 |
| Refeições | 1 | 30,00 | — | — | 30,00 |
| Transporte | 1 | 10,00 | — | — | 10,00 |

- custo por dia: R$ 238,45.

### Fórmulas da mão de obra — EVIDÊNCIA CONFIRMADA

- `F5 = (A5×C5×D5) + (A5×C5×D5)×(E5/100)`
- `D6 = D5`
- `F6 = (A6×C6×D6) + (A6×C6×D6)×(E6/100)`
- `D7 = D6`
- `F7 = (A7×C7×D7) + (A7×C7×D7)×(E7/100)`
- `F8 = (A8×C8×D8) + (A8×C8×D8)×(E8/100)`
- `A9 = A5 + A8 + A6 + A7`
- `F9 = A9 × C9`
- `A10 = A9`
- `F10 = A10 × C10`
- `F11 = SOMA(F5:F10)`

### Serviços e recursos — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Unidade | Quantidade | Preço unitário | Total |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | Guindaste para carregamento | dia | vazio | 2.500,00 | 0,00 |
| 2 | Treinamentos — Trabalho em Altura e espaço confinado | dia | vazio | 3.000,00 | 0,00 |
| 3 | Mobiliário Canteiro | vb | vazio | 3.500,00 | 0,00 |
| 4 | Carreta Carga Seca para DRAGA | un | vazio | 2.500,00 | 0,00 |
| 5 | Guindaste para descarregamento e montagem DRAGA | dia | vazio | 2.500,00 | 0,00 |
| 6 | Frete | vb | vazio | 5.000,00 | 0,00 |
| 7 | Trator D4 para lançar draga na água | dia | vazio | 2.000,00 | 0,00 |
| 8 | Mão de obra p/carga e montagem | dia | 1 | 238,45 | 238,45 |

Observação na linha do guindaste de descarregamento: `chute`.

### Fórmulas dos serviços — EVIDÊNCIA CONFIRMADA

- `F16 = D16 × E16`
- `F17 = D17 × E17`
- `F20 = D20 × E20`
- `F21 = D21 × E21`
- `E23 = F11`
- `F24 = SOMA(F16:F23)`
- `F25 = F24 × (E25/100)`
- `F26 = SOMA(F24:F25)`
- `F28 = SOMA(F26:F27)`

### Resultados — EVIDÊNCIA CONFIRMADA

- subtotal: R$ 238,45;
- BDI interno: 0%;
- preço final: R$ 238,45;
- preço final repetido: R$ 238,45.

### Entidades conceituais

As mesmas entidades de mobilização, aplicadas ao evento de retirada.

### Regras implícitas — EVIDÊNCIA PARCIAL

- A desmobilização usa a mesma lógica de custo de equipe da mobilização.
- A maior parte da estrutura de recursos permanece disponível, porém inativa.
- O custo ativo é exclusivamente um dia de ajudante, refeição e transporte.
- O BDI interno é separado do BDI comercial posterior.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

1. O título interno é `Mobilização da Draga 6"`, embora a aba seja de desmobilização de equipe.
2. O preço de treinamento é R$ 3.000, enquanto na mobilização é R$ 1.500.
3. O treinamento aparece na desmobilização, mas está sem quantidade.
4. O texto do item de mão de obra continua `carga e montagem`, não retirada/desmontagem.
5. O guindaste menciona `descarregamento e montagem`, incompatível com desmobilização.
6. Há dois campos de `Preço Final`.
7. A linha 27 está vazia, mas integra a soma final.
8. A composição não inclui documentação nem combustível, ao contrário da mobilização.

### Dúvidas

- A desmobilização deveria usar `desmontagem e carregamento`?
- Por que o título menciona draga de 6" se o objeto é batimetria?
- A ausência de combustível/frete é intencional?
- O valor de treinamento diferente é resíduo ou preço distinto?
- O barco/equipamento necessita dos recursos listados?

---

## 5.7. Aba `5. Plan. Preços`

### Objetivo

Consolidar custos das quatro composições, definir quantidade e unidade comercial, aplicar BDI individual e calcular preço de venda.

### Papel no fluxo

É a saída econômica final do arquivo.

### Estrutura — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Custo Total | Quant. | Unidade | Custo Unitário | BDI | Preço Unitário | Preço Total |
| ---: | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | Mobilizaçao Barco | 1.638,45 | 1 | un | 1.638,45 | 47% | 2.408,5215 | 2.408,5215 |
| 3 | Batimetria Jasao | 11.500,00 | 1 | m² | 11.500,00 | 46,6% | 16.859,00 | 16.859,00 |
| 4 | Relatorio final | 250,00 | 1 | m³ | 250,00 | 47% | 367,50 | 367,50 |
| 8 | Desmobilização Barco | 238,45 | 1 | un | 238,45 | 47% | 350,5215 | 350,5215 |

### Fórmulas — EVIDÊNCIA CONFIRMADA

Mobilização:

- `C4 = '1. Mob. Equipe'!F30`
- `G4 = C4 ÷ E4`
- `I4 = ((H4/100)+1) × G4`
- `J4 = E4 × I4`

Batimetria:

- `C5 = '2. Batimetria Jasao'!F19`
- `G5 = C5 ÷ E5`
- `I5 = ((H5/100)+1) × G5`
- `J5 = E5 × I5`

Relatório:

- `C6 = '3. Relatorio final'!F20`
- `G6 = C6 ÷ E6`
- `I6 = ((H6/100)+1) × G6`
- `J6 = E6 × I6`

Desmobilização:

- `C7 = '4. Desmob. Equipe'!F28`
- `G7 = C7 ÷ E7`
- `I7 = ((H7/100)+1) × G7`
- `J7 = E7 × I7`

Totais:

- `C8 = SOMA(C5:C7)`
- `J8 = SOMA(J4:J7)`

### Finalidade das fórmulas

- `C`: importar custo total de cada pacote;
- `G`: transformar custo total em custo unitário;
- `I`: aplicar BDI ao custo unitário;
- `J`: multiplicar preço unitário pela quantidade;
- `J8`: somar todos os preços de venda.

### Resultados — EVIDÊNCIA CONFIRMADA

- soma exibida como `Custo Total`: R$ 11.988,45;
- preço de venda: R$ 19.985,543;
- custo real dos quatro itens, calculado pela soma de `C4:C7`: R$ 13.626,90;
- acréscimo absoluto entre custo real dos quatro itens e venda: R$ 6.358,643;
- relação preço de venda/custo real: aproximadamente 1,46662;
- margem sobre o preço de venda, considerando os quatro custos listados: aproximadamente 31,815%.

Os dois últimos percentuais são cálculos derivados para documentar a relação entre os valores presentes; não são fórmulas existentes no Excel.

### Entidades conceituais

- item comercial;
- descrição;
- custo total;
- quantidade;
- unidade de venda;
- custo unitário;
- BDI;
- preço unitário;
- preço total;
- preço de venda.

### Regras implícitas — EVIDÊNCIA PARCIAL

- Cada pacote pode ter BDI próprio.
- O BDI comercial é aplicado sobre o custo unitário.
- Quantidade e unidade são definidas novamente na consolidação, independentemente da unidade da composição de origem.
- Mobilização e desmobilização são vendidas como unidade.
- Batimetria e relatório podem ser apresentados em unidades físicas, mesmo quando o custo de origem é verba.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

1. `C8 = SOMA(C5:C7)` exclui a mobilização em `C4`.
2. Consequentemente, o `Custo Total` exibido, R$ 11.988,45, não é o custo total dos quatro itens.
3. O custo correto pela soma das quatro linhas é R$ 13.626,90.
4. O preço de venda `J8` inclui os quatro itens.
5. A base de custo e a base de venda exibidas no rodapé não são diretamente comparáveis.
6. A unidade da batimetria é `m²`, mas sua quantidade é 1 e a composição de origem é `vb`.
7. A unidade do relatório é `m³`, mas sua quantidade é 1 e a composição de origem é `vb`.
8. Os itens são numerados 1, 3, 4 e 8, com lacunas.
9. A batimetria usa BDI de 46,6%, enquanto os demais itens usam 47%.
10. O título `Preços com BDI` aparece apenas sobre as colunas finais, sem explicar a diferença de BDI.
11. O preço final possui mais de duas casas decimais.
12. Não existe linha de impostos, desconto, contingência, arredondamento ou total por extenso.

### Dúvidas

- A exclusão da mobilização em `C8` é erro de fórmula ou decisão para exibir apenas custos de execução?
- Por que o BDI da batimetria é 46,6%?
- As unidades `m²` e `m³` são exigências do cliente ou resíduos de outro orçamento?
- O preço comercial deveria ser arredondado?
- As lacunas de numeração indicam itens removidos da proposta?
- A margem é controlada apenas por BDI ou existe composição externa do BDI?

---

# 6. Dependências entre abas

## EVIDÊNCIA CONFIRMADA

| Origem | Destino | Dados transferidos |
| --- | --- | --- |
| `Dados Obra` | `Produção` | horas/dia e volume total |
| `1. Mob. Equipe` | `5. Plan. Preços` | preço final da mobilização |
| `2. Batimetria Jasao` | `5. Plan. Preços` | preço final da batimetria |
| `3. Relatorio final` | `5. Plan. Preços` | preço final do relatório |
| `4. Desmob. Equipe` | `5. Plan. Preços` | preço final da desmobilização |

Não foram observadas:

- dependências da aba `Produção` para as composições;
- dependências entre mobilização, batimetria, relatório e desmobilização;
- nomes definidos;
- comentários estruturados do Excel;
- gráficos ou outros desenhos;
- tabelas formais do Excel.

# 7. Fórmulas e regras transversais

## 7.1. Custo de mão de obra com leis sociais — EVIDÊNCIA CONFIRMADA

Aplicado repetidamente nas abas de composição:

```text
custo = quantidade × valor-hora × horas/dia × (1 + leis sociais/100)
```

Leis sociais utilizadas: 110%.

## 7.2. Refeição e transporte — EVIDÊNCIA CONFIRMADA

A quantidade é derivada da soma das quantidades de profissionais e multiplicada pelo custo por pessoa.

Neste arquivo:

- refeição: R$ 30;
- transporte: R$ 10.

## 7.3. Serviço por quantidade — EVIDÊNCIA CONFIRMADA

```text
preço total = quantidade × preço unitário
```

## 7.4. BDI interno — EVIDÊNCIA CONFIRMADA

Nas abas que possuem linha de BDI:

```text
BDI interno = subtotal × percentual / 100
preço final = subtotal + BDI interno
```

Todos os BDIs internos ativos estão em 0%.

## 7.5. BDI comercial — EVIDÊNCIA CONFIRMADA

Na planilha final:

```text
preço unitário = custo unitário × (1 + BDI/100)
preço total = quantidade × preço unitário
```

## 7.6. Repetição da batimetria — EVIDÊNCIA CONFIRMADA

```text
preço final da batimetria = total do pacote × quantidade de repetições
```

Quantidade usada: 1.

## 7.7. Valores vazios e zeros — EVIDÊNCIA PARCIAL

O arquivo utiliza tanto células vazias quanto zero para desativar recursos. As duas formas resultam em custo zero nas fórmulas aritméticas, mas carregam significados potencialmente diferentes que não podem ser comprovados:

- vazio pode representar não preenchido ou não aplicável;
- zero pode representar decisão explícita de não usar.

# 8. Entidades encontradas

## EVIDÊNCIA CONFIRMADA

### Comerciais

- proposta;
- cliente;
- contato;
- objeto;
- local;
- item comercial;
- unidade;
- custo;
- BDI;
- preço de venda.

### Técnicas

- batimetria;
- lagoa de aeração;
- lagoa de decantação;
- material de fundo;
- recalque;
- linha flutuante;
- linha de terra;
- profundidade;
- área;
- volume;
- draga;
- barco;
- relatório;
- desenho DWG;
- amostra.

### Recursos humanos

- engenheiro;
- operador líder;
- operador de draga;
- operador de preparo de polímero;
- ajudante geral.

### Recursos e serviços

- refeição;
- transporte;
- guindaste;
- carreta;
- mobiliário;
- documentação;
- combustível;
- frete;
- trator;
- treinamento;
- coleta;
- análise;
- fornecedor de batimetria.

### Parâmetros econômicos

- salário-hora;
- leis sociais;
- custo diário;
- preço unitário;
- quantidade;
- subtotal;
- BDI interno;
- BDI comercial;
- preço final.

# 9. Terminologia observada

| Termo | Uso no arquivo | Classificação |
| --- | --- | --- |
| `vb` | verba, usada como unidade de pacotes | EVIDÊNCIA CONFIRMADA |
| `Seio da linha` | parcela adicionada ao comprimento da linha | EVIDÊNCIA CONFIRMADA quanto à fórmula; significado operacional é DÚVIDA |
| `JASAO` | identificação do fornecedor de batimetria | EVIDÊNCIA CONFIRMADA quanto ao texto; razão social é DÚVIDA |
| `chute` | observação em preço de guindaste | EVIDÊNCIA CONFIRMADA quanto ao texto; significado presumido de estimativa é EVIDÊNCIA PARCIAL |
| `Peba` | anotação na mobilização | EVIDÊNCIA CONFIRMADA quanto ao texto; significado é DÚVIDA |
| `Leonardo` | anotação junto ao ajudante | EVIDÊNCIA CONFIRMADA quanto ao texto; significado é DÚVIDA |
| `Preço passado ... Zap` | registro informal de data e canal de cotação | EVIDÊNCIA CONFIRMADA |

# 10. Cotações, referências e valores datados

## EVIDÊNCIA CONFIRMADA

A única referência explícita de data e origem de preço é:

- serviço: Batimetria (JASAO);
- valor: R$ 11.500;
- data: 26/02/2025;
- canal: WhatsApp, escrito como `Zap Jasao`.

Os demais preços não possuem data-base ou fonte identificada dentro do arquivo.

## DÚVIDA

- Os salários-hora são tabela interna, preço histórico ou valor específico da proposta?
- Os preços de guindaste, carreta, treinamento, mobiliário, frete e trator possuem cotações externas?
- Os valores de refeição e transporte são reembolso, diária ou média histórica?

# 11. Anomalias consolidadas

## EVIDÊNCIA CONFIRMADA

### Fórmula quebrada

- `Produção!D24` apresenta `#DIV/0!`.

### Total de custo inconsistente

- `5. Plan. Preços!C8` exclui a mobilização;
- o rótulo `Custo Total` mostra R$ 11.988,45;
- a soma de todos os custos listados é R$ 13.626,90;
- o preço de venda inclui todos os itens.

### Estruturas herdadas

- título de preparo de célula na aba de batimetria;
- título de mobilização de draga na aba de desmobilização;
- recursos de draga e polímero em orçamento de batimetria;
- cálculo de produção de draga sem uso comercial;
- cabeçalhos de montagem de canteiro em outras atividades.

### Unidades incompatíveis ou não demonstradas

- batimetria: origem `vb`, venda `m²`, quantidade 1;
- relatório: origem `vb`, venda `m³`, quantidade 1.

### Custos calculados mas não incorporados

- mão de obra do engenheiro: R$ 945/dia;
- preço final do relatório: R$ 250;
- não existe fórmula que transfira R$ 945 para o pacote.

### Nomenclaturas e grafias

- títulos internos divergentes;
- numeração comercial com lacunas;
- textos informais sem campo estruturado;
- grafias sem acentuação ou com erro.

### Precisão monetária

- preços finais de mobilização e desmobilização têm quatro casas decimais após BDI;
- preço total geral mantém casas além de centavos;
- não há regra visível de arredondamento.

# 12. Padrões observados exclusivamente neste arquivo

## EVIDÊNCIA PARCIAL

1. Um orçamento de batimetria pode ser formado por quatro eventos autônomos: mobilização, levantamento, relatório e desmobilização.
2. O levantamento pode ser contratado por verba e revendido com BDI individual.
3. Mobilização e desmobilização podem ser simplificadas para um único ajudante mais refeição e transporte.
4. A entrega de relatório pode ser separada da execução da batimetria.
5. A planilha pode preservar blocos de dragagem não utilizados para manter um modelo-base.
6. O acompanhamento FOS pode existir como linha opcional de custo.
7. A quantidade de repetições permite multiplicar o serviço terceirizado.
8. BDIs podem variar por pacote dentro da mesma proposta.

Nenhum desses itens deve ser tratado como regra geral da FOS sem crosscheck futuro.

# 13. Exceções específicas deste arquivo

## EVIDÊNCIA CONFIRMADA

- volume de dragagem igual a zero;
- ausência de operação de dragagem na formação do preço;
- prazo indefinido por divisão por zero;
- batimetria terceirizada por verba;
- relatório com custo final inferior ao custo diário de engenheiro calculado;
- mobilização contendo documentação e combustível/frete;
- desmobilização contendo apenas mão de obra ativa;
- BDI de 46,6% exclusivamente na batimetria;
- custo total final excluindo mobilização;
- unidades comerciais não sustentadas pelas composições de origem.

# 14. Conhecimentos específicos do orçamento

## EVIDÊNCIA CONFIRMADA

- Cliente Aegea.
- Local Holambra/SP.
- Objeto relacionado a lagoas de aeração e decantação.
- Fundo caracterizado como lodo e areia.
- Fornecedor de batimetria identificado como JASAO.
- Cotação da batimetria no valor de R$ 11.500 em 26/02/2025.
- Preço de venda calculado em R$ 19.985,543.
- Mobilização calculada em R$ 1.638,45.
- Relatório calculado em R$ 250.
- Desmobilização calculada em R$ 238,45.
- Todos os itens comerciais possuem quantidade 1.

# 15. Dúvidas consolidadas para validação futura

1. Qual é o escopo técnico exato da batimetria?
2. Quantas lagoas estão incluídas na cotação?
3. Qual é a área efetiva levantada?
4. Por que a unidade comercial é m² com quantidade 1?
5. Por que o relatório é vendido em m³?
6. O relatório está incluído no preço da JASAO?
7. O custo do engenheiro deveria ser incorporado?
8. A coleta e análise de amostra realmente fazem parte da batimetria?
9. Quem ou o que são `Peba` e `Leonardo`?
10. `chute` indica preço estimado?
11. Quais recursos efetivamente foram mobilizados?
12. Por que existe produção de draga neste orçamento?
13. As distâncias de linha são relevantes?
14. `Batimetria` no campo bota-fora significa “não aplicável”?
15. O total de custo deve incluir a mobilização?
16. Qual é a origem do BDI de 46,6%?
17. Deve haver arredondamento monetário para centavos?
18. Os itens ausentes da numeração comercial foram removidos de uma versão anterior?
19. O arquivo teve origem em cópia de outro orçamento?
20. Existe proposta ou relatório externo associado a esta planilha?

# 16. Limitações da análise

## EVIDÊNCIA CONFIRMADA

- A análise foi limitada ao conteúdo do arquivo Excel fornecido.
- Não foram fornecidas propostas comerciais, cotações anexas, conversas, relatórios, desenhos ou validações do especialista.
- A versão do arquivo não está identificada.
- O arquivo não contém comentários estruturados, nomes definidos, gráficos ou tabelas formais detectáveis.
- As células vazias não permitem distinguir com certeza “não aplicável”, “não utilizado” e “pendente”.
- Textos informais foram preservados sem atribuição de significado não comprovado.
- Não foi feita comparação decisória com outros orçamentos.
- Não foi realizada consolidação da Base de Conhecimento.
- Não foram alterados índices, documentos compartilhados ou registros de outros orçamentos.

# 17. Checklist de validação

- [x] Todas as 7 abas analisadas.
- [x] Todas as fórmulas observáveis registradas e explicadas.
- [x] Dependências entre abas registradas.
- [x] Entradas, saídas, entidades, regras, exceções e anomalias preservadas.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma consolidação realizada.
- [x] Nenhum documento pertencente a outro orçamento alterado.
- [x] Nenhum índice geral atualizado.

# 18. Resultado da análise

A engenharia reversa vertical de `D_010_2025 - Batimetria Aegea Holambra.xlsx` está concluída.

O arquivo documenta um orçamento aparente de levantamento batimétrico com forte reaproveitamento de uma estrutura de orçamento de dragagem. A formação comercial utiliza quatro pacotes, sendo a batimetria terceirizada o componente dominante. O arquivo contém elementos suficientes para reproduzir os valores calculados, mas preserva inconsistências, estruturas inativas e questões operacionais que exigem validação futura.

Todas as conclusões permanecem restritas a esta fonte.
