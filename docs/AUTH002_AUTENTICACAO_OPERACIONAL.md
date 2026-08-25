# AUTH-002 — Autenticação operacional segura

## Arquitetura híbrida

`APP_USERS` continua autenticando as contas protegidas sem migração ou mudança
de formato. Usuários de `data/usuarios_operacionais.csv` podem autenticar apenas
quando o cadastro está ativo, o marcador `credencial_configurada` está coerente
e existe exatamente uma credencial bcrypt válida em
`data/credenciais_operacionais.csv`, vinculada ao `usuario_id` imutável.

A senha original nunca é persistida ou recuperável. O arquivo de credenciais
armazena somente hash bcrypt, algoritmo e metadados de configuração. A interface
administrativa permite configurar ou redefinir a senha, mas nunca exibi-la.

## Segurança e consistência

Contas protegidas têm precedência. Qualquer colisão normalizada com `APP_USERS`,
falha de leitura, duplicidade, usuário inativo, perfil elevado, marcador
inconsistente, hash ausente/corrompido ou senha incorreta nega o login com a
mesma mensagem genérica.

A configuração administrativa lê identidade e credenciais no mesmo snapshot da
branch e publica ambos os CSVs em um único commit Git, com atualização sem força
e verificação do snapshot. Assim, uma falha ou conflito não pode deixar o
marcador afirmando que existe credencial sem a credencial correspondente.

## Sessão e autorização

O login operacional preenche o contrato existente: `autenticado`, `usuario`,
`perfil`, `matricula`, `nome`, `ultimo_acesso` e `tela`. Login, logout e timeout
continuam usando o log existente. `perfil_base` é limitado a `user`,
`funcionario`, `encarregado` e `aprovador`; não cria autoridade administrativa.

A autorização efetiva continua em `services/permissoes.py` e
`data/permissoes_usuarios.csv`. O serviço `rbac_shadow.py` não é importado pelo
login nem pelas guardas e permanece exclusivamente diagnóstico.

## Riscos residuais e rollback

- bcrypt não implementa MFA, recuperação, histórico ou expiração de senha;
- a inativação impede novos logins, mas não revoga imediatamente sessão aberta;
- disponibilidade do login operacional depende das leituras do GitHub;
- o login continua sendo a chave compatível com permissões legadas.

Rollback: reverter o commit/PR do AUTH-002 restaura o login exclusivo por
`APP_USERS`. O arquivo de credenciais pode permanecer sem consumidor ou ser
removido em commit separado; nenhuma conta protegida precisa ser restaurada.
