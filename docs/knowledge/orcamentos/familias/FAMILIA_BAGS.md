# Família de Orçamentos — Bags, Geotêxteis e Paliçada/Bacia

## Status e cobertura

Consolidação de domínio da Fase 3. Reúne 22 modelos: `003`, `016`, `018`, `019`, `020`, `021`, `024`, `027`, `029`, `030`, `031`, `033`, `034`, `036`, `037`, `038`, `039`, `040`, `041`, `042`, `043` e `045`.

O modelo `016` possui análise semântica aprofundada. Os demais sustentam principalmente evidência estrutural, fórmulas, nomes de abas e conceitos; por isso, recorrência não significa regra universal. Os modelos `036` e `037`, classificados originalmente como paliçada/bacia, entram nesta família porque tratam outra solução de contenção/desaguamento e formam um par comparável com/sem polímero.

## Objetivo da família

Formar preço para remover sedimentos por dragagem hidráulica e acondicioná-los/desaguá-los em bags geotêxteis ou em estruturas de contenção equivalentes. A solução combina transporte hidráulico, preparação da área, contenção do material, drenagem, possível uso de polímero, medição e responsabilidades de destinação.

A unidade econômica costuma ser m³ dragado/desaguado, mas pacotes fixos usam verba, peça, m², mês, dia, hora, kg e tonelada seca.

## Núcleo comum observado

1. Identificação da obra e premissas de volume, material, sólidos, linha e jornada.
2. Produção da draga e prazo operacional.
3. Linha/barrilete para condução e distribuição da polpa.
4. Mobilização da draga e do sistema de polímero quando aplicável.
5. Canteiro e equipe.
6. Preparação da célula, bacia ou estrutura de contenção.
7. Dimensionamento/fornecimento de bags ou solução equivalente.
8. Operação de dragagem e desaguamento.
9. Medição, amostragem, batimetria ou controle.
10. Desmobilização e consolidação comercial.

## Diferenças internas

- Bags em um nível, dois níveis ou arranjos híbridos.
- Célula impermeabilizada com PEAD/bidim/brita, paliçada ou bacia preparada.
- Operação com ou sem polímero.
- Fornecimento dos bags pela FOS, pelo cliente ou incluído em item composto.
- Separação ou agrupamento entre dragagem, bags e operação da planta.
- Volume in situ, massa seca ou volume desaguado como direcionador.
- Carga, transporte e destinação incluídos, opcionais ou de responsabilidade do cliente.
- Planilha de BDI própria e resumo técnico/comercial em alguns modelos.
- Reinício/repetição de célula, capacidade por bag e restrição de área em configurações específicas.

Os pares `029/030`, `031/032`, `036/037`, `039/040` e `041/042` são especialmente úteis para distinguir revisão, tecnologia e presença de polímero sem confundir arquivos semelhantes.

## Pacotes utilizados

| Pacote | Papel na família | Aplicabilidade |
|---|---|---|
| Premissas e produção | Define quantidade, vazão, eficiência, sólidos, prazo e linha | Estrutural, exceto quando preço for exclusivamente mensal |
| Barrilete/linha | Distribui polpa, válvulas, mangueiras e bombas auxiliares | Geralmente necessário, configuração variável |
| Mobilização da draga | Logística, montagem, guindaste, carretas e equipe | Estrutural quando equipamento é da FOS |
| Mobilização do sistema | Cobertura, piso, hidráulica, elétrica e polímero | Opcional conforme tecnologia |
| Canteiro | Apoio, documentação, segurança, integração e utilidades | Variável por responsabilidade do cliente |
| Preparo da área/célula | Terraplenagem, PEAD, bidim, brita, paliçada ou bacia | Opcional e dimensionável |
| Bags/geotêxteis | Seleção, quantidade, frete, descarga e instalação | Central nos modelos de bags |
| Polímero | Equipamento, dosagem, produto, água, energia e operação | Ativável; não universal |
| Dragagem | Equipamento, combustível, pessoal, manutenção e linha | Central |
| Medição/controle | Batimetria, amostras, acompanhamento e relatórios | Conforme contrato |
| Transporte/destinação | Carga, distância, veículo, taxa e descarte | Opcional/responsabilidade explícita |
| Desmobilização | Retirada da draga, planta e canteiro | Pacotes separados |

## Parâmetros recorrentes

- volume in situ e volume total;
- percentual de sólidos in situ e após desaguamento;
- vazão, eficiência e concentração da draga;
- jornada, dias/mês e horas produtivas;
- dimensões, capacidade e fator de enchimento dos bags;
- área disponível, níveis e número de células/repetições;
- coeficientes de PEAD, geotêxtil drenante, brita e mão de obra por m²;
- dosagem e preço do polímero;
- linha flutuante/terrestre, perdas e acessórios;
- salários, encargos, refeições, transporte e integração;
- manutenção, depreciação, juros, BDI e arredondamento do prazo;
- distância, densidade/volume transportado e taxa de destinação.

Todo parâmetro exige unidade, origem, vigência, valor sugerido e valor adotado separados.

## Fórmulas recorrentes

```text
horas_mês = horas_dia × dias_mês
produção_horária = vazão × eficiência × concentração
produção_mensal = produção_horária × horas_produtivas_mês
prazo = quantidade_total ÷ produção_mensal
massa_seca = volume_in_situ × fração_sólidos_in_situ
volume_desaguado = massa_seca ÷ fração_sólidos_desaguado
quantidade_bags = volume_a_acondicionar ÷ capacidade_adotada_por_bag
consumo_polímero = massa_seca × dosagem
quantidade_material_célula = área_célula × coeficiente_por_m²
custo_recurso = quantidade × preço_unitário
preço_pacote = custo_pacote × (1 + BDI)
```

As expressões são conceituais. Eficiência, concentração, capacidade útil, perdas, arredondamentos e níveis variam por modelo.

## Exceções conhecidas

- Paliçada/bacia sem bag como peça unitária.
- Bags em dois níveis e célula reiniciada.
- Solução com polímero e sua variante sem polímero.
- Água e energia fornecidas pelo cliente.
- Transporte/destinação fora do escopo.
- Preço agregado de dragagem + operação + fornecimento do bag.
- Medição em unidade diferente da unidade de cobrança principal.
- Área disponível que limita o arranjo físico antes do custo.

## Riscos

- Confundir volume in situ, volume de polpa, volume desaguado e massa seca.
- Generalizar capacidade nominal de bag como capacidade útil.
- Duplicar custo de bag, instalação ou polímero entre pacote técnico e item comercial.
- Aplicar BDI em composição e novamente no consolidado.
- Tratar zero como ausência quando significa responsabilidade do cliente.
- Usar cotação antiga ou sem fornecedor/data.
- Ocultar dependência de água, energia, área e destinação.
- Copiar coeficientes físicos sem validar solo, sólidos e geometria.
- Recalcular toda a proposta quando apenas dosagem ou preço do polímero mudou.

## Oportunidades de padronização

- Balanço de massa e volume com unidades explícitas.
- Catálogo versionado de bags por dimensões, capacidade nominal, capacidade adotada e fornecedor.
- Biblioteca de arranjos de célula/paliçada com coeficientes auditáveis.
- Pacote de polímero independente e ativável.
- Matriz de responsabilidades para água, energia, área, descarga e destinação.
- Grafo de dependências para recalcular somente bags, célula, polímero ou consolidado afetados.
- Resumo técnico separado do comercial.
- Alertas para sólidos incompatíveis, área insuficiente, bag fracionário e cotação vencida.

## Candidatos ao núcleo do novo sistema

- Orçamento e versão imutável.
- Cenário técnico e unidade econômica.
- Premissa com unidade/origem.
- Valor sugerido e valor adotado.
- Pacote ativável com aplicabilidade e responsabilidade.
- Recurso, cotação e fotografia do catálogo.
- Fórmula explicável e resultado calculado.
- Dependência entre resultados/pacotes.
- Validação, alerta e histórico de decisão.
- Consolidação técnica e resumo comercial.

## Pendências de homologação

- Critério oficial de capacidade útil dos bags.
- Política para dosagem de polímero e teste de bancada.
- Regra de arredondamento de quantidade de bags/células.
- Incidência correta de BDI por pacote.
- Forma oficial de apresentar exclusões e responsabilidades.
- Distinção validada entre famílias bags, paliçada e bacia.

