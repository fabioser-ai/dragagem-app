# Modelo 048 — Motobomba 3Barras - Westrock.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `Motobomba 3Barras - Westrock.xlsx`
- Família provisória: **Equipamento / motobomba**
- SHA-256 do arquivo: `91b9518652bd9ccfacf48ceff5c46ad113dcefdbd676266ecf8f9b493f04f4d6`
- Abas analisadas: **3**
- Fórmulas encontradas: **28**

## Conceitos identificados

- `dados_obra`: 1 aba(s)
- `equipamento`: 1 aba(s)
- `formacao_preco`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:H27` | 3 | dados_obra |
| 2 | `MOTOBOMBA` | `A1:F23` | 15 | equipamento |
| 3 | `10. Plan. Preços` | `A1:J7` | 10 | formacao_preco |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `Dados Obra` | 2 |

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
- D_040_2025
- Data
- Cliente
- WESTROCK
- Contato
- e-mail
- Dados da obra
- Objeto
- Locaçao Motobomba
- Local
- Tres Barras
- Volume dragagem (m³)
- Tipo de material
- Lodo - ETA
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
- Bombeamento Direto
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

### 2. MOTOBOMBA

- Faixa usada: `A1:F23`
- Fórmulas: **15**
- Conceitos provisórios: equipamento
- Células numéricas observadas: **49**

#### Rótulos e textos observados

- Locaçao Motobomba
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
- vb
- Mobilizaçao
- Startup
- Desmob
- Hospedagem Funcionários
- Mão de obra de instal. Bidim e Brita
- dia
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D5` | `='Dados Obra '!B26` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `='Dados Obra '!B26` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7+A6` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `F15` | `=D15*E15` |
| `E20` | `=F10` |
| `F21` | `=SUM(F15:F20)` |
| `F22` | `=F21*(E22/100)` |
| `F23` | `=SUM(F21:F22)` |

### 3. 10. Plan. Preços

- Faixa usada: `A1:J7`
- Fórmulas: **10**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **23**

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
- Mobilizaçao e montagem Motobomba
- vb
- Locaçao e Operação Motobomba
- Desmobilizaçao Equipamento Motobomba
- Preço de Venda

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `=MOTOBOMBA!F16` |
| `G4` | `=C4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `C5` | `=MOTOBOMBA!F23-(MOTOBOMBA!F16+MOTOBOMBA!F18)` |
| `G5` | `=C5/E5` |
| `C6` | `=MOTOBOMBA!F18` |
| `G6` | `=C6/E6` |
| `C7` | `=SUM(C4:C6)` |
| `J7` | `=SUM(J4:J6)` |

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
