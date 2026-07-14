# Modelo 011 — Composição preços - Draga 14.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `Composição preços - Draga 14.xlsx`
- Família provisória: **Composição padrão de draga**
- SHA-256 do arquivo: `77c0681b5685b9d52840d60c69052d126bbed3991f5b78999413cb9ed91a336c`
- Abas analisadas: **5**
- Fórmulas encontradas: **201**

## Conceitos identificados

- `dados_obra`: 1 aba(s)
- `desmobilizacao`: 1 aba(s)
- `dragagem_operacao`: 1 aba(s)
- `outros`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:I27` | 3 | dados_obra |
| 2 | `Produção` | `A1:H24` | 9 | producao_prazo |
| 3 | `1. Mobilização` | `A1:N40` | 49 | outros |
| 4 | `2. Dragagem` | `A1:S249` | 88 | dragagem_operacao |
| 5 | `3. Desmobilização` | `A1:N39` | 52 | desmobilizacao |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `Dados Obra` | 9 |
| `1. Mobilização` | 2 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:I27`
- Fórmulas: **3**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **12**

#### Rótulos e textos observados

- ROCHA E MELO
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- Proposta
- Proposta D_010_2026
- Data
- Cliente
- Contato
- Leandro
- e-mail
- Dados da obra
- Objeto
- Execução dragagem 500.000
- Local
- Torres - RS
- Volume dragagem (m³)
- chutei volume para calcular custo de locação mensal
- Tipo de material
- areia fina
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
- Horário de Trabalho (24h)
- h/dia
- Dias de Trabalho (2ª a sabado)
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
- Dias / Mês (2ª a sábado)
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

### 3. 1. Mobilização

- Faixa usada: `A1:N40`
- Fórmulas: **49**
- Conceitos provisórios: outros
- Células numéricas observadas: **145**

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
- Engenheiro Residente
- 1º
- 2º
- 3º
- Salário
- com 25%
- Encarregado
- Engº
- Operador de Draga
- Maquinistas
- Mecânico
- Barqueiro
- Operador Draga
- Ajudante Draga
- Maquinista
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
- MOBILIZAÇÃO EQUIPE
- Treinamentos de Segurança
- un
- Exames médicos
- Comunicaçao
- vb
- Viagem de ida para obra
- chute
- Laudo de flutuabilidade
- MOBILIZAÇÃO DOS EQUIPAMENTOS
- Guindaste para Carregamento
- dia
- Carreta prancha rebaixada
- CRUZ DE MALTA
- Carreta extensível
- Seguro de Transporte da Carga
- Carreta Carga Seca
- Guindaste para descarregamento e montagem
- Planos de Rigging
- Aluguel de Veículo + combustível
- vb/mês
- Mão de obra Integração e Mobilização (r$/dia)
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
- R$ carga
- Carga seca graneleira
- Total da Linha
- Quant de Carretas para tubos

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `=L5` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `=N6` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `L5` | `=I5+J5+K5` |
| `C6` | `=N8` |
| `N6` | `=M6*1.25` |
| `C7` | `=N10` |
| `N7` | `=M7*1.25` |
| `A8` | `=L11` |
| `C8` | `=N11` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `N8` | `=M8*1.25` |
| `A9` | `=L7` |
| `C9` | `=N7` |
| `F10` | `=(A10*C10*D10)+(A10*C10*D10)*(E10/100)` |
| `N10` | `=M10*1.25` |
| `C11` | `=M9` |
| `M11` | `=M10` |
| `N11` | `=M11*1.25` |
| `A12` | `=SUM(A4:A11)` |
| `F12` | `=A12*C12` |
| `I12` | `=SUM(I5:I11)` |
| `J12` | `=SUM(J6:J11)` |
| `K12` | `=SUM(K6:K11)` |
| `L12` | `=SUM(I12:K12)` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F4:F13)` |
| `D18` | `=A12` |
| `F18` | `=D18*E18` |
| `D19` | `=A12` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `D21` | `=A12` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `F24` | `=D24*E24` |
| `D28` | `=I40` |
| `F29` | `=D29*E29` |
| `E32` | `=F14` |
| `F33` | `=SUM(F18:F32)` |
| `F34` | `=F33*(E34/100)` |
| `F35` | `=SUM(F33:F34)` |
| `G38` | `=((D38+E38)/F38)*(C38/F38)` |
| `I38` | `=G38*H38` |
| `K38` | `=I38*J38` |
| `I39` | `='Dados Obra '!B16` |
| `I40` | `=ROUNDUP(((I39/I38)+1),0)` |

### 4. 2. Dragagem

- Faixa usada: `A1:S249`
- Fórmulas: **88**
- Conceitos provisórios: dragagem_operacao
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `=Produção!H6` |
| `F10` | `=C9*D9*E9*F9` |
| `S10` | `=R10*1.25` |
| `F11` | `=(C9*D9*E9*J9)*0.1` |
| `R11` | `=(R10*Q11)/Q10` |
| `S11` | `=R11*1.25` |
| `F12` | `=F11*0.1` |
| `F13` | `=F12*0.5` |
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
| `D26` | `='1. Mobilização'!N7` |
| `A27` | `=L24` |
| `D27` | `='1. Mobilização'!C9` |
| `E27` | `=D27*B27*A27` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `B52` | `=B21+B22+B23` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B24+B25+B26` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `E71` | `=E69` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E139` | `=(0.6/100)*F7` |
| `E140` | `=(1/100)*F7` |
| `E141` | `=E139*0.1` |
| `E144` | `=E139+E140+E141+E142` |
| `H146` | `=E144` |
| `E150` | `=K167` |
| `I151` | `='Dados Obra '!H16` |
| `K151` | `=I151*J151` |
| `E152` | `=D152*B152` |
| `J152` | `=K151/I152` |
| `J153` | `=K151*(1/100)` |
| `J154` | `=SUM(J152:J153)` |
| `I156` | `='Dados Obra '!H17/12*3` |
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
| `D222` | `=G181` |
| `D225` | `=E189` |
| `P226` | `=(P225*O226)/O225` |
| `Q226` | `=P226*1.25` |
| `D227` | `=E196` |
| `D229` | `=D222+D225+D227` |
| `E232` | `=Produção!D13` |
| `E234` | `=D229/E232` |
| `D236` | `=D229*B236` |
| `D238` | `=D236+D229` |
| `H242` | `=Produção!H4` |
| `I242` | `=Produção!H3` |
| `J242` | `=H242*I242` |
| `C246` | `=ROUNDUP(Produção!D24,0)` |
| `D246` | `=C246*D238` |
| `D247` | `=D246/'Dados Obra '!B14` |

### 5. 3. Desmobilização

- Faixa usada: `A1:N39`
- Fórmulas: **52**
- Conceitos provisórios: desmobilizacao
- Células numéricas observadas: **141**

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
- Engenheiro Residente
- 1º
- 2º
- 3º
- Salário
- com 25%
- Encarregado
- Engº
- Operador de Draga
- Maquinistas
- Mecânico
- Barqueiro
- Operador Draga
- Ajudante Draga
- Maquinista
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
- MOBILIZAÇÃO EQUIPE
- Treinamentos de Segurança
- un
- Exames médicos
- Viagem de ida para obra
- vb
- chute
- Laudo de flutuabilidade
- MOBILIZAÇÃO DOS EQUIPAMENTOS
- Guindaste para Carregamento
- dia
- Carreta prancha rebaixada
- Carreta extensível
- Seguro de Transporte da Carga
- Carreta Carga Seca
- Guindaste para descarregamento e montagem
- Planos de Rigging
- Aluguel de Veículo + combustível
- vb/mês
- Mão de obra Integração e Mobilização (r$/dia)
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
- R$ carga
- Carga seca graneleira
- Total da Linha
- Quant de Carretas para tubos

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `=L5` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `A5` | `=L6` |
| `C5` | `=N6` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `L5` | `=I5+J5+K5` |
| `A6` | `=L8` |
| `C6` | `=N8` |
| `N6` | `=M6*1.25` |
| `A7` | `=L10` |
| `C7` | `=N10` |
| `N7` | `=M7*1.25` |
| `A8` | `=L11` |
| `C8` | `=N11` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `N8` | `=M8*1.25` |
| `A9` | `=L7` |
| `C9` | `=N7` |
| `F10` | `=(A10*C10*D10)+(A10*C10*D10)*(E10/100)` |
| `N10` | `=M10*1.25` |
| `A11` | `=L9` |
| `C11` | `=M9` |
| `M11` | `=M10` |
| `N11` | `=M11*1.25` |
| `A12` | `=SUM(A4:A11)` |
| `F12` | `=A12*C12` |
| `I12` | `=SUM(I5:I11)` |
| `J12` | `=SUM(J6:J11)` |
| `K12` | `=SUM(K6:K11)` |
| `L12` | `=SUM(I12:K12)` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F4:F13)` |
| `D18` | `=A12` |
| `F18` | `=D18*E18` |
| `D19` | `=A12` |
| `F19` | `=D19*E19` |
| `D20` | `=A12` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `F23` | `=D23*E23` |
| `D27` | `=I39` |
| `E28` | `=E23` |
| `E31` | `=F14` |
| `F32` | `=SUM(F18:F31)` |
| `F33` | `=F32*(E33/100)` |
| `F34` | `=SUM(F32:F33)` |
| `G37` | `=((D37+E37)/F37)*(C37/F37)` |
| `I37` | `=G37*H37` |
| `K37` | `=I37*J37` |
| `I38` | `='Dados Obra '!B16` |
| `I39` | `=ROUNDUP(((I38/I37)+1),0)` |

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
