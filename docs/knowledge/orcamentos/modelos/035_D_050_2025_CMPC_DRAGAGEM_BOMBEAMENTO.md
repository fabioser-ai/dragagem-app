# Modelo 035 — D_050_2025 - CMPC - Dragagem - Bombeamento.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `D_050_2025 - CMPC - Dragagem - Bombeamento.xlsx`
- Família provisória: **Dragagem/bombeamento**
- SHA-256 do arquivo: `84f1389bb6a8d5b0523929f503b4ead0077cfb0ceb5e274d399bc4a7a1979d63`
- Abas analisadas: **8**
- Fórmulas encontradas: **334**

## Conceitos identificados

- `desmobilizacao`: 2 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `outros`: 2 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:O27` | 11 | dados_obra |
| 2 | `Produção` | `A1:I38` | 13 | producao_prazo |
| 3 | `3. Canteiro` | `A1:N38` | 51 | canteiro |
| 4 | `4. Mob Draga` | `A1:N36` | 57 | mobilizacao_draga |
| 5 | `7.2 Draga` | `A1:L207` | 88 | outros |
| 6 | `9. DesMob Draga` | `A1:G36` | 50 | mobilizacao_draga, desmobilizacao |
| 7 | `15. Desmob Final` | `A1:N38` | 37 | desmobilizacao |
| 8 | `Plan. Final` | `A1:L17` | 27 | outros |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `3. Canteiro` | 46 |
| `Dados Obra` | 10 |
| `15. Desmob Final` | 3 |
| `4. Mob Draga` | 1 |
| `7.2 Draga` | 1 |
| `9. DesMob Draga` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:O27`
- Fórmulas: **11**
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
- Proposta D_042_2025
- Data
- REVISÃO ATUAL
- Cliente
- CMPC IGUAÇU
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
- Bombeamento Direto lagoa 2
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
| `H16` | `=B16+E16` |
| `B17` | `=M15` |
| `H17` | `=B17+E17` |
| `O18` | `=2*300` |
| `G21` | `=B21*D21*B20` |

### 2. Produção

- Faixa usada: `A1:I38`
- Fórmulas: **13**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **22**

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
| `H34` | `=D27` |
| `H38` | `=SUM(H32:H37)` |

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
| `D18` | `=Produção!H38` |
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

### 4. 4. Mob Draga

- Faixa usada: `A1:N36`
- Fórmulas: **57**
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
- Zap de 11/07/25
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
| `F27` | `=D27*E27` |
| `E28` | `=F13` |
| `F28` | `=D28*E28` |
| `E29` | `=F13` |
| `F30` | `=SUM(F16:F29)` |
| `F31` | `=F30*(E31/100)` |
| `N31` | `=SUM(N19:N30)` |
| `F32` | `=SUM(F30:F31)` |

### 5. 7.2 Draga

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
| `D201` | `=Produção!H34` |
| `J201` | `=D200` |
| `D202` | `=D200*D201` |
| `J203` | `=J201*J202` |
| `L203` | `=J203/J204` |
| `L205` | `=L203*L204` |
| `J206` | `=J204*J205` |
| `J207` | `=J203/J206` |

### 6. 9. DesMob Draga

- Faixa usada: `A1:G36`
- Fórmulas: **50**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **89**

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
| `F27` | `=D27*E27` |
| `D28` | `=A11` |
| `F28` | `=D28*E28` |
| `E29` | `=F13` |
| `F30` | `=SUM(F16:F29)` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=SUM(F30:F31)` |

### 7. 15. Desmob Final

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

### 8. Plan. Final

- Faixa usada: `A1:L17`
- Fórmulas: **27**
- Conceitos provisórios: outros
- Células numéricas observadas: **42**

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
- DRAGAGEM E DESAGUAMENTO
- 7.2
- Dragagem
- m³
- Desmobilização da Draga e Eqto Pol.
- Desmobilização FINAL
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='3. Canteiro'!F34` |
| `E5` | `=Produção!H38` |
| `G5` | `=C5/E5` |
| `I5` | `=((H5/100)+1)*G5` |
| `J5` | `=E5*I5` |
| `L5` | `=I5` |
| `C6` | `='4. Mob Draga'!F30` |
| `L6` | `=I6` |
| `C8` | `='7.2 Draga'!D202` |
| `E8` | `='Dados Obra '!B14` |
| `G8` | `=C8/E8` |
| `I8` | `=((H8/100)+1)*G8` |
| `J8` | `=E8*I8` |
| `C9` | `='9. DesMob Draga'!F30` |
| `G9` | `=C9/E9` |
| `I9` | `=((H9/100)+1)*G9` |
| `J9` | `=E9*I9` |
| `L9` | `=I9` |
| `C10` | `='15. Desmob Final'!F34` |
| `G10` | `=C10/E10` |
| `I10` | `=((H10/100)+1)*G10` |
| `J10` | `=E10*I10` |
| `L10` | `=I10` |
| `C12` | `=SUM(C10:C11)` |
| `J12` | `=SUM(J4:J11)` |
| `C14` | `=J12-C12` |
| `C17` | `=J12*0.01` |

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
