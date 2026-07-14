# Modelo 005 — composição - 054R1_25 - Suzano B - BDI 65 - apresentado.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `composição - 054R1_25 - Suzano B - BDI 65 - apresentado.xlsx`
- Família provisória: **Dragagem com centrífuga**
- SHA-256 do arquivo: `8e269c5ffbebdb9bd19334df58529ed20cdfdcc3c3c2d57392031825e5a69687`
- Abas analisadas: **14**
- Fórmulas encontradas: **702**

## Conceitos identificados

- `outros`: 5 aba(s)
- `operacao_desaguamento`: 3 aba(s)
- `desmobilizacao`: 2 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `mobilizacao_sistema`: 2 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `producao_prazo`: 1 aba(s)
- `resumo_comercial`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:P43` | 26 | dados_obra |
| 2 | `Produção` | `A1:S23` | 30 | producao_prazo |
| 3 | `cronograma` | `A1:V10` | 1 | outros |
| 4 | `Canteiro` | `A1:N33` | 51 | canteiro |
| 5 | `1.1.Mob. Draga` | `A1:M40` | 57 | mobilizacao_draga |
| 6 | `1.2.Mob Centrífuga` | `A1:N39` | 87 | mobilizacao_sistema, operacao_desaguamento |
| 7 | `2.1. Draga Dec` | `A1:M206` | 107 | outros |
| 8 | `2.2 Centrífuga` | `A1:M205` | 111 | operacao_desaguamento |
| 9 | `2.3. manutenção` | `A1:L25` | 45 | outros |
| 10 | `DesMob. Draga` | `A1:M40` | 52 | mobilizacao_draga, desmobilizacao |
| 11 | `DesMob Centrífuga` | `A1:N39` | 76 | mobilizacao_sistema, operacao_desaguamento, desmobilizacao |
| 12 | `Plan. Final` | `A1:M25` | 47 | outros |
| 13 | `Final` | `A1:L6` | 11 | outros |
| 14 | `Planilha1` | `A1:B14` | 1 | resumo_comercial |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `Canteiro` | 100 |
| `Dados Obra` | 17 |
| `2.1. Draga Dec` | 14 |
| `1.1.Mob. Draga` | 13 |
| `Plan. Final` | 7 |
| `1.2.Mob Centrífuga` | 4 |
| `2.2 Centrífuga` | 1 |
| `2.3. manutenção` | 1 |
| `DesMob Centrífuga` | 1 |
| `DesMob. Draga` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:P43`
- Fórmulas: **26**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **50**

#### Rótulos e textos observados

- SUZANO - B
- Azul :
- Dados a serem preenchidos
- ESCOPO CLIENTE
- Vermelho :
- Informações pendentes
- Ton Desag por mês (TSD/mês)
- Preto :
- resultados automáticos
- Teor de Sólido desaguado (%)
- Proposta
- Proposta D_054_2025
- Data
- DADOS DA OBRA
- QUANT
- HORAS /DIA
- Cliente
- SUZANO
- DRAGA
- x 3 Turnos
- Contato
- Jorge e Eduardo
- e-mail
- CENTRÍFUGA
- Jornada (dias)
- 2ª feira a sábado
- Dados da obra
- Prazo
- meses
- Objeto
- Dragagem e desaguamento lagoa de Emergência
- Eficiência Produtiva
- Local
- Suzano SP
- Vazão da Centrífuga
- #NAME?
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
- chute pois não temos a informação
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
- Horário de Trabalho (das 7 as 7h)
- h/dia
- 3 turnos de 8 horas cada
- Dias de Trabalho (2ª a sábado)
- dias/mês
- PRODUÇÃO TOTAL
- Ton Desag
- Produção alcançada em Aracruz

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `M7` | `=B26` |
| `M8` | `=B26` |
| `M10` | `=B27` |
| `L13` | `=Produção!M4` |
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
| `O25` | `=L25*L20` |
| `L27` | `=L22*K11` |
| `N28` | `=L28/0.25` |
| `L29` | `=L28*K11` |
| `L37` | `=L35/L36` |
| `L38` | `=L33*L34` |
| `L39` | `=L37/L38` |
| `O39` | `=SUM(O34:O38)` |
| `L40` | `=20+30` |
| `L42` | `=L40+40` |
| `L43` | `=(L42*L39)/L40` |
| `P43` | `=L43*(B26*B27)` |

### 2. Produção

- Faixa usada: `A1:S23`
- Fórmulas: **30**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **42**

#### Rótulos e textos observados

- PRODUÇÃO CENTRÍFUGA
- Horas Trabalhadas por mês
- Centrífuga 1
- Skid Velho
- m³/h
- DRAGA
- Unid.
- Quant.
- Centrífuga 2
- Nossa
- Vazão
- Horário de Trabalho (das 7 as 7h)
- Centrífuga 3
- a Comprar
- Eficiência
- %
- Dias de Trabalho (2ª a sábado)
- Concentração
- Total de Horas / mês
- Volume processado
- % SS entrada Centrífuga
- Ton SS / h
- Vazão Nominal Centrífuga =
- Volume por Dia
- dia
- Horas trabalhadas
- h/mês
- Eficiência operacional
- Vazão Operacional =
- (Estimativa experiência FOS)
- Produção mensal
- ton/mês
- Volume mensal
- m³/mês
- Cálculo do Prazo da obra
- Meses
- Volume total
- m³
- Mobilização
- QUANTIDADE TOTAL
- Ton SS
- Eficiência Real da Draga considerando vazão das Centrífugas:
- Operação
- desmob
- Horas
- Consumo
- Vazão Draga
- Prazo Operação
- meses
- Total
- trabalhadas
- litros/h
- Vazão Centrífugas
- Produção Mensal Ton Desag
- ton desag/mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D3` | `=H12` |
| `F3` | `='Dados Obra '!A26` |
| `H3` | `='Dados Obra '!B26` |
| `F4` | `='Dados Obra '!A27` |
| `H4` | `='Dados Obra '!B27` |
| `M4` | `=SUM(M1:M3)` |
| `H6` | `=H3*H4` |
| `D7` | `=D3*D4*D5` |
| `S7` | `=S3*S4*S5` |
| `D8` | `='Dados Obra '!L14` |
| `D10` | `=D3*D8` |
| `H10` | `='Dados Obra '!L13` |
| `S10` | `=S7*H3` |
| `D11` | `=H6*D4` |
| `S11` | `=H6` |
| `H12` | `=H10*H11` |
| `D13` | `=D10*D11` |
| `S13` | `=S7*S11` |
| `K16` | `=H3*D10` |
| `S16` | `=S13*G21` |
| `D18` | `=D13*G19` |
| `G19` | `=G21-G20-G17-G18` |
| `D21` | `=ROUNDUP(D18/D13,0)` |
| `E21` | `=D18/D13` |
| `G21` | `='Dados Obra '!K11` |
| `S21` | `=M4` |
| `K22` | `=H3*S22` |
| `M22` | `=K22*L22` |
| `S22` | `=S21/S20` |
| `D23` | `=D13/'Dados Obra '!M3` |

### 3. cronograma

- Faixa usada: `A1:V10`
- Fórmulas: **1**
- Conceitos provisórios: outros
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- DESCRIÇÃO DOS SERVIÇOS
- Mês 1
- Mês 2
- Mês 3
- ..... até .....
- Mês 12
- Plano de Trabalho
- Mobilização e Montagem da Draga
- Preparo da Base de Concreto para instalação das Centrífugas
- Mobilização e Montagem da Centrífuga 1
- Mobilização e Montagem da Centrífuga 2
- Mobilização e Montagem da Centrífuga 3
- Dragagem e desidratação em Centrífuga
- Transporte e destinação de lodo (SUZANO)
- Desmobilização

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `None` | `` |

### 4. Canteiro

- Faixa usada: `A1:N33`
- Fórmulas: **51**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **107**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
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
- TST e ADM
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
- #NAME?
- Brasmódulos para Jacareí
- Container Vestiário
- Container Escritório
- material de escritório
- Banheiro Quimico
- mes
- Mão de obra (integração)
- dia
- lançar docs no sistema após contratação + 1 dia integração + 2 dias aprovação + 2 dias pra entrar
- TOTAL
- Prazo de Operação
- preço unitário
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
| `E5` | `=E4` |
| `A6` | `=L9` |
| `C6` | `=(M9*N2)+M9` |
| `D6` | `=D4` |
| `E6` | `=E5` |
| `A7` | `=L10` |
| `C7` | `=(N10*N2)+N10` |
| `D7` | `=D4` |
| `E7` | `=E6` |
| `L7` | `=I7+J7+K7` |
| `N7` | `=M7*1.25` |
| `A8` | `=L12` |
| `C8` | `=N12` |
| `D8` | `=D7` |
| `E8` | `=E7` |
| `L8` | `=I8+J8+K8` |
| `N8` | `=M8*1.25` |
| `A9` | `=L11+L13` |
| `C9` | `=(M13*N2)+M13` |
| `D9` | `=D8` |
| `E9` | `=E8` |
| `L9` | `=I9+J9+K9` |
| `A10` | `=SUM(A4:A9)` |
| `F10` | `=A10*C10` |
| `N10` | `=M10*1.25` |
| `A11` | `=A10` |
| `F11` | `=A11*C11` |
| `F12` | `=SUM(F4:F11)` |
| `N12` | `=M12*1.25` |
| `M13` | `=M11` |
| `I14` | `=SUM(I7:I13)` |
| `J14` | `=SUM(J7:J13)` |
| `K14` | `=SUM(K8:K13)` |
| `L14` | `=SUM(I14:K14)` |
| `D15` | `=Produção!G21` |
| `F15` | `=D15*E15` |
| `D16` | `=D15` |
| `F20` | `=D20*E20` |
| `D26` | `=D15` |
| `E28` | `=F12` |
| `F29` | `=SUM(F15:F28)` |
| `F30` | `=Produção!G19` |
| `F31` | `=F29/F30` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |

### 5. 1.1.Mob. Draga

- Faixa usada: `A1:M40`
- Fórmulas: **57**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **114**

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
- Encarregado
- Técnico segurança / ADM
- TST / Adm
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
- Frete para Containers
- vb
- Mobiliário Canteiro
- Mobiliário Alojamento
- PGR + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- itens de segurança
- está na dragagem
- Tenda do Canteiro
- usaremos a edificação existente
- Bebedouro elétrico
- custo Exames médicos
- un
- Guindaste para carregamento em Cubatão
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- nosso TST pode aplicar
- Hospedagem da equipe (aluguel)
- mês
- #NAME?
- Estimativa para 2 casas
- Carreta Carga Seca para DRAGA
- Fabiano zap em 07/10/25 R$ 4.300 + 0,2% adv
- Guindaste p/descarregamento e montagem DRAGA
- cotado pelo Fabio (zap 07/10/25) empresa Truckup
- Mob / desmob Guindaste
- Plano de Rigger
- Reforma de edificação para canteiro e wc
- chute
- Mão de obra p MOBILIZAÇÃO DRAGA (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- Carreta 1 (draga)
- Carreta 2 (Tubulação 900 m)
- Carreta 3 (flutuantes e outros periféricos)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A5` | `=M5` |
| `C5` | `=' Canteiro'!C4` |
| `E5` | `=' Canteiro'!E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `=' Canteiro'!I8` |
| `M5` | `=SUM(I5:L5)` |
| `A6` | `=M6` |
| `C6` | `=' Canteiro'!C6` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `I6` | `=' Canteiro'!I9` |
| `A7` | `=M8` |
| `C7` | `=' Canteiro'!C7` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=M9` |
| `C8` | `=' Canteiro'!C9` |
| `E8` | `=E7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `I8` | `=' Canteiro'!I10` |
| `J8` | `=' Canteiro'!J10` |
| `K8` | `=' Canteiro'!K10` |
| `M8` | `=SUM(I8:L8)` |
| `A9` | `=A5+A8+A6+A7` |
| `C9` | `=' Canteiro'!C10` |
| `F9` | `=A9*C9` |
| `I9` | `=' Canteiro'!I11` |
| `J9` | `=' Canteiro'!J11` |
| `K9` | `=' Canteiro'!K11` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=A9` |
| `C10` | `=' Canteiro'!C11` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `M11` | `=SUM(I11:L11)` |
| `M12` | `=SUM(I12:L12)` |
| `F14` | `=D14*E14` |
| `F15` | `=D15*E15` |
| `F17` | `=D17*E17` |
| `D22` | `=' Canteiro'!A10` |
| `F24` | `=D24*E24` |
| `D25` | `=Produção!G17` |
| `E25` | `=2500*2` |
| `D26` | `=C40` |
| `F26` | `=D26*E26` |
| `F27` | `=D27*E27` |
| `F28` | `=D28*E28` |
| `F29` | `=D29*E29` |
| `F30` | `=D30*E30` |
| `F31` | `=D31*E31` |
| `E32` | `=F11` |
| `F33` | `=SUM(F14:F32)` |
| `F34` | `=F33*(E34/100)` |
| `F35` | `=SUM(F33:F34)` |
| `C40` | `=SUM(C37:C39)` |

### 6. 1.2.Mob Centrífuga

- Faixa usada: `A1:N39`
- Fórmulas: **87**
- Conceitos provisórios: mobilizacao_sistema, operacao_desaguamento
- Células numéricas observadas: **155**

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
- Encarregado
- Técnico segurança / ADM
- Tec segurança
- Operador de Draga
- ADM Tec
- Líder de Centrífuga
- Operador de Centrífuga
- DRAGA
- Ajudante Geral
- Operador Draga
- Refeições
- Ajudante Draga
- Transporte
- CENTRÍFUGA
- Custo por dia
- Líder Centrífuga
- Operador Centrífuga
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Verba para Cobertura do CENTRÍFUGA
- pç
- Loc up Tendas
- depreciação
- Instalações hidráulicas
- vb
- Materiais elétricos
- Largura
- compr
- esp
- m³
- Instalações elétricas
- Base de Concreto
- Guindaste p/descarregamento e montagem Centrífuga
- dia
- área de giro da rosca
- Mob / desmob Guindaste
- Base apoio Tq Equal.
- Plano de Rigger
- Carreta Carga Seca para CENTRÍFUGA (02 un)
- Concreto usinado 25 Mpa
- Bases de concreto para instal. Centrífuga e outros
- Forma de madeira
- Alvenaria de bloco para contenção da base (sinapi)
- m²
- Armação
- Mão de obra p/carga e montagem da planta (r$/dia)
- mês
- Mão de obra de aplicação
- TOTAL
- Preços unitários Sinapi
- R$ /m³
- BDI (%)
- Preço Final
- COTAÇÃO FÁBIO
- $ unit
- Quant
- $ Total
- Cabo Flexível 1KV 90G - 240mm
- Eletroduto PEAD 160mm
- Decanter Centrífuga Skid - 1
- Painel com Disjuntor 500A
- Tanque de Equalização - conjunto 1
- MDO para instalação

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `=' Canteiro'!C4` |
| `E5` | `=' Canteiro'!E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `=' Canteiro'!I8` |
| `M5` | `=SUM(I5:L5)` |
| `C6` | `=' Canteiro'!C6` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `I6` | `=' Canteiro'!I8` |
| `M6` | `=SUM(I6:L6)` |
| `C7` | `=' Canteiro'!C7` |
| `D7` | `=D5` |
| `E7` | `=E6` |
| `A8` | `=M13` |
| `C8` | `=' Canteiro'!C5` |
| `D8` | `=D6` |
| `E8` | `=E7` |
| `A9` | `=M14` |
| `C9` | `=' Canteiro'!C8` |
| `D9` | `=D7` |
| `E9` | `=E8` |
| `A10` | `=M15` |
| `C10` | `=' Canteiro'!C9` |
| `E10` | `=E9` |
| `I10` | `=' Canteiro'!I10` |
| `J10` | `=' Canteiro'!J10` |
| `K10` | `=' Canteiro'!K10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=SUM(A5:A10)` |
| `C11` | `=' Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `I11` | `=' Canteiro'!I11` |
| `J11` | `=' Canteiro'!J11` |
| `K11` | `=' Canteiro'!K11` |
| `M11` | `=SUM(I11:L11)` |
| `A12` | `=A11` |
| `C12` | `=' Canteiro'!C11` |
| `F12` | `=A12*C12` |
| `F13` | `=SUM(F5:F12)` |
| `I13` | `=' Canteiro'!I12` |
| `J13` | `=' Canteiro'!J12` |
| `K13` | `=' Canteiro'!K12` |
| `M13` | `=SUM(I13:L13)` |
| `I14` | `=' Canteiro'!I12` |
| `J14` | `=' Canteiro'!J12` |
| `K14` | `=' Canteiro'!K12` |
| `M14` | `=SUM(I14:L14)` |
| `I15` | `=' Canteiro'!I13` |
| `J15` | `=' Canteiro'!J13` |
| `K15` | `=' Canteiro'!K13` |
| `M15` | `=SUM(I15:L15)` |
| `E17` | `=J17*N17` |
| `F17` | `=D17*E17` |
| `F18` | `=D18*E18` |
| `E19` | `=M31+M32+M33` |
| `F19` | `=D19*E19` |
| `E20` | `=M34` |
| `F20` | `=D20*E20` |
| `N20` | `=M20*L20*K20` |
| `E21` | `='1.1.Mob. Draga'!E27` |
| `F21` | `=D21*E21` |
| `N21` | `=M21*L21*K21` |
| `E22` | `='1.1.Mob. Draga'!E28` |
| `F22` | `=D22*E22` |
| `N22` | `=K22*L22*M22` |
| `E23` | `='1.1.Mob. Draga'!E29` |
| `F23` | `=D23*E23` |
| `N23` | `=SUM(N20:N22)` |
| `D24` | `=C39` |
| `E24` | `='1.1.Mob. Draga'!E26` |
| `N24` | `=L24*M24` |
| `E25` | `=N28*1.1` |
| `F25` | `=D25*E25` |
| `N25` | `=M25*L25` |
| `F26` | `=D26*E26` |
| `N26` | `=L26*M26` |
| `E27` | `=F13` |
| `N27` | `=L27*M27` |
| `F28` | `=SUM(F17:F27)` |
| `N28` | `=SUM(N24:N27)` |
| `F29` | `=F28*(E29/100)` |
| `F30` | `=SUM(F28:F29)` |
| `L31` | `=4*150*1.1` |
| `M31` | `=K31*L31` |
| `M32` | `=K32*L32` |
| `M35` | `=SUM(M31:M34)` |
| `C39` | `=SUM(C33:C38)` |

### 7. 2.1. Draga Dec

- Faixa usada: `A1:M206`
- Fórmulas: **107**
- Conceitos provisórios: outros
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `=Produção!H6` |
| `D9` | `=Produção!S22` |
| `F9` | `=L11` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=(C9*D9*E9*L10)*0.1` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `K20` | `='Dados Obra '!B27` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `B21` | `=' Canteiro'!I8` |
| `D21` | `=' Canteiro'!C4` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `B22` | `='1.1.Mob. Draga'!A7` |
| `D22` | `=' Canteiro'!C7` |
| `A23` | `=L24` |
| `B23` | `='1.1.Mob. Draga'!A8` |
| `D23` | `=' Canteiro'!C9` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `B24` | `='1.1.Mob. Draga'!A6` |
| `D24` | `=' Canteiro'!C6` |
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
| `A37` | `=' Canteiro'!E4` |
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
| `B109` | `='1.1.Mob. Draga'!A9` |
| `E109` | `=B109*D109` |
| `I109` | `='Dados Obra '!H17/12*3` |
| `K109` | `=I109*J109` |
| `J110` | `=K109/I110` |
| `E111` | `=' Canteiro'!F31` |
| `J111` | `=K109*(1/100)` |
| `B112` | `=B109` |
| `E112` | `=D112*B112` |
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
| `G134` | `=E131+D114+H99+G87+E15` |
| `E138` | `=G134*(5/100)` |
| `E139` | `=G134*(5/100)` |
| `E142` | `=E138+E139` |
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

- Faixa usada: `A1:M205`
- Fórmulas: **111**
- Conceitos provisórios: operacao_desaguamento
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 7.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `F7` | `=K9+K14+K16` |
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
| `B21` | `=' Canteiro'!A5` |
| `D21` | `=' Canteiro'!C5` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `A23` | `=L24` |
| `B23` | `='1.2.Mob Centrífuga'!M15` |
| `D23` | `=' Canteiro'!C9` |
| `L23` | `=J23*K23` |
| `A24` | `=L24` |
| `B24` | `='1.2.Mob Centrífuga'!M13` |
| `D24` | `=' Canteiro'!C8` |
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
| `A37` | `=' Canteiro'!E4` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `B52` | `=B24+B21` |
| `D52` | `='2.1. Draga Dec'!D52` |
| `E52` | `='2.1. Draga Dec'!E52` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B23` |
| `D53` | `='2.1. Draga Dec'!D53` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `C59` | `='2.1. Draga Dec'!C59` |
| `C60` | `='2.1. Draga Dec'!C60` |
| `C62` | `='2.1. Draga Dec'!C62` |
| `E62` | `=C59+C60+C61+C62` |
| `B69` | `=B52/2` |
| `D69` | `='2.1. Draga Dec'!D69` |
| `E69` | `=D69*B69` |
| `E71` | `=SUM(E67:E69)` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E92` | `=F7*(0.1/100)` |
| `E97` | `=E92+E93+E94+E95` |
| `H99` | `=E97` |
| `I104` | `='Dados Obra '!B16` |
| `K104` | `=I104*J104` |
| `J105` | `=K104/I105` |
| `E106` | `=B106*D106` |
| `J106` | `=K104*(1/100)` |
| `B107` | `='2.1. Draga Dec'!B107` |
| `D107` | `='2.1. Draga Dec'!D107` |
| `E107` | `=B107*D107` |
| `J107` | `=SUM(J105:J106)` |
| `E108` | `=D108*B108` |
| `E109` | `=(B109*D109)/Produção!G19` |
| `I109` | `=('Dados Obra '!B17/12)*3` |
| `K109` | `=I109*J109` |
| `J110` | `=K109/I110` |
| `B111` | `='1.2.Mob Centrífuga'!A11` |
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
| `G134` | `=E131+D114+H99+G87+E15` |
| `E138` | `=G134*(5/100)` |
| `E139` | `=G134*(5/100)` |
| `E142` | `=E138+E139` |
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

- Faixa usada: `A1:L25`
- Fórmulas: **45**
- Conceitos provisórios: outros
- Células numéricas observadas: **76**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Encarregado
- Mão de OBRA
- TURNOS
- Técnico de Segurança
- 1º
- 2º
- 3º
- Operador de Draga
- Engº
- Operador de Centrífuga
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
- Visita Trimestral técnico GRATT
- un
- mês
- GRATT - manutenção mecânica preventiva - incluindo MDO de troca peças
- Serviços de reparos Elétricos (3 diárias por mês
- Mão de obra (de acompanhamento)
- #NAME?
- TOTAL
- Prazo de Operação
- preço unitário
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A4` | `=L7` |
| `C4` | `=' Canteiro'!C4` |
| `E4` | `=' Canteiro'!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `A5` | `=L8` |
| `C5` | `=' Canteiro'!C6` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `A6` | `=L9` |
| `C6` | `=' Canteiro'!C7` |
| `D6` | `=D4` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `L6` | `=I6+J6+K6` |
| `A7` | `=L11` |
| `C7` | `=' Canteiro'!C8` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `L7` | `=I7+J7+K7` |
| `A8` | `=L10+L12` |
| `C8` | `=' Canteiro'!C9` |
| `E8` | `=E7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `L8` | `=I8+J8+K8` |
| `A9` | `=SUM(A4:A8)` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F4:F10)` |
| `I13` | `=SUM(I6:I12)` |
| `J13` | `=SUM(J7:J12)` |
| `K13` | `=SUM(K7:K12)` |
| `L13` | `=SUM(I13:K13)` |
| `F14` | `=D14*E14` |
| `F16` | `=D16*E16` |
| `D18` | `=D20` |
| `D20` | `=Produção!D21` |
| `E20` | `=F11` |
| `F21` | `=SUM(F14:F20)` |
| `F22` | `=Produção!G19` |
| `F23` | `=F21/F22` |
| `F24` | `=F23*(E24/100)` |
| `F25` | `=F23+F24` |

### 10. DesMob. Draga

- Faixa usada: `A1:M40`
- Fórmulas: **52**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **105**

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
- Encarregado
- Técnico segurança / ADM
- TST / Adm
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
- Frete para Containers
- vb
- Mobiliário Canteiro
- Mobiliário Alojamento
- PGR + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- itens de segurança
- Tenda do Canteiro
- Bebedouro elétrico
- custo Exames médicos
- un
- Guindaste para carregamento em Cubatão
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Hospedagem da equipe (aluguel)
- mês
- Carreta Carga Seca para DRAGA
- Fabiano zap em 07/10/25 R$ 4.300 + 0,2% adv
- Guindaste p/descarregamento e montagem DRAGA
- cotado pelo Fabio (zap 07/10/25) empresa Truckup
- Mob / desmob Guindaste
- Plano de Rigger
- Reforma de edificação para canteiro e wc
- chute
- Mão de obra p MOBILIZAÇÃO DRAGA (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- Carreta 1 (draga)
- Carreta 2 (Tubulação 900 m)
- Carreta 3 (flutuantes e outros periféricos)

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `A5` | `=M5` |
| `C5` | `=' Canteiro'!C4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `=' Canteiro'!I8` |
| `M5` | `=SUM(I5:L5)` |
| `A6` | `=M6` |
| `C6` | `=' Canteiro'!C6` |
| `D6` | `=D5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `I6` | `=' Canteiro'!I9` |
| `A7` | `=M8` |
| `C7` | `=' Canteiro'!C7` |
| `D7` | `=D6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=M9` |
| `C8` | `=' Canteiro'!C9` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `I8` | `=' Canteiro'!I10` |
| `J8` | `=' Canteiro'!J10` |
| `K8` | `=' Canteiro'!K10` |
| `M8` | `=SUM(I8:L8)` |
| `A9` | `=A5+A8+A6+A7` |
| `C9` | `=' Canteiro'!C10` |
| `F9` | `=A9*C9` |
| `I9` | `=' Canteiro'!I11` |
| `J9` | `=' Canteiro'!J11` |
| `K9` | `=' Canteiro'!K11` |
| `M9` | `=SUM(I9:L9)` |
| `A10` | `=A9` |
| `C10` | `=' Canteiro'!C11` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `M11` | `=SUM(I11:L11)` |
| `M12` | `=SUM(I12:L12)` |
| `F14` | `=D14*E14` |
| `F15` | `=D15*E15` |
| `F17` | `=D17*E17` |
| `D22` | `=' Canteiro'!A10` |
| `F24` | `=D24*E24` |
| `E25` | `=2500*2` |
| `D26` | `=C40` |
| `F26` | `=D26*E26` |
| `F27` | `=D27*E27` |
| `F28` | `=D28*E28` |
| `F29` | `=D29*E29` |
| `F30` | `=D30*E30` |
| `F31` | `=D31*E31` |
| `E32` | `=F11` |
| `F33` | `=SUM(F14:F32)` |
| `F34` | `=F33*(E34/100)` |
| `F35` | `=SUM(F33:F34)` |
| `C40` | `=SUM(C37:C39)` |

### 11. DesMob Centrífuga

- Faixa usada: `A1:N39`
- Fórmulas: **76**
- Conceitos provisórios: mobilizacao_sistema, operacao_desaguamento, desmobilizacao
- Células numéricas observadas: **149**

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
- Encarregado
- Técnico segurança / ADM
- Tec segurança
- Operador de Draga
- ADM Tec
- Líder de Centrífuga
- Operador de Centrífuga
- DRAGA
- Ajudante Geral
- Operador Draga
- Refeições
- Ajudante Draga
- Transporte
- CENTRÍFUGA
- Custo por dia
- Líder Centrífuga
- Operador Centrífuga
- Ajudante Centrífuga
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Verba para Cobertura do CENTRÍFUGA
- pç
- Loc up Tendas
- depreciação
- Instalações hidráulicas
- vb
- Materiais elétricos
- Largura
- compr
- esp
- m³
- Instalações elétricas
- Base de Concreto
- Guindaste p/descarregamento e montagem Centrífuga
- dia
- área de giro da rosca
- Mob / desmob Guindaste
- Base apoio Tq Equal.
- Plano de Rigger
- Carreta Carga Seca para CENTRÍFUGA (02 un)
- Concreto usinado 25 Mpa
- Bases de concreto para instal. Centrífuga e outros
- Forma de madeira
- Alvenaria de bloco para contenção da base (sinapi)
- m²
- Armação
- Mão de obra p/carga e montagem da planta (r$/dia)
- mês
- Mão de obra de aplicação
- TOTAL
- Preços unitários Sinapi
- R$ /m³
- BDI (%)
- Preço Final
- COTAÇÃO FÁBIO
- $ unit
- Quant
- $ Total
- Cabo Flexível 1KV 90G - 240mm
- Eletroduto PEAD 160mm
- Decanter Centrífuga Skid - 1
- Painel com Disjuntor 500A
- Tanque de Equalização - conjunto 1
- MDO para instalação

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `=' Canteiro'!C4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `I5` | `=' Canteiro'!I8` |
| `M5` | `=SUM(I5:L5)` |
| `C6` | `=' Canteiro'!C6` |
| `D6` | `=D5` |
| `I6` | `=' Canteiro'!I8` |
| `C7` | `=' Canteiro'!C7` |
| `D7` | `=D5` |
| `A8` | `=M13` |
| `C8` | `=' Canteiro'!C5` |
| `D8` | `=D6` |
| `A9` | `=M14` |
| `C9` | `=' Canteiro'!C8` |
| `D9` | `=D7` |
| `A10` | `=M15` |
| `C10` | `=' Canteiro'!C9` |
| `I10` | `=' Canteiro'!I10` |
| `J10` | `=' Canteiro'!J10` |
| `K10` | `=' Canteiro'!K10` |
| `M10` | `=SUM(I10:L10)` |
| `A11` | `=SUM(A5:A10)` |
| `C11` | `=' Canteiro'!C10` |
| `F11` | `=A11*C11` |
| `I11` | `=' Canteiro'!I11` |
| `J11` | `=' Canteiro'!J11` |
| `K11` | `=' Canteiro'!K11` |
| `M11` | `=SUM(I11:L11)` |
| `A12` | `=A11` |
| `C12` | `=' Canteiro'!C11` |
| `F12` | `=A12*C12` |
| `F13` | `=SUM(F5:F12)` |
| `I13` | `=' Canteiro'!I12` |
| `J13` | `=' Canteiro'!J12` |
| `K13` | `=' Canteiro'!K12` |
| `M13` | `=SUM(I13:L13)` |
| `I14` | `=' Canteiro'!I12` |
| `J14` | `=' Canteiro'!J12` |
| `K14` | `=' Canteiro'!K12` |
| `M14` | `=SUM(I14:L14)` |
| `I15` | `=' Canteiro'!I13` |
| `J15` | `=' Canteiro'!J13` |
| `K15` | `=' Canteiro'!K13` |
| `M15` | `=SUM(I15:L15)` |
| `E17` | `=J17*N17` |
| `F17` | `=D17*E17` |
| `F18` | `=D18*E18` |
| `E19` | `=M31+M32+M33` |
| `F19` | `=D19*E19` |
| `E20` | `=M34` |
| `F20` | `=D20*E20` |
| `N20` | `=M20*L20*K20` |
| `E21` | `='1.1.Mob. Draga'!E27` |
| `F21` | `=D21*E21` |
| `N21` | `=M21*L21*K21` |
| `E22` | `='1.1.Mob. Draga'!E28` |
| `N22` | `=K22*L22*M22` |
| `E23` | `='1.1.Mob. Draga'!E29` |
| `N23` | `=SUM(N20:N22)` |
| `D24` | `=C39` |
| `E24` | `='1.1.Mob. Draga'!E26` |
| `N24` | `=L24*M24` |
| `E25` | `=N28*1.1` |
| `N25` | `=M25*L25` |
| `N26` | `=L26*M26` |
| `E27` | `=F13` |
| `N27` | `=L27*M27` |
| `F28` | `=SUM(F17:F27)` |
| `N28` | `=SUM(N24:N27)` |
| `F29` | `=F28*(E29/100)` |
| `F30` | `=SUM(F28:F29)` |
| `L31` | `=4*150*1.1` |
| `M31` | `=K31*L31` |
| `M32` | `=K32*L32` |
| `M35` | `=SUM(M31:M34)` |
| `C39` | `=SUM(C33:C38)` |

### 12. Plan. Final

- Faixa usada: `A1:M25`
- Fórmulas: **47**
- Conceitos provisórios: outros
- Células numéricas observadas: **60**

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
- 1.1
- Mobilização Draga
- vb
- 1.2
- Mobilização Centrífugas
- Dragagem e desaguamento Centrífuga
- 2.1
- Operação da Draga
- #NAME?
- TSd
- 2.2
- Operação Centrífuga
- 2.3
- Manutenção dos equipamentos
- Desmobilização
- 3.1
- 3.2
- Preço de Venda
- possível desc 10% pra negociação
- Custo de Operação
- Valor de Venda operação
- Quantidade em Tonelada de Sólidos Secos (TSs)
- RESULTADO
- Custo de Operação em TSS
- Preço praticado em Aracruz
- RESULTADO MENSAL
- Valor de Venda em Tonelada Seca
- ton seca

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `L4` | `=I4+I5+I6` |
| `C5` | `='1.1.Mob. Draga'!F33` |
| `G5` | `=C5/E5` |
| `I5` | `=((H5/100)+1)*G5` |
| `J5` | `=E5*I5` |
| `C6` | `='1.2.Mob Centrífuga'!F28` |
| `G6` | `=C6/E6` |
| `I6` | `=((H6/100)+1)*G6` |
| `J6` | `=E6*I6` |
| `C9` | `='2.1. Draga Dec'!D201` |
| `E9` | `='Dados Obra '!M2*Produção!G19` |
| `G9` | `=C9/E9` |
| `I9` | `=((H9/100)+1)*G9` |
| `J9` | `=E9*I9` |
| `L9` | `=I9+I10+I11` |
| `C10` | `='2.2 Centrífuga'!D199` |
| `E10` | `=E9` |
| `F10` | `=F9` |
| `G10` | `=C10/E10` |
| `I10` | `=((H10/100)+1)*G10` |
| `J10` | `=E10*I10` |
| `C11` | `='2.3. manutenção'!F21` |
| `E11` | `=E9` |
| `F11` | `=F10` |
| `G11` | `=C11/E11` |
| `C14` | `='DesMob. Draga '!F33` |
| `G14` | `=C14/E14` |
| `I14` | `=((H14/100)+1)*G14` |
| `J14` | `=E14*I14` |
| `L14` | `=J14+J15` |
| `C15` | `='DesMob Centrífuga'!F28` |
| `G15` | `=C15/E15` |
| `I15` | `=((H15/100)+1)*G15` |
| `J15` | `=E15*I15` |
| `C17` | `=SUM(C4:C16)` |
| `J17` | `=SUM(J4:J16)` |
| `L17` | `=J17*0.9` |
| `C19` | `=J17-C17` |
| `J19` | `=J17/E9` |
| `C22` | `=C9+C10+C11` |
| `J22` | `=C22` |
| `C23` | `=J9+J10+J11` |
| `J23` | `='Plan. Final'!E9*'Dados Obra '!M3` |
| `C24` | `=C23-C22` |
| `J24` | `=J22/J23` |
| `C25` | `=C24/Produção!G19` |
| `J25` | `=(J9+J10+J11)/J23` |

### 13. Final

- Faixa usada: `A1:L6`
- Fórmulas: **11**
- Conceitos provisórios: outros
- Células numéricas observadas: **19**

#### Rótulos e textos observados

- Preço Apresentado na Concorrência que Perdemos para Allonda e Dragagem Brasil
- ITEM
- DESCRIÇÃO DOS SERVIÇOS
- UN
- QUANT
- PREÇO UNIT
- PREÇO TOTAL
- Preço unitário Venda ATUAL
- Mobilização e Montagem dos Equipamentos de Dragagem, Planta de Desidratação e Canteiro de Obras
- vb
- Dragagem e desidratação de lodo através do processo de Centrifugação
- tonelada
- BDI 50%
- Desmobilização dos Equipamentos e Desmontagem do Canteiro de Obras
- VALOR TOTAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `E3` | `=I3` |
| `F3` | `=D3*E3` |
| `I3` | `='Plan. Final'!J5+'Plan. Final'!J6` |
| `D4` | `='Plan. Final'!E9` |
| `E4` | `=I4` |
| `F4` | `=D4*E4` |
| `I4` | `='Plan. Final'!L9` |
| `E5` | `=I5+2534.85` |
| `F5` | `=D5*E5` |
| `I5` | `='Plan. Final'!J14+'Plan. Final'!J15` |
| `F6` | `=SUM(F3:F5)` |

### 14. Planilha1

- Faixa usada: `A1:B14`
- Fórmulas: **1**
- Conceitos provisórios: resumo_comercial
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- QUADRO DE RESUMO TÉCNICO DA PROPOSTA
- RESPONSABILIDADE TÉCNICA
- Emissão e apresentação de ART (anotação de responsabilidade técnica) emitida junto ao Conselhor Regional de Engenharia
- Certificado de Regularidade com Ministério de Meio Ambiente - Certificado IBAMA
- MÃO DE OBRA ESPECIALIZADA
- Operadores de Draga com larga experiência, que atuaram nas últimas obras executadas para Suzano em Jacareí e Aracruz
- Supervisão técnica de engenheiros responsáveis técnicos da empresa e que supervisionaram as últimas obras executadas para Suzano
- EQUIPAMENTOS
- a DRAGA de sucção e recalque com DESAGREGADOR motor a diesel vazão nominal de operação de 350 m³/h
- CENTRÍFUGA 1 - Skid completo que atuou com sucesso na obra de Jacareí em 2023 e Aracruz 2024/25(vazão de operação 40m³/h)
- CENTRÍFUGA 2 - ano de fabricação 2024 e que atuou com sucesso na obra de Aracruz (vazão de operação 40m³/h)
- CENTRÍFUGA 3 - todo o conjunto completamente NOVO (vazão de operação 40m³/h)
- Plano de manutenção preventiva semanal com equipe de operação e trimestral com técnicos da fabricante das Centrífugas - GRATT
- OUTROS
- Jornada de trabalho : das 7h00 às 7h00 de 2ª feira à sábado
- Vazão de Operação da draga de até 350 m³/h
- Vazão de Operação das Centrífugas 40 m³/h cada

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
