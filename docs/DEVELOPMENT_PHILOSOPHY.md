# Filosofia de Desenvolvimento — APP FOS

## Propósito

Esta filosofia define como o APP FOS é compreendido e evoluído. Ela complementa o estado e o workflow registrados em `docs/PROJECT_STATE.md`; não substitui evidência observável no código nem na documentação oficial.

## Princípios

- Baby steps: mudanças pequenas, deliberadas e verificáveis.
- Uma alteração por vez.
- Arquitetura antes de implementação.
- Auditoria antes de implementação.
- Código observado acima de hipóteses.
- Documentação oficial acima da memória de uma conversa.
- Não refatorar por preferência pessoal.
- Não alterar comportamento funcional durante auditorias.
- Confirmar toda escrita por leitura posterior.
- Melhorias permanentes do processo devem ser documentadas antes de se tornarem padrão.
- O conhecimento oficial do projeto pertence ao repositório, nunca exclusivamente à conversa.

## Regras de auditoria

1. Ler o estado oficial e a documentação arquitetural aplicável antes da auditoria.
2. Auditar apenas um subsistema ou um recorte transversal definido.
3. Registrar fatos observados; identificar explicitamente hipóteses, lacunas e limites da evidência.
4. Registrar a análise detalhada em `docs/audit/`.
5. Consolidar os fatos relevantes em `docs/architecture/`.
6. Atualizar `docs/PROJECT_STATE.md` somente depois dos registros anteriores.
7. Confirmar cada gravação pela releitura do trecho alterado.
8. Considerar a auditoria concluída somente quando todos os registros previstos estiverem confirmados.

## Integridade operacional

Nunca simular leituras, buscas, alterações, permissões, commits, erros ou resultados de ferramentas. Se uma escrita falhar, registrar a ferramenta, a operação e o erro real; não declarar a atualização como realizada e continuar apenas nas etapas independentes dessa escrita.
