# Composição de Orçamento — matriz de origem dos campos (v1)

**Estado:** análise documental, sem integração ativa nem migração de dados.  
**Escopo:** 19 campos da Etapa 1 e fontes candidatas para as demais etapas.  
**Base verificada:** código do repositório, não conteúdo dos CSVs operacionais. Uma fonte identificada não implica que tenha registros válidos.

## Regras de integração

1. CRM é a fonte preferencial de **identidade do cliente e contato**, vinculados por `id_cliente` e `id_contato`. Não reconciliar automaticamente nomes do cadastro legado.
2. Dados é a fonte preferencial de **catálogos técnicos e salários**; copiar para a proposta os valores efetivamente usados e registrar origem, data e eventual ajuste.
3. Dados específicos da obra permanecem editáveis. Não confundir endereço do cliente com local da execução.
4. Se a leitura de uma fonte falhar, **não** tratá-la como cadastro vazio nem substituir silenciosamente o valor anterior.
5. Proposta concluída é fotografia histórica: atualização de cadastros não a altera. Na duplicação, cotações exigem revisão manual; salários podem ser atualizados **mediante escolha explícita**, com registro do valor anterior.
6. Integração somente leitura nesta fase. Escrita em CRM, Dados e orçamento legado fica fora de escopo.
7. Respeitar RBAC e verificar a autorização para consulta entre módulos antes de disponibilizar dados.

## Etapa 1 — matriz de 19 campos

| Campo (ID) | Fonte no código | Chave/campo de origem | Política sugerida | Situação |
|---|---|---|---|---|
| `data_composicao` | Sistema | Data atual | Inicializar com data atual; editável; congelar na versão | Definido |
| `numero_proposta` | Orçamento legado `data/orcamentos.csv` | `Codigo` (formato `D_NNN_AAAA`) | **Não reutilizar como sequência nova** sem decisão; verificar unicidade e concorrência | Pendente |
| `cliente` | CRM `data/crm/clientes.csv`; legado `data/clientes.csv` | `id_cliente`, `nome_empresa`; legado `Cliente` | Seleção pelo ID do CRM; manter nome fotografado; reconciliar legado manualmente | Fonte confirmada |
| `contato` | CRM `data/crm/contatos.csv` | `id_contato`, `id_cliente`, `nome_contato` | Filtrar contatos por `id_cliente`; permitir ausência de contato; guardar ID e nome | Fonte confirmada |
| `objeto_obra` | Proposta | Texto específico | Manual; não inferir de `necessidade_cliente` do CRM | Manual |
| `local` | Proposta; CRM como sugestão | `cidade`, `estado`, `endereco_local` | Endereço do CRM é da empresa, **não** necessariamente da obra; confirmação manual | Sugestão condicionada |
| `volume_dragagem` | Proposta; histórico legado | `Volume` em `data/orcamentos.csv` | Manual ou copiar proposta explicitamente selecionada; unidade m³ | Manual |
| `tipo_material` | Dados `data/materiais.csv` | `Material` | Lista do cadastro, com possibilidade de exceção documentada; fotografar descrição | Fonte confirmada |
| `distancia_recalque_total` | Cálculo | `recalque_terra + recalque_flutuante` | Somente leitura; nunca terceira entrada independente | Calculado |
| `recalque_terra` | Proposta; histórico legado | `Terrestre` | Manual; histórico apenas na duplicação explícita | Manual |
| `recalque_flutuante` | Proposta; histórico legado | `Flutuante` | Manual; histórico apenas na duplicação explícita | Manual |
| `profundidade_dragagem` | Proposta | Sem equivalência comprovada | Manual, com unidade m | Manual |
| `espessura_media` | Proposta | Sem equivalência comprovada | Manual, com unidade m | Manual |
| `tipo_bota_fora` | Proposta | Sem cadastro específico comprovado | Manual até criar/identificar catálogo válido | Pendente |
| `sistema_medicao` | Proposta | Sem cadastro específico comprovado | Manual até definir opções e implicações comerciais | Pendente |
| `canteiro_obra` | Proposta | Sem correspondência comprovada | Manual; não confundir com `locais_trabalho` de RH | Pendente |
| `mobilizacao` | Proposta | Sem correspondência comprovada | Manual; especificar natureza/unidade antes de automatizar | Pendente |
| `horario_trabalho` | Dados `data/horarios.csv` | `Inicio`, `Fim` | Seleção de faixa; guardar horários estruturados; validar turno noturno e intervalo | Fonte confirmada |
| `dias_trabalho` | Dados `data/dias.csv` | `Descricao` | **Incompatibilidade de tipo:** cadastro é regime textual, Etapa 1 define número decimal. Separar regime e dias/mês efetivos | Exige decisão |

## Fontes e estrutura confirmadas no código

- `pages/crm/config.py`: colunas do CRM e chaves `id_cliente`/`id_contato`.
- `pages/crm/repositorio.py`: leitura CRM via `ler_csv_operacional`, com arquivos `data/crm/clientes.csv` e `data/crm/contatos.csv` na branch operacional.
- `pages/dados.py` e `pages/dados_hub.py`: catálogos `data/equipamentos.csv` (`Equipamento,Vazao,Consumo,Valor`), `data/materiais.csv` (`Material,Solidos_InSitu,Solidos_Desaguado`), `data/desaguamento.csv` (`Tipo`), `data/horarios.csv` (`Inicio,Fim`), `data/dias.csv` (`Descricao`), `data/salarios.csv` (`Posicao,Valor_Hora`).
- `pages/orcamento/etapa0.py` e `etapa1.py`: orçamento legado usa `data/clientes.csv`, `data/orcamentos.csv`, `data/materiais.csv`, `data/equipamentos.csv`; campos como `Codigo`, `Cliente`, `Volume`, `Terrestre`, `Flutuante`, `Material`, `Horario`, `Dias`.
- `modulos/composicao_orcamento/campos_etapa1.json`: contrato declarativo atual, ainda sem opções de seleção.

## Integrações prioritárias nas demais etapas

| Etapas | Fonte candidata | Uso previsto | Validação pendente |
|---|---|---|---|
| 2 — Cotações | Histórico próprio da composição, ainda não implementado | Referência de cotação por fornecedor, data e unidade; atualização **manual** | Confirmar existência de cadastro de fornecedores e cotações antes de ligar |
| 3 e 11 — Produtividade/dragagem | Dados: equipamentos, materiais, horários e dias | Vazão, consumo, sólidos, jornada | Fórmulas, eficiência, turnos e unidade |
| 4–15 — Composições operacionais | Dados: salários e equipamentos | Preço/hora por função, parâmetros de equipamentos | Identificação de função, encargos, disponibilidade e duplicidade de custos |
| 16 — Custo e venda | Resultados congelados das etapas | Custo unitário, BDI individual e venda | Reconciliação, arredondamento e evitar BDI duplicado |
| 17 — Apresentação comercial | Etapa 16 | Agrupamento comercial sem novo BDI | Soma integral e alocações de itens fracionados |

## Modelo de proveniência recomendado por valor

```json
{
  "valor": 35.0,
  "unidade": "BRL/h",
  "origem_modulo": "dados",
  "origem_arquivo": "data/salarios.csv",
  "origem_chave": "Posicao",
  "origem_registro": "Operador de draga",
  "capturado_em": "data/hora da captura",
  "valor_original": 35.0,
  "ajuste_manual": false,
  "justificativa_ajuste": null
}
```

O exemplo é ilustrativo, **não** é um salário real confirmado. Para CRM, armazenar IDs além dos nomes; para catálogos sem IDs, avaliar chaves estáveis antes de construir vínculos duradouros.

## Riscos e testes antes de codificar integrações

1. **Duas bases de clientes:** levantar sobreposição, homônimos, nomes divergentes e política de migração; sem atualização automática.
2. **Regime de dias versus quantidade:** decidir se `dias_trabalho` será quantidade calculada, editável, e se novo `regime_trabalho` será incluído.
3. **Valores sem identidade estável:** catálogos por nome podem sofrer renomeação e gerar vínculos quebrados.
4. **Falha de leitura:** distinguir indisponibilidade, ausência real de arquivo e cadastro vazio.
5. **RBAC:** definir consulta controlada de CRM/Dados pelo orçamentista.
6. **Reprodutibilidade:** orçamento salvo deve calcular o mesmo resultado mesmo depois de mudanças nos cadastros.
7. **Concorrência:** número de proposta e gravação de rascunhos precisam ser atômicos/validados na branch operacional.
8. **Separação de branches:** verificar origem real dos CSVs em runtime; não presumir que arquivos do código em `main` sejam os dados vigentes.

## Sequência sugerida

1. Homologar esta matriz e resolver `dias_trabalho` e numeração de propostas.
2. Implementar adaptadores **somente leitura**, isolados e testados, para clientes/contatos e materiais/horários/dias.
3. Evoluir a tela Etapa 1 com seletores e valores fotografados; manter fallback manual explícito.
4. Adicionar persistência versionada somente depois de revisar formato, RBAC e branch.
5. Expandir adaptadores a salários/equipamentos/cotações, sem atualização silenciosa de preços.
