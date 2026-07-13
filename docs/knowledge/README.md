# Conhecimento Operacional — APP FOS

## Objetivo

Preservar o conhecimento operacional da FOS independentemente da implementação tecnológica vigente.

Esta camada registra como a empresa trabalha, como o conhecimento foi descoberto e como decisões operacionais evoluem ao longo do tempo.

## Princípios

- Conhecimento operacional é ativo permanente do projeto.
- Código e arquitetura podem mudar sem apagar a memória do processo de negócio.
- Fatos observados, interpretações, hipóteses e decisões devem permanecer claramente separados.
- Uma regra antiga não deve ser apagada quando for substituída; sua revisão deve registrar contexto, motivo e consequência.
- Conhecimento consolidado representa o método vigente, não uma verdade imutável.
- Exceções são parte do método e não devem ser descartadas para simplificar a arquitetura.
- Nenhuma regra encontrada em planilha será promovida a regra geral da FOS antes de comparação suficiente entre modelos e validação do especialista de negócio.

## Tipos de documento

### Registro de descoberta

Preserva a origem do conhecimento:

- fonte analisada;
- fatos observados;
- interpretação inicial;
- hipóteses;
- correções trazidas pelos especialistas;
- perguntas em aberto;
- decisões posteriores.

### Conhecimento consolidado

Descreve como a FOS trabalha no estado atualmente aceito.

Esse conteúdo pode ser revisado quando o uso real, novos modelos de orçamento ou resultados históricos demonstrarem necessidade.

## Relação com as demais camadas

- `docs/audit/`: auditorias técnicas e arquiteturais do software.
- `docs/architecture/`: representação consolidada da arquitetura do APP FOS.
- `docs/knowledge/`: memória operacional e conhecimento de negócio.
- código: implementação vigente do conhecimento e da arquitetura.

## Regra de revisão

Toda mudança relevante de lógica operacional deve registrar:

1. método anterior;
2. evidência ou problema que motivou a revisão;
3. decisão tomada;
4. novo método;
5. impacto esperado;
6. possibilidade de reavaliação futura.
