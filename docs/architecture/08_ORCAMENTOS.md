# Arquitetura Atual — Orçamentos

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_034_ORCAMENTOS.md`

## Visão geral

O módulo de Orçamentos é acessado pelo menu quando `pode_acessar_modulo("orcamento")` retorna verdadeiro. O roteamento principal usa `st.session_state.tela` para direcionar o usuário ao dashboard e às etapas 0 a 3.

Arquivos principais:

- `pages/orcamento/dashboard.py`
- `pages/orcamento/etapa0.py`
- `pages/orcamento/etapa1.py`
- `pages/orcamento/etapa2.py`
- `pages/orcamento/etapa3.py`

Persistência principal:

- `data/orcamentos.csv`

Bases auxiliares observadas:

- `data/clientes.csv`
- `data/materiais.csv`
- `data/desaguamento.csv`
- `data/medicao.csv`
- `data/horarios.csv`
- `data/dias.csv`
- `data/equipamentos.csv`
- `data/salarios.csv`
- `data/insumos.csv`

## Navegação e estado

O dashboard usa `st.session_state.modo_orcamento` para alternar entre início e continuação. O orçamento corrente é mantido em `st.session_state.orcamento`.

As etapas reconhecidas são:

- Etapa 0 — informações da obra;
- Etapa 1 — produção da draga;
- Etapa 2 — dimensionamento da equipe;
- Etapa 3 — custo do barrilete.

Não foi observada revalidação interna de permissão dentro das telas do módulo.

## Etapa 0 — Informações da obra

A etapa gera código no formato `D_NNN_ANO`, cadastra ou seleciona cliente, recebe os dados gerais da obra e salva o orçamento como `Rascunho` em `data/orcamentos.csv`.

Fatos observados:

- a sequência depende da última linha encontrada para o ano;
- não há busca explícita pelo maior número;
- salvar novamente a etapa regrava `Data_Criacao`;
- diversos campos não possuem validação obrigatória;
- a gravação substitui integralmente o CSV.

## Etapa 1 — Produção da draga

O cálculo observado usa vazão, eficiência, concentração, horário e dias mensais fixos.

Fatos observados:

- minutos do horário são ignorados;
- existe desconto fixo de uma hora de almoço;
- os dias mensais são mapeados para 22, 26 ou 30;
- vazão, eficiência e concentração podem ser alteradas manualmente;
- a sessão é atualizada durante a renderização, mas a persistência ocorre em “Salvar e continuar”.

## Etapa 2 — Equipe

A equipe é calculada a partir da base de salários, quantidade por posição, leis sociais e adicional opcional de 25%.

Fatos observados:

- a composição é serializada em JSON dentro de `data/orcamentos.csv`;
- existem campos de compatibilidade em minúsculas;
- `custo_mensal_equipe` recebe o mesmo valor do custo por hora;
- a chave de edição da equipe é isolada pelo código do orçamento.

## Etapa 3 — Barrilete

A tela edita a base global de insumos e calcula a composição do barrilete do orçamento corrente.

Fatos observados:

- a tela mistura administração global de insumos e composição do orçamento;
- `st.session_state.insumos_editados` não é isolado por orçamento;
- os resultados são colocados somente na sessão;
- o botão “Finalizar” apenas exibe mensagem de sucesso;
- não há gravação de `Status = Finalizado`;
- não há persistência da composição nem dos custos da etapa;
- não há atualização de `Etapa_Atual` ou `Ultima_Atualizacao` na finalização.

## Persistência

O módulo não possui repositório ou serviço único. As etapas mantêm implementações próprias de salvamento do agregado em `data/orcamentos.csv`.

As implementações não são equivalentes: a Etapa 2 possui tratamento adicional para colunas, valores nulos, listas e dicionários.

## Observações técnicas consolidadas

- Orçamentos não possui repositório ou serviço próprio.
- O salvamento do agregado está duplicado entre etapas.
- A data de criação é sobrescrita ao salvar novamente a Etapa 0.
- A geração de código depende da última linha do ano.
- O cálculo de horário e calendário mensal é simplificado.
- `custo_mensal_equipe` contém custo horário.
- A Etapa 3 mistura cadastro global e composição.
- O estado de insumos não é isolado por orçamento.
- A finalização não é persistida.
- As telas internas não revalidam permissão.
- Os dados da Etapa 3 permanecem apenas na sessão.

## Perguntas em aberto

- Qual é o escopo final do fluxo de Orçamentos?
- Quais campos são obrigatórios?
- Qual é a unidade econômica do custo do barrilete?
- Qual deve ser o ciclo de vida do orçamento?
- O orçamento finalizado pode ser reaberto?
- Qual deve ser a regra de geração e unicidade do código?
- A administração de insumos deve permanecer na Etapa 3?
- Qual é o significado correto de `custo_mensal_equipe`?
- Como a composição do barrilete deve ser persistida e restaurada?
- O cálculo de dias deve usar calendário real?
- Deve existir defesa interna de autorização?

## Baby step seguro futuro

Persistir a conclusão da Etapa 3 somente após confirmar que essa etapa representa o encerramento oficial do orçamento e definir o significado econômico do barrilete.