# Arquitetura Atual — Encerramento da Fase 1

Última atualização: 2026-07-13

Fonte de auditoria:

- `docs/audit/AUDIT_050_ENCERRAMENTO_FASE_1.md`.

## Objetivo

Consolidar os critérios objetivos para encerrar a Fase 1 — Consolidação da Plataforma e separar bloqueadores críticos de manutenção secundária e decisões funcionais futuras.

## Fundação consolidada

A plataforma possui:

- contrato explícito de leitura;
- contrato explícito de escrita por arquivo;
- persistência multi-arquivo atômica baseada em commit Git único;
- consumidores de Dados migrados para os contratos aplicáveis;
- exclusão composta de Atestados migrada e homologada;
- suíte completa automatizada em Ubuntu com Python 3.12;
- documentação modular, filosofia e workflow oficiais.

## Critério de bloqueio

Uma lacuna bloqueia o encerramento da Fase 1 quando um fluxo funcional crítico executa duas ou mais gravações independentes que representam uma única operação lógica e pode expor estado divergente após falha parcial.

## Último bloqueador crítico conhecido

O cadastro de interação do CRM:

1. grava `data/crm/interacoes.csv`;
2. atualiza `data/crm/clientes.csv`.

As gravações são independentes. Falha parcial pode deixar a interação registrada sem a atualização correspondente do cliente.

Essa operação deve reutilizar a fundação multi-arquivo homologada e publicar os dois CSVs no mesmo commit, condicionado a snapshot comum.

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

Esses itens permanecem registrados, mas não bloqueiam a Fase 2 após a correção do CRM.

## Documento legado

`docs/ARCHITECTURE_CURRENT.md` permanece como fonte de transição. Ele contém descrições anteriores aos contratos explícitos e não representa integralmente o estado atual da persistência.

A documentação modular prevalece. O legado não será removido nem reescrito em massa para encerrar a Fase 1.

## Critérios finais de encerramento

A Fase 1 será considerada encerrada quando:

1. a operação composta do CRM usar persistência multi-arquivo atômica;
2. houver cobertura específica do consumidor;
3. a suíte completa concluir com sucesso no GitHub Actions;
4. o resultado for registrado em `PROJECT_STATE.md`;
5. as lacunas restantes estiverem classificadas como manutenção ou backlog funcional.

## Próximo passo

Migrar exclusivamente o cadastro de interação do CRM e a atualização do cliente para um único commit Git, sem alterar outros comportamentos do módulo.
