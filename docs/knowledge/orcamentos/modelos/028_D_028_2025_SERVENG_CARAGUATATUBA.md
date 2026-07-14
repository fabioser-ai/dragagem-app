# Modelo 028 — D_028_2025- SERVENG - CARAGUATATUBA.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `D_028_2025- SERVENG - CARAGUATATUBA.xlsx`
- Família provisória: **Dragagem/bombeamento**
- SHA-256 do arquivo: `63058fc1f292ab56e320f521d9f8910c1c2914a374abf076d866acd77bd643e6`
- Abas analisadas: **8**
- Fórmulas encontradas: **184**

## Conceitos identificados

- `mobilizacao_draga`: 2 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `desmobilizacao`: 1 aba(s)
- `dragagem_operacao`: 1 aba(s)
- `formacao_preco`: 1 aba(s)
- `medicao_batimetria`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:H27` | 3 | dados_obra |
| 2 | `Produção` | `A1:H24` | 8 | producao_prazo |
| 3 | `1. Mob. Draga` | `A1:G24` | 18 | mobilizacao_draga |
| 4 | `2. Canteiro de obras` | `A1:G32` | 21 | canteiro |
| 5 | `3. Dragagem` | `A1:L251` | 84 | dragagem_operacao |
| 6 | `4. Desmob. Draga` | `A1:F24` | 18 | mobilizacao_draga, desmobilizacao |
| 7 | `5. Mediçao` | `A1:H23` | 19 | medicao_batimetria |
| 8 | `6. Plan. Preços` | `A1:L8` | 13 | formacao_preco |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `Dados Obra` | 12 |
| `1. Mob. Draga` | 1 |
| `2. Canteiro de obras` | 1 |
| `3. Dragagem` | 1 |
| `4. Desmob. Draga` | 1 |
| `5. Mediçao` | 1 |

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
- Proposta D_028_2025
- Data
- Cliente
- SERVENG
- Contato
- e-mail
- Dados da obra
- Objeto
- Rio Juqueriquere
- Local
- Caraguatatuba - SP
- Volume dragagem (m³)
- Tipo de material
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
- Bacia de Decantaçao
- Sistema de Medição
- preços unitários de serviços
- Canteiro de obras
- FOS
- Mobilização
- Horário de Trabalho (7 as 17)
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
- Fórmulas: **8**
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
- Células numéricas observadas: **49**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 10"
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
- Fabiano (7200 - 23/04/2025)
- Guindaste p/descarregamento e montagem DRAGA
- Serveng
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

### 4. 2. Canteiro de obras

- Faixa usada: `A1:G32`
- Fórmulas: **21**
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
- Serveng
- Container Sanitário/Vestiário
- Container Escritório c/sanitário
- Frete para Containers
- vb
- PPRA + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- EPI
- Func
- Placa de obra
- Vigilância
- água potável
- gl
- material de escritório
- #NAME?
- Banheiro quimico
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
| `F15` | `=D15*E15` |
| `D21` | `=A8` |
| `F23` | `=D23*E23` |
| `D24` | `=8*F30` |
| `D25` | `=ROUNDUP(Produção!D24,0)+1` |
| `E28` | `=F10` |
| `F29` | `=SUM(F15:F28)` |
| `F30` | `=ROUNDUP(Produção!D24,0)` |
| `F31` | `=F29*(E31/100)` |
| `F32` | `=F29/F30` |

### 5. 3. Dragagem

- Faixa usada: `A1:L251`
- Fórmulas: **84**
- Conceitos provisórios: dragagem_operacao
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `=Produção!H6` |
| `F10` | `=C9*D9*E9*F9` |
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
| `E158` | `='2. Canteiro de obras'!F32` |
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
| `D225` | `=Produção!D13` |
| `D231` | `=D227+D229` |
| `D234` | `=J251*0.6*0.62` |
| `H235` | `=Produção!H4` |
| `I235` | `=Produção!H3` |
| `J235` | `=H235*I235` |
| `D244` | `=D222` |
| `D245` | `=SUM(D244:D244)` |
| `J245` | `=D245` |
| `D246` | `=ROUNDUP(Produção!D24,0)` |
| `D247` | `=D245*D246` |
| `J247` | `=J245*J246` |
| `J248` | `=Produção!H6` |
| `L248` | `=J247/J248` |
| `J250` | `=J248*J249` |
| `L250` | `=L248*L249` |
| `J251` | `=J247/J250` |

### 6. 4. Desmob. Draga

- Faixa usada: `A1:F24`
- Fórmulas: **18**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **49**

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

### 7. 5. Mediçao

- Faixa usada: `A1:H23`
- Fórmulas: **19**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **40**

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
- Topografia
- un
- 5 Ações de Topografia
- Seguro de RC
- vb
- Acompanhamento FOS
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
| `D15` | `=22142*5` |
| `F15` | `=D15*E15` |
| `E16` | `=8269.69*1.3` |
| `F16` | `=D16*E16` |
| `E17` | `=F10` |
| `F18` | `=SUM(F15:F17)` |
| `F19` | `=F18*(E19/100)` |
| `F20` | `=SUM(F18:F19)` |
| `F22` | `=F21*(E22/100)` |
| `F23` | `=SUM(F21:F22)` |

### 8. 6. Plan. Preços

- Faixa usada: `A1:L8`
- Fórmulas: **13**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **31**

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
- Dragagem
- m3
- Medição
- Desmobilizaçao Equipamento de Dragagem
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Mob. Draga '!F24` |
| `G4` | `=C4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `C5` | `='3. Dragagem'!D247` |
| `E5` | `='Dados Obra '!B14` |
| `G5` | `=C5/E5` |
| `C6` | `='5. Mediçao'!F20` |
| `L6` | `=(SUM(J5:J6))/E5` |
| `C7` | `='4. Desmob. Draga'!F24` |
| `G7` | `=C7/E7` |
| `C8` | `=SUM(C4:C7)` |
| `J8` | `=SUM(J4:J7)` |

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
