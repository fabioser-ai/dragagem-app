# Vocabulário Oficial do Domínio de Orçamentos

## Status e regra de uso

Vocabulário documental consolidado na Fase 3 a partir dos 49 modelos, do Método FOS provisório e dos crosschecks estrutural e semântico.

As definições abaixo fixam significado de domínio para comunicação e documentação. Elas não definem tabela, coluna, classe, tela ou arquitetura física. Quando um Excel usa o mesmo termo com significado diferente, o documento individual deve registrar a divergência.

## Identidade, ciclo e rastreabilidade

| Conceito | Definição oficial |
|---|---|
| **Orçamento** | Processo identificado de estudo e formação de escopo, custo e preço para uma oportunidade/objeto. Mantém identidade mesmo quando revisado. |
| **Versão do orçamento** | Fotografia reproduzível de entradas, decisões, cálculos, cotações, resultados e apresentação em determinado momento. Revisão gera nova versão. |
| **Modelo de origem** | Excel ou outra fonte histórica usada como evidência de conhecimento. Não é automaticamente template oficial. |
| **Família de orçamento** | Conjunto de modelos com objetivo técnico/econômico e cadeia de pacotes suficientemente semelhantes para comparação. |
| **Cenário** | Combinação alternativa de premissas, equipamentos, turnos, pacotes ou condições comerciais comparada sem apagar as demais. |
| **Revisão** | Nova versão decorrente de alteração rastreável. Não substitui silenciosamente a versão anterior. |
| **Estado** | Situação do orçamento/versão no ciclo de trabalho; não se confunde com etapa de cálculo. |
| **Histórico de alteração** | Registro de autor, momento, valor anterior, valor novo, origem e motivo disponível. |
| **Evidência** | Dado observável em fonte, fórmula, cotação, documento ou decisão registrada. |
| **Interpretação** | Explicação apoiada por evidência, mas ainda dependente de validação quando a intenção não é explícita. |
| **Hipótese** | Possível regra ou significado ainda não confirmado. Nunca deve operar como regra definitiva. |
| **Exceção** | Situação válida que foge ao padrão da família e precisa ser suportada sem virar regra geral. |

## Estrutura do método

| Conceito | Definição oficial |
|---|---|
| **Etapa** | Unidade lógica de elaboração, análise ou validação. Pode consumir e produzir informações. |
| **Pacote** | Bloco técnico/econômico ativável, como mobilização, canteiro, dragagem, desaguamento ou medição. |
| **Composição** | Formação auditável do custo/preço de um item, recurso ou pacote por quantidades, incidências e valores unitários. |
| **Item** | Linha quantificável ou apresentável dentro de pacote, composição ou resumo. |
| **Submodelo** | Cálculo coeso reutilizável, como produção, linha de recalque, equipe, célula ou balanço de massa. |
| **Aplicabilidade** | Decisão explícita de que etapa/pacote/item se aplica ou não ao cenário, com motivo. Não aplicável não significa apagado. |
| **Dependência** | Relação em que alteração de uma entrada/resultado exige revisar ou recalcular outro resultado/pacote. |
| **Grafo de dependências** | Representação conceitual das dependências usada para identificar somente os resultados afetados. |
| **Núcleo comum** | Conceitos e comportamentos confirmados em várias famílias e candidatos a suporte transversal. |
| **Regra da família** | Padrão recorrente dentro de uma família, ainda sujeito a variações e validação. |

## Dados, valores e origem

| Conceito | Definição oficial |
|---|---|
| **Entrada** | Informação fornecida ou confirmada para o orçamento. |
| **Premissa** | Entrada assumida para cálculo ou decisão, com unidade, origem e responsável. |
| **Parâmetro** | Grandeza usada por fórmula ou decisão; pode ser informada, sugerida ou adotada. |
| **Constante embutida** | Número escrito diretamente em fórmula. Deve ser identificado e não generalizado sem validação. |
| **Valor sugerido** | Referência apresentada a partir de catálogo, histórico, política ou modelo. Não substitui a decisão do engenheiro. |
| **Valor adotado** | Valor efetivamente escolhido para a versão, preservando sugestão/origem e justificativa quando diferente. |
| **Valor calculado** | Resultado determinístico produzido a partir de entradas e fórmula identificadas. |
| **Valor informado pelo cliente** | Dado de origem externa mantido separado do valor adotado pela FOS. |
| **Valor histórico** | Evidência de orçamento/obra anterior; não é automaticamente sugestão atual. |
| **Origem** | Fonte do valor: cliente, engenheiro, catálogo, cotação, histórico, política, fórmula ou terceiro. |
| **Vigência** | Período em que preço, salário, taxa ou parâmetro é considerado válido. |
| **Fotografia** | Cópia contextual de cadastro/cotação usada por uma versão, imune a alterações futuras do mestre. |
| **Catálogo** | Conjunto administrado de opções reutilizáveis, com identidade, unidade, estado e vigência quando aplicável. |
| **Cotação** | Evidência comercial datada de fornecedor, escopo, unidade, preço, condição e contato. |
| **Responsabilidade** | Parte encarregada de fornecer/executar/custear item: FOS, cliente, terceiro ou outra definida. |
| **Zero real** | Valor numérico intencionalmente igual a zero. Deve ser distinguido de não aplicável, fornecido pelo cliente e pendente. |
| **Pendente** | Informação necessária ainda não confirmada. Não equivale a zero. |

## Engenharia e produção

| Conceito | Definição oficial |
|---|---|
| **Volume in situ** | Volume do material em sua condição original no local. |
| **Volume de polpa** | Volume transportado como mistura de sólidos e líquido. |
| **Volume desaguado** | Volume do material após retirada parcial de água. |
| **Massa seca / tonelada seca** | Massa de sólidos sem a parcela líquida, usada para produção, polímero ou cobrança. |
| **Teor de sólidos** | Fração/percentual de sólidos em uma mistura; deve informar base de medição. |
| **Vazão nominal** | Capacidade declarada do equipamento em condição de referência. |
| **Vazão operacional** | Vazão adotada/esperada nas condições do orçamento. |
| **Eficiência** | Fator que representa aproveitamento da capacidade; sua definição e base devem ser explícitas. |
| **Concentração** | Relação de sólidos usada no cálculo de produção; unidade/base não pode ser inferida apenas do rótulo. |
| **Horas disponíveis** | Janela total de disponibilidade prevista. |
| **Horas trabalhadas** | Horas em que equipe/equipamento está em atividade, antes ou depois de critérios especificados. |
| **Horas produtivas** | Parcela efetivamente usada para gerar produção após paradas/perdas definidas. |
| **Produção horária** | Quantidade produzida por hora na unidade adotada. |
| **Produção mensal** | Produção do período, derivada da produção horária e horas produtivas. |
| **Prazo técnico** | Quantidade total dividida pela produção adotada, antes de arredondamentos comerciais. |
| **Prazo custeado** | Período usado para incidência de custos mensais, com arredondamento explícito. |
| **Capacidade nominal** | Limite declarado de equipamento, bag ou sistema. |
| **Capacidade adotada** | Capacidade usada no orçamento após eficiência, segurança, experiência ou restrição. |
| **Gargalo** | Componente cuja capacidade limita a produção do sistema. |
| **Linha de recalque** | Conjunto de tubulações/acessórios que transporta a polpa; pode ter trechos flutuantes e terrestres. |
| **Barrilete** | Conjunto de distribuição/controle da linha, com tubos, válvulas, mangueiras e acessórios. |
| **Booster** | Bomba/equipamento auxiliar usado para vencer distância/desnível ou manter desempenho. |

## Soluções técnicas

| Conceito | Definição oficial |
|---|---|
| **Dragagem direta** | Remoção e recalque ao destino sem desaguamento central obrigatório por bags ou centrífuga. |
| **Desaguamento** | Processo de redução de água do material dragado. |
| **Bag geotêxtil** | Elemento permeável de contenção/desaguamento com dimensões e capacidade próprias. |
| **Célula de desaguamento** | Área preparada para receber bags/fluxos, podendo conter PEAD, geotêxtil drenante, brita e drenagem. |
| **Paliçada/bacia** | Estrutura alternativa de contenção/recepção do material, com regras físicas próprias. |
| **Centrífuga** | Equipamento de separação sólido-líquido por rotação, dimensionado por capacidade e regime operacional. |
| **Polímero** | Reagente usado para favorecer separação/desaguamento, definido por produto, dosagem, preço e condição de aplicação. |
| **Dosagem** | Quantidade de reagente por unidade de massa/volume, preferencialmente validada por ensaio. |
| **Batimetria** | Levantamento das cotas/profundidades para geometria, volume, medição ou projeto. |
| **Amostragem** | Coleta planejada de material, com quantidade, local, método e finalidade. |
| **Medição** | Determinação contratual/técnica da quantidade executada; método deve ser explícito. |
| **Destinação** | Recebimento/tratamento/disposição final do material, com responsabilidade, distância e taxa. |

## Recursos, incidência e custos

| Conceito | Definição oficial |
|---|---|
| **Recurso** | Mão de obra, equipamento, material, insumo, serviço de terceiro, logística ou despesa usado por composição. |
| **Categoria de recurso** | Classificação que determina semântica e controles, sem alterar a identidade do recurso. |
| **Unidade** | Grandeza de medição do valor: m³, t, kg, m², m, h, dia, mês, peça, viagem, verba etc. |
| **Incidência** | Forma temporal/produtiva de aplicação: única, horária, diária, mensal, por quantidade ou percentual. |
| **Custo unitário** | Custo por unidade, antes da política comercial salvo indicação explícita. |
| **Custo mensal** | Custo recorrente por mês do cenário/pacote. |
| **Custo total** | Soma dos custos aplicáveis na versão/cenário. |
| **Custo direto** | Custo atribuível diretamente ao serviço/pacote conforme regra registrada. |
| **Custo indireto** | Custo compartilhado/administrativo cuja incidência precisa ser explícita. |
| **Custo fixo** | Não varia diretamente com a quantidade dentro do cenário considerado. |
| **Custo variável** | Varia com produção, tempo, consumo ou quantidade. |
| **Mobilização** | Pacote de preparação, deslocamento, chegada e montagem de equipe/equipamentos. |
| **Desmobilização** | Pacote de desmontagem, retirada e retorno; não é automaticamente espelho da mobilização. |
| **Canteiro** | Estrutura temporária de apoio, documentação, segurança, instalações e serviços de obra. |
| **Manutenção** | Recursos para manter equipamento disponível; taxa/base/período devem ser explícitos. |
| **Depreciação** | Alocação do valor depreciável ao longo da vida/período adotado. |
| **Juros de capital** | Custo do capital aplicado, separado de BDI e margem. |

## Formação comercial

| Conceito | Definição oficial |
|---|---|
| **Preço unitário** | Preço de venda por unidade econômica. |
| **Preço total** | Valor comercial total da versão/cenário. |
| **BDI** | Incidência comercial/indireta declarada sobre base definida. Não é sinônimo automático de margem. |
| **Markup** | Multiplicador aplicado ao custo para obter preço; deve explicitar componentes. |
| **Margem** | Relação entre resultado e receita conforme base declarada. |
| **Desconto** | Redução entre preço de referência e preço adotado. |
| **Contingência** | Reserva explícita para risco/incerteza, separada de erro ou arredondamento. |
| **Faturamento mínimo** | Receita mínima contratual por período/quantidade, independente do realizado dentro das condições. |
| **Resultado** | Receita/preço menos custos conforme escopo e período definidos. |
| **Fase contratual** | Intervalo com premissas, custos ou receitas próprios, como implantação e operação recorrente. |
| **Unidade econômica** | Unidade que governa cobrança/comparação: m³, t seca, m², mês, hora, verba etc. |
| **Resumo técnico** | Consolidação destinada à análise interna, preservando pacotes, quantidades e dependências. |
| **Resumo comercial** | Apresentação simplificada ao cliente, sem apagar a memória técnica que a sustenta. |
| **Exclusão** | Item explicitamente fora do escopo/preço, com responsabilidade quando conhecida. |

## Qualidade, validação e experiência

| Conceito | Definição oficial |
|---|---|
| **Validação** | Regra que confirma, alerta ou bloqueia inconsistência de entrada, cálculo ou decisão. |
| **Alerta** | Sinal não bloqueante de risco, desvio, vigência ou incoerência. |
| **Erro de fórmula** | Resultado inválido do mecanismo de cálculo, como `#REF!` ou `#DIV/0!`; não prova sozinho erro de negócio. |
| **Inconsistência** | Divergência observada entre rótulo, unidade, fórmula, valor, data ou dependência, pendente de interpretação. |
| **Arredondamento** | Política explícita de conversão numérica; deve preservar valor original e regra. |
| **Cache** | Reaproveitamento controlado de dados/resultados com política de invalidação. Não é fonte oficial. |
| **Invalidação** | Condição que torna cache/resultado obsoleto após alteração de entrada, catálogo ou dependência. |
| **Recalculo incremental** | Atualização somente dos resultados descendentes afetados por uma mudança. |
| **Rerun visível** | Nova renderização perceptível que pode causar espera, piscar ou perda de contexto; não deve ser solução padrão. |
| **Continuidade de contexto** | Preservação de orçamento, versão, etapa, seleção e posição durante edição e persistência. |

## Distinções obrigatórias

- Orçamento ≠ versão.
- Cadastro mestre ≠ fotografia usada pela versão.
- Valor sugerido ≠ valor adotado ≠ valor calculado.
- Valor do cliente ≠ decisão FOS.
- Zero real ≠ não aplicável ≠ fornecido pelo cliente ≠ pendente.
- Custo ≠ preço.
- BDI ≠ margem ≠ markup ≠ desconto ≠ contingência.
- Prazo técnico ≠ prazo custeado.
- Capacidade nominal ≠ capacidade adotada ≠ produção garantida.
- Volume in situ ≠ volume de polpa ≠ volume desaguado ≠ massa seca.
- Mobilização ≠ desmobilização.
- Resumo comercial ≠ memória técnica.
- Família de orçamento ≠ template físico de planilha.

## Governança do vocabulário

Novo termo só deve ser oficializado quando:

1. houver significado necessário não coberto;
2. a evidência de origem estiver registrada;
3. não criar sinônimo ambíguo;
4. unidade e fronteira conceitual estiverem claras;
5. impacto nas famílias e documentos existentes for reconciliado.

Termos históricos dos Excel podem permanecer citados, mas devem apontar para o conceito oficial correspondente e registrar divergências.

