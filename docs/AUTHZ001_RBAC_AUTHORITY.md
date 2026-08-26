# AUTHZ-001 — RBAC como autoridade única

## Decisão

O modo normal é `RBAC`. Para usuários operacionais, a decisão segue somente:

`identidade ativa → associações ativas → Roles ativas → matriz → catálogo ativo → escopo`

Ausência, ambiguidade, chave desconhecida, leitura não confirmada ou escopo
incompatível resultam em negação. `data/permissoes_usuarios.csv` permanece como
referência histórica, diagnóstico e rollback, mas não é consultado pelo motor RBAC.

Contas e credenciais não foram alteradas. O proprietário identificado exatamente
por `SYSTEM_OWNER_ID` possui o bypass explícito `TEMPORARY_OWNER_BYPASS`. Nenhum
perfil, Role, CSV ou tela pode incluir outra identidade nesse bypass.

## Escopo

A associação Pessoa → Role recebeu `obra_id`. O valor `todas` aplica as permissões
da Role a todas as obras; outro valor restringe todas as permissões daquela
associação à obra indicada quando a permissão do catálogo exige obra. A mesma
pessoa pode possuir a mesma Role em escopos diferentes e múltiplas Roles ativas.

### Precedência allow/deny

O efeito é resolvido por permissão e por escopo:

- `deny` vence `allow` para a mesma combinação módulo/recurso/ação e obra;
- `deny obra A` não interfere em `allow obra B`;
- `deny` de uma ação não contamina outra ação do mesmo módulo;
- `allow todas + deny obra A` significa todas as obras exceto A;
- `deny todas + allow obra A` continua negado, pois o deny global se aplica a A;
- o módulo aparece quando existe ao menos uma capacidade allow efetiva.

Na API de listagem, “todas, exceto A” é representado por `["todas",
"!obra-a"]`. Consumidores devem aplicar as exclusões antes de liberar registros.

## Inventário de impacto

| Área | Decisão anterior | Decisão nova | Risco principal | Cobertura |
|---|---|---|---|---|
| Rotas e menu | `permissoes_usuarios.csv` pela camada central | RBAC pela camada central | módulo desaparecer sem Role válida | `test_authz001_rbac_authority.py`, `test_autorizacao_rotas.py` |
| Dados/Atestados | regras individuais legadas | Role + permissão exata | exclusão/edição negada sem concessão | regressão de Dados e catálogo |
| Férias/Folgas | regras individuais legadas | Role + permissão exata | alertas e ciclo de vida negados | regressão de Férias |
| Prestação de Contas | regras individuais legadas | Role + permissão exata | criação negada | regressão do módulo |
| CRM | regras individuais legadas | Role + permissão exata | interação negada | regressão de CRM |
| Uniformes/EPIs | regras individuais legadas | Role + permissão exata | cadastros/entregas negados | regressão do módulo |
| Orçamentos | regras individuais legadas | Role + permissão exata | edição/criação negada | regressão de Orçamentos |
| Medições | `usuarios_obras.csv` e perfil próprio | motor central RBAC + `obra_id` | usuários históricos sem identidade/Role perdem acesso | testes AUTHZ e regressão de Medições |
| Administração | custódia por superadmin legado | bypass temporário do owner | secret inválido bloqueia Administração | testes de owner e AUTHZ |
| Diagnóstico | Shadow Mode | RBAC real × legado anterior | nomenclatura ser confundida com autoridade | testes UX |

`data/medicoes/usuarios_obras.csv` não foi apagado, mas deixou de participar das
decisões. Os consumidores funcionais continuam chamando a API central e não leem
CSV de Roles diretamente.

## Modos e rollback

O secret não editável pela interface é `AUTHORIZATION_MODE`:

- ausente ou `RBAC`: somente RBAC;
- `LEGACY`: somente o motor legado;
- qualquer outro valor: negação segura.

Não existe fallback. Para rollback emergencial, definir `AUTHORIZATION_MODE =
"LEGACY"` nos secrets do Streamlit Cloud e reiniciar o app. Para retornar ao modo
normal, definir `"RBAC"` (ou remover a chave) e reiniciar. O arquivo legado deve
ser preservado enquanto essa opção existir.

## Homologação e riscos

O cadastro TESTE encontrado na implantação já possui associações ativas
FUNCIONARIO e APROVADOR, divergindo do cenário inicial descrito na missão. Antes
de homologar “sem Role”, retirar essas associações pela Administração; não houve
mutação silenciosa dos dados reais.

A matriz atual não contém concessões para Medições. Além disso, identidades que
existem apenas em `usuarios_obras.csv` não são identidades RBAC. Esses usuários
serão negados até que identidade, Role, permissão e escopo sejam configurados.
Este é o efeito esperado do corte, mas exige acompanhamento operacional.

## Dívida obrigatória

`TEMPORARY_OWNER_BYPASS` contém TODO explícito e deve ser removido após:

1. cadastrar Fabio no RBAC normal;
2. homologar suas Roles, permissões e escopos;
3. retirar o bypass;
4. retirar o modo `LEGACY`;
5. arquivar a infraestrutura anterior.
