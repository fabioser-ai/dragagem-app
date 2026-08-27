import streamlit as st


_LOGO_FOS = "data:image/jpeg;base64,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"


def iniciar_carregamento(destino, rotulo):
    st.session_state["carregamento_fos"] = {"destino": destino, "rotulo": rotulo}
    st.rerun()


def processar_carregamento_pendente():
    carregamento = st.session_state.get("carregamento_fos")
    if not carregamento:
        return False

    rotulo = str(carregamento.get("rotulo") or "módulo")
    destino = str(carregamento.get("destino") or "menu")
    st.markdown(
        f"""
        <style>
        .fos-loading {{ min-height: 72vh; display:flex; flex-direction:column; align-items:center;
            justify-content:center; text-align:center; background:#fff; }}
        .fos-loading img {{ width:190px; max-width:38vw; margin-bottom:1.8rem; }}
        .fos-loading h2 {{ color:#263445; font-size:2rem; margin:0 0 .65rem; font-weight:750; }}
        .fos-loading p {{ color:#718096; margin:0 0 1.35rem; font-size:1rem; }}
        .fos-dots {{ display:flex; gap:12px; }}
        .fos-dots span {{ width:12px; height:12px; border-radius:50%; background:#d7d7d7;
            animation:fosPulse 1.15s infinite ease-in-out; }}
        .fos-dots span:nth-child(1) {{ background:#a95035; }}
        .fos-dots span:nth-child(2) {{ animation-delay:.14s; }}
        .fos-dots span:nth-child(3) {{ animation-delay:.28s; }}
        .fos-dots span:nth-child(4) {{ animation-delay:.42s; }}
        .fos-dots span:nth-child(5) {{ animation-delay:.56s; }}
        @keyframes fosPulse {{ 0%,80%,100% {{ opacity:.32; transform:scale(.82); }} 40% {{ opacity:1; transform:scale(1.12); }} }}
        </style>
        <div class="fos-loading">
          <img src="{_LOGO_FOS}" alt="FOS Engenharia">
          <h2>Carregando {rotulo}...</h2>
          <p>Aguarde enquanto preparamos as informações para você.</p>
          <div class="fos-dots"><span></span><span></span><span></span><span></span><span></span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.session_state.pop("carregamento_fos", None)
    st.session_state.tela = destino
    st.rerun()
    return True
