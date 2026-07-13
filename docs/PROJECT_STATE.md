# PROJECT_STATE

## Objetivo

Centralizar o estado oficial do desenvolvimento do APP FOS.

## Filosofia

A filosofia oficial de desenvolvimento está registrada em `docs/DEVELOPMENT_PHILOSOPHY.md`.

Princípios centrais:

- Baby steps.
- Uma alteração por vez.
- Arquitetura antes de implementação.
- Auditoria antes de implementação.
- Código observado acima de hipóteses.
- Documentação oficial acima da memória.
- Não refatorar por preferência pessoal.
- Confirmar toda escrita por leitura posterior.
- O conhecimento oficial do projeto pertence ao repositório.

## Estado atual

- Arquitetura auditada no ciclo priorizado e documentado.
- Fluxo legado de lançamento identificado e documentado.
- Dependências básicas declaradas em `requirements.txt`.
- Auditorias incrementais preservadas em `docs/audit/`.
- Estrutura modular oficial criada em `docs/architecture/`.
- Auditoria de Orçamentos concluída em `docs/audit/AUDIT_034_ORCAMENTOS.md` e consolidada em `docs/architecture/08_ORCAMENTOS.md`.
- Auditoria de Prestação de Contas concluída em `docs/audit/AUDIT_035_PRESTACAO_CONTAS.md` e consolidada em `docs/architecture/09_PRESTACAO_CONTAS.md`.
- Auditoria do CRM concluída em `docs/audit/AUDIT_036_CRM.md` e consolidada em `docs/architecture/10_CRM.md`.
- Auditoria de Administração concluída em `docs/audit/AUDIT_037_ADMINISTRACAO.md` e consolidada em `docs/architecture/11_ADMINISTRACAO.md`.
- Auditoria de Serviços Compartilhados concluída em `docs/audit/AUDIT_038_SERVICOS_COMPARTILHADOS.md` e consolidada em `docs/architecture/12_SERVICOS_COMPARTILHADOS.md`.
- `docs/ARCHITECTURE_CURRENT.md` permanece como documento legado durante a migração gradual.
- A filosofia de desenvolvimento foi formalizada em `docs/DEVELOPMENT_PHILOSOPHY.md`.
- AUDIT_039 — Auditoria Transversal de Consistência concluída em `docs/audit/AUDIT_039_AUDITORIA_TRANSVERSAL.md` e consolidada em `docs/architecture/13_AUDITORIA_TRANSVERSAL.md`.
- AUDIT_040 — Auditoria do Conhecimento Registrado concluída em `docs/audit/AUDIT_040_CONHECIMENTO_REGISTRADO.md` e consolidada em `docs/architecture/14_CONHECIMENTO_REGISTRADO.md`.
- AUDIT_041 — Migração documental de Medições concluída em `docs/audit/AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md` e consolidada em `docs/architecture/01_MEDICOES_FUNDACAO.md` a `04_MEDICOES_GESTAO.md`.
- O conhecimento específico de Medições possui agora fontes modulares; `docs/ARCHITECTURE_CURRENT.md` permanece legado até reconciliação completa.
- AUDIT_042 — Matriz de Cobertura Documental concluída em `docs/audit/AUDIT_042_MATRIZ_COBERTURA_DOCUMENTAL.md` e consolidada em `docs/architecture/15_MATRIZ_COBERTURA_DOCUMENTAL.md`.
- A matriz demonstra cobertura forte para Medições, Orçamentos, Prestação de Contas, CRM, Administração e Serviços Compartilhados.
- AUDIT_043 — Auditoria do módulo Dados concluída em `docs/audit/AUDIT_043_DADOS.md` e consolidada em `docs/architecture/16_DADOS.md`.
- AUDIT_044 — Auditoria do módulo Férias concluída em `docs/audit/AUDIT_044_FERIAS.md` e consolidada em `docs/architecture/17_FERIAS.md`.
- AUDIT_045 — Auditoria da rota Obras concluída em `docs/audit/AUDIT_045_OBRAS.md` e consolidada em `docs/architecture/18_OBRAS.md`.
- A cobertura modular dos domínios funcionais explicitamente roteados no ciclo auditado está concluída.
- AUDIT_046 — Contrato Explícito de Resultado de Leitura concluída em `docs/audit/AUDIT_046_CONTRATO_LEITURA.md` e consolidada em `docs/architecture/19_CONTRATO_LEITURA.md`.
- O contrato explícito de leitura foi implementado em `services/github.py` com `StatusLeitura`, `ResultadoLeituraCSV` e `ler_csv_github()`.
- O contrato explícito de escrita foi implementado em `services/github.py` com `StatusEscrita`, `ResultadoEscritaCSV` e `salvar_csv_github()`.
- `carregar_github()` e `salvar_github()` permanecem como adaptadores legados para consumidores ainda não migrados.
- Administração foi migrada como primeiro consumidor do contrato explícito.
- Logs foram migrados como segundo consumidor do contrato explícito.
- O CRUD dos seis cadastros simples de Dados foi migrado para `services/dados_persistencia.py`.
- A administração de Locais de Trabalho foi migrada para persistência segura; o consumidor interno de Medições permanece em camada legada separada.
- AUDIT_047 — Locais de Trabalho concluída em `docs/audit/AUDIT_047_LOCAIS_TRABALHO.md` e consolidada em `docs/architecture/16_DADOS.md`.
- AUDIT_048 — Atestados e Serviços Vinculados concluída em `docs/audit/AUDIT_048_ATESTADOS_SERVICOS.md` e consolidada em `docs/architecture/16_DADOS.md`.
- Atestados e serviços formam agregado lógico em dois CSVs.
- As operações de Atestados que alteram um único arquivo foram migradas para persistência segura nos commits `06c210207988d1e66d196e7a5e7dd96ea2ef47a2`, `acba093eeb0f095875bbe31ccc62fbb68f0ea7ea` e `297425a178dcde8d003f5aff1851ee6794faab0c`.
- Criação e edição de atestado usam leitura estruturada e escrita segura de `data/atestados.csv`; criação e exclusão de serviço usam o mesmo contrato em `data/atestados_servicos.csv`.
- A cobertura específica das operações de arquivo único de Atestados possui 8 testes; a suíte completa dessa etapa foi homologada com 60 testes, 0 falhas e 0 erros.
- AUDIT_049 — Consistência da Exclusão Composta de Atestados concluída em `docs/audit/AUDIT_049_CONSISTENCIA_EXCLUSAO_ATESTADOS.md` e consolidada em `docs/architecture/16_DADOS.md`.
- A decisão arquitetural preserva a exclusão física e exige um único commit Git contendo os dois CSVs, condicionado a um snapshot comum da branch.
- A fundação de persistência multi-arquivo foi implementada em `services/persistencia_multi_arquivo.py` no commit `3dbed44` e coberta em `tests/test_persistencia_multi_arquivo.py` no commit `571f692`.
- O workflow `.github/workflows/testes.yml` foi criado no commit `1ad6d1e` para homologação automática em Ubuntu com Python 3.12.
- O workflow do commit `571f692` concluiu com sucesso em 31 segundos; a fundação multi-arquivo foi homologada antes da migração do consumidor.
- A exclusão composta de atestado e serviços foi migrada para persistência atômica no commit `b41d0207192cf91cd03fa7486e4a39a72c95d357` e coberta no commit `07ea0dce151545d026fc74b87810103f29491719`.
- A exclusão exige confirmação explícita, leituras autorizadas e snapshot comum; os dois CSVs são publicados em um único commit, sem falso sucesso em conflito ou falha.
- O GitHub Actions do commit `07ea0dce151545d026fc74b87810103f29491719` concluiu com sucesso em 27 segundos em Ubuntu com Python 3.12.
- A exclusão composta deixou de usar duas gravações legadas independentes; criação, edição e exclusão individual permanecem nos contratos já definidos para cada arquivo.
- AUDIT_050 — Encerramento da Fase 1 concluída em `docs/audit/AUDIT_050_ENCERRAMENTO_FASE_1.md` e consolidada em `docs/architecture/20_ENCERRAMENTO_FASE_1.md`.
- A auditoria confirmou que a plataforma está tecnicamente madura, mas identificou um único bloqueador crítico conhecido: o cadastro de interação do CRM ainda grava `interacoes.csv` e `clientes.csv` em operações independentes.
- Prestação de Contas mantém risco de comprovante órfão, mas esse caso combina binário e CSV e foi classificado como risco funcional prioritário, não como bloqueador da fundação multi-CSV.
- `docs/ARCHITECTURE_CURRENT.md` permanece como legado de transição e contém descrições anteriores aos contratos atuais; a documentação modular prevalece e sua reconciliação não bloqueia a Fase 2.
- O aviso de depreciação do runtime Node.js usado por `actions/checkout@v4` e `actions/setup-python@v5` permanece no parking lot de manutenção do CI; não afetou as homologações.
- Permanecem lacunas secundárias de menu, bootstrap, fallback, seletores, permissões granulares e normalização de dados históricos.

## Workflow oficial de auditoria

1. Ler `docs/PROJECT_STATE.md`, `docs/DEVELOPMENT_PHILOSOPHY.md` e a documentação aplicável de `docs/architecture/`.
2. Auditar um subsistema por vez ou um recorte transversal explicitamente definido.
3. Registrar a auditoria concluída em `docs/audit/AUDIT_XXX_<SUBSISTEMA>.md`.
4. Consolidar os fatos observados no arquivo correspondente em `docs/architecture/`.
5. Registrar apenas fatos observados; hipóteses, lacunas e limites devem ser explicitamente marcados.
6. Confirmar toda escrita por leitura posterior do trecho alterado.
7. Atualizar este `PROJECT_STATE.md`.
8. Somente depois considerar a auditoria encerrada e avançar para o próximo subsistema.

## Hierarquia documental

- `docs/PROJECT_STATE.md`: estado oficial e workflow do projeto.
- `docs/DEVELOPMENT_PHILOSOPHY.md`: princípios e regras permanentes de desenvolvimento e auditoria.
- `docs/architecture/`: fonte modular e consolidada da arquitetura atual por domínio.
- `docs/audit/`: histórico incremental e detalhado das auditorias realizadas.
- `docs/ARCHITECTURE_CURRENT.md`: documento legado de transição; a documentação modular prevalece.

## Próximo passo

Executar o último Kid Step bloqueador da Fase 1:

1. migrar somente o cadastro de interação do CRM e a atualização correspondente do cliente para persistência multi-arquivo atômica;
2. preservar schemas, campos, seletores, datas, permissões e demais comportamentos do CRM;
3. preparar `data/crm/interacoes.csv` e `data/crm/clientes.csv` em memória;
4. publicar ambos em um único commit Git condicionado a snapshot comum;
5. bloquear falso sucesso e nova tentativa automática em conflito ou falha;
6. criar cobertura específica do consumidor;
7. homologar a suíte completa no GitHub Actions;
8. após sucesso, registrar oficialmente o encerramento da Fase 1 e iniciar a priorização da primeira entrega da Fase 2 — Expansão Funcional.
