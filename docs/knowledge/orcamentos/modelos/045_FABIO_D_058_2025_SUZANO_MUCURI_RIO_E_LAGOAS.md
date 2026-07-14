# Modelo 045 — FABIO D_058_2025 - Suzano Mucuri - rio e lagoas.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `FABIO D_058_2025 - Suzano Mucuri - rio e lagoas.xlsx`
- Família provisória: **Dragagem com bags/geotêxteis**
- SHA-256 do arquivo: `0aebc624b9705d1bca0d290e47bdb7bb00b6016948ca408e57062de4ccce035b`
- Abas analisadas: **16**
- Fórmulas encontradas: **632**

## Conceitos identificados

- `outros`: 5 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `bags_geotexteis`: 1 aba(s)
- `barrilete_linha`: 1 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `desmobilizacao`: 1 aba(s)
- `estrutura_desaguamento`: 1 aba(s)
- `formacao_preco`: 1 aba(s)
- `medicao_batimetria`: 1 aba(s)
- `producao_prazo`: 1 aba(s)
- `resumo_comercial`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:S27` | 15 | dados_obra |
| 2 | `Produção` | `A1:R27` | 23 | producao_prazo |
| 3 | `Dúvidas` | `A1:B21` | 1 | outros |
| 4 | `1.1. Canteiro` | `A1:N29` | 39 | canteiro |
| 5 | `1.2. Mob Draga + Pol.` | `A1:N51` | 69 | mobilizacao_draga |
| 6 | `1.2.1.Barrilete` | `A1:F31` | 39 | barrilete_linha |
| 7 | `2. Prep Célula` | `A1:O39` | 72 | estrutura_desaguamento |
| 8 | `3.1. Bags` | `A1:M54` | 73 | bags_geotexteis |
| 9 | `3.2 Draga` | `A1:L207` | 96 | outros |
| 10 | `3.3 Op.Planta` | `A1:M36` | 39 | outros |
| 11 | `3.4.Medição` | `A1:F26` | 22 | medicao_batimetria |
| 12 | `3.5.Retorno perc.` | `A1:K20` | 30 | outros |
| 13 | `DesMob Draga + Pol. (2)` | `A1:N51` | 61 | mobilizacao_draga, desmobilizacao |
| 14 | `Plan. BDI` | `A1:K23` | 36 | formacao_preco |
| 15 | `Plan. Final.` | `A1:H6` | 16 | outros |
| 16 | `Planilha1` | `A1:D10` | 1 | resumo_comercial |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `1.1. Canteiro` | 96 |
| `Dados Obra` | 16 |
| `3.3 Op.Planta` | 7 |
| `Plan. BDI` | 7 |
| `1.2. Mob Draga + Pol.` | 5 |
| `2. Prep Célula` | 2 |
| `3.1. Bags` | 2 |
| `3.2 Draga` | 2 |
| `3.4.Medição` | 2 |
| `1.2.1.Barrilete` | 1 |
| `3.5.Retorno perc.` | 1 |
| `DesMob Draga + Pol. (2)` | 1 |
| `[1]Dados Obra` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:S27`
- Fórmulas: **15**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **42**

#### Rótulos e textos observados

- 058_2025
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- Comprimento
- Largura
- Perímetro
- Profun- didade
- Volume Total
- Rio Mucuri
- Proposta
- Proposta D_058_2025
- Data
- % de Assoreamento
- Volume de Assoreamento (dado informado Suzano)
- Cliente
- SUZANO - Mucuri
- Distância MÁXIMA de Recalque Rio até Bota Fora (m)
- Contato
- Ítalo / Itamar ? Thamires
- e-mail
- Distância MÉDIA de Recalque Rio até Bota Fora (m)
- PERÍODO OPERAÇÃO (sugerido Suzano)
- abril a outubro
- meses
- Dados da obra
- Objeto
- DRAGAGEM do Rio Mucuri e LAGOAs de Polimento e Aeradas
- Área estimada
- Esp. Lodo Estimada
- Volume Lodo
- %ST in situ
- % ST desaguado Sugerido
- M3 base seca
- Volume Desaguado
- Distância Máxima Recalque
- Local
- Mucuri BA
- Lagoa de Polimento
- Volume dragagem (m³)
- Lagoas aeradas
- Tipo de material
- Efluente industríal Papel
- Distância de Recalque (m)
- Seio da linha =
- Total
- novembro a março
- Linha Flutuante (m)
- Linha de terra (m)
- Profundidade de dragagem (m)
- Espessura média de dragagem (m)
- Área de Dragagem (m² ou L x C)
- X
- Volume (m³) =
- Tipo de Bota Fora
- BOMBEAMENTO DIRETO
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
| `O4` | `=K4*L4*N4` |
| `O6` | `=O5*O4` |
| `M13` | `=K13*L13` |
| `P13` | `=M13*N13` |
| `Q13` | `=P13/O13` |
| `B14` | `=O6` |
| `M14` | `=K14*L14` |
| `P14` | `=M14*N14` |
| `Q14` | `=P14/O14` |
| `M15` | `=SUM(M13:M14)` |
| `B16` | `=R14` |
| `H16` | `=B16+E16` |
| `H17` | `=B17+E17` |
| `B18` | `=B16-B17` |
| `G21` | `=B21*D21*B20` |

### 2. Produção

- Faixa usada: `A1:R27`
- Fórmulas: **23**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **38**

#### Rótulos e textos observados

- PRODUÇÃO - RIO MUCURI
- Horas Trabalhadas por mês
- PRODUÇÃO LAGOAS
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
- Dragagem direto
- Dragagem Bags
- Desmob. Draga
- Prazo de Execução
- mês
- Desmobilização
- Lagoas
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
| `O8` | `=O3*(O4/100)*(O5/100)` |
| `D11` | `=I6` |
| `O11` | `=I6` |
| `D13` | `=D8*D11` |
| `O13` | `=O8*O11` |
| `D17` | `=D13` |
| `O17` | `=O13` |
| `D20` | `='Dados Obra '!B14` |
| `O20` | `='Dados Obra '!M14` |
| `H21` | `=D27` |
| `R21` | `=O23` |
| `D23` | `=ROUNDUP(D20/D17,0)` |
| `E23` | `=D20/D17` |
| `O23` | `=ROUNDUP(O20/O17,0)` |
| `H24` | `=R25` |
| `H25` | `=SUM(H18:H24)` |
| `R25` | `=SUM(R18:R24)` |
| `D27` | `=D23` |
| `O27` | `=O23` |

### 3. Dúvidas

- Faixa usada: `A1:B21`
- Fórmulas: **1**
- Conceitos provisórios: outros
- Células numéricas observadas: **16**

#### Rótulos e textos observados

- Qual o volume estimado de areia a ser dragado do Rio Mucuri ?
- No MD de Dragagem que nos enviaram é informado que o processo prevê o aprofundamento de 1,50m do leito do rio. Esse 1,50m é a espessura de remoção de areia que devemos considerar ou 1,50m será a lâmina de água que deverá ficar no rio, considerando já a lâmina atual de água existente ?
- Qual a lâmina de água média existente atualmente ou média que costuma ter no período da escassez hídrica no trecho do rio Mucuri a ser dragado?
- A dragagem do Rio só pode ser realizada no período de escassez hídrica ou podemos montar um planejamento para dragar em qualquer época ?
- Poderia nos informar por imagem o local exato para lançamento do material dragado do rio ?
- Nesse bota fora do material dragado do rio Mucuri, existe algum tipo de drenagem já existente ou precisa ser previsto ?
- Esse material dragado deverá permanecer neste bota fora ou deverá ser posteriormente destinado para outro local ?
- Fora do período de Dragagem do rio Mucuri (novembro a março) a draga deverá permanecer a disposição no rio para uma eventual necessidade ou poderemos considerar a retirada dela e o retorno em data propícia ?
- Qual o volume de lodo previsto para dragagem da lagoa de polimento ?
- Qual o volume de lodo previsto para dragagem das lagoas aeradas ?
- Qual o percentual de sólidos totais que o lodo dentro das lagoas encontra-se atualmente ?
- Para o envio do lodo para os tanques MBRR a tubulação de recalque deverá ser mudada de ponto de lançamento entre um tanque e outro ou ela permanecerá fixa sempre?
- Qual a altura de lançamento do lodo nos tanques MBRR em relação ao nível das lagoas ?
- No MD de dragagem fornecido, é informado que deverá ser adicionado uma tela de proteção na saída dos tanques para retenção da parte sólido do material dragado. O fornecimento e instalação desta tela será de responsabilidade da Suzano ou da Contratada?
- Se a resposta ao questionamento anterior for Contratada, favor informar quantas telas serão e a dimensão do vão de instalação e se possível imagem do local a ser instalado.
- No MD de dragagem fornecido, é informado que o pagamento será realizado com base no volume de horas trabalhadas. Favor esclarecer se será por VOLUME de material dragado ou por HORA TRABALHADA.
- Canteiro de obras (almoxarifado, banheiro e vestiário)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `None` | `` |

### 4. 1.1. Canteiro

- Faixa usada: `A1:N29`
- Fórmulas: **39**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **99**

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
- Aux Técnico / Téc Segurança
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
- #NAME?
- Container Sanitário/Vestiário
- Container Escritório
- Banheiro químico
- Intens de organização e segurança
- vb
- MDO (limpeza)
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
| `J5` | `=I5/220` |
| `M5` | `=J5+K5+L5` |
| `D6` | `='Dados Obra '!B26` |
| `I6` | `=J6*220` |
| `L6` | `=(J6+K6)*0.25` |
| `M6` | `=J6+K6+L6` |
| `D7` | `=D6` |
| `I7` | `=J7*220` |
| `D8` | `=D7` |
| `I8` | `=J8*220` |
| `M8` | `=J8+K8+L8` |
| `D9` | `=D8` |
| `I9` | `=J9*220` |
| `D10` | `=D9` |
| `I10` | `=J10*220` |
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
| `D21` | `=D20` |
| `F21` | `=D21*E21` |
| `F23` | `=D23*E23` |
| `D24` | `=D21` |
| `E24` | `=F10` |
| `F25` | `=SUM(F18:F24)` |
| `F26` | `=Produção!H21+Produção!R21` |
| `F27` | `=F25/F26` |
| `F28` | `=F27*(E28/100)` |
| `F29` | `=F27+F28` |

### 5. 1.2. Mob Draga + Pol.

- Faixa usada: `A1:N51`
- Fórmulas: **69**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **168**

#### Rótulos e textos observados

- 1 - Mobilização DRAGA
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Engenheiro
- Aux Técnico / Téc Segurança
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
- MOBILIZAÇÃO DE 01 DRAGA SÓ POR ENQUANTO
- Frete para Containers
- vb
- PGR + PCMSO + LTCAT + PR
- ART Principal + ARTS co-resp.
- Tenda do Canteiro
- água potável
- gl
- material de escritório
- mês
- Custo de viagem da equipe
- Hospedagem da equipe durante mobilização
- custo Exames médicos
- un
- Máscara de Fuga
- Máquina de Solda para Tubos PEAD - locação
- Guindaste para carregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Preços VALE Vitória
- Mobiliário Canteiro
- Mesa escritório
- mobiliário do alojamento
- Carreta Carga Seca - Draga + tubos
- Fabiano R$ 18.800,00 + 0,2%
- Carreta Carga Seca - Eqto Polímero
- Zap de 17/10/25
- Guindaste p/descarregamento e montagem DRAGA
- cliente
- cadeira
- Mob / desmob Guindaste
- armário escritório
- Plano de Rigger
- cestos lixo
- Instalações hidráulicas
- Instalações elétricas
- Máquina Wap
- Barrilete
- Munck para apoio de montagem
- Mão de obra p/carga e montagem (r$/dia)
- armário vestiário
- TOTAL
- Bebedouro
- BDI (%)
- Preço Final
- Carreta (draga)
- MÃO DE OBRA
- DIAS
- Carreta (Tubulação 700 m)
- Exames
- Carreta (flutuantes e outros periféricos)
- viagem
- integração
- montagem
- Carreta (equto polímero)

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
| `D20` | `=8*'1.1. Canteiro'!D18` |
| `D21` | `='1.1. Canteiro'!D18` |
| `D22` | `=A11` |
| `D24` | `=A11` |
| `D25` | `=D24` |
| `D28` | `=A11` |
| `F28` | `=D28*E28` |
| `E29` | `=N43` |
| `N29` | `=L29*M29` |
| `E30` | `=E29` |
| `N30` | `=L30*M30` |
| `D31` | `=C49` |
| `F31` | `=D31*E31` |
| `N31` | `=L31*M31` |
| `D32` | `=C51` |
| `E32` | `=E31` |
| `F32` | `=D32*E32` |
| `F33` | `=D33*E33` |
| `N33` | `=L33*M33` |
| `F34` | `=D34*E34` |
| `N34` | `=L34*M34` |
| `F35` | `=D35*E35` |
| `F36` | `=D36*E36` |
| `F37` | `=D37*E37` |
| `F38` | `=D38*E38` |
| `E39` | `='1.2.1.Barrilete'!F29` |
| `F39` | `=D39*E39` |
| `F40` | `=D40*E40` |
| `D41` | `=F51` |
| `E41` | `=F13` |
| `F42` | `=SUM(F16:F41)` |
| `F43` | `=F42*(E43/100)` |
| `N43` | `=SUM(N29:N42)` |
| `F44` | `=SUM(F42:F43)` |
| `C49` | `=SUM(C46:C48)` |
| `F51` | `=SUM(F47:F50)` |

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
| `A7` | `=SUM(A4:A6)` |
| `C7` | `='1.1. Canteiro'!C12` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
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
- Fórmulas: **72**
- Conceitos provisórios: estrutura_desaguamento
- Células numéricas observadas: **146**

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
- Aux Técnico / Téc Segurança
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
- 2 níveis de bag
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
- 1º nível - 3 lilnhas com 7 bags cada = 21bags
- Preparo Terreno - Aluguel de Retro
- 2º nível - 2 lilnhas com 6 bags cada = 12 bags
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
- Sistema de Drenagem e caixa percolado
- Frete para entregar na Suzano = R$ 800,00 por viagem de 12m³
- GEOCOMPOSTO DRENANTE (rolo 2x30m)
- Frete do Geocomposto Drenante
- Retro escavadeira para espalhamento Brita
- Geocomposto Drenante - empresa Geomembrana (Thales gerente comercial)
- Mão de obra de instal. Geocomposto
- Frete FOB (considerei Fabiano em Graneleira levando 72 rolos por viagem)
- TOTAL
- Estamos substituindo a camada Drenante de Brita pelo Geocomposto, com isso eliminamos

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A5` | `='1.1. Canteiro'!A5` |
| `C5` | `='1.1. Canteiro'!C5` |
| `D5` | `='1.1. Canteiro'!D5` |
| `E5` | `='1.1. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `='1.1. Canteiro'!A6` |
| `B6` | `='1.1. Canteiro'!B6` |
| `C6` | `='1.1. Canteiro'!C6` |
| `D6` | `='1.1. Canteiro'!D6` |
| `E6` | `=E5` |
| `A7` | `='1.1. Canteiro'!A7` |
| `C7` | `='1.1. Canteiro'!C7` |
| `D7` | `=D6` |
| `M7` | `=M17` |
| `N7` | `=J7*M7` |
| `A8` | `='1.1. Canteiro'!A8` |
| `C8` | `='1.1. Canteiro'!C8` |
| `D8` | `=D7` |
| `M8` | `=M7` |
| `N8` | `=J8*M8` |
| `A9` | `='1.1. Canteiro'!A9` |
| `C9` | `='1.1. Canteiro'!C9` |
| `D9` | `=D8` |
| `M9` | `=M7` |
| `N9` | `=J9*M9` |
| `A10` | `='1.1. Canteiro'!A10` |
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
| `L22` | `=(J22*K22)+1+10.5+0.5` |
| `D23` | `=N7` |
| `D24` | `=D23` |
| `D26` | `=N8` |
| `D27` | `=N9*1.1` |
| `D28` | `=D27/12` |
| `D30` | `=M17*1.1` |
| `E30` | `=M33` |
| `D31` | `=M37` |
| `E31` | `='1.2. Mob Draga + Pol.'!E31` |
| `F31` | `=D31*E31` |
| `D33` | `=ROUNDDOWN(N12,0)` |
| `E33` | `=E20` |
| `E34` | `=F14` |
| `F34` | `=D34*E34` |
| `F35` | `=SUM(F18:F34)` |
| `F36` | `=M17` |
| `F37` | `=F35/F36` |
| `K37` | `=(30*2)*72` |
| `M37` | `=ROUNDUP(D30/K37,0)` |
| `F38` | `=F37*(E38/100)` |
| `F39` | `=F37+F38` |

### 8. 3.1. Bags

- Faixa usada: `A1:M54`
- Fórmulas: **73**
- Conceitos provisórios: bags_geotexteis
- Células numéricas observadas: **188**

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
- P18 X 35
- % ST desaguado
- P20 X 25
- VOLUME DESAGUADO
- P18 X 40
- P18 X 45
- Vol. Lodo
- % ST des Bacia
- % ST des BAG
- Volume Desag. Bag
- Lagoa emergência
- MÃO DE OBRA DE ESPALHAMENTO
- dia
- TOTAL
- Prazo de Operação
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
- P18 X 20
- 1º Nível
- 2º nível
- CAPACIDADE DA CÉLULA - 1
- CÉLULA - 2
- v
- P20 X 20
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
| `I19` | `='Dados Obra '!N13` |
| `D20` | `=E49` |
| `E20` | `=M49` |
| `I20` | `=I18*I19` |
| `D21` | `=E41+E50` |
| `E21` | `=M41` |
| `D22` | `=E42` |
| `E22` | `=M42` |
| `I22` | `='Dados Obra '!O13` |
| `I23` | `=I20/I22` |
| `E24` | `=M48` |
| `I24` | `=I23/D41` |
| `E25` | `=M49` |
| `E26` | `=M50` |
| `I27` | `=I18` |
| `J27` | `=I19` |
| `L27` | `=J27*1.5` |
| `M27` | `=(I27*J27)/L27` |
| `E28` | `=F14` |
| `I28` | `='Dados Obra '!P14` |
| `F29` | `=SUM(F18:F28)` |
| `I29` | `='Dados Obra '!P15` |
| `I30` | `='Dados Obra '!P16` |
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
| `K41` | `=K40` |
| `K42` | `=K41` |
| `K43` | `=K42` |
| `F44` | `=SUM(F38:F43)` |
| `D47` | `=B47*C47` |
| `F47` | `=D47*E47` |
| `M48` | `=(I48*J48)*K48` |
| `K49` | `=K48` |
| `M49` | `=(I49*J49)*K49` |
| `K50` | `=K49` |
| `M50` | `=(I50*J50)*K50` |
| `F53` | `=SUM(F47:F52)` |
| `F54` | `=F44+F53` |
| `G54` | `=G53` |

### 9. 3.2 Draga

- Faixa usada: `A1:L207`
- Fórmulas: **96**
- Conceitos provisórios: outros
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 5.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F7` | `=J8` |
| `J8` | `=SUM(K6:K7)` |
| `E9` | `=30+20` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=F10*0.1` |
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
| `D26` | `=D23` |
| `A27` | `=L24` |
| `E27` | `=D27*B27*A27` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `A37` | `='1.1. Canteiro'!E5` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `B52` | `=B20+B21+B22+B23+B26` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B25` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `D69` | `=C71` |
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
| `J108` | `=SUM(J106:J107)` |
| `I110` | `=('Dados Obra '!B17/12)*3` |
| `K110` | `=I110*J110` |
| `I111` | `=I106` |
| `J111` | `=K110/I111` |
| `E112` | `='1.1. Canteiro'!F27` |
| `J112` | `=K110*(1/100)` |
| `E113` | `=B113*D113` |
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
- Fórmulas: **39**
- Conceitos provisórios: outros
- Células numéricas observadas: **81**

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
- Instalações hidráulicas
- vb
- Instalações eletrica
- Máquina Wap
- Mão de obra para operação do sistema
- TOTAL
- Prazo de Operação
- preço unitário
- #DIV/0!
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
| `A6` | `='1.1. Canteiro'!A6` |
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
| `E23` | `=4500+2500` |
| `D27` | `=D18*30` |
| `E27` | `=F14` |
| `F28` | `=SUM(F18:F27)` |
| `F30` | `=F28/F29` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=F30+F31` |
| `D34` | `='3.1. Bags'!I20` |
| `D36` | `=D34*D35` |

### 11. 3.4.Medição

- Faixa usada: `A1:F26`
- Fórmulas: **22**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **42**

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
- análises de laboratório
- un
- Acompanhamento FOS
- dia
- TOTAL
- BDI (%)
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
| `F17` | `=D17*E17` |
| `E20` | `=F11` |
| `F21` | `=SUM(F16:F20)` |
| `F22` | `=F21*(E22/100)` |
| `F23` | `=SUM(F21:F22)` |
| `F25` | `=F24*(E25/100)` |
| `F26` | `=SUM(F24:F25)` |

### 12. 3.5.Retorno perc.

- Faixa usada: `A1:K20`
- Fórmulas: **30**
- Conceitos provisórios: outros
- Células numéricas observadas: **39**

#### Rótulos e textos observados

- Retorno do percolado
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
- Volume
- Bomba booster
- mês
- LAGOA 6
- LAGOA 7
- LAGOA 8
- Mão de obra de limpeza fina
- dia
- POLIMENTO
- TOTAL
- Preço Final
- Volume de lodo
- Produção diária m³/dia
- #NAME?
- m³/dia
- Prazo
- dias

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
| `E15` | `='3.2 Draga'!D200/'Dados Obra '!B27` |
| `D16` | `=22*4` |
| `E16` | `=F9` |
| `F16` | `=D16*E16` |
| `F17` | `=SUM(F12:F16)` |
| `J17` | `=SUM(J13:J16)` |
| `F18` | `=F17` |
| `J18` | `='[1]Dados Obra '!N17` |
| `J19` | `=([1]Produção!D3*3)*[1]Produção!H3` |
| `J20` | `=(J17-J18)/J19` |

### 13. DesMob Draga + Pol. (2)

- Faixa usada: `A1:N51`
- Fórmulas: **61**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **154**

#### Rótulos e textos observados

- 1 - Mobilização DRAGA + PLANTA DE POLÍMERO
- Nº Func.
- Mão de obra p/carga e montagem / dia
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Engenheiro
- Aux Técnico / Téc Segurança
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
- Frete para Containers
- vb
- PGR + PCMSO + LTCAT + PR
- ART Principal + ARTS co-resp.
- Tenda do Canteiro
- água potável
- gl
- material de escritório
- mês
- Custo de viagem da equipe
- Hospedagem da equipe durante mobilização
- custo Exames médicos
- un
- Máscara de Fuga
- Máquina de Solda para Tubos PEAD - locação
- Guindaste para carregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Preços VALE Vitória
- Mobiliário Canteiro
- Mesa escritório
- mobiliário do alojamento
- Carreta Carga Seca - Draga + tubos
- Fabiano R$ 18.800,00 + 0,2%
- Carreta Carga Seca - Eqto Polímero
- Zap de 17/10/25
- Guindaste p/descarregamento e montagem DRAGA
- cliente
- cadeira
- Mob / desmob Guindaste
- armário escritório
- Plano de Rigger
- cestos lixo
- Instalações hidráulicas
- Instalações elétricas
- Máquina Wap
- Munck para apoio de montagem
- Mão de obra p/carga e montagem (r$/dia)
- armário vestiário
- TOTAL
- Bebedouro
- BDI (%)
- Preço Final
- Carreta 1 (draga)
- MÃO DE OBRA
- DIAS
- Carreta 2 (Tubulação 2200 m)
- Exames
- Carreta 3 (flutuantes e outros periféricos)
- viagem
- integração
- desmontagem
- Carreta (equto polímero)

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
| `D22` | `=A11` |
| `D24` | `=A11` |
| `F28` | `=D28*E28` |
| `E29` | `=N43` |
| `N29` | `=L29*M29` |
| `E30` | `=E29` |
| `N30` | `=L30*M30` |
| `D31` | `=C49` |
| `F31` | `=D31*E31` |
| `D32` | `=C51` |
| `E32` | `=E31` |
| `F32` | `=D32*E32` |
| `F33` | `=D33*E33` |
| `F34` | `=D34*E34` |
| `F35` | `=D35*E35` |
| `F36` | `=D36*E36` |
| `F37` | `=D37*E37` |
| `F38` | `=D38*E38` |
| `F39` | `=D39*E39` |
| `F40` | `=D40*E40` |
| `D41` | `=F51` |
| `E41` | `=F13` |
| `F42` | `=SUM(F16:F41)` |
| `F43` | `=F42*(E43/100)` |
| `N43` | `=SUM(N29:N42)` |
| `F44` | `=SUM(F42:F43)` |
| `C49` | `=SUM(C46:C48)` |
| `F51` | `=SUM(F47:F50)` |

### 14. Plan. BDI

- Faixa usada: `A1:K23`
- Fórmulas: **36**
- Conceitos provisórios: formacao_preco
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
- Retorno do percolado
- 5.1
- Desmobilização da Draga e Eqto Pol.
- Preço de Venda
- PREÇO DE VENDA/M³

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `G4` | `=C4/E4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `K4` | `=I4+I5` |
| `C5` | `='1.2. Mob Draga + Pol.'!F42` |
| `C7` | `='2. Prep Célula'!F35` |
| `E7` | `='2. Prep Célula'!M17` |
| `I7` | `=((H7/100)+1)*G7` |
| `J7` | `=E7*I7` |
| `K7` | `=I7` |
| `C10` | `='3.1. Bags'!F29` |
| `E10` | `='Dados Obra '!B14` |
| `G10` | `=C10/E10` |
| `I10` | `=((H10/100)+1)*G10` |
| `J10` | `=E10*I10` |
| `K10` | `=I10+I11+I12+I13+I14` |
| `C11` | `='3.2 Draga'!D202` |
| `E11` | `=E10` |
| `C12` | `='3.3 Op.Planta'!F28` |
| `G12` | `=C12/E12` |
| `I12` | `=((H12/100)+1)*G12` |
| `J12` | `=E12*I12` |
| `C13` | `='3.4.Medição'!F23` |
| `C14` | `='3.5.Retorno perc.'!F17` |
| `G14` | `=C14/E14` |
| `I14` | `=((H14/100)+1)*G14` |
| `J14` | `=E14*I14` |
| `C16` | `='DesMob Draga + Pol. (2)'!F42` |
| `G16` | `=C16/E16` |
| `I16` | `=((H16/100)+1)*G16` |
| `K16` | `=I16` |
| `C18` | `=SUM(C4:C17)` |
| `J18` | `=SUM(J4:J17)` |
| `C20` | `=J18-C18` |
| `J20` | `=J18/E10` |
| `C23` | `=J18*0.01` |

### 15. Plan. Final.

- Faixa usada: `A1:H6`
- Fórmulas: **16**
- Conceitos provisórios: outros
- Células numéricas observadas: **21**

#### Rótulos e textos observados

- ITEM
- DESCRIÇÃO DOS SERVIÇOS
- UNID
- QUANT
- PREÇO UNITÁRIO
- PREÇO TOTAL
- Pr. Unit.
- Mobilização e Montagem dos Equipamentos de Dragagem e Preparo e injeção de Polímero
- vb
- Preparo da Célula de desaguamento dos Bags, incluindo impermeabilização com manta PEAD, bidim e Camada Drenante
- m²
- Dragagem e desaguamento de sedimentos através do processo de acondicionamento em Geobags de alta resistência, incluindo fornecimento e operação dos Geobags
- m³
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
| `E4` | `=H4` |
| `F4` | `=D4*E4` |
| `H4` | `='Plan. BDI'!K10` |
| `D5` | `='Plan. BDI'!E16` |
| `E5` | `=H5` |
| `F5` | `=D5*E5` |
| `H5` | `='Plan. BDI'!K16` |
| `F6` | `=SUM(F2:F5)` |

### 16. Planilha1

- Faixa usada: `A1:D10`
- Fórmulas: **1**
- Conceitos provisórios: resumo_comercial
- Células numéricas observadas: **3**

#### Rótulos e textos observados

- VOLUME DE SEDIMENTOS A SEREM REMOVIDOS DA LAGOA
- M³
- VOLUMDE DE SEDIMENTOS SERÃO DEPOSITADOS NO ATERRO INTERNO DA SUZANO - ESCAVAÇÃO MECÂNICA
- VOLUMDE DE SEDIMENTOS SERÃO DEPOSITADOS NO ATERRO INTERNO DA SUZANO - SISTEMA DE GEOBAG'S

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `None` | `` |

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
