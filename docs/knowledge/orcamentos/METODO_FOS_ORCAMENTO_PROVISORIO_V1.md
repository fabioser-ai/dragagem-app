# APP FOS — MÉTODO FOS DE ORÇAMENTO PROVISÓRIO V1

## 1. Base de evidência

- 49 arquivos recebidos; 48 `.xlsx` analisados estruturalmente e 1 `.xls` legado pendente de conversão.
- 19.678 fórmulas extraídas e comparadas.
- 10 famílias provisórias identificadas.
- 2 pares binariamente duplicados preservados como documentos administrativos, mas contados uma vez como evidência estrutural.

## 2. Conclusão executiva

> A FOS não faz orçamento por uma sequência universal de abas. Ela usa um raciocínio comum e seleciona modelos de engenharia e pacotes conforme o serviço.

O fluxo comum é:

```text
Identificação e premissas
        ↓
Produção, prazo ou regime operacional
        ↓
Dimensionamentos técnicos
        ↓
Seleção de pacotes aplicáveis
        ↓
Composições de recursos e custos
        ↓
Formação do preço
        ↓
Resumo técnico e comercial
```

O novo sistema deve preservar esse raciocínio, mas substituir cópias de planilhas por etapas guiadas, parâmetros rastreáveis, pacotes reutilizáveis e cálculo testável.

## 3. Recorrência estrutural

| Componente | Arquivos | Classificação de produto |
|---|---:|---|
| Dados/Premissas | 47/48 | Núcleo ou etapa padrão |
| Produção/Prazo | 46/48 | Núcleo ou etapa padrão |
| Mão de obra | 6/48 | Pacote especializado ou apoio |
| Mobilização draga | 37/48 | Núcleo ou etapa padrão |
| Canteiro/Apoio | 38/48 | Núcleo ou etapa padrão |
| Barrilete/Linha | 22/48 | Pacote recorrente e condicional |
| Célula/Bacia/Paliçada | 22/48 | Pacote recorrente e condicional |
| Bags/Geotêxteis | 20/48 | Pacote recorrente e condicional |
| Mobilização sistema | 19/48 | Pacote recorrente e condicional |
| Operação desaguamento | 17/48 | Pacote recorrente e condicional |
| Dragagem/Operação | 21/48 | Pacote recorrente e condicional |
| Medição/Batimetria | 30/48 | Núcleo ou etapa padrão |
| Carga/Transporte | 4/48 | Pacote especializado ou apoio |
| Desmobilização | 45/48 | Núcleo ou etapa padrão |
| Cotações | 5/48 | Pacote especializado ou apoio |
| Formação de preço | 31/48 | Núcleo ou etapa padrão |
| Resumo comercial | 12/48 | Pacote especializado ou apoio |
| Equipamento específico | 1/48 | Pacote especializado ou apoio |

## 4. Núcleo funcional recomendado

### 4.1 Identificação e premissas
Obrigatório. Deve reunir cliente, objeto, local, data-base, características físicas, responsabilidades, regime de trabalho e demais condicionantes.

### 4.2 Família e configuração
Obrigatório. O engenheiro escolhe uma família inicial e o sistema sugere os modelos e pacotes aplicáveis, sem impedir ajustes.

### 4.3 Produção, prazo ou regime operacional
Obrigatório para orçamentos operacionais. Em serviços como batimetria ou composição de equipamento, o conceito pode assumir outra forma, mas continua representando o direcionador de tempo e capacidade.

### 4.4 Pacotes e composições
O orçamento é formado por pacotes ativáveis. Cada pacote contém recursos, direcionadores, parâmetros adotados, fórmulas e resultados.

### 4.5 Formação de preço e consolidação
Obrigatório. Deve separar custo técnico, incidências, BDI/margem, preço de venda e apresentação comercial.

## 5. Famílias e pacotes sugeridos

### Dragagem com bags/geotêxteis — 20 arquivo(s)
Representante estrutural: `D_047_2025 - Suzano 3 Lagoas- Paliçada Hibrida Reduzida.xlsx` (808 fórmulas, 19 abas).
- Dados e premissas
- Produção e prazo
- Mobilização da draga
- Canteiro
- Preparo de célula/bacia/paliçada
- Bags/geotêxteis
- Sistema de polímero
- Operação de desaguamento
- Dragagem
- Medição/controle
- Desmobilizações
- Formação de preço
- Resumo comercial

### Dragagem com centrífuga — 7 arquivo(s)
Representante estrutural: `Composição - Klabin Ortigueira.xlsx` (1105 fórmulas, 21 abas).
- Dados e premissas
- Produção e prazo
- Mobilização da draga
- Mobilização da centrífuga
- Canteiro
- Operação da centrífuga
- Dragagem
- Medição/controle
- Desmobilizações
- Formação de preço
- Resumo comercial

### Dragagem/bombeamento — 7 arquivo(s)
Representante estrutural: `FABIO D_058_2025 - Suzano Mucuri.xlsx` (390 fórmulas, 12 abas).
- Dados e premissas
- Produção e prazo
- Mobilização
- Canteiro
- Barrilete/linha de recalque
- Dragagem ou bombeamento
- Medição
- Desmobilização
- Formação de preço
- Resumo

### Composição padrão de draga — 4 arquivo(s)
Representante estrutural: `Composiçao - Draga 14 - com equipe.xlsx` (327 fórmulas, 8 abas).
- Configuração do equipamento
- Regime operacional
- Equipe opcional
- Consumos
- Manutenção/depreciação
- Custos indiretos
- Preço por hora/mês

### Batimetria / levantamento — 4 arquivo(s)
Representante estrutural: `Composição - Batimetria - Gerdau Pinda.xlsx` (125 fórmulas, 7 abas).
- Dados do serviço
- Escopo e metodologia
- Equipe
- Equipamentos
- Mobilização
- Execução do levantamento
- Processamento/relatório
- Desmobilização
- Formação de preço
- Resumo

### Dragagem com paliçada/bacia — 2 arquivo(s)
Representante estrutural: `D_059_2025 - Bracell - paliçada COM polímero.xlsx` (594 fórmulas, 16 abas).
- Dados e premissas
- Produção e prazo
- Implantação de paliçada/bacia
- Mobilização
- Dragagem
- Operação auxiliar
- Desmobilização
- Formação de preço

### Composição de mão de obra — 1 arquivo(s)
Representante estrutural: `01RF_26 - composição MDO - máx. desc..xlsx` (676 fórmulas, 12 abas).
- Regime de trabalho
- Funções
- Quantidades
- Salários
- Encargos
- Benefícios/adicionais
- Custo horário/mensal
- Preço

### Equalização técnica — 1 arquivo(s)
Representante estrutural: `260228_Equalização Técnica_FOS_Bacia.xlsx` (1 fórmulas, 1 abas).
- Não tratar como orçamento-base; usar como documento comparativo/apoio

### Outros / composição específica — 1 arquivo(s)
Representante estrutural: `D_003_2025- Suzano PCH Mucuri.xlsx` (217 fórmulas, 13 abas).
- Classificação manual antes de selecionar pacotes

### Equipamento / motobomba — 1 arquivo(s)
Representante estrutural: `Motobomba 3Barras - Westrock.xlsx` (28 fórmulas, 3 abas).
- Configuração técnica
- Regime de uso
- Consumo
- Equipe
- Manutenção
- Mobilização
- Custo horário/mensal
- Preço

## 6. Entidades conceituais

| Entidade | Responsabilidade |
|---|---|
| Orçamento | Identidade comercial e técnica do trabalho cotado. |
| Versão | Fotografia imutável de uma revisão do orçamento. |
| Família | Configuração inicial que sugere modelos e pacotes. |
| Etapa | Unidade de navegação e validação. |
| Pacote | Unidade técnica/econômica ativável, como mobilização, dragagem ou bags. |
| Composição | Conjunto de itens que forma o custo de um pacote. |
| Recurso | Mão de obra, equipamento, material, serviço ou despesa. |
| Direcionador | Tempo, volume, massa, área, quantidade, distância, evento ou valor de equipamento. |
| Parâmetro sugerido | Referência proveniente de catálogo ou histórico. |
| Parâmetro adotado | Valor confirmado pelo engenheiro para aquela versão. |
| Fórmula | Regra de domínio versionada e testável. |
| Resultado | Valor calculado com rastreabilidade até suas entradas. |
| Cotação | Preço contextualizado por fornecedor, data-base e condições. |
| Validação | Pendência, alerta ou confirmação necessária. |
| Histórico | Registro de alteração, responsável, data e justificativa. |

## 7. Regras essenciais do produto

- Catálogo mestre e fotografia do orçamento são objetos diferentes.
- Alterar um catálogo nunca modifica versões antigas.
- O engenheiro vê valor sugerido, valor adotado e origem.
- Fórmulas críticas ficam fora das telas e possuem testes.
- Etapa marcada como Não aplicável não participa dos cálculos, mas seus dados não são apagados.
- Um pacote pode consumir resultados de outro; o motor deve trabalhar com dependências.
- Alterações de entrada recalculam resultados dependentes e informam o impacto.
- Resumo comercial pode agregar itens técnicos sem perder rastreabilidade.
- Exceções são suportadas por configuração ou item livre, sem virar regra universal.
- Finalização cria uma versão; revisão posterior não sobrescreve a versão anterior.

## 8. Proposta de experiência do usuário

1. **Criar orçamento** e informar identificação básica.
2. **Escolher família** a partir de modelos reconhecidos.
3. **Revisar pacotes sugeridos**, ativando, desativando ou acrescentando exceções.
4. **Preencher premissas** e confirmar parâmetros sugeridos.
5. **Acompanhar memória de cálculo** por etapa.
6. **Resolver alertas e pendências** antes da conclusão.
7. **Visualizar custo, preço, preço unitário e impactos** em tempo real.
8. **Gerar resumo técnico e comercial**.
9. **Finalizar versão** e preservar rastreabilidade.

## 9. Telas do MVP

- **Painel de Orçamentos:** Criar, localizar, duplicar, revisar e consultar versões.
- **Identificação e Premissas:** Dados comerciais, físicos, operacionais e responsabilidades.
- **Família e Pacotes:** Seleção guiada dos componentes aplicáveis.
- **Produção e Prazo:** Modelos de capacidade, regime e prazo.
- **Pacotes do Orçamento:** Lista navegável de pacotes com status e aplicabilidade.
- **Composição do Pacote:** Recursos, quantidades, preços, fórmulas e memória de cálculo.
- **Cotações e Referências:** Fornecedores, data-base, condições e valor adotado.
- **Formação de Preço:** Custos, incidências, BDI/margem e preço.
- **Revisão e Validações:** Pendências, alertas, justificativas e comparações.
- **Resumo Técnico/Comercial:** Consolidação detalhada e versão apresentável.

## 10. Direcionadores de custo observados

- tempo
- volume
- massa seca
- área
- quantidade
- distância
- evento único
- valor do equipamento
- percentual sobre subtotal
- regime de trabalho

## 11. O que não deve ser universalizado

- eficiência por tipo de desaguamento;
- consumo de polímero;
- capacidade efetiva de bags;
- percentuais de manutenção, depreciação, juros, perdas e BDI;
- composição padrão de equipe;
- calendário de 22, 26 ou 30 dias;
- fatores embutidos em fórmulas específicas;
- nomes e sequências físicas das abas.

## 12. Estratégia para o legado

Preservar os dados úteis e a rastreabilidade. Funcionalidades incompletas podem ser aposentadas. `data/orcamentos.csv` deve ser classificado campo a campo antes de migração; o fluxo antigo não precisa permanecer acessível se não trouxer valor.

## 13. Critério de validação

O primeiro marco será reproduzir integralmente o modelo SABESP:

```text
Mesmas entradas
→ mesmos resultados intermediários
→ mesmos custos por pacote
→ mesmo preço final
```

Depois, um representante de cada família deverá ser reproduzido para provar flexibilidade.

## 14. Sequência recomendada para implementação

1. Fundação do domínio: identidade, versão, etapa, aplicabilidade e estado.
2. Painel e criação de orçamento sem cálculo.
3. Identificação, premissas e seleção de família.
4. Motor de pacotes e aplicabilidade.
5. Produção e prazo da família dragagem.
6. Composição genérica de recursos.
7. Mobilização, canteiro, operação e desmobilização.
8. Pacotes de bags, polímero e estruturas de desaguamento.
9. Formação de preço e resumo.
10. Equivalência completa com SABESP.
11. Generalização para centrífuga, bombeamento e batimetria.
12. Histórico e sugestões baseadas em orçamentos concluídos.

## 15. Limites desta versão

A análise estrutural é suficiente para orientar a arquitetura. A validação fórmula a fórmula continuará por representantes de família durante os Kid Steps. O arquivo `.xls` legado será convertido apenas se trouxer evidência não coberta por sua versão `.xlsx` correspondente.