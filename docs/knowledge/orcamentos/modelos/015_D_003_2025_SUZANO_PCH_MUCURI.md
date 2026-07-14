# Modelo 015 — D_003_2025- Suzano PCH Mucuri.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `D_003_2025- Suzano PCH Mucuri.xlsx`
- Família provisória: **Outros / composição específica**
- SHA-256 do arquivo: `2970faaded3a4c24033f4095adc8f9805800c30ffa421ca15f861df5965537b9`
- Abas analisadas: **13**
- Fórmulas encontradas: **217**

## Conceitos identificados

- `outros`: 6 aba(s)
- `desmobilizacao`: 2 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `formacao_preco`: 1 aba(s)
- `medicao_batimetria`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:H27` | 3 | dados_obra |
| 2 | `Produção` | `A1:H24` | 8 | producao_prazo |
| 3 | `1. Mob. Hidrotractor` | `A1:F20` | 17 | outros |
| 4 | `2. Mob. Escavadeira` | `A1:F20` | 17 | outros |
| 5 | `3. Canteiro de obras` | `A1:G39` | 29 | canteiro |
| 6 | `4. Hidrotractor` | `A1:J21` | 16 | outros |
| 7 | `5. Escadeira` | `A1:J21` | 16 | outros |
| 8 | `6. Caminhao&Comboio` | `A1:J26` | 19 | outros |
| 9 | `7. Triturador` | `A1:F22` | 16 | outros |
| 10 | `8. Mediçao` | `A1:F23` | 16 | medicao_batimetria |
| 11 | `9. DesMob. Hidrotractor` | `A1:F20` | 17 | desmobilizacao |
| 12 | `10. DesMob. Escavadeira` | `A1:F20` | 17 | desmobilizacao |
| 13 | `11. Plan. Preços` | `A1:M14` | 26 | formacao_preco |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `Dados Obra` | 20 |
| `1. Mob. Hidrotractor` | 1 |
| `10. DesMob. Escavadeira` | 1 |
| `2. Mob. Escavadeira` | 1 |
| `3. Canteiro de obras` | 1 |
| `4. Hidrotractor` | 1 |
| `5. Escadeira` | 1 |
| `6. Caminhao&Comboio` | 1 |
| `7. Triturador` | 1 |
| `8. Mediçao` | 1 |
| `9. DesMob. Hidrotractor` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:H27`
- Fórmulas: **3**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **8**

#### Rótulos e textos observados

- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- Proposta
- Proposta D_003_2025
- Data
- Cliente
- Suzano
- Contato
- e-mail
- Dados da obra
- Objeto
- Remoçao de vegetaçao sobrenadante - 7km2
- Local
- PCH MUCURI
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

### 3. 1. Mob. Hidrotractor

- Faixa usada: `A1:F20`
- Fórmulas: **17**
- Conceitos provisórios: outros
- Células numéricas observadas: **36**

#### Rótulos e textos observados

- 1 - Mobilização Hidrotractor
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
- Munck para descarregamento
- dia
- Mobilizaçao (HIDROTRACTOR)
- vb
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
| `E17` | `=F10` |
| `F18` | `=SUM(F15:F17)` |
| `F19` | `=F18*(E19/100)` |
| `F20` | `=SUM(F18:F19)` |

### 4. 2. Mob. Escavadeira

- Faixa usada: `A1:F20`
- Fórmulas: **17**
- Conceitos provisórios: outros
- Células numéricas observadas: **35**

#### Rótulos e textos observados

- 1 - Mobilização Escavadeira
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
- Munck para descarregamento
- dia
- Mobilizaçao (HIDROTRACTOR)
- vb
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
| `E17` | `=F10` |
| `F18` | `=SUM(F15:F17)` |
| `F19` | `=F18*(E19/100)` |
| `F20` | `=SUM(F18:F19)` |

### 5. 3. Canteiro de obras

- Faixa usada: `A1:G39`
- Fórmulas: **29**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **98**

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
- Nutrilog
- Container Sanitário/Vestiário
- Container Escritório c/sanitário
- Frete para Containers
- vb
- PPRA + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- EPI
- Func
- Aluguel de Alojamento
- Moveis para casa
- Veiculo (obra)
- mes
- Combustivel Veiculo
- Barreira Contençao
- Viagem de inspeçao
- Barco de Apoio
- Placa de obra
- Vigilância
- Nao será necessario
- água potável
- gl
- material de escritório
- Banheiro quimico
- vestiário
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
| `E21` | `=400*3*8` |
| `D22` | `=D15` |
| `D24` | `=D15` |
| `E25` | `=4*40*6` |
| `E26` | `=370*300` |
| `D27` | `=D15` |
| `D28` | `=D15` |
| `F30` | `=D30*E30` |
| `D31` | `=24*8` |
| `D32` | `=D15` |
| `D33` | `=D15` |
| `D34` | `=A9` |
| `D35` | `=22*24` |
| `E35` | `=F10` |
| `F36` | `=SUM(F15:F35)` |
| `F38` | `=F36*(E38/100)` |
| `F39` | `=F36/F37` |

### 6. 4. Hidrotractor

- Faixa usada: `A1:J21`
- Fórmulas: **16**
- Conceitos provisórios: outros
- Células numéricas observadas: **36**

#### Rótulos e textos observados

- HIDROTRACTOR
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
- Locaçao Mensal
- mês
- Diesel
- vb
- Consumo Hidrotractor
- 17 litros / hora
- Container Escritório c/sanitário
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
| `D16` | `=22*17*7*24` |
| `F18` | `=SUM(F15:F17)` |
| `F20` | `=F18*(E20/100)` |
| `F21` | `=F18/F19` |

### 7. 5. Escadeira

- Faixa usada: `A1:J21`
- Fórmulas: **16**
- Conceitos provisórios: outros
- Células numéricas observadas: **36**

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
- Locaçao Mensal
- mês
- Diesel
- vb
- Consumo Escavadeira
- 23 litros / hora
- Container Escritório c/sanitário
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
| `D16` | `=22*23*7*24` |
| `F18` | `=SUM(F15:F17)` |
| `F20` | `=F18*(E20/100)` |
| `F21` | `=F18/F19` |

### 8. 6. Caminhao&Comboio

- Faixa usada: `A1:J26`
- Fórmulas: **19**
- Conceitos provisórios: outros
- Células numéricas observadas: **46**

#### Rótulos e textos observados

- Caminhao + Comboio
- Empresa R3 - Local
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Motorisa
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
- Locaçao Mensal
- mês
- Capacidade do Caminhao
- m3
- Diesel
- vb
- Consumo Caminhao
- 20 litros / hora
- Comboio
- mes
- Refeiçao Motorista
- TOTAL
- Numero de Viagens
- Prazo de Operação
- BDI (%)
- m2
- por mes
- Preço Final
- m
- espessura vegetaçao
- Volume do material
- dias
- periodo trabalho
- m3/dia
- Viagens / dia

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
| `D18` | `=2*2*22*24` |
| `F19` | `=SUM(F15:F18)` |
| `F21` | `=F19*(E21/100)` |
| `F22` | `=F19/F20` |
| `H23` | `=H21*H22` |
| `H25` | `=H23/H24` |
| `H26` | `=H25/I15` |

### 9. 7. Triturador

- Faixa usada: `A1:F22`
- Fórmulas: **16**
- Conceitos provisórios: outros
- Células numéricas observadas: **41**

#### Rótulos e textos observados

- Triturador
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Motorisa
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
- Locaçao Mensal
- mês
- Diesel
- vb
- Mob
- Desmob
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
| `D16` | `=22*7*5*24` |
| `F19` | `=SUM(F15:F18)` |
| `F21` | `=F19*(E21/100)` |
| `F22` | `=F19/F20` |

### 10. 8. Mediçao

- Faixa usada: `A1:F23`
- Fórmulas: **16**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **37**

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
- Escada 1,70m (apontador)
- vb
- Cobertura
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
| `F15` | `=D15*E15` |
| `F16` | `=D16*E16` |
| `F18` | `=SUM(F15:F17)` |
| `F19` | `=F18*(E19/100)` |
| `F20` | `=SUM(F18:F19)` |
| `F22` | `=F21*(E22/100)` |
| `F23` | `=SUM(F21:F22)` |

### 11. 9. DesMob. Hidrotractor

- Faixa usada: `A1:F20`
- Fórmulas: **17**
- Conceitos provisórios: desmobilizacao
- Células numéricas observadas: **36**

#### Rótulos e textos observados

- 1 - DesMobilização Hidrotractor
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
- Munck para descarregamento
- dia
- Mobilizaçao (HIDROTRACTOR)
- vb
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
| `E17` | `=F10` |
| `F18` | `=SUM(F15:F17)` |
| `F19` | `=F18*(E19/100)` |
| `F20` | `=SUM(F18:F19)` |

### 12. 10. DesMob. Escavadeira

- Faixa usada: `A1:F20`
- Fórmulas: **17**
- Conceitos provisórios: desmobilizacao
- Células numéricas observadas: **35**

#### Rótulos e textos observados

- 1 - Mobilização Escavadeira
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
- Munck para descarregamento
- dia
- Mobilizaçao (HIDROTRACTOR)
- vb
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
| `E17` | `=F10` |
| `F18` | `=SUM(F15:F17)` |
| `F19` | `=F18*(E19/100)` |
| `F20` | `=SUM(F18:F19)` |

### 13. 11. Plan. Preços

- Faixa usada: `A1:M14`
- Fórmulas: **26**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **70**

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
- Mobilizaçao Hidrotractor
- un
- MOB
- Mobilizaçao Escavadeira
- Canteiro de obras
- LIMPEZA
- Hidrotractor
- Escavadeira Long Reach
- Caminhao Movimentaçao + Comboio
- Triturador
- Mediçao
- DESMOB
- Desmob Hidrotractor
- Desmob Escavadeira
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Mob. Hidrotractor '!F20` |
| `G4` | `=C4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `M4` | `=J4+J5+(J6*0.1)+J11` |
| `C5` | `='2. Mob. Escavadeira'!F20` |
| `G5` | `=C5/E5` |
| `C6` | `='3. Canteiro de obras'!F36` |
| `E6` | `=45000*0.03*24` |
| `M6` | `=(J6*0.9)+J7+J8+J9+J10` |
| `C7` | `='4. Hidrotractor'!F18` |
| `E7` | `=E6` |
| `C8` | `='5. Escadeira'!F18` |
| `E8` | `=E7` |
| `C9` | `='6. Caminhao&Comboio'!F19` |
| `E9` | `=E8` |
| `C10` | `='7. Triturador'!F19` |
| `E10` | `=E9` |
| `C11` | `='8. Mediçao'!F18` |
| `M11` | `=I12+I13` |
| `C12` | `='9. DesMob. Hidrotractor'!F20` |
| `C13` | `='10. DesMob. Escavadeira'!F18` |
| `G13` | `=C13/E13` |
| `C14` | `=SUM(C4:C13)` |
| `J14` | `=SUM(J4:J13)` |
| `M14` | `=SUM(M4:M11)` |

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
