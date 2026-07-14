# Modelo 003 — Aguas de Joinville- Dragagem ETA PIRAI.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `Aguas de Joinville- Dragagem ETA PIRAI.xlsx`
- Família provisória: **Dragagem com bags/geotêxteis**
- SHA-256 do arquivo: `768c3072c91265f28b3e087ce15f3d60a16eba9849cc6bd0c1e1dd100e4650a7`
- Abas analisadas: **15**
- Fórmulas encontradas: **307**

## Conceitos identificados

- `desmobilizacao`: 2 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `mobilizacao_sistema`: 2 aba(s)
- `bags_geotexteis`: 1 aba(s)
- `barrilete_linha`: 1 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `dragagem_operacao`: 1 aba(s)
- `estrutura_desaguamento`: 1 aba(s)
- `formacao_preco`: 1 aba(s)
- `medicao_batimetria`: 1 aba(s)
- `operacao_desaguamento`: 1 aba(s)
- `outros`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:H27` | 3 | dados_obra |
| 2 | `Produção` | `A1:H24` | 9 | producao_prazo |
| 3 | `1. Mob. Draga` | `A1:G24` | 18 | mobilizacao_draga |
| 4 | `Barrilete` | `A1:F31` | 15 | barrilete_linha |
| 5 | `2. Mob. Eq. Polimero` | `A1:F25` | 15 | mobilizacao_sistema |
| 6 | `3. Prep. Célula` | `A1:P33` | 29 | estrutura_desaguamento |
| 7 | `4. Forn. Bag` | `A1:I36` | 28 | bags_geotexteis |
| 8 | `5. Canteiro de obras` | `A1:G31` | 20 | canteiro |
| 9 | `6. Operação Sistema` | `A1:N24` | 19 | operacao_desaguamento |
| 10 | `7. Dragagem` | `A1:L253` | 83 | dragagem_operacao |
| 11 | `8. Desmob. Draga` | `A1:F24` | 18 | mobilizacao_draga, desmobilizacao |
| 12 | `9. Desmob. Eq. Polimero` | `A1:F23` | 14 | mobilizacao_sistema, desmobilizacao |
| 13 | `Batimetria` | `A1:M20` | 9 | medicao_batimetria |
| 14 | `10. Plan. Preços` | `A1:L16` | 24 | formacao_preco |
| 15 | `11. Arredondamento` | `A1:F8` | 3 | outros |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `Dados Obra` | 25 |
| `3. Prep. Célula` | 3 |
| `4. Forn. Bag` | 3 |
| `1. Mob. Draga` | 1 |
| `2. Mob. Eq. Polimero` | 1 |
| `5. Canteiro de obras` | 1 |
| `6. Operação Sistema` | 1 |
| `7. Dragagem` | 1 |

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
- D_0XX_2025
- Data
- Cliente
- Agua de Joinville
- Contato
- e-mail
- Dados da obra
- Objeto
- Lagoa de Decantaçao
- Local
- Joinville
- Volume dragagem (m³)
- Tipo de material
- Lodo - ETA
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
- preços unitários de serviços
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

### 2. Produção

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

### 3. 1. Mob. Draga

- Faixa usada: `A1:G24`
- Fórmulas: **18**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **51**

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
- Carreta prancha rebaixada
- un
- Carreta extensível
- Carreta Carga Seca para DRAGA
- Fabiano ( 8.800 + 0,2% adv)
- Guindaste p/descarregamento e montagem DRAGA
- Guindaste de 30 toneladas - Munckville 1400 Reais \ Nortec guindastes - 35 toneladas - 2300
- Trator D4 para lançar draga na água
- Mão de obra p/carga e montagem (r$/dia)
- TOTAL
- BDI (%)
- Preço Final

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
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F19` | `=D19*E19` |
| `E21` | `=F10` |
| `F22` | `=SUM(F15:F21)` |
| `F23` | `=F22*(E23/100)` |
| `F24` | `=SUM(F22:F23)` |

### 4. Barrilete

- Faixa usada: `A1:F31`
- Fórmulas: **15**
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
- Tubo de ferro c/6m diametro de 6"
- pç
- Toco 0,50m
- Joelho 90°
- Tee 6" x 4" flangeado
- Ponteira flange x escama diam. 4"
- Cap. 6"
- Válvula Gaveta 6"
- Válvula Gaveta 4"
- Mangueira Conduto d'água
- m
- Braçadeiras
- Curva longa de PVC 4"
- Válvula esfera 2"
- Bomba lameira
- Mão de obra de montagem
- dia
- TOTAL
- 40 % de depreciação
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
| `E27` | `=F9` |
| `F28` | `=SUM(F14:F27)` |
| `F29` | `=F28*0.4` |
| `F30` | `=F29*(E30/100)` |
| `F31` | `=F29+F30` |

### 5. 2. Mob. Eq. Polimero

- Faixa usada: `A1:F25`
- Fórmulas: **15**
- Conceitos provisórios: mobilizacao_sistema
- Células numéricas observadas: **53**

#### Rótulos e textos observados

- 2 - MOBILIZAÇÃO E MONTAGEM DE EQUIP. POLÍMERO
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
- Frete para mobilização do equipamento
- Instalações hidráulicas
- Instalações elétricas
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
| `E20` | `=Barrilete!F31` |
| `E21` | `=F9` |
| `F23` | `=SUM(F14:F21)` |
| `F24` | `=F23*(E24/100)` |
| `F25` | `=SUM(F23:F24)` |

### 6. 3. Prep. Célula

- Faixa usada: `A1:P33`
- Fórmulas: **29**
- Conceitos provisórios: estrutura_desaguamento
- Células numéricas observadas: **91**

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
- Preparo Terreno - Aluguel de Patrol
- dia
- Mobilização da Patrol
- Preparo Terreno - Aluguel de Retro
- Mobilização/desmobilização de Retro
- Regularização manual - Mão de obra
- Danlo 10/06/25 - 15,90 - DIPROTEC
- Mão de obra instal. PEAD
- taxa Mobilizaçao Mao de Obra PEAD
- vb
- Bidim RT 14 (4,90 x 100m)
- Danilo 10/06/25 - 3,39 - DIPROTEC
- Brita 2
- Vogelsanger - Brita 2 - ??? Era 60
- Retro escavadeira para espalhamento Brita
- Mão de obra de instal. Bidim e Brita
- TOTAL
- BDI (%)
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
| `O7` | `=K7*N7` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `O8` | `=K8*N8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `O9` | `=K9*N9` |
| `F10` | `=SUM(F5:F9)` |
| `O10` | `=K10*N10` |
| `O11` | `=O10/10` |
| `F15` | `=D15*E15` |
| `E19` | `=F10` |
| `D21` | `=D20` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `D23` | `=O7` |
| `D24` | `=O8*1.3` |
| `E26` | `=F10` |
| `F27` | `=SUM(F15:F26)` |
| `F28` | `=F27*(E28/100)` |
| `F29` | `=SUM(F27:F28)` |
| `B33` | `=SUM(F24,F25,F26)` |

### 7. 4. Forn. Bag

- Faixa usada: `A1:I36`
- Fórmulas: **28**
- Conceitos provisórios: bags_geotexteis
- Células numéricas observadas: **53**

#### Rótulos e textos observados

- 4. Fornecimento de Bag
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
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
- Bag 8,00 x 30m (un)
- vb
- Frete para os Bags
- un
- Munck para descarregamento
- dia
- Mão de obra para instalação
- TOTAL
- BDI (%)
- Preço Final
- m3
- 1 BAG
- 8 x 52
- 6 x 30
- VOLUME A SER DRAGADO
- 8 x 24
- %
- ST in situ
- ST Desaguado

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
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `E18` | `=F10` |
| `F18` | `=D18*E18` |
| `F19` | `=SUM(F15:F18)` |
| `F20` | `=F19*(E20/100)` |
| `F21` | `=SUM(F19:F20)` |
| `D25` | `=B25*C25` |
| `I27` | `=8*52*2.4*0.85` |
| `I28` | `=6*30*2.2*0.85` |
| `B29` | `='Dados Obra '!B14` |
| `I29` | `=8*24*2.2*0.85` |
| `I30` | `=SUM(I27:I29)` |
| `B34` | `=B29*B30` |
| `B35` | `=B34/B31` |
| `B36` | `=B35/C25` |

### 8. 5. Canteiro de obras

- Faixa usada: `A1:G31`
- Fórmulas: **20**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **75**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
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
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Container almoxarifado
- mês
- #NAME?
- Bunker 6 x 2,45 - 350 reais
- Container Sanitário/Vestiário
- Bunker 6 x 2,45 900 reais
- Container Escritório c/sanitário
- Frete para Containers
- vb
- PPRA + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Placa de obra
- Vigilância
- água potável
- gl
- material de escritório
- Gerador
- Autogeradora + diesel
- custo Exames médicos
- un
- Mão de obra (integração)
- dia
- TOTAL
- Prazo de Operação
- BDI (%)
- Preço Final

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
| `A9` | `=A5+A6+A7` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `D15` | `=ROUNDUP(Produção!D24,0)+1` |
| `F15` | `=D15*E15` |
| `F22` | `=D22*E22` |
| `D23` | `=6*D15` |
| `E25` | `=5500+(9*7*22*7)` |
| `E27` | `=F10` |
| `F28` | `=SUM(F15:F27)` |
| `F30` | `=F28*(E30/100)` |
| `F31` | `=F28/F29` |

### 9. 6. Operação Sistema

- Faixa usada: `A1:N24`
- Fórmulas: **19**
- Conceitos provisórios: operacao_desaguamento
- Células numéricas observadas: **53**

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
- Total Base Seca
- Consumo Polimero
- Polimero (calculado sobre base seca)
- kg
- Frete Polimero
- un
- fornecimento de água para operação
- ENFIL
- fornecimento de energia para operação
- Instalações hidráulicas
- Máquina Wap
- Mão de obra para operação do sistema
- dia
- TOTAL
- Prazo de Execução
- mês
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
| `E14` | `=90000*0.7` |
| `F14` | `=D14*E14` |
| `D15` | `=N15` |
| `F15` | `=D15*E15` |
| `L15` | `='4. Forn. Bag'!B34` |
| `N15` | `=L15*M15` |
| `F16` | `=D16*E16` |
| `E21` | `=F9` |
| `F22` | `=SUM(F14:F21)` |
| `F24` | `=F22/F23` |

### 10. 7. Dragagem

- Faixa usada: `A1:L253`
- Fórmulas: **83**
- Conceitos provisórios: dragagem_operacao
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `=Produção!H6` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=F10*0.1` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `K20` | `='Dados Obra '!B27` |
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
| `I151` | `='Dados Obra '!H16` |
| `K151` | `=I151*J151` |
| `J152` | `=K151/I152` |
| `J153` | `=K151*(1/100)` |
| `J154` | `=SUM(J152:J153)` |
| `I156` | `='Dados Obra '!H17/12*3` |
| `K156` | `=I156*J156` |
| `J157` | `=K156/I157` |
| `E158` | `='5. Canteiro de obras'!F31` |
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
| `E196` | `=E192+E193+E194` |
| `D215` | `=G181` |
| `D218` | `=E189` |
| `D220` | `=E196` |
| `D222` | `=D215+D218+D220` |
| `D225` | `=Produção!D13` |
| `D231` | `=D227+D229` |
| `D234` | `=J253*0.6` |
| `H235` | `=Produção!H4` |
| `I235` | `=Produção!H3` |
| `J235` | `=H235*I235` |
| `D244` | `=D222` |
| `D245` | `='6. Operação Sistema'!F24` |
| `D246` | `=SUM(D244:D245)` |
| `J247` | `=D246` |
| `D248` | `=D246*D247` |
| `J249` | `=J247*J248` |
| `L249` | `=J249/J250` |
| `J250` | `=Produção!H6` |
| `J252` | `=J250*J251` |
| `J253` | `=J249/J252` |

### 11. 8. Desmob. Draga

- Faixa usada: `A1:F24`
- Fórmulas: **18**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **50**

#### Rótulos e textos observados

- 8 - Desmobilização da Draga 6"
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
- Guindaste para carregamento
- dia
- Carreta prancha rebaixada
- un
- Carreta extensível
- Carreta Carga Seca para DRAGA
- Guindaste p/descarregamento e montagem DRAGA
- Trator D4 para lançar draga na água
- Mão de obra p/carga e montagem (r$/dia)
- TOTAL
- BDI (%)
- Preço Final

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
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F19` | `=D19*E19` |
| `E21` | `=F10` |
| `F22` | `=SUM(F15:F21)` |
| `F23` | `=F22*(E23/100)` |
| `F24` | `=SUM(F22:F23)` |

### 12. 9. Desmob. Eq. Polimero

- Faixa usada: `A1:F23`
- Fórmulas: **14**
- Conceitos provisórios: mobilizacao_sistema, desmobilizacao
- Células numéricas observadas: **46**

#### Rótulos e textos observados

- 9. DESMOBILIZAÇÃO DE EQUIP. POLÍMERO - unidade: Global
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
- Piso de concreto armado
- m³
- Desmontagem de tenda p/cobertura
- vb
- Frete para transporte do equipamento
- Instalações hidráulicas
- Instalações elétricas
- Máquina Wap
- Mão de obra de desmontagem
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
| `E20` | `=F9` |
| `F21` | `=SUM(F14:F20)` |
| `F22` | `=F21*(E22/100)` |
| `F23` | `=SUM(F21:F22)` |

### 13. Batimetria

- Faixa usada: `A1:M20`
- Fórmulas: **9**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **24**

#### Rótulos e textos observados

- Projeto + Batimetria + Analises
- Quant.
- preço Unit.
- Valor total
- Análises laboratoriais Solidos Totais
- Analises lab Densidade
- quantidade de meses
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Batimetria
- vb
- Analises
- un
- Projeto
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `M5` | `=K5*L5` |
| `M6` | `=K6*L6` |
| `M7` | `=(M5+M6)/L7` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `F18` | `=SUM(F15:F17)` |
| `F19` | `=F18*(E19/100)` |
| `F20` | `=SUM(F18:F19)` |

### 14. 10. Plan. Preços

- Faixa usada: `A1:L16`
- Fórmulas: **24**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **60**

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
- Mobilizaçao e montagem de Equipamento de Dragagem
- un
- Mobilizaçao e Montagem Equipto Polímero e Barrilete
- Preparo de Célula
- m²
- Fornecimento de Bags 8 x 30m (equivalente a 4 bag de 8x30 - real será 3 bags com dimensoes especificas (aba bags)
- Dragagem e desaguamento
- ton base seca
- Desmobilizaçao Equipamento de Dragagem
- Desmobilização do Equipamento Polímero
- Analise + Batimetria + Projeto
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Mob. Draga '!F24` |
| `G4` | `=C4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `C5` | `='2. Mob. Eq. Polimero'!F25` |
| `G5` | `=C5/E5` |
| `C6` | `='3. Prep. Célula'!F29` |
| `E6` | `='3. Prep. Célula'!N6` |
| `C7` | `='4. Forn. Bag'!F21` |
| `G7` | `=C7/E7` |
| `I7` | `=((H7/100)+1)*G7` |
| `J7` | `=E7*I7` |
| `C8` | `='7. Dragagem'!D248` |
| `E8` | `='4. Forn. Bag'!B34` |
| `L8` | `=(J8+J7)/E8` |
| `C9` | `=C4` |
| `G9` | `=C9/E9` |
| `C10` | `=C5*0.7` |
| `C11` | `=Batimetria!F20` |
| `G11` | `=C11/E11` |
| `I11` | `=((H11/100)+1)*G11` |
| `J11` | `=E11*I11` |
| `C12` | `=SUM(C4:C10)` |
| `J12` | `=SUM(J4:J11)` |

### 15. 11. Arredondamento

- Faixa usada: `A1:F8`
- Fórmulas: **3**
- Conceitos provisórios: outros
- Células numéricas observadas: **25**

#### Rótulos e textos observados

- PLANILHA DE PREÇOS – ETE CANDIDO MOTA
- Mobilização e montagem de Equipamentos de dragagem
- un
- Mobilização e Montagem dos Equipamentos de Preparo e Injeção de Polímero, incluindo barrilete de distribuição
- Preparo de célula para instalação dos Bags, incluindo aplicação de manta impermeabilizante, proteção com geotextil tecido e camada drenante
- m²
- Dragagem e desaguamento (inclui manutenção canteiro , fornecimento de bags , operação sistema bags e operação sistema de prep. E inj. Polimero)
- tonelada 100% seca
- Desmobilização dos Equipamentos de dragagem
- Desmobilização e Desmontagem dos Equipamentos de Preparo e Injeção de Polímero, incluindo barrilete
- Total Global

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F2` | `=E2*D2` |
| `D4` | `='3. Prep. Célula'!N6` |
| `F8` | `=SUM(F2:F7)` |

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
