# MODELO CONCEITUAL V0 — NOVO SISTEMA DE ORÇAMENTOS FOS

**Data:** 28/08/2026  
**Natureza:** timestamp arquitetural / hipótese conceitual inicial  
**Status:** desenho aprovado para preservação; não representa especificação final de implementação  
**Escopo:** Novo Sistema de Orçamentos FOS  

---

## 1. Objetivo deste documento

Este documento preserva o pensamento arquitetural inicial construído em paralelo à mineração histórica dos orçamentos FOS.

Ele não pretende homologar a taxonomia definitiva dos blocos, fórmulas, dependências ou estrutura de dados. Seu objetivo é registrar decisões que já parecem suficientemente sólidas, hipóteses que merecem ser testadas e pontos que deliberadamente permanecem abertos até que haja evidência histórica e testes suficientes.

A V0 deve ser tratada como um **timestamp arquitetural**. Se a mineração histórica, os testes ou o uso real mostrarem que alguma decisão precisa mudar, a evolução deverá ser registrada em nova versão, preservando esta V0 como memória do raciocínio inicial.

### Etiquetas utilizadas

- **CONFIRMADO** — prática atual da FOS descrita e validada durante a concepção ou evidência já disponível.
- **HIPÓTESE V0** — desenho considerado adequado neste momento, mas ainda sujeito a validação prática/histórica.
- **PENDENTE DE EVIDÊNCIA** — decisão que não deve ser cristalizada antes da mineração histórica e/ou testes.

---

## 2. Princípios orientadores

### 2.1. A base acelera; o engenheiro decide

**CONFIRMADO**

As tabelas-base e cadastros institucionais existem para acelerar o preenchimento e melhorar consistência, mas não são juízes dos valores utilizados no orçamento.

Obras são específicas e podem exigir valores muito diferentes dos padrões, inclusive valores que pareçam inicialmente improváveis. O engenheiro deve manter liberdade para alterar valores quando a condição real da obra justificar.

O sistema poderá informar referência, origem, histórico ou alertas, mas não deverá bloquear um valor apenas porque ele diverge da base.

### 2.2. Representar primeiro a prática real da FOS

**CONFIRMADO**

O Novo Orçamentos não deve tentar corrigir de imediato todas as práticas atuais. Mudanças abruptas criariam atrito operacional e poderiam prejudicar adoção.

A primeira obrigação do sistema é representar corretamente a forma como a FOS trabalha hoje, deixando a arquitetura preparada para melhorias futuras identificadas com evidência.

### 2.3. Desenhar flexível, validar cedo, cristalizar tarde

**CONFIRMADO**

Recorrências encontradas em planilhas não devem ser automaticamente transformadas em regras rígidas de domínio.

A mineração histórica do Work e os futuros testes devem confirmar quais relações são estruturais, quais são apenas recorrentes e quais possuem exceções relevantes.

---

## 3. Identidade do Orçamento e ciclo de vida

### 3.1. Orçamento como identidade permanente

**CONFIRMADO**

O **Orçamento** representa a identidade permanente do trabalho/oportunidade que está sendo orçado.

Alterações durante sua elaboração não criam automaticamente versões formais.

### 3.2. Elaboração antes da versão

**CONFIRMADO**

Enquanto o orçamento está sendo construído, o engenheiro pode:

- alterar dados;
- rever premissas;
- incluir blocos;
- remover blocos;
- duplicar blocos;
- substituir equipamentos;
- modificar quantitativos;
- recalcular custos;
- salvar e continuar trabalhando.

Essas alterações fazem parte da elaboração. Não constituem versões formais por si só.

### 3.3. Uma versão só nasce quando o orçamento é concluído/formalizado

**CONFIRMADO**

Uma versão técnica só deve existir quando o orçamento tiver sido levado até sua conclusão/formalização.

Fluxo conceitual:

```text
ORÇAMENTO EM ELABORAÇÃO
        ↓
edições / revisões internas / salvamentos
        ↓
CONCLUIR / FORMALIZAR
        ↓
VERSÃO TÉCNICA V1
```

Caso uma revisão futura seja necessária:

```text
VERSÃO TÉCNICA V1
        ↓
criar revisão em elaboração
        ↓
alterações
        ↓
CONCLUIR / FORMALIZAR
        ↓
VERSÃO TÉCNICA V2
```

Se a revisão não chegar à conclusão, ela não deve ser apresentada como uma nova versão técnica formal.

### 3.4. Versões formalizadas são memória histórica

**CONFIRMADO**

Uma versão concluída deve preservar o estado técnico daquele momento. Alterações posteriores devem ocorrer em nova elaboração/revisão e não sobrescrever retroativamente a versão formalizada.

---

## 4. Técnica e Comercial são entidades separadas

### 4.1. Separação obrigatória

**CONFIRMADO**

Proposta/Orçamento Técnico e Proposta Comercial são conceitos distintos e não devem ser misturados.

A camada técnica responde essencialmente ao que será executado, com quais recursos, premissas, produtividades, quantidades, durações e custos.

A camada comercial representa preço e condições oferecidas ao cliente, incluindo as decisões de negociação pertinentes.

### 4.2. Versionamentos independentes e relacionados

**CONFIRMADO**

O versionamento técnico e o versionamento comercial devem ser independentes, mantendo vínculo explícito entre eles.

Exemplo sem alteração técnica:

```text
TÉCNICA V1
   ├── COMERCIAL V1 — oferta inicial
   ├── COMERCIAL V2 — negociação/desconto
   └── COMERCIAL V3 — nova condição financeira
```

A Técnica V1 permanece inalterada se o cliente aceitar a solução técnica e solicitar somente negociação financeira.

Exemplo com alteração técnica:

```text
TÉCNICA V1 → COMERCIAL V1

cliente solicita mudança técnica
        ↓
TÉCNICA V2 → nova COMERCIAL vinculada à Técnica V2
```

Uma versão comercial deve saber exatamente qual versão técnica lhe serviu de base.

### 4.3. Mudança financeira não implica revisão técnica

**CONFIRMADO**

Desconto, negociação financeira ou mudança exclusivamente comercial não deve criar artificialmente uma nova versão técnica.

### 4.4. Mudança técnica com impacto deve refletir na técnica e na comercial

**CONFIRMADO**

Quando o cliente solicita alteração técnica que afeta o custo ou a composição da solução, uma nova elaboração técnica deve ser produzida e, ao ser formalizada, gerar nova versão técnica. A proposta comercial correspondente passa a utilizar essa nova base.

---

## 5. BDI, impostos, margem e leis sociais

### 5.1. Preservar inicialmente a prática atual da FOS

**CONFIRMADO**

Na prática atual da FOS, BDI, impostos e margem são tratados conjuntamente no campo/percentual de BDI aplicado na planilha final.

A V0 não propõe alterar imediatamente esse processo.

O sistema deve conseguir representar fielmente essa prática antes de tentar sofisticá-la.

### 5.2. Possibilidade de evolução futura

**HIPÓTESE V0**

A arquitetura não deve impedir que futuramente o BDI seja decomposto em componentes, caso a FOS decida evoluir o processo.

Essa decomposição futura não é requisito desta V0 e não deve ser imposta ao usuário agora.

### 5.3. Leis sociais não devem ser confundidas com BDI final

**CONFIRMADO**

Algumas composições possuem leis sociais/encargos aplicados à mão de obra. Embora possuam natureza tributária ou de encargos, fazem parte da composição de custo da mão de obra e não devem ser confundidos com o BDI final utilizado na formação do preço.

---

## 6. Dados-base antes da escolha dos blocos

### 6.1. O orçamento começa pelo contexto da obra

**CONFIRMADO**

Antes da escolha dos blocos funcionais, o engenheiro deve informar dados-base do orçamento.

Já identificados nesta V0:

- volume;
- local;
- objeto da obra;
- regime de trabalho.

Outros dados-base poderão ser identificados pela mineração histórica e pelos testes.

### 6.2. Dados-base podem alimentar vários blocos

**CONFIRMADO**

Esses dados formam o contexto comum do orçamento e podem ser utilizados por diversos blocos.

Não se deve duplicar desnecessariamente uma informação que conceitualmente pertence ao orçamento como um todo.

### 6.3. Relações automáticas ainda não homologadas

**PENDENTE DE EVIDÊNCIA**

Ainda é prematuro determinar todas as relações automáticas entre dados-base e blocos ou entre os próprios blocos.

Essas relações deverão surgir da combinação de:

1. mineração histórica;
2. análise funcional das planilhas;
3. implementação experimental futura;
4. testes unitários e de domínio;
5. uso real pelos engenheiros.

---

## 7. Composição dinâmica por blocos

### 7.1. Engenheiro escolhe a composição

**CONFIRMADO**

O orçamento técnico deve ser composto dinamicamente por blocos selecionados pelo engenheiro.

Enquanto o orçamento estiver em elaboração, ele poderá voltar à seleção e incluir, remover ou reconfigurar blocos.

A estrutura somente será congelada quando uma versão técnica for formalizada.

### 7.2. Não homologar taxonomia prematuramente

**PENDENTE DE EVIDÊNCIA**

A lista final de tipos de bloco ainda depende da mineração histórica.

Nomes de abas não devem ser automaticamente tratados como tipos de bloco. Abas com nomes diferentes podem representar o mesmo conceito, e abas com nomes iguais podem ter comportamentos distintos.

### 7.3. Múltiplas instâncias do mesmo tipo de bloco

**CONFIRMADO**

O mesmo orçamento deve permitir múltiplas instâncias independentes de um mesmo tipo de bloco.

Exemplos:

```text
DRAGAGEM
   ├── Draga 1
   └── Draga 2
```

```text
CENTRÍFUGA
   ├── Centrífuga 1
   └── Centrífuga 2
```

Cada instância poderá possuir equipamentos, parâmetros, equipe, produtividade, duração e custos próprios.

---

## 8. Blocos e componentes já esclarecidos

### 8.1. Mobilização

**CONFIRMADO**

Mobilização é tratada como bloco próprio.

Ela pode exigir recursos e quantitativos de mão de obra diferentes daqueles necessários durante a operação de Dragagem, Centrífuga ou outras etapas.

### 8.2. Mão de obra

**CONFIRMADO**

Mão de obra não deve ser tratada como um único bloco global do orçamento.

Cada etapa/bloco pode possuir sua própria composição e quantitativo de mão de obra.

Exemplo: a equipe necessária para Mobilização pode ser diferente da equipe necessária para Dragagem ou operação de Centrífuga.

**HIPÓTESE V0:** mão de obra tende a ser melhor representada como componente reutilizável dentro das etapas/blocos, e não como bloco independente universal.

### 8.3. Combustível

**CONFIRMADO**

No domínio de Dragagem, combustível faz parte da composição do bloco de Dragagem e não deve ser tratado, por padrão, como bloco independente.

### 8.4. Tubulação

**CONFIRMADO**

Tubulação faz parte do bloco de Dragagem na prática atual identificada e não é tratada como bloco independente.

### 8.5. Outras fronteiras

**PENDENTE DE EVIDÊNCIA**

A mineração histórica deverá indicar se energia, manutenção, destinação, polímero, bombeamento, batimetria e outros elementos devem ser blocos, componentes internos, dados compartilhados ou assumir papéis diferentes conforme o cenário.

---

## 9. Dados compartilhados e relações entre blocos

### 9.1. Compartilhamento pelo dado

**CONFIRMADO**

Alguns dados podem estar interligados e ser utilizados por vários blocos.

A preferência inicial é permitir que a ligação aconteça pelo dado comum, evitando criar dependências rígidas entre blocos antes de haver evidência de que elas são realmente necessárias.

### 9.2. Dependências estruturais entre blocos

**PENDENTE DE EVIDÊNCIA**

Não se deve presumir nesta V0 que determinados blocos obrigatoriamente exigem outros blocos.

A existência de dependências diretas deverá ser demonstrada pela prática histórica e validada pelos testes.

### 9.3. Papel dos testes na descoberta do domínio

**HIPÓTESE V0**

Os futuros testes não servirão apenas para verificar código. Casos reais transformados em testes poderão revelar regras de domínio que hoje ainda não são explícitas.

Cenários como múltiplas dragas, múltiplas centrífugas, equipes diferentes por etapa, regimes de trabalho distintos e compartilhamento de volumes/premissas deverão ajudar a separar regra estrutural de mera recorrência histórica.

---

## 10. Dados Mestre

### 10.1. Fonte de preenchimento e aceleração

**CONFIRMADO**

Dados institucionais da FOS devem ser mantidos em cadastros próprios no módulo Dados sempre que fizer sentido.

Exemplos candidatos incluem equipamentos, dragas, serviços, insumos, unidades, clientes e outros catálogos que a mineração histórica venha a justificar.

Esses cadastros existem para acelerar o trabalho e fornecer referências consistentes.

### 10.2. Dados Mestre não bloqueiam o engenheiro

**CONFIRMADO**

Nenhum valor deve se tornar imutável dentro do orçamento apenas porque veio de uma tabela-base.

O engenheiro pode alterar o valor para representar a condição específica da obra.

### 10.3. Atualização da base é ação separada

**CONFIRMADO**

Uma alteração feita pelo engenheiro dentro de um orçamento não deve atualizar automaticamente o cadastro Mestre.

Uma condição excepcional de uma obra não pode alterar silenciosamente a referência institucional utilizada em todos os novos orçamentos.

A manutenção da base deve continuar sendo uma ação administrativa controlada.

---

## 11. Salvamento e memória histórica dos valores

### 11.1. O orçamento salvo possui valores próprios

**CONFIRMADO**

Ao salvar os dados do orçamento, os valores utilizados passam a pertencer ao próprio orçamento.

O orçamento não deve depender de uma consulta futura à tabela-base para reconstruir seu cálculo.

Exemplo:

```text
Base Mestre hoje:
Draga X → consumo = 70 L/h

Orçamento A salvo:
consumo utilizado = 70 L/h

Base Mestre atualizada depois:
Draga X → consumo = 75 L/h

Orçamento A continua:
consumo utilizado = 70 L/h
```

Novos orçamentos podem receber 75 L/h como valor inicial, mas o orçamento histórico não é alterado.

### 11.2. Salvamento como snapshot funcional

**CONFIRMADO**

O snapshot funcional ocorre naturalmente pelo salvamento dos valores próprios do orçamento.

A formalização posterior congela o conjunto de dados salvo como uma versão técnica formal.

### 11.3. Referência de origem é metadado, não dependência de cálculo

**HIPÓTESE V0**

Pode ser útil preservar qual cadastro ou fonte originou determinado valor para fins de auditoria e inteligência histórica.

Entretanto, depois de salvo, o cálculo deve usar o valor pertencente ao orçamento e não voltar à tabela Mestre para obter o valor atual.

---

## 12. Proveniência dos valores

### 12.1. Registrar de onde veio sem limitar seu uso

**HIPÓTESE V0**

Para valores relevantes, o sistema poderá registrar proveniência, por exemplo:

- cadastro/base Mestre;
- digitado/alterado pelo engenheiro;
- sugerido a partir do histórico;
- calculado/derivado.

A proveniência serve para auditoria, explicabilidade e inteligência futura. Ela não deve criar lock operacional.

### 12.2. Sugestão histórica não é decisão automática

**CONFIRMADO**

O histórico poderá futuramente sugerir valores, faixas ou casos semelhantes, mas o engenheiro continua responsável pela escolha do valor efetivamente utilizado.

Exemplo futuro possível:

```text
Referência Mestre: 70 L/h
Histórico semelhante: 68–82 L/h
Valor utilizado pelo engenheiro: 78 L/h
```

O sistema informa; o engenheiro decide.

---

## 13. Bloco coringa — Locação de Equipamentos

### 13.1. Necessidade identificada

**CONFIRMADO**

A FOS nem sempre utiliza equipamento próprio. Equipamentos podem ser locados de fornecedores, desde uma draga com impacto relevante no orçamento até uma ferramenta/máquina simples, como uma furadeira.

O sistema precisa representar esses cenários sem exigir a criação de um bloco específico para cada tipo possível de equipamento locado.

### 13.2. Bloco genérico candidato

**HIPÓTESE V0 — forte, porém necessita teste**

Criar um bloco genérico de **Locação de Equipamentos**, parametrizável conforme a complexidade do caso.

Campos/capacidades candidatos, ainda não homologados:

- descrição/tipo do equipamento;
- fornecedor;
- quantidade;
- unidade de cobrança;
- período de locação;
- valor unitário;
- operador incluso ou não;
- combustível incluso ou não;
- manutenção inclusa ou não;
- frete/mobilização associada;
- seguros/taxas quando aplicáveis;
- observações e condições específicas.

Um caso simples poderá utilizar poucos campos. Um caso complexo poderá exigir uma composição maior.

### 13.3. Relação com blocos operacionais

**PENDENTE DE EVIDÊNCIA**

Não está decidido se uma locação de grande equipamento, como uma draga, substitui parte de um bloco operacional ou apenas fornece um custo/recurso utilizado pelo bloco de Dragagem.

A resposta deve ser obtida pela análise histórica e por testes de cenários reais.

---

## 14. Inteligência histórica futura

### 14.1. Histórico como assistência

**HIPÓTESE V0**

A preservação estruturada dos valores poderá permitir que, no futuro, o sistema apresente informações como:

- valores utilizados anteriormente em determinada região;
- faixas de produtividade observadas;
- custos históricos de equipamentos ou serviços;
- combinações frequentes de blocos;
- casos semelhantes ao orçamento atual.

### 14.2. Histórico não vira regra automática

**CONFIRMADO**

Essas informações devem ser apresentadas como apoio à decisão, nunca como substituição silenciosa do julgamento do engenheiro.

---

## 15. Fluxo conceitual V0

```text
NOVO ORÇAMENTO
      ↓
DADOS-BASE DA OBRA
(volume, local, objeto, regime, ...)
      ↓
ESCOLHA DOS BLOCOS PELO ENGENHEIRO
      ↓
INSTÂNCIAS DOS BLOCOS
(1 ou várias dragas, centrífugas etc.)
      ↓
PREENCHIMENTO
├── valores vindos de Dados Mestre
├── valores digitados/alterados
├── dados compartilhados
├── sugestões históricas futuras
└── valores calculados
      ↓
SALVAR
(valores tornam-se próprios do orçamento)
      ↓
REVISÕES INTERNAS LIVRES
      ↓
CONCLUIR / FORMALIZAR
      ↓
VERSÃO TÉCNICA CONGELADA
      ↓
FORMAÇÃO / PROPOSTA COMERCIAL
      ↓
VERSÕES COMERCIAIS INDEPENDENTES
```

---

## 16. Decisões deliberadamente adiadas

**PENDENTE DE EVIDÊNCIA**

Esta V0 deliberadamente não define:

1. taxonomia final de blocos;
2. todos os campos de cada bloco;
3. fórmulas definitivas;
4. dependências obrigatórias entre blocos;
5. quais elementos são sempre blocos versus componentes internos;
6. estrutura definitiva de persistência/banco;
7. interface definitiva;
8. mecanismo definitivo de sugestões históricas;
9. decomposição futura do BDI;
10. regras completas de estados e aprovações;
11. integração futura com resultado comercial da concorrência;
12. integração futura com execução e custos realizados.

Esses pontos não são lacunas acidentais. Permanecem abertos para evitar que a arquitetura seja fechada antes de existir evidência suficiente.

---

## 17. Questões que a mineração do Work deve ajudar a responder

A auditoria funcional histórica deverá fornecer evidência para perguntas como:

- quais blocos realmente existem de forma recorrente;
- quais nomes diferentes representam o mesmo conceito;
- quais blocos possuem variantes relevantes;
- quais campos são Mestre, Contextual, Derivado ou Histórico;
- quais dados são compartilhados entre blocos;
- quais relações entre blocos são obrigatórias e quais são apenas comuns;
- quais componentes aparecem dentro de vários blocos;
- como mão de obra varia por etapa;
- como equipamentos próprios e locados são tratados historicamente;
- como diferentes dragas/centrífugas coexistem no mesmo orçamento;
- quais dados-base aparecem transversalmente;
- onde fórmulas dependem de parâmetros de outros blocos;
- quais valores precisam de preservação histórica especial;
- quais práticas são exceções legítimas e não erros.

---

## 18. Papel dos futuros testes

**HIPÓTESE V0**

Quando houver implementação, os testes deverão usar cenários representativos do domínio real, não apenas casos artificiais simples.

Casos importantes já identificados para futura validação incluem:

- orçamento com uma única draga;
- orçamento com duas dragas independentes;
- múltiplas centrífugas;
- Mobilização com equipe diferente da operação;
- Dragagem com combustível e tubulação internos;
- alteração livre de valor originalmente vindo da base;
- base Mestre alterada após orçamento salvo;
- equipamento locado simples;
- draga locada em cenário operacional complexo;
- revisão técnica que gera nova versão;
- negociação exclusivamente financeira que gera nova versão comercial sem alterar a técnica;
- inclusão de novo bloco antes da formalização;
- abandono de uma revisão ainda não formalizada.

Os testes poderão revelar novas relações de domínio. Quando isso ocorrer, a documentação conceitual deverá evoluir junto com a evidência.

---

## 19. Relação com a evolução futura

Esta V0 preserva espaço para uma arquitetura futura mais ampla, sem trazê-la para o escopo atual.

Conceitualmente, o conhecimento poderá futuramente formar uma cadeia como:

```text
ORÇADO → VENDIDO → EXECUTADO → REALIZADO
```

A prioridade atual permanece no domínio de **Orçamentos**.

A existência dessa direção futura apenas reforça a necessidade de identidade permanente, versões rastreáveis, valores históricos próprios, proveniência e separação entre Técnica e Comercial.

---

## 20. Síntese da V0

A V0 parte de uma visão simples:

> O Novo Orçamentos deve organizar e acelerar o conhecimento da FOS sem retirar do engenheiro a liberdade necessária para representar uma obra real.

O sistema fornece estrutura, dados-base, cadastros, histórico, cálculos e assistência. O engenheiro escolhe os blocos, ajusta os valores e responde pela solução técnica.

O histórico deve permanecer íntegro. Uma base atualizada não reescreve um orçamento salvo. Uma negociação comercial não reescreve a técnica. Uma nova necessidade do cliente não apaga a versão anterior.

E, principalmente, esta V0 não tenta responder prematuramente aquilo que a mineração histórica e os testes ainda precisam ensinar.
