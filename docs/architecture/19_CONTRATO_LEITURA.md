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

O resultado deve transportar:

- status classificado;
- DataFrame;
- caminho do arquivo;
- HTTP status, quando disponível;
- SHA observado;
- descrição segura do erro.

## Estados previstos

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
- o SHA da leitura confirmada deve acompanhar a atualização;
- a escrita não deve buscar um SHA novo e sobrescrever silenciosamente alterações concorrentes.

## Compatibilidade

`carregar_github()` permanece temporariamente como adaptador legado porque muitos chamadores esperam um DataFrame.

A migração será feita um fluxo por vez. O adaptador legado não deve ser considerado seguro em rotinas que regravam arquivos após uma leitura possivelmente vazia.

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

Administração será o primeiro chamador migrado após a implementação e validação da infraestrutura.

O piloto deve apenas:

- usar o resultado explícito;
- bloquear inclusão, desativação e exclusão quando a leitura não for confirmada;
- preservar o SHA observado para a escrita;
- apresentar mensagem coerente.

Não deve incluir no mesmo passo validação de usuários, duplicidades, trilha de auditoria ou alteração de schema.

## Primeiro baby step de implementação

Alterar somente `services/github.py` para adicionar:

1. enum de estados;
2. estrutura imutável do resultado;
3. função `ler_csv_github()`;
4. timeout explícito;
5. classificação de HTTP, rede, conteúdo e CSV;
6. testes ou validações focadas.

Nenhum chamador será migrado no mesmo commit.