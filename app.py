import streamlit as st
import streamlit.components.v1 as components

from services.auth import processar_log_pendente, verificar_login
from services.loading_fos import _LOGO_FOS, processar_carregamento_pendente
from services.ui import aplicar_estilo_global


st.set_page_config(layout="wide")


def _instalar_overlay_loading_menu():
    """Instala um loading reentrante no navegador para cada clique de módulo."""
    components.html(
        f"""
        <script>
        (() => {{
          const p = window.parent;
          const d = p.document;
          const labels = {{
            "ABRIR ORÇAMENTO": "Orçamento",
            "ABRIR NOVO SISTEMA": "Novo Sistema de Orçamentos",
            "ABRIR FÉRIAS E FOLGAS": "Férias e Folgas",
            "ABRIR PRESTAÇÃO DE CONTAS": "Prestação de Contas",
            "ABRIR CRM": "CRM",
            "ABRIR UNIFORMES E EPIs": "Uniformes e EPIs",
            "ABRIR OBRAS": "Obras",
            "ABRIR DADOS": "Dados",
            "ABRIR MEDIÇÕES": "Medições",
            "ABRIR ADMINISTRAÇÃO": "Administração"
          }};

          const limparOverlayAtual = () => {{
            const overlay = d.getElementById("fos-loading-overlay");
            if (overlay) overlay.remove();
            if (p.__fosLoadingFailsafe) {{
              p.clearTimeout(p.__fosLoadingFailsafe);
              p.__fosLoadingFailsafe = null;
            }}
          }};

          if (p.__fosLoadingClickHandler) {{
            d.removeEventListener("click", p.__fosLoadingClickHandler, true);
          }}

          const clickHandler = (event) => {{
            const button = event.target && event.target.closest
              ? event.target.closest('[data-testid="stButton"] button')
              : null;
            if (!button) return;

            const text = (button.innerText || button.textContent || "")
              .trim().replace(/\s+/g, " ");
            const rotulo = labels[text];
            if (!rotulo) return;

            limparOverlayAtual();

            const transitionId = `${{Date.now()}}-${{Math.random().toString(36).slice(2)}}`;
            const overlay = d.createElement("div");
            overlay.id = "fos-loading-overlay";
            overlay.dataset.transitionId = transitionId;
            overlay.dataset.startedAt = String(Date.now());
            overlay.innerHTML = `
              <div class="fos-loading-client-card">
                <img src="{_LOGO_FOS}" alt="FOS Engenharia" />
                <div class="fos-loading-client-title">Carregando ${{rotulo}}...</div>
                <div class="fos-loading-client-subtitle">Aguarde enquanto preparamos as informações para você.</div>
                <div class="fos-loading-client-dots">
                  <span></span><span></span><span></span><span></span><span></span>
                </div>
              </div>`;

            const style = d.createElement("style");
            style.id = "fos-loading-overlay-style";
            style.textContent = `
              #fos-loading-overlay {{
                position: fixed; inset: 0; z-index: 2147483647;
                display: flex; align-items: center; justify-content: center;
                background: rgba(255,255,255,.985);
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
              }}
              #fos-loading-overlay .fos-loading-client-card {{
                display:flex; flex-direction:column; align-items:center; justify-content:center;
                text-align:center; padding: 2rem; min-width: 320px;
              }}
              #fos-loading-overlay img {{ width: 190px; max-width: 42vw; margin-bottom: 1.8rem; }}
              #fos-loading-overlay .fos-loading-client-title {{
                color:#263445; font-size:2rem; line-height:1.2; font-weight:750; margin-bottom:.7rem;
              }}
              #fos-loading-overlay .fos-loading-client-subtitle {{
                color:#718096; font-size:1rem; margin-bottom:1.45rem;
              }}
              #fos-loading-overlay .fos-loading-client-dots {{ display:flex; gap:12px; }}
              #fos-loading-overlay .fos-loading-client-dots span {{
                width:12px; height:12px; border-radius:50%; background:#d7d7d7;
                animation:fosClientPulse 1.15s infinite ease-in-out;
              }}
              #fos-loading-overlay .fos-loading-client-dots span:nth-child(1) {{ background:#a95035; }}
              #fos-loading-overlay .fos-loading-client-dots span:nth-child(2) {{ animation-delay:.14s; }}
              #fos-loading-overlay .fos-loading-client-dots span:nth-child(3) {{ animation-delay:.28s; }}
              #fos-loading-overlay .fos-loading-client-dots span:nth-child(4) {{ animation-delay:.42s; }}
              #fos-loading-overlay .fos-loading-client-dots span:nth-child(5) {{ animation-delay:.56s; }}
              @keyframes fosClientPulse {{
                0%,80%,100% {{ opacity:.32; transform:scale(.82); }}
                40% {{ opacity:1; transform:scale(1.12); }}
              }}
            `;
            const oldStyle = d.getElementById("fos-loading-overlay-style");
            if (oldStyle) oldStyle.remove();
            d.head.appendChild(style);
            d.body.appendChild(overlay);

            // Segurança defensiva: nunca permitir overlay eterno caso o sinal
            // de módulo pronto se perca por qualquer razão do navegador.
            p.__fosLoadingFailsafe = p.setTimeout(() => {{
              const atual = d.getElementById("fos-loading-overlay");
              if (atual && atual.dataset.transitionId === transitionId) atual.remove();
              p.__fosLoadingFailsafe = null;
            }}, 30000);
          }};

          p.__fosLoadingClickHandler = clickHandler;
          d.addEventListener("click", clickHandler, true);
        }})();
        </script>
        """,
        height=0,
        width=0,
    )


def _sinalizar_modulo_pronto_loading():
    """Remove o overlay após o módulo renderizar e após 3 s mínimos."""
    components.html(
        """
        <script>
        (() => {
          const p = window.parent;
          const d = p.document;
          const overlay = d.getElementById("fos-loading-overlay");
          if (!overlay) return;

          const transitionId = overlay.dataset.transitionId;
          const inicio = Number(overlay.dataset.startedAt || Date.now());
          const restante = Math.max(0, 3000 - (Date.now() - inicio));

          const finalizar = () => {
            const atual = d.getElementById("fos-loading-overlay");
            if (!atual || atual.dataset.transitionId !== transitionId) return;
            p.requestAnimationFrame(() => {
              p.requestAnimationFrame(() => {
                const finalOverlay = d.getElementById("fos-loading-overlay");
                if (finalOverlay && finalOverlay.dataset.transitionId === transitionId) {
                  finalOverlay.remove();
                }
                if (p.__fosLoadingFailsafe) {
                  p.clearTimeout(p.__fosLoadingFailsafe);
                  p.__fosLoadingFailsafe = null;
                }
              });
            });
          };

          if (restante > 0) p.setTimeout(finalizar, restante);
          else finalizar();
        })();
        </script>
        """,
        height=0,
        width=0,
    )


if not verificar_login():
    st.stop()


aplicar_estilo_global()

# Uma transição já preparada tem prioridade sobre a renderização do módulo.
if processar_carregamento_pendente():
    st.stop()

from services.autorizacao import iniciar_execucao_autorizacao, pode_acessar_rota

# Cada execução/rerun recebe fontes RBAC novas; todas as decisões feitas abaixo
# compartilham esse único snapshot consistente.
iniciar_execucao_autorizacao()

if "tela" not in st.session_state:
    st.session_state.tela = "menu"


tela = st.session_state.tela

if not pode_acessar_rota(tela):
    st.session_state.tela = "menu"
    st.error("Você não possui permissão para acessar esta área.")
    st.stop()

# Detecta genericamente a saída do menu para qualquer módulo. Assim todos os
# cards atuais e futuros recebem a mesma transição sem duplicar lógica no menu.
_rotulos_loading = {
    "dados": "Dados",
    "administracao": "Administração",
    "ferias": "Férias e Folgas",
    "prestacao_contas": "Prestação de Contas",
    "medicoes": "Medições",
    "carregando_medicoes": "Medições",
    "crm": "CRM",
    "uniformes_epis": "Uniformes e EPIs",
    "novo_orcamento": "Novo Sistema de Orçamentos",
    "obras": "Obras",
    "orcamento": "Orçamento",
    "orcamento_lista": "Orçamento",
}
_tela_anterior = st.session_state.get("_fos_tela_anterior")
if _tela_anterior == "menu" and tela != "menu" and tela in _rotulos_loading:
    destino = "medicoes" if tela == "carregando_medicoes" else tela
    st.session_state["carregamento_fos"] = {
        "destino": destino,
        "rotulo": _rotulos_loading[tela],
    }
    st.session_state["_fos_tela_anterior"] = destino
    st.rerun()

st.session_state["_fos_tela_anterior"] = tela

if tela == "menu":
    from pages import menu

    _instalar_overlay_loading_menu()
    menu.render()

elif tela == "dados":
    from pages import dados_hub

    dados_hub.render()

elif tela == "administracao":
    from pages import administracao

    administracao.render()

elif tela == "ferias":
    from pages import ferias_hub

    ferias_hub.render()

elif tela == "prestacao_contas":
    from pages import prestacao_contas

    prestacao_contas.render()

elif tela == "carregando_medicoes":
    st.session_state["carregamento_fos"] = {"destino": "medicoes", "rotulo": "Medições"}
    st.session_state["_fos_tela_anterior"] = "medicoes"
    st.rerun()

elif tela == "medicoes":
    from pages import medicoes

    medicoes.medicoes()

elif tela == "crm":
    from pages.crm.crm import crm

    crm()

elif tela == "uniformes_epis":
    from pages import uniformes_epis

    uniformes_epis.render()

elif tela == "novo_orcamento":
    from modulos.orcamentos.apresentacao import entrada as novo_orcamento

    novo_orcamento.render(autorizado=True)

elif tela == "obras":
    import pandas as pd

    from services.orcamentos_legado_operacional import carregar_github

    st.title("📊 Obras")
    try:
        df = carregar_github(
            "data/orcamentos.csv",
            st.secrets["GITHUB_TOKEN"],
            st.secrets["REPO"],
        )
    except Exception:
        df = pd.DataFrame()

    if df.empty:
        st.warning("Nenhuma obra cadastrada ainda.")
    else:
        st.subheader("Lista de Obras")
        st.dataframe(df, use_container_width=True)

    if st.button("⬅ Voltar", key="voltar_obras"):
        st.session_state.tela = "menu"
        st.rerun()

elif tela in {"orcamento", "orcamento_lista"}:
    from pages.orcamento.dashboard import dashboard_orcamento

    dashboard_orcamento()

elif tela == "orcamento_etapa0":
    from pages.orcamento.etapa0 import etapa0

    etapa0()

elif tela == "orcamento1":
    from pages.orcamento.etapa1 import etapa1

    etapa1()

elif tela == "orcamento2":
    from pages.orcamento.etapa2 import etapa2

    etapa2()

elif tela == "orcamento3":
    from pages.orcamento.etapa3 import etapa3

    etapa3()

else:
    st.error("Rota indisponível.")
    st.stop()

# Só sinalizamos "pronto" depois que o módulo de destino terminou de renderizar.
# O navegador ainda exige os 3 segundos mínimos antes de remover o overlay.
if tela != "menu":
    _sinalizar_modulo_pronto_loading()

# O menu já foi enviado ao navegador antes da escrita remota do log.
processar_log_pendente()
