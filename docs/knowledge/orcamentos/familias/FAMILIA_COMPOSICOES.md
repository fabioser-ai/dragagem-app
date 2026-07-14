# Família Transversal — Composições, Equipamentos e Equalizações

## Status e cobertura

Consolidação de nove modelos que não pertencem integralmente a uma única família operacional: `001`, `002`, `004`, `009`, `010`, `011`, `015`, `048` e `049`.

Inclui composição de mão de obra, equalização técnica, composições padrão da draga 14, composição específica com vários equipamentos, motobomba e o arquivo legado `.xls` ainda pendente. O modelo `004` possui aprofundamento semântico; o `049` não foi convertido/analisado e permanece apenas identificado.

## Objetivo da família

Preservar modelos reutilizáveis ou transversais usados para:

- formar custo de equipamento, equipe ou serviço;
- comparar alternativas técnicas/comerciais;
- precificar locação/operação padrão;
- servir de base para famílias operacionais;
- documentar composições específicas que não justificam ainda uma família própria.

Esta família é uma zona de consolidação de conhecimento, não uma categoria final de produto.

## Núcleo comum

1. Identificação do equipamento/serviço e condição de uso.
2. Recursos: mão de obra, equipamento, insumo, logística e apoio.
3. Quantidade, unidade, incidência e preço unitário.
4. Custo horário, diário, mensal ou total.
5. Manutenção, depreciação e financeiras quando aplicáveis.
6. BDI/margem e preço final.
7. Cenários com/sem equipe, desconto, quantidade ou configuração.
8. Resumo ou equalização para tomada de decisão.

## Diferenças internas

- **Mão de obra (`001`):** equipe, turnos, salários, mobilização, operação e desconto máximo.
- **Equalização (`002`):** comparação técnica pontual, com pouca fórmula e forte conteúdo decisório.
- **Draga 14 (`004`, `009`, `010`, `011`, `049`):** com equipe, sem equipe, variações SBV e arquivo legado.
- **Composição específica (`015`):** hidrotrator, escavadeira, caminhão/combóio, triturador, medição e logística.
- **Motobomba (`048`):** equipamento isolado com composição compacta.

## Pacotes utilizados

- ficha técnica/econômica do equipamento;
- equipe/turno;
- mobilização/desmobilização;
- operação/locação;
- combustível e insumos;
- manutenção/reposição;
- depreciação, juros e risco;
- linha/acessórios;
- apoio/logística;
- medição;
- desconto, BDI e preço final;
- comparação/equalização.

## Parâmetros recorrentes

- potência, vazão, capacidade e disponibilidade;
- jornada, dias/mês e regime de turno;
- quantidade/função, salário, custo-hora e encargos;
- consumo de combustível/lubrificante;
- valor do equipamento, vida útil, valor residual e manutenção;
- prazo, intensidade de uso e incidência temporal;
- frete, carga, montagem e desmontagem;
- BDI, desconto, margem e preço mínimo;
- responsabilidade por equipe, combustível, apoio e manutenção.

## Fórmulas recorrentes

```text
custo_hora_mão_obra = salário_base ÷ horas_base + adicionais
custo_equipe_período = soma(quantidade × custo_hora × horas × encargos)
custo_combustível_hora = consumo_hora × preço_combustível
depreciação_período = base_depreciável ÷ vida_útil
manutenção_período = valor_equipamento × taxa_manutenção
custo_equipamento = operação + pessoal + manutenção + apoio + financeiras
custo_unitário = custo_total ÷ unidade_produtiva
preço = custo × (1 + BDI ou margem)
desconto = 1 − preço_proposto ÷ preço_referência
```

BDI, margem e desconto não são sinônimos e não devem compartilhar um único campo.

## Exceções

- Equipamento sem equipe.
- Composição apenas de mão de obra.
- Equalização que compara propostas sem formar preço completo.
- Locação mensal sem produção garantida.
- Equipamentos auxiliares combinados em solução específica.
- Arquivo `.xls` sem análise estrutural completa.
- Preço mínimo ou desconto máximo como saída principal.

## Riscos

- Tratar composição padrão como orçamento completo.
- Duplicar equipe/equipamento ao inserir composição em pacote operacional.
- Misturar custo, preço, BDI, margem e desconto.
- Reutilizar cotação ou salário sem vigência.
- Usar vida útil/manutenção idênticas para ativos diferentes.
- Não distinguir com/sem equipe e responsabilidades.
- Transformar equalização técnica em regra de cálculo.
- Considerar o `049` analisado antes de conversão controlada.
- Criar família permanente para cada planilha específica.

## Oportunidades de padronização

- Composição reutilizável com versão e fotografia no orçamento.
- Recurso com unidade e incidência temporal.
- Equipamento com ficha técnica e econômica separadas.
- Configuração com/sem equipe, combustível, manutenção e operador.
- Modelo de turno/equipe compartilhável.
- Comparador de cenários sem alterar a composição-base.
- Separação entre custo técnico, política comercial e preço adotado.
- Catálogo de composições aprovadas com origem e validade.

## Candidatos ao núcleo do novo sistema

- Composição e versão de composição.
- Recurso e categoria de recurso.
- Incidência: única, horária, diária, mensal ou por produção.
- Equipamento/configuração.
- Equipe/turno.
- Fotografia de preço/salário/cotação.
- Custo calculado, markup, margem, BDI, desconto e preço adotado separados.
- Cenário e comparação.
- Responsabilidade e aplicabilidade.
- Validação de unidade, vigência e dupla contagem.

## Pendências

- Critério para aprovar uma composição como padrão corporativo.
- Separação oficial entre BDI, margem e desconto.
- Política de atualização de salários, combustível e equipamentos.
- Forma de incorporar composição sem duplicar recursos no pacote.
- Conversão/análise controlada do modelo `049`.
- Destino futuro dos modelos `002`, `015` e `048` após mais evidência.

