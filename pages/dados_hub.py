import streamlit as st
import pandas as pd

from services.autorizacao import pode
from services.github import StatusLeitura
from services.dados_persistencia import carregar_cadastro_resultado, salvar_cadastro_seguro
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
    return {
        chave: cfg for chave, cfg in RECURSOS.items()
        if _permitido(cfg["recurso"], "visualizar")
    }


def _salvar(df, cfg, leitura, acao):
    recurso = cfg["recurso"]
    if not _permitido(recurso, acao):
        st.error("Operação não autorizada.")
        return False
    resultado = salvar_cadastro_seguro(
        df,
        cfg["arquivo"],
        cfg["colunas"],
        TOKEN,
        REPO,
        resultado_leitura=leitura,
    )
    if resultado.sucesso:
        st.success("Alteração salva com sucesso.")
        st.rerun()
        return True
    st.error(resultado.erro or "Não foi possível salvar a alteração.")
    return False


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
    df = df[cfg["colunas"]].fillna("")

    st.subheader(cfg["titulo"])
    st.dataframe(df, use_container_width=True, hide_index=True)

    pode_criar = _permitido(recurso, "criar")
    pode_editar = _permitido(recurso, "editar")
    pode_excluir = _permitido(recurso, "excluir")

    if pode_editar and not df.empty:
        st.divider()
        st.markdown("#### Editar")
        indice = st.selectbox("Selecionar registro", df.index, key=f"{chave}_editar_idx")
        novos = {}
        for coluna in cfg["colunas"]:
            novos[coluna] = st.text_input(
                coluna,
                value=str(df.at[indice, coluna]),
                key=f"{chave}_editar_{coluna}",
            )
        if st.button("Salvar alterações", key=f"{chave}_salvar"):
            candidato = df.copy()
            for coluna, valor in novos.items():
                candidato.at[indice, coluna] = valor
            _salvar(candidato, cfg, leitura, "editar")

    if pode_excluir and not df.empty:
        st.divider()
        st.markdown("#### Excluir")
        indice_excluir = st.selectbox("Selecionar para excluir", df.index, key=f"{chave}_excluir_idx")
        confirmar = st.checkbox("Confirmo a exclusão.", key=f"{chave}_excluir_confirmar")
        if st.button("Excluir registro", key=f"{chave}_excluir", disabled=not confirmar):
            candidato = df.drop(indice_excluir).reset_index(drop=True)
            _salvar(candidato, cfg, leitura, "excluir")

    if pode_criar:
        st.divider()
        st.markdown("#### Adicionar novo")
        novo = {}
        for coluna in cfg["colunas"]:
            novo[coluna] = st.text_input(coluna, key=f"{chave}_novo_{coluna}")
        if st.button("Adicionar", key=f"{chave}_adicionar"):
            candidato = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
            _salvar(candidato, cfg, leitura, "criar")


def _render_atestados_somente_leitura():
    df_atestados, df_servicos, _, _ = dados_legado.garantir_estrutura_atestados()
    st.subheader("Atestados")
    busca = st.text_input("Buscar por palavra-chave", key="dados_hub_busca_atestado")
    filtrados = dados_legado.filtrar_atestados_por_busca(df_atestados, df_servicos, busca)
    if filtrados.empty:
        st.info("Nenhum atestado encontrado.")
        return
    colunas = ["cliente", "contrato", "obra", "local", "ano", "data_inicio", "data_fim"]
    st.dataframe(filtrados[colunas], use_container_width=True, hide_index=True)
    opcoes = {
        f"{row['cliente']} | {row['obra']} | {row['contrato']}": row["id_atestado"]
        for _, row in filtrados.iterrows()
    }
    escolha = st.selectbox("Selecionar atestado", list(opcoes), key="dados_hub_sel_atestado")
    atestado_id = opcoes[escolha]
    linha = df_atestados[df_atestados["id_atestado"] == atestado_id].iloc[0]
    for rotulo, coluna in [
        ("Cliente", "cliente"), ("Contrato", "contrato"), ("Obra", "obra"),
        ("Local", "local"), ("Ano", "ano"), ("Data início", "data_inicio"),
        ("Data fim", "data_fim"), ("Descrição", "descricao"), ("Observações", "observacoes"),
    ]:
        st.write(f"**{rotulo}:**", linha[coluna])
    servicos = df_servicos[df_servicos["id_atestado"] == atestado_id]
    st.markdown("#### Serviços vinculados")
    if servicos.empty:
        st.info("Nenhum serviço vinculado.")
    else:
        st.dataframe(servicos[["servico", "unidade", "quantidade", "observacoes"]], use_container_width=True, hide_index=True)


def _render_recurso(chave):
    cfg = RECURSOS[chave]
    recurso = cfg["recurso"]
    if not _permitido(recurso, "visualizar"):
        st.session_state.pop("dados_recurso", None)
        st.error("Você não possui permissão para visualizar este recurso.")
        return

    if chave == "atestados":
        if any(_permitido("atestado", acao) for acao in ("criar", "editar", "excluir")):
            dados_legado.render_atestados()
        else:
            _render_atestados_somente_leitura()
    elif chave == "locais":
        render_locais_trabalho()
    else:
        _render_crud(cfg, chave)

    st.divider()
    if st.button("← Voltar para Dados", key="dados_hub_voltar_recursos"):
        st.session_state.pop("dados_recurso", None)
        st.rerun()


def render():
    st.title("Dados")
    visiveis = _recursos_visiveis()
    recurso_atual = st.session_state.get("dados_recurso")

    if recurso_atual in visiveis:
        _render_recurso(recurso_atual)
        return

    st.session_state.pop("dados_recurso", None)
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

    st.divider()
    if st.button("← Voltar ao menu", key="dados_hub_voltar_menu", use_container_width=True):
        st.session_state.tela = "menu"
        st.rerun()
