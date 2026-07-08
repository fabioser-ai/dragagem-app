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



# 5. Persistência

## Visão Geral

O APP FOS utiliza arquivos CSV armazenados diretamente no repositório GitHub como mecanismo principal de persistência.

O GitHub atua como repositório de dados da aplicação.

Não existe atualmente um banco de dados relacional.

---

## Serviço responsável

Arquivo:

services/github.py

Este serviço centraliza toda comunicação entre o aplicativo e o GitHub.

Toda leitura e gravação de dados deve passar por esse serviço.

---

## Operações principais

Foram identificadas as seguintes responsabilidades:

- carregar arquivos CSV
- salvar arquivos CSV
- carregar arquivos binários
- salvar arquivos binários

O restante do sistema normalmente não acessa a API do GitHub diretamente.

---

## Estrutura dos dados

Os módulos armazenam seus dados em arquivos CSV.

Exemplos:

data/orcamentos.csv

data/permissoes_usuarios.csv

data/log_acessos.csv

data/crm/

data/medicoes/

Cada módulo é responsável apenas pelo conteúdo de seus próprios arquivos.

---

## Funcionamento

Fluxo simplificado:

Tela

↓

DataFrame (pandas)

↓

services/github.py

↓

GitHub

↓

Arquivo CSV

---

## Vantagens observadas

Arquitetura simples.

Baixo custo operacional.

Deploy simples utilizando Streamlit Cloud.

Versionamento automático através do GitHub.

Facilidade para backup.

Estrutura facilmente compreendida.

---

## Limitações observadas

Não existe controle transacional.

Gravações simultâneas podem gerar conflitos.

Arquivos CSV tendem a crescer continuamente.

Não existe mecanismo de locking.

---

## Motivo histórico

DESCONHECIDO.

Hipótese:

A arquitetura foi escolhida para manter simplicidade operacional durante o desenvolvimento inicial.

Status:

A confirmar.


# 9. Observações Técnicas
