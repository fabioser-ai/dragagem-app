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
- A primeira prioridade funcional da Fase 2 foi definida: sistema orçamentário da FOS.
- A estratégia oficial está registrada em `docs/architecture/21_ESTRATEGIA_FASE_2_ORCAMENTOS.md`.
- A camada permanente de conhecimento operacional está registrada em `docs/knowledge/`.
- O workflow oficial do Curador da Base de Conhecimento está registrado em `docs/knowledge/KNOWLEDGE_CURATOR.md`.
- Toda sessão de curadoria documental deve iniciar pela leitura desse bootstrap e da documentação relacionada ao assunto.
- A engenharia reversa vertical do primeiro modelo, dragagem com desaguamento em bags, foi concluída e registrada em `docs/knowledge/orcamentos/001_DESAGUAMENTO_BAGS_SABESP.md`.
- A AUDIT_052 concluiu a descoberta documental do domínio legado de Orçamentos no snapshot `8d2f8463b07fd7a71b28833853522c548af74be2`.
- Foram inventariados o fluxo ativo, seis rotas, cinco páginas, estado de sessão, dez CSVs diretamente usados e três bases externas de fronteira.
- A auditoria confirmou catálogos compartilhados reutilizáveis, duplicidades reais de implementação e dados, falsos duplicados entre clientes e obras, e a ausência de vínculo entre orçamento, cliente CRM e obra operacional.
- Nenhum código funcional, CSV, comportamento ou migração foi alterado pela AUDIT_052.
- A AUDIT_052 foi homologada como base factual para a fundação arquitetural provisória do Novo Sistema de Orçamentos.
- A decisão de produto vigente é preservar dados e conhecimento úteis e preservar funcionalidades legadas somente quando houver benefício comprovado.
- A arquitetura provisória está registrada em `docs/architecture/22_NOVO_SISTEMA_ORCAMENTOS.md`.
- A estratégia recomendada é substituir imediatamente o acesso principal ao fluxo legado, preservar `data/orcamentos.csv` como histórico e evoluir de retirada de acesso para aposentadoria completa controlada.
- Quebras deliberadas de compatibilidade são permitidas quando documentadas, testadas, homologadas e acompanhadas da preservação ou migração dos dados relevantes.
- Nenhum código funcional ou CSV foi alterado pela criação da fundação arquitetural.

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

### Knowledge Curator

Responsável por:

- curadoria da base de conhecimento;
- auditoria documental;
- organização da arquitetura documental;
- revisão de consistência;
- classificação das evidências;
- preservação da rastreabilidade;
- consolidação do conhecimento somente após evidência suficiente.

O Curador não implementa software e não define arquitetura por opinião.

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
- validação do conhecimento operacional;
- intervenção de infraestrutura somente quando os ambientes não puderem prosseguir.

## Hierarquia documental

- `docs/PROJECT_STATE.md`: estado oficial e workflow do projeto.
- `docs/DEVELOPMENT_PHILOSOPHY.md`: princípios e regras permanentes.
- `docs/architecture/`: fonte consolidada da arquitetura atual por domínio.
- `docs/audit/`: histórico incremental e detalhado das auditorias técnicas e arquiteturais.
- `docs/knowledge/`: memória técnica e conhecimento operacional independente da implementação.
- `docs/knowledge/KNOWLEDGE_CURATOR.md`: bootstrap oficial de toda sessão de curadoria documental.
- `docs/ARCHITECTURE_CURRENT.md`: documento legado de transição; a documentação modular prevalece.

## Próximo passo

Homologar `docs/architecture/22_NOVO_SISTEMA_ORCAMENTOS.md` antes de qualquer implementação.

Após homologação, executar somente o primeiro Kid Step definido nessa fundação: criar a entrada navegável isolada do novo domínio e retirar o fluxo antigo do acesso principal, sem formulário, fórmula, CSV, migração, histórico funcional ou alteração da rota Obras.

Em paralelo documental, continuar a engenharia reversa vertical do sistema orçamentário.

Para cada novo modelo fornecido:

1. analisar o arquivo integralmente;
2. registrar abas, fórmulas, dependências, regras, exceções e inconsistências;
3. separar fatos observados, informações do especialista, interpretações e hipóteses;
4. criar documento próprio em `docs/knowledge/orcamentos/`;
5. não implementar.

Após quantidade suficiente de modelos completos:

1. executar crosscheck horizontal;
2. identificar núcleo comum, famílias de obra, componentes opcionais e exceções;
3. consolidar o Método de Orçamento FOS;
4. definir a arquitetura do sistema orçamentário;
5. decompor a implementação em Kid Steps;
6. validar equivalência com as planilhas originais antes de otimizar.

## Fases 4 e 5 — Orçamentos

### Fase 4 homologada

A modelagem conceitual oficial do domínio de Orçamentos está registrada em `docs/architecture/22_DOMINIO_ORCAMENTOS.md`.

A Fase 4 encerrou a descoberta inicial baseada nos 49 modelos e consolidou:

- fronteiras do domínio;
- fluxo conceitual;
- entidades e relacionamentos principais;
- versões, cenários, pacotes, composições e memórias de cálculo;
- regras universais e por família;
- desempenho, UX e rastreabilidade;
- proposta futura e decisões adiadas.

Nenhuma implementação foi realizada.

### Fase 5 homologada — modelo lógico

O modelo lógico oficial está registrado em `docs/architecture/23_MODELO_LOGICO_DADOS_ORCAMENTOS.md`.

Foram definidos, de forma tecnológica-neutra:

- identidades lógicas;
- propriedade das informações;
- cardinalidades e relacionamentos;
- ciclos de vida e imutabilidade;
- distinção entre cadastro mestre e fotografia da versão;
- estados semânticos dos valores;
- fórmulas, dependências, memórias e resultados;
- validações, decisões, aprovações e histórico;
- vínculos futuros com proposta e obra;
- estruturas que permitem carregamento e recálculo seletivos.

Nenhum código funcional, tela, CSV, formato físico de dados ou tecnologia de persistência foi criado ou alterado.

### Fase 6 homologada — motor lógico de cálculo e dependências

O motor lógico oficial está registrado em `docs/architecture/24_MOTOR_CALCULO_ORCAMENTOS.md`.

Foram definidos, sem implementação:

- contrato lógico de fórmulas identificadas e versionadas;
- grafo conceitual de dependências por cenário;
- invalidação seletiva e recálculo incremental em ordem topológica;
- compatibilidade de unidades e bases físicas/econômicas;
- separação entre valores brutos, arredondados, custeados e comerciais;
- comportamento dos estados semânticos;
- conversão de erros de planilha em validações compreensíveis;
- memória de cálculo reproduzível e controle de overrides;
- contratos provisórios dos submodelos;
- protocolo de equivalência com os Excel, iniciado obrigatoriamente pela SABESP.

Nenhum código funcional, tela, CSV, formato físico de dados, biblioteca de cálculo ou tecnologia de persistência foi criado ou alterado.

### Fase 7 homologada — fluxo oficial do usuário

O fluxo e a experiência oficiais estão registrados em `docs/architecture/25_FLUXO_USUARIO_ORCAMENTOS.md`.

Foram definidos, sem implementação:

- perfis conceituais, jornada e navegação com continuidade;
- painel resumido e carregamento sob demanda;
- aplicabilidade, valores sugeridos/adotados e cenários;
- pacotes, composições e feedback de cálculo;
- salvamento conceitual, conflitos e desempenho funcional;
- validações, revisão, aprovação, resumos e histórico;
- wireframes e matrizes conceituais;
- MVP inicial capaz de reproduzir integralmente a SABESP.

Nenhum código funcional, tela real, CSV, componente de interface ou tecnologia de persistência foi criado ou alterado.

### Fase 8 — arquitetura física mínima e plano de Kid Steps

A arquitetura física selecionada está registrada em `docs/architecture/26_ARQUITETURA_FISICA_ORCAMENTOS.md`.

Decisões principais:

- módulo isolado e dividido em apresentação, aplicação, domínio, cálculo, persistência, catálogos e validações;
- persistência híbrida com índice resumido em CSV e documento JSON por versão;
- catálogos separados e fotografias dentro da versão;
- carregamento sob demanda e cálculo sem chamada remota;
- escrita composta e conflito por snapshot/SHA, sem last-write-wins;
- legado preservado até equivalência SABESP e transição reversível;
- rota Obras mantida sem alteração enquanto depender de `data/orcamentos.csv`.

O plano oficial está em `docs/architecture/27_PLANO_KID_STEPS_ORCAMENTOS.md` e contém 15 Kid Steps até a homologação integral da SABESP.

Nenhum código funcional, tela, CSV, rota, migração ou desativação do legado foi realizado.

## Novo Sistema de Orçamentos — Kid Step 001

O Kid Step 001 criou a fronteira física e navegável do Novo Sistema de Orçamentos:

- pacote isolado em `modulos/orcamentos/`;
- entrada inequívoca no menu, protegida pela permissão atual de Orçamentos;
- rota própria e página inicial informativa;
- retorno seguro ao menu com um único rerun intencional;
- zero leitura remota de dados de Orçamentos na página;
- legado, rota Obras e `data/orcamentos.csv` preservados.

Nenhum orçamento, versão, cenário, pacote de domínio, fórmula, cálculo, persistência, CSV, JSON, catálogo ou integração foi criado.

### Próximo passo recomendado

Após homologação do Merlin sobre o Kid Step 001, executar somente o Kid Step 002 — núcleo do domínio em memória.
