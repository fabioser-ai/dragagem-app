# Arquitetura Atual — Estrutura Modular

Esta pasta contém a documentação oficial e consolidada da arquitetura atual do APP FOS.

## Regra de autoridade

- `docs/PROJECT_STATE.md` registra o estado oficial e o workflow do projeto.
- `docs/DEVELOPMENT_PHILOSOPHY.md` define os princípios permanentes de desenvolvimento e auditoria.
- `docs/architecture/` é a fonte consolidada da arquitetura atual por domínio.
- `docs/audit/` preserva o histórico detalhado de cada auditoria.
- `docs/ARCHITECTURE_CURRENT.md` permanece como documento legado durante a transição para a estrutura modular.

A documentação oficial prevalece sobre memória de conversas. Conclusões devem ser baseadas em código observado e nos registros oficiais; hipóteses, lacunas e limites precisam ser identificados como tais.

## Workflow oficial

1. Ler `docs/PROJECT_STATE.md`, `docs/DEVELOPMENT_PHILOSOPHY.md` e a documentação modular aplicável.
2. Auditar um subsistema por vez ou um recorte transversal explicitamente definido.
3. Criar `docs/audit/AUDIT_XXX_<SUBSISTEMA>.md`.
4. Consolidar os fatos observados no arquivo modular correspondente desta pasta.
5. Não alterar comportamento funcional nem refatorar por preferência durante auditorias.
6. Confirmar toda escrita por leitura posterior.
7. Atualizar `docs/PROJECT_STATE.md`.
8. Não registrar hipóteses como fatos.

## Índice atual

- `01_MEDICOES_FUNDACAO.md`
- `02_MEDICOES_LANCAMENTOS.md`
- `03_MEDICOES_APROVACAO.md`
- `04_MEDICOES_GESTAO.md`
- `08_ORCAMENTOS.md`
- `09_PRESTACAO_CONTAS.md`
- `10_CRM.md`
- `11_ADMINISTRACAO.md`
- `12_SERVICOS_COMPARTILHADOS.md`
- `13_AUDITORIA_TRANSVERSAL.md`
- `14_CONHECIMENTO_REGISTRADO.md`
- `15_MATRIZ_COBERTURA_DOCUMENTAL.md`
- `16_DADOS.md`
- `17_FERIAS.md`

## Cobertura

A matriz em `15_MATRIZ_COBERTURA_DOCUMENTAL.md` relaciona as rotas observadas em `app.py` às fontes arquiteturais vigentes e registra o nível de cobertura e as lacunas conhecidas.

A documentação modular possui cobertura forte para Medições, Orçamentos, Prestação de Contas, CRM, Administração, Serviços Compartilhados, Dados e Férias. `Obras` permanece sem auditoria modular dedicada.

## Migração

Os demais domínios serão migrados gradualmente a partir do documento legado e de novas auditorias. Nenhum conteúdo do arquivo legado deve ser removido até a migração correspondente ser confirmada.