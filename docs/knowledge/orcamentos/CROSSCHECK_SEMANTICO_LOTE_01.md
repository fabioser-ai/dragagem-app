# Crosscheck Semântico — Lote Piloto 01

## Escopo e autoridade

Comparação semântica dos modelos `004`, `006`, `007`, `014` e `016`, baseada na leitura integral dos cinco Excel originais e nas análises estruturais já publicadas. Fatos, interpretações e perguntas permanecem separados. O crosscheck confirma padrões do lote, não regras universais da FOS.

## Cobertura confirmada

| Modelo | Família | Abas lidas | Papel econômico dominante |
|---|---|---:|---|
| 004 — Draga 14 SBV | Composição padrão de draga | 8 | m³ + visão mensal |
| 006 — Gerdau Pinda | Batimetria/levantamento | 7 | verba e R$/m² |
| 007 — Klabin Ortigueira | Dragagem com centrífuga | 21 | t seca/mês e cenários de 58 meses |
| 014 — Nutrilog | Dragagem/bombeamento direto | 8 | m³ + verbas |
| 016 — SABESP | Dragagem com bags/geotêxteis | 17 | m³ + pacotes físicos |
| **Total** | cinco famílias representativas | **61** | múltiplas unidades e contratos |

Os SHA-256 coincidem com os documentos individuais. Nenhum Excel foi alterado.

## Núcleo comum confirmado

1. Identificação de proposta, cliente, contato, objeto, local e data.
2. Premissas físicas e operacionais separadas visualmente de resultados.
3. Produção/prazo quando o serviço depende de volume processado.
4. Equipe, salário/custo-hora, horas, encargos, refeições e transporte.
5. Mobilização e desmobilização como pacotes próprios.
6. Composição de custo por quantidade × preço unitário e/ou custo mensal.
7. Separação entre custo técnico, BDI e preço de venda.
8. Consolidação detalhada seguida de resumo comercial simplificado.
9. Dependências entre pacotes, ainda que implementadas por referências diretas de células.
10. Uso de valores zerados tanto para ausência quanto para responsabilidade de terceiro, exigindo semântica explícita no futuro.

## Etapas equivalentes com nomes diferentes

| Conceito | Nomes observados |
|---|---|
| Premissas | `Dados Obra`, campos no `RESUMO` |
| Produção/prazo | `Produção`, `Produção (cliente)`, `Produção (NOVO CALCULO)` |
| Canteiro/equipe | `Canteiro`, `1. Canteiro`, `1. Mobilização` |
| Operação principal | `Dragagem`, `Draga Dec`, `Operação Sistema`, `Centrífuga` |
| Preparação física | `Prep. Célula`, `BASE DE CONCRETO`, `Remoção Ensecadeira` |
| Consolidação | `Plan. Preços`, `Plan. Final`, `RESUMO`, `Final`, `Planilha1` |

O novo método deve mapear conceitos estáveis sem exigir padronização retroativa dos nomes das abas.

## Fórmulas equivalentes

- Horas/mês = horas/dia × dias/mês.
- Produção horária = vazão × eficiência × concentração, com variações de unidade.
- Produção mensal = produção horária × horas disponíveis/produtivas.
- Prazo = quantidade total ÷ produção mensal, frequentemente arredondado para cima para custos mensais.
- Custo de mão de obra = quantidade × custo-hora × horas × encargos.
- Preço total do recurso = quantidade × preço unitário.
- Custo unitário = custo total ÷ quantidade econômica.
- Preço = custo × (1 + BDI), aplicado em níveis diferentes conforme o arquivo.
- Resultado comercial = faturamento/preço − custo, simples nos modelos curtos e por fases na Klabin.

## Diferenças por família

- **Draga padrão/direta:** produção volumétrica, combustível, linha de recalque, manutenção e custo mensal são centrais.
- **Batimetria:** geometria, amostragem, laboratório e terceiros substituem a produção de dragagem; o template de produção pode ser não aplicável.
- **Centrífuga:** massa seca, quantidade de equipamentos, turnos, recuperação de investimento e fases contratuais dominam.
- **Bags:** balanço de sólidos, capacidade de bags, área/célula, geossintéticos e polímero criam dimensionamentos adicionais.
- **Composição padrão de equipamento:** pode existir contratação mensal sem volume final fechado; preço mensal deve ser um resultado de primeira classe.

## Parâmetros comuns e não universais

Recorrentes no lote: horas/dia, dias/mês, eficiência, concentração, encargos, adicionais, consumo, manutenção, docagem, vida útil, juros, atraso, BDI e arredondamento de prazo. A recorrência confirma a necessidade de representação própria, mas não confirma os valores.

Exemplos de divergência que impedem generalização:

- encargos de 110% no modelo 004 e percentuais diferentes em outros;
- BDI de 50%, 70%, 90% de referência ou 100% conforme arquivo/pacote;
- depreciação em 60 meses para draga e 12 meses para centrífuga;
- dosagem de polímero de 3 kg/t seca apenas no SABESP;
- fator líquido de 85% e fases 15 + 43 meses apenas na Klabin;
- plano de 5/8 amostras por tipo de lagoa apenas na Gerdau.

## Pacotes comuns e opcionais

| Pacote | Presença no lote | Regra semântica proposta |
|---|---|---|
| Mobilização | cinco modelos | independente do prazo operacional; pode conter responsabilidades do cliente |
| Canteiro | quatro modelos | mensal ou por prazo; não obrigatório em levantamento simples |
| Operação principal | quatro modelos | draga, centrífuga ou combinação |
| Medição/levantamento | quatro modelos | serviço principal ou pacote auxiliar |
| Preparação/estrutura | SABESP e Klabin | ativável e dimensionável |
| Desaguamento | SABESP e Klabin | tecnologia específica, não etapa universal |
| Transporte/destinação | SABESP e referências em outros | opcional, com distância e responsabilidade |
| Desmobilização | quatro modelos | pacote próprio; não mera cópia da mobilização |

## Resultados comuns

- produção horária/mensal e prazo quando aplicáveis;
- custo de equipe e custo mensal;
- custo por pacote e custo total;
- BDI e preço por pacote;
- preço unitário na unidade econômica do contrato;
- preço total e resumo comercial;
- resultado/margem, simples ou por fase.

O sistema precisa suportar múltiplas unidades econômicas simultâneas: m³, t seca, m², mês, hora, peça e verba.

## Inconsistências e riscos transversais

- Herança de templates deixa títulos incompatíveis com o serviço real.
- Datas internas, nomes de arquivo e cotações podem divergir.
- Valores e percentuais aparecem embutidos em fórmulas ou notas laterais.
- Zero é semanticamente ambíguo: não aplicável, fornecido pelo cliente, pendente ou valor real zero.
- BDI pode existir na composição e no consolidado, criando risco de dupla incidência.
- Arredondamento de prazo afeta custos mensais e pode diferir do prazo técnico.
- Klabin contém dois `#DIV/0!` e um `#REF!`; Gerdau contém 12 `#DIV/0!` por entradas/divisores zerados. Esses estados não foram corrigidos.
- Cotações históricas não possuem política uniforme de validade.

## Hipóteses do Método FOS provisório confirmadas

- O orçamento é rede de dependências, não formulário linear.
- Pacotes técnicos e econômicos precisam ser ativáveis.
- Valor sugerido, valor adotado, origem e resultado calculado devem ser separados.
- Cadastro mestre precisa gerar fotografia por versão.
- Fórmulas devem ser explicáveis e rastreáveis.
- Resumo comercial não substitui a memória técnica.
- Regras observadas em um arquivo não podem virar universais sem validação horizontal.

## Hipóteses contrariadas ou refinadas

- Produção/prazo não é etapa obrigatória para toda família: em batimetria pode ser residual e não aplicável.
- Volume em m³ não é unidade econômica universal; t seca, m² e mês podem comandar o contrato.
- BDI único global não representa os modelos observados; é necessário suportar incidência por pacote e validar duplicidades.
- Um orçamento não possui necessariamente uma única curva econômica: Klabin exige fases contratuais.
- Desmobilização não deve ser gerada automaticamente como espelho da mobilização; valores e responsabilidades diferem.

## Decisão de produto — desempenho e experiência

Decisão aprovada pelo Fabio:

> O Novo Sistema de Orçamentos deve ser rápido, fluido, previsível e com o mínimo possível de recarregamentos visíveis.

Implicações documentais para a arquitetura futura:

- painel carrega apenas resumos e abre detalhes sob demanda;
- catálogos são lidos uma vez por contexto válido e possuem invalidação explícita;
- dependências acima formam o grafo de recálculo: alteração recalcula somente resultados descendentes;
- pacotes independentes não são recalculados quando uma premissa não os afeta;
- persistência preserva orçamento, etapa, seleção e posição;
- leituras idênticas não se repetem na mesma renderização;
- chamadas ao GitHub são agrupadas e reduzidas;
- operações demoradas mostram estado/progresso;
- `st.rerun()` é excepcional, documentado e testado contra ciclos, piscadas e perda de contexto;
- Kid Steps com risco de lentidão incluem medição de tempo, chamadas externas e reruns visíveis.

Desempenho percebido passa a integrar a homologação funcional junto com a correção matemática.

## Decisões que dependem do Fabio

1. Quais percentuais de BDI representam política, negociação específica ou margem de segurança?
2. Zero deve exigir motivo (`não aplicável`, `cliente`, `pendente`, `zero real`)?
3. Qual política de arredondamento de prazo deve valer para equipe/canteiro e para o prazo apresentado?
4. Como distinguir produção contratual, garantida, estimada pelo cliente e adotada pela FOS?
5. Água, energia, estrutura e apoio fornecidos pelo cliente devem aparecer como exclusões ou responsabilidades no resumo?
6. Qual validade mínima de cotações e como atualizar preço sem alterar versões emitidas?
7. Os custos financeiros e de manutenção devem ser parâmetros corporativos, por equipamento ou por orçamento?
8. Como representar contratos por fase, mínimos mensais e recuperação de investimento?

## Pontos ainda não cobertos

- validação dos coeficientes por especialistas;
- comparação com realizados de obra;
- impostos e regime fiscal por proposta;
- aprovação interna e limites de margem;
- versionamento de cotações e moedas;
- permissões para custos, salários e margens;
- regras de emissão/revisão da proposta;
- famílias não representadas no lote e o arquivo legado `.xls`.

## Encerramento do lote

O lote explicita um método repetível: identificar finalidade e unidade econômica; reconstruir o fluxo lógico; separar entradas, sugestões, fórmulas, pacotes e resultados; traduzir fórmulas; mapear dependências; registrar tratamento comercial; distinguir fatos, interpretações, riscos e perguntas. Nenhuma arquitetura física ou implementação é autorizada por este documento.
