# Modelo 004 — Composiçao - Draga 14 - com equipe.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `Composiçao - Draga 14 - com equipe.xlsx`
- Família provisória: **Composição padrão de draga**
- SHA-256 do arquivo: `c84bafdbf725be88e7ef440f61e2fe3b8bbd03bf491ed2de3480a170f2df2ce3`
- Abas analisadas: **8**
- Fórmulas encontradas: **327**

## Conceitos identificados

- `outros`: 2 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `desmobilizacao`: 1 aba(s)
- `dragagem_operacao`: 1 aba(s)
- `mao_obra`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:H27` | 4 | dados_obra |
| 2 | `Produção` | `A1:N24` | 16 | producao_prazo |
| 3 | `MDO x Turno` | `A1:E15` | 1 | mao_obra |
| 4 | `Canteiro` | `A1:N36` | 41 | canteiro |
| 5 | `1. Mobilização` | `A1:K49` | 61 | outros |
| 6 | `2. Dragagem` | `A1:R253` | 117 | dragagem_operacao |
| 7 | `3. Desmobilização` | `A1:K45` | 66 | desmobilizacao |
| 8 | `Final` | `A1:K11` | 21 | outros |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `MDO x Turno` | 53 |
| `1. Mobilização` | 12 |
| `Dados Obra` | 11 |
| `2. Dragagem` | 1 |
| `3. Desmobilização` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:H27`
- Fórmulas: **4**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **12**

#### Rótulos e textos observados

- SBV
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- Proposta
- Proposta D_020_2025
- Data
- Cliente
- Contato
- Cadu
- e-mail
- Dados da obra
- Objeto
- Locaçao Draga 14" com execuçao
- Local
- Parnaíba - PI
- Volume dragagem (m³)
- Tipo de material
- Areia Fina
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
- Sistema de Medição
- preço mensal
- Canteiro de obras
- Mobilização
- Horário de Trabalho (das 7 as 17h)
- h/dia
- Dias de Trabalho (2ª a 6ª)
- dias/mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `B16` | `=SUM(B17:B18)` |
| `H16` | `=B16+E16` |
| `H17` | `=B17+E17` |
| `G21` | `=B21*D21*B20` |

### 2. Produção

- Faixa usada: `A1:N24`
- Fórmulas: **16**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **25**

#### Rótulos e textos observados

- Cálculo de Produção da Draga
- Horas Trabalhadas por mês
- Unid.
- Quant.
- Tempo de Paralisações
- Vazão
- m³/h
- Horas / dia (6 as 18h)
- DDS
- Eficiência
- %
- Dias / Mês (2ª a 2ª)
- Deslocamento Ida
- Concentração
- Almoço
- Total de Horas / mês
- Desloc. Almoço
- Desloc. Volta
- Produção
- TOTAL
- MANOBRAS e ABASTECIMENTO
- Horas trabalhadas
- h/mês
- TURNO 1
- 6 às 12h
- EFICIÊNCIA
- TURNO 2
- 12 às 18h
- Produção mensal (m³/mês)
- ou
- Cálculo do Prazo da obra
- TURNO
- 12 x 36h
- Turno 1
- 2ª feira
- 4ª feira
- 6ª feira
- Domingo
- 3ª feira
- 5ª feira
- Turno 2
- sábado
- Produção mensal
- m³/mês
- MONTAR BARRILETE PARA ENCHER AS CHICANES
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
| `L8` | `=SUM(L3:L7)` |
| `M8` | `=L8*24` |
| `N8` | `=M8/H3` |
| `M9` | `=L9*24` |
| `N9` | `=M9/H3` |
| `D11` | `=H6` |
| `N11` | `=N8+N9` |
| `D13` | `=D8*D11` |
| `D18` | `=D13` |
| `D21` | `='Dados Obra '!B14` |
| `D24` | `=D21/D18` |
| `E24` | `=ROUNDUP(D24,0)` |

### 3. MDO x Turno

- Faixa usada: `A1:E15`
- Fórmulas: **1**
- Conceitos provisórios: mao_obra
- Células numéricas observadas: **8**

#### Rótulos e textos observados

- JORNADA DE TRABALHO
- 44H semanais - seg a sexta
- ADM
- TURNO - A
- Engenheiro
- Aux Técnico
- Mecânico
- Encarregado
- Operador de Draga
- Maquinista
- Barqueiro
- Ajudante
- fornecido pelo cliente
- Veículo (ajudantes nosso)
- Veículo (ajudantes Coedra)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `None` | `` |

### 4. Canteiro

- Faixa usada: `A1:N36`
- Fórmulas: **41**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **152**

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
- Mecânico
- Encarregado
- Operador de Draga
- Maquinista
- Barqueiro
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
- COEDRA
- Container Sanitário/Vestiário
- Container Escritório
- Frete para Containers
- vb
- Mobiliário Canteiro
- Mobiliário Alojamento
- PGR + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Placa de obra
- Itens sinalização e segurançaq
- água potável
- gl
- material de escritório
- Banheiro Quimico
- mes
- custo Exames médicos
- un
- Mão de obra (manutenção)
- dia
- MÃO DE OBRA
- DIAS
- TOTAL
- viagem de ida
- Prazo de Operação
- Treinamentos
- preço unitário
- Integração
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `='MDO x Turno'!B5` |
| `C4` | `=M4` |
| `D4` | `='Dados Obra '!B26*N4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `J4` | `=I4/220` |
| `K4` | `=J4*0.075` |
| `M4` | `=J4+K4+L4` |
| `A5` | `='MDO x Turno'!B6` |
| `D5` | `='Dados Obra '!B26*N5` |
| `E5` | `=E4` |
| `K5` | `=J5*0.075` |
| `A6` | `='MDO x Turno'!B7` |
| `D6` | `=D5` |
| `A7` | `='MDO x Turno'!C8+'MDO x Turno'!D8` |
| `L7` | `=(J7+K7)*0.25` |
| `A8` | `='MDO x Turno'!C9+'MDO x Turno'!D9` |
| `L8` | `=(J8+K8)*0.25` |
| `A9` | `='MDO x Turno'!C10+'MDO x Turno'!D10` |
| `L9` | `=(J9+K9)*0.25` |
| `A10` | `='MDO x Turno'!C11+'MDO x Turno'!D11` |
| `L10` | `=(J10+K10)*0.25` |
| `A11` | `='MDO x Turno'!B12` |
| `A12` | `=SUM(A4:A11)` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F4:F13)` |
| `D17` | `=Produção!E24` |
| `F17` | `=D17*E17` |
| `D18` | `=D17` |
| `D19` | `=D17` |
| `D27` | `=D17*(1*22)` |
| `D28` | `=D17` |
| `D29` | `=D17` |
| `E31` | `=F14` |
| `F32` | `=SUM(F17:F31)` |
| `F33` | `=Produção!E24` |
| `F34` | `=F32/F33` |
| `F35` | `=F34*(E35/100)` |
| `I35` | `=SUM(I32:I34)` |
| `F36` | `=F34+F35` |

### 5. 1. Mobilização

- Faixa usada: `A1:K49`
- Fórmulas: **61**
- Conceitos provisórios: outros
- Células numéricas observadas: **151**

#### Rótulos e textos observados

- 1.1. Canteiro de obras, mobilização e manutenção de equipes e equipamentos
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Mão de OBRA
- TURNOS
- Engenheiro
- A
- B
- Aux Técnico
- Mecânico
- Encarregado
- Operador de Draga
- Maquinista
- Barqueiro
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
- MOBILIZAÇÃO EQUIPE
- Treinamentos de Segurança
- un
- Exames médicos
- Viagem de ida para obra
- vb
- chute
- Laudo de flutuabilidade
- Mobiliário Canteiro
- SBV
- Mobiliário Alojamento
- PGR + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Itens sinalização e segurançaq
- Mão de obra Integração, Viagens e treinamentos
- dia
- MOBILIZAÇÃO DOS EQUIPAMENTOS
- Guindaste para Carregamento
- Carreta prancha rebaixada
- Cruz de Malta em 14/04/25
- Carreta extensível
- Cruz de Malta em 14/04/26
- Seguro de Transporte da Carga
- Carreta Carga Seca
- Fabiano zap 14/04/25 = 11.500 + 0,2% adv
- Guindaste para descarregamento e montagem
- Cliente
- Planos de Rigging
- Aluguel de Veículo + combustível
- vb/mês
- Mão de obra Mobilização (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- Largura carga
- Altura grade
- altura acima
- Diâmetro tubo
- Quant. Tubos
- compr. Tubo
- R$ tubo
- Carga seca graneleira
- Total da Linha
- Quant de Carretas para tubos
- RESPONSABILIDADE SBV

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `=K5` |
| `C4` | `=Canteiro!C4` |
| `D4` | `=Canteiro!D4` |
| `E4` | `=Canteiro!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `=Canteiro!C5` |
| `D5` | `=Canteiro!D5` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `='MDO x Turno'!B5` |
| `J5` | `='MDO x Turno'!D5` |
| `K5` | `=I5+J5` |
| `C6` | `=Canteiro!C6` |
| `D6` | `=D5` |
| `I6` | `='MDO x Turno'!B6` |
| `J6` | `='MDO x Turno'!D6` |
| `K6` | `=I6+J6` |
| `C7` | `=Canteiro!C7` |
| `I7` | `='MDO x Turno'!B7` |
| `J7` | `='MDO x Turno'!D7` |
| `C8` | `=Canteiro!C8` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `I8` | `='MDO x Turno'!C8` |
| `J8` | `='MDO x Turno'!D8` |
| `C9` | `=Canteiro!C9` |
| `I9` | `='MDO x Turno'!C9` |
| `J9` | `='MDO x Turno'!D9` |
| `C10` | `=Canteiro!C10` |
| `F10` | `=(A10*C10*D10)+(A10*C10*D10)*(E10/100)` |
| `I10` | `='MDO x Turno'!C10` |
| `J10` | `='MDO x Turno'!D10` |
| `A11` | `='MDO x Turno'!B12` |
| `C11` | `=Canteiro!C11` |
| `I11` | `='MDO x Turno'!C11` |
| `J11` | `='MDO x Turno'!D11` |
| `A12` | `=SUM(A4:A11)` |
| `C12` | `=Canteiro!C12` |
| `F12` | `=A12*C12` |
| `I12` | `='MDO x Turno'!C12` |
| `J12` | `='MDO x Turno'!D12` |
| `K12` | `=SUM(I12:J12)` |
| `A13` | `=A12` |
| `C13` | `=Canteiro!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F4:F13)` |
| `D18` | `=A12` |
| `F18` | `=D18*E18` |
| `D19` | `=A12` |
| `D20` | `=SUM(A6:A10)` |
| `E27` | `=F14` |
| `F29` | `=D29*E29` |
| `F34` | `=D34*E34` |
| `D36` | `='MDO x Turno'!B15+'MDO x Turno'!C15+'MDO x Turno'!D15` |
| `E37` | `=F14` |
| `F38` | `=SUM(F18:F37)` |
| `F39` | `=F38*(E39/100)` |
| `F40` | `=SUM(F38:F39)` |
| `G43` | `=((D43+E43)/F43)*(C43/F43)` |
| `I43` | `=G43*H43` |
| `I44` | `='Dados Obra '!B16` |
| `I45` | `=ROUNDUP(((I44/I43)+1),0)` |

### 6. 2. Dragagem

- Faixa usada: `A1:R253`
- Fórmulas: **117**
- Conceitos provisórios: dragagem_operacao
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `=Produção!H6` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=(C9*D9*E9*J9)*0.1` |
| `F12` | `=F11*0.1` |
| `F13` | `=F12` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24*0.2` |
| `B20` | `='1. Mobilização'!K5` |
| `D20` | `=Canteiro!M4` |
| `E20` | `=D20*B20*A20` |
| `K20` | `='Dados Obra '!B27` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `B21` | `='1. Mobilização'!K6` |
| `D21` | `=Canteiro!M5` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `B22` | `='1. Mobilização'!K7` |
| `D22` | `=Canteiro!M6` |
| `A23` | `=L24` |
| `B23` | `='1. Mobilização'!K8` |
| `D23` | `=Canteiro!M7` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `B24` | `='1. Mobilização'!K9` |
| `D24` | `=Canteiro!M8` |
| `L24` | `=(L20*1.7)+(L21*2)+L23` |
| `A25` | `=L24` |
| `B25` | `='1. Mobilização'!K10` |
| `D25` | `=Canteiro!M9` |
| `A26` | `=L24` |
| `B26` | `='1. Mobilização'!K11` |
| `D26` | `=Canteiro!M10` |
| `A27` | `=L24` |
| `B27` | `='MDO x Turno'!B12` |
| `D27` | `=Canteiro!M11` |
| `E27` | `=D27*B27*A27` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `A37` | `=Canteiro!E4` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `B52` | `=B22+B23+B24+B25+B26` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B21+B27` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `E71` | `=E69` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E139` | `=(0.6/100)*F7` |
| `E140` | `=(1/100)*F7` |
| `E141` | `=E139*0.1` |
| `E142` | `=E141` |
| `E144` | `=E139+E140+E141+E142` |
| `H146` | `=E144` |
| `E150` | `=K167` |
| `I151` | `='Dados Obra '!H16` |
| `K151` | `=I151*J151` |
| `O151` | `=370*12` |
| `P151` | `=400*2` |
| `Q151` | `=O151+P151` |
| `R151` | `=Q151/12` |
| `J152` | `=K151/I152` |
| `J153` | `=K151*(1/100)` |
| `J154` | `=SUM(J152:J153)` |
| `I156` | `='Dados Obra '!H17/12*3` |
| `K156` | `=I156*J156` |
| `E157` | `=P157/D157` |
| `J157` | `=K156/I157` |
| `O157` | `=457600+301000` |
| `P157` | `=N157*O157` |
| `E158` | `=Canteiro!F34` |
| `J158` | `=K156*(1/100)` |
| `O158` | `=24162+9162` |
| `E159` | `=P164/D159` |
| `J159` | `=SUM(J157:J158)` |
| `O159` | `=O158` |
| `D161` | `=E150+E151+E152+E155+E156+E157+E158+E159+E153+E154` |
| `I161` | `=(I151/12)+2` |
| `K161` | `=I161*J161` |
| `O161` | `=7444+7154` |
| `J162` | `=K161/I162` |
| `O162` | `=46502+78469` |
| `J163` | `=K161*(1/100)` |
| `J164` | `=SUM(J162:J163)` |
| `P164` | `=SUM(P158:P163)` |
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
| `D222` | `=G181` |
| `D225` | `=E189` |
| `D227` | `=E196` |
| `D229` | `=D222+D225+D227` |
| `E232` | `=Produção!D13` |
| `E234` | `=D229/E232` |
| `D236` | `=D229*B236` |
| `D238` | `=D236+D229` |
| `J242` | `=D229` |
| `J244` | `=J242*J243` |
| `L244` | `=J244/J245` |
| `J245` | `=Produção!H6` |
| `L246` | `=L244*L245` |
| `J248` | `=(J244/J247)*J246` |
| `D249` | `=D229` |
| `J250` | `=J248*J249` |
| `D251` | `=SUM(D249:D250)` |
| `D252` | `=Produção!E24` |
| `D253` | `=D251*D252` |

### 7. 3. Desmobilização

- Faixa usada: `A1:K45`
- Fórmulas: **66**
- Conceitos provisórios: desmobilizacao
- Células numéricas observadas: **150**

#### Rótulos e textos observados

- 3. DESMOBILIZAÇÃO
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Mão de OBRA
- TURNOS
- Engenheiro
- A
- B
- Aux Técnico
- Mecânico
- Encarregado
- Operador de Draga
- Maquinista
- Barqueiro
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
- MOBILIZAÇÃO EQUIPE
- Treinamentos de Segurança
- un
- MÃO DE OBRA
- DIAS
- Exames médicos
- viagem de volta
- Viagem de volta da obra
- vb
- Laudo de flutuabilidade
- Mobiliário Canteiro
- Mobiliário Alojamento
- PGR + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Itens sinalização e segurançaq
- Mão de obra Integração, Viagens e treinamentos
- dia
- MOBILIZAÇÃO DOS EQUIPAMENTOS
- Guindaste para DESCarregamento
- Carreta prancha rebaixada
- Cruz de Malta em 14/04/25
- Carreta extensível
- Cruz de Malta em 14/04/26
- Seguro de Transporte da Carga
- chute
- Carreta Carga Seca
- Fabiano zap 14/04/25 = 11.500 + 0,2% adv
- Guindaste para carregamento e DESmontagem
- Cliente
- Planos de Rigging
- Aluguel de Veículo + combustível
- vb/mês
- Mão de obra Mobilização (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- Largura carga
- Altura grade
- altura acima
- Diâmetro tubo
- Quant. Tubos
- compr. Tubo
- R$ tubo
- Carga seca graneleira
- Total da Linha
- Quant de Carretas para tubos

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `=K5` |
| `C4` | `=Canteiro!C4` |
| `D4` | `=Canteiro!D4` |
| `E4` | `=Canteiro!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `=Canteiro!C5` |
| `D5` | `=Canteiro!D5` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `='MDO x Turno'!B5` |
| `J5` | `='MDO x Turno'!D5` |
| `K5` | `=I5+J5` |
| `C6` | `=Canteiro!C6` |
| `D6` | `=D5` |
| `I6` | `='MDO x Turno'!B6` |
| `J6` | `='MDO x Turno'!D6` |
| `K6` | `=I6+J6` |
| `C7` | `=Canteiro!C7` |
| `I7` | `='MDO x Turno'!B7` |
| `J7` | `='MDO x Turno'!D7` |
| `C8` | `=Canteiro!C8` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `I8` | `='MDO x Turno'!C8` |
| `J8` | `='MDO x Turno'!D8` |
| `C9` | `=Canteiro!C9` |
| `I9` | `='MDO x Turno'!C9` |
| `J9` | `='MDO x Turno'!D9` |
| `C10` | `=Canteiro!C10` |
| `F10` | `=(A10*C10*D10)+(A10*C10*D10)*(E10/100)` |
| `I10` | `='MDO x Turno'!C10` |
| `J10` | `='MDO x Turno'!D10` |
| `A11` | `='MDO x Turno'!B12` |
| `C11` | `=Canteiro!C11` |
| `I11` | `='MDO x Turno'!C11` |
| `J11` | `='MDO x Turno'!D11` |
| `A12` | `=SUM(A4:A11)` |
| `C12` | `=Canteiro!C12` |
| `F12` | `=A12*C12` |
| `I12` | `='MDO x Turno'!C12` |
| `J12` | `='MDO x Turno'!D12` |
| `K12` | `=SUM(I12:J12)` |
| `A13` | `=A12` |
| `C13` | `=Canteiro!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F4:F13)` |
| `F18` | `=D18*E18` |
| `D19` | `=A12` |
| `D20` | `=SUM(A6:A10)` |
| `I22` | `=SUM(I19:I21)` |
| `D27` | `=I22` |
| `E27` | `=F14` |
| `F29` | `=D29*E29` |
| `E30` | `='1. Mobilização'!E30` |
| `E31` | `='1. Mobilização'!E31` |
| `E32` | `='1. Mobilização'!E32` |
| `E33` | `='1. Mobilização'!E33` |
| `F34` | `=D34*E34` |
| `D36` | `='MDO x Turno'!B15+'MDO x Turno'!C15+'MDO x Turno'!D15` |
| `E37` | `=F14` |
| `F38` | `=SUM(F18:F37)` |
| `F39` | `=F38*(E39/100)` |
| `F40` | `=SUM(F38:F39)` |
| `G43` | `=((D43+E43)/F43)*(C43/F43)` |
| `I43` | `=G43*H43` |
| `I44` | `='Dados Obra '!B16` |
| `I45` | `=ROUNDUP(((I44/I43)+1),0)` |

### 8. Final

- Faixa usada: `A1:K11`
- Fórmulas: **21**
- Conceitos provisórios: outros
- Células numéricas observadas: **29**

#### Rótulos e textos observados

- PLANILHA DETALHADA PREÇOS DE CUSTO E VENDA
- Preços com BDI
- Item
- Descrição dos Serviços
- Custo Total
- Quantidade
- Unid
- Custo Unitário
- BDI (%)
- Preço Unitário
- Preço Total
- Mobilizaçao e montagem de Equipamento de Dragagem
- un
- Dragagem
- M³
- Desmobilizaçao Equipamento de Dragagem
- Preço de Venda
- Custo mensal Dragagem
- RESULTADO FINAL
- Faturamento de Dragagem
- Resultado mensal LIVRE

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Mobilização'!F38` |
| `G4` | `=C4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `C5` | `='2. Dragagem'!D253` |
| `E5` | `='Dados Obra '!B14` |
| `G5` | `=C5/E5` |
| `I5` | `=((H5/100)+1)*G5` |
| `J5` | `=E5*I5` |
| `C6` | `='3. Desmobilização '!F38` |
| `G6` | `=C6/E6` |
| `I6` | `=((H6/100)+1)*G6` |
| `J6` | `=E6*I6` |
| `C7` | `=SUM(C4:C6)` |
| `J7` | `=SUM(J4:J6)` |
| `K7` | `=J7/4` |
| `C9` | `=C5/4` |
| `J9` | `=J7-C7` |
| `C10` | `=J5/4` |
| `J10` | `=J9/4` |
| `C11` | `=C10-C9` |

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
