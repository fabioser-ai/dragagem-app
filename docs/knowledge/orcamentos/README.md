# Conhecimento Operacional — Orçamentos

## Missão

Descobrir, registrar e consolidar o Método de Orçamento FOS antes da construção do novo sistema orçamentário.

## Estratégia oficial

O trabalho será executado em três movimentos.

### 1. Engenharia reversa vertical

Cada planilha será analisada integralmente, de cabo a rabo, preservando:

- tipo de obra;
- sequência das abas;
- entradas e resultados;
- fórmulas e dependências;
- regras explícitas e implícitas;
- coeficientes;
- cotações e referências;
- exceções;
- inconsistências e fórmulas quebradas;
- esclarecimentos do especialista.

Cada modelo terá seu próprio registro de descoberta.

### 2. Crosscheck horizontal

Após quantidade suficiente de modelos completos, será realizada comparação entre planilhas para separar:

- estrutura comum a todos os orçamentos;
- lógica comum a famílias de obras;
- componentes opcionais;
- regras específicas de um método construtivo;
- valores próprios de uma obra;
- conhecimentos candidatos à base histórica;
- exceções que precisam ser suportadas pelo sistema.

Nenhuma repetição observada em um único arquivo será considerada regra geral antes desse crosscheck.

### 3. Arquitetura e implementação

Somente depois do crosscheck será definido o sistema orçamentário da FOS.

A arquitetura deverá:

- reproduzir os resultados vigentes antes de otimizar;
- aceitar diferentes tipos de obra;
- preservar exceções reais;
- separar premissas, dimensionamentos, recursos, custos e apresentação comercial quando a evidência sustentar essa separação;
- permitir evolução guiada pelo uso real;
- registrar valor sugerido, valor efetivamente utilizado e, futuramente, resultado realizado quando aplicável.

## Classificação das evidências

Cada registro deverá indicar uma das categorias:

- **Fato observado:** presente diretamente no arquivo analisado.
- **Informação do especialista:** explicação fornecida por Fabio sobre a operação.
- **Interpretação:** leitura conceitual provisória baseada nas evidências.
- **Hipótese para crosscheck:** possibilidade que depende de comparação com outros modelos.
- **Decisão consolidada:** entendimento aprovado após evidência suficiente.

## Regra de prudência

Números encontrados em uma planilha não são automaticamente constantes da FOS.

Antes de consolidar um coeficiente, deve-se identificar se ele é:

- específico da obra;
- específico do material;
- específico do equipamento ou método;
- preço de uma cotação datada;
- decisão operacional;
- regra legal ou trabalhista;
- estimativa empírica;
- valor histórico reutilizável.

## Registros de descoberta existentes

### `D_004_2026 - SABESP.xlsx`

- Documento: `001_DESAGUAMENTO_BAGS_SABESP.md`
- Classificação aparente: dragagem com desaguamento e acondicionamento em bags.
- Status: engenharia reversa vertical concluída; interpretações pendentes de crosscheck.

### `D_001_2025- Nutrilog(1).xlsx`

- Documento: `D_001_2025_NUTRILOG_1.md`
- Classificação aparente: dragagem de gesso com disposição em bacia de decantação.
- Status: engenharia reversa vertical concluída; possível nova família de orçamento, ainda provisória.

## Registros previstos

- um documento por planilha analisada;
- um documento de crosscheck entre modelos;
- um modelo consolidado do Método de Orçamento FOS;
- documentação arquitetural somente após a consolidação do conhecimento.
