# Modelo 007 — Composição - Klabin Ortigueira.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `Composição - Klabin Ortigueira.xlsx`
- Família provisória: **Dragagem com centrífuga**
- SHA-256 do arquivo: `c8554a40b0c25089f08dd3eacd88f91d1258838f472ba020100a32e4ffa173ff`
- Abas analisadas: **21**
- Fórmulas encontradas: **1105**

## Conceitos identificados

- `outros`: 10 aba(s)
- `desmobilizacao`: 3 aba(s)
- `producao_prazo`: 3 aba(s)
- `canteiro`: 2 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `dados_obra`: 1 aba(s)
- `operacao_desaguamento`: 1 aba(s)
- `resumo_comercial`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `RESUMO` | `A1:K64` | 50 | resumo_comercial |
| 2 | `Dados Obra` | `A1:S28` | 15 | dados_obra |
| 3 | `Fornecedores` | `A1:F15` | 1 | outros |
| 4 | `Produção (NOVO CALCULO)` | `A1:S89` | 124 | producao_prazo |
| 5 | `Produção (cliente)` | `A1:Q22` | 14 | producao_prazo |
| 6 | `Produção` | `A1:U65` | 97 | producao_prazo |
| 7 | `1. Canteiro` | `A1:N33` | 50 | canteiro |
| 8 | `2.1 Mob Draga` | `A1:M43` | 57 | mobilizacao_draga |
| 9 | `2.2 Mob Centr` | `A1:M42` | 49 | outros |
| 10 | `3.1 - Aluguel 3 meses Centrif` | `A1:M21` | 44 | outros |
| 11 | `3.3 - Manutenção` | `A1:M21` | 46 | outros |
| 12 | `3.4. BASE DE CONCRETO` | `A1:M23` | 41 | outros |
| 13 | `3.5. Remoção Ensecadeira` | `A1:M23` | 44 | outros |
| 14 | `3.5. Mov. Lodo desag` | `A1:M23` | 44 | outros |
| 15 | `4.1 Draga Dec` | `A1:L206` | 101 | outros |
| 16 | `4.2 Centrífuga` | `A1:R205` | 95 | operacao_desaguamento |
| 17 | `5. Desmob Canteiro` | `A1:N33` | 38 | canteiro, desmobilizacao |
| 18 | `Desmob Draga` | `A1:M43` | 56 | mobilizacao_draga, desmobilizacao |
| 19 | `Desmob Centr` | `A1:M42` | 49 | desmobilizacao |
| 20 | `Plan. Final` | `A1:O34` | 68 | outros |
| 21 | `Final` | `A1:N21` | 22 | outros |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `1. Canteiro` | 162 |
| `Dados Obra` | 20 |
| `Plan. Final` | 6 |
| `4.1 Draga Dec` | 4 |
| `2.1 Mob Draga` | 3 |
| `Produção (NOVO CALCULO)` | 2 |
| `2.2 Mob Centr` | 1 |
| `3.1 - Aluguel 3 meses Centrif` | 1 |
| `3.3 - Manutenção` | 1 |
| `3.4. BASE DE CONCRETO` | 1 |
| `3.5. Mov. Lodo desag` | 1 |
| `3.5. Remoção Ensecadeira` | 1 |
| `4.2 Centrífuga` | 1 |
| `Desmob Centr` | 1 |
| `Desmob Draga` | 1 |

## Análise por aba

### 1. RESUMO

- Faixa usada: `A1:K64`
- Fórmulas: **50**
- Conceitos provisórios: resumo_comercial
- Células numéricas observadas: **287**

#### Rótulos e textos observados

- Quantidade minima
- Custo Minimo
- Custo obra
- 3 Centrifugas
- 2 Centrífugas
- Situação
- Centriguga
- Turno
- Base
- Estrutura Metalica
- Preço Propostos
- Faturamento Minimo
- Resultado Primeiros 15 meses
- Resultado ultimo 43 meses
- FINAL OBRA
- FINAL OBRA MÊS
- com metaalica
- 90% de BDI (Aracruz)
- Fazemos esse peso hoje na Suzano Aracruz - ES - 28/11/2024
- com metalica

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F2` | `=220000` |
| `F9` | `=E9*$C$2` |
| `G9` | `=((F9*0.85)-($F$2+$F$3))*15` |
| `H9` | `=((F9*0.85)-$F$2)*43` |
| `I9` | `=H9+G9` |
| `J9` | `=I9/58` |
| `G10` | `=((F10*0.85)-($F$2+$F$3))*15` |
| `J10` | `=I10/58` |
| `G11` | `=((F11*0.85)-($F$2+$F$3))*15` |
| `G12` | `=((F12*0.85)-($F$2+$F$3))*15` |
| `G13` | `=((F13*0.85)-($F$2+$F$3))*15` |
| `G14` | `=((F14*0.85)-($F$2+$F$4))*15` |
| `G15` | `=((F15*0.85)-($F$2+$F$4))*15` |
| `F24` | `=E24*$C$17` |
| `G24` | `=((F24*0.85)-($F$2+$F$3))*15` |
| `H24` | `=((F24*0.85)-$F$2)*43` |
| `I24` | `=H24+G24` |
| `J24` | `=I24/58` |
| `G25` | `=((F25*0.85)-($F$2+$F$3))*15` |
| `J25` | `=I25/58` |
| `G26` | `=((F26*0.85)-($F$2+$F$3))*15` |
| `G27` | `=((F27*0.85)-($F$2+$F$3))*15` |
| `G28` | `=((F28*0.85)-($F$2+$F$3))*15` |
| `G29` | `=((F29*0.85)-($F$2+$F$4))*15` |
| `G30` | `=((F30*0.85)-($F$2+$F$4))*15` |
| `F40` | `=E40*$C$33` |
| `G40` | `=((F40*0.85)-($F$2+$F$3))*15` |
| `H40` | `=((F40*0.85)-$F$2)*43` |
| `I40` | `=H40+G40` |
| `J40` | `=I40/58` |
| `G41` | `=((F41*0.85)-($F$2+$F$3))*15` |
| `J41` | `=I41/58` |
| `G42` | `=((F42*0.85)-($F$2+$F$3))*15` |
| `G43` | `=((F43*0.85)-($F$2+$F$3))*15` |
| `G44` | `=((F44*0.85)-($F$2+$F$3))*15` |
| `G45` | `=((F45*0.85)-($F$2+$F$4))*15` |
| `G46` | `=((F46*0.85)-($F$2+$F$4))*15` |
| `F58` | `=E58*$C$51` |
| `G58` | `=((F58*0.85)-($F$2+$F$3))*15` |
| `H58` | `=((F58*0.85)-$F$2)*43` |
| `I58` | `=H58+G58` |
| `J58` | `=I58/58` |
| `F59` | `=E59*$C$51` |
| `G59` | `=((F59*0.85)-($F$2+$F$3))*15` |
| `J59` | `=I59/58` |
| `G60` | `=((F60*0.85)-($F$2+$F$3))*15` |
| `G61` | `=((F61*0.85)-($F$2+$F$3))*15` |
| `G62` | `=((F62*0.85)-($F$2+$F$3))*15` |
| `G63` | `=((F63*0.85)-($F$2+$F$4))*15` |
| `G64` | `=((F64*0.85)-($F$2+$F$4))*15` |

### 2. Dados Obra

- Faixa usada: `A1:S28`
- Fórmulas: **15**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **33**

#### Rótulos e textos observados

- KLABIN
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- PARÂMETROS DO ESCOPO
- Preto :
- resultados automáticos
- Proposta
- Proposta D_026_2024
- Data
- Produção Desejada ( MINIMA)
- Ton des/mês
- Ton desaguada total
- % SS in situ
- informado 10% KLABIN
- % SS desaguado
- Cliente
- SUZANO
- Volume Estimado a Dragar
- m³/mês
- Contato
- Jorge / Camila
- e-mail
- Prazo de Operação
- meses
- VOLUME TOTAL ESTIMADO
- m³
- Dados da obra
- Volume Estimado
- Linha Flut
- Linha Terra
- Recalque
- % ST is
- Lodo Seco
- % ST des
- Lodo Des (m³)
- Objeto
- Dragagem e desidratação de lodo
- Lagoa de Emergência
- Local
- ORTIGUEIRA - PR
- Volume dragagem (m³)
- Tipo de material
- Lodo de ETE
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
- CENTRÍFUGA
- Sistema de Medição
- preços unitários de serviços
- Canteiro de obras
- FOS
- Mobilização
- Horário de Trabalho (das 7 as 23h)
- h/dia
- Dias de Trabalho (2ª a sábado feira)
- dias/mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `O5` | `=M5*M9` |
| `M8` | `=(M5*M7)/M6` |
| `M10` | `=M8*M9` |
| `L13` | `=M10` |
| `M13` | `=B18` |
| `N13` | `=B19` |
| `O13` | `=M13+N13` |
| `Q13` | `=L13*P13` |
| `S13` | `=Q13/R13` |
| `Q16` | `=SUM(Q13:Q15)` |
| `S16` | `=SUM(S13:S15)` |
| `H17` | `=B17+E17` |
| `H18` | `=B18+E18` |
| `G22` | `=B22*D22*B21` |
| `N26` | `=L26*M26` |

### 3. Fornecedores

- Faixa usada: `A1:F15`
- Fórmulas: **1**
- Conceitos provisórios: outros
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- ATIVIDADE:
- GUINDASTE - 100 TON
- EMPRESA
- CONTATO
- TELEFONE
- E-MAIL
- PREÇO
- OBSERVAÇAO

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `None` | `` |

### 4. Produção (NOVO CALCULO)

- Faixa usada: `A1:S89`
- Fórmulas: **124**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **217**

#### Rótulos e textos observados

- x2 Centrigufas
- M3/h
- m3/h
- x3 Centrífugas
- 20 metros de skid - centrifuga de 60M3/h
- DIAS
- 1 turno
- 2 turnos
- %ST
- HIGIENIZAÇÃO
- TEMPO UTIL
- TURNOS
- TURNOS 1
- TURNOS 2
- FINAL
- 2X CENTRIFUGAS DE 40 m3/h
- 3X CENTRIFUGAS DE 40 m3/h
- REGIME DE 12 HORAS (1 turno)
- ton base seca / hora
- Ton Hora
- Ton Dia
- Ton Mês
- REGIME DE 16 HORAS (2 turnos)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `E2` | `=C2*2` |
| `E4` | `=C4*3` |
| `F12` | `=E12-D12` |
| `H12` | `=F12-G12` |
| `S12` | `=S10-S11` |
| `F13` | `=E13-D13` |
| `L13` | `=L11*L12` |
| `F14` | `=E14-D14` |
| `H15` | `=(F13+F14)-G12` |
| `I15` | `=L13` |
| `C27` | `=C25*$E$2` |
| `D27` | `=D25*$E$2` |
| `L27` | `=L25*$E$4` |
| `M27` | `=M25*$E$4` |
| `C28` | `=C27/$D$8` |
| `D28` | `=D27/$D$8` |
| `L28` | `=L27/$D$8` |
| `M28` | `=M27/$D$8` |
| `C29` | `=C28*$I$12` |
| `D29` | `=D28*$I$12` |
| `L29` | `=L28*$I$12` |
| `M29` | `=M28*$I$12` |
| `C30` | `=C29*$D$6` |
| `D30` | `=D29*$D$6` |
| `L30` | `=L29*$D$6` |
| `M30` | `=M29*$D$6` |
| `C36` | `=C34*$E$2` |
| `D36` | `=D34*$E$2` |
| `L36` | `=L34*$E$4` |
| `M36` | `=M34*$E$4` |
| `C37` | `=C36/$D$8` |
| `D37` | `=D36/$D$8` |
| `L37` | `=L36/$D$8` |
| `M37` | `=M36/$D$8` |
| `C38` | `=C37*$I$15` |
| `D38` | `=D37*$I$15` |
| `L38` | `=L37*$I$15` |
| `M38` | `=M37*$I$15` |
| `C39` | `=C38*$D$7` |
| `D39` | `=D38*$D$6` |
| `L39` | `=L38*$D$7` |
| `M39` | `=M38*$D$7` |
| `C52` | `=E2*C50` |
| `D52` | `=E2*D50` |
| `E52` | `=E2*E50` |
| `L52` | `=E4*L50` |
| `M52` | `=E4*M50` |
| `N52` | `=E4*N50` |
| `C53` | `=C52/D9` |
| `D53` | `=D52/D9` |
| `E53` | `=E52/D9` |
| `L53` | `=L52/D9` |
| `M53` | `=M52/D9` |
| `N53` | `=N52/D9` |
| `C54` | `=C53*I12` |
| `D54` | `=D53*I12` |
| `E54` | `=E53*I12` |
| `L54` | `=L53*I12` |
| `M54` | `=M53*I12` |
| `N54` | `=N53*I12` |
| `C55` | `=C54*D6` |
| `D55` | `=D54*D6` |
| `E55` | `=E54*D6` |
| `L55` | `=L54*D6` |
| `M55` | `=M54*D6` |
| `N55` | `=N54*D6` |
| `C61` | `=E2*C59` |
| `D61` | `=E2*D59` |
| `E61` | `=E2*E59` |
| `K61` | `=K59*E4` |
| `L61` | `=E4*L50` |
| `M61` | `=E4*M59` |
| `N61` | `=N59*E4` |
| `C62` | `=C61/D9` |
| `D62` | `=D61/D9` |
| `E62` | `=E61/D9` |
| `K62` | `=K61/D9` |
| `L62` | `=L61/D9` |
| `M62` | `=M61/D9` |
| `N62` | `=N61/D9` |
| `C63` | `=C62*I15` |
| `D63` | `=D62*I15` |
| `E63` | `=E62*I15` |
| `K63` | `=K62*I15` |
| `L63` | `=L62*I15` |
| `M63` | `=M62*I15` |
| `N63` | `=N62*I15` |
| `C64` | `=C63*$D$7` |
| `D64` | `=D63*$D$7` |
| `K64` | `=K63*D7` |
| `L64` | `=L63*$D$7` |
| `M64` | `=M63*$D$7` |
| `C77` | `=$E$2*C75` |
| `D77` | `=$E$2*D75` |
| `L77` | `=L75*$E$4` |
| `M77` | `=M75*$E$4` |
| `C78` | `=C77/$D$10` |
| `D78` | `=D77/$D$10` |
| `L78` | `=L77/$D$10` |
| `M78` | `=M77/$D$10` |
| `C79` | `=C78*$I$12` |
| `D79` | `=D78*$I$12` |
| `L79` | `=L78*$I$12` |
| `M79` | `=M78*$I$12` |
| `C80` | `=C79*$D$6` |
| `D80` | `=D79*$D$6` |
| `L80` | `=L79*$D$6` |
| `M80` | `=M79*$D$6` |
| `C86` | `=C84*$E$2` |
| `D86` | `=D84*$E$2` |
| `L86` | `=L84*$E$4` |
| `M86` | `=M84*$E$4` |
| `C87` | `=C86/$D$10` |
| `D87` | `=D86/$D$10` |
| `L87` | `=L86/$D$10` |
| `M87` | `=M86/$D$10` |
| `C88` | `=C87*$I$15` |
| `D88` | `=D87*$I$15` |
| `L88` | `=L87*$I$15` |
| `M88` | `=M87*$I$15` |
| `C89` | `=C88*$D$7` |
| `D89` | `=D88*$D$7` |
| `L89` | `=L88*$D$7` |
| `M89` | `=M88*$D$7` |

### 5. Produção (cliente)

- Faixa usada: `A1:Q22`
- Fórmulas: **14**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **25**

#### Rótulos e textos observados

- PRODUÇÃO CENTRÍFUGA
- Horas Trabalhadas por mês
- Centrífuga Suzano
- m³/h
- Unid.
- Quant.
- Vazão
- Horário de Trabalho (das 7 as 23h)
- Eficiência
- %
- Dias de Trabalho (2ª a sábado feira)
- Concentração
- Produção de Lodo desaguado (informado pela Suzano)
- ton des/mês
- Total de Horas / mês
- % Sólidos do lodo desaguado
- Volume processado
- % SS entrada Centrífuga
- Ton SS / h
- Conferindo Prazo
- Horas trabalhadas
- h/mês
- Volume total
- m³
- Produção mês
- m³/mês
- Produção mensal
- ton SECA/mês
- Prazo
- meses
- Produção Mensal Lodo DESAGUADO
- Ton Des/mês
- PRODUÇÃO MÍNIMA DESEJADA PELA SUZANO
- Lodo Desaguado (ton des/mês)
- % ST in situ
- % ST desaguado
- Jornada de Trabalho diária (h/dia)
- Jornada de trabalho (dias / mês)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F3` | `='Dados Obra '!A27` |
| `H3` | `='Dados Obra '!B27` |
| `M3` | `=SUM(M1:M2)` |
| `F4` | `='Dados Obra '!A28` |
| `H4` | `='Dados Obra '!B28` |
| `H6` | `=H3*H4` |
| `D7` | `=D3*D4*D5` |
| `D10` | `=D3*D8` |
| `D11` | `=H6*D4` |
| `G11` | `='Dados Obra '!B15` |
| `G12` | `=D7*H6` |
| `D13` | `=D10*D11` |
| `G13` | `=G11/G12` |
| `D15` | `=D13/P6` |

### 6. Produção

- Faixa usada: `A1:U65`
- Fórmulas: **97**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **200**

#### Rótulos e textos observados

- PRODUÇÃO CENTRÍFUGA
- Horas Trabalhadas por mês
- Nossa centrífuga
- m³/h
- Unid.
- Quant.
- Alugada
- ou Comprada
- Vazão
- Horário de Trabalho (das 7 as 23h)
- Eficiência
- %
- Dias de Trabalho (2ª a sábado feira)
- Concentração
- Dado da obra de Palotina - 1 centrífuga
- Total de Horas / mês
- Tonelada
- Dias (9h)
- Ton/dia
- Horas/dia
- Ton seca /h
- Volume processado
- Fizemos
- % SS entrada Centrífuga
- Isso com centrifuga trabalhando meia boca c/vazão em média de
- Ton SS / h
- Conferindo Prazo
- Se trabalhássemos com a centrífuga com vazão a
- ton seca/h
- Horas trabalhadas
- h/mês
- Volume total
- m³
- Produção mês
- m³/mês
- Produção mensal
- ton seca/mês
- Prazo
- meses
- NA OBRA SUZANO JACAREÍ - LAGOA A - TIVEMOS ESSE RESULTADO
- Média Produção (m³/dia)
- Dias (21h)
- Total Dragado
- Volume Dragado / hora
- Peso desaguado Produzido
- % Desaguado médio
- Cálculo do Prazo da obra
- Meses
- Mobilização
- ®
- TON SECA
- QUANTIDADE TOTAL
- Ton SS
- Preparo
- Dragagem
- ajuste manual
- Vazão média de Entrada na Centrífuga (m³/h)
- desmob
- PRODUZIMOS - Ton seca / hora
- Ton seca/h
- Prazo Operação
- Total
- PRODUZIMOS - Volume dragado / hora
- % Sólidos Secos que conseguimos fazer entrar na Centrífuga
- PÉSSIMO
- DADOS DA OBRA SUZANO JACAREÍ - LAGOA A (3 MELHORES MESES)
- PRODUÇÃO DESEJADA PELA SUZANO
- Ton desag (m³/dia)
- % Médio Lodo Desag
- Total Lodo SECO / dia
- Horas / dia
- Lodo Seco / hora
- Volume Dragado (mês)
- Dias Trabalhados
- Volume Dragado (dia)
- Volume Dragado (hora)
- Lodo Desaguado e Sólidos Secos (ton SS/mês)
- Mês 1
- % ST in situ
- Mês 2

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F3` | `='Dados Obra '!A27` |
| `H3` | `='Dados Obra '!B27` |
| `M3` | `=SUM(M1:M2)` |
| `F4` | `='Dados Obra '!A28` |
| `H4` | `='Dados Obra '!B28` |
| `H6` | `=H3*H4` |
| `D7` | `=D3*D4*D5` |
| `M7` | `=K7/L7` |
| `O7` | `=M7/N7` |
| `D10` | `=D3*D8` |
| `P10` | `=(O7/P8)*O10` |
| `D11` | `=H6` |
| `G11` | `='Dados Obra '!B15` |
| `P11` | `=(O7/P8)*O11` |
| `G12` | `=D7*H6` |
| `P12` | `=(O7/P8)*O12` |
| `D13` | `=D10*D11` |
| `G13` | `=G11/G12` |
| `D15` | `=D13/0.5` |
| `N16` | `=L16*M16` |
| `O16` | `=M16*21` |
| `P16` | `=N16/O16` |
| `R17` | `=Q16*R16` |
| `D18` | `='Dados Obra '!Q13` |
| `N18` | `=N16*N17` |
| `Q20` | `=R17/O16` |
| `D21` | `=ROUNDUP(D18/D13,0)` |
| `E21` | `=D18/D13` |
| `G21` | `=(SUM(G17:G20))` |
| `Q21` | `=N16/O16` |
| `Q22` | `=Q20/P19` |
| `N26` | `=L26*M26` |
| `P26` | `=N26/O26` |
| `S26` | `=Q26/R26` |
| `T26` | `=S26/O26` |
| `N27` | `=L27*M27` |
| `S27` | `=Q27/R27` |
| `T27` | `=S27/O27` |
| `N28` | `=L28*M28` |
| `P28` | `=N28/O28` |
| `S28` | `=Q28/R28` |
| `T28` | `=S28/O28` |
| `L29` | `=(L26+L28)/2` |
| `N29` | `=L29*M29` |
| `P29` | `=AVERAGE(P26:P28)` |
| `Q29` | `=(Q26+Q28)/2` |
| `T29` | `=(T26+T28)/2` |
| `T32` | `=Q22` |
| `N37` | `=K37*L37*M37` |
| `P37` | `=N37*O37` |
| `R37` | `=P37*Q37` |
| `T37` | `=R37*S37` |
| `K38` | `=K37*2` |
| `L38` | `=L37` |
| `N38` | `=K38*L38*M38` |
| `O38` | `=O37` |
| `P38` | `=N38*O38` |
| `R38` | `=P38*Q38` |
| `T38` | `=R38*S38` |
| `N40` | `=K40*L40*M40` |
| `P40` | `=N40*O40` |
| `R40` | `=P40*Q40` |
| `T40` | `=R40*S40` |
| `K41` | `=K40*2` |
| `L41` | `=L40` |
| `N41` | `=K41*L41*M41` |
| `O41` | `=O40` |
| `P41` | `=N41*O41` |
| `R41` | `=P41*Q41` |
| `T41` | `=R41*S41` |
| `P45` | `=P26` |
| `Q45` | `=P19` |
| `S45` | `=P45/Q45` |
| `I48` | `=Q22` |
| `M48` | `=Q20` |
| `Q48` | `=M48*O48*P48` |
| `S48` | `=Q48*R48` |
| `M49` | `=(I49*M48)/I48` |
| `Q49` | `=M49*O49*P49` |
| `S49` | `=Q49*R49` |
| `M50` | `=(I50*M48)/I48` |
| `Q50` | `=M50*O50*P50` |
| `M51` | `=(I51*M49)/I49` |
| `M52` | `=(I52*M50)/I50` |
| `M53` | `=(I53*M51)/I51` |
| `G60` | `=G58/G59` |
| `L60` | `=L58/L59` |
| `Q60` | `=Q58/Q59` |
| `G63` | `=(G58*G62)/G61` |
| `L63` | `=(L58*L62)/L61` |
| `Q63` | `=(Q58*Q62)/Q61` |
| `G64` | `=G61*G63` |
| `L64` | `=L61*L63` |
| `Q64` | `=Q61*Q63` |
| `G65` | `=G64/G59` |
| `L65` | `=L64/L59` |
| `Q65` | `=Q64/Q59` |

### 7. 1. Canteiro

- Faixa usada: `A1:N33`
- Fórmulas: **50**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **130**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Mão de OBRA
- TURNOS
- Técnico de Segurança
- 1º
- 2º
- 3º
- Salário
- com 25%
- Operador de Draga
- Engº
- Operador de Centrífuga
- Ajudante Geral
- técnico Segurança
- Refeições
- Operador Draga
- Transporte
- Ajudante Draga
- Custo por dia
- Operador Centrífuga
- Ajudante Centrífuga
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
- Material de limpeza
- Preços VALE Vitória
- Mesa escritório
- mesa redonda
- cadeira
- armário escritório
- cestos lixo
- armário vestiário
- material de escritório
- Bebedouro
- Banheiro (reforma / caixa limpeza)
- mes
- Mão de obra (integração)
- dia
- Tendas Paraná zap em 16/01/24
- (h= 3,0m)
- (h= 4,0m)
- TOTAL
- (6 x 6m) c/logotipo
- Prazo de Operação
- (4 x 4m) c/logotipo
- preço unitário
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `=L7` |
| `C4` | `=(N7*N2)+N7` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `A5` | `=L8` |
| `C5` | `=(M8*N2)+M8` |
| `D5` | `=D4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `=L9` |
| `C6` | `=(N9*N2)+N9` |
| `D6` | `=D4` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `L6` | `=I6+J6+K6` |
| `A7` | `=L11` |
| `C7` | `=(N11*N2)+N11` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `L7` | `=I7+J7+K7` |
| `N7` | `=M7*1.25` |
| `A8` | `=SUM(L10,L12)` |
| `C8` | `=(M12*N2)+M12` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `L8` | `=I8+J8+K8` |
| `A9` | `=SUM(A4:A8)` |
| `F9` | `=A9*C9` |
| `N9` | `=M9*1.25` |
| `A10` | `=A9` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F4:F10)` |
| `N11` | `=M11*1.25` |
| `I13` | `=SUM(I6:I12)` |
| `J13` | `=SUM(J7:J12)` |
| `K13` | `=SUM(K7:K12)` |
| `L13` | `=SUM(I13:K13)` |
| `D14` | `=Produção!G21` |
| `F14` | `=D14*E14` |
| `D15` | `=D14` |
| `D16` | `=D14` |
| `D17` | `=D16` |
| `F19` | `=D19*E19` |
| `K19` | `=I19*J19` |
| `D25` | `=D14` |
| `D26` | `=D25` |
| `K26` | `=SUM(K19:K25)` |
| `F27` | `=D27*E27` |
| `E28` | `=F11` |
| `F29` | `=SUM(F14:F28)` |
| `F30` | `=Produção!G19` |
| `F31` | `=F29/F30` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |

### 8. 2.1 Mob Draga

- Faixa usada: `A1:M43`
- Fórmulas: **57**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **137**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 10"
- Mão de OBRA
- TURNOS
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- 1º
- 2º
- 3º
- Operador Líder
- Líder
- Técnico segurança
- Tec segurança
- Operador de Draga
- DRAGA
- Operador de Centrifuga
- Ajudante Geral
- Operador Draga
- Refeições
- Ajudante Draga
- Transporte
- CENTRÍFUGA
- Custo por dia
- Operador Centrífuga
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Guindaste para carregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Hospedagem da equipe (aluguel)
- mês
- Estimativa
- Carreta Carga Seca para DRAGA
- un
- Fabiano zap em 21/08/24 R$ 4.000 + 0,2% adv
- Guindaste p/descarregamento e montagem DRAGA
- KLABIN
- Plano de Rigger
- vb
- Mob do Guindaste
- Munck para descarregamento dos Containeres
- Frete para Containers
- Mobiliário Canteiro
- Mobiliário Alojamento
- Materiais SEGURANÇA (isolamentos e placas)
- PGR + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Tenda do Canteiro
- Locup
- Bebedouro
- custo Exames médicos
- Carreta p/ Equipamentos de complemento centrífuga
- Mão de obra p MOBILIZAÇÃO (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- Carreta 1 (draga)
- Carreta 2 (Tubulação 1500 m)
- Carreta 3 (flutuantes e outros periféricos)
- Carreta 4 (Draga elétrica)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A5` | `=M5` |
| `C5` | `='1. Canteiro'!C4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `='1. Canteiro'!I7` |
| `M5` | `=SUM(I5:L5)` |
| `A6` | `=M6` |
| `C6` | `='1. Canteiro'!C5` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=M9` |
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=M12` |
| `C8` | `='1. Canteiro'!C7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=M10+M13` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `I9` | `='1. Canteiro'!I9` |
| `J9` | `='1. Canteiro'!J9` |
| `K9` | `='1. Canteiro'!K9` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=SUM(A5:A9)` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `I10` | `='1. Canteiro'!I10` |
| `J10` | `='1. Canteiro'!J10` |
| `K10` | `='1. Canteiro'!K10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=A10` |
| `C11` | `='1. Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F5:F11)` |
| `K12` | `='1. Canteiro'!K11` |
| `M12` | `=SUM(I12:L12)` |
| `K13` | `='1. Canteiro'!K12` |
| `M13` | `=SUM(I13:L13)` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `D18` | `=C43` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `F26` | `=D26*E26` |
| `D31` | `=A11` |
| `F31` | `=D31*E31` |
| `F32` | `=D32*E32` |
| `E33` | `=E18` |
| `F33` | `=D33*E33` |
| `E34` | `=F12` |
| `F35` | `=SUM(F15:F34)` |
| `F36` | `=F35*(E36/100)` |
| `F37` | `=SUM(F35:F36)` |
| `C43` | `=SUM(C39:C42)` |

### 9. 2.2 Mob Centr

- Faixa usada: `A1:M42`
- Fórmulas: **49**
- Conceitos provisórios: outros
- Células numéricas observadas: **125**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 10" e DRAGA ELETRICA OU MIUDA
- Mão de OBRA
- TURNOS
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- 1º
- 2º
- 3º
- Operador Líder
- Líder
- Técnico segurança
- Tec segurança
- Operador de Draga
- DRAGA
- Operador de Centrifuga
- Ajudante Geral
- Operador Draga
- Refeições
- Ajudante Draga
- Transporte
- CENTRÍFUGA
- Custo por dia
- Operador Centrífuga
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Guindaste para carregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Hospedagem da equipe (aluguel)
- mês
- Estimativa
- un
- Fabiano zap em 21/08/24 R$ 4.000 + 0,2% adv
- Guindaste p/descarregamento e montagem DRAGA
- FOS
- Plano de Rigger
- vb
- Mob guindaste
- Munck para descarregamento dos Containeres
- Instalações elétrica
- Materiais elétricas
- gl
- custo Exames médicos
- Carreta p/ Equipamentos de complemento centrífuga
- Mão de obra p MOBILIZAÇÃO (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- Carreta 1 (skid 1)
- Carreta 2 (skid 2)
- Carreta 3 (skid 3)
- Carreta 4 e 5 (Tqs Equalização + periféricos)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='1. Canteiro'!C4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `='1. Canteiro'!I7` |
| `M5` | `=SUM(I5:L5)` |
| `C6` | `='1. Canteiro'!C5` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=M9` |
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=M12` |
| `C8` | `='1. Canteiro'!C7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=M10+M13` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `K9` | `='1. Canteiro'!K9` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=SUM(A5:A9)` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `K10` | `='1. Canteiro'!K10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=A10` |
| `C11` | `='1. Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F5:F11)` |
| `K12` | `='1. Canteiro'!K11` |
| `M12` | `=SUM(I12:L12)` |
| `K13` | `='1. Canteiro'!K12` |
| `M13` | `=SUM(I13:L13)` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `E28` | `=J35*10` |
| `D30` | `=A11-A5-A6` |
| `F31` | `=D31*E31` |
| `E32` | `=E18` |
| `F32` | `=D32*E32` |
| `E33` | `=F12` |
| `F34` | `=SUM(F15:F33)` |
| `F35` | `=F34*(E35/100)` |
| `F36` | `=SUM(F34:F35)` |
| `C42` | `=SUM(C38:C41)` |

### 10. 3.1 - Aluguel 3 meses Centrif

- Faixa usada: `A1:M21`
- Fórmulas: **44**
- Conceitos provisórios: outros
- Células numéricas observadas: **67**

#### Rótulos e textos observados

- 4.3 - Manutençao Equipamentos SUZANO
- Mão de OBRA
- NAO SERÁ UTILIZADO POIS UTILIZAREMOS A ESTRUTURA ATUAL SUZANO
- TURNOS
- 1º
- 2º
- 3º
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Líder
- Operador Líder
- Tec segurança
- Técnico
- DRAGA
- Operador de Draga
- Operador Draga
- Ajudante Geral
- Ajudante Draga
- Refeições
- CENTRÍFUGA
- Transporte
- Operador Centrífuga
- Custo por dia
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Jumbo 4
- mês
- Giant 2
- vb
- Juros Compra ( 15% Valor Compra)
- Mao de obra
- dia
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `I5` | `='1. Canteiro'!I7` |
| `M5` | `=SUM(I5:L5)` |
| `C6` | `='1. Canteiro'!C4` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `I6` | `='1. Canteiro'!I8` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='1. Canteiro'!C6` |
| `D8` | `=D7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `I8` | `='1. Canteiro'!I9` |
| `J8` | `='1. Canteiro'!J9` |
| `K8` | `='1. Canteiro'!K9` |
| `M8` | `=SUM(I8:L8)` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `I9` | `='1. Canteiro'!I10` |
| `J9` | `='1. Canteiro'!J10` |
| `K9` | `='1. Canteiro'!K10` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=A6+A9+A7+A8` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `A11` | `=A10` |
| `C11` | `='1. Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `I11` | `='1. Canteiro'!I11` |
| `J11` | `='1. Canteiro'!J11` |
| `K11` | `='1. Canteiro'!K11` |
| `M11` | `=SUM(I11:L11)` |
| `F12` | `=SUM(F6:F11)` |
| `I12` | `='1. Canteiro'!I12` |
| `J12` | `='1. Canteiro'!J12` |
| `K12` | `='1. Canteiro'!K12` |
| `M12` | `=SUM(I12:L12)` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `D18` | `=2*D15` |
| `E18` | `=F12` |
| `F18` | `=D18*E18` |
| `F19` | `=SUM(F15:F18)` |
| `F20` | `=F19*(E20/100)` |
| `F21` | `=SUM(F19:F20)` |

### 11. 3.3 - Manutenção

- Faixa usada: `A1:M21`
- Fórmulas: **46**
- Conceitos provisórios: outros
- Células numéricas observadas: **66**

#### Rótulos e textos observados

- 4.3 - Manutençao Equipamentos SUZANO
- Mão de OBRA
- NAO É DE RESPONSABILIDADE FOS ESTRUTURA SUZANO - SOMENTE NOSSA ESTRUTURA - CUSTOS DE MANUTENÇAO ESTAO DENTRO DE CENTRIFUGA
- TURNOS
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- 1º
- 2º
- 3º
- Operador Líder
- Líder
- Técnico
- Tec segurança
- Operador de Draga
- DRAGA
- Ajudante Geral
- Operador Draga
- Refeições
- Ajudante Draga
- Transporte
- CENTRÍFUGA
- Custo por dia
- Operador Centrífuga
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- VERBA MANUTENÇAO MENSAL GRATT
- mês
- Rodrigo + Jonas
- VERBA REPARO INICIAL
- vb
- INSUMOS (lub,
- Mão de obra p MOBILIZAÇÃO (r$/dia)
- dia
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C6` | `='1. Canteiro'!C4` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `I6` | `='1. Canteiro'!I7` |
| `M6` | `=SUM(I6:L6)` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `I7` | `='1. Canteiro'!I8` |
| `C8` | `='1. Canteiro'!C6` |
| `D8` | `=D7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `I9` | `='1. Canteiro'!I9` |
| `J9` | `='1. Canteiro'!J9` |
| `K9` | `='1. Canteiro'!K9` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=A6+A9+A7+A8` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `I10` | `='1. Canteiro'!I10` |
| `J10` | `='1. Canteiro'!J10` |
| `K10` | `='1. Canteiro'!K10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=A10` |
| `C11` | `='1. Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F6:F11)` |
| `I12` | `='1. Canteiro'!I11` |
| `J12` | `='1. Canteiro'!J11` |
| `K12` | `='1. Canteiro'!K11` |
| `M12` | `=SUM(I12:L12)` |
| `I13` | `='1. Canteiro'!I12` |
| `J13` | `='1. Canteiro'!J12` |
| `K13` | `='1. Canteiro'!K12` |
| `M13` | `=SUM(I13:L13)` |
| `D15` | `='Dados Obra '!M9` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `D17` | `=D15` |
| `F17` | `=D17*E17` |
| `D18` | `=2*D15` |
| `E18` | `=F12` |
| `F18` | `=D18*E18` |
| `F19` | `=SUM(F15:F17)` |
| `F20` | `=F19*(E20/100)` |
| `F21` | `=SUM(F19:F20)` |

### 12. 3.4. BASE DE CONCRETO

- Faixa usada: `A1:M23`
- Fórmulas: **41**
- Conceitos provisórios: outros
- Células numéricas observadas: **56**

#### Rótulos e textos observados

- 4.3 - Manutençao Equipamentos SUZANO
- Mão de OBRA
- NAO SERÁ REALIZADA PELA FOS - REPASSADO PARA SUZANO
- TURNOS
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- 1º
- 2º
- 3º
- Operador Líder
- Líder
- Técnico
- Tec segurança
- Operador de Draga
- DRAGA
- Ajudante Geral
- Operador Draga
- Refeições
- Ajudante Draga
- Transporte
- CENTRÍFUGA
- Custo por dia
- Operador Centrífuga
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- BASE DE CONCRETO - TERCEIRIZADA
- m3
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C6` | `='1. Canteiro'!C4` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `I6` | `='1. Canteiro'!I7` |
| `M6` | `=SUM(I6:L6)` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `I7` | `='1. Canteiro'!I8` |
| `C8` | `='1. Canteiro'!C6` |
| `D8` | `=D7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `I9` | `='1. Canteiro'!I9` |
| `J9` | `='1. Canteiro'!J9` |
| `K9` | `='1. Canteiro'!K9` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=A6+A9+A7+A8` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `I10` | `='1. Canteiro'!I10` |
| `J10` | `='1. Canteiro'!J10` |
| `K10` | `='1. Canteiro'!K10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=A10` |
| `C11` | `='1. Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F6:F11)` |
| `I12` | `='1. Canteiro'!I11` |
| `J12` | `='1. Canteiro'!J11` |
| `K12` | `='1. Canteiro'!K11` |
| `M12` | `=SUM(I12:L12)` |
| `I13` | `='1. Canteiro'!I12` |
| `J13` | `='1. Canteiro'!J12` |
| `K13` | `='1. Canteiro'!K12` |
| `M13` | `=SUM(I13:L13)` |
| `F15` | `=D15*E15` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=SUM(F15:F20)` |
| `F22` | `=F21*(E22/100)` |
| `F23` | `=SUM(F21:F22)` |

### 13. 3.5. Remoção Ensecadeira

- Faixa usada: `A1:M23`
- Fórmulas: **44**
- Conceitos provisórios: outros
- Células numéricas observadas: **60**

#### Rótulos e textos observados

- 4.3 - Manutençao Equipamentos SUZANO
- Mão de OBRA
- REMOÇAO ENSECADEIRA
- TURNOS
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- 1º
- 2º
- 3º
- Operador Líder
- Líder
- Técnico
- Tec segurança
- Operador de Draga
- DRAGA
- Ajudante Geral
- Operador Draga
- Refeições
- Ajudante Draga
- Transporte
- CENTRÍFUGA
- Custo por dia
- Operador Centrífuga
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Escavadeira
- diaria
- Movimentação volume ensecadeira
- viagem
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C6` | `='1. Canteiro'!C4` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `I6` | `='1. Canteiro'!I7` |
| `M6` | `=SUM(I6:L6)` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `I7` | `='1. Canteiro'!I8` |
| `C8` | `='1. Canteiro'!C6` |
| `D8` | `=D7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `I9` | `='1. Canteiro'!I9` |
| `J9` | `='1. Canteiro'!J9` |
| `K9` | `='1. Canteiro'!K9` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=A6+A9+A7+A8` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `I10` | `='1. Canteiro'!I10` |
| `J10` | `='1. Canteiro'!J10` |
| `K10` | `='1. Canteiro'!K10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=A10` |
| `C11` | `='1. Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F6:F11)` |
| `I12` | `='1. Canteiro'!I11` |
| `J12` | `='1. Canteiro'!J11` |
| `K12` | `='1. Canteiro'!K11` |
| `M12` | `=SUM(I12:L12)` |
| `I13` | `='1. Canteiro'!I12` |
| `J13` | `='1. Canteiro'!J12` |
| `K13` | `='1. Canteiro'!K12` |
| `M13` | `=SUM(I13:L13)` |
| `F15` | `=D15*E15` |
| `D16` | `=ROUNDUP((50*4*5)/14,0)` |
| `E16` | `=450*1.5` |
| `F16` | `=D16*E16` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=SUM(F15:F20)` |
| `F22` | `=F21*(E22/100)` |
| `F23` | `=SUM(F21:F22)` |

### 14. 3.5. Mov. Lodo desag

- Faixa usada: `A1:M23`
- Fórmulas: **44**
- Conceitos provisórios: outros
- Células numéricas observadas: **58**

#### Rótulos e textos observados

- 4.3 - Manutençao Equipamentos SUZANO
- Mão de OBRA
- MOVIMENTAÇAO LODO DESAGUADO
- TURNOS
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- 1º
- 2º
- 3º
- Operador Líder
- Líder
- Técnico
- Tec segurança
- Operador de Draga
- DRAGA
- Ajudante Geral
- Operador Draga
- Refeições
- Ajudante Draga
- Transporte
- CENTRÍFUGA
- Custo por dia
- Operador Centrífuga
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- 15.000 x 10% x 0,2
- Viagem
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C6` | `='1. Canteiro'!C4` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `I6` | `='1. Canteiro'!I7` |
| `M6` | `=SUM(I6:L6)` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `I7` | `='1. Canteiro'!I8` |
| `C8` | `='1. Canteiro'!C6` |
| `D8` | `=D7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `I9` | `='1. Canteiro'!I9` |
| `J9` | `='1. Canteiro'!J9` |
| `K9` | `='1. Canteiro'!K9` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=A6+A9+A7+A8` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `I10` | `='1. Canteiro'!I10` |
| `J10` | `='1. Canteiro'!J10` |
| `K10` | `='1. Canteiro'!K10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=A10` |
| `C11` | `='1. Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F6:F11)` |
| `I12` | `='1. Canteiro'!I11` |
| `J12` | `='1. Canteiro'!J11` |
| `K12` | `='1. Canteiro'!K11` |
| `M12` | `=SUM(I12:L12)` |
| `I13` | `='1. Canteiro'!I12` |
| `J13` | `='1. Canteiro'!J12` |
| `K13` | `='1. Canteiro'!K12` |
| `M13` | `=SUM(I13:L13)` |
| `D15` | `=ROUNDUP(((15000*0.1)/0.2)/14,)` |
| `E15` | `=450*1.5` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=SUM(F15:F20)` |
| `F22` | `=F21*(E22/100)` |
| `F23` | `=SUM(F21:F22)` |

### 15. 4.1 Draga Dec

- Faixa usada: `A1:L206`
- Fórmulas: **101**
- Conceitos provisórios: outros
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F7` | `=K7` |
| `K7` | `=SUM(K4:K6)` |
| `C9` | `=Produção!H6` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=(C9*D9*E9*L12)*0.1` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `K20` | `='Dados Obra '!B28` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `B21` | `='2.1 Mob Draga'!M5` |
| `D21` | `='1. Canteiro'!C4` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `B22` | `='1. Canteiro'!L9` |
| `D22` | `='1. Canteiro'!C6` |
| `A23` | `=L24` |
| `B23` | `='1. Canteiro'!L10` |
| `D23` | `='1. Canteiro'!C8` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `B24` | `='2.1 Mob Draga'!A6` |
| `D24` | `='1. Canteiro'!C5` |
| `L24` | `=(L20*1.7)+(L21*2)+L23` |
| `A25` | `=L24` |
| `A26` | `=L24` |
| `A27` | `=L24` |
| `E27` | `=D27*B27*A27` |
| `K28` | `=I28*J28` |
| `K29` | `=J29*I29` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `K31` | `=(K28+K29)*K30` |
| `K33` | `=K32+K31` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `B52` | `=B21+B22` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B23+B24` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `B69` | `=B52` |
| `E69` | `=D69*B69` |
| `E71` | `=SUM(E67:E69)` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E92` | `=(0.6/100)*F7` |
| `E93` | `=(1/100)*F7` |
| `E97` | `=E92+E93+E94+E95` |
| `H99` | `=E97` |
| `E103` | `=K120` |
| `I104` | `='Dados Obra '!H17` |
| `K104` | `=I104*J104` |
| `J105` | `=K104/I105` |
| `J106` | `=K104*(1/100)` |
| `E107` | `=B107*D107` |
| `J107` | `=SUM(J105:J106)` |
| `E109` | `=B109*D109` |
| `I109` | `='Dados Obra '!H18/12*3` |
| `K109` | `=I109*J109` |
| `J110` | `=K109/I110` |
| `E111` | `='1. Canteiro'!F33` |
| `J111` | `=K109*(1/100)` |
| `J112` | `=SUM(J110:J111)` |
| `D114` | `=E103+E104+E105+E108+E109+E110+E111+E112+E106+E107` |
| `I114` | `=(I104/12)+2` |
| `K114` | `=I114*J114` |
| `J115` | `=K114/I115` |
| `J116` | `=K114*(1/100)` |
| `J117` | `=SUM(J115:J116)` |
| `H120` | `=J107` |
| `I120` | `=J112` |
| `J120` | `=J117` |
| `K120` | `=SUM(H120:J120)` |
| `E131` | `=E126+E127+E128+E129+E130` |
| `G134` | `=E131+D114+H99+G87+E15` |
| `E138` | `=G134*(5/100)` |
| `E139` | `=G134*(5/100)` |
| `E142` | `=E138+E139` |
| `E145` | `=F7/60` |
| `E149` | `=E145+E146+E147` |
| `D168` | `=G134` |
| `D171` | `=E142` |
| `D173` | `=E149` |
| `D175` | `=D168+D171+D173` |
| `D178` | `=Produção!D13` |
| `D184` | `=D180+D182` |
| `D187` | `=J206*0.6*0.62` |
| `H188` | `=Produção!H4` |
| `I188` | `=Produção!H3` |
| `J188` | `=H188*I188` |
| `D197` | `=D175` |
| `D199` | `=SUM(D197:D198)` |
| `D200` | `=Produção!G19` |
| `J200` | `=D199` |
| `D201` | `=D199*D200` |
| `J202` | `=J200*J201` |
| `J203` | `=Produção!H6` |
| `D205` | `=D201/D203` |
| `D206` | `=D205*4000` |
| `J206` | `=(J202/J203)*J204` |

### 16. 4.2 Centrífuga

- Faixa usada: `A1:R205`
- Fórmulas: **95**
- Conceitos provisórios: operacao_desaguamento
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F7` | `=R7` |
| `R7` | `=Q7*P7` |
| `C9` | `='4.1 Draga Dec'!C9` |
| `K9` | `=SUM(K3:K8)` |
| `F10` | `=(F9*E9*D9*C9)` |
| `K14` | `=K12-K13` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `K20` | `='Dados Obra '!B28` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `A23` | `=L24` |
| `B23` | `='1. Canteiro'!L12` |
| `D23` | `='1. Canteiro'!C8` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `B24` | `='1. Canteiro'!L11` |
| `D24` | `='1. Canteiro'!C7` |
| `L24` | `=(L20*1.7)+(L21*2)+L23` |
| `A25` | `=L24` |
| `A26` | `=L24` |
| `A27` | `=L24` |
| `E27` | `=D27*B27*A27` |
| `K27` | `=I27*J27` |
| `K28` | `=J28*I28` |
| `K30` | `=(K27+K28)*K29` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `K32` | `=K31+K30` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `B52` | `=B24` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B23` |
| `F53` | `='Dados Obra '!B28` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `B69` | `=B52` |
| `E69` | `=D69*B69` |
| `E71` | `=SUM(E67:E69)` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E92` | `=F7*0.005` |
| `E97` | `=E92+E93+E94+E95` |
| `H99` | `=E97` |
| `I104` | `='Dados Obra '!B17` |
| `K104` | `=I104*J104` |
| `J105` | `=K104/I105` |
| `E106` | `=B106*D106` |
| `J106` | `=K104*(1/100)` |
| `E107` | `=B107*D107` |
| `J107` | `=SUM(J105:J106)` |
| `E109` | `=B109*D109` |
| `I109` | `=('Dados Obra '!B18/12)*3` |
| `K109` | `=I109*J109` |
| `J110` | `=K109/I110` |
| `J111` | `=K109*(1/100)` |
| `D112` | `='4.1 Draga Dec'!D109` |
| `E112` | `=B112*D112` |
| `J112` | `=SUM(J110:J111)` |
| `D114` | `=E103+E104+E105+E108+E109+E110+E111+E112+E106+E107` |
| `I114` | `=(I104/12)+2` |
| `K114` | `=I114*J114` |
| `J115` | `=K114/I115` |
| `J116` | `=K114*(1/100)` |
| `J117` | `=SUM(J115:J116)` |
| `H120` | `=J107` |
| `I120` | `=J112` |
| `J120` | `=J117` |
| `K120` | `=SUM(H120:J120)` |
| `E131` | `=E126+E127+E128+E129+E130` |
| `G134` | `=E131+D114+H99+G87+E15` |
| `E138` | `=G134*(5/100)` |
| `E139` | `=G134*(5/100)` |
| `E142` | `=E138+E139` |
| `E145` | `=F7/12` |
| `E146` | `=F7*0.005` |
| `E149` | `=E145+E146+E147` |
| `D168` | `=G134` |
| `D171` | `=E142` |
| `D173` | `=E149` |
| `D175` | `=D168+D171+D173` |
| `D184` | `=D180+D182` |
| `D187` | `=#REF!*0.6*0.62` |
| `J188` | `=H188*I188` |
| `D197` | `=D175` |
| `D198` | `='4.1 Draga Dec'!D200` |
| `D199` | `=D197*D198` |
| `J199` | `=D197` |
| `D201` | `=D199+D200` |
| `J201` | `=J199*J200` |
| `J202` | `=Produção!H6` |
| `J205` | `=(J201/J202)*J203` |

### 17. 5. Desmob Canteiro

- Faixa usada: `A1:N33`
- Fórmulas: **38**
- Conceitos provisórios: canteiro, desmobilizacao
- Células numéricas observadas: **124**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Mão de OBRA
- TURNOS
- Técnico de Segurança
- 1º
- 2º
- 3º
- Salário
- com 25%
- Operador de Draga
- Engº
- Operador de Centrífuga
- Ajudante Geral
- técnico Segurança
- Refeições
- Operador Draga
- Transporte
- Ajudante Draga
- Custo por dia
- Operador Centrífuga
- Ajudante Centrífuga
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
- Material de limpeza
- Preços VALE Vitória
- Mesa escritório
- mesa redonda
- cadeira
- armário escritório
- cestos lixo
- armário vestiário
- material de escritório
- Bebedouro
- Banheiro Quimico
- mes
- Mão de obra (integração)
- dia
- Tendas Paraná zap em 16/01/24
- (h= 3,0m)
- (h= 4,0m)
- TOTAL
- (6 x 6m) c/logotipo
- Prazo de Operação
- #NAME?
- (4 x 4m) c/logotipo
- preço unitário
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `=L7` |
| `C4` | `=(N7*N2)+N7` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `=(M8*N2)+M8` |
| `D5` | `=D4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `=(N9*N2)+N9` |
| `D6` | `=D4` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `L6` | `=I6+J6+K6` |
| `C7` | `=(N11*N2)+N11` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `L7` | `=I7+J7+K7` |
| `N7` | `=M7*1.25` |
| `C8` | `=(M12*N2)+M12` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `L8` | `=I8+J8+K8` |
| `A9` | `=SUM(A4:A8)` |
| `F9` | `=A9*C9` |
| `N9` | `=M9*1.25` |
| `A10` | `=A9` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F4:F10)` |
| `N11` | `=M11*1.25` |
| `I13` | `=SUM(I6:I12)` |
| `J13` | `=SUM(J7:J12)` |
| `K13` | `=SUM(K7:K12)` |
| `L13` | `=SUM(I13:K13)` |
| `F14` | `=D14*E14` |
| `K19` | `=I19*J19` |
| `K26` | `=SUM(K19:K25)` |
| `E28` | `=F11` |
| `F29` | `=SUM(F14:F28)` |
| `F30` | `=Produção!G19` |
| `F31` | `=F29/F30` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |

### 18. Desmob Draga

- Faixa usada: `A1:M43`
- Fórmulas: **56**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **128**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 10" e DRAGA ELETRICA OU MIUDA
- Mão de OBRA
- TURNOS
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- 1º
- 2º
- 3º
- Operador Líder
- Líder
- Técnico segurança
- Tec segurança
- Operador de Draga
- DRAGA
- Operador de Centrifuga
- Ajudante Geral
- Operador Draga
- Refeições
- Ajudante Draga
- Transporte
- CENTRÍFUGA
- Custo por dia
- Operador Centrífuga
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Guindaste para carregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Hospedagem da equipe (aluguel)
- mês
- Estimativa
- Carreta Carga Seca para DRAGA
- un
- Fabiano zap em 21/08/24 R$ 4.000 + 0,2% adv
- Guindaste p/descarregamento e montagem DRAGA
- FOS
- Plano de Rigger
- vb
- Mob do Guindaste
- Munck para descarregamento dos Containeres
- Frete para Containers
- Mobiliário Canteiro
- Mobiliário Alojamento
- Materiais SEGURANÇA (isolamentos e placas)
- PGR + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Tenda do Canteiro
- Locup
- Bebedouro
- custo Exames médicos
- Carreta p/ Equipamentos de complemento centrífuga
- Mão de obra p MOBILIZAÇÃO (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- Carreta 1 (draga)
- Carreta 2 (Tubulação 1500 m)
- Carreta 3 (flutuantes e outros periféricos)
- Carreta 4 (Draga elétrica)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A5` | `=M5` |
| `C5` | `='1. Canteiro'!C4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `='1. Canteiro'!I7` |
| `M5` | `=SUM(I5:L5)` |
| `A6` | `=M6` |
| `C6` | `='1. Canteiro'!C5` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=M9` |
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=M12` |
| `C8` | `='1. Canteiro'!C7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=M10+M13` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `I9` | `='1. Canteiro'!I9` |
| `J9` | `='1. Canteiro'!J9` |
| `K9` | `='1. Canteiro'!K9` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=SUM(A5:A9)` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `I10` | `='1. Canteiro'!I10` |
| `J10` | `='1. Canteiro'!J10` |
| `K10` | `='1. Canteiro'!K10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=A10` |
| `C11` | `='1. Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F5:F11)` |
| `K12` | `='1. Canteiro'!K11` |
| `M12` | `=SUM(I12:L12)` |
| `K13` | `='1. Canteiro'!K12` |
| `M13` | `=SUM(I13:L13)` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `D18` | `=C43` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `D31` | `=A11` |
| `F31` | `=D31*E31` |
| `F32` | `=D32*E32` |
| `E33` | `=E18` |
| `F33` | `=D33*E33` |
| `E34` | `=F12` |
| `F35` | `=SUM(F15:F34)` |
| `F36` | `=F35*(E36/100)` |
| `F37` | `=SUM(F35:F36)` |
| `C43` | `=SUM(C39:C42)` |

### 19. Desmob Centr

- Faixa usada: `A1:M42`
- Fórmulas: **49**
- Conceitos provisórios: desmobilizacao
- Células numéricas observadas: **119**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 10" e DRAGA ELETRICA OU MIUDA
- Mão de OBRA
- TURNOS
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- 1º
- 2º
- 3º
- Operador Líder
- Líder
- Técnico segurança
- Tec segurança
- Operador de Draga
- DRAGA
- Operador de Centrifuga
- Ajudante Geral
- Operador Draga
- Refeições
- Ajudante Draga
- Transporte
- CENTRÍFUGA
- Custo por dia
- Operador Centrífuga
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Guindaste para carregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Hospedagem da equipe (aluguel)
- mês
- Estimativa
- un
- Fabiano zap em 21/08/24 R$ 4.000 + 0,2% adv
- Guindaste p/descarregamento e montagem DRAGA
- FOS
- Plano de Rigger
- vb
- Mob guindaste
- Munck para descarregamento dos Containeres
- Instalações elétrica
- Materiais elétricas
- gl
- custo Exames médicos
- Carreta p/ Equipamentos de complemento centrífuga
- Mão de obra p MOBILIZAÇÃO (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- Carreta 1 (skid 1)
- Carreta 2 (skid 2)
- Carreta 3 (skid 3)
- Carreta 4 e 5 (Tqs Equalização + periféricos)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='1. Canteiro'!C4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `='1. Canteiro'!I7` |
| `M5` | `=SUM(I5:L5)` |
| `C6` | `='1. Canteiro'!C5` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=M9` |
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=M12` |
| `C8` | `='1. Canteiro'!C7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=M10+M13` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `K9` | `='1. Canteiro'!K9` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=SUM(A5:A9)` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `K10` | `='1. Canteiro'!K10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=A10` |
| `C11` | `='1. Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F5:F11)` |
| `K12` | `='1. Canteiro'!K11` |
| `M12` | `=SUM(I12:L12)` |
| `K13` | `='1. Canteiro'!K12` |
| `M13` | `=SUM(I13:L13)` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `E28` | `=J35*10` |
| `D30` | `=A11-A5-A6` |
| `D32` | `=C42` |
| `E32` | `=E18` |
| `F32` | `=D32*E32` |
| `E33` | `=F12` |
| `F34` | `=SUM(F15:F33)` |
| `F35` | `=F34*(E35/100)` |
| `F36` | `=SUM(F34:F35)` |
| `C42` | `=SUM(C38:C41)` |

### 20. Plan. Final

- Faixa usada: `A1:O34`
- Fórmulas: **68**
- Conceitos provisórios: outros
- Células numéricas observadas: **114**

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
- 1.1
- Mobilização Draga
- vb
- Dragagem e desaguamento Centrífuga
- 4.1
- Dragagem
- ton
- 4.2
- Operação Centrífuga
- Manutenção
- Base de Concreto
- Ensecadeira
- Aluguel
- Movimentaçao Lodo
- Desmobilização Draga
- DesMobilização Centrífuga
- Preço de Venda
- Quant mês
- Quant Total
- CUSTO UNIT
- BDI
- VENDA
- Custo TOTAL OPERAÇÃO
- Produção IDEAL CALCULADA
- TON/mês
- #NAME?
- Resultado SUZANO ARACRUZ
- Custo MENSAL OPERAÇÃO
- Impostos sobre NF
- Produção CONTRATUAL
- Faturamento mínimo para ZERAR
- Produção com Entrada FOS (1,5% ST)
- Produção mínima MENSAL (ton)
- PRODUÇÃO SEGURA (1,1%)
- Valor MÍNIMO da TON para ZERAR
- Produção MÍNIMA (1500 ton/mês)
- BDI praticado com a produção possível (1,5%) e o custo de produção mínima (1,0%)
- Custo para produção mínima + BDI
- CHORO

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='2.1 Mob Draga'!F37` |
| `G4` | `=C4/E4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `L4` | `=SUM(J4:J5)` |
| `C5` | `='2.2 Mob Centr'!F36` |
| `G5` | `=C5/E5` |
| `I5` | `=((H5/100)+1)*G5` |
| `J5` | `=E5*I5` |
| `C8` | `='4.1 Draga Dec'!D201` |
| `E8` | `=J24` |
| `G8` | `=C8/E8` |
| `I8` | `=((H8/100)+1)*G8` |
| `J8` | `=E8*I8` |
| `L8` | `=SUM(I8:I14)` |
| `C9` | `='4.2 Centrífuga'!D199` |
| `E9` | `=E8` |
| `G9` | `=C9/E9` |
| `I9` | `=((H9/100)+1)*G9` |
| `J9` | `=E9*I9` |
| `C10` | `='3.3 - Manutenção'!F21` |
| `E10` | `=E9` |
| `C11` | `='3.4. BASE DE CONCRETO'!F23` |
| `C12` | `='3.5. Remoção Ensecadeira'!F21` |
| `C13` | `='3.1 - Aluguel 3 meses Centrif'!F21` |
| `C14` | `='3.5. Mov. Lodo desag'!F23` |
| `C15` | `='Desmob Draga'!F37` |
| `G15` | `=C15/E15` |
| `I15` | `=((H15/100)+1)*G15` |
| `L15` | `=SUM(J15:J16)` |
| `C16` | `='Desmob Centr'!F36` |
| `G16` | `=C16/E16` |
| `I16` | `=((H16/100)+1)*G16` |
| `C18` | `=SUM(C4:C17)` |
| `J18` | `=SUM(J4:J17)` |
| `C20` | `=J18-C18` |
| `J20` | `=J18/E8` |
| `C22` | `=C8+C9` |
| `J22` | `=I22*Produção!G19` |
| `L22` | `=(C8+C9)/J22` |
| `N22` | `=(L22*M22)+L22` |
| `C23` | `=C22/Produção!G19` |
| `J24` | `=I24*Produção!G19` |
| `L24` | `=(C8+C9)/J24` |
| `N24` | `=(L24*M24)+L24` |
| `C25` | `=(C23*C24)+C23` |
| `I26` | `='Produção (NOVO CALCULO)'!M64` |
| `J26` | `='Plan. Final'!I26*58` |
| `L26` | `=(C8+C9)/J26` |
| `N26` | `=(L26*M26)+L26` |
| `C27` | `=I27` |
| `I27` | `='Produção (NOVO CALCULO)'!N64` |
| `J27` | `=I27*58` |
| `L27` | `=(C8+C9)/J27` |
| `N27` | `=(L27*M27)+L27` |
| `C28` | `=C25/C27` |
| `L28` | `=C23/C27` |
| `N28` | `=(L28*M28)+L28` |
| `L29` | `=L26` |
| `M29` | `=(N29/L29)-1` |
| `N29` | `=N24` |
| `C30` | `=C23/C27` |
| `L31` | `=L28` |
| `M31` | `=(N31/L31)-1` |
| `N31` | `=N27` |
| `L32` | `=L31` |
| `N32` | `=(L32*M32)+L32` |
| `N34` | `=N32*N33` |

### 21. Final

- Faixa usada: `A1:N21`
- Fórmulas: **22**
- Conceitos provisórios: outros
- Células numéricas observadas: **36**

#### Rótulos e textos observados

- Preço Aracruz REVISÃO FINAL
- Preço Suzano Jacareí
- ITEM
- DESCRIÇÃO DOS SERVIÇOS
- UN
- QUANT
- PREÇO UNIT
- PREÇO TOTAL
- $ Unit
- Ton SS
- Volume Dragado
- Mobilização e Montagem dos Equipamentos de Dragagem e Desaguamento por centrifuga
- vb
- OBS.: na condição errônea de medição aplicada na obra, acabamos praticando o valor de R$ 980,00/ton SS (50% do preço) e saímos com um resultado de 15%
- Dragagem e desaguamento de lodo através do processo de Centrifugação , inclui remoção da ensecadeira e movimentaçao do lodo desaguado até patio localizado a aproximadamente 9,5 km
- ton desaguada
- Remoção ensecadeira
- m3
- Desmobilização dos Equipamentos
- VALOR TOTAL
- Ton SDesaguada
- Preço total por TON
- a 40%
- Preço por Volume Dragado E centrifugado
- m³

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D3` | `='Plan. Final'!E4` |
| `E3` | `=H3` |
| `F3` | `=D3*E3` |
| `H3` | `='Plan. Final'!L4` |
| `D4` | `=5000` |
| `E4` | `=ROUNDUP(H4,2)` |
| `F4` | `=D4*E4` |
| `H4` | `='Plan. Final'!L8` |
| `F5` | `=D5*E5` |
| `E6` | `=H6` |
| `F6` | `=D6*E6` |
| `H6` | `='Plan. Final'!L15` |
| `F7` | `=SUM(F3:F6)` |
| `H7` | `=H3+H6+(I4*D4)` |
| `E8` | `=F7/F8` |
| `F8` | `='Plan. Final'!C18` |
| `F10` | `=F7/D4` |
| `J11` | `=J4*0.4` |
| `E12` | `='Dados Obra '!M10` |
| `F12` | `=F4/E12` |
| `E21` | `=D4*0.4` |
| `F21` | `=F4/E21` |

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
