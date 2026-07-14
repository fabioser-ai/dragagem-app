# Família de Orçamentos — Dragagem e Bombeamento Direto

## Status e cobertura

Consolidação dos modelos `014`, `023`, `025`, `028`, `032`, `035` e `046`. O modelo `014` possui aprofundamento semântico. Os pares CMPC `032/035` permitem observar repetição/revisão de estrutura.

## Objetivo da família

Formar preço para remover e recalcar material por draga ou motobomba diretamente ao destino definido, sem etapa central obrigatória de bags ou centrífuga. Pode incluir preparo da área, remoção de vegetação, medição, apoio, transporte interno e desmobilização.

A unidade principal costuma ser m³; locação ou disponibilidade pode ser cobrada por mês/hora, e pacotes fixos por verba.

## Núcleo comum

1. Dados da obra: volume, material, distância, linha, profundidade, jornada e medição.
2. Produção e prazo.
3. Mobilização de draga/equipe.
4. Canteiro e apoio mensal.
5. Composição da operação de dragagem/bombeamento.
6. Medição/batimetria quando exigida.
7. Desmobilização.
8. Planilha de preços e resumo comercial.

## Diferenças internas

- Dragagem por produção versus locação/disponibilidade mensal.
- Bombeamento direto para área do cliente, bacia ou destino externo.
- Linha curta/longa, flutuante/terrestre e necessidade de booster.
- Preparo de área, ensecadeira, remoção de vegetação ou movimentação prévia.
- Medição por batimetria, volume, hora ou preço mensal.
- Equipamentos e equipe fornecidos parcial ou integralmente pelo cliente.
- Custo mensal detalhado versus composição mais simples por pacote.

## Pacotes utilizados

- premissas e produção;
- mobilização da draga/equipe;
- canteiro;
- preparo da área/ensecadeira/vegetação;
- linha de recalque e booster;
- operação da draga/bombeamento;
- medição/batimetria;
- transporte/destinação quando houver;
- desmobilização;
- consolidação comercial.

## Parâmetros recorrentes

- volume, material, distância e desnível;
- vazão, eficiência, concentração e horas produtivas;
- jornada, dias/mês e prazo arredondado;
- diâmetro/comprimento da linha, flutuantes e acoplamentos;
- consumo de combustível, filtros e lubrificantes;
- equipe, salários, encargos, refeições e alojamento;
- valor do equipamento, manutenção, docagem, depreciação e juros;
- custo de medição, mobilização e BDI por pacote.

## Fórmulas recorrentes

```text
horas_mês = horas_dia × dias_mês
produção_horária = vazão × eficiência × concentração
produção_mensal = produção_horária × horas_mês
prazo_técnico = volume ÷ produção_mensal
prazo_custeado = arredondamento_aplicável(prazo_técnico)
custo_combustível = horas × consumo_hora × preço
custo_equipe = soma(quantidade × custo_hora × horas × encargos)
custo_mensal = operação + pessoal + manutenção + apoio + administração + financeiras
custo_total = custo_mensal × prazo_custeado + pacotes_fixos
preço_unitário = preço_total ÷ volume
```

## Exceções

- Contratação mensal sem volume fechado.
- Preparo de área sob responsabilidade do cliente.
- Booster ou equipamento auxiliar.
- Medição como pacote relevante e não mera atividade administrativa.
- Remoção de vegetação e ensecadeira.
- Destino próximo com bombeamento direto versus logística adicional.
- Prazo fracionário tecnicamente, mas custo mensal inteiro comercialmente.

## Riscos

- Usar concentração como percentual sem normalização decimal.
- Confundir horas disponíveis, trabalhadas e produtivas.
- Arredondar prazo silenciosamente.
- Misturar custo mensal e total.
- Cobrar linha/booster em dois pacotes.
- Manter rótulos de desaguamento herdados em proposta de dragagem direta.
- Generalizar percentuais de manutenção, financeiras ou BDI.
- Tratar item fornecido pelo cliente como valor zero sem motivo.
- Atualizar toda a memória ao alterar somente preço comercial.

## Oportunidades de padronização

- Motor comum de produção/prazo com unidades auditáveis.
- Composição mensal padrão de draga, parametrizada por equipamento.
- Linha de recalque como submodelo independente.
- Política explícita de prazo técnico versus prazo custeado.
- Modos de contratação por produção, mês, hora ou disponibilidade.
- Matriz de responsabilidade e exclusões.
- Pacotes de preparo/medição ativáveis.
- Indicadores separados de custo mensal, custo total, R$/m³ e preço/hora.

## Candidatos ao núcleo do novo sistema

- Premissa física/operacional.
- Equipamento e configuração da linha.
- Produção, prazo e arredondamento rastreável.
- Pacote fixo ou mensal.
- Recurso e incidência temporal.
- Responsabilidade FOS/cliente/terceiro.
- Unidade econômica e modalidade de cobrança.
- Resultado técnico, custo e preço separados.
- Dependência incremental entre premissa, produção, prazo e pacotes.

## Pendências

- Definição oficial de eficiência e concentração.
- Política de horas produtivas e paradas.
- Regra de arredondamento por pacote.
- Quando usar preço por m³, mês, hora ou disponibilidade.
- Percentuais corporativos versus específicos do orçamento.

