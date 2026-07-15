# Plano de Kid Steps do Novo Sistema de Orçamentos

Data: 2026-07-15

Status: plano oficial da Fase 8; execução bloqueada até homologação.

## 1. Regra do plano

Cada Kid Step possui uma missão única, commit próprio preferencial, testes proporcionais, medição de desempenho, aceite observável e rollback. O passo seguinte só começa após homologação do anterior. Nenhum passo amplia escopo silenciosamente.

O alvo inicial é o MVP SABESP; outras famílias, proposta, CRM, Obras e migração integral ficam fora.

## 2. Sequência

~~~mermaid
flowchart TD
    A["001–003: fronteira, domínio e persistência"] --> B["004–007: painel, premissas, pacotes e produção"]
    B --> C["008–011: composições e pacotes SABESP"]
    C --> D["012–014: preço, resumo e aprovação"]
    D --> E["015: equivalência integral e homologação"]
~~~

## 3. Kid Step 001 — Fronteira do novo módulo

- Missão: criar pacote isolado, entrada navegável e visão informativa.
- Arquivos candidatos: modulos/orcamentos/__init__.py, apresentacao/entrada.py, ajuste mínimo de menu/roteador.
- Inclui: rota nova protegida pela permissão atual de módulo, título e retorno.
- Exclui: dados, formulário, cálculo, CSV/JSON, desligamento legado.
- Testes: importação, roteamento, permissão e retorno ao menu.
- Desempenho: zero leitura remota ao abrir a visão informativa.
- Aceite: entrada isolada abre sem afetar legado/Obras.
- Risco: colisão com roteamento por session_state.
- Dependências: nenhuma implementação de domínio.
- Rollback: remover rota/entrada e pacote novo.

## 4. Kid Step 002 — Núcleo do domínio em memória

- Missão: representar IDs, Orçamento, Versão, Cenário e estados.
- Arquivos: dominio/identidades.py, modelos.py, estados.py; aplicacao/resultados.py.
- Inclui: invariantes de identidade, propriedade, elaboração/congelamento e estados semânticos.
- Exclui: persistência, interface real, fórmulas SABESP.
- Testes: criação, unicidade, transições válidas/inválidas, cenário isolado.
- Desempenho: testes locais; nenhuma rede.
- Aceite: objetos reproduzem invariantes dos documentos 22/23.
- Risco: modelar domínio amplo demais.
- Dependências: KS001 apenas como fronteira.
- Rollback: remover pacote interno sem dado persistido.

## 5. Kid Step 003 — Persistência híbrida mínima

- Missão: criar índice leve + JSON de versão com criação atômica e conflito.
- Arquivos: persistencia/contratos.py, serializacao.py, indice.py, github_repositorio.py e testes.
- Inclui: resultados explícitos, schema inicial, leitura, criação composta, SHA/snapshot esperado.
- Exclui: painel funcional, migração, edição de pacotes.
- Testes: round-trip, dado corrompido, conflito, branch avançada, falha em cada estágio e ausência de parcialidade.
- Desempenho: criação em uma operação composta; carregar versão em uma leitura.
- Aceite: nunca existe índice sem detalhe; conflito não sobrescreve.
- Risco: adaptar fundação hoje específica de CSV.
- Dependências: KS002 e persistência multi-arquivo homologada.
- Rollback: apagar somente artefatos de teste; nenhum dado produtivo antes da homologação.

## 6. Kid Step 004 — Painel rápido

- Missão: listar resumos, buscar e abrir detalhe sob demanda.
- Arquivos: apresentacao/painel.py, casos de uso de consulta.
- Inclui: índice, filtros, seleção e abertura de uma versão.
- Exclui: edição e cálculo.
- Testes: uma leitura de índice, uma de detalhe, filtros, vazio/erro.
- Desempenho: painel até uma leitura remota; sem leitura de versões.
- Aceite: lista não carrega cenários/composições/memórias.
- Risco: renderização provocar leitura repetida.
- Dependências: KS003.
- Rollback: voltar à entrada informativa; legado intacto.

## 7. Kid Step 005 — Identificação e premissas

- Missão: editar identificação mínima e premissas com estados/origens.
- Arquivos: aplicacao/premissas.py, catalogos/servico.py e apresentação específica.
- Inclui: sugerido/adotado/manual, unidade, vigência, rascunho e salvamento.
- Exclui: pacotes e cálculos.
- Testes: validações, fotografia, continuidade após salvar, conflito.
- Desempenho: edição local zero rede; salvar um commit.
- Aceite: sugestão não substitui adotado e contexto permanece.
- Risco: acoplar widgets ao domínio.
- Dependências: KS002–004.
- Rollback: versão anterior pelo Git; dados novos isolados.

## 8. Kid Step 006 — Aplicabilidade e pacotes

- Missão: sugerir pacotes Bags/SABESP e controlar aplicabilidade.
- Arquivos: dominio/pacotes.py, aplicacao/pacotes.py, apresentação e testes.
- Inclui: aplicável, não aplicável, pendente, cliente; motivo e histórico.
- Exclui: composição completa e preço.
- Testes: preservação de dados, reativação, responsabilidade e invalidação declarada.
- Desempenho: zero leitura ao alternar pacote já carregado.
- Aceite: não aplicável não vira zero nem apaga conteúdo.
- Risco: confundir etapa com pacote.
- Dependências: KS005.
- Rollback: restaurar versão anterior.

## 9. Kid Step 007 — Primeiro submodelo: calendário, produção e prazo

- Missão: executar primeira cadeia verificável da SABESP.
- Arquivos: calculo/formulas.py, grafo.py, motor.py, validacoes/producao.py.
- Inclui: fórmula versionada, unidades, memória, erros de domínio, invalidação seletiva.
- Exclui: bags, polímero, composição e preço.
- Testes: unitários de fórmulas/grafo, divisor zero, unidades, memória e equivalência parcial.
- Desempenho: zero rede no cálculo; alterar vazão executa somente descendentes.
- Aceite: intermediários escolhidos reproduzem SABESP dentro da tolerância definida.
- Risco: importar constantes do legado como universais.
- Dependências: KS002, 005 e 006.
- Rollback: remover registro de fórmulas; dados persistidos continuam legíveis.

## 10. Kid Step 008 — Composição genérica

- Missão: formar custo auditável por itens/recursos.
- Inclui: quantidade, unidade, incidência, fotografia, item livre e total.
- Exclui: pacotes SABESP específicos e política comercial completa.
- Testes: unidade, vigência, dupla contagem, total e serialização.
- Desempenho: editar item recalcula somente composição/consumidores.
- Aceite: memória reconcilia itens e total.
- Risco: composição virar tabela genérica sem semântica.
- Dependências: KS003, 005 e 007.
- Rollback: inativar caso de uso preservando versão.

## 11. Kid Step 009 — Mobilizações e canteiro

- Missão: implementar mobilização draga/sistema e canteiro SABESP.
- Inclui: responsabilidades, itens únicos/mensais e prazo custeado.
- Exclui: bags/polímero.
- Testes: independência entre mobilização/desmobilização, cliente e prazo.
- Desempenho: mudar frete não recalcula produção.
- Aceite: custos de referência reconciliados por pacote.
- Risco: duplicar recurso/canteiro na operação.
- Dependências: KS008.
- Rollback: desativar pacotes na configuração.

## 12. Kid Step 010 — Célula e bags

- Missão: dimensionar/custear preparo de célula e bags.
- Inclui: balanço necessário, materiais, capacidade, quantidade teórica/adquirida e área.
- Exclui: polímero e transporte.
- Testes: unidades/bases, arredondamento, área/capacidade e equivalência.
- Desempenho: alterar bag não recalcula salários/produção sem dependência.
- Aceite: resultados SABESP explicados.
- Risco: densidade/sólidos implícitos.
- Dependências: KS007–009.
- Rollback: inativar fórmulas/pacotes versionados.

## 13. Kid Step 011 — Polímero e operação de desaguamento

- Missão: implementar consumo/custo de polímero e operação.
- Inclui: massa seca, dosagem, responsabilidade de água/energia e memória.
- Exclui: generalização para centrífuga.
- Testes: base kg/t seca, pendência, cliente e invalidação seletiva.
- Desempenho: dosagem altera somente ramo dependente.
- Aceite: cadeia SABESP até custo do pacote.
- Risco: tornar 3 kg/t regra corporativa.
- Dependências: KS010.
- Rollback: voltar à fórmula/pacote anterior.

## 14. Kid Step 012 — Medição e desmobilizações

- Missão: fechar pacotes técnicos restantes do recorte SABESP.
- Inclui: medição e desmobilizações próprias.
- Exclui: transporte quando não necessário ao cenário de referência.
- Testes: aplicabilidade, responsabilidade, custo e independência.
- Desempenho: pacote fechado sem reler catálogos válidos.
- Aceite: todos os pacotes escolhidos reconciliados.
- Risco: espelhar mobilização indevidamente.
- Dependências: KS008–011.
- Rollback: inativar pacotes.

## 15. Kid Step 013 — Formação de preço

- Missão: separar custo, incidências e preço.
- Inclui: bases explícitas, BDI/markup/margem distintos, dupla aplicação e resumo de preço.
- Exclui: proposta física.
- Testes: bases, ordem, desconto, conflito e não recálculo técnico.
- Desempenho: alterar BDI recalcula somente ramo comercial.
- Aceite: preço SABESP reconciliado sem expor custo indevido.
- Risco: interpretar percentuais históricos como política.
- Dependências: KS008–012.
- Rollback: versão anterior das regras comerciais.

## 16. Kid Step 014 — Resumos, revisão e congelamento

- Missão: consolidar técnico/comercial, revisar e congelar.
- Inclui: vínculos técnicos, validações, ressalvas, aprovação mínima e somente leitura.
- Exclui: geração de proposta e permissões granulares definitivas.
- Testes: congelamento atômico, imutabilidade, revisão derivada e autorização.
- Desempenho: resumo usa resultados válidos já carregados.
- Aceite: versão congelada reproduzível e revisão não sobrescreve.
- Risco: congelar com bloqueios.
- Dependências: KS013.
- Rollback: não desfazer congelada; criar revisão corretiva.

## 17. Kid Step 015 — Equivalência integral e homologação MVP

- Missão: provar SABESP ponta a ponta e decidir transição.
- Inclui: entradas, intermediários, pacotes, preço, contagem de operações, navegação e conflitos.
- Exclui: outras famílias e aposentadoria automática.
- Testes: protocolo completo de equivalência, regressão, desempenho e rollback ensaiado.
- Desempenho: painel 1 leitura; abertura 1 detalhe; edição/cálculo 0 rede; salvamento 1 operação composta; etapa 0 rede.
- Aceite: diferenças explicadas/homologadas e UX estável.
- Risco: validar só total final.
- Dependências: KS001–014.
- Rollback: manter entrada antiga e dados v2 isolados.

## 18. Transição posterior ao MVP

Somente após KS015 homologado: criar Kid Step próprio para tornar novo painel entrada principal, ocultar legado reversivelmente e monitorar. Aposentadoria definitiva aguarda desacoplamento de Obras de data/orcamentos.csv. Não migrar automaticamente registros históricos.

## 19. Matriz de Kid Steps

| Kid Step | Entrega | Testes | Desempenho | Dependências |
|---|---|---|---|---|
| 001 | fronteira/entrada | rota/permissão | 0 leituras | nenhuma |
| 002 | domínio em memória | invariantes | local | 001 |
| 003 | persistência híbrida | atomicidade/conflito | 1 versão | 002 |
| 004 | painel | leitura/filtros | 1 índice | 003 |
| 005 | premissas | estados/continuidade | edição 0 rede | 002–004 |
| 006 | pacotes | aplicabilidade | troca 0 rede | 005 |
| 007 | produção/prazo | cálculo/equivalência | cálculo 0 rede | 002,005,006 |
| 008 | composição | itens/unidades | seletivo | 003,005,007 |
| 009 | mobilizações/canteiro | pacotes | seletivo | 008 |
| 010 | célula/bags | balanço/dimensão | seletivo | 007–009 |
| 011 | polímero/operação | dosagem/cliente | seletivo | 010 |
| 012 | medição/desmobilização | aplicabilidade | sem releitura | 008–011 |
| 013 | preço | incidências | ramo comercial | 008–012 |
| 014 | resumo/aprovação | congelamento | reuso válido | 013 |
| 015 | homologação SABESP | ponta a ponta | orçamento completo | 001–014 |

## 20. Estratégia transversal de testes

- domínio e cálculo sem Streamlit ou rede;
- persistência com respostas Git simuladas e serialização real;
- integração por casos de uso;
- navegação por estado/contexto, não somente screenshot;
- autorização em cada caso de uso sensível;
- equivalência com resultados intermediários;
- desempenho por contagem e duração registrada;
- testes de rollback nos passos de entrada/transição.

## 21. Critério para iniciar

Somente após homologação dos documentos 26 e 27. O primeiro comando de implementação deve ter escopo exclusivo do KS001.
