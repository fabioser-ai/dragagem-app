# AUDIT_044 — Auditoria Arquitetural do Módulo Férias

Data: 2026-07-11

## Status e escopo

- Auditoria concluída.
- Nenhum comportamento funcional foi alterado.
- Escopo: entrada, autorização, cadastro de férias, cálculo de prazos, folgas, alertas, e-mail, persistência e uso organizacional por Prestação de Contas.

## Componentes diretamente envolvidos

- `pages/ferias.py`;
- `services/github.py`;
- `services/email_service.py`;
- `services/permissoes.py`;
- `pages/prestacao_contas.py`;
- `data/ferias.csv`;
- `data/folgas.csv`.

## 1. Entrada e autorização

O menu expõe Férias quando `pode_acessar_modulo("ferias")` retorna verdadeiro. O roteador principal chama `ferias.render()` para a rota `ferias`.

O perfil global `funcionario` é impedido de alcançar essa rota pelo bloqueio geral de `app.py`. Dentro de `pages/ferias.py` não existe nova validação de permissão nem autorização granular por operação.

Quem alcança a tela pode visualizar, incluir, editar e excluir férias e folgas, além de disparar manualmente alertas por e-mail quando a configuração SMTP está disponível.

## 2. Modelo de dados

### Férias

Schema observado:

- `Matricula`;
- `Funcionario`;
- `Unidade`;
- `Departamento`;
- `Periodo_Aquisitivo_Inicio`;
- `Periodo_Aquisitivo_Fim`;
- `Data_Inicio_Gozo`;
- `Data_Fim_Gozo`;
- `Dias_Gozo`;
- `Limite_Gozo`;
- `Periodo_Gozo`;
- `Situacao_Ferias`;
- `Situacao_Prazo`.

### Folgas

Schema observado:

- `Matricula`;
- `Funcionario`;
- `Unidade`;
- `Departamento`;
- `Data_Saida`;
- `Data_Retorno`;
- `Dias_Folga`;
- `Observacoes`;
- `Criado_Por`;
- `Data_Registro`.

Não existem IDs estáveis próprios para registros de férias ou folgas. A interface usa índice de DataFrame para edição e exclusão.

## 3. Matrícula como identidade compartilhada

A matrícula é usada para:

- localizar o funcionário ao criar folga;
- agrupar histórico e calcular próxima folga recomendada;
- detectar sobreposição de folgas;
- preencher funcionário, unidade e departamento em Prestação de Contas.

A criação e edição de férias não validam matrícula vazia, duplicada ou existente em `APP_USERS`. Apenas o nome do funcionário é obrigatório.

Consequência: matrículas duplicadas podem tornar relações ambíguas; matrícula vazia pode agrupar pessoas distintas; alteração de matrícula em Férias não reconcilia folgas ou despesas já registradas.

Prestação de Contas seleciona a primeira linha de `ferias.csv` que corresponda à matrícula da sessão. Caso existam duplicidades, a escolha é implícita pela ordem atual do CSV.

## 4. Cálculo de férias

`calcular_status()` usa a data atual, o fim do período aquisitivo e o limite de gozo.

- `Férias Vencidas` é atribuído quando hoje é maior ou igual ao fim do período aquisitivo.
- `Férias em Dobro` é atribuído quando hoje ultrapassa o limite de gozo.
- `Atenção` é atribuído quando faltam 60 dias ou menos para o limite.
- Quando o limite não existe, o código usa `periodo_fim + 335 dias`.

A tela permite informar manualmente período aquisitivo, limite e período textual de gozo. Não existe validação observada para:

- fim anterior ao início;
- início de gozo posterior ao fim;
- quantidade legal de dias;
- coerência entre `Dias_Gozo` e `Periodo_Gozo`;
- sobreposição entre períodos de férias do mesmo funcionário.

Os status persistidos só são recalculados quando o registro é incluído ou editado. Na renderização, a interface usa os valores já armazenados; portanto, a passagem do tempo não atualiza automaticamente `Situacao_Ferias` e `Situacao_Prazo` no CSV.

Os dados atuais mostram registros cuja classificação persistida pode divergir da regra calculável a partir das datas, indicando dependência de atualização manual.

## 5. Controle de folgas

Folgas dependem da existência prévia do funcionário em `ferias.csv`.

A interface:

- calcula retorno como `Data_Saida + Dias_Folga`;
- recomenda intervalo de 60 dias entre saídas;
- alerta quando faltam 20 dias ou menos para a próxima data recomendada;
- impede sobreposição de folgas do mesmo número de matrícula;
- registra autor e data apenas na criação.

O intervalo de 60 dias é tratado como recomendação visual: uma folga dentro desse intervalo continua podendo ser salva, desde que não haja sobreposição.

Na edição, autor e data de criação não são atualizados e não existem campos próprios de autor/data da alteração.

Excluir uma linha de férias não exclui nem bloqueia folgas relacionadas. Alterar nome, unidade, departamento ou matrícula no cadastro de férias não propaga alterações aos registros históricos de folgas, que mantêm cópias textuais desses dados.

## 6. Persistência e schema

`normalizar_dataframe()` cria colunas ausentes, reduz o DataFrame ao schema declarado e converte colunas para `object`.

Consequências:

- colunas extras podem desaparecer na gravação seguinte;
- leitura ambígua como DataFrame vazio pode preceder sobrescrita integral;
- toda inclusão, edição ou exclusão regrava o CSV completo;
- não existe locking, transação, retry ou releitura de confirmação.

Mensagens de sucesso são apresentadas após retorno sem exceção de `salvar_github()`, sem confirmar por nova leitura o conteúdo persistido.

## 7. Exclusão e rastreabilidade

Férias e folgas podem ser excluídas fisicamente, sem confirmação adicional.

Férias não registram autor, data de criação, data de alteração ou justificativa. Folgas registram `Criado_Por` e `Data_Registro`, mas não histórico de edição ou exclusão.

Não existe política de inativação ou preservação histórica para cadastros usados por Prestação de Contas.

## 8. Alertas por e-mail

O envio é manual pela interface e depende de secrets SMTP.

`services/email_service.py`:

- usa SMTP com STARTTLS;
- autentica com usuário e senha;
- envia texto simples;
- não define timeout explícito;
- não registra evento de envio em arquivo ou domínio próprio.

O conteúdo inclui nome, matrícula, unidade, departamento e datas de funcionários em situação crítica. A tela permite visualizar o corpo antes do envio.

## 9. Papel como fonte organizacional

`data/ferias.csv` não contém apenas informações de férias. Ele atua também como cadastro de funcionário, unidade e departamento para Prestação de Contas.

Esse acoplamento faz com que:

- editar dados organizacionais em Férias altere o preenchimento de novas despesas;
- excluir funcionário possa remover a fonte de unidade e departamento;
- falhas ou duplicidades em Férias afetem outro módulo;
- um domínio trabalhista seja usado como cadastro mestre de pessoas sem contrato arquitetural explícito.

## 10. Observações Técnicas

### OT-095 — Férias funciona também como cadastro organizacional

Prestação de Contas usa `ferias.csv` para obter funcionário, unidade e departamento.

### OT-096 — Matrícula é chave informal sem validação de unicidade

Férias, folgas e despesas dependem da matrícula, mas o cadastro não garante preenchimento ou unicidade.

### OT-097 — Registros não possuem ID estável

Edição e exclusão usam índice de DataFrame.

### OT-098 — Status persistidos envelhecem

Situações de férias são recalculadas apenas em inclusão ou edição, não automaticamente com a passagem do tempo.

### OT-099 — Regras de datas são parcialmente validadas

Não há validação completa de coerência entre períodos aquisitivos, gozo, limite e quantidade de dias.

### OT-100 — Intervalo de folga é recomendação, não bloqueio

A regra de 60 dias produz alertas, mas não impede salvamento.

### OT-101 — Alterações de funcionário não reconciliam históricos

Mudanças em matrícula ou dados organizacionais não propagam para folgas e despesas existentes.

### OT-102 — Exclusões são físicas e sem confirmação

Férias e folgas podem ser removidas sem trilha de domínio.

### OT-103 — Normalização pode descartar colunas desconhecidas

Os CSVs são reduzidos aos schemas declarados antes da gravação.

### OT-104 — Alertas por e-mail não possuem trilha própria

O envio manual não é persistido como evento auditável.

## 11. Perguntas em aberto

- Qual é a fonte oficial de funcionários, matrícula, unidade e departamento?
- Matrícula deve ser obrigatória e única?
- Férias e folgas precisam de IDs estáveis?
- Os status devem ser calculados em tempo de leitura ou persistidos e atualizados automaticamente?
- Qual regra legal e operacional define `Limite_Gozo` e `Férias em Dobro`?
- Deve haver validação de sobreposição entre períodos de férias?
- O intervalo de 60 dias entre folgas é recomendação ou regra impeditiva?
- Como tratar alteração ou exclusão de funcionário com folgas e despesas relacionadas?
- Quem pode visualizar, editar, excluir e enviar alertas?
- Os envios de alerta precisam de histórico, destinatários e resultado persistidos?

## 12. Baby step seguro

Definir e documentar a identidade canônica do funcionário antes de alterar cálculos ou telas.

O primeiro passo deve decidir se matrícula é obrigatória e única e qual fonte é responsável por nome, unidade e departamento. Depois, validar duplicidades e referências existentes sem alterar ainda registros históricos ou regras de férias.