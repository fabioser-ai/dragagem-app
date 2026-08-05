# RBAC-004 — Concessão inicial de permissões às Roles

## Princípio

Uma Role representa uma função institucional.

Uma permissão representa uma decisão administrativa.

Sempre que uma nova permissão não representar uma decisão diferente de negócio, ela não deverá existir.

A matriz usa apenas capacidades já existentes em `data/permissoes_catalogo.csv`.
Somente linhas `allow` foram registradas. Tudo que não foi concedido permanece
negado por padrão. Não foram usados `deny`, pois precedência entre efeitos ainda
não faz parte da arquitetura homologada.

## Matriz institucional

### FUNCIONARIO

Objetivo: registrar e consultar as próprias prestações de contas.

Concedidas: `prestacao_contas/despesa/visualizar` e
`prestacao_contas/despesa/criar`.

Negadas: aprovação, pagamento, tipos de despesa e toda Administração.

### ENCARREGADO

Objetivo: acompanhar produção, registrar lançamentos e coordenar movimentação
física de Uniformes/EPIs.

Concedidas: visualização de medição e lançamento; criação de lançamento;
visualização de estoque; criação de movimentação.

Negadas: aprovação, alteração estrutural de medições, compras, administração de
usuários, Roles ou permissões.

### APROVADOR

Objetivo: executar exclusivamente decisões formais de aprovação.

Concedidas: aprovação de decisão de despesa e de lançamento de Medições.

Negadas: criação, edição, exclusão, pagamento e Administração.

### FINANCEIRO

Objetivo: consultar despesas, registrar pagamento e manter tipos de despesa.

Concedidas: visualização de despesa; edição de pagamento; visualização e criação
de tipo de despesa.

Negadas: decisão de aprovação, gestão técnica e Administração do sistema.

### ENGENHARIA

Objetivo: manter cadastros e atestados técnicos, estruturar medições, consultar
obras e produzir orçamentos.

Concedidas: visualização, criação e edição de cadastros e atestados; visualização
e criação de local de trabalho; visualização, criação e edição de medição;
visualização de lançamentos e obras; visualização, criação e edição de orçamento;
criação de cliente de orçamento; edição de insumos.

Negadas: exclusões, aprovações, finanças, RH e Administração.

### RH

Objetivo: gerir férias e folgas e custodiar entrega, devolução e baixa de
Uniformes/EPIs.

Concedidas: visualização de registros; criação, edição e exclusão de férias e
folgas; visualização de estoque; criação de item, entrega, devolução e baixa.

Negadas: compra e movimentação entre obras, aprovação, finanças e Administração.

## Garantias e limitações

Nenhuma permissão crítica ou de `administracao` foi concedida. Proprietário,
superadmin, recuperação administrativa, custódia e contas protegidas continuam
fora do RBAC.

Nenhum usuário foi associado a Role. A matriz não participa da autenticação nem
do cálculo efetivo de acesso; `data/permissoes_usuarios.csv` continua sendo a
fonte vigente. Portanto, este PR não altera acesso efetivo.

Algumas capacidades concedidas ainda estão classificadas como parciais ou
específicas de Medições. Sua futura ativação dependerá das etapas próprias de
integração, preservando negação por padrão e as fronteiras documentadas.
