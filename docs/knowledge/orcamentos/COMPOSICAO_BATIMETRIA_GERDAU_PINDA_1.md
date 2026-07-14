# Composição - Batimetria - Gerdau Pinda(1).xlsx — Batimetria de Lagoas de Estabilização

## Status da análise

- **Status:** ENGENHARIA REVERSA VERTICAL CONCLUÍDA.
- **Data da análise:** 14/07/2026.
- **Arquivo original:** `Composição - Batimetria - Gerdau Pinda(1).xlsx`.
- **Versão explícita no nome:** não identificada; o sufixo `(1)` aparenta ser duplicação de arquivo, não uma versão de negócio comprovada.
- **Proposta registrada no conteúdo:** `Proposta D_034/2025`.
- **Data registrada na proposta:** 21/05/2025.
- **Quantidade de abas:** 7.
- **Tamanho do arquivo analisado:** 34.392 bytes.
- **SHA-256 da fonte analisada:** `fff05b65ee231c9875671cd6ce61339e599d09d8bfe32167b46a52ce5319c32c`.
- Todas as sete abas foram examinadas integralmente.
- Nenhuma funcionalidade, arquitetura, banco de dados, tela, modelo consolidado ou decisão de implementação foi criada.
- Este documento registra exclusivamente o conhecimento encontrado neste arquivo.

## Regra de classificação usada

| Categoria operacional solicitada | Correspondência documental |
| --- | --- |
| **EVIDÊNCIA CONFIRMADA** | Informação comprovada diretamente no Excel; inclui anomalias cuja existência é observável. |
| **EVIDÊNCIA PARCIAL** | Interpretação ou possível regra observada somente neste orçamento; confiança Nível C. |
| **DÚVIDA** | Informação sem comprovação suficiente ou cuja finalidade não pode ser determinada apenas pela planilha. |

Todas as descobertas reutilizáveis permanecem com **confiança Nível C**, pois foram observadas em uma única fonte.

# 1. Classificação do orçamento

## EVIDÊNCIA CONFIRMADA

O arquivo representa uma proposta para serviços relacionados à **batimetria das Lagoas de Estabilização da GERDAU**, identificada como `Proposta D_034/2025`.

O escopo comercial consolidado contém quatro componentes:

1. mobilização;
2. coleta de amostras e análise geral;
3. batimetria;
4. elaboração do projeto e escopo de dragagem.

O arquivo não precifica a execução da dragagem. A dragagem aparece como contexto futuro: existe uma aba de produção de draga e o item comercial `Elaboração do projeto e Escopo Dragagem`, mas a composição final vendida é de estudos, levantamentos, amostragem e projeto.

## EVIDÊNCIA PARCIAL

O orçamento aparenta pertencer a uma família de **serviços preliminares de diagnóstico e engenharia para futura dragagem**, em que a área das lagoas é a principal base física do preço da batimetria.

Características que o diferenciam:

- contratação de empresa especializada (`SubGeo`) para a batimetria;
- quantidade de amostras calculada por lagoa;
- caracterização ambiental pela NBR 10004;
- projeto/escopo de dragagem como entrega separada;
- preço comercial final também expresso em R$/m²;
- ausência de custo de operação de draga no resumo final.

Esta classificação não deve ser promovida a padrão geral antes do crosscheck com outros arquivos.

# 2. Identidade comercial e técnica

## EVIDÊNCIA CONFIRMADA

| Campo | Conteúdo observado |
| --- | --- |
| Proposta | `Proposta D_034/2025` |
| Data | 21/05/2025 |
| Cliente | `GERDAU` |
| Contato | `Inácio` |
| E-mail | não preenchido |
| Objeto | `Batimetria das Lagoas de Estabilização` |
| Local | não preenchido |
| Volume de dragagem | não preenchido; há anotação textual `(30x90x2)` |
| Tipo de material | não preenchido |
| Distância de recalque | não preenchida |
| Linha flutuante | não preenchida |
| Linha de terra | não preenchida |
| Profundidade de dragagem | não preenchida no bloco principal |
| Espessura média de dragagem | não preenchida |
| Área de dragagem no bloco principal | não preenchida |
| Tipo de bota-fora | não preenchido |
| Sistema de medição | não preenchido |
| Canteiro de obras | não preenchido no bloco principal |
| Mobilização | não preenchida no bloco principal |
| Horário de trabalho | 9 h/dia |
| Dias de trabalho | 22 dias/mês |

# 3. Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identidade da proposta, premissas gerais, cadastro geométrico das lagoas, quantidade de amostras e referência de preço da SubGeo. |
| 2 | `Produção` | Modelo genérico de produção de draga e prazo; não preenchido para esta proposta. |
| 3 | `1. Mobilização` | Composição de mobilização, integração, documentação, viagem, apoio e mão de obra. |
| 4 | `2.Amostras` | Composição de coleta, análises laboratoriais e caracterização NBR 10004. |
| 5 | `3. Batimetria` | Composição do serviço subcontratado de batimetria e acompanhamento FOS. |
| 6 | `4. Projeto` | Composição de engenharia para elaboração do projeto e escopo de dragagem. |
| 7 | `RESUMO` | Consolidação de custos, aplicação de BDI comercial de 70% e preço final. |

# 4. Fluxo completo observado

```text
Identidade da proposta
    ↓
Geometria das lagoas
    ├── área total de 13.440 m²
    └── 18 amostras
          ↓
Referência comercial SubGeo: R$ 18.000
          ↓
Composições independentes
    ├── Mobilização
    ├── Amostras
    ├── Batimetria
    └── Projeto
          ↓
RESUMO
    ├── custo total
    ├── BDI comercial por item
    ├── preço de venda
    └── preço equivalente por m²
```

A aba `Produção` está estruturalmente ligada às premissas gerais, mas não alimenta o resumo final deste orçamento.

---

# 5. Análise por aba

## 5.1 Aba `Dados Obra`

### Objetivo

Registrar a identidade da proposta e os parâmetros físicos usados para dimensionar amostras e preço da batimetria.

### Papel no fluxo

É a principal fonte de:

- jornada de trabalho usada nas composições;
- área total das lagoas usada na batimetria e no resumo;
- quantidade total de amostras usada na aba `2.Amostras`;
- preço total e preço unitário da cotação SubGeo.

### Convenção visual — EVIDÊNCIA CONFIRMADA

A própria aba declara:

- azul: dados a serem preenchidos;
- vermelho: informações pendentes;
- preto: resultados automáticos.

### Cadastro das lagoas — EVIDÊNCIA CONFIRMADA

| Lagoa | Área exibida | Amostras | Largura | Comprimento | Profundidade | Quantidade |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Lagoas Anaeróbias | 4.290 m² | 10 | 33 m | 65 m | 3 m | 2 |
| Lagoa Facultativa | 9.150 m² | 8 | 61 m | 150 m | 2,4 m | 1 |
| **Total** | **13.440 m²** | **18** | — | — | — | — |

### Fórmulas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula | Finalidade operacional |
| --- | --- | --- |
| `K13` | `=M13*N13*P13` | Calcula a área total das duas lagoas anaeróbias: largura × comprimento × quantidade. |
| `L13` | `=5*P13` | Calcula 5 amostras por lagoa anaeróbia. |
| `K14` | `=M14*N14*P14` | Calcula a área da lagoa facultativa. |
| `L14` | `=8*P14` | Calcula 8 amostras por lagoa facultativa. |
| `H16` | `=B16+E16` | Soma distância informada e “seio da linha” para recalque total. |
| `H17` | `=B17+E17` | Soma linha informada e “seio da linha” para linha flutuante total. |
| `K19` | `=SUM(K13:K18)` | Consolida a área total das lagoas. |
| `L19` | `=SUM(L13:L18)` | Consolida a quantidade total de amostras. |
| `G21` | `=B21*D21*B20` | Calcula volume geométrico a partir de dimensões e espessura; permanece zero por entradas vazias. |
| `K21` | `=J22/K19` | Divide o preço total da SubGeo pela área total, gerando preço em R$/m². |

### Referência de fornecedor/preço — EVIDÊNCIA CONFIRMADA

- anotação: `SubGeo ZAP em 15/05/25`;
- valor total: R$ 18.000,00;
- área: 13.440 m²;
- preço unitário calculado: R$ 1,339285714/m², exibido como aproximadamente R$ 1,34/m².

### Regras implícitas — EVIDÊNCIA PARCIAL

- Para as lagoas anaeróbias, a planilha utiliza 5 amostras por lagoa.
- Para a lagoa facultativa, utiliza 8 amostras por lagoa.
- A área usada para a batimetria é calculada pela projeção largura × comprimento × quantidade; a profundidade não participa da área.
- A cotação da empresa subcontratada é convertida em preço unitário por área para alimentar a composição de batimetria.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- A linha 19 do bloco principal está rotulada `Profundidade de dragagem (m)`, mas as células `K19` e `L19` contêm, respectivamente, **área total** e **quantidade total de amostras** do bloco lateral. A coincidência de linha é apenas visual; os conteúdos pertencem a estruturas diferentes.
- A célula `J22` contém R$ 18.000,00, apesar de a linha 22 do bloco principal ser `Tipo de Bota Fora`; o valor pertence ao quadro lateral da cotação.
- A célula `K24` contém `0,3` sem rótulo explicativo suficiente.
- O texto `(30x90x2)` aparece ao lado de `Volume dragagem`, mas não participa de fórmula e não coincide com as dimensões cadastradas das lagoas.

### DÚVIDAS

- O que representa o valor `0,3` em `K24`?
- A anotação `(30x90x2)` é resíduo de outro orçamento, aproximação de volume ou premissa ainda não transferida para fórmula?
- Qual critério técnico definiu 5 amostras por lagoa anaeróbia e 8 na facultativa?
- A profundidade cadastrada será usada futuramente para estimar volume de lodo, embora não seja usada neste preço?
- O preço SubGeo de R$ 18.000,00 inclui mobilização da própria contratada ou somente levantamento?

---

## 5.2 Aba `Produção`

### Objetivo

Modelar produção horária, produção mensal e prazo de uma draga.

### Papel no fluxo

Nesta proposta, a aba permanece como estrutura de modelo e não alimenta o `RESUMO`.

### Entradas observadas — EVIDÊNCIA CONFIRMADA

- vazão: vazia;
- eficiência: vazia;
- concentração: vazia;
- horas/dia: referência à aba `Dados Obra`;
- dias/mês: referência à aba `Dados Obra`;
- quantidade total a dragar: referência ao volume da aba `Dados Obra`, que está vazio.

### Fórmulas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula | Finalidade |
| --- | --- | --- |
| `H3` | `='Dados Obra '!B26` | Recebe horas de trabalho por dia. |
| `H4` | `='Dados Obra '!B27` | Recebe dias de trabalho por mês. |
| `H6` | `=H3*H4` | Calcula horas trabalhadas por mês. |
| `D8` | `=D3*(D4/100)*(D5/100)` | Calcula produção útil horária por vazão × eficiência × concentração. |
| `D11` | `=H6` | Replica horas mensais. |
| `D13` | `=D8*D11` | Calcula produção mensal. |
| `D18` | `=D13` | Replica produção mensal no cálculo de prazo. |
| `D21` | `='Dados Obra '!B14` | Recebe quantidade/volume total a dragar. |
| `F22` | `=D21/D8` | Calcula número de horas necessárias. |
| `D24` | `=D21/D8` | Replica prazo em horas. |
| `G24` | `=D24/9` | Converte horas para dias usando divisor fixo de 9 h/dia. |

### Resultados atuais — EVIDÊNCIA CONFIRMADA

- produção horária: 0;
- produção mensal: 0;
- prazo: `#DIV/0!` por divisão de volume vazio/zero por produção zero.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- A conversão de horas para dias em `G24` usa o número fixo `9`, embora a jornada exista como parâmetro em `H3`. Isso cria duplicação de premissa.
- As fórmulas usam o nome técnico `'Dados Obra '` com espaço final antes da aspa. Esse detalhe é significativo: ferramentas que removem o espaço do nome da aba podem transformar referências válidas no Excel em `#REF!`.
- A aba está incompleta e produz divisões por zero, mas esses erros não se propagam ao resumo comercial.

### EVIDÊNCIA PARCIAL

A presença desta aba indica reaproveitamento de um modelo de orçamento de dragagem, mesmo quando o escopo atual é apenas de estudos preliminares.

### DÚVIDAS

- A aba deveria ter sido removida/ocultada para esta proposta ou foi mantida intencionalmente para estimativa futura?
- O projeto de dragagem previsto no resumo deveria usar essa aba após levantamento de volume?
- Vazão, eficiência e concentração ainda não eram conhecidas ou são irrelevantes para o escopo contratado?

---

## 5.3 Aba `1. Mobilização`

### Objetivo

Compor o custo de deslocamento, integração, documentação, apoio e preparação da equipe para executar os levantamentos.

### Composição diária de mão de obra — EVIDÊNCIA CONFIRMADA

| Recurso | Quantidade | Valor-hora | Horas/dia | Leis sociais | Total diário |
| --- | ---: | ---: | ---: | ---: | ---: |
| Encarregado | 1 | R$ 30,375 | 9 | 110% | R$ 574,0875 |
| Operador Líder | 1 | R$ 28,4875 | 9 | 110% | R$ 538,41375 |
| Ajudante Geral – pré parada | 1 | R$ 14,125 | 9 | 110% | R$ 266,9625 |
| Terceirizados (SubGeo) | 2 | vazio | 9 | 110% | R$ 0 |
| Refeições | 5 | R$ 35,00 | — | — | R$ 175,00 |
| Transporte | 5 | R$ 15,00 | — | — | R$ 75,00 |
| **Custo por dia** | — | — | — | — | **R$ 1.629,46375** |

### Base salarial auxiliar — EVIDÊNCIA CONFIRMADA

- encarregado: R$ 24,30/h × 1,25 = R$ 30,375/h;
- operador de draga: R$ 22,79/h × 1,25 = R$ 28,4875/h;
- ajudante de draga: R$ 11,30/h × 1,25 = R$ 14,125/h;
- há rótulo `Engº`, mas não existe valor preenchido nessa tabela auxiliar.

### Serviços e custos — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Unidade | Quantidade | Preço unitário | Total usado | Observação |
| ---: | --- | --- | ---: | ---: | ---: | --- |
| 1 | Container almoxarifado | mês | vazia | R$ 600 | R$ 0 | Westrock |
| 2 | Container Sanitário/Vestiário | mês | vazia | R$ 850 | R$ 0 | Westrock |
| 3 | Container Escritório c/sanitário | mês | vazia | R$ 550 | R$ 0 | Westrock |
| 4 | Frete para Containers | vb | vazia | R$ 500 | R$ 0 | Westrock |
| 5 | PPRA + PCMSO + LTCAT | vb | 1 | R$ 2.500 | R$ 2.500 | — |
| 6 | ART Principal + ARTs corresponsáveis | vb | 1 | R$ 750 | R$ 750 | — |
| 7 | Placa de obra | vb | vazia | R$ 1.500 | R$ 0 | — |
| 8 | Vigilância | mês | vazia | R$ 8.000 | R$ 0 | Westrock |
| 9 | Água potável | gl | vazia | R$ 20 | R$ 0 | — |
| 10 | Material de escritório | mês | vazia | R$ 100 | R$ 0 | — |
| 11 | Mobiliário Casa | vb | vazia | R$ 4.000 | R$ 0 | — |
| 12 | Custo exames covid | un | vazia | R$ 350 | R$ 0 | — |
| 13 | Documentação e custo Bancodoc | un | 1 | R$ 1.000 | R$ 1.000 | `chute` |
| 14 | Treinamentos e acesso portal Gerdau | dia | 5 | R$ 500 | R$ 2.500 | — |
| 15 | Carro Peba + gasolina para viagem | dia | 2 | R$ 1.000 | R$ 2.000 | — |
| 16 | Carro Aguinaldo + gasolina para viagem | dia | 1 | R$ 1.000 | R$ 1.000 | — |
| 17 | Hospedagem + refeição | vb | 5 | R$ 1.100 | R$ 5.500 | — |
| 18 | Equipamentos de apoio (cordas, jarros etc.) | vb | 1 | R$ 500 | R$ 500 | — |
| 19 | Integração prévia | dia | 1 | R$ 1.629,46375 | R$ 1.629,46375 | — |
| 20 | Mão de obra (viagem e integração) | dia | 2 | R$ 1.629,46375 | R$ 3.258,9275 | — |
|  | **TOTAL** |  |  |  | **R$ 20.638,39125** |  |

### Memória de hospedagem/alimentação — EVIDÊNCIA CONFIRMADA

| Perfil | Hospedagem | Alimentação |
| --- | ---: | ---: |
| Eu | R$ 250 | R$ 100 |
| Líder | R$ 150 | R$ 100 |
| Ajudantes | R$ 150 | R$ 100 |
| Operador | R$ 150 | R$ 100 |
| **Totais** | **R$ 700** | **R$ 400** |

O total diário calculado é R$ 1.100,00 e alimenta o preço unitário de `Hospedagem + refeição`.

### Fórmulas importantes — EVIDÊNCIA CONFIRMADA

- mão de obra com encargos: `quantidade × R$/h × horas/dia × (1 + leis sociais/100)`;
- salários usados recebem acréscimo de 25% sobre a tabela auxiliar;
- refeições e transportes usam a soma de pessoas nas linhas de mão de obra;
- custo diário é a soma das linhas de equipe, refeições e transporte;
- totais de itens são quantidade × preço unitário;
- total da composição é a soma dos itens 1 a 20;
- `E32 = M35` transfere R$ 1.100/dia da memória de hospedagem/alimentação;
- `E34` e `E35` recebem o custo diário da equipe.

### Cálculo inferior não utilizado — EVIDÊNCIA CONFIRMADA

- `F38 = F36/F37`: preço unitário por prazo;
- `F39 = F38*(E39/100)`: BDI de 50%;
- `F40 = F38+F39`: preço final.

Como `F37` (`Prazo de Operação`) está vazio, as três células resultam em `#DIV/0!`.

### Regras e interpretações — EVIDÊNCIA PARCIAL

- Recursos listados com quantidade vazia permanecem como opções do modelo, mas têm custo zero nesta proposta.
- O custo de mobilização combina despesas únicas, despesas diárias e um custo diário de equipe.
- A SubGeo é contada como duas pessoas para refeição/transporte, embora sua mão de obra direta não receba valor-hora.
- O acréscimo de 25% parece transformar salário-base/hora em custo-hora adotado antes da aplicação de leis sociais.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- O título da aba é `CANTEIRO DE OBRAS : subitem da Dragagem`, embora o conteúdo e o nome da aba indiquem mobilização.
- A linha `Documentação e Custo Bancodoc` possui a observação explícita `chute`.
- `Custo exames covid` permanece no modelo, embora a proposta seja de 2025; não é possível concluir se é requisito vigente ou resíduo.
- O BDI interno de 50% não é usado pelo `RESUMO`, que importa o custo total antes desse cálculo e aplica 70%.
- A quantidade de `Terceirizados (SubGeo)` é usada para contagem de refeição/transporte, mas não há custo de hora associado.

### DÚVIDAS

- O acréscimo de 25% representa adicional, benefício, custo indireto ou atualização salarial?
- Por que leis sociais são 110% nesta composição?
- O custo de hospedagem de `Eu` corresponde a engenheiro, responsável comercial ou outro perfil?
- Os cinco dias de treinamento representam cinco pessoas por um dia, uma pessoa por cinco dias ou preço fechado diário?
- O custo de R$ 500/dia do portal Gerdau é taxa real, mão de obra ou estimativa?
- Os itens Westrock são referências de outro cliente/modelo ou fornecedores ainda válidos?

---

## 5.4 Aba `2.Amostras`

### Objetivo

Compor a coleta das amostras, análises laboratoriais, caracterização ambiental e logística de entrega.

### Mão de obra diária — EVIDÊNCIA CONFIRMADA

A aba replica a mesma estrutura e o mesmo custo diário de R$ 1.629,46375 da mobilização:

- 1 encarregado;
- 1 operador líder;
- 1 ajudante geral;
- 2 terceirizados SubGeo;
- 5 refeições;
- 5 transportes;
- leis sociais de 110%;
- jornada de 9 h/dia.

### Serviços — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Unidade | Quantidade | Preço unitário | Total |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | Análise laboratorial (12 amostras) | un | 18 | R$ 60 | R$ 1.080 |
| 2 | Caracterização NBR 10004 | un | 3 | R$ 4.095 | R$ 12.285 |
| 3 | Viagem para levar as amostras | vb | 1 | R$ 1.000 | R$ 1.000 |
| 4 | Mão de obra (coleta das amostras) | dia | 1 | R$ 1.629,46375 | R$ 1.629,46375 |
|  | **TOTAL** |  |  |  | **R$ 15.994,46375** |

### Referência de preço — EVIDÊNCIA CONFIRMADA

- `BioAgri em 21/05/25` está associado ao item de caracterização NBR 10004.

### Fórmulas e dependências — EVIDÊNCIA CONFIRMADA

- valores-hora e custos auxiliares são importados da aba `1. Mobilização`;
- quantidade de análises laboratoriais em `D16` recebe `Dados Obra!L19`, totalizando 18;
- custo da mão de obra da coleta usa o custo diário da equipe;
- total é a soma dos quatro itens.

### Cálculo inferior não utilizado — EVIDÊNCIA CONFIRMADA

Repete a estrutura:

- total ÷ prazo de operação;
- BDI de 50%;
- preço final.

O prazo está vazio e as células resultam em `#DIV/0!`. O resumo importa o custo total de R$ 15.994,46375 e aplica BDI próprio de 70%.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- A descrição do item 1 diz `Análise laboratorial (12 amostras)`, mas a quantidade utilizada é 18.
- A caracterização NBR 10004 usa quantidade 3, sem vínculo explícito com o número de lagoas, tipos de lagoa ou grupos de amostras.
- O título também é `CANTEIRO DE OBRAS : subitem da Dragagem`, incompatível com o conteúdo de amostragem.

### EVIDÊNCIA PARCIAL

- As 18 amostras individuais recebem análise de R$ 60 cada.
- As três caracterizações NBR 10004 podem corresponder às três lagoas físicas (duas anaeróbias e uma facultativa), mas a fórmula não comprova essa relação.

### DÚVIDAS

- O texto `12 amostras` deveria ter sido atualizado para 18?
- As três caracterizações NBR 10004 representam uma por lagoa, uma por tipo de lagoa ou três compostas?
- Qual laboratório/preço está associado ao valor de R$ 60 por amostra?
- A coleta em um dia é suficiente para as três lagoas por regra técnica ou estimativa comercial?

---

## 5.5 Aba `3. Batimetria`

### Objetivo

Compor o custo do levantamento batimétrico subcontratado e do acompanhamento da FOS.

### Mão de obra diária — EVIDÊNCIA CONFIRMADA

Repete a estrutura de R$ 1.629,46375/dia da mobilização e da amostragem.

### Serviços — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Unidade | Quantidade | Preço unitário | Total |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | Subcontratada – SUBGEO | m² | 13.440 | R$ 1,339285714 | R$ 18.000 |
| 2 | Mobilização | vb | 1 | R$ 2.500 | R$ 2.500 |
| 3 | descrição vazia | vazia | vazia | R$ 0 | R$ 0 |
| 4 | Mão de obra (acompanhamento) | dia | 2 | R$ 1.629,46375 | R$ 3.258,9275 |
|  | **TOTAL** |  |  |  | **R$ 23.758,9275** |

### Fórmulas e dependências — EVIDÊNCIA CONFIRMADA

- quantidade do serviço SubGeo = área total das lagoas (`Dados Obra!K19`);
- preço unitário SubGeo = preço total cotado ÷ área (`Dados Obra!K21`);
- custo SubGeo = 13.440 × 1,339285714 = R$ 18.000;
- acompanhamento FOS = 2 dias × custo diário da equipe;
- total = soma dos quatro itens.

### Cálculo inferior não utilizado — EVIDÊNCIA CONFIRMADA

O prazo está vazio, portanto preço unitário, BDI interno de 50% e preço final resultam em `#DIV/0!`. O resumo usa o total de custo antes desse bloco.

### Regras e interpretações — EVIDÊNCIA PARCIAL

- A subcontratação é tratada como custo variável por m², derivado de uma cotação global.
- A mobilização da SubGeo/FOS é acrescida separadamente ao preço cotado.
- A FOS prevê dois dias de acompanhamento com a equipe completa modelada na aba de mobilização.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- Existe item 3 sem descrição, unidade ou quantidade, com preço unitário e total zero.
- O título genérico de canteiro/dragagem não descreve a finalidade real da aba.
- Não está explícito se a mobilização de R$ 2.500 pertence à SubGeo, à FOS ou a ambas.
- O custo diário de acompanhamento inclui 2 terceirizados SubGeo na contagem de refeição/transporte, enquanto a linha de serviço SubGeo já é cobrada separadamente.

### DÚVIDAS

- A cotação de R$ 18.000 já incluía mobilização?
- Os dois dias de acompanhamento são dias de campo, viagem ou processamento?
- A equipe completa é necessária durante a batimetria ou o custo diário foi reaproveitado sem ajuste?
- O item 3 vazio representa recurso removido ou reserva de modelo?

---

## 5.6 Aba `4. Projeto`

### Objetivo

Compor o custo de engenharia para elaborar o projeto e o escopo da futura dragagem.

### Mão de obra diária — EVIDÊNCIA CONFIRMADA

| Recurso | Quantidade | Valor-hora | Horas/dia | Leis sociais | Total diário |
| --- | ---: | ---: | ---: | ---: | ---: |
| Engenheiro | 1 | R$ 90 | 9 | 110% | R$ 1.701 |
| Refeição | 1 | R$ 35 | — | — | R$ 35 |
| Transporte | 1 | R$ 15 | — | — | R$ 15 |
| **Custo por dia** | — | — | — | — | **R$ 1.751** |

### Serviços — EVIDÊNCIA CONFIRMADA

| Item | Descrição | Unidade | Quantidade | Preço unitário | Total |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | descrição vazia | vazia | vazia | R$ 75 | R$ 0 |
| 2 | descrição vazia | vazia | vazia | R$ 0 | R$ 0 |
| 3 | descrição vazia | vazia | vazia | R$ 0 | R$ 0 |
| 4 | Mão de obra | dia | 5 | R$ 1.751 | R$ 8.755 |
|  | **TOTAL** |  |  |  | **R$ 8.755** |

### Fórmulas — EVIDÊNCIA CONFIRMADA

- custo do engenheiro: 1 × R$ 90/h × 9 h × (1 + 110%) = R$ 1.701/dia;
- refeição e transporte somam R$ 50/dia;
- custo diário total: R$ 1.751;
- projeto: 5 dias × R$ 1.751 = R$ 8.755.

### Cálculo inferior não utilizado — EVIDÊNCIA CONFIRMADA

Repete a divisão por prazo vazio, BDI interno de 50% e preço final, todos com `#DIV/0!`. O resumo usa o custo total.

### Regras e interpretações — EVIDÊNCIA PARCIAL

- O esforço de projeto é estimado em cinco dias de um engenheiro.
- O custo-hora do engenheiro é informado diretamente como R$ 90 e depois recebe 110% de leis sociais.
- Não há custos explícitos de software, desenho, levantamento complementar, revisão ou emissão documental.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- Três itens vazios permanecem na composição.
- O item 1 possui preço unitário de R$ 75,00 sem descrição, quantidade ou total.
- A célula `D8` ainda referencia a jornada da aba `Dados Obra`, mas a linha está vazia e não participa do total.
- O título genérico de canteiro/dragagem não corresponde ao conteúdo de projeto.

### DÚVIDAS

- O valor-hora de R$ 90 é salário, custo pleno, preço histórico ou valor comercial?
- O item vazio de R$ 75 representa impressão, ART, plotagem ou outro recurso removido?
- Os cinco dias incluem elaboração, revisão, reunião e emissão final?
- O projeto inclui apenas escopo de dragagem ou também estimativa de volume e método executivo?

---

## 5.7 Aba `RESUMO`

### Objetivo

Consolidar custos das quatro composições e formar o preço de venda.

### Composição comercial — EVIDÊNCIA CONFIRMADA

| Item | Serviço | Custo total | Quantidade | Unidade | Custo unitário | BDI | Preço unitário | Preço total |
| ---: | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | Mobilização | R$ 20.638,39125 | 1 | un | R$ 20.638,39125 | 70% | R$ 35.085,265125 | R$ 35.085,265125 |
| 2 | Coleta de amostras e análise geral | R$ 15.994,46375 | 1 | un | R$ 15.994,46375 | 70% | R$ 27.190,588375 | R$ 27.190,588375 |
| 3 | Batimetria | R$ 23.758,9275 | 1 | un | R$ 23.758,9275 | 70% | R$ 40.390,17675 | R$ 40.390,17675 |
| 4 | Elaboração do projeto e Escopo Dragagem | R$ 8.755 | 1 | un | R$ 8.755 | 70% | R$ 14.883,50 | R$ 14.883,50 |
|  | **Totais** | **R$ 69.146,7825** |  |  |  |  |  | **R$ 117.549,53025** |

### Resultado comercial — EVIDÊNCIA CONFIRMADA

- custo total: R$ 69.146,7825;
- acréscimo absoluto sobre custo: R$ 48.402,74775;
- preço de venda calculado: R$ 117.549,53025;
- área: 13.440 m²;
- preço equivalente: R$ 8,7462448103/m²;
- preço final apresentado: R$ 117.549.

### Fórmulas — EVIDÊNCIA CONFIRMADA

| Célula | Fórmula | Finalidade |
| --- | --- | --- |
| `C4` | `='1. Mobilização'!F36` | Importa custo de mobilização. |
| `G4` | `=C4` | Define custo unitário para quantidade 1. |
| `I4` | `=((H4/100)+1)*G4` | Aplica BDI de 70%. |
| `J4` | `=E4*I4` | Calcula preço total. |
| `C5` | `='2.Amostras'!F20` | Importa custo da amostragem. |
| `G5` | `=C5/E5` | Calcula custo unitário. |
| `C6` | `='3. Batimetria'!F20` | Importa custo de batimetria. |
| `C7` | `='4. Projeto'!F20` | Importa custo de projeto. |
| `G7` | `=C7/E7` | Calcula custo unitário. |
| `C8` | `=SUM(C4:C7)` | Soma custos. |
| `J8` | `=SUM(J4:J7)` | Soma preços de venda. |
| `J9` | `=J8-C8` | Calcula diferença entre preço e custo. |
| `J11` | `='Dados Obra '!K19` | Importa área total. |
| `J12` | `=J8/J11` | Calcula preço de venda por m². |

As fórmulas de preço nas linhas 5 e 6 são cópias/preenchimentos equivalentes às linhas exibidas, embora o extrator tenha listado explicitamente apenas parte delas.

### Regra comercial observada — EVIDÊNCIA PARCIAL

- Cada pacote recebe BDI uniforme de 70%.
- O preço final apresentado é truncado/arredondado de R$ 117.549,53025 para R$ 117.549,00, reduzindo R$ 0,53025.
- O preço por m² é indicador global do pacote completo, não apenas do serviço de batimetria.

### Anomalias observadas — EVIDÊNCIA CONFIRMADA

- As abas individuais exibem BDI de 50%, porém o resumo aplica 70% sobre o custo. O BDI de 50% das abas não influencia o preço final.
- A linha `Preço de Venda` está posicionada na coluna H enquanto o valor está na coluna J.
- A linha 9 contém a margem/acréscimo absoluto de R$ 48.402,74775, mas não possui rótulo.
- O preço final apresentado não usa fórmula observada; é valor digitado.
- A unidade comercial dos quatro itens é `un`, enquanto o resumo também calcula referência em R$/m².

### DÚVIDAS

- O BDI correto desta proposta é 70%, e os 50% das composições são resíduos de modelo?
- O preço final apresentado deveria ser R$ 117.550,00 por arredondamento convencional?
- A diferença preço − custo representa margem bruta, BDI em valor ou apenas acréscimo comercial sem separação de impostos e lucro?
- O preço por m² foi usado para comparação comercial, negociação ou medição contratual?

---

# 6. Entidades conceituais encontradas

## EVIDÊNCIA CONFIRMADA

- proposta;
- cliente;
- contato;
- objeto;
- lagoa;
- tipo de lagoa;
- geometria da lagoa;
- área;
- profundidade;
- amostra;
- análise laboratorial;
- caracterização NBR 10004;
- fornecedor/subcontratada;
- cotação datada;
- mobilização;
- integração;
- documentação de segurança e saúde;
- ART;
- treinamento e portal do cliente;
- viagem;
- hospedagem;
- alimentação;
- transporte;
- equipe;
- função profissional;
- salário-base/hora;
- custo-hora adotado;
- leis sociais;
- custo diário;
- item de composição;
- unidade;
- quantidade;
- preço unitário;
- custo total;
- BDI;
- preço de venda;
- preço equivalente por m²;
- projeto;
- escopo de dragagem;
- produção de draga;
- prazo.

# 7. Dependências entre abas

## EVIDÊNCIA CONFIRMADA

```text
Dados Obra
├── horas/dia ──────────────→ Produção
├── dias/mês ───────────────→ Produção
├── horas/dia ──────────────→ composições de mão de obra
├── total de amostras ──────→ 2.Amostras
├── área total ─────────────→ 3. Batimetria
├── preço SubGeo por m² ────→ 3. Batimetria
└── área total ─────────────→ RESUMO

1. Mobilização
├── valores-hora ───────────→ 2.Amostras
├── valores-hora ───────────→ 3. Batimetria
├── refeição/transporte ────→ 2.Amostras, 3.Batimetria e 4.Projeto
└── custo total ────────────→ RESUMO

2.Amostras ─ custo total ───→ RESUMO
3.Batimetria ─ custo total ─→ RESUMO
4.Projeto ─ custo total ────→ RESUMO
```

A aba `Produção` não possui saída usada pelas demais abas neste arquivo.

# 8. Regras de cálculo observadas

## EVIDÊNCIA CONFIRMADA

1. **Área de lagoa:** largura × comprimento × quantidade de lagoas.
2. **Amostras anaeróbias:** 5 × quantidade de lagoas.
3. **Amostras facultativa:** 8 × quantidade de lagoas.
4. **Preço SubGeo por m²:** cotação global ÷ área total.
5. **Mão de obra diária:** quantidade × custo-hora × horas/dia × (1 + leis sociais).
6. **Refeição/transporte:** quantidade total de pessoas × valor unitário.
7. **Item de composição:** quantidade × preço unitário.
8. **Custo do pacote:** soma dos itens.
9. **Preço com BDI:** custo unitário × (1 + BDI/100).
10. **Preço total:** quantidade comercial × preço unitário com BDI.
11. **Preço global por m²:** preço de venda total ÷ área total.
12. **Produção genérica da draga:** vazão × eficiência × concentração.
13. **Horas mensais:** horas/dia × dias/mês.
14. **Prazo em horas:** volume ÷ produção horária.

# 9. Valores embutidos e coeficientes

## EVIDÊNCIA CONFIRMADA, confiança Nível C

| Valor | Uso observado |
| ---: | --- |
| 5 amostras/lagoa | Lagoas anaeróbias |
| 8 amostras/lagoa | Lagoa facultativa |
| 25% | Acréscimo sobre salários-base auxiliares |
| 110% | Leis sociais nas composições |
| 9 h/dia | Jornada |
| 22 dias/mês | Calendário |
| R$ 35/pessoa | Refeição |
| R$ 15/pessoa | Transporte |
| R$ 60/amostra | Análise laboratorial |
| R$ 4.095/un | Caracterização NBR 10004 |
| 3 unidades | Caracterizações NBR 10004 |
| R$ 18.000 | Cotação SubGeo datada de 15/05/2025 |
| R$ 2.500 | Mobilização na batimetria |
| 2 dias | Acompanhamento da batimetria |
| R$ 90/h | Engenheiro |
| 5 dias | Elaboração do projeto |
| 50% | BDI nas abas de composição, não utilizado no resumo |
| 70% | BDI efetivamente usado no resumo |
| 0,3 | Valor sem identificação em `Dados Obra!K24` |

Nenhum desses valores deve ser tratado como constante geral da FOS sem validação e crosscheck.

# 10. Terminologias e nomenclaturas

## EVIDÊNCIA CONFIRMADA

- `vb`: verba/preço global, interpretação usual não explicitada no arquivo;
- `un`: unidade;
- `mês`: custo mensal;
- `dia`: custo diário;
- `gl`: galão, interpretação provável, não explicitada;
- `m²`: metro quadrado;
- `L.Sociais`: leis sociais/encargos;
- `Bancodoc`: sistema/serviço documental citado;
- `PPRA`, `PCMSO`, `LTCAT`: documentos/programas de segurança e saúde;
- `ART`: Anotação de Responsabilidade Técnica;
- `NBR 10004`: referência de caracterização/classificação de resíduos;
- `SubGeo`: empresa subcontratada/referência de cotação;
- `BioAgri`: referência de laboratório/fornecedor de caracterização;
- `ZAP`: registro de cotação por WhatsApp;
- `Peba`, `Aguinaldo`: identificadores informais associados a carros/pessoas;
- `Eu`: perfil informal usado na memória de hospedagem.

# 11. Anomalias transversais

## EVIDÊNCIA CONFIRMADA

1. **Nome de aba com espaço final:** fórmulas referenciam `'Dados Obra '`. Esse espaço é parte técnica do nome usado pelas fórmulas e pode ser perdido por ferramentas.
2. **Títulos copiados:** quatro abas exibem `CANTEIRO DE OBRAS : subitem da Dragagem`, embora tratem de mobilização, amostras, batimetria e projeto.
3. **Blocos de prazo vazios:** todas as composições têm cálculos inferiores de preço unitário, BDI de 50% e preço final, mas o prazo está vazio e gera `#DIV/0!`.
4. **Erros não propagados:** o resumo importa o custo total anterior aos erros; assim, o preço comercial permanece calculável.
5. **Dois BDIs:** 50% nas composições e 70% no resumo; somente 70% influencia a venda.
6. **Itens vazios/residuais:** há linhas sem descrição e preços zero ou valor unitário isolado.
7. **Referências informais:** `chute`, `Eu`, nomes próprios e fornecedores de outros contextos aparecem no arquivo.
8. **Dados principais incompletos:** local, e-mail, material, volume, bota-fora e sistema de medição não foram preenchidos.
9. **Aba de produção não utilizada:** contém estrutura de dragagem, mas não participa do resumo.
10. **Descrição desatualizada:** `Análise laboratorial (12 amostras)` é calculada com 18 amostras.
11. **Preço final digitado:** R$ 117.549 não é fórmula e difere em R$ 0,53025 do total calculado.
12. **Indicador sem rótulo:** R$ 48.402,74775 aparece como diferença entre venda e custo sem identificação.
13. **Valor órfão:** `0,3` em `Dados Obra!K24` não possui finalidade comprovável.

# 12. Conhecimentos específicos deste orçamento

## EVIDÊNCIA CONFIRMADA

- O objeto é batimetria de lagoas de estabilização da Gerdau.
- A área total considerada é 13.440 m².
- Existem três lagoas físicas: duas anaeróbias e uma facultativa.
- Foram orçadas 18 amostras.
- A batimetria da SubGeo foi cotada em R$ 18.000 em 15/05/2025.
- A caracterização NBR 10004 foi referenciada à BioAgri em 21/05/2025.
- O custo total calculado é R$ 69.146,7825.
- O preço de venda calculado é R$ 117.549,53025.
- O preço final apresentado é R$ 117.549.
- O equivalente comercial é R$ 8,7462448103/m².

# 13. Possíveis padrões para crosscheck

## EVIDÊNCIA PARCIAL

- Orçamentos de estudos preliminares podem ser organizados em mobilização, amostragem, levantamento técnico e projeto.
- Cotações globais de subcontratados podem ser convertidas em preço unitário físico para composição.
- Custos diários de equipe podem ser centralizados em uma aba e reaproveitados.
- O resumo pode aplicar BDI diferente daquele existente nas abas de composição.
- Recursos opcionais podem permanecer no modelo com quantidade vazia e custo zero.
- O preço total pode ser convertido em indicador unitário por área para comparação/negociação.
- Planilhas derivadas de modelos de dragagem podem conservar abas e campos não usados no escopo atual.

Esses pontos não são regras gerais e dependem de outros arquivos e validação do especialista.

# 14. Dúvidas consolidadas para validação futura

1. Qual é o significado de `0,3` em `Dados Obra!K24`?
2. O que representa `(30x90x2)` próximo ao volume?
3. Qual regra define 5 e 8 amostras por lagoa?
4. As três caracterizações NBR 10004 correspondem às três lagoas?
5. Por que a descrição cita 12 amostras, mas a quantidade é 18?
6. A cotação SubGeo de R$ 18.000 inclui mobilização?
7. O item de mobilização de R$ 2.500 pertence a quem?
8. Por que a equipe de acompanhamento inclui os terceirizados na contagem de alimentação/transporte?
9. O acréscimo salarial de 25% representa qual componente?
10. Por que as leis sociais são 110%?
11. Qual é a finalidade dos itens vazios nas composições?
12. Qual BDI deve ser considerado correto: 50% ou 70%?
13. O preço final apresentado deveria ser arredondado para R$ 117.550?
14. A diferença preço − custo é tratada como BDI, margem, lucro bruto ou indicador sem decomposição?
15. A aba `Produção` deveria ser utilizada após a batimetria para gerar o escopo de dragagem?
16. A unidade contratual final é pacote (`un`) ou área (`m²`)?
17. O valor-hora de engenheiro de R$ 90 é custo pleno ou salário-base?
18. O item vazio de R$ 75 na aba de projeto representa qual recurso?
19. O orçamento foi efetivamente apresentado/contratado ou é apenas composição interna?

# 15. Limitações da análise

## EVIDÊNCIA CONFIRMADA

- A análise foi realizada sobre o arquivo Excel fornecido, sem acesso a proposta em PDF, contrato, e-mails, mensagens, cotações originais ou resultado executado.
- Não houve esclarecimento do especialista durante esta sessão.
- Fórmulas foram analisadas com seus valores armazenados no arquivo.
- O nome da aba `Dados Obra` apresenta evidência de espaço final nas referências; ferramentas de leitura podem normalizar esse nome e exibir `#REF!` durante recálculo fora do Excel. A análise preservou as fórmulas originais e os valores armazenados.
- Não foi possível determinar intenção de negócio de células órfãs, itens vazios e textos residuais sem evidência adicional.
- Nenhuma conclusão deste documento foi comparada para consolidação com outros orçamentos.

# 16. Validação final

- [x] Todas as sete abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Identidade integral do arquivo preservada.
- [x] Fórmulas importantes registradas com finalidade operacional.
- [x] Entradas, saídas, dependências, entidades, regras, exceções e anomalias registradas.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhum documento de outro orçamento alterado.
- [x] Nenhum índice geral alterado.
- [x] Nenhuma consolidação realizada.
- [x] Nenhuma decisão arquitetural tomada.
