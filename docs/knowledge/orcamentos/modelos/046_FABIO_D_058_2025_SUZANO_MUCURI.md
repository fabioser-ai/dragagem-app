# Modelo 046 — FABIO D_058_2025 - Suzano Mucuri.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `FABIO D_058_2025 - Suzano Mucuri.xlsx`
- Família provisória: **Dragagem/bombeamento**
- SHA-256 do arquivo: `94e53bf65e1b53095373c1ec272e215a54a712a562bd14bdfc295fa318e20ba7`
- Abas analisadas: **12**
- Fórmulas encontradas: **390**

## Conceitos identificados

- `outros`: 5 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `desmobilizacao`: 1 aba(s)
- `formacao_preco`: 1 aba(s)
- `producao_prazo`: 1 aba(s)
- `resumo_comercial`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:S27` | 15 | dados_obra |
| 2 | `Produção` | `A1:R28` | 27 | producao_prazo |
| 3 | `Dúvidas` | `A1:C21` | 1 | outros |
| 4 | `1.1. Canteiro` | `A1:N30` | 42 | canteiro |
| 5 | `1. Mob Draga` | `A1:N51` | 62 | mobilizacao_draga |
| 6 | `2. Draga` | `A1:L207` | 96 | outros |
| 7 | `H.Extra Dia` | `A1:O15` | 19 | outros |
| 8 | `H.Extra FDS` | `A1:O15` | 17 | outros |
| 9 | `3. DesMob Draga  (2)` | `A1:N51` | 55 | mobilizacao_draga, desmobilizacao |
| 10 | `Plan. BDI` | `A1:N23` | 39 | formacao_preco |
| 11 | `Plan. Final.` | `A1:H6` | 16 | outros |
| 12 | `Planilha1` | `A1:D10` | 1 | resumo_comercial |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `1.1. Canteiro` | 45 |
| `Dados Obra` | 9 |
| `Plan. BDI` | 7 |
| `H.Extra Dia` | 2 |
| `H.Extra FDS` | 2 |
| `1. Mob Draga` | 1 |
| `2. Draga` | 1 |
| `3. DesMob Draga  (2)` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:S27`
- Fórmulas: **15**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **43**

#### Rótulos e textos observados

- 058_2025
- Azul :
- Dados a serem preenchidos
- Prazo Contratual da obra
- meses
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
- Distância Média Recalque
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
| `B16` | `=O7+R13` |
| `H16` | `=B16+E16` |
| `H17` | `=B17+E17` |
| `B18` | `=B16-B17` |
| `G21` | `=B21*D21*B20` |

### 2. Produção

- Faixa usada: `A1:R28`
- Fórmulas: **27**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **44**

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
- 2ª a 5ª feira
- 7 as 17h
- Horas trabalhadas
- h/mês
- 6ª feira
- 7 as 16h
- Horas por semana =
- Produção mensal (m³/mês)
- Dias de Semana
- Média de horas por dia
- Cálculo do Prazo da obra
- Horas Efetivas no Mês
- Produção mensal
- m³/mês
- PRAZO EXECUÇÃO
- Canteiro
- Mobiliz. Draga
- Quantidade total a dragar
- m³
- Preparo Célula
- Dragagem direto
- Período Contratual
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
| `I10` | `=4*I3` |
| `D11` | `=I6` |
| `O11` | `=I6` |
| `I12` | `=SUM(I10:I11)` |
| `D13` | `=D8*D11` |
| `O13` | `=O8*O11` |
| `I14` | `=I12/I13` |
| `I15` | `=I14*I4` |
| `D17` | `=D13` |
| `O17` | `=O13` |
| `D20` | `='Dados Obra '!B14` |
| `O20` | `='Dados Obra '!M14` |
| `H21` | `='Dados Obra '!N1` |
| `R21` | `=O23` |
| `D23` | `=ROUNDUP(D20/D17,0)` |
| `E23` | `=D20/D17` |
| `O23` | `=ROUNDUP(O20/O17,0)` |
| `H25` | `=SUM(H18:H24)` |
| `R25` | `=SUM(R18:R24)` |
| `D27` | `=D23` |
| `O27` | `=O23` |
| `H28` | `=D17*H21` |

### 3. Dúvidas

- Faixa usada: `A1:C21`
- Fórmulas: **1**
- Conceitos provisórios: outros
- Células numéricas observadas: **21**

#### Rótulos e textos observados

- Qual o volume estimado de areia a ser dragado do Rio Mucuri ?
- Não tem volume, pois será por Hora trabalhada
- No MD de Dragagem que nos enviaram é informado que o processo prevê o aprofundamento de 1,50m do leito do rio. Esse 1,50m é a espessura de remoção de areia que devemos considerar ou 1,50m será a lâmina de água que deverá ficar no rio, considerando já a lâmina atual de água existente ?
- não tem calado exato, pois o objetivo é manter calado para captação da bomba
- Qual a lâmina de água média existente atualmente ou média que costuma ter no período da escassez hídrica no trecho do rio Mucuri a ser dragado?
- sem informação
- A dragagem do Rio só pode ser realizada no período de escassez hídrica ou podemos montar um planejamento para dragar em qualquer época ?
- obrigatório manter draga no rio ano inteiro
- Poderia nos informar por imagem o local exato para lançamento do material dragado do rio ?
- dentro do rio (soleira hidráulica)
- Nesse bota fora do material dragado do rio Mucuri, existe algum tipo de drenagem já existente ou precisa ser previsto ?
- é dentro do rio
- Qual a área deste bota fora ?
- Devemos fazer algum tipo de preparo de contenção para os sedimentos (bacia) ou já existe algo preparado no local ?
- Esse material dragado deverá permanecer neste bota fora ou deverá ser posteriormente destinado para outro local ?
- Fora do período de Dragagem do rio Mucuri (novembro a março) a draga deverá permanecer a disposição no rio para uma eventual necessidade ou poderemos considerar a retirada dela e o retorno em data propícia ?
- No item 4 do MD - prazo contratual é informado que o prazo deverá ser definido pelo proponente. Como definir prazo sem quantidade ?
- 24 meses
- Qual o volume de lodo previsto para dragagem da lagoa de polimento ?
- não tem volume, pois será por hora trabalhada
- Qual o volume de lodo previsto para dragagem das lagoas aeradas ?
- Qual o percentual de sólidos totais que o lodo dentro das lagoas encontra-se atualmente ?
- não importa
- Para o envio do lodo para os tanques MBRR a tubulação de recalque deverá ser mudada de ponto de lançamento entre um tanque e outro ou ela permanecerá fixa sempre?
- sim
- Qual a altura de lançamento do lodo nos tanques MBRR em relação ao nível das lagoas ?
- nível do solo
- No MD de dragagem fornecido, é informado que deverá ser adicionado uma tela de proteção na saída dos tanques para retenção da parte sólido do material dragado. O fornecimento e instalação desta tela será de responsabilidade da Suzano ou da Contratada?
- contratada
- Se a resposta ao questionamento anterior for Contratada, favor informar quantas telas serão e a dimensão do vão de instalação e se possível imagem do local a ser instalado.
- não tem
- Qual a capacidade de armazenamento e ou operação dos tanques MBRR ?
- O lodo ficará dentro do MBRR ou posteriormente haverá a necessidade de remoção? Se sim, como se dará isso ?
- ficará dentro
- No MD de dragagem fornecido, é informado que o pagamento será realizado com base no volume de horas trabalhadas. Favor esclarecer se será por VOLUME de material dragado ou por HORA TRABALHADA.
- criar 3 preços de hora trabalhada (normal, H.extra dia de semana, H. extra domingos e feriados)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `None` | `` |

### 4. 1.1. Canteiro

- Faixa usada: `A1:N30`
- Fórmulas: **42**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **106**

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
- iremos utilizar estrutura antiga da soludraga
- Container Sanitário/Vestiário
- Container Escritório
- Banheiro químico
- Intens de organização e segurança + reforma da estrutura antiga
- vb
- água potável
- gl
- material de escritório
- MDO (limpeza = 0,5 dia por mês)
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
| `E6` | `=E5` |
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
| `D23` | `=D20*4` |
| `D24` | `=D18` |
| `F24` | `=D24*E24` |
| `D25` | `=D21*0.5` |
| `E25` | `=F10` |
| `F26` | `=SUM(F18:F25)` |
| `F27` | `=Produção!H21+Produção!R21` |
| `F28` | `=F26/F27` |
| `F29` | `=F28*(E29/100)` |
| `F30` | `=F28+F29` |

### 5. 1. Mob Draga

- Faixa usada: `A1:N51`
- Fórmulas: **62**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **165**

#### Rótulos e textos observados

- 1 - Mobilização DRAGA - DUAS DRAGAS
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
- Custo de viagem da equipe - IDA
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
- Zap de 11/11/25
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
- Carreta (2 dragas)
- MÃO DE OBRA
- DIAS
- Carreta (Tubulação 400 m)
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
| `C7` | `='1.1. Canteiro'!C7` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `C8` | `='1.1. Canteiro'!C8` |
| `D8` | `=D7` |
| `E8` | `=E7` |
| `A9` | `='1.1. Canteiro'!A9` |
| `C9` | `='1.1. Canteiro'!C9` |
| `D9` | `=D6` |
| `E9` | `=E8` |
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
| `D25` | `=D24` |
| `D28` | `=A11` |
| `F28` | `=D28*E28` |
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

### 6. 2. Draga

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
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=(C9*D9*E9*K11)*0.1` |
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
| `E112` | `='1.1. Canteiro'!F28` |
| `J112` | `=K110*(1/100)` |
| `B113` | `=B23+B25+B24+B22+B20+B21+B26` |
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

### 7. H.Extra Dia

- Faixa usada: `A1:O15`
- Fórmulas: **19**
- Conceitos provisórios: outros
- Células numéricas observadas: **27**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Hora Extra dia Semana
- ADICIONAL NOTURNO
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- % HE
- R$
- Diferença entre os valores de hora
- % ADIC
- Operador de Draga
- Ajudante
- Custo da Hora Normal
- Diferença
- Hora Extra DIA SEMANA - convenção Bahia
- Hora Extra SÁBADO - convenção Bahia
- HE DOMINGOS E FERIADOS - convenção Bahia
- Adicional Noturno

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='1.1. Canteiro'!C8` |
| `E5` | `='1.1. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `H5` | `=C11` |
| `I5` | `=(F5*H5)+F5` |
| `N5` | `=C15` |
| `O5` | `=(I5*N5)+I5` |
| `C6` | `='1.1. Canteiro'!C10` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `H6` | `=C11` |
| `I6` | `=(F6*H6)+F6` |
| `N6` | `=C15` |
| `O6` | `=(I6*N6)+I6` |
| `O7` | `=SUM(O5:O6)` |
| `F8` | `=SUM(F5:F7)` |
| `I8` | `=SUM(I5:I7)` |
| `L8` | `=I8-F8` |
| `O8` | `=O7-F8` |

### 8. H.Extra FDS

- Faixa usada: `A1:O15`
- Fórmulas: **17**
- Conceitos provisórios: outros
- Células numéricas observadas: **27**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Hora Extra dia Semana
- ADICIONAL NOTURNO
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- % HE
- R$
- Diferença entre os valores de hora
- % ADIC
- Operador de Draga
- Ajudante
- Custo da Hora Normal
- Diferença
- Hora Extra DIA SEMANA - convenção Bahia
- Hora Extra SÁBADO - convenção Bahia
- HE DOMINGOS E FERIADOS - convenção Bahia
- Adicional Noturno

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='1.1. Canteiro'!C8` |
| `E5` | `='1.1. Canteiro'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `=(F5*H5)+F5` |
| `N5` | `=C15` |
| `O5` | `=(I5*N5)+I5` |
| `C6` | `='1.1. Canteiro'!C10` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `I6` | `=(F6*H6)+F6` |
| `N6` | `=C15` |
| `O6` | `=(I6*N6)+I6` |
| `O7` | `=SUM(O5:O6)` |
| `F8` | `=SUM(F5:F7)` |
| `I8` | `=SUM(I5:I7)` |
| `L8` | `=I8-F8` |
| `O8` | `=O7-F8` |

### 9. 3. DesMob Draga  (2)

- Faixa usada: `A1:N51`
- Fórmulas: **55**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **165**

#### Rótulos e textos observados

- 1 - Mobilização DRAGA - DUAS DRAGAS
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
- Custo de viagem da equipe - VOLTA
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
- Zap de 11/11/25
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
- Carreta (2 dragas)
- MÃO DE OBRA
- DIAS
- Carreta (Tubulação 400 m)
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
| `C7` | `='1.1. Canteiro'!C7` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `C8` | `='1.1. Canteiro'!C8` |
| `D8` | `=D7` |
| `E8` | `=E7` |
| `A9` | `='1.1. Canteiro'!A9` |
| `C9` | `='1.1. Canteiro'!C9` |
| `D9` | `=D6` |
| `E9` | `=E8` |
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
| `D25` | `=D24` |
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
| `E41` | `=F13` |
| `F42` | `=SUM(F16:F41)` |
| `F43` | `=F42*(E43/100)` |
| `N43` | `=SUM(N29:N42)` |
| `F44` | `=SUM(F42:F43)` |
| `C49` | `=SUM(C46:C48)` |
| `F51` | `=SUM(F47:F50)` |

### 10. Plan. BDI

- Faixa usada: `A1:N23`
- Fórmulas: **39**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **58**

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
- Mobilização Draga DAS DRAGAS
- vb
- DRAGAGEM
- QUANT.
- R$ / M³
- 2.1
- Operação em Horário normal
- h
- #NAME?
- 2.2
- Operação em Hora Extra dias de Semana
- 2.3
- Operação em Hora Extra Finais de Semana e Feriados
- 2.4
- Operação em Hora Extra dias de Semana com adicional noturno
- 2.5
- Operação em Hora Extra FDS e Feriados com adicional noturno
- 5.1
- Desmobilização da Draga e Eqto Pol.
- Preço de Venda
- PREÇO DE VENDA/MÊS
- RESULTADO
- PRAZO
- RESULTADO POR MÊS
- REAL CUSTO

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Mob Draga '!F42` |
| `G4` | `=C4/E4` |
| `I4` | `=((H4/100)+1)*G4` |
| `J4` | `=E4*I4` |
| `K4` | `=I4` |
| `C8` | `='2. Draga'!D202` |
| `E8` | `=176*24` |
| `G8` | `=C8/E8` |
| `I8` | `=((H8/100)+1)*G8` |
| `J8` | `=E8*I8` |
| `K8` | `=I8` |
| `M8` | `=Produção!H28` |
| `N8` | `=J8/M8` |
| `C9` | `=G8+'H.Extra Dia'!L8` |
| `F9` | `=F8` |
| `G9` | `=C9/E9` |
| `I9` | `=((H9/100)+1)*G9` |
| `J9` | `=E9*I9` |
| `K9` | `=I9` |
| `C10` | `=G8+'H.Extra FDS'!L8` |
| `K10` | `=I10` |
| `C11` | `=G8+'H.Extra Dia'!O8` |
| `F11` | `=F10` |
| `G11` | `=C11/E11` |
| `I11` | `=((H11/100)+1)*G11` |
| `J11` | `=E11*I11` |
| `K11` | `=I11` |
| `C12` | `=G8+'H.Extra FDS'!O8` |
| `E12` | `=E11` |
| `K12` | `=I12` |
| `C14` | `='3. DesMob Draga  (2)'!F42` |
| `G14` | `=C14/E14` |
| `I14` | `=((H14/100)+1)*G14` |
| `K14` | `=I14` |
| `C16` | `=SUM(C4:C15)` |
| `J16` | `=SUM(J4:J15)` |
| `J18` | `=J8/C20` |
| `C19` | `=J16-C16` |
| `C21` | `=C19/C20` |

### 11. Plan. Final.

- Faixa usada: `A1:H6`
- Fórmulas: **16**
- Conceitos provisórios: outros
- Células numéricas observadas: **9**

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
- #REF!
- Preparo da Célula de desaguamento dos Bags, incluindo impermeabilização com manta PEAD, bidim e Camada Drenante
- m²
- Dragagem e desaguamento de sedimentos através do processo de acondicionamento em Geobags de alta resistência, incluindo fornecimento e operação dos Geobags
- m³
- Desmobilização dos equipamentos
- TOTAL GERAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D2` | `='Plan. BDI'!#REF!` |
| `E2` | `=H2` |
| `F2` | `=D2*E2` |
| `H2` | `='Plan. BDI'!#REF!` |
| `D3` | `='Plan. BDI'!#REF!` |
| `E3` | `=H3` |
| `F3` | `=D3*E3` |
| `H3` | `='Plan. BDI'!#REF!` |
| `E4` | `=H4` |
| `F4` | `=D4*E4` |
| `H4` | `='Plan. BDI'!#REF!` |
| `D5` | `='Plan. BDI'!E14` |
| `E5` | `=H5` |
| `F5` | `=D5*E5` |
| `H5` | `='Plan. BDI'!K14` |
| `F6` | `=SUM(F2:F5)` |

### 12. Planilha1

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
