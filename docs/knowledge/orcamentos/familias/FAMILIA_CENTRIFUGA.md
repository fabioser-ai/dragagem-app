# Família de Orçamentos — Dragagem com Centrífuga

## Status e cobertura

Consolidação de sete modelos: `005`, `007`, `008`, `012`, `013`, `044` e `047`. O modelo `007` possui aprofundamento semântico; os demais sustentam principalmente evidência estrutural. Os arquivos Xisto (`008` e `013`) e Jacareí (`044` e `047`) formam pares úteis de comparação entre versões/alternativas.

## Objetivo da família

Formar preço para dragagem hidráulica seguida de separação sólido-líquido por uma ou mais centrífugas, incluindo mobilizações, equipe, operação, manutenção, infraestrutura, movimentação/destinação do lodo e desmobilização.

A unidade principal pode ser tonelada seca, m³, mês ou preço mínimo de faturamento. Contratos longos podem exigir fases econômicas distintas.

## Núcleo comum

1. Dados da obra e qualidade/quantidade do material.
2. Produção da draga e capacidade das centrífugas.
3. Quantidade de centrífugas, turnos e horas produtivas.
4. Canteiro e equipe integrada.
5. Mobilização separada da draga e da centrífuga.
6. Composição mensal da dragagem.
7. Composição mensal da centrifugação/desaguamento.
8. Manutenção e equipamentos de apoio.
9. Pacotes civis/logísticos opcionais.
10. Desmobilizações e consolidação final.

## Diferenças internas

- Uma, duas ou três centrífugas.
- Dois ou três turnos e diferentes jornadas.
- Produção informada pelo cliente versus recalculada pela FOS.
- Contrato curto por quantidade versus contrato longo com faturamento mínimo.
- Base de concreto, estrutura metálica, aluguel inicial e remoção de ensecadeira.
- Movimentação e destinação do lodo desaguado incluídas ou separadas.
- Modelo “sem centrífuga” preservado como alternativa de família, não como prova de que o pacote seja obrigatório.
- BDI aplicado por pacote, referência histórica ou preço definido por cenário de resultado.

## Pacotes utilizados

- dados/premissas e produção;
- canteiro e equipe;
- mobilização da draga;
- mobilização das centrífugas;
- aluguel ou recuperação inicial de equipamento;
- operação da draga;
- operação das centrífugas;
- manutenção;
- base/estrutura civil;
- movimentação do lodo desaguado;
- transporte/destinação;
- desmobilização do canteiro, draga e centrífugas;
- consolidação e cenários comerciais.

## Parâmetros recorrentes

- massa seca/volume e teor de sólidos;
- vazão e produção da draga;
- capacidade nominal/operacional da centrífuga;
- quantidade de máquinas, turnos, horas e dias;
- eficiência e disponibilidade;
- equipe por turno e encargos;
- consumo de energia, combustível, polímero e água quando aplicável;
- valor, vida útil, manutenção, juros e aluguel do equipamento;
- prazo contratual, período inicial e período recorrente;
- quantidade/faturamento mínimo, retenções e BDI.

## Fórmulas recorrentes

```text
capacidade_total = quantidade_centrífugas × capacidade_operacional_unitária
produção_mensal = capacidade_total × horas_produtivas_dia × dias_mês
prazo = quantidade_total ÷ produção_mensal
custo_mensal_equipe = soma(quantidade × custo_hora × horas × encargos)
custo_total_fase = custo_mensal_fase × meses_fase
custo_unitário = custo_total ÷ quantidade_processada
faturamento_mínimo = preço_unitário × quantidade_mínima
resultado_fase = receita_líquida_fase − custos_fase
preço_pacote = custo_pacote × (1 + BDI)
```

No modelo `007`, o horizonte de 58 meses é dividido em 15 + 43 e a receita é multiplicada por 0,85. Esses números são específicos do arquivo.

## Exceções

- Cenário sem centrífuga.
- Produção do cliente mantida paralela à produção FOS.
- Faturamento mínimo e resultado por fases.
- Recuperação acelerada/aluguel inicial das centrífugas.
- Estrutura metálica ou base de concreto como opção.
- Três centrífugas com equipe/turnos distintos.
- Desaguamento contratado por tonelada seca em vez de m³.

## Riscos

- Misturar capacidade nominal, operacional, garantida e adotada.
- Sobrescrever premissa do cliente com decisão FOS.
- Duplicar custo inicial nas fases ou no preço unitário.
- Vida útil/depreciação incompatível com prazo contratual.
- BDI e retenções sem significado explícito.
- Resultado mensal positivo ocultar recuperação inicial negativa.
- Fórmulas quebradas: no modelo `007`, dois `#DIV/0!` e um `#REF!` foram confirmados.
- Generalizar equipe/turno de um cenário.

## Oportunidades de padronização

- Cenários comparáveis de quantidade de máquinas e turnos.
- Separação formal entre premissa do cliente, sugestão histórica e valor adotado.
- Modelo de fases contratuais com custos de implantação e recorrência.
- Catálogo versionado de centrífugas e capacidades.
- Pacotes civis/logísticos ativáveis.
- Indicadores de capacidade, utilização, custo/t seca, faturamento mínimo e payback sem misturá-los ao custo técnico.
- Validações de gargalo entre draga e centrífugas.

## Candidatos ao núcleo do novo sistema

- Cenário e comparação de cenários.
- Equipamento com fotografia técnica/econômica.
- Fase contratual.
- Quantidade mínima e unidade econômica.
- Produção informada, sugerida e adotada separadas.
- Pacote ativável e dependência entre dragagem/desaguamento.
- Resultado mensal, por fase e total.
- Validação de capacidade, divisor zero, referência quebrada e dupla incidência.

## Pendências

- Unidade contratual dominante por tipo de proposta.
- Regra de dimensionamento do número de centrífugas.
- Significado comercial de retenções/fatores líquidos.
- Política de recuperação do investimento e vida útil.
- Incidência do BDI e tratamento do faturamento mínimo.

