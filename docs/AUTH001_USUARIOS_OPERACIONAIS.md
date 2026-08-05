# AUTH-001 — Modelo e administração de usuários operacionais

## Arquitetura híbrida

`APP_USERS` permanece responsável exclusivamente pelas contas protegidas e
pela autenticação atual. `SYSTEM_OWNER_ID` permanece a única fonte canônica da
propriedade. O AUTH-001 cria uma base separada,
`data/usuarios_operacionais.csv`, administrada somente pela autoridade central.

**Usuários operacionais cadastrados neste AUTH-001 ainda não podem autenticar no APP.**

## Identidade e dados

O vínculo futuro com `data/permissoes_usuarios.csv` usa o `login` normalizado,
enquanto `usuario_id` é um UUID imutável e jamais reutilizado. Login é único
sem distinção de caixa; matrícula também é única quando informada. Nome não é
chave. Não há exclusão física: a conta é ativada ou inativada.

A base contém somente os campos homologados. Não contém senha, hash, token ou
secret. `credencial_configurada` e `exige_troca_senha` são marcadores
informativos fixados como `nao` nesta etapa.

## Perfis e autorização

Perfis aceitos: `user`, `funcionario`, `encarregado` e `aprovador`. O cadastro
inicial usa `user` e fica inativo. `admin`, `superadmin`, `proprietario`,
`owner` e valores desconhecidos são negados. Somente superadmin ou proprietário
com recuperação administrativa ativa pode administrar a base, por meio de
`pode_gerenciar_usuarios_operacionais()`, revalidado imediatamente antes da
persistência.

Antes de criar um login, o serviço lê `APP_USERS` sem devolver seus dados à
interface. Se a leitura falhar, criação e renomeação são negadas. Conflitos são
comparados após `strip` e `casefold` e informados apenas como identificador
reservado.

## Persistência e permissões

A escrita usa o SHA obtido na leitura confirmada do CSV, impedindo sobrescrita
concorrente silenciosa. Falha de leitura nunca é interpretada como base vazia.
O cadastro não cria linhas em `permissoes_usuarios.csv`: módulos, ações e obras
continuam exigindo concessão administrativa explícita e separada.

## Limitações e riscos residuais

- A base operacional ainda não autentica e não possui credenciais.
- O login, e não o UUID, é o identificador compatível com o arquivo legado de permissões.
- A consistência entre uma futura troca de login e permissões deverá ser resolvida antes de permitir renomeação; por isso o login é somente leitura no AUTH-001.
- A persistência continua dependente da disponibilidade e das garantias da API do GitHub.
- O perfil `admin` operacional não foi habilitado porque não é indispensável neste passo.

## Próximos passos

- **AUTH-002:** credenciais seguras e integração controlada com o login, sem migrar contas protegidas automaticamente.
- **AUTH-003:** ciclo de senha, troca obrigatória e controles adicionais homologados para autenticação operacional.
