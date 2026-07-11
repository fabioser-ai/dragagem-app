# Arquitetura Atual — Contrato Explícito de Leitura

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_046_CONTRATO_LEITURA.md`

## Problema arquitetural

`carregar_github()` retorna diretamente um DataFrame e converte respostas HTTP diferentes de 200 em DataFrame vazio. O chamador não consegue distinguir arquivo validamente vazio de falha de autenticação, indisponibilidade, inexistência ou conteúdo inválido.

Como as gravações substituem o arquivo completo, essa ambiguidade pode levar à sobrescrita de dados válidos após falha de leitura.

## Direção definida

Adicionar uma nova API explícita, preservando temporariamente a função legada:

```python
ler_csv_github(arquivo, token, repo) -> ResultadoLeituraCSV
```

O resultado transporta:

- status classificado;
- DataFrame;
- caminho do arquivo;
- HTTP status, quando disponível;
- SHA observado;
- descrição segura do erro.

## Estados implementados

- `SUCESSO_COM_DADOS`;
- `SUCESSO_VAZIO`;
- `ARQUIVO_INEXISTENTE`;
- `NAO_AUTORIZADO`;
- `CONFLITO_OU_LIMITE`;
- `FALHA_TEMPORARIA`;
- `CONTEUDO_INVALIDO`;
- `ERRO_DESCONHECIDO`.

## Política de escrita

- atualização de arquivo existente somente após `SUCESSO_COM_DADOS` ou `SUCESSO_VAZIO`;
- criação somente após `ARQUIVO_INEXISTENTE` e autorização explícita do chamador;
- qualquer falha bloqueia a escrita derivada;
- o SHA da leitura confirmada deve acompanhar a futura atualização;
- a escrita não deve buscar um SHA novo e sobrescrever silenciosamente alterações concorrentes.

A função estruturada de escrita com SHA esperado ainda não foi implementada. `salvar_github()` permanece legado.

## Compatibilidade

`carregar_github()` permanece temporariamente como adaptador legado porque muitos chamadores esperam um DataFrame.

A migração será feita um fluxo por vez. O adaptador legado não deve ser considerado seguro em rotinas que regravam arquivos após uma leitura possivelmente vazia.

Nenhum chamador foi migrado durante a implementação inicial da infraestrutura.

## Implementação realizada

`services/github.py` contém agora:

- `DEFAULT_REQUEST_TIMEOUT`;
- enum `StatusLeitura`;
- dataclass imutável `ResultadoLeituraCSV`;
- propriedades `leitura_confirmada` e `pode_sobrescrever`;
- função `ler_csv_github()`;
- classificação de HTTP 401, 403, 404, 409, 422, 429 e 5xx;
- classificação de timeout e falha de conexão;
- validação de JSON, conteúdo base64, UTF-8 e CSV;
- normalização das quebras de linha do base64 retornado pela API do GitHub;
- preservação do SHA observado.

As funções legadas de leitura e escrita de CSV e arquivos binários permanecem disponíveis.

## Validação automatizada

Foi criado `tests/test_github_leitura.py` usando `unittest` da biblioteca padrão, sem adicionar dependência de teste ao projeto.

Cenários cobertos:

1. sucesso com dados e SHA;
2. base64 com quebras de linha;
3. CSV somente com cabeçalho;
4. arquivo fisicamente vazio;
5. arquivo inexistente — HTTP 404;
6. não autorizado — HTTP 401;
7. limite ou conflito — HTTP 429;
8. falha temporária — HTTP 500;
9. timeout de rede;
10. JSON inválido;
11. base64 inválido.

Foi criado `.github/workflows/tests.yml` para executar:

```text
python -m unittest discover -s tests -p "test_*.py" -v
```

Em 2026-07-11, a suíte foi executada localmente no commit `14dd73d23b12f15607c4ebaffa15a3e18b1b8101`, após instalar as dependências declaradas em `requirements.txt`. Os 10 testes passaram. As ações disponíveis do conector ainda não retornaram uma execução ou status de CI para esse commit; a confirmação registrada é, portanto, local e reproduz o comando definido pelo workflow.

## Ordem de migração

### Prioridade de bloqueio de escrita

1. Administração;
2. logs;
3. Dados;
4. Férias;
5. CRM;
6. Prestação de Contas;
7. Orçamentos;
8. Medições.

### Somente leitura e mensagens operacionais

Depois dos fluxos de escrita, migrar consultas como Obras e demais telas que apresentam falha como ausência de dados.

## Piloto recomendado

Administração será o primeiro chamador migrado depois que a execução dos testes da infraestrutura estiver confirmada.

O piloto deve apenas:

- usar o resultado explícito;
- bloquear inclusão, desativação e exclusão quando a leitura não for confirmada;
- preservar o SHA observado para a escrita;
- apresentar mensagem coerente.

Não deve incluir no mesmo passo validação de usuários, duplicidades, trilha de auditoria ou alteração de schema.

## Próximo passo seguro

1. definir se a escrita estruturada que receba o SHA esperado é indispensável ao piloto de Administração;
2. se for indispensável, implementá-la em Kid Step isolado, sem migrar chamadores;
3. migrar Administração em alteração isolada;
4. não combinar essa migração com mudanças de schema, permissões ou regras de negócio.
