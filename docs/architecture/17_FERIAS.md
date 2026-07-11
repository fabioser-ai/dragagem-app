# Arquitetura Atual — Férias

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_044_FERIAS.md`

## Visão geral

O módulo Férias mantém dois domínios relacionados:

- controle de férias;
- controle de folgas.

Além disso, `data/ferias.csv` funciona como fonte organizacional de matrícula, nome, unidade e departamento para Prestação de Contas.

## Arquivos principais

- `pages/ferias.py`;
- `services/github.py`;
- `services/email_service.py`;
- `pages/prestacao_contas.py`.

## Arquivos de dados

- `data/ferias.csv`;
- `data/folgas.csv`.

## Entrada e autorização

O menu exibe Férias quando `pode_acessar_modulo("ferias")` retorna verdadeiro. O perfil global `funcionario` é impedido de alcançar a rota pelo bloqueio geral do roteador.

Dentro do módulo não existe revalidação da permissão geral nem autorização granular por operação. Quem alcança a tela pode executar as ações expostas de inclusão, edição, exclusão e envio manual de alerta.

## Modelo de férias

Campos principais:

- matrícula;
- funcionário;
- unidade;
- departamento;
- período aquisitivo;
- período de gozo;
- dias de gozo;
- limite de gozo;
- situação de férias;
- situação de prazo.

Os registros não possuem ID estável próprio. Edição e exclusão usam o índice atual do DataFrame.

Somente o nome do funcionário é obrigatório na criação. Matrícula não é validada como preenchida ou única.

## Cálculo de status

A situação usa a data atual, o fim do período aquisitivo e o limite de gozo:

- hoje maior ou igual ao fim do período: `Férias Vencidas`;
- hoje posterior ao limite: `Férias em Dobro`;
- até 60 dias para o limite: `Atenção`;
- demais casos: `Dentro do Prazo`.

Quando o limite não existe, o cálculo usa `periodo_fim + 335 dias`.

Os status são persistidos e só são recalculados na inclusão ou edição. A passagem do tempo não atualiza automaticamente os valores gravados no CSV.

Não existe validação completa de coerência entre início e fim dos períodos, datas de gozo, limite e quantidade de dias.

## Controle de folgas

Folgas dependem dos funcionários presentes em `ferias.csv`.

A interface:

- calcula data de retorno;
- impede sobreposição de folgas para a mesma matrícula;
- recomenda intervalo de 60 dias entre saídas;
- alerta quando faltam 20 dias ou menos para a próxima data recomendada;
- registra autor e data na criação.

O intervalo de 60 dias é apenas recomendação visual e não bloqueia o salvamento.

Folgas não possuem ID estável. Edição e exclusão usam índice de DataFrame.

Alterações posteriores em matrícula, nome, unidade ou departamento no cadastro de férias não são propagadas para folgas já registradas.

## Identidade compartilhada

A matrícula é usada como chave informal entre:

- férias;
- folgas;
- Prestação de Contas.

Prestação de Contas busca em `ferias.csv` a primeira linha cuja matrícula corresponde à sessão e usa essa linha para preencher nome, unidade e departamento.

Como não existe validação de unicidade, duplicidades podem gerar escolha implícita pela ordem do arquivo. Matrícula vazia pode agrupar registros de pessoas diferentes.

## Persistência

Férias e folgas usam `services/github.py` e regravam os CSVs integralmente.

A normalização:

- cria colunas ausentes;
- reduz o DataFrame ao schema declarado;
- pode descartar colunas extras.

Persistem os riscos transversais já registrados:

- leitura ambígua como arquivo vazio;
- sobrescrita integral;
- ausência de locking, transação, retry e releitura de confirmação.

## Exclusão e histórico

Férias e folgas podem ser excluídas fisicamente sem confirmação adicional.

Férias não registram autor ou timestamps. Folgas registram autor e data apenas na criação, sem histórico de edição ou exclusão.

Excluir férias não reconcilia folgas nem despesas relacionadas.

## Alertas por e-mail

O envio é manual e depende de secrets SMTP.

O serviço usa SMTP com STARTTLS e autenticação por usuário e senha. Não existe timeout explícito nem histórico persistido do envio.

O corpo pode conter nome, matrícula, unidade, departamento e datas de funcionários em situação crítica.

## Papel organizacional

`ferias.csv` atua simultaneamente como:

- controle trabalhista;
- cadastro de funcionário;
- fonte de unidade e departamento para Prestação de Contas.

Esse acoplamento não possui contrato arquitetural explícito e faz alterações ou falhas em Férias afetarem o preenchimento de novas despesas.

## Observações técnicas consolidadas

- Férias funciona também como cadastro organizacional.
- Matrícula é chave informal sem validação de unicidade.
- Registros de férias e folgas não possuem ID estável.
- Status persistidos podem envelhecer com a passagem do tempo.
- Regras de datas são parcialmente validadas.
- O intervalo de folga é recomendação, não bloqueio.
- Alterações de funcionário não reconciliam históricos.
- Exclusões são físicas e sem confirmação.
- A normalização pode descartar colunas desconhecidas.
- Alertas por e-mail não possuem trilha própria.

## Perguntas em aberto

- Qual é a fonte oficial de funcionários, matrícula, unidade e departamento?
- Matrícula deve ser obrigatória e única?
- Férias e folgas precisam de IDs estáveis?
- Status devem ser calculados em leitura ou atualizados automaticamente?
- Qual regra oficial define limite de gozo e férias em dobro?
- Deve existir validação de sobreposição de férias?
- O intervalo de 60 dias entre folgas é recomendação ou impedimento?
- Como tratar alterações e exclusões com folgas e despesas relacionadas?
- Quem pode editar, excluir e enviar alertas?
- Envios de e-mail precisam de histórico persistido?

## Baby step seguro futuro

Definir a identidade canônica do funcionário.

Antes de alterar cálculos ou telas, decidir se matrícula é obrigatória e única e qual fonte responde por nome, unidade e departamento. Em seguida, validar duplicidades e referências existentes sem alterar registros históricos.