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

## Fase atual

**Fase 2 — Expansão Funcional.**

A Fase 1 — Consolidação da Plataforma foi oficialmente encerrada em 2026-07-13 após a homologação da operação composta do CRM.

## Estado atual

- Arquitetura auditada no ciclo priorizado e documentado.
- Auditorias incrementais preservadas em `docs/audit/`.
- Estrutura modular oficial consolidada em `docs/architecture/`.
- A filosofia de desenvolvimento foi formalizada em `docs/DEVELOPMENT_PHILOSOPHY.md`.
- A cobertura modular dos domínios funcionais explicitamente roteados no ciclo auditado está concluída.
- O contrato explícito de leitura foi implementado em `services/github.py` com `StatusLeitura`, `ResultadoLeituraCSV` e `ler_csv_github()`.
- O contrato explícito de escrita foi implementado em `services/github.py` com `StatusEscrita`, `ResultadoEscritaCSV` e `salvar_csv_github()`.
- `carregar_github()` e `salvar_github()` permanecem como adaptadores legados para consumidores ainda não migrados.
- Administração, Logs, o CRUD dos seis cadastros simples de Dados e Locais de Trabalho foram migrados para persistência segura.
- As operações de Atestados que alteram um único arquivo foram migradas nos commits `06c210207988d1e66d196e7a5e7dd96ea2ef47a2`, `acba093eeb0f095875bbe31ccc62fbb68f0ea7ea` e `297425a178dcde8d003f5aff1851ee6794faab0c`.
- A fundação multi-arquivo foi implementada em `services/persistencia_multi_arquivo.py` no commit `3dbed44` e coberta no commit `571f692`.
- A exclusão composta de Atestados foi migrada no commit `b41d0207192cf91cd03fa7486e4a39a72c95d357` e coberta no commit `07ea0dce151545d026fc74b87810103f29491719`.
- O cadastro de interação do CRM e a atualização correspondente do cliente foram migrados no commit `4abddf3b2d267e073132815c8af76807aca89310` e cobertos no commit `836187cbed0c9e9eab0d70bcb44e79fade09402f`.
- O workflow `.github/workflows/testes.yml` realiza homologação automática em Ubuntu com Python 3.12.
- O GitHub Actions do commit `836187cbed0c9e9eab0d70bcb44e79fade09402f` concluiu com `Success` em 26 segundos.
- AUDIT_050 definiu os critérios de encerramento da plataforma.
- AUDIT_051 confirmou o atendimento dos critérios e encerrou oficialmente a Fase 1.
- `docs/ARCHITECTURE_CURRENT.md` permanece como legado de transição; a documentação modular prevalece.

## Fundação homologada

A plataforma dispõe de:

- leitura com resultado explícito;
- escrita por arquivo com resultado explícito e controle de concorrência;
- publicação atômica de múltiplos CSVs em um único commit Git;
- cobertura automatizada;
- homologação reproduzível em Linux;
- documentação modular;
- workflow oficial entre Merlin, Work e Fabio;
- processo de contingência por `git bundle` quando a publicação direta não está disponível.

A fundação não deve ser reaberta por preferência. Nova infraestrutura somente deve ser criada quando uma entrega funcional demonstrar necessidade concreta.

## Riscos e parking lot não bloqueadores

- comprovante binário órfão em Prestação de Contas;
- aviso de runtime Node.js das GitHub Actions;
- lacunas de menu, bootstrap e fallback de rota;
- seletores ambíguos e homônimos;
- permissões internas granulares;
- normalização de datas e dados históricos;
- reconciliação gradual do documento legado;
- política de validade dos tokens;
- limpeza de artefatos locais não rastreados.

Esses itens permanecem registrados para priorização própria e não bloqueiam a Fase 2.

## Workflow oficial

### Merlin

Responsável por:

- arquitetura;
- auditorias;
- definição dos Kid Steps;
- revisão técnica e arquitetural;
- homologação;
- documentação oficial.

### Work

Responsável por:

- implementação;
- testes;
- validação;
- commits locais;
- publicação quando possível;
- diagnóstico operacional.

### Fabio

Responsável por:

- decisões de produto e prioridade;
- aprovação estratégica;
- intervenção de infraestrutura somente quando os ambientes não puderem prosseguir.

## Hierarquia documental

- `docs/PROJECT_STATE.md`: estado oficial e workflow do projeto.
- `docs/DEVELOPMENT_PHILOSOPHY.md`: princípios e regras permanentes.
- `docs/architecture/`: fonte consolidada da arquitetura atual por domínio.
- `docs/audit/`: histórico incremental e detalhado das auditorias.
- `docs/ARCHITECTURE_CURRENT.md`: documento legado de transição; a documentação modular prevalece.

## Próximo passo

Priorizar a primeira entrega da Fase 2 — Expansão Funcional.

A escolha deve comparar candidatos por:

1. valor operacional e financeiro;
2. frequência do uso ou da dor;
3. número de usuários beneficiados;
4. redução de trabalho manual ou risco;
5. prontidão arquitetural e dependências;
6. tamanho apropriado para entrega incremental.

Após a escolha:

1. auditar somente o fluxo diretamente afetado;
2. definir o primeiro Kid Step funcional;
3. implementar e testar em commits separados;
4. homologar pelo GitHub Actions;
5. medir o valor entregue antes de expandir o escopo.