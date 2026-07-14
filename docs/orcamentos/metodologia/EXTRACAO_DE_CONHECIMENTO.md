# Metodologia Oficial de Extração de Conhecimento

## Missão
Extrair conhecimento permanente do domínio de orçamentos da FOS Engenharia por engenharia reversa das planilhas históricas.

## Princípios
- Cada planilha representa conhecimento operacional acumulado.
- Compreender antes de concluir.
- Separar fatos observados de hipóteses.
- Não inferir regras sem evidência.
- Não tomar decisões arquiteturais nesta etapa.

## Identificação
Cada análise será identificada exclusivamente pelo nome completo do arquivo Excel e gerará um documento em docs/orcamentos/analises/<NOME_DO_ARQUIVO>.md.

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

## Estrutura obrigatória da planilha
- Objetivo geral.
- Fluxo completo do orçamento.
- Conhecimentos específicos desta obra.
- Conhecimentos reutilizáveis.
- Conceitos inéditos.
- Dúvidas em aberto.

## Restrições
É proibido propor banco de dados, arquitetura, classes, APIs, interface ou implementação.

## Consolidação futura
As análises são independentes. Somente após um conjunto representativo de planilhas será produzida uma síntese arquitetural baseada nas evidências acumuladas, nunca em uma única planilha.