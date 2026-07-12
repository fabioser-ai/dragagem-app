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
- Foram criadas as suítes `tests/test_github_leitura.py`, `tests/test_github_escrita.py` e `tests/test_log.py`.
- A suíte completa mais recente foi executada localmente com as dependências do projeto: 25 testes passaram, sem falhas ou erros.
- Administração foi migrada como primeiro consumidor do contrato explícito.
- `pages/administracao.py` bloqueia inclusão, desativação e exclusão quando a leitura não autoriza sobrescrita.
- As gravações administrativas usam o SHA obtido na leitura confirmada.
- A migração de Administração foi validada por testes, compilação sintática e inspeção estática.
- Logs foram migrados como segundo consumidor do contrato explícito.
- `services/log.py` atualiza o arquivo com o SHA da leitura, cria explicitamente após 404 e bloqueia escrita após falha de leitura.
- A migração de logs preservou schema, autenticação e comportamento dos chamadores e foi validada por testes, compilação sintática e inspeção estática.
- Nenhum schema ou regra de permissão foi alterado nessas migrações.
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

Preparar a migração isolada do módulo Dados para o contrato explícito de leitura e escrita:

1. auditar novamente todos os caminhos de escrita de `pages/dados.py` e serviços relacionados;
2. separar cadastros simples, locais de trabalho e o conjunto atestados/serviços;
3. definir como bloquear regravações quando a leitura dos CSVs envolvidos não for confirmada;
4. preservar schemas e comportamento funcional atual;
5. não corrigir a conversão numérica identificada na AUDIT_043 no mesmo Kid Step;
6. implementar e validar uma etapa por vez antes de avançar para Férias.