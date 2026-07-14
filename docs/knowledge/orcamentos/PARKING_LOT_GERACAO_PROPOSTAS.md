# PARKING LOT — Geração de Propostas Técnicas e Comerciais

## Status

Parking lot. Não implementar nesta fase.

## Objetivo

Após a conclusão e validação de um orçamento, o APP FOS deverá ser capaz de gerar propostas técnica e comercial com base direta nos dados estruturados do orçamento.

O orçamento será a fonte oficial de dados. Informações já existentes não deverão ser redigitadas.

## Fluxo futuro desejado

```text
CRM
↓
Orçamento
↓
Validação técnica e comercial
↓
Proposta técnica
↓
Proposta comercial
↓
Revisão humana
↓
Emissão em DOCX e PDF
↓
Envio, negociação e versionamento
↓
Aceite
↓
Obra
```

## Proposta técnica

Conteúdo esperado:

- identificação do cliente e do objeto;
- entendimento do escopo;
- metodologia executiva;
- etapas e pacotes aplicáveis;
- equipamentos;
- equipe;
- produtividade e prazo, quando aplicáveis;
- mobilização e desmobilização;
- sistema de desaguamento, quando aplicável;
- medição e controle;
- responsabilidades da FOS;
- responsabilidades do cliente;
- premissas;
- inclusões;
- exclusões;
- entregáveis;
- anexos técnicos.

## Proposta comercial

Conteúdo esperado:

- identificação do cliente;
- objeto;
- escopo resumido;
- itens comerciais;
- quantidades e unidades;
- preços unitários e totais;
- impostos, BDI ou incidências quando aplicáveis;
- prazo;
- validade;
- condições de pagamento;
- reajustes;
- observações comerciais;
- assinatura e identificação da revisão.

## Biblioteca de modelos históricos

Os modelos reais já utilizados pela FOS deverão servir como referência.

A biblioteca poderá classificar modelos por:

- família de orçamento;
- tipo de serviço;
- cliente;
- segmento;
- nível de detalhamento;
- idioma;
- versão;
- situação de aprovação.

Os modelos históricos serão evidências e referências. Não serão automaticamente tratados como templates oficiais sem validação.

## Uso de IA

A IA poderá auxiliar em:

- redação de textos técnicos;
- organização de capítulos;
- adaptação de linguagem;
- consolidação de informações;
- geração de versões executivas;
- sugestão de trechos históricos aprovados;
- verificação de consistência entre orçamento e proposta.

A IA não poderá inventar:

- preços;
- equipamentos;
- produtividade;
- prazo;
- escopo;
- responsabilidades;
- premissas;
- exclusões;
- condições comerciais.

Toda informação crítica deverá vir do orçamento aprovado, de catálogo validado ou de decisão humana registrada.

## Requisito para o modelo de dados do orçamento

Mesmo antes da implementação desta funcionalidade, o novo sistema deverá preservar informações suficientes para permitir sua evolução futura.

Entre elas:

- descrição técnica de cada pacote;
- descrição comercial de cada item;
- premissas;
- inclusões;
- exclusões;
- responsabilidades;
- entregáveis;
- metodologia;
- observações aprovadas;
- justificativas;
- vínculo entre composição técnica e item comercial;
- textos reutilizáveis e sua origem;
- versão do orçamento que originou a proposta.

Essas informações não deverão existir apenas como um único texto livre sem estrutura.

## Versionamento e rastreabilidade

Cada proposta deverá possuir:

- identificador;
- número da versão;
- data;
- autor;
- orçamento e versão de origem;
- modelo utilizado;
- histórico de alterações;
- situação: rascunho, em revisão, aprovada internamente, enviada, aceita, rejeitada, substituída ou cancelada.

Alterações relevantes no orçamento deverão gerar nova versão da proposta, sem sobrescrever silenciosamente a anterior.

## Formatos de saída

A evolução futura deverá considerar:

- DOCX editável;
- PDF final;
- versão interna detalhada;
- versão externa para o cliente;
- resumo para e-mail;
- planilha comercial anexa, quando aplicável.

## Revisão humana

Nenhuma proposta deverá ser enviada automaticamente ao cliente sem revisão e aprovação humana.

A revisão deverá confirmar, no mínimo:

- escopo;
- preços;
- prazo;
- responsabilidades;
- premissas;
- exclusões;
- condições comerciais;
- coerência com a versão do orçamento.

## Relação com a Base de Conhecimento

A funcionalidade poderá reutilizar:

- modelos históricos de propostas;
- textos técnicos aprovados;
- metodologias por família;
- premissas recorrentes;
- exclusões usuais;
- responsabilidades típicas;
- lições aprendidas de propostas e obras anteriores.

A origem de todo texto sugerido deverá permanecer rastreável.

## Critério futuro de sucesso

Uma proposta gerada deverá:

1. refletir fielmente o orçamento aprovado;
2. não exigir redigitação dos dados estruturados;
3. não expor custos internos indevidos;
4. preservar rastreabilidade entre item comercial e memória técnica;
5. permitir edição antes da emissão;
6. gerar documento profissional consistente com o padrão FOS;
7. manter histórico e versões.

## Limites atuais

- Não implementar agora.
- Não definir ainda tecnologia de geração, provedor de IA ou biblioteca de templates.
- Não alterar o escopo dos Kid Steps atuais.
- Considerar este parking lot ao definir campos, entidades e rastreabilidade do Novo Sistema de Orçamentos.
