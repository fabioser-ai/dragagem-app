# AUDIT_054 — Desacoplamento entre Cliente e Solução Técnica

## 1. Objetivo e escopo

Auditoria corretiva exclusivamente documental destinada a eliminar qualquer interpretação de que cliente determina família, tecnologia, solução, pacote, equipamento, produção, parâmetro ou fórmula. Base oficial: documentos arquiteturais 22 a 28, vocabulário, cinco famílias, Crosscheck Semântico do Lote 01, Método FOS provisório e análises individuais dos 49 modelos.

Nenhum Excel foi reprocessado porque a documentação publicada forneceu evidência suficiente. Nenhum código, rota, tela ou dado foi alterado.

## 2. Evidência observada

- O Método FOS declara que os modelos e pacotes são selecionados conforme o serviço e que a família inicial é escolha do engenheiro.
- O crosscheck representa cinco famílias por modelos distintos: composição de draga, batimetria, centrífuga, bombeamento direto e bags. SABESP e Klabin compartilham necessidade de preparação/desaguamento com tecnologias diferentes.
- As famílias documentam responsabilidades do cliente como variação de fornecimento/custeio, não como seletor técnico.
- Batimetria é reutilizável como pacote de medição em outras famílias; composições são explicitamente reutilizáveis e fotografadas no orçamento.
- A variabilidade oficial já proibia condicionais por cliente, mas os documentos anteriores ainda continham formulações como “MVP SABESP” capazes de sugerir especialização indevida.

Conclusão: as cinco famílias são técnicas/econômicas; exceções e condições comerciais não invalidam o desacoplamento.

## 3. Fluxo oficial corrigido

```text
Cliente ou oportunidade
→ problema e condições da obra
→ solução/configuração técnica do cenário
→ capacidades necessárias
→ pacotes sugeridos
→ aplicabilidade no cenário
→ fórmulas versionadas e parâmetros adotados
→ custos e preço
```

É proibida a interpretação Cliente → Tecnologia fixa.

## 4. Responsabilidades conceituais

| Conceito | Responsabilidade |
|---|---|
| Cliente | contexto comercial, contratual, documental e responsabilidades |
| Oportunidade | demanda/objeto comercial que origina o estudo |
| Obra/condições | problema, material, volume, sólidos, área, distância, desnível, acessos, prazo, utilidades, destinação e restrições |
| Família | padrão técnico/econômico compartilhado por soluções |
| Cenário | alternativa comparável que contém uma configuração técnica e comercial própria |
| Solução Técnica | configuração contextual do cenário: família, capacidades, pacotes, parâmetros e aplicabilidades |

## 5. Decisões terminológicas

### Família

Preservar “Família de orçamento” por rastreabilidade histórica. Sua definição normativa passa a ser **família técnica/econômica de soluções**. O termo nunca significa cliente, segmento, empresa ou template físico.

### Solução Técnica

Não criar entidade lógica independente nesta auditoria. A evidência sustenta um agregado contextual pertencente ao cenário, composto por família, capacidades, pacotes, parâmetros e aplicabilidades. Criar identidade mestre agora produziria abstração não comprovada e contrariaria o baby step.

A solução sugerida e a adotada permanecem distinguíveis por decisão rastreável: origem, responsável, momento e justificativa. A decisão pode ser revista em novo cenário ou versão.

## 6. Matriz de influências

| Elemento | Influenciado pelo cliente | Influenciado pela obra | Influenciado pela solução técnica | Influenciado pelo cenário |
|---|---:|---:|---:|---:|
| Responsabilidades | Sim | Sim | Sim | Sim |
| Condições comerciais | Sim | Sim | Não necessariamente | Sim |
| Tecnologia | Não | Sim | Sim | Sim |
| Pacotes | Não diretamente | Sim | Sim | Sim |
| Fórmulas | Não | Sim, por condições | Sim | Sim |
| Equipamentos | Não | Sim | Sim | Sim |
| BDI | Pode | Pode | Não como regra técnica | Pode |
| Apresentação comercial | Sim | Sim | Pode | Sim |

“Influência do cliente” significa contexto ou decisão comercial explícita. Dado técnico informado pelo cliente continua sendo premissa com origem; não transforma a identidade do cliente em chave técnica.

## 7. Invariantes corretivas

1. Cliente não define tecnologia.
2. Tecnologia não define cliente.
3. Um cliente pode possuir múltiplas soluções técnicas.
4. Uma solução técnica pode ser utilizada por múltiplos clientes.
5. Um orçamento pode comparar múltiplas soluções por cenários.
6. Cenários podem utilizar tecnologias diferentes.
7. Fórmulas técnicas não consultam nome de cliente.
8. Pacotes não são ativados por nome de cliente.
9. Condições comerciais podem variar por cliente sem contaminar o motor técnico.
10. O orçamento SABESP é evidência e caso de equivalência, não template universal.

## 8. Contratos por camada

- Domínio: cliente, oportunidade, obra, cenário, família e solução mantêm responsabilidades distintas.
- Modelo lógico: Cliente 1 → N Orçamentos → N Versões → N Cenários; cada cenário possui configuração própria.
- Motor: elegibilidade por pacote, submodelo, capacidade, condição técnica, aplicabilidade e versão da regra.
- Fluxo: contexto → problema/condições → configuração técnica → sugestões → escolha consciente.
- Arquitetura física: nenhum módulo, função, constante, rota ou persistência por cliente.
- Kid Steps: SABESP é fixture de equivalência de uma capacidade genérica.

## 9. Padrões proibidos

```python
if cliente == "SABESP": ativar_bags()
if cliente == "Klabin": ativar_centrifuga()
calcular_orcamento_sabesp()
BDI_PADRAO_SABESP = ...
```

O nome do cliente não pode ser chave oculta de lógica técnica.

## 10. Revisão dos documentos

Foram revisados os documentos 22 a 28, o vocabulário, as cinco famílias, o crosscheck e o Método FOS. Correções normativas foram acrescentadas aos documentos 22 a 28 e ao vocabulário. README e PROJECT_STATE registram a auditoria. As famílias, análises e crosscheck preservam evidência histórica e não exigiram reclassificação ou renomeação.

## 11. Critério de encerramento

> O APP FOS seleciona e calcula soluções técnicas com base nas condições da obra, nos cenários, nas capacidades e nos pacotes aplicáveis. O cliente fornece contexto comercial e contratual, mas nunca determina automaticamente a tecnologia ou a lógica técnica.

AUDIT_054 concluída documentalmente. Kid Step 002 permanece bloqueado até homologação do Merlin.
