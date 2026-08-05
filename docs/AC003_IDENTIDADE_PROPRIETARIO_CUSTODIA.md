# AC-003 — Identidade canônica do proprietário e custódia

**Commit-base:** `fe0220c5f642f015540dd5e46e72f0ab3357eaa5`

**Estado:** implementação mínima de identidade e recuperação administrativa.
A segurança integral do APP continua sendo um processo incremental.

## Modelo de identidade

O APP passa a distinguir quatro conceitos:

| Conceito | Fonte | Alcance |
|---|---|---|
| Proprietário canônico | secret `SYSTEM_OWNER_ID` | custódia permanente e recuperação administrativa |
| Superadmin | perfil autenticado em `APP_USERS` | bypass global existente no AC-001/AC-002 |
| Admin operacional | perfil autenticado em `APP_USERS` | funções administrativas operacionais existentes |
| Usuário comum | autenticação e permissões legadas | módulos, recursos, ações e obras autorizados |

Proprietário e superadmin são conceitos independentes. Um superadmin não se
torna proprietário. O proprietário sem perfil superadmin continua sendo o
custodiante e pode iniciar a recuperação mínima da Administração.

## Fonte canônica

`services/autorizacao.py` é a única camada autorizada a consultar
`SYSTEM_OWNER_ID`. Não existe fallback para `APP_USERS`, CSV, perfil, e-mail,
nome, constante de usuário ou configuração administrativa.

Uma identidade válida é uma string não vazia, sem espaços periféricos, com até
128 caracteres e composta por letras ASCII, números e `_.@+-`. A comparação com
o usuário autenticado é normalizada sem diferenciar maiúsculas e minúsculas.

O identificador não é mostrado na interface, nos diagnósticos ou nos resultados
da recuperação. A tela administrativa não lê nem altera secrets.

## Autoridade central

A fachada `services/autorizacao.py` fornece:

- `identificador_proprietario()` — leitura interna da identidade válida;
- `identidade_proprietario_valida()` — validade da configuração;
- `usuario_proprietario()` — correspondência da sessão autenticada;
- `pode_recuperar_administracao()` — decisão de recuperação;
- `recuperar_administracao()` — revalidação, elevação mínima e registro;
- `diagnostico_identidade_proprietario()` — códigos seguros, sem o secret;
- `pode_gerenciar_administracao()` — superadmin ou proprietário recuperado.

Nenhum módulo interpreta a identidade canônica diretamente.

## Fluxo de recuperação

1. O usuário autentica pelo fluxo existente de `APP_USERS`.
2. A autoridade central valida exclusivamente `SYSTEM_OWNER_ID`.
3. Se a sessão corresponde ao proprietário e ainda não possui acesso à
   Administração, o menu oferece a recuperação.
4. No clique, a identidade é revalidada imediatamente.
5. Em sucesso, a sessão recebe apenas a marca temporária
   `_custodia_admin_recuperada`.
6. A tentativa concedida ou negada é enviada ao log de acesso existente.
7. Logout ou expiração remove a marca; uma nova recuperação exige nova sessão e
   nova validação do secret.

A recuperação não altera `APP_USERS`, perfil, permissões, proprietário ou CSV de
configuração. Ela não converte o proprietário em superadmin e não concede bypass
global: permite somente a autoridade administrativa necessária.

## Estados e inconsistências

| Código de diagnóstico | Significado | Comportamento |
|---|---|---|
| `secret_ausente` | secret não configurado | nega propriedade e recuperação |
| `secret_invalido` | tipo ou formato inválido | nega propriedade e recuperação |
| `sessao_nao_autenticada` | configuração válida, sem login | nega recuperação |
| `sessao_nao_proprietaria` | outro usuário autenticado | mantém seus privilégios normais |
| `proprietario_sem_superadmin` | proprietário autenticado sem bypass | oferece recuperação mínima |
| `proprietario_recuperado` | recuperação ativa e revalidada | permite Administração nesta sessão |
| `proprietario_superadmin` | proprietário também possui perfil superadmin | preserva o acesso global existente |

Falhas no registro do log não promovem outro usuário nem expõem o secret. O
resultado informa apenas se a tentativa de log foi concluída.

## Procedimento manual de emergência

1. Confirmar no painel protegido da implantação que `SYSTEM_OWNER_ID` contém o
   identificador canônico esperado. Não copiar seu valor para logs, chamados ou
   documentação.
2. Confirmar que `APP_USERS` ainda contém uma credencial autenticável para o
   mesmo identificador. `APP_USERS` autentica; não define propriedade.
3. Se a entrada de autenticação foi removida acidentalmente, restaurá-la
   manualmente no painel de secrets, sem alterar `SYSTEM_OWNER_ID`.
4. Reiniciar a sessão, autenticar como proprietário e usar **Recuperar
   Administração** no menu.
5. Confirmar no log apenas o evento de recuperação, sem registrar o conteúdo do
   secret.

Não existe recuperação por e-mail, senha, código temporário ou promoção de
terceiros neste Kid Step.

## Compatibilidade preservada

- AC-001: catálogo de rotas, negação por padrão e proteção contra alteração de
  `session_state.tela` permanecem ativos.
- AC-002: `pode()`, permissões por módulo/recurso/ação/obra e guardas de
  persistência permanecem inalterados.
- `APP_USERS` continua sendo usado somente para autenticação, usuários e perfis.
- `data/permissoes_usuarios.csv` e todos os demais CSVs mantêm schema e conteúdo.
- Medições conserva integralmente sua arquitetura própria.

## Limitações e riscos residuais

1. A autenticação do proprietário ainda depende de existir uma credencial
   correspondente em `APP_USERS`; a custódia é permanente, mas a restauração de
   uma credencial removida exige intervenção manual nos secrets.
2. A recuperação dura a sessão atual; não existe revogação server-side imediata.
3. O registro utiliza o log de acesso legado e pode falhar se o GitHub estiver
   indisponível; a falha é informada no resultado técnico.
4. Hash de senha, MFA, bloqueio por tentativas, múltiplos proprietários e sucessão
   continuam deliberadamente fora do escopo.
5. Medições continua com autoridade específica própria.
