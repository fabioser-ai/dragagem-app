# DECISÕES DE DOMÍNIO — ORÇAMENTOS FOS — PÓS-CHECKPOINT 1

**Data:** 31/08/2026  
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

### 3.1 Cenário

**CONFIRMADO POR FABIO**

Cenário é uma alternativa de solução para atender ao mesmo problema/objeto do cliente. Pode decorrer de disponibilidade financeira, limitação de área, restrição técnica, preferência/confiança do cliente em determinada tecnologia ou da necessidade de explorar alternativas quando o cliente ainda não sabe qual solução deseja.

Na prática, a solução mais econômica tende a vencer na grande maioria dos casos, mas custo não é regra automática: critérios técnicos, físicos ou preferência do cliente podem prevalecer. O sistema não deve selecionar automaticamente o cenário vencedor pelo menor preço; a decisão permanece humana.

### 3.2 Elaboração do orçamento

**CONFIRMADO POR FABIO**

Antes da formalização, o orçamento é vivo e iterativo. Hoje a solução é concebida inicialmente em conversas/reuniões e depois construída no Excel. Durante essa construção, engenharia e aspectos financeiros são populados e refinados conjuntamente.

O novo sistema não deve impor um processo artificial em que toda a técnica precise ser encerrada antes de qualquer informação financeira. Alterações enquanto a proposta ainda não foi fechada/enviada são parte normal da elaboração e não constituem versões formais.

### 3.3 Relação técnico-financeira

**CONFIRMADO POR FABIO**

A composição técnico-financeira é iterativa: equipamentos, produção, prazo, efetivo, consumos e premissas técnicas alimentam custos, e a leitura econômica pode provocar nova reflexão sobre a solução.

Apesar dessa integração, decisões puramente comerciais não devem adulterar artificialmente a engenharia para justificar o preço ofertado. Quando a solução técnica está conceitualmente aprovada e a discussão passa para a proposta comercial, ajustes posteriores são financeiros/comerciais, salvo se uma nova necessidade técnica efetivamente surgir.

### 3.4 Exercícios econômicos internos

**CONFIRMADO POR FABIO**

Podem ser feitos vários exercícios econômicos antes do envio ao cliente, testando margem, BDI, descontos, preço-alvo, estratégia e outras condições. Esses exercícios internos não são versões formais e não devem poluir a numeração formal enviada ao cliente.

### 3.5 Fechar Proposta

**CONFIRMADO POR FABIO**

Deve existir um marco explícito ao final da elaboração: **Fechar Proposta**. O ato significa que a proposta foi revisada, pensada e considerada pronta para envio ao cliente.

Até esse marco, o conteúdo permanece editável. No fechamento, o sistema deve gerar um snapshot integral da configuração adotada.

### 3.6 Versão formal e imutabilidade

**CONFIRMADO POR FABIO**

A versão formal nasce quando a proposta é fechada para envio ao cliente. Uma versão formal deve ser imutável. A preservação é necessária também para comparação futura entre versões.

Alterações posteriores devem ocorrer em nova elaboração derivada da versão anterior, nunca pela sobrescrita da versão já formalizada.

### 3.7 Revisão e vigência

**CONFIRMADO POR FABIO**

Revisão significa nova proposta completa, e não apenas um delta ou aditivo. Mesmo quando o gatilho é um acréscimo aparentemente simples, a nova proposta pode conter alterações mais amplas.

Quando uma nova versão formal é emitida, ela se torna a proposta vigente. A versão anterior torna-se histórica/legacy, permanecendo imutável, consultável e comparável.

### 3.8 Proposta técnica e proposta comercial

**CONFIRMADO POR FABIO**

Na prática da FOS existe proposta técnica e, após sua definição/finalização, parte-se para a proposta comercial. Entretanto, a construção da composição no Excel não ocorre como dois silos rígidos: o cenário técnico é construído ao mesmo tempo em que seus efeitos financeiros são populados.

O novo sistema deve distinguir informação técnica, custo e decisão comercial sem obrigar dois gates burocráticos durante toda a elaboração. O verdadeiro cadeado do processo é o fechamento/formalização para envio ao cliente.

## 4. Fluxo conceitual refinado

1. Necessidade / objeto do cliente.
2. Criação de um ou mais cenários de solução.
3. Elaboração técnico-financeira iterativa de cada cenário.
4. Refinamento de premissas, produção, recursos, custos e condições.
5. Exercícios econômicos/comerciais internos, quando necessários.
6. Escolha da configuração a apresentar.
7. **FECHAR PROPOSTA**.
8. Snapshot integral.
9. **Versão Formal V1** — imutável e vigente.
10. Se houver nova rodada: nova elaboração derivada da versão vigente.
11. **FECHAR PROPOSTA** novamente.
12. **Versão Formal V2** — imutável e vigente; V1 passa a histórica/legacy.

## 5. Refinamento da hipótese de versionamento do Checkpoint 1

O Checkpoint 1 propôs, como normalização candidata:

`Orçamento → Cenário → Revisão técnica → Rodada comercial → Documento emitido`

Após a entrevista de domínio, essa sequência **não deve ser homologada literalmente**.

Hipótese refinada atual:

`Orçamento → Cenário → Elaboração técnico-financeira → Fechamento → Versão Formal`

Histórico de edição, simulações e exercícios econômicos podem existir dentro da elaboração, mas não devem ser confundidos com versões formais. A numeração formal representa propostas efetivamente fechadas para envio.

## 6. Regras candidatas de implementação futura — ainda não especificação técnica

- Permitir múltiplos cenários dentro de um mesmo orçamento.
- Permitir combinações distintas de blocos, premissas, equipamentos, produção, custos e condições por cenário.
- Manter técnica, custos e comercial semanticamente distinguíveis, mas interoperáveis durante a elaboração.
- Permitir múltiplas simulações econômicas internas sem criar versões formais.
- Disponibilizar ação explícita **Fechar Proposta**.
- No fechamento, congelar snapshot completo: blocos, campos, valores, unidades, fórmulas/dependências, proveniência, preços, condições e documento/saída aplicável.
- Impedir edição direta de versão formal.
- Criar revisão por derivação/cópia controlada da versão vigente.
- Manter somente uma versão formal vigente por cadeia de revisão; anteriores ficam históricas/legacy.
- Permitir comparação entre versões, idealmente mostrando alterações técnicas, quantitativas, econômicas e comerciais.
- Não usar menor preço como decisão automática de cenário.
- Não alterar premissas técnicas apenas para forçar a composição a coincidir com decisão comercial.

## 7. Pontos ainda pendentes / gray areas

- Nomenclatura final e fronteiras dos blocos funcionais do catálogo.
- Quais blocos serão núcleo obrigatório e quais serão opcionais/instanciáveis.
- Como representar formalmente os motivos/restrições de um cenário.
- Granularidade do histórico de edição/autosave durante a elaboração.
- Regras exatas para comparação V1 × V2 e quais diferenças destacar.
- Relação entre **Fechar Proposta** e registro do envio efetivo ao cliente: mesmo evento ou eventos distintos.
- Tratamento de múltiplos documentos emitidos associados à mesma versão formal, caso necessário.
- Governança de quem pode fechar/reabrir/criar revisão e quais aprovações internas serão necessárias.
- Nomenclatura final para preço calculado, preço comercial adotado, desconto/override e preço apresentado.

## 8. Decisões que não devem ser tomadas ainda

- Não homologar a taxonomia dos blocos com base apenas neste lote.
- Não transformar nomes de abas históricas em entidades definitivas.
- Não criar workflow rígido de `aprovar técnica → liberar comercial`.
- Não tratar cada edição interna como revisão formal.
- Não assumir que proposta mais barata é automaticamente a escolhida.
- Não iniciar implementação antes de consolidar as gray areas que afetam o modelo de dados e o fluxo principal.

## 9. Estado deste registro

Este documento consolida somente as decisões discutidas após o Checkpoint 1 até este momento. Deve permanecer separado do relatório de mineração histórica. Novas decisões de domínio devem ser acrescentadas de forma rastreável, sem reescrever silenciosamente as evidências originais.

**Status:** DECISÕES PARCIAIS CONSOLIDADAS — CONTINUAR ENTREVISTA DE DOMÍNIO ANTES DE HOMOLOGAR O MODELO.
