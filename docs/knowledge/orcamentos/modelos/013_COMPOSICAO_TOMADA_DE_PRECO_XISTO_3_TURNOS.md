# Modelo 013 — Composição Tomada de preço - Xisto - 3 turnos.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `Composição Tomada de preço - Xisto - 3 turnos.xlsx`
- Família provisória: **Dragagem com centrífuga**
- SHA-256 do arquivo: `a60a510f9fb8c3a757f4c9e5f2501f28839a79470c8174a53fd192852a6f9309`
- Abas analisadas: **15**
- Fórmulas encontradas: **577**

## Conceitos identificados

- `outros`: 5 aba(s)
- `desmobilizacao`: 3 aba(s)
- `canteiro`: 2 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `operacao_desaguamento`: 2 aba(s)
- `carga_transporte_destinacao`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:S28` | 14 | dados_obra |
| 2 | `Fornecedores` | `A1:F15` | 1 | outros |
| 3 | `Historico - PALOTINA` | `A1:D10` | 1 | outros |
| 4 | `Produção (NOVO CALCULO)` | `A1:S43` | 38 | producao_prazo |
| 5 | `1. Canteiro` | `A1:N33` | 49 | canteiro |
| 6 | `2.1 Mob Draga` | `A1:M42` | 49 | mobilizacao_draga |
| 7 | `2.2 Mob Centr` | `A1:M42` | 49 | outros |
| 8 | `4.1 Draga Dec` | `A1:L206` | 95 | outros |
| 9 | `4.2 Centrífuga` | `A1:R205` | 92 | operacao_desaguamento |
| 10 | `Op. Centrifuga` | `A1:G19` | 4 | operacao_desaguamento |
| 11 | `Transp e Destinacao` | `A1:H19` | 2 | carga_transporte_destinacao |
| 12 | `5. Desmob Canteiro` | `A1:N33` | 38 | canteiro, desmobilizacao |
| 13 | `Desmob Draga` | `A1:M43` | 54 | mobilizacao_draga, desmobilizacao |
| 14 | `Desmob Centr` | `A1:M42` | 46 | desmobilizacao |
| 15 | `Plan. Final` | `A1:O31` | 45 | outros |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `1. Canteiro` | 59 |
| `Dados Obra` | 13 |
| `4.1 Draga Dec` | 4 |
| `Produção (NOVO CALCULO)` | 3 |
| `2.1 Mob Draga` | 2 |
| `Op. Centrifuga` | 2 |
| `2.2 Mob Centr` | 1 |
| `4.2 Centrífuga` | 1 |
| `Desmob Centr` | 1 |
| `Desmob Draga` | 1 |
| `Transp e Destinacao` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:S28`
- Fórmulas: **14**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **30**

#### Rótulos e textos observados

- SANEPAR / XISTO
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
- % SS desaguado
- Cliente
- SANEPAR
- Volume Estimado a Dragar
- m³/mês
- Contato
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
| `O5` | `=(M10*M6)/M7` |
| `M8` | `=(M5*M7)/M6` |
| `P9` | `=M10*M6` |
| `M10` | `=M8*M9` |
| `L13` | `=M10` |
| `O13` | `=M13+N13` |
| `Q13` | `=L13*P13` |
| `S13` | `=Q13/R13` |
| `B15` | `=L13` |
| `Q16` | `=SUM(Q13:Q15)` |
| `S16` | `=SUM(S13:S15)` |
| `H17` | `=B17+E17` |
| `H18` | `=B18+E18` |
| `G22` | `=B22*D22*B21` |

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

### 3. Historico - PALOTINA

- Faixa usada: `A1:D10`
- Fórmulas: **1**
- Conceitos provisórios: outros
- Células numéricas observadas: **11**

#### Rótulos e textos observados

- PALOTINA
- Percentua Médio de Desaguamento
- CONCLUSÃO : Média dos percentuais (% ST determinados pela SANEPAR) = 22,04%

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `B10` | `=AVERAGE(B5:B9)` |

### 4. Produção (NOVO CALCULO)

- Faixa usada: `A1:S43`
- Fórmulas: **38**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **63**

#### Rótulos e textos observados

- x1 Centrigufa
- Se na lagoa 8%
- M3/h
- m3/h
- Bombeamento 20% material
- 20 metros de skid - centrifuga de 60M3/h
- 20% de 8%
- DIAS
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
- REGIME DE 16 HORAS (2 turno)
- Ton Desaguada Hora
- Ton Desaguada Dia
- Ton Desaguada Mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `E2` | `=C2*1` |
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
| `E16` | `=E14-E15` |
| `F16` | `=F14-F15` |
| `C26` | `=E2*C24` |
| `D26` | `=E2*D24` |
| `E26` | `=E2*E24` |
| `C27` | `=C26/D7` |
| `D27` | `=D26/D7` |
| `E27` | `=E26/D7` |
| `C28` | `=C27*H10` |
| `D28` | `=D27*H10` |
| `E28` | `=E27*H10` |
| `C29` | `=C28*D6` |
| `D29` | `=D28*D6` |
| `E29` | `=E28*D6` |
| `C40` | `=E2*C38` |
| `D40` | `=E2*D38` |
| `E40` | `=E38*E2` |
| `C41` | `=C40/D7` |
| `D41` | `=D40/D7` |
| `E41` | `=E40/D7` |
| `C42` | `=C41*I13` |
| `D42` | `=D41*I13` |
| `E42` | `=E41*I13` |
| `C43` | `=C42*D6` |
| `D43` | `=D42*D6` |
| `E43` | `=E42*D6` |

### 5. 1. Canteiro

- Faixa usada: `A1:N33`
- Fórmulas: **49**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **132**

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
| `A8` | `=L12+L10` |
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
| `F30` | `='Dados Obra '!M9` |
| `F31` | `=F29/F30` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |

### 6. 2.1 Mob Draga

- Faixa usada: `A1:M42`
- Fórmulas: **49**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **131**

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
- Carreta Carga Seca para DRAGA
- un
- Fabiano zap em 16/04/25 R$ 6.200 + 0,2% adv
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
- Locup - 5k (Tenda 3x3)
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
| `C6` | `='1. Canteiro'!C5` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='1. Canteiro'!C7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `C9` | `='1. Canteiro'!C8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `I9` | `='1. Canteiro'!I9` |
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
| `F31` | `=D31*E31` |
| `E32` | `=E17` |
| `F32` | `=D32*E32` |
| `E33` | `=F12` |
| `F34` | `=SUM(F15:F33)` |
| `F35` | `=F34*(E35/100)` |
| `F36` | `=SUM(F34:F35)` |
| `C42` | `=SUM(C38:C41)` |

### 7. 2.2 Mob Centr

- Faixa usada: `A1:M42`
- Fórmulas: **49**
- Conceitos provisórios: outros
- Células numéricas observadas: **122**

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
- Fabiano zap em 16/04/25 R$ 6.200 + 0,2% adv
- Guindaste p/descarregamento e montagem DRAGA
- FOS
- Plano de Rigger
- vb
- Mob guindaste
- Munck para descarregamento dos Containeres
- Criaçao de Base de concreto
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
| `A5` | `=M5` |
| `C5` | `='1. Canteiro'!C4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `='1. Canteiro'!I7` |
| `M5` | `=SUM(I5:L5)` |
| `C6` | `='1. Canteiro'!C5` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
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
| `D32` | `=C42` |
| `E32` | `=E18` |
| `F32` | `=D32*E32` |
| `E33` | `=F12` |
| `F34` | `=SUM(F15:F33)` |
| `F35` | `=F34*(E35/100)` |
| `F36` | `=SUM(F34:F35)` |
| `C42` | `=SUM(C38:C41)` |

### 8. 4.1 Draga Dec

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
| `B21` | `='2.1 Mob Draga'!M5` |
| `D21` | `='1. Canteiro'!C4` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `D22` | `='1. Canteiro'!C6` |
| `A23` | `=L24` |
| `D23` | `='1. Canteiro'!C8` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
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
| `D200` | `='Dados Obra '!M9` |
| `J200` | `=D199` |
| `D201` | `=D199*D200` |
| `J202` | `=J200*J201` |
| `J203` | `='Produção (NOVO CALCULO)'!J10` |
| `J206` | `=(J202/J203)*J204` |

### 9. 4.2 Centrífuga

- Faixa usada: `A1:R205`
- Fórmulas: **92**
- Conceitos provisórios: operacao_desaguamento
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
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
| `D23` | `='1. Canteiro'!C8` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
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
| `E145` | `=F7/60` |
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
| `J202` | `='Produção (NOVO CALCULO)'!J10` |
| `J205` | `=(J201/J202)*J203` |

### 10. Op. Centrifuga

- Faixa usada: `A1:G19`
- Fórmulas: **4**
- Conceitos provisórios: operacao_desaguamento
- Células numéricas observadas: **29**

#### Rótulos e textos observados

- Operação Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Consumo Polimero
- kg
- Assumindo consumo de 13 kg / ton
- Frete Polimero
- un
- mês
- material de escritório
- Banheiro Quimico
- mes
- TOTAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `=13*'Dados Obra '!Q13` |
| `F5` | `=D5*E5` |
| `D6` | `=ROUNDUP(D5/2000,0)` |
| `F19` | `=SUM(F5:F18)` |

### 11. Transp e Destinacao

- Faixa usada: `A1:H19`
- Fórmulas: **2**
- Conceitos provisórios: carga_transporte_destinacao
- Células numéricas observadas: **25**

#### Rótulos e textos observados

- Transporte e Destinaçao
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Internaçao de Material
- m3
- Parana Ambiental
- Essensys cobrou 980 reais / ton
- Transporte
- Sendo que a densidade do lodo da torta de merda é de 1,06
- TOTAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F5` | `=D5*E5` |
| `F19` | `=SUM(F5:F18)` |

### 12. 5. Desmob Canteiro

- Faixa usada: `A1:N33`
- Fórmulas: **38**
- Conceitos provisórios: canteiro, desmobilizacao
- Células numéricas observadas: **121**

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
- #REF!
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
| `F30` | `=#REF!` |
| `F31` | `=F29/F30` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |

### 13. Desmob Draga

- Faixa usada: `A1:M43`
- Fórmulas: **54**
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
- Fabiano zap em 16/04/25 R$ 6.200 + 0,2% adv
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
| `C6` | `='1. Canteiro'!C5` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=M9` |
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='1. Canteiro'!C7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=M10` |
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

### 14. Desmob Centr

- Faixa usada: `A1:M42`
- Fórmulas: **46**
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
- Fabiano zap em 16/04/25 R$ 6.200 + 0,2% adv
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
| `C7` | `='1. Canteiro'!C6` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=M12` |
| `C8` | `='1. Canteiro'!C7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=M13` |
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
| `F32` | `=D32*E32` |
| `E33` | `=F12` |
| `F34` | `=SUM(F15:F33)` |
| `F35` | `=F34*(E35/100)` |
| `F36` | `=SUM(F34:F35)` |
| `C42` | `=SUM(C38:C41)` |

### 15. Plan. Final

- Faixa usada: `A1:O31`
- Fórmulas: **45**
- Conceitos provisórios: outros
- Células numéricas observadas: **64**

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
- Mobilização Centrifuga
- m3
- volume desaguado (15%)
- Dragagem e desaguamento Centrífuga
- 4.1
- Dragagem
- ton
- 4.2
- Operação Centrífuga
- Fornecimento Polimero
- kg
- Desmobilização Draga
- DesMobilização Centrífuga
- Preço de Venda
- Transporte e Destinaçao Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='2.1 Mob Draga'!F36` |
| `G4` | `=C4/E4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `L4` | `=SUM(J4:J5)` |
| `C5` | `='2.2 Mob Centr'!F36` |
| `G5` | `=C5/E5` |
| `I5` | `=((H5/100)+1)*G5` |
| `J5` | `=E5*I5` |
| `O7` | `='Dados Obra '!O5` |
| `C8` | `='4.1 Draga Dec'!D201` |
| `E8` | `='Dados Obra '!P9` |
| `G8` | `=C8/E8` |
| `I8` | `=((H8/100)+1)*G8` |
| `J8` | `=E8*I8` |
| `L8` | `=SUM(I8:I9)` |
| `N8` | `=SUM(J8:J9)/N7` |
| `O8` | `=(SUM(J8:J9))/O7` |
| `C9` | `='4.2 Centrífuga'!D199` |
| `E9` | `=E8` |
| `G9` | `=C9/E9` |
| `I9` | `=((H9/100)+1)*G9` |
| `J9` | `=E9*I9` |
| `C10` | `='Op. Centrifuga'!F19` |
| `E10` | `='Op. Centrifuga'!D5` |
| `G10` | `=C10/E10` |
| `I10` | `=((H10/100)+1)*G10` |
| `J10` | `=E10*I10` |
| `C11` | `='Desmob Draga'!F37` |
| `G11` | `=C11/E11` |
| `I11` | `=((H11/100)+1)*G11` |
| `L11` | `=SUM(J11:J12)` |
| `C12` | `='Desmob Centr'!F36` |
| `G12` | `=C12/E12` |
| `I12` | `=((H12/100)+1)*G12` |
| `C14` | `=SUM(C4:C13)` |
| `J14` | `=SUM(J4:J13)` |
| `J16` | `=J14/E8` |
| `C21` | `='Transp e Destinacao'!F19` |
| `G21` | `=C21/E21` |
| `I21` | `=((H21/100)+1)*G21` |
| `J21` | `=E21*I21` |
| `C23` | `=SUM(C21:C22)` |
| `J23` | `=SUM(J21:J22)` |
| `J31` | `=J23+J14` |

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
