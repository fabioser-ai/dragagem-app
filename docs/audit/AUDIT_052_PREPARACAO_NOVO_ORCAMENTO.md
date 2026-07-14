# AUDIT_052 — Preparação do Novo Sistema de Orçamento

## Missão

Auditar o módulo atual de Orçamentos e os catálogos compartilhados antes da criação do novo sistema orçamentário da FOS.

Esta auditoria não implementa funcionalidades e não altera o comportamento do módulo existente.

## Contexto oficial

A Fase 2 prioriza o sistema orçamentário. O objetivo inicial do novo ciclo é reproduzir funcionalmente um orçamento real da FOS dentro do APP, preservando o módulo atual como legado e estruturando os dados de modo que os resultados futuros possam apoiar decisões.

O primeiro modelo de referência é `D_004_2026 - SABESP.xlsx`, documentado em `docs/knowledge/orcamentos/001_DESAGUAMENTO_BAGS_SABESP.md`.

## Escopo da auditoria

1. Mapear integralmente o roteamento e os arquivos do módulo atual de Orçamentos.
2. Confirmar os arquivos CSV lidos e gravados por cada etapa.
3. Inventariar os catálogos compartilhados potencialmente reutilizáveis pelo novo sistema.
4. Classificar cada CSV como:
   - reutilizar;
   - ampliar;
   - relacionar;
   - consolidar;
   - manter separado;
   - legado.
5. Identificar duplicidades reais de conceito, schema ou responsabilidade.
6. Distinguir catálogo mestre, registro transacional, fotografia histórica e resultado calculado.
7. Definir a fronteira mínima entre `Orçamento — Legado` e `Novo Sistema de Orçamento`.
8. Propor o primeiro Kid Step de implementação sem alterar o legado.

## Arquivos mínimos a ler

- `docs/PROJECT_STATE.md`
- `docs/DEVELOPMENT_PHILOSOPHY.md`
- `docs/architecture/README.md`
- `docs/architecture/08_ORCAMENTOS.md`
- `docs/architecture/16_DADOS.md`
- `docs/architecture/21_ESTRATEGIA_FASE_2_ORCAMENTOS.md`
- `docs/knowledge/orcamentos/001_DESAGUAMENTO_BAGS_SABESP.md`
- `app.py`
- `pages/menu.py`
- `pages/orcamento/dashboard.py`
- `pages/orcamento/etapa0.py`
- `pages/orcamento/etapa1.py`
- `pages/orcamento/etapa2.py`
- `pages/orcamento/etapa3.py`
- serviços diretamente chamados pelo módulo
- todos os CSVs consumidos ou alterados pelas etapas de orçamento

## Restrições

- Não alterar código funcional.
- Não renomear, mover, apagar ou migrar o módulo atual.
- Não criar CSV novo durante a auditoria.
- Não consolidar arquivos apenas por semelhança de nome.
- Não registrar hipótese como fato.
- Não definir fórmula nova sem evidência em Excel ou validação do especialista.

## Critérios para análise dos CSVs

Para cada arquivo, registrar:

- caminho;
- finalidade observada;
- colunas reais;
- identidade do registro;
- leitores;
- escritores;
- granularidade;
- se é catálogo, transação, histórico ou agregado;
- riscos de alteração;
- potencial de reutilização pelo novo orçamento;
- classificação recomendada;
- justificativa.

## Resultado esperado

A auditoria deverá concluir com:

1. inventário completo dos arquivos e dependências do orçamento legado;
2. matriz de sobreposição dos CSVs;
3. duplicidades confirmadas e falsos duplicados;
4. catálogos reutilizáveis pelo novo módulo;
5. arquivos que devem permanecer exclusivos do legado;
6. proposta de coexistência no menu e no roteador;
7. proposta do primeiro Kid Step de implementação;
8. riscos e perguntas que dependem de decisão de produto do Fabio.

## Critério de encerramento

A auditoria somente estará concluída após:

- registrar fatos observados com referência aos arquivos;
- consolidar os achados relevantes em `docs/architecture/08_ORCAMENTOS.md`;
- atualizar `docs/PROJECT_STATE.md` com o próximo passo aprovado;
- reler e confirmar todas as gravações.
