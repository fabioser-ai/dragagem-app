# Família de Orçamentos — Batimetria e Levantamentos

## Status e cobertura

Consolidação dos modelos `006`, `017`, `022` e `026`. O modelo `006` possui aprofundamento semântico. Os modelos `017`, `022` e `026` compartilham estrutura quase paralela de mobilização de equipe, batimetria terceirizada, relatório final, desmobilização e formação de preço.

## Objetivo da família

Formar preço para levantar geometria/volume, coletar dados ou amostras, acompanhar campo e produzir relatório, projeto ou escopo técnico. A batimetria pode ser serviço principal autônomo ou pacote auxiliar de uma futura dragagem.

A unidade econômica pode ser verba, visita, dia, amostra, lagoa ou m². Volume e produção de draga não são obrigatórios.

## Núcleo comum

1. Identificação do cliente, local, corpos d'água/estruturas e finalidade.
2. Geometria ou área a levantar.
3. Mobilização de equipe e terceiros.
4. Execução da batimetria/levantamento.
5. Acompanhamento FOS e logística.
6. Relatório final, projeto ou escopo.
7. Desmobilização.
8. Consolidação do custo, BDI e preço.

## Diferenças internas

- Batimetria simples versus batimetria acompanhada de amostragem e caracterização NBR 10004.
- Contratação de terceiro por m², verba ou campanha.
- Projeto/escopo de dragagem incluído ou relatório apenas.
- Quantidade de lagoas, pontos/amostras e visitas.
- Equipe própria maior ou simples acompanhamento.
- Mobilização/desmobilização explícitas ou embutidas no serviço do terceiro.
- Indicador comercial por m² ou itens globais.

## Pacotes utilizados

| Pacote | Conteúdo típico |
|---|---|
| Premissas/geometria | lagoas, dimensões, áreas, profundidades, quantidades |
| Mobilização | viagens, integração, documentação, hospedagem, alimentação e apoio |
| Amostragem | plano, coleta, recipientes, transporte e cadeia de custódia |
| Laboratório | ensaios e caracterização |
| Batimetria | subcontratada, equipamento, equipe e processamento |
| Acompanhamento | mão de obra FOS e segurança |
| Relatório/projeto | engenharia, desenho, volume e escopo |
| Desmobilização | retorno e encerramento |
| Consolidação | custo, BDI, preço global e indicador unitário |

## Parâmetros recorrentes

- quantidade e tipo de lagoa/área;
- largura, comprimento, profundidade e área;
- pontos, seções, resolução e quantidade de amostras;
- dias/visitas de campo;
- quantidade e custo da equipe;
- preço do terceiro por m², diária ou verba;
- número/tipo de ensaios;
- viagem, hospedagem, alimentação e mobilização;
- dias de engenharia/relatório;
- BDI e arredondamentos.

## Fórmulas recorrentes

```text
área_elemento = largura × comprimento × quantidade
área_total = soma(áreas_elementos)
amostras_total = soma(amostras_por_elemento × quantidade_elementos)
custo_terceiro = quantidade_medida × preço_unitário
custo_equipe = quantidade_pessoas × custo_hora × horas × encargos
custo_pacote = terceiros + equipe + logística + despesas
preço_pacote = custo_pacote × (1 + BDI)
preço_por_m² = preço_total ÷ área_total
```

O cálculo de produção de draga aparece nos quatro modelos, mas no aprofundamento do `006` ficou zerado e não alimentou o resumo. Portanto, é template residual ou informação opcional, não núcleo da família.

## Exceções

- Amostragem e laboratório sem batimetria completa.
- Projeto/escopo após o levantamento.
- Áreas múltiplas com planos de amostragem diferentes.
- Subcontratada que inclui mobilização própria.
- Preço global sem unidade física final.
- Batimetria como apoio de medição em outra família.

## Riscos

- Forçar volume/produção de dragagem onde não se aplica.
- Confundir área de levantamento com volume de sedimento.
- Quantidade de amostras sem fundamento técnico documentado.
- Cotação de terceiro sem data, escopo ou precisão.
- Dividir por prazo/quantidade zerados: o modelo `006` contém 12 `#DIV/0!` em blocos não alimentados.
- Aplicar BDI novamente sobre preço já fornecido pelo terceiro.
- Não registrar precisão, datum, método, entregável e responsabilidade técnica.
- Usar rótulos herdados de canteiro/dragagem em serviço de levantamento.

## Oportunidades de padronização

- Cadastro do corpo d'água/estrutura e sua geometria.
- Plano de levantamento com método, resolução e entregáveis.
- Plano de amostragem separado, vinculável à área.
- Catálogo de ensaios e fornecedores versionados.
- Pacotes ativáveis de amostragem, laboratório, batimetria e projeto.
- Indicadores por m², ponto, amostra, visita e verba.
- Validação de área zero, plano incompleto e cotação vencida.
- Reutilização como pacote de medição em outras famílias.

## Candidatos ao núcleo do novo sistema

- Local/elemento mensurável.
- Geometria e unidade.
- Plano técnico e entregável.
- Serviço de terceiro/cotação.
- Pacote de campo, laboratório ou engenharia.
- Responsável técnico e validação.
- Resultado medido versus resultado estimado.
- Aplicabilidade explícita da produção/prazo.
- Consolidação e indicador unitário.

## Pendências

- Critério técnico para quantidade de amostras/pontos.
- Método, precisão e entregável padrão.
- Quando mobilização do terceiro está inclusa.
- BDI aplicável a serviço terceirizado e laboratório.
- Forma comercial preferida: verba, m², visita ou pacote misto.

