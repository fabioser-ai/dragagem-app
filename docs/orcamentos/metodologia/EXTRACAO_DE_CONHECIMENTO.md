# Metodologia Oficial de Extração de Conhecimento

## Missão

Extrair conhecimento permanente do domínio de orçamentos da FOS Engenharia por engenharia reversa das planilhas históricas, antes de qualquer arquitetura ou implementação.

## Princípios

- Cada planilha representa conhecimento operacional acumulado.
- Compreender antes de concluir.
- Separar fatos observados de informações do especialista, interpretações e hipóteses.
- Não inferir regras sem evidência.
- Não tomar decisões arquiteturais nesta etapa.
- Preservar exceções, inconsistências e dúvidas.

## Limites da etapa

É proibido propor ou criar banco de dados, arquitetura, classes, APIs, interfaces, componentes, tabelas de sistema ou implementação.

A engenharia reversa extrai somente:

- regras de negócio;
- conhecimento operacional;
- entidades do domínio;
- dependências;
- conceitos;
- fluxo operacional;
- decisões implícitas;
- exceções e inconsistências.

## Identificação

Cada análise será identificada exclusivamente pelo nome completo do arquivo Excel, incluindo extensão. Identificadores genéricos como `ANALYSIS_001`, `PLANILHA_A` e `ORCAMENTO_01` são proibidos.

## Procedimento obrigatório

1. Registrar o nome completo do arquivo Excel.
2. Inventariar todas as abas na ordem original.
3. Identificar o fluxo completo e as dependências em rede.
4. Analisar cada aba integralmente.
5. Explicar a finalidade das fórmulas, sem apenas copiá-las.
6. Separar fatos, informações do especialista, interpretações e hipóteses.
7. Atribuir grau de confiança às descobertas relevantes.
8. Registrar dúvidas sem preenchê-las por dedução.
9. Submeter as interpretações relevantes à homologação.
10. Somente após homologação considerar a análise concluída.

## Estrutura obrigatória por aba

1. Objetivo.
2. Papel no orçamento.
3. Entradas.
4. Saídas.
5. Dependências.
6. Entidades encontradas.
7. Regras de negócio.
8. Lógica dos cálculos e fórmulas.
9. Variáveis importantes.
10. Observações operacionais.
11. Dúvidas.

## Estrutura obrigatória da planilha

- Objetivo Geral.
- Fluxo Completo.
- Conhecimentos Específicos.
- Conhecimentos Reutilizáveis.
- Conceitos Inéditos.
- Possíveis Padrões.
- Dúvidas.

## Graus de confiança

- **Nível A — Confirmado:** observado em diversas planilhas e homologado como padrão consolidado.
- **Nível B — Forte indício:** observado em várias planilhas, ainda sujeito à consolidação final.
- **Nível C — Evidência individual:** observado em apenas uma planilha.
- **Nível D — Hipótese:** interpretação ainda não comprovada.

Hipóteses de Nível D nunca podem definir arquitetura.

## Consolidação futura

As análises são independentes. Somente após conjunto significativo e homologado de planilhas será produzida consolidação transversal. Nenhuma repetição encontrada em um único arquivo será tratada como padrão universal.