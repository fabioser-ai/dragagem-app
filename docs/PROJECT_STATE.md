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
- O contrato define estados explícitos de leitura, bloqueio de escrita após falha, preservação do SHA observado e migração gradual dos chamadores.
- A infraestrutura inicial foi implementada em `services/github.py` com `StatusLeitura`, `ResultadoLeituraCSV` e `ler_csv_github()`.
- `carregar_github()` e os demais chamadores permanecem legados; nenhum fluxo funcional foi migrado.
- Foi criada a suíte `tests/test_github_leitura.py` com testes unitários focados no contrato explícito.
- Foi criado `.github/workflows/tests.yml` para executar a suíte com `unittest` em Python 3.11.
- A suíte `tests/test_github_leitura.py` foi executada localmente com as dependências de `requirements.txt` no commit `14dd73d23b12f15607c4ebaffa15a3e18b1b8101`: 10 testes passaram.
- Nenhuma execução de CI foi confirmada pelas ferramentas disponíveis nesta sessão; a validação confirmada é local e reproduz o comando do workflow.
- Permanecem lacunas secundárias de menu, bootstrap, fallback e reconciliação final do documento legado.

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
- `docs/ARCHITECTURE_CURRENT.md`: documento legado de transição; não remover conteúdo até a migração correspondente ser confirmada.

## Próximo passo

Definir se a escrita estruturada com SHA esperado é indispensável ao piloto de Administração:

1. se indispensável, implementá-la em Kid Step isolado, sem migrar chamadores;
2. migrar somente Administração em alteração isolada após a escrita segura estar disponível;
3. não combinar essa migração com mudanças de schema, permissões ou regras de negócio.
