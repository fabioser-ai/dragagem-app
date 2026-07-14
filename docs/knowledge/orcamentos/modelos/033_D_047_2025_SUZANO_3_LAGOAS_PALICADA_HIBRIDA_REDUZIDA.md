# Modelo 033 — D_047_2025 - Suzano 3 Lagoas- Paliçada Hibrida Reduzida.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `D_047_2025 - Suzano 3 Lagoas- Paliçada Hibrida Reduzida.xlsx`
- Família provisória: **Dragagem com bags/geotêxteis**
- SHA-256 do arquivo: `bd67d176b2b90d01838bcb9266212d17d809ac1491ffb30fc72c286f3bf14170`
- Abas analisadas: **19**
- Fórmulas encontradas: **808**

## Conceitos identificados

- `bags_geotexteis`: 4 aba(s)
- `estrutura_desaguamento`: 4 aba(s)
- `dragagem_operacao`: 2 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `outros`: 2 aba(s)
- `producao_prazo`: 2 aba(s)
- `barrilete_linha`: 1 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `desmobilizacao`: 1 aba(s)
- `formacao_preco`: 1 aba(s)
- `medicao_batimetria`: 1 aba(s)
- `mobilizacao_sistema`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:S27` | 11 | dados_obra |
| 2 | `Produção Paliçada` | `A1:P36` | 34 | producao_prazo, estrutura_desaguamento |
| 3 | `Produção Draga` | `A1:P36` | 35 | producao_prazo |
| 4 | `1. Canteiro` | `A1:L30` | 41 | canteiro |
| 5 | `2.1 Mob. Draga` | `A1:G29` | 31 | mobilizacao_draga |
| 6 | `2.2. Mob. Eq. Polimero` | `A1:G26` | 30 | mobilizacao_sistema |
| 7 | `2.2.1 Barrilete` | `A1:F32` | 36 | barrilete_linha |
| 8 | `3. Paliçada` | `A1:M23` | 37 | estrutura_desaguamento |
| 9 | `3.1 Impermeabilização` | `A1:L24` | 42 | outros |
| 10 | `3.2 Reparo PEAD` | `A1:I17` | 27 | outros |
| 11 | `Preparo CEL BAG` | `A1:O38` | 55 | bags_geotexteis |
| 12 | `BAGS` | `A1:M54` | 56 | bags_geotexteis |
| 13 | `4.1 Dragagem Paliçada` | `A1:L253` | 86 | estrutura_desaguamento, dragagem_operacao |
| 14 | `4.1 Dragagem BAG` | `A1:L253` | 86 | bags_geotexteis, dragagem_operacao |
| 15 | `Op. Polimero Paliçada` | `A1:M36` | 39 | estrutura_desaguamento |
| 16 | `Op. Polimero BAG` | `A1:M36` | 39 | bags_geotexteis |
| 17 | `4.4. Medição` | `A1:K28` | 34 | medicao_batimetria |
| 18 | `6.1 Desmob. Draga + Eq. Pol` | `A1:F29` | 35 | mobilizacao_draga, desmobilizacao |
| 19 | `Plan. Preços` | `A1:L19` | 54 | formacao_preco |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `1. Canteiro` | 44 |
| `[1]3. Canteiro` | 40 |
| `Dados Obra` | 20 |
| `2.1 Mob. Draga` | 17 |
| `Produção Paliçada` | 13 |
| `4.4. Medição` | 8 |
| `3. Paliçada` | 7 |
| `Produção Draga` | 3 |
| `3.1 Impermeabilização` | 2 |
| `3.2 Reparo PEAD` | 2 |
| `Preparo CEL BAG` | 2 |
| `[1]7.1. Bags` | 2 |
| `2.2. Mob. Eq. Polimero` | 1 |
| `2.2.1 Barrilete` | 1 |
| `4.1 Dragagem BAG` | 1 |
| `4.1 Dragagem Paliçada` | 1 |
| `6.1 Desmob. Draga + Eq. Pol` | 1 |
| `Op. Polimero BAG` | 1 |
| `Op. Polimero Paliçada` | 1 |
| `[1]Dados Obra` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:S27`
- Fórmulas: **11**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **37**

#### Rótulos e textos observados

- DRAGAGEM
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- Proposta
- Proposta D_047_2025
- Data
- Cliente
- SUZANO - TRES LAGOAS
- Contato
- e-mail
- Dados da obra
- Objeto
- Dragagem Lagoa 6,7,8 e Polimento
- ESCOPO
- Local
- Tres Lagoas - MS
- Volume de lodo a dragar L6
- m³
- Volume dragagem (m³)
- Volume de lodo a dragar L7
- Tipo de material
- LODO ESGOTO
- Volume de lodo a dragar L8
- Distância de Recalque (m)
- Seio da linha =
- Total
- Volume de lodo a dragar Polimento
- Linha Flutuante (m)
- TOTAL
- Linha de terra (m)
- Profundidade de dragagem (m)
- Espessura média de dragagem (m)
- Área de Dragagem (m² ou L x C)
- X
- Volume (m³) =
- Tipo de Bota Fora
- PALIÇADA
- Sistema de Medição
- preços unitários de serviços
- Canteiro de obras
- FOS
- Mobilização
- % ST in situ
- desconhecido
- Horário de Trabalho (das 7 as 17h)
- h/dia
- % ST desaguado
- Dias de Trabalho (2ª a 6ª)
- dias/mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `R13` | `=N13*P13` |
| `S13` | `=R13/Q13` |
| `B14` | `=N17` |
| `R14` | `=N14*P14` |
| `S14` | `=R14/Q14` |
| `H16` | `=B16+E16` |
| `H17` | `=B17+E17` |
| `N17` | `=SUM(N13:N16)` |
| `R17` | `=SUM(R13:R16)` |
| `S17` | `=SUM(S13:S16)` |
| `G21` | `=B21*D21*B20` |

### 2. Produção Paliçada

- Faixa usada: `A1:P36`
- Fórmulas: **34**
- Conceitos provisórios: producao_prazo, estrutura_desaguamento
- Células numéricas observadas: **71**

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
- PALIÇADA
- GEOXTEEL
- ÁREA DE BACIA
- M²
- Produção mensal (m³/mês)
- Perímetro
- Tamanho Tanque
- Largura de perda p/montagem paliçada
- Quant de Tanques possíveis
- Perda de área com a paliçada
- m²
- Capacidade Volum. Tanque
- m³
- Cálculo do Prazo da obra
- Área interna útil da Paliçada
- Capacidade vol. 2 Tanques
- Altura de enchimento
- m
- Produção mensal
- m³/mês
- Capacidade Volumétrica da Bacia
- Quant. Possível de reuso Tecido
- Volume a Dragar
- Nº de Vezes de preparo Paliçada
- vezes
- Nº de Vezes de reuso
- Quantidade total a dragar
- PRAZO
- temos que comprar tecido 2 vezes
- Mobilização
- Prazo de Execução
- mês
- Paliçada
- 10 dias por vez
- Dragagem
- Destinação
- Carga transp e destinação
- #REF!
- dias
- Largura
- Comprimento
- M2
- PERIMETRO
- Altura Enchimento
- Volume Bacia
- Numero utilizaçao
- Volume Final
- BACIA 1
- BACIA 2
- BACIA 3
- BACIA 4
- TOTAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `H3` | `='Dados Obra '!B26` |
| `H6` | `=H3*H4` |
| `D8` | `=D3*(D4/100)*(D5/100)` |
| `D11` | `=H6` |
| `I12` | `=G36` |
| `D13` | `=D8*D11` |
| `I15` | `=I14*I13` |
| `I16` | `=I12-I15` |
| `O16` | `=O14*O15` |
| `D18` | `=D13` |
| `I18` | `=I16*I17` |
| `I19` | `=SUM('Dados Obra '!S13:S15)` |
| `O19` | `=I19` |
| `I20` | `=I19/I18` |
| `O20` | `=O19/O16` |
| `D21` | `=SUM('Dados Obra '!N13:N15)` |
| `D24` | `=D21/D18` |
| `G25` | `=ROUNDUP(D24,0)` |
| `L26` | `=#REF!` |
| `G27` | `=SUM(G23:G26)` |
| `G32` | `=E32*F32` |
| `H32` | `=(E32*2)+(F32*2)` |
| `J32` | `=G32*I32` |
| `L32` | `=J32*K32` |
| `G33` | `=E33*F33` |
| `H33` | `=(E33*2)+(F33*2)` |
| `J33` | `=G33*I33` |
| `L33` | `=J33*K33` |
| `G34` | `=E34*F34` |
| `H34` | `=(E34*2)+(F34*2)` |
| `G36` | `=SUM(G32:G35)` |
| `H36` | `=SUM(H32:H35)` |
| `J36` | `=SUM(J32:J35)` |
| `L36` | `=SUM(L32:L35)` |

### 3. Produção Draga

- Faixa usada: `A1:P36`
- Fórmulas: **35**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **72**

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
- PALIÇADA
- GEOXTEEL
- ÁREA DE BACIA
- M²
- Produção mensal (m³/mês)
- Perímetro
- Tamanho Tanque
- Largura de perda p/montagem paliçada
- Quant de Tanques possíveis
- Perda de área com a paliçada
- m²
- Capacidade Volum. Tanque
- m³
- Cálculo do Prazo da obra
- Área interna útil da Paliçada
- Capacidade vol. 2 Tanques
- Altura de enchimento
- m
- Produção mensal
- m³/mês
- Capacidade Volumétrica da Bacia
- Quant. Possível de reuso Tecido
- Volume a Dragar
- Nº de Vezes de preparo Paliçada
- vezes
- Nº de Vezes de reuso
- Quantidade total a dragar
- PRAZO
- temos que comprar tecido 2 vezes
- Mobilização
- Prazo de Execução
- mês
- Paliçada
- 10 dias por vez
- Dragagem
- Destinação
- Carga transp e destinação
- #REF!
- dias
- Largura
- Comprimento
- M2
- PERIMETRO
- Altura Enchimento
- Volume Bacia
- Numero utilizaçao
- Volume Final
- BACIA 1
- BACIA 2
- BACIA 3
- BACIA 4
- TOTAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `H3` | `='Dados Obra '!B26` |
| `H6` | `=H3*H4` |
| `D8` | `=D3*(D4/100)*(D5/100)` |
| `D11` | `=H6` |
| `I12` | `=G36` |
| `D13` | `=D8*D11` |
| `I15` | `=I14*I13` |
| `I16` | `=I12-I15` |
| `O16` | `=O14*O15` |
| `D18` | `=D13` |
| `I18` | `=I16*I17` |
| `I19` | `='Dados Obra '!S17` |
| `O19` | `=I19` |
| `I20` | `=I19/I18` |
| `O20` | `=O19/O16` |
| `D21` | `='Dados Obra '!N16` |
| `D24` | `=D21/D18` |
| `G25` | `=ROUNDUP(D24,0)` |
| `D26` | `=ROUNDUP(D24,0)` |
| `L26` | `=#REF!` |
| `G27` | `=SUM(G23:G26)` |
| `G32` | `=E32*F32` |
| `H32` | `=(E32*2)+(F32*2)` |
| `J32` | `=G32*I32` |
| `L32` | `=J32*K32` |
| `G33` | `=E33*F33` |
| `H33` | `=(E33*2)+(F33*2)` |
| `J33` | `=G33*I33` |
| `L33` | `=J33*K33` |
| `G34` | `=E34*F34` |
| `H34` | `=(E34*2)+(F34*2)` |
| `G36` | `=SUM(G32:G35)` |
| `H36` | `=SUM(H32:H35)` |
| `J36` | `=SUM(J32:J35)` |
| `L36` | `=SUM(L32:L35)` |

### 4. 1. Canteiro

- Faixa usada: `A1:L30`
- Fórmulas: **41**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **101**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- R$ / mês
- $/h
- dissídio 5%
- Trasnf 25%
- Encarregado
- Engenheiro
- Operador Draga
- Operador de preparo de polímero
- Ajudante Geral
- Opera bomba sub
- Refeições
- Op. Polímero
- Transporte
- Ajudante
- Custo por dia
- TEC segurança
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Container almoxarifado
- mês
- Cliente
- Container Sanitário/Vestiário
- Container Escritório
- Frete para Containers
- vb
- PPRA + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Vigilância
- água potável
- gl
- material de escritório
- Banheiro Quimico
- mes
- custo Exames médicos
- un
- Mão de obra (integração/viagem)
- dia
- TOTAL
- Prazo de Operação
- preço unitário
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `=L5` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `L4` | `=I4+J4+K4` |
| `B5` | `=G6` |
| `C5` | `=L6` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `K5` | `=(I5+J5)*0.25` |
| `L5` | `=I5+J5+K5` |
| `C6` | `=L8` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `K6` | `=(I6+J6)*0.25` |
| `C7` | `=L9` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=SUM(A4:A7)` |
| `F8` | `=A8*C8` |
| `K8` | `=(I8+J8)*0.25` |
| `L8` | `=I8+J8+K8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `L9` | `=I9+J9+K9` |
| `F10` | `=SUM(F4:F9)` |
| `L10` | `=I10+J10+K10` |
| `D14` | `=ROUNDUP('Produção Paliçada'!G27,0)+'Produção Draga'!D26` |
| `F14` | `=D14*E14` |
| `D15` | `=D14` |
| `D16` | `=D14` |
| `D21` | `=8*D14` |
| `D22` | `=D14` |
| `D23` | `=D14` |
| `D24` | `=A8` |
| `E25` | `=F10` |
| `F26` | `=SUM(F14:F25)` |
| `F27` | `=D14-1` |
| `F28` | `=F26/F27` |
| `F29` | `=F28*(E29/100)` |
| `F30` | `=F28+F29` |

### 5. 2.1 Mob. Draga

- Faixa usada: `A1:G29`
- Fórmulas: **31**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **61**

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
- Operador de preparo de polímero
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
- Treinamentos (Trabalho em Altura e espaço confinado)
- Mobiliário Canteiro
- vb
- mobiliário do alojamento
- Carreta Carga Seca para DRAGA
- un
- Fabiano 29/07/25 - R$ 9800+ 02,%
- Guindaste p/descarregamento e montagem DRAGA
- SUZANO
- Frete
- Mão de obra p/carga e montagem (r$/dia)
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='1. Canteiro'!C4` |
| `E5` | `='1. Canteiro'!E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C5` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='1. Canteiro'!C7` |
| `E8` | `=E7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=A5+A8+A6+A7` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `E20` | `=E19` |
| `F22` | `=D22*E22` |
| `F23` | `=D23*E23` |
| `E24` | `=F11` |
| `F25` | `=SUM(F16:F24)` |
| `F26` | `=F25*(E26/100)` |
| `F27` | `=SUM(F25:F26)` |
| `F29` | `=SUM(F27:F28)` |

### 6. 2.2. Mob. Eq. Polimero

- Faixa usada: `A1:G26`
- Fórmulas: **30**
- Conceitos provisórios: mobilizacao_sistema
- Células numéricas observadas: **70**

#### Rótulos e textos observados

- 2 - MOBILIZAÇÃO E MONTAGEM DE EQUIP. POLÍMERO
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
- Operador de Draga
- Operador de preparo de polímero
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
- Carpintaria
- Munck para montagem cobertura
- Brita 1 para lastro no piso
- m³
- Concreto para piso
- Frete para mobilização do equipamento
- Fabiano 29/07/25 - R$ 9800+ 02,%
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
| `C4` | `='2.1 Mob. Draga'!C5` |
| `E4` | `='1. Canteiro'!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `='1. Canteiro'!C5` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C6` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='1. Canteiro'!C7` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A4+A7+A5+A6` |
| `C8` | `='1. Canteiro'!C8` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `C9` | `='1. Canteiro'!C9` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F4:F9)` |
| `F13` | `=D13*E13` |
| `F15` | `=D15*E15` |
| `E17` | `='2.1 Mob. Draga'!E21` |
| `G17` | `='2.1 Mob. Draga'!G21` |
| `E21` | `='2.2.1 Barrilete'!F32` |
| `E22` | `=F10` |
| `F24` | `=SUM(F13:F22)` |
| `F25` | `=F24*(E25/100)` |
| `F26` | `=SUM(F24:F25)` |

### 7. 2.2.1 Barrilete

- Faixa usada: `A1:F32`
- Fórmulas: **36**
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
| `C5` | `='1. Canteiro'!C4` |
| `D5` | `='Dados Obra '!B26` |
| `E5` | `='1. Canteiro'!E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C6` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='1. Canteiro'!C7` |
| `D7` | `='Dados Obra '!B26` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7` |
| `C8` | `='1. Canteiro'!C8` |
| `F8` | `=A8*C8` |
| `A9` | `=A5+A7` |
| `C9` | `='1. Canteiro'!C9` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `E15` | `=400*1.4` |
| `F15` | `=D15*E15` |
| `E16` | `=165*1.4` |
| `E17` | `=165*1.4` |
| `E18` | `=220*1.4` |
| `E19` | `=55*1.4` |
| `E20` | `=35*1.4` |
| `E21` | `=2000*1.4` |
| `E22` | `=1100*1.4` |
| `E24` | `=14*1.4` |
| `E25` | `=35*1.4` |
| `E26` | `=60*1.4` |
| `E28` | `=F10` |
| `F29` | `=SUM(F15:F28)` |
| `F30` | `=F29*0.3` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=F30+F31` |

### 8. 3. Paliçada

- Faixa usada: `A1:M23`
- Fórmulas: **37**
- Conceitos provisórios: estrutura_desaguamento
- Células numéricas observadas: **66**

#### Rótulos e textos observados

- 3. DIQUE DE PALIÇADA
- EXEMPLO DE PRODUÇÃO EXECUTADO EM CAMPO
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Quant (m²)
- Dias
- horas
- Operador Líder
- Operador de Draga
- W
- Y
- Ajudante Geral
- Refeições
- Y =
- m²/h
- Transporte
- W =
- m²/dia
- Custo por dia
- Custo por m²
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Preços cotados em 08/05/25 no site do Leo Madeiras em Santos (R$ / m)
- QUANTIFICAÇÃO
- Eucalipto 3" (5 x 11 = R$ 12,60)
- m
- Comprimento
- Sarrafo 15 cm
- altura
- Prazo
- Tábua de 30 cm
- m²
- HUESKER - MANTA
- plástico preto
- Nº de Vezes para encher e esvaziar a bacia
- vezes
- prego
- kg
- Nº vezes refazer PALIÇADA COMPLETA
- Mão de obra de montagem
- dia
- Vão de aberturar para entrada caminhão
- TOTAL
- Nº vezes do Vão de entrada
- Quantidade total a ser construído
- Preço Final
- QUANTIFICAÇÃO TOTAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Canteiro'!C4` |
| `D4` | `='Dados Obra '!B26` |
| `E4` | `='1. Canteiro'!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `K4` | `=I4*9` |
| `C5` | `='1. Canteiro'!C5` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C7` |
| `D6` | `='Dados Obra '!B26` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A4+A6+A5` |
| `C7` | `='2.1 Mob. Draga'!C9` |
| `F7` | `=A7*C7` |
| `I7` | `=H4/K4` |
| `A8` | `=A7` |
| `C8` | `='2.1 Mob. Draga'!C10` |
| `F8` | `=A8*C8` |
| `I8` | `=H4/I4` |
| `F9` | `=SUM(F4:F8)` |
| `F10` | `=F9/I8` |
| `F13` | `=D13*E13` |
| `I13` | `='Produção Paliçada'!H36` |
| `I15` | `=I13*I14` |
| `K15` | `=I15/I8` |
| `L17` | `='Produção Paliçada'!I20` |
| `F19` | `=D19*E19` |
| `E20` | `=F10` |
| `F20` | `=D20*E20` |
| `L20` | `=6*1.5` |
| `F21` | `=SUM(F13:F20)` |
| `L21` | `=L17` |
| `F22` | `=L23` |
| `F23` | `=F22*F21` |
| `L23` | `=(I15*L19)+(L20*L21)` |

### 9. 3.1 Impermeabilização

- Faixa usada: `A1:L24`
- Fórmulas: **42**
- Conceitos provisórios: outros
- Células numéricas observadas: **76**

#### Rótulos e textos observados

- 3. DIQUE DE PALIÇADA
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
- Largura
- Comprimento
- Numero de bacias
- Area total
- Regularizaçao terreno
- dia
- PEAD interno
- m²
- BACIA 1
- PEAD Externo / canaleta
- BACIA 2
- Mao de Obra Instalaçao PEAD
- BACIA 3
- Taxa de Mobilizaçao PEAD
- vb
- BACIA 4
- Mão de obra de montagem
- TOTAL
- Preço Final
- Perimetro

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Canteiro'!C4` |
| `D4` | `='Dados Obra '!B26` |
| `E4` | `='1. Canteiro'!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `='1. Canteiro'!C5` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C7` |
| `D6` | `='Dados Obra '!B26` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A4+A6+A5` |
| `C7` | `='2.1 Mob. Draga'!C9` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `C8` | `='2.1 Mob. Draga'!C10` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F4:F8)` |
| `F12` | `=D12*E12` |
| `D13` | `=L17*1.1` |
| `I13` | `=20+0.3+0.3` |
| `J13` | `=150+0.3+0.3` |
| `L13` | `=I13*J13*K13` |
| `D14` | `=K24*1.1` |
| `I14` | `=20+0.3+0.3` |
| `J14` | `=150+0.3+0.3` |
| `L14` | `=I14*J14*K14` |
| `D15` | `=D13+D14` |
| `E17` | `=F9` |
| `F17` | `=D17*E17` |
| `L17` | `=SUM(L13:L16)` |
| `F18` | `=SUM(F12:F17)` |
| `F19` | `=F18` |
| `I20` | `='Produção Paliçada'!H32` |
| `K20` | `=I20*J20` |
| `I21` | `='Produção Paliçada'!H33` |
| `K21` | `=I21*J21` |
| `I22` | `='Produção Paliçada'!H34` |
| `K22` | `=I22*J22` |
| `I23` | `='Produção Paliçada'!H35` |
| `K24` | `=SUM(K20:K23)` |

### 10. 3.2 Reparo PEAD

- Faixa usada: `A1:I17`
- Fórmulas: **27**
- Conceitos provisórios: outros
- Células numéricas observadas: **41**

#### Rótulos e textos observados

- 3. DIQUE DE PALIÇADA
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
- Área
- PEAD
- m²
- LAGOA 6
- Mao de Obra Instalaçao PEAD
- LAGOA 7
- Taxa de Mobilizaçao PEAD
- vb
- LAGOA 8
- Mão de obra de montagem
- dia
- POLIMENTO
- TOTAL
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Canteiro'!C4` |
| `D4` | `='Dados Obra '!B26` |
| `E4` | `='1. Canteiro'!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `='1. Canteiro'!C5` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C7` |
| `D6` | `='Dados Obra '!B26` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A4+A6+A5` |
| `C7` | `='2.1 Mob. Draga'!C9` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `C8` | `='2.1 Mob. Draga'!C10` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F4:F8)` |
| `D12` | `=I16` |
| `F12` | `=D12*E12` |
| `D13` | `=D12` |
| `E15` | `=F9` |
| `F15` | `=D15*E15` |
| `F16` | `=SUM(F12:F15)` |
| `I16` | `=SUM(I12:I15)` |
| `F17` | `=F16` |

### 11. Preparo CEL BAG

- Faixa usada: `A1:O38`
- Fórmulas: **55**
- Conceitos provisórios: bags_geotexteis
- Células numéricas observadas: **126**

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
- Preço Danlo - Curitiba
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
| `C5` | `='[1]3. Canteiro'!C5` |
| `D5` | `='[1]3. Canteiro'!D5` |
| `E5` | `='[1]3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='[1]3. Canteiro'!C6` |
| `D6` | `='[1]3. Canteiro'!D6` |
| `E6` | `=E5` |
| `C7` | `='[1]3. Canteiro'!C7` |
| `D7` | `=D6` |
| `M7` | `=M17` |
| `N7` | `=J7*M7` |
| `C8` | `='[1]3. Canteiro'!C8` |
| `D8` | `=D7` |
| `M8` | `=M7` |
| `N8` | `=J8*M8` |
| `C9` | `='[1]3. Canteiro'!C9` |
| `D9` | `=D8` |
| `M9` | `=M7` |
| `N9` | `=J9*M9` |
| `C10` | `='[1]3. Canteiro'!C10` |
| `D10` | `=D9` |
| `M10` | `=M9` |
| `N10` | `=J10*M10` |
| `D11` | `=D10` |
| `M11` | `=M10` |
| `N11` | `=J11*M11` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='[1]3. Canteiro'!C12` |
| `F12` | `=A12*C12` |
| `N12` | `=N11/8` |
| `A13` | `=A12` |
| `C13` | `='[1]3. Canteiro'!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `K15` | `=I15*J15` |
| `M15` | `=K15*L15` |
| `M16` | `=K16*L16` |
| `M17` | `=SUM(M15:M16)` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `D20` | `=D18` |
| `E22` | `=F14` |
| `D23` | `=N7` |
| `M23` | `=F34/M17` |
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

### 12. BAGS

- Faixa usada: `A1:M54`
- Fórmulas: **56**
- Conceitos provisórios: bags_geotexteis
- Células numéricas observadas: **175**

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
- P18 X 30
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
| `C5` | `='[1]3. Canteiro'!C5` |
| `D5` | `='[1]3. Canteiro'!D5` |
| `E5` | `='[1]3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='[1]3. Canteiro'!C6` |
| `D6` | `='[1]3. Canteiro'!D6` |
| `E6` | `=E5` |
| `C7` | `='[1]3. Canteiro'!C7` |
| `D7` | `=D6` |
| `C8` | `='[1]3. Canteiro'!C8` |
| `D8` | `=D7` |
| `C9` | `='[1]3. Canteiro'!C9` |
| `D9` | `=D8` |
| `C10` | `='[1]3. Canteiro'!C10` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='[1]3. Canteiro'!C12` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `C13` | `='[1]3. Canteiro'!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `E18` | `=M38` |
| `F18` | `=D18*E18` |
| `I18` | `='[1]Dados Obra '!B14` |
| `I20` | `=I18*I19` |
| `D21` | `=E41` |
| `I23` | `='Dados Obra '!S16` |
| `E24` | `=M48` |
| `I24` | `=I23/D41` |
| `E25` | `=M49` |
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

### 13. 4.1 Dragagem Paliçada

- Faixa usada: `A1:L253`
- Fórmulas: **86**
- Conceitos provisórios: estrutura_desaguamento, dragagem_operacao
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 5.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `='Produção Paliçada'!H6` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=(C9*D9*E9*J9)*0.1` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `D21` | `='1. Canteiro'!C4` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `D22` | `='1. Canteiro'!C5` |
| `A23` | `=L24` |
| `D23` | `='1. Canteiro'!C7` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `L24` | `=(L20*1.7)+(L21*2)+L23` |
| `A25` | `=L24` |
| `A26` | `=L24` |
| `A27` | `=L24` |
| `D27` | `=D23` |
| `E27` | `=D27*B27*A27` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `A37` | `='1. Canteiro'!E4` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `B52` | `=B21+B22` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B23+B27` |
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
| `I151` | `='Dados Obra '!B16` |
| `K151` | `=I151*J151` |
| `J152` | `=K151/I152` |
| `J153` | `=K151*(1/100)` |
| `J154` | `=SUM(J152:J153)` |
| `I156` | `=('Dados Obra '!B17/12)*3` |
| `K156` | `=I156*J156` |
| `J157` | `=K156/I157` |
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
| `D225` | `='Produção Paliçada'!D13` |
| `D231` | `=D227+D229` |
| `D234` | `=J253*0.6*0.62` |
| `J235` | `=H235*I235` |
| `D244` | `=D222` |
| `D246` | `=SUM(D244:D245)` |
| `D247` | `=ROUNDUP('Produção Paliçada'!D24,0)` |
| `J247` | `=D246` |
| `D248` | `=D246*D247` |
| `J249` | `=J247*J248` |
| `L249` | `=J249/J250` |
| `L251` | `=L249*L250` |
| `J252` | `=J250*J251` |
| `J253` | `=J249/J252` |

### 14. 4.1 Dragagem BAG

- Faixa usada: `A1:L253`
- Fórmulas: **86**
- Conceitos provisórios: bags_geotexteis, dragagem_operacao
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 5.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `='Produção Paliçada'!H6` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=(C9*D9*E9*J9)*0.1` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `D21` | `='1. Canteiro'!C4` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `D22` | `='1. Canteiro'!C5` |
| `A23` | `=L24` |
| `D23` | `='1. Canteiro'!C7` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `L24` | `=(L20*1.7)+(L21*2)+L23` |
| `A25` | `=L24` |
| `A26` | `=L24` |
| `A27` | `=L24` |
| `D27` | `=D23` |
| `E27` | `=D27*B27*A27` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `A37` | `='1. Canteiro'!E4` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `B52` | `=B21+B22` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B23+B27` |
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
| `I151` | `='Dados Obra '!B16` |
| `K151` | `=I151*J151` |
| `J152` | `=K151/I152` |
| `J153` | `=K151*(1/100)` |
| `J154` | `=SUM(J152:J153)` |
| `I156` | `=('Dados Obra '!B17/12)*3` |
| `K156` | `=I156*J156` |
| `J157` | `=K156/I157` |
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
| `D225` | `='Produção Paliçada'!D13` |
| `D231` | `=D227+D229` |
| `D234` | `=J253*0.6*0.62` |
| `J235` | `=H235*I235` |
| `D244` | `=D222` |
| `D246` | `=SUM(D244:D245)` |
| `D247` | `='Produção Draga'!D26` |
| `J247` | `=D246` |
| `D248` | `=D246*D247` |
| `J249` | `=J247*J248` |
| `L249` | `=J249/J250` |
| `L251` | `=L249*L250` |
| `J252` | `=J250*J251` |
| `J253` | `=J249/J252` |

### 15. Op. Polimero Paliçada

- Faixa usada: `A1:M36`
- Fórmulas: **39**
- Conceitos provisórios: estrutura_desaguamento
- Células numéricas observadas: **83**

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
- JONAS - ZAP AGUINALDO 5/5/25
- Refeições
- UAP de 10 m³ + bombas de 10m³/h
- Transporte
- UAP de 20 m³ + bombas de 20m³/h
- Custo por dia
- Tanques de 5 m³ + bombas de 10m³/h
- Tanques de 10 m³ + bombas de 20m³/h
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Custo Depreciação - Equitº Preparo Polímero
- mês
- Depreciação em
- meses
- Custo manutenção - Equitº Preparo Polímero
- Polimero (calculado sobre base seca)
- kg
- Repassado para Suzano
- Frete Polimero
- un
- (Caminhao Pipa) fornecimento de água para operação
- mes
- (Gerador) fornecimento de energia para operação + diesel
- Fornecimento Suzano (Agua + Eletrica)
- Instalações hidráulicas
- vb
- Instalações Eletrica
- Máquina Wap
- Mão de obra para operação do sistema
- dia
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
| `C5` | `='[1]3. Canteiro'!C5` |
| `D5` | `='[1]3. Canteiro'!D5` |
| `E5` | `='[1]3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='[1]3. Canteiro'!C6` |
| `D6` | `='[1]3. Canteiro'!D6` |
| `E6` | `=E5` |
| `C7` | `='[1]3. Canteiro'!C7` |
| `D7` | `=D6` |
| `C8` | `='[1]3. Canteiro'!C8` |
| `D8` | `=D7` |
| `C9` | `='1. Canteiro'!L8` |
| `D9` | `=D8` |
| `C10` | `='1. Canteiro'!L9` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='[1]3. Canteiro'!C12` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `C13` | `='[1]3. Canteiro'!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `L15` | `=257000*1.3` |
| `D18` | `=ROUNDUP('Produção Paliçada'!D24,0)` |
| `E18` | `=M12/J18` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `E19` | `=E18*0.1` |
| `D20` | `=D36` |
| `E23` | `=4500+2500` |
| `D27` | `=D18*30` |
| `E27` | `=F14` |
| `F28` | `=SUM(F18:F27)` |
| `F30` | `=F28/F29` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=F30+F31` |
| `D34` | `='[1]7.1. Bags'!I20` |
| `D36` | `=D34*D35` |

### 16. Op. Polimero BAG

- Faixa usada: `A1:M36`
- Fórmulas: **39**
- Conceitos provisórios: bags_geotexteis
- Células numéricas observadas: **82**

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
- JONAS - ZAP AGUINALDO 5/5/25
- Refeições
- UAP de 10 m³ + bombas de 10m³/h
- Transporte
- UAP de 20 m³ + bombas de 20m³/h
- Custo por dia
- Tanques de 5 m³ + bombas de 10m³/h
- Tanques de 10 m³ + bombas de 20m³/h
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Custo Depreciação - Equitº Preparo Polímero
- mês
- Depreciação em
- meses
- Custo manutenção - Equitº Preparo Polímero
- Polimero (calculado sobre base seca)
- kg
- Repassado para Suzano
- Frete Polimero
- un
- (Caminhao Pipa) fornecimento de água para operação
- mes
- (Gerador) fornecimento de energia para operação + diesel
- Fornecimento Suzano (Agua + Eletrica)
- Instalações hidráulicas
- vb
- Instalações Eletrica
- Máquina Wap
- Mão de obra para operação do sistema
- dia
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
| `C5` | `='[1]3. Canteiro'!C5` |
| `D5` | `='[1]3. Canteiro'!D5` |
| `E5` | `='[1]3. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='[1]3. Canteiro'!C6` |
| `D6` | `='[1]3. Canteiro'!D6` |
| `E6` | `=E5` |
| `C7` | `='[1]3. Canteiro'!C7` |
| `D7` | `=D6` |
| `C8` | `='[1]3. Canteiro'!C8` |
| `D8` | `=D7` |
| `C9` | `='1. Canteiro'!L8` |
| `D9` | `=D8` |
| `C10` | `='1. Canteiro'!L9` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='[1]3. Canteiro'!C12` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `C13` | `='[1]3. Canteiro'!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `L15` | `=257000*1.3` |
| `D18` | `='Produção Draga'!D26` |
| `E18` | `=M12/J18` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `E19` | `=E18*0.1` |
| `D20` | `=D36` |
| `E23` | `=4500+2500` |
| `D27` | `=D18*30` |
| `E27` | `=F14` |
| `F28` | `=SUM(F18:F27)` |
| `F30` | `=F28/F29` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=F30+F31` |
| `D34` | `='[1]7.1. Bags'!I20` |
| `D36` | `=D34*D35` |

### 17. 4.4. Medição

- Faixa usada: `A1:K28`
- Fórmulas: **34**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **56**

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
- Operador de preparo de polímero
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
- Batimetria L6
- m2
- JASAO GERDAU 2,18
- Batimetria L7
- Batimetria L8
- Batimetria POL
- COLETA BACIA
- un
- dias
- Acompanhamento FOS
- dia
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='3. Paliçada'!C4` |
| `E5` | `='3. Paliçada'!E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='3. Paliçada'!C5` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='3. Paliçada'!C6` |
| `E8` | `=E7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=SUM(A5:A8)` |
| `C9` | `='3. Paliçada'!C7` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `C10` | `='3. Paliçada'!C8` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `E17` | `=E16` |
| `F17` | `=D17*E17` |
| `E18` | `=E16` |
| `E19` | `=E16` |
| `D20` | `=(12*10)+(24*3)` |
| `F20` | `=D20*E20` |
| `E22` | `=F11` |
| `K22` | `=J21/J22` |
| `F23` | `=SUM(F16:F22)` |
| `F24` | `=F23*(E24/100)` |
| `F25` | `=SUM(F23:F24)` |
| `F27` | `=F26*(E27/100)` |
| `F28` | `=SUM(F26:F27)` |

### 18. 6.1 Desmob. Draga + Eq. Pol

- Faixa usada: `A1:F29`
- Fórmulas: **35**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **62**

#### Rótulos e textos observados

- 7 - DESMOBILIZAÇÃO E DESMONTAGEM DRAGA
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
- Operador de Draga
- Operador de preparo de polímero
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
- Guindaste para descarregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Mobiliário Canteiro
- vb
- Carreta Carga Seca para DRAGA
- un
- Carreta Carga Seca para Eq. Pol
- Guindaste p/descarregamento e montagem DRAGA
- Frete
- Trator D4 para lançar draga na água
- Mão de obra p/DEScarga e DESmontagem (r$/dia)
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='2.1 Mob. Draga'!C5` |
| `E5` | `='4.4. Medição'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='2.1 Mob. Draga'!C6` |
| `D6` | `=D5` |
| `E6` | `='4.4. Medição'!E6` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='2.1 Mob. Draga'!C7` |
| `D7` | `=D6` |
| `E7` | `='4.4. Medição'!E7` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='4.4. Medição'!C8` |
| `E8` | `='4.4. Medição'!E8` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=A5+A8+A6+A7` |
| `C9` | `='4.4. Medição'!C9` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `C10` | `='4.4. Medição'!C10` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `D19` | `='2.1 Mob. Draga'!D21` |
| `E19` | `='2.1 Mob. Draga'!E21` |
| `E20` | `=E19` |
| `D21` | `='2.1 Mob. Draga'!D22` |
| `E21` | `='2.1 Mob. Draga'!E22` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `E24` | `=F11` |
| `F25` | `=SUM(F16:F24)` |
| `F26` | `=F25*(E26/100)` |
| `F27` | `=SUM(F25:F26)` |
| `F29` | `=SUM(F27:F28)` |

### 19. Plan. Preços

- Faixa usada: `A1:L19`
- Fórmulas: **54**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **88**

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
- Canteiro de Obras
- vb
- Mobilizaçao Draga
- Mobilizaçao Equipto Polímero e Barrilete
- Paliçada
- m²
- Impermeabilizaçao
- Reparo PEAD - Lagoas
- Dragagem (PALIÇADA+ BAG)
- m3
- OP Polimero (PALIÇADA + BAG)
- Preparo Celula BAGS
- Fornecimento BAGS
- un
- Medição
- m³
- Desmobilização Draga
- Desmobilização do Equipamento Polímero
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D4` | `='1. Canteiro'!F26` |
| `H4` | `=D4/F4` |
| `J4` | `=((I4/100)+1)*H4` |
| `K4` | `=F4*J4` |
| `L4` | `=K4+K5+K6` |
| `D5` | `='2.1 Mob. Draga'!F25` |
| `H5` | `=D5/F5` |
| `J5` | `=((I5/100)+1)*H5` |
| `K5` | `=F5*J5` |
| `D6` | `='2.2. Mob. Eq. Polimero'!F24` |
| `H6` | `=D6/F6` |
| `J6` | `=((I6/100)+1)*H6` |
| `K6` | `=F6*J6` |
| `D7` | `='3. Paliçada'!F23` |
| `F7` | `=F8` |
| `H7` | `=D7/F7` |
| `J7` | `=((I7/100)+1)*H7` |
| `K7` | `=F7*J7` |
| `L7` | `=J7+J8` |
| `D8` | `='3.1 Impermeabilização'!F19` |
| `F8` | `='3.1 Impermeabilização'!L16` |
| `D9` | `='3.2 Reparo PEAD'!F17` |
| `F9` | `='3.2 Reparo PEAD'!I16` |
| `D10` | `='4.1 Dragagem Paliçada'!D248+'4.1 Dragagem BAG'!D248` |
| `F10` | `='Dados Obra '!B14` |
| `H10` | `=D10/F10` |
| `J10` | `=((I10/100)+1)*H10` |
| `K10` | `=F10*J10` |
| `L10` | `=J10+J11+J13+J14` |
| `D11` | `='Op. Polimero Paliçada'!F28+'Op. Polimero BAG'!F28` |
| `F11` | `=F10` |
| `H11` | `=D11/F11` |
| `J11` | `=((I11/100)+1)*H11` |
| `K11` | `=F11*J11` |
| `D12` | `='Preparo CEL BAG'!F34` |
| `F12` | `='Preparo CEL BAG'!M15` |
| `H12` | `=D12/F12` |
| `J12` | `=((I12/100)+1)*H12` |
| `K12` | `=F12*J12` |
| `D13` | `=BAGS!F29` |
| `F13` | `=BAGS!D21` |
| `D14` | `='4.4. Medição'!F25` |
| `F14` | `=F10` |
| `H14` | `=D14/F14` |
| `J14` | `=((I14/100)+1)*H14` |
| `K14` | `=F14*J14` |
| `D15` | `='6.1 Desmob. Draga + Eq. Pol'!F25` |
| `H15` | `=D15/F15` |
| `J15` | `=((I15/100)+1)*H15` |
| `K15` | `=F15*J15` |
| `L15` | `=J15+J16` |
| `D17` | `=SUM(D4:D16)` |
| `K17` | `=SUM(K4:K16)` |
| `K19` | `=K17/F10` |

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
