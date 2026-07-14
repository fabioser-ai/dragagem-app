# Modelo 023 — D_011_2025 - SAMAE IBIPORA.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `D_011_2025 - SAMAE IBIPORA.xlsx`
- Família provisória: **Dragagem/bombeamento**
- SHA-256 do arquivo: `1d1c918b823e707c0f8bb174f569d11df20d33287368d16bc2ae2959ed01cde2`
- Abas analisadas: **11**
- Fórmulas encontradas: **228**

## Conceitos identificados

- `outros`: 3 aba(s)
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
| 2 | `Produção` | `A1:H24` | 9 | producao_prazo |
| 3 | `1. Mob. Draga` | `A1:G25` | 18 | mobilizacao_draga |
| 4 | `2. Canteiro` | `A1:F28` | 19 | canteiro |
| 5 | `3. Remoção de Veg` | `A1:F20` | 14 | outros |
| 6 | `4. Prep. Área - Ensecadeira` | `A1:G43` | 23 | outros |
| 7 | `5. Mov. De Vegetação` | `A1:F38` | 9 | outros |
| 8 | `6. Medição` | `A1:G38` | 6 | medicao_batimetria |
| 9 | `7. Dragagem` | `A1:L250` | 85 | dragagem_operacao |
| 10 | `8. Desmob. Draga` | `A1:G21` | 18 | mobilizacao_draga, desmobilizacao |
| 11 | `Plan. Preços` | `A1:J12` | 24 | formacao_preco |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `Dados Obra` | 16 |
| `5. Mov. De Vegetação` | 2 |
| `1. Mob. Draga` | 1 |
| `2. Canteiro` | 1 |
| `3. Remoção de Veg` | 1 |
| `4. Prep. Área - Ensecadeira` | 1 |
| `6. Medição` | 1 |
| `7. Dragagem` | 1 |
| `8. Desmob. Draga` | 1 |

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
- D_011_225
- Data
- Cliente
- SAMAE
- Contato
- Eloise Vitoria Verlingue da Silva
- e-mail
- Dados da obra
- Objeto
- Desassoreamento do Leito de Captação do Ribeirãso Jacutinga
- Local
- Ibiporã
- Volume dragagem (m³)
- Tipo de material
- Areia + Argila
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
- Ensecadeira
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
- Variável Pode oscilar dependendo do resultado da batimetria
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

### 3. 1. Mob. Draga

- Faixa usada: `A1:G25`
- Fórmulas: **18**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **49**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 6"
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
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
- Fabiano
- Guindaste p/descarregamento e montagem DRAGA
- Chute
- Projeto Basico
- vb
- Projeto Executivo
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
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=SUM(A5:A6)` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `F14` | `=D14*E14` |
| `F15` | `=D15*E15` |
| `F18` | `=D18*E18` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `E22` | `=F9` |
| `F23` | `=SUM(F14:F22)` |
| `F24` | `=F23*(E24/100)` |
| `F25` | `=SUM(F23:F24)` |

### 4. 2. Canteiro

- Faixa usada: `A1:F28`
- Fórmulas: **19**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **60**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
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
- #NAME?
- Banheiro Quimico
- Transferencia ( Munck )
- vb
- Frete para Containers
- PPRA + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Placa de obra
- Gerador (Locaçao + Diesel = 2000 + 5000)
- mes
- água potável
- gl
- material de escritório
- Mão de obra (Montagem / Desmontagem)
- dia
- TOTAL
- Meses
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=SUM(A5:A6)` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `D14` | `=(ROUNDUP(Produção!D24,0))+1` |
| `F14` | `=D14*E14` |
| `D15` | `=(ROUNDUP(Produção!D24,0))+1` |
| `D22` | `=2*4*D14` |
| `D23` | `=(ROUNDUP(Produção!D24,0))+1` |
| `E24` | `=F9` |
| `F25` | `=SUM(F14:F24)` |
| `F26` | `=(ROUNDUP(Produção!D24,0))+1` |
| `F27` | `=F25*(E27/100)` |
| `F28` | `=F25/F26` |

### 5. 3. Remoção de Veg

- Faixa usada: `A1:F20`
- Fórmulas: **14**
- Conceitos provisórios: outros
- Células numéricas observadas: **34**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
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
- Hidrotractor
- mes
- Mob / Desmob
- vb
- Mão de obra (Montagem / Desmontagem)
- dia
- TOTAL
- Unitario
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=SUM(A5:A6)` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `F14` | `=D14*E14` |
| `E16` | `=F9` |
| `F17` | `=SUM(F14:F16)` |
| `F19` | `=F17*(E19/100)` |
| `F20` | `=F17/F18` |

### 6. 4. Prep. Área - Ensecadeira

- Faixa usada: `A1:G43`
- Fórmulas: **23**
- Conceitos provisórios: outros
- Células numéricas observadas: **53**

#### Rótulos e textos observados

- 3. PREPARO DA ÁREA - Caixa
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
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
- Regularização manual - Mão de obra
- dia
- Escavadeira Hidraulica (sem frete)
- Danilo 2500 curitiba
- Trator para limpeza do terreno + Acesso
- Tubulaçao para drenagem
- m
- Mao de obra
- dias
- TOTAL
- BDI (%)
- Preço Final
- m3
- h
- Dia
- horas
- TCPO
- Area: 10848,98 m2
- Perimeto: 400 m
- Volume: 10848,98 x 1,25 = 13561 m3
- Leira: Área: 1,25 x 1,25 = 1,56 + 1,56 = 3,12 m2 ( Secçao)
- Logo: 3,12 x 400 = 1248 m3
- Trator - Limpeza terreno
- m2

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=SUM(A5:A6)` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `E14` | `=F9` |
| `F14` | `=D14*E14` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `E18` | `=F9` |
| `F18` | `=D18*E18` |
| `F20` | `=SUM(F14:F18)` |
| `F21` | `=F20*(E21/100)` |
| `F22` | `=SUM(F20:F21)` |
| `D28` | `=(D27*C28)/C27` |
| `F28` | `=(G28*F27)/G27` |
| `G28` | `=D28` |
| `C43` | `=C42*B43` |

### 7. 5. Mov. De Vegetação

- Faixa usada: `A1:F38`
- Fórmulas: **9**
- Conceitos provisórios: outros
- Células numéricas observadas: **46**

#### Rótulos e textos observados

- 5 - MOVIMENTAÇÃO VEGETAÇÃO
- Transporte Vegetaçao até 10KM
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
- Técnico
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
- Escavadeira
- diaria
- Movimentação volume ensecadeira
- viagem
- TOTAL
- BDI (%)
- Preço Final
- Area de vegetaçao =
- Lagoa
- m2
- Bacia
- Volume de vegetaçao =
- Vai perder volume no sol desidratando
- Caminhoes de 15 m3 farao tantas viagens
- Preço do danilo em Curitina para cada viagem
- Portnto custo total de 76 viagem com margem é
- Chutado

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D17` | `=ROUNDUP(C34,0)` |
| `E17` | `=C36*1.3` |
| `F17` | `=D17*E17` |
| `F22` | `=SUM(F16:F21)` |
| `F24` | `=F22` |
| `C30` | `=(D27*0.3)+(D28*0.2)` |
| `C32` | `=C30*0.499` |
| `C34` | `=C32/15` |
| `C38` | `=(C36*1.3)*C34` |

### 8. 6. Medição

- Faixa usada: `A1:G38`
- Fórmulas: **6**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **42**

#### Rótulos e textos observados

- 6 - MEDIÇÃO
- Mediçao volumétrica - Ensecadeira
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
- Técnico
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
- m2
- Chute - para retornar 6 vezes e fazer o levantamento
- serao 6 visitas - acredito que é negociavel por esse preço
- nao fiz cotaçao
- TOTAL
- BDI (%)
- Preço Final
- Area de vegetaçao =
- Lagoa
- Bacia
- Volume de vegetaçao =
- Vai perder volume no sol desidratando
- Caminhoes de 15 m3 farao tantas viagens
- Preço do danilo em Curitina para cada viagem
- Portnto custo total de 76 viagem com margem é
- Chutado

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F16` | `=D16*E16` |
| `F22` | `=SUM(F16:F21)` |
| `C30` | `=(D27*0.3)+(D28*0.2)` |
| `C32` | `=C30*0.499` |
| `C34` | `=C32/15` |
| `C38` | `=(C36*1.3)*C34` |

### 9. 7. Dragagem

- Faixa usada: `A1:L250`
- Fórmulas: **85**
- Conceitos provisórios: dragagem_operacao
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `=Produção!H6` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=F10*0.1` |
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
| `E158` | `='2. Canteiro'!F28` |
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
| `D225` | `=Produção!D13` |
| `D227` | `=D222/D225` |
| `D231` | `=(D227*(B229))+D227` |
| `D234` | `=J250*0.6*0.62` |
| `H235` | `=Produção!H4` |
| `I235` | `=Produção!H3` |
| `J235` | `=H235*I235` |
| `D244` | `=D222` |
| `J244` | `=D245` |
| `D245` | `=SUM(D244:D244)` |
| `D246` | `=ROUNDUP(Produção!D24,0)` |
| `J246` | `=J244*J245` |
| `L246` | `=J246/J247` |
| `D247` | `=D245*D246` |
| `J247` | `=Produção!H6` |
| `D248` | `=SUM(D247:D247)` |
| `L248` | `=L246*L247` |
| `J249` | `=J247*J248` |
| `J250` | `=J246/J249` |

### 10. 8. Desmob. Draga

- Faixa usada: `A1:G21`
- Fórmulas: **18**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **38**

#### Rótulos e textos observados

- 8 - Desmobilização da Draga 6"
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
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
- Carreta Carga Seca para DRAGA
- un
- Genival (25/06/18)
- Guindaste p/descarregamento e montagem DRAGA
- Trator D4 para lançar draga na água
- Terraplenagem Lavoro
- Mão de obra p/carga e montagem (r$/dia)
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `='Dados Obra '!B26` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=SUM(A5:A6)` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F5:F8)` |
| `F14` | `=D14*E14` |
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `E18` | `=F9` |
| `F18` | `=D18*E18` |
| `F19` | `=SUM(F14:F18)` |
| `F20` | `=F19*(E20/100)` |
| `F21` | `=SUM(F19:F20)` |

### 11. Plan. Preços

- Faixa usada: `A1:J12`
- Fórmulas: **24**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **44**

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
- 1.2
- Mobilização
- vb
- Remoção de Vegetaçao
- Movimentaçao de Vegetaçao
- m3
- Ensecadeira
- 2.1
- Dragagem
- Medição
- m2
- Desmobilização
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='1. Mob. Draga '!F25` |
| `G5` | `=C5/E5` |
| `I5` | `=((H5/100)+1)*G5` |
| `J5` | `=E5*I5` |
| `C6` | `='3. Remoção de Veg'!F20` |
| `G6` | `=C6/E6` |
| `I6` | `=((H6/100)+1)*G6` |
| `J6` | `=E6*I6` |
| `C7` | `='5. Mov. De Vegetação'!F24` |
| `E7` | `='5. Mov. De Vegetação'!C32` |
| `G7` | `=C7/E7` |
| `I7` | `=((H7/100)+1)*G7` |
| `J7` | `=E7*I7` |
| `C8` | `='4. Prep. Área - Ensecadeira'!F22` |
| `G8` | `=C8/E8` |
| `I8` | `=((H8/100)+1)*G8` |
| `J8` | `=E8*I8` |
| `C9` | `='7. Dragagem'!D247` |
| `C10` | `='6. Medição'!F22` |
| `I10` | `=((H10/100)+1)*G10` |
| `J10` | `=E10*I10` |
| `C11` | `='8. Desmob. Draga'!F21` |
| `C12` | `=SUM(C5:C9)` |
| `J12` | `=SUM(J5:J11)` |

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
