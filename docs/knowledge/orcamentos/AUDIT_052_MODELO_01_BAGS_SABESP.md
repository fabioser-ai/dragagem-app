# AUDIT_052 — Modelo 01 — Obra com desaguamento em Bags

## Status

- Primeiro modelo analisado integralmente.
- Nenhuma implementação funcional autorizada.
- Documento de descoberta; não representa ainda o método geral da FOS.
- Sujeito a correções por novos modelos, uso real e validação do especialista.

## Fonte

Arquivo analisado:

`D_004_2026 - SABESP.xlsx`

Identificação interna observada no conteúdo:

- proposta indicada na aba de dados: `Proposta D_055_2021`;
- cliente: `SABESP - CUBATAO ETA 3`;
- objeto: `Dragagem ETEL ETA3`;
- volume de referência: `5.000 m³`;
- material: `Areia + Lodo + Antracito`;
- destinação ou método indicado: `Bag`.

A divergência entre o nome externo do arquivo e a identificação interna deve ser preservada como fato e esclarecida futuramente. Não assumir que ano, código ou versão estejam corretos sem confirmação.

## Objetivo desta análise

Compreender como este orçamento foi construído, quais informações são usadas, como as abas se relacionam e quais conceitos deverão ser comparados com os próximos modelos.

O objetivo não foi desenhar telas nem definir a arquitetura definitiva.

## Método de análise

As evidências são classificadas como:

- **Fato observado:** conteúdo presente no Excel.
- **Informação do especialista:** explicação dada por Fabio.
- **Interpretação:** significado provisório atribuído ao conteúdo.
- **Hipótese para crosscheck:** entendimento que depende da comparação com outros orçamentos.

## Inventário do arquivo

O arquivo possui 17 abas:

1. `Dados Obra`;
2. `Cotaçoes`;
3. `Produção`;
4. `Barrilete`;
5. `1. Mob. Draga`;
6. `2. Mob. Eq. Polimero`;
7. `Canteiro`;
8. `3. Prep. Célula`;
9. `4. Forn. Bag`;
10. `5. Operação Sistema`;
11. `6. Dragagem`;
12. `7. Medição`;
13. `8. Carga e Transporte`;
14. `8. Desmob. Draga`;
15. `9. Desmob. Eq. Polimero`;
16. `10. Plan. Preços`;
17. `Planilha1`.

## Leitura global do modelo

### Fato observado

O orçamento combina:

- dados gerais da obra;
- premissas de produção;
- cotações;
- dimensionamentos físicos;
- composições de mão de obra, materiais, equipamentos e serviços;
- custos mensais e custos globais;
- aplicação de BDI por item na consolidação;
- apresentação final resumida ao cliente.

### Interpretação

O Excel funciona como implementação atual de um método operacional e comercial. A matemática é majoritariamente simples; a complexidade relevante está na decomposição da execução, nas dependências entre variáveis e na escolha dos componentes que entram em cada composição.

### Hipótese para crosscheck

O futuro sistema poderá ser um motor de orçamento formado por componentes reutilizáveis. Essa hipótese ainda não está consolidada, pois foi observada em apenas um tipo de obra.

# Análise por aba

## 1. Dados Obra

### Fatos observados

A aba reúne:

- proposta e data;
- cliente e contato;
- objeto e local;
- volume;
- tipo de material;
- distâncias de recalque, linha flutuante e linha de terra;
- profundidade, espessura e área;
- tipo de bota-fora;
- sistema de medição;
- responsabilidade pelo canteiro e mobilização;
- horas de trabalho por dia;
- dias de trabalho por mês.

O arquivo distingue visualmente dados a preencher, pendências e resultados automáticos.

Para este modelo foram observados, entre outros:

- volume de 5.000 m³;
- recalque total informado de 200 m;
- 100 m de linha flutuante;
- 100 m de linha de terra;
- 9 h/dia;
- 22 dias/mês.

### Interpretação

A aba funciona como conjunto de premissas do orçamento, misturando identidade comercial, características físicas, decisões executivas e calendário operacional.

### Hipóteses para crosscheck

- parte dos dados poderá vir do CRM;
- parte poderá pertencer ao cadastro futuro da obra;
- premissas técnicas devem permanecer versionadas por orçamento;
- os campos obrigatórios e opcionais podem variar por tipo de obra.

## 2. Cotaçoes

### Fatos observados

A aba possui seções para:

- guindaste;
- container;
- banheiro químico;
- destinação.

As colunas registram nome, contato, telefone, detalhe e preço, com unidade de preço adaptada à categoria.

No arquivo analisado, a estrutura está presente, mas as linhas de cotação estão vazias.

### Interpretação

A aba registra informação de mercado que pode alimentar o orçamento, mas não demonstra ainda um cadastro histórico estruturado.

### Hipóteses para crosscheck

- fornecedor e contato podem ser cadastros reutilizáveis;
- preço cotado deve permanecer ligado ao orçamento, à data e à condição específica;
- não consolidar ainda um único modelo para clientes e fornecedores.

## 3. Produção

### Fatos observados

Entradas principais:

- vazão: 120 m³/h;
- eficiência: 60%;
- concentração: 15%;
- jornada: 9 h/dia;
- calendário: 22 dias/mês.

Resultados apresentados:

- produção: 10,8 m³/h;
- horas trabalhadas: 198 h/mês;
- produção mensal: 2.138,4 m³/mês;
- prazo: aproximadamente 2,338 meses para 5.000 m³.

### Interpretação

A aba transforma premissas hidráulicas e operacionais em produção e prazo. O prazo alimenta custos dependentes do tempo em outras abas.

### Hipóteses para crosscheck

- produção pode ser núcleo comum a vários tipos de orçamento;
- eficiência, concentração e vazão podem ser próprias da obra, do equipamento, do material ou de combinação entre eles;
- valores históricos poderão futuramente sugerir premissas, sem eliminar a decisão do engenheiro.

## 4. Barrilete

### Fatos observados

A aba calcula inicialmente um custo diário de mão de obra com:

- operadores;
- ajudantes;
- refeições;
- transporte;
- leis sociais.

Depois compõe um conjunto físico com tubos, tocos, joelhos, tees, válvulas, mangueira, braçadeiras, curvas, bomba e mão de obra de montagem.

O total dos componentes é R$ 29.616,80. A aba aplica 20% de depreciação e obtém R$ 5.923,36 como preço final interno neste modelo. O BDI da própria aba está zerado.

### Interpretação

A aba mistura composição técnica, custo de montagem e regra de recuperação ou depreciação do ativo.

### Perguntas para crosscheck

- por que somente 20% do valor total é levado adiante;
- quando o barrilete é comprado, depreciado, reutilizado ou cobrado integralmente;
- quais componentes variam com diâmetro, distância e sistema de desaguamento.

## 5. Mobilização da Draga

### Fatos observados

A composição inclui:

- equipe para carga e montagem;
- guindaste;
- carreta;
- frete;
- possível trator;
- treinamentos;
- mobiliário;
- mão de obra por dias.

Itens sem quantidade produzem valor zero e permanecem visíveis como alternativas.

Custo final observado: R$ 16.961,72, com BDI interno zerado.

### Interpretação

Trata-se de evento de implantação composto por mão de obra e contratações específicas.

## 6. Mobilização e montagem do equipamento de polímero

### Fatos observados

A composição inclui:

- equipe;
- cobertura;
- munck;
- brita e concreto;
- frete;
- instalações hidráulicas e elétricas;
- máquina WAP;
- barrilete referenciado pelo valor de R$ 5.923,36;
- mão de obra de apoio.

Custo final observado: R$ 39.925,08, com BDI interno zerado.

### Interpretação

A aba demonstra dependência entre pacotes: o resultado do Barrilete é consumido pela mobilização do sistema de polímero.

## 7. Canteiro

### Fatos observados

A aba é identificada como subitem da Dragagem.

Ela combina:

- custo diário de equipe;
- containers;
- fretes;
- documentos e programas legais;
- ART;
- placa;
- vigilância;
- água;
- material de escritório;
- banheiro químico;
- exames médicos;
- integração.

O total é dividido por um prazo de operação informado como 2, gerando preço unitário mensal antes do BDI.

Foi observada fórmula quebrada com resultado `#NAME?` na quantidade de container. Apesar disso, o preço total do container aparece como R$ 3.000,00, indicando valor calculado ou preservado no arquivo.

### Interpretação

O canteiro reúne infraestrutura e conformidade necessárias à operação e possui custos direcionados pelo tempo.

### Risco observado

Fórmulas `#NAME?` indicam incompatibilidade, nome definido ausente ou função não reconhecida. O comportamento original precisa ser recuperado antes da migração.

## 8. Preparo de Célula

### Fatos observados

A aba contém coeficientes de dimensionamento por área:

- manta PEAD: 1,196 m² por m² de célula;
- Bidim: 1,48 m² por m² de célula;
- brita: 0,15 m³ por m² de célula;
- retroescavadeira: 0,023 h por m² de célula;
- mão de obra: 0,023 h por m² de célula.

Esses coeficientes são convertidos em quantitativos e depois em custos de preparo, mobilização, regularização, PEAD, instalação, Bidim, brita, retroescavadeira e mão de obra.

Preço final observado: R$ 177.323,61 para uma repetição.

### Interpretação

A aba separa implicitamente dimensionamento físico e composição financeira.

### Hipóteses para crosscheck

- os coeficientes podem depender do padrão construtivo, fornecedor, geometria, reaproveitamento ou experiência histórica;
- não tratá-los como constantes globais antes de outras planilhas.

## 9. Fornecimento de Bags

### Fatos observados

A parte superior compõe custos de:

- diferentes modelos de bags;
- frete;
- munck;
- mão de obra de instalação.

Foram selecionados neste modelo:

- 10 bags de 8 x 15 m;
- 5 bags de 8 x 30 m.

Preço final observado: R$ 355.460,245, sem BDI interno.

A parte inferior calcula:

- volume dragado: 5.000 m³;
- sólidos in situ: 10%;
- tonelada seca: 500;
- sólidos após desaguamento: 20%;
- volume a acomodar: 2.500 m³.

Também mantém uma tabela de capacidades por modelo de bag e uma combinação escolhida que soma 15 bags e capacidade final de 4.550 m³.

### Interpretação

A aba liga uma necessidade de armazenamento ou desaguamento à seleção de bags e à composição comercial de fornecimento e instalação.

### Perguntas para crosscheck

- diferença entre o volume a acomodar, 2.500 m³, e a capacidade final selecionada, 4.550 m³;
- significado e aplicação da coluna `Reinicio Celula`;
- origem das capacidades por bag;
- regras para combinação de tamanhos.

## 10. Operação do Sistema de Desidratação

### Fatos observados

A composição inclui:

- equipamento de preparo e injeção de polímero;
- polímero calculado sobre base seca;
- frete;
- água e energia, zeradas e indicadas como fornecidas pela contratante;
- instalações hidráulicas;
- máquina WAP;
- mão de obra por 90 dias.

Para o polímero, a planilha registra 1.575 kg e anotação de `3 kg por ton seca`, com preço unitário de R$ 22,00.

Custo total observado: R$ 122.994,8175. Custo mensal observado: R$ 40.998,2725.

A célula do prazo apresenta `#NAME?`.

### Informação do especialista

O consumo de polímero varia conforme:

- tipo de material;
- equipamento ou método de desaguamento;
- características da obra;
- experiência histórica.

O valor de 3 kg/t seca é premissa deste orçamento, não constante geral da FOS.

Com o tempo, o histórico deverá permitir sugestões de consumo por combinação de material e equipamento, mantendo o valor efetivamente escolhido pelo engenheiro.

### Decisão de conhecimento

Nunca codificar `3 kg/t` como constante global.

## 11. Dragagem

### Fatos observados

A aba é identificada como `CUSTO DE DRAGAGEM, Canteiro e Operação do Sistema de Desidratação de lodo` e apresenta uma estrutura ampla de custos.

Foram observadas as seguintes seções:

1. Operação;
2. Pessoal;
3. Manutenção;
4. Equipamentos de apoio;
5. Administrativas;
6. BDI;
7. Financeiras;
8. Resumo;
9. cálculo de hora à disposição;
10. consolidação com operação dos bags e polímero.

Na operação aparecem combustível, filtros, fretes e materiais de segurança.

A fórmula descrita para combustível é `0,15 x HP x hora`, aplicada neste modelo sobre 198 horas, eficiência de 0,9, consumo de 7 e combustível de R$ 9,00, resultando em R$ 11.226,60.

A seção de pessoal modela horas normais e extras, salários, encargos sociais, cantina, alojamento, viagens nas folgas e prêmios de produção.

A seção de manutenção inclui peças, docagem, limpeza, pintura e terceiros.

Equipamentos de apoio incluem linha de recalque, batimetria final, automóvel, medidor de vazão e densidade, ferramentas e canteiro.

O resumo observado contém:

- despesas diretas: R$ 57.823,3591;
- BDI interno: R$ 5.782,3359;
- financeiras: R$ 4.289,1168;
- custo mensal da dragagem: R$ 67.894,8118;
- custo mensal de operação dos bags e polímero: R$ 40.998,2725;
- custo mensal total: R$ 108.893,0843;
- custo total da dragagem mais operação dos bags: R$ 326.679,2530.

A célula de tempo de operação apresenta `#NAME?`, embora o custo total preserve valor compatível com três meses de custo mensal.

### Interpretação

Esta aba é uma composição operacional mensal extensa, com subgrupos de custo e consolidação da dragagem com a operação do sistema de desaguamento.

### Perguntas para crosscheck

- quais percentuais são regras gerais, decisões comerciais ou premissas deste modelo;
- como é obtido o valor `0,15` do combustível;
- qual é a origem dos custos de manutenção e financeiros;
- quais itens se repetem em outros tipos de draga;
- quais custos pertencem ao canteiro e quais pertencem exclusivamente à dragagem.

## 12. Medição

### Fatos observados

A aba compõe:

- amostras;
- batimetria FOS;
- acompanhamento de coleta dos bags;
- equipe de apoio calculada por dia.

Preço final observado: R$ 14.204,144.

### Interpretação

O conteúdo trata de custos de geração de evidências e acompanhamento técnico, e não do módulo operacional de boletins de medição já existente no APP.

## 13. Carga e Transporte

### Fatos observados

Apesar do nome da aba, seu título interno permanece `8 - Medição`.

A composição contém:

- carga e transporte a 6 km;
- batimetria;
- acompanhamento FOS;
- equipe diária.

As quantidades estão vazias, e todos os preços totais resultam em zero.

### Interpretação

A aba funciona como alternativa ou pacote não utilizado neste orçamento.

### Risco observado

Nome da aba e título interno divergentes indicam cópia ou reaproveitamento de template. A migração não deve inferir semântica somente pelo nome da aba.

## 14. Desmobilização da Draga

### Fatos observados

A composição inclui:

- equipe;
- fretes;
- mão de obra de desmontagem;
- guindaste.

Preço final observado: R$ 17.310,245.

### Interpretação

A desmobilização é calculada como evento próprio; não é simples cópia aritmética da mobilização.

## 15. Desmobilização do Equipamento de Polímero

### Fatos observados

A aba mantém diversos itens da montagem como possibilidades, mas somente frete e mão de obra possuem quantidade neste modelo.

Preço final observado: R$ 6.808,91.

### Interpretação

A estrutura preserva itens opcionais com valor zero, permitindo adaptar a composição sem remover linhas.

## 16. Planilha Detalhada de Preços

### Fatos observados

A aba consolida custos e aplica BDI por item.

Itens observados:

- mobilização da draga;
- mobilização do equipamento de polímero e barrilete;
- preparo de célula;
- fornecimento de bags;
- dragagem e operação do sistema de polímero;
- medição;
- desmobilização da draga;
- desmobilização do equipamento de polímero.

BDIs aplicados:

- 60% na maior parte dos itens;
- 45% no fornecimento de bags.

Valores consolidados:

- custo total: R$ 937.711,4870;
- preço de venda: R$ 1.474.158,0945.

### Interpretação

A aba traduz composições internas para itens comerciais, unidades, quantidades, preços unitários e preços totais.

### Hipótese para crosscheck

Uma mesma composição técnica pode admitir apresentações comerciais diferentes conforme edital, contrato ou estratégia de venda.

## 17. Planilha1

### Fatos observados

A aba não está vazia. Ela apresenta uma versão comercial ainda mais resumida com quatro linhas:

1. mobilização e montagem dos equipamentos;
2. preparo da célula de desaguamento;
3. dragagem e desaguamento com fornecimento e operação dos geobags;
4. desmobilização dos equipamentos.

O total geral é o mesmo preço de venda da planilha detalhada: R$ 1.474.158,0945.

### Correção de interpretação anterior

A aba não deve ser classificada como residual sem função. Ela representa uma apresentação comercial agregada, possivelmente próxima da estrutura entregue ao cliente.

# Padrões observados neste modelo

## 1. Cálculo de custo diário de equipe

Diversas abas repetem a estrutura:

- quantidade de funcionários;
- valor por hora;
- horas por dia;
- leis sociais;
- refeições;
- transporte;
- custo diário resultante.

Esse custo é reutilizado em itens de montagem, operação, integração, batimetria ou acompanhamento.

## 2. Separação entre quantidade física e preço

Os custos normalmente nascem de um direcionador operacional:

- tempo;
- volume;
- massa seca;
- área;
- quantidade de peças;
- evento único.

Somente depois são convertidos em dinheiro.

## 3. Itens opcionais preservados com zero

Muitas composições mantêm linhas com preço unitário, mas quantidade vazia ou zero. Isso permite ativar ou desativar componentes sem alterar a estrutura da planilha.

## 4. Dependências entre abas

Exemplos observados:

- volume da obra alimenta Produção e Bags;
- prazo de Produção influencia custos mensais;
- Barrilete alimenta mobilização do equipamento de polímero;
- operação do sistema alimenta a composição de Dragagem;
- resultados das composições alimentam a Planilha de Preços;
- a Planilha1 agrega os itens comerciais detalhados.

## 5. BDI em mais de um nível

Algumas abas possuem campo de BDI interno, muitas vezes zerado. A planilha detalhada aplica BDI comercial por item, com percentuais diferentes.

A política de BDI precisa ser compreendida antes da implementação.

## 6. Mistura de dados, memória e cálculo

O arquivo mistura:

- entradas editáveis;
- fórmulas;
- preços de referência;
- anotações de fornecedor;
- datas de cotação;
- observações operacionais;
- valores copiados ou preservados mesmo quando fórmulas apresentam erro.

A migração deve preservar a origem e a data das premissas relevantes.

# Modelo conceitual provisório

Somente para orientar o crosscheck, este arquivo sugere as seguintes camadas:

1. identificação e premissas da obra;
2. informação de mercado;
3. modelos de produção e dimensionamento;
4. composições executivas;
5. custos operacionais mensais;
6. eventos de mobilização e desmobilização;
7. consolidação de custo;
8. aplicação comercial de BDI;
9. apresentação detalhada e apresentação resumida.

Esse modelo é provisório. Não criar arquitetura definitiva com base apenas nele.

# Correções produzidas durante a análise

## Consumo de polímero

Interpretação inicial incorreta: tratar 3 kg/t seca como coeficiente geral.

Correção do especialista: o consumo depende do tipo de material, do equipamento ou método de desaguamento e da experiência histórica.

Decisão: preservar valor utilizado por orçamento e futuramente relacionar histórico por contexto operacional.

## Planilha1

Interpretação inicial incorreta: aba residual ou de teste.

Correção pela inspeção integral: a aba contém a apresentação comercial agregada do orçamento e reproduz o preço total final.

# Riscos e inconsistências observadas

- nome externo do arquivo diverge da proposta interna;
- fórmulas com resultado `#NAME?` em Canteiro, Operação do Sistema e Dragagem;
- nomes e numeração de abas não são perfeitamente consistentes;
- `Carga e Transporte` mantém título interno de Medição;
- dados e preços de épocas diferentes podem coexistir;
- diversas regras e percentuais não informam origem;
- alguns valores finais permanecem disponíveis apesar de fórmulas intermediárias quebradas;
- o arquivo contém itens não utilizados preservados com zero;
- valores comerciais são agregados de formas diferentes nas duas abas finais.

# Conhecimento ainda não consolidado

Não estão definidos como regra geral:

- estrutura obrigatória de todo orçamento FOS;
- conceito definitivo de pacote executivo;
- hierarquia entre sistema, pacote, subpacote e recurso;
- coeficientes gerais de produção, combustível, célula ou bags;
- política geral de BDI;
- modelo canônico de mão de obra;
- tratamento de ativos reutilizáveis e depreciação;
- forma geral de apresentar a proposta ao cliente;
- quais dados pertencem a CRM, Dados, Obras ou Orçamentos.

# Próximo passo oficial

1. Receber outros modelos de orçamento.
2. Analisar cada arquivo integralmente em documento próprio.
3. Preservar fatos, exceções e correções do especialista.
4. Não implementar ainda.
5. Após amostra suficiente, executar crosscheck horizontal entre modelos.
6. Consolidar o Método de Orçamento FOS.
7. Somente então definir arquitetura, Kid Steps e implementação do sistema orçamentário.

# Decisão final desta etapa

O primeiro Excel é tratado como um modelo completo de obra com dragagem e desaguamento em bags, não como template universal.

Ele fornece a primeira referência do futuro sistema orçamentário, mas nenhuma estrutura encontrada será considerada definitiva antes da análise dos demais modelos e do crosscheck formal.
