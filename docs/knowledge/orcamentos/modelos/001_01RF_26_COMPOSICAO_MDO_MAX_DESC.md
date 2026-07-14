# Modelo 001 — 01RF_26 - composição MDO - máx. desc..xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `01RF_26 - composição MDO - máx. desc..xlsx`
- Família provisória: **Composição de mão de obra**
- SHA-256 do arquivo: `8a3d7333e39d4c9b61e6aeb31dca54273af48082f08959b1a76e0b3f2043ad42`
- Abas analisadas: **12**
- Fórmulas encontradas: **676**

## Conceitos identificados

- `outros`: 5 aba(s)
- `mobilizacao_sistema`: 2 aba(s)
- `operacao_desaguamento`: 2 aba(s)
- `dados_obra`: 1 aba(s)
- `desmobilizacao`: 1 aba(s)
- `mao_obra`: 1 aba(s)
- `mobilizacao_draga`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:Q35` | 19 | dados_obra |
| 2 | `Produção` | `A1:K21` | 19 | producao_prazo |
| 3 | `1. Cant. e Mob Equipe` | `A1:N45` | 72 | mobilizacao_sistema, mao_obra |
| 4 | `Mob. Draga` | `A1:M29` | 54 | mobilizacao_draga |
| 5 | `Mob Centrífuga` | `A1:N34` | 64 | mobilizacao_sistema, operacao_desaguamento |
| 6 | `Operação` | `A1:N34` | 61 | outros |
| 7 | `2.1. Draga Dec` | `A1:L206` | 103 | outros |
| 8 | `2.2 Centrífuga` | `A1:L205` | 103 | operacao_desaguamento |
| 9 | `2.3. manutenção` | `A1:H26` | 44 | outros |
| 10 | `3. Desmob.` | `A1:N45` | 66 | desmobilizacao |
| 11 | `Plan. Final` | `A1:L30` | 44 | outros |
| 12 | `Final` | `A1:AC8` | 27 | outros |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `1. Cant. e Mob Equipe` | 66 |
| `Dados Obra` | 22 |
| `2.1. Draga Dec` | 14 |
| `Mob. Draga` | 6 |
| `Plan. Final` | 6 |
| `2.2 Centrífuga` | 4 |
| `Mob Centrífuga` | 2 |
| `2.3. manutenção` | 1 |
| `3. Desmob.` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:Q35`
- Fórmulas: **19**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **43**

#### Rótulos e textos observados

- SUZANO - ARACRUZ
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- MÁXIMO DESCONTO
- Proposta
- Proposta D_01R3_2026
- Data
- DADOS DA OBRA
- QUANT
- HORAS /DIA
- Cliente
- SUZANO
- DRAGA
- x 1 Turno
- Contato
- Robson / Thamires
- e-mail
- CENTRÍFUGA
- x 2 Turnos
- Jornada (dias)
- 2ª feira a sábado
- Dados da obra
- Prazo
- meses
- Objeto
- Operação da ETE Aracruz
- Eficiência Produtiva
- Local
- Aracruz - ES
- Vazão da Centrífuga
- m³/h
- Volume dragagem (m³)
- % Entrada
- %
- Tipo de material
- Lodo de ETE
- Horas Produtivas
- h
- Distância de Recalque (m)
- Seio da linha =
- Total
- Produção Ton SS / dia
- Ton SS/dia
- Linha Flutuante (m)
- Produção Ton SS / mês
- Ton SS/mês
- Linha de terra (m)
- Profundidade de dragagem (m)
- % MÉDIO de ST desag
- Espessura média de dragagem (m)
- % MÉDIO de ST in situ
- Área de Dragagem (m² ou L x C)
- X
- Volume (m³) =
- Tipo de Bota Fora
- Volume Lodo desag
- m³/mês
- Sistema de Medição
- preços unitários de serviços
- Volume Lodo DRAGADO
- Canteiro de obras
- FOS
- Mobilização
- Volume Total a Dragar
- m³
- Horário de Trabalho (das 7 as 23h)
- h/dia
- 2 turnos de 8 horas cada
- Dias de Trabalho (2ª a sábado)
- dias/mês
- TQ Equalização
- m3
- Vazão nominal da Draga
- Quant. Total
- Tempo para encher o TQ Eq.
- horas

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `M8` | `=B26` |
| `B14` | `=L25` |
| `L15` | `=M8*K12` |
| `H16` | `=B16+E16` |
| `L16` | `=L13*L14*L15` |
| `H17` | `=B17+E17` |
| `L17` | `=L16*M10` |
| `G21` | `=B21*D21*B20` |
| `L22` | `=L17/L19` |
| `L23` | `=(L22*L19)/L20` |
| `L25` | `=L23*K11` |
| `L29` | `=L27/L28` |
| `P30` | `=K11` |
| `L31` | `=L17*K11` |
| `N31` | `=N29*N30` |
| `P31` | `=P29*P30` |
| `L33` | `=L30` |
| `L34` | `=M7*K12` |
| `L35` | `=L33*L34` |

### 2. Produção

- Faixa usada: `A1:K21`
- Fórmulas: **19**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **23**

#### Rótulos e textos observados

- PRODUÇÃO CENTRÍFUGA
- Horas Trabalhadas por mês
- Unid.
- Quant.
- Vazão
- m³/h
- Horário de Trabalho (das 7 as 23h)
- Eficiência
- %
- Dias de Trabalho (2ª a sábado)
- Concentração
- Total de Horas / mês
- Volume processado
- % SS entrada Centrífuga
- Ton SS / h
- Vazão Nominal Centrífuga =
- Horas trabalhadas
- h/mês
- Eficiência operacional
- Vazão Operacional =
- (Estimativa experiência FOS)
- Produção mensal
- ton/mês
- Cálculo do Prazo da obra
- Meses
- Mobilização
- QUANTIDADE TOTAL
- Ton SS
- Operação
- desmob
- Prazo Operação
- meses
- Total

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D3` | `='Dados Obra '!L13` |
| `F3` | `='Dados Obra '!A26` |
| `H3` | `='Dados Obra '!B26` |
| `F4` | `='Dados Obra '!A27` |
| `H4` | `='Dados Obra '!B27` |
| `H6` | `=H3*H4` |
| `D7` | `=D3*D4*D5` |
| `D8` | `='Dados Obra '!L14` |
| `D10` | `=D3*D8` |
| `H10` | `='Dados Obra '!L13` |
| `D11` | `=H6*D4` |
| `H12` | `=H10*H11` |
| `D13` | `=D10*D11` |
| `K16` | `=H3*D10` |
| `D18` | `=D13*G19` |
| `G19` | `='Dados Obra '!K11` |
| `D21` | `=ROUNDUP(D18/D13,0)` |
| `E21` | `=D18/D13` |
| `G21` | `=SUM(G17:G20)` |

### 3. 1. Cant. e Mob Equipe

- Faixa usada: `A1:N45`
- Fórmulas: **72**
- Conceitos provisórios: mobilizacao_sistema, mao_obra
- Células numéricas observadas: **201**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS e MOBILIZAÇÃO EQUIPE
- Nº Func.
- Mão de obra
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Mão de OBRA
- TURNOS
- Líder de Operação
- Técnico de Segurança
- 1º
- 2º
- Salário
- com 25%
- Operador de Draga
- Operador de Centrífuga
- Líder Operação
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
- locmeq
- Container Sanitário/Vestiário
- Na Draga
- pessoas por turno
- Container Escritório
- Na Planta
- Frete para Containers
- vb
- Mobiliário Canteiro
- Mobiliário Alojamento
- PGR + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- itens de segurança
- Tenda do Canteiro
- Bebedouro elétrico
- material de escritório
- #NAME?
- custo Exames médicos
- un
- Viagem da equipe IDA
- Hospedagem
- Almoço
- jantar
- café
- Hospedagem EQUIPE
- dia
- Uilson
- Alimentação EQUIPE
- Pedro Paulo
- Veículo para uso na obra
- Uildes
- Viagem AGUINALDO ida e volta
- Paulo Araújo
- Veículo para Aguinaldo
- Hospedagem AGUINALDO
- Aguinaldo
- Alimentação AGUINALDO
- Mão de obra (integração)
- lançar docs no sistema após contratação + 1 dia integração + 2 dias aprovação + 2 dias pra entrar + 5 dias exames
- TOTAL
- Prazo de Operação
- preço unitário
- Viagem
- Uber 1

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `=L7` |
| `C4` | `=N7` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `A5` | `=L8` |
| `C5` | `=N8` |
| `D5` | `=D4` |
| `A6` | `=L9` |
| `C6` | `=(M9*N2)+M9` |
| `D6` | `=D4` |
| `A7` | `=L10` |
| `C7` | `=(N10*N2)+N10` |
| `D7` | `=D4` |
| `L7` | `=I7+J7+K7` |
| `N7` | `=M7*1.25` |
| `A8` | `=L12` |
| `C8` | `=N12` |
| `D8` | `=D7` |
| `L8` | `=I8+J8+K8` |
| `N8` | `=M8*1.25` |
| `A9` | `=L11+L13` |
| `C9` | `=(M13*N2)+M13` |
| `L9` | `=I9+J9+K9` |
| `A10` | `=SUM(A4:A9)` |
| `F10` | `=A10*C10` |
| `N10` | `=M10*1.25` |
| `A11` | `=A10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F4:F11)` |
| `N12` | `=M12*1.25` |
| `I14` | `=SUM(I7:I13)` |
| `J14` | `=SUM(J7:J13)` |
| `K14` | `=SUM(K8:K13)` |
| `L14` | `=SUM(I14:K14)` |
| `D16` | `=D15` |
| `D17` | `=D15` |
| `F17` | `=D17*E17` |
| `E20` | `=E19` |
| `F20` | `=D20*E20` |
| `D26` | `=Produção!G19` |
| `D27` | `=A10` |
| `F27` | `=D27*E27` |
| `E28` | `=N44` |
| `E29` | `=I33` |
| `F29` | `=D29*E29` |
| `D30` | `=D29` |
| `E30` | `=K33+L33` |
| `F30` | `=D30*E30` |
| `F31` | `=D31*E31` |
| `E32` | `=N45` |
| `F32` | `=D32*E32` |
| `F33` | `=D33*E33` |
| `I33` | `=SUM(I29:I32)` |
| `J33` | `=SUM(J29:J32)` |
| `K33` | `=SUM(K29:K32)` |
| `L33` | `=SUM(L29:L32)` |
| `D34` | `=D33` |
| `E34` | `=I34` |
| `F34` | `=D34*E34` |
| `D35` | `=D34` |
| `E35` | `=J34+K34` |
| `F35` | `=D35*E35` |
| `D36` | `=10+0` |
| `E36` | `=F12` |
| `F37` | `=SUM(F15:F36)` |
| `F38` | `=Produção!G19` |
| `F39` | `=F37/F38` |
| `F40` | `=F39*(E40/100)` |
| `N40` | `=SUM(I40:M40)` |
| `F41` | `=F39+F40` |
| `N41` | `=SUM(I41:M41)` |
| `N44` | `=SUM(N40:N43)` |
| `N45` | `=SUM(I45:M45)` |

### 4. Mob. Draga

- Faixa usada: `A1:M29`
- Fórmulas: **54**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **86**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 6" hidráulica
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
- #NAME?
- Estimativa
- Carreta Carga Seca para DRAGA
- un
- Fabiano zap em 24/11/23 R$ 14.500 + 0,2% adv (mantido em 16/01/24)
- Guindaste p/descarregamento e montagem DRAGA
- Repassado para Cliente
- Transferência da Draga entre lagoas
- Viagem de ida
- Mão de obra p MOBILIZAÇÃO (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- Carreta 1 (draga)
- Carreta 2 (Tubulação 700 m)
- Carreta 3 (flutuantes e outros periféricos)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A5` | `=M5` |
| `C5` | `='1. Cant. e Mob Equipe'!C4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `='1. Cant. e Mob Equipe'!I8` |
| `M5` | `=SUM(I5:L5)` |
| `A6` | `=M6` |
| `C6` | `='1. Cant. e Mob Equipe'!C6` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `I6` | `='1. Cant. e Mob Equipe'!I9` |
| `A7` | `=M8` |
| `C7` | `='1. Cant. e Mob Equipe'!C7` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=M9` |
| `C8` | `='1. Cant. e Mob Equipe'!C9` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `I8` | `='1. Cant. e Mob Equipe'!I10` |
| `J8` | `='1. Cant. e Mob Equipe'!J10` |
| `K8` | `='1. Cant. e Mob Equipe'!K10` |
| `M8` | `=SUM(I8:L8)` |
| `A9` | `=A5+A8+A6+A7` |
| `C9` | `='1. Cant. e Mob Equipe'!C10` |
| `F9` | `=A9*C9` |
| `I9` | `='1. Cant. e Mob Equipe'!I11` |
| `J9` | `='1. Cant. e Mob Equipe'!J11` |
| `K9` | `='1. Cant. e Mob Equipe'!K11` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=A9` |
| `C10` | `='1. Cant. e Mob Equipe'!C11` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `I11` | `='1. Cant. e Mob Equipe'!I12` |
| `J11` | `='1. Cant. e Mob Equipe'!J12` |
| `K11` | `='1. Cant. e Mob Equipe'!K12` |
| `M11` | `=SUM(I11:L11)` |
| `I12` | `='1. Cant. e Mob Equipe'!I13` |
| `J12` | `='1. Cant. e Mob Equipe'!J13` |
| `K12` | `='1. Cant. e Mob Equipe'!K13` |
| `M12` | `=SUM(I12:L12)` |
| `F14` | `=D14*E14` |
| `F15` | `=D15*E15` |
| `D16` | `=Produção!G17` |
| `D17` | `=C29` |
| `F17` | `=D17*E17` |
| `F18` | `=D18*E18` |
| `E19` | `=F11` |
| `F19` | `=D19*E19` |
| `E20` | `=F11` |
| `F20` | `=D20*E20` |
| `E21` | `=F11` |
| `F23` | `=F22*(E23/100)` |
| `F24` | `=SUM(F22:F23)` |
| `C29` | `=SUM(C26:C28)` |

### 5. Mob Centrífuga

- Faixa usada: `A1:N34`
- Fórmulas: **64**
- Conceitos provisórios: mobilizacao_sistema, operacao_desaguamento
- Células numéricas observadas: **109**

#### Rótulos e textos observados

- Mobilização 2 centrífugas
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
- Operador de Draga
- Tec segurança
- Operador de Centrífuga
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
- Verba para Cobertura do CENTRÍFUGA
- vb
- Tendas Paraná via zap em 16/01/24
- depreciação
- Munck para montagem cobertura
- Cliente
- Instalações hidráulicas
- Largura
- compr
- esp
- m³
- Instalações elétricas
- Base de Concreto
- Guindaste p/descarregamento e montagem Centrífuga
- dia
- área de giro da rosca
- Verba de eletricista para ligações
- preço de Piraí
- Base apoio Tq Equal.
- Carreta Carga Seca para CENTRÍFUGA (02 un)
- Bases de concreto para instal. Centrífuga e outros
- cliente
- Carreta para transp. Tanque de Equalização 20m³
- pç
- Fabiano 24/11/23 R$ 18.000 + 0,2% adv
- não vamos usar esse tipo de carreta com loc
- Mão de obra p/carga e montagem (r$/dia)
- mês
- TOTAL
- BDI (%)
- Preço Final
- Quant
- Decanter Centrífuga Skid - 1
- Tanque de Equalização - conjunto 1
- Decanter Centrífuga Skid - 2
- Tanque de Equalização - conjunto 2

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='1. Cant. e Mob Equipe'!C4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `='1. Cant. e Mob Equipe'!I8` |
| `M5` | `=SUM(I5:L5)` |
| `C6` | `='1. Cant. e Mob Equipe'!C7` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `I6` | `='1. Cant. e Mob Equipe'!I9` |
| `A7` | `=M11` |
| `C7` | `='1. Cant. e Mob Equipe'!C8` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=M12` |
| `C8` | `='1. Cant. e Mob Equipe'!C9` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `I8` | `='1. Cant. e Mob Equipe'!I10` |
| `J8` | `='1. Cant. e Mob Equipe'!J10` |
| `K8` | `='1. Cant. e Mob Equipe'!K10` |
| `M8` | `=SUM(I8:L8)` |
| `A9` | `=A5+A8+A7` |
| `C9` | `='1. Cant. e Mob Equipe'!C10` |
| `F9` | `=A9*C9` |
| `I9` | `='1. Cant. e Mob Equipe'!I11` |
| `J9` | `='1. Cant. e Mob Equipe'!J11` |
| `K9` | `='1. Cant. e Mob Equipe'!K11` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=A9` |
| `C10` | `='1. Cant. e Mob Equipe'!C11` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `I11` | `='1. Cant. e Mob Equipe'!I12` |
| `J11` | `='1. Cant. e Mob Equipe'!J12` |
| `K11` | `='1. Cant. e Mob Equipe'!K12` |
| `M11` | `=SUM(I11:L11)` |
| `I12` | `='1. Cant. e Mob Equipe'!I13` |
| `J12` | `='1. Cant. e Mob Equipe'!J13` |
| `K12` | `='1. Cant. e Mob Equipe'!K13` |
| `M12` | `=SUM(I12:L12)` |
| `E14` | `=J14*N14` |
| `F14` | `=D14*E14` |
| `J14` | `='1. Cant. e Mob Equipe'!J38*3` |
| `F15` | `=D15*E15` |
| `D16` | `=D14` |
| `F16` | `=D16*E16` |
| `D17` | `=D14` |
| `F17` | `=D17*E17` |
| `N17` | `=M17*L17*K17` |
| `E18` | `='Mob. Draga'!E18` |
| `F18` | `=D18*E18` |
| `N18` | `=M18*L18*K18` |
| `F19` | `=D19*E19` |
| `N19` | `=K19*L19*M19` |
| `E20` | `=F11` |
| `F20` | `=D20*E20` |
| `N20` | `=SUM(N17:N19)` |
| `D21` | `=C34` |
| `E21` | `='Mob. Draga'!E17` |
| `F22` | `=D22*E22` |
| `F23` | `=D23*E23` |
| `D24` | `='Mob. Draga'!D21` |
| `E24` | `=F11` |
| `F26` | `=F25*(E26/100)` |
| `F27` | `=SUM(F25:F26)` |
| `C34` | `=SUM(C30:C33)` |

### 6. Operação

- Faixa usada: `A1:N34`
- Fórmulas: **61**
- Conceitos provisórios: outros
- Células numéricas observadas: **117**

#### Rótulos e textos observados

- OPERAÇÃO DO SISTEMA
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Mão de OBRA
- TURNOS
- Líder de Operação
- Técnico de Segurança
- 1º
- 2º
- 3º
- Salário
- com 25%
- Operador de Draga
- Operador de Centrífuga
- Líder Operação
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
- Fretes e carretos
- mês
- #NAME?
- Materiais de segurança
- Aluguel alojamento
- Água e luz alojamento
- materiais de limpeza alojamento
- viagens de folga
- veículo + combustível
- plano de saúde
- un
- plano odontológico
- viagens de inspeção engº
- comunicações
- internet
- Mão de obra (integração)
- dia
- TOTAL
- Prazo de Operação
- custo mensal
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `=L7` |
| `C4` | `=N7` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `A5` | `=L8` |
| `C5` | `=M8` |
| `D5` | `=D4` |
| `A6` | `=L9` |
| `C6` | `=(M9*N2)+M9` |
| `D6` | `=D4` |
| `A7` | `=L10` |
| `C7` | `=(N10*N2)+N10` |
| `D7` | `=D4` |
| `L7` | `=I7+J7+K7` |
| `N7` | `=M7*1.25` |
| `A8` | `=L12` |
| `C8` | `=N12` |
| `D8` | `=D7` |
| `L8` | `=I8+J8+K8` |
| `N8` | `=M8*1.25` |
| `A9` | `=L11+L13` |
| `C9` | `=(M13*N2)+M13` |
| `D9` | `=D8` |
| `L9` | `=I9+J9+K9` |
| `A10` | `=SUM(A4:A9)` |
| `C10` | `=10+30+30` |
| `F10` | `=A10*C10` |
| `N10` | `=M10*1.25` |
| `A11` | `=A10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F4:F11)` |
| `N12` | `=M12*1.25` |
| `I14` | `=SUM(I7:I13)` |
| `J14` | `=SUM(J7:J13)` |
| `K14` | `=SUM(K8:K13)` |
| `L14` | `=SUM(I14:K14)` |
| `D15` | `=Produção!D21` |
| `F15` | `=D15*E15` |
| `D16` | `=D15` |
| `F16` | `=D16*E16` |
| `D17` | `=D16` |
| `F17` | `=D17*E17` |
| `D18` | `=D17` |
| `D19` | `=D18` |
| `D20` | `=D19` |
| `D21` | `=D20*2` |
| `D22` | `=A10*D15` |
| `D23` | `=D22` |
| `D24` | `=D15` |
| `D25` | `=D24` |
| `D26` | `=D25` |
| `E27` | `=I27` |
| `F27` | `=D27*E27` |
| `E28` | `=J27+K27` |
| `F28` | `=D28*E28` |
| `D29` | `='Dados Obra '!B27*'Dados Obra '!P30` |
| `E29` | `=F12` |
| `F30` | `=SUM(F15:F29)` |
| `F31` | `=Produção!G19` |
| `F32` | `=F30/F31` |
| `F33` | `=F32*(E33/100)` |
| `F34` | `=F32+F33` |

### 7. 2.1. Draga Dec

- Faixa usada: `A1:L206`
- Fórmulas: **103**
- Conceitos provisórios: outros
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
| `A21` | `=K33` |
| `B21` | `='1. Cant. e Mob Equipe'!I7` |
| `D21` | `='1. Cant. e Mob Equipe'!C4` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `B22` | `='Mob. Draga'!A7` |
| `D22` | `='1. Cant. e Mob Equipe'!C7` |
| `A23` | `=L24` |
| `B23` | `='Mob. Draga'!A8` |
| `D23` | `='1. Cant. e Mob Equipe'!C9` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `B24` | `='Mob. Draga'!A6` |
| `D24` | `='1. Cant. e Mob Equipe'!C6` |
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
| `F53` | `='Dados Obra '!B27` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `B69` | `=B52/2` |
| `D69` | `=C71` |
| `E69` | `=D69*B69` |
| `E71` | `=SUM(E67:E69)` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E92` | `=(0.6/100)*F7` |
| `E93` | `=(1/100)*F7` |
| `E97` | `=E92+E93+E94+E95` |
| `H99` | `=E97` |
| `E103` | `=K120` |
| `I104` | `='Dados Obra '!H16` |
| `K104` | `=I104*J104` |
| `J105` | `=K104/I105` |
| `J106` | `=K104*(1/100)` |
| `E107` | `=B107*D107` |
| `J107` | `=SUM(J105:J106)` |
| `B109` | `=B52+B53` |
| `E109` | `=B109*D109` |
| `I109` | `='Dados Obra '!H17/12*3` |
| `K109` | `=I109*J109` |
| `J110` | `=K109/I110` |
| `J111` | `=K109*(1/100)` |
| `B112` | `=B109` |
| `E112` | `=D112*B112` |
| `J112` | `=SUM(J110:J111)` |
| `I114` | `=(I104/12)` |
| `K114` | `=I114*J114` |
| `E115` | `=SUM(E103:E114)` |
| `J115` | `=K114/I115` |
| `J116` | `=K114*(1/100)` |
| `J117` | `=SUM(J115:J116)` |
| `H120` | `=J107` |
| `I120` | `=J112` |
| `J120` | `=J117` |
| `K120` | `=SUM(H120:J120)` |
| `E131` | `=E126+E127+E128+E129+E130` |
| `G134` | `=E131+E115+H99+G87+E15` |
| `E138` | `=G134*(5/100)` |
| `E139` | `=G134*(5/100)` |
| `E142` | `=E139` |
| `E145` | `=F7/60` |
| `E146` | `=F7*0.01` |
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

### 8. 2.2 Centrífuga

- Faixa usada: `A1:L205`
- Fórmulas: **103**
- Conceitos provisórios: operacao_desaguamento
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `='2.1. Draga Dec'!C9` |
| `K9` | `=SUM(K5:K8)` |
| `F10` | `=(F9*E9*D9*C9)` |
| `F11` | `=F10*0.1` |
| `K14` | `=K12-K13` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `K20` | `='Dados Obra '!B27` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `B21` | `='1. Cant. e Mob Equipe'!A5` |
| `D21` | `='1. Cant. e Mob Equipe'!C5` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `A23` | `=L24` |
| `B23` | `='Mob Centrífuga'!M12` |
| `D23` | `='1. Cant. e Mob Equipe'!C9` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `B24` | `='Mob Centrífuga'!M11` |
| `D24` | `='1. Cant. e Mob Equipe'!C8` |
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
| `B52` | `=B21` |
| `D52` | `='2.1. Draga Dec'!D52` |
| `E52` | `='2.1. Draga Dec'!E52` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B23+B24` |
| `D53` | `='2.1. Draga Dec'!D53` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `B69` | `=B52/2` |
| `D69` | `=C71` |
| `E69` | `=D69*B69` |
| `E71` | `=SUM(E67:E69)` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E92` | `=F7*0.01` |
| `E97` | `=E92+E93+E94+E95` |
| `H99` | `=E97` |
| `I104` | `='Dados Obra '!B16` |
| `K104` | `=I104*J104` |
| `J105` | `=K104/I105` |
| `E106` | `=B106*D106` |
| `J106` | `=K104*(1/100)` |
| `B107` | `='2.1. Draga Dec'!B107` |
| `E107` | `=B107*D107` |
| `J107` | `=SUM(J105:J106)` |
| `E108` | `=D108*B108` |
| `I109` | `=('Dados Obra '!B17/12)*3` |
| `K109` | `=I109*J109` |
| `J110` | `=K109/I110` |
| `B111` | `=B112` |
| `D111` | `='2.1. Draga Dec'!D112` |
| `E111` | `=B111*D111` |
| `J111` | `=K109*(1/100)` |
| `B112` | `=B52+B53` |
| `D112` | `='2.1. Draga Dec'!D109` |
| `E112` | `=B112*D112` |
| `J112` | `=SUM(J110:J111)` |
| `I114` | `=(I104/12)+2` |
| `K114` | `=I114*J114` |
| `E115` | `=SUM(E103:E114)` |
| `J115` | `=K114/I115` |
| `J116` | `=K114*(1/100)` |
| `J117` | `=SUM(J115:J116)` |
| `H120` | `=J107` |
| `I120` | `=J112` |
| `J120` | `=J117` |
| `K120` | `=SUM(H120:J120)` |
| `E131` | `=E126+E127+E128+E129+E130` |
| `G134` | `=E131+E115+H99+G87+E15` |
| `E138` | `=G134*(5/100)` |
| `E139` | `=G134*(5/100)` |
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
| `D198` | `='2.1. Draga Dec'!D200` |
| `D199` | `=D197*D198` |
| `J199` | `=D197` |
| `D201` | `=D199+D200` |
| `J201` | `=J199*J200` |
| `J202` | `=Produção!H6` |
| `J205` | `=(J201/J202)*J203` |

### 9. 2.3. manutenção

- Faixa usada: `A1:H26`
- Fórmulas: **44**
- Conceitos provisórios: outros
- Células numéricas observadas: **61**

#### Rótulos e textos observados

- MANUTENÇÃO PREVENTIVA - GRATT
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Líder de Operação
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
- Visita Trimestral técnico GRATT
- un
- cotação jan26 = R$ 9.850
- GRATT - manutenção mecânica preventiva - incluindo MDO de troca peças
- cotação jan26 = R$34.400
- Serviços de reparos Elétricos (3 diárias por mês
- mês
- Mão de obra (de acompanhamento)
- TOTAL
- Prazo de Operação
- #NAME?
- preço unitário
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `='1. Cant. e Mob Equipe'!A4` |
| `C4` | `='1. Cant. e Mob Equipe'!C4` |
| `E4` | `='1. Cant. e Mob Equipe'!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `A5` | `='1. Cant. e Mob Equipe'!A5` |
| `C5` | `='1. Cant. e Mob Equipe'!C5` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='1. Cant. e Mob Equipe'!A6` |
| `C6` | `='1. Cant. e Mob Equipe'!C6` |
| `D6` | `=D4` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `='1. Cant. e Mob Equipe'!A7` |
| `C7` | `='1. Cant. e Mob Equipe'!C7` |
| `D7` | `=D4` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `='1. Cant. e Mob Equipe'!A8` |
| `C8` | `='1. Cant. e Mob Equipe'!C8` |
| `D8` | `=D7` |
| `E8` | `=E7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `='1. Cant. e Mob Equipe'!A9` |
| `C9` | `='1. Cant. e Mob Equipe'!C9` |
| `E9` | `=E8` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `A10` | `=SUM(A4:A9)` |
| `C10` | `='1. Cant. e Mob Equipe'!C10` |
| `F10` | `=A10*C10` |
| `A11` | `=A10` |
| `C11` | `='1. Cant. e Mob Equipe'!C11` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F4:F11)` |
| `E15` | `=10000` |
| `F15` | `=D15*E15` |
| `F17` | `=D17*E17` |
| `E21` | `=F12` |
| `F22` | `=SUM(F15:F21)` |
| `F23` | `=Produção!G19` |
| `F24` | `=F22/F23` |
| `F25` | `=F24*(E25/100)` |
| `F26` | `=F24+F25` |

### 10. 3. Desmob.

- Faixa usada: `A1:N45`
- Fórmulas: **66**
- Conceitos provisórios: desmobilizacao
- Células numéricas observadas: **191**

#### Rótulos e textos observados

- DESMOBILIZAÇÃO
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Mão de OBRA
- TURNOS
- Líder de Operação
- Técnico de Segurança
- 1º
- 2º
- 3º
- Salário
- com 25%
- Operador de Draga
- Operador de Centrífuga
- Líder Operação
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
- locmeq
- Container Sanitário/Vestiário
- Na Draga
- pessoas por turno
- Container Escritório
- Na Planta
- Frete para Containers
- vb
- Mobiliário Canteiro
- Mobiliário Alojamento
- PGR + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- itens de segurança
- Tenda do Canteiro
- Bebedouro elétrico
- material de escritório
- custo Exames médicos
- un
- Viagem da equipe VOLTA
- Hospedagem
- Almoço
- jantar
- café
- Hospedagem EQUIPE
- dia
- Uilson
- Alimentação EQUIPE
- Pedro Paulo
- Veículo para uso na obra
- Uildes
- Viagem AGUINALDO ida e volta
- Paulo Araújo
- Veículo para Aguinaldo
- Hospedagem AGUINALDO
- Aguinaldo
- Alimentação AGUINALDO
- Mão de obra (integração)
- TOTAL
- Prazo de Operação
- #NAME?
- preço unitário
- Viagem
- Uber 1

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `=L7` |
| `C4` | `=N7` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `A5` | `=L8` |
| `C5` | `=M8` |
| `D5` | `=D4` |
| `A6` | `=L9` |
| `C6` | `=(M9*N2)+M9` |
| `D6` | `=D4` |
| `A7` | `=L10` |
| `C7` | `=(N10*N2)+N10` |
| `D7` | `=D4` |
| `L7` | `=I7+J7+K7` |
| `N7` | `=M7*1.25` |
| `A8` | `=L12` |
| `C8` | `=N12` |
| `D8` | `=D7` |
| `L8` | `=I8+J8+K8` |
| `N8` | `=M8*1.25` |
| `A9` | `=L11+L13` |
| `C9` | `=(M13*N2)+M13` |
| `L9` | `=I9+J9+K9` |
| `A10` | `=SUM(A4:A9)` |
| `F10` | `=A10*C10` |
| `N10` | `=M10*1.25` |
| `A11` | `=A10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F4:F11)` |
| `N12` | `=M12*1.25` |
| `I14` | `=SUM(I7:I13)` |
| `J14` | `=SUM(J7:J13)` |
| `K14` | `=SUM(K8:K13)` |
| `L14` | `=SUM(I14:K14)` |
| `F15` | `=D15*E15` |
| `E20` | `=E19` |
| `D27` | `=A10` |
| `E28` | `=N44` |
| `E29` | `=I33` |
| `F29` | `=D29*E29` |
| `D30` | `=D29` |
| `E30` | `=K33+L33` |
| `F30` | `=D30*E30` |
| `F31` | `=D31*E31` |
| `E32` | `=N45` |
| `F32` | `=D32*E32` |
| `F33` | `=D33*E33` |
| `I33` | `=SUM(I29:I32)` |
| `J33` | `=SUM(J29:J32)` |
| `K33` | `=SUM(K29:K32)` |
| `L33` | `=SUM(L29:L32)` |
| `D34` | `=D33` |
| `E34` | `=I34` |
| `F34` | `=D34*E34` |
| `D35` | `=D34` |
| `E35` | `=J34+K34` |
| `F35` | `=D35*E35` |
| `E36` | `=F12` |
| `F37` | `=SUM(F15:F36)` |
| `F38` | `=Produção!G19` |
| `F39` | `=F37/F38` |
| `F40` | `=F39*(E40/100)` |
| `N40` | `=SUM(I40:M40)` |
| `F41` | `=F39+F40` |
| `N41` | `=SUM(I41:M41)` |
| `N44` | `=SUM(N40:N43)` |
| `N45` | `=SUM(I45:M45)` |

### 11. Plan. Final

- Faixa usada: `A1:L30`
- Fórmulas: **44**
- Conceitos provisórios: outros
- Células numéricas observadas: **57**

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
- Canteiro de Obras
- vb
- Dragagem e desaguamento Centrífuga
- Operação da Draga
- TSS
- Operação Centrífuga
- Manutenção dos equipamentos
- Desmobilização do Canteiro
- Preço de Venda
- Custo da Hora a disposição
- Custo REAL de Operação
- Custo total de operação
- #NAME?
- Valor de Venda operação
- RESULTADO
- total do Custo
- RESULTADO MENSAL
- Total de Horas por mês
- Total de meses de operação
- Total de horas ano
- Custo por hora
- BDI
- VALOR DA HORA A DISPOSIÇÃO
- Faturamento mensal

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Cant. e Mob Equipe'!F37` |
| `G4` | `=C4/E4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `L4` | `=I4` |
| `C7` | `='2.1. Draga Dec'!D201` |
| `E7` | `='Dados Obra '!P31` |
| `G7` | `=C7/E7` |
| `I7` | `=((H7/100)+1)*G7` |
| `J7` | `=E7*I7` |
| `L7` | `=I7+I8+I9` |
| `C8` | `='2.2 Centrífuga'!D199` |
| `E8` | `=E7` |
| `F8` | `=F7` |
| `G8` | `=C8/E8` |
| `I8` | `=((H8/100)+1)*G8` |
| `J8` | `=E8*I8` |
| `C9` | `='2.3. manutenção'!F22` |
| `E9` | `=E7` |
| `F9` | `=F8` |
| `G9` | `=C9/E9` |
| `C11` | `='3. Desmob.'!F37` |
| `G11` | `=C11/E11` |
| `I11` | `=((H11/100)+1)*G11` |
| `L11` | `=I11` |
| `C13` | `=SUM(C4:C12)` |
| `J13` | `=SUM(J4:J12)` |
| `C15` | `=J13-C13` |
| `J15` | `=J13/E7` |
| `C18` | `=(C7+C8+C9)-(('2.1. Draga Dec'!E139+'2.1. Draga Dec'!E138+'2.1. Draga Dec'!E94:F94+'2.1. Draga Dec'!E95:F95+'2.1. Draga Dec'!F12:G12+'2.2 Centrífuga'!F12:G12+'2.2 Centrífuga'!E138+'2.2 Centrífuga'!E139)*'Dados Obra '!K11)` |
| `J18` | `=Operação!F30` |
| `C19` | `=J7+J8+J9` |
| `C20` | `=C19-C18` |
| `J20` | `=SUM(J18:J19)` |
| `C21` | `=C20/'Dados Obra '!P30` |
| `J22` | `=Produção!H6` |
| `J23` | `='Dados Obra '!P30` |
| `J24` | `=J22*J23` |
| `J25` | `=J20/J24` |
| `J26` | `=J25*I26` |
| `J27` | `=J25+J26` |
| `J29` | `=J27*J22` |
| `L29` | `=L7*'Dados Obra '!P29` |
| `J30` | `=J29/L29` |

### 12. Final

- Faixa usada: `A1:AC8`
- Fórmulas: **27**
- Conceitos provisórios: outros
- Células numéricas observadas: **64**

#### Rótulos e textos observados

- Revisão Final 17/04/26
- PROP. REVISÃO 02 (2.000 toneladas)
- PROP. REVISÃO 01 (2.000 toneladas)
- 3.000 toneladas
- INICIAL
- Preço Fos Contrato que Executamos
- só MDO 2 turnos completos obra passada
- BDI praticado
- ITEM
- DESCRIÇÃO DOS SERVIÇOS
- UN
- QUANT
- PREÇO UNIT
- PREÇO TOTAL
- BDI
- Desc Atual
- Preço enviado em 20/03/26
- aumento/desconto
- Preço enviado em 11/02/26
- Preço enviado em 21/jan/26
- aumento
- Preço enviado em ago/25
- COM NOSSO EQTO
- Mobilização de Equipe e Manutenção de Canteiro
- vb
- Operação do Sistema de Dragagem e desidratação de lodo, incluindo manutenção dos equipamentos
- Ton Seca
- Desmobilização Final
- Com MDO maior
- VALOR TOTAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D3` | `='Plan. Final'!E4` |
| `E3` | `='Plan. Final'!L4` |
| `F3` | `=D3*E3` |
| `I3` | `=(E3/K3)-1` |
| `M3` | `=(K3/O3)-1` |
| `Q3` | `=(O3/S3)-1` |
| `U3` | `=(S3/W3)-1` |
| `D4` | `='Plan. Final'!E7` |
| `E4` | `='Plan. Final'!L7` |
| `F4` | `=D4*E4` |
| `I4` | `=(E4/K4)-1` |
| `M4` | `=(K4/O4)-1` |
| `Q4` | `=(O4/S4)-1` |
| `U4` | `=(S4/W4)-1` |
| `D5` | `='Plan. Final'!E11` |
| `E5` | `='Plan. Final'!L11` |
| `F5` | `=D5*E5` |
| `I5` | `=(E5/K5)-1` |
| `M5` | `=(K5/O5)-1` |
| `Q5` | `=(O5/S5)-1` |
| `U5` | `=(S5/W5)-1` |
| `F6` | `=SUM(F3:F5)` |
| `I6` | `=(F6/K8)-1` |
| `M8` | `=(K8/O8)-1` |
| `Q8` | `=(O8/S8)-1` |
| `S8` | `=S3+S5+(S4*2000)` |
| `U8` | `=(O8/S8)-1` |

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
