# Arquitetura Atual — Medições: Gestão

Última atualização: 2026-07-11

Fonte: `docs/ARCHITECTURE_CURRENT.md` e `docs/audit/AUDIT_041_MIGRACAO_MEDICOES_LEGADO.md`.

## Acesso e sequência

Gestão é destinada ao perfil interno `admin`. Os modelos definem sequências entre obra, BM, frentes, MC, lançamentos e resumo. O estado usa, entre outras, `obra_id`, `medicao_id`, `frente_id` e `lancamentos_selecionados`.

Trocar obra ou BM não limpa explicitamente todo o estado descendente. Os botões de etapa são visuais; a navegação efetiva usa Voltar e Próximo.

## Persistência por etapa

- Obra: `data/obras.csv`;
- BM em rascunho: `data/medicoes/medicoes.csv`;
- frentes: `data/medicoes/frentes.csv`;
- memória de cálculo: `data/medicoes/mc.csv`.

A MC contratual reduz identidade estrutural de item a texto no schema legado; a MC genérica aceita linhas dinâmicas sem IDs explícitos. `padrao_fos` possui implementação de MC, mas essa etapa não está na sequência configurada desse modelo.

## Lançamentos e resumo

A seleção exige obra, aprovação aprovada e status não medido; grava apenas IDs na sessão. Não exige BM, não filtra por período e não persiste a seleção.

O resumo agrupa quantidade por item e unidade, mas não calcula valor financeiro, não revalida elegibilidade e pode somar unidades heterogêneas no indicador total.

Não foi observada ação que vincule lançamento ao BM, preencha `medicao_id_vinculada`, altere para medido, finalize o BM ou consolide financeiro. A função de vinculação existe, mas não é chamada no fluxo auditado.

`etapa5_itens.py` permanece desconectada da sequência atual.
