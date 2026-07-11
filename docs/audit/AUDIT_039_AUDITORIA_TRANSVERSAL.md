# AUDIT_039 — Auditoria Transversal de Consistência

Data: 2026-07-11

## Status e escopo

- Auditoria concluída.
- Nenhum comportamento funcional foi alterado.
- Escopo: Medições, Orçamentos, Prestação de Contas, CRM, Administração e Serviços Compartilhados.
- Evidências: documentação oficial modular dos domínios 08 a 12, `docs/ARCHITECTURE_CURRENT.md` para Medições durante a migração, e código dos serviços e módulos diretamente envolvidos.
- Limite documental observado: a arquitetura de Medições permanece no documento legado de transição; não existe, neste momento, consolidação modular de Medições listada em `docs/architecture/README.md`.

## Padrões arquiteturais observados

| Tema | Fatos observados |
| --- | --- |
| Interface e navegação | Aplicação Streamlit com roteamento central por `st.session_state.tela`; módulos também mantêm estados locais em sessão. |
| Persistência | CSVs e arquivos binários são persistidos pela GitHub Contents API; cada escrita substitui o arquivo completo. |
| Acesso aos dados | `services/github.py` é a base comum. Medições e CRM criam wrappers próprios; Prestação de Contas chama o serviço diretamente. |
| Autorização | Há perfil global em `APP_USERS`, permissões granulares em `data/permissoes_usuarios.csv` e, em Medições, vínculos e perfis próprios por obra. |
| Identidade | CRM, Prestação de Contas e lançamentos de Medições usam UUIDs. Outros fluxos ainda usam nomes, códigos, matrículas, índices de DataFrame ou texto livre conforme o domínio. |
| Auditoria | Há log técnico de acessos. Prestação de Contas, CRM e Medições registram parte dos metadados de domínio; Administração não possui trilha própria de alterações. |

## Inconsistências e duplicações observadas

### Persistência e erro

- `carregar_github()` retorna DataFrame vazio para respostas HTTP diferentes de 200. O retorno não diferencia arquivo vazio válido, inexistência, autenticação, rede/API ou conteúdo indisponível.
- `salvar_github()` e a gravação binária fazem leitura do SHA e substituição integral do arquivo; não há locking, transação, retry, timeout explícito ou tratamento específico de conflito.
- Wrappers de leitura e escrita são implementados em Medições e CRM com políticas próprias de schema, normalização e erro; Prestação de Contas usa diretamente o serviço comum.
- CRM e Administração reduzem DataFrames aos schemas declarados; colunas extras podem desaparecer na escrita posterior.
- A combinação de leitura ambígua como vazio e escrita integral existe como risco comum aos módulos que regravam CSVs.
- Prestação de Contas grava comprovante antes da linha da despesa; uma falha posterior pode deixar binário órfão.
- CRM grava interação e depois atualiza o resumo do cliente em arquivos distintos; a operação não é transacional.
- Medições possui fluxos que podem exibir sucesso sem confirmar o resultado da gravação e seleciona lançamentos para BM apenas em estado de sessão.

### Autorização

- O menu usa `pode_acessar_modulo()` para exposição geral; a função considera módulo e ativação, não recurso, ação ou obra.
- A função granular `pode_executar()` existe, mas não teve uso efetivo confirmado nas auditorias registradas.
- Orçamentos e CRM não possuem revalidação interna da permissão geral do módulo.
- Prestação de Contas separa a interface pelo perfil global e `exigir_admin()` aceita apenas `admin`; `superadmin` não recebe automaticamente a interface administrativa desse módulo.
- Administração exige exclusivamente perfil global `superadmin`, independente das linhas de permissões granulares.
- Medições possui uma segunda camada de autorização por vínculo de obra e perfil interno; ela não é equivalente ao perfil global nem à permissão granular geral.
- Em Medições, há fatos registrados de decisões baseadas em maior perfil global do usuário e filtragem baseada na primeira linha de vínculo, além de aprovação sem cruzamento com obra vinculada.

### Estados e ciclo de vida

- Orçamentos persistem `Rascunho`, mas a finalização da etapa 3 não persiste estado, composição ou custos.
- Prestação de Contas permite marcar diretamente `Aprovado`, `Reprovado` ou `Pago` sem máquina de transição; pagamento reutiliza e sobrescreve os campos da decisão anterior.
- CRM não possui máquina de estados transversal; a interação duplica no cliente um resumo comercial atualizado em gravação separada.
- Medições usa estados de aprovação e medição em lançamentos, e BMs iniciam em `rascunho`; a seleção atual não persiste a vinculação ao BM nem altera o lançamento para medido.
- Administração usa `ativo` para autorização e permite exclusão física, sem metadados próprios ou histórico do domínio.

### Identidade e referência de dados

- UUIDs estão presentes em CRM, Prestação de Contas e lançamentos de Medições, mas seletores do CRM usam nomes de empresa e de contato como chaves visuais, tornando homônimos ambíguos.
- O CRM não impõe integridade referencial entre clientes, contatos e interações; contatos podem ser movidos sem reconciliação do histórico.
- Prestação de Contas identifica despesas próprias por `Criado_Por`, embora também persista matrícula.
- Administração recebe `usuario` e `obra_id` como texto sem confirmar a existência na fonte de identidade ou no cadastro de obras.
- Medições mantém identidade de obra e vínculo em camada própria; filtros registrados usam também nomes de obra em alguns pontos.
- Orçamentos geram código pela última linha encontrada para o ano, sem busca explícita pelo maior número ou garantia observada de unicidade.

## Acoplamentos relevantes

- Serviços compartilhados acessam diretamente `st.secrets` e `st.session_state`, acoplando autenticação, autorização e persistência ao runtime Streamlit.
- A cadeia observada é `auth → log → github`; falhas de log são silenciadas para não bloquear autenticação.
- Prestação de Contas depende do arquivo de Férias para completar unidade e departamento.
- CRM depende de múltiplos CSVs relacionados e atualiza um resumo duplicado em cliente após gravar interação.
- Medições possui repositório geral e repositório de lançamentos com acesso sobreposto a locais, vínculos e lançamentos.
- Orçamentos mantém a etapa 3 entre administração global de insumos e dados do orçamento corrente.

## Riscos sistêmicos priorizados por dependência observada

1. **Integridade de escrita:** leitura ambígua como vazio combinada com regravação integral pode substituir dados válidos após falha transitória.
2. **Concorrência:** alterações simultâneas podem perder atualizações em qualquer CSV compartilhado.
3. **Consistência entre arquivos:** comprovante/despesa, interação/resumo de cliente e seleção de lançamento/BM não possuem transação ou confirmação conjunta.
4. **Autorização desigual:** a existência de modelo granular não significa aplicação uniforme; regras globais, por módulo e por obra coexistem.
5. **Rastreabilidade insuficiente:** mudanças em permissões não têm trilha de domínio; estados de despesas e reprovações reutilizam campos; decisões de Medições possuem lacunas documentadas.
6. **Ambiguidade de identidade:** nomes, índices e textos livres ainda participam de fluxos que também possuem identificadores estáveis.

## Oportunidades de simplificação — não implementar nesta auditoria

- Definir um contrato único de resultado de leitura antes de qualquer alteração estrutural nos wrappers.
- Padronizar, depois de validar o contrato, como cada módulo preserva schema, colunas desconhecidas e falhas.
- Definir por domínio a identidade canônica para seletores, vínculos e filtros: IDs estáveis para decisão; rótulos descritivos apenas para exibição.
- Formalizar máquinas de estado antes de alterar telas de finalização, aprovação, pagamento ou vinculação.
- Mapear explicitamente a matriz entre perfil global, permissão granular e permissão interna de Medições antes de ampliar acessos.
- Delimitar as fronteiras entre dados globais e dados do agregado corrente nos fluxos de Orçamentos e Medições.

Esses itens são oportunidades de investigação e decisão; não são recomendação de refatoração imediata.

## Sequência segura de evolução

1. Definir e implementar, isoladamente, resultado explícito de leitura em `services/github.py`; bloquear escritas quando a leitura não for válida.
2. Verificar esse contrato nos módulos de maior risco de sobrescrita: Administração, logs, CRM, Prestação de Contas e Medições.
3. Definir máquinas de estado oficiais, começando por Prestação de Contas e pela vinculação de lançamentos/BM de Medições.
4. Definir a matriz de autorização e a identidade canônica de obras e usuários antes de aplicar permissões granulares adicionais.
5. Tratar operações compostas por domínio após as definições anteriores: comprovante/despesa, interação/cliente e lançamento/BM.
6. Somente depois revisar duplicações de wrappers e sobreposições de repositórios com base em contratos já definidos.

## Perguntas em aberto transversais

- Qual é a política oficial para erro de leitura e bloqueio de escrita?
- Qual é a estratégia aceitável de concorrência enquanto GitHub e CSVs forem a persistência?
- Qual camada define acesso efetivo em caso de divergência entre perfil global, permissão granular e vínculo interno de Medições?
- Quais transições de estado devem ser permitidas e quais metadados de auditoria cada uma exige?
- Quais identificadores são canônicos para usuário, obra, cliente, contato, despesa, lançamento e orçamento?
- Quando uma operação envolve mais de um arquivo, qual consistência mínima é necessária e como falhas parciais devem ser tratadas?
