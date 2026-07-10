# Auditoria Arquitetural — Prestação de Contas

Data: 2026-07-10

## Status

- Auditoria concluída.
- Consolidação em `docs/ARCHITECTURE_CURRENT.md` pendente.

## Escopo auditado

- entrada pelo menu e roteamento;
- autorização por perfil;
- identificação do usuário e dados funcionais;
- cadastro de nova despesa;
- upload, persistência e leitura de comprovantes;
- consulta das despesas próprias;
- consulta e análise administrativa;
- aprovação, reprovação e pagamento;
- cadastro de tipos de despesa;
- persistência e estados gerados;
- tratamento de erros e efeitos colaterais.

## Componentes diretamente envolvidos

- `app.py`
- `pages/menu.py`
- `pages/prestacao_contas.py`
- `pages/ferias.py`
- `services/auth.py`
- `services/permissoes.py`
- `services/github.py`

## Arquivos de dados

- `data/prestacao_contas.csv`
- `data/tipos_despesa.csv`
- `data/ferias.csv`
- `data/comprovantes/`

## Entrada e autorização

O cartão do módulo é apresentado pelo menu quando `pode_acessar_modulo("prestacao_contas")` retorna verdadeiro. O roteador principal chama `pages.prestacao_contas.render()` quando `st.session_state.tela == "prestacao_contas"`.

O perfil global define as abas:

- `funcionario`: Nova Despesa e Minhas Despesas;
- `admin`: Todas as Despesas, Nova Despesa, Minhas Despesas e Tipos de Despesa;
- demais perfis: Nova Despesa e Minhas Despesas.

As funções administrativas `render_todas_despesas()` e `render_tipos_despesa()` executam novamente `exigir_admin()`. Essa função autoriza apenas quando `st.session_state.perfil == "admin"`.

Consequência observada: um perfil global `superadmin` não é aceito por `exigir_admin()` e recebe bloqueio nas funções administrativas, mesmo que o menu possa lhe conceder acesso geral ao módulo por outra regra.

## Identificação do funcionário

`obter_dados_funcionario()` lê da sessão:

- `matricula`;
- `nome`;
- `usuario`.

Em seguida, importa `pages.ferias` e consulta o arquivo usado pelo módulo Férias para buscar funcionário, unidade e departamento pela matrícula.

Se a leitura falhar, se não houver correspondência ou se ocorrer qualquer exceção, retorna os dados da sessão e deixa unidade e departamento vazios.

A dependência de Prestação de Contas com o cadastro funcional está, portanto, acoplada ao arquivo e à constante pertencentes ao módulo Férias.

## Nova despesa

A criação de despesa recebe:

- data;
- tipo ativo;
- valor;
- descrição opcional;
- comprovante opcional em PNG, JPG, JPEG ou PDF.

O valor deve ser maior que zero. Não foi observada validação obrigatória para descrição, matrícula, unidade, departamento ou comprovante.

O identificador é um UUID textual.

Estado inicial:

- `Status = Pendente`;
- `Aprovado_Por` vazio;
- `Data_Aprovacao` vazia;
- `Observacoes_Aprovacao` vazia.

A nova linha é adicionada ao DataFrame completo e `data/prestacao_contas.csv` é substituído integralmente.

## Comprovantes

Quando há upload, `salvar_comprovante()` cria o nome usando:

- data e hora até segundos;
- UUID da despesa;
- nome original parcialmente sanitizado.

O arquivo é salvo em `data/comprovantes/` antes da gravação da linha no CSV.

Consequência observada: se o comprovante for salvo com sucesso e a gravação posterior do CSV falhar, o arquivo binário permanece sem referência no cadastro de despesas.

O nome original substitui espaços e separadores de caminho, mas outros caracteres não são normalizados.

Na leitura:

- imagens são exibidas e podem ser baixadas;
- PDFs apenas podem ser baixados;
- outros formatos recebem download genérico, embora o uploader da criação limite os tipos aceitos.

## Minhas despesas

A consulta pessoal filtra exclusivamente por correspondência exata entre:

- `Criado_Por` do CSV;
- `st.session_state.usuario`.

Ela não usa matrícula ou UUID do usuário.

A tela mostra o total de todas as despesas do usuário, independentemente do status. Portanto, pendentes, aprovadas, reprovadas e pagas entram no mesmo indicador.

A escolha do comprovante usa o índice atual do DataFrame incorporado ao texto da opção. Depois recupera a linha com `df.loc[idx]`.

## Todas as despesas

A tela administrativa permite filtrar por:

- status;
- funcionário;
- tipo de despesa.

Os filtros usam comparação textual exata e não normalizam caixa ou espaços.

Os indicadores calculam:

- total financeiro filtrado, incluindo todos os status;
- quantidade de pendentes;
- quantidade de aprovadas;
- quantidade de reprovadas.

O status `Pago` não possui indicador de quantidade próprio, embora seu valor participe do total financeiro.

A seleção administrativa também incorpora o índice do DataFrame à opção visual e recupera a linha original por `df.loc[idx]`.

## Estados e decisões administrativas

A mesma tela pode definir diretamente qualquer despesa como:

- `Aprovado`;
- `Reprovado`;
- `Pago`.

Não existem validações de transição de estado. Assim, o código permite, por exemplo:

- marcar uma despesa pendente diretamente como paga;
- transformar uma despesa reprovada em paga;
- transformar uma despesa paga novamente em aprovada ou reprovada.

As três decisões reutilizam os campos:

- `Aprovado_Por`;
- `Data_Aprovacao`;
- `Observacoes_Aprovacao`.

Consequências observadas:

- uma reprovação é registrada nos campos nomeados como aprovação;
- o pagamento sobrescreve responsável, data e observações da decisão anterior;
- não existe histórico de transições;
- não existem campos próprios para pagador ou data de pagamento.

Não foi observada exigência de justificativa para reprovar.

## Tipos de despesa

A tela administrativa:

- lista os tipos;
- cria novos tipos;
- rejeita duplicidade ignorando caixa.

Novos tipos nascem com `Ativo = Sim`.

Apesar de o schema possuir a coluna `Ativo`, a tela auditada não oferece ação para:

- editar tipo;
- editar descrição;
- ativar;
- desativar;
- excluir.

A criação de despesa reconhece como ativo apenas o valor textual que, convertido para minúsculas, seja exatamente `sim`.

## Persistência e concorrência

CSV e comprovantes são persistidos diretamente pela tela através de `services/github.py`.

As decisões administrativas e a criação de despesas substituem integralmente `data/prestacao_contas.csv`. Não existe locking, transação ou reconciliação de alterações concorrentes.

O upload do comprovante e a gravação da linha são duas operações separadas e não atômicas.

## Tratamento de erros

Foi observado tratamento desigual:

- a obtenção de dados funcionais captura qualquer exceção e usa fallback silencioso;
- o upload do comprovante captura erro e impede a criação da linha;
- a gravação do CSV da despesa não possui `try/except` local;
- as decisões administrativas não possuem `try/except` local;
- a leitura do comprovante apresenta erro ao usuário;
- leituras CSV herdam do serviço central o comportamento de retornar DataFrame vazio para respostas HTTP diferentes de 200.

## O que foi aprendido

1. O módulo concentra criação, consulta, análise, pagamento e cadastro auxiliar em um único arquivo de tela.
2. Existe defesa administrativa dentro das funções críticas, além da seleção de abas por perfil.
3. A despesa nasce independente de aprovação e usa UUID.
4. O comprovante binário é persistido antes da linha do CSV.
5. A máquina de estados não possui transições protegidas nem histórico.
6. Aprovação, reprovação e pagamento compartilham campos de auditoria que não representam corretamente todos os eventos.
7. Os dados funcionais dependem do cadastro mantido pelo módulo Férias.
8. A consulta pessoal usa `Criado_Por`, e não matrícula.
9. Tipos podem ser criados, mas não administrados além da inclusão.

## O que ainda não foi compreendido

1. Se `superadmin` deve possuir as mesmas capacidades do perfil global `admin` neste módulo.
2. Se comprovante deve ser obrigatório para todos ou apenas alguns tipos.
3. Se a despesa pode ser marcada como paga sem aprovação anterior.
4. Se uma decisão administrativa pode ser revertida.
5. Se é necessário preservar histórico de aprovação, reprovação e pagamento.
6. Se valores reprovados devem participar do indicador financeiro total.
7. Se Prestação de Contas deve depender do cadastro de Férias ou de um cadastro funcional compartilhado.
8. Se o usuário deve poder corrigir ou cancelar uma despesa pendente.
9. Se tipos de despesa precisam de edição e ativação/desativação pela interface.

## Observações Técnicas propostas

- OT-045 — Prestação de Contas concentra múltiplas responsabilidades em uma tela.
- OT-046 — Dados funcionais dependem do cadastro do módulo Férias.
- OT-047 — Comprovante e registro CSV não formam operação atômica.
- OT-048 — Consulta pessoal identifica autoria por `Criado_Por`.
- OT-049 — Indicadores financeiros incluem todos os estados.
- OT-050 — Transições de status não possuem restrições.
- OT-051 — Campos de aprovação registram reprovação e pagamento.
- OT-052 — Pagamento sobrescreve auditoria da decisão anterior.
- OT-053 — Tipos de despesa possuem ativação no schema, mas não gestão completa na tela.
- OT-054 — `exigir_admin()` aceita somente perfil global `admin`.
- OT-055 — Seletores de despesa dependem do índice do DataFrame.

## Perguntas em Aberto propostas

- PA-036 — Relação entre `superadmin` e `admin` em Prestação de Contas.
- PA-037 — Obrigatoriedade do comprovante.
- PA-038 — Máquina de estados da despesa.
- PA-039 — Histórico de decisões e pagamento.
- PA-040 — Regra dos indicadores financeiros por status.
- PA-041 — Fonte oficial dos dados funcionais.
- PA-042 — Correção ou cancelamento pelo usuário.
- PA-043 — Administração completa dos tipos de despesa.

## Baby step seguro

Antes de qualquer implementação funcional, documentar e confirmar a máquina de estados desejada para a despesa. A primeira correção futura deve impedir transições inválidas e preservar separadamente os eventos de aprovação, reprovação e pagamento.

## Próximo subsistema

CRM, após a consolidação desta auditoria e da auditoria de Orçamentos em `docs/ARCHITECTURE_CURRENT.md`.
