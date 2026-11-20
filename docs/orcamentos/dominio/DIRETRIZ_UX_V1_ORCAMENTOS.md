# DIRETRIZ DE UX — ORÇAMENTOS V1

**Data:** 01/09/2026  
**Status:** CONFIRMADO POR FABIO  
**Escopo:** Novo módulo de Orçamentos do APP FOS — V1

## 1. Objetivo da V1

A V1 não tem como objetivo reinventar a forma como a FOS elabora orçamentos. O objetivo é transformar o processo hoje executado em Excel em um processo estruturado, rastreável, persistente e reutilizável dentro do APP FOS.

A engenharia e a lógica funcional existentes nos orçamentos atuais devem ser preservadas como referência principal. A primeira versão deve reduzir ruptura de hábito e facilitar adoção.

Princípio central:

> **A arquitetura pode ser nova sem a experiência parecer nova.**

## 2. Perfil de adoção

Os usuários que elaboram orçamentos na FOS são profissionais experientes, habituados há muitos anos à lógica dos Excel existentes. A V1 deve ser desenhada para baixa carga cognitiva e alta familiaridade.

O sucesso da V1 depende de o usuário reconhecer rapidamente onde estão os conceitos que já utiliza hoje: Mobilização, Dragagem, Canteiro, Célula de Desaguamento e demais blocos equivalentes às abas/etapas conhecidas.

A solução não deve depender de treinamento extenso para ser utilizável.

## 3. Regra de decisão de UX

Quando houver dúvida entre:

- uma solução mais sofisticada, porém diferente da prática atual; e
- uma solução mais familiar ao Excel atual, que preserve capacidade de evolução futura;

na V1 deve prevalecer a segunda opção.

Isso não significa copiar limitações do Excel. Significa preservar linguagem, sequência mental, agrupamentos e referências funcionais conhecidas, enquanto a estrutura interna passa a ser organizada corretamente no APP.

## 4. Estrutura interna dos blocos

A anatomia inicial de cada bloco funcional deve ser derivada do que foi capturado pelo Work nas abas históricas analisadas.

Para cada bloco, a V1 deve usar como referência os campos, parâmetros, unidades, fórmulas, dependências, equipamentos, mão de obra, consumos, premissas e resultados efetivamente encontrados nas abas correspondentes.

A transformação esperada é principalmente de forma:

- célula/aba passa a campo estruturado;
- valores institucionais podem vir de cadastro mestre;
- valores específicos da obra permanecem contextuais e editáveis;
- fórmulas passam a cálculos derivados e rastreáveis;
- valores consolidados passam a snapshots preservados;
- histórico deixa de depender de arquivos soltos.

A V1 não deve redesenhar a engenharia da FOS sem necessidade comprovada.

## 5. Critério de sucesso de usabilidade

Um engenheiro habituado aos Excel atuais da FOS deve conseguir criar e elaborar um orçamento no APP com pouca ou nenhuma explicação adicional.

Indicadores qualitativos de sucesso:

- reconhecer imediatamente os blocos do orçamento;
- entender onde preencher cada dado;
- perceber continuidade com a lógica das abas atuais;
- não precisar aprender uma nova metodologia de orçamento para usar o sistema;
- conseguir revisar e fechar a proposta com segurança.

Se a V1 exigir treinamento longo para entender a nova organização, a UX deve ser considerada excessivamente distante da prática atual.

## 6. Estratégia de evolução

A evolução do módulo será progressiva:

- **V1 — adoção e equivalência funcional:** estruturar o processo atual no APP mantendo forte familiaridade com o Excel;
- **V2 — simplificação e automação:** eliminar redundâncias comprovadas e automatizar etapas com base no uso real;
- **V3 — inteligência e otimização:** introduzir sugestões, reaproveitamento histórico e melhorias de decisão sem retirar autonomia do engenheiro.

Nenhuma dessas fases futuras deve ser antecipada de forma que prejudique a adoção da V1.

## 7. Diretriz para o próximo trabalho do Work

O próximo trabalho deve partir da mineração já realizada e transformar as abas/blocos históricos em uma proposta de catálogo V1 e anatomia inicial de cada bloco, mantendo fidelidade funcional ao Excel.

O Work deve priorizar:

1. mapear aba histórica → bloco macro V1;
2. consolidar campos e parâmetros por bloco sem inventar simplificações;
3. preservar unidades, fórmulas e dependências encontradas;
4. indicar quais dados parecem mestres, contextuais, derivados ou históricos;
5. apontar somente divergências reais que exijam decisão de domínio;
6. evitar redesenho conceitual e mudanças de UX não necessárias nesta fase.

**Regra:** primeiro reproduzir de forma estruturada o que funciona hoje; evoluir somente depois de uso real e validação dos usuários.
