# Modelo 002 — Dragagem e Desaguamento por Centrífuga — Suzano Aracruz

## Status

- Engenharia reversa vertical concluída para o arquivo analisado.
- Nenhuma implementação funcional foi realizada.
- As anomalias do Excel foram registradas, mas não interromperam a análise.
- As interpretações permanecem provisórias até o crosscheck com outros modelos.

## Fonte analisada

- Arquivo: `01RF_26 - composição MDO - máx. desc..xlsx`.
- Cliente: Suzano.
- Local: Aracruz — ES.
- Objeto: operação da ETE Aracruz.
- Método de desaguamento: centrífuga decanter.
- Base comercial principal observada: 2.000 toneladas de sólidos secos.
- Prazo de operação utilizado: 8 meses.

## Regra de evidência

Este documento distingue:

- **Fato observado:** valor, fórmula, texto ou dependência presente no Excel.
- **Informação do especialista:** explicação fornecida por Fabio.
- **Interpretação:** leitura conceitual provisória.
- **Hipótese para crosscheck:** entendimento que depende de outros modelos.
- **Anomalia observada:** erro ou inconsistência do arquivo que não impede compreender o método.

## Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Identificação, premissas, metas de produção e cálculo global de massa/volume. |
| 2 | `Produção` | Produção da centrífuga, horas mensais, tonelada seca por hora e prazo. |
| 3 | `1. Cant. e Mob Equipe` | Canteiro, mobilização de equipe, integração, viagens e custo mensal equivalente. |
| 4 | `Mob. Draga` | Mobilização física da draga. |
| 5 | `Mob Centrífuga` | Mobilização das centrífugas e tanques de equalização. |
| 6 | `Operação` | Custos mensais de apoio à operação: equipe, alojamento, veículos, saúde e comunicações. |
| 7 | `2.1. Draga Dec` | Composição mensal detalhada do custo da draga, custo total e hora à disposição. |
| 8 | `2.2 Centrífuga` | Composição mensal detalhada do custo da centrífuga e hora à disposição. |
| 9 | `2.3. manutenção` | Manutenção preventiva especializada dos equipamentos. |
| 10 | `3. Desmob.` | Desmobilização final da equipe e do canteiro. |
| 11 | `Plan. Final` | Consolidação detalhada de custo, BDI, preço unitário, resultado e hora à disposição. |
| 12 | `Final` | Histórico comercial de propostas, revisões, descontos e comparação com referências anteriores. |

## Fluxo observado

```text
Dados e metas da obra
        ↓
Produção da centrífuga e prazo
        ↓
Canteiro e mobilizações
        ↓
Operação de apoio
        ↓
Custos mensais separados da draga e da centrífuga
        ↓
Manutenção preventiva
        ↓
Desmobilização
        ↓
Consolidação detalhada
        ↓
Negociação e histórico de revisões comerciais
```

O fluxo possui sequência de trabalho, mas também dependências em rede. A produção alimenta prazo, quantidades mensais, custos de apoio e indicadores finais.

# 1. Dados da obra

## Fatos observados

A aba registra:

- proposta e data;
- cliente e contatos;
- objeto e local;
- volume de dragagem;
- tipo de material: lodo de ETE;
- tipo de bota-fora: centrífuga;
- sistema de medição por preços unitários de serviços;
- responsabilidade da FOS por canteiro e mobilização;
- jornada de segunda-feira a sábado;
- prazo de 8 meses;
- eficiência produtiva de 80%;
- vazão de centrífuga;
- porcentagem de sólidos na entrada;
- horas produtivas;
- produção em toneladas de sólidos secos por dia e por mês;
- porcentagem média de sólidos após desaguamento e in situ;
- volumes mensais dragado e desaguado;
- tanque de equalização;
- vazão nominal da draga e da centrífuga;
- produção total em toneladas de sólidos secos.

## Fórmulas e relações observadas

- horas produtivas = horas disponíveis × eficiência;
- produção de sólidos por dia depende de vazão, horas produtivas e percentual de entrada;
- produção mensal depende da produção diária e da jornada mensal;
- volume de lodo desaguado depende da produção de sólidos e do teor médio de sólidos desaguado;
- volume dragado depende da produção de sólidos e do teor de sólidos in situ;
- tempo de enchimento do tanque de equalização depende do volume do tanque e da vazão nominal da draga;
- produção total é consolidada para 2.000 toneladas de sólidos secos.

## Interpretação

Esta aba combina cadastro do empreendimento, premissas operacionais e metas contratuais. Diferentemente do Modelo 001, a unidade econômica central é a tonelada de sólidos secos, não apenas o volume dragado.

# 2. Produção

## Fatos observados

Entradas principais:

- vazão da centrífuga: 44,19 m³/h;
- eficiência: 80%;
- concentração usada no cálculo de volume processado: 30%;
- percentual de sólidos na entrada: 1,7%;
- jornada: 16 horas por dia;
- 26 dias por mês;
- eficiência operacional adicional de 90% para a vazão operacional.

Resultados observados:

- 416 horas disponíveis por mês;
- 332,8 horas trabalhadas após eficiência;
- 10,6056 m³/h de volume processado na primeira transformação;
- 0,75123 tonelada de sólidos secos por hora;
- 250,009344 toneladas de sólidos secos por mês;
- 2.000,074752 toneladas de sólidos secos totais;
- prazo de operação adotado: 8 meses.

## Interpretação

A produção transforma vazão e teor de sólidos em tonelada seca. Essa unidade passa a ser o driver da proposta comercial e da comparação entre revisões.

## Anomalia de modelagem

A aba mostra também um cálculo de prazo bruto próximo de 12 meses, enquanto o prazo operacional consolidado é fixado em 8 meses. A diferença deve ser entendida com Fabio antes da consolidação do método; pode representar máximo desconto, premissa comercial, uso de mais de uma centrífuga ou outra decisão de capacidade.

# 3. Canteiro e mobilização da equipe

## Fatos observados

A aba possui dois blocos.

### Equipe e turnos

- encarregado;
- líder de operação;
- técnico de segurança;
- operador de draga;
- operador de centrífuga;
- cinco ajudantes;
- refeições e transporte;
- custo diário consolidado de R$ 3.854,939.

A matriz lateral distribui pessoas entre draga e centrífuga e calcula salários com adicional de 25% para funções selecionadas.

### Canteiro, viagens e integração

Inclui:

- mobiliário de canteiro e alojamento;
- PGR, PCMSO e LTCAT;
- ART principal e corresponsáveis;
- itens de segurança;
- exames médicos;
- viagens, hospedagem, alimentação e veículos;
- integração da equipe por 10 dias;
- observação de lead time operacional: documentos, integração, aprovação, entrada e exames.

Custo total observado: R$ 80.099,39.

## Interpretação

O pacote reúne implantação administrativa, conformidade, logística de pessoas e preparação da equipe. Ele não é apenas canteiro físico.

# 4. Mobilização da draga

## Fatos observados

- draga hidráulica de 6 polegadas;
- equipe específica de mobilização;
- três carretas de carga seca;
- treinamentos de trabalho em altura e espaço confinado;
- transferência da draga entre lagoas;
- viagem de ida;
- 22 dias de mão de obra de mobilização;
- guindaste de descarga atribuído ao cliente;
- referência histórica de preço de carreta registrada em observação.

A planilha mantém uma decomposição física das três carretas:

1. draga;
2. tubulação;
3. flutuantes e periféricos.

## Interpretação

A mobilização da draga é independente da mobilização da centrífuga e pode possuir responsabilidades contratuais transferidas ao cliente.

# 5. Mobilização das centrífugas

## Fatos observados

- mobilização de duas centrífugas;
- um operador de centrífuga e quatro ajudantes;
- cobertura, instalações hidráulicas e elétricas;
- verba de eletricista;
- quatro carretas para duas centrífugas;
- bases de concreto;
- transporte de tanques de equalização;
- 22 dias de mão de obra;
- inventário físico: dois skids de centrífuga e dois tanques de equalização.

A aba contém um pequeno dimensionamento de bases de concreto por largura, comprimento e espessura.

## Interpretação

O sistema de desaguamento possui mobilização própria e ativos duplicados. A quantidade de unidades deve ser tratada como premissa explícita do sistema.

# 6. Operação de apoio

## Fatos observados

A aba calcula custo mensal para:

- encarregado;
- líder de operação;
- técnico de segurança;
- operador de draga;
- operador de centrífuga;
- cinco ajudantes;
- refeições;
- fretes e carretos;
- materiais de segurança;
- alojamento e utilidades;
- viagens de folga;
- dois veículos mensais;
- planos de saúde e odontológico;
- inspeções de engenharia;
- comunicação e internet;
- mão de obra de integração/operação por 208 dias.

Custo total observado: R$ 917.209,248.

Preço mensal equivalente observado: R$ 114.651,156 para oito meses.

## Interpretação

Este pacote reúne custos de estrutura e pessoas compartilhados pela operação, enquanto as abas seguintes detalham os centros de custo técnicos da draga e da centrífuga.

# 7. Custo da draga

## Estrutura observada

A aba é um modelo mensal completo com os grupos:

1. operações;
2. pessoal;
3. manutenção;
4. equipamentos de apoio;
5. administrativas;
6. BDI interno;
7. financeiras.

## Operação

- diesel marcado como responsabilidade do cliente;
- consumo teórico indicado por `0,15 × HP × hora`;
- fretes e materiais de segurança permanecem como custo FOS.

## Pessoal

Inclui salários, horas extras, encargos sociais de 110%, refeições, alojamento, viagens e possibilidade de prêmios de produção.

## Manutenção

Registra regras textuais para:

- peças e acessórios como percentual mensal do equipamento;
- docagem anual;
- limpeza e pintura;
- mão de obra de terceiros.

## Equipamentos de apoio

Inclui veículo, medidor de vazão e densidade, gerador, ferramentas, plano de saúde e plano odontológico. Existe composição de linha de recalque, embora zerada neste modelo.

## Administrativas e financeiras

Inclui viagens de inspeção, comunicações, oficina, administração, depreciação, juros e atrasos.

## Resultados observados

- despesas diretas: R$ 62.902,2186749;
- BDI interno registrado no resumo: R$ 3.145,110933745;
- custo mensal: R$ 66.047,329608645;
- custo total para 8 meses: R$ 528.378,63686916;
- preço de venda mensal auxiliar com fator 1,6;
- preço de operação por hora: R$ 177,81973356.

## Anomalias observadas

- algumas referências à aba `Produção` aparecem como `#NAME?` no valor armazenado/importado;
- o cálculo de preço por tonelada seca termina em `#DIV/0!` porque o denominador correspondente está zerado;
- o texto ainda menciona bags em uma linha de resumo, evidenciando reaproveitamento de modelo anterior.

Essas anomalias não impedem compreender a composição mensal da draga.

# 8. Custo da centrífuga

## Estrutura observada

Repete a família de composição da draga:

1. operação;
2. pessoal;
3. manutenção;
4. equipamentos de apoio;
5. administrativas;
6. BDI;
7. financeiras.

## Ativos e referências

A aba registra valores referenciais de:

- centrífuga FOS;
- tanque de equalização FOS;
- centrífuga nova;
- estrutura móvel skid;
- equipamentos GRATT.

## Pessoal

Inclui operador líder, quatro ajudantes e operador de decanter, com salários, encargos, refeições e viagens.

## Equipamentos de apoio

Inclui automóvel, planos de saúde e odontológico, tanque de equalização, mangotes, ferramentas e linha de recalque auxiliar.

## Resultados observados

- despesas diretas: R$ 57.438,73096875;
- custo mensal: R$ 57.438,73096875;
- total para oito meses: R$ 459.509,84775;
- preço de venda mensal auxiliar com fator 1,6;
- preço de operação por hora: R$ 154,64273722.

## Anomalia observada

A célula `D187` contém referência quebrada `#REF! × 0,6 × 0,62`, afetando o campo de hora à disposição. A origem perdida não foi reconstruída por inferência.

# 9. Manutenção preventiva

## Fatos observados

O pacote separa manutenção especializada da manutenção genérica embutida nos equipamentos.

Inclui:

- duas visitas trimestrais de técnico GRATT;
- manutenção mecânica preventiva, incluindo mão de obra de troca de peças;
- possibilidade de reparos elétricos mensais;
- quatro meses de mão de obra de acompanhamento.

Custo total observado: R$ 70.419,756.

Preço unitário para oito meses: R$ 8.802,4695 por mês, antes da consolidação comercial por tonelada seca.

## Interpretação

Manutenção preventiva é um pacote autônomo e não apenas um percentual genérico de equipamento. Esse comportamento precisa ser comparado em outros modelos.

# 10. Desmobilização

## Fatos observados

A aba concentra:

- equipe e custo diário;
- exames médicos;
- viagem de retorno;
- hospedagem, alimentação e veículo;
- logística específica para Aguinaldo;
- sete dias de mão de obra;
- planilha lateral com composição das viagens.

Custo total observado: R$ 45.686,35975.

## Interpretação

A desmobilização é mais focada em pessoas, encerramento de canteiro e retorno da equipe. Os itens físicos de mobilização da draga e centrífuga não são simplesmente espelhados aqui.

# 11. Consolidação detalhada

## Fatos observados

A `Plan. Final` consolida três macroitens:

1. Canteiro de obras;
2. Dragagem e desaguamento por centrífuga;
3. Desmobilização do canteiro.

O item de operação é decomposto em:

- operação da draga;
- operação da centrífuga;
- manutenção dos equipamentos.

## Unidade comercial

A operação é precificada por tonelada de sólidos secos (`TSS`).

Valores observados:

- custo total: R$ 1.184.093,99036916;
- preço de venda: R$ 1.778.425,30354124;
- preço unitário final da operação: R$ 793,73118046 por TSS;
- resultado: R$ 631.426,8800245;
- resultado mensal: R$ 78.928,36000306;
- hora à disposição calculada: R$ 440,96598462;
- faturamento mensal aproximado: R$ 183.441,8496.

## BDI observado

- 50% para canteiro e componentes de operação;
- 55% para desmobilização;
- fator auxiliar de 60% para hora à disposição.

## Interpretação

O BDI não é universal. Ele varia por macroitem e também aparece em cálculos auxiliares.

# 12. Consolidação comercial e revisões

## Fatos observados

A aba `Final` não é apenas uma proposta. Ela preserva histórico de negociação:

- revisão final de 17/04/2026;
- proposta enviada em 20/03/2026;
- proposta enviada em 11/02/2026;
- proposta de 21/01/2026;
- preço inicial de agosto de 2025;
- percentuais de aumento ou desconto entre versões;
- referência ao contrato anterior executado;
- comparação entre preço com equipamento próprio e composição de somente mão de obra.

A revisão final apresenta:

- mobilização de equipe e manutenção de canteiro;
- operação do sistema de dragagem e desidratação, incluindo manutenção;
- desmobilização final;
- total de R$ 1.778.425,30354124.

## Interpretação

O sistema orçamentário precisa preservar versões comerciais, e não somente o estado mais recente. O histórico da negociação é parte do conhecimento econômico da proposta.

# Padrões observados no Modelo 002

1. O orçamento nasce da operação e depois é convertido em preço.
2. Produção e prazo são nós centrais.
3. O método separa draga, centrífuga e manutenção como centros de custo.
4. Custos de apoio compartilhados ficam em pacote próprio.
5. A unidade de venda pode ser tonelada de sólidos secos.
6. Mobilização e desmobilização não são espelhos automáticos.
7. O BDI varia por item.
8. Responsabilidades do cliente podem zerar custos relevantes, como combustível e guindastes.
9. A composição preserva referências de preços, fornecedores e datas.
10. A proposta comercial possui histórico de revisões, descontos e comparações.

# Hipóteses para o crosscheck

- `Dados Obra`, `Produção`, mobilização, operação, desmobilização e consolidação parecem formar um núcleo recorrente.
- Draga e sistema de desaguamento podem ser centros de custo independentes combinados conforme o método construtivo.
- A unidade comercial deve ser configurável por orçamento: volume, tonelada seca, verba, mês, hora ou outra unidade contratual.
- Manutenção pode existir em dois níveis: percentual/estimativa dentro do equipamento e pacote especializado externo.
- Histórico de versões comerciais deve ser entidade própria do futuro sistema.
- Responsabilidade contratual por insumos e equipamentos precisa ser explícita por item.

# Anomalias consolidadas

- referência quebrada em `2.2 Centrífuga!D187`;
- divisão por zero em `2.1. Draga Dec!D205:D206`;
- referências exibidas como `#NAME?` em várias células que apontam para a aba `Produção`;
- texto residual sobre bags dentro da composição da draga;
- diferença entre prazo bruto calculado e prazo operacional adotado;
- campos com quantidade vazia ou zerada que permanecem no template;
- BDI interno de composição e BDI comercial coexistem em níveis diferentes.

Nenhuma dessas anomalias impediu a análise integral.

# Comparação preliminar com o Modelo 001

## Elementos que se repetem

- dados e premissas da obra;
- produção e prazo;
- mobilizações separadas por sistema;
- canteiro e apoio;
- operação técnica;
- manutenção;
- desmobilização;
- consolidação detalhada;
- apresentação comercial.

## Diferenças relevantes

- o Modelo 001 dimensiona bags, células e polímero;
- o Modelo 002 dimensiona e opera centrífugas e tanques de equalização;
- o Modelo 002 separa explicitamente draga, centrífuga e manutenção;
- o Modelo 002 vende principalmente por tonelada de sólidos secos;
- o Modelo 002 contém histórico estruturado de revisões comerciais;
- o Modelo 001 possui maior detalhamento de pacotes construtivos do acondicionamento em bags.

Esta comparação é apenas preliminar. O crosscheck oficial será realizado depois da análise de quantidade suficiente de modelos.

# Próximo passo

Analisar integralmente o próximo modelo de orçamento e criar documento individual. Não definir arquitetura nem implementar antes do crosscheck horizontal.