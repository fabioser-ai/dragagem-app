# AUDIT_045 — Auditoria Arquitetural da Rota Obras

Data: 2026-07-11

## Status e escopo

- Auditoria concluída.
- Nenhum comportamento funcional foi alterado.
- Escopo: entrada, autorização, roteamento, origem dos dados, apresentação, tratamento de erros, relação com Orçamentos, relação com o cadastro operacional de Medições e significado arquitetural do termo obra.

## Componentes diretamente envolvidos

- `app.py`;
- `pages/menu.py`;
- `services/permissoes.py`;
- `services/github.py`;
- `data/orcamentos.csv`;
- `data/obras.csv`;
- `pages/orcamento/etapa0.py`;
- `pages/orcamento/etapa1.py`;
- `pages/orcamento/etapa2.py`;
- `modulos/medicoes/config.py`;
- `modulos/medicoes/repositorio.py`.

## 1. Entrada e autorização

O menu exibe o cartão Obras quando `pode_acessar_modulo("obras")` retorna verdadeiro. O botão define `st.session_state.tela = "obras"`, e o roteador principal executa a implementação embutida diretamente em `app.py`.

O perfil global `funcionario` não pode alcançar a rota porque `obras` não pertence à lista geral de telas permitidas para esse perfil.

A rota não repete a validação de `pode_acessar_modulo("obras")` e não usa `pode_executar()`, `obras_permitidas()` ou qualquer filtro por usuário, recurso, ação ou obra.

Quem alcança a rota visualiza todas as linhas e todas as colunas do arquivo carregado.

## 2. Implementação e responsabilidade

Obras não possui página, serviço, repositório ou componente próprio. A implementação está dentro do bloco de roteamento de `app.py`.

Fluxo observado:

1. define `ARQ_OBRAS = "data/orcamentos.csv"`;
2. chama `carregar_github()`;
3. captura qualquer exceção e substitui o resultado por DataFrame vazio;
4. quando vazio, informa que nenhuma obra está cadastrada;
5. caso contrário, exibe o DataFrame integral com `st.dataframe()`;
6. oferece apenas retorno ao menu.

A rota é somente leitura pela interface observada. Não existem busca, filtro, ordenação de domínio, detalhe, edição, criação, arquivamento ou navegação para os módulos relacionados.

## 3. Origem real dos dados exibidos

A rota usa `data/orcamentos.csv`, arquivo persistido pelo fluxo de Orçamentos.

O schema atual contém, entre outros:

- `Codigo`;
- `Status`;
- `Etapa_Atual`;
- datas de criação e atualização;
- cliente;
- nome e local da obra proposta;
- volume, material e desaguamento;
- distâncias e desnível;
- sistema de medição;
- horário e dias;
- draga, vazão, eficiência e concentração;
- produção e prazo calculados;
- equipe serializada em JSON;
- custos e leis sociais.

O registro atual observado está em `Status = Rascunho` e `Etapa_Atual = Etapa 2`.

Portanto, a rota denominada Obras apresenta propostas orçamentárias, inclusive incompletas, e não um cadastro confirmado de contratos ou obras em execução.

## 4. Exposição integral do agregado de Orçamentos

A tabela não seleciona colunas próprias para consulta operacional. Ela exibe todo o agregado persistido por Orçamentos.

Consequências observadas:

- campos técnicos e financeiros são mostrados juntos;
- `Equipe_JSON` é exibido como texto serializado;
- custos de equipe e parâmetros de cálculo ficam disponíveis a qualquer usuário com acesso ao módulo Obras;
- não existe diferenciação entre informação resumida e detalhe sensível;
- não existe filtragem por status, cliente, responsável ou vínculo de obra.

A permissão `obras` controla acesso ao conjunto integral, mas não existe autorização granular para campos ou registros.

## 5. Dois cadastros distintos chamados de obra

Medições utiliza outro arquivo:

- `data/obras.csv`.

Esse cadastro possui identidade e schema próprios:

- `obra_id`;
- `nome_obra`;
- contratante;
- contrato;
- objeto;
- cidade;
- status;
- modelo de medição;
- arquivo de tabela de serviços;
- observações;
- timestamps.

O arquivo atual contém obras operacionais com IDs no formato `obra_<identificador>`.

Já Orçamentos usa `Codigo` no formato `D_NNN_ANO` e armazena o agregado de elaboração orçamentária.

Não foi observado, nos componentes auditados, campo que vincule:

- `Codigo` de `data/orcamentos.csv`;
- `obra_id` de `data/obras.csv`.

Também não foi observada conversão explícita de orçamento aprovado em obra operacional.

Assim, coexistem dois conceitos diferentes:

1. obra proposta dentro de um orçamento;
2. obra operacional usada por Medições.

A rota Obras apresenta apenas o primeiro conceito, enquanto sua descrição no menu promete acompanhamento operacional, histórico e gestão de obras cadastradas.

## 6. Divergência entre descrição e comportamento

O cartão do menu descreve Obras como:

> Acompanhamento operacional, histórico e gestão de obras cadastradas.

O comportamento observado oferece apenas uma tabela bruta e somente leitura de `data/orcamentos.csv`.

Não foram observados na rota:

- acompanhamento operacional;
- histórico próprio de obra;
- gestão do cadastro operacional;
- integração visual com Medições;
- status de execução contratual;
- responsável pela obra;
- vínculo de usuários;
- acesso à tabela contratual;
- indicadores ou evolução.

## 7. Tratamento de erros

A rota envolve a leitura em `try/except Exception` e transforma qualquer falha em DataFrame vazio.

Consequência: erro de autenticação, rede, API, arquivo inexistente ou CSV inválido pode ser apresentado ao usuário como “Nenhuma obra cadastrada ainda”.

A tela não registra o erro, não diferencia estados de leitura e não oferece tentativa explícita de recarga.

Como a rota é somente leitura, esse comportamento não causa escrita destrutiva diretamente nela. Porém, oculta indisponibilidade e pode induzir interpretação operacional incorreta.

## 8. Identidade, histórico e ciclo de vida

Na fonte exibida, a identidade é `Codigo` do orçamento. No cadastro de Medições, a identidade é `obra_id`.

Não existe identidade canônica transversal de obra registrada entre os dois domínios.

A rota também não define quais estados de orçamento qualificam um registro como obra. Atualmente, um `Rascunho` aparece como obra.

Não foi observada regra para:

- orçamento aprovado;
- orçamento convertido em contrato;
- criação de obra operacional;
- cancelamento;
- arquivamento;
- reconciliação entre proposta e execução.

## 9. Relação com permissões

`pode_acessar_modulo("obras")` verifica apenas módulo e ativação da linha de permissão.

Embora `services/permissoes.py` ofereça `pode_executar()` e `obras_permitidas()`, a rota não utiliza essas funções.

O campo `obra_id` das permissões granulares também pertence semanticamente ao cadastro operacional de Medições, enquanto a rota Obras exibe códigos de orçamento. Não existe correspondência observada entre esses identificadores.

## 10. Efeitos sistêmicos

- A rota pode levar usuários a interpretar orçamentos em elaboração como obras efetivas.
- A exposição integral pode revelar composição de equipe, parâmetros e custos a usuários que receberam apenas acesso geral ao módulo.
- A ausência de vínculo entre orçamento e obra operacional impede rastrear, pela rota, qual proposta originou qual execução.
- A divergência de identidade dificulta aplicar permissões por obra de forma uniforme.
- Uma falha de leitura pode simular ausência completa de obras.

## 11. Observações Técnicas

### OT-095 — Obras é uma rota embutida no roteador

Não existe módulo próprio; a implementação está diretamente em `app.py`.

### OT-096 — A rota lê o agregado de Orçamentos

`data/orcamentos.csv` é apresentado como lista de obras.

### OT-097 — Orçamentos rascunho são tratados visualmente como obras

A rota não filtra status nem etapa.

### OT-098 — O cadastro operacional de Medições é separado

Medições usa `data/obras.csv` com `obra_id` e schema próprio.

### OT-099 — Não existe vínculo observado entre orçamento e obra operacional

`Codigo` e `obra_id` coexistem sem referência cruzada confirmada.

### OT-100 — A descrição do menu não corresponde à funcionalidade

A promessa de acompanhamento, histórico e gestão não é atendida pela tabela somente leitura.

### OT-101 — Todos os campos do orçamento são expostos

A tabela inclui parâmetros técnicos, equipe serializada e custos.

### OT-102 — Não existe autorização granular por registro ou campo

A rota usa apenas o acesso geral ao módulo.

### OT-103 — Falha de leitura é apresentada como ausência de obras

Qualquer exceção é convertida em DataFrame vazio.

### OT-104 — Identidade de obra não é canônica no sistema

Orçamentos usa `Codigo`; Medições usa `obra_id`.

## 12. Perguntas em aberto

- O módulo Obras deve representar propostas orçamentárias, contratos ganhos ou obras em execução?
- Qual cadastro é a fonte oficial da identidade de obra?
- Um orçamento aprovado deve gerar automaticamente uma obra operacional?
- Qual vínculo deve existir entre `Codigo` e `obra_id`?
- Quais estados de orçamento podem aparecer em Obras?
- Quais campos podem ser exibidos a cada perfil?
- A rota deve usar as permissões por `obra_id`?
- O cadastro operacional deve ser administrado pela própria rota Obras ou por Medições?
- Como preservar histórico entre proposta, contratação, execução e medição?
- A descrição do cartão deve ser ajustada ao comportamento atual ou a funcionalidade deve evoluir para cumprir a descrição?

## 13. O que foi aprendido

- Obras é uma consulta bruta de Orçamentos, não um módulo operacional independente.
- O sistema possui dois cadastros de obra com identidades, schemas e finalidades diferentes.
- Não existe vínculo observado entre esses cadastros.
- A rota expõe todo o agregado orçamentário e mascara falhas de leitura como ausência de dados.

## 14. O que ainda não foi compreendido

- A regra de negócio para conversão de orçamento em obra.
- A fonte canônica da identidade de obra.
- O público autorizado a visualizar custos e composição.
- O ciclo de vida esperado entre proposta, contrato, execução e medição.

## 15. O que deve ser documentado

- definição oficial de obra no APP FOS;
- relação entre Orçamentos e Medições;
- identidade canônica e vínculo entre códigos;
- política de exposição de campos;
- estados que qualificam um registro como obra operacional.

## 16. Baby step seguro futuro

Antes de alterar a rota, definir formalmente o significado de “Obras” e escolher a fonte canônica exibida.

O primeiro passo deve ser documental: registrar se a rota é uma lista de propostas/orçamentos ou um cadastro de obras operacionais. Somente depois decidir entre filtrar e resumir `data/orcamentos.csv`, exibir `data/obras.csv` ou criar uma relação explícita entre ambos.
