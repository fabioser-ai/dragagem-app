# Modelo 034 — D_048_2025_REV03 - Suzano 3 Lagoas - Bags - Aguinaldo Bags em 2 níveis.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `D_048_2025_REV03 - Suzano 3 Lagoas - Bags - Aguinaldo Bags em 2 níveis.xlsx`
- Família provisória: **Dragagem com bags/geotêxteis**
- SHA-256 do arquivo: `f66aa253db40f26740e1fa460f1ff925f3773d19aa9506ccbe8247f06c4bc33c`
- Abas analisadas: **17**
- Fórmulas encontradas: **688**

## Conceitos identificados

- `outros`: 6 aba(s)
- `desmobilizacao`: 2 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `bags_geotexteis`: 1 aba(s)
- `barrilete_linha`: 1 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `estrutura_desaguamento`: 1 aba(s)
- `formacao_preco`: 1 aba(s)
- `medicao_batimetria`: 1 aba(s)
- `producao_prazo`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:P27` | 13 | dados_obra |
| 2 | `Dados técnicos` | `A1:H9` | 13 | outros |
| 3 | `Produção` | `A1:I27` | 13 | producao_prazo |
| 4 | `1.1. Canteiro` | `A1:P38` | 40 | canteiro |
| 5 | `1.2. Mob Draga + Pol.` | `A1:N36` | 57 | mobilizacao_draga |
| 6 | `1.2.1.Barrilete` | `A1:F31` | 39 | barrilete_linha |
| 7 | `2. Prep Célula` | `A1:O39` | 61 | estrutura_desaguamento |
| 8 | `3.1. Bags` | `A1:M54` | 75 | bags_geotexteis |
| 9 | `3.2 Draga` | `A1:L207` | 89 | outros |
| 10 | `3.3 Op.Planta` | `A1:M36` | 40 | outros |
| 11 | `3.4.Medição` | `A1:K28` | 29 | medicao_batimetria |
| 12 | `3.5.Drenagem Lagoas` | `A1:K20` | 30 | outros |
| 13 | `4.Reparo PEAD` | `A1:J19` | 31 | outros |
| 14 | `5.1. DesMob Draga + Pol.` | `A1:G36` | 52 | mobilizacao_draga, desmobilizacao |
| 15 | `5.2. Desmob Final` | `A1:N38` | 36 | desmobilizacao |
| 16 | `Plan. BDI` | `A1:K24` | 49 | formacao_preco |
| 17 | `Plan. Final.` | `A1:N7` | 21 | outros |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `1.1. Canteiro` | 87 |
| `Dados Obra` | 23 |
| `3.3 Op.Planta` | 13 |
| `Plan. BDI` | 10 |
| `1.2. Mob Draga + Pol.` | 5 |
| `3.1. Bags` | 3 |
| `3.4.Medição` | 3 |
| `5.2. Desmob Final` | 3 |
| `1.2.1.Barrilete` | 2 |
| `2. Prep Célula` | 2 |
| `3.2 Draga` | 2 |
| `4.Reparo PEAD` | 2 |
| `3.5.Drenagem Lagoas` | 1 |
| `5.1. DesMob Draga + Pol.` | 1 |
| `[1]Dados Obra` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:P27`
- Fórmulas: **13**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **39**

#### Rótulos e textos observados

- 048_2025_Rev3
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- Proposta
- Proposta D_048_2025_R03
- Data
- LEGENDA ATUAL REVISÃO
- Cliente
- SUZANO - 3 lagoas
- Revisão 03 - 05/12/25
- Contato
- Thamires
- e-mail
- Dados da obra
- Objeto
- DRAGAGEM LAGOAS L6,L7,L8 e POLIMENTO
- NOVO ESCOPO
- Volume
- %ST in situ
- Densidade
- % ST desaguado Sugerido
- M3 base seca
- Volume Desaguado
- Local
- TRES LAGOAS
- Volume de lodo a dragar L6
- Volume dragagem (m³)
- Volume de lodo a dragar L7
- Tipo de material
- Efluente industríal Papel
- Volume de lodo a dragar L8
- Distância de Recalque (m)
- Seio da linha =
- Total
- Volume de lodo a dragar Polimento
- Linha Flutuante (m)
- Linha de terra (m)
- Profundidade de dragagem (m)
- Espessura média de dragagem (m)
- Área de Dragagem (m² ou L x C)
- X
- Volume (m³) =
- Tipo de Bota Fora
- Bags
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
| `N13` | `=L13*1.5` |
| `O13` | `=K13*L13` |
| `P13` | `=O13/N13` |
| `B14` | `=K17` |
| `N14` | `=L14*1.5` |
| `O14` | `=K14*L14` |
| `P14` | `=O14/N14` |
| `H16` | `=B16+E16` |
| `H17` | `=B17+E17` |
| `K17` | `=SUM(K13:K16)` |
| `O17` | `=SUM(O13:O16)` |
| `P17` | `=SUM(P13:P16)` |
| `G21` | `=B21*D21*B20` |

### 2. Dados técnicos

- Faixa usada: `A1:H9`
- Fórmulas: **13**
- Conceitos provisórios: outros
- Células numéricas observadas: **24**

#### Rótulos e textos observados

- LAGOAS
- Volume de Lodo a Dragar (m³)
- % ST in situ
- % ST desaguado
- Volume de Lodo em Base Seca (m³)
- Volume de Lodo Desaguado (m³)
- Lagoa 06
- Lagoa 07
- Lagoa 08
- Lagoa de Polimento
- TOTAL
- Limitação da SUZANO para Carregamento, transporte e Destinação do Lodo Desaguado em 1.500 ton por mês (fator que aumenta consideravelmente o prazo de execução da obra e consequentemente o custo)
- Produção limitante da Suzano (m³ desaguado/mês)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F2` | `='Dados Obra '!N13` |
| `G2` | `=D2*E2` |
| `H2` | `=G2/F2` |
| `F3` | `='Dados Obra '!N14` |
| `G3` | `=D3*E3` |
| `H3` | `=G3/F3` |
| `F4` | `='Dados Obra '!N15` |
| `G4` | `=D4*E4` |
| `F5` | `='Dados Obra '!N16` |
| `G5` | `=D5*E5` |
| `D6` | `=SUM(D2:D5)` |
| `G6` | `=SUM(G2:G5)` |
| `H6` | `=SUM(H2:H5)` |

### 3. Produção

- Faixa usada: `A1:I27`
- Fórmulas: **13**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **21**

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
- PRAZO EXECUÇÃO
- Canteiro
- Mobiliz. Draga
- Quantidade total a dragar
- m³
- Preparo Célula
- Dragagem Bags
- Desmob. Draga
- Prazo de Execução
- mês
- Desmobilização
- TOTAL
- Mobilizações
- Operação

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
| `H21` | `=D27` |
| `D23` | `=ROUNDUP(D20/D17,0)` |
| `E23` | `=D20/D17` |
| `H25` | `=SUM(H18:H24)` |
| `D27` | `=D23` |

### 4. 1.1. Canteiro

- Faixa usada: `A1:P38`
- Fórmulas: **40**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **150**

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
- Operador Draga
- Operador de Draga
- Opera bomba sub
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
- igualando orçamento com proposta da paliçada
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
| `C5` | `=M5` |
| `D5` | `='Dados Obra '!B26*'1.1. Canteiro'!N5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `M5` | `=J5+K5+L5` |
| `D6` | `='Dados Obra '!B26` |
| `J6` | `=I6/220` |
| `L6` | `=(J6+K6)*0.25` |
| `M6` | `=J6+K6+L6` |
| `D7` | `=D6` |
| `D8` | `=D7` |
| `M8` | `=J8+K8+L8` |
| `D9` | `=D8` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `A12` | `=SUM(A5:A11)` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `F13` | `=A13*C13` |
| `M13` | `=J13+K13+L13` |
| `F14` | `=SUM(F5:F13)` |
| `D18` | `=Produção!H25` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `D20` | `=D18` |
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
| `F35` | `='1.1. Canteiro'!D18` |
| `F36` | `=F34/F35` |
| `F37` | `=F36*(E37/100)` |
| `F38` | `=F36+F37` |

### 5. 1.2. Mob Draga + Pol.

- Faixa usada: `A1:N36`
- Fórmulas: **57**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **130**

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
- Fabiano R$ 9.800,00 + 0,2%
- Carreta Carga Seca - Eqto Polímero
- Zap de 22/04/25
- Guindaste p/descarregamento e montagem DRAGA
- cadeira
- Instalações hidráulicas
- armário escritório
- Instalações elétricas
- cestos lixo
- Máquina Wap
- Barrilete
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
| `A5` | `='1.1. Canteiro'!A5` |
| `C5` | `='1.1. Canteiro'!C5` |
| `D5` | `='1.1. Canteiro'!D5` |
| `E5` | `='1.1. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='1.1. Canteiro'!A6` |
| `C6` | `='1.1. Canteiro'!C6` |
| `D6` | `='1.1. Canteiro'!D6` |
| `E6` | `=E5` |
| `A7` | `='1.1. Canteiro'!A7` |
| `C7` | `='1.1. Canteiro'!C7` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `A8` | `='1.1. Canteiro'!A8` |
| `C8` | `='1.1. Canteiro'!C8` |
| `D8` | `=D7` |
| `E8` | `=E7` |
| `A9` | `='1.1. Canteiro'!A9` |
| `C9` | `='1.1. Canteiro'!C9` |
| `D9` | `=D6` |
| `E9` | `=E8` |
| `A10` | `='1.1. Canteiro'!A10` |
| `C10` | `='1.1. Canteiro'!C10` |
| `D10` | `=D6` |
| `E10` | `=E9` |
| `A11` | `=SUM(A5:A10)` |
| `C11` | `='1.1. Canteiro'!C12` |
| `F11` | `=A11*C11` |
| `A12` | `=A11` |
| `C12` | `='1.1. Canteiro'!C13` |
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
| `E27` | `='1.2.1.Barrilete'!F29` |
| `F27` | `=D27*E27` |
| `F28` | `=D28*E28` |
| `E29` | `=F13` |
| `F30` | `=SUM(F16:F29)` |
| `F31` | `=F30*(E31/100)` |
| `N31` | `=SUM(N19:N30)` |
| `F32` | `=SUM(F30:F31)` |

### 6. 1.2.1.Barrilete

- Faixa usada: `A1:F31`
- Fórmulas: **39**
- Conceitos provisórios: barrilete_linha
- Células numéricas observadas: **82**

#### Rótulos e textos observados

- Composição - BARRILETE - unidade: Global
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Operador de Draga + técnico operação polím.
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
- Tubo de ferro c/6m diametro de 8"
- pç
- Toco 0,50m
- Joelho 90°
- Tee 6" x 4" flangeado
- Ponteira flange x escama diam. 4"
- Cap. 6"
- Válvula Gaveta 4"
- Válvula Gaveta 3"
- Mangueira Conduto d'água
- m
- Braçadeiras
- Curva longa de PVC 4"
- Válvula esfera 2"
- Bomba lameira
- Mão de obra de montagem
- dia
- TOTAL
- 30 % de depreciação
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `='1.2. Mob Draga + Pol.'!A7` |
| `C4` | `='1.1. Canteiro'!C7` |
| `D4` | `='1.1. Canteiro'!D6` |
| `E4` | `='1.1. Canteiro'!E5` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `A5` | `='1.2. Mob Draga + Pol.'!A9` |
| `C5` | `='1.1. Canteiro'!C9` |
| `D5` | `='1.1. Canteiro'!D6` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='1.2. Mob Draga + Pol.'!A10` |
| `C6` | `='1.1. Canteiro'!C10` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A4+A6` |
| `C7` | `='1.1. Canteiro'!C12` |
| `F7` | `=A7*C7` |
| `A8` | `=A4+A6` |
| `C8` | `='1.1. Canteiro'!C13` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F4:F8)` |
| `E14` | `=400*1.4` |
| `F14` | `=D14*E14` |
| `E15` | `=165*1.4` |
| `E16` | `=165*1.4` |
| `E17` | `=220*1.4` |
| `E18` | `=55*1.4` |
| `E19` | `=35*1.4` |
| `E20` | `=2000*1.4` |
| `E21` | `=1100*1.4` |
| `E23` | `=14*1.4` |
| `E24` | `=35*1.4` |
| `E25` | `=60*1.4` |
| `E27` | `=F9` |
| `F28` | `=SUM(F14:F27)` |
| `F29` | `=F28*0.3` |
| `F30` | `=F29*(E30/100)` |
| `F31` | `=F29+F30` |

### 7. 2. Prep Célula

- Faixa usada: `A1:O39`
- Fórmulas: **61**
- Conceitos provisórios: estrutura_desaguamento
- Células numéricas observadas: **141**

#### Rótulos e textos observados

- PREPARO DE CÉLULA
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Engenheiro
- Área da
- Quant.
- Aux Técnico
- Composição Real
- Célua
- total
- Encarregado
- Manta PEAD
- m²/m² de Célula
- m²
- Operador de Draga
- Bidim
- Op. Polímero
- Brita
- m³/m² de Célula
- m³
- Ajudante
- Retro escavadeira
- h/m² de Célula
- h
- Mão de Obra
- Refeições
- (4 oficiais + 6 ajudantes)
- dias
- Transporte
- Custo por dia
- CÉLULAS
- largura
- Compr.
- Área M²
- Nº Vezes
- Célula 1
- Célula 2
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Preparo Terreno - Patrola / tratos de esteira
- dia
- Mobilização da Patrol
- Disposição dos Bags na célula
- 1º Nível - 3 lilnhas com 17 bags cada
- Preparo Terreno - Aluguel de Retro
- 2º Nível - 3 linhas com 16 bags
- Mobilização/desmobilização de Retro
- Largura
- m
- Regularização manual - Mão de obra
- Comprimento
- PEAD
- Preço Danlo - Curitiba
- Mão de obra instal. PEAD
- taxa Mobilizaçao PEAD Mao de obras
- vb
- Bidim RT 07 (4,90 x 100m)
- Brita 2
- consultado junto a empresa Porto de Areia 3 irmãos em Três lagoas
- Frete para entregar Brita
- viagens
- (67) 99965-8472 / 3522-8857 / 3522-4442
- Frete para entregar na Suzano = R$ 800,00 por viagem de 12m³
- GEOCOMPOSTO DRENANTE (rolo 2x30m)
- Frete do Geocomposto Drenante
- frete consultado Fabiano R$ 9.500 + 0,2% adv em 02/10/25
- Retro escavadeira para espalhamento Brita
- Geocomposto Drenante - empresa Geomembrana (Thales gerente comercial)
- Mão de obra de instal. Bidim e Brita
- mes
- Frete FOB (considerei Fabiano em Graneleira levando 72 rolos por viagem)
- TOTAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='1.1. Canteiro'!C5` |
| `D5` | `='1.1. Canteiro'!D5` |
| `E5` | `='1.1. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1.1. Canteiro'!C6` |
| `D6` | `='1.1. Canteiro'!D6` |
| `E6` | `=E5` |
| `C7` | `='1.1. Canteiro'!C7` |
| `D7` | `=D6` |
| `M7` | `=M17` |
| `N7` | `=J7*M7` |
| `C8` | `='1.1. Canteiro'!C8` |
| `D8` | `=D7` |
| `M8` | `=M7` |
| `N8` | `=J8*M8` |
| `C9` | `='1.1. Canteiro'!C9` |
| `D9` | `=D8` |
| `M9` | `=M7` |
| `N9` | `=J9*M9` |
| `C10` | `='1.1. Canteiro'!C10` |
| `D10` | `=D9` |
| `M10` | `=M9` |
| `N10` | `=J10*M10` |
| `D11` | `=D10` |
| `M11` | `=M10` |
| `N11` | `=J11*M11` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='1.1. Canteiro'!C12` |
| `F12` | `=A12*C12` |
| `N12` | `=N11/8` |
| `A13` | `=A12` |
| `C13` | `='1.1. Canteiro'!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `I15` | `=L21` |
| `J15` | `=L22` |
| `K15` | `=I15*J15` |
| `M15` | `=K15*L15` |
| `M16` | `=K16*L16` |
| `M17` | `=SUM(M15:M16)` |
| `F18` | `=D18*E18` |
| `L21` | `=(J21*K21)+1+1+0.5+0.5` |
| `E22` | `=F14` |
| `L22` | `=(J22*K22)+1+1+0.5+0.5` |
| `D23` | `=N7` |
| `D24` | `=D23` |
| `D26` | `=N8` |
| `D27` | `=N9*1.1` |
| `D28` | `=D27/12` |
| `D30` | `=M17*1.1` |
| `E30` | `=M33` |
| `D31` | `=M37` |
| `F31` | `=D31*E31` |
| `E33` | `=E20` |
| `E34` | `=F14` |
| `F34` | `=D34*E34` |
| `F35` | `=SUM(F18:F34)` |
| `F37` | `=F35/F36` |
| `M37` | `=ROUNDUP(D30/K37,0)` |
| `F38` | `=F37*(E38/100)` |
| `F39` | `=F37+F38` |

### 8. 3.1. Bags

- Faixa usada: `A1:M54`
- Fórmulas: **75**
- Conceitos provisórios: bags_geotexteis
- Células numéricas observadas: **198**

#### Rótulos e textos observados

- FORNECIMENTO E OPERAÇÃO DE BAGS
- Nº Func.
- Mão de obra montagem canteiro
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
- P13 X 20
- un
- VOLUME A DRAGAR
- m³
- P13 X 25
- % ST in situ
- P18 X 25
- Volume SECO
- m³ seco
- P18 X 30
- P20 X 20
- % ST desaguado
- P20 X 25
- VOLUME DESAGUADO
- Quant. Bag P18 x 30
- P18 X 40
- P18 X 45
- Vol. Seco
- % ST des Bacia
- % ST des BAG
- Volume Desag. Bag
- LAGOA 6
- MÃO DE OBRA DE ESPALHAMENTO
- dia
- LAGOA 7
- TOTAL
- LAGOA 8
- Prazo de Operação
- POLIMENTO
- preço unitário
- BDI (%)
- Preço Final
- CÉLULA - 1
- Preços praticados em 2025 nas obras Chapecó e Curitiba R$ 55,00/m²
- Área Seção a 2,30m
- Comprimento
- Volume
- Quant Bags
- Volume total
- Perímetro
- Compr.
- R$ / m²
- Data
- R$ do Bag
- 2º nível
- 1º Nível
- P18 X 20
- CAPACIDADE DA CÉLULA - 1
- CÉLULA - 2
- v
- CAPACIDADE DA CÉLULA - 2

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='1.1. Canteiro'!C5` |
| `D5` | `='1.1. Canteiro'!D5` |
| `E5` | `='1.1. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1.1. Canteiro'!C6` |
| `D6` | `='1.1. Canteiro'!D6` |
| `E6` | `=E5` |
| `C7` | `='1.1. Canteiro'!C7` |
| `D7` | `=D6` |
| `C8` | `='1.1. Canteiro'!C8` |
| `D8` | `=D7` |
| `C9` | `='1.1. Canteiro'!C9` |
| `D9` | `=D8` |
| `C10` | `='1.1. Canteiro'!C10` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='1.1. Canteiro'!C12` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `C13` | `='1.1. Canteiro'!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `E18` | `=M38` |
| `F18` | `=D18*E18` |
| `I18` | `='Dados Obra '!B14` |
| `D20` | `=E49` |
| `E20` | `=M49` |
| `I20` | `=I31` |
| `D21` | `=E41+E50` |
| `E21` | `=M41` |
| `I23` | `='Dados Obra '!P17` |
| `E24` | `=M48` |
| `I24` | `=I23/D41` |
| `E25` | `=M49` |
| `E26` | `=M50` |
| `I27` | `='Dados Obra '!O13` |
| `L27` | `=J27*1.5` |
| `M27` | `=I27/L27` |
| `E28` | `=F14` |
| `I28` | `='Dados Obra '!O14` |
| `L28` | `=J28*1.5` |
| `M28` | `=I28/L28` |
| `F29` | `=SUM(F18:F28)` |
| `I29` | `='Dados Obra '!O15` |
| `L29` | `=J29*1.5` |
| `I30` | `='Dados Obra '!O16` |
| `L30` | `=J30*4` |
| `F31` | `=F29/F30` |
| `I31` | `=SUM(I27:I30)` |
| `M31` | `=SUM(M27:M30)` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |
| `D38` | `=B38*C38` |
| `F38` | `=D38*E38` |
| `M38` | `=(I38*J38)*K38` |
| `K40` | `=K39` |
| `D41` | `=B41*C41` |
| `E41` | `=(3*17)+2` |
| `K41` | `=K40` |
| `K42` | `=K41` |
| `K43` | `=K42` |
| `F44` | `=SUM(F38:F43)` |
| `D47` | `=B47*C47` |
| `F47` | `=D47*E47` |
| `M48` | `=(I48*J48)*K48` |
| `E49` | `=1*16` |
| `K49` | `=K48` |
| `M49` | `=(I49*J49)*K49` |
| `E50` | `=2*16` |
| `K50` | `=K49` |
| `M50` | `=(I50*J50)*K50` |
| `F53` | `=SUM(F47:F52)` |
| `F54` | `=F44+F53` |
| `G54` | `=G53` |

### 9. 3.2 Draga

- Faixa usada: `A1:L207`
- Fórmulas: **89**
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
| `D20` | `='1.1. Canteiro'!C5` |
| `E20` | `=D20*B20*A20` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `D21` | `='1.1. Canteiro'!C6` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `B22` | `='1.1. Canteiro'!A7` |
| `D22` | `='1.1. Canteiro'!C7` |
| `A23` | `=L24` |
| `B23` | `='1.1. Canteiro'!A8` |
| `D23` | `='1.1. Canteiro'!C8` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `D24` | `='1.1. Canteiro'!C9` |
| `L24` | `=(L20*1.7)+(L21*2)+L23` |
| `A25` | `=L24` |
| `D25` | `='1.1. Canteiro'!C10` |
| `A26` | `=L24` |
| `A27` | `=L24` |
| `E27` | `=D27*B27*A27` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `A37` | `='1.1. Canteiro'!E5` |
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
| `E108` | `=D108*B108` |
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
| `D201` | `=Produção!H21` |
| `J201` | `=D200` |
| `D202` | `=D200*D201` |
| `J203` | `=J201*J202` |
| `L203` | `=J203/J204` |
| `L205` | `=L203*L204` |
| `J206` | `=J204*J205` |
| `J207` | `=J203/J206` |

### 10. 3.3 Op.Planta

- Faixa usada: `A1:M36`
- Fórmulas: **40**
- Conceitos provisórios: outros
- Células numéricas observadas: **85**

#### Rótulos e textos observados

- PREPARO DE CÉLULA
- Nº Func.
- Mão de obra montagem canteiro
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
- Equipamento de Polímero - cotado com Gratt em 07/01/22
- JONAS - ZAP AGUINALDO 5/5/25
- Refeições
- UAP de 10 m³ + bombas de 10m³/h
- Transporte
- UAP de 20 m³ + bombas de 20m³/h
- Gratt 07/jan/22
- Custo por dia
- Tanques de 5 m³ + bombas de 10m³/h
- chute
- Tanques de 10 m³ + bombas de 20m³/h
- Valor orçado com 30% adicional - estimativa 2023
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Custo Depreciação - Equitº Preparo Polímero
- mês
- #NAME?
- Depreciação em
- meses
- Custo manutenção - Equitº Preparo Polímero
- Polimero (calculado sobre base seca)
- kg
- Repassado para Suzano
- Frete Polimero
- un
- (Caminhao Pipa) fornecimento de água para operação
- mes
- (Gerador) fornecimento de energia para operação + diesel
- Fornecimento Suzano (Agua + Eletrica)
- Instalações hidráulicas
- vb
- Instalações eletrica
- Máquina Wap
- Mão de obra para operação do sistema
- TOTAL
- Horas/ mês
- Prazo de Operação
- h/dia
- preço unitário
- #DIV/0!
- dias
- BDI (%)
- Preço Final
- Quantidade de lodo em tonelada seca
- TS
- Consumo de polímero
- kg/TS

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='1.1. Canteiro'!C5` |
| `D5` | `='1.1. Canteiro'!D5` |
| `E5` | `='1.1. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1.1. Canteiro'!C6` |
| `D6` | `='1.1. Canteiro'!D6` |
| `E6` | `=E5` |
| `C7` | `='1.1. Canteiro'!C7` |
| `D7` | `=D6` |
| `C8` | `='1.1. Canteiro'!C8` |
| `D8` | `=D7` |
| `C9` | `='1.1. Canteiro'!C9` |
| `D9` | `=D8` |
| `C10` | `='1.1. Canteiro'!C10` |
| `D10` | `=D9` |
| `D11` | `=D10` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='1.1. Canteiro'!C12` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `C13` | `='1.1. Canteiro'!C13` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `L15` | `=257000*1.3` |
| `D18` | `=Produção!H21` |
| `E18` | `=M12/J18` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `E19` | `=E18*0.1` |
| `D20` | `=D36` |
| `E23` | `=4500+2500` |
| `D27` | `=D18*J30` |
| `E27` | `=F14` |
| `F28` | `=SUM(F18:F27)` |
| `F30` | `=F28/F29` |
| `J30` | `=ROUNDUP(J28/J29,0)` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=F30+F31` |
| `D34` | `='Dados Obra '!O17` |
| `D36` | `=D34*D35` |

### 11. 3.4.Medição

- Faixa usada: `A1:K28`
- Fórmulas: **29**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **56**

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
- Batimetria L6
- m2
- JASAO GERDAU 2,18
- Batimetria L7
- Batimetria L8
- Batimetria POL
- COLETA BACIA
- un
- dias
- Quantidade de bags
- Acompanhamento FOS
- dia
- TOTAL
- Nº de medições de cada bag
- BDI (%)
- Prazo de execução
- #NAME?
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `E8` | `=E7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=SUM(A5:A8)` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `E17` | `=E16` |
| `F17` | `=D17*E17` |
| `E18` | `=E16` |
| `E19` | `=E16` |
| `D20` | `=H22*K23` |
| `D22` | `=(K24-1)*0.5` |
| `E22` | `=F11` |
| `H22` | `='3.1. Bags'!D20+'3.1. Bags'!D21` |
| `F23` | `=SUM(F16:F22)` |
| `F24` | `=F23*(E24/100)` |
| `K24` | `=Produção!H21` |
| `F25` | `=SUM(F23:F24)` |
| `F27` | `=F26*(E27/100)` |
| `F28` | `=SUM(F26:F27)` |

### 12. 3.5.Drenagem Lagoas

- Faixa usada: `A1:K20`
- Fórmulas: **30**
- Conceitos provisórios: outros
- Células numéricas observadas: **45**

#### Rótulos e textos observados

- Drenagem das Lagoas
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
- Vazão da bomba p/água
- m³/h
- Transporte
- Horas Trabalhadas por dia
- Custo por dia
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Volume
- materiais diversos para apoio para drenagem
- vb
- LAGOA 6
- LAGOA 7
- Drenagem das lagoas
- dias
- LAGOA 8
- Mão de obra de limpeza fina
- dia
- POLIMENTO
- TOTAL
- Preço Final
- Volume de lodo
- Produção diária m³/dia
- m³/dia
- Prazo

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='3.3 Op.Planta'!C7` |
| `D4` | `='3.3 Op.Planta'!D6` |
| `E4` | `='3.3 Op.Planta'!E5` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `='3.3 Op.Planta'!C8` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='3.3 Op.Planta'!C10` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A4+A6+A5` |
| `C7` | `='3.3 Op.Planta'!C12` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `C8` | `='3.4.Medição'!C10` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F4:F8)` |
| `F12` | `=D12*E12` |
| `D15` | `=ROUNDUP(J20,0)` |
| `E15` | `='3.2 Draga'!D200/'Dados Obra '!B27` |
| `E16` | `=F9` |
| `F16` | `=D16*E16` |
| `F17` | `=SUM(F12:F16)` |
| `J17` | `=SUM(J13:J16)` |
| `F18` | `=F17` |
| `J18` | `='Dados Obra '!K17` |
| `J19` | `=J7*J8` |
| `J20` | `=(J17-J18)/J19` |

### 13. 4.Reparo PEAD

- Faixa usada: `A1:J19`
- Fórmulas: **31**
- Conceitos provisórios: outros
- Células numéricas observadas: **47**

#### Rótulos e textos observados

- Reaparo da Manta de fundo da lagoa
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
- Área
- Quant Lagoas
- PEAD
- m²
- Mao de Obra Instalaçao PEAD
- LAGOA 6
- Taxa de Mobilizaçao PEAD
- LAGOA 7
- LAGOA 8
- Mão de obra
- dia
- POLIMENTO
- TOTAL
- Preço Final
- Volume de lodo
- Quantidade de Dias por lagoa

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='3.3 Op.Planta'!C7` |
| `D4` | `='3.3 Op.Planta'!D6` |
| `E4` | `='3.3 Op.Planta'!E5` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `='3.3 Op.Planta'!C8` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='3.3 Op.Planta'!C10` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A4+A6+A5` |
| `C7` | `='3.3 Op.Planta'!C12` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `C8` | `='3.4.Medição'!C10` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F4:F8)` |
| `D12` | `=I17` |
| `F12` | `=D12*E12` |
| `D13` | `=D12` |
| `D14` | `=J17` |
| `D16` | `=J17*J19` |
| `E16` | `=F9` |
| `F16` | `=D16*E16` |
| `F17` | `=SUM(F12:F16)` |
| `I17` | `=SUM(I12:I16)` |
| `J17` | `=SUM(J13:J16)` |
| `F18` | `=F17` |
| `J18` | `='[1]Dados Obra '!N17` |

### 14. 5.1. DesMob Draga + Pol.

- Faixa usada: `A1:G36`
- Fórmulas: **52**
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
- Fabiano R$ 9.800,00 + 0,2%
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
| `A5` | `='1.1. Canteiro'!A5` |
| `C5` | `='1.1. Canteiro'!C5` |
| `D5` | `='1.1. Canteiro'!D5` |
| `E5` | `='1.1. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='1.1. Canteiro'!A6` |
| `C6` | `='1.1. Canteiro'!C6` |
| `D6` | `='1.1. Canteiro'!D6` |
| `E6` | `=E5` |
| `A7` | `='1.1. Canteiro'!A7` |
| `C7` | `='1.1. Canteiro'!C7` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `A8` | `='1.1. Canteiro'!A8` |
| `C8` | `='1.1. Canteiro'!C8` |
| `D8` | `=D7` |
| `E8` | `=E7` |
| `A9` | `='1.1. Canteiro'!A9` |
| `C9` | `='1.1. Canteiro'!C9` |
| `D9` | `=D6` |
| `E9` | `=E8` |
| `A10` | `='1.1. Canteiro'!A10` |
| `C10` | `='1.1. Canteiro'!C10` |
| `D10` | `=D6` |
| `E10` | `=E9` |
| `A11` | `=SUM(A5:A10)` |
| `C11` | `='1.1. Canteiro'!C12` |
| `F11` | `=A11*C11` |
| `A12` | `=A11` |
| `C12` | `='1.1. Canteiro'!C13` |
| `F12` | `=A12*C12` |
| `F13` | `=SUM(F5:F12)` |
| `F16` | `=D16*E16` |
| `F17` | `=D17*E17` |
| `F18` | `=D18*E18` |
| `E20` | `=E19` |
| `E21` | `='1.2. Mob Draga + Pol.'!E21` |
| `F21` | `=D21*E21` |
| `E22` | `=E21` |
| `F22` | `=D22*E22` |
| `F23` | `=D23*E23` |
| `F24` | `=D24*E24` |
| `F25` | `=D25*E25` |
| `F26` | `=D26*E26` |
| `E27` | `='1.2.1.Barrilete'!F29` |
| `F27` | `=D27*E27` |
| `D28` | `=A11` |
| `F28` | `=D28*E28` |
| `E29` | `=F13` |
| `F30` | `=SUM(F16:F29)` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=SUM(F30:F31)` |

### 15. 5.2. Desmob Final

- Faixa usada: `A1:N38`
- Fórmulas: **36**
- Conceitos provisórios: desmobilizacao
- Células numéricas observadas: **143**

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
| `C5` | `=M5` |
| `D5` | `='Dados Obra '!B26*'5.2. Desmob Final'!N5` |
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
| `F35` | `='5.2. Desmob Final'!D18` |
| `F36` | `=F34/F35` |
| `F37` | `=F36*(E37/100)` |
| `F38` | `=F36+F37` |

### 16. Plan. BDI

- Faixa usada: `A1:K24`
- Fórmulas: **49**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **77**

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
- 1.1
- CANTEIRO DE OBRAS
- vb
- 1.2
- Mobilização Draga
- Preparo de Célula de desaguamento
- m²
- DRAGAGEM E DESAGUAMENTO
- 3.1
- Fornecimento de Bags
- m³
- 3.2
- Dragagem
- 3.3
- Operação do sistema de polímero
- 3.4
- Mediçao
- 3.5
- Drenagem das lagoas
- Reparo do PEAD das Lagoas
- 5.1
- Desmobilização da Draga e Eqto Pol.
- 5.2
- Desmobilização FINAL
- Preço de Venda
- Retorno mensal
- #NAME?

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1.1. Canteiro'!F34` |
| `G4` | `=C4/E4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `K4` | `=I4+I5` |
| `C5` | `='1.2. Mob Draga + Pol.'!F30` |
| `C7` | `='2. Prep Célula'!F35` |
| `E7` | `='2. Prep Célula'!M17` |
| `I7` | `=((H7/100)+1)*G7` |
| `J7` | `=E7*I7` |
| `K7` | `=I7` |
| `C10` | `='3.1. Bags'!F29` |
| `E10` | `='Dados Obra '!K17` |
| `G10` | `=C10/E10` |
| `I10` | `=((H10/100)+1)*G10` |
| `J10` | `=E10*I10` |
| `K10` | `=I10+I11+I12+I13+I14` |
| `C11` | `='3.2 Draga'!D202` |
| `E11` | `=E10` |
| `C12` | `='3.3 Op.Planta'!F28` |
| `E12` | `=E11` |
| `G12` | `=C12/E12` |
| `I12` | `=((H12/100)+1)*G12` |
| `J12` | `=E12*I12` |
| `C13` | `='3.4.Medição'!F25` |
| `E13` | `=E12` |
| `C14` | `='3.5.Drenagem Lagoas'!F17` |
| `E14` | `=E13` |
| `G14` | `=C14/E14` |
| `I14` | `=((H14/100)+1)*G14` |
| `J14` | `=E14*I14` |
| `C16` | `='4.Reparo PEAD'!F17` |
| `E16` | `='4.Reparo PEAD'!J17` |
| `G16` | `=C16/E16` |
| `I16` | `=((H16/100)+1)*G16` |
| `J16` | `=E16*I16` |
| `K16` | `=I16` |
| `C18` | `='5.1. DesMob Draga + Pol.'!F30` |
| `G18` | `=C18/E18` |
| `I18` | `=((H18/100)+1)*G18` |
| `K18` | `=I18+I19` |
| `C19` | `='5.2. Desmob Final'!F34` |
| `G19` | `=C19/E19` |
| `I19` | `=((H19/100)+1)*G19` |
| `J19` | `=E19*I19` |
| `C21` | `=SUM(C4:C20)` |
| `J21` | `=SUM(J4:J20)` |
| `C23` | `=J21-C21` |
| `C24` | `=C23/Produção!H25` |

### 17. Plan. Final.

- Faixa usada: `A1:N7`
- Fórmulas: **21**
- Conceitos provisórios: outros
- Células numéricas observadas: **34**

#### Rótulos e textos observados

- ITEM
- DESCRIÇÃO DOS SERVIÇOS
- UNID
- QUANT
- PREÇO UNITÁRIO
- PREÇO TOTAL
- Pr. Unit.
- Preços unitários Rev.02 com volume de 85.470,45m³
- Mobilização e Montagem dos Equipamentos de Dragagem e Preparo e injeção de Polímero
- vb
- Preparo da Célula de desaguamento dos Bags, incluindo impermeabilização com manta PEAD, bidim e Camada Drenante
- m²
- Dragagem e desaguamento de sedimentos através do processo de acondicionamento em Geobags de alta resistência, incluindo fornecimento e operação dos Geobags
- m³
- R$/Tss
- R$/m³
- Reparo da manta PEAD das lagoas (50m² por lagoa)
- un
- Desmobilização dos equipamentos
- TOTAL GERAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D2` | `='Plan. BDI'!E4` |
| `E2` | `=H2` |
| `F2` | `=D2*E2` |
| `H2` | `='Plan. BDI'!K4` |
| `D3` | `='Plan. BDI'!E7` |
| `E3` | `=H3` |
| `F3` | `=D3*E3` |
| `H3` | `='Plan. BDI'!K7` |
| `D4` | `='Plan. BDI'!E10` |
| `E4` | `=H4` |
| `F4` | `=D4*E4` |
| `H4` | `='Plan. BDI'!K10` |
| `D5` | `='Plan. BDI'!E16` |
| `E5` | `=N5` |
| `F5` | `=D5*E5` |
| `H5` | `='Plan. BDI'!K16` |
| `D6` | `='Plan. BDI'!E18` |
| `E6` | `=H6` |
| `F6` | `=D6*E6` |
| `H6` | `='Plan. BDI'!K18` |
| `F7` | `=SUM(F2:F6)` |

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
