# Arquitetura Atual — Serviços Compartilhados

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_038_SERVICOS_COMPARTILHADOS.md`

## Visão geral

A infraestrutura compartilhada do APP FOS está concentrada principalmente em:

- `services/auth.py`;
- `services/permissoes.py`;
- `services/github.py`;
- `services/log.py`;
- `services/ui.py`.

Esses serviços fornecem autenticação, sessão, autorização, persistência no GitHub, logging e estilo visual global.

## Autenticação e sessão

`services/auth.py` carrega as contas de `APP_USERS` em `st.secrets`.

A sessão armazena:

- usuário;
- perfil;
- matrícula;
- nome;
- último acesso;
- estado de autenticação.

A senha informada é comparada diretamente com o valor armazenado em `APP_USERS`.

A sessão possui timeout de uma hora. O logout tenta registrar o evento, limpa chaves específicas de `st.session_state` e executa `st.rerun()`.

Falhas no logging de autenticação são silenciadas para não impedir login, logout ou expiração da sessão.

## Permissões

`services/permissoes.py` lê e grava `data/permissoes_usuarios.csv` por meio de `services/github.py`.

Funções principais:

- `eh_superadmin()`;
- `permissoes_usuario()`;
- `pode_acessar_modulo()`;
- `pode_executar()`;
- `obras_permitidas()`.

O perfil global `superadmin` recebe acesso direto. Os demais usuários dependem de permissões ativas no CSV.

A leitura de permissões captura exceções e retorna DataFrame vazio. O chamador não consegue distinguir, apenas pelo retorno, um arquivo realmente vazio de falhas de rede, autenticação, inexistência ou leitura.

## Persistência no GitHub

`services/github.py` implementa:

- `salvar_github()`;
- `carregar_github()`;
- `salvar_arquivo_github()`;
- `carregar_arquivo_github()`.

As operações usam a GitHub Contents API com chamadas HTTP síncronas.

### Leitura CSV

- Executa `GET` autenticado.
- Retorna DataFrame vazio quando o status não é 200.
- Retorna DataFrame vazio quando o campo `content` não existe.
- Decodifica base64 e usa `pandas.read_csv()` quando o conteúdo está presente.

### Gravação CSV

- Executa `GET` para obter o SHA atual.
- Serializa o DataFrame inteiro.
- Executa `PUT` substituindo o arquivo completo.
- Lança exceção quando o status não é 200 ou 201.

### Arquivos binários

A gravação segue o mesmo padrão de obtenção de SHA e substituição integral.

A leitura tenta primeiro `download_url` e, se necessário, usa o conteúdo base64 retornado pela API.

### Limitações observadas

- não existe locking;
- não existe transação;
- não existe retry central;
- não existe timeout HTTP explícito;
- não existe classificação estruturada de erros;
- gravações concorrentes podem conflitar;
- uma leitura mascarada como vazia pode preceder uma sobrescrita destrutiva.

## Logging

`services/log.py` registra eventos em `data/log_acessos.csv`.

Schema observado:

- `data_hora`;
- `usuario`;
- `perfil`;
- `acao`.

Cada evento:

1. relê o arquivo inteiro;
2. concatena uma linha;
3. regrava o arquivo completo.

Uma falha de leitura pode ser interpretada como log vazio. A gravação posterior pode substituir o histórico existente pelo novo evento.

Não existe identificador do evento, severidade, detalhes técnicos ou política de retenção.

## Interface global

`services/ui.py` injeta CSS global com `st.markdown(..., unsafe_allow_html=True)`.

O estilo cobre:

- tema claro;
- contraste;
- sidebar;
- botões;
- inputs e seletores;
- tabelas e DataFrames;
- métricas;
- expanders;
- tabs;
- espaçamento da página.

Parte do CSS depende de `data-testid` e atributos internos do Streamlit/BaseWeb. Mudanças nessas bibliotecas podem alterar o resultado visual sem gerar erro de execução Python.

## Acoplamento

Os serviços acessam diretamente `st.secrets` e `st.session_state`.

Esse desenho simplifica o uso dentro da aplicação Streamlit, mas acopla infraestrutura ao runtime da interface e dificulta testes unitários isolados.

A cadeia observada inclui:

```text
auth
  ↓
log
  ↓
github
```

Módulos adicionais criam wrappers próprios sobre `services/github.py`, com schemas, normalizações e políticas de erro diferentes.

## Risco transversal principal

O principal risco compartilhado é a combinação de:

1. leitura que converte falhas em vazio;
2. gravação que substitui o arquivo inteiro.

Essa combinação pode transformar uma falha transitória de leitura em perda de dados na escrita seguinte.

## Direção segura de evolução

O primeiro passo recomendado é fazer a camada de persistência devolver estados explícitos de leitura, distinguindo:

- sucesso com dados;
- sucesso com arquivo vazio;
- arquivo inexistente;
- falha de autenticação;
- falha temporária de rede/API;
- conteúdo inválido.

Operações de escrita devem ser bloqueadas quando a leitura anterior não tiver sido confirmada como válida.
