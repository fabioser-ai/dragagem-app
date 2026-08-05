# AC-002 — Autoridade única de autorização

**Commit-base:** `8e5fdef8e054fb4e064c8641db0cba20a042d441`

**Escopo:** decisões globais de identidade, módulo, recurso, ação e obra.

**Estado:** implementação incremental; a segurança do APP não está concluída.

## Interface central

`services/autorizacao.py` é a fachada canônica consumida pelos módulos. Ela
interpreta a sessão autenticada e delega a leitura do modelo legado exclusivamente
a `services/permissoes.py`.

| Pergunta | Função canônica |
|---|---|
| Há sessão autenticada? | `autenticado()` |
| É superadmin? | `usuario_superadmin()` |
| É administrador operacional ou superadmin? | `possui_privilegio_administrativo()` |
| Possui um perfil global específico? | `possui_perfil()` |
| Pode entrar no módulo? | `pode_acessar()` |
| Pode agir sobre módulo/recurso/ação/obra? | `pode()` |
| Pode agir sobre uma obra explícita? | `pode_operar_obra()` |
| Quais obras são permitidas? | `listar_obras_permitidas()` |
| Pode entrar na rota? | `pode_acessar_rota()` |

Sem sessão, sem concessão ou com falha na leitura das permissões, a decisão é
negativa. `superadmin` mantém bypass no modelo legado. `admin` passa apenas pela
consulta administrativa e não é promovido a superadmin.

## Inventário e classificação

| Local | Decisão encontrada | Classe | Tratamento AC-002 |
|---|---|---|---|
| `app.py` / `pode_acessar_rota` | entrada de rota | global/módulo | preservada na fachada central |
| `pages/menu.py` / cartões | exibição de módulos | visual | passou a consumir a fachada; não é fronteira de segurança |
| `pages/administracao.py` / `render`, `_salvar_alteracao` | superadmin e alteração de permissões | global/ação administrativa | centralizada e revalidada antes da gravação |
| `pages/ferias.py` / `salvar_csv_seguro`, `aplicar_transicao` | criar, editar, excluir e transicionar | ação/recurso | centralizada antes da persistência |
| `pages/uniformes_epis.py` / `_salvar` | editar cadastros e movimentações | ação/recurso | revalidada antes da persistência |
| `pages/prestacao_contas.py` / criação e análise | criar despesa; aprovar, reprovar, pagar; gerir tipos | ação/administrativa | criação consulta `pode`; ações administrativas consultam autoridade central |
| `pages/dados.py` / `_salvar_cadastro`, `_publicar_exclusao_composta` | CRUD e exclusão composta | ação/recurso | centralizada antes de qualquer commit |
| `pages/crm/repositorio.py` / gravações | criar/editar cadastros e interação composta | ação/recurso | centralizada no repositório funcional |
| `modulos/orcamentos/persistencia/github_repositorio.py` | persistir versão/documento | ação/recurso | centralizada imediatamente antes da chamada remota |
| `pages/orcamento/etapa0.py` a `etapa3.py` e `pages/orcamento_old.py` | rascunho, cliente e insumos | ação/recurso | guardas adicionadas nos pontos legados de gravação |
| `pages/obras.py` | leitura e composição da tela | módulo/visual | acesso continua na rota central; não havia mutação a migrar |
| `services/auth.py` / `exigir_admin` | autoridade administrativa | global | passou a consumir a fachada; fluxo de login não foi alterado |
| `services/permissoes.py` | interpretação do CSV e curingas | modelo de autorização | mantida como única fonte persistida, sem mudança de schema |

## Decisões preservadas nos módulos

- Validações de campos, estados, sobreposição de férias, consistência de
  snapshots e demais regras de negócio permanecem onde estavam.
- A escolha de quais abas e botões mostrar continua sendo responsabilidade de
  apresentação, mas não autoriza persistência.
- Medições mantém integralmente `modulos/medicoes/permissoes.py` e suas regras
  por obra/perfil. Sua integração global continua sendo a rota `medicoes` da
  fachada central; nenhuma regra interna foi refatorada.
- Obras permanece somente leitura no fluxo auditado.

## Compatibilidade

O arquivo `data/permissoes_usuarios.csv`, seus campos, valores ativos e curingas
`todos`/`todas` não foram modificados. As novas decisões usam `pode_executar()`
com a mesma semântica. Usuários com concessões curinga mantêm os fluxos atuais.
Nenhum usuário, perfil, secret ou CSV de produção foi alterado.

## Testes e propriedades verificadas

`tests/test_autorizacao_ac002.py` cobre negação de criar/editar/excluir/aprovar,
chamada direta, independência de botão, usuário autorizado, superadmin, separação
de admin, falha fechada, obra e ausência de gravação CSV/remota. A regressão do
catálogo e de alteração direta de `session_state.tela` permanece em
`tests/test_autorizacao_rotas.py`.

## Limitações e riscos residuais

1. A identidade canônica do proprietário continua fora do escopo; superadmin
   ainda deriva do perfil global da sessão.
2. A revogação imediata de sessão, hash de senha, MFA e bloqueio de tentativas
   continuam pendentes.
3. Medições mantém uma autoridade própria por obra e será unificada em missão
   específica.
4. Uniformes/EPIs conserva a granularidade legada `cadastros/editar` para suas
   diversas movimentações; separar capacidades exige decisão e migração de dados.
5. Prestação de Contas conserva a autoridade administrativa histórica para
   aprovação/reprovação/pagamento; uma matriz granular dessas ações requer
   decisão humana e dados compatíveis.
6. Operações somente de leitura e exportações não classificadas como sensíveis
   não receberam novas capacidades neste passo.

## Próximas etapas

1. Homologar a matriz de ações por módulo e definir capacidades hoje agrupadas.
2. Tratar a autorização por obra de Medições sem promover perfil entre obras.
3. Definir identidade canônica e recuperação segura do proprietário.
4. Adicionar revogação de sessão e trilha de auditoria das decisões negadas.
5. Migrar permissões somente após validar usuários e dados legados.
