# DECISÕES DE DOMÍNIO — ORÇAMENTOS FOS — PÓS-CHECKPOINT 1

**Data:** 01/09/2026  
**Natureza:** interpretação de domínio posterior à mineração histórica  
**Base:** `CHECKPOINT 1 — Lote das 12 Unidades de Orçamentos FOS`  
**Status:** decisões parciais consolidadas; continuar entrevista de domínio antes de homologar o modelo

## 1. Finalidade

Este documento registra a interpretação de domínio construída após o Checkpoint 1. Ele não substitui o checkpoint, que permanece como evidência histórica da mineração. Aqui são separados: fatos observados nos arquivos, regras de negócio confirmadas por Fabio e hipóteses/nomenclaturas ainda pendentes.

Princípio: preservar a flexibilidade real da FOS, aumentar rastreabilidade e evitar transformar hábitos ou limitações do Excel em regras artificiais do novo sistema.

## 2. Evidências do Checkpoint 1

- Cenário técnico, revisão da memória, rodada comercial, proposta emitida, preço calculado/negociado/apresentado e status contratual divergiram em obras reais; não devem ser reduzidos a um único número de revisão.
- O histórico sustenta um orçamento composto por blocos funcionais variáveis, e não um modelo único baseado em nomes de abas.
- Snapshot é estrutural: valores, fórmulas, unidades, responsabilidades e referências usadas precisam ser preservados.
- Memória de cálculo e proposta emitida podem divergir e precisam de ponte auditável.
- Unidades e bases físicas não são intercambiáveis: m³, m³ in situ, m³ desaguado, t úmida, t seca e tSS carregam significado de negócio.
- BDI, margem, markup, tributos, descontos e overrides apareceram de formas distintas e não devem ser confundidos com engenharia.
- Templates históricos apresentaram resíduos, `#REF!`, contaminações e mudanças de base sem rastreabilidade; o novo sistema deve impedir ambiguidades silenciosas.

## 3. Decisões confirmadas por Fabio

### 3.1 Orçamento como unidade independente

**CONFIRMADO POR FABIO**

Cada orçamento é um processo único e independente. Mesmo quando duas alternativas nascem da mesma necessidade do cliente e compartilham cliente, local, volume ou descrição semelhante, elas devem ser tratadas como orçamentos separados.

Exemplo: uma solução com dragagem + bags e outra com dragagem + centrífuga são dois orçamentos distintos, cada um com seu próprio ID, elaboração, fechamento, versões formais e histórico.

Não deve existir, como regra de domínio, orçamento-pai, grupo obrigatório de cenários ou vínculo estrutural entre alternativas.

A palavra **cenário** pode continuar sendo usada na linguagem de engenharia para descrever uma alternativa estudada, mas não precisa existir como entidade estrutural filha do orçamento no novo sistema.

### 3.2 Duplicar orçamento

**CONFIRMADO POR FABIO**

Deve existir uma função de produtividade **Duplicar Orçamento**.

A duplicação cria um novo orçamento independente copiando o conteúdo do orçamento de origem naquele instante. O objetivo é economizar tempo quando uma nova alternativa reutiliza boa parte dos dados existentes.

Regra central:

> **Duplicar copia conteúdo, não cria vínculo.**

Após a duplicação, original e cópia evoluem de forma totalmente independente. Alterações em um não afetam o outro.

### 3.3 Elaboração do orçamento

**CONFIRMADO POR FABIO**

Antes da formalização, o orçamento é vivo e iterativo. Hoje a solução é concebida inicialmente em conversas/reuniões e depois construída no Excel. Durante essa construção, engenharia e aspectos financeiros são populados e refinados conjuntamente.

O novo sistema não deve impor um processo artificial em que toda a técnica precise ser encerrada antes de qualquer informação financeira. Alterações enquanto a proposta ainda não foi fechada são parte normal da elaboração e não constituem versões formais.

### 3.4 Relação técnico-financeira

**CONFIRMADO POR FABIO**

A composição técnico-financeira é iterativa: equipamentos, produção, prazo, efetivo, consumos e premissas técnicas alimentam custos, e a leitura econômica pode provocar nova reflexão sobre a solução.

Apesar dessa integração, decisões puramente comerciais não devem adulterar artificialmente a engenharia para justificar o preço ofertado. Quando a solução técnica está conceitualmente aprovada e a discussão passa para a proposta comercial, ajustes posteriores são financeiros/comerciais, salvo se uma nova necessidade técnica efetivamente surgir.

### 3.5 Exercícios econômicos internos

**CONFIRMADO POR FABIO**

Podem ser feitos vários exercícios econômicos antes do fechamento, testando margem, BDI, descontos, preço-alvo, estratégia e outras condições. Esses exercícios internos não são versões formais e não devem poluir a numeração formal.

### 3.6 Fechar Proposta

**CONFIRMADO POR FABIO**

Deve existir um marco explícito ao final da elaboração: **Fechar Proposta**. O ato significa que a proposta foi revisada, pensada e considerada pronta para envio ao cliente.

Até esse marco, o conteúdo permanece editável. No fechamento, o sistema deve gerar um snapshot integral da configuração adotada.

**Fechar Proposta e enviar ao cliente pertencem ao mesmo marco de negócio.** A formalização não depende de um segundo evento de envio. Ao fechar, a proposta já é considerada final para fins de versionamento; o envio é consequência operacional desse fechamento.

Portanto, o clique em **Fechar Proposta** deve imediatamente:

- congelar o snapshot completo;
- criar a versão formal;
- torná-la a versão vigente da cadeia;
- impedir edição direta dessa versão;
- deixá-la pronta para geração/saída e envio ao cliente.

Não deve existir um estado de negócio intermediário do tipo `fechada, mas ainda não formal`. Se houver qualquer alteração após o fechamento, ela deverá ocorrer em nova elaboração/revisão derivada da versão formal vigente.

### 3.7 Versão formal e imutabilidade

**CONFIRMADO POR FABIO**

A versão formal nasce no ato de **Fechar Proposta**. Uma versão formal deve ser imutável. A preservação é necessária também para comparação futura entre versões.

Alterações posteriores devem ocorrer em nova elaboração derivada da versão anterior, nunca pela sobrescrita da versão já formalizada.

### 3.8 Revisão e vigência

**CONFIRMADO POR FABIO**

Revisão significa nova proposta completa, e não apenas um delta ou aditivo. Mesmo quando o gatilho é um acréscimo aparentemente simples, a nova proposta pode conter alterações mais amplas.

Quando uma nova versão formal é emitida, ela se torna a proposta vigente. A versão anterior torna-se histórica/legacy, permanecendo imutável, consultável e comparável.

### 3.9 Proposta técnica e proposta comercial

**CONFIRMADO POR FABIO**

Na prática da FOS existe proposta técnica e, após sua definição/finalização, parte-se para a proposta comercial. Entretanto, a construção da composição no Excel não ocorre como dois silos rígidos: a solução técnica é construída ao mesmo tempo em que seus efeitos financeiros são populados.

O novo sistema deve distinguir informação técnica, custo e decisão comercial sem obrigar dois gates burocráticos durante toda a elaboração. O verdadeiro cadeado do processo é o fechamento/formalização.

### 3.10 Catálogo principal de blocos

**CONFIRMADO POR FABIO**

O menu inicial do orçamento deve funcionar como um **cardápio de blocos funcionais macro**, no nível conceitual das grandes abas/etapas existentes nos orçamentos atuais.

Exemplos: Mobilização, Dragagem, Canteiro, Célula de Desaguamento, Centrífuga, Bags, Batimetria e outros conceitos gerais que conduzem aos componentes internos necessários.

Equipamentos, mão de obra, combustível, tubulação, insumos e outros recursos menores pertencem à composição interna desses blocos, e não precisam ocupar o menu principal como regra geral.

Casos excepcionais podem justificar a criação de um novo bloco específico no catálogo. Exemplo: um serviço formado apenas por escavadeira pode receber uma nova entrada se essa necessidade efetivamente surgir.

O objetivo não é prever todas as exceções desde o início, e sim manter um catálogo suficientemente fluido para absorvê-las quando necessário.

### 3.11 Catálogo fluido e administrável

**CONFIRMADO POR FABIO**

O catálogo de blocos não deve ser fixo em código. Deve ser administrável por usuários com permissão adequada, permitindo incluir, alterar, ordenar e retirar opções de uso corrente.

Para preservar histórico:

- bloco nunca utilizado pode ser excluído fisicamente se tiver sido cadastrado por engano;
- bloco já utilizado em qualquer orçamento não deve ser apagado: deve ser **inativado**;
- bloco inativado deixa de aparecer no cardápio de novos orçamentos, mas permanece preservado para históricos e snapshots existentes.

Alterações no catálogo não devem modificar silenciosamente orçamentos já existentes ou em elaboração.

### 3.12 Seleção dos blocos pelo engenheiro

**CONFIRMADO POR FABIO**

A definição de quais blocos compõem o orçamento é responsabilidade do engenheiro. O conhecimento da solução está no profissional; o sistema deve disponibilizar as peças necessárias e permitir que ele escolha o que deseja utilizar.

O APP não deve decidir automaticamente quais blocos um orçamento precisa conter com base em um tipo pré-definido de orçamento.

Campos técnicos obrigatórios devem decorrer da estrutura dos blocos selecionados, e não de um formulário inicial excessivamente rígido.

### 3.13 Múltiplas instâncias do mesmo bloco

**CONFIRMADO POR FABIO**

Um mesmo bloco de catálogo pode aparecer mais de uma vez dentro do mesmo orçamento.

Exemplo: uma obra pode utilizar simultaneamente uma draga hidráulica e uma draga elétrica, ambas dentro do conceito de Dragagem, porém com equipamentos, produções, consumos, jornadas e condições operacionais diferentes.

Portanto, o modelo deve distinguir:

- **Bloco de Catálogo:** conceito reutilizável, por exemplo `Dragagem`;
- **Bloco do Orçamento:** instância concreta daquele conceito dentro de um orçamento.

Um orçamento deve aceitar N instâncias independentes do mesmo bloco. Cada instância possui seus próprios dados e pode receber um nome operacional para facilitar leitura, sem alterar o conceito do catálogo.

Essa estrutura deve permitir atender particularidades futuras sem multiplicar desnecessariamente os tipos de bloco no catálogo.

### 3.14 Diretriz de UX para a V1

**CONFIRMADO POR FABIO**

A V1 deve priorizar adoção, familiaridade e baixa carga cognitiva. Os usuários de orçamento são profissionais experientes, habituados à forma atual de trabalhar no Excel; portanto, o novo módulo não deve exigir que aprendam uma nova metodologia de orçamento ao mesmo tempo em que aprendem uma nova ferramenta.

A estrutura interna de cada bloco funcional deve partir do que foi capturado pelo Work nas abas históricas correspondentes. O objetivo inicial é converter células, abas, fórmulas e parâmetros em dados estruturados no APP, preservando a lógica funcional conhecida.

Regra de decisão da V1:

> **Quando houver dúvida entre uma solução mais sofisticada e uma solução mais familiar ao Excel atual, deve prevalecer a solução mais familiar, desde que ela não comprometa a arquitetura futura.**

Princípio complementar:

> **A arquitetura pode ser nova sem a experiência parecer nova.**

O critério de sucesso é que um engenheiro habituado aos Excel atuais consiga elaborar um orçamento no APP com pouca ou nenhuma explicação adicional.

A evolução deve ser progressiva:

- **V1:** adoção e equivalência funcional;
- **V2:** simplificação e automação;
- **V3:** inteligência, sugestões e otimização baseadas no histórico e no uso real.

Essa diretriz é detalhada em `DIRETRIZ_UX_V1_ORCAMENTOS.md`.

## 4. Fluxo conceitual refinado

1. **Novo Orçamento**.
2. Identificação administrativa mínima para criação/localização do processo.
3. Seleção, pelo engenheiro, dos blocos macro necessários no catálogo.
4. Criação de uma ou mais instâncias dos blocos escolhidos, quando necessário.
5. Elaboração técnico-financeira iterativa do orçamento.
6. Refinamento de premissas, produção, recursos, custos e condições.
7. Exercícios econômicos/comerciais internos, quando necessários.
8. **FECHAR PROPOSTA** — marco formal; envio é consequência operacional.
9. Snapshot integral + criação da **Versão Formal V1**.
10. **Versão Formal V1** — imutável e vigente.
11. Se houver nova rodada: nova elaboração derivada da versão vigente.
12. **FECHAR PROPOSTA** novamente.
13. **Versão Formal V2** — imutável e vigente; V1 passa a histórica/legacy.

Alternativas de solução que precisem ser estudadas separadamente devem nascer como **outros orçamentos independentes**, podendo ser criados por duplicação para reaproveitamento de conteúdo.

## 5. Refinamento da hipótese de versionamento do Checkpoint 1

O Checkpoint 1 propôs, como normalização candidata:

`Orçamento → Cenário → Revisão técnica → Rodada comercial → Documento emitido`

Após a entrevista de domínio, essa sequência **não deve ser homologada literalmente**.

Hipótese refinada atual:

`Orçamento → Elaboração técnico-financeira → Fechar Proposta / Versão Formal`

O conceito de cenário não precisa ser uma entidade filha do orçamento. Quando uma alternativa técnica precisa ser estudada como processo próprio, ela constitui outro orçamento independente.

Histórico de edição, simulações e exercícios econômicos podem existir dentro da elaboração, mas não devem ser confundidos com versões formais. A numeração formal representa propostas efetivamente fechadas. O envio ao cliente não cria uma nova etapa de versionamento: é consequência do fechamento.

## 6. Regras candidatas de implementação futura — ainda não especificação técnica

- Tratar cada orçamento como processo soberano e independente.
- Não criar vínculo estrutural obrigatório entre orçamentos semelhantes.
- Disponibilizar **Duplicar Orçamento** como ferramenta de produtividade, sem relação viva entre origem e cópia.
- Disponibilizar catálogo administrável de blocos funcionais macro.
- Permitir inclusão, edição, ordenação e inativação de blocos do catálogo.
- Impedir exclusão física de bloco que já possua uso histórico.
- Permitir ao engenheiro selecionar livremente quais blocos compõem cada orçamento.
- Permitir N instâncias do mesmo bloco dentro do mesmo orçamento.
- Manter dados independentes por instância de bloco.
- Permitir nome operacional por instância para facilitar identificação.
- Manter técnica, custos e comercial semanticamente distinguíveis, mas interoperáveis durante a elaboração.
- Permitir múltiplas simulações econômicas internas sem criar versões formais.
- Disponibilizar ação explícita **Fechar Proposta**.
- No fechamento, congelar snapshot completo: blocos, instâncias, campos, valores, unidades, fórmulas/dependências, proveniência, preços, condições e documento/saída aplicável.
- O próprio fechamento cria a versão formal; não exigir confirmação posterior de envio para formalizá-la.
- Impedir edição direta de versão formal.
- Criar revisão por derivação/cópia controlada da versão vigente.
- Manter somente uma versão formal vigente por cadeia de revisão; anteriores ficam históricas/legacy.
- Preservar na V1 a linguagem, a sequência mental e a anatomia funcional reconhecível dos Excel atuais.
- Derivar a anatomia inicial dos blocos da mineração histórica já executada pelo Work.
- Evitar redesenho conceitual ou de UX que não seja necessário para a V1.
- Permitir evolução posterior sem obrigar ruptura de uso na primeira versão.

## 7. Pontos ainda pendentes / gray areas

- Nomenclatura final e fronteiras dos blocos funcionais do catálogo.
- Quais blocos serão núcleo obrigatório e quais serão opcionais/instanciáveis.
- Responsabilidades e estados explícitos por componente: FOS, cliente, terceiro, opcional, não aplicável, zero etc.
- Granularidade do histórico de edição/autosave durante a elaboração.
- Regras exatas para comparação V1 × V2 e quais diferenças destacar.
- Tratamento de múltiplos documentos emitidos associados à mesma versão formal, caso necessário.
- Governança de quem pode fechar/criar revisão e quais aprovações internas serão necessárias.
- Nomenclatura final para preço calculado, preço comercial adotado, desconto/override e preço apresentado.

### Gray areas encerradas nesta rodada

- ~~Relação entre **Fechar Proposta** e envio efetivo ao cliente.~~ **ENCERRADA:** são o mesmo marco de negócio. O fechamento cria a versão formal; o envio é consequência operacional.
- ~~Fronteira estrutural **Orçamento × Cenário**.~~ **ENCERRADA:** não há entidade cenário filha; alternativas estudadas separadamente são orçamentos independentes.
- ~~Granularidade do cardápio inicial.~~ **ENCERRADA:** blocos funcionais macro equivalentes conceitualmente às grandes abas/etapas atuais.
- ~~Exclusão de blocos já utilizados.~~ **ENCERRADA:** inativar para preservar histórico.
- ~~Múltiplas ocorrências do mesmo bloco.~~ **ENCERRADA:** o mesmo bloco de catálogo pode gerar N instâncias independentes dentro de um orçamento.
- ~~Anatomia inicial dos blocos e ruptura de UX na V1.~~ **ENCERRADA:** partir das abas históricas capturadas pelo Work e preservar forte familiaridade com o Excel atual.

## 8. Decisões que não devem ser tomadas ainda

- Não homologar a taxonomia dos blocos com base apenas no primeiro lote histórico.
- Não copiar cegamente nomes de abas históricas como entidades definitivas; usá-las como referência funcional para a V1.
- Não criar workflow rígido de `aprovar técnica → liberar comercial`.
- Não tratar cada edição interna como revisão formal.
- Não assumir que proposta mais barata é automaticamente a escolhida.
- Não reinventar a metodologia de orçamento na V1.
- Não antecipar automações ou inteligência de V2/V3 se isso aumentar a carga cognitiva da V1.
- Não iniciar implementação antes de consolidar as gray areas que afetam o modelo de dados e o fluxo principal.

## 9. Estado deste registro

Este documento consolida as decisões discutidas após o Checkpoint 1 até este momento. Deve permanecer separado do relatório de mineração histórica. Novas decisões de domínio devem ser acrescentadas de forma rastreável, sem reescrever silenciosamente as evidências originais.

A diretriz de UX da V1 está formalizada em documento próprio para servir de critério de produto e orientar a próxima missão do Work.

**Status:** DECISÕES PARCIAIS CONSOLIDADAS — PRONTO PARA NOVA MISSÃO DIRIGIDA DO WORK, SEM IMPLEMENTAÇÃO AINDA.
