# AUDIT-ACESSO-UX-001 — Auditoria funcional, técnica e de usabilidade

## 1. Resumo executivo

**Commit efetivamente inspecionado:** `8a67f0a7375383fb73b36c6182fa5c543215fc54`.
O SHA é posterior ao baseline informado (`22e2a016...`) e, conforme a missão,
foi tratado como fonte da verdade. Entre ambos há somente quatro commits de
dados: um registro de acesso, criação e ativação legítimas de um usuário
operacional e uma associação Usuário → Role. Nenhuma lógica foi alterada.

O cadastro operacional, a ativação, a associação de Role e o diagnóstico em
modo sombra funcionam e persistem com controle de concorrência. Porém, o usuário
operacional ainda **não é uma conta autenticável**. Seu e-mail é apenas dado
cadastral; não existe geração de senha, convite, token, primeiro acesso ou envio
de e-mail nesse fluxo. A autenticação continua usando exclusivamente o secret
`APP_USERS`, com comparação direta de senha (`services/auth.py:14-18,88-136`).

A página Administração reuniu, em uma única sequência vertical, catálogo,
Roles, usuários, vínculos, diagnóstico e permissões legadas
(`pages/administracao.py:123-179,182-259,262-340,343-488,491-635`). A
separação técnica está sinalizada em legendas, mas a jornada principal — “criar
uma pessoa e definir o que pode fazer” — exige rolagem, seletores independentes
e interpretação de RBAC. O sistema não fornece uma visão consolidada do usuário.

### Conclusão executiva

- **Funcional:** cadastro/edição/inativação operacional; catálogo de Roles;
  associação/inativação/reativação de Role; Shadow Mode; login/logout das contas
  já existentes em `APP_USERS`; autorização legada.
- **Somente documental/diagnóstico:** Role do usuário e permissão calculada pelo
  RBAC; elas não autorizam o APP.
- **Inexistente no fluxo operacional:** credencial, hash, convite, e-mail de
  primeiro acesso, senha temporária, reset, troca obrigatória e revogação de uma
  sessão já autenticada.
- **Impedimento para piloto real:** não há caminho seguro para o usuário
  operacional entrar; e, quando existir, ainda será necessário ativar RBAC e
  definir escopo de dados.

## 2. Mapa da arquitetura atual

| Componente | Fonte | Estado | Evidência |
|---|---|---|---|
| Conta autenticável | secret `APP_USERS` | efetivo | `services/auth.py:14-18,118-130` |
| Proprietário | secret `SYSTEM_OWNER_ID` | efetivo para custódia | `services/autorizacao.py:46-86` |
| Usuário operacional | `data/usuarios_operacionais.csv` | cadastro funcional; não autentica | `services/usuarios_operacionais.py:1-5,20-25,133-182` |
| Role institucional | `data/roles.csv` | catálogo funcional | `services/roles.py:20-35,71-76,174-223` |
| Permissão da Role | `data/roles_permissoes.csv` | matriz documental | `services/roles.py:21,26,86-126` |
| Usuário → Role | `data/usuarios_roles.csv` | vínculo funcional; sem efeito de acesso | `services/usuarios_roles.py:1,15-19,104-159` |
| Cálculo RBAC | snapshots dos catálogos | Shadow Mode somente | `services/rbac_shadow.py:58-173` |
| Autorização efetiva | `data/permissoes_usuarios.csv` + AC-001/002/003 | efetivo | `services/permissoes.py:16-25,123-218`; `services/autorizacao.py:208-263` |
| Medições | modelo próprio por obra | efetivo e separado | `data/medicoes/usuarios_obras.csv`; `modulos/medicoes/permissoes.py` |
| Log mínimo | `data/log_acessos.csv` | login/logout/expiração e recuperação | `services/log.py:13-71`; `services/auth.py:50-76,88-104` |

O roteador autentica antes de carregar páginas e revalida a rota centralmente
(`app.py:10-27`). Administração exige superadmin ou proprietário com custódia
recuperada (`pages/administracao.py:491-497`; `services/autorizacao.py:178-200`).

## 3. Fluxo real de criação e ativação

### Respostas obrigatórias sobre o fluxo atual

1. **Criação:** a Administração lê a base com status e SHA, recebe login, nome,
   matrícula, e-mail e perfil, valida os campos e contas protegidas, cria uma
   linha inativa e persiste o CSV (`pages/administracao.py:262-302`;
   `services/usuarios_operacionais.py:47-59,82-113,133-153`).
2. **Campos persistidos:** os 13 campos de `COLUNAS`: `usuario_id`, `login`,
   `nome`, `matricula`, `email`, `perfil_base`, `ativo`, criação/autoria,
   atualização/autoria, `exige_troca_senha` e `credencial_configurada`
   (`services/usuarios_operacionais.py:20-25`).
3. **Geração do ID:** `uuid4()` no momento da criação
   (`services/usuarios_operacionais.py:11,147-151`).
4. **Estado inicial:** `ativo=nao`, `exige_troca_senha=nao` e
   `credencial_configurada=nao` (`services/usuarios_operacionais.py:147-152`).
5. **Ativação/inativação:** seleção do usuário, alteração do campo `ativo` e
   salvamento com o mesmo UUID e login; a autorização é revalidada antes da
   persistência (`pages/administracao.py:304-334`;
   `services/usuarios_operacionais.py:156-182,116-130`).
6. **Exclusão física:** não existe para usuário operacional; a interface informa
   isso (`pages/administracao.py:336-339`).
7. **E-mail:** apenas cadastral e validado sintaticamente
   (`services/usuarios_operacionais.py:82-95,110-113`).
8. **Geração de senha:** inexistente.
9. **Senha temporária:** inexistente.
10. **Hash de senha:** inexistente para usuários operacionais; o login atual
    compara diretamente a senha digitada com `APP_USERS.password`
    (`services/auth.py:118-120`).
11. **Token de primeiro acesso:** inexistente.
12. **Tentativa de envio de e-mail:** inexistente nesse fluxo. Não há importação
    ou chamada de serviço de e-mail nos arquivos de Administração/usuários.
13. **SMTP/Gmail/API:** nenhuma integração no módulo de acesso. Existe SMTP em
    Férias, mas é um fluxo separado (`pages/ferias.py:19-21,497-502`).
14. **Expectativa de envio:** não há botão ou texto prometendo convite. Contudo,
    o campo “E-mail” sem a mensagem “somente cadastral; nenhum convite será
    enviado” cria expectativa plausível para um administrador não técnico
    (`pages/administracao.py:290-297`).
15. **`credencial_configurada`:** marcador informativo que hoje significa
    somente o valor literal inicial `nao`; não comprova consulta a provedor.
16. **Origem do marcador:** inicializado como `nao`, não editável e não derivado;
    não há outra atribuição no código (`services/usuarios_operacionais.py:147-152`;
    `pages/administracao.py:281-286`).
17. **Autenticação operacional hoje:** não. O cadastro não é lido por
    `services/auth.py` (`services/usuarios_operacionais.py:1-5`).
18. **O que falta:** armazenamento de credencial com hash; ativação segura;
    primeiro acesso; reset/troca; integração do usuário operacional no login;
    revalidação de estado; revogação; e ligação homologada entre RBAC e a
    autoridade efetiva.
19. **Atribuição de Role:** exige usuário e Role ativos, nega contas protegidas,
    cria UUID da associação e salva com SHA
    (`services/usuarios_roles.py:63-85,104-138`).
20. **Retirada/reativação:** retirada marca `ativo=nao`; reatribuição do mesmo
    par reativa o registro e preserva UUID/criação
    (`services/usuarios_roles.py:115-138,141-159`).
21. **Shadow Mode:** resolve associações e Roles ativas, reúne apenas permissões
    `allow` existentes no catálogo, deduplica e compara com as concessões atuais
    pelo login (`services/rbac_shadow.py:58-141`).
22. **Funcional versus documental:** persistência de usuários/Roles/vínculos é
    funcional; cálculo é funcional como diagnóstico; o efeito autorizador das
    Roles é apenas documental (`services/rbac_shadow.py:1,58-62`;
    `pages/administracao.py:439-488`).
23. **Fonte efetiva:** `permissoes_usuarios.csv`, superadmin/custódia e regras
    centrais AC-001/002/003 (`services/autorizacao.py:208-263`).
24. **Coexistência ambígua:** sim para o administrador. A interface mostra
    simultaneamente “permissões RBAC” e “permissões cadastradas” sem uma ficha
    única explicar que apenas a segunda fonte autoriza. Tecnicamente o código
    mantém isolamento; semanticamente a experiência é ambígua.

## 4. Estado real de credenciais e e-mail

| Capacidade | Estado | Evidência |
|---|---|---|
| E-mail cadastral | já existe | `services/usuarios_operacionais.py:82-95` |
| Envio de convite | inexistente | ausência de chamada em Administração/serviços de usuários |
| Geração de senha | inexistente | `services/usuarios_operacionais.py:20-25,133-153` |
| Hash operacional | inexistente | cadastro não possui campo de hash |
| Primeiro acesso | inexistente | nenhum token/estado/fluxo |
| Senha temporária | inexistente | nenhum gerador ou persistência |
| Reset administrativo | inexistente | nenhuma ação na Administração |
| Troca obrigatória | inexistente funcionalmente | marcador nasce `nao` e nunca muda |
| Login protegido atual | já existe, mas só para `APP_USERS` | `services/auth.py:14-18,88-136` |

**Achado alto — falsa completude percebida.** “Ativo”, e-mail preenchido, Role
atribuída e diagnóstico calculado podem parecer uma conta pronta, embora nenhum
desses passos crie credencial. A legenda de que o usuário não autentica existe,
mas fica localizada no início de uma seção extensa (`pages/administracao.py:262-266`).

## 5. Mapa da interface atual

A ordem real é:

1. Catálogo de permissões (consulta técnica e quatro filtros);
2. Roles (lista, criação, edição e permissões);
3. Usuários operacionais (lista, criação e edição/estado);
4. Roles dos usuários (outro seletor de usuário, histórico e ações);
5. Diagnóstico RBAC (tabela ampla);
6. Permissões efetivas legadas (lista, criação, desativação e exclusão).

Essa ordem segue a arquitetura, não a tarefa humana. O administrador encontra
conceitos abstratos antes da pessoa. Cada seção recarrega suas fontes e mantém
seletores próprios; selecionar alguém em “Usuários” não seleciona a mesma pessoa
em “Roles dos usuários”. O diagnóstico exibe nove colunas
(`pages/administracao.py:470-481`), e a permissão legada exige texto livre para
usuário e obra (`pages/administracao.py:524-572`).

### Problemas de UX por severidade

| Severidade | Achado | Evidência/impacto |
|---|---|---|
| **Crítico** | Estado “ativo” não significa “pode entrar” | pode levar à liberação equivocada de piloto; autenticação ignora o cadastro operacional |
| **Alto** | Jornada fragmentada em seis blocos | rolagem e seletores independentes elevam risco de administrar a pessoa errada |
| **Alto** | RBAC e permissão efetiva coexistem na mesma página | administrador pode confundir cálculo sombra com acesso real |
| **Alto** | Exclusão física de permissão sem confirmação | `pages/administracao.py:623-635` executa ao clique |
| **Alto** | Retirada de Role sem confirmação | botões adjacentes atribuem/retiram a Role selecionada (`399-409`) |
| **Médio** | E-mail sem explicação de finalidade | cria expectativa de convite não implementado |
| **Médio** | Termos técnicos expostos | `efeito`, `allow`, `recurso`, `SHA` implícito, Shadow Mode e Role vazia exigem conhecimento |
| **Médio** | Diagnóstico sem filtro por usuário/status | tabela completa e larga dificulta ação |
| **Médio** | Inativação misturada à edição cadastral | estado não é ação primária nem possui confirmação |
| **Médio** | Sucesso genérico | “Alteração salva” não resume pessoa, estado ou efeito (`services/usuarios_operacionais.py:125-129`) |
| **Baixo** | Auditoria dispersa | autoria e timestamps existem, mas não há linha do tempo única por usuário |
| **Melhoria** | Responsividade provável limitada | várias tabelas e colunas lado a lado exigem rolagem horizontal em celular; inferência do layout, não teste em dispositivo |

### Simulação conceitual dos fluxos

Contagem aproximada considera decisões explícitas, cliques de ação e seleção;
não conta digitação caractere a caractere.

| Fluxo | Passos atuais | Decisões/cliques aproximados | Confusão/risco | Melhoria |
|---|---|---:|---|---|
| A — criar | rolar após catálogo/Role; abrir expander; preencher 5 campos; escolher perfil; cadastrar | 7 decisões, 2 cliques + rolagem | e-mail parece convite; “perfil base” parece acesso | assistente por pessoa; explicar “cria cadastro inativo, sem credencial” |
| B — ativar | selecionar usuário na mesma seção; revisar campos; escolher `sim`; salvar | 3 decisões, 1 clique | ativo parece autenticável; sem confirmação | ação “Ativar cadastro” com impacto explícito |
| C — associar Role | rolar; selecionar novamente usuário; selecionar Role; atribuir | 3 decisões, 1 clique | risco de usuário divergente do selecionado acima | ficha persistente do usuário e resumo da Role |
| D — consultar | rolar ao diagnóstico; localizar linha e interpretar diferenças | 2 decisões + leitura | tabela larga; “RBAC a mais/menos” técnico | aba “Acesso calculado” com linguagem de módulos/tarefas |
| E — retirar | selecionar usuário/Role; clicar “Retirar” | 3 decisões, 1 clique | botão adjacente a atribuição; sem confirmação | confirmar pessoa, Role e ausência de efeito atual/futuro |
| F — inativar | voltar/rolar à seção de usuário; selecionar; mudar estado; salvar | 3 decisões, 1 clique | Role ativa pode permanecer no histórico; revogação de login não existe | comando único “Suspender usuário” com checklist |
| G — credencial | impossível | — | nenhuma ação, status ou orientação | área própria: configurar, resetar, exigir troca e revogar |

## 6. Visão do administrador não técnico

Hoje não há uma tela única que responda às nove perguntas desejadas:

| Pergunta | Resposta atual |
|---|---|
| Quem é? | dispersa entre tabela e seletores |
| Está ativa? | sim, mas “ativa” só vale no cadastro operacional |
| Pode entrar? | não aparece como estado próprio; hoje a resposta é “não” |
| Quais Roles? | histórico em seção separada |
| O que permitem? | tabela técnica por Role e diagnóstico |
| Em quais módulos trabalhará? | exige interpretar combinações módulo/recurso/ação |
| Há pendência? | não existe resumo; credencial não configurada aparece como valor cru |
| Última alteração? | timestamps em tabelas separadas |
| Quem alterou? | autoria existe, mas não há timeline consolidada |

O maior impedimento cognitivo é a ausência de uma entidade visual “Pessoa”. O
administrador trabalha com seis representações parciais do mesmo usuário.

## 7. Proposta de organização da Administração

Não alterar regras nesta etapa. A organização recomendada é:

### Administração → Identidade e Acesso

1. **Pessoas e acesso** — entrada principal; busca, estado e pendências.
2. **Detalhe do usuário** — cabeçalho persistente com nome/login/matrícula e
   quatro estados separados: cadastro, credencial, Roles e acesso efetivo.
3. **Funções (Roles)** — selecionar funções institucionais e mostrar em linguagem
   simples o que permitem.
4. **Acesso resultante** — atual × RBAC Shadow, com divergência explicada.
5. **Credenciais** — inicialmente mostrar “não implementado”; no futuro,
   configurar/resetar/exigir troca/revogar.
6. **Configuração avançada** — catálogo canônico, matriz, permissões legadas,
   IDs, efeitos e evidências.

### Fluxo principal orientado pelo usuário

`Selecionar pessoa → identidade → estado → Roles → acesso resultante → credencial`

### Ações e conteúdo

- **Primárias:** criar pessoa, ativar/suspender, atribuir/retirar Role, configurar
  credencial (futura).
- **Secundárias:** editar dados, ver histórico, comparar fontes.
- **Recolhido:** UUIDs, timestamps completos, códigos técnicos e permissões
  unitárias.
- **Modo avançado:** catálogo, matriz `allow`, permissões legadas e diagnóstico bruto.
- **Mensagens obrigatórias:** “cadastro não permite login”; “Role ainda não
  autoriza”; “nenhum e-mail foi enviado”; “ativar não cria credencial”; “esta
  ação afeta/não afeta acesso real”.
- **Confirmações:** suspender usuário, retirar Role, desativar permissão e,
  especialmente, excluir linha.

## 8. Segurança para o primeiro piloto

| Requisito | Estado | Justificativa |
|---|---|---|
| Autenticação operacional funcional | **inexistente** | login lê somente `APP_USERS` |
| Senha somente como hash | **inexistente** | comparação direta do secret atual |
| Primeiro acesso seguro | **inexistente** | sem token/convite |
| Reset administrativo | **inexistente** | sem serviço ou UI |
| Troca obrigatória | **inexistente** | marcador fixo sem comportamento |
| Inativação efetiva | **parcial** | cadastro/vínculo inativam; sessão/autenticação operacional não existem |
| Autorização por Role | **parcial** | cálculo existe; efeito não |
| Proteção antes da persistência | **parcial** | existe nos fluxos migrados; piloto deve validar cada ação do módulo escolhido |
| Logout | **já existe** | `services/auth.py:65-76` |
| Sessão com expiração | **já existe** | timeout deslizante de 1 hora, `79-105` |
| Trilha mínima de acesso | **parcial** | login/logout/expiração; não há auditoria completa de decisões |
| Escopo de dados | **parcial** | modelo legado tem obra; RBAC não; Prestação ainda exige decisão “próprias/equipe/obra/todas” |
| Usuário sem Role | **parcial** | Shadow classifica; não existe usuário operacional autenticável |
| Role vazia | **parcial** | Shadow classifica; não existe efeito autorizador |
| Revogação | **parcial** | logout/timeout existem; mudança em `APP_USERS` não revoga sessão imediatamente |

**Bloqueador crítico:** não liberar funcionário real antes de autenticação com
hash, primeiro acesso, reset/troca e revogação. **Bloqueador alto:** definir e
testar o escopo dos dados do primeiro módulo.

## 9. Plano de teste com funcionários-piloto

1. Escolher 1–2 usuários-piloto voluntários e um módulo completo.
2. Criar contas individuais; proibir senha compartilhada.
3. Usar menor privilégio e dados de teste ou subconjunto seguro.
4. Validar roteiro como administrador antes da liberação.
5. Avisar explicitamente quais funções estão incompletas.
6. Garantir suspensão/revogação imediata e responsável disponível.
7. Executar tarefas curtas acompanhadas, sem expor dados de terceiros.
8. Classificar cada ocorrência como UX, defeito funcional, autorização/segurança
   ou treinamento.
9. Revisar logs e remover o acesso ao término do ciclo.
10. Ampliar apenas após homologação explícita.

### Roteiro mínimo de feedback

- Tarefa tentada:
- Conseguiu concluir? (sim/parcial/não):
- Onde ficou em dúvida?:
- Mensagem recebida (copiar ou fotografar, sem dados pessoais):
- O que esperava acontecer?:
- Dificuldade (1–5):
- Dispositivo e navegador:
- Foi UX, erro funcional ou falta de orientação? (triagem do administrador):
- Sugestão livre:

## 10. Análise dos testes com hash fixo

Os três testes gravaram o SHA-256 de uma versão vazia de
`data/usuarios_operacionais.csv`:

- `tests/test_permissoes_catalogo_rbac002.py:146-156`;
- `tests/test_rbac_shadow_rbac006.py:130-140`;
- `tests/test_roles_permissoes_rbac004.py:120-131`.

Esse mecanismo demonstra que o checkout inteiro coincide com uma fotografia,
mas não demonstra que o serviço sob teste evitou mutação. Desde AUTH-001, o
arquivo é operacional e mutável por definição. Criação e ativação legítimas
alteram o hash sem alterar schema, autenticação, permissão efetiva ou Medições.

### Estado atual comprovado

- Não há correção na `main`: os commits após o baseline alteram somente dados.
- Compilação: aprovada.
- `unittest`: 644 executados, 641 aprovados e exatamente 3 falhas.
- `pytest`: 651 executados + 367 subtests; 648 aprovados e exatamente 3 falhas.
- Nas três falhas, valor esperado e atual divergem apenas para
  `data/usuarios_operacionais.csv`.

### Estratégia correta recomendada

1. Manter hashes apenas para artefatos realmente imutáveis relevantes ao teste,
   como código de autenticação, autoridade e Medições quando essa for a intenção.
2. Para `usuarios_operacionais.csv`, validar schema exato/colunas obrigatórias,
   unicidade de `usuario_id` e login, estados válidos e ausência de campos de
   credencial sensível.
3. Criar snapshot em memória antes da operação sob teste e compará-lo depois;
   mocks devem confirmar que funções de escrita não foram chamadas quando o
   serviço é somente leitura.
4. Para serviços que escrevem sua própria base, usar DataFrames sintéticos e
   confirmar explicitamente o caminho alvo, SHA observado e ausência de chamada
   para `usuarios_operacionais.csv`.
5. Não atualizar o hash para o valor atual: isso apenas adiaria a próxima falha.

**Missão recomendada:** `TEST-REG-001 — Remover hash fixo de base operacional`,
limitada aos três testes, sem alterar código funcional ou CSV.

### Por que os e-mails de falha aparentemente cessaram

O repositório comprova que os workflows são disparados por `push` na `main`
(`.github/workflows/testes.yml:3-10`; `.github/workflows/tests.yml:3-8`) e que a
suíte local continua falhando. O arquivo `testes.yml` também cancela execuções
anteriores concorrentes (`.github/workflows/testes.yml:15-17`). Porém, regras de
notificação por e-mail, agrupamento e supressão de alertas são configurações
externas do GitHub e não estão no repositório. Portanto, **não é possível concluir
que os testes voltaram a passar porque os e-mails cessaram**. A explicação pode
envolver cancelamento, agrupamento ou preferências de notificação, mas isso não
foi verificado e não deve ser tratado como fato.

## 11. Roadmap recomendado em Baby Steps

1. **TEST-REG-001 — testes de base mutável.** Corrigir somente os três testes e
   restaurar CI verde.
2. **UX-ACESSO-001 — organização orientada pela pessoa.** Reorganizar a página,
   sem mudar regras, dados ou autorização.
3. **AUTH-002 — fundação de credenciais.** Definir armazenamento com hash,
   integração do usuário operacional ao login, primeiro acesso seguro e estado
   de credencial. Não enviar senha por e-mail.
4. **AUTH-003 — ciclo administrativo.** Reset, troca obrigatória, revogação,
   inativação efetiva e auditoria mínima.
5. **RBAC-007 — homologação individual.** Resolver curingas, escopo de dados e
   divergências do Shadow Mode para um usuário e um módulo.
6. **RBAC-008 — ativação controlada.** Fazer a autoridade central consumir RBAC
   por feature flag/escopo homologado, com retorno seguro à negação.
7. **PILOTO-001 — Prestação de Contas.** Um ou dois funcionários, criação de
   despesa, dados próprios, roteiro e revogação testada.

Essa ordem prioriza restaurar confiança no CI, reduzir erro administrativo,
criar identidade autenticável segura e somente depois ativar autorização.

## 12. Itens que exigem decisão humana

1. Qual será o primeiro módulo e quais dados o piloto poderá visualizar?
2. Em Prestação de Contas, “visualizar” significa próprias, equipe, obra ou todas?
3. Qual canal entregará o primeiro acesso sem transmitir senha em claro?
4. Quem poderá resetar, suspender e reativar credenciais?
5. Haverá ambiente separado ou dados de teste identificados na produção?
6. Qual tempo absoluto de sessão e qual requisito de revogação imediata?
7. Quais eventos precisam de trilha: login, falha, reset, troca, Role, decisão e
   leitura de dados sensíveis?
8. Quando uma divergência Shadow estará homologada para ativação?
9. A permissão legada será migrada, congelada ou mantida temporariamente?
10. A exclusão física de permissões continuará disponível?

## 13. Limitações e riscos residuais da auditoria

- A auditoria inspecionou código e dados versionados, sem ler valores de Secrets.
- Não foi enviado e-mail, criada credencial ou alterado usuário.
- A avaliação mobile é inferida da composição Streamlit; não houve teste em
  aparelho físico.
- O comportamento de notificações por e-mail do GitHub não é verificável pelo
  repositório.
- A auditoria não prova confidencialidade de dados em um piloto; isso depende do
  módulo escolhido e de teste específico de escopo.
- Enquanto RBAC e permissão legada coexistirem, a interface continuará sujeita a
  ambiguidade mesmo que a separação técnica permaneça correta.
