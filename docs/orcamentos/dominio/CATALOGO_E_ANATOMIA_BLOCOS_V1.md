# Catálogo e anatomia dos blocos V1

**Status:** proposta para checkpoint; não homologada  
**Base:** auditoria fechada de 12 unidades (U01–U12), decisões pós-checkpoint 1 e diretriz de UX V1  
**Escopo:** domínio funcional do novo módulo de Orçamentos; sem implementação

## 1. Objetivo

Este documento transforma as evidências das 12 unidades auditadas em uma proposta conservadora de catálogo e anatomia de blocos para a V1. Somente a fronteira **Bombeamento × Dragagem** está homologada nesta rodada. Os nove blocos, seus nomes, as demais fronteiras, anatomias e normalizações continuam candidatos até decisão explícita de Fabio/Merlin.

Um **bloco** é uma etapa ou serviço macro que o engenheiro pode incluir, ordenar, repetir e parametrizar em um orçamento. Abas históricas não viram automaticamente blocos. Componentes internos, memórias de cálculo, consolidações e documentos de saída são mapeados, mas não expostos como cartões independentes sem evidência funcional.

## 2. Premissas e restrições

Regras vigentes usadas como restrições:

- cada orçamento é independente; alternativas são orçamentos separados, criados inclusive por duplicação, sem vínculo vivo;
- o sistema não escolhe a solução de engenharia;
- o catálogo de blocos é administrável; blocos usados podem ser inativados, não apagados;
- um orçamento aceita várias instâncias do mesmo bloco, cada uma com rótulo operacional;
- dados mestres aceleram o preenchimento, mas não bloqueiam ajuste contextual;
- o fechamento da proposta cria versão formal, imutável e rastreável; revisão posterior deriva nova versão;
- a V1 preserva familiaridade com Excel e equivalência funcional, sem reproduzir suas fragilidades.

As conclusões se limitam a U01–U12. Não houve ampliação da amostra, e nenhum nome deste documento equivale a taxonomia homologada.

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

Legenda: **P** presente; **I** presente como componente interno; **C** camada compartilhada; **—** sem evidência relevante. A matriz registra função observada, não homologa o catálogo.

| Unidade oficial do Checkpoint 1 | Mobilização/desmob. | Canteiro | Dragagem¹ | Célula | Bags | Desag. mecânico | Batimetria/medição | Transporte/destinação | Venda equipamento | Camadas compartilhadas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| U01 International Paper 2017 | P | P | P | P | P | P | — | R | — | escopo, balanço, produção, preço, proposta |
| U02 CAESB 2017 — venda FC-001 | — | — | — | — | — | — | — | R | P | escopo, preço, proposta |
| U03 Vale Maravilhas I 2019 | P | P | P | P | — | — | P | P | — | condições, balanço, produção, tributos, proposta |
| U04 Mosaic 2020 — “só bombeamento” | P | P | P | — | — | — | P | — | — | escopo, produção, preço, proposta |
| U05 Bosch 2021 — bags | P | P | P | P | P | — | P | P | — | balanço, produção, BDI, proposta |
| U06 Matinhos/CFF 2021 | P | P | P | — | — | — | P | P | — | edital/CFF, produção, preço, proposta |
| U07 Petrobras 2022 — DFP/PPU | P | P | P | — | — | P | P | P | — | balanço, produção, preço, proposta |
| U08 Suzano Aracruz 2023 | P | P | P | — | — | P | P | R | — | escopo, balanço, produção, preço, proposta |
| U09 Venda FC-001 2024 | — | — | — | — | — | — | — | R | P | configuração, preço, proposta |
| U10 Suzano 2024 — Modelo 02 | P | P | P | — | — | P | P | P | — | balanço, produção, ABC, tributos, proposta |
| U11 Bracell 2025 — COM/SEM polímero | P | P | P | P | P | — | P | — | — | balanço, produção, BDI, proposta |
| U12 SK Confins 2026 — centrífuga | P | R | R | — | — | P | — | R | — | balanço, produção, BDI, proposta |

¹ A coluna Dragagem absorve as ocorrências históricas de bombeamento/recalque. **R** significa residual, zerado ou de responsabilidade de terceiro, conforme a matriz original do Checkpoint 1; não significa bloco confirmado na taxonomia.

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
| Mob. Draga, Mob. MO, Mob. Centrífuga, DesMob | R$/evento, viagens, dias, pessoas | **Mobilização e desmobilização** | principal | U03–U08, U10–U12 | alta; manter fases separadas dentro do bloco. |
| `Canteiro`, administração local, site/SSMA | R$/mês, mês, vb | **Canteiro e apoio local** | principal | U03–U08, U10–U12 | alta; responsabilidades podem zerar itens sem eliminar o bloco. |
| Draga, dragagem consolidada, custo mensal draga | m³/h, h, L/h, R$/mês | **Dragagem** | principal | U01, U03–U08, U10–U11 | alta. |
| bombeamento, recalque, retorno de água, Pond 1→Pond 2 | m³/h, mca, m, kW | modalidade/configuração de **Dragagem** | interno | U03, U04, U06–U07, U10 | **homologado:** não é bloco macro independente; “só bombeamento” preserva-se como alias histórico. |
| linha de recalque, barrilete, tubulação, flutuantes | m, pol, pç, R$ | componente de **Dragagem** | interno | U01, U03–U08, U10–U12 | **homologado quanto à fronteira com Dragagem**; anatomia permanece candidata. |
| `Prep Célula`, PEAD, Bidim, brita | m², m³, h, R$ | **Preparação de célula** | principal | U05–U08, U11 | alta. |
| `Bags`, geotêxtil, dois níveis | un, m, m³, R$/m² | **Bags geotêxteis** | principal | U05–U08, U11 | alta; dimensionamento exige margem e conciliação. |
| centrífuga, decanter, operação/manutenção | m³/h, % ST, tSS, R$/mês | **Desaguamento mecânico** | principal candidato | U01, U07–U08, U10, U12 | alta como família observada; fronteira/nome ainda candidatos. |
| batimetria, medição, coleta/acompanhamento | campanha, mês, R$ | **Batimetria e medição** | principal ou combinado, candidato | U03–U08, U10–U11 | média-alta; laboratório continua gray area. |
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
| B01 | Mobilização e desmobilização | Mob., DesMob., implantação, retirada | precificar logística e equipes de entrada/saída | evento, viagem, dia, pessoa, R$ | combina com qualquer serviço; pode existir isolado em revisão | sim, por frente/equipamento | alta | se comercialmente devem ser dois blocos ou duas fases. |
| B02 | Canteiro e apoio local | canteiro, administração local, site, SSMA | infraestrutura temporária e suporte local | mês, un, vb, pessoa, R$ | independente e combinável | sim, por base/frente | alta | limite entre canteiro e administração central. |
| B03 | Dragagem | draga, dragagem e recalque, sucção, “só bombeamento” | remover e recalcar material; pode configurar bombeamento direto/sem tratamento posterior | m³, t, h, m³/h, L/h, m, mca | combina potencialmente com B04–B08; bombeamento nunca é bloco separado | sim, por draga/frente | alta; fronteira bombeamento homologada | convenção para produção úmida, seca ou in situ. |
| B04 | Preparação de célula | Prep Célula, PEAD/Bidim/brita | construir/preparar área receptora | m², m³, h, un | candidato independente; pode anteceder B05 | sim, por célula | alta | fronteira e impermeabilização. |
| B05 | Bags geotêxteis | bags, geobags, tubos geotêxteis | dimensionar, fornecer e instalar bags | un, m, m², m³, R$ | candidato combinável com B03/B04 | sim, por célula/nível/modelo | alta | regra de margem e arredondamento. |
| B06 | Desaguamento mecânico | centrífuga, decanter, centrifugação | separar sólidos por equipamento mecânico | m³/h, %ST, tSS, t/mês | candidato independente; pode combinar com B03/B08 | sim, por unidade/linha | alta | nome/fronteira e operação/manutenção. |
| B07 | Batimetria e medição | medição, levantamento, coleta | medir volume, evolução e aceite | campanha, mês, ponto, amostra, m³, R$ | candidato independente ou associado | sim, por método/campanha | média-alta | laboratório/garantias. |
| B08 | Transporte e destinação | frete, caçamba, bota-fora, disposição | remover e destinar material/resíduo | t, m³, km, viagem, R$/t | candidato; recebe saída de B03/B05/B06 | sim, por rota/destino | média-alta | fronteira, base de medição e licenças. |
| B09 | Venda de equipamento | venda de draga, fornecimento de ativo | configurar e precificar transferência de ativo | un, R$, conjunto | candidato especializado; serviços podem combinar | sim, por equipamento | alta para a família | fluxo, opcionais, serviços e condição do ativo. |

**Status:** nove blocos candidatos. Apenas está homologado que Bombeamento não constitui o décimo bloco e integra Dragagem. A decisão anterior mantém Mão de obra como componente interno, não bloco global. Para Dados do orçamento, Balanço/Produção, Cronograma, Equipamentos de apoio, Combustível, Polímero, Manutenção/Depreciação, ABC, BDI/Tributos, Formação de preço e Proposta, o papel de cabeçalho, componente, motor ou saída permanece **hipótese de organização V1**, sujeito às gray areas registradas. Tubulação/Barrilete é componente da Dragagem nesta fronteira homologada.

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
| quantidade contratual | quantidade comprometida | unidade escolhida | projeto | C | sim | produção/medição | — | condicional | sim |
| prazo/período | duração ou evento | dia/mês/evento | projeto | C | sim | produção/cronograma | — | sempre | sim |
| itens de composição | recursos e serviços internos | várias | mestre + projeto | Híbrido | sim | quantidade × preço | itens/ativos/funções | detalhe | sim |
| custo calculado | soma da composição | R$ | cálculo | D | não | itens, vigências | — | resumo | sim |
| observação/justificativa | exceção e decisão de engenharia | texto | engenheiro | C | sim | override/alerta | — | condicional | sim |

### 5.2 Anatomia específica

As tabelas abaixo registram o núcleo mínimo. Todo campo contextual, histórico, híbrido e derivado que participe da proposta exige snapshot; campos mestre também exigem cópia quando sua alteração futura mudaria a versão emitida.

#### 5.2.1 B01 — Mobilização e desmobilização

| Campo histórico/sugerido | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| fase | entrada ou retirada | enum | projeto | C | sim | — | fases | sempre, abas internas | sim |
| ativo/conjunto mobilizado | carga principal | ativo | cadastro | M/C | sim | determina veículos/içamento | ativos | sempre | sim |
| origem/destino e distância | rota logística | local, km | projeto | C | sim | frete/viagens | locais | sempre | sim |
| carretas/viagens | dimensionamento | un | plano logístico | C | sim | qtd × preço | transporte | sempre | sim |
| guindaste/munck/rigging | içamento | dia/vb | cotação | Híbrido | sim | qtd × preço | serviços | condicional | sim |
| equipe, dias e horas | montagem/desmontagem | pessoa, dia, h | projeto | C | sim | custo diário da equipe × dias | funções | detalhe | sim |
| ART, exames, treinamento | obrigações | un/vb | projeto/cotação | Híbrido | sim | qtd × preço | itens | condicional | sim |
| custo/preço da fase | total | R$ | cálculo | D | não | soma dos itens; preço na camada comercial | — | resumo | sim |

#### 5.2.2 B02 — Canteiro e apoio local

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| prazo do canteiro | permanência | mês/dia | cronograma | C | sim | quantidade mensal × prazo | — | sempre | sim |
| instalações | container, banheiro, escritório, água/energia | un/mês/vb | projeto/cotação | Híbrido | sim | qtd × preço × prazo | itens | tabela | sim |
| equipe local | administração/SSMA/apoio | pessoa/h | projeto | C | sim | composição de pessoal | funções | tabela | sim |
| consumos/serviços | refeições, limpeza, comunicação, vigilância | mês/un | cotação | Híbrido | sim | qtd × preço × prazo | itens | detalhe | sim |
| responsabilidade por item **(candidato)** | quem fornece/paga | enum | contrato | C | sim | o histórico mostra item ativo, de terceiro, residual ou zerado; o comportamento V1 segue em gray area | responsáveis | condicional | sim |
| custo mensal/total | consolidação | R$/mês, R$ | cálculo | D | não | recorrentes + eventos | — | resumo | sim |

#### 5.2.3 B03 — Dragagem

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| draga/modelo | ativo principal | ativo | cadastro | M | seleção | traz capacidade e parâmetros | ativos | sempre | sim |
| modalidade da dragagem | forma de remoção/recalque, incluindo bombeamento direto sem tratamento posterior | texto/enum candidato | escopo/técnica | C | sim | organiza a configuração sem criar outro bloco | modalidades candidatas | sempre | sim |
| volume e base | quantidade a remover | m³/t + base | levantamento | C | sim | prazo, custo unitário | unidades/base | sempre | sim |
| material/profundidade | condição operacional | texto, m | projeto | C | sim | seleção e produtividade | materiais | sempre | sim |
| origem/destino ou ponto de descarga | pontos do recalque | local/texto | projeto/técnica | C | sim | define percurso e interface | locais | quando aplicável | sim |
| distância/desnível | condição do recalque | m | layout/projeto | C | sim | dimensiona linha e auxiliares | — | quando aplicável | sim |
| vazão nominal | capacidade do ativo | m³/h | cadastro | M | override justificado | produção efetiva | ativos | detalhe | sim |
| bomba auxiliar/booster | equipamento auxiliar observado | ativo/un | cadastro + projeto | M/C | sim | quantidade, horas, consumo e custo | ativos | quando aplicável | sim |
| linha de recalque | tubos, mangotes, flutuantes e conexões por trecho | m, pç, pol/mm | catálogo + projeto | M/C | sim | quantidade × preço/depreciação | tubos/conexões | tabela quando aplicável | sim |
| barrilete | conjunto de tubos, tês, válvulas, mangueiras e bomba quando utilizado | conjunto/pç/m | catálogo + projeto | M/C | sim | soma dos componentes; parcela depreciada quando adotada | itens/ativos | quando aplicável | sim |
| eficiência/concentração | premissas | % | projeto/ensaio | C | sim | `produção_h = vazão × eficiência × concentração` quando aplicável | — | sempre | sim |
| jornada/disponibilidade | regime | h/dia, dia/mês, % | projeto | C | sim | `h_mês = h_dia × dias × disponibilidade` | jornadas | sempre | sim |
| produção/prazo | resultado | m³/h, m³/mês, mês | cálculo | D | não | volume ÷ produção + fases | — | resumo | sim |
| combustível | consumo e preço | L/h, R$/L | ativo + cotação | Híbrido | sim | horas × consumo × preço | combustíveis | detalhe | sim |
| manutenção/depreciação/capital | custo do ativo | %, h, mês, R$ | política vigente | H/D | sim só premissas | valor, residual, vida útil, taxa | políticas | detalhe | sim |
| equipe e apoio | recursos internos | pessoa, ativo, h | projeto | Híbrido | sim | composição comum | funções/ativos | detalhe | sim |

Os campos absorvidos acima vêm da mineração de Dragagem, Bombeamento/retorno e Linha de recalque/barrilete do Checkpoint 1. Não constituem um sub-bloco automático: aparecem somente quando a configuração da Dragagem os utiliza.

#### 5.2.4 B04 — Preparação de célula

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| geometria/quantidade | dimensões e número de células | m, m², un | projeto | C | sim | área = comprimento × largura × qtd | — | sempre | sim |
| coeficientes PEAD/Bidim/brita | consumo por área | m²/m², m³/m² | histórico técnico | M/H | override justificado | quantidade = coeficiente × área | coeficientes | detalhe | sim |
| equipamentos/MO | execução | h/m², pessoa, h | mestre + projeto | Híbrido | sim | coeficiente × área × taxa | ativos/funções | detalhe | sim |
| materiais e preços | composição | m², m³, R$/un | cotação | H | sim | quantidade × preço | itens | tabela | sim |
| custo total/unitário | resultado | R$, R$/m² | cálculo | D | não | soma; total ÷ área | — | resumo | sim |

#### 5.2.5 B05 — Bags geotêxteis

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

#### 5.2.6 B06 — Desaguamento mecânico

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

#### 5.2.7 B07 — Batimetria e medição

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| método | tecnologia/protocolo | enum/texto | projeto | C/M | sim | define recursos e entregáveis | métodos | sempre | sim |
| frequência/campanhas | recorrência | campanha/mês | contrato | C | sim | qtd = prazo × frequência | — | sempre | sim |
| área/pontos/amostras | abrangência | ha, ponto, amostra | projeto | C | sim | esforço/custo | — | condicional | sim |
| equipe/equipamentos/terceiros | composição | h, dia, vb | mestre/cotação | Híbrido | sim | qtd × taxa | serviços/ativos/funções | detalhe | sim |
| critério de medição/aceite | regra contratual | texto/unidade | contrato | C | sim | vincula quantidade faturável | critérios | sempre | sim |
| volume medido | resultado | m³/t | levantamento | H/D | não ou importado | método e campanha | — | por campanha | sim |
| custo total | consolidação | R$ | cálculo | D | não | soma das campanhas | — | resumo | sim |

#### 5.2.8 B08 — Transporte e destinação

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

#### 5.2.9 B09 — Venda de equipamento

| Campo | Significado | Unidade | Origem | Classe | Editável | Fórmula/dependências | Catálogo | Uso/UX | Snapshot |
|---|---|---|---|---|---:|---|---|---|---:|
| ativo/configuração | equipamento ofertado | ativo/conjunto | cadastro | M | seleção | componentes e especificações | ativos | sempre | sim |
| estado/ano/horas | condição na oferta | texto, ano, h | inspeção | H | sim | preço/garantia | ativos/inspeções | sempre | sim |
| componentes incluídos | configuração entregue | un/texto | engenharia comercial | C | sim | custo/configuração | itens | tabela | sim |
| preço-base/avaliação | referência | R$ | política/avaliação | H | sim | formação comercial | avaliações | detalhe | sim |
| opcionais | itens/serviços adicionais | un, R$ | catálogo + projeto | Híbrido | sim | soma opcional | itens/serviços | condicional | sim |
| instalação/treinamento/frete | serviços associados | evento/vb | projeto/cotação | Híbrido | sim | composição própria ou B01 | serviços | condicional | sim |
| garantia/condições | compromisso | texto/período | negociação | C/H | sim | versão da proposta | condições | sempre | sim |
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
| B03 Dragagem | B04/B05/B06/B08 ou ponto de descarga | vazão/volume, material, origem/destino e características | configuração interna de recalque; vínculo entre instâncias é candidato | validar unidade/base; não criar bloco Bombeamento. |
| B04 Célula | B05 Bags | área, geometria, restrições | hipótese: uma célula pode receber N conjuntos | alertar capacidade física; regra ainda não homologada. |
| Balanço de massa | B05/B06/B08 | massa seca, volume desaguado | fórmula com ST e base; propriedade/UX em gray area | impedir mistura t, tSS e m³ sem conversão. |
| B06 Desaguamento mecânico | B08 Transporte/destinação | produto desaguado | vínculo candidato entre instâncias | exigir ST/densidade se converter. |
| Cronograma | B01/B02/todos | fases e duração | derivado + ajustes explícitos | mostrar diferença prazo matemático/comercial. |
| Todos os blocos | Formação de preço | custos por instância e unidade | soma rastreável | não aceitar referência quebrada. |
| Formação de preço | Versão formal | preço, condições, escopo | fechamento cria snapshot imutável | negociação manual exige justificativa. |

As dependências acima são **candidatas**, salvo a incorporação do bombeamento/recalque em B03 Dragagem. Elas descrevem transferências observadas e não autorizam o sistema a escolher a solução de engenharia.

## 8. Relação com cadastros mestres

| Candidato a mestre | Candidato a orçamento/instância | Hipótese de override |
|---|---|---|
| identidade e especificação estável de ativos | ativo escolhido, quantidade, jornada e desempenho adotado | copiar valor mestre; override com justificativa, sem alterar mestre. |
| modelos de bags, itens, unidades e coeficientes de referência | arranjo, níveis, margem e coeficiente adotado | preservar valor original e valor usado. |
| funções, kits, regras e benefícios de referência | efetivo, turnos, adicionais aplicáveis | salários/encargos com vigência no snapshot. |
| insumos e serviços cadastrados | fornecedor, cotação, responsabilidade e quantidade | preço sempre histórico, nunca “atual” retroativo. |
| métodos de medição e políticas de custo | método/critério contratual e parâmetros | regra versionada e visível. |
| tipos de bloco e campos configurados | instâncias, rótulos, ordem e escopo | inativação não afeta versões existentes. |

A evidência classifica tributos, salários, preços, valores de ativos, taxas de capital, BDI e benchmarks como históricos com vigência, ainda que administrados em catálogos. A forma de cadastro e override permanece candidata.

## 9. Diretrizes UX por bloco

Salvo a experiência homologada para Dragagem/bombeamento direto, esta seção é uma **hipótese UX V1** para discussão, não uma regra aprovada.

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
| B01 Mobilização/desmobilização | uma tela com duas subabas, Entrada e Saída, cada qual com a grade conhecida de equipe, frete, içamento, quantidade, preço unitário e total. |
| B02 Canteiro | a composição mensal continua em linhas; prazo e responsabilidades ficam acima, e total mensal/total do período aparece ao lado. |
| B03 Dragagem | o engenheiro escolhe somente Dragagem e configura nela como o material será dragado/recalcado. “Bombeamento direto / sem tratamento posterior” pode ser uma configuração familiar; origem, destino, distância, linha, bombas auxiliares, produção e custos ficam na mesma tela/composição. |
| B04 Preparação de célula | geometria primeiro; depois a tabela PEAD/Bidim/brita/equipamentos com coeficiente, quantidade, preço e total, equivalente à aba atual. |
| B05 Bags | catálogo selecionável e grade por nível/modelo; demanda, capacidade e margem aparecem juntas antes do custo de fornecimento. |
| B06 Desaguamento mecânico | equipamento, ST, vazão e jornada no topo; produção seca/desaguada imediatamente abaixo; periféricos, polímero, equipe e manutenção em composições. |
| B07 Batimetria/medição | método e critério de aceite primeiro; campanhas em linhas com data, área/pontos, equipe/terceiro, resultado e custo. |
| B08 Transporte/destinação | uma grade de rotas: origem, destino, material, base, distância, veículo, viagens, tarifa e total; conversões ficam abertas ao lado. |
| B09 Venda de equipamento | ficha técnica à esquerda e composição comercial à direita/abaixo, com componentes, opcionais, serviços, garantia e preço final. |

Defaults só podem vir de cadastro com origem visível; valores próprios da obra permanecem de digitação direta. Nenhum bloco esconde a memória que hoje o engenheiro consegue inspecionar no Excel.

## 10. Riscos herdados do Excel

| Problema histórico | Blocos afetados | Flexibilidade preservada | Proteção proporcional contra erro silencioso |
|---|---|---|---|
| copiar pasta/aba com dados de outra obra | todos | duplicação continua disponível | identidade única; alerta de cliente/local divergente; origem por campo. |
| `#REF!`, links externos e células quebradas | todos + preço | fórmulas configuráveis/versionadas | nenhum fechamento com erro ou dependência ausente. |
| duas fontes de produção | B03, B05, B06, B08 | engenheiro ajusta premissas | candidato: uma cadeia vigente por instância; propriedade segue em gray area. |
| nome de aba tratado como verdade | B03 e aliases | nomes familiares continuam visíveis | “só bombeamento” é alias; funcionalmente continua Dragagem. |
| mistura m³, t e tSS | B03, B05, B06, B08 | qualquer base pode ser escolhida | candidato: base explícita e conversão rastreável; UX segue aberta. |
| custo zero inferido como ausência | B01, B02, B06, B08 | cliente/terceiro pode fornecer | candidato: distinguir ausente, residual, terceiro e zero; regra segue aberta. |
| valor manual sobrescreve cálculo | todos + preço | negociação/ajuste permitido | guardar calculado e emitido; exigir justificativa curta. |
| BDI/tributos com bases implícitas | preço | práticas atuais continuam possíveis | candidato: explicitar percentual, base, ordem e vigência; detalhes aguardam homologação. |
| cenários tratados como sequência linear | orçamento/versão | duplicação livre | alternativas independentes e linhagem formal. |
| bags sem margem/conciliação | B05 | engenheiro define margem/arranjo | candidato: mostrar capacidade/demanda e alertar; intensidade segue aberta. |
| premissa “chute” sem qualificação | B03/B06 | estimativa continua possível | candidato: mostrar confiança e origem; obrigatoriedade segue aberta. |
| mestre alterado retroativamente | todos | mestre continua administrável | snapshot integral no fechamento. |

## 11. Gray areas ainda abertas

### 11.1 Decisão homologada nesta rodada

**Bombeamento × Dragagem:** Bombeamento não existe como bloco macro independente na V1. Quando há bombeamento de material neste contexto, houve Dragagem. “Bombeamento direto / sem tratamento posterior” é modalidade/configuração interna de Dragagem. Nomes históricos como “só bombeamento” permanecem como aliases para rastreabilidade e jamais significam ausência de dragagem.

### 11.2 Demais gray areas — sem resposta nesta rodada

| Gray area | Observado / insuficiência | Pergunta para Fabio/Merlin |
|---|---|---|
| Mobilização × desmobilização | são itens separados nas ofertas, mas simétricos na composição. | Um bloco com duas fases atende, ou inclusão/ordenação independentes são obrigatórias? |
| Responsabilidade por item / fornecimento do cliente | o histórico distingue FOS, cliente, terceiro, residual e custo zero, mas não define uma única UX/regra. | Responsabilidade deve existir por bloco, por item ou em ambos? Item do cliente fica visível e zerado, excluído ou apenas marcado? |
| Mão de obra interna | decisão anterior afasta bloco global, mas não fecha compartilhamento de equipes entre instâncias. | Como representar uma mesma equipe atendendo mais de um bloco sem duplicar custo? |
| Batimetria/medição × laboratório/garantias | domínio aparece, mas laboratório não tem recorrência suficiente como macroetapa. | Laboratório/qualidade deve ser bloco selecionável ou composição da medição/serviço técnico? |
| Transporte/destinação | é relevante em parte do lote; bases e licenças variam. | Transporte e destinação são um bloco, dois blocos ou fases da mesma instância? |
| Operação/manutenção | aparecem como abas, porém ligadas a ativos técnicos. | Existe orçamento real de operação pura que exija cartão próprio na V1? |
| Locação de equipamento | hipótese conceitual, não confirmada transversalmente. | Locação entra no primeiro catálogo ou aguarda evidência adicional? |
| Venda de equipamento | U09 confirma a família; fronteira com serviços não está fechada. | Venda usa o mesmo fluxo dos serviços ou uma modalidade especializada com camadas comuns? |
| Produção/balanço | parâmetros pertencem ao bloco; resultados alimentam vários blocos. | Qual tela é dona da edição: bloco produtor ou painel técnico compartilhado com vínculo explícito? |
| BDI/tributos | fórmulas e bases variam entre obras. | Quais estratégias atuais precisam ser suportadas nominalmente na V1, sem normalização? |
| Taxonomia/aliases | nove nomes são candidatos; apenas a inexistência de Bombeamento como bloco está homologada. | Quais dos nove nomes devem ser promovidos, fundidos ou renomeados após este checkpoint? |

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
- taxonomia definitiva de laboratório, garantias, locação e operação pura sem novas evidências;
- aprendizado com históricos e sugestão automática de margem/risco.

## 13. Conclusão e recomendação

Resultado desta rodada: nove blocos continuam candidatos e uma única fronteira foi homologada — Bombeamento integra Dragagem como modalidade/configuração. O restante do catálogo só deve avançar mediante tratamento individual das gray areas, reconciliação das unidades e fórmulas críticas, validação de engenharia/custos/comercial e registro explícito das decisões de Fabio/Merlin.

**Ponto de parada:** este documento conclui exclusivamente a missão de catálogo e anatomia sobre as 12 unidades já auditadas. Nenhuma outra obra foi analisada.
