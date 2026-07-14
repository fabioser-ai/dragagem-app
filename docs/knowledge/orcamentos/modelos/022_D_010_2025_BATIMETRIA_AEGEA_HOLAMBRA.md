# Modelo 022 — D_010_2025 - Batimetria Aegea Holambra.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `D_010_2025 - Batimetria Aegea Holambra.xlsx`
- Família provisória: **Batimetria / levantamento**
- SHA-256 do arquivo: `096a04ca6925f022495a4b0d6df1b3de1038d84c246fa42050a48f99ec293ebc`
- Abas analisadas: **7**
- Fórmulas encontradas: **101**

## Conceitos identificados

- `mao_obra`: 2 aba(s)
- `mobilizacao_sistema`: 2 aba(s)
- `dados_obra`: 1 aba(s)
- `desmobilizacao`: 1 aba(s)
- `formacao_preco`: 1 aba(s)
- `medicao_batimetria`: 1 aba(s)
- `outros`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:H27` | 3 | dados_obra |
| 2 | `Produção` | `A1:H24` | 8 | producao_prazo |
| 3 | `1. Mob. Equipe` | `A1:G30` | 22 | mobilizacao_sistema, mao_obra |
| 4 | `2. Batimetria Jasao` | `A1:G19` | 16 | medicao_batimetria |
| 5 | `3. Relatorio final` | `A1:F20` | 14 | outros |
| 6 | `4. Desmob. Equipe` | `A1:G28` | 20 | mobilizacao_sistema, desmobilizacao, mao_obra |
| 7 | `5. Plan. Preços` | `A1:J8` | 18 | formacao_preco |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `Dados Obra` | 4 |
| `1. Mob. Equipe` | 1 |
| `2. Batimetria Jasao` | 1 |
| `3. Relatorio final` | 1 |
| `4. Desmob. Equipe` | 1 |

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
- Proposta D_010_2025
- Data
- Cliente
- Aegea
- Contato
- e-mail
- Dados da obra
- Objeto
- Batimetria Lagoa Aeraçao e Decantaçao
- Local
- Holambra - SP
- Volume dragagem (m³)
- Tipo de material
- Lodo + Areia
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
- Batimetria
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
- Fórmulas: **8**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **11**

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
- #DIV/0!

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `H3` | `='Dados Obra '!B26` |
| `H6` | `=H3*H4` |
| `D8` | `=D3*(D4/100)*(D5/100)` |
| `D11` | `=H6` |
| `D13` | `=D8*D11` |
| `D18` | `=D13` |
| `D21` | `='Dados Obra '!B14` |
| `D24` | `=D21/D18` |

### 3. 1. Mob. Equipe

- Faixa usada: `A1:G30`
- Fórmulas: **22**
- Conceitos provisórios: mobilizacao_sistema, mao_obra
- Células numéricas observadas: **63**

#### Rótulos e textos observados

- 1 - Mobilização Barco
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
- Peba
- Operador de Draga
- Operador de preparo de polímero
- Ajudante Geral
- Leonardo
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
- Treinamentos (Trabalho em Altura e espaço confinado)
- Mobiliário Canteiro
- vb
- Carreta Carga Seca para DRAGA
- un
- Guindaste p/descarregamento e montagem DRAGA
- chute
- Documentação
- Combustivel + Frete
- Frete
- Trator D4 para lançar draga na água
- Mão de obra p/carga e montagem (r$/dia)
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=A5+A8+A6+A7` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `F22` | `=D22*E22` |
| `F23` | `=D23*E23` |
| `E25` | `=F11` |
| `F26` | `=SUM(F16:F25)` |
| `F27` | `=F26*(E27/100)` |
| `F28` | `=SUM(F26:F27)` |
| `F30` | `=SUM(F28:F29)` |

### 4. 2. Batimetria Jasao

- Faixa usada: `A1:G19`
- Fórmulas: **16**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **31**

#### Rótulos e textos observados

- 3. PREPARO DE CÉLULA - Manta PEAD
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
- Batimetria (JASAO)
- vb
- Preço passado 26/02/2025 - Zap Jasao
- Mão de obra acompanhameto (FOS)
- dia
- TOTAL
- Quantidade de Repetiçoes
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
| `E16` | `=F10` |
| `F17` | `=SUM(F15:F16)` |
| `F18` | `=F17*E18` |
| `F19` | `=F18` |

### 5. 3. Relatorio final

- Faixa usada: `A1:F20`
- Fórmulas: **14**
- Conceitos provisórios: outros
- Células numéricas observadas: **35**

#### Rótulos e textos observados

- 4. Relatorio Final
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Engenheiro
- Operador de Draga
- Operador de preparo de polímero
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
- Relatorio Final (DWG, Adaptaçao , ETC)
- vb
- Coleta + Analise amostra
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
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `F18` | `=SUM(F16:F17)` |
| `F19` | `=F18*(E19/100)` |
| `F20` | `=SUM(F18:F19)` |

### 6. 4. Desmob. Equipe

- Faixa usada: `A1:G28`
- Fórmulas: **20**
- Conceitos provisórios: mobilizacao_sistema, desmobilizacao, mao_obra
- Células numéricas observadas: **53**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 6"
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
- Operador de Draga
- Operador de preparo de polímero
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
- Treinamentos (Trabalho em Altura e espaço confinado)
- Mobiliário Canteiro
- vb
- Carreta Carga Seca para DRAGA
- un
- Guindaste p/descarregamento e montagem DRAGA
- chute
- Frete
- Trator D4 para lançar draga na água
- Mão de obra p/carga e montagem (r$/dia)
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=A5+A8+A6+A7` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `F20` | `=D20*E20` |
| `F21` | `=D21*E21` |
| `E23` | `=F11` |
| `F24` | `=SUM(F16:F23)` |
| `F25` | `=F24*(E25/100)` |
| `F26` | `=SUM(F24:F25)` |
| `F28` | `=SUM(F26:F27)` |

### 7. 5. Plan. Preços

- Faixa usada: `A1:J8`
- Fórmulas: **18**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **30**

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
- Mobilizaçao Barco
- un
- Batimetria Jasao
- m²
- Relatorio final
- m³
- Desmobilização Barco
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Mob. Equipe'!F30` |
| `G4` | `=C4/E4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `C5` | `='2. Batimetria Jasao'!F19` |
| `G5` | `=C5/E5` |
| `I5` | `=((H5/100)+1)*G5` |
| `J5` | `=E5*I5` |
| `C6` | `='3. Relatorio final'!F20` |
| `G6` | `=C6/E6` |
| `I6` | `=((H6/100)+1)*G6` |
| `J6` | `=E6*I6` |
| `C7` | `='4. Desmob. Equipe'!F28` |
| `G7` | `=C7/E7` |
| `I7` | `=((H7/100)+1)*G7` |
| `J7` | `=E7*I7` |
| `C8` | `=SUM(C5:C7)` |
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
