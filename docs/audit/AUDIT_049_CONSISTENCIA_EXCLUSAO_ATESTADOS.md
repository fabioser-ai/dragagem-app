# AUDIT_049 — Consistência da Exclusão Composta de Atestados

Data: 2026-07-13

## Status e escopo

- Auditoria arquitetural concluída.
- Nenhum comportamento funcional foi alterado.
- Escopo: exclusão de um atestado e de seus serviços vinculados, limites do contrato atual, estados possíveis após falha parcial e alternativas de consistência multi-arquivo.

## Componentes observados

- `pages/dados.py`;
- `services/github.py`;
- `services/dados_persistencia.py`;
- `data/atestados.csv`;
- `data/atestados_servicos.csv`;
- `docs/audit/AUDIT_048_ATESTADOS_SERVICOS.md`;
- `docs/architecture/16_DADOS.md`.

## Fluxo atual

A exclusão remove em memória:

1. o registro principal de `data/atestados.csv`;
2. todos os serviços com o mesmo `id_atestado` de `data/atestados_servicos.csv`.

Depois chama sequencialmente o adaptador legado:

1. `salvar_github(df_atestados, ARQ_ATESTADOS, TOKEN, REPO)`;
2. `salvar_github(df_servicos, ARQ_ATESTADOS_SERVICOS, TOKEN, REPO)`.

O fluxo apresenta mensagem de exclusão e executa `st.rerun()` após as duas chamadas. Cada chamada realiza sua própria leitura de SHA e sua própria atualização do arquivo.

## Limite do contrato atual

`salvar_csv_github()` fornece controle explícito de concorrência para um único arquivo. Ele recebe um SHA de blob esperado e executa um `PUT` para um caminho.

Esse contrato não possui:

- snapshot comum dos dois arquivos;
- commit único contendo as duas alterações;
- rollback;
- compensação;
- registro de operação pendente;
- reconciliação automática.

Executar duas escritas seguras em sequência reduziria conflitos silenciosos em cada arquivo, mas manteria a possibilidade de sucesso parcial.

## Estados possíveis após falha parcial

### A primeira gravação conclui e a segunda falha

- o atestado desaparece;
- seus serviços permanecem;
- surgem serviços órfãos.

### A primeira gravação falha e a segunda conclui

- o atestado permanece;
- seus serviços desaparecem;
- o agregado fica incompleto.

### Compensação também falha

Qualquer tentativa de restaurar automaticamente a primeira gravação exige uma terceira escrita. Essa escrita pode falhar, conflitar ou sobrescrever alteração concorrente. Portanto, compensação não fornece garantia transacional.

## Alternativas avaliadas

### 1. Manter duas escritas sequenciais seguras

Vantagem:

- pequena alteração sobre contratos existentes.

Limite decisivo:

- continua não atômica;
- ainda admite estado parcial visível.

Conclusão: insuficiente.

### 2. Compensar a primeira escrita quando a segunda falhar

Vantagem:

- tenta restaurar o estado anterior.

Limites:

- rollback é outra operação remota sujeita a falha;
- pode conflitar com alterações concorrentes;
- exige estado e observabilidade adicionais;
- não garante retorno ao estado original.

Conclusão: não deve ser a garantia principal.

### 3. Desativação lógica

Vantagem:

- evita remoção física imediata.

Limites:

- exige alteração de schema;
- exige mudança de filtros, busca, seleção e consumidores;
- introduz política de vigência e restauração ainda inexistente;
- não elimina por si só a necessidade de atualizar consistentemente o agregado.

Conclusão: pode ser decisão funcional futura, mas não é solução técnica mínima para o problema atual.

### 4. Commit Git único com os dois arquivos

Fluxo arquitetural:

1. obter um snapshot comum da branch e dos dois arquivos;
2. produzir as duas versões novas em memória;
3. criar uma única alteração de repositório contendo ambos os CSVs;
4. publicar o commit somente se a cabeça da branch continuar igual à observada;
5. em conflito, não tornar nenhuma das duas versões visível;
6. apresentar sucesso somente após confirmação da atualização da branch.

Propriedade principal:

- os dois arquivos passam a ser publicados juntos no mesmo commit;
- falha anterior à atualização da branch não expõe alteração parcial;
- avanço concorrente da branch deve resultar em conflito, não em sobrescrita.

Conclusão: alternativa arquitetural recomendada.

## Decisão arquitetural

A exclusão física atual será preservada enquanto não existir decisão funcional diferente.

A migração da exclusão composta não deve usar duas chamadas independentes de escrita segura. Deve existir antes um contrato explícito de persistência multi-arquivo que publique `atestados.csv` e `atestados_servicos.csv` em um único commit Git, condicionado ao snapshot comum observado.

Objetos intermediários eventualmente criados antes de uma falha não podem alterar a branch nem tornar apenas um arquivo visível.

## Requisitos do contrato multi-arquivo

O futuro contrato deve:

- receber os dois DataFrames e seus caminhos;
- usar um único snapshot de repositório como precondição;
- preservar os schemas atuais;
- gerar um único commit com os dois arquivos;
- recusar publicação quando a branch tiver avançado;
- retornar resultado explícito de sucesso, conflito, não autorização, validação, falha temporária ou erro desconhecido;
- não executar releitura silenciosa para contornar conflito;
- não fazer retry automático de operação destrutiva;
- não apresentar sucesso antes de a branch apontar para o commit resultante;
- permitir testes sem acesso real ao GitHub.

## Observabilidade e recuperação

Em caso de falha:

- nenhum dos dois arquivos deve ficar parcialmente publicado;
- a interface deve manter a operação não concluída;
- o usuário deve receber erro classificado;
- conflito deve exigir nova leitura e nova confirmação da exclusão;
- não deve existir compensação automática invisível.

## Fora do escopo

- desativação lógica;
- lixeira ou restauração pela interface;
- mudança de schema;
- alteração de rótulos ou datas;
- permissões granulares;
- edição de serviços;
- normalização de dados históricos;
- mudança da relação por `id_atestado`.

## Observações técnicas

### OT-106 — SHA de blob individual não representa snapshot do agregado

Os dois arquivos podem ser lidos ou alterados em instantes diferentes. A precondição da operação composta precisa estar ligada a um snapshot comum do repositório.

### OT-107 — Duas escritas seguras continuam não atômicas

Classificação de resultado e SHA esperado protegem cada arquivo isoladamente, mas não garantem publicação conjunta.

### OT-108 — Compensação não equivale a rollback transacional

A restauração é outra escrita remota e pode falhar ou conflitar.

### OT-109 — Um commit único é a fronteira atômica disponível no armazenamento atual

Como os dois CSVs pertencem ao mesmo repositório, a unidade natural de publicação conjunta é um único commit que atualize ambos.

## Próximo Kid Step seguro

Criar apenas a fundação do contrato de persistência multi-arquivo, sem conectá-lo ainda à interface:

1. definir resultados e estados explícitos da operação composta;
2. implementar a criação de um commit único para dois arquivos a partir de um snapshot comum;
3. bloquear atualização quando a branch tiver avançado;
4. criar testes unitários para sucesso, conflito, falha antes da publicação e ausência de estado parcial visível;
5. não alterar ainda o botão de exclusão em `pages/dados.py`;
6. somente após homologar essa fundação migrar o consumidor em Kid Step separado.
