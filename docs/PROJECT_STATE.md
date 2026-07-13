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
- Atestados e serviços formam agregado lógico em dois CSVs; operações simples alteram um arquivo e a exclusão de atestado altera dois arquivos sequencialmente sem transação.
- As operações de Atestados que alteram um único arquivo foram migradas para persistência segura nos commits `06c210207988d1e66d196e7a5e7dd96ea2ef47a2`, `acba093eeb0f095875bbe31ccc62fbb68f0ea7ea` e `297425a178dcde8d003f5aff1851ee6794faab0c`.
- Criação e edição de atestado usam leitura estruturada e escrita segura de `data/atestados.csv`; criação e exclusão de serviço usam o mesmo contrato em `data/atestados_servicos.csv`.
- A cobertura específica de Atestados possui 8 testes; a suíte completa foi homologada com 60 testes, 0 falhas e 0 erros.
- Persistência segura por arquivo não fornece atomicidade multi-arquivo; a exclusão composta permanece deliberadamente no fluxo legado.
- AUDIT_049 — Consistência da Exclusão Composta de Atestados concluída em `docs/audit/AUDIT_049_CONSISTENCIA_EXCLUSAO_ATESTADOS.md` e consolidada em `docs/architecture/16_DADOS.md`.
- A decisão arquitetural preserva a exclusão física e exige um único commit Git contendo os dois CSVs, condicionado a um snapshot comum da branch; duas escritas independentes, compensação e desativação lógica não foram adotadas como garantia transacional.
- A fundação de persistência multi-arquivo foi implementada em `services/persistencia_multi_arquivo.py` no commit `3dbed44` e coberta em `tests/test_persistencia_multi_arquivo.py` no commit `571f692`.
- O workflow `.github/workflows/testes.yml` foi criado no commit `1ad6d1e` para homologação automática em Ubuntu com Python 3.12.
- O workflow do commit `571f692` concluiu com sucesso em 31 segundos; a fundação multi-arquivo está homologada e ainda não está conectada à interface.
- O aviso de depreciação do runtime Node.js usado por `actions/checkout@v4` e `actions/setup-python@v5` permanece no parking lot de manutenção do CI; não afetou a homologação.
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

Migrar somente o consumidor da exclusão composta em `pages/dados.py` para a fundação multi-arquivo já homologada:

1. preservar a exclusão física e os schemas atuais;
2. exigir leitura confirmada dos dois arquivos antes de habilitar a ação;
3. preparar as duas versões em memória sem alterar dados históricos além do agregado selecionado;
4. publicar os dois CSVs por um único commit Git usando o snapshot comum;
5. apresentar sucesso e executar `st.rerun()` somente após confirmação da atualização da branch;
6. em conflito ou falha, manter a interface sem falso sucesso e exigir nova leitura antes de nova confirmação;
7. adicionar confirmação explícita da operação destrutiva sem alterar outras regras da tela;
8. criar cobertura específica e executar a suíte completa pelo GitHub Actions;
9. não incluir desativação lógica, restauração, permissões granulares, mudanças de datas, rótulos ou normalização de dados no mesmo Kid Step.