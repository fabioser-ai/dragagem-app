# RBAC-002 — Catálogo canônico de permissões

## Conceito

O catálogo canônico enumera capacidades reais encontradas no código atual. Uma
capacidade é uma operação funcional existente. Uma permissão é a representação
normalizada dessa capacidade por módulo, recurso e ação. Uma Role poderá receber
permissões em etapa futura. Um usuário é uma identidade individual e continua
fora do RBAC neste passo.

**O catálogo define quais capacidades podem ser concedidas. Ele não concede acesso por si só.**

**Roles, usuários e permissões atuais permanecem inalterados neste passo.**

O arquivo oficial é `data/permissoes_catalogo.csv`. Cada entrada possui UUID
imutável, identidade única `modulo + recurso + acao`, descrição, sensibilidade,
escopo por obra, estado da proteção e evidência técnica. Não há exclusão física.
Novas entradas posteriores deverão nascer inativas.

## Método de inspeção

Foram inspecionadas dez áreas funcionais: Administração, Dados, Férias/Folgas,
Prestação de Contas, Medições, CRM, Uniformes/EPIs, Obras, Novo Orçamento e
Orçamento legado. Novo e legado reutilizam corretamente o módulo canônico
`orcamento`; por isso o catálogo contém nove identificadores de módulo.

A inspeção partiu do roteador em `app.py`, da autoridade em
`services/autorizacao.py`, dos pontos `pode(...)`, das funções próprias de
Medições e das chamadas de persistência. Títulos de botões não foram tratados
como autorização.

## Matriz resumida

| Módulo | Entradas | Recursos principais | Estado predominante |
|---|---:|---|---|
| administracao | 11 | permissão individual, usuário operacional, Role, catálogo | completa |
| dados | 10 | cadastro, atestado, local de trabalho | completa/parcial; 1 inexistente |
| ferias | 7 | registro, férias, folga | parcial |
| prestacao_contas | 6 | despesa, decisão, pagamento, tipo | completa/parcial |
| medicoes | 6 | medição, lançamento | específica de Medições |
| crm | 8 | cliente, contato, interação | completa/parcial |
| uniformes_epis | 7 | estoque, item, compra, movimentação, ciclo do funcionário | parcial |
| obras | 1 | obra | completa |
| orcamento | 5 | orçamento, cliente, insumo | completa/parcial |

O catálogo possui 61 permissões: 31 com proteção completa, 23 parciais, 1 sem
proteção adequada confirmada e 6 dependentes da arquitetura própria de Medições.
O significado e a evidência de cada entrada estão registrados na própria matriz
CSV e são exibidos integralmente na Administração.

## Sensibilidade

- **baixa:** leitura operacional sem dado pessoal sensível;
- **média:** criação ou edição operacional;
- **alta:** dados de terceiros, exclusão, aprovação, finanças ou trânsito entre obras;
- **crítica:** usuários, Roles, permissões ou ampliação de privilégios.

A classificação é documental. Ela não concede nem bloqueia acesso.

## Lacunas de proteção encontradas

1. `dados/local_trabalho/criar`: a persistência segura controla concorrência,
   mas `salvar_locais_seguro()` não revalida autorização central. Estado:
   **inexistente** para a ação específica.
2. Leituras de recursos em vários módulos dependem da entrada na rota e não de
   guarda específica por recurso. Foram classificadas como **parciais**.
3. Férias e Folgas persistem com o recurso amplo legado `registros`; as
   capacidades específicas `ferias` e `folga` ainda não são distinguidas.
4. Uniformes/EPIs usa uma única decisão `cadastros/editar` para item, compra,
   movimentação, entrega, devolução e baixa. As capacidades existem, mas a
   autorização específica é parcial.
5. A criação de orçamento usa atualmente a autorização `orcamento/editar`.
   `orcamento/criar` foi catalogada como capacidade real com proteção parcial.
6. CRM protege as escritas por recurso e ação, mas as consultas dependem da rota.
7. Medições mantém perfis e vínculos por obra próprios. Nenhuma unificação foi
   afirmada ou implementada.

Nenhuma dessas lacunas foi corrigida neste PR.

## Operações ambíguas e decisões humanas pendentes

- `ferias/ciclo_vida/alterar` controla programar, confirmar início, confirmar
  término e cancelar. Forçar tudo para `editar` ou separar `cancelar` mudaria a
  granularidade atual. A operação ficou fora do catálogo até decisão humana.
- `ferias/alertas/enviar` não cabe nas sete ações sem perda de significado. Não
  foi criada ação nova e a capacidade ficou documentada como pendência.
- Em Prestação de Contas, aprovar e reprovar são dois resultados da mesma função
  de decisão e da mesma autoridade imediatamente revalidada. Foram representados
  por `decisao_despesa/aprovar`. Marcar como pago altera o recurso pagamento e
  foi representado por `pagamento/editar`.
- Operações de domínio do Novo Orçamento como congelar, adotar cenário e aprovar
  versão existem no modelo, mas não foi confirmada exposição persistente com
  autorização própria. Elas não foram catalogadas como concessões disponíveis.

## Próximos passos

Após decisão humana sobre as ambiguidades, uma missão específica poderá ajustar
o catálogo. A concessão de permissões às Roles e o vínculo usuário → Role
continuam fora deste PR. `roles_permissoes.csv` permanece vazio e
`permissoes_usuarios.csv` continua sendo a fonte efetiva atual.
