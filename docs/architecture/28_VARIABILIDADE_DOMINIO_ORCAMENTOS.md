# Matriz de Variabilidade do Domínio de Orçamentos

Data: 2026-07-15

Status: referência oficial de variabilidade do domínio. Documento exclusivamente conceitual e documental.

## 1. Objetivo

Este documento registra **onde e por que o domínio de Orçamentos varia**.

Sua finalidade é impedir que uma característica observada em um cliente, obra, família ou cenário específico seja implementada como regra universal do APP FOS.

Regra central:

> O modelo SABESP é o primeiro caso completo de equivalência do MVP, mas não é o modelo universal de Orçamento da FOS.

O Novo Sistema deve suportar múltiplas famílias, clientes, obras, tecnologias, responsabilidades, unidades econômicas e políticas comerciais por configuração de domínio, nunca por condicionais específicas de cliente.

## 2. Níveis oficiais de variabilidade

| Nível | Significado | Exemplo |
|---|---|---|
| Universal | Regra válida para todo orçamento, independentemente da família | identidade, versão, rastreabilidade, origem dos valores |
| Família | Regra ou pacote recorrente apenas em determinada família técnica | bags, centrífuga, batimetria |
| Cliente | Exigência, apresentação, responsabilidade ou condição associada ao cliente | formato comercial, documentação, critérios contratuais |
| Obra | Condição física, operacional ou logística daquele serviço | distância, área disponível, acesso, material |
| Cenário | Alternativa estudada dentro da mesma versão | quantidade de equipamentos, turnos, tecnologia |
| Versão | Decisão congelada em uma revisão específica | preço adotado, cotação, BDI, escopo aprovado |
| Exceção | Situação válida que foge ao padrão sem virar regra geral | item livre, pacote especial, condição singular |

Uma característica poderá variar em mais de um nível.

## 3. Invariantes universais

São universais:

- orçamento possui identidade estável;
- revisão gera versão própria;
- versão congelada não é sobrescrita silenciosamente;
- cenário não mistura resultados com outro cenário;
- valores informados, sugeridos, adotados e calculados são distintos;
- zero real, pendente, não aplicável e responsabilidade do cliente são estados diferentes;
- catálogo mestre e fotografia da versão são distintos;
- fórmula e memória de cálculo são versionadas e rastreáveis;
- pacote possui aplicabilidade explícita;
- item comercial mantém vínculo com sua origem técnica;
- alteração invalida apenas resultados dependentes;
- regras de negócio não pertencem à interface;
- desempenho e continuidade são requisitos funcionais.

Esses invariantes podem orientar código transversal.

## 4. Matriz geral de variabilidade

| Elemento | Universal | Família | Cliente | Obra | Cenário | Versão | Observação |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| Identidade do orçamento | X |  |  |  |  |  | Núcleo universal |
| Versionamento e histórico | X |  |  |  |  | X | Conteúdo varia por versão |
| Família inicial |  | X |  | X | X | X | Orienta sugestões, não impõe template |
| Pacotes aplicáveis |  | X | X | X | X | X | Configuração, não código de cliente |
| Produção |  | X |  | X | X | X | Não existe obrigatoriamente em todas as famílias |
| Volume |  | X | X | X | X | X | Unidade e base variam |
| Prazo |  | X | X | X | X | X | Técnico, custeado e comercial podem divergir |
| Mobilização |  | X | X | X | X | X | Recorrente, mas não universal em forma e custo |
| Canteiro |  | X | X | X | X | X | Pode ser FOS, cliente ou não aplicável |
| Dragagem |  | X |  | X | X | X | Central apenas em famílias aplicáveis |
| Bags/geotêxteis |  | X |  | X | X | X | Não existe fora de famílias compatíveis |
| Célula/paliçada/bacia |  | X | X | X | X | X | Solução física variável |
| Polímero |  | X | X | X | X | X | Pacote opcional; dosagem nunca universal |
| Centrífuga |  | X |  | X | X | X | Família específica |
| Batimetria |  | X | X | X | X | X | Pode ser pacote, método de medição ou serviço principal |
| Transporte/destinação |  | X | X | X | X | X | Responsabilidade precisa ser explícita |
| Desmobilização |  | X | X | X | X | X | Não é automaticamente espelho da mobilização |
| Equipamentos |  | X |  | X | X | X | Configuração e regime variam |
| Equipe |  | X | X | X | X | X | Funções, quantidade e jornada variam |
| Calendário operacional |  | X | X | X | X | X | 22, 26 ou 30 dias não são regra corporativa |
| Eficiência |  | X |  | X | X | X | Deve informar origem e base |
| Teor/concentração de sólidos |  | X |  | X | X | X | Base volumétrica ou mássica precisa ser explícita |
| Capacidade útil |  | X |  | X | X | X | Não equivale automaticamente à capacidade nominal |
| Cotações |  |  | X | X | X | X | Fotografadas por versão |
| Custos unitários |  |  | X | X | X | X | Dependem de data-base e condição |
| BDI |  |  | X | X | X | X | Nunca global e não sinônimo de margem |
| Markup |  |  | X | X | X | X | Base e composição explícitas |
| Margem |  |  | X | X | X | X | Não confundir com BDI |
| Desconto |  | X | X | X | X | X | Decisão comercial rastreável |
| Condições de pagamento |  |  | X | X | X | X | Não pertencem ao motor técnico |
| Unidade econômica |  | X | X | X | X | X | m³, t seca, mês, hora, verba etc. |
| Responsabilidades |  | X | X | X | X | X | FOS, cliente ou terceiro |
| Inclusões e exclusões |  | X | X | X | X | X | Devem ser estruturadas |
| Resumo comercial | X | X | X | X | X | X | Existe como conceito, conteúdo varia |
| Proposta futura | X | X | X | X | X | X | Derivada da versão aprovada |

## 5. Variabilidade por família

### 5.1 Bags, geotêxteis e paliçada/bacia

Candidatos recorrentes:

- balanço de massa e volume;
- linha/barrilete;
- preparação de área;
- bags ou estrutura equivalente;
- polímero opcional;
- dragagem e desaguamento;
- medição;
- responsabilidades de destinação.

Variam:

- quantidade e níveis de bags;
- capacidade adotada;
- geometria da célula;
- uso de polímero;
- responsabilidade por bags, água, energia e destinação;
- unidade de cobrança;
- forma de consolidação comercial.

A SABESP é uma instância desta família, não sua definição completa.

### 5.2 Dragagem com centrífuga

Candidatos recorrentes:

- mobilização da draga;
- mobilização da centrífuga;
- produção e prazo;
- operação de separação;
- equipe e utilidades;
- desmobilização.

Variam:

- capacidade efetiva da centrífuga;
- quantidade de equipamentos;
- regime operacional;
- sólidos de entrada e saída;
- polímero;
- água, energia e rejeito líquido;
- responsabilidade de disposição.

### 5.3 Dragagem e bombeamento direto

Candidatos recorrentes:

- produção;
- linha de recalque;
- equipamentos principais e auxiliares;
- mobilização;
- operação;
- medição;
- desmobilização.

Variam:

- distância e desnível;
- booster;
- destino do material;
- quantidade de dragas/bombas;
- jornada;
- unidade econômica;
- escopo de apoio e canteiro.

### 5.4 Batimetria e levantamentos

Candidatos recorrentes:

- metodologia;
- equipe;
- equipamentos;
- mobilização;
- levantamento;
- processamento;
- relatório/entregável.

Produção e volume podem não governar o orçamento. O direcionador pode ser área, dia, campanha, ponto, seção ou verba.

### 5.5 Composições, equipamentos e equalizações

Candidatos recorrentes:

- configuração do recurso;
- regime de uso;
- consumos;
- equipe opcional;
- manutenção;
- depreciação;
- custo horário, diário ou mensal.

Nem todo modelo desta família representa um orçamento completo. Alguns são submodelos reutilizáveis ou documentos comparativos.

## 6. Regras de implementação

### 6.1 Proibições

É proibido implementar lógica como:

```text
se cliente == "SABESP"
```

```text
calcular_bags_sabesp()
```

```text
BDI_PADRAO_FOS = valor_historico_de_um_modelo
```

```text
mostrar_polimero = verdadeiro_para_todos
```

```text
producao_obrigatoria = verdadeiro_para_todas_as_familias
```

Também é proibido:

- usar nome do cliente para selecionar fórmula técnica;
- transformar aba histórica em etapa universal;
- tornar obrigatório um campo apenas porque aparece no Excel de referência;
- usar zero para representar não aplicável ou responsabilidade do cliente;
- promover constante histórica a parâmetro corporativo sem homologação;
- misturar regra de família com regra comercial de cliente.

### 6.2 Forma correta

A seleção deverá seguir conceitos como:

```text
Família
→ capacidades técnicas
→ pacotes sugeridos
→ aplicabilidade do cenário
→ fórmulas versionadas
→ parâmetros adotados
```

O cliente poderá influenciar:

- responsabilidades;
- exigências documentais;
- critérios comerciais;
- forma de apresentação;
- condições contratuais.

O cliente não deverá ser a chave oculta da lógica técnica.

## 7. Classificação obrigatória de novos elementos

Antes de criar qualquer novo campo, fórmula, pacote ou validação, o Kid Step deverá responder:

1. É universal?
2. É específico de família?
3. Varia por cliente?
4. Varia pela obra?
5. Varia por cenário?
6. Deve ser fotografado por versão?
7. É apenas uma exceção?
8. Qual evidência sustenta a classificação?

Se a classificação não estiver clara, o elemento entra como provisório e configurável, nunca como regra universal.

## 8. Critério de revisão dos Kid Steps

Todo Kid Step funcional de Orçamentos deverá incluir uma verificação de variabilidade:

| Pergunta | Evidência esperada |
|---|---|
| A implementação cita cliente específico? | Deve ser não, salvo texto/apresentação explicitamente contextual |
| O pacote é ativável? | Estado de aplicabilidade e motivo |
| O parâmetro foi generalizado? | Fonte e homologação |
| A fórmula declara família/aplicabilidade? | Contrato da fórmula |
| O campo é realmente obrigatório? | Regra universal ou condição explícita |
| O resultado mistura cenários? | Deve ser não |
| O valor mestre altera histórico? | Deve ser não; fotografia preservada |
| O teste cobre ausência do pacote? | Obrigatório para pacote opcional |

## 9. Aplicação ao MVP SABESP

O MVP SABESP serve para provar:

- separação de camadas;
- persistência;
- motor incremental;
- pacotes;
- memória de cálculo;
- formação de preço;
- fluxo e desempenho.

Ele não autoriza concluir que:

- toda obra usa bags;
- toda obra usa polímero;
- toda obra possui volume e produção;
- toda obra utiliza os mesmos equipamentos;
- toda obra possui o mesmo BDI;
- todo cliente recebe a mesma apresentação;
- todas as famílias percorrem as mesmas etapas.

O código do MVP deverá nascer preparado para outras combinações de pacotes, mesmo que somente a combinação SABESP esteja implementada inicialmente.

## 10. Expansão após o MVP

Após homologar integralmente a SABESP, a expansão deverá ocorrer por representantes de família, nesta ordem conceitual:

1. dragagem/bombeamento direto;
2. centrífuga;
3. batimetria;
4. composição/equipamento;
5. exceções e combinações híbridas.

Cada expansão deverá validar o núcleo já implementado e acrescentar apenas capacidades que realmente faltarem.

## 11. Relação com os documentos oficiais

Este documento:

- complementa `22_DOMINIO_ORCAMENTOS.md`;
- restringe a interpretação de universalidade em `23_MODELO_LOGICO_DADOS_ORCAMENTOS.md`;
- orienta aplicabilidade de fórmulas em `24_MOTOR_CALCULO_ORCAMENTOS.md`;
- orienta telas condicionais em `25_FLUXO_USUARIO_ORCAMENTOS.md`;
- protege a arquitetura física de `26_ARQUITETURA_FISICA_ORCAMENTOS.md`;
- torna-se critério transversal do plano em `27_PLANO_KID_STEPS_ORCAMENTOS.md`.

Em caso de dúvida, as evidências das análises individuais e dos documentos de família devem ser consultadas antes de universalizar comportamento.

## 12. Decisão final

> O Novo Sistema de Orçamentos será desenvolvido por capacidades, pacotes e regras aplicáveis, e não por clientes ou cópias de planilhas.

A SABESP é o primeiro teste vertical completo. As cinco famílias e os 49 modelos definem o espaço de variabilidade que a arquitetura deve respeitar.