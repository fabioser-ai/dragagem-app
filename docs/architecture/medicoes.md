# APP FOS — Arquitetura do Módulo Medições

Status:
Em construção.

Última atualização:
2026-07-08

---

# Objetivo

Documentar a arquitetura observada do módulo Medições do APP FOS.

Este documento registra fatos observados no código e na documentação oficial existente.

Hipóteses devem permanecer explicitamente identificadas como hipóteses.

---

# 1. Visão geral

O módulo Medições é acessado a partir do menu principal do APP FOS e possui navegação interna própria.

O fluxo principal é iniciado por `pages/medicoes.py` e delegado para `modulos/medicoes/navegacao.py`.

Fluxos internos observados:

- `inicio`
- `gestao`
- `lancamento`
- `aprovacao`

Arquivos principais observados:

- `pages/medicoes.py`
- `modulos/medicoes/navegacao.py`
- `modulos/medicoes/permissoes.py`
- `modulos/medicoes/config.py`
- `modulos/medicoes/repositorio.py`
- `modulos/medicoes/lancamentos/repositorio.py`
- `modulos/medicoes/lancamentos/servicos.py`
- `modulos/medicoes/lancamentos/tela_lancar.py`

---

# 2. Dados e arquivos usados

Arquivos de dados observados no módulo Medições:

- `data/obras.csv`
- `data/medicoes/medicoes.csv`
- `data/medicoes/medicao.csv`
- `data/medicoes/frentes.csv`
- `data/medicoes/mc.csv`
- `data/medicoes/itens.csv`
- `data/medicoes/servicos.csv`
- `data/medicoes_tabelas/`
- `data/medicoes/locais_trabalho.csv`
- `data/medicoes/lancamentos_trabalho.csv`
- `data/medicoes/usuarios_obras.csv`

Observação:

`data/obras.csv` é um cadastro geral consumido diretamente pelo módulo Medições.

---

# 3. Permissões internas de Medições

O módulo Medições possui camada própria de permissão baseada em `data/medicoes/usuarios_obras.csv`.

Colunas esperadas:

- `usuario_id`
- `email`
- `nome`
- `obra_id`
- `perfil_medicao`
- `ativo`

Perfis observados:

- `funcionario`
- `encarregado`
- `aprovador`
- `admin`

Hierarquia observada:

`admin > aprovador > encarregado > funcionario`

Permissões internas observadas:

- `funcionario`, `encarregado`, `aprovador` e `admin` podem lançar trabalho.
- `encarregado`, `aprovador` e `admin` podem visualizar lançamentos.
- `aprovador` e `admin` podem aprovar lançamentos.
- Apenas `admin` pode criar ou gerenciar medição.

Observação:

O perfil `admin` de Medições é específico do módulo Medições e não equivale automaticamente ao perfil global `superadmin` do aplicativo.

---

# 4. Repositórios de Medições

## 4.1 Repositório geral

Arquivo:

`modulos/medicoes/repositorio.py`

Responsabilidades observadas:

- Definir wrappers genéricos `carregar_csv()` e `salvar_csv()` sobre `services/github.py`.
- Carregar bases principais do fluxo de gestão de Medições.
- Carregar vínculos de usuários com obras.
- Carregar tabela contratual por obra.
- Carregar e salvar locais de trabalho.
- Carregar lançamentos de produção.
- Salvar fotos de lançamentos.
- Manter temporariamente função legada de salvamento de lançamento de produção.

Observação importante:

O próprio arquivo marca `salvar_lancamento_producao()` como legado e orienta que o fluxo oficial atual deve usar `modulos.medicoes.lancamentos.servicos.criar_lancamento_trabalho`.

## 4.2 Repositório de lançamentos

Arquivo:

`modulos/medicoes/lancamentos/repositorio.py`

Responsabilidades observadas:

- Definir wrappers próprios `carregar_csv()` e `salvar_csv()` sobre `services/github.py`.
- Carregar e salvar lançamentos de trabalho.
- Carregar e salvar locais de trabalho.
- Listar locais ativos por obra.
- Buscar local por ID.
- Criar local de trabalho.
- Carregar e salvar vínculos de usuários com obras.

Uso observado:

`modulos/medicoes/lancamentos/servicos.py` usa `carregar_lancamentos_trabalho()` e `salvar_lancamentos_trabalho()` para criar, listar, aprovar e vincular lançamentos.

## 4.3 Sobreposição observada

Foi observada sobreposição entre o repositório geral de Medições e o repositório específico de lançamentos.

Arquivos acessados por ambos:

- `data/medicoes/locais_trabalho.csv`
- `data/medicoes/usuarios_obras.csv`
- `data/medicoes/lancamentos_trabalho.csv`

Interpretação operacional documentada:

- O repositório geral atende o fluxo de gestão e mantém compatibilidade com partes legadas.
- O repositório de lançamentos atende o fluxo operacional atual de lançamento de trabalho executado.

Não consolidar esses repositórios sem auditoria completa dos fluxos que ainda dependem de cada um.

---

# 5. Navegação interna

Arquivo:

`modulos/medicoes/navegacao.py`

Responsabilidades observadas:

- Definir labels visuais das etapas de medição.
- Resolver etapas disponíveis conforme modelo de medição.
- Renderizar tela inicial do módulo Medições.
- Definir opções disponíveis conforme permissões internas.
- Direcionar para fluxo de gestão.
- Direcionar para fluxo de lançamento.
- Direcionar para fluxo de aprovação.
- Proteger cada fluxo contra acesso indevido.
- Controlar avanço e retorno entre etapas da gestão.

---

# 6. Fluxo operacional de Lançamentos

Função auditada:

`tela_lancar_producao()`

Arquivo:

`modulos/medicoes/lancamentos/tela_lancar.py`

## 6.1 Entrada do fluxo

O fluxo de lançamento é acessado quando `st.session_state["fluxo_medicoes"] == "lancamento"`.

Antes da tela ser chamada, `navegacao_lancamento()` verifica `pode_lancar_trabalho()`.

Se a permissão for negada:

- exibe aviso;
- redefine `fluxo_medicoes` para `inicio`;
- interrompe o fluxo.

Se a permissão for aceita:

- chama `tela_lancar_producao()`.

## 6.2 Responsabilidades observadas da tela

`tela_lancar_producao()`:

- Exibe a tela de lançamento de trabalho executado.
- Permite voltar ao início das Medições.
- Carrega bases do módulo usando `carregar_bases()`.
- Filtra obras disponíveis conforme usuário logado.
- Exibe usuário e perfil interno de Medições identificados.
- Seleciona automaticamente a obra quando há apenas uma obra disponível.
- Permite seleção manual quando há mais de uma obra disponível.
- Informa que o lançamento será salvo como evidência operacional independente.
- Exige seleção de local de trabalho cadastrado.
- Exige tabela contratual vinculada à obra.
- Carrega tabela contratual da obra com `carregar_tabela_contrato()`.
- Filtra serviços ativos quando a coluna `ativo` existe.
- Permite selecionar o item contratual executado.
- Coleta quantidade executada.
- Coleta data do serviço.
- Coleta observação opcional.
- Aceita upload de foto comprobatória.
- Valida local de trabalho antes de salvar.
- Valida quantidade maior que zero antes de salvar.
- Salva o lançamento usando `criar_lancamento_trabalho()`.

## 6.3 Identificação do usuário

A tela tenta identificar o usuário logado por múltiplas chaves em `st.session_state`:

- `email`
- `usuario_email`
- `user_email`
- `usuario_logado`
- `usuario`
- `login`

Se o valor encontrado for dicionário, tenta extrair:

- `email`
- `usuario`
- `login`

Se nenhum usuário for identificado, o fluxo exibe aviso e nenhuma obra é liberada para lançamento.

## 6.4 Filtro de obras por usuário

A tela usa `carregar_usuarios_obras()` do repositório de lançamentos para carregar vínculos entre usuários e obras.

O vínculo é considerado quando:

- `usuario_id`, `email` ou `nome` corresponde ao usuário logado;
- `ativo` está em um dos valores aceitos como ativo.

Valores aceitos como ativo:

- `sim`
- `s`
- `true`
- `1`
- `ativo`

Se o perfil interno for `admin` ou `aprovador`, todas as obras são liberadas para seleção.

Para demais perfis, a tela filtra `obras.csv` pelos `obra_id` vinculados ao usuário.

## 6.5 Local de trabalho

A seleção de local de trabalho é feita por `_selecionar_local_trabalho(obra_id)`.

A função usa `listar_locais_por_obra(obra_id)`.

Se não houver local cadastrado para a obra, a tela exibe aviso e retorna local vazio.

Na tentativa de salvar, se `nome_local` estiver vazio, a tela exibe erro e não chama o serviço de criação do lançamento.

## 6.6 Item contratual

A tela lê `arquivo_tabela_servicos` da obra selecionada.

Se a obra não possuir tabela contratual vinculada, exibe aviso e interrompe o fluxo.

Se a tabela contratual estiver vazia ou não for encontrada, exibe aviso e interrompe o fluxo.

Se houver coluna `ativo`, a tela mantém apenas registros cujo valor seja aceito como ativo.

Valores aceitos como ativo em serviços:

- `sim`
- `s`
- `true`
- `1`
- `ativo`
- vazio

O item selecionado fornece:

- `codigo_item`
- `descricao_item`
- `unidade`
- `item_id`, definido como o próprio `codigo_item`

## 6.7 Foto comprobatória

A tela aceita upload de arquivos:

- `png`
- `jpg`
- `jpeg`

Comportamento observado:

- A foto carregada não é persistida como arquivo binário neste fluxo.
- Quando há foto, a tela exibe mensagem indicando que a foto foi carregada na tela e que o próximo passo seria salvar o arquivo no GitHub.
- O valor salvo em `foto_url` é apenas `foto.name`.

Não alterar esse comportamento sem decisão explícita, pois pode existir motivo histórico ainda não documentado.

## 6.8 Salvamento do lançamento

O salvamento é feito por:

`criar_lancamento_trabalho()`

Arquivo:

`modulos/medicoes/lancamentos/servicos.py`

O serviço:

- carrega `data/medicoes/lancamentos_trabalho.csv`;
- cria novo registro com `lancamento_id` gerado por `novo_id("LAN")`;
- adiciona campos operacionais do lançamento;
- define status iniciais;
- concatena o novo registro ao DataFrame existente;
- salva o CSV inteiro de volta via `salvar_lancamentos_trabalho()`;
- retorna o dicionário do novo lançamento.

Status inicial observado:

- `status_aprovacao = pendente`
- `status_medicao = nao_medido`
- `medicao_id_vinculada = ""`

Conclusão arquitetural:

O lançamento nasce como evidência operacional independente, ainda não vinculada a uma medição.

## 6.9 Campos persistidos em lançamentos

Colunas observadas para `data/medicoes/lancamentos_trabalho.csv`:

- `lancamento_id`
- `obra_id`
- `nome_obra`
- `local_id`
- `nome_local`
- `item_id`
- `codigo_item`
- `descricao_item`
- `unidade`
- `quantidade_executada`
- `data_servico`
- `observacao`
- `foto_url`
- `status_aprovacao`
- `aprovado_por`
- `aprovado_em`
- `status_medicao`
- `medicao_id_vinculada`
- `criado_por`
- `criado_em`
- `atualizado_em`

---

# 7. Observações Técnicas

## OT-MED-001 — Sobreposição entre repositórios de Medições

O módulo Medições possui um repositório geral e um repositório específico de lançamentos.

Ambos acessam parte dos mesmos arquivos de dados, especialmente locais de trabalho, vínculos de usuários com obras e lançamentos de trabalho.

Essa sobreposição parece refletir a coexistência entre fluxo de gestão, fluxo operacional atual e compatibilidade temporária com código legado.

Não consolidar esses repositórios sem auditoria completa dos fluxos que ainda dependem de cada um.

## OT-MED-002 — Fluxo de lançamento usa serviço atual, não salvamento legado

`tela_lancar_producao()` salva novos lançamentos através de `criar_lancamento_trabalho()`.

Não foi observado uso de `salvar_lancamento_producao()` dentro de `tela_lancar_producao()`.

Isso reforça a separação entre fluxo operacional atual e função legada ainda existente no repositório geral.

## OT-MED-003 — Foto do lançamento não é persistida como binário neste fluxo

`tela_lancar_producao()` aceita upload de foto, mas o comportamento observado é salvar apenas o nome do arquivo em `foto_url`.

A tela informa que o próximo passo seria salvar o arquivo no GitHub.

Não implementar persistência de foto durante a auditoria sem decisão explícita.

## OT-MED-004 — Lançamento nasce independente da medição

O lançamento criado por `criar_lancamento_trabalho()` nasce com `status_aprovacao = pendente`, `status_medicao = nao_medido` e `medicao_id_vinculada` vazio.

Isso confirma que o registro é uma evidência operacional antes de ser vinculado a uma medição.

---

# 8. Perguntas em Aberto

## PA-MED-001 — Fronteira futura entre repositório geral e repositório de lançamentos

Confirmar se a sobreposição entre `modulos/medicoes/repositorio.py` e `modulos/medicoes/lancamentos/repositorio.py` deve permanecer como separação de contexto ou se, futuramente, deverá ser consolidada.

Nenhuma consolidação deve ser feita antes da auditoria completa dos fluxos de Medições.

## PA-MED-002 — Persistência futura da foto de lançamento

Confirmar se o comportamento atual de salvar apenas `foto.name` em `foto_url` é temporário, intencional ou pendente de implementação futura.

Não tratar como bug sem confirmação.

## PA-MED-003 — Auditoria interna do fluxo de aprovação

Auditar separadamente `tela_aprovar_lancamentos()`.

Essa tela é chamada pelo fluxo principal de Medições, mas seus detalhes internos ainda não foram documentados neste arquivo modular.

---

# 9. Resultado da auditoria atual

## O que foi aprendido?

O fluxo operacional de lançamento está compreendido em nível arquitetural suficiente para documentação inicial.

Ele filtra obras por usuário, exige local de trabalho e tabela contratual, coleta dados operacionais e cria lançamento independente por meio de `criar_lancamento_trabalho()`.

## O que ainda não foi compreendido?

Ainda falta auditar o fluxo de aprovação e o fluxo completo de gestão da medição nas etapas 1 a 6.

Também falta confirmar a intenção futura para persistência real da foto do lançamento.

## O que deve ser documentado?

Este arquivo passa a documentar o fluxo de `tela_lancar_producao()`.

A documentação monolítica antiga ainda não foi removida nem substituída.

## Baby step seguro executado

Criar documentação modular inicial de Medições em `docs/architecture/medicoes.md`, sem alterar comportamento do sistema.
