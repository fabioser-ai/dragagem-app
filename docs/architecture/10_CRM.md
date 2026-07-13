# Arquitetura Atual — CRM

Última atualização: 2026-07-13

Fontes de auditoria:

- `docs/audit/AUDIT_036_CRM.md`;
- `docs/audit/AUDIT_051_HOMOLOGACAO_ENCERRAMENTO_FASE_1.md`.

## Visão geral

O CRM organiza clientes, contatos e interações comerciais em três arquivos CSV separados e relacionados por UUID.

Arquivos principais:

- `pages/crm/crm.py`
- `pages/crm/navegacao.py`
- `pages/crm/config.py`
- `pages/crm/repositorio.py`
- `pages/crm/etapa1_clientes.py`
- `pages/crm/etapa2_contatos.py`
- `pages/crm/etapa3_interacoes.py`
- `pages/crm/utils.py`

Arquivos de dados:

- `data/crm/clientes.csv`
- `data/crm/contatos.csv`
- `data/crm/interacoes.csv`

## Entrada, autorização e navegação

O cartão do CRM é exibido quando `pode_acessar_modulo("crm")` retorna verdadeiro. O botão define `st.session_state.tela = "crm"`, e o roteador chama `crm()`.

O perfil global `funcionario` é bloqueado no roteador principal porque `crm` não pertence à lista de telas permitidas desse perfil.

Dentro do CRM não existe nova verificação de `pode_acessar_modulo("crm")`.

A navegação interna usa um rádio na barra lateral com as páginas:

- clientes;
- contatos;
- interações;
- consulta geral.

## Modelo de dados

### Clientes

A entidade possui `id_cliente` UUID, dados cadastrais, status de relacionamento, responsável, necessidade, último contato, próxima ação e timestamps.

### Contatos

A entidade possui `id_contato` UUID e referência textual a `id_cliente`.

### Interações

A entidade possui `id_interacao` UUID, referência a `id_cliente` e referência opcional a `id_contato`.

Não existe chave estrangeira, banco relacional ou validação central de integridade referencial.

## Persistência

`pages/crm/repositorio.py` implementa wrappers próprios sobre os serviços de persistência.

As operações simples ainda usam os adaptadores por arquivo aplicáveis. O cadastro de interação usa leitura explícita e `services/persistencia_multi_arquivo.py` para publicar `interacoes.csv` e `clientes.csv` no mesmo commit Git.

Os DataFrames são normalizados para o schema declarado, convertidos para texto e regravados integralmente. Colunas extras presentes nos CSVs podem desaparecer em gravações futuras porque o DataFrame é reduzido às colunas declaradas.

## Clientes

A tela permite cadastrar, buscar, filtrar e editar clientes.

Fatos observados:

- apenas o nome da empresa é obrigatório na criação;
- a data da próxima ação usa `date_input` na criação;
- na edição, a mesma informação vira texto livre;
- o seletor de edição usa somente `nome_empresa`;
- empresas homônimas podem ser ambíguas;
- `atualizar_cliente()` retorna silenciosamente quando o ID não existe;
- a tela pode exibir sucesso mesmo quando nenhuma linha foi atualizada.

## Contatos

A tela permite cadastrar, buscar e editar contatos vinculados a clientes.

Fatos observados:

- o mapa visual usa `nome_empresa` como chave para `id_cliente`;
- empresas homônimas sobrescrevem entradas no dicionário;
- o rótulo de edição combina nome do contato e nome da empresa;
- rótulos iguais continuam ambíguos;
- um contato pode ser movido para outra empresa;
- não existe regra para garantir um único contato principal por cliente;
- `atualizar_contato()` retorna silenciosamente quando o ID não existe.

## Interações

A tela registra interações e exibe o histórico.

Ao cadastrar uma interação, o fluxo atual:

1. exige leitura confirmada de `clientes.csv` e `interacoes.csv`;
2. resolve snapshot comum da branch;
3. prepara em memória a nova interação e a atualização do cliente selecionado;
4. publica os dois CSVs em um único commit Git;
5. apresenta sucesso e executa `st.rerun()` somente após resultado confirmado.

A ação fica bloqueada quando uma leitura não autoriza escrita, quando o snapshot comum não está disponível ou quando o cliente não existe mais no snapshot observado. Conflito ou falha não produz falso sucesso nem retry automático.

A migração foi implementada no commit `4abddf3b2d267e073132815c8af76807aca89310`, coberta no commit `836187cbed0c9e9eab0d70bcb44e79fade09402f` e homologada pelo GitHub Actions em Ubuntu com Python 3.12.

O seletor de contato usa `nome_contato` como chave para `id_contato`, tornando contatos homônimos ambíguos.

Se um contato for posteriormente movido para outra empresa, interações antigas podem continuar associadas ao cliente original e ao mesmo ID de contato, criando divergência semântica.

## Consulta geral

A tela carrega clientes, contatos e interações para métricas, mas a busca textual opera somente sobre colunas de clientes.

Não existe busca integrada sobre nomes de contatos ou descrições de interações.

## Observações técnicas consolidadas

- Empresas homônimas são ambíguas nos seletores.
- Contatos homônimos são ambíguos no registro de interações.
- Não existe integridade referencial central.
- Não existe regra de contato principal único.
- Contatos podem mudar de empresa sem reconciliação do histórico.
- Registrar interação e atualizar cliente é operação atômica no nível de publicação Git.
- A data da próxima ação possui tipos de entrada diferentes entre criação e edição.
- Atualizações de IDs inexistentes nas operações legadas retornam silenciosamente.
- A interface de operações legadas pode exibir sucesso sem atualização efetiva.
- A consulta geral não pesquisa contatos nem interações.
- Os wrappers descartam colunas fora do schema declarado.
- As telas internas não revalidam a permissão geral do módulo.

## Perguntas em aberto

- Empresas devem possuir nome único ou o seletor deve usar ID com rótulo descritivo?
- Como diferenciar contatos homônimos?
- Deve existir somente um contato principal por cliente?
- Contatos podem ser transferidos de empresa?
- Como preservar a coerência das interações após transferência de contato?
- A data da próxima ação deve possuir formato único?
- Atualizações sem ID encontrado devem retornar erro explícito?
- A consulta geral deve buscar também contatos e interações?
- Colunas extras devem ser preservadas pelos wrappers?
- Deve existir validação interna de permissão no CRM?

## Baby step seguro futuro

Eliminar a ambiguidade dos seletores sem alterar o schema: exibir rótulos compostos com nome, contexto e ID abreviado, mantendo `id_cliente` e `id_contato` como valores internos.