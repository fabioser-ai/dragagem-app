# Auditoria Arquitetural — Serviços Compartilhados

Data: 2026-07-11

## Status

- Auditoria concluída.
- Nenhum comportamento funcional foi alterado.
- Consolidação prevista em `docs/architecture/12_SERVICOS_COMPARTILHADOS.md`.

## Escopo auditado

- autenticação e sessão;
- autorização geral;
- persistência CSV e binária no GitHub;
- registro de logs;
- estilo visual global;
- tratamento de erros;
- concorrência e consistência;
- dependências entre infraestrutura e módulos.

## Componentes diretamente envolvidos

- `services/auth.py`
- `services/permissoes.py`
- `services/github.py`
- `services/log.py`
- `services/ui.py`
- `app.py`
- `data/log_acessos.csv`
- `data/permissoes_usuarios.csv`
- `APP_USERS` em `st.secrets`

## 1. O que foi aprendido

### 1.1 Autenticação e sessão

`services/auth.py` carrega `APP_USERS` de `st.secrets`, compara a senha diretamente com o valor armazenado e grava em `st.session_state` o usuário, perfil, matrícula, nome e último acesso.

A sessão expira após uma hora de inatividade. Cada chamada a `sessao_expirada()` renova `ultimo_acesso` quando o prazo ainda não foi atingido.

O logout registra um evento quando possível, limpa chaves específicas da sessão e executa `st.rerun()`.

Falhas ao carregar `APP_USERS` retornam `{}`. Falhas ao registrar logs de login, logout ou expiração são silenciadas para não bloquear o fluxo principal.

### 1.2 Permissões

`services/permissoes.py` centraliza a autorização geral sobre `data/permissoes_usuarios.csv`.

O serviço oferece:

- `eh_superadmin()`;
- `permissoes_usuario()`;
- `pode_acessar_modulo()`;
- `pode_executar()`;
- `obras_permitidas()`.

O perfil global `superadmin` recebe acesso direto. Os demais usuários dependem de linhas ativas no CSV.

A camada de leitura captura qualquer exceção e retorna um DataFrame vazio. Portanto, erro de rede, autenticação, arquivo inexistente e arquivo realmente vazio podem convergir para o mesmo resultado.

### 1.3 Persistência no GitHub

`services/github.py` implementa quatro operações:

- leitura de CSV;
- gravação de CSV;
- leitura de arquivos binários;
- gravação de arquivos binários.

Todas usam chamadas HTTP síncronas para a GitHub Contents API.

A gravação busca primeiro o SHA atual e depois executa um `PUT`. O arquivo inteiro é substituído. Não existe locking, transação, retry, timeout explícito, controle de versão otimista além do SHA obtido imediatamente antes da escrita ou tratamento específico para conflito `409`.

A leitura de CSV retorna DataFrame vazio para qualquer status diferente de 200 e também quando o campo `content` não existe.

A leitura binária retorna `None` para status diferente de 200. Quando existe `download_url`, executa uma segunda requisição; em caso de falha, tenta o conteúdo base64 retornado pela API.

Nenhuma chamada `requests.get()` ou `requests.put()` define timeout explícito.

### 1.4 Logs

`services/log.py` mantém um log append-only lógico em `data/log_acessos.csv`, com:

- data e hora;
- usuário;
- perfil;
- ação.

Cada evento relê o CSV inteiro, concatena uma linha e regrava o arquivo completo.

Se a leitura gerar exceção ou retornar vazio, o serviço cria um DataFrame novo. Se a situação for uma falha transitória mascarada como vazio, a gravação seguinte pode substituir o histórico anterior apenas pelo novo evento.

Não existe identificador único, origem técnica, severidade, detalhes do erro ou política de retenção.

### 1.5 Interface global

`services/ui.py` possui uma única função, `aplicar_estilo_global()`, que injeta CSS diretamente por `st.markdown(..., unsafe_allow_html=True)`.

O CSS define tema claro, contraste, sidebar, botões, campos, seletores, tabelas, métricas, expanders, tabs e espaçamento principal.

Os seletores dependem de atributos internos e `data-testid` do Streamlit/BaseWeb. Alterações internas dessas bibliotecas podem reduzir ou quebrar a aplicação do estilo sem erro de Python.

### 1.6 Acoplamento observado

Os serviços compartilhados dependem diretamente de `st.secrets` e `st.session_state`. Isso os torna simples para uso dentro do Streamlit, mas dificulta testes isolados e reutilização fora do runtime da aplicação.

`services/auth.py` depende de `services.log.py`, que depende de `services.github.py`. Assim, autenticação possui dependência indireta da persistência no GitHub, embora as exceções de log sejam silenciadas no fluxo de autenticação.

Módulos diferentes adicionam wrappers próprios sobre `services/github.py`, com políticas diferentes de normalização e erro.

## 2. O que ainda não foi compreendido

- Qual disponibilidade e latência são aceitáveis para a aplicação?
- Falhas de leitura devem bloquear operações de escrita em todos os módulos?
- Existe intenção de manter o GitHub como persistência definitiva ou apenas durante a fase atual?
- Quais eventos precisam de auditoria obrigatória e quais podem ser descartados em caso de falha?
- Senhas em `APP_USERS` devem permanecer em texto comparável ou existe plano de hash/provedor externo?
- O CSS global deve continuar dependente de seletores internos do Streamlit?
- Existe necessidade de testes automatizados para serviços compartilhados?

## 3. O que deve ser documentado

### Observações técnicas propostas

- OT-045 — Leituras de CSV não distinguem ausência, falha HTTP e arquivo vazio.
- OT-046 — Gravações substituem arquivos inteiros e não possuem locking.
- OT-047 — Chamadas HTTP não definem timeout nem retry.
- OT-048 — Logging relê e regrava todo o histórico a cada evento.
- OT-049 — Falha transitória de leitura pode causar sobrescrita destrutiva posterior.
- OT-050 — Serviços dependem diretamente do runtime Streamlit.
- OT-051 — Wrappers de persistência por módulo possuem políticas diferentes.
- OT-052 — Autenticação compara senhas diretamente com `APP_USERS`.
- OT-053 — Logs de autenticação são best-effort e podem ser descartados silenciosamente.
- OT-054 — CSS global depende de seletores internos do Streamlit/BaseWeb.

### Perguntas em aberto propostas

- PA-036 — Política oficial de erros de leitura e bloqueio de escrita.
- PA-037 — Estratégia de concorrência e conflitos de gravação.
- PA-038 — Timeouts, retries e observabilidade das chamadas GitHub.
- PA-039 — Política de segurança de credenciais.
- PA-040 — Requisitos de auditoria e retenção de logs.
- PA-041 — Limites da dependência direta de Streamlit nos serviços.
- PA-042 — Estratégia futura de persistência.
- PA-043 — Estabilidade e testes do CSS global.

## 4. Baby step seguro

O primeiro baby step futuro deve ser criar um resultado explícito de leitura no serviço de persistência, distinguindo pelo menos:

- sucesso com dados;
- sucesso com arquivo vazio;
- arquivo inexistente;
- falha de autenticação;
- falha temporária de rede/API;
- conteúdo inválido.

As telas de escrita devem ser bloqueadas quando a leitura anterior não tiver sido confirmada como válida.

Esse passo reduz o risco transversal mais grave sem exigir migração imediata de banco de dados ou refatoração ampla.
