# AUDIT_046 — Contrato Explícito de Resultado de Leitura

Data: 2026-07-11

## Status e escopo

- Auditoria e definição arquitetural concluídas.
- Nenhum comportamento funcional foi alterado.
- Escopo: `services/github.py`, contrato de leitura CSV, compatibilidade, classificação de resultados, bloqueio de escrita e sequência de migração dos chamadores.

## Evidência atual

`carregar_github(arquivo, token, repo)` executa um GET e retorna:

- DataFrame lido, quando HTTP 200 e CSV válido;
- DataFrame vazio, quando HTTP diferente de 200;
- DataFrame vazio, quando o campo `content` está ausente ou vazio;
- exceção não classificada, quando base64, UTF-8, JSON ou CSV falha.

O retorno não informa se o DataFrame vazio representa arquivo válido sem linhas, arquivo inexistente, falha de autenticação, limitação da API, rede ou conteúdo inválido.

`salvar_github()` busca o SHA atual e substitui o arquivo integralmente. A combinação entre leitura ambígua e gravação integral foi registrada como o principal risco transversal.

## Objetivo do novo contrato

Permitir que cada chamador decida com segurança entre:

1. continuar com dados confirmados;
2. tratar arquivo validamente vazio;
3. criar arquivo inexistente de forma deliberada;
4. bloquear escrita após falha de leitura;
5. apresentar erro operacional sem confundi-lo com ausência de dados.

## Contrato proposto

Adicionar uma função nova, sem alterar imediatamente a assinatura da função legada:

```python
ler_csv_github(arquivo, token, repo) -> ResultadoLeituraCSV
```

Estrutura conceitual:

```python
@dataclass(frozen=True)
class ResultadoLeituraCSV:
    status: StatusLeitura
    dados: pd.DataFrame
    arquivo: str
    http_status: int | None
    sha: str | None
    erro: str | None

    @property
    def leitura_confirmada(self) -> bool:
        return self.status in {
            StatusLeitura.SUCESSO_COM_DADOS,
            StatusLeitura.SUCESSO_VAZIO,
            StatusLeitura.ARQUIVO_INEXISTENTE,
        }

    @property
    def pode_sobrescrever(self) -> bool:
        return self.status in {
            StatusLeitura.SUCESSO_COM_DADOS,
            StatusLeitura.SUCESSO_VAZIO,
        }
```

## Estados oficiais propostos

### `SUCESSO_COM_DADOS`

- GET HTTP 200;
- conteúdo presente;
- base64, UTF-8 e CSV válidos;
- DataFrame possui ao menos uma linha.

Permite leitura e posterior atualização, desde que o SHA observado seja usado ou reconfirmado.

### `SUCESSO_VAZIO`

- GET HTTP 200;
- conteúdo válido;
- CSV válido sem registros.

Permite atualização deliberada. Não deve ser confundido com ausência do arquivo.

### `ARQUIVO_INEXISTENTE`

- GET HTTP 404.

A criação pode ser permitida apenas quando o chamador declara explicitamente que aquele fluxo pode inicializar o arquivo. Não autoriza uma rotina de edição a recriar silenciosamente uma base esperada.

### `NAO_AUTORIZADO`

- HTTP 401 ou 403.

Bloqueia qualquer escrita derivada da leitura.

### `CONFLITO_OU_LIMITE`

- HTTP 409, 422 ou 429, conforme contexto da API.

Bloqueia escrita e exige mensagem operacional específica.

### `FALHA_TEMPORARIA`

- timeout, conexão, DNS, HTTP 5xx ou indisponibilidade transitória.

Bloqueia escrita. O chamador pode oferecer nova tentativa, mas não transformar o resultado em vazio.

### `CONTEUDO_INVALIDO`

- JSON inesperado;
- conteúdo base64 ausente ou inválido;
- falha de UTF-8;
- CSV inválido.

Bloqueia escrita e preserva o arquivo remoto.

### `ERRO_DESCONHECIDO`

- erro não classificado.

Bloqueia escrita por padrão.

## Regras de segurança

1. Somente `SUCESSO_COM_DADOS` e `SUCESSO_VAZIO` autorizam sobrescrita de arquivo existente.
2. `ARQUIVO_INEXISTENTE` autoriza criação apenas por operação explicitamente inicializadora.
3. Nenhum status de erro pode ser convertido automaticamente em DataFrame vazio válido.
4. O resultado deve transportar o SHA observado no GET.
5. A escrita deve usar o SHA originado pela leitura confirmada, reduzindo a janela de sobrescrita concorrente.
6. Se o SHA remoto mudou, a escrita deve falhar como conflito; não deve buscar um novo SHA e sobrescrever silenciosamente dados mais recentes.
7. Mensagens de sucesso da interface só devem ocorrer depois de resposta HTTP 200 ou 201 da escrita.
8. A confirmação por releitura pode ser adotada nos fluxos críticos, mas não substitui o controle de SHA.

## Compatibilidade

Não alterar `carregar_github()` no primeiro baby step. A função é usada amplamente e seus chamadores esperam diretamente um DataFrame.

Estratégia:

1. criar `StatusLeitura` e `ResultadoLeituraCSV`;
2. criar `ler_csv_github()`;
3. manter `carregar_github()` como adaptador legado temporário;
4. migrar um chamador crítico por vez;
5. somente remover ou endurecer o legado quando todos os chamadores estiverem identificados.

O adaptador legado deve ser explicitamente marcado como inseguro para fluxos que regravam arquivos.

## Chamadores prioritários para bloqueio de escrita

### Prioridade 1 — risco direto de reconstrução ou substituição após vazio

- Administração: `data/permissoes_usuarios.csv`;
- Log: `data/log_acessos.csv`;
- Dados: CRUDs técnicos, atestados e locais;
- Férias: `data/ferias.csv` e `data/folgas.csv`;
- CRM: clientes, contatos e interações;
- Prestação de Contas: tipos e despesas;
- Orçamentos: `data/orcamentos.csv` e catálogos usados em gravação;
- Medições: wrappers `carregar_csv()` seguidos por `salvar_csv()`.

### Prioridade 2 — somente leitura, mas com mensagem enganosa

- rota Obras;
- seletores e consultas que apresentam falha como ausência de dados;
- carregamento de comprovantes e binários.

## Primeiro chamador recomendado

Administração é o piloto mais seguro e valioso porque:

- possui um único CSV central;
- o risco destrutivo já está bem documentado;
- o fluxo é restrito a `superadmin`;
- inclusão, desativação e exclusão podem ser bloqueadas quando a leitura não é confirmada;
- a mudança não exige alterar regras de negócio ou schemas.

O piloto deve migrar apenas leitura, bloqueio de ações e uso do SHA. Não deve incluir simultaneamente validação de usuários, duplicidades, auditoria ou redesign da tela.

## Escrita correspondente

O contrato de leitura revela que a escrita atual também precisa de evolução isolada. A futura função deve receber o SHA esperado:

```python
salvar_csv_github(df, arquivo, token, repo, sha_esperado=None, criar=False)
```

Regras:

- atualização exige `sha_esperado`;
- criação exige `criar=True` e ausência confirmada;
- conflito HTTP deve ser retornado como resultado estruturado;
- a função não deve executar um GET independente para obter SHA antes do PUT.

Essa escrita não será implementada junto da criação inicial do resultado de leitura, exceto se for indispensável ao piloto e permanecer em alteração pequena e testável.

## Perguntas em aberto

- O projeto prefere `dataclass + Enum` ou estrutura dicionário tipada?
- Arquivo HTTP 200 com conteúdo vazio deve ser `SUCESSO_VAZIO` ou `CONTEUDO_INVALIDO`?
- Quais arquivos podem ser criados automaticamente?
- Qual timeout padrão será usado no GET e PUT?
- Haverá retry automático apenas para leitura? Quantas tentativas?
- Quais fluxos exigem releitura posterior de confirmação?
- Como mensagens técnicas serão traduzidas para a interface sem expor tokens ou payloads?

## Baby step seguro

Implementar somente em `services/github.py`:

1. `StatusLeitura`;
2. `ResultadoLeituraCSV`;
3. `ler_csv_github()` com timeout e classificação de erros;
4. testes ou validações focadas em respostas simuladas;
5. nenhuma migração de chamador no mesmo commit.

Após validar a infraestrutura, migrar Administração em um segundo baby step independente.
