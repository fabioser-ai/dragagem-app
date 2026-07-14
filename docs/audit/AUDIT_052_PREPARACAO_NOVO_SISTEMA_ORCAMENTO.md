# AUDIT_052 — Preparação do Novo Sistema de Orçamento

## Natureza deste documento

Este documento prepara a futura auditoria do estado atual do módulo de Orçamentos. Sua criação não executa a auditoria, não define a arquitetura do novo sistema e não autoriza implementação ou migração.

## Missão

Produzir, em sessão própria e com base exclusivamente em evidências observáveis no repositório, uma visão completa do módulo atual de Orçamentos e de suas dependências, para apoiar posteriormente o desenho seguro do Novo Sistema de Orçamento da FOS.

## Escopo

A futura auditoria deverá abranger:

- entrada e roteamento do módulo atual de Orçamentos;
- dashboard;
- etapas do fluxo legado;
- estado de sessão utilizado;
- persistência;
- serviços utilizados;
- todos os CSVs consumidos;
- todos os CSVs gravados;
- leitores e escritores de cada CSV;
- dependências entre Orçamentos e outros módulos;
- fronteira de coexistência entre Orçamento — Legado e Novo Sistema de Orçamento.

O módulo legado deverá ser observado sem alteração.

## Objetivos

A futura auditoria deverá:

1. inventariar integralmente o módulo legado;
2. mapear os CSVs consumidos e gravados;
3. registrar, para cada CSV:
   - finalidade;
   - schema observado;
   - identidade do registro;
   - leitores;
   - escritores;
   - granularidade;
   - natureza como catálogo, transação, histórico ou resultado calculado;
   - potencial de reutilização;
   - riscos;
   - classificação entre reutilizar, ampliar, relacionar, consolidar, manter separado ou legado;
4. construir a matriz de dependências;
5. identificar duplicidades reais e falsos duplicados;
6. identificar candidatos à consolidação;
7. identificar arquivos que devem permanecer independentes;
8. propor a reutilização dos catálogos existentes;
9. propor a coexistência entre o módulo legado e o novo sistema;
10. propor o primeiro Kid Step de implementação, sujeito à homologação posterior do Merlin.

Toda constatação deverá distinguir fato observado, lacuna de evidência e questão ainda não decidida.

## Restrições

Durante a futura auditoria, não será permitido:

- implementar funcionalidades;
- criar ou alterar telas;
- criar CSVs;
- alterar comportamento funcional;
- iniciar migração;
- mover, renomear ou apagar arquivos;
- refatorar por preferência;
- inventar fórmulas;
- registrar hipótese como fato;
- alterar o módulo legado;
- iniciar qualquer Kid Step de implementação antes da homologação do Merlin.

## Entregáveis

A futura auditoria deverá produzir:

1. inventário completo do módulo legado;
2. mapa dos CSVs;
3. matriz de dependências;
4. matriz de duplicidades;
5. proposta de reutilização dos catálogos;
6. proposta de coexistência entre Orçamento — Legado e Novo Sistema de Orçamento;
7. proposta do primeiro Kid Step de implementação.

Os entregáveis deverão permanecer documentais e fundamentados em evidências do repositório.

## Critérios de encerramento

A AUDIT_052 somente poderá ser considerada concluída quando:

- todas as fontes oficiais obrigatórias tiverem sido lidas;
- o código do módulo e suas dependências diretas tiverem sido inspecionados;
- todos os CSVs consumidos e gravados pelo módulo tiverem sido identificados e classificados;
- os sete entregáveis estiverem registrados;
- fatos, hipóteses, lacunas e decisões pendentes estiverem claramente separados;
- nenhuma implementação, migração ou alteração funcional tiver sido realizada;
- toda documentação produzida tiver sido gravada, relida diretamente do repositório e conferida;
- o resultado estiver aguardando homologação do Merlin.

## Referências oficiais

Antes de executar a futura auditoria, deverão ser lidos integralmente:

- `docs/PROJECT_STATE.md`;
- `docs/DEVELOPMENT_PHILOSOPHY.md`;
- `docs/architecture/README.md`;
- `docs/architecture/08_ORCAMENTOS.md`;
- `docs/architecture/16_DADOS.md`;
- `docs/architecture/21_ESTRATEGIA_FASE_2_ORCAMENTOS.md`;
- este documento.

Também deverão ser consultadas as fontes de auditoria e os arquivos de código diretamente relacionados que forem referenciados por esses documentos.

## Próxima etapa autorizada

Após a criação, releitura e validação deste documento, uma nova sessão poderá executar a AUDIT_052.

Esta sessão de preparação termina com a validação documental e não executa a auditoria.
