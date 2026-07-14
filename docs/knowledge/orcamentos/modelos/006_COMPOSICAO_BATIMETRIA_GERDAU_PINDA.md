# Modelo 006 — Composição - Batimetria - Gerdau Pinda.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `Composição - Batimetria - Gerdau Pinda.xlsx`
- Família provisória: **Batimetria / levantamento**
- SHA-256 do arquivo: `fff05b65ee231c9875671cd6ce61339e599d09d8bfe32167b46a52ce5319c32c`
- Abas analisadas: **7**
- Fórmulas encontradas: **125**

## Conceitos identificados

- `outros`: 3 aba(s)
- `dados_obra`: 1 aba(s)
- `medicao_batimetria`: 1 aba(s)
- `producao_prazo`: 1 aba(s)
- `resumo_comercial`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:P27` | 10 | dados_obra |
| 2 | `Produção` | `A1:H24` | 11 | producao_prazo |
| 3 | `1. Mobilização` | `A1:M40` | 32 | outros |
| 4 | `2.Amostras` | `A1:G24` | 21 | outros |
| 5 | `3. Batimetria` | `A1:F24` | 22 | medicao_batimetria |
| 6 | `4. Projeto` | `A1:F24` | 15 | outros |
| 7 | `RESUMO` | `A1:J15` | 14 | resumo_comercial |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `1. Mobilização` | 16 |
| `Dados Obra` | 11 |
| `2.Amostras` | 1 |
| `3. Batimetria` | 1 |
| `4. Projeto` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:P27`
- Fórmulas: **10**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **25**

#### Rótulos e textos observados

- Batimetria Gerdau
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- Proposta
- Proposta D_034/2025
- Data
- Cliente
- GERDAU
- Contato
- Inácio
- e-mail
- Dados da obra
- Objeto
- Batimetria das Lagoas de Estabilização
- LAGOAS
- Área (m²)
- Amostras a coletar
- Largura
- Compr
- Profund
- Quant Lagoas
- Local
- Lagoa Anaeróbias
- Volume dragagem (m³)
- (30x90x2)
- Lagoa Facultativa
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
- SubGeo ZAP em 15/05/25
- /m²
- Tipo de Bota Fora
- Sistema de Medição
- Canteiro de obras
- Mobilização
- Horário de Trabalho (das 7 as 17h)
- h/dia
- Dias de Trabalho (2ª a 6ª)
- dias/mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `K13` | `=M13*N13*P13` |
| `L13` | `=5*P13` |
| `K14` | `=M14*N14*P14` |
| `L14` | `=8*P14` |
| `H16` | `=B16+E16` |
| `H17` | `=B17+E17` |
| `K19` | `=SUM(K13:K18)` |
| `L19` | `=SUM(L13:L18)` |
| `G21` | `=B21*D21*B20` |
| `K21` | `=J22/K19` |

### 2. Produção

- Faixa usada: `A1:H24`
- Fórmulas: **11**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **8**

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
- Nº de horas trabalhadas
- #DIV/0!
- Prazo de Execução
- horas
- Dias

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
| `F22` | `=D21/D8` |
| `D24` | `=D21/D8` |
| `G24` | `=D24/9` |

### 3. 1. Mobilização

- Faixa usada: `A1:M40`
- Fórmulas: **32**
- Conceitos provisórios: outros
- Células numéricas observadas: **119**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Mão de OBRA
- Encarregado
- Salário
- com 25%
- Operador Líder
- Engº
- Ajudante Geral - pré parada
- Terceirizados (SubGeo)
- Refeições
- Operador Draga
- Transporte
- Ajudante Draga
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Container almoxarifado
- mês
- Westrock
- Container Sanitário/Vestiário
- Container Escritório c/sanitário
- Frete para Containers
- vb
- PPRA + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Placa de obra
- Vigilância
- água potável
- gl
- material de escritório
- Mobiliario Casa
- custo Exames covid
- un
- Documentação e Custo Bancodoc
- chute
- Treinamentos e acesso portal Gerdau
- dia
- Carro Peba + gasolina para viagem
- Hospedagem
- Alimentação
- Carro Aguinaldo + gasolina para viagem
- Eu
- Hospedagem + refeição
- Líder
- Equipamentos de apoio (cordas, jarros, etc)
- Ajudantes
- Integração prévia
- Operador
- R$ / dia
- Mão de obra (viagem e integração)
- TOTAL
- Prazo de Operação
- preço unitário
- #DIV/0!
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `=J7` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `=J9` |
| `C7` | `=J10` |
| `J7` | `=I7*1.25` |
| `D8` | `='Dados Obra '!B26` |
| `A9` | `=SUM(A5:A8)` |
| `F9` | `=A9*C9` |
| `J9` | `=I9*1.25` |
| `A10` | `=A9` |
| `F10` | `=A10*C10` |
| `J10` | `=I10*1.25` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `F23` | `=D23*E23` |
| `F28` | `=D28*E28` |
| `D29` | `=A9` |
| `F30` | `=D30*E30` |
| `F31` | `=D31*E31` |
| `E32` | `=M35` |
| `F32` | `=D32*E32` |
| `F33` | `=D33*E33` |
| `E34` | `=F11` |
| `F34` | `=D34*E34` |
| `E35` | `=F11` |
| `K35` | `=SUM(K31:K34)` |
| `L35` | `=SUM(L31:L34)` |
| `M35` | `=K35+L35` |
| `F36` | `=SUM(F16:F35)` |
| `F38` | `=F36/F37` |
| `F39` | `=F38*(E39/100)` |
| `F40` | `=F38+F39` |

### 4. 2.Amostras

- Faixa usada: `A1:G24`
- Fórmulas: **21**
- Conceitos provisórios: outros
- Células numéricas observadas: **44**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Operador Líder
- Ajudante Geral - pré parada
- Terceirizados (SubGeo)
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Análise laboratorial (12 amostras)
- un
- Caracterização NBR 10004
- BioAgri em 21/05/25
- viagem para levar as amostras
- vb
- Mão de obra (coleta das amostras)
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
| `C5` | `='1. Mobilização'!C5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Mobilização'!C6` |
| `A7` | `='1. Mobilização'!A7` |
| `C7` | `='1. Mobilização'!C7` |
| `A8` | `='1. Mobilização'!A8` |
| `D8` | `='Dados Obra '!B26` |
| `A9` | `=SUM(A5:A8)` |
| `C9` | `='1. Mobilização'!C9` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `C10` | `='1. Mobilização'!C10` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `D16` | `='Dados Obra '!L19` |
| `F16` | `=D16*E16` |
| `E19` | `=F11` |
| `F20` | `=SUM(F16:F19)` |
| `F22` | `=F20/F21` |
| `F23` | `=F22*(E23/100)` |
| `F24` | `=F22+F23` |

### 5. 3. Batimetria

- Faixa usada: `A1:F24`
- Fórmulas: **22**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **43**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Operador Líder
- Ajudante Geral - pré parada
- Terceirizados (SubGeo)
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Subcontratada - SUBGEO
- m²
- mobilização
- vb
- Mão de obra (acompanhamento)
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
| `C5` | `='1. Mobilização'!C5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Mobilização'!C6` |
| `A7` | `='1. Mobilização'!A7` |
| `C7` | `='1. Mobilização'!C7` |
| `D8` | `='Dados Obra '!B26` |
| `A9` | `=SUM(A5:A8)` |
| `C9` | `='1. Mobilização'!C9` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `C10` | `='1. Mobilização'!C10` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `D16` | `='Dados Obra '!K19` |
| `E16` | `='Dados Obra '!K21` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `E19` | `=F11` |
| `F20` | `=SUM(F16:F19)` |
| `F22` | `=F20/F21` |
| `F23` | `=F22*(E23/100)` |
| `F24` | `=F22+F23` |

### 6. 4. Projeto

- Faixa usada: `A1:F24`
- Fórmulas: **15**
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
- Engenheiro
- Refeições
- Transporte
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Mão de obra
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
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D8` | `='Dados Obra '!B26` |
| `A9` | `=SUM(A5:A8)` |
| `C9` | `='1. Mobilização'!C9` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `C10` | `='1. Mobilização'!C10` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `E19` | `=F11` |
| `F20` | `=SUM(F16:F19)` |
| `F22` | `=F20/F21` |
| `F23` | `=F22*(E23/100)` |
| `F24` | `=F22+F23` |

### 7. RESUMO

- Faixa usada: `A1:J15`
- Fórmulas: **14**
- Conceitos provisórios: resumo_comercial
- Células numéricas observadas: **34**

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
- Mobilização
- un
- Coleta de amostras e análise geral
- Batimetria
- Elaboração do projeto e Escopo Dragagem
- Preço de Venda
- Quantidade de m²
- Preço Unitário ( R$ / m² )
- PREÇO FINAL APRESENTADO

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Mobilização'!F36` |
| `G4` | `=C4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `C5` | `='2.Amostras'!F20` |
| `G5` | `=C5/E5` |
| `C6` | `='3. Batimetria'!F20` |
| `C7` | `='4. Projeto'!F20` |
| `G7` | `=C7/E7` |
| `C8` | `=SUM(C4:C7)` |
| `J8` | `=SUM(J4:J7)` |
| `J9` | `=J8-C8` |
| `J11` | `='Dados Obra '!K19` |
| `J12` | `=J8/J11` |

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
