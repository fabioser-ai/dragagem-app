# Modelo 019 — D_008_2025 - ENGEVIX - Corsan.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `D_008_2025 - ENGEVIX - Corsan.xlsx`
- Família provisória: **Dragagem com bags/geotêxteis**
- SHA-256 do arquivo: `e0ec4b77cafb12fa297b48835411d04cbc4281894c5d2cf64561405c4fba9cfa`
- Abas analisadas: **15**
- Fórmulas encontradas: **356**

## Conceitos identificados

- `desmobilizacao`: 2 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `mobilizacao_sistema`: 2 aba(s)
- `bags_geotexteis`: 1 aba(s)
- `barrilete_linha`: 1 aba(s)
- `canteiro`: 1 aba(s)
- `cotacoes`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `dragagem_operacao`: 1 aba(s)
- `estrutura_desaguamento`: 1 aba(s)
- `formacao_preco`: 1 aba(s)
- `medicao_batimetria`: 1 aba(s)
- `operacao_desaguamento`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:H27` | 3 | dados_obra |
| 2 | `Cotaçoes` | `A1:G55` | 1 | cotacoes |
| 3 | `Produção` | `A1:H24` | 9 | producao_prazo |
| 4 | `Barrilete` | `A1:F31` | 26 | barrilete_linha |
| 5 | `1. Mob. Draga` | `A1:G31` | 19 | mobilizacao_draga |
| 6 | `2. Mob. Eq. Polimero` | `A1:G31` | 17 | mobilizacao_sistema |
| 7 | `Canteiro` | `A1:G32` | 22 | canteiro |
| 8 | `3. Prep. Célula` | `A1:P30` | 34 | estrutura_desaguamento |
| 9 | `4. Forn. Bag` | `A1:L56` | 40 | bags_geotexteis |
| 10 | `5. Operação Sistema` | `A1:H27` | 19 | operacao_desaguamento |
| 11 | `7. Dragagem` | `A1:L253` | 78 | dragagem_operacao |
| 12 | `8. Medição` | `A1:F23` | 18 | medicao_batimetria |
| 13 | `10. Desmob. Draga` | `A1:F21` | 20 | mobilizacao_draga, desmobilizacao |
| 14 | `11. Desmob. Eq. Polimero` | `A1:F26` | 16 | mobilizacao_sistema, desmobilizacao |
| 15 | `10. Plan. Preços` | `A1:O14` | 34 | formacao_preco |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `Dados Obra` | 18 |
| `1. Mob. Draga` | 5 |
| `4. Forn. Bag` | 3 |
| `3. Prep. Célula` | 2 |
| `10. Desmob. Draga` | 1 |
| `11. Desmob. Eq. Polimero` | 1 |
| `2. Mob. Eq. Polimero` | 1 |
| `5. Operação Sistema` | 1 |
| `7. Dragagem` | 1 |
| `8. Medição` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:H27`
- Fórmulas: **3**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **12**

#### Rótulos e textos observados

- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- Proposta
- Proposta D_008_2025
- Data
- Cliente
- Engevix - Corsan
- Contato
- e-mail
- Dados da obra
- Objeto
- Dragagem ETE ANA TERRA
- Local
- CRUZ ALTA (RS)
- Volume dragagem (m³)
- Tipo de material
- ESGOTO
- Distância de Recalque (m)
- Seio da linha =
- Total
- Linha Flutuante (m)
- Linha de terra (m)
- Profundidade de dragagem (m)
- Espessura média de dragagem (m)
- Área de Dragagem (m² ou L x C)
- X
- Volume (m³) =
- Tipo de Bota Fora
- Bag
- Sistema de Medição
- M3 ( Batimetria) NAO IREMOS ACEITAR - PROPOR preço por M3 base seca
- Canteiro de obras
- FOS
- Mobilização
- Horário de Trabalho (das 7 as 17h)
- h/dia
- Dias de Trabalho (2ª a 6ª)
- dias/mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `H16` | `=B16+E16` |
| `H17` | `=B17+E17` |
| `G21` | `=B21*D21*B20` |

### 2. Cotaçoes

- Faixa usada: `A1:G55`
- Fórmulas: **1**
- Conceitos provisórios: cotacoes
- Células numéricas observadas: **6**

#### Rótulos e textos observados

- COTAÇÕES
- GUINDASTE
- NOME
- CONTATO
- TELEFONE
- DETALHE
- PREÇO (hora)
- PREÇO (DIÁRIA)
- IDEAL
- GIL(A)
- (13) 3209-9100
- Guindaste 50 toneladas
- gil@idealguindastes.com.br
- Sem frete
- CONTAINER
- PREÇO / MÊS
- FRETE / HORA
- MOVIMENTAÇAO MATERIAL
- PREÇO / dia
- FOX
- Guilherme
- (13) 97423-7742
- Escavadeira Hidraulica
- Caminhao 17 m3
- Frete Ida e Volta
- BRITA
- PREÇO / M3
- ENGEBRITA
- (13) 99742-6383
- vendas@engebrita.com.br
- ZAP ((13) 99707-1952
- RUBAO
- Mercia
- (13) 97424-5327
- Brita #2 - Posto em Obra
- Natã
- (13) 99685-9775
- CARRETA
- LINCE
- FABIANO
- https://www.lojadaconstrucao.com.br/reservatorio-de-fibra-20-000-litros-bakof-tec.html

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `None` | `` |

### 3. Produção

- Faixa usada: `A1:H24`
- Fórmulas: **9**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **12**

#### Rótulos e textos observados

- Cálculo de Produção da Draga
- Horas Trabalhadas por mês
- Unid.
- Quant.
- Vazão
- m³/h
- Horas / dia (7 as 17h)
- Eficiência
- %
- Dias / Mês (2ª a sexta)
- Concentração
- Total de Horas / mês
- Produção
- Horas trabalhadas
- h/mês
- Produção mensal (m³/mês)
- Cálculo do Prazo da obra
- Produção mensal
- m³/mês
- Quantidade total a dragar
- m³
- Prazo de Execução
- mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `H3` | `='Dados Obra '!B26` |
| `H4` | `='Dados Obra '!B27` |
| `H6` | `=H3*H4` |
| `D8` | `=D3*(D4/100)*(D5/100)` |
| `D11` | `=H6` |
| `D13` | `=D8*D11` |
| `D18` | `=D13` |
| `D21` | `='Dados Obra '!B14` |
| `D24` | `=D21/D18` |

### 4. Barrilete

- Faixa usada: `A1:F31`
- Fórmulas: **26**
- Conceitos provisórios: barrilete_linha
- Células numéricas observadas: **77**

#### Rótulos e textos observados

- Composição - BARRILETE - unidade: Global
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador de Draga + técnico operação polím.
- Ajudante Geral
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Tubo de ferro c/6m diametro de 8"
- pç
- Toco 0,50m
- Joelho 90°
- Tee 6" x 4" flangeado
- Ponteira flange x escama diam. 4"
- Cap. 6"
- Válvula Gaveta 4"
- Válvula Gaveta 3"
- Mangueira Conduto d'água
- m
- Braçadeiras
- Curva longa de PVC 4"
- Válvula esfera 2"
- Bomba lameira
- Mão de obra de montagem
- dia
- TOTAL
- 20 % de depreciação
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A5+A6` |
| `F7` | `=A7*C7` |
| `A8` | `=A5+A6` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `E14` | `=400*1.4` |
| `F14` | `=D14*E14` |
| `E15` | `=165*1.4` |
| `E16` | `=165*1.4` |
| `E17` | `=220*1.4` |
| `E18` | `=55*1.4` |
| `E19` | `=35*1.4` |
| `E20` | `=2000*1.4` |
| `E21` | `=1100*1.4` |
| `E23` | `=14*1.4` |
| `E24` | `=35*1.4` |
| `E25` | `=60*1.4` |
| `E27` | `=F9` |
| `F28` | `=SUM(F14:F27)` |
| `F29` | `=F28*0.2` |
| `F30` | `=F29*(E30/100)` |
| `F31` | `=F29+F30` |

### 5. 1. Mob. Draga

- Faixa usada: `A1:G31`
- Fórmulas: **19**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **58**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 6"
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
- Operador de Draga
- Ajudante Geral
- Tecnico de Segurança
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Guindaste para carregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Mobiliário Canteiro
- vb
- Carreta Carga Seca para DRAGA
- un
- Fabiano (
- Guindaste p/descarregamento e montagem DRAGA
- Ideal - 400 hora - minimo 10 horas (06/09/24) - 50 toneladas
- Frete
- Trator D4 para lançar draga na água
- Mão de obra p/carga e montagem (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- Dois retornos

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=A5+A7+A6` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `E23` | `=F11` |
| `F24` | `=SUM(F16:F23)` |
| `F25` | `=F24*(E25/100)` |
| `F26` | `=SUM(F24:F25)` |
| `F28` | `=SUM(F26:F27)` |

### 6. 2. Mob. Eq. Polimero

- Faixa usada: `A1:G31`
- Fórmulas: **17**
- Conceitos provisórios: mobilizacao_sistema
- Células numéricas observadas: **66**

#### Rótulos e textos observados

- 2 - MOBILIZAÇÃO E MONTAGEM DE EQUIP. POLÍMERO
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador de Polimero
- Operador Lider
- Ajudante Geral
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Verba para Cobertura do equipamento
- vb
- Munck para montagem cobertura
- Muncar
- Brita 1 para lastro no piso
- m³
- Concreto para piso
- Frete para mobilização do equipamento
- Fabiano
- Instalações hidráulicas
- Instalações elétricas
- Máquina Wap
- Barrilete
- Mão de obra de apoio na montagem
- dia
- TOTAL
- BDI (%)
- Preço Final
- 2 mobilizaçoes

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `='Dados Obra '!B26` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=SUM(A5:A7)` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `F15` | `=D15*E15` |
| `E19` | `='1. Mob. Draga'!E19` |
| `E23` | `=Barrilete!F31` |
| `E24` | `=F10` |
| `F26` | `=SUM(F15:F24)` |
| `F27` | `=F26*(E27/100)` |
| `F28` | `=SUM(F26:F27)` |

### 7. Canteiro

- Faixa usada: `A1:G32`
- Fórmulas: **22**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **77**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Lider
- Operador de Draga
- Ajudante Geral
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Container almoxarifado
- mês
- #NAME?
- Orçar
- Container Refeitório
- Container Escritório
- Frete para Containers
- vb
- PPRA + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Placa de obra
- Vigilância
- água potável
- gl
- material de escritório
- Banheiro Quimico
- mes
- custo Exames médicos
- un
- Mão de obra (integração)
- dia
- TOTAL
- Prazo de Operação
- preço unitário
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `A9` | `=A5+A6+A7` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `D15` | `=ROUNDUP(Produção!D24,0)+1` |
| `F15` | `=D15*E15` |
| `D16` | `=D15` |
| `D17` | `=D15` |
| `D23` | `=8*D15` |
| `D24` | `=D15` |
| `D25` | `=D15` |
| `D26` | `=A8` |
| `E27` | `=F10` |
| `F28` | `=SUM(F15:F27)` |
| `F29` | `=D15-1` |
| `F30` | `=F28/F29` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=F30+F31` |

### 8. 3. Prep. Célula

- Faixa usada: `A1:P30`
- Fórmulas: **34**
- Conceitos provisórios: estrutura_desaguamento
- Células numéricas observadas: **92**

#### Rótulos e textos observados

- 3. PREPARO DE CÉLULA - Manta PEAD
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Área da
- Quant.
- Operador Líder
- Composição Real
- Célua
- total
- Operador de Draga
- Manta PEAD
- m²/m² de Célula
- m²
- Ajudante Geral
- Bidim
- Refeições
- Brita
- m³/m² de Célula
- m³
- Transporte
- Retro escavadeira
- h/m² de Célula
- h
- Custo por dia
- Mão de Obra
- (4 oficiais + 6 ajudantes)
- dias
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Preparo Terreno - Patrola / tratos de esteira
- dia
- Orçar
- Mobilização dao Patrola
- Preparo Terreno - Aluguel de Retro
- Mobilização/desmobilização de Retro
- Regularização manual - Mão de obra
- PEAD
- Média Danilo (Curitiba)
- Material de emprestimo
- 233 m3 Area 1 + 300 m3 Area 3 Elias Fausto
- Mão de obra instal. PEAD
- taxa Mobilizaçao PEAD Mao de obras
- vb
- Bidim RT 14 (4,90 x 100m)
- Danilo (Diprotec) 2,80 - Bidim GT 07
- Brita 2
- Natã - Rubão 06/09/24 - R$158,00 posto em obra
- Retro escavadeira para espalhamento Brita
- Mão de obra de instal. Bidim e Brita
- TOTAL
- Quantidade de Repetiçoes
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `O6` | `=K6*N6` |
| `D7` | `='Dados Obra '!B26` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `N7` | `=N6` |
| `O7` | `=K7*N7` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `N8` | `=N6` |
| `O8` | `=K8*N8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `N9` | `=N6` |
| `O9` | `=K9*N9` |
| `F10` | `=SUM(F5:F9)` |
| `N10` | `=N6` |
| `O10` | `=K10*N10` |
| `O11` | `=O10/10` |
| `F15` | `=D15*E15` |
| `E19` | `=F10` |
| `D20` | `=O6` |
| `D22` | `=D20` |
| `F22` | `=D22*E22` |
| `E23` | `=5000+3500` |
| `F23` | `=D23*E23` |
| `D24` | `=O7` |
| `D25` | `=O8*1.2` |
| `E27` | `=F10` |
| `F28` | `=SUM(F15:F27)` |
| `F29` | `=F28*E29` |
| `F30` | `=F29` |

### 9. 4. Forn. Bag

- Faixa usada: `A1:L56`
- Fórmulas: **40**
- Conceitos provisórios: bags_geotexteis
- Células numéricas observadas: **121**

#### Rótulos e textos observados

- 4. Fornecimento de Bag
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
- Operador de Draga
- Ajudante Geral
- Refeições
- Transporte
- Custo por dia
- Será fornecido pela propria SABESP
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Bag 8 x 10m
- pç
- ELIAS FAUSTO
- Bags
- Bag 8 x 13m
- CABREUVA
- Bag 8 x 14m
- Bag 8 x 15m
- Bag 8 x 20m
- Bag 6 x 15m
- Bag 8,00 x 30m
- Bag 8,00 x 25,00m
- pc
- Bag 6,00 x 30,00m
- Frete para os Bags
- un
- Munck para descarregamento
- dia
- Mão de obra para instalação
- TOTAL
- BDI (%)
- Preço Final
- Volume
- % Solidos situ
- Tonelada Seca
- % Solidos Desagua
- Volume de material a ser acomodado em bags
- Possivel colocar em área
- Volume total
- Reinicio Celula
- Volume Final
- BAG 6 x 50
- Bag 8 x 30
- /m3
- Bag 8 x 25
- Bag 18 x 13
- Bag 6 x 30
- Bag 8 x 10
- Bag 8 x 13
- Bag 8 x 14
- Bag 8 x 15
- Bag 8 x 20
- Bag 6 x 15
- Area total (m2)
- Preço unitario (m2)
- Valor total
- Valor por bag
- P18 x 30

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `='Dados Obra '!B26` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `E15` | `=G46*B46` |
| `F15` | `=D15*E15` |
| `E16` | `=G47*B47` |
| `E21` | `=G56` |
| `E22` | `=G43*B43` |
| `E23` | `=B45*H15*1.1` |
| `E26` | `=F10` |
| `F27` | `=SUM(F15:F26)` |
| `F28` | `=F27*(E28/100)` |
| `F29` | `=SUM(F27:F28)` |
| `F30` | `=F29/D21` |
| `B33` | `='Dados Obra '!B14` |
| `B35` | `=B33*B34` |
| `B37` | `=B35/B36` |
| `D41` | `=B41*C41` |
| `F41` | `=E41*D41` |
| `C42` | `=B37/B42` |
| `I42` | `=B42*G42` |
| `D46` | `=B46*C46` |
| `F46` | `=E46*D46` |
| `D47` | `=B47*C47` |
| `F47` | `=E47*D47` |
| `C52` | `=SUM(C41:C51)` |
| `D52` | `=SUM(D41:D51)` |
| `F52` | `=SUM(F41:F51)` |
| `B56` | `=18*30` |
| `D56` | `=B56*C56` |
| `F56` | `=E56*D56` |
| `G56` | `=F56/C56` |

### 10. 5. Operação Sistema

- Faixa usada: `A1:H27`
- Fórmulas: **19**
- Conceitos provisórios: operacao_desaguamento
- Células numéricas observadas: **58**

#### Rótulos e textos observados

- Operação do Sistema de Desidratação - Subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador do Sistema de preparo e injeção
- Ajudante Geral
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Equipamento de preparo e injeção polímero
- vb
- Novo ~100k
- Iremos usar a estrutura da SABESP
- Polimero (calculado sobre base seca)
- kg
- Total ton secas (4 kg por ton seca) - SNF - Flonex 4350 SH (floculante catiônico em pó - R$23,40) 2/8/24 - Danilo Curitiba
- Frete Polimero
- un
- (Caminhao Pipa) fornecimento de água para operação
- mes
- Agua da Corsan
- (Gerador) fornecimento de energia para operação + diesel
- Energia Corsan
- Tanques de armazenamento de agua
- Frete Tanque de agua
- Consumo de Diesel (gerador 55 kva)
- litros
- Instalações hidráulicas
- Máquina Wap
- Mão de obra para operação do sistema
- dia
- TOTAL
- Prazo de Execução
- mês
- #NAME?
- Custo Mensal

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A5+A6` |
| `F7` | `=A7*C7` |
| `A8` | `=A5+A6` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `F14` | `=D14*E14` |
| `D15` | `=('4. Forn. Bag'!B35*4)*1.1` |
| `E15` | `=23.4*1.1` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `D24` | `=F26*30` |
| `E24` | `=F9` |
| `F25` | `=SUM(F14:F24)` |
| `F26` | `=ROUNDUP(Produção!D24,0)` |
| `F27` | `=F25/F26` |

### 11. 7. Dragagem

- Faixa usada: `A1:L253`
- Fórmulas: **78**
- Conceitos provisórios: dragagem_operacao
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 5.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=F10*0.1` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `A23` | `=L24` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `L24` | `=(L20*1.7)+(L21*2)+L23` |
| `A25` | `=L24` |
| `A26` | `=L24` |
| `A27` | `=L24` |
| `E27` | `=D27*B27*A27` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `E69` | `=D69*B69` |
| `E71` | `=SUM(E67:E69)` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E139` | `=(0.6/100)*F7` |
| `E140` | `=(1/100)*F7` |
| `E144` | `=E139+E140+E141+E142` |
| `H146` | `=E144` |
| `E150` | `=K167` |
| `K151` | `=I151*J151` |
| `J152` | `=K151/I152` |
| `J153` | `=K151*(1/100)` |
| `J154` | `=SUM(J152:J153)` |
| `K156` | `=I156*J156` |
| `J157` | `=K156/I157` |
| `E158` | `=Canteiro!F32` |
| `J158` | `=K156*(1/100)` |
| `J159` | `=SUM(J157:J158)` |
| `D161` | `=E150+E151+E152+E155+E156+E157+E158+E159+E153+E154` |
| `I161` | `=(I151/12)+2` |
| `K161` | `=I161*J161` |
| `J162` | `=K161/I162` |
| `J163` | `=K161*(1/100)` |
| `J164` | `=SUM(J162:J163)` |
| `H167` | `=J154` |
| `I167` | `=J159` |
| `J167` | `=J164` |
| `K167` | `=SUM(H167:J167)` |
| `E178` | `=E173+E174+E175+E176+E177` |
| `G181` | `=E178+D161+H146+G87+E15` |
| `E185` | `=G181*(5/100)` |
| `E186` | `=G181*(5/100)` |
| `E189` | `=E185+E186` |
| `E192` | `=F7/60` |
| `E193` | `=F7*0.01` |
| `E194` | `=G181*0.005` |
| `E196` | `=E192+E193+E194` |
| `D215` | `=G181` |
| `D218` | `=E189` |
| `D220` | `=E196` |
| `D222` | `=D215+D218+D220` |
| `D231` | `=D227+D229` |
| `D234` | `=J253*0.6*0.62` |
| `J235` | `=H235*I235` |
| `D244` | `=D222` |
| `D245` | `='5. Operação Sistema'!F27` |
| `D246` | `=SUM(D244:D245)` |
| `D247` | `=ROUNDUP(Produção!D24,0)` |
| `J247` | `=D246` |
| `D248` | `=D246*D247` |
| `J249` | `=J247*J248` |
| `L249` | `=J249/J250` |
| `L251` | `=L249*L250` |
| `J252` | `=J250*J251` |
| `J253` | `=J249/J252` |

### 12. 8. Medição

- Faixa usada: `A1:F23`
- Fórmulas: **18**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **38**

#### Rótulos e textos observados

- 8 - Medição
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
- Operador de Draga
- Ajudante Geral
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Amostras
- un
- Batimetria FOS
- dias
- Acompanhamento Coleta BagsFOS
- dia
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `E17` | `=F10` |
| `F17` | `=D17*E17` |
| `F18` | `=SUM(F15:F17)` |
| `F19` | `=F18*(E19/100)` |
| `F20` | `=SUM(F18:F19)` |
| `F22` | `=F21*(E22/100)` |
| `F23` | `=SUM(F21:F22)` |

### 13. 10. Desmob. Draga

- Faixa usada: `A1:F21`
- Fórmulas: **20**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **39**

#### Rótulos e textos observados

- 7 - DESMOBILIZAÇÃO E MONTAGEM DRAGA
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador de Draga + técnico operação polím.
- Ajudante Geral
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Verba para Cobertura do equipamento
- vb
- Carreta para desmobilização do equipamento
- Mão de obra de apoio na desmontagem
- dia
- Guindaste p/ carregamento e desmontagem DRAGA
- Frete para mobilização do equipamento guindaste
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A5+A6` |
| `F7` | `=A7*C7` |
| `A8` | `=A5+A6` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `F14` | `=D14*E14` |
| `E15` | `='1. Mob. Draga'!E19` |
| `F15` | `=D15*E15` |
| `E16` | `=F9` |
| `F16` | `=D16*E16` |
| `E17` | `='1. Mob. Draga'!E20` |
| `F17` | `=D17*E17` |
| `F18` | `=D18*E18` |
| `F19` | `=SUM(F14:F18)` |
| `F20` | `=F19*(E20/100)` |
| `F21` | `=SUM(F19:F20)` |

### 14. 11. Desmob. Eq. Polimero

- Faixa usada: `A1:F26`
- Fórmulas: **16**
- Conceitos provisórios: mobilizacao_sistema, desmobilizacao
- Células numéricas observadas: **47**

#### Rótulos e textos observados

- 2 - DESMOBILIZAÇÃO E MONTAGEM DE EQUIP. POLÍMERO
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador de Draga + técnico operação polím.
- Ajudante Geral
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Verba para Cobertura do equipamento
- vb
- Brita 1 para lastro no piso
- m³
- Concreto para piso
- Carreta para desmobilização do equipamento
- Instalações hidráulicas
- Instalações elétricas
- Máquina Wap
- Barrilete
- Mão de obra de apoio na montagem
- dia
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A5+A6` |
| `F7` | `=A7*C7` |
| `A8` | `=A5+A6` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `F14` | `=D14*E14` |
| `E17` | `='1. Mob. Draga'!E19` |
| `E21` | `=Barrilete!F31` |
| `E22` | `=F9` |
| `F24` | `=SUM(F14:F22)` |
| `F25` | `=F24*(E25/100)` |
| `F26` | `=SUM(F24:F25)` |

### 15. 10. Plan. Preços

- Faixa usada: `A1:O14`
- Fórmulas: **34**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **66**

#### Rótulos e textos observados

- PLANILHA DETALHADA PREÇOS DE CUSTO E VENDA
- Preços com BDI
- Item
- Descrição dos Serviços
- Custo Total
- Quantidade
- Unidade
- Custo Unitário
- BDI (%)
- Preço Unitário
- Preço Total
- Mobilizaçao e Montagem da Draga
- un
- Mobilizaçao e Montagem Equipto Polímero e Barrilete
- Preparo de Célula
- m²
- Fornecimento de Bags
- Dragagem e Operaçao do Sistema de Polimero (incluindo fornecimento do polimero)
- m3
- Medição
- Desmobilização Draga
- Desmobilização do Equipamento Polímero
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Mob. Draga'!F28` |
| `G4` | `=C4/E4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `L4` | `=SUM(J4:J5)+J9` |
| `C5` | `='2. Mob. Eq. Polimero'!F28` |
| `G5` | `=C5/E5` |
| `I5` | `=((H5/100)+1)*G5` |
| `J5` | `=E5*I5` |
| `C6` | `='3. Prep. Célula'!F30` |
| `E6` | `='3. Prep. Célula'!N7` |
| `C7` | `='4. Forn. Bag'!F29` |
| `G7` | `=C7/E7` |
| `I7` | `=((H7/100)+1)*G7` |
| `J7` | `=E7*I7` |
| `C8` | `='7. Dragagem'!D248` |
| `E8` | `='4. Forn. Bag'!B35` |
| `L8` | `=SUM(J6:J7,J8)` |
| `M8` | `=L8/E8` |
| `C9` | `='8. Medição'!F20` |
| `G9` | `=C9/E9` |
| `I9` | `=((H9/100)+1)*G9` |
| `J9` | `=E9*I9` |
| `C10` | `='10. Desmob. Draga'!F21` |
| `G10` | `=C10/E10` |
| `I10` | `=((H10/100)+1)*G10` |
| `J10` | `=E10*I10` |
| `C11` | `='11. Desmob. Eq. Polimero '!F26` |
| `L11` | `=SUM(J11,J10)` |
| `C12` | `=SUM(C4:C11)` |
| `J12` | `=SUM(J4:J11)` |
| `M12` | `=J12/12600` |
| `O13` | `=J12/O12` |
| `J14` | `=J12/E8` |

## Limites desta análise

- A classificação de família e conceitos é provisória e poderá ser refinada pelo crosscheck horizontal.
- Valores calculados, formatação visual, comentários, objetos incorporados e regras implícitas exigem validação adicional quando relevantes.
- Nenhuma fórmula deste arquivo deve ser tratada isoladamente como regra universal da FOS.

## Uso no Método FOS

Este modelo deve ser comparado com os demais para classificar:

- núcleo comum;
- lógica própria da família;
- pacote opcional;
- parâmetro histórico;
- exceção;
- possível inconsistência.
