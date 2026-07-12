# AUDIT_047 — Locais de Trabalho

Data: 2026-07-12

## Status e escopo

- Auditoria concluída.
- Nenhum comportamento funcional foi alterado.
- Escopo: entrada pela área Dados, seleção de obra, leitura e normalização de locais, inclusão, duplicidade, persistência, schema, permissões e consumo pelo fluxo de Medições.

## Componentes observados

- `pages/dados.py`;
- `pages/dados_detalhados/locais_trabalho.py`;
- `modulos/medicoes/repositorio.py`;
- `modulos/medicoes/config.py`;
- `modulos/medicoes/lancamentos/servicos.py`;
- `services/github.py`;
- `docs/architecture/02_MEDICOES_LANCAMENTOS.md`;
- `docs/architecture/16_DADOS.md`.

## O que foi aprendido

### Entrada e navegação

A subárea Locais de Trabalho é acionada por `pages/dados.py`, que chama `render_locais_trabalho()` quando `st.session_state.subdados == "locais"`.

A tela não revalida autorização. O acesso depende da autorização geral do módulo Dados. Uma vez dentro da subárea, o usuário pode selecionar qualquer obra retornada por `carregar_bases()`.

### Obras

`render_locais_trabalho()` chama `modulos.medicoes.repositorio.carregar_bases()` e recebe seis DataFrames: obras, medições, frentes, MC, itens e serviços. Somente `obras` é usado pela tela.

A lista de obras não é filtrada por vínculo usuário/obra nem por permissão específica. O rótulo visual combina `obra_id` e nome da obra.

### Schema e identidade

O arquivo administrado é `data/medicoes/locais_trabalho.csv`.

Schema observado:

- `local_id`;
- `obra_id`;
- `nome_local`;
- `ativo`;
- `observacoes`;
- `criado_em`;
- `atualizado_em`.

A identidade é estável. Novos registros recebem `local_id` no formato `LOC_<8 caracteres hexadecimais>`.

### Leitura

`carregar_locais()` usa diretamente `carregar_github()`. Quando o retorno é vazio, cria um DataFrame vazio com o schema oficial. Colunas ausentes são preenchidas com string vazia e colunas extras são descartadas pelo recorte final.

Esse comportamento ainda não distingue arquivo realmente vazio, arquivo inexistente e falha de leitura. Assim, uma falha pode ser interpretada como base vazia válida.

Existe uma segunda leitura do mesmo arquivo em `modulos/medicoes.repositorio.carregar_locais_trabalho()`, por meio do helper legado `carregar_csv()`. Esse helper também converte exceções e resultados ausentes em DataFrame vazio.

### Inclusão

A interface permite somente inclusão. Não foram observadas edição, desativação ou exclusão.

A inclusão exige nome não vazio e impede duplicidade dentro da mesma obra por comparação de `nome_local` normalizado com `lower()` e `strip()`.

O novo registro recebe:

- obra selecionada;
- `ativo = "sim"`;
- observações livres;
- timestamps de criação e atualização iguais.

### Escrita

`salvar_locais()` usa diretamente `salvar_github()` e substitui integralmente o CSV.

O retorno da escrita não é verificado. A tela apresenta sucesso e executa `st.rerun()` após a chamada, sem confirmação explícita do resultado.

Não existe SHA esperado vindo da leitura da tela. Portanto, duas sessões concorrentes podem perder alterações, e uma leitura ambígua como vazio pode preceder sobrescrita destrutiva.

### Consumo por Medições

O arquivo é configurado como `ARQ_LOCAIS_TRABALHO` e possui o mesmo schema em `COL_LOCAIS_TRABALHO`.

O repositório geral de Medições expõe `carregar_locais_trabalho()` e `salvar_locais_trabalho()` usando os helpers legados `carregar_csv()` e `salvar_csv()`.

A documentação oficial de Lançamentos registra que o fluxo operacional seleciona local ativo vinculado à obra. Ao criar um lançamento, `criar_lancamento_trabalho()` persiste cópias de `local_id` e `nome_local` no registro de lançamento. Portanto, lançamentos históricos não dependem de releitura do nome atual do cadastro para manter esses dois valores.

## O que ainda não foi compreendido

- O arquivo exato da tela atual que filtra e apresenta os locais no fluxo de lançamento não foi localizado por busca do conector nesta sessão; a relação foi confirmada pela documentação oficial, pelo repositório e pelo schema compartilhado.
- Não foi confirmado se algum consumidor adicional usa `salvar_locais_trabalho()` fora da camada legada de Medições.
- A regra desejada para limitar obras por vínculo do usuário permanece aberta.
- Não foi definida política funcional para edição, desativação ou exclusão de locais.

## O que deve ser documentado

### OT-095 — Locais possuem identidade estável e são copiados para lançamentos

O cadastro usa `local_id` estável. O lançamento persiste `local_id` e `nome_local`, preservando a identificação e o nome observados no momento do registro.

### OT-096 — Administração e consumo usam camadas legadas distintas

A tela de Dados lê e grava diretamente pelo serviço GitHub legado. Medições expõe outra camada de leitura e escrita pelo repositório geral. Ambas tratam falhas como vazio e não compartilham o resultado explícito de leitura.

### OT-097 — Inclusão pode sobrescrever após leitura ambígua

A tela cria uma base vazia quando a leitura retorna vazio e regrava o arquivo inteiro sem SHA esperado.

### OT-098 — A tela carrega bases de Medições não utilizadas

Para obter obras, a tela carrega também medições, frentes, MC, itens e serviços, embora esses DataFrames não sejam usados.

### PA-030 — Quais obras um administrador de Dados pode usar ao cadastrar locais?

Deve ser decidido se a lista permanece global ou passa a respeitar vínculos e permissões por obra.

### PA-031 — Qual camada deve ser canônica para Locais de Trabalho?

Deve ser definido se a persistência segura ficará em um adaptador próprio de Locais ou será incorporada ao repositório de Medições sem duplicar contratos.

## Baby step seguro

Migrar somente a persistência da tela `pages/dados_detalhados/locais_trabalho.py` para o contrato explícito de leitura e escrita:

1. criar leitura estruturada preservando o schema atual;
2. usar o SHA da leitura na atualização;
3. permitir criação explícita apenas após `ARQUIVO_INEXISTENTE`;
4. bloquear o botão de inclusão quando a leitura não autorizar escrita;
5. verificar o resultado da gravação antes de exibir sucesso e executar `st.rerun()`;
6. preservar seleção de obras, regra de duplicidade, geração de ID, timestamps e schema;
7. não implementar edição, desativação, exclusão ou nova política de permissões no mesmo Kid Step.

A migração do consumidor de Medições deve ser tratada em etapa separada, porque altera uma camada compartilhada por outros fluxos do domínio.