# Arquitetura Atual — Contrato Explícito de Leitura e Escrita

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_046_CONTRATO_LEITURA.md`

## Problema arquitetural

`carregar_github()` retorna diretamente um DataFrame e converte respostas HTTP diferentes de 200 em DataFrame vazio. O chamador não consegue distinguir arquivo validamente vazio de falha de autenticação, indisponibilidade, inexistência ou conteúdo inválido.

Como as gravações substituem o arquivo completo, essa ambiguidade pode levar à sobrescrita de dados válidos após falha de leitura.

## Contrato explícito de leitura

A API estruturada é:

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

### Estados implementados

- `SUCESSO_COM_DADOS`;
- `SUCESSO_VAZIO`;
- `ARQUIVO_INEXISTENTE`;
- `NAO_AUTORIZADO`;
- `CONFLITO_OU_LIMITE`;
- `FALHA_TEMPORARIA`;
- `CONTEUDO_INVALIDO`;
- `ERRO_DESCONHECIDO`.

## Contrato explícito de escrita

A API estruturada é:

```python
salvar_csv_github(
    df,
    arquivo,
    token,
    repo,
    *,
    sha_esperado=None,
    criar=False,
    mensagem=None,
    timeout=DEFAULT_REQUEST_TIMEOUT,
) -> ResultadoEscritaCSV
```

A escrita estruturada:

- exige `sha_esperado` para atualização;
- exige `criar=True` para criação;
- rejeita criação acompanhada de SHA;
- não executa GET para descobrir a versão remota;
- devolve status estruturado em vez de levantar exceção genérica para respostas esperadas;
- preserva o SHA resultante quando o GitHub o devolve.

### Estados implementados

- `SUCESSO_ATUALIZADO`;
- `SUCESSO_CRIADO`;
- `REQUISICAO_INVALIDA`;
- `NAO_AUTORIZADO`;
- `CONFLITO`;
- `LIMITE_OU_VALIDACAO`;
- `FALHA_TEMPORARIA`;
- `ERRO_DESCONHECIDO`.

## Política de segurança

- atualização de arquivo existente somente após `SUCESSO_COM_DADOS` ou `SUCESSO_VAZIO`;
- criação somente após `ARQUIVO_INEXISTENTE` e autorização explícita do chamador;
- qualquer falha de leitura bloqueia a escrita derivada;
- o SHA da leitura confirmada acompanha a atualização;
- a escrita não busca um SHA novo e não sobrescreve silenciosamente alterações concorrentes;
- conflito HTTP 409 é devolvido como `StatusEscrita.CONFLITO`;
- mensagens de sucesso só devem ser apresentadas após resultado estruturado com `sucesso=True`.

## Compatibilidade

`carregar_github()` e `salvar_github()` permanecem temporariamente como adaptadores legados porque muitos chamadores esperam diretamente um DataFrame ou uma exceção simples.

A migração será feita um fluxo por vez. Os adaptadores legados não devem ser considerados seguros para novos fluxos que regravam arquivos após leitura possivelmente ambígua.

## Implementação realizada

`services/github.py` contém agora:

- `DEFAULT_REQUEST_TIMEOUT`;
- `StatusLeitura`;
- `ResultadoLeituraCSV`;
- `ler_csv_github()`;
- `StatusEscrita`;
- `ResultadoEscritaCSV`;
- `salvar_csv_github()`;
- classificação de HTTP, rede, conteúdo e CSV;
- normalização das quebras de linha do base64 retornado pela API do GitHub;
- preservação do SHA observado e do SHA resultante.

As funções legadas de leitura e escrita de CSV e arquivos binários permanecem disponíveis.

## Validação automatizada

Foram criados:

- `tests/test_github_leitura.py`;
- `tests/test_github_escrita.py`;
- `tests/test_log.py`;
- `.github/workflows/tests.yml`.

A suíte completa foi executada localmente com as dependências instaladas:

```text
PYTHONPATH="$PWD/.venv/lib/python3.12/site-packages" python -m unittest discover -s tests -p "test_*.py" -v
```

Resultado mais recente confirmado:

- 25 testes executados;
- 25 aprovados;
- 0 falhas;
- 0 erros.

A execução direta com o Python padrão falhou antes de carregar os testes porque aquele interpretador não possuía `requests`. A execução com as dependências declaradas do projeto foi bem-sucedida.

## Consumidores migrados

### Administração — concluída

`services/permissoes.py` oferece:

- `carregar_permissoes_resultado()`;
- `salvar_permissoes_seguro()`.

`pages/administracao.py`:

- usa o resultado explícito de leitura;
- bloqueia inclusão, desativação e exclusão quando `pode_sobrescrever` é falso;
- encaminha o SHA da leitura para a escrita;
- apresenta mensagens coerentes de falha e conflito;
- não cria automaticamente o arquivo quando ele está ausente.

A migração não alterou schema, regras de autorização, validação de usuários, duplicidades, trilha de auditoria ou exclusão física.

### Logs — concluída

`services/log.py`:

- usa `ler_csv_github()`;
- atualiza `data/log_acessos.csv` com o SHA da leitura;
- cria explicitamente o arquivo após `ARQUIVO_INEXISTENTE`;
- não grava quando a leitura falha;
- preserva as colunas `data_hora`, `usuario`, `perfil` e `acao`.

Os chamadores de login, logout e sessão expirada permanecem em `services/auth.py`. As chamadas continuam protegidas por `try/except`, portanto falhas no log não bloqueiam autenticação ou encerramento de sessão.

A validação confirmou:

- 25 testes unitários aprovados;
- `py_compile` bem-sucedido para `services/log.py` e `services/auth.py`;
- inspeção estática dos três chamadores;
- nenhum arquivo rastreado relacionado à migração alterado durante a validação.

O workspace de validação possuía um comprovante binário modificado e não relacionado. Ele não pertence aos commits da migração e não foi publicado por esta etapa.

## Ordem de migração

A ordem transversal vigente é:

1. Administração — concluída;
2. logs — concluída;
3. Dados;
4. Férias;
5. CRM;
6. Prestação de Contas;
7. Orçamentos;
8. Medições.

Depois dos fluxos de escrita, migrar consultas somente leitura, como Obras, para deixarem de apresentar falha como ausência de dados.

## Próximo passo seguro

Auditar novamente os caminhos de escrita do módulo Dados e preparar sua migração isolada para o contrato explícito.

A próxima alteração deve preservar schemas e regras funcionais. O problema de conversão numérica identificado na AUDIT_043 não deve ser corrigido no mesmo Kid Step da migração de persistência.
