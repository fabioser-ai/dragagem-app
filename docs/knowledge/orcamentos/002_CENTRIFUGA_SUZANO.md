# Modelo 002 — Dragagem com Desaguamento por Centrífuga — Suzano Aracruz

## Status

- Engenharia reversa vertical concluída para o arquivo analisado.
- Nenhuma implementação funcional foi realizada.
- As interpretações permanecem provisórias até o crosscheck com outros modelos.
- Anomalias do Excel foram registradas, mas não bloquearam a análise.

## Fonte analisada

- Arquivo: `01RF_26 - composição MDO - máx. desc..xlsx`.
- Cliente: Suzano.
- Local: Aracruz — ES.
- Objeto: operação da ETE Aracruz.
- Método observado: dragagem hidráulica com desaguamento mecânico por centrífuga.
- Unidade comercial principal: tonelada de sólidos secos — `TSS`.
- Quantidade comercial usada na revisão final: 2.000 TSS.
- Prazo operacional adotado: 8 meses.

## Regra de evidência

Este documento separa:

- **Fato observado:** conteúdo, valor, fórmula ou dependência presente no Excel.
- **Informação do especialista:** explicação fornecida por Fabio.
- **Interpretação:** leitura conceitual provisória.
- **Hipótese para crosscheck:** possibilidade que depende da comparação com outros modelos.
- **Anomalia observada:** erro, referência quebrada ou incoerência existente no arquivo, sem interromper a engenharia reversa.

## Inventário das abas

| Ordem | Aba | Papel observado |
| --- | --- | --- |
| 1 | `Dados Obra` | Premissas comerciais, operacionais e balanço simplificado de sólidos e volumes. |
| 2 | `Produção` | Produção da centrífuga em TSS, horas produtivas e prazo da operação. |
| 3 | `1. Cant. e Mob Equipe` | Canteiro, mobilização da equipe, integração e custos iniciais de apoio. |
| 4 | `Mob. Draga` | Mobilização física da draga e equipe de montagem. |
| 5 | `Mob Centrífuga` | Mobilização de centrífugas, tanques de equalização e instalações associadas. |
| 6 | `Operação` | Custos gerais mensais da estrutura operacional e administrativa da obra. |
| 7 | `2.1. Draga Dec` | Centro mensal de custo da draga, com pessoal, manutenção, apoio, BDI e hora à disposição. |
| 8 | `2.2 Centrífuga` | Centro mensal de custo do sistema de centrífuga, com pessoal, manutenção, apoio e hora à disposição. |
| 9 | `2.3. manutenção` | Manutenção preventiva especializada das centrífugas e acompanhamento da FOS. |
| 10 | `3. Desmob.` | Desmobilização de equipe, canteiro e estrutura de apoio. |
| 11 | `Plan. Final` | Consolidação técnica de custo e venda por pacote. |
| 12 | `Final` | Histórico comercial das revisões, descontos e preços enviados ao cliente. |

## Fluxo observado

```text
Dados da obra e premissas contratuais
        ↓
Balanço de sólidos e produção da centrífuga
        ↓
Prazo operacional adotado
        ↓
Mobilização de equipe, draga e centrífuga
        ↓
Custos gerais de operação
        ↓
Centros de custo separados: draga, centrífuga e manutenção
        ↓
Desmobilização
        ↓
Consolidação técnica
        ↓
Revisão e negociação comercial
```

O arquivo é sequencial para uso humano, mas contém dependências em rede. Produção, prazo, quantidade de TSS e custos mensais alimentam diversas abas posteriores.

# 1. Dados da Obra

## Fatos observados

A aba reúne:

- proposta e data;
- cliente e contatos;
- objeto e local;
- volume de dragagem;
- tipo de material: lodo de ETE;
- método de bota-fora: centrífuga;
- sistema de medição por preços unitários;
- responsabilidades por canteiro e mobilização;
- jornada e prazo;
- quantidade e turnos de draga e centrífuga;
- eficiência produtiva;
- vazão da centrífuga;
- concentração de entrada;
- percentuais médios de sólidos in situ e após desaguamento;
- tanque de equalização;
- vazões nominais e operacionais;
- produção diária e mensal em TSS;
- volumes mensais dragado e desaguado.

## Modelo físico observado

O arquivo conecta:

```text
Volume dragado
× teor de sólidos in situ
→ massa de sólidos secos

Massa seca
÷ teor de sólidos após desaguamento
→ volume de lodo desaguado
```

A operação é orientada pela quantidade de sólidos secos que a centrífuga consegue processar, não apenas pelo volume hidráulico dragado.

## Interpretação

Esta aba funciona como contrato de premissas do modelo. Ela reúne informações comerciais, operacionais e um balanço simplificado de massa.

## Hipótese para crosscheck

A unidade econômica principal pode variar conforme o método construtivo. No Modelo 001, grande parte do orçamento era orientada por volume e pacotes; neste modelo, a TSS é central.

# 2. Produção

## Fatos observados

A aba calcula:

- vazão nominal da centrífuga;
- eficiência;
- concentração;
- volume processado;
- teor de sólidos na entrada;
- TSS por hora;
- horas trabalhadas por mês;
- produção mensal em TSS;
- prazo teórico;
- prazo operacional adotado.

Valores observados:

- vazão: 44,19 m³/h;
- eficiência produtiva: 80%;
- eficiência operacional auxiliar: 90%;
- jornada: 16 h/dia;
- 26 dias/mês;
- 416 horas calendário/mês;
- 332,8 horas produtivas/mês;
- produção mensal: aproximadamente 250 TSS;
- quantidade total: aproximadamente 2.000 TSS;
- prazo operacional adotado: 8 meses.

## Interpretação

Produção é novamente um nó central, mas a variável produzida muda: neste modelo, o prazo decorre da capacidade de processamento de sólidos secos pela centrífuga.

## Anomalia ou decisão manual observada

O prazo teórico exibido em uma célula não coincide necessariamente com o prazo operacional adotado de 8 meses. Isso indica ajuste executivo, arredondamento ou uso de premissas adicionais não expressas em uma única fórmula.

# 3. Canteiro e Mobilização da Equipe

## Fatos observados

A aba combina:

- composição diária de equipe;
- distribuição de funções por turno;
- mobiliário de canteiro e alojamento;
- documentos legais e de segurança;
- exames médicos;
- viagens e hospedagens;
- veículos;
- integração da equipe;
- total do pacote;
- rateio mensal pelo prazo.

A mão de obra de integração usa 10 dias e inclui observação sobre envio de documentos, aprovação, exames e entrada na planta.

## Interpretação

Diferente do Modelo 001, canteiro e mobilização da equipe aparecem agrupados em um único pacote de entrada.

## Hipótese para crosscheck

A fronteira entre `canteiro`, `mobilização de equipe` e `operação geral` não é universal. O futuro sistema precisa permitir agrupamentos comerciais diferentes sem perder a decomposição interna.

# 4. Mobilização da Draga

## Fatos observados

A aba contém:

- equipe de carga e montagem;
- treinamentos;
- carretas para draga, tubulação e periféricos;
- transferência entre lagoas;
- viagem de ida;
- mão de obra de mobilização;
- itens repassados ou fornecidos pelo cliente.

A estrutura segue o padrão recorrente:

```text
Equipe diária
+ contratações e logística
→ subtotal
→ BDI ou preço do pacote
```

## Observação

O pacote contém três carretas detalhadas ao final. A composição física é preservada mesmo quando a apresentação comercial não exibe esse detalhamento.

# 5. Mobilização da Centrífuga

## Fatos observados

A aba trata:

- equipe de montagem;
- duas centrífugas;
- dois tanques de equalização;
- cobertura;
- instalações hidráulicas e elétricas;
- guindaste;
- eletricista;
- bases de concreto;
- carretas para centrífugas e tanques;
- mão de obra de montagem.

Há memória geométrica simplificada para bases de concreto e área de giro da rosca.

## Interpretação

O método por centrífuga possui sistema operacional próprio, com ciclo de implantação distinto da draga.

## Hipótese para crosscheck

O conceito `sistema de desaguamento` parece reutilizável, mas seus componentes, dependências e drivers variam radicalmente entre bags e centrífuga.

# 6. Operação

## Fatos observados

A aba concentra custos gerais da obra:

- encarregado;
- líder de operação;
- técnico de segurança;
- operador de draga;
- operador de centrífuga;
- ajudantes;
- alimentação;
- alojamento;
- viagens de folga;
- veículos;
- saúde e odontologia;
- inspeções de engenharia;
- comunicação e internet;
- mão de obra durante toda a operação.

O total é rateado pelo prazo de 8 meses para obter custo mensal.

## Interpretação

Esta aba funciona como uma camada de custos gerais compartilhados entre os sistemas de dragagem e desaguamento.

## Hipótese para crosscheck

O futuro modelo poderá precisar distinguir:

- custos compartilhados da obra;
- custos exclusivos da draga;
- custos exclusivos do desaguamento;
- manutenção especializada.

# 7. Centro de Custo da Draga

## Fatos observados

A aba `2.1. Draga Dec` é uma composição mensal extensa, organizada em:

1. operações;
2. pessoal;
3. manutenção;
4. equipamentos de apoio;
5. administrativas;
6. BDI interno;
7. financeiras;
8. resumo;
9. hora à disposição;
10. custo total da operação.

O combustível está zerado e acompanhado da informação de que é responsabilidade da Suzano.

A composição de pessoal inclui:

- salários;
- horas normais e extras;
- encargos sociais de 110%;
- alimentação;
- alojamento;
- viagens de folga;
- prêmio de produção, ainda sem valores.

Equipamentos de apoio incluem automóvel, ferramentas, planos de saúde e odontológico. A linha de recalque é dimensionada separadamente, mas está zerada neste modelo.

O custo mensal observado da draga é aproximadamente R$ 66 mil e o total de oito meses, aproximadamente R$ 528 mil.

## Interpretação

A draga é tratada como centro de custo operacional independente. O modelo preserva tanto custo mensal quanto hora à disposição.

## Anomalias observadas

- Referências entre abas são exibidas como `#NAME?` pelo motor de inspeção utilizado; isso não foi automaticamente classificado como erro real do Excel.
- O cálculo de preço por tonelada seca em `D205` resulta em `#DIV/0!` porque depende de uma célula de horas mensais não resolvida no arquivo inspecionado.
- `D206` propaga o erro anterior.
- O texto `Operação dos Bags` permanece em uma linha, indicando reaproveitamento de template anterior sem atualização integral do rótulo.

# 8. Centro de Custo da Centrífuga

## Fatos observados

A aba `2.2 Centrífuga` repete a estrutura geral da draga, mas com recursos próprios:

- operador de centrífuga e ajudantes;
- alimentação e viagens;
- manutenção mensal;
- automóvel;
- planos de saúde e odontológico;
- tanque de equalização;
- possível locação de segundo decanter;
- linha de recalque auxiliar;
- custos administrativos;
- depreciação e juros, previstos na estrutura.

A planilha também contém valores patrimoniais e de referência:

- centrífuga FOS;
- tanque de equalização FOS;
- referência de centrífuga nova;
- estrutura móvel tipo skid;
- preço sem estrutura.

O custo mensal observado é aproximadamente R$ 57 mil e o total de oito meses, aproximadamente R$ 459,5 mil.

## Interpretação

A centrífuga é tratada como ativo e centro de custo separado. O modelo permite distinguir equipamento próprio, equipamento novo e eventual equipamento locado.

## Anomalia observada

- `2.2 Centrífuga!D187` contém fórmula quebrada `#REF!*0.6*0.62` e resultado `#REF!`.
- A referência original foi perdida e não pode ser reconstruída apenas pelo arquivo.
- A anomalia afeta o campo de hora à disposição, mas não impede compreender o centro de custo mensal nem a consolidação principal.

# 9. Manutenção Preventiva

## Fatos observados

A aba separa a manutenção especializada das centrífugas:

- visitas trimestrais do técnico GRATT;
- manutenção mecânica preventiva;
- possíveis reparos elétricos;
- mão de obra FOS de acompanhamento;
- cotações datadas de janeiro de 2026.

O total é rateado pelos 8 meses, produzindo custo unitário mensal de aproximadamente R$ 8,8 mil.

## Interpretação

Manutenção é um pacote próprio e não apenas percentual genérico sobre o equipamento. O arquivo combina estimativas paramétricas em outras abas com contratação especializada explícita nesta aba.

# 10. Desmobilização

## Fatos observados

A aba reúne:

- equipe de desmobilização;
- retirada do canteiro;
- exames, viagens, hospedagem, alimentação e veículos;
- mão de obra final;
- custos zerados de itens não aplicáveis.

O pacote não é simples cópia da mobilização. Quantidades, duração e componentes são próprios do encerramento.

## Interpretação

Confirma-se o ciclo operacional:

```text
mobilizar
→ operar
→ manter
→ desmobilizar
```

# 11. Planilha Final

## Fatos observados

A consolidação técnica apresenta três grupos comerciais:

1. canteiro de obras;
2. dragagem e desaguamento por centrífuga, subdividido em:
   - operação da draga;
   - operação da centrífuga;
   - manutenção dos equipamentos;
3. desmobilização do canteiro.

A unidade da operação é TSS.

BDIs observados:

- 50% para canteiro;
- 50% para operação da draga;
- 50% para operação da centrífuga;
- 50% para manutenção;
- 55% para desmobilização.

Valores observados na revisão final:

- custo total aproximado: R$ 1,184 milhão;
- preço de venda aproximado: R$ 1,778 milhão;
- valor unitário consolidado da operação: aproximadamente R$ 793,73/TSS;
- resultado operacional calculado: aproximadamente R$ 631 mil;
- resultado mensal calculado: aproximadamente R$ 78,9 mil.

A aba também calcula hora à disposição a partir do custo horário e BDI.

## Interpretação

A consolidação não aplica necessariamente um único BDI global. O BDI pode variar por macroitem e por momento comercial.

# 12. Final — Histórico Comercial

## Fatos observados

A aba preserva diversas versões da proposta:

- proposta inicial de agosto de 2025;
- versão de janeiro de 2026;
- revisão de fevereiro de 2026;
- revisão de março de 2026;
- revisão final de abril de 2026.

Ela compara:

- preço enviado;
- BDI praticado;
- aumento ou desconto entre revisões;
- preço final atual;
- referência de contrato anterior executado;
- cenário somente com mão de obra;
- cenário com equipamento próprio.

A revisão final apresenta três itens:

1. mobilização de equipe e manutenção de canteiro;
2. operação do sistema de dragagem e desidratação de lodo, incluindo manutenção;
3. desmobilização final.

## Interpretação

O arquivo não é apenas ferramenta de engenharia. Ele também funciona como memória da negociação comercial.

## Descoberta relevante

O preço enviado ao cliente pode se afastar do preço técnico calculado por revisões, descontos e estratégia comercial. Portanto, `custo`, `preço técnico`, `preço proposto` e `preço negociado` são conceitos distintos.

# Padrões observados no Modelo 002

## Padrões fortes

1. O orçamento começa por premissas técnicas e contratuais.
2. Produção determina prazo e custos dependentes de tempo.
3. Sistemas de draga e centrífuga possuem centros de custo separados.
4. Custos compartilhados são tratados em uma camada geral de operação.
5. Mobilização e desmobilização são eventos distintos.
6. A manutenção pode ser pacote próprio com fornecedor especializado.
7. A consolidação comercial esconde o detalhamento técnico e apresenta macroitens.
8. A proposta final preserva histórico de revisões e descontos.
9. A unidade comercial pode ser TSS, enquanto cálculos internos utilizam volume, horas, meses e massa seca.
10. Responsabilidades do cliente podem zerar custos sem eliminar o item do método.

# Primeiras diferenças em relação ao Modelo 001

| Tema | Modelo 001 — Bags | Modelo 002 — Centrífuga |
| --- | --- | --- |
| Sistema de desaguamento | Bags e células | Centrífuga e tanque de equalização |
| Driver principal | Volume, área, quantidade de bags e massa seca | Tonelada de sólidos secos e capacidade da centrífuga |
| Dimensionamento específico | Células, bags e polímero | Produção em TSS, centrífugas e equalização |
| Operação | Pacotes separados de sistema, dragagem e bags | Custos gerais + centros de custo da draga e centrífuga |
| Manutenção | Embutida em composições | Pacote especializado próprio |
| Consolidação comercial | Macroitens da solução com bags | Mobilização, operação integrada e desmobilização |
| Negociação | Consolidação final observada | Histórico explícito de revisões, descontos e BDIs |

# Hipóteses para o crosscheck futuro

1. `Dados da obra`, `Produção`, `Mobilização`, `Operação`, `Desmobilização` e `Consolidação` parecem candidatos ao núcleo comum.
2. A unidade comercial deve ser configurável por modelo e contrato.
3. Sistemas de desaguamento devem ser componentes substituíveis, não etapas fixas universais.
4. Custos compartilhados e centros de custo específicos precisam coexistir.
5. O BDI não deve ser tratado como uma única constante global.
6. Responsabilidade contratual precisa ser modelada separadamente do custo físico do item.
7. O sistema futuro deverá preservar histórico de revisões comerciais e não apenas o último preço.
8. Preço técnico, preço enviado e preço negociado devem possuir identidades próprias.
9. Modelos podem carregar resíduos de templates anteriores; a arquitetura não deve inferir domínio apenas pelo rótulo textual.
10. O uso real deverá validar quais parâmetros são mestres, quais são sugestões históricas e quais pertencem apenas à obra.

# Anomalias consolidadas

## Confirmadas no arquivo

- `2.2 Centrífuga!D187` — referência quebrada `#REF!`.
- `2.1. Draga Dec!D205` — divisão por zero.
- `2.1. Draga Dec!D206` — propagação da divisão por zero.

## Limitação de inspeção

O motor utilizado mostrou diversos `#NAME?` em referências entre abas. Esses resultados não foram classificados automaticamente como erros reais, pois podem decorrer da avaliação limitada de fórmulas externas entre planilhas. As fórmulas e dependências foram registradas, mas sua equivalência numérica deverá ser validada no Excel ou no futuro conjunto de testes de referência.

# Conclusão provisória

O Modelo 002 confirma que o futuro sistema orçamentário não pode ser uma sequência rígida de telas baseada no Modelo 001.

Ele precisa representar:

```text
Premissas
→ Produção
→ Sistemas operacionais
→ Custos compartilhados
→ Centros de custo específicos
→ Manutenção
→ Mobilização e desmobilização
→ Consolidação técnica
→ Negociação comercial versionada
```

A evidência é suficiente para documentar o modelo individual, mas ainda não para consolidar uma arquitetura universal. Novos modelos devem ser analisados antes do crosscheck horizontal definitivo.
