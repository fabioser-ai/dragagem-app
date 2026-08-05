# RBAC-004 — Matriz inicial conservadora

## Princípio homologado

Uma Role representa uma função institucional.

Uma permissão representa uma decisão administrativa.

Sempre que uma nova permissão não representar uma decisão diferente de negócio, ela não deverá existir.

**Uma Role vazia é preferível a uma Role com poder mal definido.**

**O acesso será ampliado conforme necessidade real, em Baby Steps.**

A primeira proposta, com 43 concessões, foi deliberadamente reduzida após
homologação humana. A matriz final contém somente 9 linhas `allow`. Tudo que não
foi concedido permanece negado por padrão.

## Matriz final

### FUNCIONARIO — 1 concessão

- `prestacao_contas/despesa/criar`.

Foi retirada a visualização de despesas porque o modelo ainda não distingue com
segurança despesas próprias, da equipe, da obra ou todas as despesas.

### ENCARREGADO — Role vazia

Foram retiradas todas as concessões de Medições e de Uniformes/EPIs. Medições
possui arquitetura própria de perfil e obra; as operações de Uniformes/EPIs
continuam parciais e a responsabilidade institucional não foi homologada.

### APROVADOR — 1 concessão

- `prestacao_contas/decisao_despesa/aprovar`.

A aprovação de lançamento foi retirada junto com toda integração de Medições.
A decisão de despesa permanece separada de pagamento e Administração.

### FINANCEIRO — 3 concessões

- `prestacao_contas/pagamento/editar`;
- `prestacao_contas/tipo_despesa/visualizar`;
- `prestacao_contas/tipo_despesa/criar`.

A visualização de despesas foi retirada porque seu escopo ainda é parcial e não
distingue com segurança os recortes próprios, de equipe, obra ou globais.

### ENGENHARIA — 4 concessões

- `dados/atestado/criar`;
- `dados/atestado/editar`;
- `dados/local_trabalho/criar`;
- `obras/obra/visualizar`.

Foram retiradas as capacidades amplas de cadastro, a visualização parcial de
atestados e locais, todas as capacidades de orçamento e toda Medição. Permanecem
somente ações classificadas como completas e tecnicamente delimitadas.

### RH — Role vazia

Foram retiradas todas as permissões de Férias/Folgas porque as capacidades
específicas ainda usam o recurso amplo legado `registros`. Também foram retiradas
todas as permissões de Uniformes/EPIs porque a responsabilidade institucional do
RH não está explicitamente homologada no APP. As exclusões de férias e folgas não
foram concedidas.

## Concessões retiradas

Foram removidas 34 das 43 linhas iniciais:

- toda permissão de Medições;
- toda permissão de Uniformes/EPIs;
- toda permissão de Férias/Folgas;
- visualização de despesas de FUNCIONARIO e FINANCEIRO;
- cadastros gerais, visualizações parciais, orçamentos e clientes/insumos da
  ENGENHARIA;
- visualização parcial de atestados e locais de trabalho.

## Garantias e limitações

Nenhuma permissão crítica ou de `administracao` foi concedida. Proprietário,
superadmin, recuperação administrativa, custódia e contas protegidas continuam
fora do RBAC.

Nenhum usuário foi associado a Role. A matriz não participa da autenticação nem
do cálculo efetivo de acesso; `data/permissoes_usuarios.csv` continua sendo a
fonte vigente. Portanto, este ajuste não altera acesso efetivo.

As quatro Roles com concessões ainda não estão ativas para usuários. Antes de
qualquer integração será necessário confirmar o recorte visual das rotas e a
compatibilidade operacional das permissões isoladas. Futuras ampliações exigirão
necessidade operacional real e homologação humana específica.
