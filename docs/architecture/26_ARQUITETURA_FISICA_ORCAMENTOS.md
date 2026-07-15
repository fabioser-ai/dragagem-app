# Arquitetura Física Mínima do Novo Sistema de Orçamentos

Data: 2026-07-15

Status: decisão arquitetural da Fase 8, exclusivamente documental.

## 1. Autoridade, objetivo e recorte

Esta arquitetura implementa futuramente o domínio, o modelo lógico, o motor e o fluxo definidos nos documentos 22 a 25. Seu recorte é a menor fundação física capaz de suportar um fluxo vertical verificável do MVP SABESP.

Não há código, página, CSV, rota, desativação ou migração nesta fase.

## 2. Evidência observada no repositório

- O roteador principal e o menu usam estado de sessão e rerun para navegar.
- O legado de Orçamentos está em páginas dashboard/etapas 0 a 3.
- O legado lê e grava diretamente data/orcamentos.csv e calcula dentro das páginas.
- A etapa inicial relê vários catálogos; o dashboard pode reler a mesma base em modos distintos.
- O CSV legado mistura identificação, estágio, premissas, resultados, equipe e custos.
- A rota Obras lê data/orcamentos.csv e depende desse legado.
- services/github.py possui resultados explícitos e controle por SHA esperado.
- services/persistencia_multi_arquivo.py publica múltiplos CSVs em um commit, atualiza a branch sem força e classifica conflitos.
- Os testes existentes cobrem falhas, atomicidade, SHA, branch avançada e ausência de atualização parcial.
- Permissões atuais são orientadas a módulo/recurso e ainda não representam todas as capacidades do novo domínio.

Conclusão: a nova fundação deve reutilizar os contratos Git seguros, mas não reutilizar a mistura de interface, cálculo e persistência do legado.

## 3. Decisões físicas

1. Módulo isolado em modulos/orcamentos.
2. Dependências apontam para dentro; nenhuma camada depende da apresentação.
3. Persistência híbrida: índice CSV leve, documentos JSON por versão e catálogos separados.
4. Uma versão contém cenários, pacotes, composições, resultados, memórias e histórico necessários à sua reprodução; abertura carrega somente a versão ativa.
5. Versões congeladas são arquivos imutáveis; revisão cria novo arquivo.
6. Escritas que afetam índice e detalhe usam um único commit Git.
7. Concorrência usa commit/SHA remoto esperado; last-write-wins é proibido.
8. Cálculo é local e não realiza chamada remota.
9. Cache é subordinado à revisão/SHA e nunca encobre conflito.
10. O legado permanece operacional até Kid Step específico de transição.

## 4. Camadas

### 4.1 Matriz de camadas

| Camada | Responsabilidade | Pode depender de | Não pode depender de |
|---|---|---|---|
| Apresentação | exibir, capturar ação, manter contexto, mostrar validação | aplicação e modelos de apresentação | CSV/JSON, API GitHub, fórmula, regra comercial |
| Aplicação | casos de uso e coordenação transacional | domínio, cálculo, contratos de repositório, catálogos | Streamlit, widgets, requests |
| Domínio | entidades, estados, invariantes, versões, aplicabilidade | tipos puros do próprio domínio | apresentação, GitHub, pandas, persistência |
| Cálculo | fórmulas, grafo, unidades, invalidação, memória e erros | domínio e contratos de regras | apresentação, GitHub e persistência |
| Persistência | serialização, leitura, snapshots, atomicidade e conflito | contratos do domínio/aplicação e adaptador Git | apresentação e fórmulas |
| Catálogos | mestres, vigência, seleção e fotografia | contratos de persistência e domínio | apresentação |
| Validações | validação de domínio/aplicação e mensagens | domínio e cálculo | detalhes de widget |

~~~mermaid
flowchart TD
    UI["Apresentação"] --> APP["Aplicação / casos de uso"]
    APP --> DOM["Domínio"]
    APP --> CALC["Motor de cálculo"]
    APP --> REP["Persistência e catálogos"]
    CALC --> DOM
    REP --> DOM
~~~

## 5. Organização física provisória

~~~text
modulos/orcamentos/
├── dominio/
├── aplicacao/
├── calculo/
├── persistencia/
├── catalogos/
├── validacoes/
└── apresentacao/
~~~

### 5.1 Matriz de arquivos candidatos

| Arquivo ou diretório | Responsabilidade | Kid Step de criação |
|---|---|---:|
| modulos/orcamentos/__init__.py | fronteira do pacote | 001 |
| apresentacao/entrada.py | entrada informativa e contexto | 001 |
| dominio/identidades.py | IDs e código comercial distintos | 002 |
| dominio/modelos.py | Orçamento, Versão e Cenário | 002 |
| dominio/estados.py | estados semânticos e ciclos | 002 |
| aplicacao/resultados.py | resultados explícitos de casos de uso | 002 |
| persistencia/contratos.py | portas de repositório | 003 |
| persistencia/serializacao.py | documento da versão e validação de schema | 003 |
| persistencia/github_repositorio.py | adaptador à fundação GitHub | 003 |
| persistencia/indice.py | leitura/escrita do índice leve | 003 |
| apresentacao/painel.py | painel resumido | 004 |
| aplicacao/premissas.py | alterar/adotar premissas | 005 |
| catalogos/servico.py | carregar e fotografar referência | 005 |
| dominio/pacotes.py | pacote/aplicabilidade | 006 |
| aplicacao/pacotes.py | casos de uso de aplicabilidade | 006 |
| calculo/formulas.py | contrato e registro de fórmulas | 007 |
| calculo/grafo.py | dependências e invalidação | 007 |
| calculo/motor.py | execução incremental e memória | 007 |
| validacoes/producao.py | validações do primeiro submodelo | 007 |

Arquivos só nascem quando seu Kid Step precisar deles. Nenhum arquivo central acumula todas as responsabilidades.

## 6. Persistência escolhida

### 6.1 Comparação

| Critério | CSVs normalizados | JSON por versão | Híbrido |
|---|---|---|---|
| Painel leve | bom | ruim se listar documentos | ótimo |
| Detalhe sob demanda | muitas leituras/junções | bom | ótimo |
| Chamadas GitHub | tende a crescer | uma por versão | uma para índice e uma para detalhe |
| Atomicidade | muitos arquivos | simples no detalhe | exige commit composto, já suportado |
| Conflito | por vários SHAs | por versão | índice + versão pelo snapshot |
| Legibilidade | tabular | estrutura de domínio | adequada a cada uso |
| Cenário ativo | exige agregação | documento da versão | documento da versão |
| Teste/serialização | conhecido | contrato novo | controlável |
| Arquivo gigante | alto risco de tabelas globais | risco se orçamento enorme | limitado por versão |
| Streamlit Cloud | compatível | compatível | compatível |

Decisão: alternativa C, modelo híbrido.

### 6.2 Granularidade proposta

~~~text
data/orcamentos_v2/
├── indice.csv
└── orcamentos/{orcamento_id}/versoes/{versao_id}.json
~~~

Catálogos existentes ou futuros continuam em bases separadas. indice.csv contém somente campos necessários ao painel. Cada JSON representa uma versão reproduzível e seus cenários. Se medições futuras mostrarem documento grande, memórias poderão ser separadas em decisão posterior; não antecipar agora.

### 6.3 Matriz de persistência

| Informação | Forma física proposta | Granularidade | Leitura | Escrita | Versionamento |
|---|---|---|---|---|---|
| Resumo do painel | indice.csv | uma linha por orçamento | uma leitura principal | commit composto | atualiza estado corrente |
| Identidade do orçamento | índice + cabeçalho da versão | orçamento | com resumo/detalhe | criação/revisão | estável |
| Versão em elaboração | JSON | uma versão | sob demanda | substituição controlada | revisão lógica + SHA |
| Versão congelada | JSON | uma versão | cacheável por SHA | não reescreve | imutável |
| Cenários/pacotes/composições | dentro da versão | cenário/coleção | junto da versão ativa | mesma alteração agrupada | fotografia da versão |
| Memórias/resultados/validações | dentro da versão | execução/resultado | somente quando detalhe requer | junto ao recálculo salvo | histórico reproduzível |
| Catálogos | bases separadas | catálogo | por necessidade | fluxo administrativo próprio | vigência |
| Fotografias | dentro da versão | referência usada | com versão | ao adotar referência | imutável no congelamento |

~~~mermaid
flowchart TD
    I["indice.csv: resumos"] --> O["Abrir orçamento"]
    O --> V["versao_id.json"]
    C["Catálogos separados"] --> F["Fotografia na versão"]
    F --> V
~~~

## 7. Identificadores físicos

- ID interno: UUID textual canônico gerado pela aplicação; independente de nome.
- Código comercial: D_NNN_AAAA ou política vigente; exibível, pesquisável e não chave universal.
- Versão: versão_id UUID e número/revisão humana dentro do orçamento.
- Cenário, pacote, composição, item e memória: UUID próprio.
- Fórmula: identidade lógica legível estável mais versão explícita.

Nomes e posições em listas não são chaves. Arquivo usa IDs internos; código comercial pode mudar por decisão registrada sem quebrar referências.

## 8. Contratos mínimos de persistência

Toda operação retorna status, dados/identidades relevantes, snapshot esperado/observado, arquivos envolvidos, erro seguro e correlação.

Estados: sucesso, conflito, validação recusada, branch avançada, erro remoto, dado inexistente, dado corrompido e operação parcial recusada.

Contratos:

- listar_resumos(filtros);
- carregar_orcamento(id);
- carregar_versao(orcamento_id, versao_id);
- carregar_cenario(versao, cenario_id), local após carregar versão;
- criar_orcamento(comando, snapshot_esperado);
- salvar_versao_em_elaboracao(versao, snapshot_esperado);
- salvar_alteracao_agrupada(versao, historico, snapshot_esperado);
- verificar_conflito(snapshot_esperado);
- congelar_versao(versao, resumo, snapshot_esperado);
- criar_revisao(versao_origem, snapshot_esperado);
- carregar_catalogo(tipo, vigencia);
- fotografar_referencia(referencia, versao);
- registrar_historico(evento, alteração agrupada).

## 9. Atomicidade

Mudanças atômicas:

- criação: índice + JSON com orçamento, versão e cenário iniciais;
- alteração confirmada: valores adotados + invalidações + memórias/resultados recalculados + histórico, no mesmo JSON/commit;
- congelamento: estado, cenário adotado, fotografias, aprovações e resumo; índice + JSON em um commit;
- criação de revisão: novo JSON + atualização do índice em um commit.

Reutilizar a estratégia de blobs, árvore, commit e atualização de ref sem força. O adaptador novo precisa aceitar texto/bytes genéricos, não forçar JSON a DataFrame. Nenhum índice pode apontar para detalhe inexistente.

## 10. Carregamento e operações remotas

### 10.1 Painel

~~~mermaid
flowchart LR
    A["Abrir painel"] --> C{"Índice válido em cache?"}
    C -->|sim| L["Renderizar resumos"]
    C -->|não| G["Ler indice.csv"]
    G --> L
~~~

### 10.2 Abertura

~~~mermaid
flowchart TD
    P["Selecionar resumo"] --> V["Ler JSON da versão ativa"]
    V --> S["Validar e desserializar"]
    S --> C["Ativar cenário e contexto"]
    C --> D["Carregar detalhes sob demanda"]
~~~

### 10.3 Alteração

~~~mermaid
flowchart TD
    E["Confirmar alteração local"] --> I["Invalidar descendentes"]
    I --> C["Recalcular localmente"]
    C --> H["Criar memória e histórico"]
    H --> S["Salvar em commit composto"]
~~~

### 10.4 Matriz de operações remotas

| Ação do usuário | Leituras | Escritas | Cache | Meta |
|---|---:|---:|---|---|
| Abrir painel | 0 ou 1 índice | 0 | índice por snapshot/vigência | uma leitura principal |
| Abrir orçamento | 1 versão | 0 | versão congelada por SHA | índice já disponível + detalhe |
| Trocar etapa | 0 se versão ativa | 0 | contexto ativo | zero remoto |
| Alterar campo local | 0 | 0 | rascunho local | zero remoto |
| Calcular | 0 | 0 | resultados do cenário | zero remoto |
| Salvar | snapshot conforme contrato | 1 operação composta | invalidar índice/versão afetados | um commit |
| Trocar cenário da versão | 0 | 0 | versão ativa | zero remoto |
| Abrir catálogo ainda não carregado | 1 base necessária | 0 | catálogo por SHA/vigência | não duplicar |

Metas são contagens, não promessas de tempo antes de medição.

## 11. Estado de sessão

Guardar apenas IDs ativos, etapa/pacote/filtros/posição, rascunho local, estado da persistência e resultados válidos do cenário ativo.

Distinguir:

- interface: seleção e posição;
- domínio: versão/cenário em memória;
- cache: cópia reutilizável com chave/invalidação;
- rascunho: mudanças não confirmadas;
- persistido: fotografia associada ao snapshot remoto.

Não colocar todos os orçamentos, catálogos ou versões no session_state.

## 12. Cache inicial

| Categoria | Pode cachear | Chave | Vigência/invalidação | Após gravação |
|---|---|---|---|---|
| Índice | sim | repo, branch, commit/SHA | mudança de branch ou gravação | atualizar/inutilizar |
| Catálogo | sim | tipo, SHA/vigência | alteração do mestre/vigência | invalidar catálogo afetado |
| Versão congelada | sim | versão_id, blob SHA | imutável | permanece |
| Regras de cálculo | sim | fórmula e versão | nova versão da regra | coexistem |
| Versão em elaboração | somente contexto controlado | versão_id, revisão, SHA | edição, conflito ou gravação | substituir pelo confirmado |
| Cenário ativo calculado | sim em memória | cenário + revisões das entradas/regras | invalidação do grafo | preservar só nós válidos |

Cache não converte erro remoto em sucesso nem é fonte oficial.

## 13. Rerun e navegação

Rerun só é aceitável quando o framework precisar reavaliar a apresentação após transição explícita de rota/estado ou confirmação que altere a árvore visual. É proibido como mecanismo de cálculo, persistência, polling, correção de estado ou cadeia automática.

Antes de eventual rerun, persistir no contexto os IDs, etapa, pacote, filtros e seleção. Cada ação pode provocar no máximo um rerun intencional; a renderização seguinte consulta caches/contexto e não repete leituras. Todo uso será localizado, documentado e testado.

## 14. Concorrência

Cada versão em elaboração carrega revisão lógica e snapshot remoto observado. Salvar compara o esperado; branch avançada ou SHA divergente recusa a escrita.

~~~mermaid
sequenceDiagram
    participant U as Sessão
    participant R as Repositório
    U->>R: salvar com snapshot esperado
    R->>R: comparar branch/SHA
    alt coincide
        R-->>U: commit e novo snapshot
    else diverge
        R-->>U: conflito sem sobrescrever
    end
~~~

Em conflito, preservar rascunho local e oferecer recarregar, comparar ou criar revisão. Nunca last-write-wins silencioso.

## 15. Segurança e permissões

Capacidades conceituais: consultar, criar, editar, revisar técnica/comercialmente, aprovar, congelar, administrar catálogos, ver custos internos e ver preços comerciais.

O adaptador de autorização deve consultar a fundação existente, mas casos de uso revalidam capacidade; ocultar botão não autoriza operação. Perfis físicos e alterações na base de permissões ficam para Kid Step próprio.

## 16. Transição do legado

O legado permanece preservado e funcional até equivalência/rollback comprovados. data/orcamentos.csv não é migrado nem reutilizado como índice v2. Obras continua lendo o arquivo legado até decisão própria.

### 16.1 Matriz de transição

| Elemento legado | Preservar | Ocultar | Migrar | Aposentar | Momento |
|---|---:|---:|---:|---:|---|
| data/orcamentos.csv | sim, histórico e dependência Obras | somente após nova entrada homologada | não no MVP | após Obras desacoplada | KS de transição posterior |
| Dashboard/etapas 0–3 | sim para rollback | após fluxo novo homologado | não copiar | depois da equivalência | posterior ao MVP |
| Entrada principal antiga | reversível | quando novo painel homologado | não | após janela de rollback | KS de transição |
| Catálogos úteis | sim | não | consumir por fotografia | não | conforme KS 005+ |
| Rota Obras | preservar sem alteração | não | integração adiada | não nesta fase | dependência explícita |
| Arquivos antigos não roteados | preservar | já fora do acesso principal quando aplicável | não | inventário futuro | posterior |

~~~mermaid
flowchart TD
    L["Legado preservado"] --> N["Novo fluxo em paralelo controlado"]
    N --> H["Homologar SABESP e desempenho"]
    H --> O["Ocultar entrada antiga com rollback"]
    O --> A["Aposentar após desacoplar Obras"]
~~~

## 17. Testes e observabilidade

Testes mínimos: domínio, cálculo, persistência/serialização, conflito, atomicidade, equivalência SABESP, permissões, navegação/contexto e desempenho por contagem.

Eventos: leitura de índice/versão, cache hit/miss, cálculo executado, nós invalidados/preservados, salvamento, conflito, erro remoto e duração. Logs não incluem valores comerciais sensíveis, tokens ou documentos integrais.

## 18. Validação contra documentos 22–25

- Interface não contém fórmulas.
- Domínio não importa persistência.
- Motor calcula sem rede.
- Painel usa índice leve.
- Versão ativa é carregada separadamente.
- Memórias e estados permanecem reproduzíveis.
- Aplicabilidade invalida somente dependentes.
- Salvamento composto preserva atomicidade.
- Conflito preserva rascunho e recusa sobrescrita.
- MVP permanece SABESP.

## 19. Decisões adiadas

Geração de propostas, integrações CRM/Obras, inteligência histórica, migração dos 49 modelos, escala definitiva, banco futuro, todas as famílias e processamento assíncrono complexo.

## 20. Encerramento

Esta arquitetura escolhe a menor fundação física para iniciar o MVP, sem implementá-la. A execução começa somente após homologação, pelo Kid Step 001.


## Restrição física corretiva — AUDIT_054

A arquitetura física não pode criar módulos, funções, constantes, rotas ou formatos de persistência específicos por cliente. Identidade de cliente permanece dado contextual; não participa do despacho de tecnologia, pacotes, fórmulas ou equipamentos.

A configuração técnica pertence ao documento versionado do cenário e usa os mesmos contratos genéricos para qualquer cliente. O caso SABESP é fixture/evidência de equivalência, não namespace arquitetural.
