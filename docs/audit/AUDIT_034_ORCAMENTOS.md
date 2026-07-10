# AUDIT_034_ORCAMENTOS

Status: Auditoria concluída, aguardando consolidação em docs/ARCHITECTURE_CURRENT.md.

## Escopo
- Dashboard
- Etapas 0 a 3
- Persistência
- Estado de sessão

## Principais conclusões
- Orçamentos usa st.session_state.tela e st.session_state.orcamento.
- Persistência principal em data/orcamentos.csv.
- Não existe serviço único do módulo.
- Etapa 0 sobrescreve Data_Criacao ao salvar novamente.
- Etapa 1 simplifica horários e calendário.
- Etapa 2 grava equipe em JSON e custo_mensal_equipe replica custo horário.
- Etapa 3 mistura cadastro global de insumos com composição do orçamento.
- O botão Finalizar não persiste Status nem Etapa_Atual.

## OT propostas
OT-034 a OT-044 conforme auditoria da sessão de 2026-07-10.

## PA propostas
PA-026 a PA-035.

## Próximo subsistema
Prestação de Contas.
