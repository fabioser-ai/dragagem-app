# APP FOS — AUDITORIA ARQUITETURAL DO MÓDULO ORÇAMENTOS

Status:

Auditoria concluída e registrada como documento complementar à arquitetura atual.

Data:

2026-07-10

---

# Objetivo

Este documento registra fatos observados no código do módulo Orçamentos do APP FOS.

Ele complementa `docs/ARCHITECTURE_CURRENT.md` e deve ser consolidado nesse documento em atualização futura controlada.

Nenhuma conclusão abaixo representa intenção histórica não confirmada.

---

# 1. Entrada, navegação e autorização

O módulo Orçamentos é exibido no menu quando `pode_acessar_modulo("orcamento")` retorna verdadeiro.

O botão do menu define `st.session_state.tela = "orcamento"`.

O roteador principal possui os seguintes destinos:

- `orcamento` → `dashboard_orcamento()`;
- `orcamento_lista` → `dashboard_orcamento()`;
- `orcamento_etapa0` → `etapa0()`;
- `orcamento1` → `etapa1()`;
- `orcamento2` → `etapa2()`;
- `orcamento3` → `etapa3()`.

Não foi observada nova verificação de permissão dentro do dashboard ou das etapas.

A proteção funcional observada está concentrada na exibição do módulo pelo menu e no bloqueio global aplicado ao perfil `funcionario` no roteador principal.

---

# 2. Estrutura do módulo

Arquivos principais observados:

- `pages/orcamento/dashboard.py`;
- `pages/orcamento/etapa0.py`;
- `pages/orcamento/etapa1.py`;
- `pages/orcamento/etapa2.py`;
- `pages/orcamento/etapa3.py`;
- `app.py`;
- `pages/menu.py`;
- `services/github.py`.

Não foi observada camada própria de repositório ou serviço de domínio para Orçamentos.

Cada etapa chama diretamente `carregar_github()` e `salvar_github()`.

Foram observadas três implementações locais de salvamento de rascunho:

- `salvar_rascunho()` na Etapa 0;
- `salvar_rascunho_orcamento()` na Etapa 1;
- `salvar_rascunho_orcamento()` na Etapa 2.

Essas funções possuem a mesma intenção geral, mas não compartilham uma única implementação e não aplicam exatamente o mesmo tratamento aos dados.

---

# 3. Dashboard

O dashboard usa `st.session_state.modo_orcamento` com os valores observados:

- `inicio`;
- `continuar`.

No modo inicial, o usuário pode:

- criar novo orçamento;
- visualizar a lista geral de orçamentos;
- entrar no modo de continuação.

No modo `continuar`, são apresentados registros cujo campo `Status` seja diferente de `Finalizado`.

Ao abrir um orçamento:

1. a linha do CSV é convertida em dicionário;
2. o dicionário é gravado em `st.session_state.orcamento`;
3. o campo `Etapa_Atual` define a tela de destino.

A seleção do orçamento usa uma descrição textual e depois localiza a primeira linha cujo `Codigo` corresponda ao trecho inicial da descrição.

A lógica pressupõe que `Codigo` seja único.

---

# 4. Etapa 0 — Informações da obra

A Etapa 0:

- gera ou recupera o código do orçamento;
- seleciona ou cadastra cliente;
- recebe nome e local da obra;
- recebe data e volume;
- recebe material e tipo de desaguamento;
- recebe distâncias de recalque e desnível;
- recebe sistema de medição, horário e dias de trabalho;
- salva o primeiro rascunho;
- avança para a Etapa 1.

Arquivos consumidos:

- `data/clientes.csv`;
- `data/materiais.csv`;
- `data/desaguamento.csv`;
- `data/medicao.csv`;
- `data/horarios.csv`;
- `data/dias.csv`;
- `data/orcamentos.csv`.

## 4.1 Geração do código

O código possui o formato:

`D_NNN_ANO`

A sequência é calculada procurando códigos que contenham o ano atual, obtendo a última linha encontrada e incrementando o número existente após o primeiro sublinhado.

Fatos observados:

- a sequência depende da ordem atual do CSV;
- a função não procura explicitamente o maior número existente;
- a busca do ano utiliza correspondência textual;
- não existe validação final de unicidade antes da gravação;
- duas sessões simultâneas podem calcular o mesmo próximo código.

## 4.2 Cadastro de cliente

Quando o campo de novo cliente está preenchido, o valor é acrescentado diretamente a `data/clientes.csv`.

Não foi observada normalização ou verificação de duplicidade.

## 4.3 Validações

Não foram observadas validações obrigatórias para:

- cliente;
- nome da obra;
- local;
- volume positivo;
- material;
- desaguamento;
- sistema de medição;
- horário;
- dias de trabalho.

## 4.4 Estado persistido

A Etapa 0 grava inicialmente:

- `Status = Rascunho`;
- `Etapa_Atual = Etapa 0`;
- `Data_Criacao`;
- `Ultima_Atualizacao`.

Depois, o dicionário é mantido em `st.session_state.orcamento` e o fluxo avança para `orcamento1`.

---

# 5. Etapa 1 — Produção da draga

A Etapa 1 exige `st.session_state.orcamento`.

Arquivos consumidos:

- `data/equipamentos.csv`;
- `data/materiais.csv`;
- `data/orcamentos.csv`.

## 5.1 Produção horária

A produção horária é calculada por:

`vazão × eficiência × concentração`

A vazão parte do cadastro do equipamento, mas pode ser alterada manualmente.

A concentração parte de `Solidos_InSitu / 100`, mas também pode ser alterada manualmente.

A eficiência é obtida por mapa interno:

- `Geobag` → 0,85;
- `Centrífuga` → 0,90;
- `Bombeamento direto` → 0,95;
- `Bacia ecológica` → 0,80;
- qualquer outro valor → 0,85.

Foi observado registro com valor `Geobags`, enquanto o mapa reconhece `Geobag`.

Nesse caso, o código usa o valor padrão 0,85.

## 5.2 Horas mensais

O horário é dividido pelo texto `" - "`.

Somente a parte inteira da hora é utilizada.

A regra observada é:

`hora final − hora inicial − 1 hora de almoço`

Quando o parsing falha, são usados oito horas brutas e sete horas líquidas.

Os dias mensais são definidos por mapa fixo:

- Segunda a Sexta → 22;
- Segunda a Sábado → 26;
- Segunda a Domingo → 30;
- demais valores → 22.

Não foi observado tratamento específico para:

- minutos;
- turnos atravessando meia-noite;
- múltiplos intervalos;
- calendários reais do mês.

## 5.3 Produção mensal e prazo

A produção mensal é calculada por:

`produção horária × horas mensais`

O prazo é calculado por:

`volume ÷ produção mensal`

Quando a produção mensal é zero, o prazo recebe zero.

## 5.4 Persistência

Os cálculos são atualizados na sessão durante a renderização.

A gravação em CSV ocorre somente quando o usuário aciona `Salvar e continuar`.

A etapa persiste:

- `Status = Rascunho`;
- `Etapa_Atual = Etapa 1`;
- parâmetros e resultados calculados;
- `Ultima_Atualizacao`.

---

# 6. Etapa 2 — Dimensionamento da equipe

A Etapa 2 exige `st.session_state.orcamento`.

Arquivo principal consumido:

- `data/salarios.csv`.

A composição da equipe é armazenada como JSON na coluna `Equipe_JSON`.

## 6.1 Cálculo

Para cada posição:

`Encargos = Valor_Hora × Leis_Sociais`

`Base + Encargos = Valor_Hora + Encargos`

`Valor 25% = (Base + Encargos) × 0,25`

`Valor Final = Base + Encargos + adicional, quando marcado`

`Total = Quantidade × Valor Final`

O custo horário da equipe é a soma dos totais.

O valor padrão de leis sociais é 110%.

## 6.2 Persistência e compatibilidade

A etapa grava:

- `Equipe_JSON`;
- `Custo_Hora_Equipe`;
- `Leis_Sociais`;
- `Status = Rascunho`;
- `Etapa_Atual = Etapa 2`;
- `Ultima_Atualizacao`.

Também grava os aliases:

- `custo_hora_equipe`;
- `custo_mensal_equipe`;
- `leis_sociais`.

O campo `custo_mensal_equipe` recebe o mesmo valor de custo por hora.

O nome da coluna não corresponde à unidade efetivamente gravada.

O avanço exige apenas a existência de uma chave de custo na sessão.

Uma equipe com todas as quantidades iguais a zero pode produzir custo zero e ainda criar a chave necessária para avançar.

---

# 7. Etapa 3 — Custo do barrilete

A Etapa 3 possui duas responsabilidades observadas:

1. editar a base mestre `data/insumos.csv`;
2. calcular a composição do barrilete do orçamento atual.

## 7.1 Administração da base de insumos

A tela permite editar, adicionar e remover linhas da base mestre de insumos.

Ao salvar, substitui integralmente `data/insumos.csv`.

Não foi observada permissão separada para essa operação.

Qualquer usuário que alcance a Etapa 3 pode executar essa alteração.

## 7.2 Dependência da equipe

A etapa lê somente a chave `custo_hora_equipe`.

A chave canônica `Custo_Hora_Equipe` não é consultada.

O teste usa `if not custo_hora`.

Consequentemente, custo igual a zero é tratado como custo ausente.

## 7.3 Estado dos insumos

A composição utiliza a chave global de sessão `insumos_editados`.

A chave não inclui o código do orçamento.

O dashboard limpa `orcamento` ao iniciar novo orçamento, mas não limpa `insumos_editados`.

Consequência observada:

uma composição de insumos pode permanecer na interface ao trocar de orçamento dentro da mesma sessão.

A etapa não restaura uma composição previamente salva a partir dos dados do orçamento.

## 7.4 Cálculo

O custo dos insumos é calculado por:

`quantidade × preço unitário`

O custo da equipe é calculado por:

`custo por hora × horas por dia × número de dias`

O total do barrilete é:

`total dos insumos + custo total da equipe`

A etapa atualiza apenas `st.session_state.orcamento` com:

- `insumos`;
- `custo_insumos`;
- `custo_equipe_total`;
- `custo_total_barrilete`;
- `dias_barrilete`;
- `horas_dia_barrilete`.

## 7.5 Finalização

O botão `Finalizar` apenas exibe a mensagem:

`Orçamento finalizado`

Ele não:

- chama `salvar_github()`;
- atualiza `data/orcamentos.csv`;
- muda `Status` para `Finalizado`;
- muda `Etapa_Atual` para `Etapa 3`;
- grava custos ou composição do barrilete;
- atualiza `Ultima_Atualizacao`;
- limpa o estado de sessão;
- retorna ao dashboard.

A finalização observada é apenas visual.

O registro persistido permanece no último estado salvo pela Etapa 2.

---

# 8. Relação entre Orçamentos e Obras

A tela `obras` lê diretamente `data/orcamentos.csv`.

Não foi observado cadastro operacional separado de obras nessa tela.

Consequências observadas:

- rascunhos de orçamento aparecem na lista de obras;
- a tela Obras depende do ciclo de vida de Orçamentos;
- não existe distinção estrutural nessa tela entre orçamento, proposta e obra contratada;
- não existe filtro por status.

---

# 9. Observações Técnicas

## OT-034 — Salvamento de orçamento duplicado entre etapas

As Etapas 0, 1 e 2 possuem implementações locais distintas para atualizar ou incluir o orçamento em `data/orcamentos.csv`.

A intenção é semelhante, mas não existe uma única função compartilhada para o domínio.

Não consolidar sem auditoria de compatibilidade entre os tratamentos atualmente aplicados.

## OT-035 — Código sequencial dependente da última linha

A geração do próximo código usa o código da última linha encontrada para o ano atual.

Ela não calcula explicitamente o maior número existente e não valida unicidade antes de salvar.

## OT-036 — Parâmetros técnicos embutidos na interface

Eficiência por desaguamento, dias mensais e desconto fixo de almoço estão definidos diretamente no código da Etapa 1.

Esses valores não são carregados de uma base de parâmetros observada.

## OT-037 — `custo_mensal_equipe` recebe valor por hora

A Etapa 2 grava em `custo_mensal_equipe` o mesmo valor de `Custo_Hora_Equipe` e `custo_hora_equipe`.

O nome do campo não corresponde à unidade persistida.

## OT-038 — Etapa 3 também administra a base mestre de insumos

A mesma tela responsável pelo cálculo do barrilete permite modificar e substituir integralmente `data/insumos.csv`.

Não existe permissão separada observada para essa manutenção.

## OT-039 — Estado dos insumos não é isolado por orçamento

A chave `insumos_editados` é global na sessão e não inclui o código do orçamento.

A troca de orçamento não limpa explicitamente esse estado.

## OT-040 — Etapa 3 não restaura composição persistida

A Etapa 3 inicializa a composição com a base mestre e quantidades zero quando `insumos_editados` não existe.

Não foi observado carregamento de uma composição anteriormente gravada no orçamento.

## OT-041 — Finalização apenas visual

O botão Finalizar da Etapa 3 exibe mensagem de sucesso, mas não persiste os dados da etapa e não altera o estado do orçamento.

## OT-042 — Tela Obras utiliza `data/orcamentos.csv`

A tela Obras não usa um cadastro próprio observado.

Ela apresenta diretamente os registros existentes no arquivo de Orçamentos.

## OT-043 — Proteção de Orçamentos concentrada no menu

A permissão do módulo é consultada para exibir o card no menu.

Não foi observada nova validação dentro do dashboard ou das etapas.

---

# 10. Perguntas em Aberto

## PA-026 — Ciclo de vida oficial do orçamento

Definir os estados oficiais do orçamento e o evento que realiza cada transição.

## PA-027 — Escopo completo após o barrilete

Confirmar se o fluxo termina na Etapa 3 ou se ainda deve incluir equipamentos, combustível, mobilização, impostos, BDI, margem, preço de venda ou outros componentes.

## PA-028 — Permissão para administrar insumos

Confirmar quais perfis podem alterar a base mestre `data/insumos.csv`.

## PA-029 — Relação entre orçamento e obra

Definir se `data/orcamentos.csv` deve continuar sendo a fonte da tela Obras ou se orçamento e obra contratada devem possuir cadastros distintos.

## PA-030 — Unidade correta de `custo_mensal_equipe`

Confirmar se o campo deveria representar custo mensal ou se é apenas um alias histórico de custo por hora.

## PA-031 — Origem oficial dos parâmetros técnicos

Confirmar se os mapas e valores fixos da Etapa 1 são regras oficiais, aproximações operacionais ou parâmetros provisórios.

## PA-032 — Estratégia definitiva de geração de códigos

Definir se o código deve ser sequencial por ano, globalmente único ou baseado em outro identificador.

## PA-033 — Persistência histórica das bases técnicas

Definir se cada orçamento deve preservar uma fotografia dos parâmetros e preços utilizados ou se deve sempre refletir mudanças posteriores nas bases mestres.

---

# 11. Baby step seguro

O primeiro baby step funcional recomendado é tornar a finalização da Etapa 3 real e verificável, sem realizar simultaneamente uma refatoração estrutural do módulo.

Esse passo deve:

1. persistir os dados calculados na Etapa 3;
2. atualizar `Etapa_Atual`;
3. atualizar `Status` conforme regra de negócio confirmada;
4. atualizar `Ultima_Atualizacao`;
5. verificar o retorno da gravação antes de exibir sucesso;
6. definir a navegação posterior.

A execução desse baby step depende primeiro da confirmação das regras registradas nas perguntas em aberto.
