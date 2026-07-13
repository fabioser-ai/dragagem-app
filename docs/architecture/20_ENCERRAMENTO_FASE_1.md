# Arquitetura Atual — Encerramento da Fase 1

Última atualização: 2026-07-13

Fontes de auditoria:

- `docs/audit/AUDIT_050_ENCERRAMENTO_FASE_1.md`;
- `docs/audit/AUDIT_051_HOMOLOGACAO_ENCERRAMENTO_FASE_1.md`.

## Objetivo

Consolidar os critérios objetivos e o resultado final da Fase 1 — Consolidação da Plataforma, separando a fundação homologada de manutenção secundária e decisões funcionais futuras.

## Fundação consolidada

A plataforma possui:

- contrato explícito de leitura;
- contrato explícito de escrita por arquivo;
- persistência multi-arquivo atômica baseada em commit Git único;
- consumidores de Dados migrados para os contratos aplicáveis;
- exclusão composta de Atestados migrada e homologada;
- cadastro de interação do CRM e atualização do cliente migrados para publicação atômica;
- suíte completa automatizada em Ubuntu com Python 3.12;
- documentação modular, filosofia e workflow oficiais.

## Critério de bloqueio

Uma lacuna bloqueava o encerramento quando um fluxo funcional crítico executava duas ou mais gravações independentes que representavam uma única operação lógica e podia expor estado divergente após falha parcial.

Os dois consumidores críticos conhecidos dessa classe foram tratados:

1. exclusão composta de Atestados;
2. cadastro de interação do CRM com atualização correspondente do cliente.

## Homologação final do CRM

A operação composta do CRM foi implementada no commit `4abddf3b2d267e073132815c8af76807aca89310` e coberta no commit `836187cbed0c9e9eab0d70bcb44e79fade09402f`.

O fluxo agora:

- exige leituras autorizadas de `data/crm/clientes.csv` e `data/crm/interacoes.csv`;
- resolve snapshot comum da branch;
- prepara os dois DataFrames em memória;
- publica ambos no mesmo commit Git;
- bloqueia cliente ausente no snapshot;
- apresenta sucesso e executa `st.rerun()` somente após confirmação;
- não produz falso sucesso em conflito ou falha.

O GitHub Actions concluiu com `Success` em Ubuntu com Python 3.12, com duração total de 26 segundos.

## Riscos relevantes não bloqueadores

### Prestação de Contas

O comprovante binário pode permanecer órfão se a gravação da despesa falhar. O tratamento exige política própria para binário e CSV, recuperação ou reconciliação e não deve ser improvisado como compensação invisível.

### Manutenção e parking lot

- atualização das versões das GitHub Actions por aviso de runtime Node.js;
- lacunas de menu, bootstrap e fallback;
- seletores ambíguos;
- permissões granulares;
- normalização de datas e dados históricos;
- política de tokens;
- reconciliação final do documento legado.

Esses itens permanecem registrados, mas não bloqueiam a Fase 2.

## Documento legado

`docs/ARCHITECTURE_CURRENT.md` permanece como fonte de transição. Ele contém descrições anteriores aos contratos explícitos e não representa integralmente o estado atual da persistência.

A documentação modular prevalece. O legado não será removido nem reescrito em massa como condição para evolução funcional.

## Verificação dos critérios finais

Os critérios definidos pela AUDIT_050 foram atendidos:

1. a operação composta do CRM usa persistência multi-arquivo atômica;
2. existe cobertura específica do consumidor;
3. a suíte completa concluiu com sucesso no GitHub Actions;
4. o resultado foi registrado na documentação oficial;
5. as lacunas restantes estão classificadas como manutenção ou backlog funcional.

## Estado oficial

A Fase 1 — Consolidação da Plataforma está oficialmente encerrada.

## Próximo passo

Iniciar a Fase 2 — Expansão Funcional pela priorização da primeira entrega, considerando:

1. valor operacional para a FOS;
2. frequência e impacto do problema;
3. risco técnico e de dados;
4. dependências já disponíveis;
5. tamanho adequado para Kid Steps verificáveis.

Nenhuma nova infraestrutura deve ser criada por antecipação sem necessidade concreta da entrega funcional escolhida.