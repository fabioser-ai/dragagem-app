# Arquitetura Atual — Obras

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_045_OBRAS.md`

## Visão geral

A rota Obras é uma consulta somente leitura implementada diretamente em `app.py`.

Ela não possui página, serviço ou repositório próprio.

## Entrada e autorização

O menu exibe Obras quando `pode_acessar_modulo("obras")` retorna verdadeiro.

O perfil global `funcionario` é bloqueado pelo roteador principal. Dentro da rota não existe revalidação da permissão geral nem autorização granular por registro, ação ou obra.

Quem alcança a rota visualiza todas as linhas e todas as colunas da fonte carregada.

## Fonte exibida

A rota define:

```text
ARQ_OBRAS = data/orcamentos.csv
```

Portanto, a lista exibida é formada pelos agregados do módulo Orçamentos.

O arquivo contém proposta, estágio do orçamento, parâmetros técnicos, produção calculada, equipe serializada e custos.

A rota não filtra status. Registros em `Rascunho` também aparecem como obras.

## Comportamento

A tela:

1. lê `data/orcamentos.csv`;
2. quando o resultado está vazio, informa que não existem obras cadastradas;
3. caso contrário, exibe o DataFrame integral;
4. permite apenas voltar ao menu.

Não existem busca, filtros de domínio, detalhe, edição, criação, arquivamento, indicadores ou integração navegável com Medições.

## Divergência entre descrição e implementação

O cartão do menu descreve Obras como acompanhamento operacional, histórico e gestão.

A implementação observada é somente uma tabela bruta de Orçamentos.

Não existe acompanhamento operacional ou gestão própria na rota.

## Dois conceitos de obra

Medições usa um cadastro diferente:

```text
data/obras.csv
```

Esse arquivo possui `obra_id`, contratante, contrato, objeto, cidade, status, modelo de medição e tabela contratual.

Orçamentos usa `Codigo` no formato `D_NNN_ANO`.

Não foi observado vínculo entre `Codigo` de Orçamentos e `obra_id` de Medições, nem conversão explícita de orçamento aprovado em obra operacional.

Assim, coexistem:

- obra proposta dentro de um orçamento;
- obra operacional usada por Medições.

A rota Obras apresenta apenas o primeiro conceito.

## Exposição de dados

A tabela mostra o agregado integral, incluindo:

- parâmetros técnicos;
- equipe em JSON;
- custo-hora;
- leis sociais;
- demais resultados intermediários.

Não existe política observada de seleção de colunas por perfil.

## Tratamento de erros

Qualquer exceção na leitura é convertida em DataFrame vazio.

Falhas de autenticação, rede, API, arquivo ou conteúdo podem ser apresentadas como “Nenhuma obra cadastrada ainda”.

Como a rota é somente leitura, não há escrita destrutiva direta, mas existe risco de interpretação operacional incorreta.

## Identidade e permissões

A identidade da fonte exibida é `Codigo` do orçamento.

A identidade operacional de Medições é `obra_id`.

A rota não usa `pode_executar()` nem `obras_permitidas()`. O `obra_id` das permissões granulares não possui correspondência observada com o código exibido.

## Observações técnicas consolidadas

- Obras é uma rota embutida em `app.py`.
- A rota lê `data/orcamentos.csv`.
- Orçamentos em rascunho aparecem como obras.
- O cadastro operacional de Medições está em `data/obras.csv`.
- Não existe vínculo observado entre `Codigo` e `obra_id`.
- A descrição do menu não corresponde ao comportamento atual.
- Todos os campos do orçamento são expostos.
- Não existe autorização granular por registro ou campo.
- Falha de leitura é apresentada como ausência de obras.
- A identidade de obra não é canônica no sistema.

## Perguntas em aberto

- Obras representa propostas, contratos ganhos ou execuções?
- Qual cadastro é a fonte oficial da identidade de obra?
- Um orçamento aprovado deve gerar uma obra operacional?
- Qual vínculo deve existir entre `Codigo` e `obra_id`?
- Quais estados e campos podem aparecer para cada perfil?
- A rota deve usar permissões por obra?
- O cadastro operacional deve pertencer a Obras ou a Medições?

## Baby step seguro futuro

Definir formalmente o significado do módulo Obras e escolher sua fonte canônica antes de alterar a rota.

Somente depois decidir entre resumir e filtrar Orçamentos, exibir o cadastro operacional de Medições ou relacionar explicitamente ambos.
