# RBAC-003 — Endurecimento mínimo das fronteiras de autorização

## Escopo executado

Este PR fortalece apenas as fronteiras mínimas necessárias para permitir futura concessão segura de permissões.

A redução das demais permissões parciais continuará sendo realizada em Baby Steps.

- `dados/local_trabalho/criar` passou de **inexistente** para **completa**: a
  autoridade central é revalidada dentro de `salvar_locais_seguro()`,
  imediatamente antes de `salvar_cadastro_seguro()`.
- `prestacao_contas/despesa/criar` manteve a classificação **completa**, agora
  com nova revalidação antes do upload do comprovante e outra imediatamente
  antes da gravação do CSV de despesas.
- Férias/Folgas não sofreu mudança funcional: `salvar_csv_seguro()` já revalida
  a autoridade central imediatamente antes da persistência. As seis permissões
  específicas continuam **parciais** porque o fluxo legado consulta o recurso
  amplo `registros`. As ambiguidades de ciclo de vida e alertas não foram
  reinterpretadas.
- Uniformes/EPIs passou a informar o recurso específico em cada chamada de
  persistência (`item`, `compra`, `movimentacao`, `entrega`, `devolucao` e
  `baixa`). A decisão exata é revalidada imediatamente antes da gravação, com
  compatibilidade explícita para `cadastros/editar`.

## Estados do catálogo

| Estado | Antes | Depois |
|---|---:|---:|
| completa | 31 | 32 |
| parcial | 23 | 23 |
| específica de Medições | 6 | 6 |
| inexistente | 1 | 0 |

Somente `dados/local_trabalho/criar` mudou de classificação. As seis operações
de Uniformes/EPIs permanecem parciais porque a interface ainda depende da guarda
ampla legada e removê-la alteraria o comportamento funcional atual.

## Compatibilidade e limites

Nenhum usuário ou Role recebeu permissões. `roles_permissoes.csv` permanece
vazio e o cálculo RBAC não entrou em produção. Autenticação, `APP_USERS`,
`SYSTEM_OWNER_ID`, regras de negócio e Medições não foram alterados.

Riscos residuais: leituras protegidas apenas pela rota; granularidade ampla em
Férias/Folgas; compatibilidade ampla e controle visual legado em Uniformes/EPIs;
e todas as demais permissões parciais documentadas pelo RBAC-002.
