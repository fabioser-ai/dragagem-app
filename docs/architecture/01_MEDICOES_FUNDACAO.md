# Arquitetura Atual — Medições: Fundação

Última atualização: 2026-07-11

Fonte: `docs/ARCHITECTURE_CURRENT.md` e `docs/audit/AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md`.

## Entrada e navegação

`pages/medicoes.py` inicia o módulo, valida `tem_acesso_medicoes()`, obtém o perfil interno, inicializa `fluxo_medicoes` e `etapa_medicoes` na sessão e delega a navegação a `modulos/medicoes/navegacao.py`.

Os fluxos internos observados são `inicio`, `gestao`, `lancamento` e `aprovacao`. Funcionário é direcionado ao lançamento; gestão é restringida a quem pode criar medição.

## Autorização específica

A camada geral do aplicativo decide a exposição de Medições. O módulo então usa `data/medicoes/usuarios_obras.csv`, com `usuario_id`, `email`, `nome`, `obra_id`, `perfil_medicao` e `ativo`.

Perfis internos: `funcionario < encarregado < aprovador < admin`.

- todos podem lançar;
- encarregado, aprovador e admin podem visualizar;
- aprovador e admin podem aprovar;
- somente admin pode criar ou gerenciar medição.

O perfil interno `admin` não equivale automaticamente ao perfil global `superadmin`.

## Dados e repositórios

`modulos/medicoes/config.py` declara modelos, etapas, schemas, status e caminhos de dados. Os arquivos principais incluem obras, BMs, frentes, MC, itens, serviços, locais, lançamentos e vínculos de usuários.

Há dois repositórios sobre `services/github.py`:

- `modulos/medicoes/repositorio.py`: bases da gestão, tabelas contratuais, locais, lançamentos e compatibilidade legada;
- `modulos/medicoes/lancamentos/repositorio.py`: lançamentos, locais e vínculos operacionais.

Ambos acessam `locais_trabalho.csv`, `usuarios_obras.csv` e `lancamentos_trabalho.csv`. A sobreposição está documentada; não consolidar sem necessidade comprovada.

`salvar_lancamento_producao()` é marcado como legado; o fluxo atual aponta para `criar_lancamento_trabalho()`.

## Limites registrados

- O maior perfil do usuário pode ser calculado em todos os vínculos, enquanto filtragens usam a primeira linha em alguns fluxos.
- O estado em sessão conecta etapas e pode sobreviver a mudanças de contexto.
- A persistência subjacente regrava CSVs integralmente; seus riscos estão consolidados em Serviços Compartilhados.
