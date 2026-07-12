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

A tela Administração já usa o contrato explícito de leitura e escrita. Os adaptadores legados permanecem disponíveis para consumidores ainda não migrados.

## Persistência no GitHub

`services/github.py` implementa contratos explícitos e adaptadores legados.

### Contrato explícito de leitura

- `StatusLeitura`;
- `ResultadoLeituraCSV`;
- `ler_csv_github()`.

A leitura distingue sucesso com dados, sucesso vazio, arquivo inexistente, autorização, conflito ou limite, falha temporária, conteúdo inválido e erro desconhecido.

### Contrato explícito de escrita

- `StatusEscrita`;
- `ResultadoEscritaCSV`;
- `salvar_csv_github()`.

Atualizações exigem o SHA observado na leitura confirmada. Criações exigem autorização explícita do chamador. A escrita estruturada não executa GET para descobrir uma versão mais recente antes do PUT.

### Adaptadores legados

- `salvar_github()`;
- `carregar_github()`;
- `salvar_arquivo_github()`;
- `carregar_arquivo_github()`.

Os adaptadores legados continuam disponíveis durante a migração gradual, mas não devem ser adotados por novos fluxos que regravam CSV após leitura possivelmente ambígua.

### Arquivos binários

A gravação binária ainda segue o padrão legado de obtenção de SHA e substituição integral.

A leitura tenta primeiro `download_url` e, se necessário, usa o conteúdo base64 retornado pela API.

### Limitações ainda observadas

- não existe transação entre múltiplos arquivos;
- não existe retry central;
- os adaptadores legados ainda não classificam erros;
- arquivos binários ainda usam a política legada;
- parte dos consumidores de CSV ainda não foi migrada;
- gravações concorrentes nos consumidores legados ainda podem sobrescrever alterações.

## Logging

`services/log.py` registra eventos em `data/log_acessos.csv`.

Schema preservado:

- `data_hora`;
- `usuario`;
- `perfil`;
- `acao`.

Eventos observados nos chamadores diretos:

- login;
- logout;
- sessão expirada.

O fluxo foi migrado para o contrato explícito:

1. lê o log com `ler_csv_github()`;
2. em sucesso com dados ou vazio, concatena o evento;
3. atualiza com `salvar_csv_github()` usando o SHA da leitura;
4. em `ARQUIVO_INEXISTENTE`, cria explicitamente o arquivo com `criar=True`;
5. em qualquer outra falha de leitura, não executa escrita.

Os chamadores em `services/auth.py` continuam envolvendo o registro em `try/except`, portanto falhas do log não bloqueiam login, logout ou expiração da sessão.

A migração não alterou:

- schema;
- formato de data e hora;
- ações registradas;
- autenticação;
- política de retenção;
- ausência de identificador próprio do evento.

A validação local confirmou:

- 25 testes unitários aprovados;
- compilação sintática de `services/log.py` e `services/auth.py`;
- inspeção dos três chamadores diretos;
- nenhum arquivo rastreado relacionado à migração alterado durante os testes.

O workspace do Work apresentou um comprovante binário já modificado e não relacionado à migração. Esse arquivo não pertence aos commits de logs e não foi alterado nem publicado por esta etapa.

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

Esse desenho simplifica o uso dentro da aplicação Streamlit, mas acopla infraestrutura ao runtime da interface.

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

O principal risco compartilhado era a combinação de leitura ambígua e substituição integral do arquivo. Administração e logs já foram migrados para bloquear escrita após leitura não confirmada e usar o SHA observado.

O risco permanece nos consumidores ainda legados.

## Direção segura de evolução

Prosseguir um consumidor por vez, preservando schema e comportamento funcional:

1. Administração — concluída;
2. logs — concluída;
3. Dados;
4. Férias;
5. CRM;
6. Prestação de Contas;
7. Orçamentos;
8. Medições.

Consultas somente leitura devem ser migradas depois dos fluxos de escrita para deixarem de apresentar falha como ausência legítima de dados.
