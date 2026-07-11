# Arquitetura Atual — Auditoria Transversal de Consistência

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_039_AUDITORIA_TRANSVERSAL.md`

## Escopo

Esta consolidação cruza Medições, Orçamentos, Prestação de Contas, CRM, Administração e Serviços Compartilhados. Medições permanece documentado no arquivo legado de transição; os demais domínios cruzados possuem consolidações modulares.

## Padrões comuns

- Aplicação Streamlit com roteamento principal em `st.session_state.tela` e estados internos de sessão por módulo.
- Persistência principal em CSVs e binários via GitHub Contents API, com substituição integral por arquivo.
- `services/github.py` é a base comum, complementada por wrappers próprios em CRM e Medições; Prestação de Contas chama o serviço diretamente.
- O controle de acesso combina perfil global em `APP_USERS`, permissões granulares em CSV e uma camada própria de vínculo/perfil por obra em Medições.
- UUIDs coexistem com nomes, códigos, matrículas, índices de DataFrame e textos livres como referências operacionais.

## Consistência, estados e identidade

- Leituras ambíguas como DataFrame vazio e gravações integrais são um risco transversal de perda de dados após falha temporária.
- Não há locking, transação, retry ou timeout HTTP explícito na camada comum.
- Operações compostas não são transacionais: comprovante/despesa, interação/resumo de cliente e vínculo lançamento/BM.
- Máquinas de estado são incompletas ou não formalizadas: finalização de orçamento, prestação de contas e conclusão de BM.
- A aplicação granular de autorização não é uniforme; `pode_executar()` existe, mas seu uso efetivo não foi confirmado nas auditorias registradas.
- Seletores e filtros por nome permanecem ambíguos em partes do CRM e de Medições, embora existam identificadores estáveis no modelo.

## Acoplamentos relevantes

- Serviços compartilhados dependem diretamente de `st.secrets` e `st.session_state`.
- A cadeia de infraestrutura observada é `auth → log → github`.
- Prestação de Contas obtém unidade e departamento a partir de dados de Férias.
- CRM mantém resumo comercial no cliente após registrar interação.
- Medições possui repositórios geral e de lançamentos com sobreposição de arquivos.
- A etapa 3 de Orçamentos mistura administração global de insumos e estado do orçamento corrente.

## Direção segura de evolução

1. Criar resultado explícito de leitura na persistência e bloquear escrita após leitura não confirmada.
2. Aplicar e verificar esse contrato nos módulos que regravam CSVs.
3. Definir máquinas de estado oficiais para Prestação de Contas e Medições.
4. Definir matriz de autorização e identidade canônica de obras e usuários.
5. Tratar consistência das operações entre arquivos.
6. Somente então revisar wrappers e repositórios sobrepostos.

Nenhum desses passos foi implementado por esta auditoria.
