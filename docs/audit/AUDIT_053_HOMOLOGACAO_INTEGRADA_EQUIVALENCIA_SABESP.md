# AUDIT_053 — Homologação integrada da equivalência SABESP

## 1. Identificação

- Issue: `#31 — AUDIT_053`
- Repositório: `fabioser-ai/dragagem-app`
- Branch: `agent/audit-053-homologacao-integrada-sabesp`
- Base auditada: `b6bc2bee5e888889eb5ce095892b2e45f9e0f702`
- Excel: `D_004_2026 - SABESP(5).xlsx`
- SHA-256 do Excel: `a4ee4dc458bd3f9caa90698c5c57524a64868983b411e9746dff55ecdbda8a51`
- Schema vigente: `21`
- Natureza: auditoria e testes de caracterização; nenhuma correção funcional.

## 2. Escopo e método

Foram confrontados:

1. o workbook oficial, inclusive XML interno;
2. os 17 domínios/telas do Novo Sistema de Orçamentos;
3. a cadeia local de recálculo que alimenta `10. Plan. Preços`;
4. o resumo comercial `Planilha1`;
5. a serialização/desserialização do schema 21;
6. o controle de concorrência por snapshot;
7. a regressão automatizada existente.

A inspeção XML foi complementada por leitura com fórmulas compartilhadas
expandidas. O teste golden não lê rede e começa pelo registro explícito da
fotografia oficial de `Dados Obra`.

## 3. Inventário do workbook e cobertura

Todas as worksheets estão visíveis. Não existem nomes definidos, tabelas ou
vínculos externos. Não existem linhas ou colunas ocultas.

| Pos. | Worksheet exata | Dimensão física | Intervalo funcional | Fórmulas expandidas | Tela/domínio |
|---:|---|---|---|---:|---|
| 1 | `Dados Obra ` | `A1:K27` | `A1:H27` | 3 | implementado |
| 2 | `Cotaçoes` | `A1:O35` | `A1:F25` | 0 | implementado |
| 3 | `Produção` | `A1:O33` | `A1:H24` | 9 | implementado |
| 4 | `Barrilete` | `A1:F31` | `A1:F31` | 39 | implementado |
| 5 | `1. Mob. Draga` | `A1:K27` | `A1:K27` | 24 | implementado |
| 6 | `2. Mob. Eq. Polimero` | `A1:K27` | `A1:K27` | 24 | implementado |
| 7 | `Canteiro` | `A1:P32` | `A1:J32` | 32 | implementado |
| 8 | `3. Prep. Célula` | `A1:R29` | `A1:R29` | 45 | implementado |
| 9 | `4. Forn. Bag` | `A1:H71` | `A1:H52` | 71 | implementado |
| 10 | `5. Operação Sistema` | `A1:N26` | `A1:G24` | 24 | implementado |
| 11 | `6. Dragagem` | `A1:Q253` | `A1:Q253` | 84 | implementado |
| 12 | `7. Medição` | `A1:L23` | `A1:L23` | 19 | implementado |
| 13 | `8. Carga e Transporte` | `A1:J23` | `A1:F23` | 18 | implementado |
| 14 | `8. Desmob. Draga` | `A1:J21` | `A1:G21` | 18 | implementado |
| 15 | `9. Desmob. Eq. Polimero ` | `A1:J26` | `A1:F26` | 23 | implementado |
| 16 | `10. Plan. Preços` | `A1:K20` | `A1:J18` | 38 | implementado |
| 17 | `Planilha1` | `A2:F7` | `A2:F7` | 9 | implementado |

Total real após expansão de fórmulas compartilhadas: **480**.

O inventário histórico de 370 fórmulas contava somente fórmulas materializadas
no XML. A diferença de 110 ocorrências é explicada pelas fórmulas
compartilhadas expandidas e não representa diferença matemática.

## 4. Matriz de entradas manuais

Os resultados derivados abaixo não são entradas persistidas. A serialização
armazena apenas as estruturas de entrada de cada bloco.

| Worksheet | Entradas manuais preservadas |
|---|---|
| `Dados Obra ` | identificação, data, cliente, objeto, local, volume, material, linhas, geometria, responsabilidades, horas e dias |
| `Cotaçoes` | fornecedor, contato, preço, data, observação e fonte dos itens |
| `Produção` | vazão, eficiência e concentração |
| `Barrilete` | equipe, encargos, refeições, transporte, itens e BDI |
| `1. Mob. Draga` | equipe, encargos, refeições, transporte, itens, valores manuais e BDI |
| `2. Mob. Eq. Polimero` | equipe, encargos, refeições, transporte, itens, valores manuais e BDI |
| `Canteiro` | equipe, refeições, transporte, itens mensais/manuais e BDI |
| `3. Prep. Célula` | equipe, itens, composição real, repetições, refeições, transporte e BDI |
| `4. Forn. Bag` | memorial físico adotado, opções, itens, equipe, fator de preço, refeições, transporte e BDI |
| `5. Operação Sistema` | equipe, itens, refeições e transporte |
| `6. Dragagem` | coleção de entradas manuais identificadas por célula |
| `7. Medição` | equipe, itens, refeições, transporte e dois BDIs |
| `8. Carga e Transporte` | equipe, itens, refeições, transporte e dois BDIs |
| `8. Desmob. Draga` | equipe, itens, refeições, transporte e BDI |
| `9. Desmob. Eq. Polimero ` | equipe, itens, refeições, transporte e BDI |
| `10. Plan. Preços` | quantidades manuais das linhas sem referência e BDI por linha |
| `Planilha1` | quantidades comerciais `D3:D6` |

## 5. Matriz de dependências integrada

| Origem | Consumidores diretos/relevantes |
|---|---|
| `Dados Obra ` | `Produção`, `Barrilete`, mobilizações, `Canteiro`, `3. Prep. Célula`, `4. Forn. Bag`, operação, desmobilizações |
| `Produção` | prazo de `Canteiro`, `5. Operação Sistema` e `6. Dragagem` |
| `Barrilete` | mobilização e desmobilização do equipamento de polímero |
| `Canteiro` | `6. Dragagem` |
| `3. Prep. Célula` | linhas de preparo em `10. Plan. Preços` |
| `4. Forn. Bag` | `5. Operação Sistema`, quantidade/custo de bags e quantidade comercial da dragagem |
| `5. Operação Sistema` | custo mensal consumido por `6. Dragagem` |
| `6. Dragagem` | linha de dragagem/operação em `10. Plan. Preços` |
| `7. Medição` | linha de medição em `10. Plan. Preços` |
| mobilizações/desmobilizações | linhas correspondentes em `10. Plan. Preços` |
| `10. Plan. Preços` | quatro linhas e total final de `Planilha1` |

Referências externas de fechamento verificadas:

- `1. Mob. Draga!F27 = 16.961,72`
- `2. Mob. Eq. Polimero!F27 = 39.925,08`
- `3. Prep. Célula!F29 = 177.323,61`
- `3. Prep. Célula!N7 = 2.509`
- `4. Forn. Bag!F29 = 355.460,245`
- `SUM(4. Forn. Bag!D15:D23) = 15`
- `6. Dragagem!D248 = 326.679,25303539797`
- `4. Forn. Bag!B33 = 5.000`
- `7. Medição!F20 = 14.204,144`
- `8. Desmob. Draga!F21 = 17.310,245`
- `9. Desmob. Eq. Polimero !F26 = 6.808,91`

## 6. Fórmulas de fechamento

As 480 fórmulas são caracterizadas pelas suítes específicas de cada domínio. A
auditoria integrada confirma ainda as fórmulas completas do fechamento:

### `10. Plan. Preços`

- Cada linha referencia somente a worksheet indicada no Excel.
- `G4:G11 = custo total / quantidade`.
- `I4:I11 = (1 + BDI/100) × custo unitário`.
- `J4:J11 = quantidade × preço unitário`.
- `C12 = SUM(C5:C11)`, preservando a exclusão incomum de `C4`.
- `J12 = SUM(J4:J11)`.
- `J18 = SUM(J6:J9) / E8`.

### `Planilha1`

- `E3 = SUM('10. Plan. Preços'!J4:J5)`
- `F3 = D3 × E3`
- `E4 = F4 / D4`
- `F4 = '10. Plan. Preços'!J6`
- `E5 = F5 / D5`
- `F5 = SUM('10. Plan. Preços'!J7:J9)`
- `E6 = F6`
- `F6 = SUM('10. Plan. Preços'!J10:J11)`
- `F7 = SUM(F3:F6)`

## 7. Golden integrado

Fluxo caracterizado:

1. criar orçamento e versão;
2. registrar `DadosObra()` com os valores oficiais;
3. recalcular localmente toda a cadeia;
4. calcular `10. Plan. Preços`;
5. calcular `Planilha1`;
6. serializar;
7. fechar/reabrir por desserialização;
8. recalcular e comparar.

| Resultado | Excel | Sistema |
|---|---:|---:|
| Custo total `10. Plan. Preços!C12` | 937.711,487035398 | 937.711,487035398 |
| Preço de venda `10. Plan. Preços!J12` | 1.474.158,0945066367 | 1.474.158,0945066367 |
| Auxiliar `10. Plan. Preços!J18` | 268,9097133013273 | 268,9097133013273 |
| Total geral `Planilha1!F7` | 1.474.158,0945066367 | 1.474.158,0945066367 |

O cálculo integrado realizou **zero leituras e zero escritas remotas**.

## 8. Persistência, reabertura e concorrência

- Schema 21 serializa todas as entradas das 17 telas.
- `preco_venda`, total geral e demais resultados derivados não são
  serializados.
- O round trip preserva integralmente as entradas.
- Após reabertura, o recálculo reproduz o mesmo total golden.
- Um snapshot remoto diferente do esperado retorna
  `StatusPersistencia.BRANCH_AVANCADA`.
- No conflito, nenhum `commit_sha` é produzido e não há sobrescrita.

## 9. Recálculo de dependências

O teste altera somente `Dados Obra.volume_dragagem` de 5.000 para 10.000:

- a mobilização fixa da draga permanece igual;
- `6. Dragagem!D248` é recalculada;
- o total final é recalculado;
- nenhuma operação remota ocorre.

Esse ensaio caracteriza o recálculo funcional observado. Ele não afirma que a
implementação já possua um motor de grafo incremental genérico.

## 10. Divergências e classificação

### D-001 — relevante arquitetural, não bloqueia a equivalência matemática

A composição das referências entre telas está hoje em
`apresentacao/planilha_precos.py::_referencias_externas`. O resultado é correto,
local e testável, mas a arquitetura física declara que apresentação não deve
conter fórmula/regra e que a coordenação pertence à aplicação/cálculo.

Classificação: **divergência funcional relevante de arquitetura**.

Tratamento nesta Issue: somente documentar e caracterizar. Mover a coordenação
seria refatoração funcional/transversal e ampliaria o escopo da auditoria.

### D-002 — documentação histórica

O documento histórico do modelo registra 370 fórmulas; a inspeção atual,
expandindo fórmulas compartilhadas, encontra 480.

Classificação: **apresentação/documentação**. Não há diferença de resultado.

### D-003 — particularidades preservadas do Excel

- espaços finais em `Dados Obra ` e `9. Desmob. Eq. Polimero `;
- grafia `Cotaçoes`;
- numeração ausente/repetida entre worksheets;
- `8. Carga e Transporte` mantém título interno copiado de Medição;
- `C12` exclui deliberadamente `C4`;
- entradas azuis/manuais permanecem manuais.

Classificação: **inconsistência do Excel preservada**, sem correção nesta Issue.

### Ausências

- divergência matemática bloqueadora: nenhuma;
- divergência de persistência: nenhuma;
- regressão nas telas homologadas: nenhuma;
- alteração de CSV operacional: nenhuma;
- item fora de escopo iniciado: nenhum.

## 11. Conclusão

**Equivalente com ressalvas.**

A cadeia integrada reproduz os valores intermediários e o total final oficial,
preserva entradas no ciclo salvar–fechar–reabrir, recalcula resultados e recusa
sobrescrita com snapshot divergente. A ressalva é arquitetural: a coordenação
intertelas está na camada de apresentação.

## 12. Kid Steps recomendados

1. Homologar este diagnóstico sem alterar a equivalência atual.
2. Abrir Issue própria para mover a coordenação de referências para aplicação
   ou cálculo, mantendo os mesmos testes golden.
3. Atualizar, em Issue documental própria, a contagem histórica de fórmulas
   para distinguir fórmulas XML materializadas de fórmulas compartilhadas
   expandidas.
4. Não combinar esses ajustes com novas worksheets ou novas famílias.

## 13. Recomendação

O Draft PR desta auditoria pode ser aprovado como evidência técnica. A
equivalência matemática e a persistência estão homologáveis; a ressalva D-001
deve ser tratada separadamente para não transformar uma auditoria diagnóstica
em refatoração transversal.
