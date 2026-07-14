# Registro de Descoberta — `Composição - Draga 14 - com equipe.xlsx`

## 1. Identificação da análise

- **Arquivo-fonte:** `Composição - Draga 14 - com equipe.xlsx`
- **Data da análise:** 2026-07-14
- **Versão declarada no arquivo:** não identificada.
- **Proposta indicada internamente:** `Proposta D_020_2025`.
- **Cliente indicado internamente:** `SBV`.
- **Quantidade de abas:** 8.
- **Abas analisadas:** `Dados Obra`, `Produção`, `MDO x Turno`, `Canteiro`, `1. Mobilização`, `2. Dragagem`, `3. Desmobilização`, `Final`.
- **Status:** análise vertical concluída para este arquivo.
- **Escopo:** somente este Excel. Os arquivos `Composição preços - Draga 14 SBV - sem equipe.xlsx` e `Composição preços - Draga 14 SBV.xlsx`, recebidos na mesma sessão, não foram analisados nem comparados.
- **Documento exclusivo:** este registro pertence exclusivamente ao arquivo acima.

## 2. Limitações da análise

### EVIDÊNCIA CONFIRMADA

O arquivo foi lido integralmente com ferramenta de inspeção de planilhas, incluindo valores armazenados, fórmulas e relações entre abas.

### DÚVIDA

A ferramenta de leitura apresentou valores `#NAME?` em algumas células calculadas. Em vários casos a fórmula possui referência a outra aba com nome acentuado ou com espaço final aparente, enquanto outras células do mesmo arquivo preservam valores calculados anteriores. Não foi possível provar, somente pela inspeção, se todos os erros também aparecem no Microsoft Excel original ou se parte deles decorre do motor de cálculo utilizado na análise.

### EVIDÊNCIA CONFIRMADA

Nenhuma fórmula foi alterada, recalculada manualmente ou corrigida. Nenhuma comparação com os outros dois arquivos recebidos foi realizada.

---

## 3. Classificação aparente

### EVIDÊNCIA CONFIRMADA

O arquivo representa um orçamento de:

- locação e execução com draga de 14 polegadas;
- dragagem de areia fina;
- volume indicado de 93.000 m³;
- local indicado como Parnaíba — PI;
- linha de recalque total indicada de 600 m;
- operação com equipe própria incluída;
- medição comercial indicada como “preço mensal”;
- composição separada em mobilização, dragagem/operação e desmobilização;
- fechamento comercial por preço unitário de dragagem e valores globais de mobilização/desmobilização.

### EVIDÊNCIA PARCIAL

A descrição da aba `2. Dragagem` menciona “Operação do Sistema de Desidratação de lodo”, mas os dados gerais descrevem areia fina e não apresentam, nas demais abas, um dimensionamento completo de bags, adensamento ou tratamento de lodo. A expressão pode ser resíduo de outro modelo ou indicar escopo operacional não detalhado.

### Classificação

**Orçamento de dragagem hidráulica com draga de 14", linha de recalque, equipe operacional, mobilização, operação mensal e desmobilização.**

Esta classificação vale somente para este arquivo.

---

## 4. Visão geral do fluxo

### EVIDÊNCIA CONFIRMADA

O fluxo lógico observado é:

1. `Dados Obra` registra identificação, escopo, volume, material, distâncias, jornada e dias de trabalho.
2. `Produção` usa vazão, eficiência, concentração, horas/dia e dias/mês para calcular produção horária, produção mensal e prazo.
3. `MDO x Turno` define quantitativos de pessoas e veículos por regime administrativo/turno.
4. `Canteiro` transforma salários e quantitativos em custo diário da equipe e calcula itens de canteiro.
5. `1. Mobilização` reutiliza a composição de mão de obra, agrega custos de equipe, segurança, documentos, transporte, guindastes e mobilização física.
6. `2. Dragagem` compõe custo mensal de operação, pessoal, manutenção, apoio, administração, BDI interno e despesas financeiras; depois calcula custo mensal, preço de venda e custo total para o prazo.
7. `3. Desmobilização` espelha parcialmente a mobilização, com viagens de retorno, desmontagem e transporte.
8. `Final` consolida mobilização, dragagem e desmobilização e aplica BDI comercial por item.

### EVIDÊNCIA PARCIAL

A planilha mistura três perspectivas econômicas diferentes:

- custo interno;
- acréscimos denominados BDI dentro da aba operacional;
- BDI comercial aplicado novamente na aba final.

Não há texto explicando formalmente a diferença entre esses acréscimos.

---

# 5. Análise por aba

## 5.1. Aba `Dados Obra`

### Objetivo

### EVIDÊNCIA CONFIRMADA

Centralizar os dados básicos da proposta e as premissas físicas e de calendário.

### Conteúdo observado

- Proposta: `Proposta D_020_2025`.
- Data armazenada: serial Excel `45393`, correspondente a 2024-04-11.
- Cliente: `SBV`.
- Contato: `Cadu`.
- Objeto: `Locaçao Draga 14" com execuçao`.
- Local: `Parnaíba - PI`.
- Volume: `93.000 m³`.
- Material: `Areia Fina`.
- Distância de recalque: `600 m`.
- Linha flutuante: `500 m`.
- Linha de terra: `100 m`.
- Sistema de medição: `preço mensal`.
- Jornada: `12 h/dia`.
- Dias de trabalho: `22 dias/mês`.

### Fórmulas e finalidade operacional

- `B16 = SUM(B17:B18)`: soma linha flutuante e linha de terra para obter distância de recalque.
- `H16 = B16 + E16`: permite adicionar “seio da linha” à distância total.
- `H17 = B17 + E17`: permite adicionar “seio da linha” à linha flutuante.
- `G21 = B21 * D21 * B20`: tentativa de calcular volume por área/comprimento/espessura.

### Entidades conceituais

- proposta;
- cliente;
- contato;
- obra;
- volume;
- material;
- linha de recalque;
- linha flutuante;
- linha terrestre;
- profundidade;
- espessura;
- área;
- bota-fora;
- sistema de medição;
- calendário de trabalho.

### Regras e padrões

### EVIDÊNCIA CONFIRMADA

A cor é usada como linguagem de preenchimento:

- azul: dados a preencher;
- vermelho: informações pendentes;
- preto: resultados automáticos.

### Anomalias e dúvidas

- A data da proposta é 2024-04-11, enquanto o código da proposta contém 2025.
- Profundidade, espessura, área, tipo de bota-fora, canteiro e mobilização estão vazios.
- A fórmula de volume retorna zero porque as entradas estão vazias.
- As fórmulas em outras abas referenciam o nome `'Dados Obra '` com espaço final aparente, enquanto a aba é exibida como `Dados Obra`.

---

## 5.2. Aba `Produção`

### Objetivo

Calcular produção da draga e prazo de execução.

### Entradas principais

- vazão: 850 m³/h;
- eficiência: 75%;
- concentração: 15%;
- horas/dia: 12;
- dias/mês: 22.

### Saídas principais

- produção: 95,625 m³/h;
- horas trabalhadas: 264 h/mês;
- produção mensal: 25.245 m³/mês;
- prazo matemático: 3,6839 meses;
- prazo arredondado: 4 meses.

### Fórmulas e finalidade operacional

- `D8 = D3 * (D4/100) * (D5/100)`: produção de sólidos/volume útil por hora.
- `H6 = H3 * H4`: horas mensais de calendário.
- `D11 = H6`: horas usadas no cálculo mensal.
- `D13 = D8 * D11`: produção mensal.
- `D24 = D21 / D18`: prazo em meses.
- `E24 = ROUNDUP(D24,0)`: prazo inteiro sempre arredondado para cima.

### Paralisações

A aba lista:

- DDS: 15 min;
- deslocamento de ida: 15 min;
- almoço: 1 h;
- deslocamento de almoço: 30 min;
- deslocamento de volta: 15 min;
- manobras e abastecimento: 1,5 h.

As paralisações somam 2,25 h/dia, e manobras/abastecimento mais 1,5 h/dia.

### EVIDÊNCIA CONFIRMADA

As paralisações são calculadas em células laterais, mas a produção mensal principal usa diretamente 12 h/dia × 22 dias, sem descontar essas paralisações.

### EVIDÊNCIA PARCIAL

Há uma célula intitulada “EFICIÊNCIA” com valor 31,25%, resultante da soma proporcional de paralisações. Esse valor não alimenta a eficiência de 75% usada no cálculo de produção.

### Turnos

A aba registra:

- Turno 1: 6 às 12 h;
- Turno 2: 12 às 18 h;
- alternativa de jornada 12 × 36;
- observação: “MONTAR BARRILETE PARA ENCHER AS CHICANES”.

### Anomalias e dúvidas

- Os textos “6 às 18h” e “das 7 às 17h” aparecem em partes diferentes do arquivo.
- A linha de dias menciona “2ª a 2ª”, embora sejam usados 22 dias/mês.
- Paralisações não reduzem as horas principais.
- A concentração de 15% parece ser percentual volumétrico ou operacional, mas a unidade não é definida.
- A observação sobre barrilete/chicanes não possui cálculo associado nesta aba.

---

## 5.3. Aba `MDO x Turno`

### Objetivo

Definir o quadro de mão de obra por regime de jornada/turno.

### Estrutura

Colunas principais:

- ADM;
- TURNO A;
- uma coluna adicional sem cabeçalho operacional claro;
- observações.

### Quantitativos preenchidos

- Mecânico: 1 em ADM.
- Encarregado: 1 no Turno A.
- Operador de Draga: 1 no Turno A.
- Maquinista: 1 no Turno A.
- Barqueiro: 1 no Turno A.
- Ajudante: 3 em ADM.
- Veículo “ajudantes nosso”: 1 em ADM e 1 no Turno A.

### Observação

- “fornecido pelo cliente” aparece ao lado de ajudantes.

### EVIDÊNCIA PARCIAL

A posição da observação não permite concluir se todos os três ajudantes são fornecidos pelo cliente ou se a observação se refere apenas a uma alternativa.

### Dúvidas

- O cabeçalho menciona 44 horas semanais de segunda a sexta, mas a operação usa 12 h/dia.
- Não há Turno B preenchido, embora mobilização/desmobilização tragam colunas A e B.
- O papel do veículo na composição não é claramente separado entre veículo físico e custo de equipe.

---

## 5.4. Aba `Canteiro`

### Objetivo

Calcular custo diário da equipe e custos associados ao canteiro de obras.

### Composição da mão de obra

A aba contém salários mensais, conversão para valor/hora, dissídio de 7,5% e, para algumas funções, adicional de transferência de 25%.

Salários mensais observados:

- Engenheiro: R$ 9.500;
- Auxiliar Técnico: R$ 5.000;
- Mecânico: R$ 6.000;
- Encarregado: R$ 11.132;
- Operador de Draga: R$ 5.500;
- Maquinista: R$ 3.800;
- Barqueiro: R$ 3.800;
- Ajudante: R$ 2.310.

### Fórmulas principais

- valor-base/hora: salário ÷ 220;
- dissídio: valor/hora × 7,5%;
- transferência: (valor/hora + dissídio) × 25%, aplicada a encarregado, operador, maquinista e barqueiro;
- custo por função/dia: quantidade × R$/h × horas/dia × (1 + leis sociais);
- leis sociais: 110%;
- refeições: número de pessoas × R$ 35;
- transporte: número de pessoas × R$ 15.

### Resultado

- custo diário calculado: R$ 5.721,9536.

### Itens de canteiro

Inclui:

- containers;
- fretes;
- mobiliário;
- PGR, PCMSO e LTCAT;
- ART;
- placa de obra;
- sinalização e segurança;
- água potável;
- material de escritório;
- banheiro químico;
- exames médicos;
- mão de obra de manutenção.

Vários itens aparecem com preço total zero e observação `COEDRA`, indicando possível responsabilidade externa.

### Fórmulas e relações

- quantidades de containers e meses dependem do prazo arredondado da aba `Produção`;
- água potável: prazo × 22 galões;
- mão de obra de manutenção: 1 dia × custo diário;
- total: soma dos itens;
- “Prazo de Operação” referencia o prazo;
- preço unitário divide total pelo prazo;
- BDI está em 0%.

### Anomalias

- `D17` e `F33` aparecem como `#NAME?` na leitura.
- O item “Custo por dia” incorpora leis sociais de 110%, refeições e transporte.
- Alguns itens relevantes têm quantidade vazia, portanto total zero.
- “Itens sinalização e segurançaq” contém erro de digitação.
- O campo “Preço Final” é igual ao preço unitário porque BDI = 0%.
- A coluna lateral “% de atuação na obra” possui 20% para engenheiro e 100% para os demais, mas esse fator é aplicado às horas/dia, não diretamente ao salário mensal.

### DÚVIDA

O título informa “subitem da Dragagem”, porém a aba também funciona como base de custo de mão de obra para mobilização e desmobilização.

---

## 5.5. Aba `1. Mobilização`

### Objetivo

Compor custos de mobilização da equipe, documentos, segurança, equipamentos e transporte.

### Dependências

- valores/hora e horas/dia vêm de `Canteiro`;
- quantitativos vêm de `MDO x Turno`;
- custo diário vem da composição de mão de obra;
- extensão total da linha vem de `Dados Obra`.

### Mão de obra

A composição diária é semelhante à aba `Canteiro`, com resultado de R$ 5.721,9536/dia.

### Mobilização da equipe

Itens com valor preenchido:

- treinamentos de segurança: 8 × R$ 500 = R$ 4.000;
- exames médicos: 8 × R$ 500 = R$ 4.000;
- viagens de ida: 5 × R$ 3.000 = R$ 15.000;
- laudo de flutuabilidade: R$ 5.000;
- PGR + PCMSO + LTCAT: R$ 5.000;
- ART: R$ 500.

Itens com valor unitário, mas quantidade vazia e total zero:

- mobiliário do canteiro;
- mobiliário do alojamento;
- sinalização;
- mão de obra de integração/viagens/treinamentos.

### Mobilização de equipamentos

- guindaste para carregamento: 2 dias × R$ 6.500 = R$ 13.000;
- mão de obra de mobilização: 8 dias × R$ 5.721,9536 = R$ 45.775,6291.

Os demais itens de transporte possuem preço de referência, mas quantidade zero/vazia:

- carreta prancha;
- carreta extensível;
- seguro;
- carreta carga seca;
- guindaste de descarga/montagem;
- planos de rigging;
- veículo.

### Referências de preço

- Cruz de Malta em 14/04/25: carreta prancha R$ 24.500.
- Cruz de Malta em 14/04/26: carreta extensível R$ 14.800.
- Fabiano/WhatsApp em 14/04/25: carreta carga seca R$ 11.500 + 0,2% “adv”.
- Alguns valores são marcados como “chute”.
- Guindaste e rigging aparecem como responsabilidade do cliente.

### Totais

- custo total antes do BDI: R$ 92.275,6291;
- BDI indicado: 100%;
- preço final interno da aba: R$ 184.551,2582.

### Dimensionamento de transporte de tubos

Entradas:

- largura da carga: 2,4 m;
- altura da grade: 1,8 m;
- altura adicional: 0,4 m;
- diâmetro do tubo: 0,4 m;
- comprimento por tubo: 12 m;
- linha total: 600 m.

Resultados:

- 33 tubos por carga, aproximadamente;
- 396 m por carga;
- 3 carretas para tubos, pelo arredondamento da fórmula.

### Fórmula relevante

`G43 = ((D43 + E43) / F43) * (C43 / F43)`

A fórmula estima quantidade de tubos por arranjo geométrico em largura e altura, sem arredondamento explícito por direção. O resultado é fracionário próximo de 33.

### Anomalias e dúvidas

- O título “MOBILIZAÇÃO EQUIPE” é reutilizado na desmobilização.
- O BDI de 100% desta aba não é levado ao custo da aba `Final`, que usa o total antes desse BDI.
- A aba `Final` aplica 70% adicional sobre o custo antes do BDI.
- A data 14/04/26 é futura em relação à data indicada no corpo do orçamento e pode ser erro de digitação.
- A responsabilidade SBV é declarada ao final, sem lista formal vinculada.

---

## 5.6. Aba `2. Dragagem`

### Objetivo

Compor o custo mensal de operação da draga e calcular custo total da dragagem para o prazo previsto.

### Cabeçalho e dados gerais

- referência: dragagem;
- data: 2025-04-14;
- cliente: SBV;
- equipamento: draga 14";
- valor “no estado”: R$ 2.000.000.

### I — Operação

Entradas:

- horas/mês referenciadas da produção;
- eficiência: 90%;
- consumo: 75 por hora;
- combustível: R$ 7;
- fornecimento SBV com valor lateral 6.

Fórmulas:

- combustível: horas × eficiência × consumo × preço;
- filtros/lubrificantes: 10% de cálculo de combustível usando valor lateral de combustível;
- fretes/carretos: 10% dos filtros;
- segurança/uniformes: igual a fretes/carretos.

Resultado armazenado da seção: R$ 137.570,40.

### Anomalia

A fórmula do combustível usa `F9` como preço, mas o valor R$ 7 está em `F8` na estrutura lida e a célula lateral `J9` contém 6. A estrutura visual/formulação exige validação no Excel original. O resultado armazenado corresponde a uma combinação de 264 h, 90%, 75 e R$ 7.

### II — Pessoal

A seção calcula horas remuneradas por mês:

- horas extras 70%: 1 h × 22 dias = 22 h;
- horas extras 100%: 1 h × 4 dias = 4 h;
- horas normais: 7,33333 h × 30 dias ≈ 220 h;
- total remunerado: A × 1,70 + B × 2 + C = 265,3999 h.

Essa quantidade é aplicada a cada função.

Salários mensais por função são derivados de:

- quantidade de trabalhadores;
- valor-hora vindo do canteiro;
- horas remuneradas calculadas.

Resultado de salários: R$ 56.049,4430.

Encargos sociais:

- 110% sobre salários;
- resultado: R$ 61.654,3873.

Cantina:

- alojados: 5 pessoas;
- da cidade: 3 pessoas;
- 15 dias;
- total: R$ 8.025.

Alojamento:

- aluguel R$ 4.000;
- água e luz R$ 400;
- limpeza R$ 400 com resultado armazenado de R$ 4.800;
- subtotal observado: R$ 4.800.

Viagens nas folgas:

- 1 funcionário × R$ 1.500;
- total R$ 1.500.

Prêmios de produção:

- estrutura prevista, sem valores preenchidos.

Total da seção pessoal armazenado: R$ 132.028,8302.

### III — Manutenção

Baseada no valor do equipamento de R$ 2.000.000:

- peças e acessórios: 0,6% ao mês = R$ 12.000;
- docagem anual apropriada mensalmente: 1% ao mês = R$ 20.000;
- limpeza e pintura: 10% das peças = R$ 1.200;
- mão de obra de terceiros: igual a limpeza = R$ 1.200.

Total: R$ 34.400/mês.

### IV — Equipamentos de apoio

Custos diretamente listados:

- linha de recalque: R$ 34.567,50/mês;
- rebocador e cábrea: R$ 10.000;
- barco motor: R$ 1.500;
- tanque de abastecimento: R$ 5.000;
- veículo 4×4: R$ 5.000;
- medição/topografia: R$ 5.000;
- bomba de dragagem: R$ 42.144,4444 por mês, por 18 meses de depreciação;
- canteiro: R$ 2.390,4884/mês;
- peças de reposição da bomba: R$ 23.863/mês, por 18 meses.

Subtotal armazenado: R$ 129.465,4329.

### Linha de recalque

A seção lateral separa:

#### Tubulação

- 600 m × R$ 450/m = R$ 270.000;
- depreciação em 10 meses = R$ 27.000/mês;
- juros de 1% = R$ 2.700/mês;
- subtotal = R$ 29.700/mês.

Observação:
- tubos 14": R$ 390/m;
- ponteira: R$ 400 cada;
- cálculo lateral: 12 m de tubo + 2 ponteiras = R$ 5.240 por conjunto, ou R$ 436,67/m.

#### Flutuantes

- quantidade calculada: 125 peças;
- preço: R$ 250/peça;
- total: R$ 31.250;
- depreciação em 10 meses = R$ 3.125;
- juros de 1% = R$ 312,50;
- subtotal = R$ 3.437,50/mês.

#### Acoplamentos

- 52 peças × R$ 250 = R$ 13.000;
- depreciação em 10 meses = R$ 1.300;
- juros de 1% = R$ 130;
- subtotal = R$ 1.430/mês.

Total mensal da linha: R$ 34.567,50.

### Peças da bomba

Cotação lateral “ALTONA = 2024”:

- bomba completa: R$ 758.600;
- placas de desgaste;
- buchas;
- difusores;
- rotor;
- porca do rotor.

Subtotal de peças principais: R$ 429.534, usado para derivar R$ 23.863/mês em 18 meses.

### V — Administrativas

- comissões: R$ 0;
- viagens de inspeção: R$ 8.000;
- viagens administrativas: R$ 0;
- comunicações: R$ 500;
- seguro/licenciamento: R$ 0.

Total: R$ 8.500.

### Despesas diretas

A fórmula soma:

- operação;
- pessoal;
- manutenção;
- equipamentos de apoio;
- administrativas.

Resultado: R$ 441.964,6631/mês.

### VI — BDI interno

- oficina: 5% das despesas diretas;
- administração: 5% das despesas diretas;
- outros: vazio.

Total: R$ 44.196,4663.

### VII — Financeiras

- depreciação: valor do equipamento ÷ 60 meses = R$ 33.333,3333;
- juros de capital: 1% do equipamento = R$ 20.000;
- atrasos: indicado como 0,5% das despesas diretas, porém valor zero.

Total: R$ 53.333,3333.

### Resumo mensal

- despesas diretas: R$ 441.964,6631;
- BDI interno: R$ 44.196,4663;
- financeiras: R$ 53.333,3333;
- custo total mensal: R$ 539.494,4627.

### Produção, custo unitário e preço de venda

- produção prevista: referência a `Produção!D13`, armazenada como 25.245 m³/mês, mas exibida como `#NAME?` na ferramenta;
- custo unitário: R$ 21,3703/m³;
- BDI de venda: 70%;
- acréscimo: R$ 377.646,1239;
- preço de venda mensal: R$ 917.140,5867;
- preço unitário implícito: aproximadamente R$ 36,329/m³.

### Hora à disposição

A seção calcula:

- custo mensal;
- multiplicador BDI: 1,5;
- preço mensal: R$ 809.241,6941;
- horas do mês;
- eficiência de operação: 60%;
- horas produtivas: 360;
- preço/hora: R$ 1.348,7362.

### DÚVIDA

Os valores e fórmulas dessa seção não são consistentes entre si:

- 264 h/mês aparecem na produção principal;
- 360 h produtivas aparecem na hora à disposição;
- o preço mensal usa multiplicador 1,5, diferente do BDI de 70%;
- existe valor lateral de R$ 3.065,31 e R$ 1.839,19 sem descrição completa.

### Custo total da dragagem

- custo mensal da dragagem: R$ 539.494,4627;
- prazo: 4 meses;
- custo total: R$ 2.157.977,8510.

### Anomalias

- referências `#NAME?` em produção, horas/mês e prazo;
- seções vazias extensas entre pessoal e manutenção;
- título menciona desidratação de lodo sem composição correspondente clara;
- “Desesas Diretas” contém erro de digitação;
- atraso de 0,5% está descrito, mas não calculado;
- custo mensal de canteiro depende de uma aba com erro de referência;
- o BDI interno de 10% e o BDI comercial de 70% coexistem;
- a aba final usa o custo total, não o “preço de venda” desta aba;
- o custo de combustível possui referências visualmente inconsistentes;
- vários custos têm origem em cotações ou estimativas sem data-base completa.

---

## 5.7. Aba `3. Desmobilização`

### Objetivo

Compor custos de retirada da equipe, desmontagem, carregamento e retorno dos equipamentos.

### Estrutura

Reutiliza a mesma composição diária de mão de obra da mobilização.

Itens com valor:

- exames médicos: 8 × R$ 500 = R$ 4.000;
- viagem de volta: 5 × R$ 5.000 = R$ 25.000;
- mão de obra de integração/viagens/treinamentos: 2 dias × custo diário = R$ 11.443,9073;
- guindaste: 2 dias × R$ 6.500 = R$ 13.000;
- mão de obra de desmobilização: 5 dias × custo diário = R$ 28.609,7682.

### Totais

- custo total antes do BDI: R$ 82.053,6755;
- BDI: 100%;
- preço final interno: R$ 164.107,3509.

### Referências de transporte

Preços de carreta, seguro e carga seca são herdados ou repetidos da mobilização, mas as quantidades permanecem vazias.

### Dimensionamento de tubos

Repete o cálculo de 3 carretas para 600 m de linha.

### Anomalias

- seção interna ainda se chama “MOBILIZAÇÃO EQUIPE”;
- vários custos de desmobilização estão zerados por quantidade vazia;
- BDI de 100% não é usado pela aba final;
- `D18` de treinamentos está vazio, produzindo zero;
- referências a preços de mobilização são reutilizadas diretamente;
- não há explicação para exames médicos na desmobilização.

---

## 5.8. Aba `Final`

### Objetivo

Consolidar o preço comercial por item.

### Itens

1. Mobilização e montagem do equipamento.
2. Dragagem.
3. Desmobilização do equipamento.

### Custos consolidados

- mobilização: R$ 92.275,6291;
- dragagem total: R$ 2.157.977,8510;
- desmobilização: R$ 82.053,6755;
- custo total: R$ 2.332.307,1555.

### Regra comercial

Cada item recebe BDI de 70%:

- mobilização: R$ 156.868,5695;
- dragagem: R$ 39,4469/m³ × 93.000 m³ = R$ 3.668.562,3466;
- desmobilização: R$ 139.491,2483.

Preço total de venda: R$ 3.964.922,1643.

### Resultados adicionais

- faturamento médio indicado por quarto do total: R$ 991.230,5411;
- custo mensal da dragagem: R$ 539.494,4627;
- faturamento mensal da dragagem: R$ 917.140,5867;
- resultado total: R$ 1.632.615,0088;
- resultado mensal: R$ 408.153,7522;
- resultado mensal “livre”: R$ 377.646,1239.

### Regras implícitas

- mobilização e desmobilização são itens globais de quantidade 1;
- dragagem é medida por m³;
- o custo total de dragagem usa o prazo arredondado de 4 meses;
- o preço de venda da dragagem é calculado sobre os 93.000 m³;
- os valores mensais são obtidos dividindo por 4, não pelo prazo decimal de 3,6839 meses.

### Anomalias e dúvidas

- A aba ignora o BDI de 100% calculado nas abas de mobilização e desmobilização e aplica 70% diretamente sobre o custo.
- A descrição “preço mensal” em `Dados Obra` convive com preço unitário em m³ na aba final.
- O resultado mensal total é dividido por 4, embora mobilização e desmobilização não sejam necessariamente faturadas uniformemente.
- “Resultado mensal livre” é somente preço mensal da dragagem menos custo mensal da dragagem; não há impostos, tributos ou capital de giro explicitamente abatidos.
- O campo K7 divide o preço total de venda por 4 e parece representar faturamento médio mensal, sem título explícito.

---

# 6. Entidades encontradas

### EVIDÊNCIA CONFIRMADA

- Proposta.
- Cliente.
- Contato.
- Obra.
- Local.
- Material dragado.
- Volume.
- Área e espessura de dragagem.
- Linha de recalque.
- Linha flutuante.
- Linha de terra.
- Draga.
- Bomba.
- Equipamento de apoio.
- Veículo.
- Equipe.
- Função/cargo.
- Turno.
- Jornada.
- Salário.
- Dissídio.
- Adicional de transferência.
- Leis sociais.
- Refeição.
- Transporte de pessoal.
- Alojamento.
- Canteiro.
- Mobilização.
- Desmobilização.
- Cotação.
- Item de custo.
- Quantidade.
- Unidade.
- Preço unitário.
- Custo mensal.
- Custo total.
- BDI.
- Preço de venda.
- Produção.
- Prazo.
- Hora à disposição.
- Responsabilidade do cliente.

---

# 7. Regras de negócio observadas

## Produção e prazo

### EVIDÊNCIA CONFIRMADA

- Produção horária = vazão × eficiência × concentração.
- Produção mensal = produção horária × horas/dia × dias/mês.
- Prazo = volume ÷ produção mensal.
- Prazo contratual usado no custo = arredondamento para cima do prazo matemático.

## Mão de obra

### EVIDÊNCIA CONFIRMADA

- Salários são convertidos por divisor 220.
- Dissídio de 7,5% é incorporado ao valor/hora.
- Algumas funções recebem adicional de transferência de 25%.
- Leis sociais são aplicadas em 110% do custo salarial.
- Horas remuneradas mensais incluem hora extra a 70%, hora extra a 100% e 220 horas normais.

## Manutenção

### EVIDÊNCIA CONFIRMADA

- Peças: 0,6% ao mês sobre valor do equipamento.
- Docagem: 1% ao mês sobre valor do equipamento.
- Limpeza/pintura: 10% do valor de peças.
- Terceiros: igual à limpeza/pintura.

## Capital

### EVIDÊNCIA CONFIRMADA

- Draga depreciada em 60 meses.
- Juros de capital de 1% ao mês sobre o valor do equipamento.
- Linha de recalque depreciada em 10 meses.
- Bomba e peças depreciadas em 18 meses.

## Comercial

### EVIDÊNCIA CONFIRMADA

- Mobilização e desmobilização são tratadas como verbas globais.
- Dragagem é precificada em R$/m³.
- A aba final aplica 70% sobre cada item de custo.
- O custo total de dragagem considera custo mensal × prazo arredondado.

---

# 8. Valores e coeficientes embutidos

### EVIDÊNCIA PARCIAL — específicos deste arquivo até crosscheck

- Vazão: 850 m³/h.
- Eficiência de produção: 75%.
- Concentração: 15%.
- Jornada: 12 h/dia.
- Dias: 22/mês.
- Leis sociais: 110%.
- Dissídio: 7,5%.
- Transferência: 25%.
- Eficiência de combustível: 90%.
- Consumo: 75 por hora.
- Combustível: R$ 7.
- BDI interno da operação: 10% em duas parcelas de 5%.
- BDI comercial: 70%.
- BDI de mobilização/desmobilização: 100%.
- Depreciação da draga: 60 meses.
- Depreciação de linha: 10 meses.
- Depreciação de bomba/peças: 18 meses.
- Juros: 1% ao mês.
- Manutenção de peças: 0,6% ao mês.
- Docagem: 1% ao mês.
- Horas normais mensais: 220.
- Refeição diária usada em mobilização: R$ 35.
- Transporte diário: R$ 15.

Nenhum desses valores deve ser tratado como regra geral da FOS com base somente neste arquivo.

---

# 9. Dependências entre abas

### EVIDÊNCIA CONFIRMADA

- `Dados Obra` → `Produção`: jornada, dias e volume.
- `Dados Obra` → `2. Dragagem`: extensão de linha.
- `Dados Obra` → `1. Mobilização` e `3. Desmobilização`: extensão de linha para quantidade de carretas.
- `Produção` → `Canteiro`: prazo.
- `Produção` → `2. Dragagem`: horas, produção mensal e prazo.
- `MDO x Turno` → `Canteiro`: quantitativos da equipe.
- `MDO x Turno` → `1. Mobilização` e `3. Desmobilização`: equipe e veículos.
- `Canteiro` → mobilização/desmobilização: custo/hora, horas/dia, leis sociais e custo diário.
- `Canteiro` → `2. Dragagem`: valores/hora e custo mensal do canteiro.
- `1. Mobilização` → `2. Dragagem`: quantitativos de equipe.
- `1. Mobilização`, `2. Dragagem`, `3. Desmobilização` → `Final`: custos consolidados.

---

# 10. Anomalias consolidadas

### EVIDÊNCIA CONFIRMADA

1. Referências que retornam `#NAME?` em células ligadas a `Produção`.
2. Nome de aba referenciado com espaço final aparente: `'Dados Obra '`.
3. Datas internas potencialmente conflitantes: 2024, 2025 e cotação de 2026.
4. Paralisações calculadas, mas não descontadas da produção principal.
5. BDI de 100% em mobilização/desmobilização não utilizado no fechamento.
6. BDI interno de 10% na dragagem e BDI comercial de 70% coexistem.
7. Seção “hora à disposição” usa premissas diferentes da produção mensal.
8. Sistema de medição declarado como mensal, mas fechamento de dragagem por m³.
9. Quantidades vazias zeram itens com preço unitário informado.
10. Vários preços são “chute” ou mensagens informais de cotação.
11. Responsabilidades de SBV/cliente/COEDRA são registradas em texto livre.
12. Título da dragagem menciona desidratação de lodo sem composição detalhada correspondente.
13. O prazo decimal é arredondado para 4 meses e todos os rateios finais usam 4.
14. “Resultado livre” não explicita tributos ou outros descontos.
15. Estruturas de mobilização e desmobilização contêm rótulos copiados.
16. A fórmula geométrica de carga de tubos trabalha com quantidade fracionária antes do arredondamento final.
17. Erros de digitação e nomenclatura aparecem em vários rótulos.

---

# 11. Evidências parciais e possíveis padrões para futuro crosscheck

### EVIDÊNCIA PARCIAL

- Separação do orçamento em mobilização, operação e desmobilização.
- Produção da draga baseada em vazão × eficiência × concentração.
- Prazo arredondado para cima.
- Uso de custo mensal para operação e custo global para mobilização/desmobilização.
- Composição de pessoal por salário/hora, adicional, horas extras e leis sociais.
- Depreciação e juros sobre equipamentos e linha.
- Linha de recalque decomposta em tubulação, flutuantes e acoplamentos.
- Aplicação de BDI comercial por item na planilha final.
- Registro de responsabilidade do cliente por itens zerados.

Esses elementos não são declarados como padrão geral.

---

# 12. Dúvidas para validação do especialista

1. A data correta da proposta é 2024-04-11 ou 2025?
2. O objeto é locação mensal, execução por m³ ou contrato híbrido?
3. As paralisações deveriam reduzir as 12 horas/dia?
4. A concentração de 15% é volumétrica, mássica ou fator empírico?
5. Qual é a origem do valor 90% na operação, diferente dos 75% da produção?
6. O combustível é fornecido pela SBV? O texto lateral indica isso, mas o custo é incluído.
7. O adicional de transferência de 25% deve alcançar quais funções?
8. Por que ajudantes aparecem como fornecidos pelo cliente e também entram no custo?
9. O BDI correto de mobilização/desmobilização é 100% ou 70%?
10. O BDI interno de 10% deve compor a base antes do BDI comercial de 70%?
11. A manutenção de 0,6% e docagem de 1% são regras vigentes ou estimativas deste equipamento?
12. O atraso de 0,5% deveria estar calculado?
13. O prazo de 4 meses inclui mobilização/desmobilização ou somente operação?
14. O rateio do preço total em quatro meses é usado comercialmente?
15. A seção de hora à disposição é alternativa ou parte da proposta?
16. O título sobre desidratação de lodo é aplicável a esta obra?
17. Quais itens são responsabilidade da SBV, da COEDRA e do cliente?
18. As quantidades vazias representam item excluído, pendente ou responsabilidade externa?
19. A cotação de 14/04/26 está correta?
20. O custo da linha de recalque deve usar R$ 450/m ou o cálculo lateral de R$ 436,67/m?
21. Os flutuantes são realmente calculados como 500/12 × 3 = 125 peças?
22. A bomba completa e as peças devem ser depreciadas simultaneamente?
23. Exames médicos na desmobilização são intencionais?
24. O “resultado mensal livre” deve descontar impostos, comissões e capital de giro?

---

# 13. Classificação das evidências

## EVIDÊNCIA CONFIRMADA

Tudo que foi transcrito de células, fórmulas, rótulos, dependências e resultados armazenados no arquivo.

## EVIDÊNCIA PARCIAL

Interpretações operacionais e possíveis padrões observados somente neste orçamento, incluindo a classificação da família, a separação econômica e os coeficientes.

## DÚVIDA

Significados não explicitados, inconsistências de BDI, responsabilidades, erros de referência, unidade da concentração, caráter mensal ou unitário da medição e aplicabilidade da desidratação.

---

# 14. Validação final

- [x] Todas as 8 abas analisadas.
- [x] Documento exclusivo deste orçamento produzido.
- [x] Valores, fórmulas, dependências, regras e anomalias preservados.
- [x] Evidências classificadas.
- [x] Limitações registradas.
- [x] Nenhuma comparação com outros orçamentos realizada.
- [x] Nenhuma consolidação realizada.
- [x] Nenhuma decisão arquitetural tomada.
- [x] Nenhuma funcionalidade ou banco de dados proposto.
- [x] Nenhum arquivo Excel alterado.
