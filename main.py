import streamlit as st # type: ignore

st.set_page_config(page_title="Generador de Video LTX", layout="wide")

from app.pages.inicio import inicio
from app.pages.description import descripcion
from app.pages.architecture import arquitectura
from app.pages.generator import generador
from app.pages.acerca_de import acerca_de

def main():
    # Custom CSS to increase tab font size and padding
    st.markdown(
        """
        <style>
        /* Ajustes generales para las pestañas */
        .stTabs [data-baseweb="tab-list"] {
            font-size: 1.5rem;
            height: auto;
            margin-top: 0rem;
            padding-top: 0.5rem;
            justify-content: center;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 1rem 2.5rem;
            font-weight: 700;
            font-size: 1.4rem;
        }

        .stTabs [aria-selected="true"] {
            color: #ff4b4b;
            border-bottom: 3px solid #ff4b4b;
        }

        .block-container {
            padding-top: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    tabs = st.tabs([
        "🏠 Inicio",
        "📝 Descripción",
        "🏗️ Arquitectura",
        "🎬 Generación de Video",
        "ℹ️ Acerca De"
    ])

    with tabs[0]:
        inicio()
    with tabs[1]:
        descripcion()
    with tabs[2]:
        arquitectura()
    with tabs[3]:
        generador()
    with tabs[4]:
        acerca_de()

if __name__ == "__main__":
    main()
