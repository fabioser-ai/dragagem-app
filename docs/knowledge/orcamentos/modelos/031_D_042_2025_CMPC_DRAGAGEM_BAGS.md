# Modelo 031 — D_042_2025 - CMPC - Dragagem - Bags.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `D_042_2025 - CMPC - Dragagem - Bags.xlsx`
- Família provisória: **Dragagem com bags/geotêxteis**
- SHA-256 do arquivo: `99886fcb3602d33f0efd6f014216219e901caaf1daec035fcc2476a6c4282df6`
- Abas analisadas: **12**
- Fórmulas encontradas: **541**

## Conceitos identificados

- `outros`: 3 aba(s)
- `desmobilizacao`: 2 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `bags_geotexteis`: 1 aba(s)
- `barrilete_linha`: 1 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `estrutura_desaguamento`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:O27` | 13 | dados_obra |
| 2 | `Produção` | `A1:I39` | 13 | producao_prazo |
| 3 | `3. Canteiro` | `A1:N38` | 51 | canteiro |
| 4 | `4. Mob Draga + Pol.` | `A1:N36` | 58 | mobilizacao_draga |
| 5 | `Barrilete` | `A1:F31` | 39 | barrilete_linha |
| 6 | `6. Prep Célula` | `A1:O38` | 55 | estrutura_desaguamento |
| 7 | `7.1. Bags` | `A1:M54` | 58 | bags_geotexteis |
| 8 | `7.2 Draga` | `A1:L207` | 88 | outros |
| 9 | `7.3 Op.Planta` | `A1:M35` | 39 | outros |
| 10 | `9. DesMob Draga + Pol.` | `A1:G36` | 51 | mobilizacao_draga, desmobilizacao |
| 11 | `15. Desmob Final` | `A1:N38` | 37 | desmobilizacao |
| 12 | `Plan. Final` | `A1:L20` | 39 | outros |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `3. Canteiro` | 87 |
| `Dados Obra` | 11 |
| `4. Mob Draga + Pol.` | 4 |
| `15. Desmob Final` | 3 |
| `6. Prep Célula` | 2 |
| `7.1. Bags` | 2 |
| `7.2 Draga` | 1 |
| `7.3 Op.Planta` | 1 |
| `9. DesMob Draga + Pol.` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:O27`
- Fórmulas: **13**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **23**

#### Rótulos e textos observados

- 042_2025
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- Proposta
- Proposta D_023_2025
- Data
- REVISÃO ATUAL
- Cliente
- CMPC IGUAÇU - A1 ENGENHARIA
- Contato
- Marcio Domingues
- e-mail
- Dados da obra
- Objeto
- DRAGAGEM DA LAGOA 01
- Volume
- Linha Flut
- Linha Terra
- Recalque
- Local
- PIRAÍ DO SUL PR
- Lagoa 1 - Lodo
- Volume dragagem (m³)
- 4400 x 2 metros = 8800 + 10% = 9680 (arredondado para 10k)
- Lagoa 1 - Água
- Tipo de material
- Efluente industríal
- Distância de Recalque (m)
- Seio da linha =
- Total
- Linha Flutuante (m)
- Linha de recalque
- Linha de terra (m)
- Linha de retorno do percolado para lagoa 2
- Profundidade de dragagem (m)
- Espessura média de dragagem (m)
- Área de Dragagem (m² ou L x C)
- X
- Volume (m³) =
- Tipo de Bota Fora
- Bags
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
| `O13` | `=M13+N13` |
| `B14` | `=L13` |
| `L15` | `=SUM(L13:L14)` |
| `M15` | `=AVERAGE(M13:M14)` |
| `N15` | `=AVERAGE(N13:N14)` |
| `O15` | `=AVERAGE(O13:O14)` |
| `B16` | `=B17+B18` |
| `H16` | `=B16+E16` |
| `B17` | `=M15` |
| `H17` | `=B17+E17` |
| `B18` | `=N13` |
| `O18` | `=2*300` |
| `G21` | `=B21*D21*B20` |

### 2. Produção

- Faixa usada: `A1:I39`
- Fórmulas: **13**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **23**

#### Rótulos e textos observados

- PRODUÇÃO DRAGAGEM LODO
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
- Mobilizações
- Operação
- PRAZO EXECUÇÃO
- Canteiro
- Mobiliz. Draga
- Preparo Célula
- Dragagem Bags
- Desmob. Draga
- Desmobilização
- TOTAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `I3` | `='Dados Obra '!B26` |
| `I4` | `='Dados Obra '!B27` |
| `I6` | `=I3*I4` |
| `D8` | `=D3*(D4/100)*(D5/100)` |
| `D11` | `=I6` |
| `D13` | `=D8*D11` |
| `D17` | `=D13` |
| `D20` | `='Dados Obra '!B14` |
| `D23` | `=ROUNDUP(D20/D17,0)` |
| `E23` | `=D20/D17` |
| `D27` | `=D23` |
| `H35` | `=D27` |
| `H39` | `=SUM(H32:H38)` |

### 3. 3. Canteiro

- Faixa usada: `A1:N38`
- Fórmulas: **51**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **160**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- % de atuação na obra (%/mês)
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- R$ / mês
- $/h
- dissídio 7,5%
- Transf 25%
- Engenheiro
- Aux Técnico
- Encarregado
- Operador de Draga
- Op. Polímero
- Ajudante
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
- Container Sanitário/Vestiário
- Container Escritório
- Frete para Containers
- vb
- PGR + PCMSO + LTCAT + PR
- ART Principal + ARTS co-resp.
- Placa de obra
- Tenda do Canteiro
- Locup Tendas 8 x 8m com logo e 3 fechamentos laterais
- zap em 28/11/24
- água potável
- gl
- Frete
- chute
- material de escritório
- Banheiro Quimico
- mes
- Viagem da equipe
- un
- custo Exames médicos
- Máscara de Fuga
- MDO (viagem + registro + integração)
- dia
- TOTAL
- Prazo de Operação
- preço unitário
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A5` | `=N13` |
| `C5` | `=M5` |
| `D5` | `='Dados Obra '!B26*'3. Canteiro'!N5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `J5` | `=I5/220` |
| `K5` | `=J5*0.075` |
| `M5` | `=J5+K5+L5` |
| `D6` | `='Dados Obra '!B26` |
| `J6` | `=I6/220` |
| `K6` | `=J6*0.075` |
| `L6` | `=(J6+K6)*0.25` |
| `M6` | `=J6+K6+L6` |
| `D7` | `=D6` |
| `D8` | `=D7` |
| `J8` | `=I8/220` |
| `K8` | `=J8*0.075` |
| `M8` | `=J8+K8+L8` |
| `D9` | `=D8` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `L11` | `=(J11+K11)*0.25` |
| `A12` | `=SUM(A5:A11)` |
| `F12` | `=A12*C12` |
| `L12` | `=(J12+K12)*0.25` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `K13` | `=J13*0.075` |
| `L13` | `=(J13+K13)*0.25` |
| `M13` | `=J13+K13+L13` |
| `F14` | `=SUM(F5:F13)` |
| `D18` | `=Produção!H39` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `D20` | `=D18` |
| `E22` | `=1500+750+2000+750` |
| `F25` | `=D25*E25` |
| `E26` | `=L26+L27` |
| `D27` | `=D18*8` |
| `D28` | `=D18` |
| `D29` | `=D28` |
| `D30` | `=A12` |
| `F30` | `=D30*E30` |
| `D31` | `=A12` |
| `D32` | `=D31` |
| `F32` | `=D32*E32` |
| `E33` | `=F14` |
| `F34` | `=SUM(F18:F33)` |
| `F35` | `='3. Canteiro'!D18` |
| `F36` | `=F34/F35` |
| `F37` | `=F36*(E37/100)` |
| `F38` | `=F36+F37` |

### 4. 4. Mob Draga + Pol.

- Faixa usada: `A1:N36`
- Fórmulas: **58**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **136**

#### Rótulos e textos observados

- 1 - Mobilização DRAGA + PLANTA DE POLÍMERO
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Engenheiro
- Aux Técnico
- Encarregado
- Operador de Draga
- Op. Polímero
- Ajudante
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Máquina de Solda para Tubos PEAD - locação
- vb
- Guindaste para carregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Preços VALE Vitória
- Mobiliário Canteiro
- Mesa escritório
- mobiliário do alojamento
- Carreta Carga Seca - Draga + tubos
- un
- Fabiano R$ 8.800,00 + 0,2%
- Carreta Carga Seca - Eqto Polímero
- Zap de 22/04/25
- Guindaste p/descarregamento e montagem DRAGA
- cadeira
- Instalações hidráulicas
- armário escritório
- Instalações elétricas
- cestos lixo
- Máquina Wap
- Barrilete
- Viagem de ida
- Mão de obra p/carga e montagem (r$/dia)
- armário vestiário
- TOTAL
- Bebedouro
- BDI (%)
- Preço Final
- Carreta (draga)
- Carreta (tubulação)
- Carreta (periféricos)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A5` | `='3. Canteiro'!A5` |
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='3. Canteiro'!A6` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `=E5` |
| `A7` | `='3. Canteiro'!A7` |
| `C7` | `='3. Canteiro'!C7` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `A8` | `='3. Canteiro'!A8` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `=D7` |
| `E8` | `=E7` |
| `A9` | `='3. Canteiro'!A9` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `=D6` |
| `E9` | `=E8` |
| `A10` | `='3. Canteiro'!A10` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `=D6` |
| `E10` | `=E9` |
| `A11` | `=SUM(A5:A10)` |
| `C11` | `='3. Canteiro'!C12` |
| `F11` | `=A11*C11` |
| `A12` | `=A11` |
| `C12` | `='3. Canteiro'!C13` |
| `F12` | `=A12*C12` |
| `F13` | `=SUM(F5:F12)` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `D18` | `=A11` |
| `F18` | `=D18*E18` |
| `E19` | `=N31` |
| `N19` | `=L19*M19` |
| `E20` | `=E19` |
| `N20` | `=L20*M20` |
| `F21` | `=D21*E21` |
| `N21` | `=L21*M21` |
| `E22` | `=E21` |
| `F22` | `=D22*E22` |
| `F23` | `=D23*E23` |
| `N23` | `=L23*M23` |
| `F24` | `=D24*E24` |
| `F25` | `=D25*E25` |
| `F26` | `=D26*E26` |
| `E27` | `=Barrilete!F29` |
| `F27` | `=D27*E27` |
| `E28` | `=F13` |
| `F28` | `=D28*E28` |
| `E29` | `=F13` |
| `F30` | `=SUM(F16:F29)` |
| `F31` | `=F30*(E31/100)` |
| `N31` | `=SUM(N19:N30)` |
| `F32` | `=SUM(F30:F31)` |

### 5. Barrilete

- Faixa usada: `A1:F31`
- Fórmulas: **39**
- Conceitos provisórios: barrilete_linha
- Células numéricas observadas: **82**

#### Rótulos e textos observados

- Composição - BARRILETE - unidade: Global
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
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
- 30 % de depreciação
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `='4. Mob Draga + Pol.'!A7` |
| `C4` | `='3. Canteiro'!C7` |
| `D4` | `='3. Canteiro'!D6` |
| `E4` | `='3. Canteiro'!E5` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `A5` | `='4. Mob Draga + Pol.'!A9` |
| `C5` | `='3. Canteiro'!C9` |
| `D5` | `='3. Canteiro'!D6` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='4. Mob Draga + Pol.'!A10` |
| `C6` | `='3. Canteiro'!C10` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A4+A6` |
| `C7` | `='3. Canteiro'!C12` |
| `F7` | `=A7*C7` |
| `A8` | `=A4+A6` |
| `C8` | `='3. Canteiro'!C13` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F4:F8)` |
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
| `F29` | `=F28*0.3` |
| `F30` | `=F29*(E30/100)` |
| `F31` | `=F29+F30` |

### 6. 6. Prep Célula

- Faixa usada: `A1:O38`
- Fórmulas: **55**
- Conceitos provisórios: estrutura_desaguamento
- Células numéricas observadas: **129**

#### Rótulos e textos observados

- PREPARO DE CÉLULA
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Engenheiro
- Área da
- Quant.
- Aux Técnico
- Composição Real
- Célua
- total
- Encarregado
- Manta PEAD
- m²/m² de Célula
- m²
- Operador de Draga
- Bidim
- Op. Polímero
- Brita
- m³/m² de Célula
- m³
- Ajudante
- Retro escavadeira
- h/m² de Célula
- h
- Mão de Obra
- Refeições
- (4 oficiais + 6 ajudantes)
- dias
- Transporte
- Custo por dia
- CÉLULAS
- largura
- Compr.
- Área M²
- Nº Vezes
- Célula 1
- Célula 2
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Preparo Terreno - Patrola / tratos de esteira
- dia
- Mobilização da Patrol
- Preparo Terreno - Aluguel de Retro
- Mobilização/desmobilização de Retro
- Regularização manual - Mão de obra
- PEAD
- chute pra cima
- Mão de obra instal. PEAD
- taxa Mobilizaçao PEAD Mao de obras
- vb
- Bidim RT 07 (4,90 x 100m)
- Brita 2
- Retro escavadeira para espalhamento Brita
- Mão de obra de instal. Bidim e Brita
- mes
- TOTAL
- Prazo de Operação
- preço unitário
- #DIV/0!
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `=E5` |
| `C7` | `='3. Canteiro'!C7` |
| `D7` | `=D6` |
| `M7` | `=M17` |
| `N7` | `=J7*M7` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `=D7` |
| `M8` | `=M7` |
| `N8` | `=J8*M8` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `=D8` |
| `M9` | `=M7` |
| `N9` | `=J9*M9` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `=D9` |
| `M10` | `=M9` |
| `N10` | `=J10*M10` |
| `D11` | `=D10` |
| `M11` | `=M10` |
| `N11` | `=J11*M11` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='3. Canteiro'!C12` |
| `F12` | `=A12*C12` |
| `N12` | `=N11/8` |
| `A13` | `=A12` |
| `C13` | `='3. Canteiro'!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `K15` | `=I15*J15` |
| `M15` | `=K15*L15` |
| `K16` | `=I16*J16` |
| `M16` | `=K16*L16` |
| `M17` | `=SUM(M15:M16)` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `D20` | `=D18` |
| `E22` | `=F14` |
| `D23` | `=N7` |
| `D24` | `=D23` |
| `D26` | `=N8` |
| `D27` | `=N9*1.1` |
| `D32` | `=ROUNDUP(N10/8,0)` |
| `E32` | `=E20` |
| `D33` | `=D32` |
| `E33` | `=F14` |
| `F34` | `=SUM(F18:F33)` |
| `F36` | `=F34/F35` |
| `F37` | `=F36*(E37/100)` |
| `F38` | `=F36+F37` |

### 7. 7.1. Bags

- Faixa usada: `A1:M54`
- Fórmulas: **58**
- Conceitos provisórios: bags_geotexteis
- Células numéricas observadas: **190**

#### Rótulos e textos observados

- FORNECIMENTO E OPERAÇÃO DE BAGS
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Engenheiro
- Aux Técnico
- Encarregado
- Operador de Draga
- Op. Polímero
- Ajudante
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- P13 X 20
- un
- VOLUME A DRAGAR
- m³
- P13 X 25
- % ST in situ
- P18 X 20
- Volume SECO
- m³ seco
- P18 X 25
- P20 X 20
- % ST desaguado
- média obtida na obra 25%
- P20 X 25
- VOLUME DESAGUADO
- P18 X 40
- P18 X 45
- MÃO DE OBRA DE ESPALHAMENTO
- dia
- TOTAL
- Prazo de Operação
- preço unitário
- BDI (%)
- Preço Final
- CÉLULA - 1
- Preços praticados em 2025 nas obras Chapecó e Curitiba R$ 55,00/m²
- Área Seção a 2,30m
- Comprimento
- Volume
- Quant Bags
- Volume total
- Perímetro
- Compr.
- R$ / m²
- Data
- R$ do Bag
- 2º nível
- 1º Nível
- CAPACIDADE DA CÉLULA - 1
- CÉLULA - 2
- v
- CAPACIDADE DA CÉLULA - 2

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `=E5` |
| `C7` | `='3. Canteiro'!C7` |
| `D7` | `=D6` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `=D7` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `=D8` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='3. Canteiro'!C12` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `C13` | `='3. Canteiro'!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `D18` | `=E38` |
| `E18` | `=M38` |
| `F18` | `=D18*E18` |
| `I18` | `='Dados Obra '!B14` |
| `I20` | `=I18*I19` |
| `I23` | `=I20/I22` |
| `D24` | `=E48` |
| `E24` | `=M48` |
| `D25` | `=E49` |
| `E25` | `=M49` |
| `D26` | `=E50` |
| `E26` | `=M50` |
| `E28` | `=F14` |
| `F29` | `=SUM(F18:F28)` |
| `F31` | `=F29/F30` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |
| `D38` | `=B38*C38` |
| `F38` | `=D38*E38` |
| `M38` | `=(I38*J38)*K38` |
| `K40` | `=K39` |
| `K41` | `=K40` |
| `K42` | `=K41` |
| `K43` | `=K42` |
| `F44` | `=SUM(F38:F43)` |
| `D47` | `=B47*C47` |
| `F47` | `=D47*E47` |
| `M48` | `=(I48*J48)*K48` |
| `K49` | `=K48` |
| `M49` | `=(I49*J49)*K49` |
| `K50` | `=K49` |
| `M50` | `=(I50*J50)*K50` |
| `F53` | `=SUM(F47:F52)` |
| `F54` | `=F44+F53` |
| `G54` | `=G53` |

### 8. 7.2 Draga

- Faixa usada: `A1:L207`
- Fórmulas: **88**
- Conceitos provisórios: outros
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 5.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=(C9*D9*E9*I9)*0.1` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24*0.5` |
| `D20` | `='3. Canteiro'!C5` |
| `E20` | `=D20*B20*A20` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `D21` | `='3. Canteiro'!C6` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `B22` | `='3. Canteiro'!A7` |
| `D22` | `='3. Canteiro'!C7` |
| `A23` | `=L24` |
| `B23` | `='3. Canteiro'!A8` |
| `D23` | `='3. Canteiro'!C8` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `D24` | `='3. Canteiro'!C9` |
| `L24` | `=(L20*1.7)+(L21*2)+L23` |
| `A25` | `=L24` |
| `D25` | `='3. Canteiro'!C10` |
| `A26` | `=L24` |
| `A27` | `=L24` |
| `E27` | `=D27*B27*A27` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `A37` | `='3. Canteiro'!E5` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `B52` | `=B20+B21+B22+B23` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B25` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `E69` | `=D69*B69` |
| `E71` | `=SUM(E67:E69)` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E93` | `=(0.6/100)*F7` |
| `E94` | `=(1/100)*F7` |
| `E98` | `=E93+E94+E95+E96` |
| `H100` | `=E98` |
| `E104` | `=K121` |
| `I105` | `='Dados Obra '!B16` |
| `K105` | `=I105*J105` |
| `J106` | `=K105/I106` |
| `J107` | `=K105*(1/100)` |
| `J108` | `=SUM(J106:J107)` |
| `I110` | `=('Dados Obra '!B17/12)*3` |
| `K110` | `=I110*J110` |
| `J111` | `=K110/I111` |
| `J112` | `=K110*(1/100)` |
| `J113` | `=SUM(J111:J112)` |
| `D115` | `=E104+E105+E106+E109+E110+E111+E112+E113+E107+E108` |
| `I115` | `=(I105/12)+2` |
| `K115` | `=I115*J115` |
| `J116` | `=K115/I116` |
| `J117` | `=K115*(1/100)` |
| `J118` | `=SUM(J116:J117)` |
| `H121` | `=J108` |
| `I121` | `=J113` |
| `J121` | `=J118` |
| `K121` | `=SUM(H121:J121)` |
| `E132` | `=E127+E128+E129+E130+E131` |
| `G135` | `=E132+D115+H100+G87+E15` |
| `E139` | `=G135*(5/100)` |
| `E140` | `=G135*(5/100)` |
| `E143` | `=E139+E140` |
| `E146` | `=F7/60` |
| `E147` | `=F7*0.01` |
| `E150` | `=E146+E147+E148` |
| `D169` | `=G135` |
| `D172` | `=E143` |
| `D174` | `=E150` |
| `D176` | `=D169+D172+D174` |
| `D185` | `=D181+D183` |
| `D188` | `=J207*0.6*0.62` |
| `J189` | `=H189*I189` |
| `D198` | `=D176` |
| `D200` | `=SUM(D198:D199)` |
| `D201` | `=Produção!H35` |
| `J201` | `=D200` |
| `D202` | `=D200*D201` |
| `J203` | `=J201*J202` |
| `L203` | `=J203/J204` |
| `L205` | `=L203*L204` |
| `J206` | `=J204*J205` |
| `J207` | `=J203/J206` |

### 9. 7.3 Op.Planta

- Faixa usada: `A1:M35`
- Fórmulas: **39**
- Conceitos provisórios: outros
- Células numéricas observadas: **77**

#### Rótulos e textos observados

- PREPARO DE CÉLULA
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Engenheiro
- Aux Técnico
- Encarregado
- Operador de Draga
- Op. Polímero
- Ajudante
- Equipamento de Polímero - cotado com Gratt em 07/01/22
- Refeições
- UAP de 10 m³ + bombas de 10m³/h
- Gratt 07/jan/22
- Transporte
- UAP de 20 m³ + bombas de 20m³/h
- Custo por dia
- Tanques de 5 m³ + bombas de 10m³/h
- chute
- Tanques de 10 m³ + bombas de 20m³/h
- Valor orçado com 30% adicional - estimativa 2023
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Custo Depreciação - Equitº Preparo Polímero
- mês
- #NAME?
- Depreciação em
- meses
- Custo manutenção - Equitº Preparo Polímero
- Polimero (calculado sobre base seca)
- kg
- Repassado para CMPC
- Frete Polimero
- un
- (Caminhao Pipa) fornecimento de água para operação
- mes
- (Gerador) fornecimento de energia para operação + diesel
- chute pra cima
- Instalações hidráulicas
- vb
- Máquina Wap
- Mão de obra para operação do sistema
- TOTAL
- Prazo de Operação
- preço unitário
- #DIV/0!
- BDI (%)
- Preço Final
- Quantidade de lodo em tonelada seca
- TS
- Consumo de polímero
- kg/TS

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `=E5` |
| `C7` | `='3. Canteiro'!C7` |
| `D7` | `=D6` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `=D7` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `=D8` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='3. Canteiro'!C12` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `C13` | `='3. Canteiro'!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `L15` | `=257000*1.3` |
| `D18` | `=Produção!H35` |
| `E18` | `=L15/J18` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `E19` | `=E18*0.1` |
| `D20` | `=D35` |
| `E23` | `=4500+2500` |
| `D26` | `=D18*22` |
| `E26` | `=F14` |
| `F27` | `=SUM(F18:F26)` |
| `F29` | `=F27/F28` |
| `F30` | `=F29*(E30/100)` |
| `F31` | `=F29+F30` |
| `D33` | `='7.1. Bags'!I20` |
| `D35` | `=D33*D34` |

### 10. 9. DesMob Draga + Pol.

- Faixa usada: `A1:G36`
- Fórmulas: **51**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **90**

#### Rótulos e textos observados

- 9 - DesMobilização DRAGA + PLANTA DE POLÍMERO
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Engenheiro
- Aux Técnico
- Encarregado
- Operador de Draga
- Op. Polímero
- Ajudante
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Máquina de Solda para Tubos PEAD - locação
- vb
- Guindaste para carregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Mobiliário Canteiro
- mobiliário do alojamento
- Carreta Carga Seca - Draga + tubos
- un
- Fabiano R$ 8.800,00 + 0,2%
- Carreta Carga Seca - Eqto Polímero
- Zap de 11/07/25
- Guindaste p/descarregamento e montagem DRAGA
- Instalações hidráulicas
- Instalações elétricas
- Máquina Wap
- Barrilete
- Viagem de volta
- Mão de obra
- TOTAL
- BDI (%)
- Preço Final
- Carreta (draga)
- Carreta (tubulação)
- Carreta (periféricos)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A5` | `='3. Canteiro'!A5` |
| `C5` | `='3. Canteiro'!C5` |
| `D5` | `='3. Canteiro'!D5` |
| `E5` | `='3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='3. Canteiro'!A6` |
| `C6` | `='3. Canteiro'!C6` |
| `D6` | `='3. Canteiro'!D6` |
| `E6` | `=E5` |
| `A7` | `='3. Canteiro'!A7` |
| `C7` | `='3. Canteiro'!C7` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `A8` | `='3. Canteiro'!A8` |
| `C8` | `='3. Canteiro'!C8` |
| `D8` | `=D7` |
| `E8` | `=E7` |
| `A9` | `='3. Canteiro'!A9` |
| `C9` | `='3. Canteiro'!C9` |
| `D9` | `=D6` |
| `E9` | `=E8` |
| `A10` | `='3. Canteiro'!A10` |
| `C10` | `='3. Canteiro'!C10` |
| `D10` | `=D6` |
| `E10` | `=E9` |
| `A11` | `=SUM(A5:A10)` |
| `C11` | `='3. Canteiro'!C12` |
| `F11` | `=A11*C11` |
| `A12` | `=A11` |
| `C12` | `='3. Canteiro'!C13` |
| `F12` | `=A12*C12` |
| `F13` | `=SUM(F5:F12)` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `F18` | `=D18*E18` |
| `E20` | `=E19` |
| `F21` | `=D21*E21` |
| `E22` | `=E21` |
| `F22` | `=D22*E22` |
| `F23` | `=D23*E23` |
| `F24` | `=D24*E24` |
| `F25` | `=D25*E25` |
| `F26` | `=D26*E26` |
| `E27` | `=Barrilete!F29` |
| `F27` | `=D27*E27` |
| `D28` | `=A11` |
| `F28` | `=D28*E28` |
| `E29` | `=F13` |
| `F30` | `=SUM(F16:F29)` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=SUM(F30:F31)` |

### 11. 15. Desmob Final

- Faixa usada: `A1:N38`
- Fórmulas: **37**
- Conceitos provisórios: desmobilizacao
- Células numéricas observadas: **144**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- % de atuação na obra (%/mês)
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- R$ / mês
- $/h
- dissídio 7,5%
- Transf 25%
- Engenheiro
- Aux Técnico
- Encarregado
- Operador de Draga
- Op. Polímero
- Ajudante
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
- Container Sanitário/Vestiário
- Container Escritório
- Frete para Containers
- vb
- PGR + PCMSO + LTCAT + PR
- ART Principal + ARTS co-resp.
- Viagem da equipe
- un
- custo Exames médicos
- Máscara de Fuga
- MDO (viagem +limpeza final)
- dia
- TOTAL
- Prazo de Operação
- preço unitário
- #DIV/0!
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A5` | `=N13` |
| `C5` | `=M5` |
| `D5` | `='Dados Obra '!B26*'15. Desmob Final'!N5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `J5` | `=I5/220` |
| `K5` | `=J5*0.075` |
| `M5` | `=J5+K5+L5` |
| `D6` | `='Dados Obra '!B26` |
| `K6` | `=J6*0.075` |
| `L6` | `=(J6+K6)*0.25` |
| `M6` | `=J6+K6+L6` |
| `D7` | `=D6` |
| `D8` | `=D7` |
| `D9` | `=D8` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `L11` | `=(J11+K11)*0.25` |
| `A12` | `=SUM(A5:A11)` |
| `F12` | `=A12*C12` |
| `L12` | `=(J12+K12)*0.25` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `K13` | `=J13*0.075` |
| `L13` | `=(J13+K13)*0.25` |
| `M13` | `=J13+K13+L13` |
| `F14` | `=SUM(F5:F13)` |
| `F18` | `=D18*E18` |
| `E22` | `=1500+750+2000+750` |
| `E26` | `=L26+L27` |
| `D30` | `=A12` |
| `D31` | `=A12` |
| `E33` | `=F14` |
| `F34` | `=SUM(F18:F33)` |
| `F35` | `='15. Desmob Final'!D18` |
| `F36` | `=F34/F35` |
| `F37` | `=F36*(E37/100)` |
| `F38` | `=F36+F37` |

### 12. Plan. Final

- Faixa usada: `A1:L20`
- Fórmulas: **39**
- Conceitos provisórios: outros
- Células numéricas observadas: **63**

#### Rótulos e textos observados

- PLANILHA DETALHADA PREÇOS DE CUSTO E VENDA
- Preços com BDI
- Item
- Descrição dos Serviços
- Custo Total
- Quant
- UN
- Custo Unit
- BDI (%)
- Preço Unit
- Preço Total
- UNITÁRIO
- CANTEIRO DE OBRAS
- #NAME?
- mês
- Mobilização Draga
- vb
- Preparo de Célula de desaguamento
- m²
- DRAGAGEM E DESAGUAMENTO
- 7.1
- Fornecimento de Bags
- m³
- 7.2
- Dragagem
- 7.3
- Operação do sistema de polímero
- Desmobilização da Draga e Eqto Pol.
- Desmobilização FINAL
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='3. Canteiro'!F34` |
| `E5` | `=Produção!H39` |
| `G5` | `=C5/E5` |
| `I5` | `=((H5/100)+1)*G5` |
| `J5` | `=E5*I5` |
| `L5` | `=I5` |
| `C6` | `='4. Mob Draga + Pol.'!F30` |
| `L6` | `=I6` |
| `C7` | `='6. Prep Célula'!F34` |
| `E7` | `='6. Prep Célula'!M17` |
| `I7` | `=((H7/100)+1)*G7` |
| `J7` | `=E7*I7` |
| `L7` | `=I7` |
| `C9` | `='7.1. Bags'!F29` |
| `E9` | `='Dados Obra '!L13` |
| `G9` | `=C9/E9` |
| `I9` | `=((H9/100)+1)*G9` |
| `J9` | `=E9*I9` |
| `L9` | `=SUM(I9:I11)` |
| `C10` | `='7.2 Draga'!D202` |
| `E10` | `=E9` |
| `C11` | `='7.3 Op.Planta'!F27` |
| `E11` | `=E10` |
| `G11` | `=C11/E11` |
| `I11` | `=((H11/100)+1)*G11` |
| `J11` | `=E11*I11` |
| `C12` | `='9. DesMob Draga + Pol.'!F30` |
| `G12` | `=C12/E12` |
| `I12` | `=((H12/100)+1)*G12` |
| `L12` | `=I12` |
| `C13` | `='15. Desmob Final'!F34` |
| `G13` | `=C13/E13` |
| `I13` | `=((H13/100)+1)*G13` |
| `J13` | `=E13*I13` |
| `L13` | `=I13` |
| `C15` | `=SUM(C13:C14)` |
| `J15` | `=SUM(J4:J14)` |
| `C17` | `=J15-C15` |
| `C20` | `=J15*0.01` |

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
