# Padrão Oficial de Documentação dos Orçamentos

## Identificação permanente

Cada análise deve usar o nome completo do arquivo Excel, incluindo extensão, como identificador permanente.

Exemplo: `D_004_2026 - SABESP.xlsx`.

São proibidos identificadores genéricos como `ANALYSIS_001`, `PLANILHA_A` e `ORCAMENTO_01`.

## Estrutura obrigatória por aba

Para cada aba registrar:

1. Objetivo.
2. Papel.
3. Entradas.
4. Saídas.
5. Dependências.
6. Entidades.
7. Regras de Negócio.
8. Lógica das Fórmulas.
9. Variáveis Importantes.
10. Observações.
11. Dúvidas.

Fórmulas devem ser explicadas por finalidade e efeito operacional; a simples cópia não constitui documentação suficiente.

## Estrutura obrigatória por planilha

Registrar:

- Objetivo Geral;
- Fluxo Completo;
- Conhecimentos Específicos;
- Conhecimentos Reutilizáveis;
- Conceitos Inéditos;
- Possíveis Padrões;
- Dúvidas.

## Classificação da informação

Cada registro relevante deve ser marcado como:

- fato observado;
- informação do especialista;
- interpretação;
- hipótese;
- decisão homologada.

## Evidência e confiança

Toda descoberta deve indicar arquivo, aba e origem observável. O grau de confiança deve seguir os níveis A, B, C ou D definidos em `EXTRACAO_DE_CONHECIMENTO.md`.

## Rastreabilidade

Documentos novos devem referenciar documentos existentes quando houver relação. Contradições exigem atualização explícita; nunca devem ser resolvidas silenciosamente.