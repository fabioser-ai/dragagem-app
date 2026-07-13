# Modelo 002 — Desaguamento por Centrífuga — análise interrompida

## Status

- Engenharia reversa vertical iniciada.
- Análise interrompida conforme regra definida por Fabio: parar ao encontrar erro real no arquivo.
- Nenhuma conclusão funcional consolidada foi produzida após o bloqueio.

## Fonte analisada

- Arquivo: `01RF_26 - composição MDO - máx. desc..xlsx`
- Tipo aparente de obra: dragagem com desaguamento mecânico por centrífuga.

## Inventário estrutural observado antes do bloqueio

O arquivo contém 12 abas:

1. `Dados Obra`
2. `Produção`
3. `1. Cant. e Mob Equipe`
4. `Mob. Draga`
5. `Mob Centrífuga`
6. `Operação`
7. `2.1. Draga Dec`
8. `2.2 Centrífuga`
9. `2.3. manutenção`
10. `3. Desmob.`
11. `Plan. Final`
12. `Final`

## Erro bloqueador confirmado no arquivo original

### Referência quebrada

- Aba: `2.2 Centrífuga`
- Célula: `D187`
- Fórmula armazenada no arquivo: `#REF!*0.6*0.62`
- Resultado armazenado: `#REF!`

A fórmula contém uma referência já perdida. O arquivo não informa qual célula ou origem deveria substituir `#REF!`.

## Erros derivados confirmados

### Divisão por zero

- Aba: `2.1. Draga Dec`
- Célula: `D205`
- Fórmula: `D201/D203`
- Resultado: `#DIV/0!`

### Propagação do erro

- Aba: `2.1. Draga Dec`
- Célula: `D206`
- Fórmula: `D205*4000`
- Resultado: `#DIV/0!`

## Observação sobre outros `#NAME?`

O motor usado para inspeção exibiu diversos resultados `#NAME?` em fórmulas de referência entre abas. A inspeção direta do XML do arquivo original confirmou como erros armazenados no `.xlsx` somente:

- `2.2 Centrífuga!D187` — `#REF!`;
- `2.1. Draga Dec!D205` — `#DIV/0!`;
- `2.1. Draga Dec!D206` — `#DIV/0!`.

Os demais `#NAME?` não foram classificados como erros reais do arquivo sem evidência adicional.

## Decisão

A engenharia reversa do Modelo 002 permanece bloqueada até que seja esclarecido:

1. qual referência deveria existir em `2.2 Centrífuga!D187`;
2. se `2.1. Draga Dec!D203` deveria conter valor diferente de zero;
3. se os erros são intencionais, residuais ou decorrentes de exclusão de células/colunas.

Após correção ou orientação do especialista, a análise deve continuar do ponto interrompido e percorrer todas as abas até o final.