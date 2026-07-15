# Fluxo do Usuário e Experiência do Novo Sistema de Orçamentos

Data: 2026-07-15

Status: especificação conceitual oficial da Fase 7, tecnológica-neutra e sem implementação.

## 1. Autoridade, objetivo e limites

Este documento define como um engenheiro da FOS cria, edita, calcula, revisa, compara, aprova e consulta um orçamento com continuidade, segurança e rastreabilidade. Especializa o domínio, o modelo lógico e o motor dos documentos 22, 23 e 24, sem substituí-los.

As fontes são o estado e a filosofia oficiais, domínio, modelo lógico, motor, vocabulário, Método FOS, crosscheck semântico, parking lot de propostas e documentos das famílias.

Esta fase não implementa código, não cria telas reais e não define componentes, rotas, páginas, CSS, estrutura Python, persistência, cache físico, autosave físico, processamento assíncrono ou geração de documentos.

## 2. Princípio central e modelo mental

O sistema moderniza a experiência sem alterar a lógica mental da FOS:

~~~text
Premissas
→ produção ou regime operacional
→ dimensionamentos
→ pacotes
→ composições
→ custo
→ preço
→ revisão
→ consolidação
~~~

A sequência é lógica, não reprodução das abas dos Excel nem obrigação de concluir tudo linearmente. O usuário navega conforme o trabalho exigir, enquanto dependências, validações e estados mostram o que está pronto, pendente ou bloqueado.

Princípios:

1. conceitos do domínio organizam a experiência;
2. etapa não é pacote;
3. cenário não mistura resultados com outro cenário;
4. sugestão não substitui decisão do engenheiro;
5. não aplicável não apaga dados;
6. responsabilidade do cliente não elimina necessidade técnica;
7. cálculo e persistência são experiências distintas;
8. versão congelada é somente leitura;
9. detalhe é carregado sob demanda;
10. desempenho percebido integra a correção funcional.

## 3. Perfis conceituais

### 3.1 Matriz de perfis

| Perfil | Visualiza | Edita | Revisa | Aprova |
|---|---|---|---|---|
| Engenheiro orçamentista | orçamento, versões de trabalho, cenários, memórias, custos e validações necessários | identificação, premissas, pacotes, valores, composições e cenários | prepara e responde solicitações | não por padrão conceitual |
| Revisor técnico | premissas, dimensionamentos, fórmulas, memórias e riscos | comentários, solicitações e decisões | técnica | tecnicamente, conforme governança futura |
| Revisor comercial | custos autorizados, incidências, preços, margem, condições e resumo externo | comentários, solicitações e decisões | comercial | comercialmente, conforme governança futura |
| Administrador de catálogos | mestres, vigências, origem e usos | referências mestres futuras | consistência do catálogo | vigência do mestre, sem alterar fotografias |
| Consulta | versões aprovadas, cenário adotado e histórico permitido | nada | nada | nada |

Não se definem permissões físicas ou roles de código. Uma pessoa pode exercer mais de uma função conforme governança futura, sem eliminar autoria e segregação registradas.

## 4. Jornada principal

1. Acessar o painel resumido.
2. Localizar orçamento existente ou iniciar novo.
3. Informar identificação e contexto mínimos.
4. Selecionar família inicial.
5. Criar ou abrir versão de trabalho.
6. Criar ou selecionar cenário.
7. Revisar pacotes sugeridos.
8. Marcar aplicabilidade e responsabilidade.
9. Preencher premissas com unidade e origem.
10. Confirmar sugestões ou informar valores próprios.
11. Acompanhar resultados, memórias e validações.
12. Preencher composições, recursos e cotações.
13. Formar custos e preço com incidências explícitas.
14. Criar e comparar cenários quando necessário.
15. Resolver pendências ou registrar ressalvas autorizadas.
16. Revisar consolidações técnica e comercial.
17. Congelar a versão candidata.
18. Encaminhar para revisão/aprovação.
19. Aprovar ou solicitar revisão rastreável.
20. Disponibilizar a versão aprovada como fonte futura de proposta.

O congelamento e a aprovação preservam o mesmo invariante: nada aprovado é reescrito. Ajuste posterior ocorre em versão de trabalho derivada.

## 5. Painel e criação

O painel carrega somente identificação, cliente, objeto, família, versão atual, estado, responsável, última alteração, cenário adotado quando houver, preço aprovado quando permitido, pendências, alertas e ação principal.

Ações: criar, abrir, continuar, duplicar orçamento, criar revisão, consultar versões, arquivar e acessar histórico antigo. Não carrega composições, memórias, todos os cenários ou recursos.

Criação exige apenas identificação, cliente/referência, objeto, local, responsável, família inicial, data-base e observação. O orçamento nasce rascunho. Depois, abre a versão inicial, cria cenário inicial, sugere pacotes, registra pendências e não calcula sem entradas válidas.

### Wireframe 1 — painel

~~~mermaid
flowchart TD
    F["Busca e filtros"] --> L["Lista resumida"]
    L --> R["Estado, responsável e pendências"]
    R --> A["Abrir ou continuar"]
    L --> N["Criar orçamento"]
~~~

### Wireframe 2 — cabeçalho

~~~mermaid
flowchart LR
    O["Orçamento e objeto"] --> V["Versão e estado"]
    V --> S["Cenário ativo"]
    S --> P["Salvar, revisar ou comparar"]
~~~

## 6. Navegação interna e continuidade

A visão geral mostra estado, progresso, pendências, custos/preço consolidados permitidos e impacto das últimas alterações.

Etapas: identificação, premissas, cenários, produção e prazo, pacotes, composições, cotações, formação de preço, revisão e consolidação. Atalhos por pacote abrem mobilização, canteiro, dragagem, bags, polímero, centrífuga, batimetria, transporte, desmobilização e exceções. Uma etapa pode reunir vários pacotes.

### Wireframe 3 — etapas

~~~mermaid
flowchart TD
    G["Visão geral"] --> E["Etapas lógicas"]
    E --> D["Detalhe da etapa ativa"]
    D --> K["Pacotes relacionados"]
    D --> V["Validações do contexto"]
~~~

### 6.1 Matriz de navegação

| Origem | Destino | Contexto preservado | Dados adicionais carregados |
|---|---|---|---|
| Painel | orçamento | filtros e posição | versão ativa e resumo do cenário |
| Visão geral | etapa | orçamento, versão, cenário e posição | dados da etapa |
| Etapa | pacote | contexto e etapa de origem | detalhe do pacote escolhido |
| Pacote | composição | cenário, pacote e seleção | itens, recursos e memória sob demanda |
| Validação | objeto relacionado | filtros e contexto | somente objeto/dependências necessárias |
| Cenário | comparação | versão e seleções | resumos comparáveis |
| Versão aprovada | nova revisão | origem somente leitura | nova versão derivada |

## 7. Aplicabilidade, valores e cenários

Aplicabilidade: aplicável, não aplicável, pendente e responsabilidade do cliente.

Não aplicável retira o pacote dos cálculos ativos, preserva dados/motivo, atualiza dependências, invalida seletivamente e permite reativar. Responsabilidade do cliente pode retirar custo FOS, mas preserva requisito, dimensionamento, validação, exclusão e impacto.

Para cada parâmetro relevante, mostrar sugestão, origem, data-base/vigência, adotado, unidade, justificativa de divergência e impacto. Nova sugestão não substitui adotado. Manual é identificado e mantém autoria, justificativa e cálculo original.

Cenários permitem criar, duplicar, renomear, alterar tecnologia, equipamentos, turnos, responsabilidades e pacotes, comparar, adotar e descartar sem apagar.

### Wireframe 4 — cenários

~~~mermaid
flowchart LR
    S["Cenário ativo"] --> C["Trocar"]
    S --> D["Duplicar"]
    S --> P["Comparar"]
    P --> A["Adotar"]
~~~

### Wireframe 8 — comparação

~~~mermaid
flowchart TD
    E["Escolher cenários"] --> M["Premissas e pacotes diferentes"]
    M --> R["Produção, prazo, custo e preço"]
    R --> Q["Riscos e pendências"]
    Q --> A["Decidir cenário adotado"]
~~~

A comparação mostra premissas, produção, prazo, custo, preço, margem, riscos, pendências e pacotes diferentes. Não soma nem mistura cenários.

## 8. Pacotes e composições

A visão de pacotes informa nome, aplicabilidade, responsabilidade, estado, custo, preço relacionado permitido, pendências, alertas, dependências e última alteração.

### Wireframe 5 — pacotes

~~~mermaid
flowchart TD
    P["Lista resumida"] --> S["Status, responsabilidade e impacto"]
    S --> D["Abrir detalhe sob demanda"]
    D --> C["Composições e resultados"]
    D --> V["Pendências e dependências"]
~~~

Composição apresenta itens, recursos, quantidades, unidades, incidências, custo/preço unitário conforme autorização, total, origem, fotografia, fórmula, resultado e memória. Item livre/exceção é permitido com classificação e justificativa, sem virar catálogo automaticamente.

### Wireframe 6 — composição

~~~mermaid
flowchart TD
    C["Cabeçalho e unidade"] --> I["Itens e recursos"]
    I --> Q["Quantidades, incidências e valores"]
    Q --> T["Totais e validações"]
    T --> M["Memória e origem"]
~~~

## 9. Feedback de cálculo e estados

Estados distinguíveis: válido, recalculando, inválido, pendente, não aplicável, não calculável, substituído manualmente e desatualizado.

Após alteração confirmada, informar discretamente resultados recalculados, preservados, pendentes e impacto em custo/preço. Nunca mostrar erros de planilha, coordenadas ou mensagem técnica sem contexto.

### 9.1 Matriz de estados visuais

| Estado de domínio | Apresentação esperada | Ação permitida |
|---|---|---|
| Válido | valor, unidade e memória acessível | consultar/editar origem se permitido |
| Recalculando | progresso contextual | continuar em submodelos independentes |
| Inválido | motivo e afetados | corrigir entrada |
| Pendente | falta e ação recomendada | informar, decidir ou atribuir |
| Não aplicável | motivo e dados preservados | reativar |
| Não calculável | causa em linguagem de domínio | resolver dependência |
| Substituído manualmente | manual e original acessível | revisar/reverter |
| Desatualizado | anterior não aparece vigente | recalcular ou resolver bloqueio |
| Responsabilidade do cliente | requisito separado do custo | revisar responsabilidade |
| Versão congelada | somente leitura e origem | consultar ou criar revisão |

## 10. Salvamento, conflito e desempenho

Salvar preserva orçamento, versão, cenário, etapa, pacote, seleção e posição. Estados: não confirmado, rascunho da interação, salvando, salvo localmente quando seguro, confirmação remota, erro e conflito.

Salvamento automático controlado e explícito podem coexistir conceitualmente. Mudanças agrupadas são confirmadas juntas; falha remota não apaga trabalho local; conflito exige decisão sem sobrescrita silenciosa. Implementação física fica adiada.

Requisitos funcionais:

1. painel carrega só resumo;
2. orçamento carrega versão/cenário ativos;
3. detalhes de pacotes sob demanda;
4. catálogos válidos não são relidos;
5. editar campo não recarrega módulo inteiro;
6. recálculo seletivo;
7. cálculo separado de persistência;
8. troca de etapa preserva estado;
9. salvar preserva rolagem/seleção;
10. st.rerun não é padrão e eventual uso exige motivo/teste;
11. operações demoradas têm feedback;
12. erro remoto não apaga trabalho;
13. leituras idênticas na mesma renderização são proibidas;
14. desempenho percebido é homologado.

Kid Steps de risco medem primeiro resumo útil, leituras remotas, nós recalculados/preservados, estabilidade visual, perda de contexto e duração sinalizada.

## 11. Validações

Central mostra severidade, origem, mensagem, objeto, responsável, estado, justificativa e ação recomendada. Severidades: informação, alerta, pendência, bloqueio e erro de cálculo.

### Wireframe 7 — central de validações

~~~mermaid
flowchart TD
    F["Filtros"] --> L["Validações"]
    L --> D["Origem e recomendação"]
    D --> O["Ir ao objeto"]
    D --> R["Resolver ou justificar"]
~~~

Navegação direta preserva filtros para retorno. Pendência aceita permanece ressalva; justificativa não transforma bloqueio em válido sem decisão autorizada.

## 12. Revisão e aprovação

~~~text
Em elaboração
→ revisão técnica
→ ajustes
→ aprovação técnica
→ revisão comercial
→ ajustes
→ aprovação comercial
→ versão congelada/aprovada
~~~

Comentários, solicitações, decisões, autor, momento e justificativa são históricos. Ajustes ocorrem em versão editável; conteúdo congelado exige revisão derivada. Aprovação preserva ressalvas.

### Wireframe 10 — aprovação

~~~mermaid
flowchart TD
    E["Em elaboração"] --> T["Revisão técnica"]
    T -->|ajustes| E
    T --> C["Revisão comercial"]
    C -->|ajustes| E
    C --> A["Aprovada e somente leitura"]
~~~

## 13. Resumos e histórico

Resumo técnico: premissas, equipamentos, produção, prazo, pacotes, quantidades, custos, dependências, riscos e validações.

Resumo comercial: escopo, itens, unidades, quantidades, preços, prazo, condições, responsabilidades, inclusões e exclusões. Não expõe custos internos indevidos; item comercial mantém vínculo técnico ou justificativa.

### Wireframe 9 — resumo técnico

~~~mermaid
flowchart TD
    P["Premissas e equipamentos"] --> R["Produção, prazo e quantidades"]
    R --> K["Pacotes, custos e dependências"]
    K --> V["Riscos e validações"]
    V --> C["Consolidação rastreável"]
~~~

Histórico permite consultar/comparar versões, autor/motivo, abrir congelada somente leitura, criar revisão derivada, ver cenário adotado e referências futuras a propostas. Comparação não recalcula fotografia histórica. Proposta futura consome somente conteúdo aprovado; geração física permanece fora do escopo.

## 14. Matriz de telas conceituais

| Visão | Objetivo | Dados carregados | Ações | Critério de desempenho |
|---|---|---|---|---|
| Painel | localizar/priorizar | resumos | criar, abrir, continuar, histórico | sem detalhes |
| Criação | rascunho mínimo | referências essenciais | criar/cancelar | curta, sem cálculo prematuro |
| Visão geral | orientar | versão/cenário e consolidações | navegar, salvar, revisar | resumo útil rápido |
| Premissas | informar/adotar | contexto e sugestões | editar/justificar | validação local |
| Cenários | gerir alternativas | metadados/resumos | criar, comparar, adotar | sem memórias integrais |
| Pacotes | aplicabilidade | lista resumida | ativar, responsabilizar, abrir | detalhe sob demanda |
| Composição | custo auditável | composição e referências | editar itens/exceções | descendentes apenas |
| Cotações | adotar referência | cotações relevantes | selecionar/adotar | catálogo não relido |
| Preço | incidências | custos e bases | formar/revisar | sem recálculo técnico |
| Validações | resolver | ocorrências e alvos | filtrar/navegar/resolver | navegação direta |
| Revisão | decidir | candidata e comentários | solicitar/aprovar | estabilidade |
| Consolidação | conferir saída | resumos | revisar/disponibilizar | expandir sob demanda |

## 15. Matriz de ações

| Ação | Entidade afetada | Validação | Recalcula | Persiste | Histórico |
|---|---|---|---|---|---|
| Criar orçamento | Orçamento/Versão/Cenário | mínimos | pendências iniciais | sim | criação |
| Alterar premissa | Premissa/Valor | estado, unidade, faixa | descendentes | após confirmar | antes/depois |
| Alterar aplicabilidade | Pacote/Aplicabilidade | motivo/impacto | subgrafo | sim | decisão |
| Adotar sugestão | Valor Adotado | vigência/unidade | dependentes | sim | origem |
| Inserir item livre | Item/Composição | unidade/classificação | composição | sim | justificativa |
| Atualizar cotação | Fotografia | vigência/escopo | custos/preços | sim | origem |
| Duplicar cenário | Cenário | origem | não por si | sim | linhagem |
| Comparar cenários | Comparação | unidades | não mistura | não necessariamente | decisão posterior |
| Adotar cenário | Versão/Decisão | bloqueios/ressalvas | consolidação | sim | decisão |
| Override | Valor Manual/Resultado | justificativa/alçada | consumidores | sim | original/manual |
| Congelar | Versão | completude | não por si | sim | evento |
| Aprovar | Aprovação/Versão | revisão | não reescreve | sim | autor/ressalvas |
| Criar revisão | Versão | origem | não até mudança | sim | linhagem |

## 16. MVP SABESP

### 16.1 Matriz de MVP

| Capacidade | MVP SABESP | Fase posterior | Justificativa |
|---|---:|---:|---|
| Painel, criação, versão e cenário | sim | evolução | entrada |
| Identificação, premissas e pacotes | sim | generalização | base SABESP |
| Produção e prazo | sim | outras famílias | cadeia central |
| Mobilização draga/sistema e canteiro | sim | catálogos ampliados | pacotes SABESP |
| Célula, bags e polímero | sim | configurações adicionais | desaguamento SABESP |
| Dragagem/desaguamento, medição e desmobilização | sim | logística ampliada | fechamento técnico |
| Composições, custos e preço | sim | políticas ampliadas | equivalência econômica |
| Validações e memórias | sim | automações | explicabilidade |
| Resumos internos | sim | proposta física | revisão |
| Equivalência matemática SABESP | sim | representantes/família | aceite |
| Geração física de proposta | não | sim | parking lot |
| Integração CRM/obra | não | sim | domínio externo |
| Inteligência histórica | não | sim | exige base homologada |
| Todas as famílias | não | sim | reduzir risco |
| Migração integral | não | sim | estratégia própria |

O MVP permite criar orçamento/versão/cenário, registrar premissas, configurar mobilizações, canteiro, célula, bags, polímero, dragagem/desaguamento, medição e desmobilização, formar composições/custos/preço, resolver validações, consultar memórias e comprovar intermediários, pacotes e preço do arquivo D_004_2026 - SABESP.xlsx.

Aceite inclui matemática, velocidade percebida, ausência de refresh evitável, estabilidade visual, contexto preservado, leituras não duplicadas e recálculo seletivo.

## 17. Confronto com fontes oficiais

| Fonte | Regra preservada |
|---|---|
| Domínio | lógica FOS, família, pacotes, versões/cenários e consolidações |
| Modelo lógico | propriedade, fotografias, estados, histórico e aprovações |
| Motor | unidades, memória, invalidação, estados e override |
| Parking lot | aprovado como fonte futura, sem geração física |
| Famílias | sugestões configuráveis e exceções |

## 18. Decisões consolidadas

1. Painel resumido e detalhes sob demanda.
2. Criação aceita rascunho incompleto.
3. Navegação preserva contexto e não governa cálculo.
4. Etapa e pacote são distintos.
5. Aplicabilidade e responsabilidade são explícitas.
6. Sugestão e adoção são separadas.
7. Cenários coexistem sem mistura.
8. Feedback explica cálculo e impacto.
9. Salvamento não desloca usuário nem apaga trabalho.
10. Revisões/aprovações preservam ressalvas.
11. Resumo comercial protege custos internos.
12. MVP prova a SABESP antes de expandir.

## 19. Decisões adiadas

- componentes Streamlit, widgets, cores e layout físico;
- CSS, estrutura Python, rotas e nomes de páginas;
- banco, CSV e persistência;
- cache e autosave físicos;
- processamento assíncrono;
- mecanismo físico de conflitos, eventos e permissões;
- geração de documentos/propostas;
- integrações CRM/Obras;
- alçadas físicas e política visual final.

## 20. Critérios de encerramento

Sem abrir código, é possível responder como criar orçamento, escolher família/pacotes, trabalhar com cenários, informar valores, interpretar cálculos/erros, navegar sem perder contexto, revisar/aprovar, consultar versões, evitar lentidão/refresh e executar o MVP SABESP.

## 21. Encerramento

A Fase 7 define fluxo e experiência sem criar tela ou tecnologia. Após homologação do Merlin, o próximo passo recomendado é arquitetura física mínima e plano de Kid Steps, sem implementação antes de autorização própria.


## Correção da jornada — AUDIT_054

A jornada deve solicitar primeiro cliente/oportunidade e contexto, depois problema e condições da obra. Somente então o usuário escolhe ou configura a solução técnica do cenário, recebe sugestões de capacidades/pacotes e pode alterar a configuração conscientemente.

O cliente não pré-seleciona tecnologia silenciosamente. Sugestões técnicas devem declarar evidência e aplicabilidade; adoção ou divergência deve ser rastreável. Cenários do mesmo orçamento podem comparar configurações e tecnologias diferentes.

Toda referência anterior a “MVP SABESP” significa: primeiro fluxo vertical de equivalência, usando o orçamento SABESP como caso de referência da família técnica aplicável, implementado por capacidades genéricas.
