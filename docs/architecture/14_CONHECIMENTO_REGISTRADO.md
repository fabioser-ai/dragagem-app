# Arquitetura Atual — Conhecimento Registrado

Última atualização: 2026-07-11

Fonte de auditoria: `docs/audit/AUDIT_040_CONHECIMENTO_REGISTRADO.md`

## Situação do conhecimento oficial

O APP FOS possui governança documental explícita:

- estado e workflow em `docs/PROJECT_STATE.md`;
- princípios em `docs/DEVELOPMENT_PHILOSOPHY.md`;
- consolidações por domínio em `docs/architecture/`;
- histórico detalhado em `docs/audit/`.

Orçamentos, Prestação de Contas, CRM, Administração e Serviços Compartilhados possuem trilha completa de auditoria e consolidação. A auditoria transversal registra os riscos e a sequência segura de evolução.

## Limites conhecidos

- Medições possui fontes modulares em `01_MEDICOES_FUNDACAO.md` a `04_MEDICOES_GESTAO.md`; o legado permanece preservado para reconciliação.
- `ARCHITECTURE_CURRENT.md` possui atualização anterior às consolidações atuais e contém trechos temporais que precisam de reconciliação.
- A documentação não apresenta ainda uma matriz única que prove a cobertura arquitetural de todos os módulos e fluxos roteados pelo aplicativo.
- Não existe lista única, priorizada e rastreável de perguntas arquiteturais em aberto.

## Consequência para a continuidade

Uma nova sessão consegue continuar com segurança os domínios modularizados e o principal risco transversal já identificado. Não deve assumir que todo o aplicativo está igualmente coberto nem que o legado foi totalmente reconciliado.

## Próximo baby step documental

Criar matriz de cobertura documental por módulo ou fluxo, registrando fonte arquitetural vigente, auditoria de origem, nível de atualização e lacunas conhecidas. Só depois reavaliar o início da implementação do contrato de leitura.
