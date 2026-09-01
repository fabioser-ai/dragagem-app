# Catálogo e anatomia dos blocos V1

**Status:** proposta para checkpoint; não homologada  
**Base:** auditoria fechada de 12 unidades (U01–U12), decisões pós-checkpoint 1 e diretriz de UX V1  
**Escopo:** domínio funcional do novo módulo de Orçamentos; sem implementação

## 1. Objetivo

Este documento transforma as evidências das 12 unidades auditadas em uma proposta conservadora de catálogo e anatomia de blocos para a V1. Estão homologados: **Dragagem é bloco macro próprio, independente e selecionável**; **Bombeamento integra Dragagem**; **Mobilização e Desmobilização são blocos independentes**; **Batimetria é bloco independente**; **Laboratório / Análises de Material é outro bloco independente**; e **Medição é bloco próprio, opcional e selecionável**. O catálogo contém doze entradas: seis blocos homologados e seis candidatos. As demais fronteiras, anatomias e normalizações continuam pendentes até decisão explícita de Fabio/Merlin.

Um **bloco** é uma etapa ou serviço macro que o engenheiro pode incluir, ordenar, repetir e parametrizar em um orçamento. Abas históricas não viram automaticamente blocos. Componentes internos, memórias de cálculo, consolidações e documentos de saída são mapeados, mas não expostos como cartões independentes sem evidência funcional.

## 2. Premissas e restrições

Regras vigentes usadas como restrições:

- cada orçamento é independente; alternativas são orçamentos separados, criados inclusive por duplicação, sem vínculo vivo;
- o sistema não escolhe a solução de engenharia;
- o catálogo de blocos é fluido e administrável; configuração, anatomia e componentes podem evoluir, e blocos usados podem ser inativados, não apagados;
- um orçamento aceita várias instâncias do mesmo bloco, cada uma com rótulo operacional;
- dados mestres aceleram o preenchimento, mas não bloqueiam ajuste contextual;
- o fechamento da proposta cria versão formal, imutável e rastreável; revisão posterior deriva nova versão;
- a evolução do catálogo não altera retroativamente os orçamentos: cada versão preserva a configuração e os valores efetivamente utilizados;
- a V1 preserva familiaridade com Excel e equivalência funcional, sem reproduzir suas fragilidades.

As conclusões se limitam a U01–U12. Não houve ampliação da amostra. Apenas os blocos e fronteiras expressamente indicados como homologados possuem esse status; os demais nomes continuam candidatos.

**Regra metodológica homologada:** não agrupar conceitos no mesmo bloco apenas por afinidade semântica. A modelagem prioriza serviços efetivamente praticados pela FOS, estrutura funcional observada, conhecimento de domínio confirmado por Fabio e familiaridade operacional de quem trabalha com os Excel. Afinidade conceitual, isoladamente, não cria bloco nem dependência.

### 2.1 Classes de campo

| Classe | Definição operacional | Regra de snapshot |
|---|---|---|
| **Mestre (M)** | Catálogo reutilizável: ativo, insumo, função, item, coeficiente técnico ou regra corporativa. | Copiar para a versão quando influenciar cálculo, compromisso ou descrição emitida. |
| **Contextual (C)** | Premissa ou escolha específica da obra, do orçamento, da instância ou da responsabilidade contratual. | Obrigatório no fechamento da proposta. |
| **Derivado (D)** | Resultado calculado a partir de campos rastreáveis; não deve ser digitado silenciosamente. | Recalculável durante edição; congelar valor, fórmula/versão e dependências na versão formal. |
| **Histórico (H)** | Cotação, preço, índice, alíquota, salário, benchmark, valor negociado ou dado válido em certo momento. | Obrigatório com data/vigência, fonte e unidade. |
| **Híbrido** | Campo cujo núcleo vem do mestre, mas recebe escolha/override contextual ou vigência histórica. | Guardar referência, valor copiado, override, justificativa e origem. |

“Snapshot: sim” significa preservar o valor efetivamente usado, sua unidade, origem e, para derivados, a regra aplicada. Não significa duplicar dados sem proveniência.

## 3. Matriz abas históricas × blocos

### 3.1 Evidência por obra

Legenda: **P** presente; **I** presente como componente interno; **C** camada compartilhada; **?** ocorrência histórica agrupada cuja função não pode ser separada com segurança; **—** sem evidência relevante. A matriz registra função observada, não homologa o catálogo.

| Unidade oficial do Checkpoint 1 | Mobilização | Desmobilização | Canteiro | Dragagem¹ | Célula | Bags | Desag. mecânico | Batimetria² | Laboratório/análises³ | Medição⁴ | Transporte/destinação | Venda equipamento | Camadas compartilhadas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| U01 International Paper 2017 | P | P | P | P | P | P | P | — | — | — | R | — | escopo, balanço, produção, preço, proposta |
| U02 CAESB 2017 — venda FC-001 | — | — | — | — | — | — | — | — | — | — | R | P | escopo, preço, proposta |
| U03 Vale Maravilhas I 2019 | P | P | P | P | P | — | — | — | P | P | P | — | condições, balanço, produção, tributos, proposta |
| U04 Mosaic 2020 — “só bombeamento” | P | P | P | P | — | — | — | P | — | P | — | — | escopo, produção, preço, proposta |
| U05 Bosch 2021 — bags | P | P | P | P | P | P | — | — | P | P | P | — | balanço, produção, BDI, proposta |
| U06 Matinhos/CFF 2021 | P | P | P | P | — | — | — | ? | P | ? | P | — | edital/CFF, produção, preço, proposta |
| U07 Petrobras 2022 — DFP/PPU | P | P | P | P | — | — | P | ? | P | ? | P | — | balanço, produção, preço, proposta |
| U08 Suzano Aracruz 2023 | P | P | P | P | — | — | P | ? | P | ? | R | — | escopo, balanço, produção, preço, proposta |
| U09 Venda FC-001 2024 | — | — | — | — | — | — | — | — | — | — | R | P | configuração, preço, proposta |
| U10 Suzano 2024 — Modelo 02 | P | P | P | P | — | — | P | ? | P | ? | P | — | balanço, produção, ABC, tributos, proposta |
| U11 Bracell 2025 — COM/SEM polímero | P | P | P | P | P | P | — | — | P | P | — | — | balanço, produção, BDI, proposta |
| U12 SK Confins 2026 — centrífuga | P | P | R | R | — | — | P | — | P | — | R | — | balanço, produção, BDI, proposta |

¹ A coluna Dragagem absorve as ocorrências históricas de bombeamento/recalque. **R** significa residual, zerado ou de responsabilidade de terceiro.  
² O Checkpoint 1 agrupou “Batimetria/medição”. U04 possui Batimetria explicitamente identificada; U03, U05 e U11 possuem Medição explicitamente identificada. Em U06–U08 e U10, **?** preserva a ocorrência agrupada sem atribuí-la por inferência a apenas um dos blocos.  
³ A coluna reproduz as ocorrências de “Laboratório / análises de material” sustentadas pela matriz e decomposição do Checkpoint 1, retirando “qualidade/garantias” do agrupamento.
⁴ Medição explícita em U03, U04, U05 e U11; a ocorrência consolidada de U06–U08 e U10 permanece **?** por insuficiência para decompor sua função específica.

### 3.2 Linhagem e divergências que condicionam o desenho

| Unidade | Linhagem representativa | Divergência/risco preservado |
|---|---|---|
| U01 | International Paper 2017; ramos paralelos GEOBAGS Rev.01 e Decanter Rev.2; saídas D_035/D_034 Rev.01 | os ramos não formam revisão única; referências internas a Klabin/WestRock, quando presentes nos artefatos auditados, são evidência de contaminação e não alteram a identidade International Paper. |
| U02 | CAESB 2017 — venda FC-001; composição de venda e PDF 0043/2017 | planilha e PDF reconciliam; arquivo `.pages` de 2021 é cópia tardia. |
| U03 | custo Rev2→Rev4, técnica e proposta R3 | planilha contratual e proposta R3 têm totais diferentes. |
| U04 | memória, técnica e oferta “só bombeamento” | usa draga e descreve dragagem; memória calculou R$ 370.432,93 e oferta emitiu R$ 373.000,00. |
| U05 | cenários A–D e finais | sequência de arquivos não representa progressão linear confiável. |
| U06 | Matinhos/CFF: edital/CFF, composição FOS de 12/08 e D_067R1 | edital/CFF e composição privada são linhagens relacionadas e distintas; ABC não foi localizado explicitamente. |
| U07 | Petrobras 2022: DFP FOS final, PPU de R$ 33,088 milhões e memória posterior | memória posterior de R$ 32,580 milhões diverge; versões não são intercambiáveis. |
| U08 | Suzano Aracruz 2023: `Dragagem + Centrifuga.xlsx` e D_005_2023 | 31.200 m³ na composição versus 72.000 m³/12.000 t na proposta. |
| U09 | Venda FC-001 2024: composição de venda; `.pages` não legível | PDFs D_036 pertencem a outra obra e são contaminação, não identidade da unidade. |
| U10 | Modelo 02 e D_026_2024 | identidade corrigida para Suzano; cenários e referências coexistem. |
| U11 | COM/SEM polímero R02 | capacidade dos 28 bags excede demanda por só 9 m³; linha de 31,98 bags não concilia. |
| U12 | memória e oferta de centrífuga | duas produções incompatíveis, `#REF!` e divergências de jornada, prazo e unidade. |

### 3.3 Mapeamento histórico → bloco V1

| Nome/aba/conceito histórico | Unidade/finalidade | Bloco V1 proposto | Papel | Evidência | Confiança / divergência |
|---|---|---|---|---|---|
| `Dados Obra`, dados básicos, objeto, condições | texto, m³, t, m, %, dias; definir escopo | **Camada Dados do orçamento** | compartilhada | U01–U12 | alta; unidades e bases devem ser explícitas. |
| `Produção`, balanço, prazo, cronograma | m³/h, tSS/mês, meses | **Hipótese: motor técnico compartilhado + seção do bloco consumidor** | interno/compartilhado candidato | U01, U03–U08, U10–U12 | alta para a necessidade de reconciliação; propriedade e UX seguem em gray area. |
| Mob. Draga, Mob. MO, Mob. Centrífuga, implantação | R$/evento, viagens, dias, pessoas | **Mobilização** | principal | U01, U03–U08, U10–U12 | **homologado como bloco independente**; composição própria. |
| DesMob. Draga, DesMob. Centrífuga, retirada | R$/evento, viagens, dias, pessoas | **Desmobilização** | principal | U01, U03–U08, U10–U12 | **homologado como bloco independente**; não deriva de Mobilização. |
| `Canteiro`, administração local, site/SSMA | R$/mês, mês, vb | **Canteiro e apoio local** | principal | U03–U08, U10–U12 | alta; responsabilidades podem zerar itens sem eliminar o bloco. |
| Draga, dragagem consolidada, custo mensal draga | m³/h, h, L/h, R$/mês | **Dragagem** | principal independente | U01, U03–U08, U10–U11; residual em U12 | **homologado como bloco macro próprio**; recursos diretamente necessários à execução ficam em sua composição. |
| bombeamento, recalque, retorno de água, Pond 1→Pond 2 | m³/h, mca, m, kW | modalidade/configuração de **Dragagem** | interno | U03, U04, U06–U07, U10 | **homologado:** não é bloco macro independente; “só bombeamento” preserva-se como alias histórico. |
| linha de recalque, barrilete, tubulação, mangotes, flutuantes e acessórios | m, pol, pç, R$ | componente de **Dragagem** | interno | U01, U03–U08, U10–U12 | **homologado quanto à fronteira com Dragagem**; presença e composição variam por instância. |
| `Prep Célula`, PEAD, Bidim, brita | m², m³, h, R$ | **Preparação de célula** | principal | U05–U08, U11 | alta. |
| `Bags`, geotêxtil, dois níveis | un, m, m³, R$/m² | **Bags geotêxteis** | principal | U05–U08, U11 | alta; dimensionamento exige margem e conciliação. |
| centrífuga, decanter, operação/manutenção | m³/h, % ST, tSS, R$/mês | **Desaguamento mecânico** | principal candidato | U01, U07–U08, U10, U12 | alta como família observada; fronteira/nome ainda candidatos. |
| batimetria | campanha, mês, R$ | **Batimetria** | principal independente | U04 explícita; U06–U08 e U10 permanecem inconclusivas por agrupamento histórico | **homologado como bloco independente**; não implica Medição nem Laboratório. |
| amostra, análise de material, granulometria, teor de sólidos e ensaio | amostra, un/mês, %, índice, R$/un | **Laboratório / Análises de Material** | principal independente | U03, U05–U08, U10–U12 | **homologado como bloco independente**; campos limitados à evidência existente. |
| medição, planilha contratual, controle, coleta/acompanhamento | m³, t, tSS, mês, evento, dia, vb, R$ | **Medição** | principal independente | U03–U05 e U11 explícitas; U06–U08 e U10 inconclusivas no agrupamento histórico | **homologado como bloco próprio, opcional e selecionável**; métodos e bases variam por instância. |
| transporte, frete, caçamba, destinação | t, m³, km, viagem, R$/t | **Transporte e destinação** | principal candidato | U03, U05–U07, U10; residual em U01–U02, U08–U09, U12 | média-alta; fronteira, responsabilidades e bases variam. |
| venda FC-001, configuração técnica | un, R$, características | **Venda de equipamento** | principal especializado candidato | U02, U09 | alta para existência; média para fronteira com serviço. |
| polímero, preparador, dosador, operação da planta | kg/tSS, kg, R$/kg | componente do bloco técnico | interno | U03, U05, U07, U11 | alta; cenário SEM de U11 ainda contém operação de apoio. |
| mão de obra, encargos, benefícios, EPI | pessoas, h, %, R$ | componente interno dos blocos | interno | transversal | decisão anterior registrada: não criar bloco global; detalhamento permanece candidato. |
| ativos, apoio, combustível, manutenção, depreciação | h, L/h, %, R$ | componente de custo do bloco | interno | transversal | alta. |
| ABC, BDI, impostos, lucro, `Plan. Final` | %, R$, R$/un | **Formação de preço compartilhada** | compartilhada | transversal | alta; bases variam e não devem ser uniformizadas sem regra. |
| proposta, revisão, preço negociado | documento, R$, data | **Versão formal/saída** | compartilhada | transversal | alta; não é bloco selecionável. |

## 4. Catálogo enxuto proposto para V1

| ID candidato | Nome | Aliases históricos | Finalidade | Unidades de evidência | Combinação/independência | Múltiplas instâncias | Conf. | Não resolvido |
|---|---|---|---|---|---|---:|---:|---|
| B01 | Mobilização | Mob., implantação, entrada | precificar logística, itens e equipes de entrada | evento, viagem, dia, pessoa, R$ | independente; sem dependência de domínio com B02 | sim, por frente/equipamento | alta; independência homologada | fronteira interna da composição. |
| B02 | Desmobilização | DesMob., retirada, saída | precificar logística, itens e equipes de saída | evento, viagem, dia, pessoa, R$ | independente; sem dependência de domínio com B01 | sim, por frente/equipamento | alta; independência homologada | fronteira interna da composição. |
| B03 | Canteiro e apoio local | canteiro, administração local, site, SSMA | infraestrutura temporária e suporte local | mês, un, vb, pessoa, R$ | independente e combinável, candidato | sim, por base/frente | alta | limite entre canteiro e administração central. |
| B04 | Dragagem | draga, dragagem e recalque, sucção, “só bombeamento” | executar e precificar a dragagem com seus recursos técnicos e econômicos internos; pode configurar bombeamento direto/sem tratamento posterior | m³, t, h, m³/h, L/h, kWh, m, mca | bloco independente; pode combinar, conforme o escopo, com B05, B06, B07 e B11; B08/B09/B10 permanecem independentes; bombeamento nunca é bloco separado | sim, por draga/frente/configuração | **homologado** | anatomia pode evoluir; base física e fórmulas permanecem explícitas por instância. |
| B05 | Preparação de célula | Prep Célula, PEAD/Bidim/brita | construir/preparar área receptora | m², m³, h, un | candidato independente; pode anteceder B06 | sim, por célula | alta | fronteira e impermeabilização. |
| B06 | Bags geotêxteis | bags, geobags, tubos geotêxteis | dimensionar, fornecer e instalar bags | un, m, m², m³, R$ | candidato combinável com B04/B05 | sim, por célula/nível/modelo | alta | regra de margem e arredondamento. |
| B07 | Desaguamento mecânico | centrífuga, decanter, centrifugação | separar sólidos por equipamento mecânico | m³/h, %ST, tSS, t/mês | candidato independente; pode combinar com B04/B11 | sim, por unidade/linha | alta | nome/fronteira e operação/manutenção. |
| B08 | Batimetria | batimetria, levantamento batimétrico | executar serviço batimétrico conforme escopo | campanha, mês, vb, R$ | independente; não depende de outro bloco | sim, por local/campanha | **homologado** | anatomia inicial ainda limitada. |
| B09 | Laboratório / Análises de Material | laboratório, análise, ensaio, caracterização | contratar/executar análises de material conforme escopo | amostra, análise, un/mês, %, R$/un | independente; não depende de outro bloco | sim, por material/conjunto de análises | **homologado** | catálogo de ensaios e resultados ainda incompleto. |
| B10 | Medição | medição, controle, acompanhamento, coleta | representar como serviços executados serão medidos, quantificados e/ou comprovados e seus custos | m³, t, tSS, %, dia, evento, vb, R$ | independente e opcional; pode referenciar resultados de outros blocos sem exigir nenhum | sim, por método/frente/serviço | **homologado** | métodos, instrumentos e conversões variam; anatomia inicial é evolutiva. |
| B11 | Transporte e destinação | frete, caçamba, bota-fora, disposição | remover e destinar material/resíduo | t, m³, km, viagem, R$/t | candidato; recebe saída de B04/B06/B07 | sim, por rota/destino | média-alta | fronteira, base de medição e licenças. |
| B12 | Venda de equipamento | venda de draga, fornecimento de ativo | configurar e precificar transferência de ativo | un, R$, conjunto | candidato especializado; serviços podem combinar | sim, por equipamento | alta para a família | fluxo, opcionais, serviços e condição do ativo. |

**Status:** doze entradas no catálogo. B01 Mobilização, B02 Desmobilização, B04 Dragagem, B08 Batimetria, B09 Laboratório / Análises de Material e B10 Medição estão homologados como blocos independentes; as outras seis entradas continuam candidatas. Também está homologado que Bombeamento integra Dragagem, sem criar bloco próprio. Draga/configuração, recalque, tubulação, mangotes, flutuantes, barrilete/manifold e acessórios, boosters, combustível/energia, mão de obra direta, jornada, produção e recursos auxiliares diretamente necessários pertencem à composição da instância de Dragagem quando aplicáveis; seus cadastros mestres não os transformam em blocos. Para Dados do orçamento, Balanço/Produção transversal, Cronograma, ABC, BDI/Tributos, Formação de preço e Proposta, o papel de cabeçalho, motor ou saída permanece **hipótese de organização V1**, sujeito às gray areas registradas.

## 5. Anatomia detalhada de cada bloco

### 5.1 Anatomia comum

| Campo | Significado | Unidade | Origem | Classe | Editável | Dependência | Catálogo | Exibição | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| tipo do bloco | definição funcional | código | catálogo | M | não na instância | versão do catálogo | blocos | sempre | sim |
| rótulo operacional | identificação humana da instância | texto | engenheiro | C | sim | único no orçamento | — | sempre | sim |
| ordem | sequência de leitura/execução | inteiro | engenheiro | C | sim | orçamento | — | sempre | sim |
| escopo incluído/excluído | fronteira contratual | texto estruturado | projeto | C | sim | responsabilidades | — | sempre | sim |
| responsável **(candidato)** | FOS/cliente/terceiro/compartilhado | enum | contrato | C | sim | item/fase; granularidade em gray area | responsáveis | condicional | sim |
| unidade de medição | base física/comercial | unidade | projeto | Híbrido | sim | quantidade/preço | unidades | sempre | sim |
| quantidade contratual | quantidade comprometida | unidade escolhida | projeto | C | sim | produção/base contratual | — | condicional | sim |
| prazo/período | duração ou evento | dia/mês/evento | projeto | C | sim | produção/cronograma | — | sempre | sim |
| itens de composição | recursos e serviços internos | várias | mestre + projeto | Híbrido | sim | quantidade × preço | itens/ativos/funções | detalhe | sim |
| custo calculado | soma da composição | R$ | cálculo | D | não | itens, vigências | — | resumo | sim |
| observação/justificativa | exceção e decisão de engenharia | texto | engenheiro | C | sim | override/alerta | — | condicional | sim |

### 5.2 Anatomia específica

As tabelas abaixo registram o núcleo mínimo. Todo campo contextual, histórico, híbrido e derivado que participe da proposta exige snapshot; campos mestre também exigem cópia quando sua alteração futura mudaria a versão emitida.

#### 5.2.1 B01 — Mobilização

| Campo histórico/sugerido | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| ativo/conjunto mobilizado | carga principal | ativo | cadastro | M/C | sim | determina veículos/içamento | ativos | sempre | sim |
| origem/destino e distância | rota logística | local, km | projeto | C | sim | frete/viagens | locais | sempre | sim |
| carretas/viagens | dimensionamento | un | plano logístico | C | sim | qtd × preço | transporte | sempre | sim |
| guindaste/munck/rigging | içamento | dia/vb | cotação | Híbrido | sim | qtd × preço | serviços | condicional | sim |
| equipe, dias e horas | montagem/implantação | pessoa, dia, h | projeto | C | sim | custo diário da equipe × dias | funções | detalhe | sim |
| ART, exames, treinamento | obrigações | un/vb | projeto/cotação | Híbrido | sim | qtd × preço | itens | condicional | sim |
| custo/preço da mobilização | total próprio | R$ | cálculo | D | não | soma exclusiva dos itens desta instância; preço na camada comercial | — | resumo | sim |

#### 5.2.2 B02 — Desmobilização

| Campo histórico/sugerido | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| ativo/conjunto desmobilizado | carga de retirada | ativo | cadastro + projeto | M/C | sim | dimensiona veículos/içamento da saída | ativos | sempre | sim |
| origem/destino e distância | rota logística de saída | local, km | projeto | C | sim | frete/viagens próprios | locais | sempre | sim |
| carretas/viagens | dimensionamento de saída | un | plano logístico | C | sim | qtd × preço | transporte | sempre | sim |
| guindaste/munck | içamento de retirada | dia/vb | cotação | Híbrido | sim | qtd × preço | serviços | condicional | sim |
| equipe, dias e horas | desmontagem/retirada | pessoa, dia, h | projeto | C | sim | custo diário da equipe × dias | funções | detalhe | sim |
| itens e serviços de retirada | composição própria observada | un/vb | projeto/cotação | Híbrido | sim | qtd × preço | itens/serviços | condicional | sim |
| custo/preço da desmobilização | total próprio | R$ | cálculo | D | não | soma exclusiva dos itens desta instância; preço na camada comercial | — | resumo | sim |

B01 e B02 não compartilham fórmula, quantidade ou total por definição de domínio. A UX pode oferecer duplicação ou preenchimento assistido entre composições semelhantes, mas o resultado copiado passa a ser editável e independente.

#### 5.2.3 B03 — Canteiro e apoio local

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| prazo do canteiro | permanência | mês/dia | cronograma | C | sim | quantidade mensal × prazo | — | sempre | sim |
| instalações | container, banheiro, escritório, água/energia | un/mês/vb | projeto/cotação | Híbrido | sim | qtd × preço × prazo | itens | tabela | sim |
| equipe local | administração/SSMA/apoio | pessoa/h | projeto | C | sim | composição de pessoal | funções | tabela | sim |
| consumos/serviços | refeições, limpeza, comunicação, vigilância | mês/un | cotação | Híbrido | sim | qtd × preço × prazo | itens | detalhe | sim |
| responsabilidade por item **(candidato)** | quem fornece/paga | enum | contrato | C | sim | o histórico mostra item ativo, de terceiro, residual ou zerado; o comportamento V1 segue em gray area | responsáveis | condicional | sim |
| custo mensal/total | consolidação | R$/mês, R$ | cálculo | D | não | recorrentes + eventos | — | resumo | sim |

#### 5.2.4 B04 — Dragagem

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| draga/modelo | ativo principal | ativo | cadastro | M | seleção | traz capacidade e parâmetros | ativos | sempre | sim |
| modalidade da dragagem | forma de remoção/recalque, incluindo bombeamento direto sem tratamento posterior | texto/enum candidato | escopo/técnica | C | sim | organiza a configuração sem criar outro bloco | modalidades candidatas | sempre | sim |
| volume e base | quantidade a remover | m³/t + base | levantamento | C | sim | prazo, custo unitário | unidades/base | sempre | sim |
| material/profundidade | condição operacional | texto, m | projeto | C | sim | seleção e produtividade | materiais | sempre | sim |
| origem/destino ou ponto de descarga | pontos do recalque | local/texto | projeto/técnica | C | sim | define percurso e interface | locais | quando aplicável | sim |
| distância/desnível | condição do recalque | m | layout/projeto | C | sim | dimensiona linha e auxiliares | — | quando aplicável | sim |
| carga/altura manométrica e parâmetros hidráulicos | condição hidráulica adotada quando aplicável | mca, kW, texto técnico | cálculo/projeto/ficha | C/D/Híbrido | sim nas premissas | depende de vazão, distância, desnível, linha, perdas e configuração utilizada; não há fórmula universal homologada | — | quando aplicável | sim |
| vazão nominal | capacidade do ativo | m³/h | cadastro | M | override justificado | produção efetiva | ativos | detalhe | sim |
| bomba auxiliar/booster | equipamento auxiliar observado | ativo/un | cadastro + projeto | M/C | sim | quantidade, horas, consumo e custo | ativos | quando aplicável | sim |
| linha de recalque | tubos, mangotes, flutuantes e conexões por trecho | m, pç, pol/mm | catálogo + projeto | M/C | sim | quantidade × preço/depreciação | tubos/conexões | tabela quando aplicável | sim |
| barrilete/manifold e acessórios | conjunto de tubos, tês, válvulas, mangueiras, conexões e bomba quando utilizado | conjunto/pç/m | catálogo + projeto | M/C | sim | soma dos componentes; parcela depreciada quando adotada | itens/ativos | quando aplicável | sim |
| eficiência/concentração | premissas | % | projeto/ensaio | C | sim | `produção_h = vazão × eficiência × concentração` quando aplicável | — | sempre | sim |
| jornada/disponibilidade | regime | h/dia, dia/mês, % | projeto | C | sim | `h_mês = h_dia × dias × disponibilidade` | jornadas | sempre | sim |
| produção/prazo e base física | resultado próprio da instância | m³/h, m³/mês, t/h, tSS/mês, mês + qualificador | cálculo | D | não | usa somente a fórmula e as dependências registradas na instância; não converte bases distintas implicitamente | — | resumo | sim |
| combustível | consumo e preço | L/h, R$/L | ativo + cotação | Híbrido | sim | horas × consumo × preço | combustíveis | detalhe | sim |
| energia elétrica | potência/consumo, horas, tarifa e responsabilidade quando utilizada | kW, kWh, h, R$/kWh | ativo/projeto/cotação | M/C/H | sim | potência ou consumo × horas × tarifa, conforme memória adotada | energia/ativos | detalhe quando aplicável | sim |
| manutenção/depreciação/capital | custo do ativo | %, h, mês, R$ | política vigente | H/D | sim só premissas | valor, residual, vida útil, taxa | políticas | detalhe | sim |
| mão de obra direta | funções, quantidade, jornada, adicionais, encargos e benefícios diretamente associados | pessoa, h, %, R$ | funções/RH + projeto | M/C/H | sim | composição da equipe × jornada e custos vigentes | funções | detalhe | sim |
| equipamentos e recursos auxiliares diretos | apoios necessários à execução daquela dragagem | ativo, un, h, R$ | cadastro + projeto/cotação | M/C/H | sim | quantidade × horas/período × custo | ativos/itens | quando aplicável | sim |

Os campos absorvidos acima vêm da mineração de Dragagem, Bombeamento/retorno e Linha de recalque/barrilete do Checkpoint 1. Draga, configuração, recalque, tubulação, mangotes, flutuantes, barrilete/manifold e acessórios, boosters, combustível, energia, mão de obra direta, jornada, produção e apoios diretamente necessários pertencem à composição de Dragagem quando utilizados. Não constituem sub-blocos automáticos nem são obrigatórios em toda instância.

Cada instância de Dragagem é independente e preserva sua própria configuração, ativo, linha, distância, produção, base física, combustível/energia, equipe, jornada, recursos, premissas, fórmulas e custos. Um orçamento pode ter várias instâncias — inclusive configurações hidráulicas e elétricas diferentes — sem herança automática entre elas. Cadastro mestre do recurso e bloco funcional do orçamento são conceitos distintos.

Pendências específicas da anatomia de Dragagem: refinamento futuro do catálogo de modalidades e componentes; fórmulas hidráulicas aplicáveis por configuração; e convenções de apresentação das bases físicas. Permanecem abertas, fora desta homologação, a arquitetura transversal de Produção/Balanço, as conversões entre m³, m³ in situ, m³ desaguado, tonelada úmida, tonelada seca e tSS e o compartilhamento de equipes entre blocos.

#### 5.2.5 B05 — Preparação de célula

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| geometria/quantidade | dimensões e número de células | m, m², un | projeto | C | sim | área = comprimento × largura × qtd | — | sempre | sim |
| coeficientes PEAD/Bidim/brita | consumo por área | m²/m², m³/m² | histórico técnico | M/H | override justificado | quantidade = coeficiente × área | coeficientes | detalhe | sim |
| equipamentos/MO | execução | h/m², pessoa, h | mestre + projeto | Híbrido | sim | coeficiente × área × taxa | ativos/funções | detalhe | sim |
| materiais e preços | composição | m², m³, R$/un | cotação | H | sim | quantidade × preço | itens | tabela | sim |
| custo total/unitário | resultado | R$, R$/m² | cálculo | D | não | soma; total ÷ área | — | resumo | sim |

#### 5.2.6 B06 — Bags geotêxteis

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| modelo/dimensões | tipo de bag | código, m | catálogo | M | seleção | seção, perímetro, preço | bags | sempre | sim |
| arranjo por nível | layout | nível, un | projeto | C | sim | soma por modelo/nível | — | tabela visual simples | sim |
| capacidade unitária | volume geométrico | m³ | catálogo/cálculo | M/D | não salvo isoladamente | área de seção × comprimento | bags | detalhe | sim |
| volume desaguado/demanda | material a receber | m³ | balanço | D/C | base sim | massa seca ÷ ST final | — | sempre | sim |
| margem operacional | folga requerida | %, m³ | decisão de engenharia | C | sim | capacidade − demanda | política futura | sempre com alerta | sim |
| quantidade recomendada | dimensionamento | un | cálculo | D | não | teto da demanda/capacidade + margem; regra por arranjo | — | resumo | sim |
| preço por bag/m² | cotação | R$/un, R$/m² | fornecedor/vigência | H | sim | perímetro × comprimento × preço/m², se aplicável | bags/cotações | detalhe | sim |
| custo de fornecimento | total | R$ | cálculo | D | não | soma qtd × preço | — | resumo | sim |

#### 5.2.7 B07 — Desaguamento mecânico

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| tecnologia/equipamento | centrífuga ou decanter | ativo/tipo | cadastro | M | seleção | capacidade, energia, manutenção | ativos | sempre | sim |
| quantidade de unidades | linhas operacionais | un | projeto | C | sim | multiplica capacidade/recursos | — | sempre | sim |
| vazão/eficiência | desempenho | m³/h, % | mestre + projeto | Híbrido | sim | vazão efetiva | ativos | sempre | sim |
| ST entrada/saída | teor de sólidos | % | ensaio/premissa | C | sim | balanço de massa | — | sempre | sim |
| produção seca | sólidos processados | tSS/h, tSS/mês | cálculo | D | não | vazão × ST entrada × horas | — | resumo | sim |
| produto desaguado | saída | t ou m³/mês | cálculo | D | não | massa seca ÷ ST saída | — | resumo | sim |
| polímero | dosagem/consumo/responsável | kg/tSS, kg, R$/kg | ensaio + cotação | Híbrido | sim | massa tratada × dosagem | insumos | condicional | sim |
| periféricos/energia/equipe | tanque, bombas, painéis e operação | un, kWh, pessoa | mestre + projeto | Híbrido | sim | composição | itens/ativos/funções | detalhe | sim |
| manutenção | plano/custo | evento, %, R$ | política/cotação | H/D | sim premissas | horas/vida útil/valor | políticas | detalhe | sim |

#### 5.2.8 B08 — Batimetria

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| local/escopo batimétrico | onde o serviço será executado | local/texto | solicitação/projeto | C | sim | — | locais | sempre | sim |
| frequência | recorrência observada | campanha/mês | escopo/contrato | C | sim | pode dimensionar quantidade | — | quando aplicável | sim |
| quantidade de campanhas | eventos previstos | campanha | projeto | C | sim | frequência × período, quando adotado | — | sempre | sim |
| fornecedor/cotação | referência de execução externa quando houver | texto/data | cotação | H | sim | origem do preço | fornecedores/cotações | condicional | sim |
| preço por campanha/serviço | preço histórico adotado | R$/campanha ou R$/vb | cotação/composição | H | sim | quantidade × preço unitário | cotações | detalhe | sim |
| custo total | consolidação própria | R$ | cálculo | D | não | soma dos itens/campanhas da Batimetria | — | resumo | sim |

Não há evidência consolidada suficiente para homologar método, equipamento, entregável, critério de aceite ou fórmula de volume como campos obrigatórios de Batimetria. Esses pontos permanecem pendentes e não são preenchidos por analogia com “Medição”.

#### 5.2.9 B09 — Laboratório / Análises de Material

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| material/amostra | material ao qual a análise se refere | texto/ID | obra/coleta | C | sim | — | materiais | sempre | sim |
| análise/parâmetro solicitado | ensaio ou característica requerida | texto/enum candidato | engenharia/escopo | C | sim | evidências incluem granulometria, teor de sólidos/concentração e ensaio de dosagem | análises, ainda incompleto | sempre | sim |
| quantidade/frequência | número ou recorrência de análises | un, un/mês | plano/cotação | C/H | sim | quantidade × preço unitário | — | quando aplicável | sim |
| resultado e unidade | valor obtido/adotado | %, índice ou texto | ensaio/cliente/premissa identificada | H/C | sim | pode ser referenciado explicitamente por outro bloco, sem subordinação | — | quando disponível | sim |
| laboratório/fornecedor | origem externa da análise | texto | cotação/registro | H | sim | vincula preço e proveniência | fornecedores | condicional | sim |
| preço unitário | preço da análise | R$/un | cotação | H | sim | quantidade × preço | cotações | detalhe | sim |
| custo total | consolidação própria | R$ | cálculo | D | não | soma das análises e itens desta instância | — | resumo | sim |

Pendências: o lote não sustenta catálogo fechado de ensaios, método de coleta, prazo de validade ou formato de laudo. “Qualidade/Garantias” não integra esta anatomia e permanece tratado somente pelas evidências da seção 11.2.

#### 5.2.10 B10 — Medição

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| objeto/serviço medido | o que será quantificado ou comprovado | texto/ID | escopo/contrato | C | sim | pode referenciar serviço ou instância sem criar dependência obrigatória | serviços/blocos | sempre | sim |
| método/base física | forma adotada para determinar a quantidade | texto/enum candidato | contrato/plano de controle | C | sim | governa unidade, registros e eventual conversão | métodos, ainda incompleto | sempre | sim |
| unidade e qualificador da base | grandeza medida sem perder seu significado físico | m³, m³ in situ, m³ desaguado, t úmida, t seca, tSS ou unidade contratual | contrato/engenharia | C | sim | não converter nem somar bases distintas sem regra explícita | unidades qualificadas | sempre | sim |
| frequência/período | recorrência ou janela da medição | evento, dia, mês | contrato/plano de controle | C | sim | dimensiona coletas, equipe e itens recorrentes | — | quando aplicável | sim |
| coleta/amostragem | pontos, quantidade e acompanhamento observados | coleta, amostra, evento | plano de controle/obra | C | sim | pode produzir insumo para B09 sem tornar B09 obrigatório | — | quando aplicável | sim |
| equipamento/instrumento | recurso utilizado na medição | un, dia, vb | plano/cotação | M/C/H | sim | quantidade × período × preço; U05 comprova equipamentos, sem catálogo fechado de tipos | ativos/itens, ainda incompleto | quando aplicável | sim |
| equipe de medição | funções, quantidade, jornada e dias | pessoa, h, dia | plano/RH | M/C/H | sim | quantidade × horas/dias × custo vigente | funções | quando aplicável | sim |
| ensaio/resultado referenciado | resultado usado pela metodologia, quando houver | %, índice ou unidade do ensaio | B09/cliente/ensaio identificado | H/C | sim | referência explícita e versionada; Medição não exige Laboratório | análises | condicional | sim |
| parâmetros de conversão | ST/concentração, densidade ou outro parâmetro efetivamente adotado | %, t/m³ | ensaio/premissa identificada | C/H | sim | depende da base de entrada e saída; não há fórmula universal homologada | — | condicional | sim |
| método de cálculo | memória que transforma registros na quantidade medida | fórmula versionada/texto | contrato/engenharia | C/H | sim | exemplos históricos incluem `volume × ST` e `base seca ÷ ST desaguado`; aplicar somente quando compatível com a instância | fórmulas, ainda incompleto | condicional | sim |
| quantidade medida | resultado quantificado/comprovado | unidade qualificada escolhida | cálculo/registro | D/H | não, salvo override justificado | soma de registros ou fórmula da instância, preservando base e dependências | — | resumo | sim |
| itens e custo da medição | composição de equipe, dias, equipamentos, ensaios e serviços | dia, un, vb, R$ | plano/cotação | Híbrido/D | sim nos insumos | soma de itens e mão de obra; evidência explícita em U05 e U11 | itens/funções/cotações | detalhe | sim |
| custo/preço total | consolidação própria e valor comercial quando aplicável | R$ | cálculo/cotação/negociação | D/H | override justificado | soma da composição; U04 observa custo × fator comercial | — | resumo | sim |

As evidências sustentam variação, não um método padrão: U03 usa planilha contratual com medição mensal e total; U04 registra item comercial próprio; U05 compõe equipe, dias, equipamentos e ensaios; U11 registra coletas, acompanhamento e custo. Medidor de vazão e pesagem foram exemplos de domínio informados por Fabio, mas não foram localizados de forma suficientemente específica na mineração disponível para virarem campos ou componentes obrigatórios. Permanecem possibilidades de método a validar por instância, não taxonomia homologada.

Pendências específicas da anatomia de Medição: catálogo de métodos/instrumentos; forma de registrar leituras brutas; cardinalidade da referência eventual a B09; critérios contratuais de aceite; fórmulas aplicáveis a pesagem, vazão e tonelada úmida; e propriedade das conversões quando a mesma memória também alimenta Produção/Balanço. Nenhuma dessas pendências cria dependência obrigatória.

#### 5.2.11 B11 — Transporte e destinação

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| material/base de medição | carga e base comercial | t/m³ | projeto/contrato | C | sim | conversões explícitas | materiais/unidades | sempre | sim |
| origem/destino/licença | rota e receptor | local/documento | projeto | C/H | sim | elegibilidade e distância | destinos | sempre | sim |
| distância | percurso | km | rota/cotação | C/H | sim | tarifa por viagem/t.km | rotas | sempre | sim |
| veículo/capacidade | modal | ativo, t, m³ | cadastro | M | seleção | número de viagens | veículos | sempre | sim |
| massa/volume transportado | demanda | t/m³ | bloco produtor/balanço | D/C | base sim | saída elegível × fator | — | resumo | sim |
| viagens | dimensionamento | un | cálculo | D | não | teto(demanda/capacidade) | — | resumo | sim |
| tarifa transporte/destinação | preço | R$/t, R$/m³, R$/viagem | cotação | H | sim | conforme base contratual | cotações | detalhe | sim |
| custo total | resultado | R$ | cálculo | D | não | quantidade × tarifa + taxas | — | resumo | sim |

#### 5.2.12 B12 — Venda de equipamento

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| ativo/configuração | equipamento ofertado | ativo/conjunto | cadastro | M | seleção | componentes e especificações | ativos | sempre | sim |
| estado/ano/horas | condição na oferta | texto, ano, h | inspeção | H | sim | influencia avaliação/preço | ativos/inspeções | sempre | sim |
| componentes incluídos | configuração entregue | un/texto | engenharia comercial | C | sim | custo/configuração | itens | tabela | sim |
| preço-base/avaliação | referência | R$ | política/avaliação | H | sim | formação comercial | avaliações | detalhe | sim |
| opcionais | itens/serviços adicionais | un, R$ | catálogo + projeto | Híbrido | sim | soma opcional | itens/serviços | condicional | sim |
| instalação/treinamento/frete | serviços associados | evento/vb | projeto/cotação | Híbrido | sim | composição própria ou instância independente de B01/B02, conforme escopo | serviços | condicional | sim |
| preço final | total negociado | R$ | cálculo/negociação | D/H | override justificado | base + opcionais + serviços ± negociação | — | resumo | sim |

## 6. Campos e classificações

### 6.1 Componentes internos e seus campos transversais

| Componente | Campos mínimos | Classe predominante | Fórmula/dependência | Unidade/origem | Snapshot |
|---|---|---|---|---|---:|
| Equipamento | ativo, quantidade, horas, valor, residual, vida útil | M + C + H | depreciação e capital dependem de valor/vida/taxa | ativo, un, h, R$; cadastro/avaliação | sim |
| Mão de obra | função, quantidade, jornada, salário, adicionais, encargos, benefícios/EPI | M + C + H | `qtd × base × horas + adicionais + encargos + benefícios` | pessoa, h, %, R$; RH/projeto | sim |
| Combustível/energia | tipo, consumo, preço, responsabilidade | M + C + H | `horas × consumo × preço` | L/h, kWh, R$; ativo/cotação | sim |
| Tubulação/barrilete | item, diâmetro, comprimento/qtd, preço, depreciação | M + C + H | `qtd × preço`; hidráulica no sistema | m, pol, pç, R$; catálogo/projeto | sim |
| Polímero | produto, dosagem, massa tratada, preço, responsável | M + C + H | `massa seca tratada × dosagem × preço` | kg/tSS, kg, R$/kg; ensaio/cotação | sim |
| Manutenção | plano, intervalo, peças, docagem, pneus/lavagem | M/H | custo por hora/evento ou percentual documentado | h, evento, %, R$; política/cotação | sim |
| Cotação/ABC | fornecedor, código, unidade, quantidade, preço, validade | H + C | `qtd × preço` | unidade/R$; documento datado | sim |

### 6.2 Formação de preço e versão formal

A evidência indica a necessidade de consolidar custos das instâncias sem forçar fórmula única. Permanece **candidata**, ainda não homologada, a capacidade V1 de representar BDI/fator global ou por item; administração, risco, lucro e tributos com base declarada; preço unitário e total; e desconto, arredondamento ou valor negociado com rastreabilidade. A separação entre referências, total calculado e total emitido é sustentada pelos casos, mas sua UX e obrigatoriedade aguardam decisão.

Ao **Fechar Proposta**, registrar identidade, revisão, data, escopo, instâncias e rótulos, campos usados, catálogos copiados, cotações/vigências, fórmulas, custos, preços, responsabilidades, alertas aceitos e documentos gerados. Alteração posterior cria nova revisão derivada; não reescreve a versão fechada.

## 7. Dependências e fórmulas

| Origem | Destino | Dado transferido | Cardinalidade/regra | Bloqueio/alerta |
|---|---|---|---|---|
| Dados do orçamento | todos | cliente, local, material, unidades, responsabilidades | 1 orçamento → N blocos | alteração após formalização exige nova revisão. |
| B01 Mobilização | — | não transfere composição, quantidade ou custo para B02 | instância independente | eventual duplicação é conveniência UX, não dependência. |
| B02 Desmobilização | — | não deriva composição, quantidade ou custo de B01 | instância independente | não calcular como inversão ou percentual da Mobilização. |
| B04 Dragagem | composição interna da própria instância | draga/configuração, bombeamento/recalque, linha, acessórios, boosters, combustível/energia, mão de obra direta, jornada, produção e recursos auxiliares | **homologado:** recursos diretamente necessários ficam dentro de B04 quando aplicáveis; cada instância mantém composição própria | não criar blocos separados para recursos internos; cadastro mestre ≠ bloco. |
| B04 Dragagem | B05/B06/B07/B11 ou ponto de descarga | vazão/volume, material, origem/destino e características | vínculo externo entre instâncias permanece candidato e depende do escopo | validar unidade/base; não inferir dependência obrigatória. |
| B05 Célula | B06 Bags | área, geometria, restrições | hipótese: uma célula pode receber N conjuntos | alertar capacidade física; regra ainda não homologada. |
| Balanço de massa | B06/B07/B10/B11 | massa seca, volume desaguado ou parâmetros rastreáveis | fórmula com ST e base; referência a B10 é eventual e explícita | impedir mistura de m³ in situ, m³ desaguado, t úmida, t seca e tSS sem conversão. |
| B07 Desaguamento mecânico | B11 Transporte/destinação | produto desaguado | vínculo candidato entre instâncias | exigir ST/densidade se converter. |
| B08 Batimetria | — | não exige nem cria automaticamente B09 ou B10 | bloco independente | pode coexistir com ambos ou nenhum, conforme escopo. |
| B09 Laboratório / Análises | B10 Medição, quando referenciado | resultado de análise com unidade, origem e versão | relação eventual; B09 continua independente e B10 não o exige | não criar associação automática por afinidade. |
| B10 Medição | — | não exige nem deriva de B08, B09 ou outro bloco | bloco independente e opcional; pode referenciar serviços/resultados explicitamente | método, unidade e fórmula devem pertencer à instância e ao snapshot. |
| Cronograma | B01/B02/B03/todos | fases e duração | cada bloco mantém composição/custo próprios | mostrar diferença prazo matemático/comercial sem vincular B01 a B02. |
| Todos os blocos | Formação de preço | custos por instância e unidade | soma rastreável | não aceitar referência quebrada. |
| Formação de preço | Versão formal | preço, condições, escopo | fechamento cria snapshot imutável | negociação manual exige justificativa. |

As dependências acima são **candidatas**, exceto pelas regras homologadas: B04 Dragagem é bloco independente e contém sua composição técnica/econômica direta; bombeamento/recalque integra B04; B01 e B02 não possuem dependência entre si; B08 Batimetria, B09 Laboratório / Análises e B10 Medição são blocos independentes e opcionalmente selecionáveis. A referência eventual de um resultado de B09 em B10 não funde os blocos nem cria obrigatoriedade. A homologação de B04 não decide vínculos externos com B05/B06/B07/B11 nem a arquitetura global de Produção/Balanço.

## 8. Relação com cadastros mestres

| Candidato a mestre | Candidato a orçamento/instância | Hipótese de override |
|---|---|---|
| identidade e especificação estável de ativos | ativo escolhido, quantidade, jornada e desempenho adotado | copiar valor mestre; override com justificativa, sem alterar mestre. |
| dragas, bombas, tubulações, mangotes, flutuantes, acessórios, combustíveis, energia, funções e apoios | recursos selecionados e valores efetivamente usados na instância de Dragagem | cadastro acelera e estrutura a composição, mas não cria bloco funcional; snapshot preserva configuração e overrides. |
| modelos de bags, itens, unidades e coeficientes de referência | arranjo, níveis, margem e coeficiente adotado | preservar valor original e valor usado. |
| funções, kits, regras e benefícios de referência | efetivo, turnos, adicionais aplicáveis | salários/encargos com vigência no snapshot. |
| insumos e serviços cadastrados | fornecedor, cotação, responsabilidade e quantidade | preço sempre histórico, nunca “atual” retroativo. |
| tipos de análise e serviços cadastrados, ainda incompletos | análise solicitada, material, fornecedor e quantidade | preservar origem e valor usado; catálogo aguarda evidência adicional. |
| métodos, instrumentos, unidades qualificadas e fórmulas de medição, ainda incompletos | método, base física, recursos e conversões adotados na instância | preservar configuração, fórmula, origem e valores usados; evolução do catálogo não reescreve o orçamento. |
| tipos de bloco e campos configurados | instâncias, rótulos, ordem e escopo | inativação não afeta versões existentes. |

A evidência classifica tributos, salários, preços, valores de ativos, taxas de capital, BDI e benchmarks como históricos com vigência, ainda que administrados em catálogos. A forma de cadastro e override permanece candidata.

## 9. Diretrizes UX por bloco

Para Dragagem, está homologado preservar equivalência funcional e familiaridade com a atual aba Dragagem: terminologia, sequência mental, agrupamento, parâmetros técnicos e composição reconhecíveis. A organização visual detalhada das telas continua hipótese UX V1.

- Tela do orçamento com cabeçalho fixo e lista ordenável de blocos, semelhante a índice de abas.
- Ação **Adicionar bloco** abre catálogo enxuto; a mesma opção pode ser adicionada várias vezes e recebe rótulo, por exemplo “Dragagem — Lago Norte”.
- Cada bloco tem **Resumo** e **Composição**. O resumo mostra premissas, unidade, produção/prazo e total; a composição usa grade de linhas familiar à planilha.
- Campos exibem unidade junto ao valor e origem por indicação discreta: mestre, obra, cálculo ou histórico.
- Valores derivados são somente leitura, com ação “ver cálculo” mostrando fórmula e dependências em linguagem legível.
- Overrides pedem justificativa curta e preservam valor sugerido; não atualizam o cadastro mestre.
- **Candidato:** responsabilidade por item explícita; item fornecido pelo cliente poderia permanecer visível com custo zero. A obrigatoriedade e o tratamento do zero seguem em gray area.
- Alertas são locais e acionáveis: unidade incompatível, capacidade insuficiente, cotação vencida, referência ausente, diferença entre calculado e emitido.
- Comparar revisões mostra alterações de premissas, blocos, composições e preço; não cria cenário-filho.
- **Duplicar orçamento** copia conteúdo para alternativa independente e registra somente a proveniência da cópia.

### 9.1 Como isso se parece para quem vem do Excel?

| Bloco | Tradução conservadora da aba histórica |
|---|---|
| B01 Mobilização | grade própria de entrada com ativo/conjunto, rota, equipe, frete, içamento, itens, quantidades, preços e total. Pode iniciar vazia ou receber cópia assistida, sem vínculo posterior. |
| B02 Desmobilização | grade própria de saída com ativo/conjunto, rota, equipe, frete, içamento, itens, quantidades, preços e total. Não é preenchida automaticamente por fórmula baseada em B01. |
| B03 Canteiro | a composição mensal continua em linhas; prazo e responsabilidades ficam acima, e total mensal/total do período aparece ao lado. |
| B04 Dragagem | uma estrutura reconhecível como a aba Dragagem: o engenheiro configura independentemente cada instância com draga, modalidade, recalque, linha/acessórios, bombas auxiliares, combustível/energia, equipe direta, jornada, produção, base física, apoios e custos. “Bombeamento direto / sem tratamento posterior” permanece configuração familiar, não outro bloco. |
| B05 Preparação de célula | geometria primeiro; depois a tabela PEAD/Bidim/brita/equipamentos com coeficiente, quantidade, preço e total, equivalente à aba atual. |
| B06 Bags | catálogo selecionável e grade por nível/modelo; demanda, capacidade e margem aparecem juntas antes do custo de fornecimento. |
| B07 Desaguamento mecânico | equipamento, ST, vazão e jornada no topo; produção seca/desaguada imediatamente abaixo; periféricos, polímero, equipe e manutenção em composições. |
| B08 Batimetria | composição própria por local/campanha, com frequência, quantidade, cotação, preço unitário e total; sem campos de Laboratório ou de “Medição” presumidos. |
| B09 Laboratório/Análises | grade própria por material/amostra e análise solicitada, com quantidade/frequência, resultado/unidade, fornecedor, preço e total; sem dependência de outro bloco. |
| B10 Medição | o engenheiro inclui somente quando o escopo exigir e escolhe objeto, método, unidade física qualificada, frequência, recursos, registros e fórmula. Coletas ou resultados de B09 podem ser referenciados sem fundir os blocos. |
| B11 Transporte/destinação | uma grade de rotas: origem, destino, material, base, distância, veículo, viagens, tarifa e total; conversões ficam abertas ao lado. |
| B12 Venda de equipamento | ficha técnica à esquerda e composição comercial à direita/abaixo, com componentes, opcionais, serviços e preço final. |

Defaults só podem vir de cadastro com origem visível; valores próprios da obra permanecem de digitação direta. Nenhum bloco esconde a memória que hoje o engenheiro consegue inspecionar no Excel.

## 10. Riscos herdados do Excel

| Problema histórico | Blocos afetados | Flexibilidade preservada | Proteção proporcional contra erro silencioso |
|---|---|---|---|
| copiar pasta/aba com dados de outra obra | todos | duplicação continua disponível | identidade única; alerta de cliente/local divergente; origem por campo. |
| `#REF!`, links externos e células quebradas | todos + preço | fórmulas configuráveis/versionadas | nenhum fechamento com erro ou dependência ausente. |
| duas fontes de produção | B04, B06, B07, B10, B11 | engenheiro ajusta premissas | candidato: uma cadeia vigente por instância; referências usadas por Medição devem ser explícitas e snapshotadas; propriedade segue em gray area. |
| nome de aba tratado como verdade | B04 e aliases | nomes familiares continuam visíveis | “só bombeamento” é alias; funcionalmente continua Dragagem. |
| fragmentação da execução em blocos de recurso | B04 | cadastros de draga, linha, combustível, energia, mão de obra e apoios continuam estruturados | utilização diretamente necessária fica na composição da instância de Dragagem; cadastro mestre não cria bloco. |
| parâmetros herdados entre dragagens | B04 | múltiplas instâncias e duplicação continuam permitidas | cada instância preserva configuração, produção, linha, recursos, fórmulas e custos próprios; cópia não cria vínculo vivo. |
| mistura m³ in situ, m³ desaguado, t úmida, t seca e tSS | B04, B06, B07, B10, B11 | qualquer base compatível com o escopo pode ser escolhida | qualificador físico obrigatório; conversão rastreável com parâmetros, fórmula e origem; nunca tratar como unidades intercambiáveis. |
| agrupamento por afinidade sem evidência | catálogo, especialmente B08/B09/B10 | engenheiro pode selecionar qualquer combinação exigida pelo escopo | manter blocos independentes; não criar inclusão/dependência automática. |
| catálogo alterado após uso de Medição | B10 + versão formal | métodos e componentes podem evoluir ou ser inativados | snapshot da configuração, unidade, fórmula, recursos, resultados referenciados e valores efetivamente usados. |
| Mobilização usada para calcular Desmobilização | B01/B02 | UX pode copiar/preencher composição semelhante | composições, quantidades e custos permanecem independentes; nunca aplicar inversão ou percentual por regra de domínio. |
| custo zero inferido como ausência | B01, B02, B03, B07, B11 | cliente/terceiro pode fornecer | candidato: distinguir ausente, residual, terceiro e zero; regra segue aberta. |
| valor manual sobrescreve cálculo | todos + preço | negociação/ajuste permitido | guardar calculado e emitido; exigir justificativa curta. |
| BDI/tributos com bases implícitas | preço | práticas atuais continuam possíveis | candidato: explicitar percentual, base, ordem e vigência; detalhes aguardam homologação. |
| cenários tratados como sequência linear | orçamento/versão | duplicação livre | alternativas independentes e linhagem formal. |
| bags sem margem/conciliação | B06 | engenheiro define margem/arranjo | candidato: mostrar capacidade/demanda e alertar; intensidade segue aberta. |
| premissa “chute” sem qualificação | B04/B07 | estimativa continua possível | candidato: mostrar confiança e origem; obrigatoriedade segue aberta. |
| mestre alterado retroativamente | todos | mestre continua administrável | snapshot integral no fechamento. |

## 11. Gray areas ainda abertas

### 11.1 Decisões homologadas

**Bombeamento × Dragagem:** Bombeamento não existe como bloco macro independente na V1. Quando há bombeamento de material neste contexto, houve Dragagem. “Bombeamento direto / sem tratamento posterior” é modalidade/configuração interna de Dragagem. Nomes históricos como “só bombeamento” permanecem como aliases para rastreabilidade e jamais significam ausência de dragagem.

**Dragagem:** é bloco macro próprio, independente e selecionável. Sua composição reúne tudo o que for diretamente necessário à execução daquela dragagem — incluindo, quando aplicáveis, draga/configuração, bombeamento/recalque, linha e acessórios, boosters, combustível/energia, mão de obra direta, jornada, produção e recursos auxiliares. Um mesmo orçamento pode conter múltiplas instâncias independentes, sem herança automática. A presença de cadastro mestre para um recurso não o transforma em bloco funcional.

**Mobilização × Desmobilização:** são conceitos e blocos independentes na V1. Cada um possui composição, itens, quantidades e custos próprios e pode ser incluído/configurado separadamente. Desmobilização não é cópia, inversão ou percentual de Mobilização. Similaridades podem alimentar duplicação ou preenchimento assistido, sem criar vínculo ou atualização entre as instâncias.

**Batimetria:** é bloco independente e selecionável. Não depende de Dragagem, Bags, Centrífuga, Laboratório ou qualquer outro bloco.

**Laboratório / Análises de Material:** é bloco independente e selecionável. Não é componente obrigatório de Batimetria e não fica subordinado a Dragagem, Bags, Centrífuga ou outro bloco.

**Medição:** é bloco próprio, opcional e selecionável. Representa como serviços executados serão medidos, quantificados e/ou comprovados, incluindo recursos e custos necessários. Não depende obrigatoriamente de Batimetria, Laboratório / Análises ou qualquer outro bloco. Batimetria e Medição podem existir separadamente, juntas ou ambas ausentes. Uma metodologia de Medição pode referenciar análise de B09, de forma eventual e explícita, sem fundir ou subordinar os blocos.

**Catálogo evolutivo:** configuração, anatomia e componentes de Medição podem mudar ou ser inativados conforme o uso real. Orçamentos e versões formais preservam por snapshot exatamente a configuração utilizada, sem alteração retroativa.

**Regra de modelagem:** afinidade semântica, por si só, não agrupa conceitos nem cria dependência.

### 11.2 Evidências que sustentam Medição e pendências preservadas

| Conceito | Unidade e origem já auditada | Contexto | Função observada / limite |
|---|---|---|---|
| Medição | U03, `0.FOS.xlsx`, planilha contratual | medição mensal de R$ 3.718.234,154 e total contratual de R$ 29.834.404,924 | consolidação/faturamento por itens e períodos; sustenta base, recorrência e resultado, sem vínculo com Batimetria. |
| Medição | U04, memória/planilha detalhada D_034 | item com custo R$ 48.000 e preço R$ 76.800; técnica também cita Batimetria mensal | composição comercial própria naquele caso; coexistência não homologa dependência entre os blocos. |
| Medição | U05, aba S12 `Medição` | equipe, dias, equipamentos, ensaios e total | sustenta recursos humanos, instrumentos/itens, frequência operacional, ensaios e custo do bloco. |
| Medição | U11, aba `3.4.Medição` | coletas e acompanhamento; custo observado de R$ 26.417,475 | sustenta coleta, acompanhamento, composição e custo; não torna Laboratório obrigatório. |
| Medição/Batimetria | U06–U08 e U10, matriz consolidada do Checkpoint 1 | presença registrada no agrupamento histórico anterior | insuficiente para atribuir a ocorrência a um único bloco; preservada como `?` na matriz, sem ampliar anatomia. |
| Bases e conversões | U03, U05, U10–U12, memórias já auditadas | m³, m³ in situ/desaguado, t úmida/seca, tSS, ST/concentração e densidade aparecem em cadeias distintas | sustenta qualificação explícita da unidade e snapshot da fórmula; não sustenta conversão universal. |
| Garantias | U08, `Dragagem + Centrifuga.xlsx` versus proposta D_005_2023 | composição e proposta divergem em volume, unidade e garantias | compromisso técnico/comercial da proposta; permanece pendência, sem associação a B08 ou B09. |
| Qualidade | nenhuma evidência funcional específica consolidada | a expressão apareceu apenas em agrupamento anterior e em nota editorial da auditoria | insuficiente para bloco, componente ou associação; retirada da proposta funcional. |

### 11.3 Demais gray areas — sem resposta nesta rodada

| Gray area | Observado / insuficiência | Pergunta para Fabio/Merlin |
|---|---|---|
| Responsabilidade por item / fornecimento do cliente | o histórico distingue FOS, cliente, terceiro, residual e custo zero, mas não define uma única UX/regra. | Responsabilidade deve existir por bloco, por item ou em ambos? Item do cliente fica visível e zerado, excluído ou apenas marcado? |
| Mão de obra interna | decisão anterior afasta bloco global, mas não fecha compartilhamento de equipes entre instâncias. | Como representar uma mesma equipe atendendo mais de um bloco sem duplicar custo? |
| Transporte/destinação | é relevante em parte do lote; bases e licenças variam. | Transporte e destinação são um bloco, dois blocos ou fases da mesma instância? |
| Operação/manutenção | aparecem como abas, porém ligadas a ativos técnicos. | Existe orçamento real de operação pura que exija cartão próprio na V1? |
| Locação de equipamento | hipótese conceitual, não confirmada transversalmente. | Locação entra no primeiro catálogo ou aguarda evidência adicional? |
| Venda de equipamento | U09 confirma a família; fronteira com serviços não está fechada. | Venda usa o mesmo fluxo dos serviços ou uma modalidade especializada com camadas comuns? |
| Produção/balanço | parâmetros pertencem ao bloco; resultados alimentam vários blocos. | Qual tela é dona da edição: bloco produtor ou painel técnico compartilhado com vínculo explícito? |
| BDI/tributos | fórmulas e bases variam entre obras. | Quais estratégias atuais precisam ser suportadas nominalmente na V1, sem normalização? |
| Taxonomia/aliases | B01, B02, B04, B08, B09 e B10 estão homologados como blocos; as outras seis entradas e seus nomes continuam candidatos. | Quais das seis entradas candidatas devem ser promovidas, fundidas ou renomeadas após este checkpoint? |

## 12. Itens candidatos a V2/V3

### DEIXAR PARA V2/V3

- recomendação automática de solução, equipamento, produtividade, dosagem, equipe ou combinação de blocos;
- otimização hidráulica automática e dimensionamento avançado de linha/barrilete;
- biblioteca homologada de fórmulas por tecnologia com calibração estatística;
- inteligência de preços, comparação automática de fornecedores e atualização de índices;
- decomposição fiscal/BDI universal ou simulador tributário avançado;
- comparação inteligente de cenários; na V1, alternativas são orçamentos independentes;
- detecção semântica automática de contaminação entre obras além das validações determinísticas;
- importação genérica de qualquer planilha legada;
- geração automática de cronograma executivo detalhado;
- workflow avançado de aprovação, assinatura, integração contábil/ERP e faturamento;
- taxonomia definitiva de locação e operação pura sem novas evidências;
- aprendizado com históricos e sugestão automática de margem/risco.

## 13. Conclusão e recomendação

Resultado acumulado: o catálogo possui doze entradas. Mobilização, Desmobilização, Dragagem, Batimetria, Laboratório / Análises de Material e Medição estão homologados como blocos independentes; Bombeamento integra Dragagem como modalidade/configuração e não cria bloco próprio. As outras seis entradas continuam candidatas. A composição direta de cada Dragagem fica dentro de sua própria instância; cadastros mestres de recursos não criam novos blocos. Qualidade não possui evidência funcional suficiente; Garantias permanece somente como evidência técnico-comercial localizada em U08.

**Ponto de parada:** este documento conclui exclusivamente a missão de catálogo e anatomia sobre as 12 unidades já auditadas. Nenhuma outra obra foi analisada.
