# APP FOS — ARCHITECTURE INDEX

Status:
Em construção.

Última atualização:
2026-07-08

---

# Objetivo

Este documento passa a ser o índice da documentação arquitetural modular do APP FOS.

A documentação monolítica anterior permanece em `docs/ARCHITECTURE_CURRENT.md` como referência histórica enquanto a migração incremental acontece.

A partir desta organização, cada subsistema deve ter documentação própria para permitir auditorias menores, mais seguras e independentes.

---

# Fonte oficial durante a transição

Durante a transição documental, considerar:

1. `docs/PROJECT_STATE.md` como fonte oficial do estado do projeto.
2. `docs/ARCHITECTURE_CURRENT.md` como documentação consolidada histórica ainda válida.
3. Os arquivos em `docs/architecture/` como documentação modular auditada por subsistema.

Quando houver divergência entre documentação modular e documentação antiga, a divergência deve ser tratada como Pergunta em Aberto até nova auditoria confirmar o fato no código.

---

# Documentos modulares

## Visão geral e fundações

A migrar incrementalmente.

- Visão geral
- Inicialização
- Autenticação
- Interface
- Persistência
- Permissões

## Módulos

- [Medições](architecture/medicoes.md)
- Orçamentos — a migrar
- Prestação de Contas — a migrar
- CRM — a migrar
- Administração — a migrar
- Serviços compartilhados — a migrar

## Registros transversais

A migrar incrementalmente.

- Observações Técnicas
- Perguntas em Aberto

---

# Regra de migração

A migração deve ser feita em baby steps.

Um subsistema por vez.

Não apagar nem substituir `docs/ARCHITECTURE_CURRENT.md` até que a documentação modular esteja suficientemente completa e validada.

Não alterar comportamento do sistema durante a migração documental.
