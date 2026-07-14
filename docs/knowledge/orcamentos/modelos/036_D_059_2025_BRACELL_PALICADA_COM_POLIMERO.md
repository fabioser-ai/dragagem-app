# Modelo 036 — D_059_2025 - Bracell - paliçada COM polímero.xlsx

## Status

- Análise estrutural automatizada concluída.
- Documento gerado a partir do arquivo original recebido por Fabio.
- Interpretações de negócio ainda dependem de validação humana quando não forem evidentes.

## Identificação da fonte

- Arquivo original: `D_059_2025 - Bracell - paliçada COM polímero.xlsx`
- Família provisória: **Dragagem com paliçada/bacia**
- SHA-256 do arquivo: `4bbd6b886f36f130a358799cfc904292375330d0db9158764df71b665de622bc`
- Abas analisadas: **16**
- Fórmulas encontradas: **594**

## Conceitos identificados

- `outros`: 4 aba(s)
- `mobilizacao_draga`: 2 aba(s)
- `barrilete_linha`: 1 aba(s)
- `canteiro`: 1 aba(s)
- `dados_obra`: 1 aba(s)
- `desmobilizacao`: 1 aba(s)
- `dragagem_operacao`: 1 aba(s)
- `estrutura_desaguamento`: 1 aba(s)
- `formacao_preco`: 1 aba(s)
- `medicao_batimetria`: 1 aba(s)
- `mobilizacao_sistema`: 1 aba(s)
- `producao_prazo`: 1 aba(s)
- `resumo_comercial`: 1 aba(s)

## Inventário das abas

| Ordem | Aba | Faixa usada | Fórmulas | Conceitos provisórios |
|---:|---|---|---:|---|
| 1 | `Dados Obra` | `A1:S27` | 13 | dados_obra |
| 2 | `Dados Técnicos` | `A1:H10` | 13 | outros |
| 3 | `Resumo Técnico` | `A1:B11` | 1 | resumo_comercial |
| 4 | `Produção` | `A1:R37` | 43 | producao_prazo |
| 5 | `1. Canteiro` | `A1:M32` | 46 | canteiro |
| 6 | `2.1 Mob. Draga` | `A1:G41` | 42 | mobilizacao_draga |
| 7 | `2.2. Mob. Eq. Polimero` | `A1:M26` | 35 | mobilizacao_sistema |
| 8 | `2.2.1 Barrilete` | `A1:F32` | 36 | barrilete_linha |
| 9 | `3. Paliçada` | `A1:M28` | 39 | estrutura_desaguamento |
| 10 | `3.1 Impermeabilização` | `A1:L22` | 44 | outros |
| 11 | `4.1 Dragagem` | `A1:Q253` | 95 | dragagem_operacao |
| 12 | `Op. Polimero` | `A1:M37` | 38 | outros |
| 13 | `4.4. Medição` | `A1:K28` | 37 | medicao_batimetria |
| 14 | `6.1 Desmob. Draga` | `A1:G35` | 42 | mobilizacao_draga, desmobilizacao |
| 15 | `Plan. Preços` | `A1:N17` | 50 | formacao_preco |
| 16 | `Plan Final` | `A1:H7` | 20 | outros |

## Dependências entre abas observadas

| Aba referenciada | Ocorrências em fórmulas |
|---|---:|
| `1. Canteiro` | 38 |
| `Dados Obra` | 23 |
| `2.1 Mob. Draga` | 17 |
| `Plan. Preços` | 9 |
| `4.4. Medição` | 8 |
| `3. Paliçada` | 7 |
| `3.1 Impermeabilização` | 4 |
| `2.2. Mob. Eq. Polimero` | 2 |
| `Op. Polimero` | 2 |
| `2.2.1 Barrilete` | 1 |
| `4.1 Dragagem` | 1 |
| `6.1 Desmob. Draga` | 1 |

## Análise por aba

### 1. Dados Obra

- Faixa usada: `A1:S27`
- Fórmulas: **13**
- Conceitos provisórios: dados_obra
- Células numéricas observadas: **26**

#### Rótulos e textos observados

- BACIA ECOLÓGICA - OPÇÃO 1
- Azul :
- Dados a serem preenchidos
- Vermelho :
- Informações pendentes
- Preto :
- resultados automáticos
- Proposta
- Proposta D_059_2025
- Data
- OPÇÃO 1 :
- COM POLÍMERO
- Cliente
- BRACELL - Lençóis Paulista
- OPÇÃO 2 :
- SEM POLÍMERO
- Contato
- e-mail
- Dados da obra
- Objeto
- Dragagem lagoas Norte e Sul
- ESCOPO
- in situ
- desag. FOS
- Seco
- Desag.
- Local
- Lençóis Paulista
- Lagoa Norte
- m³
- Volume dragagem (m³)
- Lagoa Sul
- Tipo de material
- fibra de madeira e areia
- Distância de Recalque (m)
- Seio da linha =
- Total
- Linha Flutuante (m)
- TOTAL
- Linha de terra (m)
- Profundidade de dragagem (m)
- Espessura média de dragagem (m)
- Área de Dragagem (m² ou L x C)
- X
- Volume (m³) =
- Tipo de Bota Fora
- PALIÇADA
- Sistema de Medição
- preços unitários de serviços
- Canteiro de obras
- FOS
- Mobilização
- Horário de Trabalho (das 7 as 17h)
- h/dia
- Dias de Trabalho (2ª a sábado)
- dias/mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `P13` | `=O13*2` |
| `Q13` | `=M13*O13` |
| `R13` | `=Q13/P13` |
| `B14` | `=M17` |
| `Q14` | `=M14*O14` |
| `R14` | `=Q14/P14` |
| `H16` | `=B16+E16` |
| `H17` | `=B17+E17` |
| `M17` | `=SUM(M13:M16)` |
| `Q17` | `=SUM(Q13:Q16)` |
| `R17` | `=SUM(R13:R16)` |
| `S17` | `=M17/R17` |
| `G21` | `=B21*D21*B20` |

### 2. Dados Técnicos

- Faixa usada: `A1:H10`
- Fórmulas: **13**
- Conceitos provisórios: outros
- Células numéricas observadas: **15**

#### Rótulos e textos observados

- LAGOAS
- Volume de Lodo a Dragar (m³)
- % ST in situ
- % ST desaguado
- Volume de Lodo em Base Seca (m³)
- Volume de Lodo Desaguado (m³)
- Lagoa Norte
- Lagoa Sul7
- TOTAL
- Dado em AZUL estimado pela Fos
- Dimensão da Bacia Ecológica
- Prazo

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D2` | `='Dados Obra '!M13` |
| `E2` | `='Dados Obra '!O13` |
| `F2` | `=E2*2` |
| `G2` | `=D2*E2` |
| `H2` | `=G2/F2` |
| `D3` | `='Dados Obra '!M14` |
| `E3` | `='Dados Obra '!O14` |
| `G3` | `=D3*E3` |
| `H3` | `=G3/F3` |
| `D6` | `=SUM(D2:D5)` |
| `G6` | `=SUM(G2:G5)` |
| `H6` | `=SUM(H2:H5)` |
| `H10` | `=H6/2000` |

### 3. Resumo Técnico

- Faixa usada: `A1:B11`
- Fórmulas: **1**
- Conceitos provisórios: resumo_comercial
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- RESPONSABILIDADE TÉCNICA
- Registro de empresa e profissionais junto ao CREA - Conselhor Regional de Engenharia
- Draga com TIE (Título de Inscrição de Embarcação) junto a Autoridade Marítma Brasileira
- Laudo de Flutuabilidade e Estanqueidade das Dragas
- Certificado de Regularidade com Ministério de Meio Ambiente - Certificado IBAMA
- MÃO DE OBRA ESPECIALIZADA
- Operador de Draga com larga experiência em dragagem de lagoas de fábricas de papel e celulose
- Supervisão técnica de engenheiros responsáveis técnicos da empresa com larga experiência em atividades de dragagem e desaguamento
- EQUIPAMENTOS
- DRAGA flutuante de sucção e recalque com bomba de 10 x 8", vazão nominal de operação de 350m³/h, com sistema de varredura e com desagregador (ideal para dragagem de areia e lodo)
- Plano de Manutenção preventiva e corretiva
- MATERIAIS EMPREGADOS
- Manta filtrante (Filter MAX 50 - HUESKER) adquirida junto a empresa multinacional com produtos reconhecidos mundialmente pela qualidade, resistência e eficiência em cada uma de suas aplicações
- Manta PEAD para impermeabilização de base em espessura adequada para união por solda em termofusão, garantindo a estanqueidade da Bacia de desague

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `None` | `` |

### 4. Produção

- Faixa usada: `A1:R37`
- Fórmulas: **43**
- Conceitos provisórios: producao_prazo
- Células numéricas observadas: **74**

#### Rótulos e textos observados

- Cálculo de Produção da Draga
- Horas Trabalhadas por mês
- Consumo de diesel
- Unid.
- Quant.
- litros por hora
- Vazão
- m³/h
- Horas / dia (7 as 17h)
- eficiência
- Eficiência
- %
- Dias / Mês (2ª a sexta)
- horas por dia
- Concentração
- dias por mês
- Total de Horas / mês
- prazo em meses
- TOTAL
- litros
- Produção
- Horas trabalhadas
- h/mês
- PALIÇADA
- CICLO DE OPERAÇÃO DAS BACIAS
- ÁREA DE BACIA
- M²
- MESES DE OPERAÇÃO
- BACIAS
- BACIAS em m³
- Produção mensal (m³/mês)
- Perímetro
- A
- B
- C
- Largura de perda p/montagem paliçada
- Dragando
- Perda de área com a paliçada
- m²
- secando
- Cálculo do Prazo da obra
- Área interna útil da Paliçada
- limpar
- Altura de enchimento
- Produção mensal
- m³/mês
- Capacidade Volumétrica da Bacia
- m³
- Volume a acondicionar na Bacia
- Dimensão Total necessária da Bacia
- Quantidade total a dragar
- Quantidades para manter o ciclo
- unidades
- LIMPEZA:
- Responsabilidade BRACELL
- PRAZO
- Prazo de Execução
- mês
- Mobilização
- Paliçada
- Dragagem
- Produção de lodo desaguado (m³/mês)
- Destinação
- Carga transp e destinação - responsabilidade Bracell
- dias úteis por bacia
- Largura
- Comprimento
- M2
- PERIMETRO
- Altura Enchimento
- Volume Bacia
- Nº utilizaçao
- Volume Final
- BACIA 1
- BACIA 2
- BACIA 3

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `H3` | `='Dados Obra '!B26` |
| `H4` | `='Dados Obra '!B27` |
| `J4` | `=H3` |
| `J5` | `=H4` |
| `H6` | `=H3*H4` |
| `J6` | `=D25` |
| `J7` | `=J2*J3*J4*J5*J6` |
| `D8` | `=D3*(D4/100)*(D5/100)` |
| `D11` | `=H6` |
| `I12` | `=G37` |
| `D13` | `=D8*D11` |
| `I13` | `=H37` |
| `D14` | `=D13/'Dados Obra '!S17` |
| `P14` | `=D14` |
| `I15` | `=I14*I13` |
| `Q15` | `=P14` |
| `I16` | `=I12` |
| `R16` | `=Q15` |
| `P17` | `=R16` |
| `D18` | `=D13` |
| `I18` | `=I16*I17` |
| `Q18` | `=I19-(P14+Q15+R16+P17)` |
| `I19` | `='Dados Obra '!R17` |
| `I20` | `=I19/I17` |
| `D21` | `='Dados Obra '!B14` |
| `D25` | `=D21/D18` |
| `G27` | `=ROUNDUP(D25,0)` |
| `D29` | `=I19/D25` |
| `G29` | `=SUM(G25:G28)` |
| `G33` | `=E33*F33` |
| `H33` | `=(E33*2)+(F33*2)` |
| `J33` | `=G33*I33` |
| `L33` | `=J33*K33` |
| `G34` | `=E34*F34` |
| `H34` | `=(E34*2)+(F34*2)` |
| `J34` | `=G34*I34` |
| `L34` | `=J34*K34` |
| `G35` | `=E35*F35` |
| `H35` | `=(E35*2)+(F35*2)` |
| `G37` | `=SUM(G33:G36)` |
| `H37` | `=SUM(H33:H36)` |
| `J37` | `=SUM(J33:J36)` |
| `L37` | `=SUM(L33:L36)` |

### 5. 1. Canteiro

- Faixa usada: `A1:M32`
- Fórmulas: **46**
- Conceitos provisórios: canteiro
- Células numéricas observadas: **91**

#### Rótulos e textos observados

- CANTEIRO DE OBRAS : subitem da Dragagem
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- R$ / mês
- $/h
- dissídio 5%
- Trasnf 25%
- Encarregado
- Engenheiro
- Operador Draga
- Operador de preparo de polímero
- Ajudante Geral
- Opera bomba sub
- Refeições
- Op. Polímero
- Transporte
- Ajudante
- Custo por dia
- TEC segurança
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Container almoxarifado
- mês
- #NAME?
- LOC Container (14) 98103-8686 cotação via zap (R$ 890,00/mês)
- Container Sanitário/Vestiário
- Container Escritório com AR
- LOC Container (14) 98103-8686 cotação via zap (R$ 1.450,00/mês)
- Tenda para Canteiro
- Loc up - Tenda de 8 x 8 p/Aracruz c/fech. laterais
- deprec.
- meses
- material de limpeza
- custo da obra de Aracruz
- material de segurança
- Vigilância
- água potável
- gl
- material de escritório
- Banheiro Quimico
- mes
- BOSS soluções ambientais - ZAP 14 99183-4303 (locação + 3 limpezas semanais) ou (14) 3222-7761
- Gerador de energia para canteiro
- Preço cotado por Fabio em Curitiba - Gerador de 13KVA = R$ 1.300,00/mês
- Mão de obra (LIMPEZA CANTEIRO)
- dia
- TOTAL
- Prazo de Operação
- preço unitário
- BDI (%)
- Preço Final
- Casma Loc. Geradores (14) 3436-2298 Fabrício por telefone 50KVA = R$ 3500,00/mês

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `=L5` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `L4` | `=I4+J4+K4` |
| `B5` | `=G6` |
| `C5` | `=L6` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `K5` | `=(I5+J5)*0.25` |
| `L5` | `=I5+J5+K5` |
| `C6` | `=L8` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `K6` | `=(I6+J6)*0.25` |
| `C7` | `=L9` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=SUM(A4:A7)` |
| `F8` | `=A8*C8` |
| `K8` | `=(I8+J8)*0.25` |
| `L8` | `=I8+J8+K8` |
| `A9` | `=A8` |
| `F9` | `=A9*C9` |
| `L9` | `=I9+J9+K9` |
| `F10` | `=SUM(F4:F9)` |
| `L10` | `=I10+J10+K10` |
| `D14` | `=Produção!G29` |
| `F14` | `=D14*E14` |
| `D16` | `=D14` |
| `D17` | `=D14` |
| `E17` | `=J17/L17` |
| `D18` | `=D14` |
| `D19` | `=D18` |
| `D21` | `=12*D14` |
| `F21` | `=D21*E21` |
| `D22` | `=D14` |
| `D23` | `=D14` |
| `D24` | `=D23` |
| `D25` | `=D24` |
| `E25` | `=F10` |
| `F26` | `=SUM(F14:F25)` |
| `F27` | `=Produção!G29` |
| `F28` | `=F26/F27` |
| `F29` | `=F28*(E29/100)` |
| `F30` | `=F28+F29` |

### 6. 2.1 Mob. Draga

- Faixa usada: `A1:G41`
- Fórmulas: **42**
- Conceitos provisórios: mobilizacao_draga
- Células numéricas observadas: **88**

#### Rótulos e textos observados

- 1 - Mobilização da Draga 10"
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
- Frete para Containers
- vb
- Munck para frete container - Étore 14 99715-4769 cotação pelo zap
- PPRA + PCMSO + LTCAT
- ART Principal + ARTS co-resp.
- Custo dos exames médicos
- un
- itens de segurança
- viagem da equipe
- Veículo para transporte pessoal
- mês
- Guindaste para carregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Hospedagem da Equipe durante mobilização
- Mobiliário Canteiro
- mobiliário do alojamento
- Carreta Carga Seca para DRAGA
- Fabiano 25/11/25 - R$ 6300+ 02,%
- Guindaste p/descarregamento e montagem DRAGA
- cliente
- Mob / desmob Guindaste
- Plano de Rigger
- Mão de obra p/carga e montagem (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- DIAS
- Carreta 1 (draga)
- Exames médicos
- Carreta 2 (Tubulação 700 m)
- viagem
- Carreta 3 (flutuantes e outros periféricos)
- integração
- montagem dos equipamentos

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Canteiro'!C4` |
| `E4` | `='1. Canteiro'!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `='1. Canteiro'!C5` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C6` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='1. Canteiro'!C7` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A4+A7+A5+A6` |
| `C8` | `='1. Canteiro'!C8` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `C9` | `='1. Canteiro'!C9` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F4:F9)` |
| `F13` | `=D13*E13` |
| `F14` | `=D14*E14` |
| `D16` | `=A8` |
| `D18` | `=A8` |
| `F19` | `=D19*E19` |
| `F20` | `=D20*E20` |
| `E21` | `=F10` |
| `F21` | `=D21*E21` |
| `E24` | `=E23` |
| `D25` | `=C40` |
| `F26` | `=D26*E26` |
| `F27` | `=D27*E27` |
| `F28` | `=D28*E28` |
| `D29` | `=G41` |
| `E29` | `=F10` |
| `F30` | `=SUM(F13:F29)` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=SUM(F30:F31)` |
| `F34` | `=SUM(F32:F33)` |
| `C40` | `=SUM(C37:C39)` |
| `G41` | `=SUM(G37:G40)` |

### 7. 2.2. Mob. Eq. Polimero

- Faixa usada: `A1:M26`
- Fórmulas: **35**
- Conceitos provisórios: mobilizacao_sistema
- Células numéricas observadas: **75**

#### Rótulos e textos observados

- 2 - MOBILIZAÇÃO E MONTAGEM DE EQUIP. POLÍMERO
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Operador Líder
- R$ / ton
- dens.
- R$ / m³
- Operador de Draga
- Brita
- Operador de preparo de polímero
- Frete
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
- Verba para Cobertura do equipamento
- vb
- #NAME?
- Loc up - Tenda de 8 x 8 p/Aracruz c/fech. laterais
- deprec.
- meses
- Munck para montagem cobertura
- cliente
- Brita 1 para lastro no piso
- m³
- Pedreira Diabasio - (14) 99885-3716 Cristiane (Brita 2 = R$ 42,00/ton + R$ 20,0/ton de frete) Fatura 30 ou até 45 dias
- Concreto para piso
- Frete para mobilização do equipamento
- Fabiano 25/11/25 - R$ 6300+ 02,%
- Instalações hidráulicas
- Instalações elétricas
- Máquina Wap
- Barrilete
- Mão de obra de apoio na montagem
- dia
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='2.1 Mob. Draga'!C4` |
| `E4` | `='1. Canteiro'!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `='1. Canteiro'!C5` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C6` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='1. Canteiro'!C7` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `J7` | `=SUM(J5:J6)` |
| `L7` | `=J7*K7` |
| `A8` | `=A4+A7+A5+A6` |
| `C8` | `='1. Canteiro'!C8` |
| `F8` | `=A8*C8` |
| `A9` | `=A8` |
| `C9` | `='1. Canteiro'!C9` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F4:F9)` |
| `D13` | `=Produção!G29` |
| `E13` | `=J13/L13` |
| `F13` | `=D13*E13` |
| `E15` | `=L7` |
| `F15` | `=D15*E15` |
| `E17` | `='2.1 Mob. Draga'!E25` |
| `G17` | `='2.1 Mob. Draga'!G25` |
| `E21` | `='2.2.1 Barrilete'!F32` |
| `E22` | `=F10` |
| `F24` | `=SUM(F13:F22)` |
| `F25` | `=F24*(E25/100)` |
| `F26` | `=SUM(F24:F25)` |

### 8. 2.2.1 Barrilete

- Faixa usada: `A1:F32`
- Fórmulas: **36**
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
| `C5` | `='1. Canteiro'!C4` |
| `D5` | `='Dados Obra '!B26` |
| `E5` | `='1. Canteiro'!E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C6` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='1. Canteiro'!C7` |
| `D7` | `='Dados Obra '!B26` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `A8` | `=A5+A7` |
| `C8` | `='1. Canteiro'!C8` |
| `F8` | `=A8*C8` |
| `A9` | `=A5+A7` |
| `C9` | `='1. Canteiro'!C9` |
| `F9` | `=A9*C9` |
| `F10` | `=SUM(F5:F9)` |
| `E15` | `=400*1.4` |
| `F15` | `=D15*E15` |
| `E16` | `=165*1.4` |
| `E17` | `=165*1.4` |
| `E18` | `=220*1.4` |
| `E19` | `=55*1.4` |
| `E20` | `=35*1.4` |
| `E21` | `=2000*1.4` |
| `E22` | `=1100*1.4` |
| `E24` | `=14*1.4` |
| `E25` | `=35*1.4` |
| `E26` | `=60*1.4` |
| `E28` | `=F10` |
| `F29` | `=SUM(F15:F28)` |
| `F30` | `=F29*0.3` |
| `F31` | `=F30*(E31/100)` |
| `F32` | `=F30+F31` |

### 9. 3. Paliçada

- Faixa usada: `A1:M28`
- Fórmulas: **39**
- Conceitos provisórios: estrutura_desaguamento
- Células numéricas observadas: **68**

#### Rótulos e textos observados

- 3. DIQUE DE PALIÇADA
- EXEMPLO DE PRODUÇÃO EXECUTADO EM CAMPO
- Nº Func.
- Mão de obra montagem canteiro
- R$/h
- Hrs/dia
- L.Sociais (%)
- Total
- Quant (m²)
- Dias
- horas
- Operador Líder
- Operador de Draga
- W
- Y
- Ajudante Geral
- Refeições
- Y =
- m²/h
- Transporte
- W =
- m²/dia
- Custo por dia
- Custo por m²
- Item
- Descrição dos serviços
- Unid.
- Quantidade
- Preço Unit.
- Preço Total
- Preços cotados em 27/11/25 empresa Madeireira Eucapinus em Lençóis Paulista (R$ / m) (14) 99753-3638
- QUANTIFICAÇÃO
- Eucalipto 3" (5 x 11 = R$ 12,60)
- m
- Comprimento
- #NAME?
- Sarrafo 15 cm
- altura
- Prazo
- Tábua de 30 cm
- m²
- HUESKER - MANTA
- plástico preto
- Nº de Vezes para encher e esvaziar a bacia
- vezes
- prego
- kg
- Nº vezes refazer PALIÇADA COMPLETA
- Mão de obra de montagem
- Vão de aberturar para entrada caminhão
- TOTAL
- Nº vezes do Vão de entrada
- Quantidade total a ser construído
- Preço Final
- QUANTIFICAÇÃO TOTAL
- MANTA HUESKER é vendido em rolos de 5,0 x 200m. Portanto, cada rolo dá para fazermos 3 faixas de 1,67m de largura
- Dimensão real da Paliçada
- Perímetro
- nº bacias
- Para um perímetro de 960 metros, divido em 3 faixas, teremos 320 metros de manta com 5,0m de largura, o que daria um total de 320 x 5 = 1.600m²

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Canteiro'!C4` |
| `D4` | `='Dados Obra '!B26` |
| `E4` | `='1. Canteiro'!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `K4` | `=I4*9` |
| `C5` | `='1. Canteiro'!C5` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C7` |
| `D6` | `='Dados Obra '!B26` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A4+A6+A5` |
| `C7` | `='2.1 Mob. Draga'!C8` |
| `F7` | `=A7*C7` |
| `I7` | `=H4/K4` |
| `A8` | `=A7` |
| `C8` | `='2.1 Mob. Draga'!C9` |
| `F8` | `=A8*C8` |
| `I8` | `=H4/I4` |
| `F9` | `=SUM(F4:F8)` |
| `F10` | `=F9/I8` |
| `F13` | `=D13*E13` |
| `I13` | `=Produção!H37` |
| `I15` | `=I13*I14` |
| `K15` | `=I15/I8` |
| `F19` | `=D19*E19` |
| `E20` | `=F10` |
| `F20` | `=D20*E20` |
| `L20` | `=6*1.5` |
| `F21` | `=SUM(F13:F20)` |
| `L21` | `=L17` |
| `F22` | `=ROUNDUP(L23,0)` |
| `F23` | `=F22*F21` |
| `L23` | `=((I15*L19)+(L20*L21))` |
| `H27` | `=Produção!H33` |
| `J27` | `=4` |
| `K27` | `=H27*I27*J27` |

### 10. 3.1 Impermeabilização

- Faixa usada: `A1:L22`
- Fórmulas: **44**
- Conceitos provisórios: outros
- Células numéricas observadas: **63**

#### Rótulos e textos observados

- 3. DIQUE DE PALIÇADA
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
- Largura
- Comprimento
- Numero de bacias
- Area total
- Regularizaçao terreno - trator ou escavad.
- dia
- PEAD interno
- m²
- última cotação R$ 15,90/m²
- BACIA 1
- #NAME?
- PEAD Externo / canaleta
- BACIA 2
- Mao de Obra Instalaçao PEAD
- BACIA 3
- Taxa de Mobilizaçao PEAD
- vb
- Mão de obra de montagem
- TOTAL
- Perimetro
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C4` | `='1. Canteiro'!C4` |
| `D4` | `='Dados Obra '!B26` |
| `E4` | `='1. Canteiro'!E4` |
| `F4` | `=(A4*C4*D4)+(A4*C4*D4)*(E4/100)` |
| `C5` | `='1. Canteiro'!C5` |
| `D5` | `=D4` |
| `E5` | `=E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='1. Canteiro'!C7` |
| `D6` | `='Dados Obra '!B26` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `A7` | `=A4+A6+A5` |
| `C7` | `='2.1 Mob. Draga'!C8` |
| `F7` | `=A7*C7` |
| `A8` | `=A7` |
| `C8` | `='2.1 Mob. Draga'!C9` |
| `F8` | `=A8*C8` |
| `F9` | `=SUM(F4:F8)` |
| `F12` | `=D12*E12` |
| `D13` | `=L16*1.1` |
| `E13` | `=15.9*1.2` |
| `F13` | `=D13*E13` |
| `I13` | `=Produção!E33+(0.3+0.3)` |
| `J13` | `=Produção!F33+(0.3+0.3)` |
| `L13` | `=I13*J13*K13` |
| `D14` | `=K22*1.1` |
| `E14` | `=E13` |
| `F14` | `=D14*E14` |
| `I14` | `=I13` |
| `L14` | `=I14*J14*K14` |
| `D15` | `=D13+D14` |
| `L16` | `=SUM(L13:L15)` |
| `E17` | `=F9` |
| `F17` | `=D17*E17` |
| `F18` | `=SUM(F12:F17)` |
| `F19` | `=F18` |
| `I19` | `=Produção!H33` |
| `K19` | `=I19*J19` |
| `I20` | `=Produção!H34` |
| `K20` | `=I20*J20` |
| `I21` | `=Produção!H35` |
| `K21` | `=I21*J21` |
| `K22` | `=SUM(K19:K21)` |

### 11. 4.1 Dragagem

- Faixa usada: `A1:Q253`
- Fórmulas: **95**
- Conceitos provisórios: dragagem_operacao
- Células numéricas observadas: **0**

#### Rótulos e textos observados

- 5.

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C9` | `=Produção!H6` |
| `F10` | `=C9*D9*E9*F9` |
| `F11` | `=(C9*D9*E9*J9)*0.1` |
| `E15` | `=F10+F11+F12+F13` |
| `A20` | `=L24` |
| `E20` | `=D20*B20*A20` |
| `K20` | `='Dados Obra '!B27` |
| `L20` | `=J20*K20` |
| `A21` | `=L24` |
| `D21` | `='1. Canteiro'!C4` |
| `L21` | `=J21*K21` |
| `A22` | `=L24` |
| `D22` | `='1. Canteiro'!C5` |
| `A23` | `=L24` |
| `D23` | `='1. Canteiro'!C7` |
| `L23` | `=J23*K23` |
| `Q23` | `=O23*P23` |
| `A24` | `=L24` |
| `L24` | `=(L20*1.7)+(L21*2)+L23` |
| `Q24` | `=P24*O24` |
| `A25` | `=L24` |
| `A26` | `=L24` |
| `Q26` | `=(Q23+Q24)*Q25` |
| `A27` | `=L24` |
| `D27` | `=D23` |
| `E27` | `=D27*B27*A27` |
| `Q28` | `=Q27+Q26` |
| `E31` | `=E20+E21+E22+E23+E24+E25+E26+E27+E28` |
| `A37` | `='1. Canteiro'!E4` |
| `C37` | `=E31` |
| `E37` | `=(C37*A37)/100` |
| `E46` | `=G52+G53` |
| `B52` | `=B21+B22` |
| `G52` | `=B52*(C52+D52+E52)*F52` |
| `B53` | `=B23+B27` |
| `F53` | `='Dados Obra '!B27` |
| `G53` | `=B53*(C53+D53+E53)*F53` |
| `E62` | `=C59+C60+C61+C62` |
| `E69` | `=D69*B69` |
| `E71` | `=SUM(E67:E69)` |
| `G87` | `=E71+E62+E46+E37+E31` |
| `E139` | `=(0.6/100)*F7` |
| `E140` | `=(1/100)*F7` |
| `E144` | `=E139+E140+E141+E142` |
| `H146` | `=E144` |
| `E150` | `=K167` |
| `I151` | `='Dados Obra '!B16` |
| `K151` | `=I151*J151` |
| `J152` | `=K151/I152` |
| `J153` | `=K151*(1/100)` |
| `E154` | `=D154*B154` |
| `J154` | `=SUM(J152:J153)` |
| `I156` | `=('Dados Obra '!B17/12)*3` |
| `K156` | `=I156*J156` |
| `J157` | `=K156/I157` |
| `J158` | `=K156*(1/100)` |
| `B159` | `='1. Canteiro'!A8` |
| `E159` | `=B159*D159` |
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
| `D231` | `=D227+D229` |
| `D234` | `=J253*0.6*0.62` |
| `J235` | `=H235*I235` |
| `D244` | `=D222` |
| `D246` | `=SUM(D244:D245)` |
| `D247` | `=ROUNDUP(Produção!D25,0)` |
| `J247` | `=D246` |
| `D248` | `=D246*D247` |
| `J249` | `=J247*J248` |
| `L249` | `=J249/J250` |
| `L251` | `=L249*L250` |
| `J252` | `=J250*J251` |
| `J253` | `=J249/J252` |

### 12. Op. Polimero

- Faixa usada: `A1:M37`
- Fórmulas: **38**
- Conceitos provisórios: outros
- Células numéricas observadas: **76**

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
- Custo por dia
- Tanques de 5 m³ + bombas de 10m³/h
- Tanques de 10 m³ + bombas de 20m³/h
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
- cliente
- Frete Polimero
- un
- (Caminhao Pipa) fornecimento de água para operação
- mes
- Consulta por telefone na Hidrogeo em Bauru (não atendem Bracell, mas o custo é de R$ 1000/caminhão de 20m³)
- Locação do Caminhão Pipa com motorista
- consulta por ZAP (Luís 19 97414-1992) aluguel de caminhão pipa - empresa Loguim Locações
- (Gerador) fornecimento de energia para operação ( diesel por conta CLIENTE)
- Casmaq Geradores (14) 3436-2298 Fabrício 50 KVA R$ 3.500,00/mês
- Instalações hidráulicas
- vb
- Caminhão Pipa
- m³
- Instalações Eletrica
- dias
- Máquina Wap
- caminhões por mês
- Mão de obra para operação do sistema
- dia
- TOTAL
- Horas/ mês
- Prazo de Operação
- h/dia
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
| `H6` | `=220/D9` |
| `C9` | `='1. Canteiro'!C6` |
| `D9` | `=D10` |
| `E9` | `=E10` |
| `F9` | `=(A9*C9*D9)+(A9*C9*D9)*(E9/100)` |
| `C10` | `='1. Canteiro'!L9` |
| `D10` | `='Dados Obra '!B26` |
| `E10` | `='1. Canteiro'!E4` |
| `A12` | `=SUM(A5:A11)` |
| `C12` | `='1. Canteiro'!C8` |
| `F12` | `=A12*C12` |
| `A13` | `=A12` |
| `C13` | `='1. Canteiro'!C9` |
| `F13` | `=A13*C13` |
| `F14` | `=SUM(F5:F13)` |
| `L15` | `=257000*1.3` |
| `D18` | `=ROUNDUP(Produção!D25,0)` |
| `E18` | `=M12/J18` |
| `F18` | `=D18*E18` |
| `D19` | `=D18` |
| `E19` | `=E18*0.1` |
| `D20` | `=D37` |
| `D22` | `=Produção!G27` |
| `E22` | `=I27*0` |
| `D23` | `=D22` |
| `F23` | `=D23*E23` |
| `D24` | `=D22` |
| `E24` | `=3500` |
| `I27` | `=I26` |
| `D28` | `='Dados Obra '!B27*Produção!G27` |
| `E28` | `=F14` |
| `F29` | `=SUM(F18:F28)` |
| `F31` | `=F29/F30` |
| `I31` | `=I29/I30` |
| `F32` | `=F31*(E32/100)` |
| `F33` | `=F31+F32` |
| `D35` | `='Dados Obra '!Q17` |
| `D37` | `=D35*D36` |

### 13. 4.4. Medição

- Faixa usada: `A1:K28`
- Fórmulas: **37**
- Conceitos provisórios: medicao_batimetria
- Células numéricas observadas: **54**

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
- m2
- JASAO GERDAU 2,18
- COLETA BACIA
- un
- Amostras por Bacia
- dias
- nº de bacias
- Acompanhamento FOS
- dia
- prazo
- #NAME?
- TOTAL
- BDI (%)
- Preço Final

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='3. Paliçada'!C4` |
| `E5` | `='3. Paliçada'!E4` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='3. Paliçada'!C5` |
| `D6` | `=D5` |
| `E6` | `=E5` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='Op. Polimero'!C9` |
| `D7` | `=D6` |
| `E7` | `=E6` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='3. Paliçada'!C6` |
| `E8` | `=E7` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=SUM(A5:A8)` |
| `C9` | `='3. Paliçada'!C7` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `C10` | `='3. Paliçada'!C8` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F16` | `=D16*E16` |
| `E17` | `=E16` |
| `F17` | `=D17*E17` |
| `E18` | `=E16` |
| `E19` | `=E16` |
| `D20` | `=K23` |
| `F20` | `=D20*E20` |
| `D22` | `=K22` |
| `E22` | `=F11` |
| `K22` | `=Produção!G27` |
| `F23` | `=SUM(F16:F22)` |
| `K23` | `=K20*K21*K22` |
| `F24` | `=F23*(E24/100)` |
| `F25` | `=SUM(F23:F24)` |
| `F27` | `=F26*(E27/100)` |
| `F28` | `=SUM(F26:F27)` |

### 14. 6.1 Desmob. Draga

- Faixa usada: `A1:G35`
- Fórmulas: **42**
- Conceitos provisórios: mobilizacao_draga, desmobilizacao
- Células numéricas observadas: **67**

#### Rótulos e textos observados

- 7 - DESMOBILIZAÇÃO E DESMONTAGEM DRAGA
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
- Guindaste para descarregamento
- dia
- Treinamentos (Trabalho em Altura e espaço confinado)
- Frete dos containeres
- vb
- Carreta Carga Seca para DRAGA
- un
- Carreta Carga Seca para Eq. Pol
- Guindaste p/descarregamento e montagem DRAGA
- cliente
- Escavadeira para desmonte das paliçadas
- Caminhões para destinação mantas e madeira
- Destinação de material contaminado
- Mão de obra p/DEScarga e DESmontagem (r$/dia)
- TOTAL
- BDI (%)
- Preço Final
- DIAS
- Exames médicos
- viagem
- integração
- desmontagem dos equipamentos

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `C5` | `='2.1 Mob. Draga'!C4` |
| `E5` | `='4.4. Medição'!E5` |
| `F5` | `=(A5*C5*D5)+(A5*C5*D5)*(E5/100)` |
| `C6` | `='2.1 Mob. Draga'!C5` |
| `D6` | `=D5` |
| `E6` | `='4.4. Medição'!E6` |
| `F6` | `=(A6*C6*D6)+(A6*C6*D6)*(E6/100)` |
| `C7` | `='2.1 Mob. Draga'!C6` |
| `D7` | `=D6` |
| `E7` | `='4.4. Medição'!E7` |
| `F7` | `=(A7*C7*D7)+(A7*C7*D7)*(E7/100)` |
| `C8` | `='4.4. Medição'!C8` |
| `E8` | `='4.4. Medição'!E8` |
| `F8` | `=(A8*C8*D8)+(A8*C8*D8)*(E8/100)` |
| `A9` | `=A5+A8+A6+A7` |
| `C9` | `='4.4. Medição'!C9` |
| `F9` | `=A9*C9` |
| `A10` | `=A9` |
| `C10` | `='4.4. Medição'!C10` |
| `F10` | `=A10*C10` |
| `F11` | `=SUM(F5:F10)` |
| `F14` | `=D14*E14` |
| `F15` | `=D15*E15` |
| `D16` | `='2.1 Mob. Draga'!D13` |
| `E16` | `='2.1 Mob. Draga'!E13` |
| `D17` | `='2.1 Mob. Draga'!D25` |
| `E17` | `='2.1 Mob. Draga'!E25` |
| `D18` | `='2.2. Mob. Eq. Polimero'!D17` |
| `E18` | `=E17` |
| `D19` | `='2.1 Mob. Draga'!D26` |
| `E19` | `='2.1 Mob. Draga'!E26` |
| `F19` | `=D19*E19` |
| `E20` | `='3.1 Impermeabilização'!E12` |
| `F20` | `=D20*E20` |
| `F22` | `=D22*E22` |
| `D23` | `=F35` |
| `E23` | `=F11` |
| `F24` | `=SUM(F14:F23)` |
| `F25` | `=F24*(E25/100)` |
| `F26` | `=SUM(F24:F25)` |
| `F28` | `=SUM(F26:F27)` |
| `F35` | `=SUM(F31:F34)` |

### 15. Plan. Preços

- Faixa usada: `A1:N17`
- Fórmulas: **50**
- Conceitos provisórios: formacao_preco
- Células numéricas observadas: **69**

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
- Canteiro de Obras
- #NAME?
- mês
- Mobilizaçao Draga
- vb
- Mobilizaçao Equipto Polímero e Barrilete
- Paliçada
- m²
- Impermeabilizaçao
- M³ em Bacia
- Dragagem
- m³
- OP Polimero
- Medição
- Desmobilização Draga
- un
- Desmobilização do Equipamento Polímero
- Preço de Venda
- Resultado Final previsto
- Resultado mensal previsto

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D4` | `='1. Canteiro'!F26` |
| `F4` | `=Produção!G29` |
| `H4` | `=D4/F4` |
| `J4` | `=((I4/100)+1)*H4` |
| `K4` | `=F4*J4` |
| `L4` | `=J4` |
| `D5` | `='2.1 Mob. Draga'!F30` |
| `H5` | `=D5/F5` |
| `J5` | `=((I5/100)+1)*H5` |
| `K5` | `=F5*J5` |
| `L5` | `=J5+J6` |
| `D6` | `='2.2. Mob. Eq. Polimero'!F24` |
| `H6` | `=D6/F6` |
| `J6` | `=((I6/100)+1)*H6` |
| `K6` | `=F6*J6` |
| `D7` | `='3. Paliçada'!F23` |
| `F7` | `=Produção!G37` |
| `H7` | `=D7/F7` |
| `J7` | `=((I7/100)+1)*H7` |
| `K7` | `=F7*J7` |
| `L7` | `=(K7+K8)/F7` |
| `D8` | `='3.1 Impermeabilização'!F19` |
| `F8` | `='3.1 Impermeabilização'!L16+'3.1 Impermeabilização'!K22` |
| `D9` | `='4.1 Dragagem'!D248` |
| `F9` | `='Dados Obra '!M17` |
| `H9` | `=D9/F9` |
| `J9` | `=((I9/100)+1)*H9` |
| `K9` | `=F9*J9` |
| `L9` | `=J9+J10+J11` |
| `N9` | `=(K7+K8+K9+K10+K11)/F9` |
| `D10` | `='Op. Polimero'!F29` |
| `F10` | `=F9` |
| `H10` | `=D10/F10` |
| `J10` | `=((I10/100)+1)*H10` |
| `K10` | `=F10*J10` |
| `D11` | `='4.4. Medição'!F25` |
| `F11` | `=F9` |
| `H11` | `=D11/F11` |
| `J11` | `=((I11/100)+1)*H11` |
| `K11` | `=F11*J11` |
| `D12` | `='6.1 Desmob. Draga'!F24` |
| `H12` | `=D12/F12` |
| `J12` | `=((I12/100)+1)*H12` |
| `K12` | `=F12*J12` |
| `L12` | `=J12+J13` |
| `D14` | `=SUM(D4:D13)` |
| `K14` | `=SUM(K4:K13)` |
| `D16` | `=K14-D14` |
| `K16` | `=K14/F9` |
| `D17` | `=D16/F4` |

### 16. Plan Final

- Faixa usada: `A1:H7`
- Fórmulas: **20**
- Conceitos provisórios: outros
- Células numéricas observadas: **26**

#### Rótulos e textos observados

- ITEM
- DESCRIÇÃO DOS SERVIÇOS
- UNID
- QUANT
- PREÇO UNITÁRIO
- PREÇO TOTAL
- Pr. Unit.
- Montagem e manutenção do Canteiro de obras
- vb/mês
- Mobilização e Montagem dos Equipamentos de Dragagem e Preparo e injeção de Polímero
- vb
- Preparo das Bacias ecológicas para desidratação do lodo dragado, incluindo impermeabilização de base
- m²
- Dragagem de lodo das lagoas, incluindo preparo e injeção de polímero e controle do processo de desaguamento das bacias ecológicas
- m³
- Desmobilização dos equipamentos
- TOTAL GERAL

#### Fórmulas observadas

| Célula | Fórmula |
|---|---|
| `D2` | `=' Plan. Preços'!F4` |
| `E2` | `=H2` |
| `F2` | `=D2*E2` |
| `H2` | `=' Plan. Preços'!L4` |
| `D3` | `=' Plan. Preços'!F5` |
| `E3` | `=H3` |
| `F3` | `=D3*E3` |
| `H3` | `=' Plan. Preços'!L5` |
| `D4` | `=' Plan. Preços'!F7` |
| `E4` | `=H4` |
| `F4` | `=D4*E4` |
| `H4` | `=' Plan. Preços'!L7` |
| `D5` | `=' Plan. Preços'!F9` |
| `E5` | `=H5` |
| `F5` | `=D5*E5` |
| `H5` | `=' Plan. Preços'!L9` |
| `E6` | `=H6` |
| `F6` | `=D6*E6` |
| `H6` | `=' Plan. Preços'!L12` |
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
