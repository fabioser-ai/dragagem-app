# APP FOS — ARCHITECTURE CURRENT

Status:
Em construção.

Última atualização:
2026-07-08

---

# Objetivo

Este documento descreve como o APP FOS funciona atualmente.

Ele documenta apenas fatos observados no código.

Ele NÃO tenta explicar os motivos históricos das decisões.

Quando um motivo histórico for confirmado pelo Fabio, ele será registrado posteriormente em um ADR (Architecture Decision Record).

---

# Organização deste documento

1. Visão Geral
2. Inicialização
3. Autenticação
4. Interface
5. Persistência
6. Permissões
7. Módulos
8. Fluxos
9. Observações Técnicas
10. Perguntas em Aberto


# 1. Visão Geral

O APP FOS é uma aplicação desenvolvida em Streamlit.

A navegação é controlada através de `st.session_state.tela`.

O ponto de entrada principal é `app.py`.

Fluxo simplificado:

Usuário
↓

Login

↓

Aplicação do estilo visual

↓

Menu Principal

↓

Módulo selecionado

↓

Leitura e gravação de dados em arquivos CSV armazenados no GitHub.


# 2. Inicialização

Responsável:

app.py

Responsabilidades observadas:

- Configurar a página Streamlit.
- Executar autenticação.
- Aplicar estilo visual global.
- Inicializar a tela principal.
- Controlar o roteamento entre módulos.
- Aplicar restrições por perfil.

Observação:

O aplicativo utiliza `st.session_state.tela` como mecanismo central de navegação.

# 3. Autenticação

Arquivo principal:

services/auth.py

Funcionamento observado:

- Usuários são carregados através de APP_USERS em st.secrets.
- A sessão armazena:
    - usuário
    - nome
    - perfil
    - matrícula
    - último acesso
- Existe timeout de sessão.
- Eventos importantes geram registro em log.

Observação:

As senhas atualmente são comparadas diretamente com os valores armazenados em APP_USERS.

Motivo histórico:

DESCONHECIDO.


# 4. Interface

Arquivo principal:

services/ui.py

Responsabilidade:

Aplicar CSS global ao Streamlit.

Características observadas:

- Tema claro.
- Correção de contraste.
- Ajustes de botões.
- Ajustes de tabelas.
- Ajustes para melhor legibilidade.

Motivo histórico provável:

Melhorar a experiência de uso em dispositivos móveis.

Status:

A confirmar.
