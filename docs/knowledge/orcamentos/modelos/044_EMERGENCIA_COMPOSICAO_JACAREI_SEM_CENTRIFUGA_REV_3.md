# Modelo 044 — EMERGENCIA - Composição - Jacarei - Sem Centrifuga  - Rev.3.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `EMERGENCIA - Composição - Jacarei - Sem Centrifuga  - Rev.3.xlsx`
- Família provisória: **Dragagem com centrífuga**
- SHA-256 do arquivo: `4257d3cc7461b4b9ce4fc87d337556d7635e4abc4553fd27aa01c23fa80d194e`
- Abas analisadas: **12**
- Fórmulas encontradas: **525**

## Conceitos identificados

- `outros`: 6 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `desmobilizacao`: 1 aba(s)
- `mao_obra`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:S28` | 14 | dados_obra |
| 2 | `Fornecedores` | `A1:F15` | 1 | outros |
| 3 | `Produção (NOVO CALCULO)` | `A1:S29` | 26 | producao_prazo |
| 4 | `1. Canteiro` | `A1:N33` | 46 | canteiro |
| 5 | `2.1 Mob Draga` | `A1:M42` | 52 | mobilizacao_draga |
| 6 | `4.1 Draga Dec` | `A1:L206` | 95 | outros |
| 7 | `Tq Equal.` | `A1:N33` | 44 | outros |
| 8 | `Venda Draga` | `A1:L26` | 26 | outros |
| 9 | `Draga MDO` | `A1:L206` | 96 | mao_obra |
| 10 | `Desmob Draga` | `A1:M43` | 57 | mobilizacao_draga, desmobilizacao |
| 11 | `Plan. Final` | `A1:L18` | 34 | outros |
| 12 | `Final` | `A1:M12` | 34 | outros |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `1. Canteiro` | 40 |
| `Dados Obra` | 12 |
| `2.1 Mob Draga` | 11 |
| `Plan. Final` | 9 |
| `4.1 Draga Dec` | 5 |
| `Produção (NOVO CALCULO)` | 4 |
| `[1]Plan. Final` | 2 |
| `Desmob Draga` | 1 |
| `Draga MDO` | 1 |
| `Tq Equal.` | 1 |
| `Venda Draga` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:S28`
- Fórmulas: **14**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **33**

#### Rótulos e textos observados

- SUZANO
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- PARÂMETROS DO ESCOPO
- Preto :
- resultados automáticos
- Proposta
- Proposta D_026_2025
- Data
- Produção Desejada ( MINIMA)
- Ton des/mês
- Ton desaguada total
- % SS in situ
- % SS desaguado
- Cliente
- Volume Estimado a Dragar
- m³/mês
- Contato
- Thais
- e-mail
- Prazo de Operação
- meses
- Base Seca
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
- Lagoa de Polimento
- Local
- Suzano - SP
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
- CENTRÍFUGA ( PROPRIEDADE SUZANO)
- Sistema de Medição
- preços unitários de serviços
- Canteiro de obras
- FOS
- Mobilização
- Horário de Trabalho (das 8 as 17h)
- h/dia
- Dias de Trabalho (2ª a sábado )
- dias/mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `O5` | `=(M10*M6)/M7` |
| `M8` | `=(M5*M7)/M6` |
| `P9` | `=M10*M6` |
| `M10` | `=M8*M9` |
| `L13` | `=M10` |
| `O13` | `=M13+N13` |
| `Q13` | `=L13*P13` |
| `S13` | `=Q13/R13` |
| `Q16` | `=SUM(Q13:Q15)` |
| `S16` | `=SUM(S13:S15)` |
| `H17` | `=B17+E17` |
| `H18` | `=B18+E18` |
| `G22` | `=B22*D22*B21` |
| `O22` | `=M22*N22` |

### 2. Fornecedores

- Faixa usada: `A1:F15`
- Fórmulas: **1**
- Conceitos provisórios: outros
- Células numéricas observadas: **7**

#### Rótulos e textos observados

- ATIVIDADE:
- GUINDASTE - 100 TON
- EMPRESA
- CONTATO
- TELEFONE
- E-MAIL
- PREÇO
- OBSERVAÇAO
- TRUCKAP
- (11) 99847-2900
- ENGEGUIND
- DANIEL
- (11) 2033-0015 / (11) 99329-7766
- Diária
- Plano de Rigger
- Mob
- Desmob
- CORTESIA
- Integraçao Antecipada
- SAO JOSE
- NAIRÊ
- (11) 2238-4444 / (11) 2238-4441
- diaria
- mob
- CONTAINER

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `None` | `` |

### 3. Produção (NOVO CALCULO)

- Faixa usada: `A1:S29`
- Fórmulas: **26**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **46**

#### Rótulos e textos observados

- x1 Centrigufa
- Se na lagoa 2%
- M3/h
- m3/h
- x3 Centrífugas
- Bombeamento 20% material
- 20 metros de skid - centrifuga de 60M3/h
- 20% de 3,5%
- DIAS
- 3 turnos
- %ST
- HIGIENIZAÇÃO
- TEMPO UTIL
- HORAS MES Trabalhadas
- TURNOS
- #REF!
- TURNOS 1
- TURNOS 2
- FINAL
- 1X CENTRIFUGA DE 40 m3/h
- REGIME DE 24 HORAS (3 turno)
- ton base seca / hora
- Ton Hora
- Ton Dia
- Ton Mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `E4` | `=C4*3` |
| `J5` | `=M1*L1` |
| `F10` | `=E10-D10` |
| `H10` | `=24*0.7` |
| `I10` | `=H10*0.75` |
| `J10` | `=H10*D6` |
| `S10` | `=#REF!-S9` |
| `F11` | `=E11-D11` |
| `L11` | `=L9*L10` |
| `F12` | `=E12-D12` |
| `H13` | `=(F11+F12)-G10` |
| `I13` | `=L11` |
| `C26` | `=E2*C24` |
| `D26` | `=E2*D24` |
| `E26` | `=E2*E24` |
| `C27` | `=C26/D7` |
| `D27` | `=D26/D7` |
| `E27` | `=E26/D7` |
| `B28` | `=C26*I10` |
| `C28` | `=C27*H10` |
| `D28` | `=D27*H10` |
| `E28` | `=E27*H10` |
| `B29` | `=B28*D6` |
| `C29` | `=C28*D6` |
| `D29` | `=D28*D6` |
| `E29` | `=E28*D6` |

### 4. 1. Canteiro

- Faixa usada: `A1:N33`
- Fórmulas: **46**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **140**

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
- Tanque de equalizaçao
- vb
- Preços VALE Vitória
- Painel eletrico
- Mesa escritório
- Eletricista
- mes
- mesa redonda
- cadeira
- armário escritório
- cestos lixo
- armário vestiário
- material de escritório
- Bebedouro
- Banheiro Quimico
- cliente
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
| `D14` | `='Dados Obra '!M9` |
| `F14` | `=D14*E14` |
| `D17` | `=D16` |
| `E18` | `=(60000/60)*D14` |
| `E19` | `=(150000/60)*D14` |
| `F19` | `=D19*E19` |
| `K19` | `=I19*J19` |
| `D20` | `=D14` |
| `F20` | `=D20*E20` |
| `D25` | `=D14` |
| `K26` | `=SUM(K19:K25)` |
| `F27` | `=D27*E27` |
| `E28` | `=F11` |
| `F29` | `=SUM(F14:F28)` |
| `F30` | `='Dados Obra '!M9` |
| `F31` | `=F29/F30` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |

### 5. 2.1 Mob Draga

- Faixa usada: `A1:M42`
- Fórmulas: **52**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **132**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 6" e DRAGA ELETRICA OU MIUDA
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
- usar tenda já possuímos
- Bebedouro
- custo Exames médicos
- Carreta Tanque Equalização
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
| `M5` | `=SUM(I5:L5)` |
| `A6` | `=M6` |
| `C6` | `='1. Canteiro'!C5` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `M6` | `=I6+J6` |
| `A7` | `=M9` |
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='1. Canteiro'!C7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=M10` |
| `C9` | `='1. Canteiro'!M12` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `J9` | `='1. Canteiro'!J9` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=SUM(A5:A9)` |
| `C10` | `='1. Canteiro'!C9` |
| `F10` | `=A10*C10` |
| `I10` | `='1. Canteiro'!I10` |
| `J10` | `='1. Canteiro'!J10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=A10` |
| `C11` | `='1. Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F5:F11)` |
| `M12` | `=SUM(I12:L12)` |
| `M13` | `=SUM(I13:L13)` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `D17` | `=C42` |
| `F17` | `=D17*E17` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `F25` | `=D25*E25` |
| `D30` | `=A11` |
| `F30` | `=D30*E30` |
| `E31` | `=E17` |
| `F31` | `=D31*E31` |
| `E32` | `=E17` |
| `F32` | `=D32*E32` |
| `E33` | `=F12` |
| `F34` | `=SUM(F15:F33)` |
| `F35` | `=F34*(E35/100)` |
| `F36` | `=SUM(F34:F35)` |
| `C42` | `=SUM(C38:C41)` |

### 6. 4.1 Draga Dec

- Faixa usada: `A1:L206`
- Fórmulas: **95**
- Conceitos provisórios: outros
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `='Produção (NOVO CALCULO)'!J10` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=(C9*D9*E9*L12)*0.1` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `K20` | `='Dados Obra '!B28` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `D21` | `='1. Canteiro'!C4` |
| `L21` | `=J21*K21` |
| `A22` | `=K33` |
| `D22` | `='1. Canteiro'!C6` |
| `A23` | `=A22` |
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
| `B109` | `=B52+B53` |
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
| `E146` | `=F7*0.01` |
| `E149` | `=E145+E146+E147` |
| `D168` | `=G134` |
| `D171` | `=E142` |
| `D173` | `=E149` |
| `D175` | `=D168+D171+D173` |
| `D178` | `=#REF!` |
| `D184` | `=D180+D182` |
| `D187` | `=J206*0.6*0.62` |
| `H188` | `=#REF!` |
| `I188` | `=#REF!` |
| `J188` | `=H188*I188` |
| `D197` | `=D175` |
| `D199` | `=SUM(D197:D198)` |
| `J200` | `=D199` |
| `D201` | `=D199*D200` |
| `J202` | `=J200*J201` |
| `J203` | `='Produção (NOVO CALCULO)'!J10` |
| `J206` | `=(J202/J203)*J204` |

### 7. Tq Equal.

- Faixa usada: `A1:N33`
- Fórmulas: **44**
- Conceitos provisórios: outros
- Células numéricas observadas: **135**

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
- Tanque de equalizaçao
- Preços VALE Vitória
- Painel eletrico
- vb
- Mesa escritório
- mesa redonda
- Mangote Flexível para Tanque Equaliz.
- m
- cadeira
- Abraçadeiras para mangueira
- armário escritório
- Verba de adaptação (peneira e sensor)
- cestos lixo
- armário vestiário
- material de escritório
- Bebedouro
- Banheiro Quimico
- mes
- Mão de obra
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
| `D18` | `='1. Canteiro'!D14` |
| `E18` | `=(60000/24)` |
| `D19` | `=D18` |
| `E19` | `=(60000/24)` |
| `K19` | `=I19*J19` |
| `F20` | `=D20*E20` |
| `D25` | `=D14` |
| `D26` | `=D25` |
| `K26` | `=SUM(K19:K25)` |
| `E28` | `=F11` |
| `F29` | `=SUM(F14:F28)` |
| `F30` | `='Dados Obra '!M9` |
| `F31` | `=F29/F30` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |

### 8. Venda Draga

- Faixa usada: `A1:L26`
- Fórmulas: **26**
- Conceitos provisórios: outros
- Células numéricas observadas: **48**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Técnico de Segurança
- Operador de Draga
- Operador de Centrífuga
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
- Custo da Draga Elétrica
- Valor Estimado para fabricar uma draga igual
- vb
- Flututante Maximus
- Inversor
- Valor de uma Draga 6" da ARVEN
- Painel
- Bomba de 6" Schinneider
- Guincho Elétrico
- Sarrilhos e outros
- TOTAL
- Prazo de Operação
- preço unitário
- #DIV/0!
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `D5` | `=D4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='1. Canteiro'!A6` |
| `C6` | `='1. Canteiro'!C6` |
| `D6` | `=D4` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `='1. Canteiro'!A8` |
| `C8` | `='1. Canteiro'!C8` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=SUM(A4:A8)` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F4:F10)` |
| `E14` | `=L20` |
| `F14` | `=D14*E14` |
| `F20` | `=D20*E20` |
| `L20` | `=SUM(L14:L19)` |
| `E21` | `=F11` |
| `F22` | `=SUM(F14:F21)` |
| `F24` | `=F22/F23` |
| `F25` | `=F24*(E25/100)` |
| `F26` | `=F24+F25` |

### 9. Draga MDO

- Faixa usada: `A1:L206`
- Fórmulas: **96**
- Conceitos provisórios: mao_obra
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F7` | `='4.1 Draga Dec'!F7` |
| `C9` | `='Produção (NOVO CALCULO)'!J10` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=(C9*D9*E9*L12)*0.1` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `K20` | `='Dados Obra '!B28` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `D21` | `='1. Canteiro'!C4` |
| `L21` | `=J21*K21` |
| `A22` | `=K33` |
| `D22` | `='1. Canteiro'!C6` |
| `A23` | `=A22` |
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
| `C59` | `='4.1 Draga Dec'!C59` |
| `D59` | `='4.1 Draga Dec'!D59` |
| `E62` | `=C59+C60+C61+C62` |
| `B69` | `=B52` |
| `E69` | `=D69*B69` |
| `E71` | `=SUM(E67:E69)` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E92` | `=(0.6/100)*F7` |
| `E97` | `=E92+E93+E94+E95` |
| `H99` | `=E97` |
| `E103` | `=K120` |
| `I104` | `='Dados Obra '!H17` |
| `K104` | `=I104*J104` |
| `J105` | `=K104/I105` |
| `J106` | `=K104*(1/100)` |
| `E107` | `=B107*D107` |
| `J107` | `=SUM(J105:J106)` |
| `B109` | `=B52+B53` |
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
| `E149` | `=E145+E146+E147` |
| `D168` | `=G134` |
| `D171` | `=E142` |
| `D173` | `=E149` |
| `D175` | `=D168+D171+D173` |
| `D178` | `=#REF!` |
| `D184` | `=D180+D182` |
| `D187` | `=J206*0.6*0.62` |
| `H188` | `=#REF!` |
| `I188` | `=#REF!` |
| `J188` | `=H188*I188` |
| `D197` | `=D175` |
| `D199` | `=SUM(D197:D198)` |
| `D200` | `='Dados Obra '!M9-'4.1 Draga Dec'!D200` |
| `J200` | `=D199` |
| `D201` | `=D199*D200` |
| `J202` | `=J200*J201` |
| `J203` | `='Produção (NOVO CALCULO)'!J10` |
| `J206` | `=(J202/J203)*J204` |

### 10. Desmob Draga

- Faixa usada: `A1:M43`
- Fórmulas: **57**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **127**

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
- Carreta Tanque Equalização
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
| `A5` | `='2.1 Mob Draga'!A5` |
| `C5` | `='1. Canteiro'!C4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `M5` | `=SUM(I5:L5)` |
| `C6` | `='1. Canteiro'!C5` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `='2.1 Mob Draga'!A7` |
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='1. Canteiro'!C7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `='2.1 Mob Draga'!A9` |
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
| `D18` | `='2.1 Mob Draga'!D17` |
| `E18` | `='2.1 Mob Draga'!E17` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `E22` | `='2.1 Mob Draga'!E21` |
| `F22` | `=D22*E22` |
| `D31` | `=A11` |
| `F31` | `=D31*E31` |
| `D32` | `='2.1 Mob Draga'!D31` |
| `E32` | `='2.1 Mob Draga'!E31` |
| `F32` | `=D32*E32` |
| `E33` | `=E18` |
| `F33` | `=D33*E33` |
| `E34` | `=F12` |
| `F35` | `=SUM(F15:F34)` |
| `F36` | `=F35*(E36/100)` |
| `F37` | `=SUM(F35:F36)` |
| `C43` | `=SUM(C39:C42)` |

### 11. Plan. Final

- Faixa usada: `A1:L18`
- Fórmulas: **34**
- Conceitos provisórios: outros
- Células numéricas observadas: **49**

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
- Dragagem (Draga + Mão de obra)
- mês
- Dragagem (Só Mão de obra)
- Tanue de Equalização
- Venda da Draga
- Draga Elétrica
- Desmobilização Draga
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='2.1 Mob Draga'!F36` |
| `G4` | `=C4/E4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `L4` | `=SUM(J4:J4)` |
| `C7` | `='4.1 Draga Dec'!D201` |
| `G7` | `=C7/E7` |
| `I7` | `=((H7/100)+1)*G7` |
| `J7` | `=E7*I7` |
| `L7` | `=SUM(I7:I7)` |
| `C8` | `='Draga MDO'!D201` |
| `E8` | `='Dados Obra '!M9-E7` |
| `G8` | `=C8/E8` |
| `I8` | `=((H8/100)+1)*G8` |
| `J8` | `=E8*I8` |
| `L8` | `=SUM(I8:I8)` |
| `C9` | `='Tq Equal.'!F29` |
| `E9` | `='Dados Obra '!M9` |
| `G9` | `=C9/E9` |
| `I9` | `=((H9/100)+1)*G9` |
| `J9` | `=E9*I9` |
| `L9` | `=SUM(I9:I9)` |
| `C12` | `='Venda Draga'!F22` |
| `G12` | `=C12/E12` |
| `I12` | `=((H12/100)+1)*G12` |
| `J12` | `=E12*I12` |
| `L12` | `=SUM(I12:I12)` |
| `C14` | `='Desmob Draga'!F37` |
| `G14` | `=C14/E14` |
| `I14` | `=((H14/100)+1)*G14` |
| `L14` | `=SUM(J14:J14)` |
| `C16` | `=SUM(C4:C15)` |
| `J16` | `=SUM(J4:J15)` |
| `J18` | `=J16/E7` |

### 12. Final

- Faixa usada: `A1:M12`
- Fórmulas: **34**
- Conceitos provisórios: outros
- Células numéricas observadas: **61**

#### Rótulos e textos observados

- ITEM
- DESCRIÇÃO DOS SERVIÇOS
- UN
- QUANT
- PREÇO UNIT
- PREÇO TOTAL
- REV.3 com desc. Possíveis
- REV.2
- SEM VENDER A DRAGA SERIA
- Mobilização e Montagem dos Equipamentos
- vb
- Operação de Dragagem, incluindo fornecimento de Draga e mão de obra de operação
- mês
- Mão de obra para Operação de Draga
- Locação de Tanque de Equalização
- Venda de Draga flutuante de sucção e recalque com vazão nominal de 300 m³/h
- Desmobilização e Desmontagem dos Equipamentos
- VALOR TOTAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D3` | `='[1]Plan. Final'!E4` |
| `F3` | `=D3*E3` |
| `H3` | `='Plan. Final'!I4` |
| `K3` | `=D3` |
| `L3` | `=E3` |
| `M3` | `=K3*L3` |
| `D4` | `='Plan. Final'!E7` |
| `F4` | `=D4*E4` |
| `H4` | `='Plan. Final'!I7` |
| `K4` | `=D4+D5` |
| `L4` | `=E4` |
| `M4` | `=K4*L4` |
| `D5` | `='Plan. Final'!E8` |
| `F5` | `=D5*E5` |
| `H5` | `='Plan. Final'!I8` |
| `D6` | `='Plan. Final'!E9` |
| `F6` | `=D6*E6` |
| `H6` | `='Plan. Final'!I9` |
| `K6` | `=D6` |
| `L6` | `=E6` |
| `F7` | `=D7*E7` |
| `H7` | `='Plan. Final'!I12` |
| `D8` | `='[1]Plan. Final'!E11` |
| `F8` | `=D8*E8` |
| `H8` | `='Plan. Final'!I14` |
| `K8` | `=D8` |
| `L8` | `=E8` |
| `F9` | `=SUM(F3:F8)` |
| `M9` | `=SUM(M3:M8)` |
| `F10` | `=1-(F9/I9)` |
| `H10` | `=1-(H9/I9)` |
| `M11` | `=F9-M9` |
| `E12` | `=E4-E5` |
| `H12` | `=H9-F9` |

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
