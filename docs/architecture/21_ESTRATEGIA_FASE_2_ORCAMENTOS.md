# Estratégia da Fase 2 — Engenharia Reversa do Sistema Orçamentário

## Objetivo

Formalizar que a evolução funcional da Fase 2 será orientada pelo conhecimento operacional da FOS e que a primeira entrega priorizada será o sistema orçamentário.

## Decisão

Antes de qualquer implementação será realizada engenharia reversa completa das planilhas utilizadas pela FOS.

O objetivo não é copiar um Excel específico. O objetivo é descobrir, comparar e consolidar o Método de Orçamento FOS.

## Fluxo obrigatório

1. engenharia reversa vertical de cada modelo;
2. documentação do modelo individual em `docs/knowledge/orcamentos/`;
3. validação das interpretações com Fabio;
4. repetição do processo para outros tipos de obra;
5. crosscheck horizontal entre modelos;
6. consolidação do núcleo comum, variações, parâmetros e exceções;
7. definição da arquitetura do sistema orçamentário;
8. implementação por Kid Steps;
9. equivalência funcional com as fontes originais;
10. evolução orientada pelo uso real e pelo histórico das obras.

## Engenharia reversa vertical

Cada arquivo deve ser analisado integralmente, incluindo:

- abas e sequência de uso;
- entradas e resultados;
- fórmulas;
- dependências entre abas;
- regras explícitas e implícitas;
- valores embutidos;
- coeficientes;
- preços e referências de mercado;
- exceções;
- erros ou fórmulas quebradas;
- esclarecimentos do especialista.

Cada modelo terá documento próprio. Uma fórmula encontrada em um único arquivo não será classificada automaticamente como regra geral da FOS.

## Crosscheck horizontal

Somente após a análise completa de quantidade suficiente de modelos será executada comparação transversal para separar:

- estrutura comum a todos os orçamentos;
- lógica comum a famílias de obras;
- componentes opcionais;
- métodos construtivos específicos;
- valores próprios de uma obra;
- valores dependentes de material ou equipamento;
- preços de mercado com data-base;
- conhecimentos candidatos a histórico operacional;
- exceções que o sistema precisa suportar.

## Camada de conhecimento

O conhecimento operacional é preservado em `docs/knowledge/` independentemente da tecnologia do APP.

A documentação deve distinguir:

- fato observado;
- informação do especialista;
- interpretação;
- hipótese para crosscheck;
- decisão consolidada.

Mudanças futuras de lógica não apagam decisões anteriores. Devem registrar o método anterior, o aprendizado que motivou a revisão, a nova decisão e seus impactos.

## Primeiro modelo concluído

A engenharia reversa vertical do arquivo `D_004_2026 - SABESP.xlsx`, referente a dragagem com desaguamento em bags, foi registrada em:

- `docs/knowledge/orcamentos/001_DESAGUAMENTO_BAGS_SABESP.md`.

O registro confirma que o arquivo combina:

- premissas da obra;
- cálculo de produção e prazo;
- dimensionamentos físicos;
- mobilização, implantação, operação, apoio e desmobilização;
- composição detalhada de custos;
- consolidação comercial.

Esses achados permanecem provisórios até o crosscheck com outros modelos.

## Regra de ouro

Nenhuma fórmula será alterada antes de ser compreendida.

Nenhuma repetição observada em um único arquivo será tratada como padrão universal.

A equivalência funcional tem prioridade sobre otimizações, e a arquitetura deve preservar exceções reais em vez de eliminá-las por conveniência.