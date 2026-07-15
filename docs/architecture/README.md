# Arquitetura Atual — Estrutura Modular

Esta pasta contém a documentação oficial e consolidada da arquitetura atual do APP FOS.

## Regra de autoridade

- `docs/PROJECT_STATE.md` registra o estado oficial e o workflow do projeto.
- `docs/DEVELOPMENT_PHILOSOPHY.md` define os princípios permanentes de desenvolvimento e auditoria.
- `docs/architecture/` é a fonte consolidada da arquitetura atual por domínio.
- `docs/audit/` preserva o histórico detalhado de cada auditoria.
- `docs/ARCHITECTURE_CURRENT.md` permanece como documento legado durante a transição para a estrutura modular.

A documentação oficial prevalece sobre memória de conversas. Conclusões devem ser baseadas em código observado e nos registros oficiais; hipóteses, lacunas e limites precisam ser identificados como tais.

## Workflow oficial

1. Ler `docs/PROJECT_STATE.md`, `docs/DEVELOPMENT_PHILOSOPHY.md` e a documentação modular aplicável.
2. Auditar um subsistema por vez ou um recorte transversal explicitamente definido.
3. Criar `docs/audit/AUDIT_XXX_<SUBSISTEMA>.md`.
4. Consolidar os fatos observados no arquivo modular correspondente desta pasta.
5. Não alterar comportamento funcional nem refatorar por preferência durante auditorias.
6. Confirmar toda escrita por leitura posterior.
7. Atualizar `docs/PROJECT_STATE.md`.
8. Não registrar hipóteses como fatos.

## Índice atual

- `01_MEDICOES_FUNDACAO.md`
- `02_MEDICOES_LANCAMENTOS.md`
- `03_MEDICOES_APROVACAO.md`
- `04_MEDICOES_GESTAO.md`
- `08_ORCAMENTOS.md`
- `09_PRESTACAO_CONTAS.md`
- `10_CRM.md`
- `11_ADMINISTRACAO.md`
- `12_SERVICOS_COMPARTILHADOS.md`
- `13_AUDITORIA_TRANSVERSAL.md`
- `14_CONHECIMENTO_REGISTRADO.md`
- `15_MATRIZ_COBERTURA_DOCUMENTAL.md`
- `16_DADOS.md`
- `17_FERIAS.md`
- `18_OBRAS.md`
- `19_CONTRATO_LEITURA.md`
- `20_ENCERRAMENTO_FASE_1.md`
- `21_ESTRATEGIA_FASE_2_ORCAMENTOS.md`
- `22_NOVO_SISTEMA_ORCAMENTOS.md`
- `22_DOMINIO_ORCAMENTOS.md`
- `23_MODELO_LOGICO_DADOS_ORCAMENTOS.md`
- `24_MOTOR_CALCULO_ORCAMENTOS.md`
- `25_FLUXO_USUARIO_ORCAMENTOS.md`
- `26_ARQUITETURA_FISICA_ORCAMENTOS.md`
- `27_PLANO_KID_STEPS_ORCAMENTOS.md`

## Cobertura

A matriz em `15_MATRIZ_COBERTURA_DOCUMENTAL.md` relaciona as rotas observadas em `app.py` às fontes arquiteturais vigentes e registra o nível de cobertura e as lacunas conhecidas.

A documentação modular possui cobertura forte para os domínios funcionais explicitamente roteados no ciclo auditado: Medições, Orçamentos, Prestação de Contas, CRM, Administração, Serviços Compartilhados, Dados, Férias e Obras.

O contrato arquitetural para leitura explícita e bloqueio de escrita está definido em `19_CONTRATO_LEITURA.md`. A fundação de escrita segura por arquivo e a persistência multi-arquivo foram implementadas e homologadas posteriormente, conforme `PROJECT_STATE.md`, `16_DADOS.md` e `20_ENCERRAMENTO_FASE_1.md`.

A auditoria de encerramento identificou um único bloqueador crítico conhecido para concluir a Fase 1: a gravação composta do cadastro de interação do CRM. Prestação de Contas e as demais lacunas registradas permanecem como riscos funcionais ou manutenção estruturada, sem impedir a expansão após a correção do CRM.

## Migração

`docs/ARCHITECTURE_CURRENT.md` permanece como documento legado de transição e contém trechos anteriores aos contratos atuais. A documentação modular prevalece. Nenhum conteúdo do arquivo legado deve ser removido ou reescrito em massa sem reconciliação deliberada.

## Fase 2 — Orçamentos

`21_ESTRATEGIA_FASE_2_ORCAMENTOS.md` define a engenharia reversa dos modelos reais. `22_NOVO_SISTEMA_ORCAMENTOS.md` registra a fundação arquitetural provisória, a homologação da AUDIT_052, a estratégia de substituição do fluxo legado e o primeiro Kid Step proposto.

A fundação do novo sistema preserva dados e conhecimento úteis, mas não exige compatibilidade com funcionalidades legadas sem benefício comprovado. Quebras devem ser deliberadas, documentadas, testadas e homologadas.

## Fases 4 e 5 — Domínio e modelo lógico de Orçamentos

`22_DOMINIO_ORCAMENTOS.md` encerra a descoberta e estabelece o modelo conceitual oficial do domínio com base nos 49 modelos, famílias, vocabulário, crosschecks e auditorias homologadas. A Fase 4 está homologada como fonte para a modelagem lógica.

`23_MODELO_LOGICO_DADOS_ORCAMENTOS.md` transforma esse domínio em estruturas lógicas de informação, identidades, propriedade, relacionamentos, cardinalidades, invariantes, ciclos de vida, versionamento, fotografias, cálculos e rastreabilidade.

O modelo lógico é tecnológico-neutro. Nenhum código funcional, tela, arquivo de dados ou tecnologia de persistência foi criado/alterado por sua publicação.

## Fase 6 — Motor lógico de cálculo e dependências

A Fase 5 foi homologada como base do motor lógico.

`24_MOTOR_CALCULO_ORCAMENTOS.md` define, de forma tecnológica-neutra, o contrato das fórmulas versionadas, o grafo conceitual de dependências, a invalidação seletiva, a ordem de recálculo, unidades, arredondamentos, estados semânticos, tratamento de erros, memórias reproduzíveis, overrides e o protocolo de equivalência com os Excel.

Nenhum código funcional, tela, CSV, mecanismo físico de persistência ou tecnologia de cálculo foi criado ou alterado.

## Fase 7 — Fluxo do usuário e experiência

A Fase 6 foi homologada como base do fluxo oficial.

`25_FLUXO_USUARIO_ORCAMENTOS.md` define jornada, perfis, navegação, aplicabilidade, cenários, pacotes, composições, feedback de cálculo, salvamento, validações, revisão, aprovação, históricos e o escopo exato do MVP SABESP.

Desempenho percebido, continuidade e ausência de recarregamentos evitáveis são requisitos funcionais. Nenhum código funcional, tela real, CSV ou tecnologia física foi criado ou alterado.

## Fase 8 — Arquitetura física mínima e Kid Steps

A Fase 7 foi homologada como base da arquitetura física.

`26_ARQUITETURA_FISICA_ORCAMENTOS.md` seleciona módulos em camadas, persistência híbrida com índice CSV leve e JSON por versão, escrita atômica, cache controlado, conflito sem sobrescrita e transição reversível do legado.

`27_PLANO_KID_STEPS_ORCAMENTOS.md` decompõe o MVP SABESP em 15 passos pequenos, testáveis e reversíveis.

Nenhum código funcional, tela, CSV, rota ou migração foi criado ou alterado.

Próximo passo recomendado, após homologação do Merlin: executar exclusivamente o Kid Step 001.


## AUDIT_054 — desacoplamento cliente–solução técnica

A AUDIT_054 consolidou que cliente é contexto comercial/contratual e nunca seletor de tecnologia, família, pacote ou fórmula. “Família de orçamento” permanece como termo rastreável, definido como família técnica/econômica de soluções. Solução Técnica é a configuração contextual do cenário, não entidade mestre independente nesta etapa.

A auditoria corrigiu a interpretação transversal dos documentos 22 a 28 e do vocabulário. SABESP permanece somente como primeiro caso vertical de equivalência da família técnica aplicável.
