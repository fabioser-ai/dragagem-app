# Arquitetura Atual — Prestação de Contas

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_035_PRESTACAO_CONTAS.md`

## Visão geral

O módulo concentra criação de despesas, upload e leitura de comprovantes, consulta pessoal, análise administrativa, aprovação, reprovação, pagamento e cadastro de tipos de despesa.

Arquivo principal:

- `pages/prestacao_contas.py`

Dependências diretas:

- `app.py`
- `pages/menu.py`
- `pages/ferias.py`
- `services/auth.py`
- `services/permissoes.py`
- `services/github.py`

Arquivos de dados:

- `data/prestacao_contas.csv`
- `data/tipos_despesa.csv`
- `data/ferias.csv`
- `data/comprovantes/`

## Entrada e autorização

O módulo é exibido pelo menu quando `pode_acessar_modulo("prestacao_contas")` retorna verdadeiro.

O perfil global `funcionario` recebe as abas Nova Despesa e Minhas Despesas. O perfil global `admin` recebe também Todas as Despesas e Tipos de Despesa.

As funções administrativas chamam `exigir_admin()`, que aceita exclusivamente `st.session_state.perfil == "admin"`.

## Identificação do funcionário

O módulo usa matrícula, nome e usuário da sessão. Para preencher funcionário, unidade e departamento, tenta localizar a matrícula no arquivo usado pelo módulo Férias.

Se essa busca falhar, usa nome e matrícula da sessão e deixa unidade e departamento vazios.

## Nova despesa

A criação recebe:

- data;
- tipo de despesa ativo;
- valor;
- descrição;
- comprovante opcional.

O ID é um UUID. O status inicial é `Pendente`.

O comprovante é salvo antes da inclusão da linha no CSV. Se o arquivo binário for salvo e a gravação do CSV falhar, pode permanecer comprovante órfão em `data/comprovantes/`.

## Comprovantes

Imagens PNG, JPG e JPEG são exibidas e podem ser baixadas. PDFs e demais extensões aceitas são disponibilizados para download.

O caminho persistido no CSV aponta para o arquivo dentro de `data/comprovantes/`.

## Minhas despesas

A consulta pessoal filtra pelo campo `Criado_Por`, comparando-o ao usuário da sessão.

O total exibido soma todas as despesas do usuário independentemente do status, incluindo despesas reprovadas.

## Administração

A tela administrativa permite filtrar por status, funcionário e tipo. Exibe total e quantidades de pendentes, aprovadas e reprovadas.

O total filtrado inclui todos os estados presentes no resultado.

A despesa selecionada pode ser marcada diretamente como:

- `Aprovado`;
- `Reprovado`;
- `Pago`.

Não existe validação de transição entre os estados.

## Campos de auditoria

Aprovação, reprovação e pagamento escrevem nos mesmos campos:

- `Aprovado_Por`;
- `Data_Aprovacao`;
- `Observacoes_Aprovacao`.

Marcar como pago sobrescreve os dados da decisão anterior. Não existe histórico de transições nem campos próprios para pagamento ou reprovação.

## Tipos de despesa

O cadastro permite adicionar novo tipo e grava `Ativo = Sim`.

Embora o schema possua a coluna `Ativo`, a interface auditada não oferece edição, desativação ou exclusão dos tipos existentes.

## Persistência

O módulo chama diretamente `services/github.py` para CSV e arquivos binários. As gravações do CSV substituem integralmente o arquivo.

Não existe transação entre o salvamento do comprovante e o registro da despesa.

## Observações técnicas consolidadas

- O comprovante pode ficar órfão quando a gravação do CSV falha.
- A máquina de estados não restringe transições.
- Pagamento pode ocorrer sem aprovação anterior.
- Aprovação, reprovação e pagamento compartilham os mesmos campos de auditoria.
- O pagamento sobrescreve a decisão anterior.
- Não existe histórico de transições.
- Minhas Despesas usa `Criado_Por`, não matrícula.
- Totais incluem despesas de todos os estados.
- Dados organizacionais dependem do arquivo do módulo Férias.
- `exigir_admin()` não aceita automaticamente um perfil global `superadmin`.
- Tipos de despesa só podem ser incluídos pela interface atual.

## Perguntas em aberto

- Qual é a máquina de estados oficial?
- Pagamento exige aprovação anterior?
- Decisões podem ser revertidas?
- Reprovação e pagamento precisam de campos próprios?
- Deve existir histórico de transições?
- Os totais devem excluir despesas reprovadas?
- A identidade da despesa própria deve usar matrícula, usuário ou ambos?
- Unidade e departamento devem depender do módulo Férias?
- O comprovante deve ser obrigatório?
- Como remover comprovantes órfãos?
- `superadmin` deve possuir acesso administrativo neste módulo?

## Baby step seguro futuro

Definir formalmente a máquina de estados antes de alterar o fluxo funcional. Uma sequência possível a validar é `Pendente → Aprovado → Pago`, com `Pendente → Reprovado` como desvio.