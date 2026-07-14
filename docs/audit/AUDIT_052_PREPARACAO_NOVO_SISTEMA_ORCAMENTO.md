# AUDIT_052 — Descoberta do Domínio de Orçamentos

Data: 2026-07-14

Status: auditoria documental concluída; aguardando homologação do Merlin.

## 1. Missão e limites

Esta auditoria registra o estado observável do domínio de Orçamentos existente no APP FOS para preparar uma etapa arquitetural posterior.

Nenhuma funcionalidade, tela, fórmula, contrato de persistência ou CSV foi criado ou alterado. O módulo legado não foi migrado.

## 2. Fontes examinadas

### Documentação oficial

- `docs/PROJECT_STATE.md`;
- `docs/DEVELOPMENT_PHILOSOPHY.md`;
- `docs/architecture/README.md`;
- `docs/architecture/08_ORCAMENTOS.md`;
- `docs/architecture/16_DADOS.md`;
- `docs/architecture/18_OBRAS.md`;
- `docs/architecture/21_ESTRATEGIA_FASE_2_ORCAMENTOS.md`;
- `docs/audit/AUDIT_034_ORCAMENTOS.md`;
- `docs/audit/AUDIT_043_DADOS.md`;
- `docs/audit/AUDIT_045_OBRAS.md`;
- `docs/AUDIT_ORCAMENTOS.md`.

### Código e dados

- `app.py`;
- `pages/menu.py`;
- `pages/orcamento/dashboard.py`;
- `pages/orcamento/etapa0.py`;
- `pages/orcamento/etapa1.py`;
- `pages/orcamento/etapa2.py`;
- `pages/orcamento/etapa3.py`;
- `pages/orcamento/orcamento_old.py`;
- `pages/orcamento_old.py`;
- `pages/dados.py`;
- `services/github.py`;
- `services/dados_persistencia.py`;
- `modulos/medicoes/config.py`;
- `modulos/medicoes/repositorio.py`;
- os CSVs inventariados na seção 6.

O snapshot auditado corresponde ao commit `8d2f8463b07fd7a71b28833853522c548af74be2` da branch `main`.

## 3. Inventário do domínio

| Componente ou entidade | Responsabilidade observada | Ciclo de vida e destino | Leitura / gravação | Dependências e limitações |
|---|---|---|---|---|
| Menu de Orçamentos | Exibir o cartão quando `pode_acessar_modulo("orcamento")` permitir | Define `tela = "orcamento"` | Não persiste dados de domínio | O perfil global `funcionario` é bloqueado pelo roteador; as telas internas não revalidam a permissão |
| Roteador | Encaminhar dashboard e etapas | Reconhece `orcamento`, `orcamento_lista`, `orcamento_etapa0`, `orcamento1`, `orcamento2` e `orcamento3` | Não persiste | Rota desconhecida retorna ao menu |
| Dashboard | Iniciar orçamento, listar todos e reabrir não finalizados | Carrega uma linha inteira em sessão e escolhe a rota por `Etapa_Atual` | Lê `data/orcamentos.csv` | Falhas e ausência de dados são convertidas em DataFrame vazio; exige `Status` apenas no fluxo continuar; usa o primeiro registro do código selecionado |
| Orçamento agregado | Concentrar identificação, premissas, resultados de produção e equipe | Criado na Etapa 0; ampliado nas Etapas 1 e 2; Etapa 3 só altera a sessão | Etapas 0, 1 e 2 leem e regravam `data/orcamentos.csv`; Dashboard e Obras leem | Identidade operacional observada: `Codigo`; não há restrição de unicidade no CSV nem camada de repositório |
| Cliente simples | Fornecer nome para o orçamento | Selecionado ou acrescentado na Etapa 0 | Etapa 0 lê e pode regravar `data/clientes.csv` | Não possui ID; não é o cadastro estruturado do CRM |
| Premissas da obra proposta | Nome, local, data, volume, material, desaguamento, recalque, desnível, medição, horário e dias | Entram na Etapa 0 e são copiadas para o agregado | Catálogos auxiliares alimentam seletores; valores escolhidos são gravados no orçamento | Campos não têm validação completa; horário salvo não é restaurado no seletor, que usa sempre índice zero |
| Produção da draga | Calcular produção horária/mensal e prazo | Calculada a cada renderização da Etapa 1; persiste ao clicar salvar e continuar | Lê equipamentos e materiais; usa premissas da Etapa 0; grava o agregado | Vazão, concentração e eficiência aceitam alteração manual; minutos são ignorados; almoço fixo de 1 h; mês fixo em 22/26/30 dias |
| Equipe | Dimensionar posições, quantidades, encargos e adicional de 25% | Inicializa por salários ou restaura `Equipe_JSON`; persiste ao calcular e ao continuar | Lê salários; grava JSON e totais no agregado | JSON mistura dados-fonte, escolhas e resultados; custo mensal recebe o custo horário; exceções de JSON são ocultadas |
| Insumos globais | Manter nomes e preços unitários | Editados e regravados dentro da Etapa 3 | Etapa 3 lê e grava `data/insumos.csv` | Administração de catálogo global está misturada ao cálculo de um orçamento; usa persistência legada |
| Composição do barrilete | Calcular insumos mais equipe para horas e dias informados | Existe apenas em `session_state.orcamento` e `insumos_editados` | Não grava `data/orcamentos.csv` | Não é restaurada do CSV; estado de insumos não é isolado por orçamento; não há unidade econômica documentada |
| Finalização | Exibir sucesso ao usuário | Botão apenas mostra `Orçamento finalizado` | Não grava arquivo nem atualiza sessão com status final | `Status`, `Etapa_Atual` e `Ultima_Atualizacao` permanecem inalterados |
| Rota Obras | Exibir o agregado orçamentário integral como tabela | Somente leitura | Lê `data/orcamentos.csv` | Rascunhos aparecem como obras; não há vínculo observado com `data/obras.csv` de Medições |
| Cadastro operacional de obra | Identificar contratos/obras usados por Medições | Mantido fora de Orçamentos | Medições lê e grava `data/obras.csv` | Usa `obra_id`; não há referência observada para `Codigo` do orçamento |
| Implementações antigas | Preservar versões anteriores do fluxo | Arquivos permanecem no repositório, mas não são importados pelo roteador atual | Referenciam os mesmos catálogos e agregado | `pages/orcamento/orcamento_old.py` e `pages/orcamento_old.py` são código legado não roteado |

## 4. Fluxo atual

1. O menu verifica acesso geral ao módulo e define `st.session_state.tela = "orcamento"`.
2. O dashboard lista `data/orcamentos.csv` e permite criar ou continuar.
3. Novo orçamento remove somente `session_state.orcamento` e abre a Etapa 0.
4. A Etapa 0 gera `D_NNN_ANO`, coleta premissas, opcionalmente acrescenta cliente e grava um rascunho com `Etapa_Atual = "Etapa 0"`.
5. A Etapa 1 calcula produção e prazo, atualiza a sessão durante a renderização e, em “Salvar e continuar”, regrava o agregado com `Etapa_Atual = "Etapa 1"`.
6. A Etapa 2 monta a equipe, serializa a composição em JSON e regrava o agregado com `Etapa_Atual = "Etapa 2"`.
7. A Etapa 3 permite editar o catálogo global de insumos, calcula o barrilete e mantém os resultados apenas na sessão.
8. “Finalizar” exibe uma mensagem, sem persistir a conclusão.
9. Ao continuar um orçamento, o dashboard usa `Etapa_Atual` persistida; como a Etapa 3 não atualiza esse campo, o registro auditado permanece reabrindo na Etapa 2.

## 5. Estado de sessão

| Chave | Escritores | Leitores | Escopo observado | Limitação |
|---|---|---|---|---|
| `tela` | menu, dashboard e etapas | `app.py` | Navegação global | Telas internas não revalidam permissão |
| `modo_orcamento` | dashboard | dashboard | `inicio` ou `continuar` | Voltar ao menu redefine para `inicio` |
| `orcamento` | dashboard e etapas 0 a 3 | etapas 0 a 3 | Dicionário do orçamento corrente | Etapa 1 o altera durante a renderização; Etapa 3 guarda resultados não persistidos |
| `df_equipe_<Codigo>` | Etapa 2 | Etapa 2 | DataFrame da equipe isolado por código | Não há limpeza observada ao abandonar orçamento |
| `editor_equipe_<Codigo>` | widget da Etapa 2 | Streamlit | Estado do editor isolado por código | Estado de interface, não registro persistente |
| `insumos_editados` | Etapa 3 | Etapa 3 | DataFrame da composição | Não é isolado por código e não é removido ao iniciar novo orçamento |
| `crud_insumos` / `editor_insumos` | widgets da Etapa 3 | Streamlit | Estado dos editores | Chaves globais à sessão, não isoladas por orçamento |

## 6. Inventário completo dos CSVs

### 6.1 CSVs diretamente usados pelo módulo roteado

| Caminho | Finalidade e schema real observado | Identidade e granularidade | Leitores / escritores observados | Natureza | Classificação documental | Riscos observados |
|---|---|---|---|---|---|---|
| `data/orcamentos.csv` | Agregado do orçamento. Colunas: `Codigo`, `Status`, `Etapa_Atual`, `Data_Criacao`, `Ultima_Atualizacao`, `Cliente`, `Nome_Obra`, `Local`, `Data`, `Volume`, `Material`, `Desag`, `Flutuante`, `Terrestre`, `Desnivel_Bombeamento`, `Medicao`, `Horario`, `Dias`, `Draga`, `Vazao`, `Eficiencia`, `Concentracao`, `Producao_Hora`, `Horas_Dia`, `Dias_Mes`, `Horas_Mes`, `Producao_Mensal`, `Prazo_Meses`, `Descricao`, `Equipe_JSON`, `Custo_Hora_Equipe`, `Leis_Sociais`, `custo_hora_equipe`, `custo_mensal_equipe`, `leis_sociais` | `Codigo`; uma linha por orçamento agregado | Dashboard, Etapas 0–2 e rota Obras leem; Etapas 0–2 regravam | Transação com agregados calculados e fotografia parcial | **Legado / manter separado** durante a coexistência | Gravação integral legada; três implementações; falha de leitura pode virar base vazia; campos duplicados; JSON embutido; finalização ausente |
| `data/clientes.csv` | Lista simples; `Cliente` | Nome textual; uma linha por nome | Etapa 0 lê e acrescenta; código antigo também referencia | Catálogo | **Relacionar** futuramente, sem consolidação nesta auditoria | Sem ID, unicidade, metadados ou vínculo com CRM; regravação integral legada |
| `data/materiais.csv` | Parâmetros de material; `Material`, `Solidos_InSitu`, `Solidos_Desaguado` | Nome textual; uma linha por material | Dados administra; Etapas 0 e 1 leem | Catálogo | **Reutilizar e ampliar** | Sem ID/vigência; parser de Dados pode reinterpretar decimais; alteração do mestre não atualiza fotografia já copiada |
| `data/desaguamento.csv` | Opções; `Tipo` | Texto; uma linha por tipo | Dados administra; Etapa 0 lê; Etapa 1 usa o texto salvo | Catálogo | **Reutilizar e ampliar** | Valores reais (`Bombeamento Direto`, `Bacia Ecológica`, `Geobags`, `Decanter Centrífuga`) não coincidem exatamente com as chaves do mapa da Etapa 1; no snapshot, todos caem no padrão `0.85` |
| `data/medicao.csv` | Opções de sistema; `Sistema` | Texto; uma linha por sistema | Etapa 0 lê; nenhum escritor Python atual foi encontrado | Catálogo | **Consolidar: candidato**, sem merge autorizado | Conteúdo e schema iguais a `data/medicoes/medicao.csv` no snapshot, mas caminhos e consumidores são separados |
| `data/horarios.csv` | Turnos; `Inicio`, `Fim` | Par textual; uma linha por turno | Dados administra; Etapa 0 lê | Catálogo | **Reutilizar e ampliar** | Sem ID/ativo; Etapa 1 ignora minutos e desconta 1 h fixa; edição da Etapa 0 não restaura o horário salvo |
| `data/dias.csv` | Regimes semanais; schema real `Descricao`, `Ativo` | Descrição textual; uma linha por regime | Dados administra; Etapa 0 lê | Catálogo | **Reutilizar e ampliar** | O CRUD de Dados declara somente `Descricao` e pode descartar `Ativo`; Etapa 1 depende de três textos exatos e converte para 22/26/30 |
| `data/equipamentos.csv` | Equipamentos e parâmetros; `Equipamento`, `Vazao`, `Consumo`, `Valor` | Nome textual; uma linha por equipamento | Dados administra; Etapa 1 lê | Catálogo | **Reutilizar e ampliar** | Etapa 1 não filtra classe draga; sem ID/vigência; parser genérico pode reinterpretar decimais; consumo e valor não entram no cálculo atual |
| `data/salarios.csv` | Posições e valor-hora; `Posicao`, `Valor_Hora` | Posição textual; uma linha por posição | Dados administra; Etapa 2 lê | Catálogo | **Reutilizar e ampliar** | Sem ID, data-base, vigência ou histórico; orçamento preserva cópia no JSON, mas não referência à versão do catálogo |
| `data/insumos.csv` | Insumos e preço; `Insumo`, `Preco_Unitario` | Nome textual; uma linha por insumo | Etapa 3 lê e regrava | Catálogo | **Ampliar e manter separado** da composição | Sem ID, unidade, data-base ou vigência; administração global dentro da Etapa 3; não é administrado pelo módulo Dados; persistência legada |

### 6.2 CSVs externos necessários para compreender a fronteira

| Caminho | Finalidade e schema real observado | Identidade / granularidade | Relação observada | Natureza | Classificação documental |
|---|---|---|---|---|---|
| `data/obras.csv` | Obra operacional: `obra_id`, `nome_obra`, `contratante`, `contrato`, `objeto`, `cidade`, `status`, `modelo_medicao`, `arquivo_tabela_servicos`, `observacoes`, `criado_em`, `atualizado_em` | `obra_id`; uma linha por obra operacional | Consumido por Medições; nenhum vínculo com `Codigo` foi encontrado | Catálogo operacional / transação de cadastro | **Manter separado e relacionar** futuramente |
| `data/crm/clientes.csv` | Cadastro comercial estruturado com UUID, dados empresariais, relacionamento e timestamps | `id_cliente`; uma linha por cliente CRM | CRM lê e grava; nenhum vínculo com `data/clientes.csv` foi encontrado | Catálogo comercial com estado de relacionamento | **Manter separado e relacionar** futuramente |
| `data/medicoes/medicao.csv` | Opções `Sistema` | Texto; uma linha por sistema | Configurado no domínio Medições; conteúdo igual a `data/medicao.csv` no snapshot | Catálogo | **Consolidar: candidato**, decisão posterior |

## 7. Mapa de dependências

| Origem | Dependência | Uso | Direção do efeito observado |
|---|---|---|---|
| Menu / permissões | `services.permissoes.pode_acessar_modulo` | Exposição do cartão | Permissão controla entrada geral |
| Dashboard | `services.github.carregar_github` + `data/orcamentos.csv` | Lista e retomada | Agregado persistido determina a etapa reaberta |
| Etapa 0 | clientes, materiais, desaguamento, medição, horários, dias | Seletores e premissas | Catálogos fornecem textos copiados ao agregado |
| Etapa 1 | equipamentos e materiais | Vazão e concentração-base | Mudança de catálogo altera defaults de novos cálculos; valores podem ser sobrescritos manualmente |
| Etapa 1 | texto de desaguamento, horário e dias salvo na Etapa 0 | Eficiência, horas e dias mensais | Dependência por correspondência textual exata |
| Etapa 2 | salários | Equipe e custo-hora | Catálogo inicial é copiado para `Equipe_JSON` com resultados calculados |
| Etapa 3 | insumos + custo-hora da Etapa 2 | Composição do barrilete | Catálogo e equipe formam resultado apenas em sessão |
| Orçamentos | `services.github.carregar_github` / `salvar_github` | Toda persistência | Usa adaptadores legados; não usa resultado explícito nem SHA fornecido pelo chamador |
| Dados | materiais, desaguamento, horários, dias, equipamentos e salários | Administração dos catálogos compartilhados | Alterações afetam opções e parâmetros de Orçamentos |
| Obras | `data/orcamentos.csv` | Exibição integral | Trata agregado orçamentário, inclusive rascunho, como obra |
| Medições | `data/obras.csv` | Identidade operacional | Domínio separado sem vínculo observado com orçamento |
| CRM | `data/crm/clientes.csv` | Cliente comercial | Domínio separado sem vínculo observado com cliente simples |

## 8. Matriz de duplicidades

| Itens comparados | Evidência | Classificação | Conclusão factual |
|---|---|---|---|
| `salvar_rascunho`, Etapa 0; `salvar_rascunho_orcamento`, Etapas 1 e 2 | Três funções leem, localizam por `Codigo` e regravam `data/orcamentos.csv` | Duplicidade real de responsabilidade; implementações não equivalentes | A Etapa 2 ainda normaliza tipos, nulos, listas, dicionários e colunas novas |
| `Custo_Hora_Equipe` e `custo_hora_equipe` | Mesmo valor gravado pela Etapa 2 | Duplicidade real de dado por compatibilidade | Ambos estão no registro real auditado |
| `Leis_Sociais` e `leis_sociais` | Mesmo valor gravado pela Etapa 2 | Duplicidade real de dado por compatibilidade | Ambos estão no registro real auditado |
| `custo_mensal_equipe` e custo horário | Etapa 2 atribui `total_hora` aos dois | Duplicidade real de valor, com nome semanticamente divergente | O campo mensal não contém cálculo mensal no código observado |
| `data/medicao.csv` e `data/medicoes/medicao.csv` | Mesmo schema e mesmas três linhas no snapshot | Duplicidade real de conteúdo; consumidores e caminhos diferentes | Candidato à consolidação posterior; não é prova de fonte canônica |
| `data/clientes.csv` e `data/crm/clientes.csv` | Nome semelhante; schemas `Cliente` versus cadastro com `id_cliente` e 18 campos | Falso duplicado / responsabilidades diferentes | Pode haver relacionamento futuro, mas merge por nome perderia identidade e ciclo de vida |
| `data/orcamentos.csv` e `data/obras.csv` | Ambos contêm descrição de obra; identidades e ciclos diferentes | Falso duplicado / responsabilidades diferentes | Um representa proposta/agregado; outro, obra operacional de Medições |
| `Codigo` e `obra_id` | Ambos identificam registros chamados de obra em telas diferentes | Semelhança conceitual, não duplicidade | Não existe vínculo observado |
| `data/insumos.csv` e `data/equipamentos.csv` / `data/materiais.csv` | Todos contêm recursos ou preços | Semelhança ampla; responsabilidades diferentes | Insumos formam composição do barrilete; equipamentos e materiais fornecem parâmetros técnicos |
| `pages/orcamento/orcamento_old.py` e `pages/orcamento_old.py` versus etapas atuais | Código antigo referencia o mesmo domínio, mas não é importado por `app.py` | Duplicidade de código legado, não duplicidade de dados ativos | Manter identificado como legado até decisão própria; não apagar nesta auditoria |

## 9. Catálogos reutilizáveis e exclusivos

### Reutilizáveis com ampliação documental posterior

- materiais;
- desaguamento;
- horários;
- dias;
- equipamentos;
- salários.

Eles já são administrados pelo módulo Dados e consumidos por Orçamentos. A reutilização observável não elimina as lacunas de identidade, unidade, vigência, histórico e interpretação numérica registradas em `16_DADOS.md`.

### Reutilização possível mediante relacionamento

- cliente simples do legado com cliente estruturado do CRM;
- orçamento agregado com obra operacional de Medições;
- os dois catálogos de sistema de medição.

Nenhum relacionamento ou fonte canônica foi observado no código atual.

### Exclusivos no comportamento atual

- `data/insumos.csv`: catálogo global usado e administrado apenas na Etapa 3 auditada;
- `data/orcamentos.csv`: agregado persistente exclusivo do fluxo legado, embora também exposto pela rota Obras;
- composição do barrilete: dados exclusivos da Etapa 3, mas somente em sessão.

## 10. Coexistência observável entre legado e trabalho futuro

Fatos que delimitam a coexistência sem definir a nova arquitetura:

- o módulo atual já possui rotas, chaves de sessão e um agregado próprios;
- `data/orcamentos.csv` é simultaneamente persistência do legado e fonte da rota Obras;
- catálogos compartilhados são administrados fora do módulo, em Dados;
- os códigos antigos não estão roteados, mas permanecem no repositório;
- não existe hoje entidade, rota, CSV ou contrato denominado Novo Sistema de Orçamento;
- a estratégia oficial exige engenharia reversa e crosscheck dos modelos antes da definição arquitetural;
- alterar `data/orcamentos.csv` ou reutilizar suas rotas durante uma primeira implementação atingiria diretamente o legado e a rota Obras.

Portanto, esta auditoria apenas registra que a fronteira atual do legado é composta pelas seis rotas, pelas cinco páginas ativas, pelo estado de sessão descrito e por `data/orcamentos.csv`; não define como o novo sistema será nomeado ou armazenado.

## 11. Pontos fortes observados

- fluxo sequencial simples e legível;
- código anual visível para o usuário;
- retomada de rascunho por etapa persistida;
- premissas, resultados de produção e equipe reunidos em um registro consultável;
- parâmetros-base externos ao código para materiais, equipamentos e salários;
- valores técnicos podem ser ajustados manualmente no orçamento;
- equipe é isolada em sessão pelo código do orçamento;
- catálogos principais já possuem administração central no módulo Dados;
- o agregado preserva a composição calculada da equipe em JSON.

## 12. Limitações observadas

- persistência inteira baseada nos adaptadores legados de GitHub;
- falhas de leitura podem ser interpretadas como base vazia antes de gravação;
- não existe serviço ou repositório canônico do domínio;
- gravação do agregado está triplicada e não é equivalente;
- geração do código usa a última linha que contém o ano, não o maior número;
- ausência de validação de unicidade concorrente;
- Etapa 0 sobrescreve `Data_Criacao` em edição;
- cliente novo é gravado separadamente antes do orçamento, sem operação composta;
- seletores dependem de textos e índices, sem IDs estáveis;
- valores reais de desaguamento não coincidem com o mapa de eficiência;
- cálculo de horário ignora minutos e travessia de dia;
- calendário mensal é fixado em 22, 26 ou 30;
- atualização da sessão na Etapa 1 ocorre antes da confirmação de salvamento;
- equipe mistura fotografia de catálogo, entradas e resultados em JSON;
- `custo_mensal_equipe` recebe custo por hora;
- exceções ao restaurar equipe são ocultadas;
- catálogo global de insumos é administrado dentro de uma etapa transacional;
- composição e resultados da Etapa 3 não são persistidos;
- `insumos_editados` pode atravessar orçamentos;
- finalização não existe no estado persistido;
- rota Obras expõe integralmente rascunhos e custos;
- orçamento, obra operacional e cliente comercial não possuem vínculos observados;
- telas internas não revalidam autorização;
- não foram encontrados testes específicos do fluxo ativo de Orçamentos.

## 13. Perguntas em aberto

### Domínio e ciclo de vida

- Quais estados oficiais um orçamento deve possuir?
- O que caracteriza aprovação, rejeição, cancelamento, revisão e finalização?
- Um orçamento finalizado pode ser reaberto ou versionado?
- Quando uma proposta se torna uma obra operacional?
- Qual vínculo deve existir entre `Codigo` e `obra_id`?

### Identidade e catálogos

- Qual será a regra oficial de identidade e unicidade do orçamento?
- Cliente do orçamento deve referenciar `id_cliente` do CRM?
- Qual dos dois arquivos de sistema de medição é canônico?
- Catálogos precisam de IDs, unidades, vigência, data-base, autoria e histórico?
- O orçamento deve preservar fotografia versionada de todos os parâmetros e preços usados?

### Regras existentes

- Quais campos da Etapa 0 são obrigatórios?
- Quais são os valores oficiais de eficiência por tipo de desaguamento?
- Horas e dias devem usar calendário real, turnos noturnos e intervalos configuráveis?
- Qual é o significado econômico e a unidade do barrilete?
- `custo_mensal_equipe` deve existir e, se sim, como é calculado?
- Quais dados da Etapa 3 compõem oficialmente o orçamento?

### Segurança e convivência

- Quais perfis podem visualizar custos, editar catálogos e finalizar orçamentos?
- A rota Obras deve continuar expondo rascunhos de `data/orcamentos.csv`?
- Como o legado será identificado ao lado do futuro sistema sem alterar seu comportamento?
- Qual destino posterior deve ser dado aos dois arquivos de código antigo não roteados?

## 14. Limite para a próxima etapa

Esta auditoria não define o primeiro Kid Step, nome de rota, componente, persistência ou arquitetura do Novo Sistema de Orçamento. Essas decisões permanecem reservadas à etapa arquitetural posterior e à homologação do Merlin.

## 15. Critérios de encerramento

- fontes oficiais e código diretamente relacionado foram lidos;
- dez CSVs usados diretamente e três externos de fronteira foram inventariados;
- fluxo, estado de sessão, entidades, dependências e duplicidades foram registrados;
- fatos e perguntas pendentes foram separados;
- nenhum código funcional ou CSV foi alterado;
- os achados foram consolidados em `docs/architecture/08_ORCAMENTOS.md`;
- `docs/PROJECT_STATE.md` foi atualizado;
- os arquivos documentais modificados foram relidos;
- a auditoria aguarda homologação do Merlin antes de qualquer implementação.
