# Registro de descoberta — `Motobomba 3Barras - Westrock.xlsx`

## 1. Identificação da análise

- **Nome completo da fonte:** `Motobomba 3Barras - Westrock.xlsx`
- **Data da análise:** 2026-07-14
- **Versão declarada no nome do arquivo:** não existe indicação explícita de versão.
- **Identificador interno da proposta:** `D_040_2025`.
- **Data registrada na planilha:** 2025-07-02.
- **Cliente:** WESTROCK.
- **Local:** Tres Barras.
- **Quantidade de abas:** 3.
- **Abas, na ordem do arquivo:** `Dados Obra `, `MOTOBOMBA`, `10. Plan. Preços`.
- **Observação de identidade da primeira aba:** o nome armazenado no Excel contém um espaço ao final: `Dados Obra `.
- **Tamanho do arquivo analisado:** 17.734 bytes.
- **SHA-256 da fonte analisada:** `91b9518652bd9ccfacf48ceff5c46ad113dcefdbd676266ecf8f9b493f04f4d6`.
- **Criador registrado nos metadados:** `user`.
- **Último modificador registrado:** `Fabio  Pereira Serafini`.
- **Criação registrada nos metadados:** 2010-07-15T18:27:10Z.
- **Última modificação registrada nos metadados:** 2025-07-02T18:41:54Z.
- **Aplicativo gravador registrado:** Microsoft Macintosh Excel.
- **Status da análise:** concluída para a fonte recebida; dúvidas operacionais permanecem abertas para esclarecimento do especialista.
- **Documento exclusivo:** este registro descreve somente `Motobomba 3Barras - Westrock.xlsx`.

### Classificação da identificação

- **EVIDÊNCIA CONFIRMADA — Fato observado:** todos os dados acima foram obtidos diretamente do arquivo Excel e de seus metadados internos.
- **EVIDÊNCIA PARCIAL — Interpretação:** a data 2025-07-02 parece ser a data da proposta, pois está no campo visual “Data”; o arquivo não apresenta campo separado de revisão.
- **DÚVIDA:** não foi encontrada indicação que permita afirmar se este é o arquivo final enviado ao cliente, uma memória interna de cálculo ou uma revisão intermediária.

## 2. Classificação aparente do orçamento

- **Tipo aparente:** orçamento de locação e operação de motobomba, com mobilização, startup, desmobilização, hospedagem e uma atividade adicional de instalação de Bidim e brita.
- **Processo operacional representado:** preparação/montagem, disponibilização e operação de motobomba, apoio de mão de obra, mobilização e desmobilização.
- **Área de atuação aparente:** bombeamento de lodo de ETA em sistema de bombeamento direto.
- **Forma comercial aparente:** preços unitários de serviços, apresentados em três itens comerciais com unidade `vb`.
- **Característica distintiva:** embora a aba de dados use termos herdados de dragagem — volume de dragagem, profundidade, espessura e área — o objeto efetivamente orçado é “Locaçao Motobomba”, sem cálculo de produção ou prazo baseado em volume.

### Classificação das evidências

- **EVIDÊNCIA CONFIRMADA — Fato observado:** o objeto, o cliente, o local, o material, o tipo de bota-fora, o sistema de medição e os itens de custo estão escritos no arquivo.
- **EVIDÊNCIA PARCIAL — Interpretação:** o orçamento representa uma família operacional mais simples que uma obra completa de dragagem, pois não dimensiona produção, volume, prazo, combustível, tubulação ou equipamento de dragagem.
- **DÚVIDA:** o arquivo não esclarece se a motobomba substitui uma draga, atua como apoio temporário, realiza transferência entre unidades ou executa exclusivamente bombeamento de lodo.

## 3. Estrutura técnica do arquivo

### 3.1 Componentes existentes

- 3 planilhas visíveis.
- 27 fórmulas armazenadas.
- Células mescladas usadas para títulos, campos amplos e totais.
- Formatação por cor de fonte:
  - azul: dados indicados como preenchíveis;
  - vermelho: informações pendentes;
  - preto: resultados automáticos.
- Uma célula de entrada destacada em amarelo: `Dados Obra !B16`, distância de recalque.
- Uma faixa azul-clara em `MOTOBOMBA!E5:E7`, usada para leis sociais.

### 3.2 Componentes não encontrados

Não foram encontrados no pacote do arquivo:

- macros/VBA;
- conexões externas;
- links externos;
- nomes definidos;
- tabelas estruturadas do Excel;
- tabelas dinâmicas;
- gráficos;
- comentários/notas;
- validações de dados;
- formatação condicional;
- filtros automáticos;
- linhas ou colunas ocultas;
- proteção de planilha.

### Classificação das evidências

- **EVIDÊNCIA CONFIRMADA — Fato observado:** presença ou ausência verificada diretamente na estrutura interna do `.xlsx`.
- **EVIDÊNCIA PARCIAL — Interpretação:** a planilha depende de disciplina visual de preenchimento, e não de controles de validação ou proteção.

## 4. Fluxo completo observado

1. O usuário preenche ou revisa as premissas gerais na aba `Dados Obra `.
2. A aba `MOTOBOMBA` calcula o custo diário de uma pequena equipe e consolida itens diretos do orçamento.
3. O custo diário calculado alimenta o item “Mão de obra de instal. Bidim e Brita” por quatro dias.
4. A aba `MOTOBOMBA` soma seis itens de custo e calcula um preço final interno, porém com BDI igual a zero.
5. A aba `10. Plan. Preços` reorganiza o custo em três itens comerciais:
   - mobilização e montagem;
   - locação e operação;
   - desmobilização.
6. A aba comercial aplica BDI de 55% aos três itens e apresenta o preço total de venda.

### Classificação das evidências

- **EVIDÊNCIA CONFIRMADA — Fato observado:** a sequência e as dependências são comprovadas pelas fórmulas.
- **EVIDÊNCIA PARCIAL — Interpretação:** `10. Plan. Preços` aparenta ser a saída comercial do cálculo, enquanto `MOTOBOMBA` aparenta ser a memória interna de custos.
- **DÚVIDA:** o arquivo não indica explicitamente qual aba é entregue ao cliente.

# 5. Análise integral por aba

## 5.1 Aba `Dados Obra `

### 5.1.1 Objetivo observado

Registrar identificação da proposta, cliente e premissas gerais da obra. A aba também contém campos herdados para dimensionamento geométrico de dragagem, embora vários estejam vazios ou não sejam consumidos pelas demais abas.

### 5.1.2 Papel no fluxo

É a aba inicial de entrada. Neste arquivo, somente o horário diário de trabalho é referenciado por outra aba. Os demais dados cumprem função cadastral, descritiva ou permanecem sem uso no cálculo financeiro observado.

### 5.1.3 Legenda visual

| Cor declarada | Significado declarado |
|---|---|
| Azul | Dados a serem preenchidos |
| Vermelho | Informações pendentes |
| Preto | resultados automáticos |

- **EVIDÊNCIA CONFIRMADA — Fato observado:** a legenda está nas linhas 1 a 3.
- **Anomalia observada:** diversos valores azuis já estão preenchidos, mas não existe validação, bloqueio ou mecanismo que diferencie entrada obrigatória de opcional.

### 5.1.4 Identificação e dados cadastrais

| Campo | Célula | Valor |
|---|---:|---|
| Proposta | B5 | `D_040_2025` |
| Data | F5 | 2025-07-02 |
| Cliente | B7 | `WESTROCK` |
| Contato | B8:C9 | vazio |
| e-mail | E8:H9 | vazio |

- **EVIDÊNCIA CONFIRMADA — Fato observado:** valores e campos diretamente presentes.
- **EVIDÊNCIA CONFIRMADA — Anomalia observada:** contato e e-mail estão vazios; a legenda indica vermelho para pendências, mas esses campos não usam fonte vermelha.
- **DÚVIDA:** não é possível saber se os dados de contato foram omitidos intencionalmente ou ficaram pendentes.

### 5.1.5 Dados da obra

| Campo | Célula | Valor observado | Uso em fórmulas |
|---|---:|---:|---|
| Objeto | B12 | `Locaçao Motobomba` | não referenciado |
| Local | B13 | `Tres Barras` | não referenciado |
| Volume dragagem (m³) | B14 | 0,00 | não referenciado |
| Tipo de material | B15 | `Lodo - ETA` | não referenciado |
| Distância de Recalque (m) | B16 | 350,00 | compõe H16 |
| Seio da linha | E16 | 0,00 | compõe H16 |
| Total de recalque | H16 | 350,00 | não referenciado fora da aba |
| Linha Flutuante (m) | B17 | 200,00 | compõe H17 |
| Seio da linha flutuante | E17 | 0,00 | compõe H17 |
| Total de linha flutuante | H17 | 200,00 | não referenciado fora da aba |
| Linha de terra (m) | B18 | 150,00 | não referenciado |
| Profundidade de dragagem (m) | B19 | vazio | não referenciado |
| Espessura média de dragagem (m) | B20 | vazio | compõe G21 |
| Dimensão 1 da área | B21 | vazio | compõe G21 |
| Dimensão 2 da área | D21 | vazio | compõe G21 |
| Volume geométrico calculado | G21 | 0,00 | não referenciado fora da aba |
| Tipo de Bota Fora | B22 | `Bombeamento Direto` | não referenciado |
| Sistema de Medição | B23 | `preços unitários de serviços` | não referenciado |
| Canteiro de obras | B24 | `FOS` | não referenciado |
| Mobilização | B25 | `FOS` | não referenciado |
| Horário de Trabalho | B26 | 9,00 h/dia | referenciado em `MOTOBOMBA!D5` e `D7` |
| Dias de Trabalho | B27 | 22,00 dias/mês | não referenciado |

### 5.1.6 Fórmulas da aba

| Célula | Fórmula armazenada | Finalidade operacional | Resultado armazenado |
|---|---|---|---:|
| H16 | `=B16+E16` | somar extensão base e seio da linha para obter distância total de recalque | 350,00 m |
| H17 | `=B17+E17` | somar extensão base e seio da linha para obter linha flutuante total | 200,00 m |
| G21 | `=B21*D21*B20` | calcular volume geométrico pela multiplicação de duas dimensões de área pela espessura média | 0,00 m³ |

### 5.1.7 Regras e relações observadas

- A distância total de recalque é tratada como distância informada mais “seio da linha”.
- A linha flutuante total usa a mesma regra.
- O volume geométrico pressupõe área retangular definida por duas dimensões e multiplicada pela espessura média.
- O horário diário de 9 horas é reutilizado apenas para Operador Líder e Ajudante Geral.
- O Operador de Draga usa 12 horas/dia diretamente na aba de custo, divergindo do horário geral de 9 horas.
- Os 22 dias/mês não participam de nenhum cálculo.
- A distância de recalque, as extensões de tubulação, o volume, o material e o sistema de medição não alteram o preço neste arquivo.

### 5.1.8 Anomalias e resíduos observados

- O nome da aba contém espaço final. As fórmulas que a referenciam preservam esse espaço: `='Dados Obra '!B26`.
- A dependência funciona no arquivo original porque o nome e a referência coincidem, mas é estruturalmente frágil para importadores que normalizam nomes de abas.
- A célula B16 está destacada em amarelo, porém a legenda da própria aba explica apenas cores de fonte, não preenchimento amarelo.
- Volume de dragagem é zero, mas o orçamento possui preço fechado e não depende do volume.
- Os campos B19, B20, B21 e D21 estão vazios; a fórmula de G21 retorna zero no valor armazenado.
- O termo “Seio da linha” aparece sem definição.
- “Linha de terra” é 150 m e “Linha Flutuante” é 200 m, cuja soma é 350 m, igual à distância de recalque. Entretanto, a fórmula de H16 não usa B17 nem B18; a igualdade é apenas numérica no estado atual.
- O local está grafado `Tres Barras`, sem acento.
- O objeto e várias descrições usam `Locaçao`, sem acento correto em “ção”.

### 5.1.9 Classificação das evidências da aba

- **EVIDÊNCIA CONFIRMADA — Fato observado:** todos os campos, fórmulas, dependências e vazios descritos.
- **EVIDÊNCIA PARCIAL — Interpretação:** a aba parece derivada de um modelo mais amplo de dragagem e reutilizada para uma contratação de motobomba.
- **DÚVIDA:** não está comprovado se 350 m é efetivamente a soma intencional de 200 m flutuantes e 150 m terrestres ou apenas uma coincidência de preenchimento.
- **DÚVIDA:** não está comprovado se o horário de 12 horas do Operador de Draga é turno, jornada específica, cobertura por revezamento ou valor residual.

## 5.2 Aba `MOTOBOMBA`

### 5.2.1 Objetivo observado

Calcular o custo diário de mão de obra e consolidar uma memória de custos com seis itens associados à locação e operação de motobomba.

### 5.2.2 Papel no fluxo

Recebe o horário de trabalho da aba `Dados Obra `, calcula equipe/benefícios diários e produz o custo total de R$ 128.091,15, posteriormente reorganizado pela aba comercial.

### 5.2.3 Bloco de mão de obra e despesas diárias

| Linha | Nº Func. | Descrição | R$/h ou valor unitário | Hrs/dia | L. Sociais | Total diário |
|---:|---:|---|---:|---:|---:|---:|
| 5 | 0 | Operador Líder | R$ 14,50/h | 9 | 120% | R$ 0,00 |
| 6 | 2 | Operador de Draga | R$ 26,71/h | 12 | 120% | R$ 1.410,288 |
| 7 | vazio | Ajudante Geral | R$ 10,75/h | 9 | 120% | R$ 0,00 |
| 8 | 2 calculado | Refeições | R$ 30,00 por pessoa | não aplicável | não aplicável | R$ 60,00 |
| 9 | 2 calculado | Transporte | R$ 10,00 por pessoa | não aplicável | não aplicável | R$ 20,00 |
| 10 | — | **Custo por dia** | — | — | — | **R$ 1.490,288** |

### 5.2.4 Fórmulas do bloco diário

| Célula | Fórmula | Finalidade | Resultado armazenado |
|---|---|---|---:|
| D5 | `='Dados Obra '!B26` | usar a jornada geral para Operador Líder | 9 |
| F5 | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` | custo salarial diário acrescido de leis sociais | 0,00 |
| F6 | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` | custo de dois operadores por 12 h acrescido de 120% | 1.410,288 |
| D7 | `='Dados Obra '!B26` | usar a jornada geral para Ajudante Geral | 9 |
| F7 | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` | custo salarial diário acrescido de leis sociais | 0,00 |
| A8 | `=A5+A7+A6` | totalizar pessoas das três funções para refeições | 2 |
| F8 | `=A8*C8` | custo diário de refeições | 60,00 |
| A9 | `=A8` | repetir total de pessoas para transporte | 2 |
| F9 | `=A9*C9` | custo diário de transporte | 20,00 |
| F10 | `=SUM(F5:F9)` | consolidar custo diário de equipe, refeição e transporte | 1.490,288 |

### 5.2.5 Regra matemática das leis sociais

A fórmula pode ser reescrita conceitualmente como:

`quantidade de funcionários × valor-hora × horas/dia × (1 + leis sociais/100)`

Para Operador de Draga:

`2 × 26,71 × 12 × 2,20 = 1.410,288`

- **EVIDÊNCIA CONFIRMADA — Fato observado:** o percentual é 120 e a fórmula soma 120% ao custo base, produzindo multiplicador total de 2,20.
- **EVIDÊNCIA PARCIAL — Interpretação:** “L.Sociais” representa encargos/leis sociais aplicados ao salário-hora.
- **DÚVIDA:** o arquivo não contém fonte, data-base ou composição do percentual de 120%.

### 5.2.6 Composição de custos

| Item | Descrição | Unidade | Quantidade | Preço unitário | Preço total | Natureza do total |
|---:|---|---|---:|---:|---:|---|
| 1 | Locaçao Motobomba | vb | 1 | R$ 104.080,00 | R$ 104.080,00 | fórmula `D15*E15` |
| 2 | Mobilizaçao | vb | 1 | R$ 5.050,00 | R$ 5.050,00 | valor fixo digitado |
| 3 | Startup | vb | 1 | R$ 6.500,00 | R$ 6.500,00 | valor fixo digitado |
| 4 | Desmob | vb | 1 | R$ 5.500,00 | R$ 5.500,00 | valor fixo digitado |
| 5 | Hospedagem Funcionários | vb | 1 | R$ 1.000,00 | R$ 1.000,00 | valor fixo digitado |
| 6 | Mão de obra de instal. Bidim e Brita | dia | 4 | R$ 1.490,288 | R$ 5.961,152 | preço unitário ligado ao custo diário; total digitado |
| — | **TOTAL** | — | — | — | **R$ 128.091,152** | fórmula de soma |
| — | BDI (%) | — | — | 0% | R$ 0,00 | fórmula sobre total |
| — | **Preço Final** | — | — | — | **R$ 128.091,152** | total + BDI interno |

### 5.2.7 Fórmulas do bloco de custos

| Célula | Fórmula | Finalidade | Resultado armazenado |
|---|---|---|---:|
| F15 | `=D15*E15` | calcular total da locação | 104.080,00 |
| E20 | `=F10` | usar o custo diário da equipe como preço unitário da instalação de Bidim e brita | 1.490,288 |
| F21 | `=SUM(F15:F20)` | somar os seis itens | 128.091,152 |
| F22 | `=F21*(E22/100)` | calcular valor de BDI interno | 0,00 |
| F23 | `=SUM(F21:F22)` | calcular preço final interno | 128.091,152 |

### 5.2.8 Valores equivalentes sem fórmula

As seguintes células contêm valores constantes, embora possam ser reproduzidas por relações visíveis:

- `F16 = 5.050,00`, igual a `D16 × E16`, mas sem fórmula.
- `F17 = 6.500,00`, igual a `D17 × E17`, mas sem fórmula.
- `F18 = 5.500,00`, igual a `D18 × E18`, mas sem fórmula.
- `F19 = 1.000,00`, igual a `D19 × E19`, mas sem fórmula.
- `F20 = 5.961,152`, igual a `D20 × E20`, mas sem fórmula.

- **EVIDÊNCIA CONFIRMADA — Anomalia observada:** o bloco mistura totais calculados e totais digitados com aparência visual semelhante.
- **Risco observado:** alterar quantidade ou preço unitário nas linhas 16 a 20 não atualiza necessariamente o preço total correspondente.

### 5.2.9 Relação entre equipe e item de instalação

- O custo diário de R$ 1.490,288 é composto por:
  - dois Operadores de Draga com leis sociais: R$ 1.410,288;
  - refeições para duas pessoas: R$ 60,00;
  - transporte para duas pessoas: R$ 20,00.
- O item de instalação usa quatro dias.
- O total digitado de R$ 5.961,152 é matematicamente igual a `4 × 1.490,288`.
- Operador Líder e Ajudante Geral possuem custo zero por ausência de quantidade.

### 5.2.10 Distribuição do custo interno

| Componente | Valor | Participação no custo total |
|---|---:|---:|
| Locação Motobomba | R$ 104.080,00 | 81,2546% |
| Mobilização | R$ 5.050,00 | 3,9425% |
| Startup | R$ 6.500,00 | 5,0745% |
| Desmobilização | R$ 5.500,00 | 4,2938% |
| Hospedagem | R$ 1.000,00 | 0,7807% |
| Mão de obra Bidim/Brita | R$ 5.961,152 | 4,6538% |
| **Total** | **R$ 128.091,152** | **100%** |

- **EVIDÊNCIA CONFIRMADA — Derivação matemática:** percentuais calculados diretamente dos valores do arquivo.
- **EVIDÊNCIA PARCIAL — Interpretação:** a locação da motobomba é o principal componente econômico do orçamento.

### 5.2.11 Anomalias e dúvidas da aba

- O título “Mão de obra montagem canteiro” não corresponde integralmente ao uso posterior, que chama o custo de “Mão de obra de instal. Bidim e Brita”.
- O item “Locaçao Motobomba” de R$ 104.080,00 não possui memória de cálculo nesta pasta de trabalho.
- Mobilização, startup, desmobilização e hospedagem também não possuem composição ou origem.
- O BDI interno é 0%, enquanto a aba comercial aplica 55%.
- A sigla/unidade `vb` não é definida no arquivo.
- “Operador de Draga” é usado em um orçamento cujo objeto é motobomba.
- O campo A7 de quantidade de Ajudante Geral está vazio, e não explicitamente zero; a fórmula o trata como zero no resultado armazenado.
- O arquivo não informa prazo total de locação/operação.
- A quantidade da locação é 1 `vb`, não dias, meses ou horas.
- Não há cálculo de combustível, manutenção, depreciação, energia, peças, mangotes, tubulação, guindaste, frete detalhado ou seguro.

### 5.2.12 Classificação das evidências da aba

- **EVIDÊNCIA CONFIRMADA — Fato observado:** toda a composição, fórmulas, valores e relações matemáticas.
- **EVIDÊNCIA PARCIAL — Interpretação:** os R$ 104.080,00 aparentam incorporar o custo principal de disponibilização/operação da motobomba, mas sua composição é externa ou empírica.
- **DÚVIDA:** origem e data-base de todos os valores unitários.
- **DÚVIDA:** significado e período coberto pelo item de locação.
- **DÚVIDA:** razão operacional para duas pessoas serem chamadas de Operadores de Draga.
- **DÚVIDA:** se startup e hospedagem devem integrar o item comercial “Locação e Operação”.

## 5.3 Aba `10. Plan. Preços`

### 5.3.1 Objetivo observado

Apresentar planilha detalhada de preços de custo e venda, reorganizando o custo interno em três itens comerciais e aplicando BDI de 55%.

### 5.3.2 Papel no fluxo

É a última aba e a única que apresenta explicitamente “Preços com BDI” e “Preço de Venda”. Ela recebe valores da aba `MOTOBOMBA`.

### 5.3.3 Itens comerciais

| Item | Descrição dos Serviços | Custo Total | Quantidade | Unidade | Custo Unitário | BDI | Preço Unitário | Preço Total |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| 1 | Mobilizaçao e montagem Motobomba | R$ 5.050,00 | 1 | vb | R$ 5.050,00 | 55% | R$ 7.827,50 | R$ 7.827,50 |
| 5 | Locaçao e Operação Motobomba | R$ 117.541,152 | 1 | vb | R$ 117.541,152 | 55% | R$ 182.188,7856 | R$ 182.188,7856 |
| 7 | Desmobilizaçao Equipamento Motobomba | R$ 5.500,00 | 1 | vb | R$ 5.500,00 | 55% | R$ 8.525,00 | R$ 8.525,00 |
| — | **Custo Total** | **R$ 128.091,152** | — | — | — | — | — | — |
| — | **Preço de Venda** | — | — | — | — | — | — | **R$ 198.541,2856** |

### 5.3.4 Fórmulas da aba

| Célula | Fórmula | Finalidade | Resultado armazenado |
|---|---|---|---:|
| C4 | `=MOTOBOMBA!F16` | obter custo de mobilização | 5.050,00 |
| G4 | `=C4` | custo unitário com quantidade 1 | 5.050,00 |
| I4 | `=((H4/100)+1)*G4` | aplicar 55% de BDI ao custo unitário | 7.827,50 |
| J4 | `=E4*I4` | calcular preço total do item | 7.827,50 |
| C5 | `=MOTOBOMBA!F23-(MOTOBOMBA!F16+MOTOBOMBA!F18)` | formar o custo de locação/operação excluindo mobilização e desmobilização | 117.541,152 |
| G5 | `=C5/E5` | obter custo unitário | 117.541,152 |
| C6 | `=MOTOBOMBA!F18` | obter custo de desmobilização | 5.500,00 |
| G6 | `=C6/E6` | obter custo unitário | 5.500,00 |
| C7 | `=SUM(C4:C6)` | somar custo dos três itens comerciais | 128.091,152 |
| J7 | `=SUM(J4:J6)` | somar preço de venda dos três itens | 198.541,2856 |

### 5.3.5 Valores de venda sem fórmula armazenada

- `I5 = 182.188,7856` está armazenado como valor constante, embora seja igual a `G5 × 1,55`.
- `J5 = 182.188,7856` está armazenado como valor constante, embora seja igual a `E5 × I5`.
- `I6 = 8.525,00` está armazenado como valor constante, embora seja igual a `G6 × 1,55`.
- `J6 = 8.525,00` está armazenado como valor constante, embora seja igual a `E6 × I6`.

- **EVIDÊNCIA CONFIRMADA — Anomalia observada:** somente o item 1 possui fórmulas completas de formação do preço de venda; itens 5 e 7 têm preços de venda digitados.
- **Risco observado:** alterações no custo ou BDI dos itens 5 e 7 não recalculam automaticamente os preços armazenados.

### 5.3.6 Regra de agrupamento comercial

A linha comercial “Locaçao e Operação Motobomba” é calculada como:

`Preço Final interno – Mobilização – Desmobilização`

No estado atual:

`128.091,152 – 5.050,00 – 5.500,00 = 117.541,152`

Consequentemente, o agrupamento inclui:

- Locação Motobomba: R$ 104.080,00;
- Startup: R$ 6.500,00;
- Hospedagem Funcionários: R$ 1.000,00;
- Mão de obra de instalação de Bidim e brita: R$ 5.961,152.

- **EVIDÊNCIA CONFIRMADA — Derivação matemática:** a composição do agrupamento decorre da fórmula de C5.
- **EVIDÊNCIA PARCIAL — Interpretação:** startup, hospedagem e instalação são comercialmente ocultados dentro do item global de locação/operação.
- **DÚVIDA:** não está comprovado se esse agrupamento é uma decisão comercial deliberada ou uma simplificação específica deste orçamento.

### 5.3.7 Formação do preço de venda

- Custo total: R$ 128.091,152.
- BDI aplicado por item: 55%.
- Acréscimo nominal: R$ 70.450,1336.
- Preço de venda: R$ 198.541,2856.
- Relação preço/custo: 1,55.

O preço total confirma aplicação uniforme de 55% sobre o custo total:

`128.091,152 × 1,55 = 198.541,2856`

- **EVIDÊNCIA CONFIRMADA — Fato observado e derivação matemática:** valores e igualdade calculados a partir do arquivo.
- **DÚVIDA:** o arquivo não apresenta composição do BDI, impostos, margem, riscos, administração central ou contingência.

### 5.3.8 Numeração dos itens

Os itens comerciais usam 1, 5 e 7, sem itens 2, 3, 4 ou 6 na planilha.

- **EVIDÊNCIA CONFIRMADA — Fato observado:** numeração diretamente presente.
- **EVIDÊNCIA PARCIAL — Interpretação:** a numeração pode seguir uma estrutura contratual externa ou ter sido preservada de outra planilha.
- **DÚVIDA:** o arquivo não permite identificar a origem da sequência.

### 5.3.9 Classificação das evidências da aba

- **EVIDÊNCIA CONFIRMADA — Fato observado:** itens, fórmulas, BDI e resultados.
- **EVIDÊNCIA PARCIAL — Interpretação:** esta aba representa a apresentação comercial final.
- **DÚVIDA:** destino da planilha, critério de agrupamento e composição do BDI.

# 6. Dependências entre abas

## 6.1 Mapa de dependências

```text
Dados Obra !B26 (9 h/dia)
    ├── MOTOBOMBA!D5 (Operador Líder)
    └── MOTOBOMBA!D7 (Ajudante Geral)

MOTOBOMBA!F5:F9
    └── MOTOBOMBA!F10 (custo por dia)
            └── MOTOBOMBA!E20 (preço unitário da instalação)

MOTOBOMBA!F15:F20
    └── MOTOBOMBA!F21 (custo total)
            ├── MOTOBOMBA!F22 (BDI interno = 0)
            └── MOTOBOMBA!F23 (preço final interno)

MOTOBOMBA!F16
    └── 10. Plan. Preços!C4 (mobilização)

MOTOBOMBA!F23, F16 e F18
    └── 10. Plan. Preços!C5 (locação e operação agrupada)

MOTOBOMBA!F18
    └── 10. Plan. Preços!C6 (desmobilização)

10. Plan. Preços!C4:C6
    └── C7 (custo total)

10. Plan. Preços!J4:J6
    └── J7 (preço de venda)
```

## 6.2 Dados sem dependência financeira observada

Não alteram os custos ou o preço de venda neste arquivo:

- proposta;
- data;
- cliente;
- contato;
- e-mail;
- objeto;
- local;
- volume;
- tipo de material;
- distância de recalque;
- linha flutuante;
- linha de terra;
- profundidade;
- espessura;
- área;
- tipo de bota-fora;
- sistema de medição;
- responsável pelo canteiro;
- responsável pela mobilização;
- dias de trabalho por mês.

- **EVIDÊNCIA CONFIRMADA — Fato observado:** nenhuma fórmula das abas seguintes referencia esses campos.
- **EVIDÊNCIA PARCIAL — Interpretação:** esses dados podem ser informativos, herdados de modelo ou usados por decisão humana fora das fórmulas.

# 7. Entidades conceituais encontradas

## 7.1 Identificação comercial

- Proposta.
- Data.
- Cliente.
- Contato.
- E-mail.

## 7.2 Obra/serviço

- Objeto.
- Local.
- Material.
- Volume.
- distância de recalque.
- linha flutuante.
- linha terrestre.
- profundidade.
- espessura média.
- área.
- bota-fora.
- sistema de medição.
- canteiro.
- mobilização.
- jornada diária.
- dias de trabalho mensais.

## 7.3 Recursos humanos e despesas associadas

- Função.
- Quantidade de funcionários.
- Valor-hora.
- Horas por dia.
- Leis sociais.
- Refeição.
- Transporte.
- Custo diário.

## 7.4 Componentes internos de custo

- Locação de motobomba.
- Mobilização.
- Startup.
- Desmobilização.
- Hospedagem.
- Instalação de Bidim e brita.
- BDI interno.
- Preço final interno.

## 7.5 Itens comerciais

- Número do item.
- Descrição do serviço.
- Custo total.
- Quantidade.
- Unidade.
- Custo unitário.
- BDI.
- Preço unitário.
- Preço total.

### Classificação

- **EVIDÊNCIA CONFIRMADA — Fato observado:** entidades extraídas dos rótulos e estruturas do arquivo.
- **EVIDÊNCIA PARCIAL:** cada entidade foi observada somente neste orçamento dentro desta análise; nenhuma é promovida aqui a padrão geral da FOS.

# 8. Regras de negócio observadas

1. **Custo diário de função com encargos**  
   `quantidade × R$/h × horas/dia × (1 + leis sociais/100)`.

2. **Benefícios/despesas por pessoa**  
   Refeição e transporte são multiplicados pela soma das quantidades das três funções de mão de obra.

3. **Custo diário total**  
   Soma de custos das funções, refeições e transporte.

4. **Custo da instalação de Bidim e brita**  
   Quatro dias multiplicados pelo custo diário da equipe, embora o total esteja digitado e não formulado.

5. **Custo total interno**  
   Soma de seis componentes.

6. **Preço final interno**  
   Custo total mais BDI interno; neste arquivo o BDI interno é zero.

7. **Separação comercial de mobilização**  
   Mobilização é apresentada como item comercial próprio.

8. **Separação comercial de desmobilização**  
   Desmobilização é apresentada como item comercial próprio.

9. **Agrupamento comercial residual**  
   Todos os demais custos são agrupados em “Locaçao e Operação Motobomba”.

10. **BDI comercial**  
    55% sobre cada item comercial.

11. **Unidade comercial**  
    Todos os itens finais usam `vb` e quantidade 1.

12. **Volume e prazo não direcionam o preço**  
    O arquivo não utiliza volume, distância ou dias/mês na formação do preço.

### Classificação

- **EVIDÊNCIA CONFIRMADA — Fato observado:** regras 1, 2, 3, 5, 6, 7, 8, 9 e 10 possuem fórmulas ou valores explícitos.
- **EVIDÊNCIA CONFIRMADA — Relação matemática:** regra 4 é comprovada numericamente, embora o total esteja digitado.
- **EVIDÊNCIA PARCIAL:** todas as regras são específicas desta fonte até crosscheck futuro.
- **DÚVIDA:** `vb` provavelmente significa verba, mas o arquivo não define a sigla; não classificado como fato.

# 9. Nomenclaturas e terminologia

| Termo no arquivo | Uso observado | Observação |
|---|---|---|
| Locaçao Motobomba | objeto e item de custo | grafia sem acento correto |
| Tres Barras | local | grafia sem acento |
| Lodo - ETA | material | ETA não é expandida no arquivo |
| Seio da linha | adicional à extensão | sem definição |
| Linha Flutuante | trecho de tubulação/linha | 200 m |
| Linha de terra | trecho terrestre | 150 m |
| Bombeamento Direto | tipo de bota-fora | sem detalhamento |
| preços unitários de serviços | sistema de medição | texto descritivo |
| L.Sociais | percentual de encargos | 120% |
| Startup | item de custo | R$ 6.500,00 |
| Desmob | abreviação de desmobilização | R$ 5.500,00 |
| Bidim e Brita | atividade de instalação | quatro dias de equipe |
| vb | unidade comercial | não definida |
| BDI | acréscimo comercial | 0% interno e 55% comercial |

# 10. Valores embutidos e parâmetros

## 10.1 Valores operacionais/cadastrais

- Distância de recalque: 350 m.
- Linha flutuante: 200 m.
- Linha terrestre: 150 m.
- Jornada geral: 9 h/dia.
- Jornada do Operador de Draga: 12 h/dia.
- Dias de trabalho: 22 dias/mês.
- Leis sociais: 120%.

## 10.2 Valores de mão de obra e despesas

- Operador Líder: R$ 14,50/h.
- Operador de Draga: R$ 26,71/h.
- Ajudante Geral: R$ 10,75/h.
- Refeição: R$ 30,00 por pessoa/dia.
- Transporte: R$ 10,00 por pessoa/dia.

## 10.3 Valores de custo

- Locação Motobomba: R$ 104.080,00.
- Mobilização: R$ 5.050,00.
- Startup: R$ 6.500,00.
- Desmobilização: R$ 5.500,00.
- Hospedagem: R$ 1.000,00.
- Instalação Bidim/Brita: 4 dias.

## 10.4 Valor comercial

- BDI: 55%.

### Classificação

- **EVIDÊNCIA CONFIRMADA — Fato observado:** valores diretamente presentes.
- **EVIDÊNCIA PARCIAL — Grau de confiança C:** observados somente nesta fonte.
- **DÚVIDA:** nenhum valor possui fonte de cotação, data-base salarial, fornecedor, memória externa ou justificativa técnica dentro do arquivo.

# 11. Anomalias consolidadas

1. Nome da aba `Dados Obra ` possui espaço final.
2. Referências à aba dependem do espaço final.
3. Campos de contato e e-mail vazios.
4. Volume igual a zero em um documento que conserva terminologia de dragagem.
5. Campos geométricos vazios e fórmula de volume sem aplicação posterior.
6. Distâncias e material não afetam o preço.
7. Jornada geral de 9 horas não é usada pelo Operador de Draga, que usa 12 horas.
8. Quantidade do Ajudante Geral vazia, não zero explícito.
9. Mistura de valores calculados e digitados no mesmo bloco de totais.
10. Total do item Bidim/Brita digitado apesar de possuir componentes suficientes para fórmula.
11. BDI interno de 0% e BDI comercial de 55% em abas diferentes.
12. Preços de venda dos itens 5 e 7 digitados, não formulados.
13. Item comercial 5 agrega componentes heterogêneos.
14. Numeração comercial salta de 1 para 5 e 7.
15. Não existe memória de cálculo para o maior componente, R$ 104.080,00.
16. Não existe período explícito da locação/operação.
17. A unidade `vb` não é definida.
18. Não há validação, proteção ou indicação técnica de campos obrigatórios.
19. Metadados registram criação em 2010, muito anterior à proposta de 2025, indicando reutilização de arquivo/modelo, sem permitir determinar quantas revisões ocorreram.
20. A extensão interna das planilhas alcança colunas/linhas além do conteúdo efetivo por formatação residual (`Dados Obra ` até K27, `MOTOBOMBA` até P27 e `10. Plan. Preços` até L11).

### Classificação

- **EVIDÊNCIA CONFIRMADA — Anomalia observada:** itens 1 a 18 e 20 são verificáveis na fonte.
- **EVIDÊNCIA PARCIAL — Interpretação:** a diferença entre criação em 2010 e uso em 2025 sugere reutilização de modelo; o histórico intermediário não está disponível.

# 12. Padrões observados exclusivamente nesta fonte

- Separação entre aba cadastral, memória interna de custo e planilha comercial.
- Uso de azul para entradas e preto para resultados.
- Aplicação de leis sociais sobre custo horário.
- Conversão de equipe diária em item de custo por número de dias.
- Custos internos detalhados em seis itens e apresentação comercial condensada em três.
- Mobilização e desmobilização isoladas comercialmente.
- Demais componentes absorvidos em item de locação/operação.
- Aplicação uniforme de BDI de 55%.
- Uso de quantidade 1 e unidade `vb` para todos os itens comerciais.

- **EVIDÊNCIA PARCIAL — Grau de confiança C:** padrões presentes somente neste orçamento; não constituem Método de Orçamento FOS consolidado.

# 13. Exceções específicas observadas

- O orçamento não usa o volume para definir custo ou prazo.
- Não existe cálculo de produção.
- Não existe cálculo de duração da locação.
- Não existe dimensionamento hidráulico da motobomba.
- Não existe seleção de equipamento por vazão, altura manométrica ou potência.
- Não existe consumo de combustível ou energia.
- A equipe ativa tem somente dois Operadores de Draga, apesar de três funções cadastradas.
- O BDI da memória interna é zero, mas a saída comercial usa 55%.
- Parte dos resultados é congelada como valor digitado.

- **EVIDÊNCIA CONFIRMADA — Fato observado:** ausência de fórmulas, tabelas ou campos correspondentes na fonte.
- **EVIDÊNCIA PARCIAL — Interpretação:** esses itens podem estar calculados externamente ou incorporados no valor global da locação.

# 14. Dúvidas para validação do especialista

1. Qual foi o serviço físico executado pela motobomba em Três Barras?
2. A motobomba foi locada por qual período?
3. O valor de R$ 104.080,00 corresponde a locação, operação, combustível, manutenção e operador ou apenas ao equipamento?
4. Qual é a memória de cálculo ou cotação que originou os R$ 104.080,00?
5. Por que o orçamento usa “Operador de Draga” em vez de operador de motobomba?
6. As 12 horas do Operador de Draga representam jornada individual, turno de operação ou cobertura por revezamento?
7. O percentual de 120% de leis sociais era padrão vigente, estimativa ou valor específico?
8. Refeição e transporte de R$ 30,00 e R$ 10,00 têm qual data-base?
9. O item de instalação de Bidim e brita fazia parte da mobilização, startup ou operação?
10. Por que startup, hospedagem e Bidim/Brita foram agrupados comercialmente em “Locação e Operação”?
11. A unidade `vb` significa “verba” neste contexto?
12. O BDI de 55% tinha composição formal?
13. Por que existe BDI 0% na aba interna e 55% na aba comercial?
14. Os preços de venda digitados nos itens 5 e 7 foram deliberadamente congelados?
15. A numeração 1, 5 e 7 segue itens de contrato, proposta ou modelo externo?
16. A distância de 350 m é formada por 200 m de linha flutuante mais 150 m de linha de terra?
17. “Seio da linha” representa folga técnica de mangote/tubulação?
18. Volume, profundidade, espessura e área eram irrelevantes para este serviço ou ficaram pendentes?
19. Os 22 dias/mês tinham alguma função fora desta planilha?
20. A aba `10. Plan. Preços` foi a planilha efetivamente apresentada ao cliente?
21. O preço de venda final de R$ 198.541,29 foi o valor proposto/contratado?
22. Há proposta em PDF, cotação do equipamento ou contrato que complemente esta memória?

# 15. Limitações da análise

- A análise foi realizada exclusivamente sobre o arquivo `Motobomba 3Barras - Westrock.xlsx` recebido nesta sessão.
- Não foram fornecidos proposta comercial em PDF, contrato, cotações, e-mails, medições ou resultado realizado.
- Fórmulas foram analisadas a partir da estrutura original do `.xlsx` e dos valores armazenados pelo Excel.
- A ferramenta de leitura normalizou visualmente o nome `Dados Obra ` para `Dados Obra`; isso provocou `#REF!` apenas na renderização importada. A estrutura original confirma que a aba e as fórmulas possuem o mesmo espaço final, e os valores armazenados no arquivo são válidos. Portanto, não foi classificada como fórmula quebrada na fonte original, mas como dependência frágil.
- Não foi possível determinar a origem de valores digitados sem memória de cálculo.
- Nenhuma conclusão deste documento foi comparada ou consolidada com outro orçamento.

# 16. Registro de evidências

## 16.1 EVIDÊNCIA CONFIRMADA

- Estrutura com três abas.
- Dados cadastrais da proposta.
- Campos, valores, fórmulas e dependências descritos.
- Custo interno de R$ 128.091,152.
- Preço de venda de R$ 198.541,2856.
- Aplicação matemática de 55%.
- Composição diária de equipe de R$ 1.490,288.
- Agrupamento comercial residual de R$ 117.541,152.
- Ausência dos componentes técnicos e controles listados.
- Anomalias de fórmulas seletivas e valores digitados.

## 16.2 EVIDÊNCIA PARCIAL

- Classificação como orçamento simplificado de locação/operação de motobomba.
- Interpretação da aba comercial como saída ao cliente.
- Interpretação de que o modelo foi derivado/reutilizado de uma planilha mais ampla de dragagem.
- Interpretação de que startup, hospedagem e instalação estão comercialmente embutidos na locação/operação.
- Todos os possíveis padrões, com confiança C, por terem sido observados em apenas uma fonte.

## 16.3 DÚVIDAS

- Origem, data-base e composição dos custos.
- Período e escopo da locação.
- Significado de `vb` e “Seio da linha”.
- Critério do BDI de 55%.
- Motivo das jornadas distintas.
- Destino da aba comercial.
- Relação contratual da numeração 1, 5 e 7.
- Valor efetivamente contratado e realizado.

# 17. Checklist de validação desta análise

- [x] Todas as abas analisadas.
- [x] Todas as células não vazias relevantes verificadas.
- [x] Todas as fórmulas armazenadas inventariadas e explicadas.
- [x] Dependências entre abas registradas.
- [x] Valores fixos e resultados automáticos diferenciados.
- [x] Entidades, regras, terminologias, padrões, exceções e anomalias preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Nenhum documento de outro orçamento alterado.
- [x] Nenhum índice geral alterado.
- [x] Nenhuma consolidação realizada.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma funcionalidade proposta ou implementada.
