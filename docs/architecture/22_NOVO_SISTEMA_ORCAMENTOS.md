# Fundação Arquitetural Provisória — Novo Sistema de Orçamentos

Data: 2026-07-14

Status: proposta arquitetural documental; nenhuma implementação autorizada nesta sessão.

## 1. Autoridade e contexto

Esta fundação resulta de:

- decisão de produto do Fabio de não proteger funcionalidades legadas sem benefício comprovado;
- homologação arquitetural da descoberta registrada na AUDIT_052;
- estratégia de engenharia reversa dos orçamentos reais;
- conhecimento provisório do primeiro modelo, `D_004_2026 - SABESP.xlsx`.

O modelo SABESP demonstra uma rede de premissas, cálculos de engenharia, pacotes, composições, cotações, custos e consolidação comercial. Como apenas um modelo foi completamente documentado, suas fórmulas e estruturas específicas não são declaradas universais.

## 2. Decisões de produto homologadas

### 2.1 Princípio central

> Preservar dados e conhecimento úteis. Preservar funcionalidades legadas somente quando houver benefício comprovado.

Consequências:

- compatibilidade com o fluxo atual não é requisito automático;
- comportamento incompleto, incorreto ou sem uso crítico comprovado pode ser substituído;
- quebra deliberada é aceitável quando documentada, testada e aprovada;
- dados não podem ser apagados sem classificação e validação;
- conhecimento dos Excel, decisões do engenheiro e rastreabilidade têm prioridade sobre o código legado.

### 2.2 Objetivo do novo sistema

Permitir aos engenheiros da FOS:

- elaborar e versionar orçamentos;
- aplicar conhecimento validado dos Excel reais;
- informar, receber sugestões e adotar parâmetros conscientemente;
- ativar ou marcar etapas opcionais como não aplicáveis;
- visualizar memórias de cálculo;
- compor custos e preços por pacotes;
- consolidar resultados técnicos e comerciais;
- preservar entradas, decisões, cálculos e alterações;
- utilizar futuramente histórico orçado e realizado como apoio, sem substituir a decisão do engenheiro.

O primeiro marco de equivalência funcional será reproduzir o orçamento `D_004_2026 - SABESP.xlsx`.

## 3. Critérios arquiteturais

1. **Rastreabilidade antes de conveniência:** valor sugerido, valor adotado, origem e alteração não podem ser confundidos.
2. **Versão imutável como referência histórica:** uma versão emitida deve permanecer reproduzível; revisão gera nova versão.
3. **Cadastro mestre não substitui fotografia:** alterações futuras em catálogos não mudam silenciosamente um orçamento anterior.
4. **Cálculo explicável:** resultados devem expor memória, entradas, regra aplicada e dependências.
5. **Aplicabilidade explícita:** componente não aplicável é decisão rastreável, não ausência ambígua de dados.
6. **Pacotes com dependências:** o orçamento não é forçado a uma sequência puramente linear; um pacote pode consumir resultados de outro.
7. **Conhecimento progressivo:** uma regra observada em um Excel não se torna regra universal antes de validação e crosscheck.
8. **Substituição deliberada:** o legado pode deixar de funcionar, mas somente por mudança separada, documentada e reversível quando necessário.

## 4. Modelo conceitual provisório

Este modelo orienta responsabilidades. Ele não fixa tabelas, arquivos, colunas ou cardinalidades finais.

| Conceito | Responsabilidade provisória |
|---|---|
| Orçamento | Identidade estável do processo orçamentário, cliente, objeto e ciclo de vida geral |
| Versão do Orçamento | Fotografia reproduzível de uma revisão, com estado, autoria, datas e origem |
| Etapa | Unidade navegável de elaboração ou validação |
| Aplicabilidade | Decisão de executar ou não uma etapa opcional, com motivo, autor e histórico |
| Parâmetro | Grandeza necessária a uma decisão ou cálculo, com unidade e domínio |
| Valor Sugerido | Valor de catálogo, regra, histórico ou modelo apresentado como apoio |
| Valor Adotado | Valor efetivamente escolhido pelo engenheiro, preservando sua origem e justificativa quando alterado |
| Pacote | Bloco técnico ou comercial como mobilização, preparo, fornecimento, operação, medição ou desmobilização |
| Composição | Formação de custo ou preço de um pacote ou item |
| Item | Elemento quantificado dentro de pacote, composição ou consolidação |
| Recurso | Mão de obra, material, equipamento, insumo, serviço ou terceiro utilizado por uma composição |
| Cotação | Evidência temporal de preço, fornecedor, contato, escopo e data-base |
| Resultado Calculado | Saída derivada com memória, regra, entradas e dependências preservadas |
| Validação | Confirmação, ressalva ou rejeição de entrada, cálculo, etapa ou versão |
| Histórico de Alteração | Registro de quem alterou o quê, quando, origem anterior e motivo disponível |

### 4.1 Separações obrigatórias

O desenho físico posterior deverá distinguir:

- cadastro mestre reutilizável;
- fotografia do cadastro usada por uma versão;
- entrada direta do engenheiro;
- sugestão apresentada;
- decisão adotada;
- regra ou fórmula aplicada;
- resultado calculado;
- validação;
- histórico de alteração.

Não é aceitável reproduzir em um único campo a ambiguidade atual entre referência mestre, entrada e resultado.

## 5. Aplicabilidade das etapas

Decisão aprovada:

- o orçamento será dividido em etapas ou telas;
- etapas opcionais poderão receber o estado `Não aplicável`;
- uma etapa não aplicável será excluída dos cálculos que dependem de sua execução;
- dados preenchidos anteriormente serão preservados;
- a etapa poderá ser reativada;
- desativação e reativação serão rastreáveis;
- etapas estruturais obrigatórias não poderão ser desativadas;
- `Não aplicável` nunca significará exclusão física.

### 5.1 Regras que ainda exigem desenho

- quais etapas são estruturais;
- quais famílias de obra oferecem cada etapa;
- como dependências reagem à mudança de aplicabilidade;
- quais validações bloqueiam emissão ou consolidação;
- como resultados dependentes são marcados para recálculo.

Essas regras não serão inferidas de um único Excel.

## 6. Equivalência com os Excel

O novo sistema não precisa ser equivalente ao módulo legado. O alvo de equivalência é o conhecimento válido das planilhas da FOS.

Critério inicial:

```text
mesmas entradas validadas do Excel
            ↓
mesmos resultados intermediários e finais no APP
```

Para o modelo SABESP, a validação futura deverá abranger:

- premissas da obra;
- produção horária e mensal;
- prazo;
- dimensionamentos de célula, bags e outros componentes aplicáveis;
- custos por pacote;
- dependências entre pacotes;
- BDIs nos níveis efetivamente validados;
- custo e preço final;
- consolidação técnica detalhada;
- consolidação comercial simplificada;
- memória e origem dos valores adotados.

Fórmulas quebradas, percentuais embutidos e interpretações ainda pendentes não devem ser copiados sem decisão explícita.

## 7. Estratégia para o legado

### 7.1 Comparação das alternativas

| Opção | Benefícios | Custos e riscos | Adequação observada |
|---|---|---|---|
| A — Coexistência temporária | Reversão imediata e comparação visual | Dois fluxos de edição, confusão para usuários, manutenção dupla e risco de continuar produzindo dados no agregado incompleto | Útil apenas se houver uso crítico do fluxo antigo, ainda não comprovado |
| B — Substituição imediata de acesso | Entrada única, implementação mais clara e interrupção de novos registros no modelo incompleto | Exige comunicar a quebra e oferecer consulta ao histórico quando necessária | **Recomendada** para o estado de produto informado por Fabio |
| C — Aposentadoria completa | Menor superfície permanente e nenhuma manutenção do fluxo antigo | Exige resolver antes a rota Obras, consulta histórica, dados úteis e reversão | Destino provável, mas prematuro como primeira mudança |

### 7.2 Recomendação

Adotar **Opção B — Substituição imediata de acesso**, em evolução controlada para a Opção C.

Estratégia:

1. preservar integralmente `data/orcamentos.csv`;
2. interromper a criação e edição de registros pelo acesso principal antigo;
3. direcionar o cartão Orçamentos ao novo domínio;
4. manter inicialmente as páginas e rotas antigas no código, sem acesso principal, como janela de reversão técnica curta;
5. oferecer posteriormente `Histórico de Orçamentos Antigos` em leitura;
6. retirar o acoplamento da rota Obras em Kid Step próprio;
7. remover rotas e páginas antigas somente após consulta histórica, dependências e reversão estarem validadas.

A coexistência recomendada é de **dados**, não de dois sistemas editáveis.

## 8. Histórico de orçamentos antigos

Alternativa aprovada à manutenção funcional completa do legado:

```text
Novo Sistema de Orçamentos
└── Histórico de Orçamentos Antigos
```

Responsabilidade futura:

- ler `data/orcamentos.csv` sem alterá-lo;
- identificar claramente a origem legada;
- localizar e visualizar registros antigos;
- apresentar campos preservados com seus limites semânticos;
- impedir edição pelo fluxo antigo;
- apoiar migração seletiva futura;
- distinguir falha de leitura de ausência de registros.

Esta consulta não será implementada nesta sessão e não transforma cada linha antiga automaticamente em uma versão válida do novo modelo.

## 9. Tratamento dos dados de `data/orcamentos.csv`

Nenhum dado será descartado nesta fase.

### 9.1 Identificação e contexto

| Campos | Classificação provisória | Tratamento proposto |
|---|---|---|
| `Codigo`, `Cliente`, `Nome_Obra`, `Local`, `Data`, `Data_Criacao`, `Ultima_Atualizacao` | Identificação e contexto | Preservar para consulta; migrar seletivamente após validar identidade, cliente e datas |
| `Status`, `Etapa_Atual` | Estado do fluxo legado | Preservar somente como histórico; não converter diretamente em estado novo |
| `Descricao` | Texto derivado para seleção | Recalcular futuramente ou descartar após validação; componentes de origem já existem |

### 9.2 Premissas e fotografias parciais

| Campos | Classificação provisória | Tratamento proposto |
|---|---|---|
| `Volume`, `Material`, `Desag`, `Flutuante`, `Terrestre`, `Desnivel_Bombeamento`, `Medicao`, `Horario`, `Dias` | Premissas textuais e técnicas | Preservar; migrar somente com unidade, significado e mapeamento validados |
| `Draga`, `Vazao`, `Eficiencia`, `Concentracao` | Fotografia parcial de catálogo mais valores adotados | Preservar; separar futuramente referência sugerida de valor adotado |

### 9.3 Resultados calculados

| Campos | Classificação provisória | Tratamento proposto |
|---|---|---|
| `Producao_Hora`, `Horas_Dia`, `Dias_Mes`, `Horas_Mes`, `Producao_Mensal`, `Prazo_Meses` | Resultados derivados | Preservar para consulta e comparação; recalcular quando entradas e regra forem validadas |
| `Equipe_JSON` | Mistura de fotografia, entrada e resultados | Preservar integralmente; analisar e migrar seletivamente, sem tratá-lo como schema novo |

### 9.4 Custos e duplicidades

| Campos | Classificação provisória | Tratamento proposto |
|---|---|---|
| `Custo_Hora_Equipe`, `Leis_Sociais` | Resultados/parâmetros com significado observável | Preservar; recalcular futuramente quando composição e regra estiverem válidas |
| `custo_hora_equipe`, `leis_sociais` | Duplicatas de compatibilidade observadas | Preservar no histórico; descartar após validação de migração |
| `custo_mensal_equipe` | Nome semanticamente incompatível com o valor horário gravado | Preservar somente como evidência histórica; não migrar como custo mensal |

### 9.5 Dados ausentes do arquivo

Os resultados da Etapa 3 — insumos adotados, custo de insumos, custo total de equipe, total do barrilete, dias e horas — não estão persistidos no CSV auditado. Não existe dado a migrar dessas sessões encerradas, salvo outra fonte ainda não identificada.

## 10. Catálogos e fronteiras de dados

| Fonte | Decisão provisória | Condições |
|---|---|---|
| `data/materiais.csv` | Ampliar e reutilizar | Identidade, unidade, vigência, histórico e parser numérico corretos |
| `data/desaguamento.csv` | Ampliar e reutilizar | Identidade estável e separação entre tipo e parâmetros sugeridos |
| `data/horarios.csv` | Ampliar e reutilizar | Turnos completos, intervalos e travessia de dia |
| `data/dias.csv` | Ampliar e reutilizar | Preservar estado ativo e substituir dependência por textos exatos |
| `data/equipamentos.csv` | Ampliar e reutilizar | Classificação, identidade, unidade, vigência e fotografia por versão |
| `data/salarios.csv` | Ampliar e reutilizar | Data-base, vigência, encargos e fotografia por versão |
| `data/insumos.csv` | Substituir ou migrar seletivamente | Unidade, identidade, preço temporal e administração fora da composição |
| `data/clientes.csv` | Preservar como legado; relacionar seletivamente | Não fundir por nome com CRM |
| `data/crm/clientes.csv` | Candidato a referência mestre de cliente | Decisão própria sobre integração e permissões |
| `data/medicao.csv` e `data/medicoes/medicao.csv` | Consolidar após definir fonte canônica | Nenhum merge automático |
| `data/obras.csv` | Manter separado e relacionar | Obra operacional não é orçamento |
| `data/orcamentos.csv` | Preservar somente como histórico após substituição de acesso | Somente leitura; migração seletiva e rastreável |

Nenhum arquivo é alterado por esta decisão documental.

## 11. Fronteira com Obras

O uso de `data/orcamentos.csv` pela rota Obras é acoplamento legado e não requisito do novo sistema.

Decisão recomendada:

- a fonte operacional de Obras deve ser `data/obras.csv`;
- rascunho orçamentário não deve ser apresentado como obra operacional;
- orçamento aprovado e obra operacional devem permanecer entidades distintas, relacionáveis por identidade explícita;
- consulta de orçamento antigo deve pertencer ao histórico de Orçamentos;
- a correção da rota Obras deve ocorrer em Kid Step próprio, antes da aposentadoria física de `data/orcamentos.csv` ou das rotas antigas.

Esta sessão não altera a rota Obras.

## 12. Funcionalidades legadas candidatas à aposentadoria

| Item | Decisão provisória | Motivo e condição |
|---|---|---|
| Dashboard atual | Substituir | Lista e retomada dependem do agregado incompleto |
| Etapas 0 a 3 | Substituir | Não representam o método completo observado no Excel |
| Falsa finalização | Desativar com retirada do acesso antigo | Sucesso não corresponde a estado persistido |
| Edição global de insumos na Etapa 3 | Desativar | Mistura catálogo mestre e transação |
| Resultado da Etapa 3 somente em sessão | Remover futuramente | Não constitui histórico recuperável |
| Três salvamentos do agregado | Remover futuramente | Responsabilidade duplicada e persistência legada |
| Campos de compatibilidade | Preservar no histórico; não reproduzir | Duplicidade confirmada |
| `custo_mensal_equipe` | Não migrar semanticamente; preservar evidência | Contém custo horário |
| Retomada incompleta | Substituir | Etapa 3 não é persistida |
| Arquivos antigos não roteados | Remover futuramente | Após janela de reversão e confirmação de ausência de consumidores |
| Exposição de rascunhos como Obras | Substituir em Kid Step próprio | Acoplamento com rota externa |
| Rotas antigas | Manter tecnicamente por janela curta, depois remover | Reversão controlada e dependências devem ser verificadas |

Nenhuma remoção ocorre nesta sessão.

## 13. Registro obrigatório de quebra deliberada

Toda quebra futura deverá registrar:

| Campo | Conteúdo obrigatório |
|---|---|
| Funcionalidade | O comportamento que deixará de existir ou mudará |
| Superfície | Rotas, páginas, serviços, arquivos e menus afetados |
| Justificativa | Benefício esperado e problema removido |
| Dados | Dados lidos, gravados, preservados, migrados ou abandonados |
| Dependências | Consumidores internos e externos verificados |
| Preservação | Estratégia de histórico, migração ou fotografia |
| Usuário | Mudança visível e comunicação necessária |
| Reversão | Como restaurar o acesso ou comportamento durante a janela definida |
| Testes | Evidências automatizadas e manuais exigidas |
| Momento | Pré-condições e Kid Step autorizado |

Quebra não documentada ou não testada é defeito, não estratégia.

## 14. Primeiro Kid Step proposto

### Substituir a entrada principal de Orçamentos por uma fundação navegável do novo domínio

Escopo proposto:

1. criar um componente inicial do Novo Sistema de Orçamentos, sem formulário nem cálculo;
2. criar uma rota própria e explícita para esse componente;
3. fazer o cartão atual de Orçamentos abrir a nova rota;
4. retirar as rotas legadas do acesso principal, preservando temporariamente código, páginas e `data/orcamentos.csv`;
5. exibir no novo componente somente a identificação de que o novo sistema está em construção e uma entrada desabilitada ou informativa para `Histórico de Orçamentos Antigos`;
6. documentar as rotas antigas que ficam sem acesso principal;
7. adicionar testes do roteamento e da ausência de escrita em CSV.

### Fora do escopo

- criar orçamento;
- implementar fórmulas;
- criar CSVs;
- migrar registros;
- apagar ou alterar `data/orcamentos.csv`;
- criar a consulta funcional do histórico;
- alterar a rota Obras;
- remover fisicamente páginas ou rotas antigas.

### Quebra deliberada prevista

- **Funcionalidade:** criação, continuação e edição pelo dashboard antigo deixam de estar acessíveis pelo menu.
- **Dados:** nenhum dado é apagado ou modificado.
- **Reversão:** durante a janela inicial, reverter o destino do cartão restaura o acesso antigo.
- **Impacto:** usuários passam a encontrar a fundação do novo sistema; registros antigos permanecem preservados, ainda sem consulta nova.
- **Testes:** cartão direciona à rota nova; rota nova renderiza; nenhuma rota nova grava CSV; rotas legadas não são destino do menu; demais módulos continuam roteados.

Esse Kid Step produz a fronteira real do novo domínio e interrompe a expansão do modelo legado sem antecipar regras ainda não compreendidas.

## 15. Decisões pendentes

- identidade e estados finais de Orçamento e Versão;
- schemas físicos e estratégia de persistência;
- etapas estruturais e opcionais por família de obra;
- motor e representação das memórias de cálculo;
- fluxo de validação, emissão e aprovação;
- integração com cliente CRM;
- conversão de orçamento aprovado em obra operacional;
- política de permissões e exposição financeira;
- migração seletiva dos registros antigos;
- prazo da janela de reversão das rotas legadas;
- momento de implementar histórico e corrigir Obras;
- regras universais que somente o crosscheck horizontal poderá consolidar.

## 16. Critérios de homologação desta fundação

- AUDIT_052 formalmente homologada;
- princípio de preservação de dados e conhecimento registrado;
- legado não protegido por padrão;
- Opções A, B e C comparadas;
- Opção B recomendada com evolução para C;
- dados legados classificados sem descarte;
- modelo conceitual mantido provisório;
- aplicabilidade de etapas registrada;
- equivalência com Excel definida como alvo;
- quebras deliberadas possuem contrato documental;
- primeiro Kid Step delimitado e não implementado;
- nenhuma alteração funcional ou de CSV realizada.
