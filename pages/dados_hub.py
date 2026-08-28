import streamlit as st
import pandas as pd

from services.autorizacao import pode
from services.github import StatusLeitura
from services.dados_persistencia import carregar_cadastro_resultado, salvar_cadastro_seguro
from services.ui import renderizar_cabecalho_modulo
from pages import dados as dados_legado
from pages.dados_detalhados.locais_trabalho import render_locais_trabalho

TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = st.secrets["REPO"]

RECURSOS = {
    "equip": {"titulo": "Equipamentos", "recurso": "cadastro", "arquivo": dados_legado.ARQ_EQUIP, "colunas": ["Equipamento", "Vazao", "Consumo", "Valor"]},
    "mat": {"titulo": "Materiais", "recurso": "cadastro", "arquivo": dados_legado.ARQ_MAT, "colunas": ["Material", "Solidos_InSitu", "Solidos_Desaguado"]},
    "desag": {"titulo": "Desaguamento", "recurso": "cadastro", "arquivo": dados_legado.ARQ_DESAG, "colunas": ["Tipo"]},
    "hor": {"titulo": "Horários", "recurso": "cadastro", "arquivo": dados_legado.ARQ_HOR, "colunas": ["Inicio", "Fim"]},
    "dias": {"titulo": "Dias", "recurso": "cadastro", "arquivo": dados_legado.ARQ_DIAS, "colunas": ["Descricao"]},
    "sal": {"titulo": "Salários", "recurso": "salario", "arquivo": dados_legado.ARQ_SAL, "colunas": ["Posicao", "Valor_Hora"]},
    "locais": {"titulo": "Locais de Trabalho", "recurso": "local_trabalho"},
    "atestados": {"titulo": "Atestados", "recurso": "atestado"},
}


def _permitido(recurso, acao):
    if pode(modulo="dados", recurso=recurso, acao=acao):
        return True
    if recurso not in {"atestado", "local_trabalho", "salario"}:
        return pode(modulo="dados", recurso="cadastro", acao=acao)
    return False


def _recursos_visiveis():
    return {chave: cfg for chave, cfg in RECURSOS.items() if _permitido(cfg["recurso"], "visualizar")}


def _salvar(df, cfg, leitura, acao, *, rerun=True):
    recurso = cfg["recurso"]
    if not _permitido(recurso, acao):
        st.error("Operação não autorizada.")
        return False
    resultado = salvar_cadastro_seguro(df, cfg["arquivo"], cfg["colunas"], TOKEN, REPO, resultado_leitura=leitura)
    if resultado.sucesso:
        st.success("Alteração salva com sucesso.")
        if rerun:
            st.rerun()
        return True
    st.error(resultado.erro or "Não foi possível salvar a alteração.")
    return False


def _normalizar_para_edicao(df, colunas):
    normalizado = df[colunas].copy()
    normalizado = normalizado.where(pd.notna(normalizado), "")
    return normalizado.astype(str)


def _parse_valor_brl(valor):
    texto = str(valor or "").strip()
    if not texto:
        raise ValueError("Informe o valor do salário.")
    texto = texto.replace("R$", "").replace(" ", "")
    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")
    numero = float(texto)
    if numero < 0:
        raise ValueError("O valor não pode ser negativo.")
    return f"{numero:.2f}"


def _formatar_brl(valor):
    try:
        numero = float(str(valor).replace(",", "."))
    except (TypeError, ValueError):
        return str(valor or "")
    formatado = f"{numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {formatado}"


def _ordenar_salarios(df):
    if df.empty or "Posicao" not in df.columns:
        return df.copy()
    ordenado = df.copy()
    ordenado["__ordem_posicao"] = ordenado["Posicao"].astype(str).str.strip().str.casefold()
    return ordenado.sort_values("__ordem_posicao", kind="stable").drop(columns=["__ordem_posicao"]).reset_index(drop=True)


def _salarios_para_display(df):
    exibicao = _ordenar_salarios(df)
    if "Valor_Hora" in exibicao.columns:
        exibicao["Valor_Hora"] = exibicao["Valor_Hora"].map(_formatar_brl)
    return exibicao.rename(columns={"Posicao": "Posição", "Valor_Hora": "Valor/hora"})


def _render_salarios(cfg):
    recurso = cfg["recurso"]
    if not _permitido(recurso, "visualizar"):
        st.error("Você não possui permissão para visualizar este conteúdo.")
        return
    leitura = carregar_cadastro_resultado(cfg["arquivo"], cfg["colunas"], TOKEN, REPO)
    if not leitura.leitura_confirmada and leitura.status != StatusLeitura.ARQUIVO_INEXISTENTE:
        st.error("Não foi possível confirmar a leitura desta base.")
        return
    df = leitura.dados.copy()
    for coluna in cfg["colunas"]:
        if coluna not in df.columns:
            df[coluna] = ""
    df = _normalizar_para_edicao(df, cfg["colunas"])
    st.subheader("Salários")
    st.caption("Valores exibidos no padrão brasileiro e posições em ordem alfabética. Selecione uma ação somente quando precisar alterar a base.")
    st.dataframe(_salarios_para_display(df), use_container_width=True, hide_index=True)
    pode_criar = _permitido(recurso, "criar")
    pode_editar = _permitido(recurso, "editar")
    if not (pode_criar or pode_editar):
        return
    st.divider()
    col_novo, col_editar = st.columns(2)
    with col_novo:
        if pode_criar and st.button("➕ Nova entrada", key="sal_acao_nova", use_container_width=True):
            st.session_state.dados_salario_acao = "novo"
            st.rerun()
    with col_editar:
        if pode_editar and st.button("✏️ Atualizar dado existente", key="sal_acao_editar", use_container_width=True):
            st.session_state.dados_salario_acao = "editar"
            st.rerun()
    acao = st.session_state.get("dados_salario_acao")
    if acao == "novo" and pode_criar:
        st.markdown("#### Nova entrada")
        posicao = st.text_input("Posição", key="sal_novo_posicao")
        valor = st.text_input("Valor/hora (R$)", placeholder="Ex.: 25,50", key="sal_novo_valor")
        col_salvar, col_cancelar = st.columns(2)
        with col_salvar:
            if st.button("Salvar nova entrada", key="sal_novo_salvar", use_container_width=True):
                try:
                    valor_canonico = _parse_valor_brl(valor)
                except ValueError as exc:
                    st.error(str(exc))
                else:
                    if not posicao.strip():
                        st.error("Informe a posição.")
                    else:
                        novo = {"Posicao": posicao.strip(), "Valor_Hora": valor_canonico}
                        candidato = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
                        candidato = _ordenar_salarios(candidato)
                        if _salvar(candidato, cfg, leitura, "criar", rerun=False):
                            st.session_state.pop("dados_salario_acao", None)
        with col_cancelar:
            if st.button("Cancelar", key="sal_novo_cancelar", use_container_width=True):
                st.session_state.pop("dados_salario_acao", None)
                st.rerun()
    elif acao == "editar" and pode_editar and not df.empty:
        st.markdown("#### Atualizar dado existente")
        opcoes = [str(v) for v in _ordenar_salarios(df)["Posicao"].tolist()]
        posicao_escolhida = st.selectbox("Posição", opcoes, key="sal_editar_posicao")
        indice = df.index[df["Posicao"].astype(str) == str(posicao_escolhida)][0]
        valor_atual = str(df.at[indice, "Valor_Hora"]).replace(".", ",")
        valor = st.text_input("Valor/hora (R$)", value=valor_atual, key="sal_editar_valor")
        col_salvar, col_cancelar = st.columns(2)
        with col_salvar:
            if st.button("Salvar alteração", key="sal_editar_salvar", use_container_width=True):
                try:
                    valor_canonico = _parse_valor_brl(valor)
                except ValueError as exc:
                    st.error(str(exc))
                else:
                    candidato = df.copy()
                    candidato.at[indice, "Valor_Hora"] = valor_canonico
                    candidato = _ordenar_salarios(candidato)
                    if _salvar(candidato, cfg, leitura, "editar", rerun=False):
                        st.session_state.pop("dados_salario_acao", None)
        with col_cancelar:
            if st.button("Cancelar", key="sal_editar_cancelar", use_container_width=True):
                st.session_state.pop("dados_salario_acao", None)
                st.rerun()


def _render_crud(cfg, chave):
    recurso = cfg["recurso"]
    if not _permitido(recurso, "visualizar"):
        st.error("Você não possui permissão para visualizar este conteúdo.")
        return
    leitura = carregar_cadastro_resultado(cfg["arquivo"], cfg["colunas"], TOKEN, REPO)
    if not leitura.leitura_confirmada and leitura.status != StatusLeitura.ARQUIVO_INEXISTENTE:
        st.error("Não foi possível confirmar a leitura desta base.")
        return
    df = leitura.dados.copy()
    for coluna in cfg["colunas"]:
        if coluna not in df.columns:
            df[coluna] = ""
    df = _normalizar_para_edicao(df, cfg["colunas"])
    st.subheader(cfg["titulo"])
    st.dataframe(df, use_container_width=True, hide_index=True)
    pode_criar = _permitido(recurso, "criar")
    pode_editar = _permitido(recurso, "editar")
    pode_excluir = _permitido(recurso, "excluir")
    if pode_editar and not df.empty:
        st.divider(); st.markdown("#### Editar")
        indice = st.selectbox("Selecionar registro", df.index, key=f"{chave}_editar_idx")
        novos = {coluna: st.text_input(coluna, value=str(df.at[indice, coluna]), key=f"{chave}_editar_{coluna}") for coluna in cfg["colunas"]}
        if st.button("Salvar alterações", key=f"{chave}_salvar"):
            candidato = df.copy()
            for coluna, valor in novos.items(): candidato.at[indice, coluna] = valor
            _salvar(candidato, cfg, leitura, "editar")
    if pode_excluir and not df.empty:
        st.divider(); st.markdown("#### Excluir")
        indice_excluir = st.selectbox("Selecionar para excluir", df.index, key=f"{chave}_excluir_idx")
        confirmar = st.checkbox("Confirmo a exclusão.", key=f"{chave}_excluir_confirmar")
        if st.button("Excluir registro", key=f"{chave}_excluir", disabled=not confirmar):
            _salvar(df.drop(indice_excluir).reset_index(drop=True), cfg, leitura, "excluir")
    if pode_criar:
        st.divider(); st.markdown("#### Adicionar novo")
        novo = {coluna: st.text_input(coluna, key=f"{chave}_novo_{coluna}") for coluna in cfg["colunas"]}
        if st.button("Adicionar", key=f"{chave}_adicionar"):
            _salvar(pd.concat([df, pd.DataFrame([novo])], ignore_index=True), cfg, leitura, "criar")


def _render_atestados_somente_leitura():
    df_atestados, df_servicos, _, _ = dados_legado.garantir_estrutura_atestados()
    st.subheader("Atestados")
    busca = st.text_input("Buscar por palavra-chave", key="dados_hub_busca_atestado")
    filtrados = dados_legado.filtrar_atestados_por_busca(df_atestados, df_servicos, busca)
    if filtrados.empty:
        st.info("Nenhum atestado encontrado."); return
    colunas = ["cliente", "contrato", "obra", "local", "ano", "data_inicio", "data_fim"]
    st.dataframe(filtrados[colunas], use_container_width=True, hide_index=True)
    opcoes = {f"{row['cliente']} | {row['obra']} | {row['contrato']}": row["id_atestado"] for _, row in filtrados.iterrows()}
    escolha = st.selectbox("Selecionar atestado", list(opcoes), key="dados_hub_sel_atestado")
    linha = df_atestados[df_atestados["id_atestado"] == opcoes[escolha]].iloc[0]
    for rotulo, coluna in [("Cliente", "cliente"), ("Contrato", "contrato"), ("Obra", "obra"), ("Local", "local"), ("Ano", "ano"), ("Data início", "data_inicio"), ("Data fim", "data_fim"), ("Descrição", "descricao"), ("Observações", "observacoes")]:
        st.write(f"**{rotulo}:**", linha[coluna])
    servicos = df_servicos[df_servicos["id_atestado"] == linha["id_atestado"]]
    st.markdown("#### Serviços vinculados")
    if servicos.empty: st.info("Nenhum serviço vinculado.")
    else: st.dataframe(servicos[["servico", "unidade", "quantidade", "observacoes"]], use_container_width=True, hide_index=True)


def _voltar_dados():
    st.session_state.pop("dados_recurso", None)
    st.session_state.pop("dados_salario_acao", None)
    st.rerun()


def _voltar_menu():
    st.session_state.tela = "menu"
    st.rerun()


def _render_recurso(chave):
    cfg = RECURSOS[chave]
    recurso = cfg["recurso"]
    if not _permitido(recurso, "visualizar"):
        st.session_state.pop("dados_recurso", None)
        st.error("Você não possui permissão para visualizar este recurso.")
        return
    renderizar_cabecalho_modulo("Dados", "← DADOS", _voltar_dados, key="dados_header_voltar")
    if chave == "atestados":
        if any(_permitido("atestado", acao) for acao in ("criar", "editar", "excluir")): dados_legado.render_atestados()
        else: _render_atestados_somente_leitura()
    elif chave == "locais": render_locais_trabalho()
    elif chave == "sal": _render_salarios(cfg)
    else: _render_crud(cfg, chave)


def render():
    visiveis = _recursos_visiveis()
    recurso_atual = st.session_state.get("dados_recurso")
    if recurso_atual in visiveis:
        _render_recurso(recurso_atual)
        return
    st.session_state.pop("dados_recurso", None)
    st.session_state.pop("dados_salario_acao", None)
    renderizar_cabecalho_modulo("Dados", "← TELA INICIAL", _voltar_menu, key="dados_header_menu")
    st.caption("Selecione uma área. Somente recursos autorizados para sua função são exibidos.")
    if not visiveis:
        st.info("Nenhum recurso de Dados disponível para seu usuário.")
    else:
        chaves = list(visiveis)
        for inicio in range(0, len(chaves), 3):
            colunas = st.columns(3)
            for coluna, chave in zip(colunas, chaves[inicio:inicio + 3]):
                cfg = visiveis[chave]
                with coluna:
                    st.markdown(f"### {cfg['titulo']}")
                    permissoes = [acao for acao in ("visualizar", "criar", "editar", "excluir") if _permitido(cfg["recurso"], acao)]
                    st.caption("Ações: " + ", ".join(permissoes))
                    if st.button("Abrir", key=f"dados_hub_abrir_{chave}", use_container_width=True):
                        st.session_state.dados_recurso = chave
                        st.rerun()
