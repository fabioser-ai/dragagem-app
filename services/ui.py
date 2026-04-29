import streamlit as st


def aplicar_estilo_global():
    st.markdown(
        """
        <style>
            [data-testid="stAppViewContainer"] {
                background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 45%, #cbd5e1 100%);
            }

            [data-testid="stHeader"] {
                background: transparent;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
